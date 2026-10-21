"""Registry v1.1 rules: stricter PROMISING, v1.0 untouched."""

from __future__ import annotations

import json
from pathlib import Path

from nhl_edge.market_audit import hypotheses as H
from nhl_edge.market_audit import hypotheses_v11 as V

REPO = Path(__file__).resolve().parents[1]


def tier(roi, lo95, hi95, lo90, slip, n=151):
    return {"roi": roi, "roi_lo95": lo95, "roi_hi95": hi95, "roi_lo90": lo90, "roi_slip_1c": slip, "n_games": n}


def test_m14_shape_is_promising_v10_but_not_v11():
    per = {"LIVE": tier(0.001, -0.177, 0.178, -0.14, -0.021)}
    assert H.classify(per, 0.976) == "PROMISING"
    assert V.classify_v11(per, 0.976) == "POINT_POSITIVE"


def test_genuinely_strong_single_tier_can_be_promising_v11():
    per = {"LIVE": tier(0.12, 0.03, 0.21, 0.05, 0.10)}
    assert H.classify(per, 0.08) == "VALIDATED"  # q <= 0.10: v1.0 VALIDATED passes through unchanged
    assert V.classify_v11(per, 0.08) == "VALIDATED"
    assert H.classify(per, 0.20) == "PROMISING"
    assert V.classify_v11(per, 0.20) == "PROMISING_V11"


def test_positive_but_low_q_blocks_promising():
    per = {"LIVE": tier(0.12, 0.03, 0.21, 0.05, 0.10)}
    assert V.classify_v11(per, 0.60) == "POINT_POSITIVE"


def test_slippage_negative_blocks_promising():
    per = {"LIVE": tier(0.05, 0.001, 0.10, 0.01, -0.001)}
    assert V.classify_v11(per, 0.1) == "POINT_POSITIVE"


def test_other_classes_pass_through_unchanged():
    per = {"LIVE": tier(-0.05, -0.2, 0.1, -0.15, -0.07)}
    assert V.classify_v11(per, 0.9) == H.classify(per, 0.9) == "INCONCLUSIVE"


def test_reclassify_does_not_mutate_input_and_flags_underpowered():
    p = REPO / "docs/research/nhl-market-audit/data/hypothesis_results.json"
    payload = json.loads(p.read_text())
    before = json.dumps(payload, sort_keys=True)
    out = V.reclassify(payload)
    assert json.dumps(payload, sort_keys=True) == before
    assert out["rows"]["M14"]["class_v10"] == "PROMISING" and out["rows"]["M14"]["class_v11"] == "POINT_POSITIVE"
    assert not [r for r in out["rows"].values() if r["class_v11"] in ("PROMISING_V11", "VALIDATED")]
    assert out["rows"]["M9"]["class_v10"] == "REJECTED" and out["rows"]["M9"]["class_v11"] == "INCONCLUSIVE"
    assert out["rows"]["M1"]["class_v11"] == "UNPROFITABLE_AT_ASK"
    assert "LIVE" in out["rows"]["M14"]["underpowered_tiers"]


def test_untestable_hold_out_blocks_validated():
    from nhl_edge.market_audit.hypotheses import BY_ID

    per = {"LIVE": tier(0.12, 0.03, 0.21, 0.05, 0.10)}
    assert V.classify_v11(per, 0.05) == "VALIDATED"  # no registered hold-out in this fixture
    assert V.classify_v11(per, 0.05, BY_ID["M6"]) == "PROMISING_V11"  # M6 registers HIST_HOLD (untestable here) and is post hoc


def test_rejected_needs_a_margin_so_endpoint_noise_cannot_flip_it():
    thin = {"LIVE": tier(-0.08, -0.16, -0.0006, -0.13, -0.097)}
    assert H.classify(thin, 0.9) == "REJECTED"
    assert V.classify_v11(thin, 0.9) == "INCONCLUSIVE"  # M9's shape
    firm = {"HIST_DISC": tier(-0.09, -0.156, -0.024, -0.14, -0.106, n=673), "LIVE": tier(-0.054, -0.19, 0.09, -0.15, -0.07)}
    assert V.classify_v11(firm, 0.9) == "UNPROFITABLE_AT_ASK"
