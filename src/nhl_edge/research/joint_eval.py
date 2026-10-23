"""Joint game-distribution validation of the simulators (RESEARCH_ONLY): win, overtime, shootout, margin and total scored TOGETHER.

The earlier V2 evidence scores the marginals separately (P(win), P(OT), the total pmf, the margin pmf). A simulator can pass each of those and still
mis-state how they hang together (a tie-heavy world has fewer decisive regulation wins and a different margin shape). This module scores the joint
distribution of one game on two partitions of the outcome space, both with proper scoring rules:

* **J_RESULT_MARGIN (10 cells)** - how the game ended and by how much: regulation home win by 1 / 2 / 3+, regulation away win by 1 / 2 / 3+, overtime home / away
  win, shootout home / away win. Overtime and shootout wins are decided by one goal in the official final, so margin only varies in regulation.
* **J_RESULT_TOTAL (36 cells)** - the same six result types x six total-goal buckets (<=3, 4, 5, 6, 7, 8+).

Scores per game: the multi-category Brier score (sum of squared cell errors) and the log score with a probability floor of ``FLOOR`` (Monte Carlo cells with
no draw would otherwise give -inf; the floor is applied identically to every arm). Plus the pooled reliability of every cell (predicted mass vs observed
count) and the overtime-conditional diagnostics (P(OT | regulation tie), P(shootout | tie)). The marginal metrics stay where they are
(``oa_evaluate``); the joint scores are additional gates, never a replacement.

Cells are built from simulator draws (``SimResult``: ``home_reg``, ``away_reg``, ``overtime``, ``shootout``, ``home_final``, ``away_final``), so any
simulator that returns that object can be scored. The observed cell comes from the official final (``home_score``, ``away_score``, ``last_period_type``).
"""

from __future__ import annotations

import numpy as np

FLOOR = 1e-3
TOTAL_BUCKETS = ("<=3", "4", "5", "6", "7", "8+")
RESULT_TYPES = ("REG_H", "REG_A", "OT_H", "OT_A", "SO_H", "SO_A")
MARGIN_CELLS = ("REG_H_1", "REG_H_2", "REG_H_3+", "REG_A_1", "REG_A_2", "REG_A_3+", "OT_H", "OT_A", "SO_H", "SO_A")
N_MARGIN = len(MARGIN_CELLS)
N_TOTAL = len(RESULT_TYPES) * len(TOTAL_BUCKETS)


def _bucket(total: np.ndarray) -> np.ndarray:
    return np.clip(np.asarray(total, int) - 3, 0, 5)       # <=3 -> 0, 4 -> 1, ..., >=8 -> 5


def _result_type(home_reg: np.ndarray, away_reg: np.ndarray, overtime: np.ndarray, shootout: np.ndarray, home_final: np.ndarray, away_final: np.ndarray) -> np.ndarray:
    """0..5 = RESULT_TYPES. OT/SO winners are read from the final score (the extra goal), regulation winners from the regulation score."""
    t = np.where(home_reg > away_reg, 0, 1)
    ot = np.asarray(overtime, bool)
    so = np.asarray(shootout, bool)
    home_won = np.asarray(home_final) > np.asarray(away_final)
    t = np.where(ot & ~so, np.where(home_won, 2, 3), t)
    t = np.where(so, np.where(home_won, 4, 5), t)
    return t


def _margin_cell(rtype: np.ndarray, reg_margin: np.ndarray) -> np.ndarray:
    m = np.clip(np.abs(np.asarray(reg_margin, int)), 1, 3)
    out = np.where(rtype == 0, m - 1, np.where(rtype == 1, 3 + m - 1, 4 + rtype))
    return out.astype(int)


