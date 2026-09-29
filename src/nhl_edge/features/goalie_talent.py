"""Point-in-time goalie true talent + workload for nhl-features-2.0 (RESEARCH_ONLY; V1's goalie factor is untouched).

Input: goalie game logs derived from MoneyPuck shot rows (``goalie_game_log``): for every goalie appearance, the
xG of unblocked attempts he faced (empty-net attempts excluded, shootout excluded) and the goals he allowed on them.

True talent at date D (``GoalieTalent.factor``): only appearances dated STRICTLY BEFORE D, exponentially weighted by
appearance age (half-life ``HALF_LIFE_APPS`` appearances, so prior seasons carry in without a hard season reset),
then shrunk hard toward league average with a prior of ``prior_xg`` expected goals:

    factor = (sum w*GA + K*r) / (sum w*xGA + K) / r        (1.0 = league average; < 1 better)

with ``r`` the league GA/xGA over the same window. ``K`` is chosen on a VALIDATION season by out-of-sample Poisson
likelihood of goalie-game goals (``choose_prior``), never on the test seasons. A goalie's recent save percentage is
never used on its own: there is no hot-hand term.

Workload: ``b2b`` (the goalie also appeared the previous calendar day) and days of rest. The back-to-back
multiplier is estimated on the training seasons as observed GA over talent-adjusted expected GA for such starts,
shrunk toward 1.0.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import numpy as np
import pandas as pd

HALF_LIFE_APPS = 120.0
DEFAULT_PRIOR_XG = 250.0
B2B_SHRINK_XG = 300.0


def goalie_game_log(shots: pd.DataFrame, nhl_games: pd.DataFrame) -> pd.DataFrame:
    """One row per (game, goalie): date, defending team, xGA, GA, shots on goal faced, first-shot time, starter flag."""
    s = shots[(shots["goalieIdForShot"] > 0) & (shots["shotOnEmptyNet"] != 1) & (shots["period"].between(1, 4))].copy()
    s["def_home"] = 1 - s["isHomeTeam"]
    s["def_team"] = np.where(s["def_home"] == 1, s["homeTeamCode"].astype(str), s["awayTeamCode"].astype(str))
    g = s.groupby(["nhl_game_id", "goalieIdForShot"]).agg(
        season=("season", "first"), playoff=("isPlayoffGame", "first"), team=("def_team", "first"), def_home=("def_home", "first"),
        xga=("xGoal", "sum"), ga=("goal", "sum"), sog=("shotWasOnGoal", "sum"), first_t=("time", "min"), last_t=("time", "max"),
        name=("goalieNameForShot", "first")).reset_index().rename(columns={"nhl_game_id": "game_id", "goalieIdForShot": "goalie_id"})
    first = g.groupby(["game_id", "def_home"])["first_t"].transform("min")
    g["starter"] = (g["first_t"] == first).astype(int)
    dates = nhl_games.drop_duplicates("game_id").set_index("game_id")["game_date"].astype(str)
    g["game_date"] = g["game_id"].map(dates)
    g["name"] = g["name"].astype(str)
    g["team"] = g["team"].astype(str)
    g = g.dropna(subset=["game_date"])
    return g.sort_values(["game_date", "game_id", "goalie_id"]).reset_index(drop=True)


@dataclass(frozen=True)
class GoalieTalent:
    goalie_id: int
    factor: float
    apps_used: int
    xga_weighted: float
    ga_weighted: float
    rest_days: int | None
    b2b: bool
    workload_mult: float
    as_of: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class GoalieBook:
    """Fast point-in-time lookups over a goalie game log (regular season + playoffs both count as evidence)."""

    def __init__(self, log: pd.DataFrame, prior_xg: float = DEFAULT_PRIOR_XG, b2b_mult: float = 1.0, half_life: float = HALF_LIFE_APPS):
        self.log = log
        self.prior_xg = float(prior_xg)
        self.b2b_mult = float(b2b_mult)
        self.half_life = float(half_life)
        self.by_goalie = {int(k): d for k, d in log.groupby("goalie_id")}
        self._dates = log["game_date"].to_numpy().astype(str)
        self._cga = np.cumsum(log["ga"].to_numpy(dtype=float))
        self._cxga = np.cumsum(log["xga"].to_numpy(dtype=float))

    def league_ratio(self, as_of: str, window_days: int = 730) -> float:
        lo = str((pd.Timestamp(as_of) - pd.Timedelta(days=window_days)).date())
        i1 = int(np.searchsorted(self._dates, as_of, side="left"))
        i0 = int(np.searchsorted(self._dates, lo, side="left"))
        if i1 - i0 < 200:
            return 1.0
        ga = self._cga[i1 - 1] - (self._cga[i0 - 1] if i0 > 0 else 0.0)
        xga = self._cxga[i1 - 1] - (self._cxga[i0 - 1] if i0 > 0 else 0.0)
        return float(ga / xga) if xga > 0 else 1.0

    def talent(self, goalie_id: int | None, as_of: str, league_ratio: float | None = None) -> GoalieTalent:
        r = league_ratio if league_ratio is not None else self.league_ratio(as_of)
        d = self.by_goalie.get(int(goalie_id)) if goalie_id else None
        if d is None:
            return GoalieTalent(int(goalie_id or 0), 1.0, 0, 0.0, 0.0, None, False, 1.0, as_of)
        d = d[d["game_date"].astype(str) < as_of]
        if d.empty:
            return GoalieTalent(int(goalie_id), 1.0, 0, 0.0, 0.0, None, False, 1.0, as_of)
        w = 0.5 ** (np.arange(len(d))[::-1] / self.half_life)
        ga = float((d["ga"].to_numpy() * w).sum())
        xga = float((d["xga"].to_numpy() * w).sum())
        k = self.prior_xg
        factor = (ga + k * r) / (xga + k) / r
        last = pd.Timestamp(str(d["game_date"].iloc[-1]))
        rest = int((pd.Timestamp(as_of) - last).days)
        b2b = rest == 1
        wl = self.b2b_mult if b2b else 1.0
        return GoalieTalent(int(goalie_id), float(factor), int(len(d)), xga, ga, rest, b2b, wl, as_of)

    def factor(self, goalie_id: int | None, as_of: str, league_ratio: float | None = None) -> float:
        t = self.talent(goalie_id, as_of, league_ratio)
        return t.factor * t.workload_mult


def v1_style_factor(log: pd.DataFrame, goalie_id: int, season: int, prior_xg: float = 60.0) -> float:
    """What DATA_ONLY_V1 would use live: the goalie's PREVIOUS full MoneyPuck season, regressed GA/xGA (prior 60 xG)."""
    prev = log[(log["season"] == season - 1) & (log["playoff"] == 0)]
    tot_ga, tot_xga = float(prev["ga"].sum()), float(prev["xga"].sum())
    r = tot_ga / tot_xga if tot_xga > 0 else 1.0
    d = prev[prev["goalie_id"] == goalie_id]
    if d.empty:
        return 1.0
    return (float(d["ga"].sum()) + prior_xg * r) / (float(d["xga"].sum()) + prior_xg) / r


