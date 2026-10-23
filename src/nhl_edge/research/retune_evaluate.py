"""Evaluation of the preregistered retuned-V1 study (docs/research/v1-retune/PREREGISTRATION.md; RESEARCH_ONLY).

Assembles every arm of the study from the per-game tables of ``oa_walk_forward`` (V1, V1_C1, OA_*, LEAGUE), ``v1_tuned_control`` (V1_T, V1_T_C1)
and ``v1_retune`` (V1_R, V1_R_C1, ablations), scores them with the shared proper scores and paired game / slate bootstraps, and applies the
decision rules R1-R5 exactly as written in the preregistration.

``python -m nhl_edge.research.retune_evaluate --dir OUT``
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.evaluation.metrics import ece
from nhl_edge.research.oa_evaluate import PRIMARY, compare, per_game_losses, reliability

FRESH = (2017,)
FRESH2 = tuple(range(2010, 2017))          # Amendment 2: second untouched tier, consistency requirement scaled to 5 of 7
FRESH2_3V3 = (2015, 2016)                  # descriptive subgroup: the first 3-on-3 overtime seasons
FRESH2_MIN_FAVOURABLE = 5
FAMILY_SEEN = (2018, 2019, 2020, 2021, 2022, 2023)
EXPOSED = (2024, 2025)
ALL_SEASONS = FRESH + FAMILY_SEEN + EXPOSED
PRACTICAL = {"brier_win": 0.0010, "rps_total": 0.0050, "brier_ot": 0.0010}
MIN_SEASONS_FAVOURABLE = 6
ABLATIONS = {"V1_R_noB2B": "back-to-back adjustment", "V1_R_noFIN": "finishing ratio"}
ARM_ORDER = ("V1", "V1_C1", "V1_T", "V1_T_C1", "V1_R", "V1_R_C1", "V1_R_noB2B", "V1_R_noFIN", "OA_XG", "OA_SVA", "OA_SVA_C1", "LEAGUE")


def assemble(dir_: Path) -> tuple[pd.DataFrame, dict[str, np.ndarray]]:
    """One frame and one pmf bundle (n x arms x bins) with every arm, rows aligned by game_id."""
    base = pd.read_csv(dir_ / "oa_games.csv")
    pm = dict(np.load(dir_ / "oa_pmfs.npz", allow_pickle=False))
    names = [str(a) for a in pm["arms"]]
    extra = [("v1t_games.csv", "v1t_pmfs.npz", ["V1_T"]), ("v1tc1_games.csv", "v1tc1_pmfs.npz", ["V1_T_C1"]), ("v1r_games.csv", "v1r_pmfs.npz", None)]
    tot, mar = [pm["total"]], [pm["margin"]]
    df = base
    for gcsv, npz, arms in extra:
        g = pd.read_csv(dir_ / gcsv)
        if "game_id" in g.columns:
            assert (g["game_id"].to_numpy() == base["game_id"].to_numpy()).all(), gcsv
            g = g.drop(columns=["game_id"])
        z = np.load(dir_ / npz, allow_pickle=False)
        if arms is None:
            arms = [str(a) for a in z["arms"]]
            t, m = z["total"], z["margin"]
        else:
            t, m = z["total"][:, None, :], z["margin"][:, None, :]
        df = pd.concat([df, g], axis=1)
        tot.append(t)
        mar.append(m)
        names += arms
    return df, {"arms": np.array(names), "total": np.concatenate(tot, axis=1), "margin": np.concatenate(mar, axis=1)}


def _sub(losses: dict[str, dict[str, np.ndarray]], mask: np.ndarray) -> dict[str, dict[str, np.ndarray]]:
    return {a: {k: v[mask] for k, v in d.items()} for a, d in losses.items()}


def _row(rows: list[dict[str, Any]], metric: str) -> dict[str, Any]:
    return next(r for r in rows if r["metric"] == metric)


def per_season_favourable(losses: dict[str, dict[str, np.ndarray]], season: np.ndarray, chall: str, inc: str, metric: str = "brier_win",
                          seasons: tuple[int, ...] = ALL_SEASONS) -> dict[str, float]:
    return {str(s): float(np.mean(losses[chall][metric][season == s] - losses[inc][metric][season == s])) for s in seasons if (season == s).any()}


def decide(losses: dict[str, dict[str, np.ndarray]], season: np.ndarray, clusters: np.ndarray, chall: str, inc: str, gate_metrics: tuple[str, ...], need_delta: float | None = None,
           seasons: tuple[int, ...] = ALL_SEASONS, min_fav: int = MIN_SEASONS_FAVOURABLE) -> dict[str, Any]:
    """Apply the preregistered better-than rule to ``chall`` vs ``inc`` pooled over every available season.

    BETTER when: every gate metric's 95% interval is below zero under BOTH bootstraps, the Brier(win) delta is at least ``need_delta`` in size (when given),
    at least MIN_SEASONS_FAVOURABLE seasons are favourable on Brier(win), and no primary metric is worse with an interval excluding zero.
    """
    mask = np.isin(season, seasons)
    rows = compare(_sub(losses, mask), inc, [chall], clusters[mask], PRIMARY)
    per = per_season_favourable(losses, season, chall, inc, seasons=seasons)
    n_fav = sum(1 for v in per.values() if v < 0)
    gate_ok = all(_row(rows, m)["better_game_ci"] and _row(rows, m)["better_slate_ci"] for m in gate_metrics)
    size_ok = True if need_delta is None else bool(_row(rows, "brier_win")["delta"] <= -need_delta)
    none_worse = not any(r["worse_game_ci"] and r["worse_slate_ci"] for r in rows)
    return {"challenger": chall, "incumbent": inc, "pooled": rows, "seasons_favourable": n_fav, "n_seasons": len(per), "per_season_brier_win": per,
            "gate_ok": gate_ok, "size_ok": size_ok, "season_consistent": n_fav >= min_fav, "no_primary_worse": none_worse,
            "BETTER": bool(gate_ok and size_ok and n_fav >= min_fav and none_worse)}


def evaluate(dir_: Path, history: Path | None = None, repo_root: Path | None = None, fresh2: bool = False, also: Path | None = None) -> dict[str, Any]:
    """``fresh2``: evaluate the Amendment-2 tier (seasons 2010-2016) with the same rules; the consistency requirement scales from 6/9 to 5/7. ``also`` is the
    main run's directory, used only to build the descriptive FRESH_ALL (2010-2017) tier."""
    df, pm = assemble(dir_)
    if fresh2 and also is not None:
        df2, pm2 = assemble(also)
        keep = (df2["season"] == FRESH[0]).to_numpy()
        df = pd.concat([df, df2[keep]], ignore_index=True)
        pm = {"arms": pm["arms"], "total": np.concatenate([pm["total"], pm2["total"][keep]]), "margin": np.concatenate([pm["margin"], pm2["margin"][keep]])}
    seasons_all = FRESH2 if fresh2 else ALL_SEASONS
    min_fav = FRESH2_MIN_FAVOURABLE if fresh2 else MIN_SEASONS_FAVOURABLE
    arms = [a for a in ARM_ORDER if a in [str(x) for x in pm["arms"]]]
    losses = per_game_losses(df, pm, [str(a) for a in pm["arms"]])
    season = df["season"].to_numpy()
    clusters = df["game_date"].astype(str).to_numpy()
    y = df["y_home_win"].to_numpy(float)
    out: dict[str, Any] = {"arms": arms, "n_games": int(len(df)), "seasons": sorted(int(s) for s in set(season)), "tiers": {}, "rules": {}, "ablations": {}, "by_season": {},
                           "mode": "FRESH2 (Amendment 2)" if fresh2 else "registered", "min_seasons_favourable": min_fav}
    tiers = ({"FRESH2_2010_2016": FRESH2, "FRESH2_3V3_2015_2016": FRESH2_3V3, "FRESH_ALL_2010_2017": FRESH2 + FRESH} if fresh2
             else {"FRESH_2017": FRESH, "FAMILY_SEEN_2018_2023": FAMILY_SEEN, "EXPOSED_2024_2025": EXPOSED, "POOLED_2017_2025": ALL_SEASONS})
    for name, ss in tiers.items():
        m = np.isin(season, ss)
        if not m.any():
            continue
        sub = _sub(losses, m)
        out["tiers"][name] = {"n": int(m.sum()), "levels": {a: {k: float(np.mean(v)) for k, v in sub[a].items()} for a in arms},
                              "ece_win": {a: float(ece(df.loc[m, f"{a}_p_home_win"].to_numpy(float), y[m], 10)) for a in arms},
                              "vs_V1": compare(sub, "V1", [a for a in arms if a != "V1"], clusters[m]),
                              "vs_V1_R_C1": compare(sub, "V1_R_C1", [a for a in arms if a not in ("V1_R_C1",)], clusters[m], PRIMARY + ("rps_margin",))}
    for s in out["seasons"]:
        m = season == s
        out["by_season"][str(s)] = {"n": int(m.sum()), "paired_win_vs_V1": {a: float(np.mean(losses[a]["brier_win"][m] - losses["V1"]["brier_win"][m])) for a in arms if a != "V1"}}
    kw = {"seasons": seasons_all, "min_fav": min_fav}
    out["rules"]["R1_retune_vs_V1"] = decide(losses, season, clusters, "V1_R", "V1", ("brier_win",), PRACTICAL["brier_win"], **kw)
    out["rules"]["R2_recalibration_on_retuned"] = decide(losses, season, clusters, "V1_R_C1", "V1_R", ("brier_win", "rps_total"), PRACTICAL["brier_win"], **kw)
    out["rules"]["R3_opponent_adjustment_incremental"] = decide(losses, season, clusters, "OA_SVA_C1", "V1_R_C1", ("brier_win",), PRACTICAL["brier_win"], **kw)
    for abl, label in ABLATIONS.items():            # informative when REMOVING the feature is worse (ablation minus V1_R > 0, CI excludes 0 under both bootstraps)
        m = np.isin(season, seasons_all)
        rows = compare(_sub(losses, m), "V1_R", [abl], clusters[m], ("brier_win", "rps_total", "brier_ot"))
        out["ablations"][abl] = {"feature": label, "pooled": rows,
                                 "informative": bool(any(r["worse_game_ci"] and r["worse_slate_ci"] for r in rows if r["metric"] in ("brier_win", "rps_total")))}
    # R4: leading candidate = lowest pooled Brier(win) among arms with no primary metric worse than V1 (CI excluding 0 under both bootstraps), ties inside the
    # practical threshold broken toward the simpler arm. Complexity order is declared here, before the results exist. Arms of EQUAL complexity inside the
    # threshold are reported as tied: the registration defines no tie-break between them, so none is invented after the fact.
    complexity = {"V1": 0, "V1_R": 1, "V1_T": 1, "V1_R_C1": 2, "V1_T_C1": 2, "V1_C1": 2, "OA_SVA": 3, "OA_XG": 3, "OA_SVA_C1": 4}
    pooled_vs_v1 = out["tiers"][next(iter(out["tiers"]))]["vs_V1"] if fresh2 else out["tiers"]["POOLED_2017_2025"]["vs_V1"]
    mask_pool = np.isin(season, seasons_all)
    ok = []
    for a in complexity:
        if a == "V1":
            ok.append(("V1", float(np.mean(losses["V1"]["brier_win"][mask_pool]))))
            continue
        if a not in arms:
            continue
        rows = [r for r in pooled_vs_v1 if r["challenger"] == a and r["metric"] in PRIMARY]
        if not any(r["worse_game_ci"] and r["worse_slate_ci"] for r in rows):
            ok.append((a, float(np.mean(losses[a]["brier_win"][mask_pool]))))
    best = min(v for _, v in ok)
    within = [a for a, v in ok if v - best < PRACTICAL["brier_win"]]
    lowest = min(complexity[a] for a in within)
    simplest = [a for a in within if complexity[a] == lowest]
    out["rules"]["R4_leading_candidate"] = {"eligible": [a for a, _ in ok], "lowest_brier_win": best, "within_practical_threshold_of_best": within,
                                            "simplest_within_threshold": simplest, "leads": simplest[0] if len(simplest) == 1 else "TIE: " + ", ".join(simplest),
                                            "note": "'leads' ranks historical evidence only; it is not a promotion"}
    out["calibration_win_pooled"] = {a: reliability(df.loc[mask_pool, f"{a}_p_home_win"].to_numpy(float), y[mask_pool]) for a in ("V1", "V1_R_C1", "OA_SVA_C1") if a in arms}
    if repo_root is not None and not fresh2:
        out["v2"] = v2_comparison(df, repo_root)
    if history is not None and (history / "kalshi").exists() and not fresh2:
        out["market"] = market_comparison(df, pm, history)
    bpath = dir_ / "v1r_boundary.json"
    if bpath.exists():
        out["grid_boundary"] = json.loads(bpath.read_text())
    return out


