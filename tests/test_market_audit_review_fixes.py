"""Regression tests for data-review findings D1 (coverage 'usable' ordering), D2 (quiet-market age rule), D6 (a discriminating availability-lag test), D7 (stale step skipping)."""

from __future__ import annotations

import pandas as pd

from nhl_edge.market_audit.coverage import last_pregame_quote
from nhl_edge.market_audit.efficiency import build_live_panel
from tests.test_market_audit_pit import _ev, _frames


def test_quote_stamped_before_the_cut_but_available_after_it_is_excluded():
    # stamp 21:59:30 < cut 22:00:00 but available_at = stamp + 45 s = 22:00:15 > cut: a mutant using observed_at or a zero lag would USE it
    ev = _ev([("T", "2026-10-20 21:30:00", 40, 44, "active"), ("T", "2026-10-20 21:59:30", 10, 14, "active")])
    p = build_live_panel(*_frames(ev), horizons_min=(60,))
    assert len(p) == 1 and p.iloc[0]["yes_bid"] == 0.40


def test_quote_stamped_just_early_enough_is_used():
    ev = _ev([("T", "2026-10-20 21:30:00", 40, 44, "active"), ("T", "2026-10-20 21:59:10", 10, 14, "active")])  # available 21:59:55 <= cut
    p = build_live_panel(*_frames(ev), horizons_min=(60,))
    assert len(p) == 1 and p.iloc[0]["yes_bid"] == 0.10


def test_quiet_market_is_dropped_by_the_legacy_age_rule_but_kept_by_the_tick_rule():
    ev = _ev([("T", "2026-10-20 18:00:00", 40, 44, "active")])  # one change four hours before the cut; the market then sat still
    legacy = build_live_panel(*_frames(ev), horizons_min=(60,))
    tick = build_live_panel(*_frames(ev), horizons_min=(60,), age_rule="tick")
    assert legacy.empty and len(tick) == 1
    assert tick.iloc[0]["quote_age_min"] > 60  # the age is still reported, only the filter changes


def test_coverage_uses_the_last_state_then_tests_usability():
    t0 = pd.Timestamp("2026-10-20 23:00:00", tz="UTC")
    e = pd.DataFrame({"ticker": ["T", "T"], "observed_at": [t0 - pd.Timedelta(hours=9), t0 - pd.Timedelta(minutes=5)],
                      "available_at": [t0 - pd.Timedelta(hours=9), t0 - pd.Timedelta(minutes=5)], "start_time_utc": [t0, t0], "usable_pregame": [True, False]})
    assert last_pregame_quote(e).empty  # the later one-sided state is a missing quote at the drop
    assert len(last_pregame_quote(e, legacy=True)) == 1 and last_pregame_quote(e, legacy=True).iloc[0]["observed_at"] == t0 - pd.Timedelta(hours=9)
