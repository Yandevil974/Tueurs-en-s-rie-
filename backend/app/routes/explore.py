"""🌍 Explorer (§18-§19): world -> continent -> country -> region -> city -> case.
No exact private address is ever published."""
from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Case, Country, Location
from ._serialise import case_card, location_out, sources_map

router = APIRouter(prefix="/explore", tags=["explore"])


def _country(db: Session, code: str) -> Country:
    row = db.get(Country, code.upper())
    if row is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Pays introuvable / Country not found: {code}")
    return row


@router.get("")
def world(db: Session = Depends(get_db)):
    countries = db.query(Country).all()
    by_continent: dict[str, list[dict]] = {}
    total = 0
    for c in countries:
        n = db.query(Case).filter_by(country_code=c.code).count()
        if n == 0:
            continue
        total += n
        by_continent.setdefault(c.continent or "—", []).append({
            "code": c.code, "names": c.names, "flag": c.flag, "cases": n,
        })
    return {
        "level": "world",
        "total_cases": total,
        "continents": [{"name": k, "countries": v, "cases": sum(x["cases"] for x in v)}
                       for k, v in sorted(by_continent.items())],
        "drilldown": {"fr": ["MONDE", "CONTINENT", "PAYS", "RÉGION", "VILLE", "AFFAIRE"],
                      "en": ["WORLD", "CONTINENT", "COUNTRY", "REGION", "CITY", "CASE"]},
        "next": "/explore/continent/{continent}",
    }


@router.get("/continent/{continent}")
def continent(continent: str, db: Session = Depends(get_db)):
    rows = [c for c in db.query(Country).all() if (c.continent or "").lower() == continent.lower()]
    if not rows:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Continent introuvable / Continent not found")
    countries = []
    for c in rows:
        n = db.query(Case).filter_by(country_code=c.code).count()
        if n:
            countries.append({"code": c.code, "names": c.names, "flag": c.flag, "cases": n})
    return {"level": "continent", "continent": continent, "countries": countries,
            "next": "/explore/country/{code}"}


@router.get("/country/{code}")
def country(code: str, db: Session = Depends(get_db)):
    c = _country(db, code)
    cases = db.query(Case).filter_by(country_code=c.code).all()
    regions: dict[str, int] = {}
    for case in cases:
        regions[case.region or "—"] = regions.get(case.region or "—", 0) + 1
    return {
        "level": "country", "country": {"code": c.code, "names": c.names, "flag": c.flag, "continent": c.continent},
        "cases": [case_card(x, c) for x in cases],
        "regions": [{"name": k, "cases": v} for k, v in sorted(regions.items(), key=lambda kv: -kv[1])],
        "next": "/explore/country/{code}/region/{region}",
    }


@router.get("/country/{code}/region/{region}")
def region(code: str, region: str, db: Session = Depends(get_db)):
    c = _country(db, code)
    cases = db.query(Case).filter_by(country_code=c.code, region=region).all()
    cities: dict[str, int] = {}
    for case in cases:
        cities[case.city or "—"] = cities.get(case.city or "—", 0) + 1
    return {"level": "region", "country": {"code": c.code, "names": c.names, "flag": c.flag}, "region": region,
            "cases": [case_card(x, c) for x in cases],
            "cities": [{"name": k, "cases": v} for k, v in sorted(cities.items(), key=lambda kv: -kv[1])],
            "next": "/explore/country/{code}/city/{city}"}


@router.get("/country/{code}/city/{city}")
def city(code: str, city: str, db: Session = Depends(get_db)):
    c = _country(db, code)
    cases = db.query(Case).filter_by(country_code=c.code, city=city).all()
    return {"level": "city", "country": {"code": c.code, "names": c.names, "flag": c.flag}, "city": city,
            "cases": [case_card(x, c) for x in cases],
            "no_exact_address": {"fr": "Aucune adresse privée exacte n'est publiée : la précision s'arrête à la ville.",
                                 "en": "No exact private address is published: precision stops at the city."},
            "next": "/cases/{slug}"}


@router.get("/map")
def map_points(country: Optional[str] = None, db: Session = Depends(get_db)):
    """Every documented place, with its precision and reliability."""
    query = db.query(Location)
    if country:
        query = query.filter(Location.country_code == country.upper())
    rows = query.all()
    smap: dict[int, dict] = {}
    out = []
    for r in rows:
        smap.update(sources_map(db, r.case_id))
        out.append(location_out(r, smap))
    cases = db.query(Case).all()
    case_points = [{"slug": c.slug, "title": c.title, "country": c.country_code, "lat": c.lat, "lon": c.lon,
                    "status": c.status, "type": c.type} for c in cases if c.lat is not None]
    return {"locations": out, "case_points": case_points,
            "precision_levels": ["city", "region", "country", "approximate"],
            "no_exact_address": {"fr": "Aucune adresse privée exacte n'est publiée.",
                                 "en": "No exact private address is published."}}


@router.get("/compare")
def compare(ids: str, db: Session = Depends(get_db)):
    """§19 comparator. NO dangerousness or intelligence ranking (§44)."""
    slugs = [s.strip() for s in ids.split(",") if s.strip()]
    if len(slugs) < 2:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY,
                            "Au moins deux dossiers sont requis / At least two cases are required")
    if len(slugs) > 4:
        slugs = slugs[:4]
    countries = {c.code: c for c in db.query(Country).all()}
    rows = [db.query(Case).filter_by(slug=s).first() for s in slugs]
    if any(r is None for r in rows):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Au moins un dossier est introuvable / A case was not found")

    def line(case: Case) -> dict:
        sentence = {}
        if case.court:
            sentence = case.court.sentence or {}
        inv = case.investigation
        steps = len(inv.steps or []) if inv else 0
        cold = (inv.cold_case or {}) if inv else {}
        return {
            "id": case.slug, "title": case.title,
            "country": countries.get(case.country_code).names if countries.get(case.country_code) else {},
            "period": case.period_label, "status": case.status, "type": case.type,
            "victims_documented": len(case.victims),
            "victims_named": sum(1 for v in case.victims if not v.anonymised and v.last_name),
            "investigation_steps": steps,
            "cold_case_unknowns": len(cold.get("what_is_unknown") or []),
            "sentence_label": sentence.get("label", {}),
            "sentence_pronounced": sentence.get("pronounced", ""),
            "counterfactuals": len(case.counterfactuals),
            "episodes": len(case.episodes),
            "sources": len(case.sources),
            "lessons": len(case.lessons or []),
        }

    return {
        "cases": [line(c) for c in rows],
        "axes": {"fr": ["période", "pays", "statut", "victimes documentées", "étapes d'enquête", "zones d'ombre",
                        "décision de justice", "sources"],
                 "en": ["period", "country", "status", "documented victims", "investigation steps", "unknown zones",
                        "court decision", "sources"]},
        "forbidden": {"fr": "Aucun classement par dangerosité, intelligence ou nombre de victimes n'est proposé.",
                      "en": "No ranking by dangerousness, intelligence or victim count is offered."},
    }
