"""RUN NHL thesis card (RESEARCH_ONLY): the game-script / thesis / portfolio layer on top of the PLAYER_SIM_V1 draw.

``shadow_player`` keeps each game's joint draw in memory just long enough to build a :class:`GameDistribution`
(``build_game_distribution``); ``nhl simulate`` then calls :func:`run_thesis_card`, which

1. labels every family's reliability from evaluation artifacts and the PIT-safe prospective ledger;
2. reads the latest sportsbook moneylines observed at or before the cutoff (quarantined kind, benchmark only);
3. runs ``thesis.engine`` per game and for the slate (scripts, mapping, expressions, joint matrix, portfolios, gate);
4. writes ``thesis_card`` into slate.json / packet.json, ``card.md`` next to them, and two append-only ledger kinds:
   ``thesis_games`` (per game: scripts, thesis events, portfolios, joint card check) and ``thesis_decisions`` (per
   shortlisted bet: the complete pregame decision state, chosen or rejected, and why) for the postmortem.

Never a gate on V1 / V2 / PLAYER_SIM_V1: any exception is caught by the caller and recorded.
"""

from __future__ import annotations

import hashlib
import os
from datetime import datetime
from typing import Any

import numpy as np

from nhl_edge.log import get_logger, kv
from nhl_edge.thesis import CARD_VERSION, THESIS_VERSION
from nhl_edge.thesis.engine import GameDistribution, analyze_game, finalize_slate
from nhl_edge.thesis.features import DrawFeatures
from nhl_edge.thesis.mapping import Bet
from nhl_edge.thesis.outcomes import capture_view, contract_outcome
from nhl_edge.thesis.portfolio import PortfolioConfig

log = get_logger(__name__)


def enabled() -> bool:
    return os.environ.get("NHL_EDGE_THESIS_CARD", "1") not in ("0", "false", "False", "")


def portfolio_config() -> PortfolioConfig:
    try:
        bank = float(os.environ.get("NHL_EDGE_CARD_BANKROLL", "1000"))
    except ValueError:
        bank = 1000.0
    return PortfolioConfig(bankroll=bank if bank > 0 else 1000.0)


