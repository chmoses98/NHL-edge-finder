"""Completeness audit of the prospective ledger against the archived NHL schedule (RESEARCH_ONLY; runner-safe: reads only public schedule/result facts and the PUBLIC manifest).

    python -m nhl_edge.sealed_ledger.audit --archive A --through YYYY-MM-DD [--store S] [--dev-window]

The "authoritative historical schedule" available to the workflow is the archive's ``context/schedule`` (timestamped snapshots of the NHL schedule API) joined to the
``results`` kind. For every date from the first prospective date through ``--through`` the audit lists the scheduled regular-season games on the prospective side of the
freeze and checks, with game ids and counts only (no outcome):

* OPEN DAY: a past date with scheduled games that no DAY entry closed (a skipped or incomplete day) -- PROBLEM, so a gap can never be silently passed over;
* INCOMPLETE: a scheduled game that is not final long after its start (postponed / unfinished) -- PROBLEM for a past date: the day stays open;
* DRIFT: a closed day whose DAY entry no longer matches the archive's schedule for that date (a game was added or removed after closing) -- PROBLEM;
* EXTRA / UNSEALED: a sealed game the schedule does not list for that date, or a scheduled final game that is neither sealed nor declared missing -- PROBLEM;
* ORPHAN RESULT: a result row whose game id is absent from the schedule on or after the first prospective date (an eligible game the schedule missed) -- PROBLEM;
* RESULT REVISED: the source's final score of an already sealed game changed after sealing and no later versioned correction exists -- PROBLEM (a late revision is never
  absorbed silently; the runner skips sealed games, so only an explicit ``GAME_ID@VERSION`` correction can supersede a record);
* BOUNDARY: a game whose start time moved across the freeze instant between snapshots (eligibility is ambiguous) -- PROBLEM, resolved only by an explicit owner decision.

``--dev-window`` runs the same checks on the DEVELOPMENT side of the freeze (no store), which is how the logic is validated against real history without touching the
prospective tier. An independent cross-check against the live NHL API is provided by ``--nhl-api`` (needs network access to api-web.nhle.com; run it locally).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import pandas as pd

from nhl_edge.model_research import DEV_LAST_GAME_DATE_ET, PROSPECTIVE_FREEZE_UTC
from nhl_edge.sealed_ledger.core import read_manifest

FIRST_PROSPECTIVE_DATE_ET = "2026-10-21"  # the first ET date with a game starting after the freeze instant
FIRST_DEV_DATE_ET = "2026-09-29"
OVERDUE_AFTER = timedelta(hours=8)  # a regular-season game is final well within this after its scheduled start


def _dates(first: str, last: str) -> list[str]:
    d0, d1 = datetime.fromisoformat(first), datetime.fromisoformat(last)
    return [(d0 + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((d1 - d0).days + 1)]


def schedule_audit(archive: Path, through: str, *, store: Path | None = None, dev_window: bool = False, now: datetime | None = None,
                   games: pd.DataFrame | None = None, results: pd.DataFrame | None = None) -> dict[str, Any]:
    """``games`` (build_games output) and ``results`` (every observed results row: game_id, _observed_at_utc, home_final, away_final, last_period_type, _file) may be
    injected for tests; otherwise they are read from the archive."""
    from nhl_edge.market_audit.games import build_games, read_kind

    now = now or datetime.now(UTC)
    fz = pd.Timestamp(PROSPECTIVE_FREEZE_UTC)
    g_all = build_games(archive) if games is None else games.copy()
    g_all["game_id"] = g_all["game_id"].astype(str)
    g = g_all[g_all["season_type"] == "regular"]
    first = FIRST_DEV_DATE_ET if dev_window else FIRST_PROSPECTIVE_DATE_ET
    last = min(through, DEV_LAST_GAME_DATE_ET) if dev_window else through
    side = (g["start_time_utc"] < fz) if dev_window else (g["start_time_utc"] >= fz)
    problems: list[str] = []
    warnings: list[str] = []
    rows: dict[str, Any] = {}
    entries = read_manifest(store) if store is not None else []
    days = {e["game_date_et"]: e for e in entries if e.get("kind") == "DAY"}
    sealed_by_date: dict[str, set[str]] = {}
    for e in entries:
        if e.get("kind") == "RECORD" and e.get("version") == 1:
            sealed_by_date.setdefault(e["game_date_et"], set()).add(e["game_id"])
    for d in _dates(first, last):
        day_games = g[side & (g["game_date_et"] == d)]
        sched = sorted(day_games["game_id"])
        final = sorted(day_games[day_games["is_final"]]["game_id"])
        overdue = sorted(day_games[(~day_games["is_final"]) & (day_games["start_time_utc"] + pd.Timedelta(OVERDUE_AFTER) < pd.Timestamp(now))]["game_id"])
        row: dict[str, Any] = {"scheduled": len(sched), "final": len(final), "overdue_not_final": overdue}
        past = d < now.astimezone(UTC).strftime("%Y-%m-%d")
        if overdue:
            problems.append(f"INCOMPLETE {d}: scheduled games not final long after their start: {overdue} (postponed or unfinished; the day stays open)")
        if store is not None:
            day = days.get(d)
            row["closed"] = day is not None
            if sched and past and day is None and d <= through:
                problems.append(f"OPEN DAY {d}: {len(sched)} scheduled game(s) and no DAY entry (a skipped or incomplete day)")
            if day is not None and sorted(day["scheduled_game_ids"]) != sched:
                problems.append(f"DRIFT {d}: the archive's schedule for this closed day now differs from the DAY entry "
                                f"(added {sorted(set(sched) - set(day['scheduled_game_ids']))}, removed {sorted(set(day['scheduled_game_ids']) - set(sched))})")
            extra = sorted(sealed_by_date.get(d, set()) - set(sched))
            if extra:
                problems.append(f"EXTRA {d}: sealed game id(s) the schedule does not list for this date: {extra}")
            if day is not None:
                unsealed = sorted(set(final) - set(day["sealed_game_ids"]) - set(day["missing_pregame_game_ids"]))
                if unsealed:
                    problems.append(f"UNSEALED {d}: final scheduled game(s) neither sealed nor declared missing: {unsealed}")
        rows[d] = row
    # boundary games: eligibility depends on which snapshot of the start time is believed
    if "first_start_seen" in g.columns:
        moved = g[(g["first_start_seen"] < fz) != (g["start_time_utc"] < fz)]
        if len(moved):
            problems.append(f"BOUNDARY: start time moved across the freeze instant for game(s) {sorted(moved['game_id'])}: eligibility needs an explicit owner decision")
    # results whose game id the schedule does not know (an eligible game the schedule missed would otherwise vanish silently)
    if results is None:
        results = read_kind(archive, "results")
    results = results.copy()
    results["game_id"] = results["game_id"].astype(str)
    known = set(g_all["game_id"])
    window_files = tuple(f"dt={x}" for x in _dates(first, last))
    orphans = sorted({a for a, f in zip(results["game_id"], results["_file"].astype(str), strict=True) if a not in known and any(w in f for w in window_files)})
    if orphans:
        problems.append(f"ORPHAN RESULT: result row(s) with no schedule row on/after {first}: {orphans}")
    # a source revision of a final score AFTER the game was sealed must not be absorbed silently: it needs an explicit, versioned correction
    for gid, e1 in {e["game_id"]: e for e in entries if e.get("kind") == "RECORD" and e.get("version") == 1}.items():
        rr = results[results["game_id"] == gid].sort_values("_observed_at_utc")
        if rr.empty:
            continue
        sealed_at = pd.Timestamp(e1["sealed_utc"])
        at_seal = rr[pd.to_datetime(rr["_observed_at_utc"], utc=True) <= sealed_at]
        after = rr[pd.to_datetime(rr["_observed_at_utc"], utc=True) > sealed_at]
        if at_seal.empty or after.empty:
            continue
        cols = [c for c in ("home_final", "away_final", "last_period_type") if c in rr.columns]
        if (after[cols].astype(str).drop_duplicates().values.tolist() != [at_seal[cols].astype(str).iloc[-1].tolist()]):
            later_corr = any(e.get("kind") == "RECORD" and e["game_id"] == gid and e["version"] > 1 and pd.Timestamp(e["sealed_utc"]) > pd.Timestamp(after["_observed_at_utc"].iloc[-1]) for e in entries)
            if not later_corr:
                problems.append(f"RESULT REVISED {gid}: the source result changed after the game was sealed and no later versioned correction exists (use GAME_ID@VERSION with SOURCE_SCORE_REVISED)")
    return {"through": through, "window": "DEVELOPMENT" if dev_window else "PROSPECTIVE", "dates": rows, "problems": problems, "warnings": warnings, "ok": not problems}


def open_days_before(archive: Path, date: str, store: Path, now: datetime | None = None, games: pd.DataFrame | None = None,
                     results: pd.DataFrame | None = None) -> list[str]:
    """Used by the sealing path to fail closed: dates strictly before ``date`` that have scheduled games but no DAY entry."""
    prev = (datetime.fromisoformat(date) - timedelta(days=1)).strftime("%Y-%m-%d")
    if prev < FIRST_PROSPECTIVE_DATE_ET:
        return []
    rep = schedule_audit(archive, prev, store=store, now=now, games=games, results=results if results is not None else pd.DataFrame({"game_id": [], "_file": [], "_observed_at_utc": []}))
    return [p for p in rep["problems"] if p.startswith(("OPEN DAY", "INCOMPLETE", "DRIFT", "EXTRA", "UNSEALED", "BOUNDARY", "RESULT REVISED", "ORPHAN"))]


def nhl_api_crosscheck(first: str, last: str, scheduled_by_date: dict[str, list[str]]) -> list[str]:  # pragma: no cover - needs the network
    """Compare the archive's scheduled game ids (regular season) with api-web.nhle.com/v1/schedule/<date> for each date. Run locally; prints ids only."""
    import httpx

    out: list[str] = []
    for d in _dates(first, last):
        r = httpx.get(f"https://api-web.nhle.com/v1/schedule/{d}", timeout=30)
        r.raise_for_status()
        api = sorted(str(x["id"]) for w in r.json().get("gameWeek", []) if w.get("date") == d for x in w.get("games", []) if x.get("gameType") == 2)
        mine = sorted(scheduled_by_date.get(d, []))
        if api != mine:
            out.append(f"{d}: NHL API lists {api}, archive lists {mine}")
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--archive", type=Path, required=True)
    ap.add_argument("--through", required=True)
    ap.add_argument("--store", type=Path)
    ap.add_argument("--dev-window", action="store_true")
    ap.add_argument("--nhl-api", action="store_true", help="also compare with the live NHL API (needs network; run locally)")
    a = ap.parse_args(argv)
    rep = schedule_audit(a.archive, a.through, store=a.store, dev_window=a.dev_window)
    if a.nhl_api:
        from nhl_edge.market_audit.games import build_games

        g = build_games(a.archive)
        g = g[g["season_type"] == "regular"]
        by = {d: sorted(g[g["game_date_et"] == d]["game_id"].astype(str)) for d in rep["dates"]}
        diffs = nhl_api_crosscheck(min(rep["dates"]), max(rep["dates"]), by)
        rep["problems"] += [f"NHL API MISMATCH {x}" for x in diffs]
        rep["ok"] = not rep["problems"]
    print(json.dumps(rep, indent=1, default=str))
    return 0 if rep["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
