"""Build a PLAYER_SIM_V1 ``TeamRoster`` for one team in one game from point-in-time player profiles + deployment.

Deployment has three possible sources, in order of preference, and every player records which one was used:

* ``LINES_CONFIRMED`` tonight's DailyFaceoff line combinations sourced from warmups / morning skate
* ``LINES_PROJECTED``  DailyFaceoff lines from practice or projection
* ``RECENT_SHIFTS``    the player's own recent shift-derived shares and the team's recent shift co-ice (the only source
                       available to historical backtests: it is what was known before the game)

Line templates (share of the team's time in the state, and co-ice fractions) come from the historical median for the
slot (``SLOT_TEMPLATES``); they are blended with the player's own recent history, never used alone when history
exists. A player with no NHL history keeps position priors and is flagged ``PRIOR_HEAVY``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from nhl_edge.players.engine import ALL_STATES, ON_ICE_TEAMMATES, TeamRoster
from nhl_edge.players.features import LeaguePriors, PlayerBook, PlayerParams, PlayerProfile

# share of the team's state time by deployment slot (medians of 2021-23 regular-season shift data; see
# docs/research/PLAYER_SIM_V1.md): EV for forward lines / defence pairs, PP units, PK units.
EV_SLOT_SHARE = {"f1": 0.335, "f2": 0.300, "f3": 0.245, "f4": 0.180, "d1": 0.410, "d2": 0.345, "d3": 0.265}
PP_SLOT_SHARE = {"pp1": 0.62, "pp2": 0.30, None: 0.02}
PK_SLOT_SHARE = {"pk1": 0.50, "pk2": 0.40, None: 0.03}


@dataclass
class Deployment:
    """Tonight's slots for one team, keyed by NHL player id (from ``data.lines``)."""

    ev: dict[int, str] = field(default_factory=dict)  # f1..f4 / d1..d3
    pp: dict[int, str] = field(default_factory=dict)  # pp1 / pp2
    pk: dict[int, str] = field(default_factory=dict)  # pk1 / pk2
    out: set[int] = field(default_factory=set)  # listed on IR / out
    source: str = "RECENT_SHIFTS"
    updated_at_utc: str | None = None

    @classmethod
    def from_line_rows(cls, rows: list[dict[str, Any]], confirmed: bool) -> Deployment:
        d = cls(source="LINES_CONFIRMED" if confirmed else "LINES_PROJECTED")
        for r in rows:
            pid = r.get("player_id")
            if pid is None:
                continue
            cat, unit = r.get("category"), r.get("unit")
            if cat == "ev" and unit in EV_SLOT_SHARE:
                d.ev[int(pid)] = unit
            elif cat == "pp" and unit in ("pp1", "pp2"):
                d.pp[int(pid)] = unit
            elif cat == "pk" and unit in ("pk1", "pk2"):
                d.pk[int(pid)] = unit
            elif cat == "oi" or (r.get("injury_status") or "").lower() in ("out", "ir", "ltir"):
                d.out.add(int(pid))
            d.updated_at_utc = d.updated_at_utc or r.get("lines_updated_at_utc")
        return d


def _uniform_F(share: np.ndarray, k: float) -> np.ndarray:
    n = len(share)
    F = np.zeros((n, n))
    tot = share.sum()
    for i in range(n):
        rest = tot - share[i]
        if rest > 0:
            F[i] = k * share / rest
        F[i, i] = 0.0
    return np.clip(F, 0.0, 1.0)


def _lines_F(pids: list[int], dep: Deployment, state: str) -> np.ndarray | None:
    n = len(pids)
    F = np.zeros((n, n))
    if state == "ev":
        slots = [dep.ev.get(p) for p in pids]
        if sum(s is not None for s in slots) < 10:
            return None
        for i, si in enumerate(slots):
            for j, sj in enumerate(slots):
                if i == j or si is None or sj is None:
                    continue
                fi, fj = si[0], sj[0]
                if si == sj:
                    F[i, j] = 0.75 if fi == "f" else 0.80
                elif fi == "f" and fj == "d":
                    F[i, j] = EV_SLOT_SHARE[sj] / 1.02  # a forward shares ice with each pair about in proportion to its TOI
                elif fi == "d" and fj == "f":
                    F[i, j] = EV_SLOT_SHARE[sj] / 1.06
                elif fi == fj:
                    F[i, j] = 0.05
        return F
    units = dep.pp if state == "pp" else dep.pk
    if len(units) < 6:
        return None
    slots = [units.get(p) for p in pids]
    for i, si in enumerate(slots):
        for j, sj in enumerate(slots):
            if i != j and si is not None and sj is not None:
                F[i, j] = 0.80 if si == sj else 0.08
    return F


