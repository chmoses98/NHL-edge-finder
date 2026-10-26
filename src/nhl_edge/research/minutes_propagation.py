"""How ice time propagates through the production player model, and what correcting it is worth (RESEARCH_ONLY, development evidence, leakage-safe walk-forward).

Trace (code, ``players/roster.py`` + ``workflows/shadow_player.py``): expected ice time by strength state = the player's recency-weighted share of his team's seconds in that state
(6-game half-life, 0.5 pseudo-games of shrinkage) times FIXED team minutes per state (EV 50.6, PP 4.4 x p_pp/0.215, SH 4.4, EA 0.6, EN 0.6, OT 1.2). Expected shots = sum over EV/PP/SH of
those state minutes x the player's shots-per-60 in the state. Goals and assists use the SHARES (and rates), not absolute minutes, so team-minute constants do not move them.

This module measures, on the champion's own per-state frames (2023-2025, each season scored with factors fitted on earlier seasons only):
  * league-average team minutes by state vs the constants;
  * the champion's per-state minutes bias and its effect on total ice time, power-play time and shots;
  * arms: CH (as is), CH_STATECAL (each state's minutes x a factor fitted on earlier seasons), CH_x_USAGE (frozen last-3 usage term on top of CH_STATECAL), WL (WORKLOAD_V1 minutes with the
    champion's shot rates) and WL_x_USAGE -- all scored on the same rows with game-clustered paired intervals against CH.

Seasons 2022-2025 are exposed development seasons: this selects a specification, validates nothing. The production model is not touched.

    python -m nhl_edge.research.minutes_propagation --cache <derived cache> --history data/history --out out/minutes_propagation.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.research import player_diagnosis as PD

PROD_TEAM_MINUTES = {"ev": 50.6, "pp": 4.4, "sh": 4.4, "ea": 0.6, "en": 0.6, "ot": 1.2}        # shadow_player.py (pp scales with p_pp / 0.215; 4.4 at the league mean)
STATES = ("ev", "pp", "sh", "ea", "en", "ot")
USAGE_B = 0.23                                                                                    # frozen minutes-v1 coefficient (data/params/minutes-v1.json)


def team_minutes_actual(history: Path, seasons: tuple[int, ...] = (2023, 2024, 2025)) -> dict[str, Any]:
    from nhl_edge.research import workload_shadow as S

    ts = S.load_tables(history, None)["team_states"]
    ts = ts[(ts["game_type"] == 2) & ts["season"].isin(seasons)]
    per = {c.replace("sec_", ""): float(ts[c].mean() / 60.0) for c in ("sec_ev", "sec_pp", "sec_sh", "sec_ea", "sec_en")}
    return {"n_team_games": int(len(ts)), "league_mean_team_minutes": per, "total_team_minutes": float(ts["n_seconds"].mean() / 60.0), "production_constants": PROD_TEAM_MINUTES,
            "production_total_minutes": float(sum(PROD_TEAM_MINUTES.values()))}


def fit_state_factors(train: pd.DataFrame, pred_prefix: str = "ch_toi_", act_prefix: str = "y_toi_") -> dict[str, float]:
    """Per-state multiplicative factor = sum(actual) / sum(predicted) over the training rows (rows with valid shift data)."""
    ok = train["shifts_ok"].astype(bool)
    out = {}
    for s in STATES:
        p, a = train.loc[ok, f"{pred_prefix}{s}"].sum(), train.loc[ok, f"{act_prefix}{s}"].sum()
        out[s] = float(a / p) if p > 0 else 1.0
    return out


def shots_from_states(d: pd.DataFrame, toi: dict[str, np.ndarray]) -> np.ndarray:
    """The champion's expected shots from state minutes: sum over EV/PP/SH of minutes x shots-per-60 (exactly the production identity, checked in tests)."""
    return (toi["ev"] * d["ch_rate_ev"].to_numpy(float) + toi["pp"] * d["ch_rate_pp"].to_numpy(float) + toi["sh"] * d["ch_rate_sh"].to_numpy(float)) / 60.0


