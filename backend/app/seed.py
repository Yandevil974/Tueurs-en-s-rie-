"""
Seed the database from the Python case dossiers and the reference tables.

Idempotent: `python -m app.seed` can be run any number of times; content tables
are rebuilt, user tables are preserved.
"""
from __future__ import annotations

import hashlib
import os
import secrets
from datetime import datetime, timezone

from . import ethics, reference
from .cases_data import CASES
from .db import SessionLocal, init_db
from .models import (
    Case,
    Counterfactual,
    Country,
    Course,
    Court,
    Episode,
    Evidence,
    Expert,
    GlossaryEntry,
    Investigation,
    Location,
    MediaItem,
    Memorial,
    Psychology,
    Question,
    Source,
    TimelineEvent,
    User,
    UserProgress,
    Victim,
    Victimology,
)

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def _now() -> datetime:
    return datetime.now(timezone.utc)


def hash_password(password: str, salt: str | None = None) -> str:
    salt = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 120_000).hex()
    return f"pbkdf2_sha256${salt}${digest}"


def verify_password(password: str, stored: str) -> bool:
    try:
        _, salt, digest = stored.split("$")
    except ValueError:
        return False
    candidate = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 120_000).hex()
    return secrets.compare_digest(candidate, digest)


def _bi(value) -> dict:
    """Normalise anything textual to {"fr": ..., "en": ...}."""
    if isinstance(value, dict):
        return {"fr": value.get("fr", ""), "en": value.get("en", value.get("fr", ""))}
    if value is None:
        return {"fr": "", "en": ""}
    return {"fr": str(value), "en": str(value)}


def _list(value) -> list:
    return value if isinstance(value, list) else []


# ---------------------------------------------------------------------------
# counterfactual engine (computed once at seed time, recomputed on demand)
# ---------------------------------------------------------------------------
def _parse_date(value: str):
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(str(value), fmt).date()
        except ValueError:
            continue
    return None


