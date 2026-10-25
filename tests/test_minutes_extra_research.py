from __future__ import annotations

import numpy as np
import pandas as pd

from nhl_edge.research import minutes_extra_research as X


def _champ():
    rows = []
    for d, g in ((20261001, 1), (20261002, 2), (20261005, 3), (20261006, 4)):
        for p, t in ((1, 10), (2, 20)):
            rows.append({"game_id": g, "player_id": p, "team_id": t, "opp_id": 30 if t == 10 else 10, "date_int": d, "y_toi": 15.0 + g * p, "pos": "F", "is_home": t == 10})
    return pd.DataFrame(rows)


def test_rest_is_days_since_the_teams_previous_game_and_usage_uses_only_earlier_games():
    c = X.rest_features(X.usage_features(_champ()))
    r = c[(c.player_id == 1)].set_index("game_id")
    assert r.loc[2, "team_rest"] == 1 and r.loc[3, "team_rest"] == 3 and np.isnan(r.loc[1, "team_rest"])
    u = X.usage_features(_champ())
    p1 = u[u.player_id == 1].set_index("game_id")
    assert np.isnan(p1.loc[1, "last1_toi"]) and p1.loc[2, "last1_toi"] == 16.0 and np.isnan(p1.loc[3, "last3_toi"]) and p1.loc[4, "last3_toi"] == (16 + 17 + 18) / 3


def test_the_frozen_specification_is_among_the_candidates_unchanged():
    assert CAND_OK(X.CANDIDATES)


def CAND_OK(c):
    return c["usage last 3 (frozen spec, alone)"] == ["u3"]
