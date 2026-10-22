"""Unattended daily reconciliation of the sealed prospective ledger (RESEARCH_ONLY). Encrypt-only: like ``runner`` it can seal but never read back.

``reconcile`` brings the ledger up to date in ONE idempotent pass and decides everything mechanically, from public schedule/results facts and fixed, hash-committed
rules (``PROTOCOL_RULES``). It never needs a human for the routine cases:

* **missed days** -- every date from the first prospective date through ``--through`` that has scheduled games and no DAY entry is processed in ascending order (bounded
  per run; the next run continues), so a skipped run, a retry or a re-run all converge to the same ledger;
* **source revisions** -- a sealed game whose final score was revised in the archive is re-derived as the next versioned correction (reason SOURCE_SCORE_REVISED; earlier
  versions stay; at most 3 versions per game; at most 10 corrections per run);
* **postponed / cancelled games** -- a scheduled game still listed on its date and not final 14 days after its start is excluded from its day (POSTPONED_OR_CANCELLED);
  a game whose scheduled start moved across the freeze instant is excluded (START_TIME_BOUNDARY). Both rules depend only on the schedule, never on an outcome; a game
  that is merely late (< 14 days) makes the day WAIT, which is normal and raises no alert;
* **model integrity** -- the V1 distribution is regenerated bit-exactly from the archived seeds; any difference, or a change of the frozen C1 parameters, means the model
  code drifted and the run is BLOCKED (nothing further is sealed) instead of recording forecasts from a different model.

Everything else (schedule drift after closing, an extra id, an unsealed final game, an orphan result, a missing pregame forecast for a whole day, a game excluded after it
was sealed, too many corrections) is a genuine exception: status BLOCKED, whatever was safely sealed before it is kept, and the workflow raises ONE deduplicated alert.
The summary printed and uploaded is outcome-free: statuses, counts and game ids of public schedule facts only.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
from collections.abc import Callable
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import pandas as pd

from nhl_edge.sealed_ledger import PROTOCOL_RULES
from nhl_edge.sealed_ledger.audit import (
    FIRST_PROSPECTIVE_DATE_ET,
    _dates,
    boundary_games,
    load_orphan_allowlist,
    open_days_before,
    results_asof,
    revised_games,
    schedule_audit,
)
from nhl_edge.sealed_ledger.core import read_manifest
from nhl_edge.sealed_ledger.seal import SealedStore, SealError

MAX_DATES_PER_RUN = 14
MAX_CORRECTIONS_PER_RUN = 10
MAX_VERSIONS = 3  # PROTOCOL_RULES["source_revision_policy"]
AUTO_EXCLUDE_AFTER = timedelta(days=int(PROTOCOL_RULES["unfinished_game_exclusion_after_days"]))
REPRODUCTION_TOLERANCE = 1e-9
C1_PARAMS_FILE = "docs/research/nhl-model-improvement/data/cal_experiments.json"


def c1_params_sha256(repo: Path) -> str:
    p = json.loads((Path(repo) / C1_PARAMS_FILE).read_text())["c1_frozen_all_wf"]
    return hashlib.sha256(json.dumps(p, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _blocked(summary: dict[str, Any], code: str, detail: str) -> None:
    summary["blocked"].append({"code": code, "detail": detail[:400]})


def reconcile(archive: Path, repo: Path, store: Path, recipients: Path, *, through: str, now: datetime | None = None, dry_run: bool = False, run_id: str = "",
              code_sha: str = "", build_rows_fn: Callable[..., tuple[list[dict[str, Any]], dict[str, Any]]] | None = None, games: pd.DataFrame | None = None,
              results: pd.DataFrame | None = None, max_dates: int = MAX_DATES_PER_RUN, check_c1: bool = True) -> dict[str, Any]:
    """One idempotent pass. ``dry_run`` works on a throw-away copy of the store and reports what WOULD be sealed. The test hooks (``build_rows_fn``, ``games``,
    ``results``) default to the real derivation and the archive."""
    from nhl_edge.market_audit.games import build_games, read_kind

    now = now or datetime.now(UTC)
    store = Path(store)
    tmp: Path | None = None
    if dry_run:
        tmp = Path(tempfile.mkdtemp(prefix="reconcile_dry_"))
        shutil.copytree(store, tmp / "store")
        store = tmp / "store"
    summary: dict[str, Any] = {"mode": "DRY_RUN" if dry_run else "RECONCILE", "through": through, "status": "IDLE", "dates_closed": [], "games_sealed": 0, "corrections": [],
                               "exclusions": [], "waiting": [], "blocked": [], "reproduction_max_abs_diff": None}
    try:
        before = len(read_manifest(store))
        if check_c1 and c1_params_sha256(repo) != PROTOCOL_RULES["c1_frozen_params_sha256"]:
            _blocked(summary, "C1_PARAMS_CHANGED", "the frozen challenger C1 parameters differ from the hash committed in the protocol rules")
            summary["status"] = "BLOCKED"
            return _finish(summary, store, before)
        if build_rows_fn is None:
            from nhl_edge.model_research import daily

            build_rows_fn = daily.build_rows
        st = SealedStore(store, recipients, run_id=run_id, code_sha=code_sha, create=False)
        g_all = (build_games(archive) if games is None else games.copy())
        g_all["game_id"] = g_all["game_id"].astype(str)
        res = read_kind(archive, "results") if results is None else results
        asof = results_asof(res) if res is not None and not res.empty else None
        allow = load_orphan_allowlist(repo)
        start_of = dict(zip(g_all["game_id"], pd.to_datetime(g_all["start_time_utc"], utc=True), strict=True))
        boundary = boundary_games(g_all)

        # ---- A. source revisions of sealed games -> versioned corrections ------------------------------------------------------------------------------------------
        revised = revised_games(st.entries, res)
        by_date: dict[str, list[dict[str, Any]]] = {}
        for r in revised:
            by_date.setdefault(r["date"], []).append(r)
        n_corr = 0
        for d in sorted(by_date):
            todo = by_date[d][: max(0, MAX_CORRECTIONS_PER_RUN - n_corr)]
            if len(todo) < len(by_date[d]) or n_corr >= MAX_CORRECTIONS_PER_RUN:
                _blocked(summary, "TOO_MANY_CORRECTIONS", f"more than {MAX_CORRECTIONS_PER_RUN} revised games in one run (continues next run if legitimate)")
                break
            if any(r["version"] >= MAX_VERSIONS for r in todo):
                _blocked(summary, "CORRECTION_LIMIT", f"a game on {d} already has {MAX_VERSIONS} versions and was revised again: " + str([r["game_id"] for r in todo if r["version"] >= MAX_VERSIONS]))
                break
            try:
                rows, info = build_rows_fn(archive, d, repo)
            except Exception as e:  # noqa: BLE001 - type only: a derivation error message can echo row values
                _blocked(summary, "DERIVATION_FAILED", f"row derivation raised {type(e).__name__} for {d}")
                break
            drift = info.get("reproduction_max_abs_diff")
            if drift is not None and drift > REPRODUCTION_TOLERANCE:
                _blocked(summary, "MODEL_DRIFT", f"V1 regeneration differs from the archive on {d}")
                break
            sealed_ids = set(st.sealed_versions())
            rows = [x for x in rows if str(x["game_id"]) in sealed_ids]  # never let a correction run seal a game that was never sealed (e.g. an excluded one)
            have = {str(x["game_id"]) for x in rows}
            if not {r["game_id"] for r in todo} <= have:
                _blocked(summary, "CANNOT_REDERIVE", f"revised game(s) on {d} cannot be re-derived: {sorted({r['game_id'] for r in todo} - have)}")
                break
            try:
                st.seal_rows(rows, correct={r["game_id"]: r["version"] for r in todo}, reason="SOURCE_SCORE_REVISED", source_asof=asof)
            except SealError as e:
                _blocked(summary, "CORRECTION_REFUSED", str(e))
                break
            n_corr += len(todo)
            summary["corrections"] += [{"game_id": r["game_id"], "from_version": r["version"], "date": d} for r in todo]

        # ---- B. missed / open days, ascending ------------------------------------------------------------------------------------------------------------------
        if not summary["blocked"]:
            excluded_global = {x for e in st.entries if e["kind"] == "DAY" for x in e.get("excluded_game_ids", [])}
            closed = {e["game_date_et"] for e in st.entries if e["kind"] == "DAY"}
            reg = g_all[(g_all["season_type"] == "regular") & (pd.to_datetime(g_all["start_time_utc"], utc=True) >= pd.Timestamp(_freeze()))]
            open_dates = [d for d in _dates(FIRST_PROSPECTIVE_DATE_ET, through) if d not in closed and len(reg[(reg["game_date_et"] == d) & ~reg["game_id"].isin(excluded_global)])]
            for d in open_dates[:max_dates]:
                gaps = open_days_before(archive, d, store, now=now, games=g_all, results=res if res is not None else pd.DataFrame(), orphan_allowlist=allow)
                if gaps:
                    _blocked(summary, "EARLIER_DAY_NOT_CLEAN", "; ".join(gaps[:3]))
                    break
                try:
                    rows, info = build_rows_fn(archive, d, repo)
                except Exception as e:  # noqa: BLE001 - type only
                    _blocked(summary, "DERIVATION_FAILED", f"row derivation raised {type(e).__name__} for {d}: earlier days in this run were kept")
                    break
                drift = info.get("reproduction_max_abs_diff")
                if drift is not None:
                    summary["reproduction_max_abs_diff"] = max(drift, summary["reproduction_max_abs_diff"] or 0.0)
                    if drift > REPRODUCTION_TOLERANCE:
                        _blocked(summary, "MODEL_DRIFT", f"V1 regeneration differs from the archive on {d}: the model code is not the frozen one")
                        break
                sched = sorted(set(info["scheduled_game_ids"]) - excluded_global)
                final = set(info["final_game_ids"]) - excluded_global
                if not sched:
                    continue
                unfinished = set(sched) - final
                # a game is "not played" only if the results collector was demonstrably alive AFTER the 14-day mark (some results observation at or after start + 14 days):
                # otherwise "no result" may just mean the collector was down, and an exclusion cannot be undone
                asof_ts = pd.Timestamp(asof) if asof else None
                overdue = {gid for gid in unfinished if gid in start_of and start_of[gid] + AUTO_EXCLUDE_AFTER < pd.Timestamp(now) and asof_ts is not None
                           and asof_ts >= start_of[gid] + AUTO_EXCLUDE_AFTER}
                bnd = set(sched) & boundary
                exclude = overdue | bnd
                reason = None if not exclude else ("OTHER_DOCUMENTED" if overdue and bnd else "POSTPONED_OR_CANCELLED" if overdue else "START_TIME_BOUNDARY")
                waiting = sorted(unfinished - exclude)
                if sched and info["games_with_pregame_forecast"] == 0 and final and not (set(sched) <= exclude):
                    _blocked(summary, "NO_PREGAME_FORECAST", f"no scheduled game on {d} has a pregame forecast (incomplete archive fetch?)")
                    break
                rows_to_seal = [r for r in rows if str(r["game_id"]) not in exclude and str(r["game_id"]) not in excluded_global]
                try:
                    out = st.seal_rows(rows_to_seal, source_asof=asof)
                    summary["games_sealed"] += out["sealed_new"]
                    if waiting:
                        summary["waiting"].append({"date": d, "game_ids": waiting})
                        break  # a later day cannot close before this one: wait (normal; the next run continues)
                    missing = sorted(set(info["missing_pregame_forecast"]) - exclude - excluded_global)
                    st.close_day(d, sched, missing, sorted(exclude), reason)
                except SealError as e:
                    _blocked(summary, "SEAL_REFUSED", f"{d}: {e}")
                    break
                summary["dates_closed"].append(d)
                if exclude:
                    summary["exclusions"].append({"date": d, "game_ids": sorted(exclude), "reason": reason})
            if len(open_dates) > max_dates and not summary["blocked"] and not summary["waiting"]:
                summary["status"] = "PARTIAL"

        # ---- C. integrity audit of what is now closed ---------------------------------------------------------------------------------------------------------------
        closed_dates = sorted(e["game_date_et"] for e in st.entries if e["kind"] == "DAY")
        if closed_dates:
            rep = schedule_audit(archive, closed_dates[-1], store=store, now=now, games=g_all, results=res if res is not None else pd.DataFrame(), orphan_allowlist=allow)
            for p in rep["problems"]:
                words = p.split(" ")
                _blocked(summary, (words[0] + ("_" + words[1].rstrip(":") if words[0] in ("OPEN", "RESULT", "ORPHAN") else "")).rstrip(":"), p)
        if summary["blocked"]:
            summary["status"] = "BLOCKED"
        elif summary["waiting"]:
            summary["status"] = "WAITING"
        elif summary["status"] != "PARTIAL":
            summary["status"] = "OK" if (summary["dates_closed"] or summary["corrections"]) else "IDLE"
        return _finish(summary, store, before)
    finally:
        if tmp is not None:
            shutil.rmtree(tmp, ignore_errors=True)


def _freeze() -> str:
    from nhl_edge.model_research import PROSPECTIVE_FREEZE_UTC

    return PROSPECTIVE_FREEZE_UTC


def _finish(summary: dict[str, Any], store: Path, before: int) -> dict[str, Any]:
    entries = read_manifest(store)
    summary["manifest_entries"] = len(entries)
    summary["head_seq"] = len(entries) - 1
    summary["head_hash"] = entries[-1]["entry_hash"] if entries else ""
    summary["changed"] = len(entries) > before
    summary["note"] = {"IDLE": "nothing to do", "OK": "ledger is up to date", "WAITING": "waiting for games that have not finished (normal)",
                       "PARTIAL": "more days remain; the next run continues", "BLOCKED": "exception: see blocked; safely sealed days were kept"}[summary["status"]]
    return summary
