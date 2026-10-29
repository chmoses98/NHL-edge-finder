"""Expression challenger invariants: full eligible board, broad families only, shadow authority."""
from __future__ import annotations

from types import SimpleNamespace

import numpy as np

from nhl_edge.scripts_v1.expression_challenger import build_expression_challenger
from nhl_edge.thesis.mapping import Bet


def _bet(name: str, family: str, yes: list[int], price: int = 40) -> Bet:
    y = np.asarray(yes, dtype=bool)
    return Bet(
        bet_id=name + "|yes", ticker=name, side="yes", title=name,
        family=family, game_id="test", y=y, p=float(y.mean()),
        price_cents=price, fee=0.01, p_mid=price / 100.0,
    )


def _fixture():
    # The incumbent 40-side shortlist could contain only player props.
    # Our broad market MUST still be found from a["candidates"].
    broad = _bet("GAME-ML", "game_winner", [1, 1, 1, 1, 0, 0, 0, 0])
    alt = _bet("GAME-SPREAD", "game_spread", [1, 1, 1, 0, 0, 0, 0, 0], 27)
    player = _bet("GOAL-1", "player_goals", [1, 0, 0, 0, 1, 0, 0, 0], 20)
    bets = [broad, alt, player]
    E = np.asarray([[1, 1, 1, 1, 0, 0, 0, 0]], dtype=np.float32)
    em = SimpleNamespace(E=E, p=E.mean(axis=1),
                         events=[SimpleNamespace(key="HOME:WINS", label="Home wins")])
    econ = {b.bet_id: SimpleNamespace(eligible=True, p_adj=b.p,
                                    ev_adj=b.p - b.cost, bet_up_to_adj=45) for b in bets}
    sv = {b.bet_id: SimpleNamespace(data_quality="OK", tier="MODERATE", mass=0.58,
                                  n_major_survived=3, worst_major_ev=-0.10,
                                  to_dict=lambda: {"failure_script": "AWAY_CONTROL"})
          for b in bets}
    a = {"candidates": bets, "short": [player], "econ": econ, "em": em,
         "gd": SimpleNamespace(features=SimpleNamespace(n=8)),
         "rel": {b.bet_id: "EVIDENCE_MIXED" for b in bets}}
    return a, sv


def test_full_board_and_no_goal_scorer():
    a, sv = _fixture()
    out = build_expression_challenger(a, sv)
    assert out["status"] == "SHADOW_READY"
    assert out["n_compared"] == 2
    assert out["n_player_candidates_excluded"] == 1
    assert out["selected"][0]["ticker"] == "GAME-ML"
    assert out["selected"][0]["best_alternative"]["bet_id"] == "GAME-SPREAD|yes"
    assert all(r["family"] != "player_goals" for r in out["selected"])
    assert all(r["stake_dollars"] == 0 for r in out["selected"])


def test_unavailable_market_never_selected():
    a, sv = _fixture()
    sv["GAME-ML|yes"].data_quality = "STALE_QUOTE"
    out = build_expression_challenger(a, sv)
    assert out["n_compared"] == 1
    assert out["selected"][0]["ticker"] == "GAME-SPREAD"


def test_no_broad_market_returns_no_bet():
    a, sv = _fixture()
    a["candidates"] = [a["short"][0]]
    out = build_expression_challenger(a, sv)
    assert out["status"] == "NO_ELIGIBLE_BROAD_MARKET"
    assert out["selected"] == []