def cells_from_draws(home_reg, away_reg, overtime, shootout, home_final, away_final) -> tuple[np.ndarray, np.ndarray]:
    """Probability vectors (10 margin cells, 36 total cells) from simulator draws."""
    rt = _result_type(np.asarray(home_reg), np.asarray(away_reg), overtime, shootout, home_final, away_final)
    mc = _margin_cell(rt, np.asarray(home_reg) - np.asarray(away_reg))
    tot = _bucket(np.asarray(home_final) + np.asarray(away_final))
    p_m = np.bincount(mc, minlength=N_MARGIN) / len(mc)
    p_t = np.bincount(rt * len(TOTAL_BUCKETS) + tot, minlength=N_TOTAL) / len(mc)
    return p_m, p_t


def cells_from_result(res) -> tuple[np.ndarray, np.ndarray]:
    return cells_from_draws(res.home_reg, res.away_reg, res.overtime, res.shootout, res.home_final, res.away_final)


def observed_cells(home_score: int, away_score: int, last_period_type: str) -> tuple[int, int]:
    """(margin cell, total cell) of an official final. In OT/SO games the regulation score is tied at the loser's score."""
    lpt = str(last_period_type)
    hs, as_ = int(home_score), int(away_score)
    if lpt == "SO":
        rt = 4 if hs > as_ else 5
        reg_margin = 0
    elif lpt == "OT":
        rt = 2 if hs > as_ else 3
        reg_margin = 0
    else:
        rt = 0 if hs > as_ else 1
        reg_margin = hs - as_
    mc = int(_margin_cell(np.array([rt]), np.array([reg_margin]))[0])
    return mc, int(rt * len(TOTAL_BUCKETS) + _bucket(np.array([hs + as_]))[0])


def brier_cat(p: np.ndarray, k: np.ndarray) -> np.ndarray:
    """Multi-category Brier per game: sum_c (p_c - 1[c==k])^2. ``p`` is (n, cells), ``k`` the observed cell index."""
    y = np.zeros_like(p)
    y[np.arange(len(k)), k] = 1.0
    return ((p - y) ** 2).sum(axis=1)


def logscore_cat(p: np.ndarray, k: np.ndarray, floor: float = FLOOR) -> np.ndarray:
    """Negative log probability of the observed cell, with the probability floored (identically for every arm). Lower is better."""
    q = np.maximum(p[np.arange(len(k)), k], floor)
    return -np.log(q)


def cell_reliability(p: np.ndarray, k: np.ndarray, names: tuple[str, ...]) -> list[dict[str, float]]:
    """Pooled predicted mass vs observed count per cell, with the z-score of (observed - expected) under independent Bernoulli(p_cell)."""
    n = len(k)
    exp = p.sum(axis=0)
    obs = np.bincount(k, minlength=p.shape[1]).astype(float)
    var = (p * (1 - p)).sum(axis=0)
    return [{"cell": names[i], "expected": float(exp[i]), "observed": float(obs[i]), "z": float((obs[i] - exp[i]) / np.sqrt(max(var[i], 1e-12))), "n": n} for i in range(p.shape[1])]


def total_cell_names() -> tuple[str, ...]:
    return tuple(f"{r}|{b}" for r in RESULT_TYPES for b in TOTAL_BUCKETS)


def overtime_conditionals(p_m: np.ndarray, k_m: np.ndarray) -> dict[str, float]:
    """P(OT/SO) and P(SO | OT/SO), predicted (mean over games) vs observed, from the 10-cell vectors."""
    ot_idx = [6, 7, 8, 9]
    so_idx = [8, 9]
    pred_tie = p_m[:, ot_idx].sum(axis=1)
    pred_so = p_m[:, so_idx].sum(axis=1)
    obs_tie = np.isin(k_m, ot_idx)
    obs_so = np.isin(k_m, so_idx)
    return {"pred_p_ot_or_so": float(pred_tie.mean()), "obs_p_ot_or_so": float(obs_tie.mean()),
            "pred_p_so_given_tie": float(pred_so.sum() / max(pred_tie.sum(), 1e-12)), "obs_p_so_given_tie": float(obs_so.sum() / max(obs_tie.sum(), 1))}


# ---------------------------------------------------------------------------------------------------------------------------------
# driver: walk-forward simulation with joint cells (same fits, features, seeds and draw counts as ``walk_forward_v2``)
# ---------------------------------------------------------------------------------------------------------------------------------
ARMS = ("V1", "SIM2", "SIM2_ST")


