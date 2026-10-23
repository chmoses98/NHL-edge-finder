"""Evaluation of J2 (docs/research/v2-joint-retuned/PREREGISTRATION.md): retuned and recalibrated V1 rates through the V2 simulator, scored jointly.

Everything is paired on the same games with the shared bootstraps (games and slates). Rules J2-A (additivity), J2-B (unchanged promotion scorecards for four targets)
and J2-C (complementary vs the better single fix) are applied exactly as registered; team totals, puck lines, the regulation 3-class outcome and the market
comparison are descriptive. Nothing here promotes anything.

    python -m nhl_edge.research.joint_retuned_eval --dirs OUT/shard* --out OUT --history data/history
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.evaluation.metrics import ece
from nhl_edge.research import joint_eval as J
from nhl_edge.research.oa_evaluate import compare, per_game_losses
from nhl_edge.research.promotion import score_challenger

INCUMBENT = "V1"
CHALLENGER = "RC_SIM2"
CLEAN2 = tuple(range(2010, 2017))
SEEN = tuple(range(2017, 2023))
EXPOSED = (2023, 2024, 2025)
TEAM_LINES = (1.5, 2.5, 3.5, 4.5)
PRIMARY = ("brier_win", "brier_ot", "rps_total", "rps_margin")
DESCRIPTIVE = ("brier_reg3", "brier_puck_line", "brier_team_total", "brier_over_5.5", "brier_over_6.5", "logloss_win", "brier_joint_margin", "brier_joint_total",
               "logscore_joint_margin", "logscore_joint_total")
ADDITIVITY_SLACK = 0.0005
PRACTICAL = {"brier_win": 0.0010, "brier_ot": 0.0010, "rps_total": 0.0050, "rps_margin": 0.0050}


def extra_losses(df: pd.DataFrame, arms: list[str]) -> dict[str, dict[str, np.ndarray]]:
    """Per-game losses for the preregistered targets that ``oa_evaluate.per_game_losses`` does not cover."""
    lpt = df["last_period_type"].astype(str).to_numpy()
    hs, as_ = df["home_score"].to_numpy(int), df["away_score"].to_numpy(int)
    reg = lpt == "REG"
    y_h, y_a, y_t = (reg & (hs > as_)).astype(float), (reg & (as_ > hs)).astype(float), (~reg).astype(float)
    y_hpl, y_apl = (hs - as_ >= 2).astype(float), (as_ - hs >= 2).astype(float)
    out: dict[str, dict[str, np.ndarray]] = {}
    for a in arms:
        ph, pt, pa = (df[f"{a}_p_reg_{k}"].to_numpy(float) for k in ("home", "tie", "away"))
        tt = []
        for L in TEAM_LINES:
            tt.append((df[f"{a}_p_home_o{L}"].to_numpy(float) - (hs > L)) ** 2)
            tt.append((df[f"{a}_p_away_o{L}"].to_numpy(float) - (as_ > L)) ** 2)
        out[a] = {"brier_reg3": (ph - y_h) ** 2 + (pt - y_t) ** 2 + (pa - y_a) ** 2,
                  "brier_puck_line": ((df[f"{a}_p_home_pl"].to_numpy(float) - y_hpl) ** 2 + (df[f"{a}_p_away_pl"].to_numpy(float) - y_apl) ** 2) / 2.0,
                  "brier_team_total": np.mean(tt, axis=0)}
    return out


def _sub(losses: dict[str, dict[str, np.ndarray]], mask: np.ndarray) -> dict[str, dict[str, np.ndarray]]:
    return {a: {k: v[mask] for k, v in d.items()} for a, d in losses.items()}


def _row(rows: list[dict[str, Any]], ch: str, metric: str) -> dict[str, Any]:
    return next(r for r in rows if r["challenger"] == ch and r["metric"] == metric)


def rules(losses: dict[str, dict[str, np.ndarray]], season: np.ndarray, clusters: np.ndarray, n_boot: int = 4000) -> dict[str, Any]:
    m = np.isin(season, CLEAN2)
    sub = _sub(losses, m)
    cl = clusters[m]
    vs_inc = compare(sub, INCUMBENT, [a for a in sub if a != INCUMBENT], cl, PRIMARY + DESCRIPTIVE, n_boot=n_boot)
    d = lambda ch, met: _row(vs_inc, ch, met)["delta"]  # noqa: E731
    pair = {}
    for ref in ("RC_SIM1", "SIM2", "R_SIM2"):
        rows = compare(sub, ref, [CHALLENGER], cl, PRIMARY + ("brier_joint_margin", "brier_joint_total"), n_boot=n_boot)
        pair[f"{CHALLENGER}_minus_{ref}"] = rows
    keeps_win = d(CHALLENGER, "brier_win") <= d("RC_SIM1", "brier_win") + ADDITIVITY_SLACK
    keeps_ot = d(CHALLENGER, "brier_ot") <= d("SIM2", "brier_ot") + ADDITIVITY_SLACK
    # J2-C: no worse than the better single fix by the practical threshold on each target, and the joint scores not worse than BOTH single fixes (interval excl. 0)
    complementary = True
    detail = {}
    for met in PRIMARY:
        best_single = min(d("RC_SIM1", met), d("SIM2", met))
        gap = d(CHALLENGER, met) - best_single
        detail[met] = {"challenger": d(CHALLENGER, met), "best_single_fix": best_single, "gap": gap}
        if gap > PRACTICAL[met]:
            complementary = False
    joint_ok = {}
    for met in ("brier_joint_margin", "brier_joint_total"):
        worse_than_both = all(_row(pair[f"{CHALLENGER}_minus_{ref}"], CHALLENGER, met)["worse_game_ci"] and _row(pair[f"{CHALLENGER}_minus_{ref}"], CHALLENGER, met)["worse_slate_ci"]
                              for ref in ("RC_SIM1", "SIM2"))
        joint_ok[met] = not worse_than_both
        complementary = complementary and not worse_than_both
    return {"tier": "CLEAN2 (2010-2016)", "n_games": int(m.sum()), "vs_incumbent": vs_inc, "pairwise": pair,
            "J2A_additive": {"keeps_win_gain": bool(keeps_win), "keeps_ot_gain": bool(keeps_ot), "ADDITIVE": bool(keeps_win and keeps_ot),
                             "win_delta_RC_SIM2": d(CHALLENGER, "brier_win"), "win_delta_RC_SIM1": d("RC_SIM1", "brier_win"),
                             "ot_delta_RC_SIM2": d(CHALLENGER, "brier_ot"), "ot_delta_SIM2": d("SIM2", "brier_ot")},
            "J2C_complementary": {"COMPLEMENTARY": bool(complementary), "per_metric": detail, "joint_not_worse_than_both_single_fixes": joint_ok}}


def scorecards(df: pd.DataFrame, losses: dict[str, dict[str, np.ndarray]], challenger: str = CHALLENGER, n_boot: int = 4000) -> dict[str, Any]:
    season = df["season"].to_numpy()
    clusters = df["game_date"].astype(str).to_numpy()
    arms = [challenger, INCUMBENT]
    un = np.isin(season, CLEAN2)
    metrics = PRIMARY + ("brier_over_5.5", "brier_over_6.5", "brier_joint_margin", "brier_joint_total")
    sub = _sub({a: losses[a] for a in arms}, un)
    pooled = compare(sub, INCUMBENT, [challenger], clusters[un], metrics, n_boot=n_boot)
    by_un = {str(s): compare(_sub({a: losses[a] for a in arms}, season == s), INCUMBENT, [challenger], clusters[season == s], PRIMARY, n_boot=1500) for s in CLEAN2 if (season == s).any()}
    ex_seasons = SEEN + EXPOSED
    by_ex = {str(s): compare(_sub({a: losses[a] for a in arms}, season == s), INCUMBENT, [challenger], clusters[season == s], PRIMARY, n_boot=1500) for s in ex_seasons if (season == s).any()}
    out: dict[str, Any] = {}
    targets = (("overtime / regulation tie", "brier_ot", f"{challenger}_p_overtime", f"{INCUMBENT}_p_overtime", "y_overtime"),
               ("goal-margin distribution", "rps_margin", f"{challenger}_p_home_win", f"{INCUMBENT}_p_home_win", "y_home_win"),
               ("win probability", "brier_win", f"{challenger}_p_home_win", f"{INCUMBENT}_p_home_win", "y_home_win"),
               ("total goals", "rps_total", f"{challenger}_p_over_5.5", f"{INCUMBENT}_p_over_5.5", None))
    for name, primary, pc, pi, ycol in targets:
        y = df[ycol].to_numpy(float) if ycol else (df["y_total"].to_numpy(float) > 5.5).astype(float)
        sc = score_challenger(target=name, challenger=challenger, incumbent=INCUMBENT, primary_metric=primary, pooled_unexposed=pooled, by_season_unexposed=by_un, exposed=by_ex,
                              n_unexposed_games=int(un.sum()), secondary_metrics=tuple(m for m in metrics if m != primary and m not in ("brier_joint_margin", "brier_joint_total")),
                              ece=(float(ece(df.loc[un, pc].to_numpy(float), y[un], 10)), float(ece(df.loc[un, pi].to_numpy(float), y[un], 10))))
        d = sc.to_dict()
        joint_bad = [f"{m} upper {r['hi95']:+.4f} > 0.0020" for m in ("brier_joint_margin", "brier_joint_total") if (r := _row(pooled, challenger, m))["hi95"] > J.JOINT_NON_INFERIORITY[m]]
        d["gates"].append({"gate": "J1_joint_non_inferiority", "passed": not joint_bad, "detail": "; ".join(joint_bad) or "joint margin and joint total Brier within 0.0020"})
        hard = [g for g in d["gates"] if g["passed"] is False]
        pend = [g for g in d["gates"] if g["passed"] is None]
        d["verdict"] = "RETAIN_INCUMBENT" if hard else ("SHADOW_MORE" if pend else "PROMOTE_CANDIDATE")
        out[name] = d
    return out


def tiers_table(losses: dict[str, dict[str, np.ndarray]], season: np.ndarray, clusters: np.ndarray, n_boot: int = 3000) -> dict[str, Any]:
    out = {}
    tiers = {"CLEAN2_2010_2016": CLEAN2, "SEEN_2017_2022": SEEN, "EXPOSED_2023_2025": EXPOSED, "POOLED_2010_2025": CLEAN2 + SEEN + EXPOSED, "3V3_2015_2025": tuple(range(2015, 2026))}
    for name, ss in tiers.items():
        m = np.isin(season, ss)
        if not m.any():
            continue
        sub = _sub(losses, m)
        out[name] = {"n": int(m.sum()), "levels": {a: {k: float(np.mean(v)) for k, v in d.items()} for a, d in sub.items()},
                     "vs_incumbent": compare(sub, INCUMBENT, [a for a in sub if a != INCUMBENT], clusters[m], PRIMARY + DESCRIPTIVE, n_boot=n_boot)}
    out["by_season"] = {str(s): {a: {k: float(np.mean(v[season == s] - losses[INCUMBENT][k][season == s])) for k, v in d.items() if k in PRIMARY} for a, d in losses.items() if a != INCUMBENT}
                        for s in sorted(set(int(x) for x in season))}
    return out


def mean_total_check(df: pd.DataFrame, arms: list[str]) -> dict[str, dict[str, float]]:
    """Predicted vs observed mean total goals and mean overtime rate per arm, by tier (calibration drift of the combination)."""
    season = df["season"].to_numpy()
    out = {}
    for tier, ss in (("CLEAN2", CLEAN2), ("SEEN", SEEN), ("EXPOSED", EXPOSED)):
        m = np.isin(season, ss)
        out[tier] = {"observed_total": float(df.loc[m, "y_total"].mean()), "observed_ot": float(df.loc[m, "y_overtime"].mean()),
                     **{f"{a}_total": float(df.loc[m, f"{a}_mean_total"].mean()) if f"{a}_mean_total" in df else float(df.loc[m, f"{a}_expected_total"].mean()) for a in arms},
                     **{f"{a}_ot": float(df.loc[m, f"{a}_p_overtime"].mean()) for a in arms}}
    return out


def market_2025(df: pd.DataFrame, pm: dict[str, np.ndarray], history: Path, arms: tuple[str, ...] = ("V1", "SIM2", "RC_SIM1", "RC_SIM2")) -> dict[str, Any]:
    """Kalshi midpoint at T-60 min for 2025-26 (winner, totals, puck line). Team totals and overtime have no usable quote history (empty / playoff-only series)."""
    from nhl_edge.research import oa_market as M

    keep = (df["season"] == 2025).to_numpy()
    names = [str(a) for a in pm["arms"]]
    idx = [names.index(a) for a in arms]
    sub = df[keep].reset_index(drop=True)
    pms = {"arms": np.array(arms), "total": pm["total"][keep][:, idx, :], "margin": pm["margin"][keep][:, idx, :]}
    t = M.build_targets(history, sub, pms, "T-60m")
    return {"horizon": "T-60m", "season": 2025, "targets": {k: M.compare_target(v, list(arms)) for k, v in t.items() if len(v) >= 100},
            "unavailable": ["team totals (KXNHLTEAMTOTAL has no markets in the history)", "overtime (KXNHLOVERTIME has 49 playoff markets only)"]}


def evaluate(dirs: list[str], history: Path | None = None, n_boot: int = 4000) -> dict[str, Any]:
    df, cm, ct, pm, metas = J._load_shards(dirs)
    arms = [str(a) for a in pm["arms"]]
    losses = per_game_losses(df, pm, arms)
    ex = extra_losses(df, arms)
    k_m, k_t = df["k_margin"].to_numpy(int), df["k_total"].to_numpy(int)
    for a in arms:
        losses[a].update(ex[a])
        losses[a].update({"brier_joint_margin": J.brier_cat(cm[a], k_m), "logscore_joint_margin": J.logscore_cat(cm[a], k_m),
                          "brier_joint_total": J.brier_cat(ct[a], k_t), "logscore_joint_total": J.logscore_cat(ct[a], k_t)})
    season = df["season"].to_numpy()
    clusters = df["game_date"].astype(str).to_numpy()
    res: dict[str, Any] = {"arms": arms, "n_games": int(len(df)), "seasons": sorted(int(s) for s in set(season)), "rules": rules(losses, season, clusters, n_boot),
                           "scorecards": scorecards(df, losses, CHALLENGER, n_boot), "tiers": tiers_table(losses, season, clusters), "mean_total_check": mean_total_check(df, arms),
                           "ot_conditionals": J.evaluate_joint(df, cm, ct, INCUMBENT, n_boot=1000)["ot_conditionals"]}
    res["fits"] = {k: v for m in metas for k, v in m["fits"].items()}
    if history is not None and (history / "kalshi").exists():
        res["market"] = market_2025(df, pm, history)
    return res


def _fmt(r: dict[str, Any]) -> str:
    return f"{r['delta']:+.4f} [{r['lo95']:+.4f}, {r['hi95']:+.4f}]"


def render(res: dict[str, Any]) -> str:
    L = ["# J2 — retuned + recalibrated V1 rates through the V2 simulator: joint results", "",
         f"{res['n_games']} games, seasons {res['seasons'][0]}–{res['seasons'][-1]} · incumbent `{INCUMBENT}` · negative Δ = better · 95% intervals (games | slates) · RESEARCH_ONLY, nothing is promoted", ""]
    r = res["rules"]
    a, c = r["J2A_additive"], r["J2C_complementary"]
    L += ["## Registered rules (decision tier CLEAN2 = 2010–2016)", "",
          f"* **J2-A additive: {a['ADDITIVE']}** — keeps the win gain {a['keeps_win_gain']} (Δwin RC_SIM2 {a['win_delta_RC_SIM2']:+.4f} vs RC_SIM1 {a['win_delta_RC_SIM1']:+.4f}); keeps the overtime gain {a['keeps_ot_gain']} (ΔOT RC_SIM2 {a['ot_delta_RC_SIM2']:+.4f} vs SIM2 {a['ot_delta_SIM2']:+.4f})",
          f"* **J2-C complementary: {c['COMPLEMENTARY']}** — joint scores not worse than both single fixes: {c['joint_not_worse_than_both_single_fixes']}", "",
          "| metric | RC_SIM2 Δ vs V1 | best single fix Δ | gap |", "|---|---:|---:|---:|"]
    for m, v in c["per_metric"].items():
        L.append(f"| {m} | {v['challenger']:+.4f} | {v['best_single_fix']:+.4f} | {v['gap']:+.4f} |")
    L += ["", "### Paired RC_SIM2 against the single fixes (CLEAN2)", "", "| comparison | metric | Δ | 95% games | 95% slates |", "|---|---|---:|---|---|"]
    for k, rows in r["pairwise"].items():
        for x in rows:
            L.append(f"| {k} | {x['metric']} | {x['delta']:+.4f} | [{x['lo95']:+.4f}, {x['hi95']:+.4f}] | [{x['lo95_slate']:+.4f}, {x['hi95_slate']:+.4f}] |")
    L += ["", "## Promotion scorecards for RC_SIM2 vs V1 (unchanged gates; unexposed = CLEAN2; the scorecard recommends, a human decides)", ""]
    for t, sc in res["scorecards"].items():
        L += [f"### {t}: **{sc['verdict']}**", "", "| gate | result | detail |", "|---|---|---|"]
        for g in sc["gates"]:
            L.append(f"| {g['gate']} | {'PASS' if g['passed'] else 'FAIL' if g['passed'] is False else 'pending'} | {g['detail']} |")
        L.append("")
    for tier, v in res["tiers"].items():
        if tier == "by_season":
            continue
        L += [f"## {tier} (n={v['n']})", "", "Levels:", "", "| arm | " + " | ".join(next(iter(v["levels"].values()))) + " |", "|---|" + "---:|" * len(next(iter(v["levels"].values())))]
        for arm, lv in v["levels"].items():
            L.append(f"| {arm} | " + " | ".join(f"{x:.4f}" for x in lv.values()) + " |")
        L += ["", "Δ vs V1:", "", "| arm | metric | Δ | 95% games | 95% slates |", "|---|---|---:|---|---|"]
        for x in v["vs_incumbent"]:
            if x["challenger"] in ("RC_SIM2", "RC_SIM1", "SIM2", "R_SIM2"):
                L.append(f"| {x['challenger']} | {x['metric']} | {x['delta']:+.4f} | [{x['lo95']:+.4f}, {x['hi95']:+.4f}] | [{x['lo95_slate']:+.4f}, {x['hi95_slate']:+.4f}] |")
        L.append("")
    L += ["## Mean total goals and overtime rate, predicted vs observed", "", "| tier | observed total | " + " | ".join(f"{a} total" for a in ("V1", "SIM2", "RC_SIM1", "RC_SIM2")) + " | observed OT | " + " | ".join(f"{a} OT" for a in ("V1", "SIM2", "RC_SIM1", "RC_SIM2")) + " |",
          "|---|" + "---:|" * 10]
    for tier, v in res["mean_total_check"].items():
        L.append(f"| {tier} | {v['observed_total']:.3f} | " + " | ".join(f"{v[f'{a}_total']:.3f}" for a in ("V1", "SIM2", "RC_SIM1", "RC_SIM2")) + f" | {v['observed_ot']:.3f} | " + " | ".join(f"{v[f'{a}_ot']:.3f}" for a in ("V1", "SIM2", "RC_SIM1", "RC_SIM2")) + " |")
    L += ["", "## Per season: Δ vs V1 on the primary metrics (RC_SIM2)", "", "| season | Δ win | Δ OT | Δ RPS total | Δ RPS margin |", "|---|---:|---:|---:|---:|"]
    for s, v in res["tiers"]["by_season"].items():
        x = v["RC_SIM2"]
        L.append(f"| {s} | {x['brier_win']:+.4f} | {x['brier_ot']:+.4f} | {x['rps_total']:+.4f} | {x['rps_margin']:+.4f} |")
    if "market" in res:
        mk = res["market"]
        L += ["", f"## Against the Kalshi midpoint at {mk['horizon']} (season {mk['season']}; no depth, fee or slippage; a midpoint advantage is not an execution edge)", ""]
        for t, rr in mk["targets"].items():
            L += [f"### {t} (n={rr['n']}; market Brier {rr['market_brier']:.4f})", "", "| forecaster | Brier | Δ vs market | 95% games | verdict |", "|---|---:|---:|---|---|"]
            for arm, m in rr["forecasters"].items():
                if "+mkt" in arm:
                    continue
                v = "model better" if m["model_better_than_market"] else "market better" if m["market_better_than_model"] else "indistinguishable"
                L.append(f"| {arm} | {m['brier']:.4f} | {m['delta_brier_vs_market']:+.4f} | [{m['lo95']:+.4f}, {m['hi95']:+.4f}] | {v} |")
            L.append("")
        L.append("Unavailable: " + "; ".join(mk["unavailable"]))
    return "\n".join(L) + "\n"


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.joint_retuned_eval")
    ap.add_argument("--dirs", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--n-boot", type=int, default=4000)
    a = ap.parse_args(argv)
    res = evaluate(a.dirs, Path(a.history), a.n_boot)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "j2_results.json").write_text(json.dumps(res, indent=1, default=float))
    md = render(res)
    (out / "j2_results.md").write_text(md)
    print(md[:3000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
