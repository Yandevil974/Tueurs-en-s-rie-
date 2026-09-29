"""Helpers to build a case dossier with a consistent, source-bound structure."""
from __future__ import annotations

from typing import Any


def txt(fr: str, en: str) -> dict[str, str]:
    """A bilingual text field."""
    return {"fr": fr, "en": en}


def fact(body_fr: str, body_en: str, reliability: str = "CONFIRMED", source: str | None = None,
         title_fr: str = "", title_en: str = "", date: str = "") -> dict[str, Any]:
    """A dated fact with an explicit reliability level and an optional source key."""
    return {
        "date": date,
        "title": txt(title_fr, title_en) if title_fr else None,
        "body": txt(body_fr, body_en),
        "reliability": reliability,
        "source": source,
    }


def block(kind: str, title_fr: str, title_en: str, body_fr: str = "", body_en: str = "",
          reliability: str = "CONFIRMED", source: str | None = None,
          items: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """A dossier block: paragraph or bullet list, always labelled."""
    return {
        "kind": kind,
        "title": txt(title_fr, title_en),
        "body": txt(body_fr, body_en) if (body_fr or body_en) else None,
        "items": items or [],
        "reliability": reliability,
        "source": source,
    }


def item(text_fr: str, text_en: str, reliability: str = "CONFIRMED", source: str | None = None,
         label_fr: str = "", label_en: str = "") -> dict[str, Any]:
    return {
        "label": txt(label_fr, label_en) if label_fr else None,
        "text": txt(text_fr, text_en),
        "reliability": reliability,
        "source": source,
    }


def source(key: str, case_id: str, title_fr: str, title_en: str, publisher: str, author: str,
           url: str, date: str, type_: str = "press", reliability: str = "CONFIRMED",
           verified_at: str = "2026-09-24", note_fr: str = "", note_en: str = "") -> dict[str, Any]:
    return {
        "key": key,
        "case_id": case_id,
        "title": txt(title_fr, title_en),
        "publisher": publisher,
        "author": author,
        "url": url,
        "date": date,
        "type": type_,
        "reliability": reliability,
        "verified_at": verified_at,
        "note": txt(note_fr, note_en) if note_fr else None,
    }


def question(episode: str, at_sec: int | None, kind: str, prompt_fr: str, prompt_en: str,
             choices: list[tuple[str, str, str]], explanation: dict[str, Any],
             source: str | None = None) -> dict[str, Any]:
    """
    Interactive pedagogical question (§3, §26).
    choices: [(id, label_fr, label_en), ...]
    """
    return {
        "episode": episode,
        "at_sec": at_sec,
        "kind": kind,
        "prompt": txt(prompt_fr, prompt_en),
        "choices": [{"id": cid, "label": txt(lfr, len_)} for cid, lfr, len_ in choices],
        "explanation": explanation,
        "source": source,
    }


def counterfactual(kind: str, title_fr: str, title_en: str, question_fr: str, question_en: str,
                   parameters: dict[str, Any], documented_events: list[dict[str, Any]],
                   computable: bool = True, source: str | None = None) -> dict[str, Any]:
    """🔎 ET SI ? (§51-§57). The engine computes the answer; wording stays cautious."""
    return {
        "kind": kind,
        "title": txt(title_fr, title_en),
        "question": txt(question_fr, question_en),
        "parameters": parameters,
        "documented_events": documented_events,
        "computable": computable,
        "source": source,
    }


# The 20 mandatory dossier sections (§9). Titles are fixed so that every case
# exposes the same navigation; content comes from the dedicated modules.
DEFAULT_SECTIONS: list[tuple[str, str, str]] = [
    ("introduction", "Introduction", "Introduction"),
    ("context", "Contexte", "Context"),
    ("offender", "Auteur", "Author"),
    ("victims", "Victimes", "Victims"),
    ("timeline", "Chronologie", "Chronology"),
    ("investigation", "Enquête", "Investigation"),
    ("clues", "Indices et preuves", "Clues and evidence"),
    ("behaviour", "Analyse comportementale", "Behavioural analysis"),
    ("psychology", "Psychologie", "Psychology"),
    ("victimology", "Victimologie", "Victimology"),
    ("geography", "Géographie", "Geography"),
    ("arrest", "Arrestation", "Arrest"),
    ("trial", "Procès", "Trial"),
    ("justice", "Justice", "Justice"),
    ("consequences", "Conséquences", "Consequences"),
    ("archives", "Archives", "Archives"),
    ("sources", "Sources", "Sources"),
    ("memorial", "Mémoire", "Memory"),
    ("unknowns", "Zones d'ombre", "Unknown zones"),
    ("lessons", "Ce que l'affaire nous apprend", "What the case teaches us"),
]


def default_sections() -> list[dict[str, Any]]:
    return [{"key": k, "title": txt(fr, en), "blocks": []} for k, fr, en in DEFAULT_SECTIONS]


def merge_sections(base: list[dict[str, Any]], extra: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Inject authored blocks into the canonical 20-section structure."""
    index = {s["key"]: s for s in base}
    for section in extra:
        target = index.get(section["key"])
        if target is None:
            continue
        target["blocks"] = section.get("blocks", [])
        if "title" in section:
            target["title"] = section["title"]
    return base
