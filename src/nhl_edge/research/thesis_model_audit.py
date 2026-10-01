"""Targeted model audit for the thesis-card work (Phase 12). Diagnostic only: nothing here changes a parameter.

A. Goal attribution concentration (does the simulator over- or under-concentrate team goals in top players?)
   1. held-out walk-forward 2025-26 (``docs/research/player_sim_v1/skaters_2025.parquet``, 47k skater-games): each
      player's predicted share of his team's expected goals, s = e_g / sum(team e_g); conditional on the team's REALISED
      goals G, the allocation implies E[goals | G] = G s and P(1+ | G) ~ 1 - (1 - s)^G. Compared with realised goals by
      predicted-share bucket -- a direct test of P(player scores | team scores G) that the market props depend on;
   2. distinct scorers and the top scorer's share given team goals N: simulated (the replayed slate's joint draws) vs
      official history (2023-24 .. 2025-26 regular seasons; pooled league and the same six clubs).
B. Goalie saves: expected shots faced vs actual (held-out), shots against by the goalie team's regulation margin
   (history vs the simulated draws), replacement (pull) rate, and the prospective sample size.
C. TOI: held-out model vs recent mean (existing evidence) and the prospective line-informed forecasts vs a recent-mean
   baseline on the games played so far.
D. Assists / points: held-out calibration buckets (compression) and prospective counts vs the market. No recalibration.
"""

from __future__ import annotations

import gzip
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.config import REPO_ROOT
from nhl_edge.data.player_history import load_player_tables

WF = REPO_ROOT / "docs" / "research" / "player_sim_v1"


def _r(x: Any, n: int = 4) -> Any:
    return None if x is None or (isinstance(x, float) and not np.isfinite(x)) else round(float(x), n)


# ------------------------------------------------------------------------------------------------ A
def attribution_walk_forward(path: Path = WF / "skaters_2025.parquet") -> dict[str, Any]:
    sk = pd.read_parquet(path)
    sk = sk[sk["toi_s"].fillna(0) > 0].copy()
    team = sk.groupby(["game_id", "team_id"]).agg(G=("y_g", "sum"), EG=("e_g", "sum")).reset_index()
    sk = sk.merge(team, on=["game_id", "team_id"])
    sk = sk[(sk["G"] >= 1) & (sk["EG"] > 0)]
    sk["share"] = sk["e_g"] / sk["EG"]
    sk["exp_given_G"] = sk["G"] * sk["share"]
    sk["p1_given_G"] = 1 - (1 - sk["share"]) ** sk["G"]
    edges = [0, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.16, 1.0]
    sk["bucket"] = pd.cut(sk["share"], edges, right=False)
    rows = []
    for b, g in sk.groupby("bucket", observed=True):
        rows.append({"predicted_share": str(b), "n": int(len(g)), "goals_expected_given_G": _r(g["exp_given_G"].sum(), 1), "goals_actual": int(g["y_g"].sum()),
                     "ratio_actual_over_expected": _r(g["y_g"].sum() / g["exp_given_G"].sum(), 3),
                     "p1_expected_given_G": _r(g["p1_given_G"].mean()), "p1_actual": _r((g["y_g"] >= 1).mean())})
    by_g = []
    for G in (2, 3, 4, 5):
        g = sk[sk["G"] == G]
        top = g.sort_values("share", ascending=False).groupby(["game_id", "team_id"]).head(3)
        by_g.append({"team_goals": G, "top3_predicted_players_expected_goals": _r(top["exp_given_G"].sum(), 1), "top3_actual_goals": int(top["y_g"].sum()),
                     "ratio": _r(top["y_g"].sum() / top["exp_given_G"].sum(), 3), "n_team_games": int(g.groupby(["game_id", "team_id"]).ngroups)})
    hi = sk[sk["share"] >= 0.11]
    verdict_ratio = float(hi["y_g"].sum() / hi["exp_given_G"].sum())
    return {"n_skater_games": int(len(sk)), "by_predicted_share": rows, "top3_by_team_goals": by_g, "high_share_ratio": _r(verdict_ratio, 3),
            "reading": ("ratio < 1 for high predicted shares would mean the simulator OVER-concentrates goals in top players (they score less of the team's "
                        "goals than allocated); > 1 under-concentrates. Binomial noise on ~1-3k goals per bucket is roughly +-3-5%.")}


