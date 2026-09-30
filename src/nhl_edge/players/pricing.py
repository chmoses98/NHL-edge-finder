"""Price Kalshi player contracts from one PLAYER_SIM_V1 joint draw.

Every probability is a frequency over the SAME simulated games, so ladders (1+ >= 2+ >= 3+ points; 20+ >= 21+ saves)
are monotone by construction and goals / assists / points / team totals / moneyline stay jointly coherent.

Semantics (live rule text, docs/KALSHI_MARKET_MAP.md): "If <player> records N+ goals / assists / points / saves in
the <A> vs <B> NHL game ..." with ``strike_type=greater`` and ``floor_strike = N - 0.5``; "If <player> scores the 1st
goal ...". Official statistics include overtime (a shootout "goal" is not a goal). "If a player is active but never
enters the game, the market settles to the last fair market price before game start": every probability here is
therefore CONDITIONAL ON THE PLAYER PLAYING (for goalies: starting), and the packet reports that condition's
confidence separately instead of multiplying it in.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from nhl_edge.players.engine import PlayerSimResult
from nhl_edge.players.saves import SavesDraws

PLAYER_FAMILIES = {"player_goals": "goals", "player_points": "points", "player_assists": "assists", "goalie_saves": "saves", "first_goal": "first_goal"}


@dataclass(frozen=True)
class PlayerPrice:
    p: float | None
    se: float | None
    supported: bool
    reason: str


def _cmp(x: np.ndarray, comparator: str | None, threshold: float | None) -> np.ndarray | None:
    if threshold is None:
        return None
    if comparator == "gt":
        return x > threshold
    if comparator == "ge":
        return x >= threshold
    return None


def price_player(family: str, comparator: str | None, threshold: float | None, player_id: int | None, ps: PlayerSimResult,
                 saves: dict[int, SavesDraws] | None = None, goalie_team: dict[int, int] | None = None) -> PlayerPrice:
    """``saves``: team_id -> SavesDraws for that team's net; ``goalie_team``: goalie player id -> team id."""
    stat = PLAYER_FAMILIES.get(family)
    if stat is None:
        return PlayerPrice(None, None, False, f"family {family} is not a PLAYER_SIM_V1 family")
    if player_id is None:
        return PlayerPrice(None, None, False, "player not resolved to an NHL id")
    n = ps.n_sims
    if stat == "first_goal":
        hit = ps.first_scorer == player_id
        if not (ps.player(player_id)):
            return PlayerPrice(None, None, False, "player not in either projected lineup")
        p = float(hit.mean())
        return PlayerPrice(p, float(np.sqrt(max(p * (1 - p), 1e-12) / n)), True, "first goal from simulated event order")
    if stat == "saves":
        tid = (goalie_team or {}).get(int(player_id))
        if tid is None or not saves or tid not in saves:
            return PlayerPrice(None, None, False, "goalie not on either team's goalie list")
        x = saves[tid].saves
    else:
        found = ps.player(player_id)
        if found is None:
            return PlayerPrice(None, None, False, "player not in either projected lineup (scratched / not dressed / unknown)")
        d, _, i = found
        x = {"goals": d.goals[:, i], "assists": d.assists[:, i], "points": d.points[:, i]}[stat]
    y = _cmp(x, comparator, threshold)
    if y is None:
        return PlayerPrice(None, None, False, f"unsupported comparator/threshold {comparator} {threshold}")
    p = float(y.mean())
    return PlayerPrice(p, float(np.sqrt(max(p * (1 - p), 1e-12) / n)), True, f"{stat} {comparator} {threshold} from the joint draw")


def ladder_violations(ps: PlayerSimResult) -> list[str]:
    out = []
    for side, d in (("home", ps.home), ("away", ps.away)):
        for name, x in (("goals", d.goals), ("assists", d.assists), ("points", d.points)):
            p = np.stack([(x >= k).mean(axis=0) for k in (1, 2, 3, 4)])
            if (np.diff(p, axis=0) > 1e-12).any():
                out.append(f"{side} {name} ladder not monotone")
        if (d.points < d.goals).any() or (d.points < d.assists).any():
            out.append(f"{side} points below goals or assists")
    return out
