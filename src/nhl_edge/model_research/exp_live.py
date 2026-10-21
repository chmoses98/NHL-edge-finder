"""M-LIVE-1: ONE look at the 151 LIVE games. Frozen C1 (fitted on all WF games, sigma=0) vs production V1, V2, sportsbook consensus and the Kalshi T-60 mid.

    python -m nhl_edge.model_research.exp_live --repo . --live <live_t60.parquet> --derived <market-audit work dir> --out docs/research/nhl-model-improvement/data
Parameters are read from data/cal_experiments.json (``c1_frozen_all_wf``) and are NOT refitted here. Reads only games that start before the prospective freeze.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.model_research import challengers as C
from nhl_edge.model_research import dist_eval as D
from nhl_edge.model_research import registry
from nhl_edge.model_research import scoring as S
from nhl_edge.model_research.market_eval import FAMILIES, attach_model_p, game_level_losses
from nhl_edge.model_research.wf_data import MARGIN_LO


def run(repo: Path, live: pd.DataFrame, derived: Path, params: dict[str, float]) -> dict[str, Any]:
    n = int(live["v1_n_sims"].iloc[0])
    lam_h, lam_a, seeds = live["v1_lam_home"].to_numpy(), live["v1_lam_away"].to_numpy(), live["v1_seed"].to_numpy().astype(int)
    c1 = [C.apply_c1(params, h + a, h - a) for h, a in zip(lam_h, lam_a)]
    P_v1 = D.simulate_pmfs(lam_h, lam_a, seeds, n_sims=n)
    P_c1 = D.simulate_pmfs(np.array([x[0] for x in c1]), np.array([x[1] for x in c1]), seeds, n_sims=n)
    y_t = live["y_total"].to_numpy()
    y_m = (live["home_final"] - live["away_final"]).to_numpy()
    y_w = live["y_home_win"].to_numpy()
    L = {}
    for name, P in (("V1", P_v1), ("C1", P_c1)):
        L[name] = {"rps_total": S.rps_from_pmf(P["total"], y_t), "rps_margin": S.rps_from_pmf(P["margin"], np.clip(y_m, -10, 10) - MARGIN_LO), "brier_win": S.brier(P["p_home_win"], y_w),
                   "ll_win": S.logloss(P["p_home_win"], y_w)}
    L["V2"] = {"brier_win": S.brier(live["v2_p_home_win"].to_numpy(), y_w)}
    sb = live["sb_p_home"].to_numpy()
    ok = ~np.isnan(sb)
    out: dict[str, Any] = {"n_games": int(len(live)), "c1_params": params, "paired_C1_minus_V1": {k: S.paired_delta(L["C1"][k], L["V1"][k]) for k in L["V1"]},
                           "mean": {a: {k: float(v.mean()) for k, v in d.items()} for a, d in L.items()},
                           "moneyline_game_level": {"n_with_sportsbook": int(ok.sum()), "brier_sportsbook": float(S.brier(sb[ok], y_w[ok]).mean()),
                                                    "brier_V1_same_games": float(L["V1"]["brier_win"][ok].mean()), "brier_C1_same_games": float(L["C1"]["brier_win"][ok].mean()),
                                                    "brier_V2_same_games": float(L["V2"]["brier_win"][ok].mean()),
                                                    "paired_V1_minus_sportsbook": S.paired_delta(L["V1"]["brier_win"][ok], S.brier(sb[ok], y_w[ok])),
                                                    "paired_C1_minus_sportsbook": S.paired_delta(L["C1"]["brier_win"][ok], S.brier(sb[ok], y_w[ok]))}}
    lp = pd.read_parquet(derived / "live_panel.parquet")
    lp = lp[(lp["horizon_min"] == 60) & lp["kind"].isin(FAMILIES) & lp["game_id"].isin(live["game_id"])].copy()
    gids = live["game_id"].to_numpy()
    fam: dict[str, Any] = {}
    for arm, P in (("V1", P_v1), ("C1", P_c1)):
        pm = {g: {"total": P["total"][i], "margin": P["margin"][i], "p_home_win": float(P["p_home_win"][i])} for i, g in enumerate(gids)}
        p = attach_model_p(lp, pm, "p_model")
        p = p[p["p_model"].notna()]
        for f in FAMILIES:
            d = p[p["kind"] == f]
            t = pd.DataFrame({"model": S.brier(d["p_model"].to_numpy(), d["y"].to_numpy()), "mid": S.brier(d["mid"].to_numpy(), d["y"].to_numpy()), "game_id": d["game_id"].to_numpy()}).groupby("game_id").mean()
            fam.setdefault(arm, {})[f] = {"n_games": int(len(t)), "brier_model": float(t["model"].mean()), "brier_mid": float(t["mid"].mean()), "model_minus_mid": S.paired_delta(t["model"].to_numpy(), t["mid"].to_numpy())}
    out["kalshi_t60_families"] = fam
    return out


def record(res: dict[str, Any], repo: Path, reg: Path) -> None:
    if any(e["type"] == "RESULT" and e["id"] == "M-LIVE-1" for e in registry.read(reg)):
        return
    d = res["paired_C1_minus_V1"]
    ok = d["rps_total"]["delta"] < 0 and d["brier_win"]["delta"] < 0
    registry.append(reg, "RESULT", "M-LIVE-1", {"metrics": {"paired_C1_minus_V1": d, "mean": res["mean"], "moneyline_game_level": res["moneyline_game_level"], "kalshi_t60_families": res["kalshi_t60_families"]},
                                                 "decision": "DIRECTION_CONFIRMED" if ok else "LIVE_INCONCLUSIVE", "interpretation": "see docs/research/nhl-model-improvement/CHALLENGER_MODEL_COMPARISON.md",
                                                 "reproduction": "python -m nhl_edge.model_research.exp_live --repo . --live <live_t60.parquet> --derived <work dir> --out docs/research/nhl-model-improvement/data",
                                                 "results_file": "docs/research/nhl-model-improvement/data/live_challenger.json"}, repo)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--live", type=Path, required=True)
    ap.add_argument("--derived", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    params = json.loads((a.out / "cal_experiments.json").read_text())["c1_frozen_all_wf"]
    r = run(a.repo, pd.read_parquet(a.live), a.derived, params)
    (a.out / "live_challenger.json").write_text(json.dumps(r, indent=1, default=float))
    record(r, a.repo, a.repo / "docs/research/nhl-model-improvement/experiment_registry.jsonl")
    print(json.dumps({k: r[k] for k in ("n_games", "mean", "moneyline_game_level")}, indent=1, default=float))
    print({k: (round(v["delta"], 4), round(v["lo95"], 4), round(v["hi95"], 4)) for k, v in r["paired_C1_minus_V1"].items()})
    for arm, fs in r["kalshi_t60_families"].items():
        for f, v in fs.items():
            print(arm, f, v["n_games"], round(v["brier_model"], 4), round(v["brier_mid"], 4), round(v["model_minus_mid"]["delta"], 4), [round(v["model_minus_mid"]["lo95"], 4), round(v["model_minus_mid"]["hi95"], 4)])
