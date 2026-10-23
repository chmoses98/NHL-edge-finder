"""Re-test the documented V1 weaknesses on the full walk-forward sample (RESEARCH_ONLY; reads ``oa_walk_forward`` output).

For each season group: overtime rate predicted vs realised (+ game-level bootstrap CI of the gap), tail mass of |margin| >= 3 and total >= 8,
the dispersion of the total-goal forecast (mean squared standardised error z^2, 1.0 == calibrated width), and total-goal RPS of V1 vs the
league-average model (does V1 differentiate totals at all?). Official finals credit an OT/SO winner with the extra goal, the same convention as the simulator.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

GROUPS = {"2018-2023 (unexposed)": (2018, 2019, 2020, 2021, 2022, 2023), "2024-2025 (exposed)": (2024, 2025)}


def _boot(x: np.ndarray, n: int = 3000, seed: int = 0) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    m = x[rng.integers(0, len(x), size=(n, len(x)))].mean(axis=1)
    return float(np.quantile(m, 0.025)), float(np.quantile(m, 0.975))


def diagnose(games_csv: Path, pmf_npz: Path, arm: str = "V1") -> dict[str, Any]:
    df = pd.read_csv(games_csv)
    pm = dict(np.load(pmf_npz, allow_pickle=False))
    arms = [str(a) for a in pm["arms"]]
    k, kl = arms.index(arm), arms.index("LEAGUE")
    tot, mar = pm["total"][:, k, :], pm["margin"][:, k, :]
    ks = np.arange(tot.shape[1])
    mean_t = (tot * ks).sum(axis=1)
    sd_t = np.sqrt((tot * (ks[None, :] - mean_t[:, None]) ** 2).sum(axis=1))
    y_t = df["y_total"].to_numpy(float)
    y_m = (df["home_score"] - df["away_score"]).to_numpy(int)
    mk = np.arange(-10, 11)
    out: dict[str, Any] = {}
    for name, seasons in GROUPS.items():
        m = df["season"].isin(seasons).to_numpy()
        n = int(m.sum())
        ot_gap = df.loc[m, f"{arm}_p_overtime"].to_numpy() - df.loc[m, "y_overtime"].to_numpy()
        lo, hi = _boot(ot_gap)
        p_big = mar[m][:, np.abs(mk) >= 3].sum(axis=1)
        obs_big = (np.abs(y_m[m]) >= 3).astype(float)
        gap_big = p_big - obs_big
        p8 = tot[m][:, ks >= 8].sum(axis=1)
        z2 = ((y_t[m] - mean_t[m]) / sd_t[m]) ** 2
        out[name] = {
            "n": n,
            "overtime": {"predicted": float(df.loc[m, f"{arm}_p_overtime"].mean()), "realised": float(df.loc[m, "y_overtime"].mean()), "gap_pred_minus_real": float(ot_gap.mean()), "ci95": [lo, hi]},
            "margin_abs_ge_3": {"predicted": float(p_big.mean()), "realised": float(obs_big.mean()), "gap": float(gap_big.mean()), "ci95": list(_boot(gap_big))},
            "total_ge_8": {"predicted": float(p8.mean()), "realised": float((y_t[m] >= 8).mean())},
            "total_z2": float(z2.mean()), "total_z2_ci95": list(_boot(z2)),
            "mean_total": {"predicted": float(mean_t[m].mean()), "realised": float(y_t[m].mean())},
            "sd_of_predicted_total_across_games": float(mean_t[m].std()),
            "home_win_rate": {"predicted": float(df.loc[m, f"{arm}_p_home_win"].mean()), "realised": float(df.loc[m, "y_home_win"].mean())},
        }
        cdf_v, cdf_l = np.cumsum(tot[m], axis=1), np.cumsum(pm["total"][m][:, kl, :], axis=1)
        ind = (y_t[m][:, None] <= ks[None, :]).astype(float)
        d = ((cdf_v - ind) ** 2).sum(axis=1) - ((cdf_l - ind) ** 2).sum(axis=1)
        out[name]["total_rps_v1_minus_league"] = {"delta": float(d.mean()), "ci95": list(_boot(d))}
    return out


def main(argv: list[str] | None = None) -> int:
    d = Path(argv[0] if argv else sys.argv[1])
    res = diagnose(d / "oa_games.csv", d / "oa_pmfs.npz")
    (d / "v1_diagnostics.json").write_text(json.dumps(res, indent=1))
    print(json.dumps(res, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