def poisson_dev(y: np.ndarray, mu: np.ndarray) -> np.ndarray:
    mu = np.clip(mu, 1e-9, None)
    return 2.0 * (np.where(y > 0, y * np.log(np.where(y > 0, y, 1.0) / mu), 0.0) - (y - mu))


def arm_table(d: pd.DataFrame, usage: np.ndarray | None = None) -> dict[str, dict[str, np.ndarray]]:
    """Per arm: total TOI, PP TOI, expected shots for the rows of ``d`` (which already carries fitted factors in k_<state> columns)."""
    arms: dict[str, dict[str, np.ndarray]] = {}
    ch = {s: d[f"ch_toi_{s}"].to_numpy(float) for s in STATES}
    cal = {s: ch[s] * d[f"k_{s}"].to_numpy(float) for s in STATES}
    arms["CH"] = {"toi": sum(ch.values()), "pp": ch["pp"], "sog": shots_from_states(d, ch)}
    arms["CH_STATECAL"] = {"toi": sum(cal.values()), "pp": cal["pp"], "sog": shots_from_states(d, cal)}
    if usage is not None:
        u = usage
        arms["CH_STATECAL_x_USAGE"] = {"toi": arms["CH_STATECAL"]["toi"] * u, "pp": cal["pp"] * u, "sog": shots_from_states(d, {s: cal[s] * u for s in STATES})}
    if "wl_toi" in d.columns:
        wl = {s: d[f"wl_toi_{s}"].to_numpy(float) for s in ("evreg", "pp", "sh", "ea", "en", "ot")}
        wls = {"ev": wl["evreg"] + wl["ot"], "pp": wl["pp"], "sh": wl["sh"], "ea": wl["ea"], "en": wl["en"], "ot": wl["ot"] * 0}
        arms["WL"] = {"toi": d["wl_toi"].to_numpy(float), "pp": wl["pp"], "sog": shots_from_states(d, wls)}
        if usage is not None:
            arms["WL_x_USAGE"] = {"toi": d["wl_toi"].to_numpy(float) * usage, "pp": wl["pp"], "sog": shots_from_states(d, {s: wls[s] * usage for s in STATES})}
    return arms


def usage_multiplier(d: pd.DataFrame, base_toi: np.ndarray, b: float = USAGE_B) -> np.ndarray:
    """exp(b * log((last3 + 1) / (base + 1))) with last3 = mean ice time of the previous three games (strictly earlier), 1.0 where fewer than three are known; clipped to [e^-1, e^1]."""
    x = np.log((d["last3_toi"].to_numpy(float) + 1.0) / (base_toi + 1.0))
    return np.exp(np.clip(np.where(np.isfinite(x), b * x, 0.0), -1.0, 1.0))


def score(d: pd.DataFrame, arms: dict[str, dict[str, np.ndarray]], n_boot: int) -> dict[str, Any]:
    game = d["game_id"].to_numpy()
    y_toi, y_pp, y_sog = d["y_toi"].to_numpy(float), d["y_toi_pp"].to_numpy(float), d["y_sog"].to_numpy(float)
    okpp = d["shifts_ok"].astype(bool).to_numpy()
    out: dict[str, Any] = {}
    base = {"toi": (arms["CH"]["toi"] - y_toi) ** 2, "pp": ((arms["CH"]["pp"] - y_pp) ** 2)[okpp], "sog_dev": poisson_dev(y_sog, arms["CH"]["sog"]), "sog_se": (arms["CH"]["sog"] - y_sog) ** 2}
    for name, a in arms.items():
        rows = {"toi": (a["toi"] - y_toi) ** 2, "pp": ((a["pp"] - y_pp) ** 2)[okpp], "sog_dev": poisson_dev(y_sog, a["sog"]), "sog_se": (a["sog"] - y_sog) ** 2}
        rec: dict[str, Any] = {"bias": {"toi": float((a["toi"] - y_toi).mean()), "pp": float((a["pp"] - y_pp)[okpp].mean()), "sog": float((a["sog"] - y_sog).mean())},
                               "loss": {k: float(v.mean()) for k, v in rows.items()}}
        if name != "CH":
            rec["vs_CH"] = {k: PD.paired_game_ci(rows[k] - base[k], game[okpp] if k == "pp" else game, n_boot=n_boot) for k in rows}
        out[name] = rec
    return out


