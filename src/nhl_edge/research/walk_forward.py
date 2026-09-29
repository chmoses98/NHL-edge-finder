"""Walk-forward (point-in-time) evaluation of DATA_ONLY_V1 game probabilities on the historical dataset.

THESE RESULTS ARE HISTORICAL, NOT PROSPECTIVE, AND USE NO MARKET DATA. No Kalshi prices are ingested here, so
nothing below says anything about edge versus a market; it says whether the ratings -> expected goals -> simulator
chain produces calibrated, better-than-naive probabilities on games it has not seen.

For every regular-season NHL game in the test seasons (default MoneyPuck seasons 2024 and 2025, i.e. NHL 2024-25
and 2025-26), in date order:

1. Team ratings are built with :func:`nhl_edge.features.ratings.team_rating` ``as_of`` the game date, which uses
   only MoneyPuck rows dated STRICTLY BEFORE that date (so neither the game itself nor any other game that day is
   visible). League rates use the same cutoff. Constants are the production DATA_ONLY_V1 values; nothing is tuned
   here.
2. Goalie factors are 1.0 for both teams: the history archive has no point-in-time goalie (starter) data, so any
   goalie adjustment would be either lookahead or a guess. This is documented in the report.
3. Expected goals from :func:`expected_goals` (home advantage, back-to-back from the team's previous MoneyPuck game
   date), then :func:`nhl_edge.sim.engine.simulate_game` with a seed derived from the game id.
4. Recorded: P(home win incl. OT/SO), P(home regulation win), P(regulation tie) == P(OT), P(over 5.5), P(over 6.5),
   expected total, and the lambdas / components.

Outcomes come from the official NHL stats game list (winner incl. OT/SO, REG/OT/SO, final score). Scores: Brier,
log loss, ECE and a 10-bin calibration table for the moneyline; Brier/log loss for P(OT) and the totals; MAE and
bias of the expected total.

Baselines (also walk-forward, no lookahead):

* ``constant_home``: P(home win) = home-win rate over all final regular-season games dated before the game.
* ``league_poisson``: the same simulator fed league-average lambdas (as_of the game date) with only the home
  adjustment; i.e. what the pipeline produces with no team information at all.

Run: ``python -m nhl_edge.research.walk_forward --history data/history --out docs/research``.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge import AUTHORITY, DATA_ONLY_MODEL_VERSION, FEATURE_VERSION, SIM_VERSION
from nhl_edge.data.history import load_nhl_games, load_team_games
from nhl_edge.evaluation.metrics import brier, calibration_table, ece, log_loss
from nhl_edge.features.ratings import (
    HOME_ADJ,
    LeagueRates,
    expected_goals,
    last_game_date,
    league_rates,
    prepare_gamelog,
    rest_days,
    team_rating,
)
from nhl_edge.log import get_logger, kv
from nhl_edge.sim.engine import SimConfig, TeamParams, simulate_game
from nhl_edge.timeutil import utcnow

log = get_logger(__name__)

DEFAULT_TEST_SEASONS: tuple[int, ...] = (2024, 2025)
DEFAULT_N_SIMS = 4000
DEFAULT_SEED = 20240101
TOTAL_LINES: tuple[float, ...] = (5.5, 6.5)
CALIBRATION_BINS = 10
BANNER = ("HISTORICAL, NOT PROSPECTIVE. These numbers are a walk-forward replay on past seasons and use NO market "
          "data (no Kalshi NHL prices have been ingested). They say nothing about edge versus a market.")
GOALIE_NOTE = ("Goalie factors are fixed at 1.0 for every game: the history archive has no point-in-time starting-goalie "
               "data, so the goalie term of DATA_ONLY_V1 is switched off in this replay. Live predictions include it.")
BASELINES = ("constant_home", "league_poisson")


# --------------------------------------------------------------------------------------------------------------
# data preparation
# --------------------------------------------------------------------------------------------------------------
def build_gamelog(team_games: pd.DataFrame, include_playoffs: bool = False) -> pd.DataFrame:
    """History Parquet rows -> the ``prepare_gamelog`` frame the ratings consume, keyed by canonical abbreviation.

    Only ``situation == 'all'`` rows are used (the ratings are all-situations per-60 rates). Playoff rows are excluded
    by default: the evaluation is regular season and playoff intensity is a different environment.
    """
    d = team_games[team_games["situation"] == "all"].copy()
    if not include_playoffs and "game_type" in d.columns:
        d = d[d["game_type"] == 2]
    d["team"] = d["team_abbrev"].where(d["team_abbrev"].notna(), d["mp_team"])
    d["opposingTeam"] = d["opp_abbrev"].where(d["opp_abbrev"].notna(), d["mp_opposing_team"])
    # prepare_gamelog derives game_id from the raw gameId column; drop the history copy so the rename cannot collide
    return prepare_gamelog(d.drop(columns=["game_id"], errors="ignore"))


def evaluation_games(nhl_games: pd.DataFrame, test_seasons: Iterable[int]) -> tuple[pd.DataFrame, dict[str, int]]:
    """Final regular-season games in the test seasons with both teams resolved, in (date, game_id) order.
    Returns the frame and the skip counts by reason."""
    ss = {int(s) for s in test_seasons}
    d = nhl_games[nhl_games["season"].isin(ss)]
    skipped = {
        "not_regular_season": int((d["game_type"] != 2).sum()),
    }
    d = d[d["game_type"] == 2]
    skipped["not_final"] = int((~d["final"].astype(bool)).sum())
    d = d[d["final"].astype(bool)]
    incomplete = d["home_score"].isna() | d["away_score"].isna() | d["last_period_type"].isna()
    skipped["missing_score_or_period"] = int(incomplete.sum())
    d = d[~incomplete]
    unresolved = d["home_abbrev"].isna() | d["away_abbrev"].isna()
    skipped["unresolved_team"] = int(unresolved.sum())
    d = d[~unresolved]
    return d.sort_values(["game_date", "game_id"]).reset_index(drop=True), skipped


def constant_home_baseline(nhl_games: pd.DataFrame) -> pd.Series:
    """Walk-forward home-win rate: for each game, the mean of ``home_win`` over final regular-season games dated
    STRICTLY before it (0.5 when there is nothing prior). Indexed like ``nhl_games``."""
    d = nhl_games[(nhl_games["game_type"] == 2) & nhl_games["final"].astype(bool) & nhl_games["home_win"].notna()]
    by_date = d.groupby("game_date")["home_win"].agg(["sum", "count"]).sort_index()
    dates = np.asarray(by_date.index.astype(str))
    cum_sum = by_date["sum"].astype(float).cumsum().to_numpy()
    cum_n = by_date["count"].astype(float).cumsum().to_numpy()
    pos = np.searchsorted(dates, nhl_games["game_date"].astype(str).to_numpy(), side="left")  # training dates < game date
    prior_n = np.where(pos > 0, cum_n[np.maximum(pos - 1, 0)], 0.0)
    prior_s = np.where(pos > 0, cum_sum[np.maximum(pos - 1, 0)], 0.0)
    p = np.where(prior_n > 0, prior_s / np.where(prior_n > 0, prior_n, 1.0), 0.5)
    return pd.Series(p, index=nhl_games.index, dtype=float)


# --------------------------------------------------------------------------------------------------------------
# one game
# --------------------------------------------------------------------------------------------------------------
def game_seed(game_id: int, base_seed: int = DEFAULT_SEED) -> int:
    return int((int(base_seed) + int(game_id)) % (2**32))


def sim_probabilities(lam_home: float, lam_away: float, home: str, away: str, seed: int, config: SimConfig,
                      total_lines: Sequence[float] = TOTAL_LINES) -> dict[str, float]:
    res = simulate_game(TeamParams(team_id=0, abbrev=home, lam=lam_home), TeamParams(team_id=0, abbrev=away, lam=lam_away), seed=seed, config=config)
    out = {
        "p_home_win": res.p_win(True)[0], "p_home_reg_win": res.p_reg_win(True)[0], "p_away_reg_win": res.p_reg_win(False)[0],
        "p_reg_tie": res.p_reg_tie()[0], "p_overtime": res.p_overtime()[0], "p_shootout": res.p_shootout()[0],
        "expected_total": float(res.total.mean()), "expected_margin": float(res.margin.mean()),
    }
    for line in total_lines:
        out[f"p_over_{line}"] = res.p_total_gt(line)[0]
    return out


def predict_game(log: pd.DataFrame, home: str, away: str, game_date: str, season: int, game_id: int, *,
                 n_sims: int = DEFAULT_N_SIMS, base_seed: int = DEFAULT_SEED, league: LeagueRates | None = None,
                 team_logs: dict[str, pd.DataFrame] | None = None, total_lines: Sequence[float] = TOTAL_LINES) -> dict[str, Any]:
    """DATA_ONLY_V1 probabilities for one game using only ``log`` rows dated strictly before ``game_date``.

    ``team_logs`` (optional) maps team -> that team's rows, a pure speed-up: the ratings still apply the date cutoff.
    ``league`` (optional) is a precomputed :func:`league_rates` for the same ``as_of``/season.
    """
    lg = league if league is not None else league_rates(log, game_date, season=season)
    tl = team_logs or {}
    h_log = tl.get(home, log)
    a_log = tl.get(away, log)
    hr = team_rating(h_log, home, game_date, lg, current_season=season)
    ar = team_rating(a_log, away, game_date, lg, current_season=season)
    h_rest = rest_days(last_game_date(h_log, home, game_date), game_date)
    a_rest = rest_days(last_game_date(a_log, away, game_date), game_date)
    home_b2b, away_b2b = h_rest == 1, a_rest == 1
    lam_h, lam_a, comp = expected_goals(hr, ar, lg, home_goalie_factor=1.0, away_goalie_factor=1.0, home_b2b=home_b2b, away_b2b=away_b2b)
    seed = game_seed(game_id, base_seed)
    cfg = SimConfig(n_sims=int(n_sims))
    model = sim_probabilities(lam_h, lam_a, home, away, seed, cfg, total_lines)
    naive = sim_probabilities(lg.g60 * HOME_ADJ, lg.g60 / HOME_ADJ, home, away, seed, cfg, total_lines)
    rec: dict[str, Any] = {
        "game_id": int(game_id), "season": int(season), "game_date": game_date, "home": home, "away": away, "seed": seed,
        "lam_home": lam_h, "lam_away": lam_a, "league_g60": lg.g60, "league_xg60": lg.xg60, "league_n_games": lg.n_games,
        "home_games_used": hr.games_used, "away_games_used": ar.games_used, "home_rest_days": h_rest, "away_rest_days": a_rest,
        "home_b2b": home_b2b, "away_b2b": away_b2b, "home_off_xg60": hr.off_xg60, "home_def_xg60": hr.def_xg60,
        "away_off_xg60": ar.off_xg60, "away_def_xg60": ar.def_xg60, "home_finish": hr.finish, "away_finish": ar.finish,
        "home_goalie_factor": 1.0, "away_goalie_factor": 1.0,
    }
    rec.update(model)
    rec.update({f"league_poisson_{k}": v for k, v in naive.items()})
    return rec


# --------------------------------------------------------------------------------------------------------------
# scoring
# --------------------------------------------------------------------------------------------------------------
def _finite(x: float) -> float | None:
    return float(x) if x is not None and math.isfinite(float(x)) else None


def score_binary(p: Sequence[float], y: Sequence[float], with_table: bool = False) -> dict[str, Any]:
    pa, ya = np.asarray(p, dtype=float), np.asarray(y, dtype=float)
    if pa.size == 0:
        return {"n": 0}
    out: dict[str, Any] = {
        "n": int(pa.size), "mean_p": float(pa.mean()), "mean_y": float(ya.mean()), "brier": brier(pa, ya), "log_loss": log_loss(pa, ya),
        "ece": ece(pa, ya, CALIBRATION_BINS),
    }
    if with_table:
        out["calibration"] = calibration_table(pa, ya, CALIBRATION_BINS)
    return out


def score_predictions(df: pd.DataFrame, prefix: str = "", total_lines: Sequence[float] = TOTAL_LINES) -> dict[str, Any]:
    """Score one forecaster's columns (``{prefix}p_home_win`` etc.) against the outcome columns of ``df``."""
    if df.empty:
        return {"n": 0}
    y_home = df["y_home_win"].astype(float).to_numpy()
    y_ot = df["y_overtime"].astype(float).to_numpy()
    total = df["y_total"].astype(float).to_numpy()
    out: dict[str, Any] = {
        "n": int(len(df)),
        "moneyline": score_binary(df[f"{prefix}p_home_win"].to_numpy(), y_home, with_table=True),
        "overtime": score_binary(df[f"{prefix}p_overtime"].to_numpy(), y_ot, with_table=True),
        "totals": {},
    }
    for line in total_lines:
        col = f"{prefix}p_over_{line}"
        if col in df.columns:
            out["totals"][str(line)] = score_binary(df[col].to_numpy(), (total > line).astype(float), with_table=True)
    et = df[f"{prefix}expected_total"].astype(float).to_numpy()
    out["total"] = {"n": int(len(df)), "mae": float(np.mean(np.abs(et - total))), "bias": float(np.mean(et - total)),
                    "mean_expected": float(et.mean()), "mean_actual": float(total.mean()), "sd_actual": float(total.std())}
    if f"{prefix}p_home_reg_win" in df.columns and "y_home_reg_win" in df.columns:
        reg = df[df["y_overtime"] == 0]
        if len(reg):
            out["regulation_moneyline_given_no_ot"] = score_binary(
                (reg[f"{prefix}p_home_reg_win"] / (1 - reg[f"{prefix}p_overtime"]).clip(lower=1e-9)).clip(0, 1).to_numpy(),
                reg["y_home_reg_win"].astype(float).to_numpy())
    return out