def build_counterfactual(cf: dict, case_slug: str) -> dict:
    """
    §54: the answer is COMPUTED from documented dates, never asserted.
    Returns the serialisable payload stored on the Counterfactual row.
    """
    params = cf.get("parameters") or {}
    events = cf.get("documented_events") or []
    offences = _list(params.get("documented_offences_after"))
    computable = bool(cf.get("computable", True)) and bool(events)

    payload: dict = {
        "kind": cf.get("kind", "technology"),
        "title": _bi(cf.get("title")),
        "question": _bi(cf.get("question")),
        "signature_line": ethics.SIGNATURE_LINE,
        "disclaimer": ethics.DISCLAIMER_COUNTERFACTUAL,
        "computable": computable,
        "source": cf.get("source"),
        "parameters": params,
        "documented_events": events,
        "established": {},
        "reflection_hints": [
            {"fr": "Qu'est-ce qui, dans le dossier, aurait pu être disponible plus tôt ?",
             "en": "What in the file could have been available sooner?"},
            {"fr": "Quel élément a manqué : une technique, une décision, une parole, un délai ?",
             "en": "Which element was missing: a technique, a decision, a statement, a delay?"},
            {"fr": "Que change ce scénario pour les victimes — et que ne change-t-il pas ?",
             "en": "What does this scenario change for the victims — and what does it not change?"},
            {"fr": "Ce scénario juge-t-il une institution, ou décrit-il un enchaînement de faits ?",
             "en": "Does this scenario judge an institution, or describe a chain of facts?"},
        ],
    }

    if not computable:
        payload["established"] = {
            "computable": False,
            "reason": ethics.CALCULATION_IMPOSSIBLE,
        }
        return payload

    def _ev(key):
        return params.get(key) or {}

    reference = _ev("reference_event")
    hypothesis = _ev("hypothesis")
    scenario = _ev("scenario_event")
    outcome = _ev("outcome_event")
    actual = _ev("actual_release") or _ev("actual_arrest") or {}

    d_ref = _parse_date(reference.get("date", ""))
    d_hyp = _parse_date(hypothesis.get("date", ""))
    d_sce = _parse_date(scenario.get("date", ""))
    d_out = _parse_date(outcome.get("date", ""))
    d_act = _parse_date(actual.get("date", ""))

    def _years(a, b) -> int | None:
        if not a or not b:
            return None
        return max(0, (b - a).days // 365)

    established = {
        "computable": True,
        "unit": params.get("unit", "years"),
        "reference": reference,
        "hypothesis": hypothesis,
        "scenario": scenario,
        "outcome": outcome,
        "gap_hypothesis_to_scenario_years": _years(d_hyp, d_sce),
        "gap_reference_to_outcome_years": _years(d_ref, d_out),
        "documented_offences_after": offences,
        "spared_count": len(offences),
        "spared_is_documented_only": True,
    }
    if actual:
        established["actual"] = actual
        established["gap_hypothesis_to_actual_years"] = _years(d_hyp, d_act)

    sentence = params.get("sentence") or {}
    if sentence:
        established["sentence"] = sentence
    jurisdiction = params.get("jurisdiction_note")
    if jurisdiction:
        established["jurisdiction_note"] = _bi(jurisdiction)

    # The count is only ever the number of DOCUMENTED offences listed by the
    # editor, each with its date and source. Never an estimate.
    if not offences:
        established["count_note"] = {
            "fr": "Aucun fait ultérieur n'est documenté dans les sources consultées : aucun nombre n'est affiché.",
            "en": "No later offence is documented in the sources consulted: no number is displayed.",
        }
    else:
        established["count_note"] = {
            "fr": "Ce nombre correspond uniquement aux faits documentés et datés listés ci-dessous. Ce n'est pas une "
                  "estimation.",
            "en": "This number corresponds only to the documented, dated offences listed below. It is not an "
                  "estimate.",
        }

    payload["established"] = established
    return payload


# ---------------------------------------------------------------------------
# seeding
# ---------------------------------------------------------------------------
def seed_countries(db) -> None:
    for c in reference.COUNTRIES:
        row = db.get(Country, c["code"])
        if row is None:
            db.add(Country(code=c["code"], names=c["names"], continent=c["continent"], flag=c.get("flag", "")))
        else:
            row.names, row.continent, row.flag = c["names"], c["continent"], c.get("flag", "")


def seed_reference(db) -> None:
    for g in reference.GLOSSARY:
        row = db.query(GlossaryEntry).filter_by(slug=g["slug"]).first()
        if row is None:
            db.add(GlossaryEntry(slug=g["slug"], term=g["term"], simple=g["simple"], deep=g["deep"],
                                 field=g.get("field", "criminology"), case_refs=g.get("case_refs", [])))
        else:
            row.term, row.simple, row.deep = g["term"], g["simple"], g["deep"]
            row.field, row.case_refs = g.get("field", "criminology"), g.get("case_refs", [])

    for c in reference.COURSES:
        row = db.query(Course).filter_by(slug=c["slug"]).first()
        if row is None:
            db.add(Course(slug=c["slug"], field=c.get("field", "criminology"), title=c["title"], intro=c["intro"],
                          minutes=c.get("minutes", 8), level=c.get("level", "beginner"),
                          lessons=c.get("lessons", []), case_refs=c.get("case_refs", []),
                          tier=c.get("tier", "FREE")))
        else:
            row.title, row.intro, row.lessons = c["title"], c["intro"], c.get("lessons", [])
            row.field, row.minutes, row.level = c.get("field", "criminology"), c.get("minutes", 8), c.get("level", "beginner")
            row.case_refs, row.tier = c.get("case_refs", []), c.get("tier", "FREE")


def _purge_content(db) -> None:
    """Content is fully rebuilt from the Python dossiers (the source of truth)."""
    for model in (Counterfactual, Question, Episode, MediaItem, Expert, Court, Victimology, Psychology,
                  Investigation, Evidence, TimelineEvent, Memorial, Victim, Location, Source, Case):
        db.query(model).delete()


def seed_cases(db) -> None:
    for data in CASES:
        slug = data["id"]
        sources: dict[str, Source] = {}
        for s in _list(data.get("sources")):
            row = Source(
                scope="case", title=_bi(s.get("title")), author=s.get("author", ""),
                publisher=s.get("publisher", ""), type=s.get("type", "press"), url=s.get("url", ""),
                date=str(s.get("date", "")), reliability=s.get("reliability", "CONFIRMED"),
                verified_at=s.get("verified_at", ""), note=_bi(s.get("note")) if s.get("note") else {},
            )
            sources[s["key"]] = row

        stats = dict(data.get("stats") or {})
        # Extra editorial keys are preserved so no authored content is dropped.
        for key in ("survivors", "other_victim", "other_victims", "other_proceedings", "timeline_phases",
                    "status_note"):
            if key in data:
                stats[key] = data[key]
        stats["experts_agreement"] = _bi(data.get("experts_agreement"))
        stats["experts_disagreement"] = _bi(data.get("experts_disagreement"))
        stats["experts_uncertain"] = _bi(data.get("experts_uncertain"))
        stats["victims_documented"] = len(_list(data.get("victims")))

        case = Case(
            slug=slug, title=_bi(data["title"]), subtitle=_bi(data.get("subtitle")),
            country_code=data.get("country", ""), region=data.get("region", ""), city=data.get("city", ""),
            year_start=int(data.get("year_start") or 0), year_end=int(data.get("year_end") or 0),
            period_label=_bi(data.get("period_label")), status=data.get("status", "RESOLVED"),
            type=data.get("type", "serial"), tags=_list(data.get("tags")), tier=data.get("tier", "FREE"),
            sensitive=bool(data.get("sensitive", True)), triggers=_bi(data.get("triggers")),
            lat=data.get("lat"), lon=data.get("lon"), published_at=data.get("published_at", ""),
            editorial=data.get("editorial", "yanis"), summary=_bi(data.get("summary")),
            sections=_list(data.get("sections")), lessons=_list(data.get("lessons")),
            errors=_list((data.get("investigation") or {}).get("errors")), unknowns=_list(data.get("unknowns")),
            cover=data.get("cover", ""), stats=stats,
        )
        db.add(case)
        db.flush()

        for src in sources.values():
            src.case_id = case.id
            db.add(src)
        db.flush()

        def sid(key):
            row = sources.get(key) if key else None
            return row.id if row else None

        # --- archives / media (§22) ------------------------------------
        for s in _list(data.get("sources")):
            db.add(MediaItem(case_id=case.id, scope="case", kind=s.get("type", "press"), title=_bi(s.get("title")),
                             author=s.get("author", ""), publisher=s.get("publisher", ""), date=str(s.get("date", "")),
                             url=s.get("url", ""), reliability=s.get("reliability", "CONFIRMED"),
                             verified_at=s.get("verified_at", ""),
                             note=_bi(s.get("note")) if s.get("note") else {}))

        # --- victims & memorial (§20, §21) -----------------------------
        for v in _list(data.get("victims")):
            victim = Victim(
                case_id=case.id, order_index=int(v.get("order", 0)), first_name=v.get("first_name", ""),
                last_name=v.get("last_name", ""), age=str(v.get("age", "")),
                life=v.get("life") or {}, disappearance=v.get("disappearance") or {},
                anonymised=bool(v.get("anonymised", False)), reliability=v.get("reliability", "CONFIRMED"),
                source_id=sid(v.get("source")), note=_bi(v.get("note")) if v.get("note") else {},
            )
            db.add(victim)
            db.flush()
            full = " ".join(x for x in (v.get("first_name"), v.get("last_name")) if x)
            db.add(Memorial(
                case_id=case.id, victim_id=victim.id, tier="FREE",
                title=_bi((v.get("life") or {}).get("fr", {}).get("headline") or full),
                biography=_bi(v.get("life")), testimony=_bi(v.get("disappearance")),
                memory=_bi(v.get("note")) if v.get("note") else {}, portrait="", audio_clip="",
            ))

        mem = data.get("memorial") or {}
        if mem:
            # Case-level memorial page (the permanent 🕯 Mémoire section).
            v0 = db.query(Victim).filter_by(case_id=case.id).order_by(Victim.order_index).first()
            db.add(Memorial(case_id=case.id, victim_id=v0.id if v0 else None, tier="FREE",
                            title=_bi(mem.get("title")), biography=_bi(mem.get("biography")),
                            testimony=_bi(mem.get("testimony")), memory=_bi(mem.get("memory")),
                            portrait="", audio_clip=""))

        # --- timeline (§17) --------------------------------------------
        # Some dossiers ship `timeline_phases` as [(date, phase), ...] to label
        # each event; others omit it. Both shapes are handled.
        raw_phases = data.get("timeline_phases") or []
        phase_by_index: dict[int, str] = {}
        if raw_phases and isinstance(raw_phases[0], (list, tuple)):
            for i, pair in enumerate(raw_phases):
                if len(pair) >= 2:
                    phase_by_index[i] = str(pair[1])
        for i, t in enumerate(_list(data.get("timeline"))):
            phase = phase_by_index.get(i) or str(t.get("phase", "") or "")
            db.add(TimelineEvent(case_id=case.id, order_index=i, phase=phase, date=str(t.get("date", "")),
                                 title=_bi(t.get("title")) if t.get("title") else {}, body=_bi(t.get("body")),
                                 reliability=t.get("reliability", "CONFIRMED"), source_id=sid(t.get("source"))))

        # --- locations (§18) -------------------------------------------
        for l in _list(data.get("locations")):
            db.add(Location(case_id=case.id, kind=l.get("kind", "scene"), names=_bi(l.get("names")),
                            region=l.get("region", ""), city=l.get("city", ""),
                            country_code=l.get("country", data.get("country", "")), lat=l.get("lat"), lon=l.get("lon"),
                            precision=l.get("precision", "city"), date=str(l.get("date", "")),
                            note=_bi(l.get("note")) if l.get("note") else {},
                            reliability=l.get("reliability", "CONFIRMED"), source_id=sid(l.get("source"))))

        # --- evidence (§24) --------------------------------------------
        for e in _list(data.get("evidence")):
            db.add(Evidence(case_id=case.id, kind=e.get("kind", "physical"), title=_bi(e.get("title")),
                            description=_bi(e.get("description")), weight=e.get("weight", "documented"),
                            reliability=e.get("reliability", "CONFIRMED"), source_id=sid(e.get("source"))))

        # --- investigation (§25) ---------------------------------------
        inv = data.get("investigation") or {}
        if inv:
            db.add(Investigation(case_id=case.id, steps=_list(inv.get("steps")), reality=_bi(inv.get("reality")),
                                 errors=_list(inv.get("errors")), cold_case=inv.get("cold_case") or {}))

        # --- psychology / victimology (§27) ----------------------------
        psy = data.get("psychology") or {}
        if psy:
            db.add(Psychology(case_id=case.id, blocks=_list(psy.get("blocks")),
                              disclaimer=_bi(psy.get("disclaimer"))))
        vic = data.get("victimology") or {}
        if vic:
            db.add(Victimology(case_id=case.id, blocks=_list(vic.get("blocks")),
                               ethics_note=_bi(vic.get("ethics_note"))))

        # --- court (§32) -----------------------------------------------
        court = data.get("court") or {}
        if court:
            db.add(Court(case_id=case.id, jurisdiction=_bi(court.get("jurisdiction")), verdict=_bi(court.get("verdict")),
                         sentence=court.get("sentence") or {}, appeals=_list(court.get("appeals")),
                         consequences=_list(court.get("consequences"))))

        # --- experts (§30) ---------------------------------------------
        for x in _list(data.get("experts")):
            db.add(Expert(case_id=case.id, label=_bi(x.get("label")), field=x.get("field", ""),
                          position=_bi(x.get("position")), source_id=sid(x.get("source"))))

        # --- episodes & questions (§26) --------------------------------
        for ep in _list(data.get("episodes")):
            transcript = ep.get("transcript") or {}
            segments = _list(transcript.get("segments"))
            # Production narration may be shorter than the editorial script
            # timestamps. When an explicit media duration exists, keep that
            # measured duration; legacy script-only episodes retain the
            # segment-derived fallback.
            duration = int(ep.get("duration_sec") or (int(segments[-1]["t"]) + 90 if segments else 0))
            row = Episode(case_id=case.id, number=int(ep.get("number", 1)), title=_bi(ep.get("title")),
                          description=_bi(ep.get("description")), modes=_list(ep.get("modes")) or ["documentary"],
                          duration_sec=duration, audio=ep.get("audio", ""),
                          audio_status=ep.get("audio_status", "script_only"),
                          voice_profile=ep.get("voice_profile", ""), transcript=transcript,
                          chapters=_list(ep.get("chapters")), published_at=data.get("published_at", ""))
            db.add(row)
            db.flush()
            for q in _list(data.get("questions")):
                if str(q.get("episode", "1")) != str(ep.get("number", 1)):
                    continue
                db.add(Question(case_id=case.id, episode_id=row.id, at_sec=q.get("at_sec"),
                                kind=q.get("kind", "behaviour"), prompt=_bi(q.get("prompt")),
                                choices=_list(q.get("choices")), explanation=q.get("explanation") or {},
                                source_id=sid(q.get("source"))))

        # --- counterfactuals (§51-§57) ---------------------------------
        for cf in _list(data.get("counterfactuals")):
            payload = build_counterfactual(cf, slug)
            db.add(Counterfactual(case_id=case.id, kind=payload["kind"], title=payload["title"],
                                  signature_line=payload["signature_line"], question=payload["question"],
                                  parameters=payload["parameters"], documented_events=payload["documented_events"],
                                  established=payload["established"], reflection_hints=payload["reflection_hints"],
                                  disclaimer=payload["disclaimer"], computable=payload["computable"],
                                  source_id=sid(payload.get("source"))))


def seed_users(db) -> None:
    defaults = [
        ("yanis@yanisx.app", "yanis-admin", "Yanis", "admin", "PREMIUM"),
        ("lecteur@yanisx.app", "lecteur-demo", "Lecteur", "user", "FREE"),
        ("abonne@yanisx.app", "abonne-demo", "Abonné", "user", "PREMIUM"),
    ]
    for email, password, name, role, tier in defaults:
        if db.query(User).filter_by(email=email).first() is None:
            db.add(User(email=email, password_hash=hash_password(password), display_name=name, role=role, tier=tier,
                        language="fr"))
    db.flush()
    demo = db.query(User).filter_by(email="lecteur@yanisx.app").first()
    if demo is not None:
        for kind, ref, value in (
            ("badge", "dossier_discovered", {"case": "affaire-gregory", "at": _now().isoformat()}),
            ("question", "affaire-gregory:1:0", {"choice": "b", "correct": True}),
            ("audio", "affaire-gregory:1", {"at_sec": 240, "mode": "documentary"}),
            ("favourite", "affaire-gregory", {"on": True}),
        ):
            if db.query(UserProgress).filter_by(user_id=demo.id, kind=kind, ref=ref).first() is None:
                db.add(UserProgress(user_id=demo.id, kind=kind, ref=ref, value=value))


def seed(force: bool = True) -> dict:
    init_db()
    db = SessionLocal()
    try:
        seed_countries(db)
        seed_reference(db)
        if force:
            _purge_content(db)
            db.flush()
        seed_cases(db)
        seed_users(db)
        db.commit()
        counts = {
            "cases": db.query(Case).count(),
            "sources": db.query(Source).count(),
            "victims": db.query(Victim).count(),
            "timeline": db.query(TimelineEvent).count(),
            "locations": db.query(Location).count(),
            "evidence": db.query(Evidence).count(),
            "episodes": db.query(Episode).count(),
            "questions": db.query(Question).count(),
            "counterfactuals": db.query(Counterfactual).count(),
            "experts": db.query(Expert).count(),
            "media": db.query(MediaItem).count(),
            "glossary": db.query(GlossaryEntry).count(),
            "courses": db.query(Course).count(),
            "countries": db.query(Country).count(),
            "users": db.query(User).count(),
        }
        return counts
    finally:
        db.close()


if __name__ == "__main__":
    result = seed()
    print("YANIS//X database seeded:")
    for k, v in result.items():
        print(f"  {k:>14}: {v}")
