"""🎧 Podcasts: episodes, modes, transcript, the interactive pause points (§3, §26)."""
from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import ethics
from ..db import get_db
from ..models import Case, Episode, Question, Source
from ._serialise import episode_out, question_out, sources_map

router = APIRouter(tags=["podcasts"])


def _episode(db: Session, episode_id: int) -> Episode:
    ep = db.get(Episode, episode_id)
    if ep is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Épisode introuvable / Episode not found")
    return ep


@router.get("/episodes")
def list_episodes(case: Optional[str] = None, mode: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Episode)
    if case:
        c = db.query(Case).filter_by(slug=case).first()
        if c is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Dossier introuvable / Case not found")
        query = query.filter(Episode.case_id == c.id)
    rows = query.order_by(Episode.published_at.desc(), Episode.case_id).all()
    if mode:
        rows = [r for r in rows if mode in (r.modes or [])]
    return {
        "count": len(rows),
        "episodes": [episode_out(r, full=False) for r in rows],
        "modes": [{"key": k, "label": {"fr": v["fr"], "en": v["en"]}, "description": v["desc"]}
                  for k, v in ethics.EPISODE_MODES.items()],
    }


@router.get("/episodes/{episode_id}")
def get_episode(episode_id: int, db: Session = Depends(get_db)):
    ep = _episode(db, episode_id)
    smap = sources_map(db, ep.case_id)
    questions = db.query(Question).filter_by(episode_id=ep.id).order_by(Question.at_sec).all()
    payload = episode_out(ep, full=True)
    # The pause points drive the player: audio stops, question appears,
    # explanation is shown, then playback resumes (§3).
    payload["pause_points"] = [question_out(q, smap) for q in questions]
    payload["signature_line"] = ethics.SIGNATURE_LINE
    return payload


@router.get("/episodes/{episode_id}/transcript")
def get_transcript(episode_id: int, db: Session = Depends(get_db)):
    ep = _episode(db, episode_id)
    segments = (ep.transcript or {}).get("segments") or []
    return {"episode_id": ep.id, "case_id": ep.case.slug, "segments": segments,
            "chapters": ep.chapters or [],
            "accessibility": {"fr": "Transcription intégrale disponible ; sous-titres synchronisés sur les segments.",
                              "en": "Full transcript available; captions synchronised on segments."}}


@router.get("/episodes/{episode_id}/questions")
def episode_questions(episode_id: int, db: Session = Depends(get_db)):
    ep = _episode(db, episode_id)
    smap = sources_map(db, ep.case_id)
    rows = db.query(Question).filter_by(episode_id=ep.id).order_by(Question.at_sec).all()
    return {"episode_id": ep.id, "questions": [question_out(q, smap) for q in rows]}


@router.post("/questions/{question_id}/answer")
def answer_question(question_id: int, payload: dict, db: Session = Depends(get_db)):
    """§3-§4: the answer unlocks an EXPLANATION, never a score for violence."""
    q = db.get(Question, question_id)
    if q is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Question introuvable / Question not found")
    choice = str((payload or {}).get("choice", ""))
    valid = [c.get("id") for c in (q.choices or [])]
    if choice not in valid:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY,
                            f"Choix invalide / Invalid choice. Attendu: {valid}")
    smap = sources_map(db, q.case_id)
    explanation = q.explanation or {}
    note = ""
    for lang in ("fr", "en"):
        block = explanation.get(lang) or {}
        if isinstance(block, dict) and block.get("answer_note"):
            note = block["answer_note"]
            break
    return {
        "question_id": q.id, "choice": choice,
        "explanation": explanation,
        "source": smap.get(q.source_id) if q.source_id else None,
        "answer_note": note,
        "reward": {"fr": "Ce qui est valorisé ici : la compréhension et l'analyse, jamais la violence.",
                   "en": "What is valued here: understanding and analysis, never violence."},
        "resume": {"fr": "La lecture reprend après l'explication.", "en": "Playback resumes after the explanation."},
    }


@router.get("/episodes/{episode_id}/resume")
def resume_point(episode_id: int, db: Session = Depends(get_db)):
    """Where playback should continue if the listener comes back (§8)."""
    ep = _episode(db, episode_id)
    questions = db.query(Question).filter_by(episode_id=ep.id).order_by(Question.at_sec).all()
    return {"episode_id": ep.id, "duration_sec": ep.duration_sec,
            "pause_points": [q.at_sec for q in questions if q.at_sec is not None],
            "audio_status": ep.audio_status}
