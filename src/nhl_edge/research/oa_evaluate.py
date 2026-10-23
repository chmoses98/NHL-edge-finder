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




# ---------------------------------------------------------------------------------------------------------------------------
# preregistered tiers + promotion scorecard (docs/research/oa-walk-forward/PREREGISTRATION.md, amendment 1)
# ---------------------------------------------------------------------------------------------------------------------------
UNEXPOSED_SEASONS = (2018, 2019, 2020, 2021, 2022, 2023)
EXPOSED_SEASONS = (2024, 2025)
PRIMARY_CHALLENGERS = ("OA_SVA", "OA_SVA_C1")
SECONDARY = ("rps_total", "brier_ot", "rps_margin", "brier_over_5.5", "brier_over_6.5")


def _bonferroni(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Rows whose better/worse flags use the 97.5% intervals (two primary challengers)."""
    return [{**r, "better_game_ci": r["hi975"] < 0, "better_slate_ci": r["hi975_slate"] < 0, "worse_game_ci": r["lo975"] > 0, "worse_slate_ci": r["lo975_slate"] > 0} for r in rows]


def evaluate_tiers(games_csv: Path, pmf_npz: Path, incumbent: str = "V1", inference_seconds: float | None = None, reproducible: bool | None = None) -> dict[str, Any]:
    from nhl_edge.evaluation.metrics import ece
    from nhl_edge.research.promotion import score_challenger

    df = pd.read_csv(games_csv)
    pm = dict(np.load(pmf_npz, allow_pickle=False))
    arms = [str(a) for a in pm["arms"]]
    losses = per_game_losses(df, pm, arms)
    challengers = [a for a in arms if a != incumbent]
    clusters = df["game_date"].astype(str).to_numpy()
    season = df["season"].to_numpy()

    def sub(mask: np.ndarray) -> dict[str, dict[str, np.ndarray]]:
        return {a: {k: v[mask] for k, v in losses[a].items()} for a in arms}

    out: dict[str, Any] = {"incumbent": incumbent, "arms": arms, "tiers": {}, "by_season": {}, "scorecards": {}}
    tiers = {"UNEXPOSED_2018_2023": np.isin(season, UNEXPOSED_SEASONS), "EXPOSED_2024_2025": np.isin(season, EXPOSED_SEASONS)}
    for name, mask in tiers.items():
        out["tiers"][name] = {"n": int(mask.sum()), "levels": {a: {k: float(np.mean(v)) for k, v in sub(mask)[a].items()} for a in arms},
                              "paired": compare(sub(mask), incumbent, challengers, clusters[mask])}
    for s in sorted(set(int(x) for x in season)):
        m = season == s
        out["by_season"][str(s)] = {"n": int(m.sum()), "exposed": s in EXPOSED_SEASONS, "paired": compare(sub(m), incumbent, challengers, clusters[m], PRIMARY + ("rps_margin",), n_boot=1500)}
    pooled_un = _bonferroni(out["tiers"]["UNEXPOSED_2018_2023"]["paired"])
    by_un = {str(s): _bonferroni(out["by_season"][str(s)]["paired"]) for s in UNEXPOSED_SEASONS}
    by_ex = {str(s): out["by_season"][str(s)]["paired"] for s in EXPOSED_SEASONS}
    mun = np.isin(season, UNEXPOSED_SEASONS)
    y = df["y_home_win"].to_numpy(float)
    for ch in PRIMARY_CHALLENGERS:
        e_ch = ece(df.loc[mun, f"{ch}_p_home_win"].to_numpy(float), y[mun], 10)
        e_in = ece(df.loc[mun, f"{incumbent}_p_home_win"].to_numpy(float), y[mun], 10)
        sc = score_challenger(target="game win probability", challenger=ch, incumbent=incumbent, primary_metric="brier_win", pooled_unexposed=pooled_un, by_season_unexposed=by_un,
                              exposed=by_ex, n_unexposed_games=int(mun.sum()), secondary_metrics=SECONDARY, ece=(e_ch, e_in),
                              inference_seconds=inference_seconds, reproducible=reproducible)
        out["scorecards"][ch] = sc.to_dict()
    out["calibration_win_unexposed"] = {a: reliability(df.loc[mun, f"{a}_p_home_win"].to_numpy(float), y[mun]) for a in (incumbent, *PRIMARY_CHALLENGERS)}
    return out


def render_tiers(res: dict[str, Any]) -> str:
    lines = ["# OA_RIDGE walk-forward — preregistered tiers", "", "negative Δ = challenger better · intervals 95% (game bootstrap | date-cluster bootstrap) · the primary gate uses 97.5% (Bonferroni, two primary challengers)", ""]
    for name, t in res["tiers"].items():
        lines += [f"## {name} (n={t['n']})", "", "| arm | " + " | ".join(next(iter(t["levels"].values()))) + " |", "|---|" + "---:|" * len(next(iter(t["levels"].values())))]
        for a, v in t["levels"].items():
            lines.append(f"| {a} | " + " | ".join(f"{x:.4f}" for x in v.values()) + " |")
        lines += ["", "| challenger | metric | Δ | 95% games | 95% slates | verdict |", "|---|---|---:|---|---|---|"]
        for r in t["paired"]:
            if r["metric"] in ("abs_err_total", "logloss_win"):
                continue
            v = ("BETTER (meaningful)" if r["practically_meaningful"] and r["delta"] < 0 else "WORSE (meaningful)" if r["practically_meaningful"] and r["delta"] > 0
                 else "better, CI excludes 0" if r["better_game_ci"] and r["better_slate_ci"] else "worse, CI excludes 0" if r["worse_game_ci"] and r["worse_slate_ci"] else "indistinguishable")
            lines.append(f"| {r['challenger']} | {r['metric']} | {r['delta']:+.4f} | [{r['lo95']:+.4f}, {r['hi95']:+.4f}] | [{r['lo95_slate']:+.4f}, {r['hi95_slate']:+.4f}] | {v} |")
        lines.append("")
    lines += ["## Per season: Δ Brier(home win) vs incumbent", "", "| season | n | tier | " + " | ".join(f"{c}" for c in PRIMARY_CHALLENGERS) + " |", "|---|---:|---|" + "---|" * len(PRIMARY_CHALLENGERS)]
    for s, d in res["by_season"].items():
        cells = []
        for c in PRIMARY_CHALLENGERS:
            r = next(x for x in d["paired"] if x["challenger"] == c and x["metric"] == "brier_win")
            cells.append(f"{r['delta']:+.4f} [{r['lo95']:+.4f}, {r['hi95']:+.4f}]")
        lines.append(f"| {s} | {d['n']} | {'exposed' if d['exposed'] else 'unexposed'} | " + " | ".join(cells) + " |")
    lines += ["", "## Promotion scorecards (historical gates; G8–G10 need artifacts / live shadow)", ""]
    for ch, sc in res["scorecards"].items():
        lines += [f"### {ch} vs {sc['incumbent']} on {sc['target']}: **{sc['verdict']}**", "", "| gate | result | detail |", "|---|---|---|"]
        for g in sc["gates"]:
            lines.append(f"| {g['gate']} | {'PASS' if g['passed'] else 'FAIL' if g['passed'] is False else 'pending'} | {g['detail']} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def main_tiers(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.oa_evaluate tiers")
    ap.add_argument("--dir", required=True)
    ap.add_argument("--runtime-seconds", type=float, help="measured inference seconds per slate (G7)")
    ap.add_argument("--reproducible", action="store_true", help="two identical-seed runs produced byte-identical output (G8)")
    a = ap.parse_args(argv)
    d = Path(a.dir)
    res = evaluate_tiers(d / "oa_games.csv", d / "oa_pmfs.npz", inference_seconds=a.runtime_seconds, reproducible=True if a.reproducible else None)
    (d / "oa_tiers.json").write_text(json.dumps(res, indent=1, default=float))
    md = render_tiers(res)
    (d / "oa_tiers.md").write_text(md)
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main_tiers(sys.argv[2:]) if len(sys.argv) > 1 and sys.argv[1] == "tiers" else main())


def control_comparison(dir_: Path) -> dict[str, Any]:
    """Compare every arm with the tuned-incumbent control ``V1_T`` (see ``v1_tuned_control``) on the two tiers."""
    df = pd.read_csv(dir_ / "oa_games.csv")
    pm = dict(np.load(dir_ / "oa_pmfs.npz", allow_pickle=False))
    v1t = pd.read_csv(dir_ / "v1t_games.csv")
    ex = np.load(dir_ / "v1t_pmfs.npz")
    assert (v1t["game_id"].to_numpy() == df["game_id"].to_numpy()).all()
    df = pd.concat([df, v1t.drop(columns=["game_id"])], axis=1)
    pm = {"arms": np.array([*pm["arms"], "V1_T"]), "total": np.concatenate([pm["total"], ex["total"][:, None, :]], axis=1),
          "margin": np.concatenate([pm["margin"], ex["margin"][:, None, :]], axis=1)}
    arms = [str(a) for a in pm["arms"]]
    losses = per_game_losses(df, pm, arms)
    season = df["season"].to_numpy()
    clusters = df["game_date"].astype(str).to_numpy()
    out: dict[str, Any] = {"tiers": {}, "tuned_params": {str(s): [float(v1t.loc[df["season"] == s, c].iloc[0]) for c in ("V1_T_half_life", "V1_T_prior", "V1_T_home_adj")] for s in sorted(set(season))}}
    for name, seasons in (("UNEXPOSED_2018_2023", UNEXPOSED_SEASONS), ("EXPOSED_2024_2025", EXPOSED_SEASONS)):
        m = np.isin(season, seasons)
        sub = {a: {k: v[m] for k, v in losses[a].items()} for a in arms}
        out["tiers"][name] = {"n": int(m.sum()), "levels": {a: {k: float(np.mean(v)) for k, v in sub[a].items()} for a in arms},
                              "vs_V1_T": compare(sub, "V1_T", [a for a in arms if a != "V1_T"], clusters[m], PRIMARY + ("rps_margin",))}
    return out
