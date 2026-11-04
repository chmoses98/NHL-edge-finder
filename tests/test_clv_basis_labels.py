"""Quoted-execution CLV (close mid - entry ask) must not be mistaken for selection CLV (close mid - entry mid).

An unchanged market with a bid/ask spread scores about minus half the spread as quoted-execution CLV and exactly zero
as selection CLV. No fee is part of either figure. A last-trade fallback is not a midpoint and never yields selection CLV.
"""
from __future__ import annotations

from datetime import UTC, datetime, timedelta

import pytest

from nhl_edge.settlement.engine import SettlementOutcome, SettlementRecord
from nhl_edge.timeutil import iso
from nhl_edge.workflows.evaluate import build_evaluation_row

START = datetime(2026, 10, 22, 0, 10, tzinfo=UTC)
TICKER = "KXNHLGAME-26OCT21AAABBB-AAA"


def _rec():
    return SettlementRecord(ticker=TICKER, game_id="g1", outcome=SettlementOutcome.YES, value=1.0, reason="x",
                            settled_at_utc=START + timedelta(hours=3), result_source="t", stat_correction_version=0,
                            engine_version="e", idempotency_key="k", settles_on="final")


def _pred(yes_bid, yes_ask, no_ask, p_data=0.60, p_market=0.50):
    return {"prediction_id": "p1", "predicted_at_utc": iso(START - timedelta(hours=2)),
            "market_observed_at_utc": iso(START - timedelta(hours=2)), "ticker": TICKER, "game_id": "g1",
            "market_yes_bid": yes_bid, "market_yes_ask": yes_ask, "market_no_ask": no_ask,
            "p_data_only": p_data, "p_market": p_market}


def _obs(yes_bid, yes_ask, last=None, minutes_before=20):
    return {"ticker": TICKER, "yes_bid": yes_bid, "yes_ask": yes_ask, "last_price": last,
            "_observed_at_utc": iso(START - timedelta(minutes=minutes_before))}


def test_unchanged_spread_market_zero_selection_negative_quoted_execution():
    row = build_evaluation_row(_pred(48, 52, 52), _rec(), START, [_obs(48, 52)])
    assert row["selection_clv_yes_prob"] == pytest.approx(0.0)
    assert row["selection_clv_signed"] == pytest.approx(0.0)
    assert row["quoted_execution_clv_yes_prob"] == pytest.approx(-0.02)     # mid 50 - ask 52
    assert row["clv_yes_prob"] == row["quoted_execution_clv_yes_prob"]        # legacy name unchanged
    assert row["clv_signed"] == row["quoted_execution_clv_signed"] == pytest.approx(-0.02)


def test_genuine_move_and_yes_no_mirror():
    row = build_evaluation_row(_pred(48, 52, 52), _rec(), START, [_obs(53, 57)])   # mid 50 -> 55
    assert row["selection_clv_yes_prob"] == pytest.approx(0.05)
    assert row["selection_clv_no_prob"] == pytest.approx(-0.05)
    assert row["selection_clv_signed"] == pytest.approx(0.05)                      # model favours YES
    no = build_evaluation_row(_pred(48, 52, 52, p_data=0.40), _rec(), START, [_obs(53, 57)])
    assert no["selection_clv_signed"] == pytest.approx(-0.05)                      # model favours NO


def test_last_trade_fallback_never_produces_selection_clv():
    row = build_evaluation_row(_pred(48, 52, 52), _rec(), START, [_obs(None, None, last=55)])
    assert row["close_price_source"] == "last_trade"
    assert row["selection_clv_yes_prob"] is None and row["selection_clv_signed"] is None
    assert row["clv_yes_prob"] is not None                                          # legacy behaviour preserved, labelled


def test_one_sided_entry_book_has_no_selection_clv():
    row = build_evaluation_row(_pred(None, 52, 52), _rec(), START, [_obs(48, 52)])
    assert row["selection_clv_yes_prob"] is None
