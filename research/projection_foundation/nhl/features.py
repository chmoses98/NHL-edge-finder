"""Point-in-time feature frames for skater-, goalie- and team-games.

Rule (pf_core.pit): a feature on game g uses only games that finished before g. Every rolling
quantity is produced by `pit.lagged_features` (shifted one game within the entity) or by an
explicit `shift(1)`; schedule facts (rest, back-to-back, travel, home) are known before puck drop.

What is NOT point-in-time and how it is used
  * the dressed lineup (we evaluate players who actually played: Kalshi settles a non-entering
    player at the pre-game fair price, so the modelled quantity is P(event | plays));
  * the starting goalie for saves (conditional on the actual starter; quantified separately from
    the 2026-27 DailyFaceoff archive in inventory.starter_accuracy);
  * the `*_now` role / line columns below, which are POST-game and only used to diagnose errors.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from pf_core import pit

from . import data, xg

SK_COLS = ["toi", "toi_pp", "toi_np", "toi_sh", "sog", "sog_pp", "sog_np", "goals", "goals_pp", "goals_np",
           "assists", "assists_pp", "assists_np", "a1", "points", "points_pp", "points_np", "ixg", "ixg_pp",
           "att", "gf_on", "pp_share", "np_share", "rank_np"]
HALFLIVES = (3, 10, 30)


def _cache(name: str):
    data.CACHE.mkdir(parents=True, exist_ok=True)
    return data.CACHE / f"{name}.parquet"


def _role_now(sk: pd.DataFrame, tg: pd.DataFrame) -> pd.DataFrame:
    """POST-game role facts for game g (rank of non-PP TOI within team & position, PP unit,
    shares of team time). Lagged versions become PIT features."""
    sk = sk.merge(tg[["game_id", "team_id", "pp_min", "ot_s"]], on=["game_id", "team_id"], how="left")
    game_len = 60.0 + sk["ot_s"].fillna(0) / 60.0
    sk["np_share"] = sk["toi_np"] / (game_len - sk["pp_min"].fillna(0)).clip(lower=30)
    sk["pp_share"] = np.where(sk["pp_min"] > 0.5, sk["toi_pp"] / sk["pp_min"].clip(lower=0.5), np.nan)
    sk["rank_np"] = sk.groupby(["game_id", "team_id", "pos"])["toi_np"].rank(ascending=False, method="first")
    rank_pp = sk.groupby(["game_id", "team_id"])["toi_pp"].rank(ascending=False, method="first")
    sk["pp_unit_now"] = np.where(sk["toi_pp"].fillna(0) < 0.25, 0, np.where(rank_pp <= 5, 1, 2))
    per = np.where(sk["pos"] == "F", 3, 2)
    sk["line_now"] = np.ceil(sk["rank_np"] / per).clip(upper=4 if True else None)
    return sk.drop(columns=["ot_s", "pp_min"])


def _linemates(sk: pd.DataFrame) -> pd.DataFrame:
    """Top-2 even-strength linemates per player-game from pairwise shared ice (coice)."""
    c = data.load_kind("coice")[["game_id", "team_id", "p1", "p2", "shared_ev_s"]]
    both = pd.concat([c.rename(columns={"p1": "player_id", "p2": "mate"}),
                      c.rename(columns={"p2": "player_id", "p1": "mate"})], ignore_index=True)
    pos = sk[["game_id", "player_id", "pos"]]
    both = both.merge(pos, on=["game_id", "player_id"]).merge(
        pos.rename(columns={"player_id": "mate", "pos": "mate_pos"}), on=["game_id", "mate"])
    # forwards: linemates are forwards; defence: partner is a defenceman
    both = both[both["pos"] == both["mate_pos"]]
    both = both.sort_values(["game_id", "player_id", "shared_ev_s"], ascending=[True, True, False])
    both["k"] = both.groupby(["game_id", "player_id"]).cumcount()
    top = both[both["k"] < np.where(both["pos"] == "F", 2, 1)]
    agg = top.groupby(["game_id", "player_id"]).agg(mates=("mate", lambda s: tuple(sorted(s))),
                                                   mate_ev_s=("shared_ev_s", "sum"))
    return agg.reset_index()


def skater_frame(rebuild: bool = False) -> pd.DataFrame:
    f = _cache("skater_frame_v3")
    if f.exists() and not rebuild:
        return pd.read_parquet(f)
    shots, _ = xg.fit_and_score()
    pxg = xg.player_xg(shots)
    sk = data.skater_games(xg=pxg)
    tg = team_frame(rebuild=rebuild)
    sk = _role_now(sk, tg)
    sk["sog_np"] = sk["sog_np"].clip(lower=0)
    sk = pit.sort_chrono(sk, "player_id", "game_date", "game_id")
    sk = pit.lagged_features(sk, "player_id", SK_COLS, halflives=HALFLIVES, season_col="season")
    sk = pit.sort_chrono(sk, "player_id", "game_date", "game_id")
    g = sk.groupby("player_id", sort=False)
    for c in ("toi", "toi_pp", "toi_np", "rank_np", "pp_unit_now", "line_now", "team_id", "season", "game_date"):
        sk[f"{c}_last"] = g[c].shift(1)
    # team schedule + team PIT context
    keep = ["game_id", "team_id", "b2b", "rest_days", "travel_km", "opp_b2b", "opp_rest_days", "team_gno",
            "pp_min_ewm10", "sh_min_ewm10", "opp_sh_min_ewm10", "opp_pp_min_ewm10", "goals_for_ewm10",
            "xg_for_ewm10", "sog_for_ewm10", "len_min_ewm30"]
    sk = sk.merge(tg[keep], on=["game_id", "team_id"], how="left")
    prev_gno = sk.groupby("player_id", sort=False)["team_gno"].shift(1)
    same = (sk["team_id_last"] == sk["team_id"]) & (sk["season_last"] == sk["season"])
    sk["missed_games"] = np.where(same, sk["team_gno"] - prev_gno - 1, np.nan)
    sk["new_team"] = ((sk["team_id_last"] != sk["team_id"]) & sk["team_id_last"].notna()).astype(int)
    sk["days_since_last"] = (sk["game_date"] - sk["game_date_last"]).dt.days
    # linemates: role continuity and linemate quality (previous game's line, PIT)
    lm = _linemates(sk)
    sk = sk.merge(lm, on=["game_id", "player_id"], how="left")
    g = sk.groupby("player_id", sort=False)
    sk["mates_last"] = g["mates"].shift(1)
    sk["mates_last2"] = g["mates"].shift(2)
    sk["line_changed_pit"] = [float(a != b) if isinstance(a, tuple) and isinstance(b, tuple) else np.nan
                              for a, b in zip(sk["mates_last"], sk["mates_last2"])]
    sk["line_changed_now"] = [float(a != b) if isinstance(a, tuple) and isinstance(b, tuple) else np.nan
                              for a, b in zip(sk["mates"], sk["mates_last"])]
    # linemate quality: mean PIT points/60 of last game's linemates, as of that previous game
    rate = sk[["game_id", "player_id", "points_ewm30", "toi_ewm30"]].copy()
    rate["p60"] = 60 * rate["points_ewm30"] / rate["toi_ewm30"].clip(lower=5)
    rate = rate.set_index(["game_id", "player_id"])["p60"]
    gid_last = g["game_id"].shift(1)
    q = []
    for gl, mates in zip(gid_last, sk["mates_last"]):
        if isinstance(mates, tuple) and pd.notna(gl):
            v = [rate.get((int(gl), int(m)), np.nan) for m in mates]
            v = [x for x in v if np.isfinite(x)]
            q.append(float(np.mean(v)) if v else np.nan)
        else:
            q.append(np.nan)
    sk["mate_p60_last"] = q
    sk = sk.drop(columns=["mates", "mates_last", "mates_last2"])
    sk.to_parquet(f)
    return sk


def team_frame(rebuild: bool = False) -> pd.DataFrame:
    f = _cache("team_frame_v3")
    if f.exists() and not rebuild:
        return pd.read_parquet(f)
    tg = data.team_games()
    shots, _ = xg.fit_and_score()
    tx = xg.team_xg(shots)
    tg = tg.merge(tx, on=["game_id", "team_id"], how="left")
    tg["xg_for"] = tg["xg_for"].fillna(0)
    o = tg[["game_id", "team_id", "xg_for"]].rename(columns={"team_id": "opp_id", "xg_for": "xg_against"})
    tg = tg.merge(o, on=["game_id", "opp_id"], how="left")
    tg["len_min"] = 60.0 + tg["ot_s"].fillna(0) / 60.0
    tg = pit.sort_chrono(tg, "team_id", "game_date", "game_id")
    tg["team_gno"] = tg.groupby(["team_id", "season"]).cumcount()
    cols = ["goals_for", "goals_against", "sog_for", "sog_against", "xg_for", "xg_against", "pp_min", "sh_min",
            "len_min", "total_goals"]
    tg = pit.lagged_features(tg, "team_id", cols, halflives=(10, 30), season_col="season")
    tg = pit.sort_chrono(tg, "team_id", "game_date", "game_id")
    opp = tg[["game_id", "team_id", "sh_min_ewm10", "pp_min_ewm10", "sog_against_ewm30", "goals_against_ewm30",
              "xg_against_ewm30", "sog_for_ewm30", "goals_for_ewm30", "xg_for_ewm30"]]
    opp = opp.rename(columns={c: f"opp_{c}" for c in opp.columns if c not in ("game_id",)})
    opp = opp.rename(columns={"opp_team_id": "opp_id"})
    tg = tg.merge(opp, on=["game_id", "opp_id"], how="left")
    tg.to_parquet(f)
    return tg


def goalie_frame(rebuild: bool = False) -> pd.DataFrame:
    """Starting-goalie rows. Saves / shots-against history is built from the goalie's previous STARTS
    (relief appearances would drag the level down); start and pull frequencies from all appearances."""
    f = _cache("goalie_frame_v4")
    if f.exists() and not rebuild:
        return pd.read_parquet(f)
    gg = data.goalie_games()
    gg = gg[gg["toi_s"] > 0].copy()
    gg["starter_i"] = gg["starter"].astype(int)
    gg["pulled"] = (gg["starter"] & (gg["toi"] < 55)).astype(int)
    gg = pit.sort_chrono(gg, "player_id", "game_date", "game_id")
    gg = pit.lagged_features(gg, "player_id", ["starter_i", "pulled"], halflives=(10, 30), season_col=None)
    st = gg[gg["starter"]].copy().reset_index(drop=True)
    st = pit.sort_chrono(st, "player_id", "game_date", "game_id")
    st = pit.lagged_features(st, "player_id", ["saves", "shots_against", "goals_against", "toi"],
                             halflives=(10, 30), season_col="season")
    st = pit.sort_chrono(st, "player_id", "game_date", "game_id")
    st["shots_against_cum"] = (st["shots_against_career"] * st["shots_against_n"]).fillna(0)
    st["sv_career"] = (st["saves_career"] * st["saves_n"]) / st["shots_against_cum"].replace(0, np.nan)
    st["starts_ewm10"] = st["starter_i_ewm10"]
    st["pulled_ewm30"] = st["pulled_ewm30"]
    tg = team_frame()
    keep = ["game_id", "team_id", "b2b", "rest_days", "travel_km", "opp_b2b",
            "sog_against_ewm10", "sog_against_ewm30", "sog_against_std", "sog_against_n", "opp_sog_for_ewm30",
            "xg_against_ewm30", "opp_xg_for_ewm30", "sog_against", "len_min", "team_gno"]
    st = st.merge(tg[keep], on=["game_id", "team_id"], how="left")
    st["is_home_i"] = st["is_home"].astype(int)
    st.to_parquet(f)
    return st
