"""Normal-market (sportsbook) benchmark for the card: does the broader market corroborate the model against Kalshi?

Source: the quarantined ``context/sportsbook_odds`` kind (moneylines the official NHL schedule feed carries; no scraping,
no paid source). Only moneyline prices are carried, so only ``game_winner`` contracts can be benchmarked; every other
family is category D. Each provider's two prices are de-vigged proportionally; providers whose implied probabilities
sum outside [1.00, 1.15] are dropped (a sum below 1 is a three-way / regulation price, not a two-way moneyline). The
consensus is the median across the remaining providers.

Categories (per bet side; ``p`` = model, ``mid`` = Kalshi midpoint, ``cost`` = executable ask + fee, ``b`` = consensus):

    A  model and sportsbook agree Kalshi is mispriced: b - cost > 0 and p - cost > 0
    B  model disagrees with Kalshi and the sportsbook leans the model's way (b beyond mid by >= 0.5 pt) but not past cost
    C  the model alone disagrees with both Kalshi and the sportsbook
    D  no external benchmark

The category moves CONFIDENCE (the edge haircut in ``thesis.expression``); it never overrides the model probability.
"""

from __future__ import annotations

import statistics
from typing import Any

LEAN = 0.005
OVERROUND_MIN, OVERROUND_MAX = 1.00, 1.15
CATEGORY_TEXT = {"A": "model + sportsbook agree Kalshi is mispriced", "B": "model disagrees with Kalshi; sportsbook leans the model's way",
                 "C": "model alone disagrees with Kalshi and the sportsbook", "D": "no external benchmark available"}


def decimal_odds(v: Any) -> float | None:
    s = str(v or "").strip()
    if not s:
        return None
    try:
        if s[0] in "+-":
            a = float(s)
            return 1.0 + (a / 100.0 if a > 0 else 100.0 / -a)
        d = float(s)
        return d if d > 1.0 else None
    except ValueError:
        return None


def consensus_moneyline(rows: list[dict[str, Any]], game_id: str, home_team_id: int, away_team_id: int) -> dict[str, Any] | None:
    """{p_home, p_away, providers, n} de-vigged consensus for one game, or None."""
    by: dict[str, dict[str, float]] = {}
    for r in rows or []:
        if str(r.get("game_id")) != str(game_id) or str(r.get("game_state") or "PRE") not in ("PRE", "FUT"):
            continue
        d = decimal_odds(r.get("value"))
        if d is None:
            continue
        side = "home" if r.get("team_id") == home_team_id or r.get("side") == "home" else "away"
        by.setdefault(str(r.get("provider") or r.get("provider_id")), {})[side] = d
    ps = []
    used = []
    for prov, x in sorted(by.items()):
        if "home" not in x or "away" not in x:
            continue
        ih, ia = 1.0 / x["home"], 1.0 / x["away"]
        o = ih + ia
        if not (OVERROUND_MIN <= o <= OVERROUND_MAX):
            continue
        ps.append(ih / o)
        used.append(prov)
    if not ps:
        return None
    ph = statistics.median(ps)
    return {"p_home": round(ph, 4), "p_away": round(1 - ph, 4), "providers": used, "n": len(ps)}


def categorize(p: float, p_mid: float | None, cost: float | None, b: float | None) -> str:
    if b is None or p_mid is None or cost is None:
        return "D"
    if b - cost > 0 and p - cost > 0:
        return "A"
    direction = 1.0 if p >= p_mid else -1.0
    if direction * (b - p_mid) >= LEAN:
        return "B"
    return "C"


def book_probability(bet: Any, consensus: dict[str, Any] | None, home_abbrev: str) -> float | None:
    """Sportsbook probability that THIS bet side pays, for game_winner contracts only."""
    if consensus is None or bet.family != "game_winner" or not bet.meta.get("contract_team"):
        return None
    p_team = consensus["p_home"] if bet.meta["contract_team"] == home_abbrev else consensus["p_away"]
    return p_team if bet.side == "yes" else 1.0 - p_team