def scorer_structure_history(clubs: list[int] | None = None, seasons: tuple[int, ...] = (2023, 2024, 2025)) -> dict[str, Any]:
    gl = load_player_tables(REPO_ROOT / "data" / "history", "goals")
    gl = gl[(gl["game_type"] == 2) & gl["season"].isin(seasons) & (gl["period_type"] != "SO")]
    if clubs:
        gl = gl[gl["team_id"].isin(clubs)]
    out = {}
    for _key, g in gl.groupby(["game_id", "team_id"]):
        n = len(g)
        if 1 <= n <= 6:
            c = g["scorer_id"].value_counts()
            out.setdefault(n, []).append((len(c), int(c.iloc[0])))
    return {n: {"n_team_games": len(v), "mean_distinct_scorers": _r(np.mean([x[0] for x in v]), 3), "p_someone_2plus": _r(np.mean([x[1] >= 2 for x in v]), 4),
                "mean_top_scorer_share": _r(np.mean([x[1] / n for x in v]), 4)} for n, v in sorted(out.items())}


def scorer_structure_sim(dists: list[Any]) -> dict[int, dict[str, Any]]:
    acc: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for d in dists:
        ps = d.meta.get("_ps")
        if ps is None:
            continue
        for td in (ps.home, ps.away):
            G = td.goals.astype(int)
            tot = G.sum(axis=1)
            distinct = (G > 0).sum(axis=1)
            top = G.max(axis=1)
            for n in range(1, 7):
                m = tot == n
                acc[n] += list(zip(distinct[m].tolist(), top[m].tolist()))
    return {n: {"n_team_draws": len(v), "mean_distinct_scorers": _r(np.mean([x[0] for x in v]), 3), "p_someone_2plus": _r(np.mean([x[1] >= 2 for x in v]), 4),
                "mean_top_scorer_share": _r(np.mean([x[1] / n for x in v]), 4)} for n, v in sorted(acc.items())}


def conditional_player_goals(dists: list[Any], top_k: int = 4) -> list[dict[str, Any]]:
    """P(player 1+ goal | team goals >= N) from the joint draws for each team's top-k goal threats, next to the player's
    own 2025-26 empirical rate in games where his team scored >= N (small samples: context, not a test)."""
    pl = load_player_tables(REPO_ROOT / "data" / "history", "players")
    pl = pl[(pl["game_type"] == 2) & (pl["season"] == 2025) & (pl["toi_s"].fillna(0) > 0)]
    tg = pl.groupby(["game_id", "team_id"])["goals"].sum().rename("team_goals").reset_index()
    pl = pl.merge(tg, on=["game_id", "team_id"])
    out = []
    for d in dists:
        ps = d.meta.get("_ps")
        if ps is None:
            continue
        for td, ro in ((ps.home, ps.home_roster), (ps.away, ps.away_roster)):
            tot = td.goals.sum(axis=1)
            for i in np.argsort(-(td.goals >= 1).mean(axis=0))[:top_k]:
                pid = int(ro.player_ids[i])
                h = pl[pl["player_id"] == pid]
                row = {"player": ro.names[i], "team": ro.abbrev, "p_goal": _r((td.goals[:, i] >= 1).mean())}
                for N in (3, 4):
                    m = tot >= N
                    row[f"sim_p_goal_given_team_{N}plus"] = _r((td.goals[m, i] >= 1).mean()) if m.any() else None
                    row[f"sim_p_team_{N}plus_given_goal"] = _r(m[td.goals[:, i] >= 1].mean()) if (td.goals[:, i] >= 1).any() else None
                    hh = h[h["team_goals"] >= N]
                    row[f"hist_2025_p_goal_given_team_{N}plus"] = _r((hh["goals"] >= 1).mean()) if len(hh) else None
                    row[f"hist_2025_n_games_team_{N}plus"] = int(len(hh))
                out.append(row)
    return out


