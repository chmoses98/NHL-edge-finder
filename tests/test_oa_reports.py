from __future__ import annotations

import numpy as np
import pandas as pd

from nhl_edge.research.oa_market import compare_target
from nhl_edge.research.v1_diagnostics import diagnose


def _run(tmp_path, ot_pred, n=400, seed=0):
    rng = np.random.default_rng(seed)
    hs, as_ = rng.poisson(3.1, n), rng.poisson(3.0, n)
    ot = (rng.random(n) < 0.22).astype(int)
    df = pd.DataFrame({"game_id": range(n), "season": [2018] * n, "home_score": hs, "away_score": as_, "y_total": hs + as_, "y_overtime": ot,
                       "y_home_win": (hs > as_).astype(int), "V1_p_overtime": ot_pred, "V1_p_home_win": 0.54})
    k = 20
    tot = np.tile(np.exp(-0.5 * (np.arange(k) - 6.1) ** 2 / 5.0), (n, 2, 1))
    tot /= tot.sum(axis=2, keepdims=True)
    mar = np.tile(np.exp(-0.5 * (np.arange(-10, 11)) ** 2 / 6.0), (n, 2, 1))
    mar /= mar.sum(axis=2, keepdims=True)
    df.to_csv(tmp_path / "g.csv", index=False)
    np.savez(tmp_path / "p.npz", total=tot, margin=mar, arms=np.array(["V1", "LEAGUE"]))
    return diagnose(tmp_path / "g.csv", tmp_path / "p.npz")


def test_diagnostics_detect_overtime_under_prediction(tmp_path):
    r = _run(tmp_path, ot_pred=0.17, n=2000)["2018-2023 (unexposed)"]
    assert r["overtime"]["gap_pred_minus_real"] < -0.03 and r["overtime"]["ci95"][1] < 0
    ok = _run(tmp_path, ot_pred=0.22, n=2000)["2018-2023 (unexposed)"]
    assert ok["overtime"]["ci95"][0] < 0 < ok["overtime"]["ci95"][1]


def test_market_comparison_flags_a_worse_model_and_ignores_a_hybrid_that_adds_nothing():
    rng = np.random.default_rng(1)
    n = 3000
    truth = rng.uniform(0.3, 0.7, n)
    y = (rng.random(n) < truth).astype(float)
    df = pd.DataFrame({"y": y, "market": truth, "p_good": truth, "p_bad": np.clip(truth + rng.normal(0, 0.2, n), 0.05, 0.95),
                       "game_date": [f"2025-01-{1 + i % 28:02d}" for i in range(n)]})
    r = compare_target(df, ["good", "bad"], n_boot=500)["forecasters"]
    assert r["bad"]["market_better_than_model"] and r["bad"]["kind"] == "INDEPENDENT"
    assert not r["good"]["market_better_than_model"] and not r["good"]["model_better_than_market"]
    assert r["bad+mkt(w=0.9)"]["kind"] == "MARKET-INFORMED"
