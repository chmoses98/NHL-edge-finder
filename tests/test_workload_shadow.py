"""WORKLOAD_V1_LC forward predictor: a stub row gets exactly the retrospective prediction (real data), candidates are point-in-time, records are well-formed."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from nhl_edge.research import workload_level_cal as LC
from nhl_edge.research import workload_shadow as S
from nhl_edge.research import workload_v1 as W

ROOT = Path(__file__).resolve().parents[1]
HIST = ROOT / "data" / "history"
PARAMS = ROOT / "docs" / "research" / "workload_v1" / "preregistration.json"


def _players():
    """Team 7 plays six games; player 777 only in game 1; player 158 replaces 108 from game 4; team 8's single skater is 900."""
    rows = []
    for gid, d in ((1, "2026-10-01"), (2, "2026-10-03"), (3, "2026-10-05"), (4, "2026-10-07"), (5, "2026-10-09"), (6, "2026-10-11")):
        ids = [100 + i for i in range(10) if i != 8] + ([108] if gid <= 3 else [158]) + ([777] if gid == 1 else [])
        rows += [{"game_id": gid, "team_id": 7, "game_type": 2, "game_date": d, "player_id": pid} for pid in ids]
        rows.append({"game_id": gid, "team_id": 8, "game_type": 2, "game_date": d, "player_id": 900})
    return pd.DataFrame(rows)


def test_candidates_are_the_last_five_games_point_in_time():
    p = _players()
    five = S.candidates(p, 7, 20261010)                    # games dated before Oct 10: 1..5 -> all five are the "last five"
    assert 777 in five and 108 in five and 158 in five and 900 not in five
    after = S.candidates(p, 7, 20261012)                   # games 1..6 exist; the last five are 2..6 -> the one-game player drops out
    assert 777 not in after and 158 in after and 108 in after
    assert S.candidates(p, 7, 20261002) == sorted({100 + i for i in range(10) if i != 8} | {108, 777})      # strictly before the date: only game 1 exists
    assert S.candidates(p, 7, 20260901) == []
    assert S.candidates(p, 8, 20261012) == [900]


def test_one_day_only_for_stubs():
    sk = pd.DataFrame({"player_id": [1], "date_int": [20261001], "game_id": [1]})
    games = [{"game_id": 5, "home_team_id": 1, "away_team_id": 2, "game_date_et": "2026-10-10"}, {"game_id": 6, "home_team_id": 3, "away_team_id": 4, "game_date_et": "2026-10-11"}]
    with pytest.raises(ValueError):
        S._stubs(sk, pd.DataFrame(columns=["game_id"]), games, {}, 2026)