def run_joint(history, test_seasons, *, n_sims: int = 4000, first_shots_season: int = 2021, train_window: int | None = None, min_season: int | None = None,
              extra_shots_dir=None, extra_lams=None, max_games: int | None = None, collect=None):
    """Score ``test_seasons`` and return (games frame, {arm: (n,10) cells}, {arm: (n,36) cells}, marginal pmf arrays for ``oa_evaluate``, fits).

    ``extra_lams`` (optional): {name: DataFrame(game_id, lam_home, lam_away)} adds arms ``<name>_SIM1`` (nhl-sim-1.1) and ``<name>_SIM2`` (nhl-sim-2.0) on those
    expected goals, so a retuned rating can be put through both simulators. Every simulator draw uses ``game_seed(game_id)`` as everywhere else.
    ``collect(sims) -> dict`` (optional) adds per-game columns computed from the simulator results of every arm (e.g. team totals); default: nothing.
    """
    import time
    from pathlib import Path

    from nhl_edge.log import get_logger, kv
    from nhl_edge.research import walk_forward_v2 as W2
    from nhl_edge.research.walk_forward import evaluation_games, game_seed
    from nhl_edge.sim.engine import SimConfig, TeamParams, simulate_game
    from nhl_edge.sim.engine_v2 import simulate_game_v2

    log = get_logger(__name__)
    W2.FIRST_SHOTS_SEASON, W2.TRAIN_WINDOW = first_shots_season, train_window
    t0 = time.time()
    ctx, nhl_games, shots = W2.load_ctx(Path(history), min_season, None if extra_shots_dir is None else Path(extra_shots_dir))
    games, skipped = evaluation_games(nhl_games, test_seasons)
    from nhl_edge.model_research.wf_data import pmfs
    from nhl_edge.research.oa_walk_forward import _row_from_sim

    names = list(ARMS) + [f"{n}_{s}" for n in (extra_lams or {}) for s in ("SIM1", "SIM2")]
    cells_m = {a: [] for a in names}
    cells_t = {a: [] for a in names}
    tot_pmf = {a: [] for a in names}
    mar_pmf = {a: [] for a in names}
    rows, fits = [], {}
    lc: dict = {}
    lst: dict = {}
    for S in [int(s) for s in test_seasons]:
        fit = W2.select_params(ctx, shots, nhl_games, S, lc, lst)
        prm = fit["prm"]
        fits[str(S)] = {"env_dispersion": fit["env"], "p_ot_goal": prm.p_ot_goal, "hazard_train_seasons": W2.hazard_seasons(S)}
        log.info(kv(event="joint_fit", season=S, env=fit["env"], train=W2.hazard_seasons(S)))
        gs = games[games["season"] == S]
        if max_games:
            gs = gs.iloc[: int(max_games)]
        cfg = SimConfig(n_sims=int(n_sims))
        for i, r in enumerate(gs.itertuples(index=False)):
            f = W2.game_features(ctx, r, None, lc, lst)
            seed = game_seed(f["game_id"])
            H = TeamParams(0, f["home"], f["lam_v1_home"])
            A = TeamParams(0, f["away"], f["lam_v1_away"])
            sims = {"V1": simulate_game(H, A, seed, cfg), "SIM2": simulate_game_v2(H, A, seed, n_sims, prm),
                    "SIM2_ST": simulate_game_v2(TeamParams(0, f["home"], f["lam_st_home"]), TeamParams(0, f["away"], f["lam_st_away"]), seed, n_sims, prm)}
            for n, df in (extra_lams or {}).items():
                lam = df.loc[int(f["game_id"])]
                eh, ea = TeamParams(0, f["home"], float(lam["lam_home"])), TeamParams(0, f["away"], float(lam["lam_away"]))
                sims[f"{n}_SIM1"] = simulate_game(eh, ea, seed, cfg)
                sims[f"{n}_SIM2"] = simulate_game_v2(eh, ea, seed, n_sims, prm)
            rec = {"game_id": int(r.game_id), "season": S, "game_date": str(r.game_date)}
            for a in names:
                pm, pt = cells_from_result(sims[a])
                cells_m[a].append(pm)
                cells_t[a].append(pt)
                pp = pmfs(sims[a])
                tot_pmf[a].append(pp["total"])
                mar_pmf[a].append(pp["margin"])
                rec.update(_row_from_sim(pp, float(sims[a].home_final.mean()), float(sims[a].away_final.mean()), f"{a}_"))
            if collect is not None:
                rec.update(collect(sims))
            km, kt = observed_cells(r.home_score, r.away_score, r.last_period_type)
            rec.update({"k_margin": km, "k_total": kt, "home_score": int(r.home_score), "away_score": int(r.away_score), "last_period_type": str(r.last_period_type)})
            rows.append(rec)
            if (i + 1) % 250 == 0:
                log.info(kv(event="joint_progress", season=S, done=i + 1, total=len(gs), elapsed_s=round(time.time() - t0, 1)))
    import pandas as pd

    df = pd.DataFrame(rows)
    df["y_home_win"] = (df["home_score"] > df["away_score"]).astype(int)
    df["y_overtime"] = (df["last_period_type"] != "REG").astype(int)
    df["y_total"] = df["home_score"] + df["away_score"]
    pm = {"arms": np.array(names), "total": np.stack([np.asarray(tot_pmf[a]) for a in names], axis=1), "margin": np.stack([np.asarray(mar_pmf[a]) for a in names], axis=1)}
    return df, {a: np.asarray(v) for a, v in cells_m.items()}, {a: np.asarray(v) for a, v in cells_t.items()}, pm, {"fits": fits, "skipped": skipped, "elapsed_s": round(time.time() - t0, 1)}