V2_FILES = ("docs/research/oa-walk-forward/data/walk_forward_v2_wf2_2023_games.csv", "docs/research/walk_forward_v2_wf2_20260929_games.csv")
V2_ARMS = ("SIM2", "SIM2_ST", "SIM2_ST_GTT")
MARKET_ARMS = ("V1", "V1_R", "V1_R_C1", "V1_T_C1", "OA_SVA_C1")


def v2_comparison(df: pd.DataFrame, repo_root: Path) -> dict[str, Any]:
    """Exploratory: the V2 simulator (SIM2 on V1's own rates; SIM2_ST with special teams; SIM2_ST_GTT with goalie talent) vs V1 and the
    retuned arms on the games where ``walk_forward_v2`` ran (2023-2025). Win and overtime Brier only (that is what the committed V2 output carries)."""
    frames = [pd.read_csv(repo_root / f) for f in V2_FILES if (repo_root / f).exists()]
    if not frames:
        return {"note": "walk_forward_v2 output not found"}
    v2 = pd.concat(frames, ignore_index=True)
    cols = ["game_id"] + [f"{a}_p_{k}" for a in V2_ARMS for k in ("home_win", "overtime") if f"{a}_p_{k}" in v2.columns]
    m = df.merge(v2[cols], on="game_id", how="inner", suffixes=("", "__v2"))
    y, yo = m["y_home_win"].to_numpy(float), m["y_overtime"].to_numpy(float)
    clusters = m["game_date"].astype(str).to_numpy()
    losses: dict[str, dict[str, np.ndarray]] = {}
    for name in ("V1", "V1_R", "V1_R_C1", "OA_SVA_C1", *V2_ARMS):
        pw, po = m[f"{name}_p_home_win"].to_numpy(float), m[f"{name}_p_overtime"].to_numpy(float)
        losses[name] = {"brier_win": (pw - y) ** 2, "brier_ot": (po - yo) ** 2}
    rows = compare(losses, "V1", [a for a in losses if a != "V1"], clusters, ("brier_win", "brier_ot"))
    return {"n": int(len(m)), "seasons": sorted(int(x) for x in m["season"].unique()), "levels": {a: {k: float(np.mean(v)) for k, v in d.items()} for a, d in losses.items()}, "vs_V1": rows,
            "note": "exploratory; V2 hazards need shots from 2021 so only 2023-2025 exist; the combination of retuned rates with the V2 simulator was NOT run"}


