"""⚙️ Administration (§42-§43): reseed, revision history, catalogue health."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import ethics
from ..auth import require_admin
from ..db import get_db
from ..models import Case, Episode, Memorial, Notification, Revision, Source, User, Victim
from ..seed import seed as run_seed

router = APIRouter(prefix="/admin", tags=["admin"])


def _log(db: Session, user, entity: str, action: str, diff: dict[str, Any], reason: str = "") -> None:
    db.add(Revision(user_id=user.id, entity=entity, action=action, diff=diff, reason=reason[:400]))


@router.get("/stats")
def stats(user=Depends(require_admin), db: Session = Depends(get_db)):
    cases = db.query(Case).all()
    unsourced_victims = [
        {"case": v.case.slug, "victim": f"{v.first_name} {v.last_name}".strip()}
        for v in db.query(Victim).all() if v.source_id is None and not v.anonymised
    ]
    paywalled_memorials = [
        {"id": m.id, "case": m.case.slug if m.case else None}
        for m in db.query(Memorial).all() if m.tier != "FREE"
    ]
    return {
        "cases": len(cases),
        "by_status": {s: sum(1 for c in cases if c.status == s) for s in ethics.STATUS},
        "by_tier": {t: sum(1 for c in cases if c.tier == t) for t in ("FREE", "PREMIUM")},
        "episodes": db.query(Episode).count(),
        "sources": db.query(Source).count(),
        "victims": db.query(Victim).count(),
        "memorials": db.query(Memorial).count(),
        "health": {
            "unsourced_victims": unsourced_victims,
            "paywalled_memorials": paywalled_memorials,
            "memorial_tier_ok": len(paywalled_memorials) == 0,
            "episodes_without_transcript": [e.id for e in db.query(Episode).all()
                                            if not (e.transcript or {}).get("segments")],
            "cases_without_signature_line": [
                c.slug for c in cases
                if any(ethics.SIGNATURE_LINE["fr"] not in str((e.transcript or {})) for e in c.episodes)
            ],
        },
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }


@router.post("/notifications")
def broadcast_notification(payload: dict[str, Any], user=Depends(require_admin), db: Session = Depends(get_db)):
    """Publish an explicit, authored message to all accounts."""
    def bilingual(value: Any) -> dict[str, str]:
        if isinstance(value, dict):
            fr = str(value.get("fr", "")).strip()
            en = str(value.get("en", fr)).strip()
            return {"fr": fr, "en": en}
        text = str(value or "").strip()
        return {"fr": text, "en": text}

    title = bilingual((payload or {}).get("title"))
    body = bilingual((payload or {}).get("body"))
    if not title["fr"] or not body["fr"]:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY,
                            "Titre et message requis dans au moins une langue / Title and message required")
    kind = str((payload or {}).get("kind", "editorial"))[:30] or "editorial"
    href = str((payload or {}).get("href", ""))[:240]
    users = db.query(User).all()
    rows = [Notification(user_id=recipient.id, kind=kind, title=title, body=body, href=href)
            for recipient in users]
    db.add_all(rows)
    _log(db, user, "notification", "broadcast", {"kind": kind, "href": href, "recipients": len(rows)},
         str((payload or {}).get("reason", "editorial notification")))
    db.commit()
    return {"published": True, "recipients": len(rows), "kind": kind, "href": href}


@router.get("/revisions")
def revisions(limit: int = 100, user=Depends(require_admin), db: Session = Depends(get_db)):
    rows = db.query(Revision).order_by(Revision.id.desc()).limit(min(limit, 500)).all()
    return {"count": len(rows),
            "revisions": [{"id": r.id, "user_id": r.user_id, "entity": r.entity, "entity_id": r.entity_id,
                           "action": r.action, "diff": r.diff, "reason": r.reason,
                           "created_at": r.created_at.isoformat() if r.created_at else ""} for r in rows]}


@router.post("/reseed")
def reseed(payload: dict[str, Any] | None = None, user=Depends(require_admin), db: Session = Depends(get_db)):
    """Rebuild the content tables from the Python dossiers (the source of truth)."""
    reason = str((payload or {}).get("reason", ""))
    db.close()
    counts = run_seed(force=True)
    db2 = next(get_db())
    try:
        _log(db2, user, "catalogue", "reseed", counts, reason)
        db2.commit()
    finally:
        db2.close()
    return {"reseeded": True, "counts": counts}


@router.patch("/cases/{slug}")
def patch_case(slug: str, payload: dict[str, Any], user=Depends(require_admin), db: Session = Depends(get_db)):
    """Editorial corrections only: title, subtitle, summary, status, tier, tags.
    Structural content lives in the Python dossiers and is reseeded."""
    case = db.query(Case).filter_by(slug=slug).first()
    if case is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Dossier introuvable / Case not found")
    editable = {"title", "subtitle", "summary", "status", "tier", "tags", "sensitive", "cover"}
    diff: dict[str, Any] = {}
    for key, value in (payload or {}).items():
        if key not in editable:
            continue
        if key == "status" and value not in ethics.STATUS:
            raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, f"Statut invalide / Invalid status: {value}")
        if key == "tier":
            if value not in ("FREE", "PREMIUM"):
                raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "Niveau invalide / Invalid tier")
        diff[key] = {"before": getattr(case, key), "after": value}
        setattr(case, key, value)
    if not diff:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "Aucun champ modifiable / No editable field")
    _log(db, user, "case", "update", diff, str((payload or {}).get("reason", "")))
    db.commit()
    return {"updated": slug, "diff": diff}


@router.post("/sources/{source_id}/verify")
def verify_source(source_id: int, user=Depends(require_admin), db: Session = Depends(get_db)):
    row = db.get(Source, source_id)
    if row is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Source introuvable / Source not found")
    before = row.verified_at
    row.verified_at = datetime.now(timezone.utc).date().isoformat()
    _log(db, user, "source", "update", {"verified_at": {"before": before, "after": row.verified_at}},
         "re-verification")
    db.commit()
    return {"id": row.id, "verified_at": row.verified_at}
