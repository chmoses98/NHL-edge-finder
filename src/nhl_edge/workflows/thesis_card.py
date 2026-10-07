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
                "role_confidence": prow.get(m["ticker"], {}).get("meta_role_confidence"), "deployment_source": prow.get(m["ticker"], {}).get("meta_deployment_source"),
                "pp_unit": prow.get(m["ticker"], {}).get("meta_pp_unit"), "expected_toi_min": prow.get(m["ticker"], {}).get("meta_expected_toi_min")}
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
            "_ps": ps, "_saves": saves,  # in-memory only (research audits); "_" keys are never serialised
            "context": pregame_context(gi)}
    return GameDistribution(str(gi.game_id), gi.home_abbrev, gi.away_abbrev, hid, aid, f, bets, unpriced, lift, meta)


def pregame_context(gi: Any) -> dict[str, Any]:
    """The pregame availability / environment facts the script layer cites as dependencies (GameInputs at the cutoff)."""
    def goalie(st: Any) -> dict[str, Any] | None:
        if st is None:
            return None
        status = getattr(getattr(st, "status", None), "value", None) or str(getattr(st, "status", "") or "") or None
        return {"status": status, "name": getattr(st, "player_name", None), "player_id": getattr(st, "player_id", None),
                "confidence": None if getattr(st, "confidence", None) is None else round(float(st.confidence), 3)}
    try:
        return {"goalies": {"home": goalie(getattr(gi, "home_goalie", None)), "away": goalie(getattr(gi, "away_goalie", None))},
                "home_rest_days": getattr(gi, "home_rest_days", None), "away_rest_days": getattr(gi, "away_rest_days", None),
                "home_b2b": getattr(gi, "home_b2b", None), "away_b2b": getattr(gi, "away_b2b", None),
                "lam_home": None if getattr(gi, "lam_home", None) is None else round(float(gi.lam_home), 4),
                "lam_away": None if getattr(gi, "lam_away", None) is None else round(float(gi.lam_away), 4),
                "trusted": getattr(gi, "trusted", None), "input_reasons": list(getattr(gi, "reasons", None) or [])}
    except Exception:  # noqa: BLE001 - context is descriptive; never a failure of the distribution
        return {}


def _decision_id(ticker: str, side: str, ts: str, run_id: str) -> str:
    return hashlib.sha256(f"{ticker}|{side}|{ts}|{run_id}|{THESIS_VERSION}".encode()).hexdigest()[:32]


def snapshot_id(run_id: str, ts: str) -> str:
    """Immutable identity of ONE thesis-card generation (one ``nhl simulate`` invocation): every thesis_games /
    thesis_decisions row of that generation carries it. A worker ``run_id`` spans many generations (one per simulate
    cycle), so ``run_id`` alone is NOT a snapshot identity; (run_id, decided_at_utc) is, and this hashes exactly that
    pair, so rows written before the field existed reconstruct to the same id (``thesis_postmortem.snapshot_key``)."""
    return "snap-" + hashlib.sha256(f"{run_id}|{ts}".encode()).hexdigest()[:20]


def decision_history(ledger: Any, now: datetime, hours: float = 24.0) -> dict[str, dict[str, Any]]:
    """bet_id -> {first_mid, first_decided_at_utc} from thesis decisions logged in the ``hours`` before ``now`` (rows
    observed strictly before ``now`` only: point-in-time safe on a full archive copy). Feeds the market-movement
    corroboration check; an unreadable ledger simply means "no history" (the check reports UNAVAILABLE)."""
    from datetime import timedelta

    from nhl_edge.timeutil import parse_iso

    out: dict[str, dict[str, Any]] = {}
    if ledger is None:
        return out
    lo = now - timedelta(hours=hours)
    try:
        for r in ledger.iter_rows("thesis_decisions", dt_from=lo.date().isoformat(), dt_to=now.date().isoformat()):
            try:
                t = parse_iso(r["decided_at_utc"])
                obs = parse_iso(r.get("_observed_at_utc") or r["decided_at_utc"])
            except (KeyError, ValueError, TypeError):
                continue
            if not (lo <= t < now and obs < now) or r.get("p_kalshi_mid") is None:
                continue
            cur = out.get(r["bet_id"])
            if cur is None or t < cur["_t"]:
                out[r["bet_id"]] = {"first_mid": float(r["p_kalshi_mid"]), "first_decided_at_utc": r["decided_at_utc"], "_t": t}
    except Exception:  # noqa: BLE001 - history is optional evidence, never a failure
        return {}
    return {k: {kk: vv for kk, vv in v.items() if kk != "_t"} for k, v in out.items()}