def choose_prior(log: pd.DataFrame, val_season: int, grid: tuple[float, ...] = (50, 100, 200, 300, 450, 700, 1000)) -> dict[str, Any]:
    """Out-of-sample Poisson log-likelihood of each validation-season goalie-game's GA given xGA x talent(as_of that
    game's date), for each prior strength. Returns the grid scores and the best K."""
    val = log[(log["season"] == val_season) & (log["playoff"] == 0) & (log["xga"] > 0)]
    scores = {}
    for k in grid:
        book = GoalieBook(log, prior_xg=k)
        cache: dict[str, float] = {}
        ll = 0.0
        for r in val.itertuples(index=False):
            lr = cache.setdefault(r.game_date, book.league_ratio(r.game_date))
            mu = max(r.xga * lr * book.talent(r.goalie_id, r.game_date, lr).factor, 1e-6)
            ll += r.ga * np.log(mu) - mu
        scores[str(k)] = round(float(ll), 3)
    base = sum(r.ga * np.log(max(r.xga, 1e-6)) - r.xga for r in val.itertuples(index=False))
    best = max(scores, key=lambda x: scores[x])
    return {"val_season": val_season, "n_games": int(len(val)), "loglik_by_prior_xg": scores, "loglik_xg_only_no_league_ratio": round(float(base), 3),
            "best_prior_xg": float(best)}


def estimate_b2b(log: pd.DataFrame, train_seasons: list[int], prior_xg: float) -> dict[str, Any]:
    """Observed / expected goals for starters on the second of consecutive days, expected = xGA x talent x league ratio."""
    book = GoalieBook(log, prior_xg=prior_xg)
    d = log[(log["season"].isin(train_seasons)) & (log["playoff"] == 0) & (log["starter"] == 1)]
    obs = exp = 0.0
    n = 0
    for r in d.itertuples(index=False):
        t = book.talent(r.goalie_id, r.game_date)
        if not t.b2b:
            continue
        lr = book.league_ratio(r.game_date)
        obs += r.ga
        exp += r.xga * lr * t.factor
        n += 1
    mult = (obs + B2B_SHRINK_XG) / (exp + B2B_SHRINK_XG)
    return {"n_b2b_starts": n, "observed_ga": obs, "expected_ga": round(exp, 2), "raw_ratio": round(obs / exp, 4) if exp else None,
            "b2b_mult": round(float(mult), 4), "shrink_xg": B2B_SHRINK_XG}