def market_comparison(df: pd.DataFrame, pm: dict[str, np.ndarray], history: Path, season: int = 2025, horizon: str = "T-60m") -> dict[str, Any]:
    """Kalshi candle-close midpoint at the same instant for every forecaster (2025-26 only); no depth, fee or slippage."""
    from nhl_edge.research import oa_market as M

    keep = (df["season"] == season).to_numpy()
    sub = df[keep].reset_index(drop=True)
    names = [str(a) for a in pm["arms"]]
    use = [a for a in MARKET_ARMS if a in names]
    idx = [names.index(a) for a in use]
    pms = {"arms": np.array(use), "total": pm["total"][keep][:, idx, :], "margin": pm["margin"][keep][:, idx, :]}
    targets = M.build_targets(history, sub, pms, horizon)
    return {"horizon": horizon, "season": season, "note": "Kalshi candle-close midpoint; a midpoint advantage is not an execution edge",
            "targets": {t: M.compare_target(d, use) for t, d in targets.items() if len(d) >= 100}}


def _verdict(r: dict[str, Any]) -> str:
    return ("BETTER (meaningful)" if r["practically_meaningful"] and r["delta"] < 0 else "WORSE (meaningful)" if r["practically_meaningful"] and r["delta"] > 0
            else "better, CI excludes 0" if r["better_game_ci"] and r["better_slate_ci"] else "worse, CI excludes 0" if r["worse_game_ci"] and r["worse_slate_ci"] else "indistinguishable")


