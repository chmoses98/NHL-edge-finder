"""Incumbent predictions joined one row per player-game (never per ladder rung or snapshot).

* PLAYER_SIM_V1 prospective archive (data-archive predictions_player, 2026-27): last PREGAME snapshot
  per (game, player); means from the snapshot's meta_expected_* fields, rung probabilities from the
  same model run (p_player at threshold k-0.5 = P(X >= k)).
* PLAYER_SIM_V1 historical walk-forward (docs/research/player_sim_v1): skaters 2025-26, goalies
  2024-25 and 2025-26 (actual dressed lineup and starters, deployment from recent shifts).
* DATA_ONLY_V2 walk-forward (docs/research/walk_forward_v2_*_games.csv): SIM2_ST expected goals
  (the valid pregame arm) for 2024-25 and 2025-26.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import data, inventory

DOCS = data.ROOT / "docs" / "research"
FAM = {"player_goals": "goals", "player_assists": "assists", "player_points": "points", "goalie_saves": "saves"}


def prospective() -> tuple[pd.DataFrame, pd.DataFrame]:
    """(skater rows, goalie rows) from the PLAYER_SIM_V1 archive, last pregame snapshot."""
    d = inventory.CACHE_PP()
    if d is None or d.empty:
        return pd.DataFrame(), pd.DataFrame()
    d = d[(d["pregame"] == True) & (pd.to_numeric(d["minutes_to_start"], errors="coerce") > 0)].copy()  # noqa: E712
    d = d[d["family"].isin(FAM) & d["player_id"].notna()]
    d["player_id"] = pd.to_numeric(d["player_id"]).astype("int64")
    d["game_id"] = pd.to_numeric(d["game_id"]).astype("int64")
    d["t"] = pd.to_datetime(d["predicted_at_utc"], utc=True)
    d["fam"] = d["family"].map(FAM)
    d["k"] = np.floor(pd.to_numeric(d["threshold"]) + 1).astype(int)  # gt k-0.5  ==  >= k
    last_t = d.groupby(["game_id", "player_id"])["t"].transform("max")
    snap = d[d["t"] == last_t].copy()
    # the registered incumbent is the published template; when another team-minute allocation is published the rows carry the legacy-equivalent values (absent at the default)
    for c in ("meta_expected_toi_min", "meta_expected_pp_toi_min", "meta_expected_shots"):
        if f"{c}_legacy" in snap.columns:
            snap[c] = snap[f"{c}_legacy"].where(snap[f"{c}_legacy"].notna(), snap[c])
    # rungs: latest pregame row per (game, player, family, k)
    rung = d.sort_values("t").groupby(["game_id", "player_id", "fam", "k"]).tail(1)
    wide = rung.pivot_table(index=["game_id", "player_id"], columns=["fam", "k"], values="p_player", aggfunc="last")
    wide.columns = [f"inc_p_{f}_{k}" for f, k in wide.columns]
    meta = snap.groupby(["game_id", "player_id"]).agg(
        inc_toi=("meta_expected_toi_min", "first"), inc_toi_pp=("meta_expected_pp_toi_min", "first"),
        inc_sog=("meta_expected_shots", "first"), inc_goals=("meta_expected_goals", "first"),
        inc_assists=("meta_expected_assists", "first"), inc_points=("meta_expected_points", "first"),
        inc_saves=("meta_expected_saves", "first"), inc_quality=("meta_projection_quality", "first"),
        inc_deploy=("meta_deployment_source", "first"), inc_pred_at=("predicted_at_utc", "first"),
        inc_minutes_to_start=("minutes_to_start", "first"))
    out = meta.join(wide, how="left").reset_index()
    sk = out[out["inc_goals"].notna() | out["inc_points"].notna()].copy()
    gl = out[out["inc_saves"].notna()].copy()
    return sk, gl


def walkforward_skaters() -> pd.DataFrame:
    f = DOCS / "player_sim_v1" / "skaters_2025.parquet"
    if not f.exists():
        return pd.DataFrame()
    d = pd.read_parquet(f)
    out = d[["game_id", "player_id"]].copy()
    out["inc_toi"] = d["exp_toi"]
    out["inc_toi_pp"] = d["exp_toi_pp"]
    out["inc_goals"], out["inc_assists"], out["inc_points"] = d["e_g"], d["e_a"], d["e_p"]
    for f_, c in (("goals", "p_g"), ("points", "p_p")):
        for k in (1, 2, 3):
            out[f"inc_p_{f_}_{k}"] = d[f"{c}{k}"]
    out["inc_p_assists_1"], out["inc_p_assists_2"] = d["p_a1"], d["p_a2"]
    return out


def walkforward_goalies() -> pd.DataFrame:
    parts = []
    for s in (2024, 2025):
        f = DOCS / "player_sim_v1" / f"goalies_{s}.parquet"
        if f.exists():
            d = pd.read_parquet(f)
            x = d[["game_id", "player_id"]].copy()
            x["inc_saves"] = d["e_saves"]
            for k in range(14, 41):
                x[f"inc_p_saves_{k}"] = d[f"p_s{k}"]
            parts.append(x)
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()


def walkforward_team() -> pd.DataFrame:
    fs = sorted(DOCS.glob("walk_forward_v2_*_games.csv"))
    if not fs:
        return pd.DataFrame()
    d = pd.read_csv(fs[-1])
    teams = pd.read_csv(data.ROOT / "data" / "identity" / "teams.csv")
    ab = dict(zip(teams["abbrev"], teams["team_id"]))
    h = pd.DataFrame({"game_id": d["game_id"], "team_id": d["home"].map(ab), "inc_tg": d["SIM2_ST_exp_home"]})
    a = pd.DataFrame({"game_id": d["game_id"], "team_id": d["away"].map(ab), "inc_tg": d["SIM2_ST_exp_away"]})
    for k, c in ((3, "2.5"), (4, "3.5")):
        h[f"inc_p_tg_{k}"] = d[f"SIM2_ST_p_home_over_{c}"]
        a[f"inc_p_tg_{k}"] = d[f"SIM2_ST_p_away_over_{c}"]
    out = pd.concat([h, a], ignore_index=True)
    # Utah Hockey Club played 2024-25 as team id 59 in the boxscores (identity file maps UTA -> 68)
    out.loc[(out["team_id"] == 68) & (out["game_id"] // 1000000 == 2024), "team_id"] = 59
    # Utah: the identity file maps UTA -> 68; 2024-25 Utah HC rows are id 59 in the boxscores
    return out


def rps(prob_ge: dict[int, np.ndarray], y, ks) -> np.ndarray:
    """Ranked probability score restricted to rungs ks: sum_k (P(X>=k) - 1[y>=k])^2."""
    y = np.asarray(y, float)
    tot = np.zeros(len(y))
    for k in ks:
        tot += (np.asarray(prob_ge[k], float) - (y >= k)) ** 2
    return tot
