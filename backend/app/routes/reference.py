"""🎓 Formation (§28), glossaire (§29), références, éthique éditoriale (§44)."""
from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import ethics
from ..db import get_db
from ..models import Case, Country, Course, GlossaryEntry
from ._serialise import case_card

router = APIRouter(tags=["reference"])


@router.get("/meta")
def meta(db: Session = Depends(get_db)):
    """Everything the shell needs in one call: identity, levels, modes, rules."""
    cases = db.query(Case).all()
    return {
        "app": {"name": ethics.APP_NAME, "tagline": ethics.APP_TAGLINE},
        "languages": ["fr", "en"],
        "planned_languages": ["de", "es", "it", "pt"],
        "counts": {
            "cases": len(cases),
            "countries": len({c.country_code for c in cases}),
            "episodes": sum(len(c.episodes) for c in cases),
            "victims": sum(len(c.victims) for c in cases),
            "sources": sum(len(c.sources) for c in cases),
            "glossary": db.query(GlossaryEntry).count(),
            "courses": db.query(Course).count(),
        },
        "reliability": [{"key": k, "label": {"fr": v["fr"], "en": v["en"]}, "color": v["color"], "dot": v["dot"],
                         "definition": v["definition"]} for k, v in ethics.RELIABILITY.items()],
        "statuses": [{"key": k, "label": v} for k, v in ethics.STATUS.items()],
        "case_types": [{"key": k, "label": v} for k, v in ethics.CASE_TYPE.items()],
        "episode_modes": [{"key": k, "label": {"fr": v["fr"], "en": v["en"]}, "description": v["desc"]}
                          for k, v in ethics.EPISODE_MODES.items()],
        "question_kinds": [{"key": k, "label": v} for k, v in ethics.QUESTION_KINDS.items()],
        "counterfactual_kinds": [{"key": k, "label": v} for k, v in ethics.COUNTERFACTUAL_KINDS.items()],
        "badges": ethics.BADGES,
        "signature_line": ethics.SIGNATURE_LINE,
        "disclaimers": {"counterfactual": ethics.DISCLAIMER_COUNTERFACTUAL, "psychology": ethics.DISCLAIMER_PSYCHOLOGY,
                        "victimology": ethics.DISCLAIMER_VICTIMOLOGY, "insufficient_data": ethics.INSUFFICIENT_DATA,
                        "calculation_impossible": ethics.CALCULATION_IMPOSSIBLE},
        "editorial_rules": ethics.NEVER,
        "tier": {
            "free": {"fr": ["dossiers sélectionnés", "podcasts", "chronologies", "recherche", "découverte des victimes",
                            "mémoire"],
                     "en": ["selected dossiers", "podcasts", "chronologies", "search", "victim discovery", "memory"]},
            "premium": {"fr": ["dossiers complets", "analyses approfondies", "archives", "mode expert", "mode enquête",
                               "comparateur", "téléchargement hors ligne", "exclusivités"],
                        "en": ["complete dossiers", "in-depth analyses", "archives", "expert mode", "investigation mode",
                               "comparator", "offline download", "exclusives"]},
            "never_paywalled": ethics.DISCLAIMER_VICTIMOLOGY,
        },
    }


@router.get("/countries")
def countries(db: Session = Depends(get_db)):
    rows = db.query(Country).all()
    out = []
    for c in rows:
        cases = db.query(Case).filter_by(country_code=c.code).all()
        out.append({"code": c.code, "names": c.names, "continent": c.continent, "flag": c.flag,
                    "cases": len(cases)})
    return {"countries": out}


@router.get("/glossary")
def glossary(field: Optional[str] = None, q: Optional[str] = None, db: Session = Depends(get_db)):
    rows = db.query(GlossaryEntry).all()
    if field:
        rows = [r for r in rows if r.field == field]
    if q:
        needle = q.lower()
        rows = [r for r in rows if needle in str(r.term).lower() or needle in str(r.simple).lower()
                or needle in str(r.deep).lower()]
    rows.sort(key=lambda r: (r.term.get("fr") or "").lower())
    return {
        "count": len(rows),
        "fields": sorted({r.field for r in db.query(GlossaryEntry).all()}),
        "entries": [{"slug": r.slug, "term": r.term, "simple": r.simple, "deep": r.deep, "field": r.field,
                     "case_refs": r.case_refs or []} for r in rows],
        "method": {"fr": "Explication simple d'abord, approfondissement ensuite.",
                   "en": "Simple explanation first, deepening afterwards."},
    }


@router.get("/glossary/{slug}")
def glossary_entry(slug: str, db: Session = Depends(get_db)):
    row = db.query(GlossaryEntry).filter_by(slug=slug).first()
    if row is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Terme introuvable / Term not found")
    countries = {c.code: c for c in db.query(Country).all()}
    linked = [case_card(c, countries.get(c.country_code))
              for c in db.query(Case).all() if c.slug in (row.case_refs or [])]
    return {"slug": row.slug, "term": row.term, "simple": row.simple, "deep": row.deep, "field": row.field,
            "cases": linked}


@router.get("/courses")
def courses(db: Session = Depends(get_db)):
    rows = db.query(Course).all()
    countries = {c.code: c for c in db.query(Country).all()}
    by_slug = {c.slug: c for c in db.query(Case).all()}
    return {
        "count": len(rows),
        "courses": [{
            "slug": r.slug, "field": r.field, "title": r.title, "intro": r.intro, "minutes": r.minutes,
            "level": r.level, "lessons": r.lessons or [], "tier": r.tier,
            "cases": [case_card(by_slug[s], countries.get(by_slug[s].country_code))
                      for s in (r.case_refs or []) if s in by_slug],
        } for r in rows],
        "fields": sorted({r.field for r in rows}),
    }


@router.get("/courses/{slug}")
def course(slug: str, db: Session = Depends(get_db)):
    row = db.query(Course).filter_by(slug=slug).first()
    if row is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Formation introuvable / Course not found")
    countries = {c.code: c for c in db.query(Country).all()}
    by_slug = {c.slug: c for c in db.query(Case).all()}
    return {
        "slug": row.slug, "field": row.field, "title": row.title, "intro": row.intro, "minutes": row.minutes,
        "level": row.level, "lessons": row.lessons or [], "tier": row.tier,
        "cases": [case_card(by_slug[s], countries.get(by_slug[s].country_code))
                  for s in (row.case_refs or []) if s in by_slug],
        "glossary": [{"slug": g.slug, "term": g.term, "simple": g.simple}
                     for g in db.query(GlossaryEntry).all() if g.field == row.field],
    }


@router.get("/ethics")
def ethics_page():
    return {"app": {"name": ethics.APP_NAME, "tagline": ethics.APP_TAGLINE}, "rules": ethics.NEVER,
            "disclaimers": {"counterfactual": ethics.DISCLAIMER_COUNTERFACTUAL,
                            "psychology": ethics.DISCLAIMER_PSYCHOLOGY,
                            "victimology": ethics.DISCLAIMER_VICTIMOLOGY},
            "badges": ethics.BADGES,
            "gamification": {"fr": "La progression valorise la compréhension, l'analyse et l'esprit critique. "
                                   "Jamais la violence.",
                             "en": "Progress rewards understanding, analysis and critical thinking. Never violence."}}
