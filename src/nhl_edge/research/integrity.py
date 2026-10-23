"""Research-integrity registry: frozen historical data, frozen parameter files, frozen result artifacts and frozen evaluation cohorts (RESEARCH_ONLY).

``docs/research/INTEGRITY_REGISTRY.json`` records the sha256 of every historical data file under ``data/history``, every production parameter file under
``data/params`` and every frozen research artifact (preregistrations, walk-forward and challenger result tables), plus the literal values of the evaluation
cohorts and thresholds that define prior studies. ``tests/test_research_integrity.py`` fails when

* a registered file is modified or removed (a re-pulled season, a re-run table, an edited preregistration);
* an *unregistered* data file or parameter file appears (new seasons are welcome, but only through an explicit, reviewed ``register`` step);
* a cohort definition or a promotion threshold drifts from its registered value;
* a production or frozen-driver module reads full history instead of its pinned seasons.

The registry is append-only: ``register`` adds new entries and refuses to change an existing one. A frozen artifact is superseded by a new, differently
named file (a new parameter version, an amendment document), never edited in place.

    python -m nhl_edge.research.integrity check
    python -m nhl_edge.research.integrity register   # appends entries for files that are new; never rewrites an existing entry
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[3]
REGISTRY = REPO_ROOT / "docs" / "research" / "INTEGRITY_REGISTRY.json"

# Data that must never change silently: raw historical tables and production parameter files. Anything new under these globs must be registered.
DATA_GLOBS = ("data/history/**/*.parquet", "data/history/**/*.jsonl.gz", "data/params/*.json")
# Frozen research artifacts (preregistrations, amendments, committed per-game result tables). New files are fine; once registered they cannot change.
RESULT_GLOBS = (
    "docs/research/**/PREREGISTRATION*.md", "docs/research/**/AMENDMENT_*.md", "docs/research/WORKLOAD_V1_PREREGISTRATION.md",
    "docs/research/workload_v1/preregistration.json", "docs/research/workload_v1/LEVEL_CALIBRATION_PREREGISTRATION.md",
    "docs/research/workload_v1/*.json", "docs/research/workload_v2/*.json",
    "docs/research/oa-walk-forward/data/*", "docs/research/v1-retune/data/*", "docs/research/v2-joint/*.json", "docs/research/v2-joint-retuned/data/*",
    "docs/research/walk_forward_*_games.csv", "docs/research/walk_forward_*.json",
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _collect(globs: tuple[str, ...], root: Path) -> dict[str, Path]:
    out: dict[str, Path] = {}
    for g in globs:
        for p in sorted(root.glob(g)):
            if p.is_file():
                out[p.relative_to(root).as_posix()] = p
    return out


def scan(root: Path = REPO_ROOT) -> dict[str, dict[str, Any]]:
    files = {**_collect(DATA_GLOBS, root), **_collect(RESULT_GLOBS, root)}
    return {k: {"sha256": sha256_file(p), "bytes": p.stat().st_size} for k, p in sorted(files.items())}


def cohort_values() -> dict[str, Any]:
    """The literal definitions of the evaluation cohorts and promotion thresholds as the code currently holds them (JSON-friendly)."""
    from nhl_edge.data import history as H
    from nhl_edge.research import daily_scoreboard as DS
    from nhl_edge.research import oa_evaluate as OE
    from nhl_edge.research import promotion as P
    from nhl_edge.research import retune_evaluate as RE
    from nhl_edge.research import workload_experiment as WE

    return {
        "history.PINNED_MIN_SEASONS": dict(H.PINNED_MIN_SEASONS),
        "oa_evaluate.UNEXPOSED_SEASONS": list(OE.UNEXPOSED_SEASONS), "oa_evaluate.EXPOSED_SEASONS": list(OE.EXPOSED_SEASONS),
        "retune_evaluate.FRESH": list(RE.FRESH), "retune_evaluate.FAMILY_SEEN": list(RE.FAMILY_SEEN), "retune_evaluate.EXPOSED": list(RE.EXPOSED),
        "retune_evaluate.FRESH2": list(RE.FRESH2), "retune_evaluate.MIN_SEASONS_FAVOURABLE": RE.MIN_SEASONS_FAVOURABLE,
        "retune_evaluate.FRESH2_MIN_FAVOURABLE": RE.FRESH2_MIN_FAVOURABLE, "retune_evaluate.PRACTICAL": dict(RE.PRACTICAL),
        "workload_experiment.SEASONS": list(WE.SEASONS),
        "daily_scoreboard.PROSPECTIVE_FREEZE_UTC": DS.PROSPECTIVE_FREEZE_UTC,
        "promotion.MIN_UNEXPOSED_SEASONS": P.MIN_UNEXPOSED_SEASONS, "promotion.MIN_UNEXPOSED_GAMES": P.MIN_UNEXPOSED_GAMES,
        "promotion.MIN_MEANINGFUL": dict(P.MIN_MEANINGFUL), "promotion.NON_INFERIORITY": dict(P.NON_INFERIORITY),
        "promotion.MIN_SEASON_AGREEMENT": P.MIN_SEASON_AGREEMENT, "promotion.MAX_ECE_WORSENING": P.MAX_ECE_WORSENING,
        "promotion.COVERAGE_80_BAND": list(P.COVERAGE_80_BAND), "promotion.MAX_INFERENCE_SECONDS_PER_SLATE": P.MAX_INFERENCE_SECONDS_PER_SLATE,
    }


def load_registry(path: Path = REGISTRY) -> dict[str, Any]:
    return json.loads(path.read_text()) if path.exists() else {"schema": "nhl-integrity-1", "files": {}, "cohorts": {}}


def diff(registry: dict[str, Any], current: dict[str, dict[str, Any]], cohorts: dict[str, Any] | None = None, data_only_unregistered: bool = True) -> dict[str, list[str]]:
    reg = registry.get("files", {})
    out: dict[str, list[str]] = {"modified": [], "missing": [], "unregistered": [], "cohort_drift": []}
    for k, v in reg.items():
        if k not in current:
            out["missing"].append(k)
        elif current[k]["sha256"] != v["sha256"]:
            out["modified"].append(k)
    for k in current:
        if k not in reg and (not data_only_unregistered or k.startswith(("data/history/", "data/params/"))):
            out["unregistered"].append(k)
    if cohorts is not None:
        for k, v in registry.get("cohorts", {}).items():
            if cohorts.get(k) != v:
                out["cohort_drift"].append(f"{k}: registered {v!r} != code {cohorts.get(k)!r}")
        for k in cohorts:
            if k not in registry.get("cohorts", {}):
                out["cohort_drift"].append(f"{k}: not registered")
    return out


def register(registry: dict[str, Any], current: dict[str, dict[str, Any]], cohorts: dict[str, Any]) -> dict[str, Any]:
    """Append entries for new files and new cohort keys. Never rewrites an existing entry (raises instead)."""
    d = diff(registry, current, cohorts, data_only_unregistered=False)
    if d["modified"] or d["cohort_drift"] and any("registered" in x and "!=" in x for x in d["cohort_drift"]):
        raise SystemExit(f"refusing to change registered entries: modified={d['modified']} cohort_drift={d['cohort_drift']}. "
                         "Supersede a frozen artifact with a new, differently named file; never edit it in place.")
    new = {**registry, "files": dict(registry.get("files", {})), "cohorts": dict(registry.get("cohorts", {}))}
    for k in d["unregistered"]:
        new["files"][k] = current[k]
    for k, v in cohorts.items():
        new["cohorts"].setdefault(k, v)
    new["files"] = dict(sorted(new["files"].items()))
    return new


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.integrity")
    ap.add_argument("cmd", choices=("check", "register"))
    a = ap.parse_args(argv)
    reg, cur, coh = load_registry(), scan(), cohort_values()
    if a.cmd == "check":
        d = diff(reg, cur, coh)
        print(json.dumps(d, indent=1))
        return 1 if any(d.values()) else 0
    new = register(reg, cur, coh)
    new["schema"] = "nhl-integrity-1"
    REGISTRY.write_text(json.dumps(new, indent=1) + "\n")
    print(f"registry: {len(new['files'])} files, {len(new['cohorts'])} cohort keys")
    return 0


if __name__ == "__main__":
    sys.exit(main())
