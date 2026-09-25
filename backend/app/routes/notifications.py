"""🔔 Notifications: explicit editorial messages, never fabricated."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..auth import require_user
from ..db import get_db
from ..models import Notification

router = APIRouter(prefix="/notifications", tags=["notifications"])


def _out(row: Notification) -> dict[str, Any]:
    return {
        "id": row.id,
        "kind": row.kind,
        "title": row.title or {},
        "body": row.body or {},
        "href": row.href or "",
        "created_at": row.created_at.isoformat() if row.created_at else "",
        "read": row.read_at is not None,
    }


@router.get("")
def list_notifications(limit: int = 50, user=Depends(require_user), db: Session = Depends(get_db)):
    rows = (db.query(Notification).filter_by(user_id=user.id)
            .order_by(Notification.created_at.desc(), Notification.id.desc())
            .limit(min(max(limit, 1), 100)).all())
    return {"unread": sum(1 for row in rows if row.read_at is None), "notifications": [_out(row) for row in rows]}


@router.post("/{notification_id}/read")
def mark_read(notification_id: int, user=Depends(require_user), db: Session = Depends(get_db)):
    row = db.query(Notification).filter_by(id=notification_id, user_id=user.id).first()
    if row is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Notification introuvable / Notification not found")
    if row.read_at is None:
        row.read_at = datetime.now(timezone.utc)
        db.commit()
    return {"id": row.id, "read": True}


@router.post("/read-all")
def mark_all_read(user=Depends(require_user), db: Session = Depends(get_db)):
    rows = db.query(Notification).filter_by(user_id=user.id).all()
    now = datetime.now(timezone.utc)
    changed = 0
    for row in rows:
        if row.read_at is None:
            row.read_at = now
            changed += 1
    db.commit()
    return {"read": changed}