def evaluate_joint(df, cm: dict[str, np.ndarray], ct: dict[str, np.ndarray], incumbent: str = "V1", n_boot: int = 4000) -> dict:
    """Levels, paired deltas vs ``incumbent`` (game and slate-clustered bootstraps), reliability and OT-conditionals; pooled and per season."""
    from nhl_edge.model_research.scoring import paired_delta
    from nhl_edge.research.oa_evaluate import _cluster_boot

    k_m, k_t = df["k_margin"].to_numpy(int), df["k_total"].to_numpy(int)
    season = df["season"].to_numpy()
    clusters = df["game_date"].astype(str).to_numpy()
    arms = list(cm)
    loss = {a: {"brier_joint_margin": brier_cat(cm[a], k_m), "logscore_joint_margin": logscore_cat(cm[a], k_m),
                "brier_joint_total": brier_cat(ct[a], k_t), "logscore_joint_total": logscore_cat(ct[a], k_t)} for a in arms}

    def block(mask):
        out = {"n": int(mask.sum()), "levels": {a: {m: float(v[mask].mean()) for m, v in loss[a].items()} for a in arms}, "paired": []}
        for a in arms:
            if a == incumbent:
                continue
            for m in loss[a]:
                d = paired_delta(loss[a][m][mask], loss[incumbent][m][mask], n_boot=n_boot)
                lo_c, hi_c = _cluster_boot(loss[a][m][mask] - loss[incumbent][m][mask], clusters[mask], n_boot=min(n_boot, 2000))
                out["paired"].append({"challenger": a, "incumbent": incumbent, "metric": m, "delta": d["delta"], "lo95": d["lo95"], "hi95": d["hi95"], "lo95_slate": lo_c, "hi95_slate": hi_c})
        return out

    res = {"arms": arms, "pooled": block(np.ones(len(df), bool)), "by_season": {str(s): block(season == s) for s in sorted(set(int(x) for x in season))}}
    res["reliability_margin"] = {a: cell_reliability(cm[a], k_m, MARGIN_CELLS) for a in arms}
    res["reliability_total"] = {a: cell_reliability(ct[a], k_t, total_cell_names()) for a in arms}
    res["ot_conditionals"] = {a: overtime_conditionals(cm[a], k_m) for a in arms}
    return res


