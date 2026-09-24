"""🕯 MÉMOIRE (§12, §46) — the permanent memorial, always free."""
from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import ethics
from ..db import get_db
from ..models import Case, Country, Memorial, Victim
from ._serialise import sources_map, victim_out

router = APIRouter(prefix="/memory", tags=["memory"])


@router.get("")
def global_memorial(country: str | None = None, db: Session = Depends(get_db)):
    """Every documented victim, grouped by dossier. Never "Victim 1"."""
    cases = db.query(Case).all()
    countries = {c.code: c for c in db.query(Country).all()}
    groups = []
    total = 0
    named = 0
    for c in cases:
        if country and c.country_code != country.upper():
            continue
        smap = sources_map(db, c.id)
        rows = db.query(Victim).filter_by(case_id=c.id).order_by(Victim.order_index).all()
        if not rows:
            continue
        total += len(rows)
        named += sum(1 for v in rows if not v.anonymised and v.last_name)
        case_memorials = db.query(Memorial).filter_by(case_id=c.id).all()
        groups.append({
            "case": {
                "slug": c.slug, "title": c.title, "country": c.country_code,
                "country_name": countries.get(c.country_code).names if countries.get(c.country_code) else {},
                "period_label": c.period_label, "status": c.status,
            },
            "memorial": [{
                "id": m.id, "title": m.title, "biography": m.biography, "testimony": m.testimony,
                "memory": m.memory, "tier": m.tier,
            } for m in case_memorials if m.victim_id is None],
            "victims": [victim_out(v, smap) for v in rows],
        })
    return {
        "tier": "FREE",
        "never_paywalled": {"fr": "La mémoire des victimes n'est jamais payante.",
                            "en": "Victim memory is never paywalled."},
        "question": {"fr": "QUI ÉTAIT CETTE PERSONNE AVANT DE DEVENIR UNE VICTIME ?",
                     "en": "WHO WAS THIS PERSON BEFORE BECOMING A VICTIM?"},
        "counts": {"cases": len(groups), "victims": total, "named": named,
                   "not_documented": total - named},
        "note_on_missing": {
            "fr": "Lorsqu'une identité ou un parcours n'est pas documenté par une source vérifiable, l'absence est "
                  "affichée. Rien n'est reconstitué.",
            "en": "When an identity or a life is not documented by a verifiable source, the absence is displayed. "
                  "Nothing is reconstructed.",
        },
        "ethics_note": ethics.DISCLAIMER_VICTIMOLOGY,
        "groups": groups,
    }


@router.get("/countries")
def memorial_countries(db: Session = Depends(get_db)):
    rows = db.query(Country).all()
    out = []
    for c in rows:
        n = db.query(Victim).join(Case, Victim.case_id == Case.id).filter(Case.country_code == c.code).count()
        if n:
            out.append({"code": c.code, "names": c.names, "flag": c.flag, "victims": n})
    return {"countries": out}