# ------------------------------------------------------------------------------------------------ B
def saves_audit(dists: list[Any]) -> dict[str, Any]:
    g = pd.read_parquet(WF / "goalies_2025.parquet")
    calib = {"n_starts": int(len(g)), "mean_expected_faced": _r(g["expected_faced"].mean(), 2), "mean_actual_faced": _r(g["y_sa"].mean(), 2),
             "mean_expected_saves": _r(g["e_saves"].mean(), 2), "mean_actual_saves": _r(g["y_saves"].mean(), 2),
             "corr_expected_vs_actual_faced": _r(np.corrcoef(g["expected_faced"], g["y_sa"])[0, 1], 3),
             "p_replaced_mean_pred": _r(g["p_replaced"].mean()), "replaced_actual": _r((g["toi_s"] < 3300).mean())}
    q = pd.qcut(g["expected_faced"], 5)
    calib["by_expected_faced_quintile"] = [{"bucket": str(b), "n": int(len(x)), "expected": _r(x["expected_faced"].mean(), 2), "actual": _r(x["y_sa"].mean(), 2)}
                                           for b, x in g.groupby(q, observed=True)]
    # score effects: shots against by the goalie team's regulation margin (history) vs simulated draws
    hist = load_player_tables(REPO_ROOT / "data" / "history", "goalies")
    hist = hist[(hist["game_type"] == 2) & hist["season"].isin((2023, 2024, 2025))]
    net = hist.groupby(["game_id", "team_id"])["shots_against"].sum().rename("sa").reset_index()
    gl = load_player_tables(REPO_ROOT / "data" / "history", "goals")
    gl = gl[(gl["game_type"] == 2) & gl["season"].isin((2023, 2024, 2025)) & (gl["period"] <= 3)]
    gf = gl.groupby(["game_id", "team_id"]).size().rename("gf").reset_index()
    games = hist[["game_id", "home_team_id", "away_team_id"]].drop_duplicates()
    net = net.merge(games, on="game_id")
    net["opp"] = np.where(net["team_id"] == net["home_team_id"], net["away_team_id"], net["home_team_id"])
    net = net.merge(gf, on=["game_id", "team_id"], how="left").merge(gf.rename(columns={"team_id": "opp", "gf": "ga"}), on=["game_id", "opp"], how="left").fillna({"gf": 0, "ga": 0})
    net["margin"] = (net["gf"] - net["ga"]).clip(-3, 3)
    hist_by = {int(k): _r(v, 2) for k, v in net.groupby("margin")["sa"].mean().items()}
    sim_acc: dict[int, list[float]] = defaultdict(list)
    for d in dists:
        f = d.features
        for faced, margin in ((f.home_net_faced, f.home_reg - f.away_reg), (f.away_net_faced, f.away_reg - f.home_reg)):
            mm = np.clip(margin, -3, 3)
            for k in range(-3, 4):
                sel = faced[mm == k]
                if len(sel):
                    sim_acc[k].append(float(sel.mean() - faced.mean()))
    sim_by = {k: _r(np.mean(v), 2) for k, v in sorted(sim_acc.items())}
    hist_mean = float(net["sa"].mean())
    return {"held_out_calibration_2025": calib,
            "shots_against_by_goalie_team_reg_margin_history": hist_by,
            "history_deviation_from_mean": {k: _r(v - hist_mean, 2) for k, v in hist_by.items() if v is not None},
            "simulated_deviation_from_game_mean": sim_by,
            "reading": ("history: a net whose team LEADS faces more shots (the trailing side presses); the simulated draws should show the same sign "
                        "and similar size. Simulated values are deviations from each net's own simulated mean (matchup differences removed).")}


# ------------------------------------------------------------------------------------------------ C / D prospective
def _read_kind(archive: Path, kind: str) -> list[dict[str, Any]]:
    out = []
    man = archive / "manifest.jsonl"
    if not man.exists():
        return out
    for line in man.read_text().splitlines():
        e = json.loads(line)
        if e.get("kind") == kind:
            with gzip.open(archive / e["path"], "rt") as fh:
                out += [json.loads(x) for x in fh if x.strip()]
    return out


