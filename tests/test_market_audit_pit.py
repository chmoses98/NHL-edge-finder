"""Point-in-time and executability regression tests for the market audit."""

from __future__ import annotations

import numpy as np
import pandas as pd

from nhl_edge.market_audit.efficiency import build_live_panel
from nhl_edge.market_audit.execution import walk
from nhl_edge.market_audit.matchup_study import ewma_rate

T0 = pd.Timestamp("2026-10-20 23:00", tz="UTC")


def _ev(rows):
    df = pd.DataFrame(rows, columns=["ticker", "observed_at", "yes_bid", "yes_ask", "status"])
    df["observed_at"] = pd.to_datetime(df["observed_at"], utc=True)
    df["available_at"] = df["observed_at"] + pd.Timedelta(seconds=45)
    df["yes_bid_size"], df["yes_ask_size"], df["volume"] = 10.0, 10.0, 1.0
    return df


def _frames(events):
    cm = pd.DataFrame({"ticker": ["T"], "game_id": ["g"], "family": ["game_total"], "kind": ["total"], "period": ["FULL"], "threshold": [5.5],
                       "subject_team_id": [np.nan], "player_team_id": [np.nan], "is_tie_leg": [False]})
    games = pd.DataFrame({"game_id": ["g"], "start_time_utc": [T0], "game_date_et": ["2026-10-20"], "home_team_id": [1], "is_final": [True]})
    oc = pd.DataFrame({"ticker": ["T"], "outcome": ["YES"]})
    st = pd.DataFrame({"ticker": ["T"], "last_seen": [T0 + pd.Timedelta(hours=3)]})
    return events, cm, games, oc, st


def test_quote_that_finishes_capturing_after_the_cut_is_not_used():
    # stamped 59 min before start (cut = T-60 => stamp 61 min before is fine; 59 min is not): available_at = stamp + 45 s > cut
    ev = _ev([("T", "2026-10-20 21:30:00", 40, 44, "active"), ("T", "2026-10-20 22:00:20", 10, 14, "active")])
    p = build_live_panel(*_frames(ev), horizons_min=(60,))
    assert len(p) == 1 and p.iloc[0]["yes_bid"] == 0.40  # the later quote (available 22:01:05 > cut 22:00) is excluded


def test_one_sided_state_at_the_cut_is_missing_not_backfilled():
    ev = _ev([("T", "2026-10-20 21:00:00", 40, 44, "active"), ("T", "2026-10-20 21:30:00", np.nan, 44, "active")])
    assert build_live_panel(*_frames(ev), horizons_min=(60,)).empty


def test_inactive_state_at_the_cut_is_missing():
    ev = _ev([("T", "2026-10-20 21:00:00", 40, 44, "active"), ("T", "2026-10-20 21:30:00", 40, 44, "closed")])
    assert build_live_panel(*_frames(ev), horizons_min=(60,)).empty


def test_quote_age_is_never_negative():
    ev = _ev([("T", f"2026-10-20 {h:02d}:{m:02d}:00", 40, 44, "active") for h in (20, 21, 22) for m in (0, 20, 40)])
    p = build_live_panel(*_frames(ev), horizons_min=(1440, 360, 60, 10, 0))
    assert (p["quote_age_min"] >= 0).all()


def test_ewma_features_ignore_same_day_and_later_games():
    rows = pd.DataFrame({"date": pd.to_datetime(["2025-10-01", "2025-10-20", "2025-10-25"]), "team_id": [1, 1, 1], "v": [2.0, 100.0, 100.0]})
    asof = pd.Timestamp("2025-10-20")
    assert ewma_rate(rows, asof, 1, "v", 0.0) < 3.0  # neither the 20th itself nor the 25th leaks in


def test_book_walk_takes_best_prices_first_and_reports_partial_fills():
    no_bids = [[57, 100.0], [56, 50.0], [50, 1000.0]]  # buying YES hits NO bids: costs 43c, then 44c, then 50c
    got, vwap = walk(no_bids, 120)
    assert got == 120 and abs(vwap - (100 * 43 + 20 * 44) / 120) < 1e-9
    got2, _ = walk([[57, 10.0]], 50)
    assert got2 == 10.0  # only what is visible fills
