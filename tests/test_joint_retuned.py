from __future__ import annotations

from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

from nhl_edge.research import joint_retuned as JR
from nhl_edge.research import joint_retuned_eval as JE


def test_collect_derives_every_target_from_the_same_draws():
    # draws: reg home win 3-1 | reg away win 2-1 | OT home 3-2 (reg 2-2) | reg home win 5-2
    r = SimpleNamespace(home_reg=[3, 1, 2, 5], away_reg=[1, 2, 2, 2], home_final=[3, 1, 3, 5], away_final=[1, 2, 2, 2])
    c = JR.collect({"A": r})
    assert (c["A_p_reg_home"], c["A_p_reg_tie"], c["A_p_reg_away"]) == (0.5, 0.25, 0.25)
    assert c["A_p_home_pl"] == 0.5 and c["A_p_away_pl"] == 0.0           # 3-1 and 5-2 are wins by 2+
    assert c["A_mean_total"] == pytest.approx((4 + 3 + 5 + 7) / 4)
    assert c["A_p_home_o2.5"] == 0.75 and c["A_p_away_o1.5"] == 0.75
    assert c["A_p_reg_home"] + c["A_p_reg_tie"] + c["A_p_reg_away"] == pytest.approx(1.0)


def test_extra_losses_score_regulation_ties_puck_lines_and_team_totals():
    df = pd.DataFrame({"last_period_type": ["REG", "OT"], "home_score": [3, 3], "away_score": [1, 2]})
    for k, v in {"p_reg_home": [1.0, 0.0], "p_reg_tie": [0.0, 1.0], "p_reg_away": [0.0, 0.0], "p_home_pl": [1.0, 0.0], "p_away_pl": [0.0, 0.0]}.items():
        df[f"A_{k}"] = v
    for L in JE.TEAM_LINES:
        df[f"A_p_home_o{L}"] = (df["home_score"] > L).astype(float)
        df[f"A_p_away_o{L}"] = (df["away_score"] > L).astype(float)
    L = JE.extra_losses(df, ["A"])["A"]
    assert np.allclose(L["brier_reg3"], 0) and np.allclose(L["brier_puck_line"], 0) and np.allclose(L["brier_team_total"], 0)
    df["A_p_reg_home"] = [0.0, 0.0]                                         # now the first game is a lost probability on the realised class
    assert JE.extra_losses(df, ["A"])["A"]["brier_reg3"][0] == pytest.approx(1.0)
