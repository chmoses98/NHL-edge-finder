"""Focused case study of the routed wagers on one slate (Phase E). Real fills and real fees only -- no hypothetical stakes.

For each routed wager: the fill, the displayed board and the last pregame quote, minutes from scheduled puck drop, whether the
production thesis workflow ever considered the bet, the last pregame V1 / V2 / thesis views AT OR BEFORE the fill, the goalie /
rest context, the script forecast and the realised script, and expected value AT THE ACTUAL FILL PRICE under four probability
views (market mid, V1, V2, thesis-adjusted). Four bets cannot establish skill or its absence; the module reports the
expected-versus-realised gap and its z-score so the reader can see how little they can say.
"""

from __future__ import annotations

import json
from typing import Any

import pandas as pd

from nhl_edge.market_audit.efficiency import taker_fee


def _win_p(yes_p: float | None, side: str) -> float | None:
    return None if yes_p is None or yes_p != yes_p else (yes_p if side == "YES" else 1.0 - yes_p)


def _ev(p_win: float | None, price: float) -> float | None:
    return None if p_win is None or p_win != p_win else float(p_win - price - taker_fee(price))


def case_for_date(date: str, wag: pd.DataFrame, cm: pd.DataFrame, games: pd.DataFrame, oc: pd.DataFrame, ev: pd.DataFrame, td: pd.DataFrame,
                  p1: pd.DataFrame, p2: pd.DataFrame, tg: pd.DataFrame, sf: pd.DataFrame, spm: pd.DataFrame) -> dict[str, Any]:
    out = []
    w = wag[wag["game_date"] == date].sort_values("executed_at")
    for r in w.itertuples():
        c = cm[cm["ticker"] == r.market_ticker].iloc[0]
        g = games[games["game_id"] == c["game_id"]].iloc[0]
        gid = str(c["game_id"])
        side = r.side.upper()
        e = ev[(ev["ticker"] == r.market_ticker) & (ev["available_at"] <= r.executed_at)].tail(1)
        pre = ev[(ev["ticker"] == r.market_ticker) & (ev["available_at"] <= g["start_time_utc"])].tail(1)

        rec: dict[str, Any] = {"ticker": r.market_ticker, "matchup": f"{g['away_abbrev']} @ {g['home_abbrev']}", "side": side, "fill_price": r.execution_price,
                               "contracts": r.contracts, "stake": r.stake, "fee": r.fees_paid, "executed_at": str(r.executed_at), "scheduled_start": str(g["start_time_utc"]),
                               "minutes_after_scheduled_start": (r.executed_at - g["start_time_utc"]).total_seconds() / 60.0, "ledger_result": r.result, "net_pl": r.net_profit_loss,
                               "final": f"{g['away_abbrev']} {int(g['away_final'])} - {g['home_abbrev']} {int(g['home_final'])} ({g['last_period_type']})",
                               "resolver_outcome": oc.set_index("ticker")["outcome"].get(r.market_ticker), "resolver_value": oc.set_index("ticker")["value"].get(r.market_ticker)}
        if len(e):
            e0 = e.iloc[0]
            rec["board_at_fill"] = {"tick": str(e0["observed_at"]), "yes_bid": e0["yes_bid"], "yes_ask": e0["yes_ask"], "age_min": (r.executed_at - e0["observed_at"]).total_seconds() / 60.0}
            mid = (e0["yes_bid"] + e0["yes_ask"]) / 200.0
            rec["ev_at_fill_market_mid"] = _ev(_win_p(mid, side), r.execution_price)
        if len(pre):
            p0 = pre.iloc[0]
            rec["last_pregame_quote"] = {"tick": str(p0["observed_at"]), "yes_bid": p0["yes_bid"], "yes_ask": p0["yes_ask"]}
        for lab, pr, col in (("v1", p1, "p_data_only"), ("v2", p2, "p_data_only_v2")):
            x = pr[(pr["ticker"] == r.market_ticker) & (pd.to_datetime(pr["predicted_at_utc"], utc=True) <= r.executed_at)].sort_values("predicted_at_utc").tail(1)
            if len(x) and pd.notna(x.iloc[0][col]):
                py = float(x.iloc[0][col])
                rec[lab] = {"p_yes": py, "p_win": _win_p(py, side), "minutes_before_fill": (r.executed_at - pd.to_datetime(x.iloc[0]["predicted_at_utc"], utc=True)).total_seconds() / 60.0,
                            "ev_at_fill": _ev(_win_p(py, side), r.execution_price)}
        t = td[(td["ticker"] == r.market_ticker) & (td["side"] == side.lower())].sort_values("decided_at_utc")
        rec["thesis"] = {"n_snapshots": int(len(t)), "ever_funded_research": bool((t["research_status"] == "FUNDED_RESEARCH").any()) if len(t) else False}
        if len(t):
            last = t[t["decided_at_utc"] <= r.executed_at.isoformat().replace("+00:00", "Z")].tail(1)
            if len(last):
                l0 = last.iloc[0]
                rec["thesis"].update({"last_snapshot_before_fill": l0["decided_at_utc"], "p_model": float(l0["p_model"]), "p_adjusted": float(l0["p_adjusted"]),
                                      "p_kalshi_mid": float(l0["p_kalshi_mid"]), "ev_adjusted_claimed": float(l0["ev_adjusted"]), "reliability": l0["reliability"],
                                      "benchmark_category": l0["benchmark_category"], "research_stake_at_that_snapshot": float(l0["research_stake_dollars"]),
                                      "ev_at_fill_thesis_adjusted": _ev(float(l0["p_adjusted"]), r.execution_price)})
        gx = tg[tg["game_id"] == gid].sort_values("decided_at_utc").tail(1)
        if len(gx):
            meta = json.loads(gx.iloc[0]["meta"]) if isinstance(gx.iloc[0]["meta"], str) else gx.iloc[0]["meta"]
            ctx = meta.get("context", {})
            rec["context"] = {"home_goalie": ctx.get("goalies", {}).get("home"), "away_goalie": ctx.get("goalies", {}).get("away"), "home_rest_days": ctx.get("home_rest_days"),
                              "away_rest_days": ctx.get("away_rest_days"), "home_b2b": ctx.get("home_b2b"), "away_b2b": ctx.get("away_b2b"),
                              "lam_home": meta.get("lam_home"), "lam_away": meta.get("lam_away")}
        f = sf[sf["game_id"] == gid].sort_values("decided_at_utc").tail(1)
        if len(f):
            rec["script_probabilities_last_forecast"] = f.iloc[0]["script_probabilities"]
        m = spm[spm["game_id"] == gid].tail(1)
        if len(m):
            rec["realized_script"] = {"script": m.iloc[0]["realized_script"], "p_realized": float(m.iloc[0]["p_realized"]), "top_script": m.iloc[0]["top_script"],
                                      "top_hit": bool(m.iloc[0]["top_hit"]), "metrics": m.iloc[0]["realized_metrics"]}
        out.append(rec)
    return {"date": date, "wagers": out, "net_pl": float(sum(o["net_pl"] for o in out)), "staked": float(sum(o["stake"] for o in out)),
            "wins": int(sum(o["ledger_result"] == "WON" for o in out)), "losses": int(sum(o["ledger_result"] == "LOST" for o in out))}
