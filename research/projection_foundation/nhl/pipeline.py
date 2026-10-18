"""Build every walk-forward prediction table (cached in .cache/, gitignored).

Stage 1  feature frames + schedule-adjusted ratings + TOI (opportunity) models
Stage 2  skater ladders A..F for sog / goals / assists / points
Stage 3  goalie saves and team goals ladders
"""
from __future__ import annotations

import json
import time

import pandas as pd

from pf_core import models

from . import features, ladder, opportunity, opponent
from .data import CACHE

ALPHA = {"sog_for": 3.0, "goals_for": 30.0, "xg_for": 3.0}  # chosen on development (opponent.choose_alpha)
STATS = ["sog", "goals", "assists", "points"]


def _p(name):
    return CACHE / f"{name}.parquet"


def team_ratings(tg: pd.DataFrame) -> pd.DataFrame:
    out = tg[["game_id", "team_id"]].copy()
    for y, a in ALPHA.items():
        r = opponent.ratings(tg, y, a)
        out = out.merge(opponent.attach(tg, r, y), on=["game_id", "team_id"], how="left")
    return out


def stage1(rebuild=False, log=None):
    f = _p("stage1_sk")
    if f.exists() and not rebuild:
        return pd.read_parquet(f), json.load(open(CACHE / "stage1_params.json"))
    log = log if log is not None else []
    tg = features.team_frame()
    tr = team_ratings(tg)
    tr.to_parquet(_p("team_ratings"))
    sk = features.skater_frame()
    sk = sk.merge(tr, on=["game_id", "team_id"], how="left")
    sk = opportunity.add_roles(sk)
    sk, prm = opportunity.toi_models(sk, log)
    sk = sk.copy()
    sk.to_parquet(f)
    json.dump({"toi": prm, "log": log, "alpha": ALPHA}, open(CACHE / "stage1_params.json", "w"), default=str)
    return sk, {"toi": prm, "log": log, "alpha": ALPHA}


def stage2(rebuild=False):
    f = _p("stage2_sk")
    if f.exists() and not rebuild:
        return pd.read_parquet(f), json.load(open(CACHE / "stage2_params.json"))
    sk, _ = stage1()
    out = {}
    for s in STATS:
        t0 = time.time()
        log = []
        P = ladder.skater_ladder(sk, s, log)
        P["features_E"] = ladder.skater_E(sk, s)
        P["stack"] = ladder.stack_F(sk, s)
        P["log"] = log
        P["seconds"] = time.time() - t0
        out[s] = P
        print(f"[stage2] {s} done in {P['seconds']:.0f}s", flush=True)
    keep = [c for c in sk.columns if c.startswith(("mu_", "rate_", "oppadj_"))]
    base = ["game_id", "player_id", "team_id", "opp_id", "season", "game_date", "pos", "role", "pp_role", "name",
            "is_home", "toi_n", "toi", "toi_pp", "toi_np", "sog", "goals", "assists", "points", "line_now",
            "pp_unit_now", "line_last", "pp_unit_last", "line_changed_pit", "line_changed_now", "missed_games",
            "new_team", "b2b", "rest_days", "travel_km", "days_since_last", "toi_A", "toi_B", "toi_C", "toi_E",
            "toi_np_E", "toi_pp_E", "toi_pp_C", "toi_np_C", "sog_for_oppf", "goals_for_oppf", "xg_for_oppf",
            "sog_for_opp_n", "goals_for_opp_n", "xg_for_opp_n", "shifts_ok", "rank_np_last", "toi_last",
            "toi_pp_last"]
    hist = [c for c in sk.columns if c.endswith(("_ewm10", "_ewm3")) and c.split("_ewm")[0] in STATS + ["toi", "toi_pp"]]
    sk2 = sk[list(dict.fromkeys(base + keep + hist))].copy()
    sk2.to_parquet(f)
    json.dump(out, open(CACHE / "stage2_params.json", "w"), default=str)
    return sk2, out


def stage3(rebuild=False):
    f1, f2 = _p("stage3_goalie"), _p("stage3_team")
    if f1.exists() and f2.exists() and not rebuild:
        return pd.read_parquet(f1), pd.read_parquet(f2), json.load(open(CACHE / "stage3_params.json"))
    tg = features.team_frame()
    tr = pd.read_parquet(_p("team_ratings")) if _p("team_ratings").exists() else team_ratings(tg)
    tg = tg.merge(tr, on=["game_id", "team_id"], how="left")
    tg["is_home_i"] = tg["is_home"].astype(int)
    # ---- goalies (actual starters)
    gf = features.goalie_frame()
    opp_sa = tr[["game_id", "team_id", "sog_for_ridge", "sog_for_icpt"]].rename(
        columns={"team_id": "opp_id", "sog_for_ridge": "sa_ridge", "sog_for_icpt": "sa_icpt"})
    gf = gf.merge(opp_sa, on=["game_id", "opp_id"], how="left")
    glog = []
    gf, gP = ladder.goalie_ladder(gf, glog)
    feats = [c for c in ladder.GOALIE_E_FEATURES if c in gf.columns]
    gf["_y"] = gf["saves"].astype(float)
    gf["_train"] = gf["saves_n"].fillna(0) >= 1
    gf["mu_saves_E"] = models.lgbm_walkforward(gf, feats, "_y", "season", objective="poisson", min_train_blocks=1,
                                               params={**ladder.LGB, "min_child_samples": 100},
                                               train_mask_col="_train")
    gf["toi_n"] = gf["saves_n"]
    gP["stack"] = ladder.stack_F(gf, "saves")
    gP["features_E"] = feats
    gP["log"] = glog
    # ---- team goals
    tlog = []
    tg, tP = ladder.team_ladder(tg, tlog)
    feats_t = [c for c in ladder.TEAM_E_FEATURES if c in tg.columns]
    tg["_y"] = tg["goals_for"].astype(float)
    tg["_train"] = tg["goals_for_n"].fillna(0) >= 1
    tg["mu_tg_E"] = models.lgbm_walkforward(tg, feats_t, "_y", "season", objective="poisson", min_train_blocks=1,
                                            params={**ladder.LGB, "min_child_samples": 100, "n_estimators": 200},
                                            train_mask_col="_train")
    tg["tg"] = tg["goals_for"]
    tg["toi_n"] = tg["goals_for_n"]
    tP["stack"] = ladder.stack_F(tg, "tg")
    tP["features_E"] = feats_t
    tP["log"] = tlog
    gf.drop(columns=["_y", "_train"]).to_parquet(f1)
    tg.drop(columns=["_y", "_train"]).to_parquet(f2)
    P = {"saves": gP, "team_goals": tP}
    json.dump(P, open(CACHE / "stage3_params.json", "w"), default=str)
    return gf, tg, P


if __name__ == "__main__":
    import sys
    st = sys.argv[1] if len(sys.argv) > 1 else "all"
    rb = "--rebuild" in sys.argv
    if st in ("1", "all"):
        stage1(rebuild=rb)
    if st in ("2", "all"):
        stage2(rebuild=rb)
    if st in ("3", "all"):
        stage3(rebuild=rb)
    print("done")
