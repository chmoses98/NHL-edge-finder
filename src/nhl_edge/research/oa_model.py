"""Opponent-adjusted team strength (RESEARCH_ONLY challenger ``OA_RIDGE``).

DATA_ONLY_V1's ratings are *not* opponent-adjusted: each team's off/def xG per 60 is a recency-weighted average of its own
games, so a team that played a soft schedule looks better than it is, and the multiplicative ``off_A * def_B`` then
double-counts. This module replaces only that one component and nothing else (same simulator, home advantage, back-to-back
terms, finishing term and seeds), so any difference in a walk-forward comparison is attributable to the rating change.

Model, fit afresh at every prediction date from rows dated STRICTLY BEFORE it::

    rate_k = mu + h * is_home_k + a_{att(k)} + d_{def(k)} + e_k          (rate = per-60 xG or goals of the attacking side)

estimated by weighted ridge least squares. Row weight = minutes/60 * 0.5^(age_days / half_life) * season_discount^(seasons
back). The ridge pulls every ``a`` and ``d`` toward 0 (league average) with strength ``ridge`` expressed in pseudo-games, so
early-season and sparse teams are shrunk in proportion to how little they have played, and a team's schedule is controlled
for by construction (its opponents' ``a``/``d`` enter the same normal equations).

The three hyper-parameters (half-life, ridge, season discount) are chosen by :func:`select_hyperparameters` from games in
PRIOR seasons only. Nothing here reads a market, a result of the game being predicted, or any later row.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from nhl_edge.features.ratings import LeagueRates, TeamRating

# Candidate grid. Deliberately small and fixed in advance (see docs/research/oa-walk-forward/PREREGISTRATION.md).
GRID_HALF_LIFE_DAYS = (60.0, 120.0, 240.0, 480.0)
GRID_RIDGE = (1.0, 2.5, 5.0, 15.0, 30.0, 60.0)
GRID_SEASON_DISCOUNT = (0.1, 0.25, 0.4, 0.55, 0.7)
VALIDATION_SEASONS_BACK = 2
MAX_SEASONS_BACK = 3

TARGETS = {
    "xg": "xGoalsFor",                              # raw expected goals (what V1 uses, un-adjusted for opponent)
    "xg_sva": "scoreVenueAdjustedxGoalsFor",        # MoneyPuck score- and venue-adjusted xG
    "goals": "goalsFor",
}


@dataclass(frozen=True)
class OAConfig:
    half_life_days: float = 90.0
    ridge: float = 30.0
    season_discount: float = 0.7
    target: str = "xg_sva"
    goals_blend: float = 0.0          # weight on the goals-based rating (0 = pure xG)

    def key(self) -> tuple:
        return (self.half_life_days, self.ridge, self.season_discount, self.target, self.goals_blend)


@dataclass
class OAData:
    """Column-oriented view of regular-season 'all' team-game rows, sorted by (date, game)."""

    date: np.ndarray          # int YYYYMMDD
    day: np.ndarray           # days since epoch (for decay)
    season: np.ndarray
    att: np.ndarray           # attacking team index
    dfn: np.ndarray           # defending team index
    home: np.ndarray          # 1 if the attacker is the home side
    minutes: np.ndarray
    y: dict[str, np.ndarray]  # per-60 rates by target
    teams: list[str] = field(default_factory=list)
    game_id: np.ndarray | None = None

    @property
    def n_teams(self) -> int:
        return len(self.teams)


def build_oa_data(team_games: pd.DataFrame, teams: list[str] | None = None) -> OAData:
    d = team_games[(team_games["situation"] == "all") & (team_games["game_type"] == 2)].copy()
    d["team"] = d["team_abbrev"].where(d["team_abbrev"].notna(), d["mp_team"])
    d["opp"] = d["opp_abbrev"].where(d["opp_abbrev"].notna(), d["mp_opposing_team"])
    d = d.dropna(subset=["team", "opp", "iceTime"])
    d = d[d["iceTime"] > 0]
    d["date"] = d["game_date"].astype(str).str.replace("-", "").astype(int)
    d = d.sort_values(["date", "game_id"]).reset_index(drop=True)
    names = sorted(set(d["team"]) | set(d["opp"])) if teams is None else teams
    idx = {t: i for i, t in enumerate(names)}
    mins = d["iceTime"].to_numpy(float) / 60.0
    y = {k: pd.to_numeric(d[col], errors="coerce").to_numpy(float) / mins * 60.0 for k, col in TARGETS.items() if col in d.columns}
    day = (pd.to_datetime(d["date"].astype(str), format="%Y%m%d") - pd.Timestamp("1970-01-01")).dt.days.to_numpy(float)
    return OAData(date=d["date"].to_numpy(int), day=day, season=d["season"].to_numpy(int), att=d["team"].map(idx).to_numpy(int),
                  dfn=d["opp"].map(idx).to_numpy(int), home=(d["home"].astype(bool)).to_numpy(int), minutes=mins, y=y, teams=list(names),
                  game_id=d["game_id"].to_numpy(int))


@dataclass(frozen=True)
class OAFit:
    mu: float
    home_effect: float
    a: np.ndarray             # attack, rate units (per 60)
    d: np.ndarray             # defence (positive == concedes more)
    n_eff: np.ndarray         # effective weighted games per team (attacking rows)
    n_rows: int


def _solve(x_att, x_dfn, x_home, y, w, n_teams: int, ridge: float) -> OAFit:
    sw = w.sum()
    if sw <= 0:
        z = np.zeros(n_teams)
        return OAFit(mu=0.0, home_effect=0.0, a=z, d=z.copy(), n_eff=z.copy(), n_rows=0)
    # global mean and home effect (home/away are balanced, so the team terms do not confound them)
    hw = (w * x_home).sum()
    aw = sw - hw
    mean_home = (w * x_home * y).sum() / max(hw, 1e-9)
    mean_away = (w * (1 - x_home) * y).sum() / max(aw, 1e-9)
    mu = (mean_home + mean_away) / 2.0
    h = mean_home - mean_away  # rate difference; per-side effect is +/- h/2
    r = y - mu - (x_home - 0.5) * h
    n = n_teams
    daa = np.bincount(x_att, weights=w, minlength=n)
    ddd = np.bincount(x_dfn, weights=w, minlength=n)
    cross = np.zeros((n, n))
    np.add.at(cross, (x_att, x_dfn), w)
    g = np.zeros((2 * n, 2 * n))
    g[:n, :n] = np.diag(daa)
    g[n:, n:] = np.diag(ddd)
    g[:n, n:] = cross
    g[n:, :n] = cross.T
    g[np.diag_indices(2 * n)] += ridge
    b = np.concatenate([np.bincount(x_att, weights=w * r, minlength=n), np.bincount(x_dfn, weights=w * r, minlength=n)])
    theta = np.linalg.solve(g, b)
    return OAFit(mu=float(mu), home_effect=float(h), a=theta[:n], d=theta[n:], n_eff=daa, n_rows=int(len(y)))


def fit_oa(data: OAData, as_of: int, season: int, cfg: OAConfig) -> OAFit:
    """Ridge fit from rows with ``date < as_of``. ``as_of`` is YYYYMMDD."""
    m = (data.date < as_of) & (data.season >= season - MAX_SEASONS_BACK) & (data.season <= season)
    if not m.any():
        return _solve(np.zeros(0, int), np.zeros(0, int), np.zeros(0), np.zeros(0), np.zeros(0), data.n_teams, cfg.ridge)
    today = (pd.Timestamp(str(as_of)) - pd.Timestamp("1970-01-01")).days
    age = today - data.day[m]
    w = (data.minutes[m] / 60.0) * 0.5 ** (age / cfg.half_life_days) * cfg.season_discount ** (season - data.season[m])
    out = []
    for tgt, wt in (("goals", cfg.goals_blend), (cfg.target if cfg.target != "goals" else "goals", 1.0 - cfg.goals_blend)):
        if wt <= 0:
            continue
        y = data.y[tgt][m]
        ok = ~np.isnan(y)
        out.append((wt, _solve(data.att[m][ok], data.dfn[m][ok], data.home[m][ok].astype(float), y[ok], w[ok], data.n_teams, cfg.ridge)))
    if len(out) == 1:
        return out[0][1]
    # blend of rating vectors, each expressed relative to its own league mean: convert goals ratings to the xG scale by the mean ratio
    (w1, f1), (w2, f2) = out
    scale = f2.mu / f1.mu if f1.mu else 1.0
    return OAFit(mu=w1 * f1.mu * scale + w2 * f2.mu, home_effect=w1 * f1.home_effect * scale + w2 * f2.home_effect,
                 a=w1 * f1.a * scale + w2 * f2.a, d=w1 * f1.d * scale + w2 * f2.d, n_eff=f2.n_eff, n_rows=f2.n_rows)


def oa_team_ratings(fit: OAFit, data: OAData, home: str, away: str, league: LeagueRates, floor: float = 0.4) -> tuple[TeamRating, TeamRating]:
    """V1-compatible ``TeamRating`` objects (off/def in the league xG/60 scale) built from the opponent-adjusted effects.

    ``finish`` is left at 1.0 here; the walk-forward driver overwrites it with V1's own regressed finishing ratio so the
    comparison changes the rating component only."""
    idx = {t: i for i, t in enumerate(data.teams)}
    L = league.xg60
    scale = L / fit.mu if fit.mu else 1.0

    def one(t: str) -> TeamRating:
        i = idx.get(t)
        if i is None or fit.n_eff[i] <= 0:
            return TeamRating(team=t, off_xg60=L, def_xg60=L, finish=1.0, stop=1.0, games_used=0.0)
        return TeamRating(team=t, off_xg60=max(L + fit.a[i] * scale, floor * L), def_xg60=max(L + fit.d[i] * scale, floor * L), finish=1.0, stop=1.0,
                          games_used=float(fit.n_eff[i]))

    return one(home), one(away)


def goals_nll(fit_cache_lambda_h: np.ndarray, fit_cache_lambda_a: np.ndarray, gh: np.ndarray, ga: np.ndarray) -> float:
    """Poisson negative log-likelihood (mean per game) of the two teams' goals, dropping the constant log(y!) term."""
    lh = np.clip(fit_cache_lambda_h, 0.3, 8.0)
    la = np.clip(fit_cache_lambda_a, 0.3, 8.0)
    return float(np.mean((lh - gh * np.log(lh)) + (la - ga * np.log(la))))