def build_game_distribution(gi: Any, res: Any, ps: Any, saves: dict[int, Any], goalie_team: dict[int, int], priced: list[tuple[dict[str, Any], Any, int | None]],
                            v1_rows: list[dict[str, Any]], fee_for: Any, market_ts: datetime | None, now: datetime, minutes: float | None,
                            top_players: list[dict[str, Any]], start_time_utc: str | None = None, player_rows: list[dict[str, Any]] | None = None) -> GameDistribution:
    """``priced``: every joined (market, contract, resolved player id or None) of the game, game and player families."""
    from nhl_edge.execution.economics import compute_economics, market_implied_probability
    from nhl_edge.timeutil import iso

    hid, aid = int(gi.home_team_id), int(gi.away_team_id)
    ab = {hid: gi.home_abbrev, aid: gi.away_abbrev}
    f = DrawFeatures.from_simulation(res, ps, saves[hid], saves[aid], gi.home_abbrev, gi.away_abbrev)
    cap = capture_view(res)
    v1 = {r["ticker"]: r.get("p_data_only") for r in v1_rows or []}
    prow = {r["ticker"]: r for r in player_rows or []}
    bets: list[Bet] = []
    unpriced: list[dict[str, Any]] = []
    for m, c, pid in priced:
        y, p, reason = contract_outcome(c, pid, cap, ps, saves, goalie_team, hid, aid)
        if y is None:
            unpriced.append({"ticker": m["ticker"], "family": c.family, "title": m.get("title"), "reason": reason})
            continue
        sched = fee_for(m)
        econ = compute_economics(m, p, schedule=sched, observed_at=market_ts, now=now)
        mid = market_implied_probability(m).p_mid
        team = opp = None
        if pid is not None:
            found = ps.player(pid)
            tid = found[1].team_id if found else goalie_team.get(int(pid))
            if tid in ab:
                team, opp = ab[tid], ab[aid if tid == hid else hid]
        elif c.team_id in ab:
            team, opp = ab[c.team_id], ab[aid if c.team_id == hid else hid]
        meta = {"stale": bool(econ.stale), "crossed": bool(econ.crossed), "not_pregame": minutes is not None and minutes <= 0,
                "market_observed_at_utc": iso(market_ts) if market_ts else None, "p_v1": v1.get(m["ticker"]), "player_id": pid, "_schedule": sched,
                "contract_team": ab.get(c.team_id) if c.family == "game_winner" else None, "spread_cents": econ.spread_cents, "price_reason": reason, "threshold": c.threshold,
                "projection_quality": prow.get(m["ticker"], {}).get("meta_projection_quality"), "uncertainty_flags": prow.get(m["ticker"], {}).get("meta_uncertainty_flags"),
                "role_confidence": prow.get(m["ticker"], {}).get("meta_role_confidence"), "deployment_source": prow.get(m["ticker"], {}).get("meta_deployment_source")}
        for side, ys, se in (("yes", y, econ.yes), ("no", ~y, econ.no)):
            bets.append(Bet(f"{m['ticker']}|{side}", m["ticker"], side, m.get("title") or m["ticker"], c.family, str(gi.game_id), ys, float(ys.mean()), se.price_cents,
                            se.fee_per_contract, None if mid is None else (mid if side == "yes" else 1.0 - mid), team, opp, dict(meta)))
    lift = {}
    for tp in top_players or []:
        found = ps.player(tp["player_id"])
        if found:
            d, _, i = found
            lift[f"{tp['name']} ({tp['team']})"] = d.points[:, i] >= 1
    meta = {"start_time_utc": start_time_utc, "minutes_to_start": None if minutes is None else round(minutes, 1), "seed": int(res.seed),
            "lam_home": float(res.home.lam) if res.home else None, "lam_away": float(res.away.lam) if res.away else None,
            "source": "PLAYER_SIM_V1 joint draw (nhl-sim-2.0 team path + player allocation + saves); game markets priced on the same draw",
            "_ps": ps, "_saves": saves}  # in-memory only (research audits); "_" keys are never serialised
    return GameDistribution(str(gi.game_id), gi.home_abbrev, gi.away_abbrev, hid, aid, f, bets, unpriced, lift, meta)


def _decision_id(ticker: str, side: str, ts: str, run_id: str) -> str:
    return hashlib.sha256(f"{ticker}|{side}|{ts}|{run_id}|{THESIS_VERSION}".encode()).hexdigest()[:32]


