"""Authentication & authorisation: JWT sessions, tiers, roles (§39, §40)."""
from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from typing import Optional

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from .db import get_db
from .models import User
from .seed import hash_password, verify_password

SECRET = os.environ.get("YANISX_SECRET", "yanisx-dev-secret-change-me")
ALGORITHM = "HS256"
TOKEN_TTL_HOURS = int(os.environ.get("YANISX_TOKEN_HOURS", "72"))

bearer = HTTPBearer(auto_error=False)


def create_token(user: User) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user.id), "email": user.email, "role": user.role, "tier": user.tier,
        "name": user.display_name, "iat": now, "exp": now + timedelta(hours=TOKEN_TTL_HOURS),
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Session expirée / Session expired")
    except jwt.PyJWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Jeton invalide / Invalid token")


def current_user(credentials: Optional[HTTPAuthorizationCredentials] = Depends(bearer),
                 db: Session = Depends(get_db)) -> Optional[User]:
    """Optional auth: anonymous browsing is allowed (§46 free tier)."""
    if credentials is None or not credentials.credentials:
        return None
    data = decode_token(credentials.credentials)
    user = db.get(User, int(data["sub"]))
    return user


def require_user(user: Optional[User] = Depends(current_user)) -> User:
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Connexion requise / Login required")
    return user


def require_admin(user: User = Depends(require_user)) -> User:
    if user.role not in ("admin", "editor"):
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Droits insuffisants / Insufficient rights")
    return user


def is_premium(user: Optional[User]) -> bool:
    return user is not None and user.tier == "PREMIUM"


def require_premium(user: Optional[User] = Depends(current_user)) -> User:
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Connexion requise / Login required")
    if user.tier != "PREMIUM":
        raise HTTPException(status.HTTP_402_PAYMENT_REQUIRED,
                            "Contenu réservé à l'abonnement / Premium content")
    return user


__all__ = ["bearer", "create_token", "decode_token", "current_user", "require_user", "require_admin",
           "require_premium", "is_premium", "hash_password", "verify_password"]