def render(res: dict[str, Any]) -> str:
    L = ["# Retuned V1 vs opponent adjustment — preregistered evaluation", "",
         f"{res['n_games']} games, seasons {res['seasons']} · negative Δ = challenger better · 95% intervals: game bootstrap | slate-clustered bootstrap · RESEARCH_ONLY, nothing is promoted", ""]
    for name, t in res["tiers"].items():
        cols = list(next(iter(t["levels"].values())))
        L += [f"## {name} (n={t['n']})", "", "| arm | " + " | ".join(cols) + " | ECE(win) |", "|---|" + "---:|" * (len(cols) + 1)]
        for a, v in t["levels"].items():
            L.append(f"| {a} | " + " | ".join(f"{x:.4f}" for x in v.values()) + f" | {t['ece_win'][a]:.4f} |")
        for key, title in (("vs_V1", "paired vs production V1"), ("vs_V1_R_C1", "paired vs the retuned+recalibrated V1 (`V1_R_C1`)")):
            L += ["", f"Δ {title}:", "", "| challenger | metric | Δ | 95% games | 95% slates | verdict |", "|---|---|---:|---|---|---|"]
            for r in t[key]:
                if r["metric"] in ("brier_win", "rps_total", "brier_ot", "rps_margin") and r["challenger"] != r["incumbent"]:
                    L.append(f"| {r['challenger']} | {r['metric']} | {r['delta']:+.4f} | [{r['lo95']:+.4f}, {r['hi95']:+.4f}] | [{r['lo95_slate']:+.4f}, {r['hi95_slate']:+.4f}] | {_verdict(r)} |")
        L.append("")
    L += ["## Per season: Δ Brier(win) vs V1 (negative = better)", "", "| season | n | " + " | ".join(a for a in res["arms"] if a != "V1") + " |", "|---|---:|" + "---:|" * (len(res["arms"]) - 1)]
    for s, d in res["by_season"].items():
        L.append(f"| {s} | {d['n']} | " + " | ".join(f"{d['paired_win_vs_V1'][a]:+.4f}" for a in res["arms"] if a != "V1") + " |")
    L += ["", "## Preregistered decision rules", ""]
    for k, r in res["rules"].items():
        if k.startswith("R4"):
            L += [f"**{k}**: leads = `{r['leads']}`; within the practical threshold of the best: {r['within_practical_threshold_of_best']}; simplest of those: {r['simplest_within_threshold']} · {r['note']}", ""]
            continue
        L += [f"**{k}** — `{r['challenger']}` vs `{r['incumbent']}`: **{'BETTER' if r['BETTER'] else 'NOT BETTER'}** "
              f"(gate CIs {'ok' if r['gate_ok'] else 'fail'}; size ≥ threshold {'ok' if r['size_ok'] else 'fail'}; favourable seasons {r['seasons_favourable']}/{r['n_seasons']}; no primary metric worse {'ok' if r['no_primary_worse'] else 'FAIL'})", ""]
        L += ["| metric | Δ | 95% games | 95% slates |", "|---|---:|---|---|"]
        for p in r["pooled"]:
            L.append(f"| {p['metric']} | {p['delta']:+.4f} | [{p['lo95']:+.4f}, {p['hi95']:+.4f}] | [{p['lo95_slate']:+.4f}, {p['hi95_slate']:+.4f}] |")
        L.append("")
    L += ["## Feature ablations (R5; ablation minus `V1_R`, positive = the feature helps)", "", "| ablation | feature | metric | Δ | 95% games | 95% slates | informative |", "|---|---|---|---:|---|---|---|"]
    for a, d in res["ablations"].items():
        for p in d["pooled"]:
            L.append(f"| {a} | {d['feature']} | {p['metric']} | {p['delta']:+.4f} | [{p['lo95']:+.4f}, {p['hi95']:+.4f}] | [{p['lo95_slate']:+.4f}, {p['hi95_slate']:+.4f}] | {'yes' if d['informative'] else 'not detectable'} |")
    if "v2" in res and "vs_V1" in res["v2"]:
        v = res["v2"]
        L += ["", f"## V2 simulator (exploratory; {v['n']} games, seasons {v['seasons']}) — Δ vs V1", "", "| arm | metric | Δ | 95% games | 95% slates |", "|---|---|---:|---|---|"]
        for r in v["vs_V1"]:
            L.append(f"| {r['challenger']} | {r['metric']} | {r['delta']:+.4f} | [{r['lo95']:+.4f}, {r['hi95']:+.4f}] | [{r['lo95_slate']:+.4f}, {r['hi95_slate']:+.4f}] |")
        L.append(f"\n{v['note']}")
    if "market" in res:
        mk = res["market"]
        L += ["", f"## Against the Kalshi midpoint at {mk['horizon']} (season {mk['season']}); {mk['note']}", ""]
        for t, r in mk["targets"].items():
            L += [f"### {t} (n={r['n']}; market Brier {r['market_brier']:.4f})", "", "| forecaster | kind | Brier | Δ vs market | 95% games | verdict |", "|---|---|---:|---:|---|---|"]
            for a, m in r["forecasters"].items():
                if "+mkt" in a:
                    continue
                v = "model better" if m["model_better_than_market"] else "market better" if m["market_better_than_model"] else "indistinguishable"
                L.append(f"| {a} | {m['kind']} | {m['brier']:.4f} | {m['delta_brier_vs_market']:+.4f} | [{m['lo95']:+.4f}, {m['hi95']:+.4f}] | {v} |")
            L.append("")
    if "grid_boundary" in res:
        L += ["", "## Tuning grid boundaries (V1_R)", ""]
        for k, d in res["grid_boundary"].items():
            L.append(f"* `{k}`: selected {d['values']}; at lower edge in {d['at_lower_edge']}; at upper edge in {d['at_upper_edge']}")
    return "\n".join(L) + "\n"


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.retune_evaluate")
    ap.add_argument("--dir", required=True)
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--fresh2", action="store_true", help="evaluate the Amendment-2 tier (2010-2016); --also is the main run directory (for FRESH_ALL)")
    ap.add_argument("--also")
    a = ap.parse_args(argv)
    d = Path(a.dir)
    res = evaluate(d, Path(a.history), Path(a.repo_root), fresh2=a.fresh2, also=Path(a.also) if a.also else None)
    (d / "retune_eval.json").write_text(json.dumps(res, indent=1, default=float))
    md = render(res)
    (d / "retune_eval.md").write_text(md)
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
