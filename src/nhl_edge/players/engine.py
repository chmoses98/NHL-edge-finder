"""PLAYER_SIM_V1 joint player-event simulation, layered on one nhl-sim-2.0 draw.

The team simulator decides WHEN each team scores (half-minute steps, score-state x game-time hazards, OT). For every
simulated goal this module then draws, in order, from the hockey process underneath it:

1. **strength state** of the goal: EN (the opponent's net is empty) and EA (own net empty, extra attacker) from an
   estimated P(state | time bucket, own score differential) table -- late one-goal leads produce empty-net goals --
   otherwise PP / SH / EV from the team's special-teams expectation for THIS matchup (penalty minutes drawn and taken,
   PP and PK quality). OT goals are 3-on-3.
2. **scorer**: categorical over the team's dressed skaters with weight = share of the team's time in that state
   (deployment: line, PP unit, PK, empty-net duty) x shrunk individual xG per 60 in that state (shot creation and
   shot quality) x shrunk finishing, x this draw's ice-time multiplier for the player (game-to-game TOI noise and a
   small early-exit probability).
3. **primary assist**: the goal is unassisted with the league rate for that state; otherwise categorical over
   teammates with weight = expected share of the SCORER's state time spent with that teammate (co-ice from recent
   shift charts or tonight's line combinations) x the teammate's shrunk P(A1 | on ice for a teammate's goal).
4. **secondary assist**: none with the league rate given an A1; otherwise categorical over the remaining teammates with
   weight = mean co-ice with the scorer and the A1 x shrunk P(A2 | on ice).

Consequences, all by construction and tested: per draw, a team's player goals sum EXACTLY to its non-shootout goals;
nobody assists his own goal or is credited twice on one goal; at most two assists per goal; opponents never
assist; points = goals + assists; every ladder is monotone; shootout goals create no player statistics; the same draw
drives team totals, moneyline, player props and the goalie's goals against, so same-game outcomes are correlated
exactly as the simulated game makes them. The first goal of each draw (earliest step; ties within a half-minute step
broken uniformly) gives first-goal-scorer and team-to-score-first probabilities from simulated event ORDER, not from
normalised anytime probabilities.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from nhl_edge.sim.engine_v2 import SimV2Result

REG_STATES = ("ev", "pp", "sh", "ea", "en")
ALL_STATES = ("ev", "pp", "sh", "ea", "en", "ot")
S_IDX = {s: i for i, s in enumerate(ALL_STATES)}
F_STATE = {"ev": 0, "pp": 1, "sh": 2, "ea": 0, "en": 0, "ot": 0}  # which co-ice matrix a state uses
ON_ICE_TEAMMATES = {"ev": 4.0, "pp": 4.0, "sh": 3.0}


@dataclass
class TeamRoster:
    team_id: int
    abbrev: str
    player_ids: np.ndarray  # (n,)
    names: list[str]
    pos: list[str]
    w_goal: np.ndarray  # (6, n) unnormalised scorer weight by ALL_STATES
    a1: np.ndarray  # (6, n)
    a2: np.ndarray  # (6, n)
    F: np.ndarray  # (3, n, n) co-ice fractions (ev, pp, sh); row = scorer, diagonal 0
    toi_sigma: np.ndarray  # (n,)
    p_exit: np.ndarray  # (n,)
    p_pp: float  # share of this team's non-empty-net, non-extra-attacker regulation goals scored on the PP
    p_sh: float
    unassisted: np.ndarray  # (6,) by ALL_STATES
    no_a2: np.ndarray  # (6,)
    meta: dict[str, Any] = field(default_factory=dict)

    @property
    def n(self) -> int:
        return int(len(self.player_ids))


@dataclass
class StrengthTable:
    """P(goal is EN) and P(goal is EA) by (time bucket, scoring team's own differential before the goal)."""

    time_edges: tuple[float, ...]
    diffs: tuple[int, ...]
    p_en: np.ndarray  # (n_buckets, n_diffs)
    p_ea: np.ndarray

    def to_dict(self) -> dict[str, Any]:
        return {"time_edges": list(self.time_edges), "diffs": list(self.diffs), "p_en": self.p_en.round(5).tolist(), "p_ea": self.p_ea.round(5).tolist()}

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> StrengthTable:
        return cls(tuple(d["time_edges"]), tuple(d["diffs"]), np.asarray(d["p_en"], float), np.asarray(d["p_ea"], float))


@dataclass
class TeamDraws:
    goals: np.ndarray  # (n_sims, n) int16
    a1: np.ndarray
    a2: np.ndarray
    toi_mult: np.ndarray  # (n_sims, n) float32
    goal_state_counts: dict[str, float]  # mean goals per game by state (diagnostic)
    # per-draw goals by strength state (n_sims, len(ALL_STATES)) int16; retained for the game-script layer
    # (nhl_edge.thesis). Counting draws nothing from the generator, so every other array is unchanged.
    state_goals: np.ndarray | None = None

    @property
    def assists(self) -> np.ndarray:
        return self.a1 + self.a2

    @property
    def points(self) -> np.ndarray:
        return self.goals + self.a1 + self.a2


@dataclass
class PlayerSimResult:
    home: TeamDraws
    away: TeamDraws
    home_roster: TeamRoster
    away_roster: TeamRoster
    first_scorer: np.ndarray  # (n_sims,) player id, 0 = no goal (0-0 through OT; a shootout creates no goal scorer)
    first_team: np.ndarray  # (n_sims,) team id, 0 = none
    # goals against each team's goalie position (non-empty-net opponent goals incl. OT) and their times (minutes)
    ga_home: np.ndarray  # goals against the HOME goalie
    ga_away: np.ndarray
    ga_times_home: list[np.ndarray]  # per draw, sorted minutes of goals against the home goalie
    ga_times_away: list[np.ndarray]
    n_sims: int
    seed: int

    def team(self, team_id: int) -> tuple[TeamDraws, TeamRoster]:
        if team_id == self.home_roster.team_id:
            return self.home, self.home_roster
        if team_id == self.away_roster.team_id:
            return self.away, self.away_roster
        raise KeyError(team_id)

    def player(self, player_id: int) -> tuple[TeamDraws, TeamRoster, int] | None:
        for d, r in ((self.home, self.home_roster), (self.away, self.away_roster)):
            hit = np.nonzero(r.player_ids == player_id)[0]
            if len(hit):
                return d, r, int(hit[0])
        return None


def _bucket(edges: np.ndarray, t_mid: np.ndarray) -> np.ndarray:
    return np.clip(np.searchsorted(edges, t_mid, side="right") - 1, 0, len(edges) - 2)


def _events(steps: np.ndarray, opp_steps: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """(draw, step, own_diff_before_step) for every goal, one row per goal (a 2-goal step appears twice)."""
    own_before = np.cumsum(steps, axis=1, dtype=np.int16) - steps
    opp_before = np.cumsum(opp_steps, axis=1, dtype=np.int16) - opp_steps
    d, s = np.nonzero(steps)
    cnt = steps[d, s].astype(np.int64)
    rep = np.repeat(np.arange(len(d)), cnt)
    d, s = d[rep], s[rep]
    diff = (own_before[d, s] - opp_before[d, s]).astype(np.int64)
    return d, s, diff


def _sample_rows(rng: np.random.Generator, w: np.ndarray) -> np.ndarray:
    """One categorical draw per row of non-negative weights; -1 where a row has no mass."""
    tot = w.sum(axis=1)
    c = np.cumsum(w, axis=1)
    u = rng.random(len(w)) * tot
    idx = (c < u[:, None]).sum(axis=1)
    idx = np.minimum(idx, w.shape[1] - 1)
    return np.where(tot > 0, idx, -1)


def _allocate(rng: np.random.Generator, roster: TeamRoster, draw: np.ndarray, state: np.ndarray, mult: np.ndarray, n_sims: int) -> tuple[np.ndarray, ...]:
    n = roster.n
    m = len(draw)
    W = roster.w_goal[state] * mult[draw]
    scorer = _sample_rows(rng, W)
    # a goal whose state has no weight anywhere (e.g. nobody with SH history) falls back to EV weights
    miss = scorer < 0
    if miss.any():
        scorer[miss] = _sample_rows(rng, roster.w_goal[np.zeros(miss.sum(), dtype=int)] * mult[draw[miss]])
    fidx = np.array([F_STATE[ALL_STATES[s]] for s in range(len(ALL_STATES))])[state]
    rows = roster.F[fidx, scorer]  # (m, n)
    assisted = rng.random(m) >= roster.unassisted[state]
    W1 = rows * roster.a1[state] * mult[draw]
    W1[np.arange(m), scorer] = 0.0
    a1 = np.where(assisted, _sample_rows(rng, W1), -1)
    has1 = a1 >= 0
    second = has1 & (rng.random(m) >= roster.no_a2[state])
    rows2 = 0.5 * (rows + roster.F[fidx, np.where(has1, a1, scorer)])
    W2 = rows2 * roster.a2[state] * mult[draw]
    W2[np.arange(m), scorer] = 0.0
    W2[np.arange(m), np.where(has1, a1, scorer)] = 0.0
    a2 = np.where(second, _sample_rows(rng, W2), -1)
    G = np.zeros(n_sims * n, dtype=np.int16)
    A1 = np.zeros(n_sims * n, dtype=np.int16)
    A2 = np.zeros(n_sims * n, dtype=np.int16)
    np.add.at(G, draw * n + scorer, 1)
    ok1 = a1 >= 0
    np.add.at(A1, draw[ok1] * n + a1[ok1], 1)
    ok2 = a2 >= 0
    np.add.at(A2, draw[ok2] * n + a2[ok2], 1)
    return G.reshape(n_sims, n), A1.reshape(n_sims, n), A2.reshape(n_sims, n), scorer, a1, a2


def _mult(rng: np.random.Generator, roster: TeamRoster, n_sims: int) -> np.ndarray:
    z = rng.standard_normal((n_sims, roster.n)) * roster.toi_sigma[None, :]
    m = np.exp(z - 0.5 * roster.toi_sigma[None, :] ** 2)
    exit_ = rng.random((n_sims, roster.n)) < roster.p_exit[None, :]
    m = np.where(exit_, m * rng.random((n_sims, roster.n)), m)
    return m.astype(np.float64)


def simulate_players(res: SimV2Result, home: TeamRoster, away: TeamRoster, strength: StrengthTable, seed: int) -> PlayerSimResult:
    if res.home_steps is None or res.away_steps is None or res.ot_goal is None:
        raise ValueError("PLAYER_SIM_V1 needs an nhl-sim-2.0 result simulated with record_steps=True")
    rng = np.random.default_rng(seed)
    n_sims = res.n_sims
    step_min = res.step_min
    edges = np.asarray(strength.time_edges, float)
    dmin, dmax = min(strength.diffs), max(strength.diffs)
    out = {}
    order_keys = []
    ga_events = {"home": [], "away": []}
    for side, roster, steps, opp in (("home", home, res.home_steps, res.away_steps), ("away", away, res.away_steps, res.home_steps)):
        d, s, diff = _events(steps, opp)
        b = _bucket(edges, (s + 0.5) * step_min)
        di = np.clip(diff, dmin, dmax) - dmin
        u = rng.random(len(d))
        pen, pea = strength.p_en[b, di], strength.p_ea[b, di]
        rest = 1.0 - pen - pea
        st = np.full(len(d), S_IDX["ev"])
        st[u < pen] = S_IDX["en"]
        st[(u >= pen) & (u < pen + pea)] = S_IDX["ea"]
        u2 = (u - pen - pea) / np.maximum(rest, 1e-9)
        normal = u >= pen + pea
        st[normal & (u2 < roster.p_pp)] = S_IDX["pp"]
        st[normal & (u2 >= roster.p_pp) & (u2 < roster.p_pp + roster.p_sh)] = S_IDX["sh"]
        t = s * step_min + rng.random(len(d)) * step_min
        # overtime goal (3-on-3): the draws where OT was decided by a goal and this team won
        won = (res.home_final > res.away_final) if side == "home" else (res.away_final > res.home_final)
        otd = np.nonzero(res.ot_goal & won)[0]
        d = np.concatenate([d, otd])
        st = np.concatenate([st, np.full(len(otd), S_IDX["ot"])])
        t = np.concatenate([t, 60.0 + rng.random(len(otd)) * 5.0])
        mult = _mult(rng, roster, n_sims)
        G, A1, A2, scorer, _, _ = _allocate(rng, roster, d, st, mult, n_sims)
        counts = {ALL_STATES[i]: float((st == i).sum() / n_sims) for i in range(len(ALL_STATES))}
        sg = np.bincount(d * len(ALL_STATES) + st, minlength=n_sims * len(ALL_STATES)).reshape(n_sims, len(ALL_STATES)).astype(np.int16)
        out[side] = TeamDraws(G, A1, A2, mult.astype(np.float32), counts, sg)
        order_keys.append((d, t, roster.player_ids[scorer], np.full(len(d), roster.team_id)))
        # goals against the OTHER team's goalie: every goal except those into an empty net
        against = "away" if side == "home" else "home"
        keep = st != S_IDX["en"]
        ga_events[against].append((d[keep], t[keep]))
    # first goal of the game: earliest simulated time across both teams
    D = np.concatenate([k[0] for k in order_keys])
    T = np.concatenate([k[1] for k in order_keys])
    P = np.concatenate([k[2] for k in order_keys])
    TM = np.concatenate([k[3] for k in order_keys])
    first_scorer = np.zeros(n_sims, dtype=np.int64)
    first_team = np.zeros(n_sims, dtype=np.int64)
    if len(D):
        o = np.lexsort((T, D))
        D, T, P, TM = D[o], T[o], P[o], TM[o]
        firsts = np.r_[True, D[1:] != D[:-1]]
        first_scorer[D[firsts]] = P[firsts]
        first_team[D[firsts]] = TM[firsts]
    ga = {}
    ga_times = {}
    for side in ("home", "away"):
        dd = np.concatenate([e[0] for e in ga_events[side]]) if ga_events[side] else np.zeros(0, dtype=int)
        tt = np.concatenate([e[1] for e in ga_events[side]]) if ga_events[side] else np.zeros(0)
        ga[side] = np.bincount(dd, minlength=n_sims).astype(np.int16)
        o = np.lexsort((tt, dd))
        dd, tt = dd[o], tt[o]
        splits = np.searchsorted(dd, np.arange(n_sims + 1))
        ga_times[side] = [tt[splits[i]:splits[i + 1]] for i in range(n_sims)]
    return PlayerSimResult(out["home"], out["away"], home, away, first_scorer, first_team, ga["home"], ga["away"], ga_times["home"],
                           ga_times["away"], n_sims, seed)


def invariant_violations(res: SimV2Result, ps: PlayerSimResult) -> list[str]:
    """Coherence checks run on every simulation (reported, never repaired)."""
    out = []
    nonso_home = res.home_final - ((res.home_final > res.away_final) & res.shootout)
    nonso_away = res.away_final - ((res.away_final > res.home_final) & res.shootout)
    if not np.array_equal(ps.home.goals.sum(axis=1), nonso_home):
        out.append("home player goals != home non-shootout goals")
    if not np.array_equal(ps.away.goals.sum(axis=1), nonso_away):
        out.append("away player goals != away non-shootout goals")
    for side, d in (("home", ps.home), ("away", ps.away)):
        if (d.a1.sum(axis=1) > d.goals.sum(axis=1)).any() or (d.a2.sum(axis=1) > d.a1.sum(axis=1)).any():
            out.append(f"{side}: more primary assists than goals or more secondary than primary")
        if (d.goals < 0).any() or (d.a1 < 0).any() or (d.a2 < 0).any():
            out.append(f"{side}: negative counts")
    return out