def select_hyperparameters(data: OAData, train_games: pd.DataFrame, season: int, *, target: str = "xg_sva", goals_blend: float = 0.0,
                           grid: dict | None = None) -> tuple[OAConfig, pd.DataFrame]:
    """Pick (half-life, ridge, season discount) by Poisson goals log-likelihood on the games of the two seasons BEFORE ``season``,
    each game rated only from rows dated before it. ``train_games`` must contain only games from seasons < ``season``
    (columns: game_date, season, home_abbrev, away_abbrev, home_score, away_score). Returns the winner and the full grid."""
    g = grid or {}
    cands = list(itertools.product(g.get("half_life", GRID_HALF_LIFE_DAYS), g.get("ridge", GRID_RIDGE), g.get("discount", GRID_SEASON_DISCOUNT)))
    val = train_games[train_games["season"].between(season - VALIDATION_SEASONS_BACK, season - 1)]
    if val.empty:
        raise ValueError(f"no validation games before season {season}")
    assert int(val["season"].max()) < season
    league = _league_goals_per_team(data, val["game_date"].min())
    rows = []
    for hl, rg, dc in cands:
        cfg = OAConfig(half_life_days=hl, ridge=rg, season_discount=dc, target=target, goals_blend=goals_blend)
        lh, la, gh, ga = [], [], [], []
        for (vs, date), grp in val.groupby(["season", "game_date"], sort=True):
            fit = fit_oa(data, int(str(date).replace("-", "")), int(vs), cfg)
            for r in grp.itertuples(index=False):
                lam_h, lam_a = _lambda_from_fit(fit, data, r.home_abbrev, r.away_abbrev, league)
                lh.append(lam_h)
                la.append(lam_a)
                gh.append(r.home_score)
                ga.append(r.away_score)
        nll = goals_nll(np.array(lh), np.array(la), np.array(gh, float), np.array(ga, float))
        rows.append({"half_life_days": hl, "ridge": rg, "season_discount": dc, "val_goals_nll": nll, "n": len(gh)})
    tbl = pd.DataFrame(rows).sort_values("val_goals_nll").reset_index(drop=True)
    best = tbl.iloc[0]
    return OAConfig(half_life_days=float(best.half_life_days), ridge=float(best.ridge), season_discount=float(best.season_discount),
                    target=target, goals_blend=goals_blend), tbl