JOINT_NON_INFERIORITY = {"brier_joint_margin": 0.0020, "brier_joint_total": 0.0020}      # added gate: CI upper bound of (challenger - incumbent) must not exceed this
SECONDARY = ("brier_win", "rps_total", "rps_margin", "brier_over_5.5", "brier_over_6.5")


def scorecard_run(df, pm: dict[str, np.ndarray], cm: dict[str, np.ndarray], ct: dict[str, np.ndarray], *, unexposed: tuple[int, ...], exposed: tuple[int, ...],
                  challengers: tuple[str, ...] = ("SIM2", "SIM2_ST"), incumbent: str = "V1", inference_seconds: float | None = None, reproducible: bool | None = None,
                  n_boot: int = 4000) -> dict:
    """Promotion scorecards (``promotion.score_challenger``) for the overtime target and the margin target, plus the joint non-inferiority gate, with the V1 simulator
    as the incumbent. ``unexposed`` seasons are the ones the V2 simulator was never scored on before this study; ``exposed`` the ones it was."""
    from nhl_edge.evaluation.metrics import ece
    from nhl_edge.research.oa_evaluate import compare, per_game_losses
    from nhl_edge.research.promotion import score_challenger

    arms = [str(a) for a in pm["arms"]]
    losses = per_game_losses(df, pm, arms)
    season = df["season"].to_numpy()
    clusters = df["game_date"].astype(str).to_numpy()
    k_m, k_t = df["k_margin"].to_numpy(int), df["k_total"].to_numpy(int)
    for a in arms:
        losses[a]["brier_joint_margin"] = brier_cat(cm[a], k_m)
        losses[a]["brier_joint_total"] = brier_cat(ct[a], k_t)
    un = np.isin(season, unexposed)
    metrics = ("brier_ot", *SECONDARY, "rps_margin", *JOINT_NON_INFERIORITY)

    def sub(mask):
        return {a: {k: v[mask] for k, v in losses[a].items()} for a in arms}

    out: dict = {"incumbent": incumbent, "unexposed_seasons": list(unexposed), "exposed_seasons": list(exposed), "n_unexposed_games": int(un.sum()), "scorecards": {}}
    pooled = compare(sub(un), incumbent, list(challengers), clusters[un], metrics, n_boot=n_boot)
    by_un = {str(s): compare(sub(season == s), incumbent, list(challengers), clusters[season == s], ("brier_ot", "brier_win", "rps_total"), n_boot=1500) for s in unexposed if (season == s).any()}
    by_ex = {str(s): compare(sub(season == s), incumbent, list(challengers), clusters[season == s], ("brier_ot", "brier_win", "rps_total"), n_boot=1500) for s in exposed if (season == s).any()}
    out["pooled_unexposed"], out["by_season_unexposed"], out["by_season_exposed"] = pooled, by_un, by_ex
    y_ot = df["y_overtime"].to_numpy(float)
    for ch in challengers:
        for target, primary in (("overtime / regulation tie", "brier_ot"), ("goal-margin distribution", "rps_margin")):
            sc = score_challenger(target=target, challenger=ch, incumbent=incumbent, primary_metric=primary, pooled_unexposed=pooled, by_season_unexposed=by_un, exposed=by_ex,
                                  n_unexposed_games=int(un.sum()), secondary_metrics=tuple(m for m in (*SECONDARY, "brier_ot") if m != primary),
                                  ece=(float(ece(df.loc[un, f"{ch}_p_overtime"].to_numpy(float), y_ot[un], 10)), float(ece(df.loc[un, f"{incumbent}_p_overtime"].to_numpy(float), y_ot[un], 10))),
                                  inference_seconds=inference_seconds, reproducible=reproducible)
            d = sc.to_dict()
            joint_bad = [f"{m} upper {r['hi95']:+.4f} > {JOINT_NON_INFERIORITY[m]:.4f}" for m in JOINT_NON_INFERIORITY
                         if (r := next((x for x in pooled if x["challenger"] == ch and x["metric"] == m), None)) is not None and r["hi95"] > JOINT_NON_INFERIORITY[m]]
            d["gates"].append({"gate": "J1_joint_non_inferiority", "passed": not joint_bad, "detail": "; ".join(joint_bad) or "joint margin and joint total Brier within 0.0020"})
            hard = [g for g in d["gates"] if g["passed"] is False]
            pending = [g for g in d["gates"] if g["passed"] is None]
            d["verdict"] = "RETAIN_INCUMBENT" if hard else ("SHADOW_MORE" if pending else "PROMOTE_CANDIDATE")
            out["scorecards"][f"{ch}|{target}"] = d
    return out