def run_thesis_card(dists: list[GameDistribution], ledger: Any, now: datetime, sportsbook_rows: list[dict[str, Any]] | None, run_id: str,
                    cfg: PortfolioConfig | None = None, gov: Any = None) -> dict[str, Any]:
    import time

    from nhl_edge.thesis.benchmark import consensus_moneyline
    from nhl_edge.thesis.governance import governance_config
    from nhl_edge.thesis.reliability import reliability_table
    from nhl_edge.timeutil import iso

    t0 = time.perf_counter()
    cfg = cfg or portfolio_config()
    gov = gov or governance_config()
    fams = sorted({b.family for d in dists for b in d.bets})
    rel = reliability_table(ledger, now, fams)
    analyses = []
    for d in dists:
        cons = consensus_moneyline(sportsbook_rows or [], d.game_id, d.home_team_id, d.away_team_id)
        analyses.append(analyze_game(d, rel, cons, cfg))
    card = finalize_slate(analyses, cfg, rel, gov, decision_history(ledger, now))
    ts = iso(now)
    snap = snapshot_id(run_id, ts)
    card["generated_at_utc"] = ts
    card["run_id"] = run_id
    card["snapshot_id"] = snap
    games_rows, decision_rows, script_rows = [], [], []
    scripts_by_game = _scripts_v1(analyses, card, ts=ts, run_id=run_id, snap=snap, rows=script_rows)
    for a, g in zip(analyses, card["games"]):
        surv_by_bet = {c["bet_id"]: c for c in (scripts_by_game.get(g["game_id"]) or {}).get("candidates") or []}
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
            rs = a["research"][b.bet_id]
            decision_rows.append({
                "decision_id": _decision_id(b.ticker, b.side, ts, run_id), "decided_at_utc": ts, "run_id": run_id, "thesis_version": THESIS_VERSION, "card_version": CARD_VERSION,
                "snapshot_id": snap, "logical_wager_key": f"{g['game_id']}|{b.bet_id}",
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
                "expression_fidelity": a["fidelity"].get(b.bet_id), "research_status": rs["status"], "research_reasons": rs["reasons"],
                "research_stake_dollars": int(rs["research_stake_dollars"]), "research_stake_detail": rs.get("research_stake"),
                "market_disagreement": rs["market_disagreement"], "calibration_warning": rs["calibration_warning"], "corroboration": rs["corroboration"],
                "selection_override": next((o for o in a.get("overrides") or [] if b.bet_id in (o.get("selected"), o.get("replaced"))), None),
                "research_bankroll": gov.research_bankroll,
                "script_survival": _survival_fields(surv_by_bet.get(b.bet_id)),
            })
        games_rows.append({"game_id": g["game_id"], "decided_at_utc": ts, "run_id": run_id, "snapshot_id": snap, "thesis_version": THESIS_VERSION, "card_version": CARD_VERSION,
                           "matchup": g["matchup"], "meta": g["meta"], "research_status": g.get("research_status"), "review": g.get("review"),
                           "selection_overrides": a.get("overrides") or [], "research_governance": card.get("research_governance"),
                           "n_sims": g["n_sims"], "scripts": g["scripts"], "dimensions": g["dimensions"], "thesis_events": g["thesis_events"],
                           "sportsbook_consensus": g["sportsbook_consensus"], "portfolios": g["portfolios"], "joint_card_check": g["joint_card_check"],
                           "expressions": g["expressions"], "recommended": list(rec), "card_status": card["status"], "gate_status": card["gate"]["status"],
                           "portfolio_config": cfg.to_dict(), "authority": "RESEARCH_ONLY"})
    card["timings_ms"] = {"total": round(1000 * (time.perf_counter() - t0), 1), "by_game": {g["game_id"]: g["timings_ms"] for g in card["games"]}}
    card["_ledger"] = {"thesis_games": _jsonable(games_rows), "thesis_decisions": _jsonable(decision_rows)}
    if script_rows:
        card["_ledger"]["script_forecasts"] = _jsonable(script_rows)
    log.info(kv(event="thesis_card", status=card["status"], games=len(card["games"]), recommended=sum(len(g["card"]) for g in card["games"]),
                ms=card["timings_ms"]["total"]))
    return card


