"""YANIS//X — API.

Identity: "ARCHIVES CRIMINELLES PREMIUM". Every response carries the editorial
rules that govern it: nothing invented, nothing glorified, victims centred.
"""
from __future__ import annotations

import os
from datetime import datetime, timezone

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from . import ethics
from .db import init_db
from .routes import ROUTERS

DESCRIPTION = """
**YANIS//X — à travers mon regard / through my eyes**

Podcast documentaire interactif, dossiers d'affaires criminelles réelles,
criminologie, psychologie, victimologie, enquête, archives et mémoire.

Documentary interactive podcast, real criminal case dossiers, criminology,
psychology, victimology, investigation, archives and memory.

Règles éditoriales / editorial rules:
- aucune donnée inventée — *no invented data*
- chaque fait porte un niveau de fiabilité et sa source — *every fact carries a reliability level and its source*
- les victimes sont au centre, jamais payantes — *victims come first, never paywalled*
- aucun classement, aucune glorification, aucun jeu avec la violence — *no ranking, no glorification, no gamified violence*
"""

app = FastAPI(
    title="YANIS//X — à travers mon regard",
    description=DESCRIPTION,
    version="1.0.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    redoc_url=None,
)

_origins = os.environ.get("YANISX_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Range", "Accept-Ranges", "Content-Length"],
)

for router in ROUTERS:
    app.include_router(router, prefix="/api")


@app.on_event("startup")
def _startup() -> None:
    init_db()


@app.exception_handler(404)
async def not_found(request: Request, exc) -> JSONResponse:
    return JSONResponse(status_code=404, content={
        "detail": getattr(exc, "detail", "Introuvable / Not found"),
        "path": str(request.url.path),
        "hint": {"fr": "Aucun écran mort : vérifiez l'identifiant ou revenez à l'accueil.",
                 "en": "No dead screen: check the identifier or return to the home page."},
    })


@app.get("/api/health", tags=["system"])
def health() -> dict:
    return {
        "status": "ok",
        "app": {"name": ethics.APP_NAME, "tagline": ethics.APP_TAGLINE},
        "time": datetime.now(timezone.utc).isoformat(),
        "languages": ["fr", "en"],
        "editorial_rules": ethics.NEVER,
    }


@app.get("/api", tags=["system"])
def index() -> dict:
    """Route map — so no endpoint is a dead end for a developer or a crawler."""
    return {
        "app": {"name": ethics.APP_NAME, "tagline": ethics.APP_TAGLINE},
        "docs": "/api/docs",
        "endpoints": {
            "health": "/api/health",
            "meta": "/api/meta",
            "ethics": "/api/ethics",
            "cases": "/api/cases",
            "case": "/api/cases/{slug}",
            "case_sections": "/api/cases/{slug}/sections/{key}",
            "victims": "/api/cases/{slug}/victims",
            "memorial": "/api/cases/{slug}/memorial",
            "timeline": "/api/cases/{slug}/timeline",
            "geography": "/api/cases/{slug}/geography",
            "evidence": "/api/cases/{slug}/evidence",
            "investigation": "/api/cases/{slug}/investigation",
            "psychology": "/api/cases/{slug}/psychology",
            "victimology": "/api/cases/{slug}/victimology",
            "court": "/api/cases/{slug}/court",
            "experts": "/api/cases/{slug}/experts",
            "sources": "/api/cases/{slug}/sources",
            "lessons": "/api/cases/{slug}/lessons",
            "questions": "/api/cases/{slug}/questions",
            "recommendations": "/api/cases/{slug}/recommendations",
            "episodes": "/api/episodes",
            "episode": "/api/episodes/{id}",
            "transcript": "/api/episodes/{id}/transcript",
            "answer": "/api/questions/{id}/answer",
            "counterfactuals": "/api/counterfactuals",
            "counterfactual": "/api/counterfactuals/{id}",
            "reflect": "/api/counterfactuals/{id}/reflect",
            "world": "/api/explore",
            "continent": "/api/explore/continent/{continent}",
            "country": "/api/explore/country/{code}",
            "region": "/api/explore/country/{code}/region/{region}",
            "city": "/api/explore/country/{code}/city/{city}",
            "map": "/api/explore/map",
            "compare": "/api/explore/compare?ids=a,b",
            "search": "/api/search?q=",
            "analyst": "/api/analyst",
            "archives": "/api/archives",
            "all_sources": "/api/sources",
            "audio": "/api/audio/{file}",
            "glossary": "/api/glossary",
            "courses": "/api/courses",
            "countries": "/api/countries",
            "auth": "/api/auth/register, /api/auth/login, /api/auth/me",
            "progress": "/api/progress, /api/progress/resume, /api/progress/favourite/{slug}",
            "voices": "/api/auth/me/voices",
            "notifications": "/api/notifications, /api/notifications/{id}/read, /api/notifications/read-all",
            "admin": "/api/admin/stats, /api/admin/revisions, /api/admin/reseed, /api/admin/notifications",
        },
    }
