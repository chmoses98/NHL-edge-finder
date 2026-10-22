"""M-SCRIPT-1: calibration of the NHL_SCRIPT_V1 seven-way game-script probabilities (LIVE tier, descriptive).

Script labels are mutually exclusive and sum to 1 by construction (first matching rule in a fixed precedence; BACK_AND_FORTH is the catch-all).
Question: are the script probabilities better than the historical base rates, and calibrated per script?
    python -m nhl_edge.model_research.exp_scripts --archive ../rdata/data-archive --repo . --out docs/research/nhl-model-improvement/data
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.market_audit.games import read_kind
from nhl_edge.model_research import registry
from nhl_edge.model_research import scoring as S
from nhl_edge.model_research.live_dataset import dev_games

SCRIPTS = ["SPECIAL_TEAMS", "OPEN_GAME", "TIGHT_LOW_EVENT", "GOALIE_DRIVEN", "HOME_CONTROL", "AWAY_CONTROL", "BACK_AND_FORTH"]


def last_before_cut(pm: pd.DataFrame, games: pd.DataFrame, cut_minutes: float = 60.0) -> pd.DataFrame:
    pm = pm.copy()
    pm["decided"] = pd.to_datetime(pm["decided_at_utc"], utc=True)
    g = games.set_index("game_id")
    pm["cut"] = pm["game_id"].map(lambda x: g["start_time_utc"].get(x) - pd.Timedelta(minutes=cut_minutes) if x in g.index else pd.NaT)
    pm = pm[pm["cut"].notna() & (pm["decided"] <= pm["cut"])]
    return pm.sort_values("decided").groupby("game_id").tail(1).reset_index(drop=True)


def run(archive: Path, base_rates_path: Path) -> dict[str, Any]:
    games = dev_games(archive)
    pm = read_kind(archive, "script_postmortems")
    pm["game_id"] = pm["game_id"].astype(str)
    pm = last_before_cut(pm[pm["game_id"].isin(games["game_id"])], games)
    base = json.loads(base_rates_path.read_text())
    br = {k: float(v) for k, v in base["frequency"].items() if k in SCRIPTS}  # 2022-23..2025-26 finals, all before the LIVE tier
    tot = sum(br.values())
    br = {k: v / tot for k, v in br.items()}
    P = np.array([[r["predicted"].get(s, 0.0) for s in SCRIPTS] for r in pm.to_dict("records")])
    Y = np.array([[1.0 if r["realized_script"] == s else 0.0 for s in SCRIPTS] for r in pm.to_dict("records")])
    B = np.tile([br[s] for s in SCRIPTS], (len(pm), 1))
    brier = ((P - Y) ** 2).sum(axis=1)
    brier_b = ((B - Y) ** 2).sum(axis=1)
    ll = -np.log(np.maximum((P * Y).sum(axis=1), 1e-6))
    ll_b = -np.log(np.maximum((B * Y).sum(axis=1), 1e-6))
    out: dict[str, Any] = {"n_games": int(len(pm)), "sum_to_one_max_error": float(np.abs(P.sum(axis=1) - 1).max()),
                           "brier_model": float(brier.mean()), "brier_base_rate": float(brier_b.mean()), "paired_brier_model_minus_base": S.paired_delta(brier, brier_b),
                           "logloss_model": float(ll.mean()), "logloss_base_rate": float(ll_b.mean()), "paired_logloss_model_minus_base": S.paired_delta(ll, ll_b),
                           "per_script": {}, "top_script_hit_rate": float((P.argmax(axis=1) == Y.argmax(axis=1)).mean()),
                           "top_script_hit_rate_if_always_base_rate_mode": float((B.argmax(axis=1) == Y.argmax(axis=1)).mean())}
    for j, s in enumerate(SCRIPTS):
        k = int(Y[:, j].sum())
        n = len(pm)
        from nhl_edge.model_research.dist_eval import wilson
        lo, hi = wilson(k, n)
        out["per_script"][s] = {"mean_predicted": float(P[:, j].mean()), "observed_rate": k / n, "obs_lo95": lo, "obs_hi95": hi, "base_rate": br[s],
                                "paired_brier_vs_base": S.paired_delta((P[:, j] - Y[:, j]) ** 2, (B[:, j] - Y[:, j]) ** 2),
                                "calibration_in_ci": bool(lo <= P[:, j].mean() <= hi)}
    out["realized_counts"] = {s: int(Y[:, j].sum()) for j, s in enumerate(SCRIPTS)}
    return out


def record(res: dict[str, Any], repo: Path, reg: Path) -> None:
    ents = registry.read(reg)
    if not any(e["id"] == "M-SCRIPT-1" for e in ents):
        registry.append(reg, "PREREG", "M-SCRIPT-1", {
            "hypothesis": "The seven-way script probabilities carry calibrated, better-than-base-rate information about the realised game script.",
            "motivation": "Script layer is central to SIFT's explanation UX; its quantitative claims must be earned.",
            "method": "Last NHL_SCRIPT_V1 forecast at or before T-60 per LIVE game vs the realised script from the archived postmortem; multiclass Brier and log loss vs historical base rates, "
                      "per-script reliability with Wilson intervals; paired game bootstrap.",
            "baseline": "scripts_v1/base_rates.json (5,248 finals)", "decision_rule": "USEFUL if paired Brier delta CI < 0; CALIBRATED_SCRIPT if mean predicted lies inside the Wilson 95% interval; descriptive, n=151.",
            "tier": "LIVE_DESCRIPTIVE", "disclosure": "registered after the first execution of this script (code written before executing; not edited after)."}, repo)
    if not any(e["id"] == "M-SCRIPT-1" and e["type"] == "RESULT" for e in registry.read(reg)):
        d = res["paired_brier_model_minus_base"]
        registry.append(reg, "RESULT", "M-SCRIPT-1", {"metrics": {k: res[k] for k in ("n_games", "brier_model", "brier_base_rate", "paired_brier_model_minus_base", "logloss_model", "logloss_base_rate",
                                                                                      "paired_logloss_model_minus_base", "top_script_hit_rate", "per_script")},
                                                      "decision": "USEFUL" if d["hi95"] < 0 else ("WORSE_THAN_BASE_RATE" if d["lo95"] > 0 else "NOT_DISTINGUISHABLE_FROM_BASE_RATE"),
                                                      "interpretation": "see docs/research/nhl-model-improvement/SCRIPT_CALIBRATION.md",
                                                      "reproduction": "python -m nhl_edge.model_research.exp_scripts --archive <data-archive> --repo . --out docs/research/nhl-model-improvement/data",
                                                      "results_file": "docs/research/nhl-model-improvement/data/script_calibration.json"}, repo)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", type=Path, required=True)
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    r = run(a.archive, a.repo / "src/nhl_edge/scripts_v1/base_rates.json")
    a.out.mkdir(parents=True, exist_ok=True)
    (a.out / "script_calibration.json").write_text(json.dumps(r, indent=1, default=float))
    record(r, a.repo, a.repo / "docs/research/nhl-model-improvement/experiment_registry.jsonl")
    print(json.dumps({k: r[k] for k in ("n_games", "sum_to_one_max_error", "brier_model", "brier_base_rate", "paired_brier_model_minus_base", "top_script_hit_rate")}, indent=1))
    for s, v in r["per_script"].items():
        print(s, round(v["mean_predicted"], 3), round(v["observed_rate"], 3), [round(v["obs_lo95"], 3), round(v["obs_hi95"], 3)], v["calibration_in_ci"], round(v["paired_brier_vs_base"]["delta"], 4))
