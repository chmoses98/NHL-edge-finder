"""Control arm ``V1_T``: DATA_ONLY_V1's own (non-opponent-adjusted) ratings with the SAME tuning budget as the challengers.

The OA challengers choose three hyper-parameters per test season from the two prior seasons; the incumbent V1 uses fixed constants.
A gain of a tuned challenger over an untuned incumbent can therefore be a tuning gain rather than a modelling gain. ``V1_T`` removes that
confound: V1's recency half-life (games), shrinkage prior (games) and home-ice multiplier are chosen per test season by Poisson goals
log-likelihood on the two prior seasons (each validation game rated only from earlier rows), then used unchanged on the test season,
simulated with the same seeds and simulator.

This is a POST-RUN CONTROL added after the preregistered arms were run; it cannot change a registered verdict, only how it is interpreted.
``python -m nhl_edge.research.v1_tuned_control --history data/history --games OUT/oa_games.csv --out OUT``
"""

from __future__ import annotations

import argparse
import itertools
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.data.history import load_nhl_games, load_team_games
from nhl_edge.features.ratings import HOME_ADJ, expected_goals, last_game_date, league_rates, rest_days, team_rating
from nhl_edge.log import get_logger, kv
from nhl_edge.model_research.wf_data import pmfs, simulate_row
from nhl_edge.research.oa_model import goals_nll
from nhl_edge.research.walk_forward import DEFAULT_SEED, build_gamelog, game_seed

log = get_logger(__name__)
GRID_HALF_LIFE = (10.0, 20.0, 40.0, 80.0)
GRID_PRIOR = (10.0, 20.0, 40.0, 80.0)
GRID_HOME = (1.0, 1.03, 1.045, 1.06)
_SHARED: dict[str, Any] = {}


def _lams(game: Any, hl: float, prior: float, gamelog: pd.DataFrame, team_logs: dict[str, pd.DataFrame], league_cache: dict) -> tuple[float, float]:
    date, season = str(game.game_date), int(game.season)
    lg = league_cache.get((date, season)) or league_cache.setdefault((date, season), league_rates(gamelog, date, season=season))
    hl_log, al_log = team_logs.get(game.home_abbrev, gamelog), team_logs.get(game.away_abbrev, gamelog)
    hr = team_rating(hl_log, game.home_abbrev, date, lg, current_season=season, half_life=hl, prior_games=prior)
    ar = team_rating(al_log, game.away_abbrev, date, lg, current_season=season, half_life=hl, prior_games=prior)
    hb = rest_days(last_game_date(hl_log, game.home_abbrev, date), date) == 1
    ab = rest_days(last_game_date(al_log, game.away_abbrev, date), date) == 1
    lh, la, _ = expected_goals(hr, ar, lg, 1.0, 1.0, hb, ab)
    return lh, la


def _tune_and_predict(season: int) -> list[dict[str, Any]]:
    gamelog, team_logs, games = _SHARED["gamelog"], _SHARED["team_logs"], _SHARED["games"]
    val = games[games["season"].between(season - 2, season - 1)]
    cache: dict = {}
    scores = []
    for hl, prior in itertools.product(GRID_HALF_LIFE, GRID_PRIOR):
        lh, la, gh, ga = [], [], [], []
        for g in val.itertuples(index=False):
            a, b = _lams(g, hl, prior, gamelog, team_logs, cache)
            lh.append(a)
            la.append(b)
            gh.append(g.home_score)
            ga.append(g.away_score)
        lh, la, gh, ga = (np.asarray(x, float) for x in (lh, la, gh, ga))
        for h in GRID_HOME:
            r = h / HOME_ADJ
            scores.append((goals_nll(lh * r, la / r, gh, ga), hl, prior, h))
    _, hl, prior, h = min(scores)
    test = games[games["season"] == season]
    out = []
    cache = {}
    for g in test.itertuples(index=False):
        a, b = _lams(g, hl, prior, gamelog, team_logs, cache)
        r = h / HOME_ADJ
        out.append({"game_id": int(g.game_id), "lam_home": a * r, "lam_away": b / r, "half_life": hl, "prior": prior, "home_adj": h, "season": season})
    return out


