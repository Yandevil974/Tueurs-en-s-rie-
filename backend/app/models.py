"""
YANIS//X - data model.

Implements the architecture of the product specification (§39):

CASE
 ├── OFFENDER
 ├── VICTIMS
 ├── LOCATIONS
 ├── TIMELINE
 ├── EVIDENCE
 ├── INVESTIGATION
 ├── PSYCHOLOGY
 ├── VICTIMOLOGY
 ├── COURT
 ├── MEDIA
 ├── SOURCES
 ├── PODCAST
 ├── QUESTIONS
 ├── EXPERTS
 └── MEMORIAL
plus: counterfactual ("ET SI ?"), lessons, errors, unknowns, admin revisions.

Every substantive fact carries a reliability level (CONFIRMED / PROBABLE /
DISPUTED / UNKNOWN) and a source id (§23, §43).
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from sqlalchemy import (
    JSON,
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base

# --- reference constants -------------------------------------------------
RELIABILITY = ("CONFIRMED", "PROBABLE", "DISPUTED", "UNKNOWN")
CASE_STATUS = ("RESOLVED", "UNSOLVED", "HISTORICAL", "ONGOING", "PARTIALLY_RESOLVED")
TIER = ("FREE", "PREMIUM")


def _now() -> datetime:
    return datetime.now(timezone.utc)


# =========================================================================
# ACCOUNTS / ACCESS
# =========================================================================
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    display_name: Mapped[str] = mapped_column(String(120), default="")
    role: Mapped[str] = mapped_column(String(20), default="user")  # user | editor | admin
    tier: Mapped[str] = mapped_column(String(20), default="FREE")
    language: Mapped[str] = mapped_column(String(8), default="fr")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_now)
    # accessibility preferences (§45)
    a11y: Mapped[dict[str, Any]] = mapped_column(
        JSON,
        default=lambda: {"fontScale": 1.0, "contrast": "standard", "reduceMotion": False, "captions": True},
    )

    progresses: Mapped[list["UserProgress"]] = relationship(back_populates="user", cascade="all, delete-orphan")


class Notification(Base):
    """A user-facing editorial notification (§39). Content is authored and bilingual."""

    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    kind: Mapped[str] = mapped_column(String(30), default="editorial")
    title: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    body: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    href: Mapped[str] = mapped_column(String(240), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_now)
    read_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


class VoiceProfile(Base):
    """🎙 MA VOIX (§58-§60): the creator's narration voice."""

    __tablename__ = "voice_profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    name: Mapped[str] = mapped_column(String(120))
    kind: Mapped[str] = mapped_column(String(20), default="REAL")  # REAL | SYNTHETIC
    language: Mapped[str] = mapped_column(String(8), default="fr")
    samples: Mapped[list[Any]] = mapped_column(JSON, default=list)
    status: Mapped[str] = mapped_column(String(20), default="draft")  # draft | validated | active
    consent: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_now)


# =========================================================================
# GEOGRAPHY (§18, §19)
# =========================================================================
class Country(Base):
    __tablename__ = "countries"

    code: Mapped[str] = mapped_column(String(2), primary_key=True)
    names: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)  # {fr, en}
    continent: Mapped[str] = mapped_column(String(20), default="")
    flag: Mapped[str] = mapped_column(String(8), default="")
    cases: Mapped[list["Case"]] = relationship(back_populates="country")


class Location(Base):
    """A place attached to a case. Never stores a private exact address (§18)."""

    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), index=True)
    kind: Mapped[str] = mapped_column(String(40), default="scene")  # scene | city | region | country | court
    names: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    region: Mapped[str] = mapped_column(String(160), default="")
    city: Mapped[str] = mapped_column(String(160), default="")
    country_code: Mapped[str] = mapped_column(String(2), default="")
    lat: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    lon: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    precision: Mapped[str] = mapped_column(String(20), default="city")  # city | region | approximate
    date: Mapped[str] = mapped_column(String(24), default="")
    note: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    reliability: Mapped[str] = mapped_column(String(12), default="CONFIRMED")
    source_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    case: Mapped[Case] = relationship(back_populates="locations")


# =========================================================================
# SOURCES (§22, §23, §43)
# =========================================================================
class Source(Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[Optional[int]] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), index=True)
    scope: Mapped[str] = mapped_column(String(20), default="case")  # case | global
    title: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    author: Mapped[str] = mapped_column(String(200), default="")
    publisher: Mapped[str] = mapped_column(String(200), default="")
    type: Mapped[str] = mapped_column(String(40), default="press")
    # press | court_record | scientific | book | public_archive | interview | official | testimony
    url: Mapped[str] = mapped_column(String(600), default="")
    date: Mapped[str] = mapped_column(String(24), default="")
    reliability: Mapped[str] = mapped_column(String(12), default="CONFIRMED")
    verified_at: Mapped[str] = mapped_column(String(24), default="")
    note: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    case: Mapped[Optional[Case]] = relationship(back_populates="sources")


