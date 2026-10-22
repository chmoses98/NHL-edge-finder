"""M-MKT-1: does a model carry information beyond the Kalshi T-60 mid? Rolling-origin on the 2025-26 history tier (EVAL_B, 2025 season).

    python -m nhl_edge.model_research.exp_market --repo . --derived <market-audit work dir> --out docs/research/nhl-model-improvement/data
Reads ONLY the HIST panel (2025-26 games); no LIVE/prospective row is touched.
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
from nhl_edge.model_research.market_eval import FAMILIES, attach_model_p, game_level_losses, rolling_incremental
from nhl_edge.model_research.wf_data import load_wf

START_DATE = "2025-12-01"  # ~2 months of 2025-26 market history are training only


def pmf_dict(P: dict[str, np.ndarray], game_ids: np.ndarray) -> dict[Any, dict[str, Any]]:
    return {int(g): {"total": P["total"][i], "margin": P["margin"][i], "p_home_win": float(P["p_home_win"][i])} for i, g in enumerate(game_ids)}


def run(repo: Path, derived: Path) -> dict[str, Any]:
    wf = load_wf(repo)
    wf, _ = C.rolling_c1(wf)
    h = pd.read_parquet(derived / "hist_reg_panel.parquet")
    h = h[(h["horizon_min"] == 60) & h["kind"].isin(FAMILIES)].copy()
    h["game_id"] = h["game_id"].astype(int)
    w25 = wf[wf["season"] == 2025]
    P_v1 = D.simulate_pmfs(w25["lam_home"].to_numpy(), w25["lam_away"].to_numpy(), w25["seed"].to_numpy())
    ok = w25["lam1_home"].notna().to_numpy()
    P_c1 = D.simulate_pmfs(np.where(ok, w25["lam1_home"], w25["lam_home"]), np.where(ok, w25["lam1_away"], w25["lam_away"]), w25["seed"].to_numpy())
    gids = w25["game_id"].to_numpy()
    res: dict[str, Any] = {"start_date": START_DATE, "families": {}}
    for arm, P in (("V1", P_v1), ("C1", P_c1)):
        p = attach_model_p(h, pmf_dict(P, gids), "p_model")
        p = p[p["p_model"].notna()]
        p = pd.concat([rolling_incremental(p[p["kind"] == f].copy(), "p_model", START_DATE) for f in FAMILIES])  # one coefficient per family (as preregistered)
        for fam in FAMILIES:
            gl = game_level_losses(p, fam, {"mid": "mid", "cal": "p_cal", "inc": "p_inc", "model": "p_model"})
            if len(gl) < 30:
                continue
            d = {"n_games": int(len(gl)), "brier": {k: float(gl[k].mean()) for k in gl.columns if k != "game_id"},
                 "inc_minus_mid": S.paired_delta(gl["inc"].to_numpy(), gl["mid"].to_numpy()), "inc_minus_cal": S.paired_delta(gl["inc"].to_numpy(), gl["cal"].to_numpy()),
                 "cal_minus_mid": S.paired_delta(gl["cal"].to_numpy(), gl["mid"].to_numpy()), "model_minus_mid": S.paired_delta(gl["model"].to_numpy(), gl["mid"].to_numpy())}
            sub = p[(p["kind"] == fam) & p["c_prior"].notna()]
            d["final_c"] = float(sub["c_prior"].iloc[-1]) if len(sub) else None
            d["mean_abs_gap_pts"] = float((sub["p_model"] - sub["mid"]).abs().mean() * 100)
            res["families"].setdefault(arm, {})[fam] = d
    return res


def record(res: dict[str, Any], repo: Path, reg: Path) -> None:
    ents = registry.read(reg)
    if any(e["type"] == "RESULT" and e["id"] == "M-MKT-1" and e.get("revision") == 2 for e in ents):
        return
    if not any(e["type"] == "NOTE" and e["id"] == "M-MKT-1" for e in ents):
        registry.append(reg, "NOTE", "M-MKT-1", {"note": "The first run of exp_market fitted ONE pooled incremental coefficient c across the three families, contrary to the preregistered 'one coefficient per "
                                                          "family'. Its RESULT entry (seq earlier) is retained as history and SUPERSEDED by revision 2, rerun with per-family coefficients and no other change."}, repo)
    fam = res["families"]["V1"]
    wins = [f for f, d in fam.items() if d["inc_minus_mid"]["hi95"] < 0 and d["inc_minus_cal"]["hi95"] < 0]
    registry.append(reg, "RESULT", "M-MKT-1", {
        "metrics": {a: {f: {k: v for k, v in d.items()} for f, d in fs.items()} for a, fs in res["families"].items()},
        "revision": 2, "supersedes": "first M-MKT-1 RESULT (pooled coefficient)", "decision": "INCREMENTAL" if len(wins) >= 2 else "NO_INCREMENTAL_VALUE", "families_beating_both_baselines": wins,
        "interpretation": "see docs/research/nhl-model-improvement/MARKET_BASELINE_COMPARISON.md",
        "reproduction": "python -m nhl_edge.model_research.exp_market --repo . --derived <market-audit work dir> --out docs/research/nhl-model-improvement/data",
        "results_file": "docs/research/nhl-model-improvement/data/market_incremental.json"}, repo)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--derived", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    r = run(a.repo, a.derived)
    a.out.mkdir(parents=True, exist_ok=True)
    (a.out / "market_incremental.json").write_text(json.dumps(r, indent=1, default=float))
    record(r, a.repo, a.repo / "docs/research/nhl-model-improvement/experiment_registry.jsonl")
    for arm, fs in r["families"].items():
        for f, d in fs.items():
            print(arm, f, d["n_games"], {k: round(v, 4) for k, v in d["brier"].items()}, "inc-mid", round(d["inc_minus_mid"]["delta"], 4), [round(d["inc_minus_mid"]["lo95"], 4), round(d["inc_minus_mid"]["hi95"], 4)],
                  "model-mid", round(d["model_minus_mid"]["delta"], 4), "c", d["final_c"])