# ---------------------------------------------------------------------------------------------------------------------------------
# command line: `run` (one shard of seasons) and `evaluate` (merge shards, scorecards, joint tables)
# ---------------------------------------------------------------------------------------------------------------------------------
def _save_shard(out, df, cm, ct, pm, meta) -> None:
    import json
    from pathlib import Path

    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    df.to_csv(out / "games.csv", index=False)
    np.savez_compressed(out / "cells.npz", **{f"m|{a}": v for a, v in cm.items()}, **{f"t|{a}": v for a, v in ct.items()})
    np.savez_compressed(out / "pmfs.npz", **pm)
    (out / "meta.json").write_text(json.dumps(meta, indent=1, default=str))


def _load_shards(dirs):
    import json
    from pathlib import Path

    import pandas as pd

    dfs, cms, cts, pms, metas = [], [], [], [], []
    for d in sorted(Path(x) for x in dirs):
        dfs.append(pd.read_csv(d / "games.csv"))
        z = np.load(d / "cells.npz")
        cms.append({k[2:]: z[k] for k in z.files if k.startswith("m|")})
        cts.append({k[2:]: z[k] for k in z.files if k.startswith("t|")})
        p = dict(np.load(d / "pmfs.npz", allow_pickle=False))
        pms.append(p)
        metas.append(json.loads((d / "meta.json").read_text()))
    df = pd.concat(dfs, ignore_index=True)
    arms = list(cms[0])
    cm = {a: np.concatenate([c[a] for c in cms]) for a in arms}
    ct = {a: np.concatenate([c[a] for c in cts]) for a in arms}
    pm = {"arms": pms[0]["arms"], "total": np.concatenate([p["total"] for p in pms]), "margin": np.concatenate([p["margin"] for p in pms])}
    order = df.sort_values(["game_date", "game_id"], kind="stable").index.to_numpy()
    df = df.loc[order].reset_index(drop=True)
    return df, {a: v[order] for a, v in cm.items()}, {a: v[order] for a, v in ct.items()}, {"arms": pm["arms"], "total": pm["total"][order], "margin": pm["margin"][order]}, metas


def main(argv=None) -> int:
    import argparse
    import json
    from pathlib import Path

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.joint_eval")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--history", default="data/history")
    r.add_argument("--seasons", required=True)
    r.add_argument("--out", required=True)
    r.add_argument("--n-sims", type=int, default=4000)
    r.add_argument("--first-shots-season", type=int, default=2008)
    r.add_argument("--train-window", type=int, default=4)
    r.add_argument("--min-season", type=int, default=2008)
    r.add_argument("--max-games", type=int)
    r.add_argument("--extra-shots-dir", default="data/history/shots_extension")
    e = sub.add_parser("evaluate")
    e.add_argument("--dirs", nargs="+", required=True)
    e.add_argument("--unexposed", required=True)
    e.add_argument("--exposed", required=True)
    e.add_argument("--out", required=True)
    e.add_argument("--runtime-seconds", type=float)
    e.add_argument("--reproducible", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "run":
        seasons = [int(s) for s in a.seasons.split(",")]
        df, cm, ct, pm, meta = run_joint(a.history, seasons, n_sims=a.n_sims, first_shots_season=a.first_shots_season, train_window=a.train_window, min_season=a.min_season, extra_shots_dir=a.extra_shots_dir, max_games=a.max_games)
        _save_shard(a.out, df, cm, ct, pm, {**meta, "seasons": seasons, "n_sims": a.n_sims, "first_shots_season": a.first_shots_season, "train_window": a.train_window})
        print(json.dumps({"n_games": len(df), **meta["fits"]}, default=str)[:400])
        return 0
    df, cm, ct, pm, metas = _load_shards(a.dirs)
    un = tuple(int(s) for s in a.unexposed.split(","))
    ex = tuple(int(s) for s in a.exposed.split(","))
    res = scorecard_run(df, pm, cm, ct, unexposed=un, exposed=ex, inference_seconds=a.runtime_seconds, reproducible=True if a.reproducible else None)
    res["joint"] = evaluate_joint(df, cm, ct)
    res["fits"] = {k: v for m in metas for k, v in m["fits"].items()}
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "joint_results.json").write_text(json.dumps(res, indent=1, default=float))
    (out / "joint_results.md").write_text(render(res))
    print((out / "joint_results.md").read_text())
    return 0


