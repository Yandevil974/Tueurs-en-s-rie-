"""🔎 ET SI ? (§51-§57) — hypothetical reconstruction, computed from documented
dates, never a judgement of the justice system."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import ethics
from ..auth import current_user, require_user
from ..db import get_db
from ..models import Case, Counterfactual, UserProgress
from ._serialise import counterfactual_out, sources_map

router = APIRouter(prefix="/counterfactuals", tags=["et-si"])

IMPOSSIBLE = ethics.CALCULATION_IMPOSSIBLE


def _parse(value: str) -> Optional[datetime]:
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(str(value), fmt)
        except ValueError:
            continue
    return None


def _years(a: Optional[datetime], b: Optional[datetime]) -> Optional[int]:
    if not a or not b:
        return None
    return max(0, (b - a).days // 365)


def compute(cf: Counterfactual) -> dict[str, Any]:
    """
    Recompute the counterfactual on demand from its documented parameters.
    If anything needed is missing or unreliable -> CALCULATION_IMPOSSIBLE.
    """
    params = cf.parameters or {}
    events = cf.documented_events or []
    offences = params.get("documented_offences_after") or []
    jurisdiction_note = params.get("jurisdiction_note")

    result: dict[str, Any] = {
        "id": cf.id,
        "case_id": cf.case.slug if cf.case else None,
        "kind": cf.kind,
        "kind_label": ethics.COUNTERFACTUAL_KINDS.get(cf.kind, {"fr": cf.kind, "en": cf.kind}),
        "title": cf.title, "question": cf.question,
        "signature_line": cf.signature_line or ethics.SIGNATURE_LINE,
        "disclaimer": cf.disclaimer or ethics.DISCLAIMER_COUNTERFACTUAL,
        "jurisdiction_note": jurisdiction_note or {},
        "documented_events": events,
        "documented_offences_after": offences,
        "parameters": params,
        "computed_at": datetime.now(timezone.utc).isoformat(),
    }

    if not cf.computable or not events:
        result.update({"computable": False, "computation": {"status": "impossible", "reason": IMPOSSIBLE},
                       "spared": None})
        return result

    def ev(key: str) -> dict:
        return params.get(key) or {}

    d_ref = _parse(ev("reference_event").get("date", ""))
    d_hyp = _parse(ev("hypothesis").get("date", ""))
    d_sce = _parse(ev("scenario_event").get("date", ""))
    d_out = _parse(ev("outcome_event").get("date", ""))
    d_act = _parse((params.get("actual_release") or params.get("actual_arrest") or {}).get("date", ""))

    gaps = {
        "hypothesis_to_scenario_years": _years(d_hyp, d_sce),
        "reference_to_outcome_years": _years(d_ref, d_out),
        "hypothesis_to_actual_years": _years(d_hyp, d_act),
    }

    # The only count ever displayed is the number of DOCUMENTED offences listed
    # by the editor with a date and a source. Never an estimate (§54).
    dated = [o for o in offences if isinstance(o, dict) and _parse(o.get("date", ""))]
    countable = len(dated) == len(offences) and len(offences) > 0

    computation: dict[str, Any] = {"status": "computed", "gaps": gaps,
                                   "reference_event": ev("reference_event"),
                                   "hypothesis": ev("hypothesis"),
                                   "scenario_event": ev("scenario_event"),
                                   "outcome_event": ev("outcome_event")}
    if params.get("actual_release") or params.get("actual_arrest"):
        computation["actual"] = params.get("actual_release") or params.get("actual_arrest")
    if params.get("sentence"):
        computation["sentence"] = params["sentence"]

    if countable:
        result["spared"] = {
            "count": len(dated),
            "documented": True,
            "note": {"fr": "Ce nombre correspond uniquement aux faits documentés et datés listés ci-dessous. "
                           "Ce n'est pas une estimation.",
                     "en": "This number corresponds only to the documented, dated offences listed below. "
                           "It is not an estimate."},
        }
        computation["count_basis"] = "documented_offences_after"
    else:
        result["spared"] = {
            "count": None,
            "documented": False,
            "note": {"fr": "Aucun fait ultérieur n'est documenté et daté dans les sources consultées : aucun nombre "
                           "n'est affiché.",
                     "en": "No later offence is documented and dated in the sources consulted: no number is "
                           "displayed."},
        }
        computation["count_basis"] = "none"

    if not any(v is not None for v in gaps.values()) and not countable:
        computation["status"] = "impossible"
        computation["reason"] = IMPOSSIBLE
        result["computable"] = False
    else:
        result["computable"] = True

    result["computation"] = computation
    result["reflection_hints"] = cf.reflection_hints or []
    return result


@router.get("")
def list_counterfactuals(case: Optional[str] = None, kind: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Counterfactual)
    if case:
        c = db.query(Case).filter_by(slug=case).first()
        if c is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Dossier introuvable / Case not found")
        query = query.filter(Counterfactual.case_id == c.id)
    rows = query.all()
    if kind:
        rows = [r for r in rows if r.kind == kind]
    smap: dict[int, dict] = {}
    for r in rows:
        smap.update(sources_map(db, r.case_id))
    return {
        "count": len(rows),
        "items": [counterfactual_out(r, smap) for r in rows],
        "kinds": [{"key": k, "label": v} for k, v in ethics.COUNTERFACTUAL_KINDS.items()],
        "signature_line": ethics.SIGNATURE_LINE,
        "disclaimer": ethics.DISCLAIMER_COUNTERFACTUAL,
    }


@router.get("/{cf_id}")
def get_counterfactual(cf_id: int, db: Session = Depends(get_db)):
    cf = db.get(Counterfactual, cf_id)
    if cf is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Réflexion introuvable / Counterfactual not found")
    smap = sources_map(db, cf.case_id)
    payload = compute(cf)
    payload["source"] = smap.get(cf.source_id) if cf.source_id else None
    return payload


@router.post("/{cf_id}/reflect")
def save_reflection(cf_id: int, payload: dict, user=Depends(require_user), db: Session = Depends(get_db)):
    """§57 « À vous de réfléchir »: a private, saved reflection. No score."""
    cf = db.get(Counterfactual, cf_id)
    if cf is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Réflexion introuvable / Counterfactual not found")
    text = str((payload or {}).get("text", "")).strip()[:4000]
    if not text:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY,
                            "Réflexion vide / Empty reflection")
    ref = f"{cf.case.slug}:{cf.id}"
    row = db.query(UserProgress).filter_by(user_id=user.id, kind="reflection", ref=ref).first()
    if row is None:
        row = UserProgress(user_id=user.id, kind="reflection", ref=ref, value={"text": text})
        db.add(row)
    else:
        row.value = {"text": text}
    db.commit()
    return {"saved": True, "case_id": cf.case.slug, "counterfactual_id": cf.id, "text": text,
            "private": {"fr": "Votre réflexion reste privée. Elle n'est ni publiée ni partagée.",
                        "en": "Your reflection stays private. It is neither published nor shared."}}