def _scripts_v1(analyses: list[dict[str, Any]], card: dict[str, Any], *, ts: str, run_id: str, snap: str, rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """NHL_SCRIPT_V1 per game (scripts, script-conditioned market matrix, survival, research candidates). Attached to each card
    game as ``scripts_v1``; one immutable ``script_forecasts`` row per game. Contained per game: a failure is recorded on the
    game (``scripts_v1_error``) and never touches the card, its gate, V1, V2 or PLAYER_SIM_V1."""
    from nhl_edge.scripts_v1.build import forecast_row, game_research

    out: dict[str, dict[str, Any]] = {}
    for a, g in zip(analyses, card["games"]):
        try:
            gr = game_research(a)
            g["scripts_v1"] = gr
            out[g["game_id"]] = gr
            rows.append(forecast_row(gr, decided_at=ts, run_id=run_id, snapshot_id=snap, start_time_utc=g["meta"].get("start_time_utc")))
        except Exception as e:  # noqa: BLE001 - research layer; never a gate
            g["scripts_v1_error"] = f"{type(e).__name__}: {str(e)[:200]}"
            log.warning(kv(event="scripts_v1_failed", game=g.get("game_id"), err=str(e)[:300]))
    return out


def _survival_fields(c: dict[str, Any] | None) -> dict[str, Any] | None:
    if not c:
        return None
    sv = c["survival"]
    return {"script_version": "NHL_SCRIPT_V1", "robustness": c["robustness"], "mass_survived": sv["mass_survived"],
            "n_major_survived": sv["n_major_survived"], "n_major": sv["n_major"], "failure_script": sv["failure_script"],
            "worst_major_ev": sv["worst_major_ev"], "research_rank": c["rank"], "exposure_group": c["exposure_group"],
            "dependencies": [d["flag"] for d in c["dependencies"]]}


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
                      "snapshot_id": card.get("snapshot_id"), "research_governance": card.get("research_governance"),
                      "recommended": [{"bet_id": e["bet_id"], "title": e["contract"]["title"], "side": e["contract"]["side"], "stake": e["recommended_stake"]["dollars"],
                                       "research_status": (e.get("research_governance") or {}).get("status"),
                                       "research_stake": (e.get("research_governance") or {}).get("research_stake_dollars"),
                                       "fidelity": (e.get("expression_fidelity") or {}).get("fidelity_class"),
                                       "p": e["fair_probability"]["p_model_joint_draw"], "p_adj": e["fair_probability"]["p_confidence_adjusted"],
                                       "ask": e["executable_price"].get("ask_cents") if isinstance(e["executable_price"], dict) else None,
                                       "primary_thesis": e["primary_thesis"].get("key")} for g in card["games"] for e in g["card"]]})


