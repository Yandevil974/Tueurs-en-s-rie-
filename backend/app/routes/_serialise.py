"""Shared serialisation helpers: DB rows -> JSON the frontend consumes.

Every payload keeps its reliability level and a resolved `source` object, so the
UI can always show 🟢/🟡/🟠/⚪ and open the reference (§23, §43).
"""
from __future__ import annotations

from typing import Any

from ..models import Case, Source
from .. import ethics


def bi(value: Any, lang: str | None = None) -> Any:
    """Return a bilingual dict (or the requested language string)."""
    if isinstance(value, dict):
        out = {"fr": value.get("fr", ""), "en": value.get("en", value.get("fr", ""))}
    elif value is None:
        out = {"fr": "", "en": ""}
    else:
        out = {"fr": str(value), "en": str(value)}
    return out[lang] if lang in ("fr", "en") else out


def sources_map(db, case_id: int | None) -> dict[int, dict]:
    q = db.query(Source)
    if case_id is not None:
        q = q.filter(Source.case_id == case_id)
    return {s.id: source_out(s) for s in q.all()}


def source_out(s: Source) -> dict:
    rel = ethics.RELIABILITY.get(s.reliability, ethics.RELIABILITY["UNKNOWN"])
    return {
        "id": s.id, "scope": s.scope, "title": s.title, "author": s.author, "publisher": s.publisher,
        "type": s.type, "url": s.url, "date": s.date, "reliability": s.reliability,
        "reliability_label": {"fr": rel["fr"], "en": rel["en"]}, "verified_at": s.verified_at,
        "note": s.note or {}, "case_id": s.case_id,
    }


def attach_source(payload: dict, smap: dict[int, dict], source_id: int | None) -> dict:
    payload["source"] = smap.get(source_id) if source_id else None
    return payload


def case_card(c: Case, country=None) -> dict:
    """Compact card used by lists, search results, map pins, recommendations."""
    rel_status = ethics.STATUS.get(c.status, {"fr": c.status, "en": c.status})
    ctype = ethics.CASE_TYPE.get(c.type, {"fr": c.type, "en": c.type})
    return {
        "id": c.slug, "slug": c.slug, "title": c.title, "subtitle": c.subtitle,
        "country": c.country_code,
        "country_name": (country.names if country else {}),
        "region": c.region, "city": c.city,
        "year_start": c.year_start, "year_end": c.year_end, "period_label": c.period_label,
        "status": c.status, "status_label": rel_status, "type": c.type, "type_label": ctype,
        "tags": c.tags or [], "tier": c.tier, "sensitive": c.sensitive, "cover": c.cover,
        "lat": c.lat, "lon": c.lon, "summary": c.summary, "stats": c.stats or {},
        "published_at": c.published_at, "editorial": c.editorial,
        "victims_count": len(c.victims),
        "episodes_count": len(c.episodes),
    }


def victim_out(v, smap: dict[int, dict]) -> dict:
    memorials = [
        {"id": m.id, "title": m.title, "biography": m.biography, "testimony": m.testimony,
         "memory": m.memory, "tier": m.tier, "portrait": m.portrait, "audio_clip": m.audio_clip}
        for m in v.case.memorials if m.victim_id == v.id
    ]
    name = " ".join(x for x in (v.first_name, v.last_name) if x)
    return attach_source({
        "id": v.id, "order": v.order_index, "first_name": v.first_name, "last_name": v.last_name,
        "name": name, "age": v.age, "anonymised": v.anonymised, "life": v.life or {},
        "disappearance": v.disappearance or {}, "reliability": v.reliability, "note": v.note or {},
        "memorials": memorials,
        "question": {"fr": "QUI ÉTAIT CETTE PERSONNE AVANT DE DEVENIR UNE VICTIME ?",
                     "en": "WHO WAS THIS PERSON BEFORE BECOMING A VICTIM?"},
    }, smap, v.source_id)


def timeline_out(t, smap) -> dict:
    return attach_source({"id": t.id, "order": t.order_index, "phase": t.phase, "date": t.date,
                          "title": t.title or {}, "body": t.body, "reliability": t.reliability}, smap, t.source_id)


def location_out(l, smap) -> dict:
    return attach_source({"id": l.id, "kind": l.kind, "names": l.names, "region": l.region, "city": l.city,
                          "country": l.country_code, "lat": l.lat, "lon": l.lon, "precision": l.precision,
                          "date": l.date, "note": l.note or {}, "reliability": l.reliability, "case_id": l.case.slug},
                         smap, l.source_id)


def evidence_out(e, smap) -> dict:
    return attach_source({"id": e.id, "kind": e.kind, "title": e.title, "description": e.description,
                          "weight": e.weight, "reliability": e.reliability}, smap, e.source_id)


def expert_out(x, smap) -> dict:
    return attach_source({"id": x.id, "label": x.label, "field": x.field, "position": x.position}, smap, x.source_id)


def episode_out(ep, full: bool = True) -> dict:
    base = {
        "id": ep.id, "case_id": ep.case.slug if ep.case else None, "number": ep.number, "title": ep.title,
        "description": ep.description, "modes": ep.modes or [], "duration_sec": ep.duration_sec,
        "audio": ep.audio, "audio_status": ep.audio_status, "voice_profile": ep.voice_profile,
        "chapters": ep.chapters or [], "published_at": ep.published_at,
    }
    if full:
        base["transcript"] = ep.transcript or {}
    else:
        segs = (ep.transcript or {}).get("segments") or []
        base["segments_count"] = len(segs)
    return base


def question_out(q, smap, with_answer: bool = False) -> dict:
    payload = {
        "id": q.id, "case_id": q.case.slug if q.case else None, "episode_id": q.episode_id, "at_sec": q.at_sec,
        "kind": q.kind, "kind_label": ethics.QUESTION_KINDS.get(q.kind, {"fr": q.kind, "en": q.kind}),
        "prompt": q.prompt,
        "choices": [{"id": c.get("id"), "label": c.get("label")} for c in (q.choices or [])],
    }
    payload = attach_source(payload, smap, q.source_id)
    if with_answer:
        payload["explanation"] = q.explanation or {}
    return payload


def counterfactual_out(cf, smap) -> dict:
    return attach_source({
        "id": cf.id, "case_id": cf.case.slug if cf.case else None, "kind": cf.kind,
        "kind_label": ethics.COUNTERFACTUAL_KINDS.get(cf.kind, {"fr": cf.kind, "en": cf.kind}),
        "title": cf.title, "question": cf.question, "signature_line": cf.signature_line,
        "disclaimer": cf.disclaimer, "computable": cf.computable, "parameters": cf.parameters,
        "documented_events": cf.documented_events, "established": cf.established,
        "reflection_hints": cf.reflection_hints,
    }, smap, cf.source_id)


def item_out(i: dict) -> dict:
    """An authored item() dict (lessons, errors, unknowns, cold-case bullets)."""
    return {"label": i.get("label") or {}, "text": i.get("text") or i, "reliability": i.get("reliability", "CONFIRMED"),
            "source": i.get("source")}
