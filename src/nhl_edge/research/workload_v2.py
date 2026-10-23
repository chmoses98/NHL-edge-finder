"""WORKLOAD_V2: WORKLOAD_V1 with a role-conditional shrinkage centre for skater shot rates (RESEARCH_ONLY).

Preregistration: ``docs/research/workload_v2/PREREGISTRATION.md`` (+ ``preregistration.json``), committed before any WORKLOAD_V2 number exists.

Diagnosis that motivates it (``docs/research/workload_v2/DIAGNOSIS.md``): WORKLOAD_V1 over-predicts skater shots by +0.03 to +0.05 per skater-game in every
held-out season, and the error is not uniform. By predicted time on ice the bias is +0.13 (2023-24) / +0.09 (2024-25) shots for the lowest quintile and about
0 for the highest; players with fewer than 6 prior games are +0.31. The cause is the shrinkage of each player's shot-rate index toward 1.0, the league's
position-wide rate: depth players (lowest predicted TOI) shoot below the position average, stars above it, so shrinking toward the position average
inflates the depth players (more numerous in a lineup) and deflates stars. Minutes carry little of it (0.007 of 0.052 in 2023-24).

The single change: the pseudo-observations that anchor every index (``k_rate`` minutes at the league rate) are anchored at the shooting level of the player's
ROLE instead, mu[position, TOI quintile] = (actual shots) / (shots the league rate would give for the minutes actually played), estimated on the training
seasons only, with the role read from the point-in-time predicted TOI. Ten fitted numbers plus eight quintile edges; no tuned hyper-parameter.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.research import workload_eval as E
from nhl_edge.research import workload_experiment as X
from nhl_edge.research import workload_v1 as W

N_BUCKETS = 5
MU_CLIP = (0.5, 1.5)
POSITIONS = ("F", "D")


def league_expected_shots(d: pd.DataFrame) -> np.ndarray:
    """Shots the point-in-time league rate would give for the minutes actually played (all states incl. overtime), times the venue/opponent adjustment."""
    e = np.zeros(len(d))
    for s in W.STATES_W:
        e += d[f"t_{s}"].fillna(0).to_numpy(float) / 3600.0 * d[f"lgr_{s}"].to_numpy(float)
    return d["wl_adj"].to_numpy(float) * e


def fit_role_prior(pred: pd.DataFrame, seasons: list[int], n_buckets: int = N_BUCKETS) -> dict[str, Any]:
    """Quintile edges of predicted TOI and the shooting multiplier of each (position, quintile), from the regular-season rows of ``seasons`` only.

    ``pred`` is the output of :func:`workload_v1.skater_predictions` (point in time, no role prior). Rows without shift-chart minutes are skipped.
    """
    d = pred[pred["season"].isin(seasons) & (pred["game_type"] == 2)]
    edges: dict[str, list[float]] = {}
    mu: dict[str, list[float]] = {}
    n: dict[str, list[int]] = {}
    for pos in POSITIONS:
        dd = d[d["pos"] == pos]
        if dd.empty:                                                           # no training rows for this position: a neutral prior
            edges[pos], mu[pos], n[pos] = [0.0] * (n_buckets - 1), [1.0] * n_buckets, [0] * n_buckets
            continue
        qs = np.quantile(dd["wl_toi"].to_numpy(float), np.linspace(0, 1, n_buckets + 1)[1:-1])
        b = np.searchsorted(qs, dd["wl_toi"].to_numpy(float), side="right")
        ok = dd["t_evreg"].notna().to_numpy()
        e = league_expected_shots(dd)
        y = dd["sog"].to_numpy(float)
        m_k, n_k = [], []
        for k in range(n_buckets):
            sel = (b == k) & ok
            m_k.append(float(np.clip(y[sel].sum() / max(e[sel].sum(), 1e-9), *MU_CLIP)) if sel.any() else 1.0)
            n_k.append(int(sel.sum()))
        edges[pos], mu[pos], n[pos] = [float(x) for x in qs], m_k, n_k
    return {"edges": edges, "mu": mu, "n_rows": n, "seasons": [int(s) for s in seasons], "n_buckets": n_buckets}


def skater_arms_v2(ctx: X.Ctx, season: int, prm: W.WorkloadParams) -> tuple[pd.DataFrame, dict[str, np.ndarray], dict[str, Any]]:
    """The V1 arms of ``workload_experiment.skater_arms`` plus ``WORKLOAD_V2`` (columns ``wl2_sog``, ``wl2_adj``; pmf with its own previous-season dispersion)."""
    m, pmfs, al = X.skater_arms(ctx, season, prm)
    train = [s for s in X.SEASONS if s < season]
    c = W.fit_constants(ctx.sk, ctx.tg, ctx.data.goalies, train)
    pred1 = W.skater_predictions(ctx.sk, ctx.tg, c, prm)                      # point-in-time V1 pass: used only to FIT the role prior on earlier seasons
    rp = fit_role_prior(pred1, train)
    rp_prev = fit_role_prior(pred1, [s for s in train if s < season - 1])     # dispersion season is scored with a prior fitted before it
    pred2 = W.skater_predictions(ctx.sk, ctx.tg, c, prm, role_prior=rp)
    pred2_prev = W.skater_predictions(ctx.sk, ctx.tg, c, prm, role_prior=rp_prev)
    key = ["game_id", "player_id"]
    m = m.merge(pred2[pred2["season"] == season][[*key, "wl_sog"]].rename(columns={"wl_sog": "wl2_sog"}), on=key, how="left")
    prev = ctx.champ_sk(season - 1)[[*key, "y_sog"]].merge(pred2_prev[pred2_prev["season"] == season - 1][[*key, "wl_sog"]], on=key, how="inner")
    alpha2 = E.fit_nb_alpha(prev["y_sog"].to_numpy(), prev["wl_sog"].to_numpy())
    pmfs = dict(pmfs)
    pmfs["WORKLOAD_V2"] = E.nb_pmf(m["wl2_sog"].to_numpy(), alpha2, W.SOG_K)
    return m, pmfs, {**al, "WORKLOAD_V2": alpha2, "_role_prior": rp, "_role_prior_prev": rp_prev}


def tier_bias(m: pd.DataFrame, col: str, n: int = N_BUCKETS) -> list[dict[str, float]]:
    """Mean (prediction - actual) shots by quintile of the WORKLOAD_V1 predicted TOI (the same cut for every arm), pooled over positions."""
    q = pd.qcut(m["wl_toi"], n, duplicates="drop", labels=False)
    out = []
    for k in sorted(q.dropna().unique()):
        s = m[q == k]
        out.append({"tier": int(k), "n": int(len(s)), "mean_pred": float(s[col].mean()), "mean_actual": float(s["y_sog"].mean()), "bias": float((s[col] - s["y_sog"]).mean())})
    return out


# ---------------------------------------------------------------------------------------------------------------------
# report and acceptance
# ---------------------------------------------------------------------------------------------------------------------
def report_v2(m: pd.DataFrame, pmfs: dict[str, np.ndarray], n_boot: int = 2000) -> dict[str, Any]:
    """Skater report for WORKLOAD_V2 scored exactly like WORKLOAD_V1 (same arms, metrics, bootstrap) plus V2-vs-V1 and bias by role."""
    m2 = m.copy()
    m2["wl_sog"] = m2["wl2_sog"]
    p2 = {a: v for a, v in pmfs.items() if a != "WORKLOAD_V2"}
    p2["WORKLOAD_V1"] = pmfs["WORKLOAD_V2"]          # the V2 mean/pmf takes the challenger slot, so X.skater_report / X.accept_skaters apply unchanged
    rep = X.skater_report(m2, p2, n_boot)
    y, gid = m["y_sog"].to_numpy(), m["game_id"].to_numpy()
    rows = {a: E.score_arm(p, y, X.SOG_LADDER) for a, p in {"V1": pmfs["WORKLOAD_V1"], "V2": pmfs["WORKLOAD_V2"]}.items()}
    rep["challenger_label"] = "WORKLOAD_V2 (reported in the WORKLOAD_V1 slot of the frozen report)"
    rep["v2_minus_v1"] = E.bootstrap_diff(gid, rows["V2"], rows["V1"], n_boot)
    rep["bias_by_tier"] = {"WORKLOAD_V1": tier_bias(m, "wl_sog"), "WORKLOAD_V2": tier_bias(m, "wl2_sog"), "CHAMPION": tier_bias(m, "ch_sog")}
    rep["bias_by_position"] = {p: {"WORKLOAD_V1": float((d["wl_sog"] - d["y_sog"]).mean()), "WORKLOAD_V2": float((d["wl2_sog"] - d["y_sog"]).mean())} for p, d in m.groupby("pos")}
    rep["bias_ci95"] = {"WORKLOAD_V1": E.bootstrap_mean_diff(gid, (m["wl_sog"] - m["y_sog"]).to_numpy(), n_boot),
                        "WORKLOAD_V2": E.bootstrap_mean_diff(gid, (m["wl2_sog"] - m["y_sog"]).to_numpy(), n_boot)}
    return rep


def accept_v2(rep: dict[str, Any], rule: dict[str, Any]) -> dict[str, Any]:
    """The seven frozen WORKLOAD_V1 checks, unchanged, plus one added check: no predicted-TOI quintile is biased by more than ``max_abs_tier_bias_sog``."""
    base = X.accept_skaters(rep, rule)
    checks = dict(base["checks"])
    checks["abs_tier_bias_le_max"] = all(abs(t["bias"]) <= rule["max_abs_tier_bias_sog"] for t in rep["bias_by_tier"]["WORKLOAD_V2"])
    return {"checks": checks, "verdict": "ACCEPTED" if all(checks.values()) else "REJECTED"}


def main(argv: list[str] | None = None) -> int:
    import argparse
    import json
    from pathlib import Path

    from nhl_edge.research import workload_replication as R

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.workload_v2")
    ap.add_argument("--seasons", default="2023,2024,2025")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--cache", default="out/workload_v2_cache")
    ap.add_argument("--out", default="docs/research/workload_v2")
    ap.add_argument("--prereg", default="docs/research/workload_v2/preregistration.json")
    ap.add_argument("--n-boot", type=int, default=2000)
    a = ap.parse_args(argv)
    pre = json.loads(Path(a.prereg).read_text())
    seasons = [int(s) for s in a.seasons.split(",")]
    history = Path(a.history)
    derived = R.derive_wf(history, [2022, 2023, 2024, 2025])
    ctx = R.ReplicationCtx(history, Path(a.cache), "derived", derived)
    prm = W.WorkloadParams.from_dict(pre["frozen_params"])
    res: dict[str, Any] = {"model_version": "WORKLOAD_V2", "preregistration": pre["id"], "acceptance_rule": pre["acceptance"], "seasons": {}}
    for s in seasons:
        m, pmfs, al = skater_arms_v2(ctx, s, prm)
        rep = report_v2(m, pmfs, a.n_boot)
        rep["acceptance"] = accept_v2(rep, pre["acceptance"])
        rep["role_prior"] = al["_role_prior"]
        rep["alpha"] = {k: v for k, v in al.items() if not k.startswith("_") and isinstance(v, float)}
        res["seasons"][str(s)] = rep
        print(s, rep["acceptance"]["verdict"], {k: bool(v) for k, v in rep["acceptance"]["checks"].items()}, flush=True)
    res["accepted_all_seasons"] = all(r["acceptance"]["verdict"] == "ACCEPTED" for r in res["seasons"].values())
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(json.dumps(X._round(res), indent=1))
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())


# ---------------------------------------------------------------------------------------------------------------------
# diagnosis of the WORKLOAD_V1 skater-shots bias (uses V1 predictions only)
# ---------------------------------------------------------------------------------------------------------------------
def diagnose(m: pd.DataFrame) -> dict[str, Any]:
    """Where the WORKLOAD_V1 shot bias sits: by position, predicted-TOI quintile, prior-games bucket, month, minutes-vs-rates split, and how much of the
    power-play minutes error is the game-level penalty count (unpredictable) versus allocation among teammates."""
    b = (m["wl_sog"] - m["y_sog"]).to_numpy(float)
    out: dict[str, Any] = {"n_skater_games": int(len(m)), "bias": float(b.mean()), "mean_actual": float(m["y_sog"].mean()), "champion_bias": float((m["ch_sog"] - m["y_sog"]).mean())}
    out["by_position"] = {p: {"bias": float((d["wl_sog"] - d["y_sog"]).mean()), "n": int(len(d))} for p, d in m.groupby("pos")}
    out["by_predicted_toi_quintile"] = tier_bias(m, "wl_sog")
    ng = pd.cut(m["n_games"], [-1, 5, 15, 30, 60, 10**6], labels=["0-5", "6-15", "16-30", "31-60", "61+"])
    out["by_prior_games"] = {str(k): {"bias": float((d["wl_sog"] - d["y_sog"]).mean()), "n": int(len(d))} for k, d in m.groupby(ng, observed=True)}
    mon = pd.to_datetime(m["date_int"].astype(str), format="%Y%m%d").dt.to_period("M").astype(str)
    out["by_month"] = {k: {"bias": float((d["wl_sog"] - d["y_sog"]).mean()), "n": int(len(d))} for k, d in m.groupby(mon)}
    out["by_ot_game"] = {str(k): float((d["wl_sog"] - d["y_sog"]).mean()) for k, d in m.groupby("game_ot")}
    w = m[m["shifts_ok"].fillna(False).astype(bool)]
    if len(w):
        pred_actual_minutes = w["wl_adj"] * sum(w[f"wl_rate_{s}"].fillna(0) * w[f"t_{s}"].fillna(0) / 3600.0 for s in W.STATES_W)
        rates_only = float((pred_actual_minutes - w["y_sog"]).mean())
        total = float((w["wl_sog"] - w["y_sog"]).mean())
        out["minutes_vs_rates"] = {"bias_with_actual_minutes": rates_only, "bias": total, "minutes_component": total - rates_only}
        t = w.groupby(["game_id", "team_id"]).agg(pred=("wl_toi_pp", "sum"), act=("y_toi_pp", "sum")).reset_index()
        t["pred"] /= 5.0
        t["act"] /= 5.0
        ww = w.merge(t.rename(columns={"pred": "tp", "act": "ta"}), on=["game_id", "team_id"])
        scaled = ww["wl_toi_pp"] * np.where(ww["tp"] > 0, ww["ta"] / ww["tp"], 1.0)
        mse = float(((ww["wl_toi_pp"] - ww["y_toi_pp"]) ** 2).mean())
        out["power_play_minutes"] = {"player_mse": mse, "player_mse_given_true_team_pp_minutes": float(((scaled - ww["y_toi_pp"]) ** 2).mean()),
                                     "team_pp_minutes_pred_actual_corr": float(np.corrcoef(t["pred"], t["act"])[0, 1]), "team_pp_minutes_rmse": float(np.sqrt(((t["pred"] - t["act"]) ** 2).mean())),
                                     "share_of_mse_from_game_level_pp_time": 1.0 - float(((scaled - ww["y_toi_pp"]) ** 2).mean()) / mse}
    return out