def _league_goals_per_team(data: OAData, first_val_date: str) -> float:
    cut = int(str(first_val_date).replace("-", ""))
    m = data.date < cut
    return float(np.nanmean(data.y["goals"][m])) if m.any() else 3.0


def _lambda_from_fit(fit: OAFit, data: OAData, home: str, away: str, league_g60: float) -> tuple[float, float]:
    """Goals-scale lambdas straight from the additive fit (used only for hyper-parameter selection, not for forecasts)."""
    idx = {t: i for i, t in enumerate(data.teams)}
    ih, ia = idx.get(home), idx.get(away)
    if ih is None or ia is None or fit.mu == 0:
        return league_g60, league_g60
    scale = league_g60 / fit.mu
    mu = fit.mu
    lam_h = (mu + fit.home_effect / 2 + fit.a[ih] + fit.d[ia]) * scale
    lam_a = (mu - fit.home_effect / 2 + fit.a[ia] + fit.d[ih]) * scale
    return lam_h, lam_a


class SlopeCalibrator:
    """Online, strictly-prior recalibration of the SUM and DIFFERENCE of the two expected-goal rates (the C1 idea of the earlier
    model-improvement work, applied to any arm).

    Totals were found over-spread (calibration slope ~0.37) and margins under-spread (~1.39) in V1: team differences carry real
    signal, total-goal differences carry almost none. Given the arm's own past predictions ``s = lam_h + lam_a``,
    ``d = lam_h - lam_a`` and the realised totals / margins of games dated BEFORE the one being predicted, fit
    ``y_total ~ m_s + b_s (s - m_s)`` and ``y_margin ~ m_d + b_d (d - m_d)`` (slope only; the mean level is not recalibrated, so
    the expected total stays where the arm put it), clip slopes to [lo, hi], and rebuild the two rates. Identity until
    ``burn_in`` prior games exist. Rows are committed only when the date advances, so same-day games never inform each other.
    """

    def __init__(self, burn_in: int = 300, lo: float = 0.2, hi: float = 2.0):
        self.burn_in, self.lo, self.hi = burn_in, lo, hi
        self._pending: list[tuple[float, float, float, float]] = []
        self._pending_date: str | None = None
        self._s: list[float] = []
        self._d: list[float] = []
        self._yt: list[float] = []
        self._ym: list[float] = []

    def _commit(self) -> None:
        for s, d, yt, ym in self._pending:
            self._s.append(s)
            self._d.append(d)
            self._yt.append(yt)
            self._ym.append(ym)
        self._pending = []

    def slopes(self, date: str) -> tuple[float, float]:
        if self._pending_date is not None and date > self._pending_date:
            self._commit()
            self._pending_date = None
        if len(self._s) < self.burn_in:
            return 1.0, 1.0
        s, d, yt, ym = (np.asarray(x, float) for x in (self._s, self._d, self._yt, self._ym))

        def slope(x: np.ndarray, y: np.ndarray) -> float:
            xc = x - x.mean()
            den = float((xc * xc).sum())
            return float(np.clip((xc * (y - y.mean())).sum() / den, self.lo, self.hi)) if den > 1e-12 else 1.0

        return slope(s, yt), slope(d, ym)

    def transform(self, date: str, lam_h: float, lam_a: float) -> tuple[float, float]:
        b_s, b_d = self.slopes(date)
        if len(self._s) < self.burn_in:
            return lam_h, lam_a
        m_s, m_d = float(np.mean(self._s)), float(np.mean(self._d))
        s, d = lam_h + lam_a, lam_h - lam_a
        s2, d2 = m_s + b_s * (s - m_s), m_d + b_d * (d - m_d)
        return max((s2 + d2) / 2.0, 0.3), max((s2 - d2) / 2.0, 0.3)

    def observe(self, date: str, lam_h: float, lam_a: float, total: float, margin: float) -> None:
        if self._pending_date is not None and date > self._pending_date:
            self._commit()
        self._pending_date = date
        self._pending.append((lam_h + lam_a, lam_h - lam_a, float(total), float(margin)))