def run_thesis_card(dists: list[GameDistribution], ledger: Any, now: datetime, sportsbook_rows: list[dict[str, Any]] | None, run_id: str,
                    cfg: PortfolioConfig | None = None) -> dict[str, Any]:
    import time

    from nhl_edge.thesis.benchmark import consensus_moneyline
    from nhl_edge.thesis.reliability import reliability_table
    from nhl_edge.timeutil import iso

    t0 = time.perf_counter()
    cfg = cfg or portfolio_config()
    fams = sorted({b.family for d in dists for b in d.bets})
    rel = reliability_table(ledger, now, fams)
    analyses = []
    for d in dists:
        cons = consensus_moneyline(sportsbook_rows or [], d.game_id, d.home_team_id, d.away_team_id)
        analyses.append(analyze_game(d, rel, cons, cfg))
    card = finalize_slate(analyses, cfg, rel)
    ts = iso(now)
    card["generated_at_utc"] = ts
    card["run_id"] = run_id
    games_rows, decision_rows = [], []
    for a, g in zip(analyses, card["games"]):
        rec = {e["bet_id"]: e for e in g["card"]}
        short, fB = a["portfolios"]["B"]
        stake = {b.bet_id: float(s) * cfg.bankroll for b, s in zip(short, fB)}
        pairs = a["joint"]["pairs"]
        for b in short:
            prof = a["profiles"][b.bet_id]
            e = a["econ"][b.bet_id]
            th = a["thesis_of"][b.bet_id]
            exp = a["expressions"].get(th) or {}
            rels = {}
            for p in pairs:
                if b.bet_id in (p["a"], p["b"]):
                    o = p["b"] if p["a"] == b.bet_id else p["a"]
                    rels[o] = {"relationship": p["relationship"], "phi": p["phi"], "p_both": p["p_a_and_b"]}
            chosen = b.bet_id in rec
            why_not = None
            if not chosen:
                dups = [o for o, r in rels.items() if r["relationship"] == "DUPLICATIVE" and o in rec]
                same = [o for o in rec if a["thesis_of"].get(o) == th]
                why_not = (f"shares one exposure budget with duplicative {dups}" if dups else f"thesis budget '{th}' allocated to {same}" if same
                           else "joint optimum gives it less than the minimum stake (adds too little growth given the rest of the card)")
            cnt = a["counts"][a["idx"][b.bet_id]]
            dist = a["dist"]
            by_script = {dist.taxonomy.primary_key(k): round(float(cnt[k] / (dist.freq[k] * g["n_sims"])), 4) for k in range(len(dist.freq)) if dist.freq[k] > 0}
            decision_rows.append({
                "decision_id": _decision_id(b.ticker, b.side, ts, run_id), "decided_at_utc": ts, "run_id": run_id, "thesis_version": THESIS_VERSION, "card_version": CARD_VERSION,
                "game_id": g["game_id"], "matchup": g["matchup"], "start_time_utc": g["meta"].get("start_time_utc"), "minutes_to_start": g["meta"].get("minutes_to_start"),
                "ticker": b.ticker, "side": b.side, "bet_id": b.bet_id, "title": b.title, "family": b.family, "team": b.team, "opponent": b.opponent,
                "executable_price_cents": b.price_cents, "cost_per_contract": b.cost, "market_observed_at_utc": b.meta.get("market_observed_at_utc"),
                "p_model": b.p, "p_adjusted": e.p_adj, "p_kalshi_mid": b.p_mid, "p_sportsbook": a["book"].get(b.bet_id), "p_v1": b.meta.get("p_v1"),
                "benchmark_category": a["bench"][b.bet_id], "reliability": a["rel"][b.bet_id], "ev_raw": e.ev_raw, "ev_adjusted": e.ev_adj, "growth_bp": e.growth_bp,
                "script_mapping": prof["main_scripts"], "p_win_by_script": by_script, "thesis_concentration": prof["concentration"], "primary_thesis": prof["primary_thesis"],
                "secondary_thesis": prof["secondary_thesis"], "failure_thesis": prof["failure_thesis"], "team_offense": prof.get("team_offense"),
                "joint_relationships": rels, "alternatives_considered": [{k: r.get(k) for k in ("bet_id", "price_cents", "p_model", "ev_raw", "ev_adjusted", "growth_bp", "eligible")}
                                                                         for r in (exp.get("rows") or []) if r["bet_id"] != b.bet_id][:6],
                "best_expression_of_thesis": exp.get("best"), "chosen": chosen, "stake_dollars": round(stake.get(b.bet_id, 0.0), 2),
                "why_selected": rec[b.bet_id]["reason_chosen"] if chosen else None, "why_rejected": why_not, "card_status": card["status"], "authority": "RESEARCH_ONLY",
            })
        games_rows.append({"game_id": g["game_id"], "decided_at_utc": ts, "run_id": run_id, "thesis_version": THESIS_VERSION, "matchup": g["matchup"], "meta": g["meta"],
                           "n_sims": g["n_sims"], "scripts": g["scripts"], "dimensions": g["dimensions"], "thesis_events": g["thesis_events"],
                           "sportsbook_consensus": g["sportsbook_consensus"], "portfolios": g["portfolios"], "joint_card_check": g["joint_card_check"],
                           "expressions": g["expressions"], "recommended": list(rec), "card_status": card["status"], "gate_status": card["gate"]["status"],
                           "portfolio_config": cfg.to_dict(), "authority": "RESEARCH_ONLY"})
    card["timings_ms"] = {"total": round(1000 * (time.perf_counter() - t0), 1), "by_game": {g["game_id"]: g["timings_ms"] for g in card["games"]}}
    card["_ledger"] = {"thesis_games": _jsonable(games_rows), "thesis_decisions": _jsonable(decision_rows)}
    log.info(kv(event="thesis_card", status=card["status"], games=len(card["games"]), recommended=sum(len(g["card"]) for g in card["games"]),
                ms=card["timings_ms"]["total"]))
    return card