# =========================================================================
# THE CASE (§9, §10)
# =========================================================================
class Case(Base):
    __tablename__ = "cases"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    title: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    subtitle: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    country_code: Mapped[str] = mapped_column(String(2), ForeignKey("countries.code"), default="")
    region: Mapped[str] = mapped_column(String(160), default="")
    city: Mapped[str] = mapped_column(String(160), default="")
    year_start: Mapped[int] = mapped_column(Integer, default=0)
    year_end: Mapped[int] = mapped_column(Integer, default=0)
    period_label: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    status: Mapped[str] = mapped_column(String(24), default="RESOLVED")
    type: Mapped[str] = mapped_column(String(40), default="serial")
    # serial | cold_case | disappearance | historical | single_homicide | miscarriage
    tags: Mapped[list[str]] = mapped_column(JSON, default=list)
    tier: Mapped[str] = mapped_column(String(12), default="FREE")
    sensitive: Mapped[bool] = mapped_column(Boolean, default=True)
    triggers: Mapped[list[str]] = mapped_column(JSON, default=list)
    lat: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    lon: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    published_at: Mapped[str] = mapped_column(String(24), default="")
    editorial: Mapped[str] = mapped_column(String(40), default="")
    summary: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    sections: Mapped[list[Any]] = mapped_column(JSON, default=list)  # the 20 dossier sections (§9)
    lessons: Mapped[list[Any]] = mapped_column(JSON, default=list)  # §33
    errors: Mapped[list[Any]] = mapped_column(JSON, default=list)  # §31
    unknowns: Mapped[list[Any]] = mapped_column(JSON, default=list)  # §19 zones d'ombre
    cover: Mapped[str] = mapped_column(String(300), default="")
    stats: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)

    country: Mapped[Country] = relationship(back_populates="cases")
    offender: Mapped[Optional["Offender"]] = relationship(
        back_populates="case", uselist=False, cascade="all, delete-orphan"
    )
    victims: Mapped[list["Victim"]] = relationship(
        back_populates="case", cascade="all, delete-orphan", order_by="Victim.order_index"
    )
    timeline: Mapped[list["TimelineEvent"]] = relationship(
        back_populates="case", cascade="all, delete-orphan", order_by="TimelineEvent.order_index"
    )
    evidence: Mapped[list["Evidence"]] = relationship(back_populates="case", cascade="all, delete-orphan")
    investigation: Mapped[Optional["Investigation"]] = relationship(
        back_populates="case", uselist=False, cascade="all, delete-orphan"
    )
    psychology: Mapped[Optional["Psychology"]] = relationship(
        back_populates="case", uselist=False, cascade="all, delete-orphan"
    )
    victimology: Mapped[Optional["Victimology"]] = relationship(
        back_populates="case", uselist=False, cascade="all, delete-orphan"
    )
    court: Mapped[Optional["Court"]] = relationship(back_populates="case", uselist=False, cascade="all, delete-orphan")
    locations: Mapped[list["Location"]] = relationship(back_populates="case", cascade="all, delete-orphan")
    sources: Mapped[list["Source"]] = relationship(back_populates="case", cascade="all, delete-orphan")
    counterfactuals: Mapped[list["Counterfactual"]] = relationship(
        back_populates="case", cascade="all, delete-orphan"
    )
    experts: Mapped[list["Expert"]] = relationship(back_populates="case", cascade="all, delete-orphan")
    episodes: Mapped[list["Episode"]] = relationship(
        back_populates="case", cascade="all, delete-orphan", order_by="Episode.number"
    )
    questions: Mapped[list["Question"]] = relationship(back_populates="case", cascade="all, delete-orphan")
    memorials: Mapped[list["Memorial"]] = relationship(back_populates="case", cascade="all, delete-orphan")
    counterfactuals: Mapped[list["Counterfactual"]] = relationship(
        back_populates="case", cascade="all, delete-orphan"
    )
    media: Mapped[list["MediaItem"]] = relationship(back_populates="case", cascade="all, delete-orphan")
    sources: Mapped[list["Source"]] = relationship(
        back_populates="case", cascade="all, delete-orphan"
    )


