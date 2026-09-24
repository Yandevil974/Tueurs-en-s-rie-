"""🔎 Global search (§34) and 🧠 L'ANALYSTE (§41) — answers ONLY from
documented data, and says so when it cannot answer."""
from __future__ import annotations

import re
from typing import Any, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from .. import ethics
from ..db import get_db
from ..models import (Case, Country, Course, Episode, Evidence, Expert, GlossaryEntry, Location, Memorial, Psychology,
                      Question, Source, TimelineEvent, Victim, Victimology)
from ._serialise import case_card

router = APIRouter(tags=["search"])

INSUFFICIENT = ethics.INSUFFICIENT_DATA
STOPWORDS = {"le", "la", "les", "de", "des", "du", "un", "une", "et", "en", "dans", "sur", "pour", "par", "au", "aux",
             "que", "qui", "the", "a", "an", "of", "in", "on", "and", "to", "for", "with", "was", "were", "is", "are"}


def _flatten(value: Any) -> str:
    """Flatten bilingual dicts / lists of items into a searchable string."""
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, dict):
        return " ".join(_flatten(v) for v in value.values())
    if isinstance(value, (list, tuple)):
        return " ".join(_flatten(v) for v in value)
    return str(value)


def _tokens(q: str) -> list[str]:
    words = re.findall(r"[\w'-]{2,}", (q or "").lower())
    return [w for w in words if w not in STOPWORDS] or words


def _score(haystack: str, tokens: list[str]) -> int:
    hay = haystack.lower()
    score = 0
    for t in tokens:
        score += 3 * hay.count(t)
    return score


@router.get("/search")
def search(q: str = Query(min_length=1), limit: int = 20, db: Session = Depends(get_db)):
    tokens = _tokens(q)
    if not tokens:
        return {"query": q, "count": 0, "results": [], "facets": {}}

    countries = {c.code: c for c in db.query(Country).all()}
    results: list[dict[str, Any]] = []

    for c in db.query(Case).all():
        hay = _flatten([c.title, c.subtitle, c.summary, c.region, c.city, c.tags, c.lessons, c.unknowns])
        s = _score(hay, tokens)
        if s:
            results.append({"type": "case", "score": s, "label": c.title,
                            "context": {"fr": c.period_label.get("fr", ""), "en": c.period_label.get("en", "")},
                            "href": f"/cases/{c.slug}", "data": case_card(c, countries.get(c.country_code))})

    for v in db.query(Victim).all():
        hay = _flatten([v.first_name, v.last_name, v.life, v.disappearance, v.note])
        s = _score(hay, tokens)
        if s:
            results.append({"type": "victim", "score": s,
                            "label": {"fr": f"{v.first_name} {v.last_name}".strip(),
                                      "en": f"{v.first_name} {v.last_name}".strip()},
                            "context": v.life.get("fr", {}).get("headline", "") if isinstance(v.life, dict) else "",
                            "href": f"/cases/{v.case.slug}/victimes#{v.id}",
                            "data": {"id": v.id, "case": v.case.slug, "age": v.age, "reliability": v.reliability}})

    for t in db.query(TimelineEvent).all():
        hay = _flatten([t.title, t.body])
        s = _score(hay, tokens)
        if s:
            results.append({"type": "timeline", "score": s, "label": t.title or {"fr": t.date, "en": t.date},
                            "context": {"fr": t.date, "en": t.date}, "href": f"/cases/{t.case.slug}/chronologie",
                            "data": {"id": t.id, "case": t.case.slug, "date": t.date, "reliability": t.reliability}})

    for s_row in db.query(Source).all():
        hay = _flatten([s_row.title, s_row.publisher, s_row.author, s_row.note])
        s = _score(hay, tokens)
        if s:
            results.append({"type": "source", "score": s, "label": s_row.title,
                            "context": {"fr": s_row.publisher, "en": s_row.publisher},
                            "href": f"/cases/{s_row.case.slug}/sources" if s_row.case else "/archives",
                            "data": {"id": s_row.id, "url": s_row.url, "reliability": s_row.reliability,
                                     "verified_at": s_row.verified_at}})

    for g in db.query(GlossaryEntry).all():
        hay = _flatten([g.term, g.simple, g.deep])
        s = _score(hay, tokens)
        if s:
            results.append({"type": "glossary", "score": s, "label": g.term, "context": g.simple,
                            "href": f"/formation/glossaire/{g.slug}", "data": {"slug": g.slug, "field": g.field}})

    for c_row in db.query(Course).all():
        hay = _flatten([c_row.title, c_row.intro, c_row.lessons])
        s = _score(hay, tokens)
        if s:
            results.append({"type": "course", "score": s, "label": c_row.title, "context": c_row.intro,
                            "href": f"/formation/{c_row.slug}", "data": {"slug": c_row.slug, "field": c_row.field}})

    for e in db.query(Episode).all():
        hay = _flatten([e.title, e.description, e.transcript])
        s = _score(hay, tokens)
        if s:
            results.append({"type": "episode", "score": s, "label": e.title, "context": e.description,
                            "href": f"/podcasts/{e.id}", "data": {"id": e.id, "case": e.case.slug,
                                                                   "modes": e.modes, "duration_sec": e.duration_sec}})

    for ev in db.query(Evidence).all():
        hay = _flatten([ev.title, ev.description])
        s = _score(hay, tokens)
        if s:
            results.append({"type": "evidence", "score": s, "label": ev.title, "context": ev.description,
                            "href": f"/cases/{ev.case.slug}/indices",
                            "data": {"id": ev.id, "kind": ev.kind, "reliability": ev.reliability}})

    for x in db.query(Expert).all():
        hay = _flatten([x.label, x.position])
        s = _score(hay, tokens)
        if s:
            results.append({"type": "expert", "score": s, "label": x.label, "context": x.position,
                            "href": f"/psychologie/{x.case.slug}", "data": {"id": x.id, "field": x.field}})

    results.sort(key=lambda r: -r["score"])
    limited = results[:limit]
    facets: dict[str, int] = {}
    for r in results:
        facets[r["type"]] = facets.get(r["type"], 0) + 1
    return {"query": q, "count": len(limited), "total": len(results), "results": limited, "facets": facets}


