"""Tests for the SHADOW market-expression engine and the statistics helpers it depends on."""

from __future__ import annotations

import numpy as np
import pandas as pd

from nhl_edge.market_audit.efficiency import cluster_ratio_ci, taker_fee
from nhl_edge.market_audit.expression_engine import (
    Candidate,
    build_card,
    evaluate,
    fee,
    max_entry_price,
    research_stake,
)
from nhl_edge.market_audit.hypotheses import bh_adjust, classify


def cand(**kw):
    base = dict(ticker="T1", title="Over 5.5", family="game_total", side="yes", ask=0.50, mid_yes=0.495, p_model=0.60, factor="HIGH_SCORING", survival=0.7)
    base.update(kw)
    return Candidate(**base)


def test_fee_matches_router_verified_taker_formula():
    # 88.13 contracts at $0.55 -> the router recorded fees_paid 1.5269 on the real fill
    assert abs(88.13 * fee(0.55) - 1.5269) < 5e-4
    assert abs(float(taker_fee(0.55)) - fee(0.55)) < 1e-12


def test_max_entry_price_is_the_breakeven_price():
    for p in (0.3, 0.5, 0.8):
        x = max_entry_price(p)
        assert abs(x + fee(x) - p) < 1e-9
    assert max_entry_price(0.4) < max_entry_price(0.6)


def test_strict_policy_passes_when_no_family_is_validated():
    card = build_card("G", [cand(), cand(ticker="T2", side="no", title="Over 5.5", ask=0.52)], {"game_total": 0.9}, {"game_total": "INCONCLUSIVE"})
    assert card["decision"] == "PASS" and card["selected"] == []
    assert any("no VALIDATED" in r for r in card["best_rejected"][0]["reject_reasons"])


def test_model_gets_zero_weight_so_probability_equals_market():
    r = evaluate(cand(), w=0.0, family_class="VALIDATED")
    assert r["estimated_probability"] == 0.495 and r["model_weight"] == 0.0
    assert r["net_ev_per_contract"] < 0  # half spread + fee: negative EV by construction


def test_goal_scorer_never_recommended_even_if_gate_waived():
    c = cand(family="player_goals", ask=0.31, mid_yes=0.30, p_model=0.60)
    r = evaluate(c, w=1.0, family_class="VALIDATED", policy="research_unvalidated")
    assert not r["eligible"] and any("goal-scorer" in x for x in r["reject_reasons"])


def test_correlated_expressions_are_not_double_counted():
    a = cand(ticker="A", ask=0.60, mid_yes=0.60, p_model=0.80, factor="LOW_SCORING")
    b = cand(ticker="B", ask=0.60, mid_yes=0.60, p_model=0.80, factor="LOW_SCORING")
    card = build_card("G", [a, b], {"game_total": 0.9}, {"game_total": "VALIDATED"}, policy="strict")
    assert len(card["selected"]) == 1


def test_fragile_and_thin_candidates_are_rejected():
    r = evaluate(cand(ask=0.62, mid_yes=0.6, survival=0.3, depth_contracts=5), w=1.0, family_class="VALIDATED")
    assert not r["eligible"] and len(r["reject_reasons"]) >= 2


def test_stake_zero_without_positive_lower_bound_and_capped_by_research_limit():
    assert research_stake(-0.01, 0.4, 0.5) == 0.0
    assert research_stake(0.2, 0.95, 0.30) <= 5.0


def test_bh_adjust_monotone_and_bounded():
    q = bh_adjust({"a": 0.001, "b": 0.02, "c": 0.5})
    assert q["a"] <= q["b"] <= q["c"] <= 1.0


def test_classify_requires_live_validation_and_flags_untestable():
    assert classify({"HIST_DISC": {"roi": None, "n_games": 0}}, None) == "UNTESTABLE"
    tier = {"roi": 0.05, "n_games": 150, "roi_lo90": 0.01, "roi_hi95": 0.2, "roi_slip_1c": 0.03}
    assert classify({"LIVE": tier, "HIST_HOLD": dict(tier)}, 0.05) == "VALIDATED"
    assert classify({"LIVE": tier, "HIST_HOLD": dict(tier)}, 0.5) == "PROMISING"
    neg = {"roi": -0.05, "n_games": 150, "roi_lo90": -0.1, "roi_hi95": -0.01, "roi_slip_1c": -0.06}
    assert classify({"LIVE": neg, "HIST_HOLD": dict(neg)}, 0.9) == "REJECTED"


def test_cluster_bootstrap_resamples_games_not_rows():
    # 1 game with 100 identical rows must not look like 100 independent observations
    df = pd.DataFrame({"game_id": ["g1"] * 100 + ["g2"] * 100, "pnl": [1.0] * 100 + [-1.0] * 100, "cost": [1.0] * 200})
    point, lo, hi = cluster_ratio_ci(df, "pnl", "cost", n=2000)
    assert point == 0.0 and lo <= -0.5 and hi >= 0.5  # two clusters -> enormous uncertainty
    rows = pd.DataFrame({"game_id": np.arange(200), "pnl": [1.0] * 100 + [-1.0] * 100, "cost": [1.0] * 200})
    _, lo2, hi2 = cluster_ratio_ci(rows, "pnl", "cost", n=2000)
    assert (hi2 - lo2) < (hi - lo)
