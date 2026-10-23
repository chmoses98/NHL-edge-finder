"""Why does retuning V1 help in some seasons and not in others? Leakage-safe regime diagnostics (RESEARCH_ONLY).

Question (docs/research/v1-retune/RESULTS.md): the retuned and recalibrated V1 beats production V1 by -0.0017 Brier pooled over 2017-2025, but nearly all of it comes from
2020-2023; on the untouched 2010-2016 seasons and in 2025 the gain is about zero. This module characterises every season 2010-2025 with quantities that are not model
outputs -- scoring environment, finishing, overtime, how much true team-strength spread there is, how persistent strength is from one season to the next, schedule structure,
calibration drift of production V1 -- and relates them to the per-season gain. It also computes ORACLE tuning surfaces (the Brier a V1 with any (half-life, prior) in the
registered grid would have scored on the season itself). The oracle is a DIAGNOSTIC of how much headroom the constants have in a season, computed with the season's own
outcomes; it is never used to select anything and is labelled post hoc wherever it appears.

Leakage-safe reading of the cross-season relationships: the explanatory variables are reported twice, as measured in the season itself (descriptive) and as measured in the
PREVIOUS season (what was knowable before the season started). With 16 seasons nothing here is a test; it is a map of where to look and what to preregister next.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

GRID_HL = (10.0, 20.0, 40.0, 80.0, 160.0)
GRID_PRIOR = (2.5, 5.0, 10.0, 20.0, 40.0, 80.0, 160.0)
PRODUCTION = (20.0, 20.0)
MAXG = 14


def season_stats(games: pd.DataFrame) -> pd.DataFrame:
    """Per-season scoring environment from final regular-season results (columns season, home_score, away_score, last_period_type)."""
    g = games.copy()
    g["total"] = g["home_score"] + g["away_score"]
    g["ot"] = g["last_period_type"].astype(str) != "REG"
    g["home_win"] = g["home_score"] > g["away_score"]
    g["reg_margin_abs"] = (g["home_score"] - g["away_score"]).abs()
    out = g.groupby("season").agg(n_games=("total", "size"), goals_per_game=("total", "mean"), sd_total=("total", "std"), ot_rate=("ot", "mean"), home_win_rate=("home_win", "mean"),
                                   big_margin_rate=("reg_margin_abs", lambda x: float((x >= 3).mean())))
    return out


def team_strength_spread(games: pd.DataFrame) -> pd.DataFrame:
    """SD across teams of goal difference per game (observed) and its true-talent part (observed variance minus the sampling variance of a mean of n games)."""
    rows = []
    for s, g in games.groupby("season"):
        h = pd.DataFrame({"team": g["home"], "gd": g["home_score"] - g["away_score"]})
        a = pd.DataFrame({"team": g["away"], "gd": g["away_score"] - g["home_score"]})
        t = pd.concat([h, a]).groupby("team")["gd"].agg(["mean", "size"])
        game_var = float(pd.concat([h, a])["gd"].var())
        obs = float(t["mean"].var())
        samp = float((game_var / t["size"]).mean())
        rows.append({"season": s, "sd_gd_obs": float(np.sqrt(obs)), "sd_gd_true": float(np.sqrt(max(obs - samp, 0.0))), "reliability": float(max(obs - samp, 0.0) / obs) if obs > 0 else np.nan})
    return pd.DataFrame(rows).set_index("season")


def persistence(games: pd.DataFrame) -> pd.Series:
    """Correlation across teams of goal difference per game between a season and the previous one (franchise-keyed; teams missing in either season are dropped)."""
    gd = {}
    for s, g in games.groupby("season"):
        h = pd.DataFrame({"team": g["home"], "gd": g["home_score"] - g["away_score"]})
        a = pd.DataFrame({"team": g["away"], "gd": g["away_score"] - g["home_score"]})
        gd[int(s)] = pd.concat([h, a]).groupby("team")["gd"].mean()
    out = {}
    for s in sorted(gd):
        if s - 1 in gd:
            j = pd.concat([gd[s - 1], gd[s]], axis=1, join="inner").dropna()
            out[s] = float(j.corr().iloc[0, 1]) if len(j) > 10 else np.nan
    return pd.Series(out, name="persistence_prev_season")


def schedule_stats(games: pd.DataFrame) -> pd.DataFrame:
    """Share of back-to-back games and how concentrated pairings are (games per distinct pairing; share of games whose pairing already met within 14 days)."""
    rows = []
    for s, g in games.groupby("season"):
        g = g.sort_values(["game_date", "game_id"]).copy()
        g["pair"] = [tuple(sorted(x)) for x in zip(g["home"], g["away"], strict=True)]
        g["d"] = pd.to_datetime(g["game_date"])
        last: dict = {}
        again = 0
        for p, d in zip(g["pair"], g["d"], strict=True):
            if p in last and (d - last[p]).days <= 14:
                again += 1
            last[p] = d
        b2b = float(((g["home_b2b"].astype(bool)) | (g["away_b2b"].astype(bool))).mean()) if "home_b2b" in g else np.nan
        rows.append({"season": s, "b2b_game_share": b2b, "games_per_pairing": float(len(g) / g["pair"].nunique()), "repeat_pairing_14d_share": again / len(g)})
    return pd.DataFrame(rows).set_index("season")


def calibration_drift(games: pd.DataFrame, prefix: str = "V1") -> pd.DataFrame:
    """Per season: calibration slope of realised total on the predicted sum of rates and of realised margin on the predicted difference, and the mean total bias, for one arm."""
    rows = []
    for s, g in games.groupby("season"):
        ps = (g[f"{prefix}_lam_home"] + g[f"{prefix}_lam_away"]).to_numpy(float)
        pd_ = (g[f"{prefix}_lam_home"] - g[f"{prefix}_lam_away"]).to_numpy(float)
        yt = (g["home_score"] + g["away_score"]).to_numpy(float)
        ym = (g["home_score"] - g["away_score"]).to_numpy(float)
        slope = lambda x, y: float(np.cov(x, y)[0, 1] / np.var(x, ddof=1)) if np.var(x) > 0 else np.nan  # noqa: E731
        rows.append({"season": s, f"{prefix}_slope_total": slope(ps, yt), f"{prefix}_slope_margin": slope(pd_, ym), f"{prefix}_total_bias": float(ps.mean() - yt.mean())})
    return pd.DataFrame(rows).set_index("season")


def brier_gain(games: pd.DataFrame, challenger: str, incumbent: str = "V1") -> pd.Series:
    y = (games["home_score"] > games["away_score"]).astype(float)
    d = (games[f"{challenger}_p_home_win"] - y) ** 2 - (games[f"{incumbent}_p_home_win"] - y) ** 2
    return d.groupby(games["season"]).mean().rename(f"gain_{challenger}")


# ---------------------------------------------------------------------------------------------------------------------------------
# oracle tuning surfaces (diagnostic; uses the season's own outcomes; approximate win probability from independent Poisson goals)
# ---------------------------------------------------------------------------------------------------------------------------------
def _pois(lam: np.ndarray, k: int = MAXG) -> np.ndarray:
    ks = np.arange(k)
    lg = np.array([np.sum(np.log(np.arange(1, j + 1))) for j in ks])
    return np.exp(ks[None, :] * np.log(lam[:, None]) - lam[:, None] - lg[None, :])


def approx_brier(lh: np.ndarray, la: np.ndarray, hs: np.ndarray, as_: np.ndarray) -> float:
    """Brier of P(home wins) from independent Poisson goals with ties split evenly (an approximation of the simulator's overtime layer; used for SHAPE comparisons only)."""
    ph, pa = _pois(lh), _pois(la)
    cdf_a = np.cumsum(pa, axis=1)
    p_gt = np.sum(ph[:, 1:] * cdf_a[:, :-1], axis=1)
    p_tie = np.sum(ph * pa, axis=1)
    p = np.clip(p_gt + 0.5 * p_tie, 1e-6, 1 - 1e-6)
    return float(np.mean((p - (hs > as_)) ** 2))


def oracle_surface(season: int, lam_by_combo: dict[tuple[float, float], tuple[np.ndarray, np.ndarray]], hs: np.ndarray, as_: np.ndarray) -> dict[str, Any]:
    """Approximate Brier for every (half-life, prior) of the grid on the season itself, the best cell and the production cell."""
    surf = {f"{hl:g}|{pr:g}": approx_brier(lh, la, hs, as_) for (hl, pr), (lh, la) in lam_by_combo.items()}
    best = min(surf, key=lambda k: surf[k])
    prod = surf[f"{PRODUCTION[0]:g}|{PRODUCTION[1]:g}"]
    vals = np.array(list(surf.values()))
    return {"season": season, "surface": surf, "best_cell": best, "best_brier": surf[best], "production_brier": prod, "oracle_gain": surf[best] - prod,
            "range": float(vals.max() - vals.min()), "n_games": int(len(hs))}


def spearman(x: pd.Series, y: pd.Series) -> dict[str, float]:
    j = pd.concat([x, y], axis=1, join="inner").dropna()
    if len(j) < 5:
        return {"rho": float("nan"), "n": int(len(j))}
    return {"rho": float(j.iloc[:, 0].rank().corr(j.iloc[:, 1].rank())), "n": int(len(j))}


def relate(gain: pd.Series, features: pd.DataFrame) -> dict[str, Any]:
    """Spearman rank correlation of the per-season gain (negative = retune helps) with each feature measured in the same season and in the previous season."""
    out = {}
    for c in features.columns:
        out[c] = {"same_season": spearman(gain, features[c]), "previous_season": spearman(gain, features[c].shift(1))}
    return out


def main(argv: list[str] | None = None) -> int:
    import argparse
    import multiprocessing as mp

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.regime_analysis")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--data", default="docs/research/v1-retune/data")
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--no-oracle", action="store_true")
    a = ap.parse_args(argv)
    d = Path(a.data)
    oa = pd.concat([pd.read_csv(d / "oa_games_fresh2.csv.gz"), pd.read_csv(d / "oa_games_main.csv.gz")], ignore_index=True)
    v1r = pd.concat([pd.read_csv(d / "v1r_games_fresh2.csv.gz"), pd.read_csv(d / "v1r_games_main.csv.gz")], ignore_index=True)
    g = oa.merge(v1r.drop(columns=[c for c in v1r.columns if c in oa.columns and c != "game_id"]), on="game_id", how="left")
    stats = season_stats(g).join(team_strength_spread(g)).join(persistence(g)).join(schedule_stats(g)).join(calibration_drift(g, "V1"))
    gains = pd.concat([brier_gain(g, c) for c in ("V1_R", "V1_R_C1", "OA_SVA_C1")], axis=1)
    feat = stats.drop(columns=["n_games"])
    rel = {c: relate(gains[c], feat) for c in gains.columns}
    res: dict[str, Any] = {"per_season": stats.join(gains).reset_index().to_dict("records"), "relations": rel}
    if not a.no_oracle:
        from nhl_edge.data.history import load_nhl_games, load_team_games
        from nhl_edge.research import v1_tuned_control as T
        from nhl_edge.research.walk_forward import build_gamelog

        tg, ng = load_team_games(Path(a.history), None), load_nhl_games(Path(a.history), None)
        gamelog = build_gamelog(tg)
        fin = ng[(ng["game_type"] == 2) & ng["final"].astype(bool)].dropna(subset=["home_score", "away_score"]).sort_values(["game_date", "game_id"])
        T._SHARED.update({"gamelog": gamelog, "team_logs": {t: x for t, x in gamelog.groupby("team")}, "games": fin.reset_index(drop=True)})
        seasons = sorted(int(s) for s in g["season"].unique())

        def one(season: int) -> dict[str, Any]:
            gs = T._SHARED["games"]
            gs = gs[gs["season"] == season]
            keep = set(g.loc[g["season"] == season, "game_id"].astype(int))
            gs = gs[gs["game_id"].isin(keep)]
            combos = {}
            for hl in GRID_HL:
                for pr in GRID_PRIOR:
                    cache: dict = {}
                    lam = np.array([T._lams(x, hl, pr, T._SHARED["gamelog"], T._SHARED["team_logs"], cache) for x in gs.itertuples(index=False)])
                    combos[(hl, pr)] = (lam[:, 0], lam[:, 1])
            return oracle_surface(season, combos, gs["home_score"].to_numpy(float), gs["away_score"].to_numpy(float))

        with mp.get_context("fork").Pool(a.workers) as pool:
            res["oracle"] = pool.map(one, seasons)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "regime_analysis.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps({"seasons": len(stats), "oracle": "oracle" in res}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