def markdown(card: dict[str, Any], max_scripts: int = 6, max_board: int = 8) -> str:
    f3 = lambda x: "" if x is None else f"{x:.3f}"  # noqa: E731
    L = [f"# NHL THESIS CARD — {card['authority']} — status **{card['status']}**", "",
         f"generated {card.get('generated_at_utc')} · {card['thesis_version']} · gate {card['gate']['status']} · nominal bankroll ${card['portfolio_config']['bankroll']:.0f} "
         f"(quarter Kelly; caps bet {card['portfolio_config']['max_bet_frac']:.0%} / game {card['portfolio_config']['max_game_frac']:.0%} / thesis "
         f"{card['portfolio_config']['max_thesis_frac']:.0%} / slate {card['portfolio_config']['max_slate_frac']:.0%})", ""]
    gv = card.get("research_governance") or {}
    if gv:
        L += [f"**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll ${gv['research_bankroll']:.0f}, whole-dollar stakes, max "
              f"${gv['max_research_stake']:.0f} per wager; ≤ {gv['max_funded_player_props_per_game']} funded player prop per game; ≤ "
              f"{gv['max_funded_low_prob_player_props_per_slate']} funded player props with adjusted p < {gv['low_prob_threshold']:.2f} per slate; player props "
              f"{gv['disagreement_threshold'] * 100:.0f}+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.", ""]
    if card["status"] == "INCOMPLETE":
        L += ["**CARD NOT EMITTED: the completion gate failed.**", ""] + [f"- {x}" for x in card["gate"]["failures"][:20]] + [""]
    sp = card["slate_portfolios"]
    L += ["## Slate portfolios (simulated P/L on the joint draws)", "",
          "EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted "
          "probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.", "",
          "| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for k, lab in (("A", "A highest edges (independent)"), ("B", "B thesis-diversified (joint) ← optimiser card"), ("C", "C best expression per thesis"),
                   ("R", "R FUNDED research stakes")):
        v = sp.get(k) or {}
        if k == "R" and not v:
            continue
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
            L += ["", "**Card**", "", "| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |",
                  "|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|"]
            for e in g["card"]:
                rg = e.get("research_governance") or {}
                fd = e.get("expression_fidelity") or {}
                cap = fd.get("thesis_capture")
                L.append(f"| {e['contract']['title']} {e['contract']['side']} | {e['executable_price'].get('ask_cents')} | {f3(e['fair_probability']['p_model_joint_draw'])} | "
                         f"{f3(e['fair_probability']['p_confidence_adjusted'])} | {e['estimated_edge']['ev_raw_per_contract']:+.3f} | {e['estimated_edge']['ev_adjusted_per_contract']:+.3f} | "
                         f"${e['recommended_stake']['dollars']:.2f} | {rg.get('label', '-')} | ${rg.get('research_stake_dollars', 0)} | {e['primary_thesis'].get('key')} | "
                         f"{fd.get('fidelity_class', '-')}{'' if cap is None else f' ({cap:.2f})'} | {e['family_reliability']['label']} | {e['family_reliability']['benchmark_category']} |")
            for e in g["card"]:
                rels = e["same_game_relationships"]
                rel_txt = "; ".join(f"{k}: {v.get('relationship')} (phi {v.get('phi')})" for k, v in rels.items()) if "status" not in rels else rels["reason"]
                alt = e["best_alternative"]
                L += [f"- **{e['contract']['title']} {e['contract']['side']}** — thesis: {e['primary_thesis'].get('label')}; "
                      f"alternative: {alt.get('bet_id') if 'status' not in alt else alt['reason']}; why: {e['reason_chosen']}; relationships: {rel_txt}; "
                      f"failure: {(e['failure_case'].get('failure_thesis') or {}).get('label', '-')}"]
        else:
            L += ["", "_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_"]
        rv = g.get("review") or {}
        if rv:
            L += ["", "**Review**: scripts " + ", ".join(f"{x['script']} {x['frequency']:.2f}" for x in rv.get("top_scripts", [])) + "."]
            for t in rv.get("theses", [])[:3]:
                hf, be = t.get("highest_fidelity") or {}, t.get("best_adjusted_ev") or {}
                L.append(f"- thesis {t['thesis']} (p {t.get('p_thesis')}): highest fidelity {hf.get('bet_id', '-')} [{hf.get('fidelity_class', '-')}], "
                         f"best adjusted EV {be.get('bet_id', '-')}" + (" (same contract)" if t.get("same_contract") else f" — {t['choice']}"))
            for x in rv.get("bets", []):
                flag = []
                if x["large_disagreement"]:
                    flag.append(f"LARGE MARKET DISAGREEMENT {x['market_disagreement_pts']} pts")
                if x["expression_kind"] == "FRAGILE_PLAYER":
                    flag.append("fragile player expression")
                L.append(f"- {x['bet_id']}: {x['status_label']}; family {x['family_trust']}; {x['fails_even_if_thesis_right']}"
                         + (f"; {'; '.join(flag)}" if flag else "") + (f"; opposing: {x['opposing_evidence'][0]}" if x["opposing_evidence"] else ""))
            for o in rv.get("overrides", []):
                L.append(f"- override: {o['text']}")
        pf = g["portfolios"]
        L.append("")
        L.append("portfolios: " + " · ".join(f"{k} EV {pf[k].get('expected_profit', 0):+.2f} (adj {pf[k].get('expected_profit_confidence_adjusted') or 0:+.2f}) on "
                                             f"${pf[k].get('total_stake', 0):.2f}, P(profit) {pf[k].get('p_profit', 0)}, adj growth {pf[k].get('adjusted_log_growth_bp') or 0:.1f} bp"
                                             for k in ("A", "B", "C", "R") if k in pf))
        if g.get("equivalent_contracts"):
            L.append("equivalent contracts collapsed: " + "; ".join(f"{q['dropped']} == {q['kept']}" for q in g["equivalent_contracts"]))
    L += ["", f"_{card['note']}_", ""]
    return "\n".join(L)