@pytest.mark.slow
def test_stub_prediction_equals_the_retrospective_prediction_on_real_data():
    seasons = [2024, 2025]
    t = {k: S.load_player_tables(HIST, k, seasons) for k in S.TABLES}
    t["goals"] = t["goals"][t["goals"]["game_type"] == 2]
    sk, tg = S.build_tables(t)
    prm = W.WorkloadParams.from_dict(__import__("json").loads(PARAMS.read_text())["frozen_params"])
    c = W.fit_constants(sk, tg, t["goalies"], seasons)
    with S.stable_sorts():
        ref = W.skater_predictions(sk, tg, c, prm)
    # a mid-season day of 2025 with several games
    day = ref[(ref["season"] == 2025) & (ref["game_type"] == 2) & (ref["date_int"] > 20251201)].groupby("date_int")["game_id"].nunique()
    D = int(day[day >= 5].index[3])
    seen_before = set(sk.loc[sk["date_int"] < D, "player_id"])
    on_day = ref[(ref["date_int"] == D) & ref["player_id"].isin(seen_before)].copy()      # a debutant has no history to stub from; candidates are drawn from recent lineups, so they have one
    games = [{"game_id": int(g), "home_team_id": int(r["home_team_id"]), "away_team_id": int(r["away_team_id"]), "game_date_et": f"{str(D)[:4]}-{str(D)[4:6]}-{str(D)[6:]}",
              "start_time_utc": f"{str(D)[:4]}-{str(D)[4:6]}-{str(D)[6:]}T23:00:00Z"} for g, r in on_day.drop_duplicates("game_id").set_index("game_id").iterrows()]
    cand = {int(tid): sorted(int(x) for x in grp["player_id"]) for tid, grp in on_day.groupby("team_id")}
    pre = sk[sk["date_int"] < D]
    pre_tg = tg[tg["date_int"] < D]
    pre_players = t["players"][t["players"]["game_date"].astype(str).str.replace("-", "").str[:8].astype(int) < D]
    out, fit = S.predict_day(pre, pre_tg, games, pre_players, t["goalies"], PARAMS, season=2025, cand=cand, constants=c, dispersion_season=2024)
    m = out.merge(on_day[["game_id", "player_id", "wl_sog"]], on=["game_id", "player_id"], suffixes=("", "_ref"))
    assert len(m) == len(on_day) == len(out)                                     # every dressed player predicted, nobody extra
    assert np.abs(m["raw_mean"].to_numpy() - m["wl_sog_ref"].to_numpy()).max() < 1e-9
    # the level factor is the frozen function of strictly earlier settled outcomes only
    ref_known = ref[(ref["date_int"] < D) & (ref["season"].isin([2024, 2025])) & (ref["game_type"] == 2)]
    f = LC.level_factors(np.r_[LC._days(ref_known["date_int"]), LC._days(pd.Series([D]))], np.r_[ref_known["sog"].to_numpy(float), 0.0], np.r_[ref_known["wl_sog"].to_numpy(float), 0.0])[-1]
    assert abs(float(out["level_factor"].iloc[0]) - f) < 1e-6
    assert np.allclose(out["lc_mean"].to_numpy(), out["raw_mean"].to_numpy() * out["level_factor"].to_numpy())
    pm = np.vstack(out["pmf"].to_numpy())
    assert pm.shape[1] == S.PMF_K and np.allclose(pm.sum(axis=1), 1.0, atol=1e-6)
    rec = S.records(out, games, fit, f"{str(D)[:4]}-{str(D)[4:6]}-{str(D)[6:]}T12:00:00Z", "abc123")
    late = S.records(out, games, fit, f"{str(D)[:4]}-{str(D)[4:6]}-{str(D)[6:]}T23:30:00Z", "abc123")
    assert late[0]["pregame"] is False
    assert rec[0]["pregame"] is True and rec[0]["conditional_on"] == "dressing" and rec[0]["authority"] == "research_only" and len(rec[0]["pmf"]) == S.PMF_K


@pytest.mark.slow
def test_a_future_outcome_cannot_change_a_stub_prediction():
    seasons = [2024, 2025]
    t = {k: S.load_player_tables(HIST, k, seasons) for k in S.TABLES}
    t["goals"] = t["goals"][t["goals"]["game_type"] == 2]
    sk, tg = S.build_tables(t)
    D = int(sk[(sk["season"] == 2025) & (sk["date_int"] > 20251201)]["date_int"].iloc[2000])
    day = sk[sk["date_int"] == D].drop_duplicates("game_id")
    games = [{"game_id": int(r.game_id), "home_team_id": int(r.home_team_id), "away_team_id": int(r.away_team_id), "game_date_et": f"{str(D)[:4]}-{str(D)[4:6]}-{str(D)[6:]}",
              "start_time_utc": "x"} for r in day.itertuples(index=False)]
    cand = {int(tid): [int(x) for x in sk[(sk["date_int"] == D) & (sk["team_id"] == tid)]["player_id"]] for g in games for tid in (g["home_team_id"], g["away_team_id"])}
    pre, pre_tg = sk[sk["date_int"] < D], tg[tg["date_int"] < D]
    c = W.fit_constants(pre, pre_tg, t["goalies"], seasons)
    a, _ = S.predict_day(pre, pre_tg, games, t["players"], t["goalies"], PARAMS, season=2025, cand=cand, constants=c, dispersion_season=2024)
    poisoned = pd.concat([pre, sk[sk["date_int"] >= D].assign(sog=99.0)], ignore_index=True)       # later days exist with absurd outcomes; stubs must ignore them
    poisoned = poisoned[~poisoned["game_id"].isin([g["game_id"] for g in games])]
    b, _ = S.predict_day(poisoned[poisoned["date_int"] < D], pre_tg, games, t["players"], t["goalies"], PARAMS, season=2025, cand=cand, constants=c, dispersion_season=2024)
    assert np.allclose(a.sort_values(["game_id", "player_id"])["lc_mean"].to_numpy(), b.sort_values(["game_id", "player_id"])["lc_mean"].to_numpy())