# ---------------------------------------------------------------------------
# 🧠 L'ANALYSTE (§41)
# ---------------------------------------------------------------------------
@router.post("/analyst")
def analyst(payload: dict[str, Any], db: Session = Depends(get_db)):
    """Retrieval-only assistant. It NEVER invents: every answer is a set of
    documented extracts with their reliability level and source. When nothing
    documented matches, it says so."""
    question = str((payload or {}).get("question", "")).strip()
    case_slug = (payload or {}).get("case")
    tokens = _tokens(question)
    if not tokens:
        return {"question": question, "answer": INSUFFICIENT, "documented": False, "extracts": [],
                "levels": ethics.RELIABILITY}

    countries = {c.code: c for c in db.query(Country).all()}
    pool_cases = db.query(Case).all()
    if case_slug:
        pool_cases = [c for c in pool_cases if c.slug == case_slug]
    case_ids = {c.id: c for c in pool_cases}

    extracts: list[dict[str, Any]] = []

    def push(kind: str, case: Optional[Case], label: dict, body: Any, reliability: str, source: Optional[Source],
             score: int, href: str = ""):
        extracts.append({
            "type": kind, "case": case.slug if case else None,
            "case_title": case.title if case else {},
            "label": label, "body": body, "reliability": reliability,
            "reliability_label": ethics.RELIABILITY.get(reliability, ethics.RELIABILITY["UNKNOWN"]),
            "source": None if source is None else {"id": source.id, "title": source.title, "publisher": source.publisher,
                                                    "url": source.url, "date": source.date,
                                                    "reliability": source.reliability, "verified_at": source.verified_at},
            "score": score, "href": href,
        })

    for c in pool_cases:
        s = _score(_flatten([c.title, c.summary, c.subtitle]), tokens)
        if s:
            push("summary", c, c.title, c.summary, "CONFIRMED", None, s, f"/cases/{c.slug}")

    for v in db.query(Victim).all():
        if v.case_id not in case_ids:
            continue
        s = _score(_flatten([v.first_name, v.last_name, v.life, v.disappearance]), tokens)
        if s:
            src = db.get(Source, v.source_id) if v.source_id else None
            push("victim", v.case, {"fr": f"{v.first_name} {v.last_name}".strip(),
                                    "en": f"{v.first_name} {v.last_name}".strip()},
                 v.life, v.reliability, src, s, f"/cases/{v.case.slug}/victimes#{v.id}")

    for t in db.query(TimelineEvent).all():
        if t.case_id not in case_ids:
            continue
        s = _score(_flatten([t.title, t.body]), tokens)
        if s:
            src = db.get(Source, t.source_id) if t.source_id else None
            push("timeline", t.case, t.title or {"fr": t.date, "en": t.date}, t.body, t.reliability, src, s,
                 f"/cases/{t.case.slug}/chronologie")

    for ev in db.query(Evidence).all():
        if ev.case_id not in case_ids:
            continue
        s = _score(_flatten([ev.title, ev.description]), tokens)
        if s:
            src = db.get(Source, ev.source_id) if ev.source_id else None
            push("evidence", ev.case, ev.title, ev.description, ev.reliability, src, s,
                 f"/cases/{ev.case.slug}/indices")

    for p in db.query(Psychology).all():
        if p.case_id not in case_ids:
            continue
        for b in (p.blocks or []):
            s = _score(_flatten(b), tokens)
            if s:
                push("behaviour", p.case, b.get("title", {}), b.get("body") or b.get("items"),
                     b.get("reliability", "UNKNOWN"), None, s, f"/psychologie/{p.case.slug}")

    for vm in db.query(Victimology).all():
        if vm.case_id not in case_ids:
            continue
        for b in (vm.blocks or []):
            s = _score(_flatten(b), tokens)
            if s:
                push("victimology", vm.case, b.get("title", {}), b.get("body") or b.get("items"),
                     b.get("reliability", "UNKNOWN"), None, s, f"/cases/{vm.case.slug}/victimes")

    for x in db.query(Expert).all():
        if x.case_id not in case_ids:
            continue
        s = _score(_flatten([x.label, x.position]), tokens)
        if s:
            src = db.get(Source, x.source_id) if x.source_id else None
            push("expert", x.case, x.label, x.position, "PROBABLE", src, s, f"/psychologie/{x.case.slug}")

    for g in db.query(GlossaryEntry).all():
        s = _score(_flatten([g.term, g.simple, g.deep]), tokens)
        if s:
            push("glossary", None, g.term, {"fr": g.simple.get("fr", ""), "en": g.simple.get("en", "")},
                 "CONFIRMED", None, s, f"/formation/glossaire/{g.slug}")

    for c_row in db.query(Case).all():
        if c_row.id not in case_ids:
            continue
        court = c_row.court
        if court is not None:
            s = _score(_flatten([court.jurisdiction, court.verdict, court.sentence, court.consequences]), tokens)
            if s:
                push("court", c_row, court.jurisdiction, {"verdict": court.verdict, "sentence": court.sentence},
                     (court.sentence or {}).get("reliability", "CONFIRMED"), None, s, f"/cases/{c_row.slug}/justice")

    extracts.sort(key=lambda e: -e["score"])
    top = extracts[:8]

    if not top:
        return {"question": question, "answer": INSUFFICIENT, "documented": False, "extracts": [],
                "levels": ethics.RELIABILITY,
                "policy": {"fr": "L'analyste ne répond qu'à partir de données documentées et sourcées. Il n'invente "
                                 "jamais et ne complète jamais un trou du dossier.",
                           "en": "The analyst answers only from documented, sourced data. It never invents and never "
                                 "fills a gap in the file."}}

    counts: dict[str, int] = {}
    for e in top:
        counts[e["reliability"]] = counts.get(e["reliability"], 0) + 1
    summary_fr = "Éléments documentés trouvés : " + ", ".join(
        f"{ethics.RELIABILITY.get(k, {}).get('fr', k)} ({v})" for k, v in sorted(counts.items()))
    summary_en = "Documented elements found: " + ", ".join(
        f"{ethics.RELIABILITY.get(k, {}).get('en', k)} ({v})" for k, v in sorted(counts.items()))

    return {
        "question": question,
        "answer": {"fr": summary_fr, "en": summary_en},
        "documented": True,
        "extracts": top,
        "levels": ethics.RELIABILITY,
        "no_speculation": {"fr": "Aucune hypothèse n'est ajoutée : seuls les extraits ci-dessous sont affirmés.",
                           "en": "No hypothesis is added: only the extracts below are asserted."},
        "policy": {"fr": "L'analyste ne répond qu'à partir de données documentées et sourcées.",
                   "en": "The analyst answers only from documented, sourced data."},
    }
