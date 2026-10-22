"""Rolling-origin comparison of DATA_ONLY_V1 against opponent-adjusted challengers (RESEARCH_ONLY, no market data).

For every regular-season game of each test season, in date order, every arm sees only rows dated STRICTLY BEFORE the game
date and is simulated with the same seed and simulator, so differences between arms are differences in expected goals
alone. Per test season the challenger's three hyper-parameters are chosen from the PRIOR season's games only
(:func:`nhl_edge.research.oa_model.select_hyperparameters`); nothing is tuned on a test season.

Arms
    V1          production ratings (recency-weighted raw xG, not opponent-adjusted), goalie term off (no point-in-time starters)
    OA_XG       ridge opponent-adjusted raw xG ratings; V1's finishing, home, b2b and simulator unchanged
    OA_SVA      same on MoneyPuck score- and venue-adjusted xG
    OA_SVA_G25  OA_SVA with 25% of the rating taken from a goals-based ridge fit
    LEAGUE      league-average lambdas with home advantage only (no team information)

Outputs: per-game table (lambdas and probabilities per arm + outcomes), per-game total / margin pmfs (npz) and the
hyper-parameter selection log. ``python -m nhl_edge.research.oa_walk_forward --history data/history --out OUT``
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import replace
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.data.history import load_nhl_games, load_team_games
from nhl_edge.features.ratings import HOME_ADJ, expected_goals, last_game_date, league_rates, rest_days, team_rating
from nhl_edge.log import get_logger, kv
from nhl_edge.model_research.wf_data import pmfs, simulate_row
from nhl_edge.research.oa_model import OAConfig, build_oa_data, fit_oa, oa_team_ratings, select_hyperparameters
from nhl_edge.research.walk_forward import DEFAULT_SEED, attach_outcomes, build_gamelog, evaluation_games, game_seed

log = get_logger(__name__)

ARM_SPECS: dict[str, dict[str, Any]] = {
    "OA_XG": {"target": "xg", "goals_blend": 0.0},
    "OA_SVA": {"target": "xg_sva", "goals_blend": 0.0},
    "OA_SVA_G25": {"target": "xg_sva", "goals_blend": 0.25},
}
ARMS = ("V1", *ARM_SPECS, "LEAGUE")


def _row_from_sim(res_pmfs: dict[str, Any], lam_h: float, lam_a: float, prefix: str) -> dict[str, float]:
    total = res_pmfs["total"]
    ks = np.arange(len(total))
    return {f"{prefix}lam_home": lam_h, f"{prefix}lam_away": lam_a, f"{prefix}p_home_win": res_pmfs["p_home_win"], f"{prefix}p_overtime": res_pmfs["p_ot"],
            f"{prefix}expected_total": float((total * ks).sum()), **{f"{prefix}p_over_{ln}": float(total[ks > ln].sum()) for ln in (4.5, 5.5, 6.5, 7.5)}}


def run_oa_walk_forward(team_games: pd.DataFrame, nhl_games: pd.DataFrame, test_seasons: list[int], *, n_sims: int = 4000, base_seed: int = DEFAULT_SEED,
                        max_games: int | None = None, arms: dict[str, dict[str, Any]] | None = None) -> tuple[pd.DataFrame, dict[str, np.ndarray], dict[str, Any]]:
    t0 = time.time()
    arms = ARM_SPECS if arms is None else arms
    gamelog = build_gamelog(team_games)
    data = build_oa_data(team_games)
    games, skipped = evaluation_games(nhl_games, test_seasons)
    if max_games:
        games = games.iloc[:max_games].copy()
    team_logs = {t: d for t, d in gamelog.groupby("team")}
    selected: dict[str, dict[str, Any]] = {}
    grids: dict[str, list[dict[str, Any]]] = {}
    all_final = nhl_games[(nhl_games["game_type"] == 2) & nhl_games["final"].astype(bool)]
    for season in sorted(set(int(s) for s in games["season"].unique())):
        prior = all_final[all_final["season"] < season]
        for arm, spec in arms.items():
            cfg, tbl = select_hyperparameters(data, prior, season, target=spec["target"], goals_blend=spec["goals_blend"])
            selected[f"{arm}|{season}"] = {"half_life_days": cfg.half_life_days, "ridge": cfg.ridge, "season_discount": cfg.season_discount, **spec}
            grids[f"{arm}|{season}"] = tbl.to_dict("records")
        log.info(kv(event="oa_hyperparameters", season=season, **{a: (selected[f'{a}|{season}']['half_life_days'], selected[f'{a}|{season}']['ridge'], selected[f'{a}|{season}']['season_discount']) for a in arms}))
    recs: list[dict[str, Any]] = []
    tot_pmf, mar_pmf = [], []
    fit_cache: dict[tuple[str, int, str], Any] = {}
    league_cache: dict[tuple[str, int], Any] = {}
    for i, r in enumerate(games.itertuples(index=False)):
        date, season, home, away, gid = str(r.game_date), int(r.season), str(r.home_abbrev), str(r.away_abbrev), int(r.game_id)
        key = (date, season)
        lg = league_cache.get(key) or league_cache.setdefault(key, league_rates(gamelog, date, season=season))
        h_log, a_log = team_logs.get(home, gamelog), team_logs.get(away, gamelog)
        hr, ar = team_rating(h_log, home, date, lg, current_season=season), team_rating(a_log, away, date, lg, current_season=season)
        h_rest, a_rest = rest_days(last_game_date(h_log, home, date), date), rest_days(last_game_date(a_log, away, date), date)
        hb, ab = h_rest == 1, a_rest == 1
        seed = game_seed(gid, base_seed)
        rec: dict[str, Any] = {"game_id": gid, "season": season, "game_date": date, "home": home, "away": away, "seed": seed,
                               "home_b2b": hb, "away_b2b": ab, "home_games_used": hr.games_used, "away_games_used": ar.games_used}
        lam_by_arm: dict[str, tuple[float, float]] = {}
        lam_h, lam_a, _ = expected_goals(hr, ar, lg, 1.0, 1.0, hb, ab)
        lam_by_arm["V1"] = (lam_h, lam_a)
        lam_by_arm["LEAGUE"] = (lg.g60 * HOME_ADJ, lg.g60 / HOME_ADJ)
        for arm, spec in arms.items():
            sel = selected[f"{arm}|{season}"]
            cfg = OAConfig(half_life_days=sel["half_life_days"], ridge=sel["ridge"], season_discount=sel["season_discount"], target=spec["target"],
                           goals_blend=spec["goals_blend"])
            fk = (date, season, arm)
            fit = fit_cache.get(fk)
            if fit is None:
                fit = fit_oa(data, int(date.replace("-", "")), season, cfg)
                fit_cache[fk] = fit
            oh, oa_ = oa_team_ratings(fit, data, home, away, lg)
            oh, oa_ = replace(oh, finish=hr.finish), replace(oa_, finish=ar.finish)
            lh, la, _ = expected_goals(oh, oa_, lg, 1.0, 1.0, hb, ab)
            lam_by_arm[arm] = (lh, la)
        if len(fit_cache) > 6 * len(arms):  # a date is only needed while its games are being predicted
            fit_cache = {k: v for k, v in fit_cache.items() if k[0] == date}
        for arm in ARMS:  # one simulation per arm; pmfs are kept in ARMS order for ranked-probability scoring
            lh, la = lam_by_arm[arm]
            pm = pmfs(simulate_row(lh, la, seed, n_sims))
            rec.update(_row_from_sim(pm, lh, la, f"{arm}_"))
            tot_pmf.append(pm["total"])
            mar_pmf.append(pm["margin"])
        recs.append(rec)
        if (i + 1) % 200 == 0:
            log.info(kv(event="oa_wf_progress", done=i + 1, total=len(games), elapsed_s=round(time.time() - t0, 1)))
    df = attach_outcomes(pd.DataFrame(recs), games)
    n_arm = len(ARMS)
    pm_arrays = {"total": np.asarray(tot_pmf).reshape(len(recs), n_arm, -1), "margin": np.asarray(mar_pmf).reshape(len(recs), n_arm, -1), "arms": np.array(ARMS)}
    meta = {"test_seasons": [int(s) for s in test_seasons], "n_games": int(len(df)), "n_sims": n_sims, "base_seed": base_seed, "skipped": skipped,
            "selected_hyperparameters": selected, "elapsed_s": round(time.time() - t0, 1), "arms": list(ARMS)}
    return df, pm_arrays, meta | {"hyperparameter_grids": grids}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.oa_walk_forward")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--out", required=True)
    ap.add_argument("--test-seasons", default="2023,2024,2025")
    ap.add_argument("--n-sims", type=int, default=4000)
    ap.add_argument("--max-games", type=int)
    a = ap.parse_args(argv)
    hist = Path(a.history)
    seasons = [int(s) for s in a.test_seasons.split(",")]
    tg = load_team_games(hist, None)
    ng = load_nhl_games(hist, None)
    df, pm, meta = run_oa_walk_forward(tg, ng, seasons, n_sims=a.n_sims, max_games=a.max_games)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    df.to_csv(out / "oa_games.csv", index=False)
    np.savez_compressed(out / "oa_pmfs.npz", **pm)
    (out / "oa_meta.json").write_text(json.dumps(meta, indent=1, default=str))
    print(json.dumps({k: meta[k] for k in ("n_games", "elapsed_s", "selected_hyperparameters")}, indent=1, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
