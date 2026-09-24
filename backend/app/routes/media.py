"""📚 Archives (§22) and audio delivery with HTTP Range support (§8, §39)."""
from __future__ import annotations

import os
import re
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import FileResponse, Response, StreamingResponse
from sqlalchemy.orm import Session

from .. import ethics
from ..db import MEDIA_DIR, get_db
from ..models import Case, MediaItem, Source
from ._serialise import source_out

router = APIRouter(tags=["media"])

CHUNK = 256 * 1024


def _safe_path(name: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9._-]", "", os.path.basename(name))
    if not clean or clean.startswith("."):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Nom de fichier invalide / Invalid file name")
    path = os.path.normpath(os.path.join(MEDIA_DIR, clean))
    if not path.startswith(os.path.normpath(MEDIA_DIR)):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Chemin invalide / Invalid path")
    if not os.path.isfile(path):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Fichier absent / File not found")
    return path


@router.get("/archives")
def archives(case: Optional[str] = None, kind: Optional[str] = None, reliability: Optional[str] = None,
             db: Session = Depends(get_db)):
    """§22: SOURCE / DATE / AUTHOR / TYPE / LINK / RELIABILITY."""
    rows = db.query(MediaItem).all()
    if case:
        c = db.query(Case).filter_by(slug=case).first()
        rows = [r for r in rows if r.case_id == (c.id if c else None)]
    if kind:
        rows = [r for r in rows if r.kind == kind]
    if reliability:
        rows = [r for r in rows if r.reliability == reliability.upper()]
    by_slug = {c.id: c.slug for c in db.query(Case).all()}
    rows.sort(key=lambda r: (r.date or ""), reverse=True)
    return {
        "count": len(rows),
        "fields": {"fr": ["SOURCE", "DATE", "AUTEUR", "TYPE", "LIEN", "FIABILITÉ"],
                   "en": ["SOURCE", "DATE", "AUTHOR", "TYPE", "LINK", "RELIABILITY"]},
        "levels": [{"key": k, "label": {"fr": v["fr"], "en": v["en"]}, "color": v["color"], "dot": v["dot"],
                    "definition": v["definition"]} for k, v in ethics.RELIABILITY.items()],
        "kinds": sorted({r.kind for r in db.query(MediaItem).all()}),
        "items": [{
            "id": r.id, "case": by_slug.get(r.case_id), "kind": r.kind, "title": r.title, "author": r.author,
            "publisher": r.publisher, "date": r.date, "url": r.url, "reliability": r.reliability,
            "reliability_label": {"fr": ethics.RELIABILITY.get(r.reliability, {}).get("fr", r.reliability),
                                  "en": ethics.RELIABILITY.get(r.reliability, {}).get("en", r.reliability)},
            "verified_at": r.verified_at, "note": r.note or {},
        } for r in rows],
        "policy": {"fr": "Aucune source inventée. Une rumeur n'est jamais présentée comme un fait.",
                   "en": "No invented source. A rumour is never presented as a fact."},
    }


@router.get("/sources")
def all_sources(db: Session = Depends(get_db)):
    rows = db.query(Source).all()
    by_slug = {c.id: c.slug for c in db.query(Case).all()}
    return {"count": len(rows),
            "sources": [{**source_out(r), "case": by_slug.get(r.case_id)} for r in rows]}


@router.head("/audio/{name}")
@router.get("/audio/{name}")
def audio(name: str, request: Request):
    """Range-aware audio streaming so the player can seek and resume."""
    path = _safe_path(name)
    size = os.path.getsize(path)
    ctype = "audio/mpeg" if path.lower().endswith((".mp3", ".mpeg")) else \
        "audio/wav" if path.lower().endswith(".wav") else \
        "audio/mp4" if path.lower().endswith((".m4a", ".mp4")) else "application/octet-stream"
    range_header = request.headers.get("range") or request.headers.get("Range")

    if not range_header:
        return FileResponse(path, media_type=ctype, headers={"Accept-Ranges": "bytes", "Content-Length": str(size)})

    match = re.match(r"bytes=(\d*)-(\d*)", range_header)
    if not match:
        raise HTTPException(status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE, "Range invalide / Invalid range")
    raw_start, raw_end = match.group(1), match.group(2)
    start = int(raw_start) if raw_start else 0
    end = int(raw_end) if raw_end else size - 1
    if raw_start == "" and raw_end != "":
        start = max(0, size - int(raw_end))
        end = size - 1
    if start >= size or end >= size or start > end:
        return Response(status_code=416, headers={"Content-Range": f"bytes */{size}"})

    length = end - start + 1

    def iterator():
        with open(path, "rb") as fh:
            fh.seek(start)
            remaining = length
            while remaining > 0:
                data = fh.read(min(CHUNK, remaining))
                if not data:
                    break
                remaining -= len(data)
                yield data

    return StreamingResponse(
        iterator(), status_code=206, media_type=ctype,
        headers={"Content-Range": f"bytes {start}-{end}/{size}", "Accept-Ranges": "bytes",
                 "Content-Length": str(length), "Cache-Control": "public, max-age=86400"},
    )
