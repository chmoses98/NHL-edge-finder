"""Daily feedback loop: ledger idempotence, prospective blinding, one-time looks; registry hash chain; challenger leakage guard."""

from __future__ import annotations

import json
from datetime import UTC, datetime

import numpy as np
import pytest

from nhl_edge.model_research import challengers as C
from nhl_edge.model_research import daily, registry
from nhl_edge.model_research import scoring as S


def row(i, p1=0.55, p2=0.5, pc=0.54, sb=0.52, y=1, cls="E_normal_variance"):
    return {"game_id": str(i), "y_home_win": y, "v1_p_home_win": p1, "v2_p_home_win": p2, "c1_p_home_win": pc, "sb_p_home": sb, "attribution_class": cls, "slate_age_min": 20.0,
            "any_goalie_mismatch": False}


def test_ledger_append_is_idempotent_and_never_rewrites(tmp_path):
    p = tmp_path / "l.jsonl"
    assert daily.append_rows(p, [row(1), row(2)]) == 2
    before = p.read_text()
    assert daily.append_rows(p, [row(1, p1=0.99), row(3)]) == 1
    assert p.read_text().startswith(before)  # history untouched
    assert [r["game_id"] for r in daily.read_ledger(p)] == ["1", "2", "3"]


def test_scorecard_is_blinded_before_the_first_look(tmp_path):
    rows = [row(i, y=int(i % 2)) for i in range(149)]
    sc = daily.scorecard(rows, tmp_path)
    assert sc["status"] == "ACCUMULATING_BLINDED" and "look" not in sc and "brier" not in json.dumps(sc)
    assert not list(tmp_path.glob("LOOK_*"))


def test_look_is_written_once_and_is_immutable(tmp_path):
    rows = [row(i, y=int(i % 2)) for i in range(150)]
    sc = daily.scorecard(rows, tmp_path)
    assert sc["status"] == "AT_LOOK_150" and (tmp_path / "LOOK_150.json").exists()
    first = (tmp_path / "LOOK_150.json").read_text()
    rows2 = [row(i, p1=0.9, y=int(i % 3 == 0)) for i in range(150)]  # a different outcome history must NOT overwrite the look already taken
    daily.scorecard(rows2, tmp_path)
    assert (tmp_path / "LOOK_150.json").read_text() == first


def test_registry_detects_tampering(tmp_path):
    p = tmp_path / "r.jsonl"
    registry.append(p, "PREREG", "X", {"hypothesis": "h"}, now=datetime(2026, 10, 21, tzinfo=UTC))
    registry.append(p, "RESULT", "X", {"decision": "NO"}, now=datetime(2026, 10, 22, tzinfo=UTC))
    assert registry.verify(p) == []
    lines = p.read_text().splitlines()
    lines[0] = lines[0].replace('"h"', '"edited"')
    p.write_text("\n".join(lines) + "\n")
    assert registry.verify(p)
    with pytest.raises(ValueError):
        registry.append(tmp_path / "r2.jsonl", "RESULT", "Y", {})  # a RESULT needs a PREREG


def test_scoring_rules_are_proper_and_pmf_rps_matches_definition():
    pmf = np.array([[0.2, 0.5, 0.3]])
    assert S.rps_from_pmf(pmf, np.array([1]))[0] == pytest.approx((0.2 - 0) ** 2 + (0.7 - 1) ** 2 + (1.0 - 1) ** 2)
    p = np.array([0.7])
    assert S.brier(p, np.array([1.0]))[0] < S.brier(np.array([0.4]), np.array([1.0]))[0]


def test_c1_fit_uses_only_the_rows_it_is_given_no_look_ahead():
    import pandas as pd

    rng = np.random.default_rng(1)
    n = 400
    s = 6 + rng.normal(0, 0.3, n)
    d = rng.normal(0, 0.4, n)
    df = pd.DataFrame({"s": s, "d": d, "reg_s": s * 0.4 + 3.6 + rng.normal(0, 2, n), "reg_d": d * 1.4 + rng.normal(0, 2.2, n)})
    p = C.fit_c1(df.iloc[:200])
    p_all = C.fit_c1(df)
    assert p["n_train"] == 200 and p_all["n_train"] == 400
    h, a = C.apply_c1(p, 6.0, 0.2)
    assert h > 0 and a > 0 and abs((h + a) - (p["s_mean_target"] + p["b_s"] * (6.0 - p["sbar"]))) < 1e-9
