"""Team-minute recalibration for the PLAYER_SIM_V1 ice-time projection (RESEARCH_ONLY; development evidence on the exposed seasons 2022-2025).

Question: the hard-coded team-minute template of ``workflows/shadow_player.py`` (EV 50.6, PP 4.4 x p_pp/0.215, SH 4.4, EA 0.6, EN 0.6, OT 1.2) maps a player's share of his
team's time in a strength state to minutes. ``players/team_minutes.py`` replaces it with a physically consistent clock budget (see that module). This module

  * measures the clock budget from the history (regulation games only: the recorded team-state seconds of an overtime game are padded to a 20-minute overtime grid);
  * verifies the cross-team identities the allocation relies on (PP_A == SH_B, EA_A == EN_B, states partition the 60 minutes);
  * fits the allocation parameters on training seasons only and scores it walk-forward (each test season with parameters fitted on EARLIER seasons) on the champion's own
    per-skater frames, as a ladder of arms so each change is isolated:
        L0 incumbent                            the template as published
        L1 level refit                          same functional form, each state's constant refitted (OT still additive)
        L2 + overtime memo                      OT no longer added on top of EV/PP/SH (it is already inside them)
        L3 + clock budget (no matchup)          league-mean PP == SH, EV from the partition, kappa normalisation
        L4 candidate (team-minutes-1.0)         PP/SH from the matchup's V2 ppmin, EV from the partition
  * checks goals / assists / points are untouched (they never read minutes) in ``tests/test_team_minutes.py``, not here.

Shares, shot rates and the simulation are not re-estimated: the only thing that changes between arms is the team-minute dictionary.

    python -m nhl_edge.research.team_minutes_recal --cache <derived cache> --history data/history --wf <derived wf parquet> --out out/team_minutes_recal.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.players import team_minutes as TM
from nhl_edge.research import player_diagnosis as PD
from nhl_edge.research.minutes_propagation import poisson_dev, shots_from_states

STATES5 = ("ev", "pp", "sh", "ea", "en")
TEST_SEASONS = (2023, 2024, 2025)
ALL_SEASONS = (2022, 2023, 2024, 2025)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# clock budget (team-level, from the recorded team-state seconds)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def team_clock_table(history: Path) -> tuple[pd.DataFrame, dict[str, Any]]:
    """(regulation-only team-game clock seconds by state, expected overtime clock). Overtime games are excluded from the state means because their recorded state seconds are
    padded to a 20-minute overtime grid (the last state is held to the end of the grid), which is what inflated EN/EA/total in the first propagation trace."""
    from nhl_edge.research import workload_shadow as S

    t = S.load_tables(history, None)
    ts = t["team_states"]
    ts = ts[ts["game_type"] == 2].copy()
    reg = ts[ts["n_seconds"] == 3600].copy()
    goals = t["goals"]
    goals = goals[goals["game_type"] == 2] if "game_type" in goals.columns else goals
    ot_games = ts[ts["n_seconds"] > 3600].groupby(["season", "game_id"]).size().reset_index()[["season", "game_id"]]
    ot_goal_len = goals[goals["period"] == 4].groupby("game_id")["t_s"].max() - 3600
    ot_games["ot_len_s"] = ot_games["game_id"].map(ot_goal_len).fillna(300.0)               # no overtime goal => the 5:00 overtime ran out => shootout
    n_games = ts.groupby("season")["game_id"].nunique()
    ot = ot_games.groupby("season")["ot_len_s"].sum() / n_games / 60.0
    info = {"expected_ot_clock_min_by_season": {int(k): float(v) for k, v in ot.items()}, "n_games_by_season": {int(k): int(v) for k, v in n_games.items()},
            "p_ot_by_season": {int(k): float(v) for k, v in (ot_games.groupby("season").size() / n_games).items()},
            "padding_artifact": {
                "overtime_games_recorded_seconds": 4800, "regulation_games_recorded_seconds": 3600,
                "mean_recorded_minutes_by_state_regulation": {s: float(reg[f"sec_{s}"].mean() / 60.0) for s in STATES5},
                "mean_recorded_minutes_by_state_overtime_games": {s: float(ts[ts["n_seconds"] > 3600][f"sec_{s}"].mean() / 60.0) for s in STATES5}}}
    return reg, info


def identities(reg: pd.DataFrame) -> dict[str, Any]:
    """Cross-team identities on regulation games (both teams of the same game)."""
    h = reg[reg["is_home"].astype(bool)].set_index("game_id")
    a = reg[~reg["is_home"].astype(bool)].set_index("game_id")
    j = h.join(a, how="inner", lsuffix="_h", rsuffix="_a")  # noqa
    tot = sum(j[f"sec_{s}_h"] for s in STATES5)
    return {"n_games": int(len(j)), "pp_home_equals_sh_away": float((j["sec_pp_h"] == j["sec_sh_a"]).mean()), "pp_away_equals_sh_home": float((j["sec_pp_a"] == j["sec_sh_h"]).mean()),
            "ea_home_equals_en_away": float((j["sec_ea_h"] == j["sec_en_a"]).mean()), "ea_away_equals_en_home": float((j["sec_ea_a"] == j["sec_en_h"]).mean()),
            "states_sum_to_3600": float((tot == 3600).mean())}


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# frames
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def build_frame(cache: Path, wf: pd.DataFrame) -> pd.DataFrame:
    """Champion per-skater rows (shift charts present) with the matchup's V2 PP-minute expectations of the player's team and of the opponent."""
    c = PD.load_champion(cache).reset_index(drop=True)
    c = c[c["shifts_ok"].astype(bool)].copy()
    w = wf[["game_id", "ppmin_home", "ppmin_away"]].drop_duplicates("game_id")
    c = c.merge(w, on="game_id", how="left")
    home = c["is_home"].astype(bool)
    c["ppmin_for"] = np.where(home, c["ppmin_home"], c["ppmin_away"])
    c["ppmin_opp"] = np.where(home, c["ppmin_away"], c["ppmin_home"])
    return c[c["ppmin_for"].notna()].reset_index(drop=True)


def team_games(d: pd.DataFrame) -> pd.DataFrame:
    agg = {"season": ("season", "first"), "p_pp": ("p_pp", "first"), "ppmin_for": ("ppmin_for", "first"), "ppmin_opp": ("ppmin_opp", "first"), "n": ("player_id", "size"), "ot": ("game_ot", "first")}
    for s in STATES5:
        agg[f"sh_{s}"] = (f"ch_share_{s}", "sum")
        agg[f"y_{s}"] = (f"y_toi_{s}", "sum")
    return d.groupby(["game_id", "team_id"]).agg(**agg).reset_index()


def skater_budget(frame: pd.DataFrame, reg: pd.DataFrame) -> dict[str, Any]:
    """Clock minutes vs skater-minutes (regulation games with shift charts): skaters on the ice per clock minute by state, the total skater-minute budget of a team-game, and why the
    recorded shares need a normalisation factor (the dressed skaters' shares sum to LESS than the skaters on the ice where the recorded denominators are padded)."""
    tg = team_games(frame)
    m = tg.merge(reg[["game_id", "team_id"] + [f"sec_{s}" for s in STATES5]], on=["game_id", "team_id"], how="inner")
    out: dict[str, Any] = {"n_regulation_team_games": int(len(m)), "by_state": {}}
    for s in STATES5:
        clock_min = float(m[f"sec_{s}"].sum() / 60.0)
        out["by_state"][s] = {"clock_min_per_team_game": clock_min / len(m), "skater_min_per_team_game": float(m[f"y_{s}"].sum() / len(m)),
                              "skaters_on_ice": float(m[f"y_{s}"].sum() / clock_min), "mean_sum_of_dressed_shares_all_games": float(tg[f"sh_{s}"].mean()),
                              "mean_sum_of_dressed_shares_regulation_games": float(m[f"sh_{s}"].mean())}
    out["total_skater_min_per_team_game_regulation"] = float(sum(out["by_state"][s]["skater_min_per_team_game"] for s in STATES5))
    ot = tg[tg["ot"].astype(bool)]
    out["total_skater_min_per_team_game_overtime_games"] = float(sum(ot[f"y_{s}"].mean() for s in STATES5)) if len(ot) else None
    out["total_skater_min_per_team_game_all"] = float(sum(tg[f"y_{s}"].mean() for s in STATES5))
    return out


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# fitting
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def fit_params(train: pd.DataFrame, reg: pd.DataFrame, info: dict[str, Any], seasons: tuple[int, ...]) -> TM.AllocationParams:
    """``team-minutes-1.0`` parameters from the TRAINING seasons only."""
    tg = team_games(train[train["season"].isin(seasons)])
    r = reg[reg["season"].isin(seasons)].merge(tg[["game_id", "team_id", "ppmin_for"]], on=["game_id", "team_id"], how="inner")
    c_pp = float(r["sec_pp"].sum() / 60.0 / r["ppmin_for"].sum())
    league_pp = float(reg[reg["season"].isin(seasons)]["sec_pp"].mean() / 60.0)
    ea = float(reg[reg["season"].isin(seasons)][["sec_ea", "sec_en"]].stack().mean() / 60.0)
    ot_by = info["expected_ot_clock_min_by_season"]
    n_by = info["n_games_by_season"]
    ot = float(sum(ot_by[s] * n_by[s] for s in seasons) / sum(n_by[s] for s in seasons))
    base = TM.AllocationParams(TM.CANDIDATE_VERSION, 60.0, ot, c_pp, league_pp, ea, {s: 1.0 for s in STATES5})
    # kappa: observed skater-minutes by state over the share sums times the state's clock minutes (ratio estimator over the training team-games)
    clk = [TM.clock(a, b, base) for a, b in zip(tg["ppmin_for"], tg["ppmin_opp"])]
    kappa = {}
    for s in STATES5:
        exposure = float((tg[f"sh_{s}"].to_numpy() * np.array([x[s] for x in clk])).sum())
        kappa[s] = float(tg[f"y_{s}"].sum() / exposure) if exposure > 0 else 1.0
    prm = TM.AllocationParams(TM.CANDIDATE_VERSION, 60.0, ot, c_pp, league_pp, ea, kappa)
    return TM.AllocationParams(prm.version, prm.regulation_min, prm.ot_min, prm.pp_per_ppmin, prm.league_pp_min, prm.ea_min, prm.kappa,
                               {"train_seasons": list(seasons), "n_team_games": int(len(tg)), "n_skater_games": int(train["season"].isin(seasons).sum()),
                                "n_regulation_team_games_for_clock": int(len(r)), "source": "champion per-skater frames (shift charts) + regulation team-state seconds"})


def minutes_arms(d: pd.DataFrame, train: pd.DataFrame, reg: pd.DataFrame, info: dict[str, Any], train_seasons: tuple[int, ...]) -> tuple[dict[str, dict[str, np.ndarray]], TM.AllocationParams]:
    """Per arm and state: predicted minutes for the rows of ``d`` (the test season), everything fitted on ``train`` only."""
    prm = fit_params(train, reg, info, train_seasons)
    tg = team_games(train)
    ppf = (tg["p_pp"] / TM.LEGACY_LEAGUE_P_PP).to_numpy()
    ratio = lambda y, x: float(y / x) if x > 0 else 1.0  # noqa: E731
    # L1 / L2: constants refitted per state in the legacy functional form (PP scales with p_pp / 0.215)
    f1 = {"ev": np.ones(len(tg)), "pp": ppf, "sh": np.ones(len(tg)), "ea": np.ones(len(tg)), "en": np.ones(len(tg))}
    B1 = {s: ratio(tg[f"y_{s}"].sum(), (tg[f"sh_{s}"].to_numpy() * f1[s]).sum()) for s in STATES5}
    ot_share = train["ch_share_ot"].to_numpy(float)
    ot_exposure = float(ot_share.sum())
    B_ot = ratio(train["y_toi_ot"].sum(), ot_exposure)                                  # L1 only: OT additive (its minutes are ALSO inside ev/pp/sh in the data)
    out: dict[str, dict[str, np.ndarray]] = {}
    pf = (d["p_pp"].to_numpy(float) / TM.LEGACY_LEAGUE_P_PP)
    out["L0_incumbent"] = {s: d[f"ch_toi_{s}"].to_numpy(float) for s in (*STATES5, "ot")}
    out["L1_level_refit"] = {"ev": d["ch_share_ev"].to_numpy(float) * B1["ev"], "pp": d["ch_share_pp"].to_numpy(float) * B1["pp"] * pf, "sh": d["ch_share_sh"].to_numpy(float) * B1["sh"],
                             "ea": d["ch_share_ea"].to_numpy(float) * B1["ea"], "en": d["ch_share_en"].to_numpy(float) * B1["en"], "ot": d["ch_share_ot"].to_numpy(float) * B_ot}
    out["L2_ot_memo"] = {k: (v * 0.0 if k == "ot" else v) for k, v in out["L1_level_refit"].items()}
    # L2 refits EV without the OT term in play (the ratio estimator above never included OT in ev), so only the OT addition is removed
    league = TM.clock(None, None, prm)
    out["L3_clock_no_matchup"] = {s: d[f"ch_share_{s}"].to_numpy(float) * prm.kappa[s] * league[s] for s in STATES5} | {"ot": np.zeros(len(d))}
    cl = [TM.clock(a, b, prm) for a, b in zip(d["ppmin_for"].to_numpy(float), d["ppmin_opp"].to_numpy(float))]
    out["L4_candidate"] = {s: d[f"ch_share_{s}"].to_numpy(float) * prm.kappa[s] * np.array([x[s] for x in cl]) for s in STATES5} | {"ot": np.zeros(len(d))}
    return out, prm


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# scoring
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def targets(arm: dict[str, np.ndarray], d: pd.DataFrame) -> dict[str, np.ndarray]:
    toi = sum(arm[s] for s in (*STATES5, "ot"))
    sog = shots_from_states(d, {s: arm[s] for s in ("ev", "pp", "sh")})
    return {"toi": toi, "toi_ev": arm["ev"], "toi_pp": arm["pp"], "toi_sh": arm["sh"], "sog": sog}


def calibration(pred: np.ndarray, y: np.ndarray, bins: int = 10) -> dict[str, Any]:
    q = np.quantile(pred, np.linspace(0, 1, bins + 1))
    idx = np.clip(np.searchsorted(q, pred, side="right") - 1, 0, bins - 1)
    rows = [{"mean_pred": float(pred[idx == b].mean()), "mean_actual": float(y[idx == b].mean()), "n": int((idx == b).sum())} for b in range(bins) if (idx == b).any()]
    slope = float(np.polyfit(pred, y, 1)[0]) if pred.std() > 0 else float("nan")
    return {"slope_actual_on_pred": slope, "bins": rows, "max_abs_bin_bias": float(max(abs(r["mean_pred"] - r["mean_actual"]) for r in rows))}


def score_arms(d: pd.DataFrame, arms: dict[str, dict[str, np.ndarray]], n_boot: int) -> dict[str, Any]:
    game = d["game_id"].to_numpy()
    y = {"toi": d["y_toi"].to_numpy(float), "toi_ev": d["y_toi_ev"].to_numpy(float), "toi_pp": d["y_toi_pp"].to_numpy(float), "toi_sh": d["y_toi_sh"].to_numpy(float),
         "sog": d["y_sog"].to_numpy(float)}
    tg = {k: targets(a, d) for k, a in arms.items()}
    base = tg["L0_incumbent"]
    out: dict[str, Any] = {}
    for name, t in tg.items():
        rec: dict[str, Any] = {"bias": {k: float((t[k] - y[k]).mean()) for k in y}, "mean_pred": {k: float(t[k].mean()) for k in y}, "mean_actual": {k: float(y[k].mean()) for k in y},
                               "mse": {k: float(((t[k] - y[k]) ** 2).mean()) for k in y if k != "sog"}, "sog_poisson_deviance": float(poisson_dev(y["sog"], t["sog"]).mean()),
                               "calibration": {k: calibration(t[k], y[k]) for k in ("toi", "toi_pp", "sog")}}
        if name != "L0_incumbent":
            vs = {}
            for k in y:
                if k == "sog":
                    vs["sog_poisson_deviance"] = PD.paired_game_ci(poisson_dev(y[k], t[k]) - poisson_dev(y[k], base[k]), game, n_boot=n_boot)
                else:
                    vs[f"mse_{k}"] = PD.paired_game_ci((t[k] - y[k]) ** 2 - (base[k] - y[k]) ** 2, game, n_boot=n_boot)
            rec["vs_incumbent"] = vs
        out[name] = rec
    # team-level coherence: skater-minutes summed over the dressed skaters
    tm = d.assign(**{f"p_{k}": sum(a[s] for s in (*STATES5, "ot")) for k, a in arms.items()}).groupby(["game_id", "team_id"]).agg(
        y=("y_toi", "sum"), **{f"p_{k}": (f"p_{k}", "sum") for k in arms}).reset_index()
    out["_team_level_skater_minutes"] = {"n_team_games": int(len(tm)), "actual_mean": float(tm["y"].mean()),
                                         **{k: {"mean": float(tm[f"p_{k}"].mean()), "bias": float((tm[f"p_{k}"] - tm["y"]).mean()), "rmse": float(np.sqrt(((tm[f"p_{k}"] - tm["y"]) ** 2).mean())),
                                                "share_outside_270_330": float(((tm[f"p_{k}"] < 270) | (tm[f"p_{k}"] > 330)).mean())} for k in arms}}
    return out


def run(cache: Path, history: Path, wf: pd.DataFrame, n_boot: int = PD.N_BOOT) -> dict[str, Any]:
    reg, info = team_clock_table(history)
    frame = build_frame(cache, wf)
    res: dict[str, Any] = {"evidence": "development (exposed seasons 2022-2025): selects/fits a specification; the prospective shadow on current games is the validation",
                           "clock_budget": info, "identities": identities(reg), "skater_budget": skater_budget(frame, reg), "by_season": {},
                           "n_rows": int(len(frame))}
    pooled: dict[str, list[pd.DataFrame]] = {}
    for s in TEST_SEASONS:
        train_seasons = tuple(x for x in ALL_SEASONS if x < s)
        tr, te = frame[frame["season"].isin(train_seasons)], frame[frame["season"] == s].reset_index(drop=True)
        arms, prm = minutes_arms(te, tr, reg, info, train_seasons)
        res["by_season"][str(s)] = {"train_seasons": list(train_seasons), "n_rows": int(len(te)), "params": prm.to_dict(), "scores": score_arms(te, arms, n_boot)}
        for k, a in arms.items():
            pooled.setdefault(k, []).append(pd.DataFrame({f"{x}": v for x, v in a.items()}))
    arms_all = {k: {s: np.concatenate([p[s].to_numpy() for p in v]) for s in v[0].columns} for k, v in pooled.items()}
    # the concatenation above is in TEST_SEASONS order; make te_all follow it
    te_all = pd.concat([frame[frame["season"] == s].reset_index(drop=True) for s in TEST_SEASONS], ignore_index=True)
    res["pooled_2023_2025"] = {"n_rows": int(len(te_all)), "scores": score_arms(te_all, arms_all, n_boot)}
    final = fit_params(frame, reg, info, ALL_SEASONS)
    res["final_params_fit_on_2022_2025"] = final.to_dict()
    return res


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", type=Path, required=True)
    ap.add_argument("--history", type=Path, default=Path("data/history"))
    ap.add_argument("--wf", type=Path, required=True, help="parquet of workload_replication.derive_wf rows (game_id, ppmin_home, ppmin_away)")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--write-params", type=Path, default=None)
    ap.add_argument("--n-boot", type=int, default=PD.N_BOOT)
    a = ap.parse_args(argv)
    res = run(a.cache, a.history, pd.read_parquet(a.wf), a.n_boot)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=1, sort_keys=True))
    if a.write_params:
        a.write_params.write_text(json.dumps(res["final_params_fit_on_2022_2025"], indent=1, sort_keys=True) + "\n")
    print(json.dumps({"out": str(a.out), "final_params": res["final_params_fit_on_2022_2025"]}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
