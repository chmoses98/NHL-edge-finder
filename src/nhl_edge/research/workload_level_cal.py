"""WORKLOAD_V1_LC: WORKLOAD_V1's skater shot mean times a rolling level factor from strictly earlier games (RESEARCH_ONLY; offline).

Registered in ``docs/research/workload_v1/LEVEL_CALIBRATION_PREREGISTRATION.md`` before it was run. Constants are fixed, not tuned:
``H_DAYS`` (memory) and ``K_SHOTS`` (prior weight). Everything else is WORKLOAD_V1 as frozen; the NegBin dispersion is re-fitted on the previous
season's residuals of the corrected means.

``python -m nhl_edge.research.workload_level_cal --seasons 2023,2024,2025 --out docs/research/workload_v1``
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.research import workload_eval as E
from nhl_edge.research import workload_experiment as X
from nhl_edge.research import workload_replication as R
from nhl_edge.research import workload_v1 as W

H_DAYS = 60.0
K_SHOTS = 1000.0
COVERAGE_BAND = (0.77, 0.83)
BIAS_LIMIT = 0.02
CRPS_GIVEBACK_LIMIT = 0.0010


def level_factors(day: np.ndarray, y: np.ndarray, yhat: np.ndarray, half_life: float = H_DAYS, k: float = K_SHOTS) -> np.ndarray:
    """Factor applied to each row: (decayed sum of y + k) / (decayed sum of yhat + k) over rows on STRICTLY earlier days.

    ``day`` is an integer day number; rows need not be sorted. Rows of one day share a factor and never inform each other.
    """
    order = np.argsort(day, kind="stable")
    f = np.ones(len(day))
    sy = sp = 0.0
    last: int | None = None
    i = 0
    d_sorted = day[order]
    while i < len(order):
        d = int(d_sorted[i])
        j = i
        while j < len(order) and int(d_sorted[j]) == d:
            j += 1
        if last is not None:
            decay = 0.5 ** ((d - last) / half_life)
            sy, sp = sy * decay, sp * decay
        idx = order[i:j]
        f[idx] = (sy + k) / (sp + k)
        sy += float(y[idx].sum())
        sp += float(yhat[idx].sum())
        last = d
        i = j
    return f


def _days(date_int: pd.Series) -> np.ndarray:
    return (pd.to_datetime(date_int.astype(int).astype(str), format="%Y%m%d") - pd.Timestamp("2000-01-01")).dt.days.to_numpy()


def make_hook(stash: dict[int, pd.DataFrame]):
    """Replace ``wl_sog`` by the level-calibrated mean in the evaluated and the previous season (calibration runs across both, in date order)."""
    def hook(frames: dict[int, pd.DataFrame], season: int) -> dict[int, pd.DataFrame]:
        prev, cur = frames[season - 1].copy(), frames[season].copy()
        both = pd.concat([prev.assign(_s=0), cur.assign(_s=1)], ignore_index=True)
        f = level_factors(_days(both["date_int"]), both["y_sog"].to_numpy(float), both["wl_sog"].to_numpy(float))
        stash[season] = frames[season - 1].copy()                       # uncorrected previous season, for the uncorrected arm's dispersion
        prev["wl_sog_raw"], cur["wl_sog_raw"] = prev["wl_sog"], cur["wl_sog"]
        cur["level_factor"] = f[both["_s"].to_numpy() == 1]
        prev["wl_sog"] = prev["wl_sog"].to_numpy() * f[both["_s"].to_numpy() == 0]
        cur["wl_sog"] = cur["wl_sog"].to_numpy() * cur["level_factor"].to_numpy()
        return {season - 1: prev, season: cur}
    return hook


def run_season(ctx: Any, season: int, pre: dict[str, Any], n_boot: int) -> dict[str, Any]:
    prm = W.WorkloadParams.from_dict(pre["frozen_params"])
    stash: dict[int, pd.DataFrame] = {}
    m, pmfs, al = X.skater_arms(ctx, season, prm, frames_hook=make_hook(stash))
    rs = X.skater_report(m, pmfs, n_boot)                                # arm "WORKLOAD_V1" here IS the level-calibrated challenger
    rs["acceptance_original_rule"] = X.accept_skaters(rs, pre["acceptance"])
    prev = stash[season]
    alpha_raw = E.fit_nb_alpha(prev["y_sog"].to_numpy(), prev["wl_sog"].to_numpy())
    raw = E.score_arm(E.nb_pmf(m["wl_sog_raw"].to_numpy(), alpha_raw, W.SOG_K), m["y_sog"].to_numpy(), X.SOG_LADDER)
    lc = E.score_arm(pmfs["WORKLOAD_V1"], m["y_sog"].to_numpy(), X.SOG_LADDER)
    gid = m["game_id"].to_numpy()
    rs["uncorrected_workload_v1"] = E.summarize(raw)
    rs["lc_minus_uncorrected"] = E.bootstrap_diff(gid, lc, raw, n_boot)
    rs["level_factor"] = {"mean": float(m["level_factor"].mean()), "min": float(m["level_factor"].min()), "max": float(m["level_factor"].max()),
                          "first_week_mean": float(m.loc[m["date_int"] <= m["date_int"].min() + 7, "level_factor"].mean())}
    a = rs["arms"]["WORKLOAD_V1"]
    d_ch = rs["diffs"]["WORKLOAD_V1_minus_CHAMPION"]["crps"]["ci95"]
    giveback = rs["lc_minus_uncorrected"]["crps"]["ci95"][1]
    sub = rs["subgroups"]
    rs["development_checks"] = {
        "abs_bias_le_0.02": abs(a["bias"]) <= BIAS_LIMIT,
        "crps_vs_champion_ci_upper_lt_0": d_ch[1] < 0,
        "crps_vs_uncorrected_upper_le_0.001": giveback <= CRPS_GIVEBACK_LIMIT,
        "coverage80_in_band": COVERAGE_BAND[0] <= a["coverage80"] <= COVERAGE_BAND[1],
        "no_position_worse_crps_than_champion_nb": all(sub[p]["WORKLOAD_V1"]["crps"] <= sub[p]["CHAMPION_NB"]["crps"] for p in ("F", "D")),
    }
    # descriptive subgroup biases of the corrected mean
    y = m["y_sog"].to_numpy(float)
    e = m["wl_sog"].to_numpy(float) - y
    rs["subgroup_bias"] = {"F": float(e[(m["pos"] == "F").to_numpy()].mean()), "D": float(e[(m["pos"] == "D").to_numpy()].mean()),
                           "home": float(e[m["is_home"].astype(bool).to_numpy()].mean()), "away": float(e[~m["is_home"].astype(bool).to_numpy()].mean()),
                           "ot_games": float(e[m["game_ot"].astype(bool).to_numpy()].mean()), "regulation_games": float(e[~m["game_ot"].astype(bool).to_numpy()].mean())}
    return rs


def verdict(per_season: dict[str, Any]) -> dict[str, Any]:
    ok = {s: all(r["development_checks"].values()) for s, r in per_season.items()}
    return {"per_season": ok, "DEVELOPMENT_QUALIFIED": bool(ok and all(ok.values())),
            "original_rule_per_season": {s: r["acceptance_original_rule"]["verdict"] for s, r in per_season.items()}}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.workload_level_cal")
    ap.add_argument("--seasons", default="2023,2024,2025")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--cache", default="out/workload_v1_replication_cache")
    ap.add_argument("--out", default="docs/research/workload_v1")
    ap.add_argument("--prereg", default="docs/research/workload_v1/preregistration.json")
    ap.add_argument("--n-boot", type=int, default=2000)
    a = ap.parse_args(argv)
    seasons = [int(s) for s in a.seasons.split(",")]
    pre = json.loads(Path(a.prereg).read_text())
    history = Path(a.history)
    t0 = time.time()
    derived = R.derive_wf(history, [2022, 2023, 2024, 2025])
    ctx = R.ReplicationCtx(history, Path(a.cache) / "derived", "derived", derived)
    per = {}
    for s in seasons:
        per[str(s)] = run_season(ctx, s, pre, a.n_boot)
        print(s, json.dumps(per[str(s)]["development_checks"]), f"bias={per[str(s)]['arms']['WORKLOAD_V1']['bias']:+.4f}", f"{time.time() - t0:.0f}s", flush=True)
    res = {"model": "WORKLOAD_V1_LC", "H_days": H_DAYS, "K_shots": K_SHOTS, "preregistration": "LEVEL_CALIBRATION_PREREGISTRATION.md", "verdict": verdict(per), "seasons": per}
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / f"level_calibration_{'_'.join(map(str, seasons))}.json").write_text(json.dumps(X._round(res), indent=1))
    print(json.dumps(res["verdict"], indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
