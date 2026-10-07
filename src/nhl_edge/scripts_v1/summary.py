"""Per-script game summaries computed from the joint draw (no narrative is invented: every number is a draw statistic).

For each NHL_SCRIPT_V1 script of one game: probability (integer draw share), whether it is major, who wins inside it,
mean goals per side, the total-goals range (p10 / p50 / p90 of the draws inside the script), shots per side, each
projected starter's saves, overtime share, power-play and empty-net share of the goals, the players whose point
probability rises most inside it, and which priced markets it helps / hurts most (largest lift of P(side | script)
over P(side)).
"""

from __future__ import annotations

from typing import Any

import numpy as np

from nhl_edge.scripts_v1.taxonomy import MAJOR_MIN_FREQ, SCRIPTS
from nhl_edge.thesis.features import DrawFeatures

#: families whose YES/NO sides are game-level expressions a script naturally speaks to (player props are listed separately)
GAME_FAMILIES = ("game_winner", "game_spread", "game_total", "team_total", "game_overtime", "period_winner", "period_total", "goalie_saves", "btts")
MARKET_LIFT_MIN = 0.05  # a market is "helped" by a script when P(side | script) beats P(side) by >= 5 points


def _m(x: np.ndarray | None, mask: np.ndarray, nd: int = 2) -> float | None:
    if x is None or not mask.any():
        return None
    return round(float(np.mean(x[mask])), nd)


def _q(x: np.ndarray, mask: np.ndarray) -> dict[str, int] | None:
    if not mask.any():
        return None
    q = np.percentile(x[mask], [10, 50, 90])
    return {"p10": int(round(q[0])), "p50": int(round(q[1])), "p90": int(round(q[2]))}


def script_summaries(f: DrawFeatures, codes: np.ndarray, player_points: dict[str, np.ndarray] | None = None) -> list[dict[str, Any]]:
    n = max(f.n, 1)
    win_h = f.winner == 1
    goals = f.total.astype(float)
    pp = (f.home_pp + f.away_pp).astype(float)
    en = (f.home_en + f.away_en).astype(float)
    base_pt = {k: float(v.mean()) for k, v in (player_points or {}).items()}
    out = []
    for s in SCRIPTS:
        m = codes == s.code
        k = int(m.sum())
        freq = k / n
        g = goals[m].sum() if k else 0.0
        involve = []
        for name, v in (player_points or {}).items():
            if k and base_pt.get(name, 0) > 0.02:
                pm = float(v[m].mean())
                involve.append((name, pm / base_pt[name], pm))
        involve.sort(key=lambda t: (-t[1], t[0]))
        out.append({
            "id": s.id, "code": s.code, "label": s.name(f.home_abbrev, f.away_abbrev), "draws": k, "probability": round(freq, 4),
            "major": bool(freq >= MAJOR_MIN_FREQ),
            "p_home_win": _m(win_h.astype(float), m, 4), "p_away_win": _m((~win_h).astype(float), m, 4),
            "home_goals": _m(f.home_goals, m), "away_goals": _m(f.away_goals, m), "total_goals": _m(goals, m),
            "total_goals_range": _q(goals, m), "home_shots": _m(f.home_shots, m, 1), "away_shots": _m(f.away_shots, m, 1),
            "home_shot_share": _m(f.home_shot_share, m, 3),
            "home_starter_saves": _m(f.home_saves, m, 1), "away_starter_saves": _m(f.away_saves, m, 1),
            "p_overtime": _m(f.ot.astype(float), m, 3),
            "pp_goal_share": round(float(pp[m].sum() / g), 3) if g > 0 else None,
            "en_goal_share": round(float(en[m].sum() / g), 3) if g > 0 else None,
            "home_pp_goals": _m(f.home_pp, m), "away_pp_goals": _m(f.away_pp, m),
            "players_most_involved": [{"player": nm, "p_point": round(p, 3), "lift": round(li, 2)} for nm, li, p in involve[:3] if li > 1.05],
        })
    return out


def market_effects(bets: list[Any], P: np.ndarray, freq: np.ndarray, survival: dict[str, Any], max_n: int = 4) -> dict[str, dict[str, list[dict[str, Any]]]]:
    """script id -> {helped: [...], hurt: [...]} among game-level markets (largest lift of P(side|script) over P(side)).
    Each contract appears once per list, on the side that the script moves the most."""
    out: dict[str, dict[str, list[dict[str, Any]]]] = {}
    idx = [i for i, b in enumerate(bets) if b.family in GAME_FAMILIES and b.side == "yes" and 0.06 <= b.p <= 0.94]
    for s in SCRIPTS:
        if freq[s.code] <= 0:
            out[s.id] = {"helped": [], "hurt": []}
            continue
        rows = []
        for i in idx:
            b = bets[i]
            lift = float(P[i, s.code] - b.p)
            if np.isnan(lift):
                continue
            rows.append((lift, i, b))
        rows.sort(key=lambda t: (-abs(t[0]), t[2].ticker))
        helped, hurt = [], []
        for lift, i, b in rows:
            if abs(lift) < MARKET_LIFT_MIN:
                continue
            side = "yes" if lift > 0 else "no"
            row = {"ticker": b.ticker, "side": side, "title": b.title, "family": b.family,
                   "p": round(b.p if side == "yes" else 1 - b.p, 4),
                   "p_given_script": round(float(P[i, s.code]) if side == "yes" else 1 - float(P[i, s.code]), 4),
                   "lift": round(abs(lift), 4)}
            if len(helped) < max_n:
                helped.append(row)
        # "hurt": the sides of this game's priced, positive-adjusted-EV bets that LOSE value most in this script
        cand = [(sv.ev_by_script[s.code] - (sv.expected_ev or 0.0), bid) for bid, sv in survival.items()
                if sv.ev_by_script is not None and sv.expected_ev is not None and sv.expected_ev > 0 and not np.isnan(sv.ev_by_script[s.code])]
        cand.sort(key=lambda t: (t[0], t[1]))
        for d, bid in cand[:max_n]:
            if d < -MARKET_LIFT_MIN:
                hurt.append({"bet_id": bid, "ev_drop": round(float(d), 4)})
        out[s.id] = {"helped": helped, "hurt": hurt}
    return out