def toi_prospective(archive: Path) -> dict[str, Any]:
    preds = _read_kind(archive, "predictions_player")
    actual = {(str(r["game_id"]), int(r["player_id"])): r for r in _read_kind(archive, "player_events/players")}
    last: dict[tuple[str, int], dict[str, Any]] = {}
    for p in preds:
        if p.get("player_id") is None or p.get("meta_expected_toi_min") is None or not p.get("pregame"):
            continue
        k = (str(p["game_id"]), int(p["player_id"]))
        if k not in last or p["predicted_at_utc"] > last[k]["predicted_at_utc"]:
            last[k] = p
    hist = load_player_tables(REPO_ROOT / "data" / "history", "players")
    hist = hist[(hist["game_type"] == 2) & (hist["toi_s"].fillna(0) > 0)].sort_values("game_date")
    rows = []
    for (gid, pid), p in last.items():
        a = actual.get((gid, pid))
        if a is None or not a.get("toi_s"):
            continue
        h = hist[(hist["player_id"] == pid) & (hist["game_date"] < str(p["predicted_at_utc"])[:10])].tail(10)
        rows.append({"src": p.get("meta_deployment_source"), "model": float(p["meta_expected_toi_min"]), "actual": a["toi_s"] / 60.0,
                     "recent": float(h["toi_s"].mean() / 60.0) if len(h) else np.nan})
    df = pd.DataFrame(rows)
    if df.empty:
        return {"n": 0, "note": "no settled prospective player-games with TOI forecasts in the archive"}
    out = {"n_player_games": int(len(df)), "n_games": len({k[0] for k in last if k in actual})}
    for src, g in [("ALL", df)] + list(df.groupby("src")):
        gg = g.dropna(subset=["recent"])
        out[str(src)] = {"n": int(len(g)), "mae_model_min": _r((g["model"] - g["actual"]).abs().mean(), 3), "bias_model_min": _r((g["model"] - g["actual"]).mean(), 3),
                         "mae_recent_mean_min_same_rows": _r((gg["recent"] - gg["actual"]).abs().mean(), 3), "mae_model_min_same_rows": _r((gg["model"] - gg["actual"]).abs().mean(), 3),
                         "n_with_recent_mean": int(len(gg))}
    return out


def prospective_families(archive: Path) -> dict[str, Any]:
    ev = _read_kind(archive, "evaluations_player")
    last: dict[str, dict[str, Any]] = {}
    for r in ev:
        if not r.get("pregame") or r.get("p_player") is None:
            continue
        if r["ticker"] not in last or r["predicted_at_utc"] > last[r["ticker"]]["predicted_at_utc"]:
            last[r["ticker"]] = r
    out = {}
    for fam in sorted({r["family"] for r in last.values()}):
        rs = [r for r in last.values() if r["family"] == fam]
        m = [r for r in rs if r.get("p_market") is not None]
        out[fam] = {"n_contracts_last_pregame": len(rs), "n_games": len({r["game_id"] for r in rs}),
                    "brier_model": _r(np.mean([(r["p_player"] - r["y"]) ** 2 for r in rs])),
                    "brier_model_on_market_rows": _r(np.mean([(r["p_player"] - r["y"]) ** 2 for r in m])) if m else None,
                    "brier_market": _r(np.mean([(r["p_market"] - r["y"]) ** 2 for r in m])) if m else None, "n_market_rows": len(m),
                    "mean_p_model": _r(np.mean([r["p_player"] for r in rs])), "hit_rate": _r(np.mean([r["y"] for r in rs]))}
    return out


def held_out_compression() -> dict[str, Any]:
    d = json.loads((WF / "eval.json").read_text())["final (PLAYER_SIM_V1: fringe prior + goal co-presence k=10)"]["2025"]["skaters"]
    out = {}
    for k in ("assists 1+", "points 1+"):
        out[k] = [{"bucket": b["bucket"], "n": b["n"], "gap": _r(b["gap"]), "z": _r(b["gap"] / b["se"], 1)} for b in d[k]["buckets"] if b["n"] >= 300]
    return out


def run(dists: list[Any], archive: Path | None) -> dict[str, Any]:
    clubs = sorted({x for d in dists for x in (d.home_team_id, d.away_team_id)})
    out = {"authority": "RESEARCH_ONLY", "note": "diagnostic only; no parameter was changed",
           "A_attribution_walk_forward_2025": attribution_walk_forward(),
           "A_scorer_structure_history_league": scorer_structure_history(), "A_scorer_structure_history_same_clubs": scorer_structure_history(clubs),
           "A_scorer_structure_simulated": scorer_structure_sim(dists), "A_conditional_player_goals": conditional_player_goals(dists),
           "B_saves": saves_audit(dists), "D_held_out_compression": held_out_compression()}
    if archive is not None:
        out["C_toi_prospective"] = toi_prospective(archive)
        out["D_prospective_families"] = prospective_families(archive)
    return out