def attach_outcomes(preds: pd.DataFrame, games: pd.DataFrame) -> pd.DataFrame:
    g = games[["game_id", "home_score", "away_score", "last_period_type", "home_win"]].copy()
    g["y_home_win"] = g["home_win"].astype(bool).astype(int)
    g["y_overtime"] = (g["last_period_type"] != "REG").astype(int)
    g["y_shootout"] = (g["last_period_type"] == "SO").astype(int)
    g["y_total"] = (g["home_score"].astype(int) + g["away_score"].astype(int)).astype(int)
    g["y_home_reg_win"] = ((g["y_overtime"] == 0) & (g["y_home_win"] == 1)).astype(int)
    g = g.drop(columns=["home_win"])
    return preds.merge(g, on="game_id", how="inner")


# --------------------------------------------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------------------------------------------
def run_walk_forward(team_games: pd.DataFrame, nhl_games: pd.DataFrame, test_seasons: Sequence[int] = DEFAULT_TEST_SEASONS, *,
                     n_sims: int = DEFAULT_N_SIMS, base_seed: int = DEFAULT_SEED, max_games: int | None = None,
                     include_playoffs: bool = False, total_lines: Sequence[float] = TOTAL_LINES) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Replay the test seasons. Returns (per-game frame with predictions + outcomes, report dict)."""
    t0 = time.time()
    log_df = build_gamelog(team_games, include_playoffs=include_playoffs)
    games, skipped = evaluation_games(nhl_games, test_seasons)
    if max_games is not None:
        games = games.iloc[: int(max_games)].copy()
    const_home = dict(zip(nhl_games["game_id"].astype(int), constant_home_baseline(nhl_games).to_numpy()))  # keyed by id, not index
    team_logs = {t: d for t, d in log_df.groupby("team")}
    league_cache: dict[tuple[str, int], LeagueRates] = {}
    recs: list[dict[str, Any]] = []
    for i, r in enumerate(games.itertuples(index=False)):
        key = (str(r.game_date), int(r.season))
        lg = league_cache.get(key)
        if lg is None:
            lg = league_rates(log_df, str(r.game_date), season=int(r.season))
            league_cache[key] = lg
        rec = predict_game(log_df, str(r.home_abbrev), str(r.away_abbrev), str(r.game_date), int(r.season), int(r.game_id),
                           n_sims=n_sims, base_seed=base_seed, league=lg, team_logs=team_logs, total_lines=total_lines)
        rec["constant_home_p_home_win"] = float(const_home[int(r.game_id)])
        recs.append(rec)
        if (i + 1) % 250 == 0:
            log.info(kv(event="walk_forward_progress", done=i + 1, total=len(games), elapsed_s=round(time.time() - t0, 1)))
    preds = pd.DataFrame(recs)
    if preds.empty:
        report = _report_skeleton(test_seasons, n_sims, base_seed, skipped, log_df, nhl_games, include_playoffs, total_lines)
        report["n_games"] = 0
        report["elapsed_s"] = round(time.time() - t0, 1)
        return preds, report
    df = attach_outcomes(preds, games)
    report = _report_skeleton(test_seasons, n_sims, base_seed, skipped, log_df, nhl_games, include_playoffs, total_lines)
    report["n_games"] = int(len(df))
    report["n_games_cold_team"] = int(((df["home_games_used"] <= 0) | (df["away_games_used"] <= 0)).sum())
    report["metrics"] = {"model": score_predictions(df, "", total_lines), "league_poisson": score_predictions(df, "league_poisson_", total_lines)}
    cb = score_binary(df["constant_home_p_home_win"].to_numpy(), df["y_home_win"].astype(float).to_numpy(), with_table=True)
    report["metrics"]["constant_home"] = {"n": int(len(df)), "moneyline": cb}
    report["by_season"] = {}
    for s, d in df.groupby("season"):
        report["by_season"][str(int(s))] = {
            "n": int(len(d)),
            "model": score_predictions(d, "", total_lines), "league_poisson": score_predictions(d, "league_poisson_", total_lines),
            "constant_home": {"n": int(len(d)), "moneyline": score_binary(d["constant_home_p_home_win"].to_numpy(), d["y_home_win"].astype(float).to_numpy())},
        }
    report["elapsed_s"] = round(time.time() - t0, 1)
    return df, report


def _report_skeleton(test_seasons: Sequence[int], n_sims: int, base_seed: int, skipped: dict[str, int], log_df: pd.DataFrame,
                     nhl_games: pd.DataFrame, include_playoffs: bool, total_lines: Sequence[float]) -> dict[str, Any]:
    seasons_in_log = sorted(int(s) for s in log_df["season"].dropna().unique()) if len(log_df) else []
    seasons_in_results = sorted(int(s) for s in nhl_games["season"].dropna().unique()) if len(nhl_games) else []
    return {
        "banner": BANNER, "authority": AUTHORITY, "generated_at_utc": utcnow().isoformat(timespec="seconds").replace("+00:00", "Z"),
        "model_version": DATA_ONLY_MODEL_VERSION, "feature_version": FEATURE_VERSION, "sim_version": SIM_VERSION,
        "n_sims": int(n_sims), "base_seed": int(base_seed), "test_seasons": [int(s) for s in test_seasons],
        "season_convention": "MoneyPuck start year (2024 == NHL 2024-25)",
        "training": "every MoneyPuck 'all'-situation row dated strictly before each game's date (walk-forward); "
                    + ("playoff rows included" if include_playoffs else "regular-season rows only"),
        "seasons_in_moneypuck_log": seasons_in_log, "seasons_in_nhl_results": seasons_in_results,
        "n_log_team_games": int(len(log_df)), "skipped": skipped, "total_lines": [float(x) for x in total_lines],
        "goalie_note": GOALIE_NOTE, "market_note": "No market comparison: no historical Kalshi NHL prices have been ingested.",
        "baselines": {"constant_home": "walk-forward home-win rate over prior final regular-season games",
                      "league_poisson": "same simulator with league-average lambdas (as_of game date) and the home adjustment only"},
    }


# --------------------------------------------------------------------------------------------------------------
# outputs
# --------------------------------------------------------------------------------------------------------------
def _fmt(x: Any, nd: int = 4) -> str:
    if x is None:
        return "-"
    if isinstance(x, float):
        return f"{x:.{nd}f}"
    return str(x)


def _binary_row(name: str, m: dict[str, Any] | None) -> str:
    if not m or not m.get("n"):
        return f"| {name} | 0 | - | - | - | - | - |"
    return f"| {name} | {m['n']} | {_fmt(m['brier'])} | {_fmt(m['log_loss'])} | {_fmt(m['ece'])} | {_fmt(m['mean_p'])} | {_fmt(m['mean_y'])} |"


def render_markdown(report: dict[str, Any], run_id: str, json_name: str) -> str:
    L: list[str] = []
    L.append("# DATA_ONLY_V1 walk-forward evaluation (WALK_FORWARD_V1)\n")
    L.append(f"> **{report['banner']}**\n")
    L.append(f"Run `{run_id}` generated {report['generated_at_utc']} -- authority `{report['authority']}` -- "
             f"model `{report['model_version']}` / features `{report['feature_version']}` / sim `{report['sim_version']}` -- "
             f"machine-readable: `{json_name}`.\n")
    L.append("## Setup\n")
    L.append(f"- Test seasons: {', '.join(str(s) for s in report['test_seasons'])} ({report['season_convention']}).")
    L.append(f"- Training data: {report['training']}. MoneyPuck seasons on disk: {report['seasons_in_moneypuck_log']}; "
             f"NHL result seasons on disk: {report['seasons_in_nhl_results']}; team-game rows in the log: {report['n_log_team_games']}.")
    L.append(f"- Simulation: {report['n_sims']} draws per game, seed = base {report['base_seed']} + game id.")
    L.append(f"- Goalies: {report['goalie_note']}")
    L.append(f"- Markets: {report['market_note']}")
    L.append(f"- Baselines: constant_home = {report['baselines']['constant_home']}; league_poisson = {report['baselines']['league_poisson']}.")
    sk = report.get("skipped", {})
    L.append(f"- Sample: **{report.get('n_games', 0)} regular-season games scored**"
             + (f"; games with a team that had no prior MoneyPuck rows: {report['n_games_cold_team']}" if "n_games_cold_team" in report else "")
             + f". Skipped: {', '.join(f'{k}={v}' for k, v in sk.items()) if sk else 'none'}.")
    L.append(f"- Elapsed: {report.get('elapsed_s', '-')} s.\n")
    metrics = report.get("metrics")
    if not metrics:
        L.append("No games were scored (empty test set).\n")
        return "\n".join(L)

    L.append("## Moneyline (P(home win) incl. OT/SO)\n")
    L.append("| forecaster | n | Brier | log loss | ECE | mean p | hit rate |")
    L.append("|---|---:|---:|---:|---:|---:|---:|")
    L.append(_binary_row("DATA_ONLY_V1", metrics["model"].get("moneyline")))
    L.append(_binary_row("league_poisson", metrics["league_poisson"].get("moneyline")))
    L.append(_binary_row("constant_home", metrics["constant_home"].get("moneyline")))
    L.append("")
    L.append("### Calibration (DATA_ONLY_V1 moneyline, 10 equal-width bins)\n")
    L.append("| bin | n | mean p | hit rate | gap |")
    L.append("|---|---:|---:|---:|---:|")
    for b in metrics["model"]["moneyline"].get("calibration", []):
        L.append(f"| {b['bin_lo']:.1f}-{b['bin_hi']:.1f} | {b['n']} | {_fmt(b['mean_p'], 3)} | {_fmt(b['mean_y'], 3)} | {_fmt(b['gap'], 3)} |")
    L.append("")
    L.append("## Overtime (P(regulation tie))\n")
    L.append("| forecaster | n | Brier | log loss | ECE | mean p | OT rate |")
    L.append("|---|---:|---:|---:|---:|---:|---:|")
    L.append(_binary_row("DATA_ONLY_V1", metrics["model"].get("overtime")))
    L.append(_binary_row("league_poisson", metrics["league_poisson"].get("overtime")))
    L.append("")
    L.append("## Totals\n")
    L.append("| line | forecaster | n | Brier | log loss | ECE | mean p(over) | over rate |")
    L.append("|---|---|---:|---:|---:|---:|---:|---:|")
    for line in report.get("total_lines", []):
        for name, key in (("DATA_ONLY_V1", "model"), ("league_poisson", "league_poisson")):
            m = metrics[key].get("totals", {}).get(str(line))
            row = _binary_row(name, m)
            L.append(f"| {line} " + row)
    L.append("")
    L.append("| forecaster | n | total MAE | bias (exp - actual) | mean expected | mean actual | sd actual |")
    L.append("|---|---:|---:|---:|---:|---:|---:|")
    for name, key in (("DATA_ONLY_V1", "model"), ("league_poisson", "league_poisson")):
        t = metrics[key].get("total")
        if t:
            L.append(f"| {name} | {t['n']} | {_fmt(t['mae'], 3)} | {_fmt(t['bias'], 3)} | {_fmt(t['mean_expected'], 3)} | {_fmt(t['mean_actual'], 3)} | {_fmt(t['sd_actual'], 3)} |")
    L.append("")
    L.append("## By season (moneyline Brier / log loss; total MAE)\n")
    L.append("| season | n | model Brier | model LL | league_poisson Brier | constant_home Brier | model OT Brier | model total MAE |")
    L.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for s, d in sorted(report.get("by_season", {}).items()):
        m, lp, ch = d["model"], d["league_poisson"], d["constant_home"]
        L.append(f"| {s} | {d['n']} | {_fmt(m['moneyline']['brier'])} | {_fmt(m['moneyline']['log_loss'])} | {_fmt(lp['moneyline']['brier'])} | "
                 f"{_fmt(ch['moneyline']['brier'])} | {_fmt(m['overtime']['brier'])} | {_fmt(m['total']['mae'], 3)} |")
    L.append("")
    L.append("## Reading this\n")
    L.append("- Lower Brier / log loss is better; ECE near 0 with gaps near 0 in every populated bin means calibrated. "
             "A model that cannot beat `league_poisson` on the moneyline carries no team information; one that cannot beat "
             "`constant_home` is worse than knowing nothing but home ice.")
    L.append("- Everything above is in-sample for the *constants* of DATA_ONLY_V1 only in the sense that they were chosen "
             "before this replay from public priors; they were not fitted to these results and must not be tuned to them.")
    L.append("- The first weeks of each test season lean on the previous season at a discount (`PREV_SEASON_DISCOUNT`); the "
             "first test season (2024) has two prior seasons of history, the second has three.")
    L.append("- Utah (2024-) is treated as a new club with no Arizona history, matching the identity registry.")
    L.append(f"\n> {report['banner']}\n")
    return "\n".join(L)


def write_outputs(df: pd.DataFrame, report: dict[str, Any], out_dir: Path, run_id: str) -> dict[str, Path]:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"walk_forward_{run_id}.json"
    games_path = out_dir / f"walk_forward_{run_id}_games.csv"
    md_path = out_dir / "WALK_FORWARD_V1.md"
    report = {**report, "run_id": run_id, "files": {"json": json_path.name, "games_csv": games_path.name, "markdown": md_path.name}}
    json_path.write_text(json.dumps(report, indent=2, default=_json_default))
    df.to_csv(games_path, index=False)
    md_path.write_text(render_markdown(report, run_id, json_path.name))
    return {"json": json_path, "games_csv": games_path, "markdown": md_path}


def _json_default(o: Any) -> Any:
    if isinstance(o, np.integer | np.bool_):
        return int(o)
    if isinstance(o, np.floating):
        return _finite(float(o))
    if isinstance(o, np.ndarray):
        return o.tolist()
    return str(o)


def main(argv: Sequence[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.walk_forward", description="Walk-forward evaluation of DATA_ONLY_V1 (historical, no market data).")
    ap.add_argument("--history", default="data/history", help="history root written by nhl_edge.data.history")
    ap.add_argument("--out", default="docs/research")
    ap.add_argument("--test-seasons", default=",".join(map(str, DEFAULT_TEST_SEASONS)), help="MoneyPuck start years to score (2024 == 2024-25)")
    ap.add_argument("--n-sims", type=int, default=DEFAULT_N_SIMS)
    ap.add_argument("--seed", type=int, default=DEFAULT_SEED)
    ap.add_argument("--max-games", type=int, default=None, help="cap the number of scored games (smoke tests)")
    ap.add_argument("--include-playoffs", action="store_true", help="also feed playoff rows to the ratings")
    ap.add_argument("--run", default=None, help="run id used in output file names (default: UTC timestamp)")
    a = ap.parse_args(argv)
    test_seasons = [int(s) for s in str(a.test_seasons).split(",") if s.strip()]
    hist = Path(a.history)
    team_games = load_team_games(hist)
    nhl_games = load_nhl_games(hist)
    if team_games.empty or nhl_games.empty:
        print(f"no history under {hist} (moneypuck rows={len(team_games)}, nhl rows={len(nhl_games)}); run nhl_edge.data.history first", file=sys.stderr)
        return 2
    run_id = a.run or utcnow().strftime("%Y%m%dT%H%M%SZ")
    df, report = run_walk_forward(team_games, nhl_games, test_seasons, n_sims=a.n_sims, base_seed=a.seed, max_games=a.max_games,
                                  include_playoffs=a.include_playoffs)
    paths = write_outputs(df, report, Path(a.out), run_id)
    m = report.get("metrics", {})
    summary = {"run_id": run_id, "n_games": report.get("n_games", 0), "elapsed_s": report.get("elapsed_s"),
               "moneyline_brier": {k: (m.get(k, {}).get("moneyline") or {}).get("brier") for k in ("model", *BASELINES)},
               "files": {k: str(v) for k, v in paths.items()}}
    print(json.dumps(summary, indent=2, default=_json_default))
    return 0


if __name__ == "__main__":
    sys.exit(main())
