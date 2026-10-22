"""Completeness audit of the prospective ledger against the archived NHL schedule (RESEARCH_ONLY; runner-safe: reads only public schedule/result facts and the PUBLIC manifest).

    python -m nhl_edge.sealed_ledger.audit --archive A --through YYYY-MM-DD [--store S] [--dev-window]

The "authoritative historical schedule" available to the workflow is the archive's ``context/schedule`` (timestamped snapshots of the NHL schedule API) joined to the
``results`` kind. For every date from the first prospective date through ``--through`` the audit lists the scheduled regular-season games on the prospective side of the
freeze and checks, with game ids and counts only (no outcome):

* OPEN DAY: a past date with scheduled games that no DAY entry closed (a skipped or incomplete day) -- PROBLEM, so a gap can never be silently passed over;
* INCOMPLETE: a scheduled game that is not final long after its start (postponed / unfinished) -- PROBLEM until the owner EXCLUDES it from its day (public, reason-coded,
  approval-gated; only a game that is not final, or a boundary game, can be excluded; an excluded game can never be sealed) -- the only way to unblock later days;
* DRIFT: a closed day whose DAY entry no longer matches the archive's schedule for that date (a game was added or removed after closing) -- PROBLEM;
* EXTRA / UNSEALED: a sealed game the schedule does not list for that date, or a scheduled final game that is neither sealed nor declared missing -- PROBLEM;
* ORPHAN RESULT: a result row whose game id is absent from the schedule on or after the first prospective date (an eligible game the schedule missed) -- PROBLEM;
* RESULT REVISED: the source's final score of an already sealed game differs from the score in the archive snapshot the latest sealed version was derived from
  (``source_asof_utc``) -- PROBLEM until an explicit, versioned ``GAME_ID@VERSION`` correction re-derives it (a late revision is never absorbed silently; the runner skips
  sealed games). Correction runs pass ``--allow-revised`` so several revised games on different dates can be corrected one date at a time;
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


_RESULT_COLS = ["game_id", "_file", "_observed_at_utc", "home_final", "away_final", "last_period_type"]


def _empty_results() -> pd.DataFrame:
    return pd.DataFrame({c: [] for c in _RESULT_COLS})


def results_asof(results: pd.DataFrame) -> str | None:
    """The archive snapshot time: the latest observation in the local archive copy a run derives its rows from (NOT the time the record is sealed)."""
    if results is None or results.empty:
        return None
    return str(pd.to_datetime(results["_observed_at_utc"], utc=True).max().strftime("%Y-%m-%dT%H:%M:%SZ"))


def boundary_games(g_all: pd.DataFrame) -> set[str]:
    """Games first scheduled BEFORE the freeze instant whose start now lies AFTER it (their eligibility is ambiguous). A game that moved the other way is currently pre-freeze,
    i.e. in the development tier, and never enters the prospective window, so it is not a boundary case."""
    fz = pd.Timestamp(PROSPECTIVE_FREEZE_UTC)
    if "first_start_seen" not in g_all.columns:
        return set()
    return set(g_all[(g_all["first_start_seen"] < fz) & (g_all["start_time_utc"] >= fz)]["game_id"].astype(str))


def revised_games(entries: list[dict[str, Any]], results: pd.DataFrame | None) -> list[dict[str, Any]]:
    """Sealed games whose newest observed final score / period type differs from the observation in the archive snapshot their latest sealed version was derived from
    (``source_asof_utc``). Pure function of the PUBLIC manifest and the results observations: ids, versions and dates only."""
    latest: dict[str, dict[str, Any]] = {}
    for e in entries:
        if e.get("kind") == "RECORD":
            latest[e["game_id"]] = e
    if results is None or results.empty or not latest:
        return []
    results = results.copy()
    results["game_id"] = results["game_id"].astype(str)
    obs = pd.to_datetime(results["_observed_at_utc"], utc=True)
    cols = [c for c in ("home_final", "away_final", "last_period_type") if c in results.columns]
    out = []
    for gid, e in sorted(latest.items()):
        mask = results["game_id"] == gid
        if not mask.any():
            continue
        rr = results[mask].assign(_t=obs[mask]).sort_values("_t")
        asof = pd.Timestamp(e.get("source_asof_utc") or e["sealed_utc"])
        at_asof = rr[rr["_t"] <= asof]
        if at_asof.empty:
            continue
        if [str(rr.iloc[-1][c]) for c in cols] != [str(at_asof.iloc[-1][c]) for c in cols]:
            out.append({"game_id": gid, "version": e["version"], "date": e["game_date_et"]})
    return out


def schedule_audit(archive: Path, through: str, *, store: Path | None = None, dev_window: bool = False, now: datetime | None = None,
                   games: pd.DataFrame | None = None, results: pd.DataFrame | None = None, ignore_revised: bool = False,
                   orphan_allowlist: set[str] | frozenset[str] = frozenset()) -> dict[str, Any]:
    """``orphan_allowlist``: result ids the owner reviewed and approved by a merged change to research/sealed_ledger/orphan_allowlist.txt. ``games`` (build_games output) and ``results`` (every observed results row: game_id, _observed_at_utc, home_final, away_final, last_period_type, _file) may be
    injected for tests; otherwise they are read from the archive. ``ignore_revised`` is for a run whose purpose is to apply the versioned corrections."""
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
    excluded_ids = {x for e in entries if e.get("kind") == "DAY" for x in e.get("excluded_game_ids", [])}  # waived by the owner (public, reason-coded)
    sealed_by_date: dict[str, set[str]] = {}
    for e in entries:
        if e.get("kind") == "RECORD" and e.get("version") == 1:
            sealed_by_date.setdefault(e["game_date_et"], set()).add(e["game_id"])
    today = now.astimezone(UTC).strftime("%Y-%m-%d")
    for d in _dates(first, last):
        day_games = g[side & (g["game_date_et"] == d) & ~g["game_id"].isin(excluded_ids)]  # an excluded game is out of every day, even if the schedule later moves it
        sched = sorted(day_games["game_id"])
        final = sorted(day_games[day_games["is_final"]]["game_id"])
        overdue = sorted(set(day_games[(~day_games["is_final"]) & (day_games["start_time_utc"] + pd.Timedelta(OVERDUE_AFTER) < pd.Timestamp(now))]["game_id"]) - excluded_ids)
        row: dict[str, Any] = {"scheduled": len(sched), "final": len(final), "overdue_not_final": overdue}
        past = d < today
        if overdue:
            problems.append(f"INCOMPLETE {d}: scheduled games not final long after their start: {overdue} (postponed or unfinished; the day stays open until the owner excludes them)")
        if store is not None:
            day = days.get(d)
            row["closed"] = day is not None
            if sched and past and day is None and d <= through:
                problems.append(f"OPEN DAY {d}: {len(sched)} scheduled game(s) and no DAY entry (a skipped or incomplete day)")
            if day is not None:
                excl = set(day.get("excluded_game_ids", []))
                added, removed = set(sched) - set(day["scheduled_game_ids"]), (set(day["scheduled_game_ids"]) - set(sched)) - excl
                if added or removed:
                    problems.append(f"DRIFT {d}: the archive's schedule for this closed day now differs from the DAY entry (added {sorted(added)}, removed {sorted(removed)})")
                unsealed = sorted(set(final) - set(day["sealed_game_ids"]) - set(day["missing_pregame_game_ids"]) - excl)
                if unsealed:
                    problems.append(f"UNSEALED {d}: final scheduled game(s) neither sealed nor declared missing: {unsealed}")
            extra = sorted(sealed_by_date.get(d, set()) - set(sched))
            if extra:
                problems.append(f"EXTRA {d}: sealed game id(s) the schedule does not list for this date: {extra}")
        rows[d] = row
    # boundary games: eligibility depends on which snapshot of the start time is believed (resolved only by an explicit owner exclusion)
    if "first_start_seen" in g.columns:
        # only boundary games whose CURRENT date has been reached by this audit: a later-dated one is handled (excluded) when its own day is processed, never blocking earlier days
        moved = sorted((boundary_games(g[g["game_date_et"] <= last]) if not dev_window else set()) - excluded_ids)
        if moved:
            problems.append(f"BOUNDARY: start time moved across the freeze instant for game(s) {moved}: eligibility needs an explicit owner exclusion (START_TIME_BOUNDARY)")
    if results is None:
        results = read_kind(archive, "results")
    results = _empty_results() if results is None or results.empty else results.copy()
    results["game_id"] = results["game_id"].astype(str)
    obs = pd.to_datetime(results["_observed_at_utc"], utc=True) if len(results) else pd.Series([], dtype="datetime64[ns, UTC]")
    # results whose game id the schedule does not know: only ids that plausibly belong AFTER the freeze (numerically above every pre-freeze scheduled id) and that were
    # observed after it; an old game the schedule never captured is a data gap, not an eligible game, and must not wedge the loop
    pre_ids = [int(i) for i in g_all[g_all["start_time_utc"] < fz]["game_id"] if str(i).isdigit()]
    max_pre = max(pre_ids) if pre_ids else 0
    known = set(g_all["game_id"])
    orphans = sorted({a for a, t in zip(results["game_id"], obs, strict=True) if a not in known and t >= fz and (not a.isdigit() or int(a) > max_pre)} - excluded_ids - set(orphan_allowlist))
    if orphans:
        problems.append(f"ORPHAN RESULT: result row(s) with no schedule row, observed after the freeze: {orphans}")
    # a source revision of a final score AFTER the game was sealed must not be absorbed silently: it needs a versioned correction (the unattended reconcile applies it
    # automatically; the comparison point is the archive snapshot the latest sealed version was derived from, not the time it was sealed)
    for r in ([] if ignore_revised else revised_games(entries, results)):
        problems.append(f"RESULT REVISED {r['game_id']}: the source result changed after sealed version {r['version']} was derived and no later versioned correction covers it "
                        "(a correction re-derives it as the next version)")
    return {"through": through, "window": "DEVELOPMENT" if dev_window else "PROSPECTIVE", "dates": rows, "problems": problems, "warnings": warnings, "ok": not problems}


def load_orphan_allowlist(repo: Path) -> set[str]:
    p = Path(repo) / "research" / "sealed_ledger" / "orphan_allowlist.txt"
    if not p.exists():
        return set()
    return {ln.split("#")[0].strip() for ln in p.read_text().splitlines() if ln.split("#")[0].strip()}


def open_days_before(archive: Path, date: str, store: Path, now: datetime | None = None, games: pd.DataFrame | None = None, results: pd.DataFrame | None = None,
                     ignore_revised: bool = False, orphan_allowlist: set[str] | frozenset[str] = frozenset()) -> list[str]:
    """Used by the sealing path to fail closed: every audit problem for the dates before ``date`` (open, incomplete, drifted, extra, unsealed, boundary days), plus orphan
    results and revised scores of already sealed games (unless ``ignore_revised``: the run that applies the corrections)."""
    prev = (datetime.fromisoformat(date) - timedelta(days=1)).strftime("%Y-%m-%d")
    if prev < FIRST_PROSPECTIVE_DATE_ET:
        return []
    if results is None and games is not None:
        results = _empty_results()
    rep = schedule_audit(archive, prev, store=store, now=now, games=games, results=results, ignore_revised=ignore_revised, orphan_allowlist=orphan_allowlist)
    return list(rep["problems"])


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
    ap.add_argument("--allow-revised", action="store_true", help="for the run that applies versioned corrections: do not fail on revised scores")
    ap.add_argument("--nhl-api", action="store_true", help="also compare with the live NHL API (needs network; run locally)")
    a = ap.parse_args(argv)
    rep = schedule_audit(a.archive, a.through, store=a.store, dev_window=a.dev_window, ignore_revised=a.allow_revised)
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
    from nhl_edge.sealed_ledger.core import run_scrubbed

    sys.exit(run_scrubbed(main, name="SCHEDULE AUDIT"))
