"""The launch catalogue: 8 fully sourced dossiers (§37 "start with 10-20 cases")."""
from __future__ import annotations

from . import (btk_rader, emile_louis, estelle_mouzin, fourniret_olivier,
               golden_state_killer, gregory_villemin, guy_georges,
               peter_sutcliffe)

# Order = editorial order on the home page.
CASES: list[dict] = [
    estelle_mouzin.CASE,
    gregory_villemin.CASE,
    guy_georges.CASE,
    emile_louis.CASE,
    fourniret_olivier.CASE,
    btk_rader.CASE,
    golden_state_killer.CASE,
    peter_sutcliffe.CASE,
]

CASE_IDS: list[str] = [c["id"] for c in CASES]

BY_ID: dict[str, dict] = {c["id"]: c for c in CASES}

__all__ = ["CASES", "CASE_IDS", "BY_ID"]
