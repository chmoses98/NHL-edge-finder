"""Score NHL_SHOT_VOLUME_V1 against PLAYER_SIM_V1 (incumbent) and RECENT_MEAN_10 (simple baseline). RESEARCH_ONLY.

Reads the per-row frames written by ``python -m nhl_edge.research.shot_volume_v1 --mode eval`` and reports, per
statistic and on matched player-game rows only: MAE and MSE of the mean, exact CRPS of the simulated distribution,
log score (PMF floored at 1/(2 n)), p10-p90 coverage and PIT deciles, each as paired, game-clustered percentile
bootstrap deltas. It also writes pure_forecast.v1 sidecars + sports-sourced outcomes and runs the vendored pure_gate
``validate --require-v1`` and ``compare`` on them (one statistic at a time to bound memory).

Run: ``python -m nhl_edge.research.shot_volume_eval --rows <dir> --season 2025 --out docs/research/opportunity_efficiency``
"""

from __future__ import annotations

import argparse
import gzip
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.research.opportunity_efficiency import cluster_boot
from nhl_edge.research.shot_volume_v1 import (
    BASELINE_VERSION,
    INCUMBENT_VERSION,
    MODEL_VERSION,
    STATS,
    frame_rows,
    to_outcome,
    to_pure,
    write_jsonl,
)

PAIRS = ((INCUMBENT_VERSION, MODEL_VERSION), (BASELINE_VERSION, MODEL_VERSION), (BASELINE_VERSION, INCUMBENT_VERSION))
GATE = Path(__file__).resolve().parents[3] / "tools" / "pure_gate" / "pure_gate.py"


def load(rows_dir: Path, season: int) -> dict[str, pd.DataFrame]:
    return {arm: pd.read_parquet(rows_dir / f"rows_{arm}_{season}.parquet") for arm in (INCUMBENT_VERSION, MODEL_VERSION, BASELINE_VERSION)}


