"""Case dossiers: lists, filters, the 20-section dossier, victims, timeline,
investigation, psychology, victimology, court, sources, memorial (§9-§33)."""
from __future__ import annotations

from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from .. import ethics
from ..db import get_db
from ..models import (Case, Country, Court, Episode, Evidence, Expert, Investigation, Location, Memorial, Psychology,
                      Question, Source, TimelineEvent, Victim, Victimology)
from ._serialise import (attach_source, case_card, counterfactual_out, episode_out, evidence_out, expert_out,
                         item_out, location_out, question_out, sources_map, timeline_out, victim_out)

router = APIRouter(prefix="/cases", tags=["cases"])


def _get_case(db: Session, slug: str) -> Case:
    c = db.query(Case).filter_by(slug=slug).first()
    if c is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Dossier introuvable / Case not found: {slug}")
    return c


@router.get("")
def list_cases(
    country: Optional[str] = None,
    status_: Optional[str] = Query(default=None, alias="status"),
    type_: Optional[str] = Query(default=None, alias="type"),
    tag: Optional[str] = None,
    decade: Optional[int] = None,
    q: Optional[str] = None,
    sort: str = "editorial",
    limit: int = 60,
    db: Session = Depends(get_db),
):
    query = db.query(Case)
    if country:
        query = query.filter(Case.country_code == country.upper())
    if status_:
        query = query.filter(Case.status == status_.upper())
    if type_:
        query = query.filter(Case.type == type_)
    rows = query.all()
    if tag:
        rows = [r for r in rows if tag in (r.tags or [])]
    if decade:
        rows = [r for r in rows if r.year_start and abs((r.year_start // 10) * 10 - decade) <= 9]
    if q:
        needle = q.lower()
        def hit(c: Case) -> bool:
            hay = " ".join([
                (c.title or {}).get("fr", ""), (c.title or {}).get("en", ""),
                (c.subtitle or {}).get("fr", ""), (c.subtitle or {}).get("en", ""),
                (c.summary or {}).get("fr", ""), (c.summary or {}).get("en", ""),
                c.region or "", c.city or "", " ".join(c.tags or []),
            ]).lower()
            return needle in hay
        rows = [r for r in rows if hit(r)]

    if sort == "recent":
        rows.sort(key=lambda c: (c.year_start or 0), reverse=True)
    elif sort == "oldest":
        rows.sort(key=lambda c: (c.year_start or 9999))
    elif sort == "title":
        rows.sort(key=lambda c: (c.title or {}).get("fr", "").lower())

    countries = {c.code: c for c in db.query(Country).all()}
    return {
        "count": len(rows[:limit]),
        "cases": [case_card(c, countries.get(c.country_code)) for c in rows[:limit]],
        "filters": {
            "statuses": [{"key": k, "label": v} for k, v in ethics.STATUS.items()],
            "types": [{"key": k, "label": v} for k, v in ethics.CASE_TYPE.items()],
            "tags": sorted({t for c in db.query(Case).all() for t in (c.tags or [])}),
        },
    }


@router.get("/{slug}")
def get_case(slug: str, lang: Optional[str] = None, db: Session = Depends(get_db)):
    """Return the complete dossier."""
    c = _get_case(db, slug)
    country = db.get(Country, c.country_code)
    sections = [
        {key: value for key, value in section.items() if key not in {"tier", "locked", "upgrade"}}
        for section in (c.sections or [])
        if isinstance(section, dict)
    ]
    inv = db.query(Investigation).filter_by(case_id=c.id).first()
    return {
        "case": case_card(c, country),
        "status_note": (c.stats or {}).get("status_note", {}),
        "triggers": c.triggers,
        "sections": sections,
        "stats": c.stats or {},
        "episodes": [episode_out(e, full=False) for e in c.episodes],
        "victims_count": len(c.victims),
        "investigation_steps_count": len(inv.steps or []) if inv else 0,
    }


@router.get("/{slug}/sections/{key}")
def get_section(slug: str, key: str, db: Session = Depends(get_db)):
    c = _get_case(db, slug)
    section = next((s for s in (c.sections or []) if s.get("key") == key), None)
    if section is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Section introuvable / Section not found: {key}")
    return {"key": key, "title": section.get("title"), "blocks": section.get("blocks", [])}


@router.get("/{slug}/victims")
def get_victims(slug: str, db: Session = Depends(get_db)):
    """§11-§12: victim files are central to every dossier."""
    c = _get_case(db, slug)
    smap = sources_map(db, c.id)
    rows = db.query(Victim).filter_by(case_id=c.id).order_by(Victim.order_index).all()
    memorials = db.query(Memorial).filter_by(case_id=c.id).all()
    case_memorial = [m for m in memorials if m.victim_id is None or m.victim_id not in {r.id for r in rows}]
    return {
        "case_id": c.slug,
        "count": len(rows),
        "victims": [victim_out(v, smap) for v in rows],
        "case_memorial": [{"id": m.id, "title": m.title, "biography": m.biography, "testimony": m.testimony,
                           "memory": m.memory} for m in case_memorial],
        "ethics_note": ethics.DISCLAIMER_VICTIMOLOGY,
        "extra": {k: (c.stats or {}).get(k) for k in ("survivors", "other_victim", "other_victims", "other_proceedings")
                  if (c.stats or {}).get(k) is not None},
    }


@router.get("/{slug}/memorial")
def get_memorial(slug: str, db: Session = Depends(get_db)):
    c = _get_case(db, slug)
    rows = db.query(Memorial).filter_by(case_id=c.id).all()
    return {
        "case_id": c.slug, "title": c.title,
        "memorials": [{"id": m.id, "victim_id": m.victim_id, "title": m.title, "biography": m.biography,
                       "testimony": m.testimony, "memory": m.memory, "portrait": m.portrait,
                       "audio_clip": m.audio_clip} for m in rows],
        "editorial_note": {"fr": "La mémoire des victimes reste au cœur de ce dossier.",
                            "en": "Victims' memory remains at the heart of this dossier."},
    }


@router.get("/{slug}/timeline")
def get_timeline(slug: str, db: Session = Depends(get_db)):
    c = _get_case(db, slug)
    smap = sources_map(db, c.id)
    rows = db.query(TimelineEvent).filter_by(case_id=c.id).order_by(TimelineEvent.order_index).all()
    phases: dict[str, int] = {}
    for r in rows:
        if r.phase:
            phases[r.phase] = phases.get(r.phase, 0) + 1
    return {"case_id": c.slug, "count": len(rows), "phases": phases,
            "events": [timeline_out(r, smap) for r in rows]}


@router.get("/{slug}/geography")
def get_geography(slug: str, db: Session = Depends(get_db)):
    c = _get_case(db, slug)
    smap = sources_map(db, c.id)
    rows = db.query(Location).filter_by(case_id=c.id).all()
    return {"case_id": c.slug, "count": len(rows),
            "no_exact_address": {"fr": "Aucune adresse privée exacte n'est publiée.",
                                 "en": "No exact private address is published."},
            "locations": [location_out(r, smap) for r in rows]}


@router.get("/{slug}/evidence")
def get_evidence(slug: str, db: Session = Depends(get_db)):
    c = _get_case(db, slug)
    smap = sources_map(db, c.id)
    rows = db.query(Evidence).filter_by(case_id=c.id).all()
    return {"case_id": c.slug, "count": len(rows),
            "evidence": [evidence_out(r, smap) for r in rows]}


@router.get("/{slug}/investigation")
def get_investigation(slug: str, db: Session = Depends(get_db)):
    """§25: information is revealed in the order it became available."""
    c = _get_case(db, slug)
    inv = db.query(Investigation).filter_by(case_id=c.id).first()
    if inv is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Aucune enquête documentée / No documented investigation")
    steps = [
        {key: value for key, value in step.items() if key not in {"premium", "tier", "locked", "upgrade"}}
        for step in (inv.steps or [])
        if isinstance(step, dict)
    ]
    return {
        "case_id": c.slug, "steps": steps, "reality": inv.reality,
        "errors": [item_out(e) for e in (inv.errors or [])],
        "cold_case": inv.cold_case or {},
    }


@router.get("/{slug}/psychology")
def get_psychology(slug: str, db: Session = Depends(get_db)):
    c = _get_case(db, slug)
    row = db.query(Psychology).filter_by(case_id=c.id).first()
    if row is None:
        return {"case_id": c.slug, "blocks": [], "disclaimer": ethics.DISCLAIMER_PSYCHOLOGY}
    return {"case_id": c.slug, "blocks": row.blocks or [], "disclaimer": row.disclaimer or ethics.DISCLAIMER_PSYCHOLOGY,
            "no_diagnosis": ethics.DISCLAIMER_PSYCHOLOGY,
            "levels": [{"key": k, "label": {"fr": v["fr"], "en": v["en"]}, "color": v["color"], "dot": v["dot"]}
                       for k, v in ethics.RELIABILITY.items()]}


@router.get("/{slug}/victimology")
def get_victimology(slug: str, db: Session = Depends(get_db)):
    """§13: victimology puts victims first and never justifies the crime."""
    c = _get_case(db, slug)
    row = db.query(Victimology).filter_by(case_id=c.id).first()
    if row is None:
        return {"case_id": c.slug, "blocks": [], "ethics_note": ethics.DISCLAIMER_VICTIMOLOGY}
    return {"case_id": c.slug, "blocks": row.blocks or [], "ethics_note": row.ethics_note or ethics.DISCLAIMER_VICTIMOLOGY}


@router.get("/{slug}/court")
def get_court(slug: str, db: Session = Depends(get_db)):
    c = _get_case(db, slug)
    row = db.query(Court).filter_by(case_id=c.id).first()
    if row is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Aucune décision documentée / No documented decision")
    return {"case_id": c.slug, "jurisdiction": row.jurisdiction, "verdict": row.verdict, "sentence": row.sentence,
            "appeals": row.appeals or [], "consequences": [item_out(x) for x in (row.consequences or [])]}


@router.get("/{slug}/experts")
def get_experts(slug: str, db: Session = Depends(get_db)):
    c = _get_case(db, slug)
    smap = sources_map(db, c.id)
    rows = db.query(Expert).filter_by(case_id=c.id).all()
    stats = c.stats or {}
    return {"case_id": c.slug,
            "experts": [expert_out(r, smap) for r in rows],
            "agreement": stats.get("experts_agreement", {}),
            "disagreement": stats.get("experts_disagreement", {}),
            "uncertain": stats.get("experts_uncertain", {})}


@router.get("/{slug}/sources")
def get_sources(slug: str, db: Session = Depends(get_db)):
    c = _get_case(db, slug)
    rows = db.query(Source).filter_by(case_id=c.id).all()
    return {"case_id": c.slug, "count": len(rows),
            "levels": [{"key": k, "label": {"fr": v["fr"], "en": v["en"]}, "color": v["color"], "dot": v["dot"],
                        "definition": v["definition"]} for k, v in ethics.RELIABILITY.items()],
            "sources": [{
                "id": s.id, "title": s.title, "author": s.author, "publisher": s.publisher, "type": s.type,
                "url": s.url, "date": s.date, "reliability": s.reliability, "verified_at": s.verified_at,
                "note": s.note or {},
            } for s in rows],
            "policy": {"fr": "Aucune source n'est inventée. Aucune rumeur n'est présentée comme un fait.",
                       "en": "No source is invented. No rumour is presented as a fact."}}


@router.get("/{slug}/lessons")
def get_lessons(slug: str, db: Session = Depends(get_db)):
    c = _get_case(db, slug)
    return {"case_id": c.slug,
            "lessons": [item_out(x) for x in (c.lessons or [])],
            "errors": [item_out(x) for x in (c.errors or [])],
            "unknowns": [item_out(x) for x in (c.unknowns or [])]}


@router.get("/{slug}/questions")
def get_questions(slug: str, episode: Optional[int] = None, db: Session = Depends(get_db)):
    c = _get_case(db, slug)
    smap = sources_map(db, c.id)
    q = db.query(Question).filter_by(case_id=c.id)
    if episode is not None:
        ep = db.query(Episode).filter_by(case_id=c.id, number=episode).first()
        if ep is not None:
            q = q.filter(Question.episode_id == ep.id)
    return {"case_id": c.slug, "questions": [question_out(r, smap) for r in q.all()]}


@router.get("/{slug}/recommendations")
def recommendations(slug: str, db: Session = Depends(get_db)):
    """§35: recommend by period, context, geography, investigation, victimology.
    NEVER by violence."""
    c = _get_case(db, slug)
    countries = {x.code: x for x in db.query(Country).all()}
    scored: list[tuple[int, str, Case]] = []
    for other in db.query(Case).all():
        if other.id == c.id:
            continue
        score, reasons = 0, []
        if other.country_code == c.country_code:
            score += 2
            reasons.append("geography")
        if other.type == c.type:
            score += 2
            reasons.append("context")
        if other.status == c.status:
            score += 1
            reasons.append("investigation")
        if c.year_start and other.year_start and abs(c.year_start - other.year_start) <= 15:
            score += 1
            reasons.append("period")
        shared = set(other.tags or []) & set(c.tags or [])
        if shared:
            score += min(2, len(shared))
            reasons.append("victimology")
        if score:
            scored.append((score, ",".join(sorted(set(reasons))), other))
    scored.sort(key=lambda x: (-x[0], x[2].year_start or 0))
    return {"case_id": c.slug,
            "recommendations": [{"score": s, "reasons": r.split(","), "case": case_card(o, countries.get(o.country_code))}
                                for s, r, o in scored[:5]],
            "criteria": {"fr": ["période", "contexte", "géographie", "enquête", "victimologie"],
                         "en": ["period", "context", "geography", "investigation", "victimology"]},
            "excluded": {"fr": "Aucune recommandation fondée sur la violence.",
                         "en": "No recommendation based on violence."}}