def render(res: dict) -> str:
    L = ["# V2 simulator: joint game-distribution validation", "", f"incumbent `{res['incumbent']}` (nhl-sim-1.1 on V1 rates) · unexposed seasons {res['unexposed_seasons'][0]}–{res['unexposed_seasons'][-1]} "
         f"({res['n_unexposed_games']} games) · exposed {res['exposed_seasons']} · negative Δ = challenger better", ""]
    L += ["## Scorecards (promotion gates G1–G10 + added J1; the scorecard recommends, a human decides)", ""]
    for k, sc in res["scorecards"].items():
        L += [f"### {k}: **{sc['verdict']}**", "", "| gate | result | detail |", "|---|---|---|"]
        for g in sc["gates"]:
            L.append(f"| {g['gate']} | {'PASS' if g['passed'] else 'FAIL' if g['passed'] is False else 'pending'} | {g['detail']} |")
        L.append("")
    L += ["## Pooled paired differences on the unexposed seasons", "", "| challenger | metric | Δ | 95% games | 95% slates |", "|---|---|---:|---|---|"]
    for r in res["pooled_unexposed"]:
        L.append(f"| {r['challenger']} | {r['metric']} | {r['delta']:+.4f} | [{r['lo95']:+.4f}, {r['hi95']:+.4f}] | [{r['lo95_slate']:+.4f}, {r['hi95_slate']:+.4f}] |")
    j = res["joint"]
    L += ["", "## Joint-distribution levels (pooled, all seasons)", "", "| arm | " + " | ".join(next(iter(j["pooled"]["levels"].values()))) + " |", "|---|" + "---:|" * len(next(iter(j["pooled"]["levels"].values())))]
    for a, v in j["pooled"]["levels"].items():
        L.append(f"| {a} | " + " | ".join(f"{x:.4f}" for x in v.values()) + " |")
    L += ["", "## Overtime conditionals (predicted vs observed, pooled)", "", "| arm | P(OT or SO) pred / obs | P(SO given tie) pred / obs |", "|---|---|---|"]
    for a, c in j["ot_conditionals"].items():
        L.append(f"| {a} | {c['pred_p_ot_or_so']:.4f} / {c['obs_p_ot_or_so']:.4f} | {c['pred_p_so_given_tie']:.4f} / {c['obs_p_so_given_tie']:.4f} |")
    L += ["", "## Per-cell reliability, joint margin partition (z of observed vs expected, pooled)", "", "| cell | " + " | ".join(j["arms"]) + " |", "|---|" + "---:|" * len(j["arms"])]
    for i, cell in enumerate(MARGIN_CELLS):
        L.append(f"| {cell} | " + " | ".join(f"{j['reliability_margin'][a][i]['expected']:.0f} vs {j['reliability_margin'][a][i]['observed']:.0f} (z {j['reliability_margin'][a][i]['z']:+.1f})" for a in j["arms"]) + " |")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    import sys

    sys.exit(main())
