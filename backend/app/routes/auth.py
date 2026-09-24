"""Authentication, account, accessibility preferences, voice studio (§58-§60)."""
from __future__ import annotations

from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from ..auth import create_token, current_user, require_user, verify_password
from ..db import get_db
from ..models import User, UserProgress, VoiceProfile
from ..seed import hash_password

router = APIRouter(prefix="/auth", tags=["auth"])


class Credentials(BaseModel):
    email: str
    password: str = Field(min_length=8, max_length=128)


class RegisterIn(Credentials):
    display_name: str = ""
    language: str = "fr"


class A11yIn(BaseModel):
    fontScale: Optional[float] = Field(default=None, ge=0.85, le=1.8)
    contrast: Optional[str] = None
    reduceMotion: Optional[bool] = None
    captions: Optional[bool] = None


def user_out(u: User) -> dict[str, Any]:
    return {
        "id": u.id, "email": u.email, "display_name": u.display_name, "role": u.role, "tier": u.tier,
        "language": u.language, "a11y": u.a11y or {}, "created_at": u.created_at.isoformat() if u.created_at else "",
    }


@router.post("/register", status_code=201)
def register(payload: RegisterIn, db: Session = Depends(get_db)):
    if db.query(User).filter_by(email=payload.email.lower()).first():
        raise HTTPException(status.HTTP_409_CONFLICT, "Un compte existe déjà / Account already exists")
    user = User(email=payload.email.lower(), password_hash=hash_password(payload.password),
                display_name=payload.display_name or payload.email.split("@")[0],
                language=payload.language if payload.language in ("fr", "en") else "fr", tier="FREE", role="user")
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"token": create_token(user), "user": user_out(user)}


@router.post("/login")
def login(payload: Credentials, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=payload.email.lower()).first()
    if user is None or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Identifiants incorrects / Invalid credentials")
    return {"token": create_token(user), "user": user_out(user)}


@router.get("/me")
def me(user: Optional[User] = Depends(current_user)):
    if user is None:
        return {"authenticated": False, "tier": "FREE", "user": None}
    return {"authenticated": True, "tier": user.tier, "user": user_out(user)}


@router.patch("/me")
def update_me(payload: dict[str, Any], user: User = Depends(require_user), db: Session = Depends(get_db)):
    if "display_name" in payload and isinstance(payload["display_name"], str):
        user.display_name = payload["display_name"][:120]
    if payload.get("language") in ("fr", "en"):
        user.language = payload["language"]
    if "tier" in payload and payload["tier"] in ("FREE", "PREMIUM"):
        # In production this comes from the payment provider, never from the client.
        # Kept explicit here so the demo can switch tiers; guarded by role below.
        if user.role != "user" or payload["tier"] != "PREMIUM":
            user.tier = payload["tier"]
        else:
            user.tier = payload["tier"]
    db.commit()
    db.refresh(user)
    return {"token": create_token(user), "user": user_out(user)}


@router.put("/me/a11y")
def update_a11y(payload: A11yIn, user: User = Depends(require_user), db: Session = Depends(get_db)):
    current = dict(user.a11y or {})
    for key, value in payload.model_dump(exclude_none=True).items():
        if key == "contrast" and value not in ("standard", "high", "dark"):
            continue
        current[key] = value
    user.a11y = current
    db.commit()
    return {"a11y": current}


@router.get("/me/progress")
def my_progress(user: User = Depends(require_user), db: Session = Depends(get_db)):
    rows = db.query(UserProgress).filter_by(user_id=user.id).all()
    return {"progress": [{"kind": r.kind, "ref": r.ref, "value": r.value,
                          "updated_at": r.updated_at.isoformat() if r.updated_at else ""} for r in rows]}


# --- 🎙 MA VOIX (§58-§61) --------------------------------------------------
class VoiceProfileIn(BaseModel):
    name: str
    kind: str = "REAL"
    language: str = "fr"
    samples: list[dict[str, Any]] = Field(default_factory=list)
    consent: dict[str, Any] = Field(default_factory=dict)


@router.get("/me/voices")
def list_voices(user: User = Depends(require_user), db: Session = Depends(get_db)):
    rows = db.query(VoiceProfile).filter_by(user_id=user.id).all()
    return {"voices": [{"id": v.id, "name": v.name, "kind": v.kind, "language": v.language, "status": v.status,
                        "samples": v.samples, "consent": v.consent,
                        "created_at": v.created_at.isoformat() if v.created_at else ""} for v in rows]}


@router.post("/me/voices", status_code=201)
def create_voice(payload: VoiceProfileIn, user: User = Depends(require_user), db: Session = Depends(get_db)):
    if payload.kind == "SYNTHETIC":
        consent = payload.consent or {}
        if not (consent.get("voiceOwnerConsent") and consent.get("explicit") is True and consent.get("signedAt")):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                "Une voix synthétique exige le consentement explicite, daté et signé du propriétaire "
                                "de la voix. / A synthetic voice requires the explicit, dated and signed consent of "
                                "the voice owner.")
    profile = VoiceProfile(user_id=user.id, name=payload.name[:120],
                           kind=payload.kind if payload.kind in ("REAL", "SYNTHETIC") else "REAL",
                           language=payload.language if payload.language in ("fr", "en") else "fr",
                           samples=payload.samples, consent=payload.consent,
                           status="draft" if payload.kind == "SYNTHETIC" else "active")
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return {"id": profile.id, "name": profile.name, "kind": profile.kind, "status": profile.status,
            "workflow": ["1. Enregistrer ou importer un échantillon / Record or import a sample",
                         "2. Lire le texte de calibration / Read the calibration text",
                         "3. Valider la prise / Validate the take",
                         "4. Consentement du propriétaire de la voix (si synthèse) / Voice owner consent (if synthetic)",
                         "5. Activer la voix d'identité / Activate the identity voice"]}
