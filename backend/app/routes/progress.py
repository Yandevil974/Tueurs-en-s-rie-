"""Progress, resume, favourites, badges (§8, §36). Sober gamification only."""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import ethics
from ..auth import require_user
from ..db import get_db
from ..models import Case, Episode, User, UserProgress

router = APIRouter(prefix="/progress", tags=["progress"])

KINDS = {"audio", "case_section", "investigation_step", "question", "badge", "favourite", "reflection", "course"}


def _rows(db: Session, user: User, kind: str | None = None):
    q = db.query(UserProgress).filter_by(user_id=user.id)
    if kind:
        q = q.filter(UserProgress.kind == kind)
    return q.all()


@router.get("")
def get_all(user: User = Depends(require_user), db: Session = Depends(get_db)):
    rows = _rows(db, user)
    grouped: dict[str, list[dict[str, Any]]] = {}
    for r in rows:
        grouped.setdefault(r.kind, []).append({"ref": r.ref, "value": r.value,
                                               "updated_at": r.updated_at.isoformat() if r.updated_at else ""})
    earned = {r.ref for r in rows if r.kind == "badge"}
    return {
        "progress": grouped,
        "badges": [{"key": b["key"], "fr": b["fr"], "en": b["en"], "rule_fr": b["rule_fr"], "rule_en": b["rule_en"],
                    "earned": b["key"] in earned} for b in ethics.BADGES],
        "policy": {"fr": "Aucun badge ne récompense la violence, la cruauté ou l'identification d'un coupable.",
                   "en": "No badge rewards violence, cruelty or identifying a culprit."},
    }


@router.put("/{kind}/{ref:path}")
def put(kind: str, ref: str, payload: dict[str, Any] | None = None, user: User = Depends(require_user),
        db: Session = Depends(get_db)):
    if kind not in KINDS:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, f"Type inconnu / Unknown kind: {kind}")
    value = payload if isinstance(payload, dict) else {}
    row = db.query(UserProgress).filter_by(user_id=user.id, kind=kind, ref=ref).first()
    if row is None:
        row = UserProgress(user_id=user.id, kind=kind, ref=ref, value=value)
        db.add(row)
    else:
        merged = dict(row.value or {})
        merged.update(value)
        row.value = merged
    db.commit()
    db.refresh(row)
    return {"kind": kind, "ref": ref, "value": row.value,
            "updated_at": row.updated_at.isoformat() if row.updated_at else ""}


@router.get("/resume")
def resume(user: User = Depends(require_user), db: Session = Depends(get_db)):
    """§8: continue exactly where the listener stopped."""
    audio = [r for r in _rows(db, user, "audio")]
    audio.sort(key=lambda r: r.updated_at or r.created_at if hasattr(r, "created_at") else r.updated_at, reverse=True)
    out = []
    for r in audio[:8]:
        try:
            case_slug, ep_number = r.ref.split(":")
        except ValueError:
            continue
        case = db.query(Case).filter_by(slug=case_slug).first()
        ep = db.query(Episode).filter_by(case_id=case.id, number=int(ep_number)).first() if case else None
        if ep is None:
            continue
        out.append({
            "case_id": case_slug, "case_title": case.title, "episode_id": ep.id, "episode_number": ep.number,
            "episode_title": ep.title, "duration_sec": ep.duration_sec, "at_sec": int((r.value or {}).get("at_sec", 0)),
            "mode": (r.value or {}).get("mode", "documentary"), "audio_status": ep.audio_status,
            "updated_at": r.updated_at.isoformat() if r.updated_at else "",
        })
    sections = [r for r in _rows(db, user, "case_section")]
    return {"audio": out, "sections": [{"ref": r.ref, "value": r.value} for r in sections[:20]]}


@router.post("/favourite/{slug}")
def toggle_favourite(slug: str, user: User = Depends(require_user), db: Session = Depends(get_db)):
    case = db.query(Case).filter_by(slug=slug).first()
    if case is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Dossier introuvable / Case not found")
    row = db.query(UserProgress).filter_by(user_id=user.id, kind="favourite", ref=slug).first()
    on = True
    if row is None:
        db.add(UserProgress(user_id=user.id, kind="favourite", ref=slug, value={"on": True}))
    else:
        on = not bool((row.value or {}).get("on", False))
        row.value = {"on": on}
    db.commit()
    return {"case_id": slug, "favourite": on}


@router.post("/badge/{key}")
def award_badge(key: str, payload: dict[str, Any] | None = None, user: User = Depends(require_user),
                db: Session = Depends(get_db)):
    valid = {b["key"] for b in ethics.BADGES}
    if key not in valid:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, f"Badge inconnu / Unknown badge: {key}")
    row = db.query(UserProgress).filter_by(user_id=user.id, kind="badge", ref=key).first()
    if row is None:
        db.add(UserProgress(user_id=user.id, kind="badge", ref=key,
                            value={"context": (payload or {}).get("context", "")}))
        db.commit()
        return {"awarded": True, "badge": next(b for b in ethics.BADGES if b["key"] == key)}
    return {"awarded": False, "already": True, "badge": next(b for b in ethics.BADGES if b["key"] == key)}
