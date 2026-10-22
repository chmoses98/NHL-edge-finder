"""Prediction-error attribution for the LIVE tier (151 games), classes A-F of the research brief.

Per game: the production V1 predictive distribution is regenerated bit-for-bit from the slate's (lam, seed, n_sims); the realised
score is placed in it (randomised PIT, win-probability surprise). An 'extreme' game is one whose total or margin PIT falls outside
[0.05, 0.95]; under a calibrated model about 19% of games are extreme by chance, which is the benchmark every count is compared with.

Class labels (heuristic, evidence strings kept; never forced):
  E normal variance        : not extreme
  C timing                 : extreme AND the goalie of record differs from the goalie named at the cut AND the confirmation was first public after the cut
  B missing information    : extreme AND goalie mismatch AND the correct goalie was public (source timestamp) before the cut
  D distributional         : extreme with no goalie explanation and a score in the far tail of the predictive pmf (PIT tail on total)
  F unresolved             : extreme, none of the above
  A systematic             : not a per-game label; a pattern flagged in wf_scan / exp_cal (reported at pattern level)
Ex-post decomposition (MoneyPuck team-game xG for the 2026 games, known only after the game; ex-post, NOT causal proof):
  goals - lam = (xG - lam) [shot volume/quality vs forecast] + (goals - xG) [finishing/goaltending luck].
"""

from __future__ import annotations

import glob
import gzip
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.model_research import scoring as S
from nhl_edge.model_research.wf_data import MARGIN_HI, MARGIN_LO, pmfs, simulate_row
from nhl_edge.sim.engine import SimConfig


def moneypuck_2026(archive: Path, last_date: str = "2026-10-20") -> pd.DataFrame:
    """Latest archived MoneyPuck team-game rows for 2026 games, situation 'all' (ex-post data; lineage = the snapshot path)."""
    files = sorted(glob.glob(str(archive / "context/team_games/dt=*/*.jsonl.gz")))
    files = [f for f in files if f.split("dt=")[1][:10] <= last_date]
    rows = [json.loads(line) for line in gzip.open(files[-1], "rt")]
    df = pd.DataFrame(rows)
    df = df[(df["season"] == 2026) & (df["situation"] == "all")]
    df = df.assign(game_id=df["gameId"].astype(int).astype(str), _snapshot=files[-1])
    return df


def regenerate(live: pd.DataFrame) -> list[dict[str, Any]]:
    out = []
    for r in live.itertuples():
        res = simulate_row(r.v1_lam_home, r.v1_lam_away, int(r.v1_seed), int(r.v1_n_sims), SimConfig(n_sims=int(r.v1_n_sims)))
        p = pmfs(res)
        out.append({"game_id": r.game_id, "p_home_win_regen": p["p_home_win"], "pmf_total": p["total"], "pmf_margin": p["margin"], "pmf_home": p["home"], "pmf_away": p["away"],
                    "mu_total": float(res.total.mean()), "sd_total": float(res.total.std()), "mu_margin": float(res.margin.mean()), "sd_margin": float(res.margin.std()),
                    "p_ot_regen": p["p_ot"]})
    return out


