"""Thesis events: named binary statements about the game that a bet can depend on.

A thesis is something a bettor would say ("PIT offense succeeds", "TOR is held to few shots", "it goes to overtime").
Each is a deterministic event on :class:`DrawFeatures`, so its probability, its relationship with every contract, and
whether it actually happened (postmortem) are all computed by the same rule. ``category`` groups near-synonyms so a
secondary thesis is a genuinely different idea from the primary one.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from nhl_edge.thesis.features import DrawFeatures
from nhl_edge.thesis.scripts import (
    CONTROL_SHARE,
    ENV_HIGH_MIN,
    ENV_LOW_MAX,
    PP_DRIVEN_MIN_GOALS,
    VOLUME_HIGH_MIN,
    VOLUME_LOW_MAX,
)

OFFENSE_MIN_GOALS = 4  # "offense succeeds": the team scores 4+ non-shootout goals
SUPPRESSED_MAX_GOALS = 2  # "offense suppressed": 2 or fewer


@dataclass(frozen=True)
class ThesisEvent:
    key: str  # stable id, e.g. "PIT:OFFENSE_4PLUS"
    label: str  # human text
    category: str  # result | offense | suppression | environment | control | volume | steal | shape | special | order
    team: str | None
    mask: np.ndarray

    @property
    def p(self) -> float:
        return float(self.mask.mean()) if len(self.mask) else 0.0


def thesis_events(f: DrawFeatures) -> list[ThesisEvent]:
    ev: list[ThesisEvent] = []
    share_h = f.home_shot_share
    for home in (True, False):
        s = f.side(home)
        ab = s["abbrev"]
        opp = f.away_abbrev if home else f.home_abbrev
        share = share_h if home else 1.0 - share_h
        margin = s["final"] - s["opp_final"]
        ev += [
            ThesisEvent(f"{ab}:WINS", f"{ab} wins (incl. OT/SO)", "result", ab, s["win"]),
            ThesisEvent(f"{ab}:WINS_BY_2PLUS", f"{ab} wins by 2+", "result", ab, margin >= 2),
            ThesisEvent(f"{ab}:OFFENSE_4PLUS", f"{ab} offense succeeds (4+ goals)", "offense", ab, s["goals"] >= OFFENSE_MIN_GOALS),
            ThesisEvent(f"{ab}:SUPPRESSED", f"{ab} offense suppressed (<= {SUPPRESSED_MAX_GOALS} goals)", "suppression", ab, s["goals"] <= SUPPRESSED_MAX_GOALS),
            ThesisEvent(f"{ab}:SHOT_CONTROL", f"{ab} controls shots (share >= {CONTROL_SHARE:.2f})", "control", ab, share >= CONTROL_SHARE),
            ThesisEvent(f"{ab}:NET_HIGH_VOLUME", f"{ab} net faces heavy volume ({VOLUME_HIGH_MIN}+ shots; {opp} pressure)", "volume", ab, s["net_faced"] >= VOLUME_HIGH_MIN),
            ThesisEvent(f"{ab}:NET_LOW_VOLUME", f"{ab} net faces light volume (<= {VOLUME_LOW_MAX} shots; {opp} suppressed)", "volume", ab, s["net_faced"] <= VOLUME_LOW_MAX),
            ThesisEvent(f"{ab}:GOALIE_STEAL", f"{ab} wins while out-shot ({opp} shot control)", "steal", ab, s["win"] & (share <= 1 - CONTROL_SHARE)),
            ThesisEvent(f"{ab}:PP_DRIVEN", f"{ab} scoring driven by the power play ({PP_DRIVEN_MIN_GOALS}+ PP goals, >= half)", "special", ab,
                        (s["pp"] >= PP_DRIVEN_MIN_GOALS) & (2 * s["pp"] >= s["goals"])),
            ThesisEvent(f"{ab}:COMEBACK", f"{ab} wins after trailing", "shape", ab, s["win"] & (s["max_deficit"] >= 1)),
            ThesisEvent(f"{ab}:SCORES_FIRST", f"{ab} scores first", "order", ab, s["first"]),
        ]
    ev += [
        ThesisEvent("GAME:HIGH_EVENT", f"high-event game ({ENV_HIGH_MIN}+ goals)", "environment", None, f.total >= ENV_HIGH_MIN),
        ThesisEvent("GAME:LOW_EVENT", f"low-event game (<= {ENV_LOW_MAX} goals)", "environment", None, f.total <= ENV_LOW_MAX),
        ThesisEvent("GAME:TIGHT", "tight game (one-goal final or OT)", "shape", None, (np.abs(f.final_margin) <= 1) | f.ot),
        ThesisEvent("GAME:OVERTIME", "goes to overtime", "shape", None, f.ot.copy()),
        ThesisEvent("GAME:EMPTY_NET", "an empty-net goal is scored", "special", None, (f.home_en + f.away_en) >= 1),
    ]
    return ev