class Offender(Base):
    """§14 DANS LA TÊTE — studied, never glorified (§44)."""

    __tablename__ = "offenders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(200), default="")
    alias: Mapped[list[str]] = mapped_column(JSON, default=list)
    birth: Mapped[str] = mapped_column(String(40), default="")
    birth_place: Mapped[str] = mapped_column(String(200), default="")
    death: Mapped[str] = mapped_column(String(40), default="")
    background: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    documented_life: Mapped[list[Any]] = mapped_column(JSON, default=list)
    behaviour: Mapped[list[Any]] = mapped_column(JSON, default=list)
    no_diagnosis_note: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    case: Mapped[Case] = relationship(back_populates="offender")


class Victim(Base):
    """§11 LES VICTIMES SONT AU CENTRE — a human file, never "Victim 1"."""

    __tablename__ = "victims"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), index=True)
    order_index: Mapped[int] = mapped_column(Integer, default=0)
    first_name: Mapped[str] = mapped_column(String(120), default="")
    last_name: Mapped[str] = mapped_column(String(120), default="")
    anonymised: Mapped[bool] = mapped_column(Boolean, default=False)
    age: Mapped[Optional[str]] = mapped_column(String(40), nullable=True)
    life: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    # occupation, studies, family, friends, passions, projects, hometown, testimonies
    disappearance: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    memorial_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    reliability: Mapped[str] = mapped_column(String(12), default="CONFIRMED")
    source_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    note: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    case: Mapped[Case] = relationship(back_populates="victims")


class Memorial(Base):
    """🕯 MÉMOIRE (§12) — always FREE (§46)."""

    __tablename__ = "memorials"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), index=True)
    victim_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    title: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    biography: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    testimony: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    memory: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    portrait: Mapped[str] = mapped_column(String(300), default="")
    audio_clip: Mapped[str] = mapped_column(String(300), default="")
    tier: Mapped[str] = mapped_column(String(12), default="FREE")
    case: Mapped[Case] = relationship(back_populates="memorials")


class TimelineEvent(Base):
    __tablename__ = "timeline_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), index=True)
    order_index: Mapped[int] = mapped_column(Integer, default=0)
    phase: Mapped[str] = mapped_column(String(40), default="facts")
    # childhood | early | first_facts | first_victim | evolution | investigation | arrest | trial | after
    date: Mapped[str] = mapped_column(String(40), default="")
    title: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    body: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    reliability: Mapped[str] = mapped_column(String(12), default="CONFIRMED")
    source_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    case: Mapped[Case] = relationship(back_populates="timeline")


class Evidence(Base):
    __tablename__ = "evidence"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), index=True)
    kind: Mapped[str] = mapped_column(String(40), default="physical")
    # physical | forensic | dna | testimony | digital | documentary | trace
    title: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    description: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    weight: Mapped[str] = mapped_column(String(20), default="documented")  # documented | decisive | disputed
    reliability: Mapped[str] = mapped_column(String(12), default="CONFIRMED")
    source_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    case: Mapped[Case] = relationship(back_populates="evidence")


class Investigation(Base):
    """🔎 MODE ENQUÊTE (§16) — steps revealed in the order they existed."""

    __tablename__ = "investigations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), unique=True, index=True)
    steps: Mapped[list[Any]] = mapped_column(JSON, default=list)
    reality: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    errors: Mapped[list[Any]] = mapped_column(JSON, default=list)
    cold_case: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    # whatWeKnow / whatIsProbable / whatIsDisputed / whatIsUnknown / latestProgress / leads / limits
    case: Mapped[Case] = relationship(back_populates="investigation")


class Psychology(Base):
    __tablename__ = "psychology"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), unique=True, index=True)
    blocks: Mapped[list[Any]] = mapped_column(JSON, default=list)
    disclaimer: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    case: Mapped[Case] = relationship(back_populates="psychology")


class Victimology(Base):
    __tablename__ = "victimology"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), unique=True, index=True)
    blocks: Mapped[list[Any]] = mapped_column(JSON, default=list)
    ethics_note: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    case: Mapped[Case] = relationship(back_populates="victimology")


class Court(Base):
    __tablename__ = "courts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), unique=True, index=True)
    jurisdiction: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    verdict: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    sentence: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    appeals: Mapped[list[Any]] = mapped_column(JSON, default=list)
    consequences: Mapped[list[Any]] = mapped_column(JSON, default=list)
    case: Mapped[Case] = relationship(back_populates="court")


class Expert(Base):
    """§30 CE QUE LES EXPERTS DISENT."""

    __tablename__ = "experts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), index=True)
    label: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    field: Mapped[str] = mapped_column(String(120), default="")
    position: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    source_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    case: Mapped[Case] = relationship(back_populates="experts")