def pair_metrics(a: pd.DataFrame, b: pd.DataFrame, stat: str) -> dict[str, Any]:
    k = ["game_id", "player_id"]
    j = a[a["statistic"] == stat].merge(b[b["statistic"] == stat], on=k, suffixes=("_a", "_b"))
    if not len(j):
        return {"n": 0}
    g = j["game_id"].to_numpy()
    y = j["actual_a"].to_numpy(float)
    if not np.allclose(y, j["actual_b"].to_numpy(float)):
        raise ValueError(f"{stat}: outcome mismatch between arms")
    ma, mb = j["mean_a"].to_numpy(float), j["mean_b"].to_numpy(float)
    out: dict[str, Any] = {"n_rows": int(len(j)), "n_games": int(len(np.unique(g)))}
    for arm, m, sfx in (("a", ma, "_a"), ("b", mb, "_b")):
        out[arm] = {"mae": float(np.mean(np.abs(m - y))), "rmse": float(np.sqrt(np.mean((m - y) ** 2))), "bias": float(np.mean(m - y)),
                    "crps": float(j["crps" + sfx].mean()), "coverage_p10_p90": float(j["in80" + sfx].mean()),
                    "pit_deciles": np.histogram(j["pit" + sfx].to_numpy(float), bins=np.linspace(0, 1, 11))[0].tolist()}
        if stat != "time_on_ice_min":
            out[arm]["log_score"] = float(j["log_score" + sfx].mean())
    d = {"mae": cluster_boot(g, np.abs(ma - y), np.abs(mb - y)), "mse": cluster_boot(g, (ma - y) ** 2, (mb - y) ** 2),
         "crps": cluster_boot(g, j["crps_a"].to_numpy(float), j["crps_b"].to_numpy(float)),
         "coverage_p10_p90": cluster_boot(g, j["in80_a"].to_numpy(float), j["in80_b"].to_numpy(float))}
    if stat != "time_on_ice_min":
        d["log_score"] = cluster_boot(g, j["log_score_a"].to_numpy(float), j["log_score_b"].to_numpy(float))
    out["delta_b_minus_a"] = d
    out["identical_rows"] = bool(np.array_equal(ma, mb) and np.array_equal(j["crps_a"].to_numpy(), j["crps_b"].to_numpy()))
    # preregistered subgroups (descriptive)
    month = (j["date_int_a"] // 100) % 100
    early = month.isin([10, 11]).to_numpy()
    sg = {"oct_nov": early, "dec_onward": ~early}
    if stat != "goalie_saves":
        sg.update({"F": (j["pos_a"] == "F").to_numpy(), "D": (j["pos_a"] == "D").to_numpy()})
    out["subgroups"] = {name: {"n_rows": int(m.sum()), "d_crps": cluster_boot(g[m], j["crps_a"].to_numpy(float)[m], j["crps_b"].to_numpy(float)[m]),
                               "d_mae": cluster_boot(g[m], np.abs(ma - y)[m], np.abs(mb - y)[m])} for name, m in sg.items() if m.sum() > 30}
    return out


def evaluate(frames: dict[str, pd.DataFrame]) -> dict[str, Any]:
    res: dict[str, Any] = {}
    for a, b in PAIRS:
        res[f"{b}_vs_{a}"] = {stat: pair_metrics(frames[a], frames[b], stat) for stat in STATS}
    res["row_counts"] = {arm: frames[arm].groupby("statistic").size().to_dict() for arm in frames}
    return res


def run_gate(frames: dict[str, pd.DataFrame], hashes: dict[str, str], work: Path, sample_games: int = 40) -> dict[str, Any]:
    """Write pure_forecast.v1 sidecars per statistic, validate (--require-v1) and compare each pair with the vendored
    gate. Keeps a small gzipped sample (first ``sample_games`` games) of every sidecar for the commit."""
    work.mkdir(parents=True, exist_ok=True)
    out: dict[str, Any] = {"validate": {}, "compare": {}}
    first_games = sorted(frames[MODEL_VERSION]["game_id"].unique())[:sample_games]
    for stat in STATS:
        files = {}
        for arm, df in frames.items():
            rows = frame_rows(df[df["statistic"] == stat])
            pure = [to_pure(r, arm, hashes[arm]) for r in rows]
            f = work / f"{arm}_{stat}.jsonl"
            write_jsonl(f, pure)
            files[arm] = f
            with gzip.open(work / f"sample_{arm}_{stat}.jsonl.gz", "wt", encoding="utf-8") as z:
                for p in pure:
                    if int(p["game_id"]) in first_games:
                        z.write(json.dumps(p, sort_keys=True) + "\n")
            if arm == MODEL_VERSION:
                write_jsonl(work / f"outcomes_{stat}.jsonl", [to_outcome(r) for r in rows])
                with gzip.open(work / f"sample_outcomes_{stat}.jsonl.gz", "wt", encoding="utf-8") as z:
                    for r in rows:
                        if int(r["game_id"]) in first_games:
                            z.write(json.dumps(to_outcome(r), sort_keys=True) + "\n")
            v = subprocess.run([sys.executable, "-I", str(GATE), "validate", "--forecasts", str(f), "--require-v1"], capture_output=True, text=True)
            out["validate"][f"{arm}:{stat}"] = {"exit": v.returncode, "tail": v.stdout[-600:] + v.stderr[-300:]}
        for a, b in PAIRS:
            sc = work / f"scorecard_{b}_vs_{a}_{stat}.json"
            c = subprocess.run([sys.executable, "-I", str(GATE), "compare", "--champion", str(files[a]), "--challenger", str(files[b]),
                                "--outcomes", str(work / f"outcomes_{stat}.jsonl"), "--bootstrap", "1000", "--output", str(sc)], capture_output=True, text=True)
            out["compare"][f"{b}_vs_{a}:{stat}"] = {"exit": c.returncode, "scorecard": json.loads(sc.read_text()) if sc.exists() else None,
                                                    "stderr": c.stderr[-500:]}
        for f in list(files.values()) + [work / f"outcomes_{stat}.jsonl"]:
            f.unlink()  # full sidecars are regenerable and too large to keep; the samples stay
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.shot_volume_eval")
    ap.add_argument("--rows", required=True)
    ap.add_argument("--season", type=int, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--gate-work", default=None)
    a = ap.parse_args(argv)
    frames = load(Path(a.rows), a.season)
    res = {"season": a.season, "metrics": evaluate(frames)}
    meta = json.loads((Path(a.rows) / f"run_meta_{a.season}.json").read_text())
    res["run_meta"] = meta
    if a.gate_work:
        from nhl_edge.research.shot_volume_v1 import frozen_hash, model_files

        src = Path(__file__).resolve().parents[1]
        inc = [f for f in model_files() if f.name != "shot_volume_v1.py"] + [src / "research" / "player_walk_forward.py"]
        base = [src / "research" / "shot_volume_v1.py", src / "research" / "opportunity_efficiency.py"]
        hashes = {MODEL_VERSION: meta.get("model_frozen_hash") or frozen_hash(model_files()), INCUMBENT_VERSION: frozen_hash(inc), BASELINE_VERSION: frozen_hash(base)}
        res["model_frozen_hashes"] = hashes
        res["pure_gate"] = run_gate(frames, hashes, Path(a.gate_work))
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / f"shot_volume_eval_{a.season}.json").write_text(json.dumps(res, indent=1, default=float))
    return 0


if __name__ == "__main__":
    sys.exit(main())