def _jsonable(x: Any) -> Any:
    if isinstance(x, dict):
        return {k: _jsonable(v) for k, v in x.items() if not str(k).startswith("_")}
    if isinstance(x, (list, tuple)):
        return [_jsonable(v) for v in x]
    if isinstance(x, np.generic):
        return x.item()
    return x


def packet_view(card: dict[str, Any]) -> dict[str, Any]:
    return _jsonable({k: v for k, v in card.items() if k != "_ledger"})


def slate_view(card: dict[str, Any]) -> dict[str, Any]:
    """Compact block for slate.json (the full analysis lives in packet.json)."""
    return _jsonable({"status": card["status"], "card_emitted": card["card_emitted"], "gate": card["gate"], "slate_portfolios": card["slate_portfolios"],
                      "timings_ms": card.get("timings_ms"), "thesis_version": card["thesis_version"], "authority": card["authority"],
                      "recommended": [{"bet_id": e["bet_id"], "title": e["contract"]["title"], "side": e["contract"]["side"], "stake": e["recommended_stake"]["dollars"],
                                       "p": e["fair_probability"]["p_model_joint_draw"], "p_adj": e["fair_probability"]["p_confidence_adjusted"],
                                       "ask": e["executable_price"].get("ask_cents") if isinstance(e["executable_price"], dict) else None,
                                       "primary_thesis": e["primary_thesis"].get("key")} for g in card["games"] for e in g["card"]]})


