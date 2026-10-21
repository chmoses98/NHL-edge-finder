"""Capture-coverage and independent-observation accounting (Phase A).

"Usable pregame snapshot" is defined ONCE here and used everywhere downstream:

    a quote observation of a game-scoped contract that
      (1) is two-sided (yes_bid and yes_ask both present),
      (2) is on an ``active`` board row,
      (3) was fully AVAILABLE (``available_at`` = tick + capture-window lag) at or before the scheduled start.

Counts are reported at three honest levels -- change events, carry-forward tick observations, and independent GAMES --
because only the last is an independent observation of anything.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


def prepare_events(ev: pd.DataFrame, cm: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    e = ev.merge(cm[["ticker", "game_id", "family", "kind", "scope", "period", "threshold", "subject_team_id"]], on="ticker", how="inner")
    e = e.merge(games[["game_id", "start_time_utc", "is_final", "game_date_et"]], on="game_id", how="inner")
    e["mins_to_start"] = (e["start_time_utc"] - e["observed_at"]).dt.total_seconds() / 60.0
    e["two_sided"] = e["yes_bid"].notna() & e["yes_ask"].notna()
    e["usable_pregame"] = e["two_sided"] & (e["status"] == "active") & (e["available_at"] <= e["start_time_utc"])
    return e


def last_pregame_quote(e: pd.DataFrame, legacy: bool = False) -> pd.DataFrame:
    """Per ticker, the pregame state at puck drop, then tested for usability.

    State is the LAST event available before the start; a one-sided / inactive last state is a missing quote, never an older two-sided one
    (HISTORICAL_RECONSTRUCTION rule 2, which ``efficiency.build_live_panel`` already follows). ``legacy=True`` reproduces the v1.0 behaviour, which filtered
    to usable states FIRST and so credited 3,152 contracts with an older two-sided quote (data review D1: usable contracts 27,359 -> 24,207).
    """
    if legacy:
        u = e[e["usable_pregame"]].sort_values(["ticker", "observed_at"])
        return u.groupby("ticker", as_index=False).tail(1)
    pre = e[e["available_at"] <= e["start_time_utc"]].sort_values(["ticker", "observed_at"])
    last = pre.groupby("ticker", as_index=False).tail(1)
    return last[last["usable_pregame"]]


def coverage_report(ev: pd.DataFrame, cm: pd.DataFrame, games: pd.DataFrame, ticks_m: pd.DataFrame, ticks_b: pd.DataFrame,
                    book_ev: pd.DataFrame, outcomes: pd.DataFrame) -> dict[str, Any]:
    e = prepare_events(ev, cm, games)
    fin = games[games["is_final"]]
    rep: dict[str, Any] = {}

    tm = ticks_m.sort_values("observed_at")
    gaps = tm["observed_at"].diff().dt.total_seconds().dropna() / 60.0
    rep["ticks"] = {
        "n_market_ticks": int(len(tm)), "n_checkpoint": int((tm["encoding"] == "checkpoint").sum()), "n_delta": int((tm["encoding"] == "delta").sum()),
        "first": tm["observed_at"].min().isoformat(), "last": tm["observed_at"].max().isoformat(),
        "gap_minutes": {k: round(float(gaps.quantile(q)), 1) for k, q in (("p10", .1), ("p50", .5), ("p90", .9), ("p99", .99), ("max", 1.0))},
        "n_gaps_over_30min": int((gaps > 30).sum()), "n_gaps_over_60min": int((gaps > 60).sum()),
        "n_orderbook_ticks": int(len(ticks_b)), "books_per_tick": {"min": int(ticks_b["n_books"].min()), "median": float(ticks_b["n_books"].median()),
                                                                   "max": int(ticks_b["n_books"].max())},
        "orderbook_fetch_errors": int(ticks_b["n_errors"].sum()),
    }

    # ---- per-game pregame snapshot depth ---------------------------------------------------------
    rows = []
    for g in fin.itertuples():
        start = np.datetime64(g.start_time_utc.tz_convert("UTC").tz_localize(None))
        tt = tm["observed_at"].dt.tz_convert("UTC").dt.tz_localize(None).to_numpy()
        pre = tt[tt < start]
        last_lag = float((start - pre.max()) / np.timedelta64(1, "m")) if len(pre) else np.nan
        sub = e[e["game_id"] == g.game_id]
        first_listed = sub["observed_at"].min()
        rows.append({
            "game_id": g.game_id, "n_contracts": int(sub["ticker"].nunique()),
            "n_pregame_ticks_24h": int(((start - pre) <= np.timedelta64(24 * 60, "m")).sum()),
            "n_pregame_ticks_60m": int(((start - pre) <= np.timedelta64(60, "m")).sum()),
            "last_pregame_tick_lag_min": last_lag,
            "first_listed_hours_before": float((g.start_time_utc - first_listed).total_seconds() / 3600) if pd.notna(first_listed) else np.nan,
            "n_usable_pregame_events": int(sub["usable_pregame"].sum()),
        })
    pg = pd.DataFrame(rows)
    rep["games"] = {
        "scheduled_in_archive": int(len(games)), "final": int(len(fin)), "final_with_player_events": int(sum(1 for _ in fin.itertuples())),
        "final_with_any_pregame_usable_quote": int((pg["n_usable_pregame_events"] > 0).sum()),
        "last_pregame_tick_lag_min": {k: round(float(pg["last_pregame_tick_lag_min"].quantile(q)), 1)
                                      for k, q in (("p10", .1), ("p50", .5), ("p90", .9), ("max", 1.0))},
        "pregame_ticks_within_60m": {k: float(pg["n_pregame_ticks_60m"].quantile(q)) for k, q in (("min", 0), ("p50", .5), ("max", 1.0))},
        "first_listed_hours_before_start": {k: round(float(pg["first_listed_hours_before"].quantile(q)), 1)
                                            for k, q in (("p10", .1), ("p50", .5), ("p90", .9))},
    }

    # ---- contracts / usable snapshots by family (final games only) -------------------------------------
    ef = e[e["is_final"]]
    last = last_pregame_quote(ef)
    oc = outcomes.set_index("ticker")["outcome"]
    fam = []
    for family, sub in ef.groupby("family"):
        tickers = sub["ticker"].unique()
        lp = last[last["family"] == family]
        o = oc.reindex(tickers)
        fam.append({
            "family": family, "scope": sub["scope"].iloc[0], "contracts": int(len(tickers)), "games": int(sub["game_id"].nunique()),
            "usable_pregame_change_events": int(sub["usable_pregame"].sum()), "contracts_with_usable_pregame_quote": int(lp["ticker"].nunique()),
            "decided_YES_NO": int(o.isin(["YES", "NO"]).sum()), "void_or_unscored": int((~o.isin(["YES", "NO"])).sum()),
            "decided_with_pregame_quote": int(o.reindex(lp["ticker"]).isin(["YES", "NO"]).sum()),
        })
    rep["by_family"] = fam

    # ---- carry-forward tick observations (assumes a listed contract stays on the board until last seen) ----
    rep["totals"] = {
        "unique_game_scoped_contracts_in_archive": int(cm["ticker"].nunique()),
        "contracts_on_final_games": int(ef["ticker"].nunique()),
        "contracts_on_final_games_with_usable_pregame_quote": int(last["ticker"].nunique()),
        "decided_contracts_on_final_games": int(oc.reindex(ef["ticker"].unique()).isin(["YES", "NO"]).sum()),
        "decided_with_usable_pregame_quote": int(oc.reindex(last["ticker"]).isin(["YES", "NO"]).sum()),
        "independent_games_final": int(len(fin)),
        "usable_pregame_change_events": int(ef["usable_pregame"].sum()),
    }

    # ---- orderbook coverage -------------------------------------------------------------------------
    bk = book_ev.merge(cm[["ticker", "game_id", "family"]], on="ticker", how="left").merge(
        games[["game_id", "start_time_utc"]], on="game_id", how="left")
    bk["mins_to_start"] = (bk["start_time_utc"] - bk["observed_at"]).dt.total_seconds() / 60.0
    pre_b = bk[(bk["observed_at"] + pd.Timedelta(seconds=105)) <= bk["start_time_utc"]]
    cov = []
    for family, sub in pre_b.groupby("family", dropna=False):
        cov.append({"family": str(family), "tickers_with_any_pregame_book": int(sub["ticker"].nunique()), "book_change_events": int(len(sub))})
    rep["orderbook_coverage_by_family"] = cov
    last_t = last["ticker"].unique()
    have_book = set(pre_b["ticker"].unique())
    rep["orderbook_coverage_of_usable_contracts"] = {
        "usable_contracts": int(len(last_t)), "with_any_pregame_book": int(sum(t in have_book for t in last_t)),
        "pct": round(100.0 * sum(t in have_book for t in last_t) / max(len(last_t), 1), 1)}
    return rep