def run(history: Path, games_csv: Path, out: Path, n_sims: int = 4000, workers: int = 4) -> None:
    import multiprocessing as mp

    tg, ng = load_team_games(history, None), load_nhl_games(history, None)
    gamelog = build_gamelog(tg)
    base = pd.read_csv(games_csv)
    final = ng[(ng["game_type"] == 2) & ng["final"].astype(bool)].dropna(subset=["home_score", "away_score"])
    _SHARED.update({"gamelog": gamelog, "team_logs": {t: d for t, d in gamelog.groupby("team")}, "games": final.sort_values(["game_date", "game_id"]).reset_index(drop=True)})
    seasons = sorted(int(s) for s in base["season"].unique())
    with mp.get_context("fork").Pool(workers) as pool:
        parts = pool.map(_tune_and_predict, seasons)
    lam = pd.DataFrame([r for p in parts for r in p]).set_index("game_id")
    rows, tot, mar = [], [], []
    for g in base.itertuples(index=False):
        a = lam.loc[int(g.game_id)]
        pm = pmfs(simulate_row(a.lam_home, a.lam_away, game_seed(int(g.game_id), DEFAULT_SEED), n_sims))
        ks = np.arange(len(pm["total"]))
        rows.append({"game_id": int(g.game_id), "V1_T_lam_home": a.lam_home, "V1_T_lam_away": a.lam_away, "V1_T_p_home_win": pm["p_home_win"], "V1_T_p_overtime": pm["p_ot"],
                     "V1_T_expected_total": float((pm["total"] * ks).sum()), **{f"V1_T_p_over_{x}": float(pm["total"][ks > x].sum()) for x in (4.5, 5.5, 6.5, 7.5)},
                     "V1_T_half_life": a.half_life, "V1_T_prior": a.prior, "V1_T_home_adj": a.home_adj})
        tot.append(pm["total"])
        mar.append(pm["margin"])
    pd.DataFrame(rows).to_csv(out / "v1t_games.csv", index=False)
    np.savez_compressed(out / "v1t_pmfs.npz", total=np.asarray(tot), margin=np.asarray(mar))
    log.info(kv(event="v1_tuned_done", games=len(rows)))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.v1_tuned_control")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--games", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--n-sims", type=int, default=4000)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args(argv)
    run(Path(a.history), Path(a.games), Path(a.out), a.n_sims, a.workers)
    return 0


if __name__ == "__main__":
    sys.exit(main())


def add_c1_arm(dir_: Path, n_sims: int = 4000) -> None:
    """``V1_T_C1``: the tuned-V1 control with the same strictly-prior slope recalibration as the ``_C1`` arms (post-run, interpretive)."""
    from nhl_edge.research.oa_model import SlopeCalibrator

    base = pd.read_csv(dir_ / "oa_games.csv")
    v1t = pd.read_csv(dir_ / "v1t_games.csv")
    cal = SlopeCalibrator()
    rows, tot, mar = [], [], []
    for g, t in zip(base.itertuples(index=False), v1t.itertuples(index=False), strict=True):
        lh, la = cal.transform(str(g.game_date), t.V1_T_lam_home, t.V1_T_lam_away)
        pm = pmfs(simulate_row(lh, la, game_seed(int(g.game_id), DEFAULT_SEED), n_sims))
        ks = np.arange(len(pm["total"]))
        rows.append({"V1_T_C1_lam_home": lh, "V1_T_C1_lam_away": la, "V1_T_C1_p_home_win": pm["p_home_win"], "V1_T_C1_p_overtime": pm["p_ot"], "V1_T_C1_expected_total": float((pm["total"] * ks).sum()),
                     **{f"V1_T_C1_p_over_{x}": float(pm["total"][ks > x].sum()) for x in (4.5, 5.5, 6.5, 7.5)}})
        tot.append(pm["total"])
        mar.append(pm["margin"])
        cal.observe(str(g.game_date), t.V1_T_lam_home, t.V1_T_lam_away, float(g.home_score + g.away_score), float(g.home_score - g.away_score))
    pd.DataFrame(rows).to_csv(dir_ / "v1tc1_games.csv", index=False)
    np.savez_compressed(dir_ / "v1tc1_pmfs.npz", total=np.asarray(tot), margin=np.asarray(mar))
