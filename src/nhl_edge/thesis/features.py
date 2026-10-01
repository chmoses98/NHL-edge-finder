"""Per-draw game features: the interpretable quantities every game script and thesis event is defined from.

Two constructors produce the SAME structure:

* :meth:`DrawFeatures.from_simulation` reads one joint draw (``SimV2Result`` + ``PlayerSimResult`` + both nets'
  ``SavesDraws``) -- arrays of length ``n_sims``;
* :meth:`DrawFeatures.from_actual` reads one official final game (results row + official goal events + goalie lines)
  -- arrays of length 1, so the postmortem evaluates the realised game with exactly the functions the pregame
  analysis used.

Conventions: "goals" are non-shootout goals (regulation + overtime; a shootout creates no goal); ``*_final`` is the
official score incl. the shootout winner's +1 (what moneyline / spread / total contracts settle on). Shots on goal
for a team = shots faced by the opponent's net (every goalie who played it) + the team's empty-net goals.
"""

from __future__ import annotations

from dataclasses import dataclass, fields
from typing import Any

import numpy as np

from nhl_edge.players.engine import S_IDX

TIGHT_CHECK_MIN = 55.0  # "late tight": within one goal at 55:00 of regulation


@dataclass
class DrawFeatures:
    home_abbrev: str
    away_abbrev: str
    home_team_id: int
    away_team_id: int
    home_goals: np.ndarray  # non-shootout goals
    away_goals: np.ndarray
    home_final: np.ndarray  # incl. shootout winner +1
    away_final: np.ndarray
    home_reg: np.ndarray
    away_reg: np.ndarray
    ot: np.ndarray  # bool: went past regulation
    so: np.ndarray  # bool: decided in a shootout
    home_net_faced: np.ndarray  # shots on goal against the home net (all goalies)
    away_net_faced: np.ndarray
    home_pp: np.ndarray  # power-play goals scored by home
    away_pp: np.ndarray
    home_en: np.ndarray  # empty-net goals scored by home
    away_en: np.ndarray
    first_team: np.ndarray  # +1 home scored first, -1 away, 0 no goal before the shootout
    home_max_deficit: np.ndarray  # largest regulation deficit home faced (>= 0)
    away_max_deficit: np.ndarray
    tight_late: np.ndarray  # bool: |margin| <= 1 at 55:00
    home_saves: np.ndarray | None = None  # the projected STARTER's saves (after replacement), sim only
    away_saves: np.ndarray | None = None

    @property
    def n(self) -> int:
        return int(len(self.home_goals))

    # ---- derived ------------------------------------------------------------------------------------------
    @property
    def total(self) -> np.ndarray:
        return self.home_goals + self.away_goals

    @property
    def final_margin(self) -> np.ndarray:
        return self.home_final - self.away_final

    @property
    def reg_margin(self) -> np.ndarray:
        return self.home_reg - self.away_reg

    @property
    def winner(self) -> np.ndarray:
        """+1 home, -1 away (a game always has a winner)."""
        return np.sign(self.final_margin).astype(np.int8)

    @property
    def home_shots(self) -> np.ndarray:
        return self.away_net_faced + self.home_en

    @property
    def away_shots(self) -> np.ndarray:
        return self.home_net_faced + self.away_en

    @property
    def home_shot_share(self) -> np.ndarray:
        h, a = self.home_shots.astype(float), self.away_shots.astype(float)
        return np.divide(h, h + a, out=np.full(len(h), 0.5), where=(h + a) > 0)

    def side(self, home: bool) -> dict[str, Any]:
        """Team-perspective view (for/against) so event definitions are written once for both teams."""
        if home:
            return {"abbrev": self.home_abbrev, "goals": self.home_goals, "opp_goals": self.away_goals, "final": self.home_final, "opp_final": self.away_final,
                    "shots": self.home_shots, "opp_shots": self.away_shots, "net_faced": self.home_net_faced, "pp": self.home_pp, "en": self.home_en,
                    "max_deficit": self.home_max_deficit, "win": self.winner == 1, "first": self.first_team == 1, "saves": self.home_saves}
        return {"abbrev": self.away_abbrev, "goals": self.away_goals, "opp_goals": self.home_goals, "final": self.away_final, "opp_final": self.home_final,
                "shots": self.away_shots, "opp_shots": self.home_shots, "net_faced": self.away_net_faced, "pp": self.away_pp, "en": self.away_en,
                "max_deficit": self.away_max_deficit, "win": self.winner == -1, "first": self.first_team == -1, "saves": self.away_saves}

    def subset(self, idx: np.ndarray) -> DrawFeatures:
        kw = {}
        for f in fields(self):
            v = getattr(self, f.name)
            kw[f.name] = v[idx] if isinstance(v, np.ndarray) else v
        return DrawFeatures(**kw)

    # ---- constructors -------------------------------------------------------------------------------------
    @classmethod
    def from_simulation(cls, res: Any, ps: Any, saves_home: Any, saves_away: Any, home_abbrev: str, away_abbrev: str) -> DrawFeatures:
        """``res``: SimV2Result simulated with ``record_steps=True``; ``ps``: PlayerSimResult of the same draw;
        ``saves_home`` / ``saves_away``: SavesDraws of the HOME / AWAY net."""
        if res.home_steps is None or ps.home.state_goals is None:
            raise ValueError("thesis features need per-step goals (record_steps=True) and per-draw strength-state goals")
        n = res.n_sims
        hid, aid = ps.home_roster.team_id, ps.away_roster.team_id
        so = np.asarray(res.shootout, bool)
        hf, af = np.asarray(res.home_final, np.int64), np.asarray(res.away_final, np.int64)
        hg = hf - ((hf > af) & so)
        ag = af - ((af > hf) & so)
        diff = np.cumsum(res.home_steps.astype(np.int16) - res.away_steps.astype(np.int16), axis=1)
        k = int(round(TIGHT_CHECK_MIN / res.step_min))
        ft = np.where(ps.first_team == hid, 1, np.where(ps.first_team == aid, -1, 0)).astype(np.int8)
        return cls(home_abbrev, away_abbrev, int(hid), int(aid), hg, ag, hf, af, np.asarray(res.home_reg, np.int64), np.asarray(res.away_reg, np.int64),
                   np.asarray(res.overtime, bool), so, np.asarray(saves_home.net_shots_faced, np.int64), np.asarray(saves_away.net_shots_faced, np.int64),
                   ps.home.state_goals[:, S_IDX["pp"]].astype(np.int64), ps.away.state_goals[:, S_IDX["pp"]].astype(np.int64),
                   ps.home.state_goals[:, S_IDX["en"]].astype(np.int64), ps.away.state_goals[:, S_IDX["en"]].astype(np.int64), ft,
                   np.maximum(0, -diff.min(axis=1)).astype(np.int64) if n else np.zeros(0, np.int64),
                   np.maximum(0, diff.max(axis=1)).astype(np.int64) if n else np.zeros(0, np.int64),
                   np.abs(diff[:, k - 1]) <= 1 if n else np.zeros(0, bool),
                   np.asarray(saves_home.saves, np.int64), np.asarray(saves_away.saves, np.int64))

    @classmethod
    def from_actual(cls, result: dict[str, Any], goals: list[dict[str, Any]], goalies: list[dict[str, Any]], home_abbrev: str, away_abbrev: str) -> DrawFeatures:
        """One official final game. ``result``: a ``results`` row (home/away final + regulation, last period type);
        ``goals``: official goal events (``player_events/goals`` rows: team_id, period, period_type, t_s [game seconds],
        strength, empty_net); ``goalies``: official goalie lines (team_id, shots_against, saves)."""
        hid, aid = int(result["home_team_id"]), int(result["away_team_id"])
        g = [x for x in goals if str(x.get("period_type") or "") != "SO" and int(x.get("period") or 0) <= 4]
        g.sort(key=lambda x: (int(x.get("period") or 0), float(x.get("t_s") or 0)))
        hg = sum(1 for x in g if int(x["team_id"]) == hid)
        ag = sum(1 for x in g if int(x["team_id"]) == aid)
        lpt = str(result.get("last_period_type") or "REG")
        so = lpt == "SO"
        ot = lpt in ("OT", "SO")
        cur = 0
        hmin = amax = 0
        tight = None
        for x in g:
            t_min = float(x.get("t_s") or 0) / 60.0
            if tight is None and t_min >= TIGHT_CHECK_MIN:
                tight = abs(cur) <= 1
            if int(x.get("period") or 0) <= 3:
                cur += 1 if int(x["team_id"]) == hid else -1
                hmin, amax = min(hmin, cur), max(amax, cur)
        if tight is None:
            tight = abs(cur) <= 1  # no goal at or after 55:00: the final regulation state is the 55:00 state
        first = 0
        if g:
            first = 1 if int(g[0]["team_id"]) == hid else -1
        pp = lambda tid: sum(1 for x in g if int(x["team_id"]) == tid and str(x.get("strength") or "").upper() == "PP")  # noqa: E731
        en = lambda tid: sum(1 for x in g if int(x["team_id"]) == tid and bool(x.get("empty_net")))  # noqa: E731
        faced = lambda tid: sum(int(x.get("shots_against") or 0) for x in goalies if int(x["team_id"]) == tid)  # noqa: E731
        sv = lambda tid: max([int(x.get("saves") or 0) for x in goalies if int(x["team_id"]) == tid and x.get("starter")] or [0])  # noqa: E731
        a = lambda v, dt=np.int64: np.asarray([v], dtype=dt)  # noqa: E731
        return cls(home_abbrev, away_abbrev, hid, aid, a(hg), a(ag), a(int(result["home_final"])), a(int(result["away_final"])), a(int(result.get("home_reg", hg))),
                   a(int(result.get("away_reg", ag))), a(ot, bool), a(so, bool), a(faced(hid)), a(faced(aid)), a(pp(hid)), a(pp(aid)), a(en(hid)), a(en(aid)),
                   a(first, np.int8), a(max(0, -hmin)), a(max(0, amax)), a(bool(tight), bool), a(sv(hid)), a(sv(aid)))
