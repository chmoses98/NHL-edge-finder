"""Re-tuned V1 (``V1_R``), its recalibrated version and one-feature ablations (RESEARCH_ONLY; docs/research/v1-retune/PREREGISTRATION.md).

Per test season the half-life, shrinkage prior and home-ice multiplier of DATA_ONLY_V1's own (non-opponent-adjusted) ratings are chosen by
Poisson goals log-likelihood on the TWO PRIOR SEASONS (every validation game rated only from earlier rows) and used unchanged on the test season,
with the same simulator and per-game seeds as every other arm. The grid is wider than the earlier ``V1_T`` control, whose prior sat on its lower
boundary. The ablations reuse the constants selected for ``V1_R`` and switch off one V1 feature.

``python -m nhl_edge.research.v1_retune --history data/history --games OUT/oa_games.csv --out OUT``
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.data.history import load_nhl_games, load_team_games
from nhl_edge.features.ratings import HOME_ADJ
from nhl_edge.log import get_logger, kv
from nhl_edge.model_research.wf_data import pmfs, simulate_row
from nhl_edge.research import v1_tuned_control as T
from nhl_edge.research.oa_model import SlopeCalibrator, goals_nll
from nhl_edge.research.walk_forward import DEFAULT_SEED, build_gamelog, game_seed

log = get_logger(__name__)

GRID_HALF_LIFE = (10.0, 20.0, 40.0, 80.0, 160.0)
GRID_PRIOR = (2.5, 5.0, 10.0, 20.0, 40.0, 80.0, 160.0)
GRID_HOME = (1.0, 1.03, 1.045, 1.06)
ARMS = ("V1_R", "V1_R_C1", "V1_R_noB2B", "V1_R_noFIN")
BASE_ARMS = ("V1_R", "V1_R_noB2B", "V1_R_noFIN")        # arms that need a rating pass; the _C1 arm recalibrates V1_R
_SHARED = T._SHARED


def tune_and_predict(season: int) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    gamelog, team_logs, games = _SHARED["gamelog"], _SHARED["team_logs"], _SHARED["games"]
    val = games[games["season"].between(season - 2, season - 1)]
    cache: dict = {}
    scores: list[tuple[float, float, float, float]] = []
    for hl, prior in itertools.product(GRID_HALF_LIFE, GRID_PRIOR):
        lh, la, gh, ga = [], [], [], []
        for g in val.itertuples(index=False):
            a, b = T._lams(g, hl, prior, gamelog, team_logs, cache)
            lh.append(a)
            la.append(b)
            gh.append(g.home_score)
            ga.append(g.away_score)
        lh, la, gh, ga = (np.asarray(x, float) for x in (lh, la, gh, ga))
        for h in GRID_HOME:
            r = h / HOME_ADJ
            scores.append((goals_nll(lh * r, la / r, gh, ga), hl, prior, h))
    grid = [{"season": season, "val_goals_nll": s, "half_life": hl, "prior": p, "home_adj": h} for s, hl, p, h in sorted(scores)]
    _, hl, prior, h = min(scores)
    test = games[games["season"] == season]
    out: list[dict[str, Any]] = []
    cache = {}
    r = h / HOME_ADJ
    for g in test.itertuples(index=False):
        row: dict[str, Any] = {"game_id": int(g.game_id), "season": season, "half_life": hl, "prior": prior, "home_adj": h}
        for arm, kw in (("V1_R", {}), ("V1_R_noB2B", {"b2b": False}), ("V1_R_noFIN", {"finish": False})):
            a, b = T._lams(g, hl, prior, gamelog, team_logs, cache, **kw)
            row[f"{arm}_lam_home"], row[f"{arm}_lam_away"] = a * r, b / r
        out.append(row)
    return out, grid


def boundary_report(selected: pd.DataFrame) -> dict[str, Any]:
    """Which seasons selected a value on the edge of the grid (a binding grid is reported, never silently widened)."""
    per = selected.drop_duplicates("season").set_index("season")
    edges = {"half_life": (GRID_HALF_LIFE[0], GRID_HALF_LIFE[-1]), "prior": (GRID_PRIOR[0], GRID_PRIOR[-1]), "home_adj": (GRID_HOME[0], GRID_HOME[-1])}
    return {k: {"values": {int(s): float(per.loc[s, k]) for s in per.index}, "at_lower_edge": [int(s) for s in per.index if per.loc[s, k] == lo],
                "at_upper_edge": [int(s) for s in per.index if per.loc[s, k] == hi]} for k, (lo, hi) in edges.items()}


def run(history: Path, games_csv: Path, out: Path, n_sims: int = 4000, workers: int = 4) -> dict[str, Any]:
    import multiprocessing as mp

    tg, ng = load_team_games(history, None), load_nhl_games(history, None)
    gamelog = build_gamelog(tg)
    base = pd.read_csv(games_csv)
    final = ng[(ng["game_type"] == 2) & ng["final"].astype(bool)].dropna(subset=["home_score", "away_score"])
    _SHARED.update({"gamelog": gamelog, "team_logs": {t: d for t, d in gamelog.groupby("team")}, "games": final.sort_values(["game_date", "game_id"]).reset_index(drop=True)})
    seasons = sorted(int(s) for s in base["season"].unique())
    cache = out / "v1r_cache"                    # one file per tuned season: a restarted job resumes instead of redoing hours of tuning
    cache.mkdir(parents=True, exist_ok=True)
    done: dict[int, Any] = {}
    for s in seasons:
        f = cache / f"season_{s}.json"
        if f.exists():
            done[s] = json.loads(f.read_text())
    todo = [s for s in seasons if s not in done]
    if todo:
        with mp.get_context("fork").Pool(min(workers, len(todo))) as pool:
            for s, res in zip(todo, pool.imap(tune_and_predict, todo), strict=True):
                (cache / f"season_{s}.json").write_text(json.dumps(res))
                done[s] = res
    parts = [tuple(done[s]) for s in seasons]
    lam = pd.DataFrame([r for p, _ in parts for r in p]).set_index("game_id")
    grids = [g for _, grid in parts for g in grid]
    cal = SlopeCalibrator()
    rows: list[dict[str, Any]] = []
    tot: dict[str, list] = {a: [] for a in ARMS}
    mar: dict[str, list] = {a: [] for a in ARMS}
    for g in base.itertuples(index=False):                  # base is in (date, game_id) order, as the calibrator requires
        a = lam.loc[int(g.game_id)]
        seed = game_seed(int(g.game_id), DEFAULT_SEED)
        lams = {arm: (float(a[f"{arm}_lam_home"]), float(a[f"{arm}_lam_away"])) for arm in BASE_ARMS}
        lams["V1_R_C1"] = cal.transform(str(g.game_date), *lams["V1_R"])
        row: dict[str, Any] = {"game_id": int(g.game_id), "V1_R_half_life": a.half_life, "V1_R_prior": a.prior, "V1_R_home_adj": a.home_adj}
        for arm in ARMS:
            lh, la = lams[arm]
            pm = pmfs(simulate_row(lh, la, seed, n_sims))
            ks = np.arange(len(pm["total"]))
            row.update({f"{arm}_lam_home": lh, f"{arm}_lam_away": la, f"{arm}_p_home_win": pm["p_home_win"], f"{arm}_p_overtime": pm["p_ot"],
                        f"{arm}_expected_total": float((pm["total"] * ks).sum()), **{f"{arm}_p_over_{x}": float(pm["total"][ks > x].sum()) for x in (4.5, 5.5, 6.5, 7.5)}})
            tot[arm].append(pm["total"])
            mar[arm].append(pm["margin"])
        rows.append(row)
        cal.observe(str(g.game_date), *lams["V1_R"], float(g.home_score + g.away_score), float(g.home_score - g.away_score))
    df = pd.DataFrame(rows)
    df.to_csv(out / "v1r_games.csv", index=False)
    np.savez_compressed(out / "v1r_pmfs.npz", total=np.stack([np.asarray(tot[a]) for a in ARMS], axis=1), margin=np.stack([np.asarray(mar[a]) for a in ARMS], axis=1), arms=np.array(ARMS))
    pd.DataFrame(grids).to_csv(out / "v1r_grid.csv", index=False)
    sel = lam.reset_index()[["season", "half_life", "prior", "home_adj"]]
    rep = boundary_report(sel)
    log.info(kv(event="v1_retune_done", games=len(rows)))
    return rep


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.v1_retune")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--games", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--n-sims", type=int, default=4000)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args(argv)
    rep = run(Path(a.history), Path(a.games), Path(a.out), a.n_sims, a.workers)
    (Path(a.out) / "v1r_boundary.json").write_text(json.dumps(rep, indent=1))
    print(json.dumps(rep, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