class Counterfactual(Base):
    """🔎 ET SI ? (§51-§57). Hypothetical reconstruction, never a judgement."""

    __tablename__ = "counterfactuals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), index=True)
    kind: Mapped[str] = mapped_column(String(60), default="release")
    title: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    signature_line: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    question: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    parameters: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    documented_events: Mapped[list[Any]] = mapped_column(JSON, default=list)
    established: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    reflection_hints: Mapped[list[Any]] = mapped_column(JSON, default=list)
    disclaimer: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    computable: Mapped[bool] = mapped_column(Boolean, default=True)
    source_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    case: Mapped[Case] = relationship(back_populates="counterfactuals")


# =========================================================================
# PODCAST (§7, §25, §26)
# =========================================================================
class Episode(Base):
    __tablename__ = "episodes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), index=True)
    number: Mapped[int] = mapped_column(Integer, default=1)
    title: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    description: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    modes: Mapped[list[str]] = mapped_column(JSON, default=lambda: ["documentary"])
    duration_sec: Mapped[int] = mapped_column(Integer, default=0)
    audio: Mapped[str] = mapped_column(String(400), default="")
    audio_status: Mapped[str] = mapped_column(String(20), default="pending")  # produced | pending | script_only
    voice_profile: Mapped[str] = mapped_column(String(40), default="")
    transcript: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)  # segments[]
    chapters: Mapped[list[Any]] = mapped_column(JSON, default=list)
    published_at: Mapped[str] = mapped_column(String(24), default="")
    case: Mapped[Case] = relationship(back_populates="episodes")


class Question(Base):
    """Interactive pedagogical questions (§3, §26). Never rewards violence (§4)."""

    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), index=True)
    episode_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    at_sec: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    kind: Mapped[str] = mapped_column(String(30), default="behaviour")
    # behaviour | investigation | psychology | chronology | victimology | evidence | bias
    prompt: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    choices: Mapped[list[Any]] = mapped_column(JSON, default=list)
    explanation: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    # whatInvestigatorsKnew / whatExpertsProposed / documented / hypothetical / whatYouCouldNotKnow
    source_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    case: Mapped[Case] = relationship(back_populates="questions")


class MediaItem(Base):
    """📚 ARCHIVES (§22)."""

    __tablename__ = "media"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    case_id: Mapped[Optional[int]] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), index=True)
    scope: Mapped[str] = mapped_column(String(20), default="case")
    kind: Mapped[str] = mapped_column(String(40), default="article")
    title: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    author: Mapped[str] = mapped_column(String(200), default="")
    publisher: Mapped[str] = mapped_column(String(200), default="")
    date: Mapped[str] = mapped_column(String(24), default="")
    url: Mapped[str] = mapped_column(String(600), default="")
    reliability: Mapped[str] = mapped_column(String(12), default="PROBABLE")
    verified_at: Mapped[str] = mapped_column(String(24), default="")
    note: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    case: Mapped[Case] = relationship(back_populates="media")


# =========================================================================
# LEARNING (§28, §29)
# =========================================================================
class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    field: Mapped[str] = mapped_column(String(60), default="criminology")
    title: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    intro: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    minutes: Mapped[int] = mapped_column(Integer, default=8)
    level: Mapped[str] = mapped_column(String(20), default="beginner")
    lessons: Mapped[list[Any]] = mapped_column(JSON, default=list)
    case_refs: Mapped[list[str]] = mapped_column(JSON, default=list)
    tier: Mapped[str] = mapped_column(String(12), default="FREE")


class GlossaryEntry(Base):
    __tablename__ = "glossary"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    term: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    simple: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    deep: Mapped[dict[str, str]] = mapped_column(JSON, default=dict)
    field: Mapped[str] = mapped_column(String(60), default="criminology")
    case_refs: Mapped[list[str]] = mapped_column(JSON, default=list)
    source_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)


# =========================================================================
# ADMIN (§42, §43)
# =========================================================================
class Revision(Base):
    """History of every data modification."""

    __tablename__ = "revisions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    entity: Mapped[str] = mapped_column(String(60))
    entity_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    action: Mapped[str] = mapped_column(String(20), default="update")  # create | update | delete
    diff: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    reason: Mapped[str] = mapped_column(String(400), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_now)


class UserProgress(Base):
    """Resume (§8), interactive answers, gamification (§36)."""

    __tablename__ = "user_progress"
    __table_args__ = (UniqueConstraint("user_id", "kind", "ref", name="uq_progress"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    kind: Mapped[str] = mapped_column(String(30))
    # audio | case_section | investigation_step | question | badge | favourite | reflection
    ref: Mapped[str] = mapped_column(String(160))
    value: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=_now, onupdate=_now)
    user: Mapped[User] = relationship(back_populates="progresses")
