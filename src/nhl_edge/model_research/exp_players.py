"""M-PLAYER-1: PLAYER_SIM_V1 usage and outcome calibration at the T-60 cut (LIVE tier, descriptive; ex-post actuals are labels).

Questions: are expected ice time / PP time / shots / points biased or over-confident? How often does a priced player not dress? Is P(1+ point) calibrated?
    python -m nhl_edge.model_research.exp_players --archive <data-archive> --derived <work dir> --out docs/research/nhl-model-improvement/data
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.market_audit.games import read_kind
from nhl_edge.model_research import registry
from nhl_edge.model_research import scoring as S
from nhl_edge.model_research.live_dataset import dev_games
from nhl_edge.players import team_minutes as TM

OPTIONAL_META = ["meta_team_minutes_version", "meta_expected_toi_min_legacy", "meta_expected_pp_toi_min_legacy", "meta_expected_shots_legacy"]       # present only once another allocation is published
META = ["meta_expected_toi_min", "meta_expected_pp_toi_min", "meta_expected_shots", "meta_expected_goals", "meta_expected_assists", "meta_expected_points", "meta_toi_p10_p50_p90_min"]


def player_frame(archive: Path, derived: Path) -> pd.DataFrame:
    games = dev_games(archive)
    gm = games.set_index("game_id")
    import pyarrow.parquet as pq

    have = set(pq.read_schema(derived / "raw_predictions_player.parquet").names)
    pp = pd.read_parquet(derived / "raw_predictions_player.parquet", columns=["game_id", "player_id", "family", "threshold", "predicted_at_utc", "p_player", *META, *[c for c in OPTIONAL_META if c in have]])
    pp["game_id"] = pp["game_id"].astype(str)
    pp = pp[pp["game_id"].isin(gm.index)].copy()
    pp["cut"] = pp["game_id"].map(lambda g: gm.at[g, "start_time_utc"] - pd.Timedelta(minutes=60))
    pp["pa"] = pd.to_datetime(pp["predicted_at_utc"], utc=True)
    pp = pp[pp["pa"] <= pp["cut"]]
    pts = pp[(pp["family"] == "player_points") & (pp["threshold"] == 0.5)].sort_values("pa").groupby(["game_id", "player_id"]).tail(1)
    pts = pts[pts["meta_expected_toi_min"].notna()].copy()
    act = read_kind(archive, "player_events/players")
    act["game_id"] = act["game_id"].astype(str)
    act["player_id"] = act["player_id"].astype(float)
    pts["player_id"] = pts["player_id"].astype(float)
    df = pts.merge(act[["game_id", "player_id", "position", "goals", "assists", "points", "sog", "toi_s", "toi_pp_s"]], on=["game_id", "player_id"], how="left")
    df = TM.with_allocation(df)
    df["dressed"] = df["toi_s"].notna() & (df["toi_s"] > 0)
    for c in ("toi_s", "toi_pp_s"):
        df[c.replace("_s", "_min")] = df[c] / 60.0
    df[["p10", "p50", "p90"]] = pd.DataFrame(df["meta_toi_p10_p50_p90_min"].map(lambda v: json.loads(v) if isinstance(v, str) else list(v) if v is not None else [np.nan] * 3).tolist(), index=df.index)
    return df


def clustered_mean(x: pd.Series, groups: pd.Series, seed: int = 0) -> dict[str, float]:
    g = pd.DataFrame({"x": x.to_numpy(), "g": groups.to_numpy()}).dropna().groupby("g")["x"].agg(["sum", "count"])
    s, n = g["sum"].to_numpy(), g["count"].to_numpy()
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(s), size=(2000, len(s)))
    boots = s[idx].sum(axis=1) / n[idx].sum(axis=1)
    return {"mean": float(s.sum() / n.sum()), "lo95": float(np.quantile(boots, 0.025)), "hi95": float(np.quantile(boots, 0.975)), "n": int(n.sum()), "games": int(len(s))}


def allocation_blocks(d: pd.DataFrame) -> dict[str, Any]:
    """Mean errors of the PUBLISHED ice time, power-play time and shots, one block per team-minute allocation that drove the rows (allocations are never pooled)."""
    out: dict[str, Any] = {}
    for a, g in d.groupby("alloc"):
        out[str(a)] = {"n": int(len(g)), "games": int(g["game_id"].nunique()),
                       "bias_toi_min": clustered_mean(g["toi_min"] - g["meta_expected_toi_min"], g["game_id"]), "bias_pp_min": clustered_mean(g["toi_pp_min"] - g["meta_expected_pp_toi_min"], g["game_id"]),
                       "bias_shots": clustered_mean(g["sog"] - g["meta_expected_shots"], g["game_id"])}
    return out


def run(archive: Path, derived: Path) -> dict[str, Any]:
    df = player_frame(archive, derived)
    d = df[df["dressed"]].copy()
    out: dict[str, Any] = {"n_priced_player_games": int(len(df)), "n_dressed": int(len(d)), "share_priced_not_dressed": float(1 - len(d) / len(df)),
                           "share_priced_not_dressed_by_position": {str(k): float(v) for k, v in (1 - df.groupby("position", dropna=False)["dressed"].mean()).items()}}
    # allocation-aware: the top-level statistics use the INCUMBENT (team-minutes-0) minutes and shots for every row (the legacy-equivalent field when another allocation was published);
    # `by_allocation` reports the values exactly as published, one block per allocation, never pooled
    out["allocations_seen"] = {str(k): int(v) for k, v in d["alloc"].value_counts().items()}
    out["by_allocation"] = allocation_blocks(d)
    for c in TM.INCUMBENT_COLUMNS:
        d[c] = d[f"{c}_incumbent"]
    d["toi_err"] = d["toi_min"] - d["meta_expected_toi_min"]
    d["pp_err"] = d["toi_pp_min"] - d["meta_expected_pp_toi_min"]
    d["shots_err"] = d["sog"] - d["meta_expected_shots"]
    d["pts_err"] = d["points"] - d["meta_expected_points"]
    d["goals_err"] = d["goals"] - d["meta_expected_goals"]
    d["ast_err"] = d["assists"] - d["meta_expected_assists"]
    for k in ("toi_err", "pp_err", "shots_err", "pts_err", "goals_err", "ast_err"):
        out[f"bias_{k}"] = clustered_mean(d[k], d["game_id"])
    out["mae_toi_min"] = float(d["toi_err"].abs().mean())
    out["rmse_toi_min"] = float(math.sqrt((d["toi_err"] ** 2).mean()))
    out["mean_expected_toi_min"] = float(d["meta_expected_toi_min"].mean())
    ok = d[["p10", "p90"]].notna().all(axis=1) & (d["alloc"] == TM.LEGACY_VERSION)       # the stated band is a published (allocation-specific) quantity: only the incumbent's rows
    inside = ((d["toi_min"] >= d["p10"]) & (d["toi_min"] <= d["p90"]))[ok]
    out["toi_p10_p90_coverage"] = {"observed": float(inside.mean()), "nominal": 0.80, "n": int(ok.sum()), "note": "< 0.80 means the stated TOI interval is too NARROW; incumbent-allocation rows only"}
    # shots dispersion vs Poisson (per player-game): Var(actual)/mean(expected)
    out["shots_dispersion"] = {"obs_var_over_mean_actual": float(d["sog"].var() / d["sog"].mean()), "mean_actual": float(d["sog"].mean()), "mean_expected": float(d["meta_expected_shots"].mean())}
    # expected-vs-actual by decile of expectation (calibration of the mean)
    for nm, e, a in (("points", "meta_expected_points", "points"), ("shots", "meta_expected_shots", "sog"), ("toi", "meta_expected_toi_min", "toi_min")):
        q = pd.qcut(d[e], 5, duplicates="drop")
        t = d.groupby(q, observed=True).agg(expected=(e, "mean"), actual=(a, "mean"), n=(a, "size"))
        out[f"calibration_{nm}_by_quintile"] = t.reset_index(drop=True).to_dict("records")
    # P(1+ point) reliability among dressed players
    y = (d["points"] >= 1).astype(float).to_numpy()
    p = d["p_player"].to_numpy()
    out["p_1plus_point"] = {"n": int(len(d)), "mean_p": float(p.mean()), "obs_rate": float(y.mean()), "brier": float(S.brier(p, y).mean()), "brier_constant_league_rate": float(S.brier(np.full(len(y), y.mean()), y).mean()),
                            "table": S.calibration_table(p, y, 8)}
    out["by_position_toi_bias"] = d.groupby("position")["toi_err"].agg(["mean", "count"]).reset_index().to_dict("records")
    return out


def record(res: dict[str, Any], repo: Path, reg: Path) -> None:
    ents = registry.read(reg)
    if not any(e["id"] == "M-PLAYER-1" for e in ents):
        registry.append(reg, "PREREG", "M-PLAYER-1", {
            "hypothesis": "PLAYER_SIM_V1 usage assumptions (ice time, power-play time, shots) are biased or over-confident, and P(1+ point) is miscalibrated.",
            "motivation": "Operator question: were player projections using incorrect usage assumptions?",
            "method": "Last PLAYER_SIM prediction at or before T-60 per (game, player) (meta expectations) vs archived player events; game-clustered bootstrap of mean errors; TOI p10-p90 coverage; shots variance/mean; P(1+ point) reliability and Brier vs league rate.",
            "baseline": "zero bias; nominal 80% interval; league-constant point rate", "decision_rule": "BIASED if the game-clustered 95% CI of the mean error excludes 0; INTERVAL_TOO_NARROW if coverage < 0.80 with n>=1000. Descriptive.",
            "tier": "LIVE_DESCRIPTIVE", "disclosure": "registered after the first execution of this script (code written before executing; not edited after)."}, repo)
    if not any(e["id"] == "M-PLAYER-1" and e["type"] == "RESULT" for e in registry.read(reg)):
        biased = [k for k in ("toi_err", "pp_err", "shots_err", "pts_err", "goals_err", "ast_err") if res[f"bias_{k}"]["lo95"] > 0 or res[f"bias_{k}"]["hi95"] < 0]
        registry.append(reg, "RESULT", "M-PLAYER-1", {"metrics": {k: v for k, v in res.items() if not k.startswith("calibration_")}, "decision": "BIASED_USAGE:" + ",".join(biased),
                                                       "interpretation": "see docs/research/nhl-model-improvement/PLAYER_AND_GOALIE_STUDY.md",
                                                       "reproduction": "python -m nhl_edge.model_research.exp_players --archive <data-archive> --derived <work dir> --out docs/research/nhl-model-improvement/data --record",
                                                       "results_file": "docs/research/nhl-model-improvement/data/player_usage.json"}, repo)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", type=Path, required=True)
    ap.add_argument("--derived", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--record", action="store_true")
    a = ap.parse_args()
    r = run(a.archive, a.derived)
    (a.out / "player_usage.json").write_text(json.dumps(r, indent=1, default=float))
    if a.record:
        record(r, a.repo, a.repo / "docs/research/nhl-model-improvement/experiment_registry.jsonl")
    for k in ("n_priced_player_games", "n_dressed", "share_priced_not_dressed", "bias_toi_err", "bias_pp_err", "bias_shots_err", "bias_pts_err", "bias_goals_err", "bias_ast_err", "mae_toi_min", "toi_p10_p90_coverage", "shots_dispersion", "p_1plus_point"):
        v = r[k]
        print(k, v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items() if kk != "table"})