def run(live: pd.DataFrame, mp: pd.DataFrame, seed: int = 0) -> tuple[pd.DataFrame, dict[str, Any]]:
    rg = pd.DataFrame(regenerate(live)).set_index("game_id")
    d = live.set_index("game_id").join(rg[["p_home_win_regen", "mu_total", "sd_total", "mu_margin", "sd_margin", "p_ot_regen"]])
    rng = np.random.default_rng(seed)
    d["repro_abs_diff_p_home_win"] = (d["p_home_win_regen"] - d["v1_p_home_win"]).abs()
    y_m = (d["home_final"] - d["away_final"]).to_numpy()
    pm_t = np.stack(rg.loc[d.index, "pmf_total"].to_numpy())
    pm_m = np.stack(rg.loc[d.index, "pmf_margin"].to_numpy())
    d["pit_total"] = S.pit_randomized(pm_t, d["y_total"].to_numpy(), rng)
    d["pit_margin"] = S.pit_randomized(pm_m, np.clip(y_m, MARGIN_LO, MARGIN_HI) - MARGIN_LO, rng)
    d["p_outcome"] = np.where(d["y_home_win"] == 1, d["v1_p_home_win"], 1 - d["v1_p_home_win"])
    d["brier_v1"] = S.brier(d["v1_p_home_win"].to_numpy(), d["y_home_win"].to_numpy())
    d["rps_total"] = S.rps_from_pmf(pm_t, d["y_total"].to_numpy())
    ot = d["y_ot"].to_numpy().astype(bool)
    hw = (d["home_final"] > d["away_final"]).to_numpy()
    d["reg_home"] = d["home_final"] - (ot & hw)
    d["reg_away"] = d["away_final"] - (ot & ~hw)
    d["reg_total"] = d["reg_home"] + d["reg_away"]
    d["lam_total"] = d["v1_lam_home"] + d["v1_lam_away"]
    d["err_total_vs_lam"] = d["reg_total"] - d["lam_total"]
    # ex-post decomposition
    mpg = mp.groupby("game_id").agg(xg_total=("xGoalsFor", "sum"), goals_mp=("goalsFor", "sum"), shots_total=("shotsOnGoalFor", "sum"), hd_xg_total=("highDangerxGoalsFor", "sum"),
                                     n_rows=("team", "size"))
    d = d.join(mpg, how="left")
    d["has_xg"] = (d["n_rows"] == 2)
    d["volume_quality_err"] = d["xg_total"] - d["lam_total"]
    d["finishing_err"] = d["goals_mp"] - d["xg_total"]
    # goalie flags
    for side in ("home", "away"):
        d[f"{side}_goalie_mismatch"] = d[f"{side}_goalie_id"].astype(float) != d[f"actual_{side}_starter_id"].astype(float)
    d["any_goalie_mismatch"] = d["home_goalie_mismatch"] | d["away_goalie_mismatch"]
    labels, why = [], []
    for g in d.itertuples():
        extreme = (g.pit_total < 0.05) or (g.pit_total > 0.95) or (g.pit_margin < 0.05) or (g.pit_margin > 0.95)
        if not extreme:
            labels.append("E_normal_variance")
            why.append("")
            continue
        mism = [s for s in ("home", "away") if getattr(g, f"{s}_goalie_mismatch")]
        if mism:
            late = []
            for s in mism:
                rep = getattr(g, f"gobs_{s}_first_confirmed_reported_utc")
                obs = getattr(g, f"gobs_{s}_first_confirmed_obs_utc")
                t = rep if pd.notna(rep) else obs
                late.append(bool(pd.isna(t) or t > g.cut_utc))
            if all(late):
                labels.append("C_timing")
                why.append(f"goalie of record differed from the name at the cut ({'/'.join(mism)}); confirmation not public before the cut")
            else:
                labels.append("B_missing_information")
                why.append(f"correct goalie was public before the cut but the forecast used another ({'/'.join(mism)})")
            continue
        if (g.pit_total < 0.03) or (g.pit_total > 0.97):
            labels.append("D_distributional")
            why.append("total in the far tail of the predictive distribution, no goalie mismatch")
        else:
            labels.append("F_unresolved")
            why.append("extreme margin/total without a goalie or tail explanation")
    d["attribution_class"] = labels
    d["attribution_evidence"] = why
    n = len(d)
    extreme = (d["attribution_class"] != "E_normal_variance")
    chance = 1 - 0.9 * 0.9
    summ: dict[str, Any] = {"n_games": n, "reproduction_max_abs_diff_p_home_win": float(d["repro_abs_diff_p_home_win"].max()),
                            "class_counts": d["attribution_class"].value_counts().to_dict(),
                            "extreme_share": float(extreme.mean()), "extreme_share_expected_if_calibrated_approx": chance,
                            "pit_total_deciles": np.histogram(d["pit_total"], bins=10, range=(0, 1))[0].tolist(),
                            "pit_margin_deciles": np.histogram(d["pit_margin"], bins=10, range=(0, 1))[0].tolist(),
                            "mean_err_total_vs_lam": S.boot_mean_ci(d["err_total_vs_lam"].to_numpy()), "mean_brier_v1": float(d["brier_v1"].mean()),
                            "mean_rps_total": float(d["rps_total"].mean())}
    x = d[d["has_xg"]]
    summ["ex_post_decomposition"] = {
        "n_games_with_xg": int(len(x)),
        "var_err_total_vs_lam": float(x["err_total_vs_lam"].var()),
        "var_volume_quality_err": float(x["volume_quality_err"].var()), "var_finishing_err": float(x["finishing_err"].var()),
        "cov_vq_fin": float(np.cov(x["volume_quality_err"], x["finishing_err"])[0, 1]),
        "mean_volume_quality_err": S.boot_mean_ci(x["volume_quality_err"].to_numpy()), "mean_finishing_err": S.boot_mean_ci(x["finishing_err"].to_numpy()),
        "note": "ex-post; MoneyPuck xG excludes some goals (empty-net, shootout) so goals_mp is the MoneyPuck count, not the official goals; descriptive, not causal"}
    summ["goalie_mismatch"] = {"games_with_any_mismatch": int(d["any_goalie_mismatch"].sum()),
                               "extreme_share_when_mismatch": float(extreme[d["any_goalie_mismatch"]].mean()) if d["any_goalie_mismatch"].any() else None,
                               "extreme_share_when_match": float(extreme[~d["any_goalie_mismatch"]].mean())}
    return d.reset_index(), summ
