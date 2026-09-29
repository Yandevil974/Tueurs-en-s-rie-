"""Export the read-only API catalogue for the standalone Android package.

Run after ``python -m app.seed`` with ``PYTHONPATH=backend``. The resulting
JSON is bundled in Capacitor, so dossier pages and the world map work without a
separate backend service on the phone.
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote

from fastapi.testclient import TestClient

from .main import app

OUTPUT = Path(__file__).resolve().parents[2] / "frontend" / "src" / "data_embedded" / "index.json"


def main() -> None:
    responses: dict[str, object] = {}
    comparison_rows: dict[str, object] = {}
    comparison_note: object = None
    question_answers: dict[str, object] = {}
    skipped: list[str] = []

    with TestClient(app) as client:
        def get(path: str, request_path: str | None = None):
            url = "/api" + (request_path or path)
            response = client.get(url)
            if response.status_code != 200:
                skipped.append(f"GET {url}: {response.status_code}")
                return None
            payload = response.json()
            responses[path] = payload
            return payload

        def add_post(question_id: int, choice: str):
            path = f"/questions/{question_id}/answer"
            response = client.post("/api" + path, json={"choice": choice})
            if response.status_code == 200:
                question_answers.setdefault(str(question_id), {})[choice] = response.json()
            else:
                skipped.append(f"POST /api{path}: {response.status_code}")

        root_paths = (
            "/meta", "/ethics", "/cases", "/explore", "/explore/map",
            "/memory", "/memory/countries", "/archives", "/sources", "/glossary",
            "/countries", "/courses", "/episodes", "/counterfactuals",
        )
        for path in root_paths:
            get(path)

        cases = (responses.get("/cases") or {}).get("cases", [])
        for case in cases:
            slug = str(case.get("slug") or case.get("id") or "")
            if not slug:
                continue
            dossier = get(f"/cases/{slug}") or {}
            for suffix in (
                "victims", "memorial", "timeline", "geography", "evidence", "investigation",
                "psychology", "victimology", "court", "experts", "sources", "lessons",
                "questions", "recommendations",
            ):
                get(f"/cases/{slug}/{suffix}")
            for section in dossier.get("sections", []):
                key = str(section.get("key") or "")
                if key:
                    encoded = quote(key, safe="")
                    get(f"/cases/{slug}/sections/{key}", f"/cases/{slug}/sections/{encoded}")

        countries = (responses.get("/countries") or {}).get("countries", [])
        for country in countries:
            code = str(country.get("code") or "")
            if code:
                get(f"/explore/country/{code}")

        world = responses.get("/explore") or {}
        for continent in world.get("continents", []):
            name = str(continent.get("name") or "")
            if name:
                get(f"/explore/continent/{name}", f"/explore/continent/{quote(name, safe='')}")

        # Region and city drill-downs are captured from the case catalogue.
        seen_regions: set[tuple[str, str]] = set()
        seen_cities: set[tuple[str, str]] = set()
        for case in cases:
            code = str(case.get("country") or "")
            region = str(case.get("region") or "")
            city = str(case.get("city") or "")
            if code and region and (code, region) not in seen_regions:
                seen_regions.add((code, region))
                get(f"/explore/country/{code}/region/{region}",
                    f"/explore/country/{code}/region/{quote(region, safe='')}")
            if code and city and (code, city) not in seen_cities:
                seen_cities.add((code, city))
                get(f"/explore/country/{code}/city/{city}",
                    f"/explore/country/{code}/city/{quote(city, safe='')}")

        # One API comparison request yields a reusable row for each selected case.
        slugs = [str(case.get("slug") or case.get("id")) for case in cases]
        if len(slugs) >= 2:
            for other in slugs[1:]:
                payload = client.get("/api/explore/compare?ids=" + quote(slugs[0], safe="") + "," + quote(other, safe="")).json()
                if payload:
                    comparison_note = {key: value for key, value in payload.items() if key != "cases"}
                    for row in payload.get("cases", []):
                        comparison_rows[str(row.get("id"))] = row

        episodes = (responses.get("/episodes") or {}).get("episodes", [])
        for episode in episodes:
            episode_id = episode.get("id")
            if episode_id is None:
                continue
            get(f"/episodes/{episode_id}")
            get(f"/episodes/{episode_id}/transcript")
            get(f"/episodes/{episode_id}/questions")
            get(f"/episodes/{episode_id}/resume")

        courses = (responses.get("/courses") or {}).get("courses", [])
        for course in courses:
            slug = str(course.get("slug") or "")
            if slug:
                get(f"/courses/{slug}")

        glossary = (responses.get("/glossary") or {}).get("entries", [])
        for entry in glossary:
            slug = str(entry.get("slug") or "")
            if slug:
                get(f"/glossary/{slug}")

        counterfactuals = (responses.get("/counterfactuals") or {}).get("items", [])
        for item in counterfactuals:
            item_id = item.get("id")
            if item_id is not None:
                get(f"/counterfactuals/{item_id}")

        # Capture each choice so the offline player can return the exact API
        # response for the selection without contacting the server.
        question_ids: set[int] = set()
        for case in cases:
            payload = responses.get(f"/cases/{case.get('slug')}/questions") or {}
            for question in payload.get("questions", []):
                if question.get("id") is not None:
                    question_ids.add(int(question["id"]))
        for episode in episodes:
            payload = responses.get(f"/episodes/{episode.get('id')}") or {}
            for question in payload.get("pause_points", []):
                if question.get("id") is not None:
                    question_ids.add(int(question["id"]))
        for question_id in sorted(question_ids):
            question = next((q for key, payload in responses.items()
                             if key.endswith("/questions") or key.startswith("/episodes/")
                             for q in (payload.get("questions", []) if isinstance(payload, dict) else [])
                             if q.get("id") == question_id), None)
            if question is None:
                for key, payload in responses.items():
                    if key.startswith("/episodes/") and isinstance(payload, dict):
                        question = next((q for q in payload.get("pause_points", []) if q.get("id") == question_id), None)
                        if question:
                            break
            choices = (question or {}).get("choices") or []
            for choice in choices:
                choice_id = str(choice.get("id") or "")
                if choice_id:
                    add_post(question_id, choice_id)

    bundle = {
        "api": responses,
        "compareRows": comparison_rows,
        "compareMetadata": comparison_note or {},
        "questionAnswers": question_answers,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(bundle, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    size = OUTPUT.stat().st_size
    print(f"Embedded API catalogue exported to {OUTPUT} ({size:,} bytes; {len(responses)} routes).")
    if skipped:
        print("Some optional routes were unavailable:")
        for message in skipped:
            print(f"  - {message}")


if __name__ == "__main__":
    main()
