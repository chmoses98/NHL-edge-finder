"""WORKLOAD_V1 historical replication on other held-out seasons (RESEARCH_ONLY; offline; skaters only).

    python -m nhl_edge.research.workload_replication --seasons 2023,2024 --out docs/research/workload_v1

Nothing about WORKLOAD_V1 changes: the frozen parameters are read from the untouched ``preregistration.json``, the
constants are fit on the seasons strictly before the evaluated season and the dispersion on the season immediately
before it, exactly as ``workload_experiment.skater_arms`` already does (that function is called as is), and the SAME
seven preregistered acceptance checks (``workload_experiment.accept_skaters``) are applied to the SAME metrics with the
SAME game-clustered bootstrap. The only thing this module adds is the champion's walk-forward stand-in for seasons
the committed V2 walk-forward CSV does not cover (it covers 2024 and 2025 only):

* ``wf_mode="derived"`` (primary): the stand-in columns (point-in-time penalty-minute and PP / PK ratings) are
  re-derived for 2022 and 2023 with ``walk_forward_v2.game_features`` (no simulation; the same code and inputs that
  produced the committed 2024-25 rows, which this module reproduces exactly before using them). The champion
  normalises its PP shares by the mean of the rows it is given: here only seasons <= the season being scored.
* ``wf_mode="coded"`` (sensitivity): ``workload_experiment.Ctx.wf_for`` as it stands, i.e. the committed CSV where it
  has the season and NEUTRAL rows (constant PP minutes) where it has not.

Goalie saves were REJECTED in the original held-out run and are not re-run here.
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
from nhl_edge.research import workload_v1 as W

DERIVED_WF_COLS = ["game_id", "season", "game_date", "lam_st_home", "lam_st_away", "ppmin_home", "ppmin_away", "home_pp_off", "away_pp_off",
                   "home_pk_def", "away_pk_def"]
WF_SEASONS_AVAILABLE = (2024, 2025)  # seasons in the committed V2 walk-forward CSV


def feasible_holdouts(seasons: list[int] = X.SEASONS) -> dict[int, dict[str, Any]]:
    """Which seasons can be held out without leakage under the frozen protocol: constants on all earlier seasons, NegBin
    dispersion on the season before (which itself needs a champion frame, i.e. >= 1 season before THAT)."""
    out = {}
    for s in seasons:
        train = [t for t in seasons if t < s]
        disp = s - 1
        ok = len(train) >= 2 and (disp - 1) in seasons
        out[s] = {"train_seasons": train, "dispersion_season": disp, "feasible": ok,
                  "reason": ("" if ok else "needs a dispersion season that itself has a prior season for the production champion (>= 2 earlier seasons)")}
    return out


def derive_wf(history: Path, seasons: list[int]) -> pd.DataFrame:
    """Point-in-time V2 stand-in rows (team lambdas, penalty-minute and PP / PK ratings) for ``seasons`` via the committed
    walk-forward feature code. No simulation, no market input."""
    from nhl_edge.research import walk_forward_v2 as W2
    from nhl_edge.research.walk_forward import evaluation_games

    ctx, nhl_games, _ = W2.load_ctx(history)
    games, _ = evaluation_games(nhl_games, list(seasons))
    lc: dict = {}
    lst: dict = {}
    rows = [W2.game_features(ctx, r, None, lc, lst) for r in games.itertuples(index=False)]
    return pd.DataFrame(rows)[DERIVED_WF_COLS]


class ReplicationCtx(X.Ctx):
    def __init__(self, history: Path, cache: Path, wf_mode: str, derived: pd.DataFrame | None = None):
        super().__init__(history, cache)
        self.history = history
        if wf_mode not in ("derived", "coded"):
            raise ValueError(wf_mode)
        self.wf_mode = wf_mode
        self.dwf = derived

    def wf_for(self, season: int) -> pd.DataFrame:
        if self.wf_mode == "coded":
            return super().wf_for(season)
        assert self.dwf is not None
        return self.dwf[self.dwf["season"] <= season]


def check_derived_matches_committed(derived: pd.DataFrame, committed: pd.DataFrame) -> dict[str, float]:
    """Max abs difference between the re-derived stand-in and the committed CSV on the overlapping seasons (must be 0)."""
    m = derived.merge(committed, on="game_id", suffixes=("", "_c"))
    return {c: float(np.abs(m[c] - m[c + "_c"]).max()) for c in DERIVED_WF_COLS[3:]} | {"n_overlap": int(len(m))}


def minutes_breakdown(m: pd.DataFrame) -> dict[str, Any]:
    """Descriptive: total / PP / SH TOI error (minutes) by position and by OT status, champion vs WORKLOAD_V1 (shift-chart rows)."""
    w = m[m["shifts_ok"].fillna(False).astype(bool)]
    out: dict[str, Any] = {}
    groups = {"F": w["pos"] == "F", "D": w["pos"] == "D", "ot_games": w["game_ot"].astype(bool), "regulation_games": ~w["game_ot"].astype(bool)}
    for g, k in groups.items():
        d = w[k]
        row: dict[str, Any] = {"n": int(len(d))}
        for name, (c, wc, y) in {"total": ("ch_toi", "wl_toi", "y_toi"), "pp": ("ch_toi_pp", "wl_toi_pp", "y_toi_pp"),
                                 "sh": ("ch_toi_sh", "wl_toi_sh", "y_toi_sh")}.items():
            ce, we = d[c] - d[y], d[wc] - d[y]
            row[name] = {"champion": {"mae": float(ce.abs().mean()), "rmse": float(np.sqrt((ce**2).mean())), "bias": float(ce.mean())},
                         "workload_v1": {"mae": float(we.abs().mean()), "rmse": float(np.sqrt((we**2).mean())), "bias": float(we.mean())}}
        out[g] = row
    return out


def run_season(ctx: ReplicationCtx, season: int, pre: dict[str, Any], n_boot: int) -> dict[str, Any]:
    prm = W.WorkloadParams.from_dict(pre["frozen_params"])
    m, pmfs, al = X.skater_arms(ctx, season, prm)
    rs = X.skater_report(m, pmfs, n_boot)
    rs["alphas"] = {k: v for k, v in al.items() if not k.startswith("_")}
    rs["acceptance"] = X.accept_skaters(rs, pre["acceptance"])
    rs["minutes_breakdown"] = minutes_breakdown(m)
    gid = m["game_id"].to_numpy()
    rs["bias_ci95"] = {"WORKLOAD_V1": E.bootstrap_mean_diff(gid, (m["wl_sog"] - m["y_sog"]).to_numpy(), n_boot),
                       "CHAMPION": E.bootstrap_mean_diff(gid, (m["ch_sog"] - m["y_sog"]).to_numpy(), n_boot)}
    rs["train_seasons"] = al["_constants"]["train_seasons"]
    rs["dispersion_season"] = season - 1
    rs["n_games_without_shift_charts"] = int(m.loc[~m["shifts_ok"].fillna(False).astype(bool), "game_id"].nunique())
    rs["constants"] = al["_constants"]
    return rs


def _league_rates_stable(sk: pd.DataFrame, window: int) -> pd.DataFrame:
    """``workload_v1.league_rates`` with a deterministic tie order (date, game, player). The production-of-research function sorts
    by date only with an unstable sort, so the rows of the window's boundary DATE are chosen arbitrarily; that wobble (a few
    1e-2 in a rate for a rare state) would mask a real leak in the truncation check below. Used ONLY by that check."""
    out = pd.DataFrame(index=sk.index)
    for pos, d in sk.groupby("pos"):
        d = d.sort_values(["date_int", "game_id", "player_id"], kind="stable")
        dts = d["date_int"].to_numpy()
        q = sk.loc[sk["pos"] == pos, "date_int"].to_numpy()
        idx = sk.index[sk["pos"] == pos]
        for s in W.STATES_W:
            num = W.league_prior_mean(dts, d[f"s_{s}"].fillna(0).to_numpy(float), q, window)
            den = W.league_prior_mean(dts, d[f"t_{s}"].fillna(0).to_numpy(float), q, window)
            out.loc[idx, f"lgr_{s}"] = W._div(num, den / 3600.0, np.nan)
    return out


def leakage_truncation_check(ctx: ReplicationCtx, season: int, pre: dict[str, Any]) -> dict[str, Any]:
    """Recompute the WORKLOAD_V1 means for ``season`` from tables that contain NO row of any later season and compare with the
    means from the full tables (both with a deterministic tie order in the league-rate window). Identical = no later-season row
    reaches a prediction for ``season``."""
    d = ctx.data
    keep = lambda df: df[df["season"] <= season]  # noqa: E731
    tg = W.team_games(keep(d.players), keep(d.team_states), keep(d.shots), keep(d.goals))
    sk = W.skater_table(keep(d.players), tg, keep(d.shots))
    prm = W.WorkloadParams.from_dict(pre["frozen_params"])
    train = [s for s in X.SEASONS if s < season]
    c = W.fit_constants(sk, tg, keep(d.goalies), train)
    c_full = W.fit_constants(ctx.sk, ctx.tg, d.goalies, train)
    orig = W.league_rates
    W.league_rates = _league_rates_stable  # type: ignore[assignment]
    try:
        a = W.skater_predictions(sk, tg, c, prm)
        b = W.skater_predictions(ctx.sk, ctx.tg, c_full, prm)
    finally:
        W.league_rates = orig
    a = a[(a["season"] == season) & (a["game_type"] == 2)].set_index(["game_id", "player_id"])["wl_sog"]
    b = b[(b["season"] == season) & (b["game_type"] == 2)].set_index(["game_id", "player_id"])["wl_sog"]
    j = a.to_frame("trunc").join(b.to_frame("full"), how="outer")
    diff = float(np.nanmax((j["trunc"] - j["full"]).abs()))
    return {"season": season, "n_rows": int(len(j)), "n_missing_either": int(j.isna().any(axis=1).sum()), "constants_identical": c.to_dict() == c_full.to_dict(),
            "max_abs_diff_wl_sog": diff, "identical": bool(j.notna().all().all() and diff < 1e-9)}


def champion_truncation_check(ctx: ReplicationCtx, season: int) -> dict[str, Any]:
    """Rebuild the PRODUCTION champion's skater frame for ``season`` from a ``Data`` that holds no row of any later season (same
    stand-in rows) and compare ``ch_sog`` / ``ch_toi`` with the evaluated (full-data) frame."""
    from nhl_edge.research import workload_audit as A
    from nhl_edge.research.player_walk_forward import Data

    d = Data(ctx.history, [s for s in X.SEASONS if s <= season])
    t = A.champion_skaters(d, ctx.wf_for(season), season)
    f = ctx.champ_sk(season)
    a = t.set_index(["game_id", "player_id"])[["ch_sog", "ch_toi"]].add_suffix("_t")
    j = a.join(f.set_index(["game_id", "player_id"])[["ch_sog", "ch_toi"]].add_suffix("_f"), how="outer")
    dsog = float(np.nanmax((j["ch_sog_t"] - j["ch_sog_f"]).abs()))
    dtoi = float(np.nanmax((j["ch_toi_t"] - j["ch_toi_f"]).abs()))
    return {"season": season, "n_rows": int(len(j)), "n_missing_either": int(j.isna().any(axis=1).sum()), "max_abs_diff_ch_sog": dsog, "max_abs_diff_ch_toi": dtoi,
            "identical": bool(j.notna().all().all() and dsog < 1e-9 and dtoi < 1e-9)}


def _jsonable(o: Any) -> Any:
    return X._round(o)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.workload_replication")
    ap.add_argument("--seasons", default="2023,2024", help="comma-separated held-out seasons (start year of the NHL season)")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--cache", default="out/workload_v1_replication_cache")
    ap.add_argument("--out", default="docs/research/workload_v1")
    ap.add_argument("--prereg", default="docs/research/workload_v1/preregistration.json")
    ap.add_argument("--wf-modes", default="derived,coded")
    ap.add_argument("--n-boot", type=int, default=2000)
    ap.add_argument("--leakage-check", action="store_true")
    a = ap.parse_args(argv)
    seasons = [int(s) for s in a.seasons.split(",")]
    feas = feasible_holdouts()
    bad = [s for s in seasons if not feas.get(s, {}).get("feasible")]
    if bad:
        raise SystemExit(f"cannot hold out {bad} without leakage / a missing champion frame: {feas}")
    pre = json.loads(Path(a.prereg).read_text())
    history = Path(a.history)
    t0 = time.time()
    derived = derive_wf(history, [2022, 2023, 2024, 2025])
    committed = pd.read_csv(X.WF_GAMES)
    wf_check = check_derived_matches_committed(derived[derived["season"] == 2024], committed[committed["season"] == 2024])
    print("derived stand-in vs committed 2024 rows:", wf_check, flush=True)
    res: dict[str, Any] = {"model_version": W.MODEL_VERSION, "preregistration": pre["id"], "frozen_params": pre["frozen_params"],
                           "acceptance_rule": pre["acceptance"], "feasibility": _jsonable(feas), "derived_wf_vs_committed_2024": wf_check,
                           "note": ("2024 is the VALIDATION season of the preregistration (frozen_params were selected on it): its result is in-sample for the "
                                    "hyperparameters and is NOT an independent replication. 2023 is the only season held out of both the fitting and the selection."),
                           "seasons": {}}
    for mode in a.wf_modes.split(","):
        ctx = ReplicationCtx(history, Path(a.cache) / mode, mode, derived)
        for s in seasons:
            rs = run_season(ctx, s, pre, a.n_boot)
            res["seasons"].setdefault(str(s), {})[mode] = rs
            print(mode, s, json.dumps(_jsonable(rs["acceptance"])), f"{time.time() - t0:.0f}s", flush=True)
            if a.leakage_check and mode == "derived":
                res["seasons"][str(s)]["leakage_truncation_check"] = leakage_truncation_check(ctx, s, pre)
                print("leakage", res["seasons"][str(s)]["leakage_truncation_check"], flush=True)
                res["seasons"][str(s)]["champion_truncation_check"] = champion_truncation_check(ctx, s)
                print("champion leakage", res["seasons"][str(s)]["champion_truncation_check"], flush=True)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / f"replication_{'_'.join(str(s) for s in seasons)}.json").write_text(json.dumps(_jsonable(res), indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