def run(cache: Path, history: Path, n_boot: int = PD.N_BOOT) -> dict[str, Any]:
    champ = PD.load_champion(cache).reset_index(drop=True)
    g = champ.sort_values(["player_id", "date_int", "game_id"]).groupby("player_id", sort=False)["y_toi"]
    champ["last3_toi"] = g.transform(lambda x: x.shift(1).rolling(3, min_periods=3).mean())
    res: dict[str, Any] = {"evidence": "development (exposed seasons 2022-2025): selects a specification, validates nothing", "team_minutes": team_minutes_actual(history), "by_season": {}}
    parts = []
    for s in (2023, 2024, 2025):
        k = fit_state_factors(champ[champ["season"] < s])
        te = champ[champ["season"] == s].copy()
        for st in STATES:
            te[f"k_{st}"] = k[st]
        te["_factors"] = [k] * len(te)
        parts.append(te)
        res["by_season"][str(s)] = {"factors_fitted_on_earlier_seasons": k}
    d = pd.concat(parts, ignore_index=True)
    base_cal = sum(d[f"ch_toi_{s}"].to_numpy(float) * d[f"k_{s}"].to_numpy(float) for s in STATES)
    arms = arm_table(d, usage_multiplier(d, base_cal))
    res["champion_rows"] = {"n": int(len(d)), "arms": score(d, {k: v for k, v in arms.items() if not k.startswith("WL")}, n_boot)}
    full = _wl_state_frames(history, cache)
    m = d[d["season"].isin([2023, 2024, 2025])].merge(full, on=["game_id", "player_id"], how="inner", suffixes=("", "_w"))
    base_cal2 = sum(m[f"ch_toi_{s}"].to_numpy(float) * m[f"k_{s}"].to_numpy(float) for s in STATES)
    arms2 = arm_table(m, usage_multiplier(m, base_cal2))
    res["common_rows_with_workload"] = {"n": int(len(m)), "arms": score(m, arms2, n_boot)}
    return res


def _wl_state_frames(history: Path, cache: Path) -> pd.DataFrame:
    from nhl_edge.research import workload_experiment as X
    from nhl_edge.research import workload_level_cal as LC
    from nhl_edge.research import workload_replication as R
    from nhl_edge.research import workload_v1 as W

    pre = json.loads(Path("docs/research/workload_v1/preregistration.json").read_text())
    prm = W.WorkloadParams.from_dict(pre["frozen_params"])
    ctx = R.ReplicationCtx(history, cache, "derived", R.derive_wf(history, [2022, 2023, 2024, 2025]))
    keep = ["game_id", "player_id", "wl_toi", "wl_toi_evreg", "wl_toi_pp", "wl_toi_sh", "wl_toi_ea", "wl_toi_en", "wl_toi_ot"]
    fr = []
    for s in (2023, 2024, 2025):
        m, _, _ = X.skater_arms(ctx, s, prm, frames_hook=LC.make_hook({}))
        fr.append(m[keep])
    return pd.concat(fr, ignore_index=True)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.minutes_propagation")
    ap.add_argument("--cache", default="out/workload_v1_replication_cache/derived")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    Path(a.out).write_text(json.dumps(run(Path(a.cache), Path(a.history)), indent=1, default=float))
    print(f"wrote {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
