"""Walk-forward comparison of DATA_ONLY_V1 and the DATA_ONLY_V2 candidate arms on IDENTICAL games (RESEARCH_ONLY).

HISTORICAL, NOT PROSPECTIVE. Test seasons default to MoneyPuck 2024 and 2025 (NHL 2024-25, 2025-26): the exact games
of WALK_FORWARD_V1. For each test season S every V2 parameter is fitted on data strictly before S (nested
chronological validation; docs/research/V2_RESEARCH.md lists the dates):

* sim hazards (``state_hazards``): shots seasons 2021 .. S-1;  p(OT decided before SO): NHL results seasons < S;
* shared-environment dispersion: chosen on season S-1 with hazards fitted on seasons < S-1 (total-goals log-lik);
* goalie prior strength K: chosen on season S-1 (goalie-game Poisson log-lik), talent itself strictly point-in-time.

Arms (all see the same V1 team ratings; every probability comes from ONE simulator draw per arm):

    V1            DATA_ONLY_V1: V1 lambdas, goalie 1.0, nhl-sim-1.1 (reproduces WALK_FORWARD_V1 exactly)
    SIM2          V1 lambdas, nhl-sim-2.0 (isolates the simulator change: OT / score state / empty net / periods)
    SIM2_ST       special-teams lambdas (nhl-features-2.0), goalie 1.0, nhl-sim-2.0     <- valid pregame arm
    V1_G1         V1 lambdas x V1-style goalie factors of the ACTUAL starters, nhl-sim-1.1   (oracle starters)
    SIM2_ST_GTT   SIM2_ST x goalie true talent of the ACTUAL starters                         (oracle starters)

The two goalie arms use the starter who actually played (first goalie to face a shot): that is RETROSPECTIVE
ORACLE-STYLE analysis, not a valid pregame backtest, because historical starter confirmation timing is not
available. They answer "given the right starter, does the V2 goalie rating help?" and nothing more.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge import AUTHORITY
from nhl_edge.data.history import load_nhl_games, load_team_games
from nhl_edge.data.shots import load_shots
from nhl_edge.evaluation.metrics import brier, ece, log_loss
from nhl_edge.features import goalie_talent as gt
from nhl_edge.features import special_teams as stm
from nhl_edge.features.ratings import expected_goals, last_game_date, league_rates, rest_days, team_rating
from nhl_edge.log import get_logger, kv
from nhl_edge.research import state_hazards as sh
from nhl_edge.research.walk_forward import attach_outcomes, build_gamelog, evaluation_games, game_seed
from nhl_edge.sim.engine import SimConfig, TeamParams, simulate_game
from nhl_edge.sim.engine_v2 import SIM_V2_VERSION, SimV2Params, simulate_game_v2
from nhl_edge.timeutil import utcnow

log = get_logger(__name__)

ARMS = ("V1", "SIM2", "SIM2_ST", "V1_G1", "SIM2_ST_GTT")
ORACLE_ARMS = ("V1_G1", "SIM2_ST_GTT")
TOTAL_LINES = (4.5, 5.5, 6.5, 7.5)
ENV_GRID = (0.0, 0.015, 0.03, 0.05)
GOALIE_K_GRID = (300.0, 700.0, 1000.0, 1500.0, 2500.0)
BANNER = ("HISTORICAL, NOT PROSPECTIVE. Walk-forward replay on past seasons with every V2 parameter fitted on earlier "
          "seasons only. Goalie arms use the actual starter (retrospective oracle), not a pregame backtest.")


# --------------------------------------------------------------------------------------------------------------
# parameter fitting (all on seasons strictly before the scored one)
# --------------------------------------------------------------------------------------------------------------
def fit_sim_params(shots: pd.DataFrame, nhl_games: pd.DataFrame, train_seasons: Sequence[int], env_dispersion: float = 0.0,
                   scale_seed: int = 7) -> SimV2Params:
    tr = [int(s) for s in train_seasons]
    hd = sh.build_hazard_data(shots, tr)
    m, info = sh.fit_multipliers(hd, sh.team_game_rates(shots, tr))
    ng = nhl_games[nhl_games["season"].isin(tr) & (nhl_games["game_type"] == 2) & nhl_games["final"].astype(bool)]
    lp = ng["last_period_type"].value_counts()
    n_ot, n_so = int(lp.get("OT", 0)), int(lp.get("SO", 0))
    p_ot_goal = (n_ot + 0.66 * 50) / (n_ot + n_so + 50) if (n_ot + n_so) else 0.66
    prm = SimV2Params(mult=tuple(tuple(float(x) for x in r) for r in m), env_dispersion=float(env_dispersion), p_ot_goal=float(p_ot_goal))
    # scale: at a league-average matchup the simulator's mean regulation goals per team equals the input lambda
    lam = 3.0
    r = simulate_game_v2(TeamParams(1, "H", lam), TeamParams(2, "A", lam), seed=scale_seed, n_sims=200_000, params=prm)
    scale = lam / float((r.home_reg.mean() + r.away_reg.mean()) / 2)
    return prm.replace(scale=float(scale), provenance={
        "sim_version": SIM_V2_VERSION, "train_shots_seasons": tr, "train_nhl_result_seasons": sorted(int(x) for x in ng["season"].unique()),
        "n_team_games": info["n_team_games"], "goals": info["goals"], "shrink_pseudo_goals": info["shrink_pseudo_goals"],
        "raw_exposure_weighted_mean": info["raw_exposure_weighted_mean"], "p_ot_goal_counts": {"OT": n_ot, "SO": n_so},
        "goals_by_cell": info["goals_by_cell"], "fitted_at_utc": utcnow().isoformat(timespec="seconds")})


def total_loglik(res: Any, total: int) -> float:
    return float(np.log(max(np.mean(res.total == total), 1.0 / (res.n_sims * 10))))


# --------------------------------------------------------------------------------------------------------------
# per-game features
# --------------------------------------------------------------------------------------------------------------
@dataclass
class Ctx:
    log_df: pd.DataFrame
    team_logs: dict[str, pd.DataFrame]
    st_df: pd.DataFrame
    st_logs: dict[str, pd.DataFrame]
    glog: pd.DataFrame
    starters: dict[tuple[int, int], int]  # (game_id, is_home) -> goalie id (actual starter)


def game_features(ctx: Ctx, r: Any, book: gt.GoalieBook | None, league_cache: dict, lst_cache: dict) -> dict[str, Any]:
    date, season, home, away, gid = str(r.game_date), int(r.season), str(r.home_abbrev), str(r.away_abbrev), int(r.game_id)
    key = (date, season)
    lg = league_cache.get(key) or league_cache.setdefault(key, league_rates(ctx.log_df, date, season=season))
    lst = lst_cache.get(key) or lst_cache.setdefault(key, stm.league_st(ctx.st_df, date, season))
    hl, al = ctx.team_logs.get(home, ctx.log_df), ctx.team_logs.get(away, ctx.log_df)
    hr = team_rating(hl, home, date, lg, current_season=season)
    ar = team_rating(al, away, date, lg, current_season=season)
    h_rest = rest_days(last_game_date(hl, home, date), date)
    a_rest = rest_days(last_game_date(al, away, date), date)
    hb, ab = h_rest == 1, a_rest == 1
    lam_h, lam_a, _ = expected_goals(hr, ar, lg, home_b2b=hb, away_b2b=ab)
    hst = stm.team_st(ctx.st_logs.get(home, ctx.st_df), home, date, lst, season)
    ast = stm.team_st(ctx.st_logs.get(away, ctx.st_df), away, date, lst, season)
    sth, sta, comp = stm.expected_goals_v2(hr, ar, hst, ast, lg, lst, home_b2b=hb, away_b2b=ab)
    out = {"game_id": gid, "season": season, "game_date": date, "home": home, "away": away, "lam_v1_home": lam_h, "lam_v1_away": lam_a,
           "lam_st_home": sth, "lam_st_away": sta, "ppmin_home": comp.get("ppmin_home"), "ppmin_away": comp.get("ppmin_away"),
           "home_pp_off": hst.pp_off, "away_pp_off": ast.pp_off, "home_pk_def": hst.pk_def, "away_pk_def": ast.pk_def,
           "home_draw": hst.draw, "away_draw": ast.draw, "home_take": hst.take, "away_take": ast.take}
    hg, ag = ctx.starters.get((gid, 1)), ctx.starters.get((gid, 0))
    out["home_starter"], out["away_starter"] = hg, ag
    if book is not None:
        lr = book.league_ratio(date)
        th, ta = book.talent(hg, date, lr), book.talent(ag, date, lr)
        out.update({"home_gtt": th.factor * th.workload_mult, "away_gtt": ta.factor * ta.workload_mult, "home_g_apps": th.apps_used, "away_g_apps": ta.apps_used,
                    "home_g_b2b": th.b2b, "away_g_b2b": ta.b2b,
                    "home_gv1": gt.v1_style_factor(ctx.glog, hg, season) if hg else 1.0, "away_gv1": gt.v1_style_factor(ctx.glog, ag, season) if ag else 1.0})
    return out


def select_params(ctx: Ctx, shots: pd.DataFrame, nhl_games: pd.DataFrame, S: int, league_cache: dict, lst_cache: dict,
                  env_grid: Sequence[float] = ENV_GRID, k_grid: Sequence[float] = GOALIE_K_GRID) -> dict[str, Any]:
    """Every V2 parameter for scoring season ``S``, fitted on seasons < S (validation season S-1, see module doc)."""
    val = S - 1
    prm_val = fit_sim_params(shots, nhl_games, [s for s in range(2021, val)])
    val_games, _ = evaluation_games(nhl_games, [val])
    vfeat = [game_features(ctx, r, None, league_cache, lst_cache) for r in val_games.itertuples(index=False)]
    vtot = dict(zip(val_games["game_id"].astype(int), (val_games["home_score"] + val_games["away_score"]).astype(int)))
    env_scores = {}
    for e in env_grid:
        p = prm_val.replace(env_dispersion=float(e))
        ll = 0.0
        for f in vfeat:
            res = simulate_game_v2(TeamParams(0, f["home"], f["lam_st_home"]), TeamParams(0, f["away"], f["lam_st_away"]), game_seed(f["game_id"]), 2000, p)
            ll += total_loglik(res, vtot[f["game_id"]])
        env_scores[str(e)] = round(ll / max(len(vfeat), 1), 5)
    env_best = float(max(env_scores, key=lambda k: env_scores[k]))
    gk = gt.choose_prior(ctx.glog, val, tuple(k_grid))
    prm = fit_sim_params(shots, nhl_games, [s for s in range(2021, S)], env_dispersion=env_best)
    b2b = gt.estimate_b2b(ctx.glog, [s for s in range(2022, S)], gk["best_prior_xg"])
    book = gt.GoalieBook(ctx.glog, prior_xg=gk["best_prior_xg"], b2b_mult=b2b["b2b_mult"])
    return {"prm": prm, "book": book, "env": env_best, "env_scores": env_scores, "goalie_prior": gk, "b2b": b2b}


def load_ctx(history: Path) -> tuple[Ctx, pd.DataFrame, pd.DataFrame]:
    team_games = load_team_games(history)
    nhl_games = load_nhl_games(history)
    shots = load_shots(history)
    log_df = build_gamelog(team_games)
    st_df = stm.prepare_situation_log(team_games[team_games["game_type"] == 2])
    glog = gt.goalie_game_log(shots, nhl_games)
    starters = {(int(r.game_id), int(r.def_home)): int(r.goalie_id) for r in glog[glog["starter"] == 1].itertuples(index=False)}
    return Ctx(log_df, {t: d for t, d in log_df.groupby("team")}, st_df, {t: d for t, d in st_df.groupby("team")}, glog, starters), nhl_games, shots


def _probs(res: Any, prefix: str, total_lines: Sequence[float], y_total: int | None) -> dict[str, float]:
    d = {f"{prefix}p_home_win": res.p_win(True)[0], f"{prefix}p_home_reg_win": res.p_reg_win(True)[0], f"{prefix}p_away_reg_win": res.p_reg_win(False)[0],
         f"{prefix}p_reg_tie": res.p_reg_tie()[0], f"{prefix}p_overtime": res.p_overtime()[0], f"{prefix}expected_total": float(res.total.mean()),
         f"{prefix}p_home_minus_1_5": res.p_margin_gt(True, 1.5)[0], f"{prefix}p_away_minus_1_5": res.p_margin_gt(False, 1.5)[0],
         f"{prefix}exp_home": float(res.home_final.mean()), f"{prefix}exp_away": float(res.away_final.mean())}
    for x in total_lines:
        d[f"{prefix}p_over_{x}"] = res.p_total_gt(x)[0]
    for x in (2.5, 3.5):
        d[f"{prefix}p_home_over_{x}"] = res.p_team_total_gt(True, x)[0]
        d[f"{prefix}p_away_over_{x}"] = res.p_team_total_gt(False, x)[0]
    if y_total is not None:
        d[f"{prefix}ll_total"] = total_loglik(res, int(y_total))
    if hasattr(res, "home_periods") and res.home_periods is not None:
        for p in (1, 2, 3):
            h, a = res.period_goals(p, True), res.period_goals(p, False)
            d[f"{prefix}p{p}_home_win"] = float(np.mean(h > a))
            d[f"{prefix}p{p}_tie"] = float(np.mean(h == a))
            d[f"{prefix}p{p}_over_1_5"] = float(np.mean(h + a > 1.5))
            d[f"{prefix}p{p}_exp_total"] = float((h + a).mean())
    return d


# --------------------------------------------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------------------------------------------
def run(history: Path, test_seasons: Sequence[int] = (2024, 2025), n_sims: int = 4000, max_games: int | None = None,
        env_grid: Sequence[float] = ENV_GRID, k_grid: Sequence[float] = GOALIE_K_GRID) -> tuple[pd.DataFrame, dict[str, Any]]:
    t0 = time.time()
    ctx, nhl_games, shots = load_ctx(history)
    games, skipped = evaluation_games(nhl_games, test_seasons)
    reg_by_game = _regulation_by_period(shots)
    report: dict[str, Any] = {"banner": BANNER, "authority": AUTHORITY, "generated_at_utc": utcnow().isoformat(timespec="seconds"), "arms": list(ARMS),
                              "oracle_arms": list(ORACLE_ARMS), "n_sims": n_sims, "test_seasons": list(test_seasons), "skipped": skipped, "fits": {}}
    recs: list[dict[str, Any]] = []
    league_cache: dict = {}
    lst_cache: dict = {}
    for S in test_seasons:
        S = int(S)
        # --- nested parameter selection -------------------------------------------------------------------
        fit = select_params(ctx, shots, nhl_games, S, league_cache, lst_cache, env_grid, k_grid)
        prm, book, env_best, env_scores, gk, b2b, val = fit["prm"], fit["book"], fit["env"], fit["env_scores"], fit["goalie_prior"], fit["b2b"], S - 1
        report["fits"][str(S)] = {"validation_season": val, "env_loglik_per_game": env_scores, "env_dispersion": env_best,
                                  "goalie_prior": gk, "goalie_b2b": b2b, "sim_params": prm.to_dict(),
                                  "hazard_train_seasons_for_validation": [s for s in range(2021, val)]}
        log.info(kv(event="v2_fit", season=S, env=env_best, goalie_k=gk["best_prior_xg"], p_ot_goal=round(prm.p_ot_goal, 3), scale=round(prm.scale, 4)))
        # --- score the test season -----------------------------------------------------------------------
        gs = games[games["season"] == S]
        if max_games:
            gs = gs.iloc[: int(max_games)]
        cfg = SimConfig(n_sims=int(n_sims))
        for i, r in enumerate(gs.itertuples(index=False)):
            f = game_features(ctx, r, book, league_cache, lst_cache)
            seed = game_seed(f["game_id"])
            y_total = int(r.home_score) + int(r.away_score)
            H = lambda lam, ab=f["home"]: TeamParams(0, ab, lam)  # noqa: E731
            A = lambda lam, ab=f["away"]: TeamParams(0, ab, lam)  # noqa: E731
            rec = dict(f)
            rec.update(_probs(simulate_game(H(f["lam_v1_home"]), A(f["lam_v1_away"]), seed, cfg), "V1_", TOTAL_LINES, y_total))
            rec.update(_probs(simulate_game_v2(H(f["lam_v1_home"]), A(f["lam_v1_away"]), seed, n_sims, prm), "SIM2_", TOTAL_LINES, y_total))
            rec.update(_probs(simulate_game_v2(H(f["lam_st_home"]), A(f["lam_st_away"]), seed, n_sims, prm), "SIM2_ST_", TOTAL_LINES, y_total))
            gh1, ga1 = f.get("home_gv1", 1.0), f.get("away_gv1", 1.0)
            rec.update(_probs(simulate_game(H(f["lam_v1_home"] * ga1), A(f["lam_v1_away"] * gh1), seed, cfg), "V1_G1_", TOTAL_LINES, y_total))
            ght, gat = f.get("home_gtt", 1.0), f.get("away_gtt", 1.0)
            rec.update(_probs(simulate_game_v2(H(f["lam_st_home"] * gat), A(f["lam_st_away"] * ght), seed, n_sims, prm), "SIM2_ST_GTT_", TOTAL_LINES, y_total))
            recs.append(rec)
            if (i + 1) % 250 == 0:
                log.info(kv(event="wf2_progress", season=S, done=i + 1, total=len(gs), elapsed_s=round(time.time() - t0, 1)))
    df = attach_outcomes(pd.DataFrame(recs), games)
    per = pd.DataFrame(reg_by_game)
    df = df.merge(per, on="game_id", how="left")
    report["n_games"] = int(len(df))
    report["metrics"] = score_all(df)
    report["subgroups"] = subgroups(df)
    report["elapsed_s"] = round(time.time() - t0, 1)
    return df, report


def _regulation_by_period(shots: pd.DataFrame) -> list[dict[str, Any]]:
    g = sh.regulation_goals(shots)
    out = []
    piv = g.pivot_table(index="nhl_game_id", columns=["period", "isHomeTeam"], values="time", aggfunc="count", fill_value=0)
    all_games = shots[shots["isPlayoffGame"] == 0]["nhl_game_id"].unique()
    for gid in all_games:
        row = {"game_id": int(gid)}
        for p in (1, 2, 3):
            h = int(piv.loc[gid, (p, 1)]) if gid in piv.index and (p, 1) in piv.columns else 0
            a = int(piv.loc[gid, (p, 0)]) if gid in piv.index and (p, 0) in piv.columns else 0
            row[f"y_p{p}_home"], row[f"y_p{p}_away"] = h, a
        out.append(row)
    return out


def _bin(p: np.ndarray, y: np.ndarray) -> dict[str, Any]:
    return {"n": int(len(p)), "brier": brier(p, y), "log_loss": log_loss(p, y), "ece": ece(p, y, 10), "mean_p": float(np.mean(p)), "mean_y": float(np.mean(y))}


def score_all(df: pd.DataFrame) -> dict[str, Any]:
    out: dict[str, Any] = {}
    y_home = df["y_home_win"].astype(float).to_numpy()
    y_ot = df["y_overtime"].astype(float).to_numpy()
    tot = df["y_total"].astype(float).to_numpy()
    margin = (df["home_score"] - df["away_score"]).astype(float).to_numpy()
    reg_tot_known = df["y_p1_home"].notna()
    for arm in ARMS:
        p = f"{arm}_"
        m: dict[str, Any] = {"moneyline": _bin(df[p + "p_home_win"].to_numpy(), y_home), "overtime": _bin(df[p + "p_overtime"].to_numpy(), y_ot)}
        et = df[p + "expected_total"].to_numpy()
        m["total"] = {"mae": float(np.mean(np.abs(et - tot))), "bias": float(np.mean(et - tot)), "mean_expected": float(et.mean()), "mean_actual": float(tot.mean()),
                      "mean_loglik_exact_total": float(df[p + "ll_total"].mean())}
        m["totals"] = {str(x): _bin(df[f"{p}p_over_{x}"].to_numpy(), (tot > x).astype(float)) for x in TOTAL_LINES}
        m["puck_line"] = {"home_-1.5": _bin(df[p + "p_home_minus_1_5"].to_numpy(), (margin > 1.5).astype(float)),
                          "away_-1.5": _bin(df[p + "p_away_minus_1_5"].to_numpy(), (margin < -1.5).astype(float))}
        m["team_totals"] = {}
        for x in (2.5, 3.5):
            m["team_totals"][f"home_{x}"] = _bin(df[f"{p}p_home_over_{x}"].to_numpy(), (df["home_score"].to_numpy() > x).astype(float))
            m["team_totals"][f"away_{x}"] = _bin(df[f"{p}p_away_over_{x}"].to_numpy(), (df["away_score"].to_numpy() > x).astype(float))
        reg = df["y_overtime"] == 0
        m["regulation_winner"] = _bin(df.loc[reg, p + "p_home_reg_win"].to_numpy() / (1 - df.loc[reg, p + "p_reg_tie"].to_numpy()).clip(1e-9),
                                      df.loc[reg, "y_home_win"].astype(float).to_numpy())
        m["three_way_home_reg_win"] = _bin(df[p + "p_home_reg_win"].to_numpy(), ((df["y_overtime"] == 0) & (df["y_home_win"] == 1)).astype(float).to_numpy())
        if f"{p}p1_home_win" in df.columns:
            per = {}
            d = df[reg_tot_known]
            for q in (1, 2, 3):
                yh, ya = d[f"y_p{q}_home"].to_numpy(), d[f"y_p{q}_away"].to_numpy()
                per[f"P{q}"] = {"home_win": _bin(d[f"{p}p{q}_home_win"].to_numpy(), (yh > ya).astype(float)), "tie": _bin(d[f"{p}p{q}_tie"].to_numpy(), (yh == ya).astype(float)),
                                "over_1.5": _bin(d[f"{p}p{q}_over_1_5"].to_numpy(), (yh + ya > 1.5).astype(float)),
                                "exp_total": float(d[f"{p}p{q}_exp_total"].mean()), "actual_total": float((yh + ya).mean())}
            m["periods"] = per
        out[arm] = m
    return out


def subgroups(df: pd.DataFrame) -> dict[str, Any]:
    out: dict[str, Any] = {}
    y = df["y_home_win"].astype(float).to_numpy()
    if "home_gtt" in df.columns:
        gdiff = np.abs(np.log(df["home_gtt"].astype(float)) - np.log(df["away_gtt"].astype(float)))
        sel = gdiff >= np.quantile(gdiff, 0.75)
        out["goalie_sensitive_top_quartile"] = {a: _bin(df.loc[sel, f"{a}_p_home_win"].to_numpy(), y[sel]) for a in ARMS} | {"n": int(sel.sum()),
                                                                                                                        "definition": "|log home_gtt - log away_gtt| in top quartile (oracle starters)"}
    sdiff = np.abs(np.log(df["lam_st_home"] / df["lam_st_away"]) - np.log(df["lam_v1_home"] / df["lam_v1_away"]))
    sel = sdiff >= np.quantile(sdiff, 0.75)
    out["special_teams_extreme_top_quartile"] = {a: _bin(df.loc[sel, f"{a}_p_home_win"].to_numpy(), y[sel]) for a in ARMS} | {
        "n": int(sel.sum()), "definition": "|log(lam ratio ST) - log(lam ratio V1)| in top quartile"}
    for s, d in df.groupby("season"):
        yy = d["y_home_win"].astype(float).to_numpy()
        out[f"season_{int(s)}"] = {a: {"moneyline": _bin(d[f"{a}_p_home_win"].to_numpy(), yy),
                                       "overtime": _bin(d[f"{a}_p_overtime"].to_numpy(), d["y_overtime"].astype(float).to_numpy())} for a in ARMS}
    return out


def render(report: dict[str, Any], run_id: str) -> str:
    M = report["metrics"]
    f = lambda x, n=4: "-" if x is None else f"{x:.{n}f}"  # noqa: E731
    L = ["# DATA_ONLY_V2 candidate walk-forward (WALK_FORWARD_V2)", "", f"> **{report['banner']}**", "",
         f"Run `{run_id}` · {report['generated_at_utc']} · authority `{report['authority']}` · n = {report['n_games']} regular-season games "
         f"(test seasons {report['test_seasons']}, identical games for every arm) · {report['n_sims']} draws per arm per game · {report['elapsed_s']} s", "",
         "Arms: `V1` = DATA_ONLY_V1 (nhl-sim-1.1) · `SIM2` = V1 lambdas + nhl-sim-2.0 · `SIM2_ST` = special-teams lambdas + nhl-sim-2.0 (goalie 1.0; **valid pregame arm**) · "
         "`V1_G1` = V1 + V1-style goalie factor of the actual starter · `SIM2_ST_GTT` = SIM2_ST + goalie true talent of the actual starter. "
         "**The two goalie arms are retrospective oracle-style analysis** (actual starters), not a pregame backtest.", "",
         "## Moneyline (P(home win) incl. OT/SO)", "", "| arm | Brier | log loss | ECE | mean p | hit rate |", "|---|---:|---:|---:|---:|---:|"]
    for a in ARMS:
        m = M[a]["moneyline"]
        L.append(f"| {a} | {f(m['brier'])} | {f(m['log_loss'])} | {f(m['ece'])} | {f(m['mean_p'], 3)} | {f(m['mean_y'], 3)} |")
    L += ["", "## Regulation tie / OT", "", "| arm | predicted P(OT) | observed | Brier | log loss | ECE |", "|---|---:|---:|---:|---:|---:|"]
    for a in ARMS:
        m = M[a]["overtime"]
        L.append(f"| {a} | {f(m['mean_p'], 4)} | {f(m['mean_y'], 4)} | {f(m['brier'])} | {f(m['log_loss'])} | {f(m['ece'])} |")
    L += ["", "## Regulation winner (3-way home regulation win; and home win given no OT)", "", "| arm | 3-way Brier | 3-way LL | given-no-OT Brier | given-no-OT LL |", "|---|---:|---:|---:|---:|"]
    for a in ARMS:
        t, g = M[a]["three_way_home_reg_win"], M[a]["regulation_winner"]
        L.append(f"| {a} | {f(t['brier'])} | {f(t['log_loss'])} | {f(g['brier'])} | {f(g['log_loss'])} |")
    L += ["", "## Totals", "", "| arm | exp total | actual | bias | MAE | exact-total log-lik/game | O4.5 Brier | O5.5 Brier | O6.5 Brier | O7.5 Brier | O5.5 ECE | O6.5 ECE |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for a in ARMS:
        t, tt = M[a]["total"], M[a]["totals"]
        L.append(f"| {a} | {f(t['mean_expected'], 3)} | {f(t['mean_actual'], 3)} | {f(t['bias'], 3)} | {f(t['mae'], 3)} | {f(t['mean_loglik_exact_total'])} | "
                 f"{f(tt['4.5']['brier'])} | {f(tt['5.5']['brier'])} | {f(tt['6.5']['brier'])} | {f(tt['7.5']['brier'])} | {f(tt['5.5']['ece'])} | {f(tt['6.5']['ece'])} |")
    L += ["", "## Puck line and team totals (Brier)", "", "| arm | home -1.5 | away -1.5 | home o2.5 | home o3.5 | away o2.5 | away o3.5 |", "|---|---:|---:|---:|---:|---:|---:|"]
    for a in ARMS:
        pl, tt = M[a]["puck_line"], M[a]["team_totals"]
        L.append(f"| {a} | {f(pl['home_-1.5']['brier'])} | {f(pl['away_-1.5']['brier'])} | {f(tt['home_2.5']['brier'])} | {f(tt['home_3.5']['brier'])} | "
                 f"{f(tt['away_2.5']['brier'])} | {f(tt['away_3.5']['brier'])} |")
    L += ["", "## Periods (nhl-sim-2.0 arms only; outcomes from MoneyPuck goal times)", "", "| arm | period | exp total | actual | home-win Brier | tie Brier | over 1.5 Brier | tie mean p / rate |",
          "|---|---|---:|---:|---:|---:|---:|---|"]
    for a in ARMS:
        for q, pm in (M[a].get("periods") or {}).items():
            L.append(f"| {a} | {q} | {f(pm['exp_total'], 3)} | {f(pm['actual_total'], 3)} | {f(pm['home_win']['brier'])} | {f(pm['tie']['brier'])} | "
                     f"{f(pm['over_1.5']['brier'])} | {f(pm['tie']['mean_p'], 3)} / {f(pm['tie']['mean_y'], 3)} |")
    L += ["", "## Subgroups (moneyline Brier)", ""]
    for name, d in report["subgroups"].items():
        if name.startswith("season_"):
            continue
        L.append(f"- **{name}** (n={d['n']}; {d['definition']}): " + ", ".join(f"{a} {f(d[a]['brier'])}" for a in ARMS))
    L += ["", "| season | " + " | ".join(f"{a} ML Brier" for a in ARMS) + " | " + " | ".join(f"{a} OT Brier" for a in ARMS) + " |",
          "|---|" + "---:|" * (2 * len(ARMS))]
    for name, d in sorted(report["subgroups"].items()):
        if name.startswith("season_"):
            L.append(f"| {name[7:]} | " + " | ".join(f(d[a]['moneyline']['brier']) for a in ARMS) + " | " + " | ".join(f(d[a]['overtime']['brier']) for a in ARMS) + " |")
    L += ["", "## Fitted parameters (per test season; fitted on earlier seasons only)", ""]
    for s, fit in report["fits"].items():
        sp = fit["sim_params"]
        L.append(f"- test {s}: hazards from shots seasons {sp['provenance']['train_shots_seasons']}, p(OT goal | OT) = {sp['p_ot_goal']:.3f}, scale = {sp['scale']:.4f}, "
                 f"env dispersion = {fit['env_dispersion']} (validation {fit['validation_season']}: {fit['env_loglik_per_game']}), goalie prior K = {fit['goalie_prior']['best_prior_xg']} xG "
                 f"(validation log-lik {fit['goalie_prior']['loglik_by_prior_xg']}), goalie back-to-back multiplier {fit['goalie_b2b']['b2b_mult']} ({fit['goalie_b2b']['n_b2b_starts']} starts).")
    L += ["", f"> {report['banner']}", ""]
    return "\n".join(L)


def main(argv: Sequence[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.walk_forward_v2")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--out", default="docs/research")
    ap.add_argument("--test-seasons", default="2024,2025")
    ap.add_argument("--n-sims", type=int, default=4000)
    ap.add_argument("--max-games", type=int, default=None)
    ap.add_argument("--run", default=None)
    a = ap.parse_args(argv)
    run_id = a.run or utcnow().strftime("%Y%m%dT%H%M%SZ")
    df, report = run(Path(a.history), [int(s) for s in a.test_seasons.split(",")], n_sims=a.n_sims, max_games=a.max_games)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    report["run_id"] = run_id
    (out / f"walk_forward_v2_{run_id}.json").write_text(json.dumps(report, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o)))
    df.to_csv(out / f"walk_forward_v2_{run_id}_games.csv", index=False)
    (out / "WALK_FORWARD_V2.md").write_text(render(report, run_id))
    print(json.dumps({a_: report["metrics"][a_]["moneyline"]["brier"] for a_ in ARMS}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())


def fit_live_params(history: Path, out_dir: Path, season: int, use_special_teams: bool, goalie_model: str) -> dict[str, Any]:
    """Parameters for LIVE DATA_ONLY_V2 predictions in MoneyPuck season ``season`` (2026 == 2026-27), by the same nested
    procedure the walk-forward used: validation season ``season - 1``, hazards / p(OT goal) from every earlier season.
    ``use_special_teams`` / ``goalie_model`` are decided from the walk-forward results, never from the live season."""
    ctx, nhl_games, shots = load_ctx(history)
    fit = select_params(ctx, shots, nhl_games, int(season), {}, {})
    out_dir.mkdir(parents=True, exist_ok=True)
    sim = fit["prm"].to_dict()
    sim["provenance"] = sim["provenance"] | {"env_validation_season": season - 1, "env_loglik_per_game": fit["env_scores"], "for_mp_season": season}
    (out_dir / "nhl-sim-2.0.json").write_text(json.dumps(sim, indent=1))
    feat = {"feature_version": "nhl-features-2.0", "for_mp_season": season, "use_special_teams": bool(use_special_teams), "goalie_model": goalie_model,
            "goalie_prior_xg": fit["goalie_prior"]["best_prior_xg"], "goalie_prior_selection": fit["goalie_prior"],
            "goalie_b2b_mult": fit["b2b"]["b2b_mult"], "goalie_b2b_estimate": fit["b2b"], "fitted_at_utc": utcnow().isoformat(timespec="seconds")}
    (out_dir / "nhl-features-2.0.json").write_text(json.dumps(feat, indent=1))
    return {"sim": sim, "features": feat}
