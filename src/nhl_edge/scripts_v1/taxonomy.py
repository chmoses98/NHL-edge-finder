"""NHL_SCRIPT_V1 taxonomy: seven mutually exclusive, hockey-native game scripts.

Every script is a fixed rule on :class:`~nhl_edge.thesis.features.DrawFeatures`. Rules are applied in a fixed
PRECEDENCE order and the first one that matches wins, so every draw (and every real game) gets exactly one script and
the script probabilities of a game sum to exactly 1 (integer counts over the same draws). The last script,
BACK_AND_FORTH, is the explicit catch-all: there is no hidden "other" bucket.

    precedence  id               rule (on one draw or one final game)
    1           SPECIAL_TEAMS    a team scores >= 2 power-play goals AND they are at least half of its goals
    2           OPEN_GAME        >= 8 non-shootout goals
    3           TIGHT_LOW_EVENT  <= 4 non-shootout goals AND a one-goal final or overtime
    4           GOALIE_DRIVEN    the winner had <= 42% of the shots on goal (out-shot clearly and won anyway)
    5           HOME_CONTROL     home wins by 2+ with >= 50% of the shots on goal
    6           AWAY_CONTROL     away wins by 2+ with >= 50% of the shots on goal
    7           BACK_AND_FORTH   everything else: normal scoring, roughly even play or a one-goal finish

Thresholds are a priori choices aligned with ``thesis.scripts`` (the same 8-goal / 4-goal environment cut points and
the same "2+ PP goals and half the team's goals" PP_DRIVEN rule) plus two new cut points (goalie-driven <= 42%
winner shot share; control = 2+ goal win without being out-shot). They were chosen so that every script has a
historical base rate between ~8% and ~25% on completed regular seasons 2022-23 .. 2025-26 (5,248 official games,
``research/script_base_rates.py`` -> ``base_rates.json``); they were NOT fit to any slate, price or result.

Known caveat (documented, measured by the learning loop rather than hidden): simulated shots on goal come from the
goalie-saves layer, whose score effects are muted (``docs/research/THESIS_ENGINE.md`` 11B). Real trailing teams out-shoot
leaders, so GOALIE_DRIVEN is expected to be UNDER-forecast by the simulation relative to history. The realised-script
classifier uses the identical rule on the official final, and the script calibration report shows the gap.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

import numpy as np

from nhl_edge.scripts_v1 import REALIZED_VERSION, SCRIPT_METHODOLOGY, SCRIPT_VERSION
from nhl_edge.thesis.features import DrawFeatures

PP_DRIVEN_MIN_GOALS = 2
OPEN_MIN_GOALS = 8
TIGHT_LOW_MAX_GOALS = 4
GOALIE_WINNER_MAX_SHARE = 0.42
CONTROL_MIN_SHARE = 0.50
CONTROL_MIN_MARGIN = 2
MAJOR_MIN_FREQ = 0.05  # a script is "major" for a game when it holds >= 5% of the draws

THRESHOLDS = {
    "pp_driven_min_goals": PP_DRIVEN_MIN_GOALS, "open_min_goals": OPEN_MIN_GOALS, "tight_low_max_goals": TIGHT_LOW_MAX_GOALS,
    "goalie_winner_max_shot_share": GOALIE_WINNER_MAX_SHARE, "control_min_shot_share": CONTROL_MIN_SHARE,
    "control_min_margin": CONTROL_MIN_MARGIN, "major_min_frequency": MAJOR_MIN_FREQ,
    "provenance": "a priori; aligned with thesis.scripts cut points; base rates 8-25% on 2022-23..2025-26 official finals; never fit to a slate",
}


@dataclass(frozen=True)
class ScriptDef:
    id: str
    code: int
    label: str  # may contain {home} / {away}
    short: str
    summary: str  # one plain-English sentence: what the game looks like
    needs: str  # what would need to happen
    breaks: str  # what breaks it
    rule: str  # the exact rule, human-readable
    side: str | None = None  # "home" / "away" for directional scripts

    def name(self, home: str, away: str) -> str:
        return self.label.format(home=home, away=away)

    def text(self, field: str, home: str, away: str) -> str:
        return getattr(self, field).format(home=home, away=away)


SCRIPTS: tuple[ScriptDef, ...] = (
    ScriptDef("SPECIAL_TEAMS", 0, "Special teams decide it", "Special teams",
              "Power plays drive the scoring: one side converts repeatedly with the man advantage.",
              "Penalties pile up and one power play converts at least twice.",
              "A clean, low-penalty game decided at even strength.",
              f"a team scores >= {PP_DRIVEN_MIN_GOALS} power-play goals and they are at least half of its goals"),
    ScriptDef("OPEN_GAME", 1, "Open, high-event game", "Open game",
              "Chances flow both ways and the scoreboard keeps moving: eight or more goals.",
              "Both offenses generate quality chances and the goaltending does not hold.",
              "Either goalie settles in, or one team shuts the game down after taking a lead.",
              f">= {OPEN_MIN_GOALS} non-shootout goals"),
    ScriptDef("TIGHT_LOW_EVENT", 2, "Tight, low-event game", "Tight, low-event",
              "Few chances, strong goaltending, and a one-goal or overtime finish with four goals or fewer.",
              "Both teams defend well and neither power play converts much.",
              "An early multi-goal lead, or either team's finishing running hot.",
              f"<= {TIGHT_LOW_MAX_GOALS} non-shootout goals and a one-goal final or overtime"),
    ScriptDef("GOALIE_DRIVEN", 3, "Goaltending steals it", "Goalie steals it",
              "One team is clearly out-shot and wins anyway behind its goaltender or opportunistic finishing.",
              "The out-shot team's goalie stops nearly everything and it converts its few chances.",
              "The team with the territorial edge simply converts its shot volume.",
              f"the winner had <= {round(GOALIE_WINNER_MAX_SHARE * 100)}% of the shots on goal"),
    ScriptDef("HOME_CONTROL", 4, "{home} controls and pulls away", "{home} control",
              "{home} holds the territorial edge and wins by two or more.",
              "{home} out-chances {away} and converts enough to pull clear (an empty-net goal often seals it).",
              "{away}'s goalie stealing it, or {away} keeping it to a one-goal game.",
              f"home wins by {CONTROL_MIN_MARGIN}+ with >= {round(CONTROL_MIN_SHARE * 100)}% of the shots on goal", "home"),
    ScriptDef("AWAY_CONTROL", 5, "{away} controls and pulls away", "{away} control",
              "{away} holds the territorial edge on the road and wins by two or more.",
              "{away} out-chances {home} and converts enough to pull clear.",
              "{home}'s goalie stealing it, or {home} keeping it to a one-goal game.",
              f"away wins by {CONTROL_MIN_MARGIN}+ with >= {round(CONTROL_MIN_SHARE * 100)}% of the shots on goal", "away"),
    ScriptDef("BACK_AND_FORTH", 6, "Back-and-forth game", "Back-and-forth",
              "A normal-scoring game with roughly even play, usually decided late or by one goal.",
              "Neither team establishes sustained control, and the score stays within reach.",
              "Any team pulling clear with territorial control, a goalie steal, or a power-play barrage.",
              "everything not matched above (the explicit catch-all; no hidden 'other' bucket)"),
)
N_SCRIPTS = len(SCRIPTS)
BY_ID = {s.id: s for s in SCRIPTS}


def classify(f: DrawFeatures) -> np.ndarray:
    """Script code (0..6) per draw / per final game, by precedence. Pure function of the features."""
    total = f.total
    margin = f.final_margin
    share = f.home_shot_share
    home_win = f.winner == 1
    win_share = np.where(home_win, share, 1.0 - share)
    pp_h = (f.home_pp >= PP_DRIVEN_MIN_GOALS) & (2 * f.home_pp >= f.home_goals)
    pp_a = (f.away_pp >= PP_DRIVEN_MIN_GOALS) & (2 * f.away_pp >= f.away_goals)
    rules = [
        pp_h | pp_a,
        total >= OPEN_MIN_GOALS,
        (total <= TIGHT_LOW_MAX_GOALS) & ((np.abs(margin) <= 1) | f.ot),
        win_share <= GOALIE_WINNER_MAX_SHARE,
        (margin >= CONTROL_MIN_MARGIN) & (share >= CONTROL_MIN_SHARE),
        (margin <= -CONTROL_MIN_MARGIN) & ((1.0 - share) >= CONTROL_MIN_SHARE),
    ]
    return np.select(rules, list(range(len(rules))), default=N_SCRIPTS - 1).astype(np.int8)


def frequencies(codes: np.ndarray) -> np.ndarray:
    n = max(len(codes), 1)
    return np.bincount(codes.astype(np.int64), minlength=N_SCRIPTS).astype(float) / n


@lru_cache(maxsize=1)
def base_rates() -> dict[str, Any]:
    """Historical realised-script frequencies (completed regular seasons), frozen in ``base_rates.json``."""
    p = Path(__file__).with_name("base_rates.json")
    return json.loads(p.read_text(encoding="utf-8"))


def taxonomy_doc(home: str, away: str) -> list[dict[str, Any]]:
    br = (base_rates().get("frequency") or {})
    return [{"id": s.id, "code": s.code, "order": s.code + 1, "label": s.name(home, away), "short": s.short.format(home=home, away=away),
             "summary": s.text("summary", home, away), "needs": s.text("needs", home, away), "breaks": s.text("breaks", home, away),
             "rule": s.rule, "side": s.side, "league_base_rate": br.get(s.id)} for s in SCRIPTS]


def methodology() -> dict[str, Any]:
    br = base_rates()
    return {"script_version": SCRIPT_VERSION, "methodology_version": SCRIPT_METHODOLOGY, "realized_version": REALIZED_VERSION,
            "partition": "mutually exclusive by precedence; probabilities are integer draw counts and sum to 1",
            "precedence": [s.id for s in SCRIPTS], "thresholds": THRESHOLDS,
            "base_rates": {"n_games": br.get("n_games"), "seasons": br.get("seasons"), "source": br.get("source")},
            "caveat": ("simulated shot volume comes from the goalie-saves layer with muted score effects; GOALIE_DRIVEN is expected to be "
                       "under-forecast relative to history. The script calibration report measures it.")}


# ------------------------------------------------------------------------------------------------ realised (postgame only)
def realized(f: DrawFeatures) -> dict[str, Any]:
    """The realised script of ONE official final game (``DrawFeatures.from_actual``). POSTGAME ONLY: this uses the
    result and is never an input to a pregame forecast. Same rule as the pregame classifier, so a forecast is scored
    against exactly the partition it predicted."""
    if f.n != 1:
        raise ValueError("realized() classifies exactly one final game")
    code = int(classify(f)[0])
    s = SCRIPTS[code]
    hs, as_ = int(f.home_shots[0]), int(f.away_shots[0])
    return {"script_id": s.id, "code": code, "label": s.name(f.home_abbrev, f.away_abbrev), "realized_version": REALIZED_VERSION,
            "script_version": SCRIPT_VERSION,
            "metrics": {"home_goals": int(f.home_goals[0]), "away_goals": int(f.away_goals[0]), "home_final": int(f.home_final[0]),
                        "away_final": int(f.away_final[0]), "total_goals": int(f.total[0]), "overtime": bool(f.ot[0]), "shootout": bool(f.so[0]),
                        "home_shots": hs, "away_shots": as_, "home_shot_share": round(float(f.home_shot_share[0]), 4),
                        "home_pp_goals": int(f.home_pp[0]), "away_pp_goals": int(f.away_pp[0]),
                        "home_en_goals": int(f.home_en[0]), "away_en_goals": int(f.away_en[0])}}
