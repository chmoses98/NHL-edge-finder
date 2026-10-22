"""Scoring and paired uncertainty for the opponent-adjusted walk-forward (``oa_walk_forward``).

Primary metrics (proper scoring rules, lower is better): Brier and log loss of P(home win), Brier of P(overtime), ranked
probability score of the total-goal and goal-margin distributions (RPS == discrete CRPS, in goals). Supporting: Brier of
the 5.5 / 6.5 totals and MAE of the expected total. Every comparison is PAIRED against the incumbent on the same games,
with two bootstraps: resampling games, and resampling whole game dates (slates), which is the more conservative because
games on one night share a market state and an environment.

A difference is called PRACTICALLY MEANINGFUL only when its 95% interval excludes zero AND the point estimate is at least
``MIN_MEANINGFUL`` of the metric's own scale (see below); statistical significance on thousands of games can be real and
still be economically irrelevant.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.model_research.scoring import brier, logloss, paired_delta, rps_from_pmf

MARGIN_LO = -10
# smallest paired improvement treated as practically meaningful, by metric (Brier/log loss units; RPS in goals)
MIN_MEANINGFUL = {"brier_win": 0.0010, "logloss_win": 0.0020, "brier_ot": 0.0010, "rps_total": 0.0050, "rps_margin": 0.0050,
                  "brier_over_5.5": 0.0010, "brier_over_6.5": 0.0010}
PRIMARY = ("brier_win", "rps_total", "brier_ot")


def per_game_losses(df: pd.DataFrame, pm: dict[str, np.ndarray], arms: list[str]) -> dict[str, dict[str, np.ndarray]]:
    y_home = df["y_home_win"].to_numpy(float)
    y_ot = df["y_overtime"].to_numpy(float)
    y_tot = df["y_total"].to_numpy(int)
    margin = (df["home_score"] - df["away_score"]).to_numpy(int)
    # official finals already credit an OT/SO winner with the extra goal, the same convention the simulator uses
    arms_all = [str(a) for a in pm["arms"]]
    out: dict[str, dict[str, np.ndarray]] = {}
    for arm in arms:
        k = arms_all.index(arm)
        p = df[f"{arm}_p_home_win"].to_numpy(float)
        tot_pmf = pm["total"][:, k, :]
        mar_pmf = pm["margin"][:, k, :]
        mi = np.clip(margin, MARGIN_LO, MARGIN_LO + mar_pmf.shape[1] - 1) - MARGIN_LO
        cdf = np.cumsum(mar_pmf, axis=1)
        kk = np.arange(mar_pmf.shape[1])[None, :]
        rps_m = ((cdf - (mi[:, None] <= kk)) ** 2).sum(axis=1)
        out[arm] = {
            "brier_win": brier(p, y_home), "logloss_win": logloss(p, y_home), "brier_ot": brier(df[f"{arm}_p_overtime"].to_numpy(float), y_ot),
            "rps_total": rps_from_pmf(tot_pmf, y_tot), "rps_margin": rps_m,
            "brier_over_5.5": brier(df[f"{arm}_p_over_5.5"].to_numpy(float), (y_tot > 5.5).astype(float)),
            "brier_over_6.5": brier(df[f"{arm}_p_over_6.5"].to_numpy(float), (y_tot > 6.5).astype(float)),
            "abs_err_total": np.abs(df[f"{arm}_expected_total"].to_numpy(float) - y_tot),
        }
    return out


def _cluster_boot(d: np.ndarray, clusters: np.ndarray, n_boot: int = 2000, seed: int = 0, level: float = 0.95) -> tuple[float, float]:
    """CI of mean(d) resampling whole clusters (game dates)."""
    ids, inv = np.unique(clusters, return_inverse=True)
    s = np.bincount(inv, weights=d)
    n = np.bincount(inv).astype(float)
    rng = np.random.default_rng(seed)
    pick = rng.integers(0, len(ids), size=(n_boot, len(ids)))
    m = s[pick].sum(axis=1) / n[pick].sum(axis=1)
    a = (1 - level) / 2
    return float(np.quantile(m, a)), float(np.quantile(m, 1 - a))


def compare(losses: dict[str, dict[str, np.ndarray]], incumbent: str, challengers: list[str], clusters: np.ndarray, metrics: tuple[str, ...] | None = None,
            n_boot: int = 4000) -> list[dict[str, Any]]:
    rows = []
    for arm in challengers:
        for m in metrics or tuple(losses[arm]):
            a, b = losses[arm][m], losses[incumbent][m]
            d = paired_delta(a, b, n_boot=n_boot)
            d975 = paired_delta(a, b, n_boot=n_boot, level=0.975)       # two primary challengers: Bonferroni level for the primary gate
            lo_c, hi_c = _cluster_boot(a - b, clusters)
            lo_c975, hi_c975 = _cluster_boot(a - b, clusters, level=0.975)
            thr = MIN_MEANINGFUL.get(m)
            sig = d["hi95"] < 0 or d["lo95"] > 0
            sig_c = hi_c < 0 or lo_c > 0
            rows.append({"challenger": arm, "incumbent": incumbent, "metric": m, "n": d["n"], "mean_incumbent": float(np.mean(b)), "mean_challenger": float(np.mean(a)),
                         "delta": d["delta"], "lo95": d["lo95"], "hi95": d["hi95"], "lo95_slate": lo_c, "hi95_slate": hi_c, "lo975": d975["lo95"], "hi975": d975["hi95"], "lo975_slate": lo_c975, "hi975_slate": hi_c975,
                         "better_game_ci": bool(d["hi95"] < 0), "worse_game_ci": bool(d["lo95"] > 0), "better_slate_ci": bool(hi_c < 0), "worse_slate_ci": bool(lo_c > 0),
                         "practically_meaningful": bool(thr is not None and sig and sig_c and abs(d["delta"]) >= thr)})
    return rows


def reliability(p: np.ndarray, y: np.ndarray, bins: int = 10) -> list[dict[str, float]]:
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(p, edges) - 1, 0, bins - 1)
    out = []
    for b in range(bins):
        m = idx == b
        if m.sum():
            out.append({"bin": f"{edges[b]:.1f}-{edges[b + 1]:.1f}", "n": int(m.sum()), "mean_p": float(p[m].mean()), "hit_rate": float(y[m].mean())})
    return out


def evaluate_run(games_csv: Path, pmf_npz: Path, incumbent: str = "V1") -> dict[str, Any]:
    df = pd.read_csv(games_csv)
    pm = dict(np.load(pmf_npz, allow_pickle=False))
    arms = [a for a in (str(x) for x in pm["arms"])]
    losses = per_game_losses(df, pm, arms)
    challengers = [a for a in arms if a != incumbent]
    res: dict[str, Any] = {"arms": arms, "incumbent": incumbent, "n_games": int(len(df)), "seasons": sorted(int(s) for s in df["season"].unique()), "pooled": {}, "by_season": {}}
    clusters = df["game_date"].astype(str).to_numpy()
    res["pooled"]["levels"] = {a: {m: float(np.mean(v)) for m, v in losses[a].items()} for a in arms}
    res["pooled"]["paired_vs_incumbent"] = compare(losses, incumbent, challengers, clusters)
    for s in res["seasons"]:
        m = (df["season"] == s).to_numpy()
        sub = {a: {k: v[m] for k, v in losses[a].items()} for a in arms}
        res["by_season"][str(s)] = {"n": int(m.sum()), "levels": {a: {k: float(np.mean(v)) for k, v in sub[a].items()} for a in arms},
                                    "paired_vs_incumbent": compare(sub, incumbent, challengers, clusters[m], PRIMARY, n_boot=2000)}
    res["calibration_win"] = {a: reliability(df[f"{a}_p_home_win"].to_numpy(float), df["y_home_win"].to_numpy(float)) for a in arms}
    res["outcome_rates"] = {"home_win": float(df["y_home_win"].mean()), "overtime": float(df["y_overtime"].mean()), "mean_total": float(df["y_total"].mean())}
    return res


def render_markdown(res: dict[str, Any], title: str = "Opponent-adjusted walk-forward") -> str:
    lines = [f"# {title}", "", f"{res['n_games']} games · seasons {res['seasons']} · incumbent `{res['incumbent']}` · negative delta = challenger better. "
             "Intervals are 95%: game-level bootstrap [lo, hi] and date-level (slate-clustered) bootstrap in brackets after the `|`.", ""]
    lines += ["## Levels (pooled)", "", "| arm | " + " | ".join(next(iter(res["pooled"]["levels"].values()))) + " |", "|---|" + "---:|" * len(next(iter(res["pooled"]["levels"].values())))]
    for a, v in res["pooled"]["levels"].items():
        lines.append(f"| {a} | " + " | ".join(f"{x:.4f}" for x in v.values()) + " |")

    def table(rows: list[dict[str, Any]]) -> list[str]:
        out = ["| challenger | metric | n | Δ vs incumbent | 95% CI (games) | 95% CI (slates) | verdict |", "|---|---|---:|---:|---|---|---|"]
        for r in rows:
            v = ("BETTER (meaningful)" if r["practically_meaningful"] and r["delta"] < 0 else "WORSE (meaningful)" if r["practically_meaningful"] and r["delta"] > 0
                 else "better, CI excludes 0" if r["better_game_ci"] and r["better_slate_ci"] else "worse, CI excludes 0" if r["worse_game_ci"] and r["worse_slate_ci"] else "indistinguishable")
            out.append(f"| {r['challenger']} | {r['metric']} | {r['n']} | {r['delta']:+.4f} | [{r['lo95']:+.4f}, {r['hi95']:+.4f}] | [{r['lo95_slate']:+.4f}, {r['hi95_slate']:+.4f}] | {v} |")
        return out

    lines += ["", "## Paired vs incumbent (pooled)", ""] + table(res["pooled"]["paired_vs_incumbent"])
    for s, d in res["by_season"].items():
        lines += ["", f"## Season {s} (n={d['n']})", ""] + table(d["paired_vs_incumbent"])
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.oa_evaluate")
    ap.add_argument("--dir", required=True, help="directory with oa_games.csv and oa_pmfs.npz")
    ap.add_argument("--incumbent", default="V1")
    a = ap.parse_args(argv)
    d = Path(a.dir)
    res = evaluate_run(d / "oa_games.csv", d / "oa_pmfs.npz", a.incumbent)
    (d / "oa_eval.json").write_text(json.dumps(res, indent=1))
    md = render_markdown(res)
    (d / "oa_eval.md").write_text(md)
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
