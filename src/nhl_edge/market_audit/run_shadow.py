"""Replay the SHADOW expression engine over the archive: one decision per final game at T-60m, strict policy and a
research_unvalidated counterfactual. Reads only derived tables; writes JSON; touches nothing in production.

``python -m nhl_edge.market_audit.run_shadow --derived <dir> --out <json> [--cards <json>]``
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from nhl_edge.market_audit.efficiency import cluster_ratio_ci, taker_fee
from nhl_edge.market_audit.expression_engine import Candidate, build_card

FACTOR = {("total", "no"): "LOW_SCORING", ("total", "yes"): "HIGH_SCORING", ("period_total", "no"): "LOW_SCORING", ("period_total", "yes"): "HIGH_SCORING",
          ("team_total", "no"): "LOW_SCORING", ("team_total", "yes"): "HIGH_SCORING", ("early_goal", "no"): "LOW_SCORING", ("early_goal", "yes"): "HIGH_SCORING"}
IN_SCOPE = ("winner", "spread", "total", "team_total", "period_winner", "period_spread", "period_total", "overtime", "early_goal", "player_stat")


def audited_weights(audit: dict) -> dict[str, float]:
    """w = max(0, c - 1.28 se) per family, from the HISTORY-tier audit (never from the data being replayed)."""
    w: dict[str, float] = {}
    for key, kind in (("HIST|V2|winner", "game_winner"), ("HIST|V2|total", "game_total"), ("HIST|V2|spread", "game_spread")):
        inc = audit[key]["incremental"]
        se = inc["se"]
        w[kind] = max(0.0, inc["c"] - 1.2816 * se) if se == se else 0.0
    return w


def family_classes(reg: dict) -> dict[str, str]:
    """Evidence class per family = best class of any registered hypothesis touching it (conservative: UNTESTED if none)."""
    order = ["UNTESTABLE", "REJECTED", "INCONCLUSIVE", "PROMISING", "VALIDATED"]
    fam_of = {"M1": ["game_total"], "M2": ["game_total"], "M3": ["game_winner", "game_spread", "game_total", "team_total"],
              "M4": ["game_winner", "game_spread", "game_total", "team_total"], "M5": ["game_spread"], "M7": ["team_total"], "M8": ["team_total"],
              "M9": ["period_total"], "M10": ["period_total"], "M13": ["game_overtime"], "M14": ["game_early_goal"],
              "M11": ["game_winner"], "M12": ["game_winner"], "C1": ["game_winner", "game_spread", "game_total", "team_total"],
              "C2": ["game_winner", "game_spread", "game_total", "team_total", "period_winner", "period_spread", "period_total"]}
    best: dict[str, str] = {}
    for hid, fams in fam_of.items():
        cls = reg[hid]["class"]
        for f in fams:
            if f not in best or order.index(cls) > order.index(best[f]):
                best[f] = cls
    return best


def run(derived: Path, reg_json: Path, audit_json: Path) -> tuple[dict, list[dict]]:
    reg = json.loads(reg_json.read_text())["results"]
    audit = json.loads(audit_json.read_text())
    w_fam, cls = audited_weights(audit), family_classes(reg)
    live = pd.read_parquet(derived / "live_panel.parquet")
    lv = live[(live["horizon_min"] == 60) & live["kind"].isin(IN_SCOPE)].copy()
    cm = pd.read_parquet(derived / "contract_master.parquet")[["ticker", "family"]]
    st = pd.read_parquet(derived / "market_static.parquet")[["ticker", "title"]]
    lv = lv.merge(cm, on="ticker", how="left", suffixes=("", "_c")).merge(st, on="ticker", how="left")
    # model views at or before the cut
    for fn, col, new in (("raw_predictions.parquet", "p_data_only", "p_v1"), ("raw_predictions_v2.parquet", "p_data_only_v2", "p_v2"),
                         ("raw_predictions_player.parquet", "p_player", "p_pl")):
        pr = pd.read_parquet(derived / fn, columns=["ticker", "predicted_at_utc", col])
        pr = pr[pr[col].notna()].assign(pa=lambda d: pd.to_datetime(d["predicted_at_utc"], utc=True)).sort_values("pa")
        q = lv[["ticker", "cut"]].drop_duplicates("ticker").sort_values("cut")
        m = pd.merge_asof(q, pr[["ticker", "pa", col]], left_on="cut", right_on="pa", by="ticker", direction="backward")
        lv = lv.merge(m[["ticker", col]].rename(columns={col: new}), on="ticker", how="left")
    td = pd.read_parquet(derived / "raw_thesis_decisions.parquet")
    td["t"] = pd.to_datetime(td["decided_at_utc"], utc=True)
    if "mass_survived" in td.columns:  # pipeline flattens nested objects; the survival mass is extracted before that
        td["mass"] = td["mass_survived"]
    else:
        td["mass"] = td["script_survival"].map(lambda s: s.get("mass_survived") if isinstance(s, dict) else np.nan)

    cards, rows = [], []
    for gid, g in lv.groupby("game_id"):
        cut = g["cut"].iloc[0]
        cands: list[Candidate] = []
        for r in g.itertuples():
            pm = next((x for x in (r.p_v2, r.p_v1, r.p_pl) if x == x and x is not None), None)
            pa_ = r.p_v1 if (r.p_v2 == r.p_v2 and r.p_v1 == r.p_v1) else None
            for side in ("yes", "no"):
                ask = r.yes_ask if side == "yes" else r.no_ask
                if not 0.02 <= ask <= 0.98:
                    continue
                mass = td[(td["ticker"] == r.ticker) & (td["side"] == side) & (td["t"] <= cut)].sort_values("t")["mass"].tail(1)
                cands.append(Candidate(ticker=r.ticker, title=f"{r.title} [{r.kind} {r.threshold}]", family=r.family, side=side, ask=float(ask),
                                       mid_yes=float(r.mid), p_model=None if pm is None else float(pm), p_model_alt=None if pa_ is None else float(pa_),
                                       survival=float(mass.iloc[0]) if len(mass) and mass.iloc[0] == mass.iloc[0] else None,
                                       factor=FACTOR.get((r.kind, side), ""), thesis="(research view; see thesis_card)",
                                       counter="market mid and model disagree" if pm is not None and abs(pm - r.mid) > 0.05 else "market is the only estimate; no demonstrated edge"))
        y = dict(zip(g["ticker"], g["y"], strict=True))
        for pol in ("strict", "research_unvalidated", "naive_ev"):
            card = build_card(str(gid), cands, w_fam, cls, policy=pol)
            for s in card["selected"]:
                yy = y[s["ticker"]]
                win = yy if s["side"] == "yes" else 1 - yy
                price = s["current_price"]
                rows.append({"policy": pol, "game_id": gid, "ticker": s["ticker"], "family": s["family"], "side": s["side"], "price": price,
                             "pnl": win - price - float(taker_fee(price)), "cost": price + float(taker_fee(price)), "ev_claimed": s["net_ev_per_contract"]})
            if pol == "strict" or card["decision"] == "BET":
                cards.append({**card, "policy": pol, "best_rejected": card["best_rejected"][:2]})
    res = pd.DataFrame(rows)
    summary: dict = {"games": int(lv["game_id"].nunique()), "audited_model_weights": w_fam, "family_evidence_class": cls}
    for pol in ("strict", "research_unvalidated", "naive_ev"):
        d = res[res["policy"] == pol] if len(res) else res
        if d.empty:
            summary[pol] = {"n_bets": 0, "games_with_bet": 0, "pass_rate": 1.0}
            continue
        roi = cluster_ratio_ci(d, "pnl", "cost")
        summary[pol] = {"n_bets": int(len(d)), "games_with_bet": int(d["game_id"].nunique()), "pass_rate": round(1 - d["game_id"].nunique() / lv["game_id"].nunique(), 3),
                        "roi_net": roi[0], "roi_lo95": roi[1], "roi_hi95": roi[2], "claimed_ev_per_contract": float(d["ev_claimed"].mean()),
                        "hit_rate": float((d["pnl"] + d["cost"]).mean()), "by_family": d.groupby("family").apply(lambda x: {"n": int(len(x)), "roi": float(x["pnl"].sum() / x["cost"].sum())}).to_dict(),
                        "by_side": d.groupby("side").apply(lambda x: {"n": int(len(x)), "roi": float(x["pnl"].sum() / x["cost"].sum())}).to_dict()}
    return summary, cards


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--derived", type=Path, required=True)
    ap.add_argument("--registry", type=Path, required=True)
    ap.add_argument("--audit", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--cards", type=Path)
    a = ap.parse_args()
    summ, cards = run(a.derived, a.registry, a.audit)
    a.out.write_text(json.dumps(summ, indent=1, default=float))
    if a.cards:
        a.cards.write_text(json.dumps(cards[:60], indent=1, default=float))
    print(json.dumps(summ, indent=1, default=float))
