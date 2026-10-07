"""Opponent-adjusted team strength (``nhl-oppadj-1.0``): regularised offense / defense effects, point in time.

WHAT IT IS. For one rate metric (5v5 expected goals, shot attempts, unblocked attempts, high-danger xG, shots on goal,
goals) every team-game row ``i`` (team ``t`` against opponent ``o``) contributes one observation, the team's rate for
per 60 minutes, modelled as

    rate_i = mu + OFF_t + DEF_o + eta * home_i + noise

fit by weighted ridge regression (``mu`` and ``eta`` unpenalised; ``OFF`` and ``DEF`` shrunk toward 0 with penalty
``RIDGE_HOURS`` -- the prior is worth ~15 games of 5v5 ice time). Weights are ice time (hours) x recency
(half-life ``HALF_LIFE_DAYS`` days) x ``PREV_SEASON_DISCOUNT`` for last-season games. A team's

    adjusted offense  = mu + OFF_t   (its rate against a league-average defense on neutral ice)
    adjusted defense  = mu + DEF_t   (the rate it allows to a league-average offense on neutral ice)
    adjusted share    = offense / (offense + defense)
    schedule effect   = raw rate - adjusted rate   (positive: the raw number was inflated by soft opponents)

are reported together with the RAW rate computed on exactly the same rows and weights, so the two are directly
comparable and the raw number is never overwritten.

POINT IN TIME. :func:`fit` uses only rows dated strictly before ``as_of``; callers pass the cutoff of the run. The
walk-forward check (``research/opponent_adjust_eval.py``) refits at each checkpoint on prior games only.

WHAT IT IS NOT. It does not feed DATA_ONLY_V1 (the production model is unchanged), it is not validated to VERIFIED, and
special teams are not adjusted (PP/PK samples are too small for a stable opponent model here). Capability status:
RESEARCH. Any number from this module is labelled ``OPPONENT_ADJUSTED`` with this version; raw numbers stay ``RAW``.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import date
from typing import Any

import numpy as np

OPP_ADJ_VERSION = "nhl-oppadj-1.0"
HALF_LIFE_DAYS = 60.0
PREV_SEASON_DISCOUNT = 0.6
RIDGE_HOURS = 12.0  # ~15 games x ~48 min of 5v5 ice time
MIN_ROWS = 10  # a team needs >= 10 games in the window to be rated at all
CURRENT_SEASON_FULL = 15  # below this many current-season games a rating is labelled PRIOR_HEAVY

#: metric -> (for column, against column, name, unit, higher offense is better)
METRICS: dict[str, tuple[str, str, str]] = {
    "xg": ("xgf", "xga", "expected goals"),
    "cf": ("cf", "ca", "shot attempts"),
    "ff": ("ff", "fa", "unblocked shot attempts"),
    "hdxg": ("hdxgf", "hdxga", "high-danger expected goals"),
    "sf": ("sf", "sa", "shots on goal"),
    "g": ("gf", "ga", "goals"),
}


@dataclass
class TeamAdj:
    team_id: int
    metric: str
    situation: str
    off_adj: float | None
    def_adj: float | None
    share_adj: float | None
    off_raw: float | None
    def_raw: float | None
    share_raw: float | None
    off_se: float | None
    def_se: float | None
    games: int
    games_current: int
    schedule_off: float | None  # raw - adjusted offense
    schedule_def: float | None
    status: str  # OK / PRIOR_HEAVY / INSUFFICIENT

    def to_dict(self) -> dict[str, Any]:
        r = lambda x, n=4: None if x is None else round(float(x), n)  # noqa: E731
        return {"team_id": self.team_id, "metric": self.metric, "situation": self.situation, "off_adj": r(self.off_adj), "def_adj": r(self.def_adj),
                "share_adj": r(self.share_adj), "off_raw": r(self.off_raw), "def_raw": r(self.def_raw), "share_raw": r(self.share_raw),
                "off_se": r(self.off_se), "def_se": r(self.def_se), "games": self.games, "games_current": self.games_current,
                "schedule_off": r(self.schedule_off), "schedule_def": r(self.schedule_def), "status": self.status}


@dataclass
class AdjFit:
    metric: str
    situation: str
    as_of: str
    mu: float | None
    home: float | None
    sigma: float | None
    n_rows: int
    teams: dict[int, TeamAdj] = field(default_factory=dict)
    version: str = OPP_ADJ_VERSION

    def rank(self, key: str, higher_is_better: bool = True) -> dict[int, int]:
        vals = [(t, getattr(a, key)) for t, a in self.teams.items() if getattr(a, key) is not None]
        vals.sort(key=lambda x: (-x[1] if higher_is_better else x[1], x[0]))
        return {t: i + 1 for i, (t, _) in enumerate(vals)}

    def predict(self, team_id: int, opp_id: int, home: bool) -> float | None:
        """Expected rate for ``team_id`` against ``opp_id`` (per 60)."""
        a, b = self.teams.get(team_id), self.teams.get(opp_id)
        if self.mu is None or a is None or b is None or a.off_adj is None or b.def_adj is None:
            return None
        return a.off_adj + b.def_adj - self.mu + (self.home or 0.0) * (0.5 if home else -0.5)


def _days(d: str) -> int:
    return date.fromisoformat(str(d)[:10]).toordinal()


def fit(rows: list[dict[str, Any]], *, as_of: str, season: int, metric: str = "xg", situation: str = "5on5",
        half_life_days: float = HALF_LIFE_DAYS, ridge_hours: float = RIDGE_HOURS) -> AdjFit:
    """Weighted ridge offense / defense effects from team-game rows dated strictly before ``as_of``.

    ``rows``: dicts with team_id, opp_team_id, home (bool), date (YYYY-MM-DD), season (int, start year), situation,
    toi (seconds) and the metric's for / against columns (``METRICS``). Only ``season`` and ``season - 1`` are used."""
    fcol, acol, _ = METRICS[metric]
    cut = _days(as_of)
    use = [r for r in rows if str(r.get("situation")) == situation and r.get("date") and _days(r["date"]) < cut
           and r.get("season") in (season, season - 1) and (r.get("toi") or 0) > 0 and r.get(fcol) is not None and r.get(acol) is not None
           and r.get("team_id") is not None and r.get("opp_team_id") is not None]
    teams = sorted({int(r["team_id"]) for r in use} | {int(r["opp_team_id"]) for r in use})
    out = AdjFit(metric, situation, as_of, None, None, None, len(use))
    if len(use) < 2 * MIN_ROWS or len(teams) < 4:
        return out
    ix = {t: i for i, t in enumerate(teams)}
    T = len(teams)
    n = len(use)
    # design: [mu, home, OFF_0..T-1, DEF_0..T-1]
    X = np.zeros((n, 2 + 2 * T))
    y = np.zeros(n)
    w = np.zeros(n)
    rec = np.zeros(n)
    for k, r in enumerate(use):
        hours = float(r["toi"]) / 3600.0
        y[k] = float(r[fcol]) / hours
        age = cut - _days(r["date"])
        rec[k] = 0.5 ** (age / half_life_days) * (1.0 if r["season"] == season else PREV_SEASON_DISCOUNT)
        w[k] = hours * rec[k]
        X[k, 0] = 1.0
        X[k, 1] = 0.5 if r.get("home") else -0.5
        X[k, 2 + ix[int(r["team_id"])]] = 1.0
        X[k, 2 + T + ix[int(r["opp_team_id"])]] = 1.0
    pen = np.full(2 + 2 * T, ridge_hours)
    pen[:2] = 0.0
    A = (X * w[:, None]).T @ X + np.diag(pen)
    beta = np.linalg.solve(A, (X * w[:, None]).T @ y)
    resid = y - X @ beta
    sigma2 = float((w * resid**2).sum() / max(w.sum(), 1e-9))
    try:
        cov = np.linalg.inv(A) * float((w * resid**2).sum() / max(n - 2 * T - 2, 1))
    except np.linalg.LinAlgError:
        cov = None
    mu, h = float(beta[0]), float(beta[1])
    out.mu, out.home, out.sigma = mu, h, math.sqrt(max(sigma2, 0.0))
    for t in teams:
        i = ix[t]
        mine = [k for k, r in enumerate(use) if int(r["team_id"]) == t]
        games = len(mine)
        cur = sum(1 for k in mine if use[k]["season"] == season)
        if games < MIN_ROWS:
            out.teams[t] = TeamAdj(t, metric, situation, None, None, None, None, None, None, None, None, games, cur, None, None, "INSUFFICIENT")
            continue
        wf = sum(rec[k] * float(use[k][fcol]) for k in mine)
        wa = sum(rec[k] * float(use[k][acol]) for k in mine)
        wh = sum(rec[k] * float(use[k]["toi"]) / 3600.0 for k in mine)
        off_raw, def_raw = wf / wh, wa / wh
        off_adj, def_adj = mu + float(beta[2 + i]), mu + float(beta[2 + T + i])
        se_o = math.sqrt(max(float(cov[2 + i, 2 + i]), 0.0)) if cov is not None else None
        se_d = math.sqrt(max(float(cov[2 + T + i, 2 + T + i]), 0.0)) if cov is not None else None
        out.teams[t] = TeamAdj(t, metric, situation, off_adj, def_adj, off_adj / (off_adj + def_adj) if off_adj + def_adj > 0 else None,
                               off_raw, def_raw, off_raw / (off_raw + def_raw) if off_raw + def_raw > 0 else None, se_o, se_d, games, cur,
                               off_raw - off_adj, def_raw - def_adj, "OK" if cur >= CURRENT_SEASON_FULL else "PRIOR_HEAVY")
    return out


def fit_all(rows: list[dict[str, Any]], *, as_of: str, season: int, situation: str = "5on5", metrics: tuple[str, ...] = ("xg", "cf", "ff", "hdxg", "sf", "g")) -> dict[str, AdjFit]:
    return {m: fit(rows, as_of=as_of, season=season, metric=m, situation=situation) for m in metrics}


def methodology() -> dict[str, Any]:
    return {"version": OPP_ADJ_VERSION, "model": "rate_for = mu + OFF_team + DEF_opponent + eta*home, weighted ridge",
            "weights": f"ice-time hours x 0.5^(days/{HALF_LIFE_DAYS:g}) x {PREV_SEASON_DISCOUNT} for last season", "ridge_hours": RIDGE_HOURS,
            "window": "current season + previous season, games strictly before the cutoff", "min_games": MIN_ROWS,
            "prior_heavy_below_current_games": CURRENT_SEASON_FULL, "situation": "5v5 (MoneyPuck situation 5on5)",
            "status": "RESEARCH: walk-forward sanity-checked (docs/research/opponent_adjustment), not validated to VERIFIED; not a DATA_ONLY_V1 input",
            "not_adjusted": ["power play / penalty kill rates", "save percentage", "player rates"]}
