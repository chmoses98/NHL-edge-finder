"""Per-draw settlement indicators for Kalshi contracts, from the SAME joint draw that priced them.

* Game families (winner, spread, total, team total, OT, period markets) reuse the production V2 pricer through a
  mask-capturing subclass of the draw: the pricer's own ``res.p(mask)`` call hands over the exact indicator it averaged,
  so semantics can never drift from the price (tested: ``mask.mean() == price``).
* Player families (goals / assists / points / saves / first goal) use ``players.pricing.player_outcome``, the function
  ``price_player`` itself averages.

Anything the pricers do not support returns ``None`` with the pricer's reason (fail closed: an unsupported contract is
never given an invented outcome vector).
"""

from __future__ import annotations

from dataclasses import fields
from typing import Any

import numpy as np

from nhl_edge.players.pricing import PLAYER_FAMILIES, player_outcome
from nhl_edge.pricing.price_v2 import price_contract_v2
from nhl_edge.sim.engine_v2 import SimV2Result


class _MaskCapture(SimV2Result):
    """A SimV2Result whose ``p`` records the indicator it was asked to average (the pricer calls it exactly once)."""

    _captured: list[np.ndarray]

    def p(self, mask: np.ndarray) -> tuple[float, float]:
        self._captured.append(np.asarray(mask, dtype=bool))
        return super().p(mask)


def capture_view(res: SimV2Result) -> _MaskCapture:
    cap = _MaskCapture(**{f.name: getattr(res, f.name) for f in fields(res)})
    cap._captured = []
    return cap


def game_outcome(contract: Any, cap: _MaskCapture, home_team_id: int, away_team_id: int) -> tuple[np.ndarray | None, float | None, str]:
    """(YES indicator, priced p, reason) for a game-scope contract priced by the V2 pricer."""
    cap._captured.clear()
    pr, _support = price_contract_v2(contract, cap, home_team_id, away_team_id)
    if not pr.supported or pr.p is None:
        return None, None, pr.reason
    if len(cap._captured) != 1:
        return None, None, f"pricer made {len(cap._captured)} probability calls; outcome vector not identifiable (fail closed)"
    y = cap._captured[0]
    if abs(float(y.mean()) - float(pr.p)) > 1e-12:
        return None, None, "captured outcome does not reproduce the price (fail closed)"
    return y, float(pr.p), pr.reason


def contract_outcome(contract: Any, player_id: int | None, cap: _MaskCapture, ps: Any, saves: dict[int, Any], goalie_team: dict[int, int],
                     home_team_id: int, away_team_id: int) -> tuple[np.ndarray | None, float | None, str]:
    if contract.family in PLAYER_FAMILIES:
        y, reason = player_outcome(contract.family, contract.comparator, contract.threshold, player_id, ps, saves, goalie_team)
        return (y, float(np.mean(y)), reason) if y is not None else (None, None, reason)
    if contract.scope != "game":
        return None, None, f"scope {contract.scope} has no simulated outcome"
    return game_outcome(contract, cap, home_team_id, away_team_id)