def markdown(card: dict[str, Any], max_scripts: int = 6, max_board: int = 8) -> str:
    f3 = lambda x: "" if x is None else f"{x:.3f}"  # noqa: E731
    L = [f"# NHL THESIS CARD — {card['authority']} — status **{card['status']}**", "",
         f"generated {card.get('generated_at_utc')} · {card['thesis_version']} · gate {card['gate']['status']} · nominal bankroll ${card['portfolio_config']['bankroll']:.0f} "
         f"(quarter Kelly; caps bet {card['portfolio_config']['max_bet_frac']:.0%} / game {card['portfolio_config']['max_game_frac']:.0%} / thesis "
         f"{card['portfolio_config']['max_thesis_frac']:.0%} / slate {card['portfolio_config']['max_slate_frac']:.0%})", ""]
    if card["status"] == "INCOMPLETE":
        L += ["**CARD NOT EMITTED: the completion gate failed.**", ""] + [f"- {x}" for x in card["gate"]["failures"][:20]] + [""]
    sp = card["slate_portfolios"]
    L += ["## Slate portfolios (simulated P/L on the joint draws)", "",
          "EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted "
          "probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.", "",
          "| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for k, lab in (("A", "A highest edges (independent)"), ("B", "B thesis-diversified (joint) ← card"), ("C", "C best expression per thesis")):
        v = sp.get(k) or {}
        L.append(f"| {lab} | {v.get('total_stake', 0):.2f} | {v.get('expected_profit', 0):+.2f} | {v.get('expected_profit_confidence_adjusted', 0):+.2f} | "
                 f"{v.get('median_profit', 0):+.2f} | {v.get('p_profit', 0):.3f} | {v.get('p10', 0):+.2f} | {v.get('p05', 0):+.2f} | "
                 f"{v.get('adjusted_log_growth_bp_sum_of_games', 0):.2f} |")
    for g in card["games"]:
        L += ["", f"## {g['matchup']}  ·  {g['n_sims']} joint draws  ·  {g['n_bets_mapped']} bet sides mapped, {g['n_candidates']} +EV candidates, {len(g['card'])} on card", ""]
        if g.get("sportsbook_consensus"):
            c = g["sportsbook_consensus"]
            L.append(f"sportsbook moneyline consensus ({c['n']} books): home {c['p_home']:.3f} / away {c['p_away']:.3f}")
        home, away = g["matchup"].split(" @ ")[1], g["matchup"].split(" @ ")[0]
        pk = [f"p_{home}_win", f"p_{away}_win", "p_overtime"]
        L += ["", f"**Game scripts** (shot control · environment · margin; {len(g['scripts'])} occur, top {max_scripts} shown)", "",
              "| script | freq | " + " | ".join(pk) + f" | goals | shots {home}/{away} | {home}/{away} starter saves | driver |", "|---|---:|---:|---:|---:|---:|---|---|---|"]
        for s in g["scripts"][:max_scripts]:
            L.append(f"| {s['name']} | {s['frequency']:.3f} | " + " | ".join(f"{s.get(k, 0):.2f}" for k in pk) +
                     f" | {s['total_goals']} | {s.get(home + '_shots')}/{s.get(away + '_shots')} | {s.get(home + '_starter_saves')}/{s.get(away + '_starter_saves')} | {s['driver']} |")
        if g["card"]:
            L += ["", "**Card**", "", "| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |", "|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|"]
            for e in g["card"]:
                L.append(f"| {e['contract']['title']} {e['contract']['side']} | {e['executable_price'].get('ask_cents')} | {f3(e['fair_probability']['p_model_joint_draw'])} | "
                         f"{f3(e['fair_probability']['p_confidence_adjusted'])} | {e['estimated_edge']['ev_raw_per_contract']:+.3f} | {e['estimated_edge']['ev_adjusted_per_contract']:+.3f} | "
                         f"${e['recommended_stake']['dollars']:.2f} | {e['primary_thesis'].get('key')} | {e['thesis_concentration'].get('top2')} | "
                         f"{e['family_reliability']['label']} | {e['family_reliability']['benchmark_category']} |")
            for e in g["card"]:
                rels = e["same_game_relationships"]
                rel_txt = "; ".join(f"{k}: {v.get('relationship')} (phi {v.get('phi')})" for k, v in rels.items()) if "status" not in rels else rels["reason"]
                alt = e["best_alternative"]
                L += [f"- **{e['contract']['title']} {e['contract']['side']}** — thesis: {e['primary_thesis'].get('label')}; "
                      f"alternative: {alt.get('bet_id') if 'status' not in alt else alt['reason']}; why: {e['reason_chosen']}; relationships: {rel_txt}; "
                      f"failure: {(e['failure_case'].get('failure_thesis') or {}).get('label', '-')}"]
        else:
            L += ["", "_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_"]
        pf = g["portfolios"]
        L.append("")
        L.append("portfolios: " + " · ".join(f"{k} EV {pf[k].get('expected_profit', 0):+.2f} (adj {pf[k].get('expected_profit_confidence_adjusted') or 0:+.2f}) on "
                                             f"${pf[k].get('total_stake', 0):.2f}, P(profit) {pf[k].get('p_profit', 0)}, adj growth {pf[k].get('adjusted_log_growth_bp') or 0:.1f} bp"
                                             for k in ("A", "B", "C")))
        if g.get("equivalent_contracts"):
            L.append("equivalent contracts collapsed: " + "; ".join(f"{q['dropped']} == {q['kept']}" for q in g["equivalent_contracts"]))
    L += ["", f"_{card['note']}_", ""]
    return "\n".join(L)
