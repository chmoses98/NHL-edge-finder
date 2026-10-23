"""WORKLOAD_V1 experiment driver: audit, validation grid, preregistered held-out evaluation (RESEARCH_ONLY; offline).

    python -m nhl_edge.research.workload_experiment audit    --season 2025 --out docs/research/workload_v1
    python -m nhl_edge.research.workload_experiment validate --season 2024 --out docs/research/workload_v1
    python -m nhl_edge.research.workload_experiment evaluate --season 2025 --prereg docs/research/workload_v1/preregistration.json

``audit`` / ``evaluate`` reuse champion frames cached as ``<cache>/champ_{sk,gl}_<season>.parquet`` (built on first use
with the production code paths, see ``workload_audit``). Arms are scored on exactly the same rows. Nothing is written
outside ``--out`` / ``--cache``; nothing here touches production, wagering or the archive.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
import time
from dataclasses import replace
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.research import workload_audit as A
from nhl_edge.research import workload_eval as E
from nhl_edge.research import workload_v1 as W

SOG_LADDER = [1, 2, 3, 4, 5]
SAVES_LADDER = list(range(14, 41))
WF_GAMES = "docs/research/walk_forward_v2_wf2_20260929_games.csv"
SEASONS = [2021, 2022, 2023, 2024, 2025]


class Ctx:
    def __init__(self, history: Path, cache: Path, wf_path: str = WF_GAMES):
        from nhl_edge.research.player_walk_forward import Data

        t0 = time.time()
        self.data = Data(history, SEASONS)
        self.wf = pd.read_csv(wf_path)
        self.cache = cache
        cache.mkdir(parents=True, exist_ok=True)
        d = self.data
        self.tg = W.team_games(d.players, d.team_states, d.shots, d.goals)
        self.sk = W.skater_table(d.players, self.tg, d.shots)
        print(f"context built in {time.time() - t0:.0f}s: {len(self.sk)} skater-games, {len(self.tg)} team-games", flush=True)

    def champ_sk(self, season: int) -> pd.DataFrame:
        f = self.cache / f"champ_sk_{season}.parquet"
        if not f.exists():
            A.champion_skaters(self.data, self.wf_for(season), season).to_parquet(f, index=False)
        return pd.read_parquet(f)

    def champ_gl(self, season: int) -> pd.DataFrame:
        f = self.cache / f"champ_gl_{season}.parquet"
        if not f.exists():
            A.champion_goalies(self.data, self.wf_for(season), season).to_parquet(f, index=False)
        return pd.read_parquet(f)

    def wf_for(self, season: int) -> pd.DataFrame:
        """V2 walk-forward rows (lambdas, penalty ratings) for the season; seasons the V2 walk-forward did not cover get
        neutral rows (only the champion's PP-share scaling reads them, and only for the alpha fit season)."""
        w = self.wf[self.wf["season"] == season]
        if len(w):
            return self.wf
        g = self.data.players[(self.data.players["season"] == season) & (self.data.players["game_type"] == 2)].drop_duplicates("game_id")
        neutral = pd.DataFrame({"game_id": g["game_id"], "season": season, "game_date": g["game_date"], "lam_st_home": 3.0, "lam_st_away": 3.0,
                                "ppmin_home": 4.3, "ppmin_away": 4.3, "home_pp_off": 1.0, "away_pp_off": 1.0, "home_pk_def": 1.0, "away_pk_def": 1.0})
        return pd.concat([self.wf, neutral], ignore_index=True)


# ---------------------------------------------------------------------------------------------------------------------
# skaters
# ---------------------------------------------------------------------------------------------------------------------
def _sk_frames(ctx: Ctx, seasons: list[int], prm: W.WorkloadParams, c: W.TrainedConstants) -> dict[int, pd.DataFrame]:
    pred = W.skater_predictions(ctx.sk, ctx.tg, c, prm)
    pred["base_sog"] = W.baseline_sog(pred).to_numpy()
    keep = ["game_id", "player_id", "share_ok"] + [f"wl_toi_{s}" for s in W.STATES_W] + ["wl_toi", "wl_sog", "wl_adj", "base_sog"] + \
        [f"wl_rate_{s}" for s in W.STATES_W] + [f"t_{s}" for s in W.STATES_W]
    out = {}
    for season in seasons:
        ps = pred[(pred["season"] == season) & (pred["game_type"] == 2)]
        m = ctx.champ_sk(season).merge(ps[keep], on=["game_id", "player_id"], how="inner")
        m["cw_sog"] = ((m["wl_toi_evreg"] + m["wl_toi_ot"]) * m["ch_rate_ev"] + m["wl_toi_pp"] * m["ch_rate_pp"] + m["wl_toi_sh"] * m["ch_rate_sh"]) / 60.0
        m["ce_sog"] = m["wl_adj"] * (m["ch_toi_ev"] * m["wl_rate_evreg"] + m["ch_toi_pp"] * m["wl_rate_pp"] + m["ch_toi_sh"] * m["wl_rate_sh"]) / 60.0
        out[season] = m
    return out


SK_ARMS = {"BASELINE": "base_sog", "CHAMPION": "ch_sog", "CHAMPION_NB": "ch_sog", "WORKLOAD_ONLY": "cw_sog", "EFFICIENCY_ONLY": "ce_sog", "WORKLOAD_V1": "wl_sog"}


def skater_arms(ctx: Ctx, season: int, prm: W.WorkloadParams, frames_hook: Any = None) -> tuple[pd.DataFrame, dict[str, np.ndarray], dict[str, float]]:
    """``frames_hook(frames, season)`` (research variants only, e.g. level calibration) may rewrite the per-season frames before scoring; the default
    path is unchanged."""
    train = [s for s in SEASONS if s < season]
    c = W.fit_constants(ctx.sk, ctx.tg, ctx.data.goalies, train)
    fr = _sk_frames(ctx, [season, season - 1], prm, c)
    if frames_hook is not None:
        fr = frames_hook(fr, season)
    m, prev = fr[season], fr[season - 1]  # dispersion of every NB arm: fit on the previous season's own residuals
    alphas = {a: (0.0 if a in ("BASELINE", "CHAMPION") else E.fit_nb_alpha(prev["y_sog"].to_numpy(), prev[col].to_numpy())) for a, col in SK_ARMS.items()}
    pmfs = {a: E.nb_pmf(m[col].to_numpy(), alphas[a], W.SOG_K) for a, col in SK_ARMS.items()}
    return m, pmfs, alphas | {"_constants": c.to_dict()}  # type: ignore[operator]


def skater_report(m: pd.DataFrame, pmfs: dict[str, np.ndarray], n_boot: int = 2000) -> dict[str, Any]:
    y = m["y_sog"].to_numpy()
    gid = m["game_id"].to_numpy()
    rows = {a: E.score_arm(p, y, SOG_LADDER) for a, p in pmfs.items()}
    out: dict[str, Any] = {"n_skater_games": int(len(m)), "n_games": int(m["game_id"].nunique()), "mean_actual": float(y.mean()),
                           "arms": {a: E.summarize(r) for a, r in rows.items()}}
    out["diffs"] = {f"{a}_minus_{b}": E.bootstrap_diff(gid, rows[a], rows[b], n_boot) for a, b in
                    (("WORKLOAD_V1", "CHAMPION"), ("WORKLOAD_V1", "CHAMPION_NB"), ("WORKLOAD_V1", "BASELINE"), ("WORKLOAD_ONLY", "CHAMPION_NB"),
                     ("EFFICIENCY_ONLY", "CHAMPION_NB"), ("CHAMPION_NB", "CHAMPION"), ("CHAMPION", "BASELINE"))}
    sub = {}
    for pos in ("F", "D"):
        k = (m["pos"] == pos).to_numpy()
        sub[pos] = {a: E.summarize({kk: v[k] for kk, v in rows[a].items()}) for a in ("CHAMPION", "CHAMPION_NB", "WORKLOAD_V1")}
    for flag in (False, True):
        k = (m["game_ot"] == flag).to_numpy()
        sub["ot_games" if flag else "regulation_games"] = {a: E.summarize({kk: v[k] for kk, v in rows[a].items()}) for a in ("CHAMPION", "CHAMPION_NB", "WORKLOAD_V1")}
    out["subgroups"] = sub
    # workload accuracy (minutes), shift-chart rows only
    w = m[m["shifts_ok"].fillna(False).astype(bool)]
    g2 = w["game_id"].to_numpy()
    tw = {}
    pairs = {"total": ("ch_toi", "wl_toi", w["y_toi"]), "pp": ("ch_toi_pp", "wl_toi_pp", w["y_toi_pp"]), "sh": ("ch_toi_sh", "wl_toi_sh", w["y_toi_sh"]),
             "ev_incl_ot": ("ch_toi_ev", None, w["y_toi_ev"])}
    for k, (ccol, wcol, yv) in pairs.items():
        ch_e = w[ccol] - yv
        wl_e = (w[wcol] if wcol else w["wl_toi_evreg"] + w["wl_toi_ot"]) - yv
        tw[k] = {"champion": {"mae": float(ch_e.abs().mean()), "rmse": float(np.sqrt((ch_e**2).mean())), "bias": float(ch_e.mean())},
                 "workload_v1": {"mae": float(wl_e.abs().mean()), "rmse": float(np.sqrt((wl_e**2).mean())), "bias": float(wl_e.mean())},
                 "mae_diff_wl_minus_champion": E.bootstrap_mean_diff(g2, (wl_e.abs() - ch_e.abs()).to_numpy(), n_boot)}
    out["workload_minutes"] = tw | {"n_skater_games": int(len(w))}
    # efficiency: shots given the ACTUAL minutes (oracle workload), each arm's own rates
    ch_or = sum(w[f"y_toi_{s}"] * w[f"ch_rate_{s}"] for s in A.SOG_STATES) / 60.0
    wl_or = w["wl_adj"] * sum(w[f"t_{s}"].fillna(0) / 60.0 * w[f"wl_rate_{s}"] for s in W.STATES_W) / 60.0
    yw = w["y_sog"]
    eff = {}
    for name, pr in (("champion_rates", ch_or), ("workload_v1_rates", wl_or)):
        e = pr - yw
        eff[name] = {"mae": float(e.abs().mean()), "rmse": float(np.sqrt((e**2).mean())), "bias": float(e.mean()),
                     "poisson_deviance": float(np.mean(2 * (np.where(yw > 0, yw * np.log(np.maximum(yw, 1e-9) / np.maximum(pr, 1e-6)), 0) - (yw - pr))))}
    eff["sq_err_diff_wl_minus_champion"] = E.bootstrap_mean_diff(g2, ((wl_or - yw) ** 2 - (ch_or - yw) ** 2).to_numpy(), n_boot)
    out["efficiency_given_actual_minutes"] = eff
    return out


# ---------------------------------------------------------------------------------------------------------------------
# goalies
# ---------------------------------------------------------------------------------------------------------------------
def goalie_arms(ctx: Ctx, season: int, prm: W.WorkloadParams) -> tuple[pd.DataFrame, dict[str, np.ndarray], dict[str, Any]]:
    train = [s for s in SEASONS if s < season]
    c = W.fit_constants(ctx.sk, ctx.tg, ctx.data.goalies, train)
    sa = W.team_sa_expectation(ctx.tg, c, prm)
    tg = ctx.tg.merge(sa, on=["game_id", "team_id"], how="left")
    prev = tg[(tg["season"] == season - 1) & (tg["game_type"] == 2)]
    alpha_sa = E.fit_nb_alpha((prev["sa_reg"] + prev["sa_ot"]).to_numpy(), prev["E_sa_net"].to_numpy())
    sv = W.goalie_sv(ctx.data.goalies, prm)
    gl = ctx.champ_gl(season)
    m = gl.merge(tg[["game_id", "team_id", "E_sa_net", "sa_rate", "lg"]], on=["game_id", "team_id"], how="left").merge(sv, on=["game_id", "player_id"], how="left")
    m["sv_hat"] = m["sv_hat"].fillna(m["lg_sv"])
    ch_sv = (m["ch_saves"] / m["ch_faced_starter"].clip(lower=1e-6)).to_numpy()
    pmfs = {"BASELINE": E.poisson_pmf((m["sa_rate"] * m["lg_sv"]).to_numpy(), W.SAVES_K),
            "CHAMPION": np.vstack(m["ch_pmf"].to_numpy()).astype(float),
            "WORKLOAD_ONLY": W.goalie_saves_pmf(m["E_sa_net"].to_numpy(), alpha_sa, ch_sv, c),
            "EFFICIENCY_ONLY": W.goalie_saves_pmf(m["expected_faced"].to_numpy(), alpha_sa, m["sv_hat"].to_numpy(), c),
            "WORKLOAD_V1": W.goalie_saves_pmf(m["E_sa_net"].to_numpy(), alpha_sa, m["sv_hat"].to_numpy(), c)}
    m["wl_e_sa_start"] = m["E_sa_net"] * (1 - c.p_pull * (1 - c.f_pull))
    return m, pmfs, {"alpha_sa": alpha_sa, "constants": c.to_dict()}


def goalie_report(m: pd.DataFrame, pmfs: dict[str, np.ndarray], n_boot: int = 2000) -> dict[str, Any]:
    y = m["y_saves"].to_numpy()
    gid = m["game_id"].to_numpy()
    rows = {a: E.score_arm(p, y, SAVES_LADDER) for a, p in pmfs.items()}
    out: dict[str, Any] = {"label": A.LABEL_STARTER, "n_starts": int(len(m)), "n_games": int(m["game_id"].nunique()), "mean_actual": float(y.mean()),
                           "arms": {a: E.summarize(r) for a, r in rows.items()}}
    out["diffs"] = {f"{a}_minus_{b}": E.bootstrap_diff(gid, rows[a], rows[b], n_boot) for a, b in
                    (("WORKLOAD_V1", "CHAMPION"), ("WORKLOAD_V1", "BASELINE"), ("WORKLOAD_ONLY", "CHAMPION"), ("EFFICIENCY_ONLY", "CHAMPION"),
                     ("CHAMPION", "BASELINE"))}
    # workload: shots the starter faced
    ch_e = m["ch_faced_starter"] - m["y_sa"]
    wl_e = m["wl_e_sa_start"] - m["y_sa"]
    out["workload_shots_faced"] = {"champion": {"mae": float(ch_e.abs().mean()), "rmse": float(np.sqrt((ch_e**2).mean())), "bias": float(ch_e.mean())},
                                   "workload_v1": {"mae": float(wl_e.abs().mean()), "rmse": float(np.sqrt((wl_e**2).mean())), "bias": float(wl_e.mean())},
                                   "sq_err_diff_wl_minus_champion": E.bootstrap_mean_diff(gid, (wl_e**2 - ch_e**2).to_numpy(), n_boot)}
    # efficiency: saves given the ACTUAL shots faced
    ch_sv = m["ch_saves"] / m["ch_faced_starter"].clip(lower=1e-6)
    eff = {}
    for name, sv in (("champion_implied_sv", ch_sv), ("workload_v1_goalie_sv", m["sv_hat"]), ("league_sv", m["lg_sv"])):
        e = m["y_sa"] * sv - m["y_saves"]
        eff[name] = {"mae": float(e.abs().mean()), "rmse": float(np.sqrt((e**2).mean())), "bias": float(e.mean())}
    eff["sq_err_diff_wl_minus_champion"] = E.bootstrap_mean_diff(gid, ((m["y_sa"] * m["sv_hat"] - m["y_saves"]) ** 2 - (m["y_sa"] * ch_sv - m["y_saves"]) ** 2).to_numpy(), n_boot)
    out["efficiency_given_actual_shots"] = eff
    sub = {}
    for flag in (False, True):
        k = (m["game_ot"] == flag).to_numpy()
        sub["ot_games" if flag else "regulation_games"] = {a: E.summarize({kk: v[k] for kk, v in rows[a].items()}) for a in ("CHAMPION", "WORKLOAD_V1")}
    out["subgroups"] = sub
    return out


# ---------------------------------------------------------------------------------------------------------------------
# acceptance (frozen in the preregistration)
# ---------------------------------------------------------------------------------------------------------------------
def accept_skaters(rep: dict[str, Any], rule: dict[str, Any]) -> dict[str, Any]:
    d1, d2 = rep["diffs"]["WORKLOAD_V1_minus_CHAMPION"], rep["diffs"]["WORKLOAD_V1_minus_CHAMPION_NB"]
    a = rep["arms"]["WORKLOAD_V1"]
    checks = {
        "crps_vs_champion_ci_upper_lt_0": d1["crps"]["ci95"][1] < 0,
        "crps_vs_champion_nb_ci_upper_lt_0": d2["crps"]["ci95"][1] < 0,
        "rmse_vs_champion_ci_upper_lt_0": d1["rmse"]["ci95"][1] < 0,
        "ladder_brier_vs_champion_nb_ci_upper_lt_0": d2["ladder_brier"]["ci95"][1] < 0,
        "abs_bias_le_max": abs(a["bias"]) <= rule["max_abs_bias_sog"],
        "coverage80_in_band": rule["coverage80_band"][0] <= a["coverage80"] <= rule["coverage80_band"][1],
        "no_position_worse_crps": all(rep["subgroups"][p]["WORKLOAD_V1"]["crps"] <= rep["subgroups"][p]["CHAMPION_NB"]["crps"] for p in ("F", "D")),
    }
    return {"checks": checks, "verdict": "ACCEPTED" if all(checks.values()) else "REJECTED"}


def accept_goalies(rep: dict[str, Any], rule: dict[str, Any]) -> dict[str, Any]:
    d1 = rep["diffs"]["WORKLOAD_V1_minus_CHAMPION"]
    a = rep["arms"]["WORKLOAD_V1"]
    checks = {
        "crps_vs_champion_ci_upper_lt_0": d1["crps"]["ci95"][1] < 0,
        "rmse_vs_champion_ci_upper_lt_0": d1["rmse"]["ci95"][1] < 0,
        "ladder_brier_vs_champion_ci_upper_lt_0": d1["ladder_brier"]["ci95"][1] < 0,
        "abs_bias_le_max": abs(a["bias"]) <= rule["max_abs_bias_saves"],
        "coverage80_in_band": rule["coverage80_band"][0] <= a["coverage80"] <= rule["coverage80_band"][1],
    }
    return {"checks": checks, "verdict": "ACCEPTED" if all(checks.values()) else "REJECTED"}


# ---------------------------------------------------------------------------------------------------------------------
# validation grid (2024-25 only)
# ---------------------------------------------------------------------------------------------------------------------
SK_GRID = {"minutes_mode": ["share", "direct"], "hl_share": [4.0, 8.0], "hl_rate": [30.0, 80.0], "beta_opp": [0.0, 0.5, 1.0], "league_rows": [10000, 30000]}
GL_GRID = {"hl_sa": [15.0, 25.0, 40.0], "schedule_adjust": [False, True], "k_sv": [1000.0, 3000.0], "league_window_sa": [400, 1200]}


def validate(ctx: Ctx, season: int) -> dict[str, Any]:
    res_sk = []
    for combo in itertools.product(*SK_GRID.values()):
        kw = dict(zip(SK_GRID, combo))
        prm = replace(W.WorkloadParams(), **kw)
        m, pmfs, _ = skater_arms(ctx, season, prm)
        r = E.summarize(E.score_arm(pmfs["WORKLOAD_V1"], m["y_sog"].to_numpy(), SOG_LADDER))
        res_sk.append(kw | r)
        print("sk", res_sk[-1], flush=True)
    res_gl = []
    for combo in itertools.product(*GL_GRID.values()):
        kw = dict(zip(GL_GRID, combo))
        prm = replace(W.WorkloadParams(), **kw)
        m, pmfs, _ = goalie_arms(ctx, season, prm)
        r = E.summarize(E.score_arm(pmfs["WORKLOAD_V1"], m["y_saves"].to_numpy(), SAVES_LADDER))
        res_gl.append(kw | r)
        print("gl", res_gl[-1], flush=True)
    best_sk = min(res_sk, key=lambda r: r["crps"])
    best_gl = min(res_gl, key=lambda r: r["crps"])
    return {"season": season, "criterion": "lowest mean CRPS of WORKLOAD_V1 on the validation season", "skater_grid": res_sk, "goalie_grid": res_gl,
            "best_skater": best_sk, "best_goalie": best_gl}


def params_from_selection(sel: dict[str, Any]) -> W.WorkloadParams:
    s, g = sel["best_skater"], sel["best_goalie"]
    return replace(W.WorkloadParams(), **{k: s[k] for k in SK_GRID}, **{k: (bool(g[k]) if k == "schedule_adjust" else g[k]) for k in GL_GRID})


def _round(o: Any) -> Any:
    if isinstance(o, float):
        return round(o, 6)
    if isinstance(o, dict):
        return {str(k): _round(v) for k, v in o.items()}
    if isinstance(o, list | tuple):
        return [_round(v) for v in o]
    if isinstance(o, np.generic):
        return _round(o.item())
    return o


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.workload_experiment")
    ap.add_argument("mode", choices=["audit", "validate", "evaluate"])
    ap.add_argument("--season", type=int, required=True)
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--cache", default="out/workload_v1_cache")
    ap.add_argument("--out", default="docs/research/workload_v1")
    ap.add_argument("--prereg", default="docs/research/workload_v1/preregistration.json")
    ap.add_argument("--n-boot", type=int, default=2000)
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    ctx = Ctx(Path(a.history), Path(a.cache))
    if a.mode == "audit":
        sk, gl = ctx.champ_sk(a.season), ctx.champ_gl(a.season)
        heur = A.starter_heuristic(ctx.data.goalies, a.season)
        rep = {"season": a.season, "model": "PLAYER_SIM_V1 (production shadow arm), walk-forward", "skaters": A.skater_decomposition(sk),
               "goalies": A.goalie_decomposition(gl), "starting_goalie": A.starter_uncertainty(gl, heur, ctx.data.goalies)}
        (out / f"audit_{a.season}.json").write_text(json.dumps(_round(rep), indent=1))
    elif a.mode == "validate":
        sel = validate(ctx, a.season)
        (out / f"validation_{a.season}.json").write_text(json.dumps(_round(sel), indent=1))
    else:
        pre = json.loads(Path(a.prereg).read_text())
        if a.season != int(pre["held_out_season"]):
            raise SystemExit("evaluate runs only on the preregistered held-out season")
        prm = W.WorkloadParams.from_dict(pre["frozen_params"])
        m, pmfs, al = skater_arms(ctx, a.season, prm)
        rs = skater_report(m, pmfs, a.n_boot)
        rs["alphas"] = {k: v for k, v in al.items() if not k.startswith("_")}
        rs["acceptance"] = accept_skaters(rs, pre["acceptance"])
        mg, pg, ag = goalie_arms(ctx, a.season, prm)
        rg = goalie_report(mg, pg, a.n_boot)
        rg["alpha_sa"] = ag["alpha_sa"]
        rg["acceptance"] = accept_goalies(rg, pre["acceptance"])
        res = {"season": a.season, "model_version": W.MODEL_VERSION, "frozen_params": prm.to_dict(), "constants": al["_constants"],
               "goalie_constants": ag["constants"], "skaters": rs, "goalies": rg}
        (out / f"results_{a.season}.json").write_text(json.dumps(_round(res), indent=1))
        print(json.dumps(_round({"skaters": rs["acceptance"], "goalies": rg["acceptance"]}), indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