@dataclass
class RosterBuild:
    roster: TeamRoster
    profiles: dict[int, PlayerProfile]
    player_meta: dict[int, dict[str, Any]]


def build_roster(book: PlayerBook, team_id: int, abbrev: str, date_int: int, players: list[dict[str, Any]], F_obs: dict[str, np.ndarray] | None,
                 p_pp: float, p_sh: float, team_minutes: dict[str, float], season: int | None = None, deployment: Deployment | None = None,
                 params: PlayerParams | None = None) -> RosterBuild:
    """``players``: [{player_id, name, position}] dressed (or expected-to-dress) skaters, goalies excluded.
    ``F_obs``: output of :func:`features.coice_fractions` for exactly this player order, or None.
    ``team_minutes``: expected team minutes by state for this game (ev, pp, sh, ea, en, ot) for the TOI projection."""
    prm = params or book.params
    pri: LeaguePriors = book.priors
    dep = deployment or Deployment()
    pids = [int(p["player_id"]) for p in players]
    n = len(pids)
    profs = {pid: book.profile(pid, date_int, p.get("position"), season) for pid, p in zip(pids, players)}
    share = {s: np.array([profs[p].share[s] for p in pids]) for s in ALL_STATES}
    # blend in tonight's line template where a line source exists (history-weighted: 3 pseudo-games for the template)
    if dep.source != "RECENT_SHIFTS":
        w_t = 3.0 if dep.source == "LINES_CONFIRMED" else 1.5
        for i, p in enumerate(pids):
            hist = min(profs[p].n_games, 10) / 2.0
            ev_slot = dep.ev.get(p)
            if ev_slot:
                share["ev"][i] = (hist * share["ev"][i] + w_t * EV_SLOT_SHARE[ev_slot]) / (hist + w_t)
            share["pp"][i] = (hist * share["pp"][i] + w_t * PP_SLOT_SHARE.get(dep.pp.get(p), 0.02)) / (hist + w_t)
            share["sh"][i] = (hist * share["sh"][i] + w_t * PK_SLOT_SHARE.get(dep.pk.get(p), 0.03)) / (hist + w_t)
    w_goal = np.zeros((len(ALL_STATES), n))
    a1 = np.zeros((len(ALL_STATES), n))
    a2 = np.zeros((len(ALL_STATES), n))
    for i, p in enumerate(pids):
        pr = profs[p]
        fin = pr.finish if prm.use_finishing else 1.0
        rate = {"ev": pr.ixg60["ev"], "pp": pr.ixg60["pp"], "sh": pr.ixg60["sh"], "ea": pr.ixg60["ea"], "en": pr.en60 / max(fin, 1e-6), "ot": pr.ixg60["ev"]}
        for k, s in enumerate(ALL_STATES):
            w_goal[k, i] = max(share[s][i], 0.0) * max(rate[s], 0.0) * fin
            a1[k, i] = pr.a1[s]
            a2[k, i] = pr.a2[s]
    # co-ice: observed recent co-ice (rows with data), mixed 85/15 with the share-proportional uniform; tonight's lines
    # blended on top when available; rows without data use the uniform (or lines) alone
    F = np.zeros((3, n, n))
    for k, s in enumerate(("ev", "pp", "sh")):
        U = _uniform_F(np.maximum(share[s], 1e-4), ON_ICE_TEAMMATES[s])
        Fo = F_obs.get(s) if F_obs else None
        if Fo is not None:
            good = ~np.isnan(Fo).all(axis=1)
            Fm = np.where(good[:, None], 0.85 * np.nan_to_num(Fo) + 0.15 * U, U)
        else:
            Fm = U
        Fl = _lines_F(pids, dep, s) if dep.source != "RECENT_SHIFTS" else None
        if Fl is not None:
            wl = 0.6 if dep.source == "LINES_CONFIRMED" else 0.4
            Fm = wl * Fl + (1 - wl) * Fm
        np.fill_diagonal(Fm, 0.0)
        F[k] = Fm
    meta = {}
    for i, p in enumerate(pids):
        pr = profs[p]
        flags = list(pr.flags)
        if pr.last_team_id is not None and pr.last_team_id != team_id:
            flags.append("NEW_TEAM")
        if pr.n_games_season == 0 and pr.n_games > 0:
            flags.append("NO_CURRENT_SEASON_GAMES")
        if dep.source == "RECENT_SHIFTS":
            flags.append("ROLE_FROM_RECENT_SHIFTS")
        elif p not in dep.ev:
            flags.append("NOT_IN_TONIGHTS_LINES")
        if pr.n_games == 0:
            flags.append("PRIOR_HEAVY")
        exp_toi = {s: float(share[s][i] * team_minutes.get(s, 0.0)) for s in ALL_STATES}
        role_conf = "HIGH" if (dep.source == "LINES_CONFIRMED" and p in dep.ev and pr.n_games >= 20) else (
            "MEDIUM" if (pr.n_games >= 10 and "NEW_TEAM" not in flags) or (dep.source != "RECENT_SHIFTS" and p in dep.ev) else "LOW")
        quality = "FULL" if role_conf == "HIGH" and pr.n_games >= 40 else ("PRIOR_HEAVY" if pr.n_games < 10 else ("DEGRADED_ROLE" if role_conf == "LOW" else "STANDARD"))
        meta[p] = {"expected_toi_min": exp_toi, "expected_toi_total_min": float(sum(exp_toi.values())), "share": {s: float(share[s][i]) for s in ALL_STATES},
                   "ev_slot": dep.ev.get(p), "pp_unit": dep.pp.get(p), "pk_unit": dep.pk.get(p), "deployment_source": dep.source, "role_confidence": role_conf,
                   "projection_quality": quality, "uncertainty_flags": flags, "n_games": pr.n_games, "n_games_season": pr.n_games_season,
                   "ixg60": pr.ixg60, "finish": pr.finish, "a1": {s: pr.a1[s] for s in ("ev", "pp")}, "a2": {s: pr.a2[s] for s in ("ev", "pp")},
                   "expected_sog": float(sum(exp_toi[s] * (pr.sog60[s] if np.isfinite(pr.sog60.get(s, np.nan)) else pri.ixg60.get((pr.pos, s), 0) * 10) / 60.0
                                             for s in ("ev", "pp", "sh"))), "toi_recent_mean_min": pr.toi_mean_s / 60.0 if np.isfinite(pr.toi_mean_s) else None}
    sigma = np.array([prm.toi_sigma * (1.5 if "LOW" == meta[p]["role_confidence"] else 1.0) for p in pids])
    un = np.array([pri.unassisted.get(s, 0.06) for s in ALL_STATES])
    no2 = np.array([pri.no_a2.get(s, 0.2) for s in ALL_STATES])
    roster = TeamRoster(team_id, abbrev, np.array(pids, dtype=np.int64), [p.get("name") or str(p["player_id"]) for p in players],
                        [profs[p].pos for p in pids], w_goal, a1, a2, F, sigma, np.full(n, prm.p_early_exit), float(p_pp), float(p_sh), un, no2,
                        {"deployment_source": dep.source, "lines_updated_at_utc": dep.updated_at_utc})
    return RosterBuild(roster, profs, meta)


def team_pp_shares(pp_min_for: float, pp_min_against: float, pp_quality: float = 1.0, pk_quality_opp: float = 1.0,
                   league_ppmin: float = 4.3, base_pp: float = 0.215, base_sh: float = 0.028) -> tuple[float, float]:
    """Share of a team's non-empty-net regulation goals scored on the power play / short-handed, from tonight's
    expected penalty minutes and PP / PK quality ratios (1.0 = league). Odds-scaled so shares stay in (0, 1)."""
    r = max(pp_min_for / league_ppmin, 0.05) * max(pp_quality, 0.05) * max(pk_quality_opp, 0.05)
    pp = base_pp * r / (base_pp * r + (1 - base_pp))
    sh = base_sh * max(pp_min_against / league_ppmin, 0.05)
    return float(pp), float(min(sh, 0.08))
