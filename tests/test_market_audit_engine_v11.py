"""Regression tests for the expression-engine defects found in the independent review of PR #52 (F1 double-counted model weight, F2 unit/NaN gate,
F3 crossed book, F4 side-specific evidence, F6 correlation reporting). All use REALISTIC books (ask >= mid)."""

from __future__ import annotations

import math

import pytest

from nhl_edge.market_audit.expression_engine import Candidate, build_card, evaluate, research_stake


def cand(**kw):
    base = dict(ticker="T1", title="Under 5.5", family="game_total", side="no", ask=0.50, mid_yes=0.50, p_model=0.35, factor="LOW_SCORING", survival=0.8)
    base.update(kw)
    return Candidate(**base)


def test_realistic_book_can_be_eligible_when_the_model_has_earned_weight():
    # ask == mid: a 15-point model disagreement at weight 0.8 -> p_hat 0.62 on the NO side, lower bound clears price + fee
    r = evaluate(cand(), w=0.8, family_class="VALIDATED")
    assert r["eligible"], r["reject_reasons"]
    assert r["net_ev_lower_bound"] > 0


def test_zero_weight_never_clears_price_plus_fee():
    r = evaluate(cand(), w=0.0, family_class="VALIDATED")
    assert not r["eligible"] and r["net_ev_per_contract"] < 0


def test_weight_is_clamped_to_unit_interval():
    r = evaluate(cand(p_model=0.0), w=5.0, family_class="VALIDATED")
    assert r["model_weight"] <= 1.0 and 0.0 <= r["estimated_probability"] <= 1.0


@pytest.mark.parametrize("kw", [dict(ask=float("nan")), dict(mid_yes=float("nan")), dict(p_model=float("nan")), dict(ask=50), dict(p_model=60), dict(ask=1.0), dict(ask=0.0)])
def test_invalid_inputs_are_never_eligible(kw):
    r = evaluate(cand(**kw), w=0.8, family_class="VALIDATED")
    assert not r["eligible"] and r["reject_reasons"]


def test_crossed_book_is_rejected_even_with_zero_weight():
    r = evaluate(cand(ask=0.40, mid_yes=0.50), w=0.0, family_class="VALIDATED")  # NO mid 0.50, ask 0.40
    assert not r["eligible"] and any("crossed" in x for x in r["reject_reasons"])


def test_research_stake_guards():
    assert research_stake(0.05, 0.6, 1.0) == 0.0
    assert research_stake(0.05, float("nan"), 0.5) == 0.0


def test_side_specific_evidence_blocks_the_other_direction():
    over = cand(ticker="O", side="yes", mid_yes=0.50, p_model=0.65, factor="HIGH")
    under = cand(ticker="U", side="no", p_model=0.35, factor="LOW")
    card = build_card("G", [over, under], {"game_total": 0.8}, {"game_total|no": "VALIDATED", "game_total|yes": "REJECTED", "game_total": "VALIDATED"}, policy="strict")
    assert [r["ticker"] for r in card["selected"]] == ["U"]


def test_correlated_skip_is_reported():
    a = cand(ticker="A", factor="LOW_SCORING")
    b = cand(ticker="B", factor="LOW_SCORING", ask=0.51)
    card = build_card("G", [a, b], {"game_total": 0.8}, {"game_total": "VALIDATED"}, policy="strict")
    assert len(card["selected"]) == 1 and len(card["skipped_correlated"]) == 1
    assert math.isfinite(card["selected"][0]["net_ev_lower_bound"])
