"""Database engine / session management (SQLite by default, swappable for Postgres)."""
from __future__ import annotations

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.environ.get("YANISX_DB", os.path.join(BASE_DIR, "data", "yanisx.sqlite3"))
MEDIA_DIR = os.environ.get("YANISX_MEDIA", os.path.join(BASE_DIR, "content", "media"))
CASES_DIR = os.path.join(BASE_DIR, "data", "cases")

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)

engine = create_engine(
    f"sqlite:///{DB_PATH}",
    connect_args={"check_same_thread": False},
    future=True,
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False, future=True)


class Base(DeclarativeBase):
    pass


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    from . import models  # noqa: F401  (registers mappers)

    Base.metadata.create_all(bind=engine)
