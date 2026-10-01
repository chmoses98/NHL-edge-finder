"""``nhl simulate``: the RUN NHL job.

For every NOT_STARTED game on the target ET date (latest archived schedule snapshot, start strictly after now):
  1. assemble point-in-time inputs from the archived context kinds observed at or before ``now`` (the cutoff);
  2. simulate the game (``sim/engine.py``) with a deterministic seed; check ladder consistency;
  3. map every archived Kalshi market for the game to a Contract and price it from the same draws;
  4. compute executable economics (asks, fees) from the latest market board strictly before now;
  5. freeze ContractPrediction + Contract rows in the ledger (append-only) and write slate.json / slate.md / packet.json.

Model arms on every row: DATA_ONLY_V1 (hockey data only), MARKET_BASELINE (Kalshi midpoint), MARKET_ANCHORED_V1
(logit blend, market weight ``MARKET_ANCHOR_WEIGHT`` prior recorded on the row; not independent evidence).
Authority is RESEARCH_ONLY for every family. Positive edge rows are reported, never recommended.
"""

from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

from nhl_edge import (
    AUTHORITY,
    DATA_ONLY_MODEL_VERSION,
    DATA_ONLY_V2_MODEL_VERSION,
    FEATURE_VERSION,
    MARKET_ANCHORED_MODEL_VERSION,
    SIM_VERSION,
)
from nhl_edge.archive.ledger import Ledger, entry_observed_at
from nhl_edge.archive.reconstruct import DeltaChainError, reconstruct_at
from nhl_edge.data.moneypuck import mp_season
from nhl_edge.data.nhl_api import season_id_for
from nhl_edge.execution.economics import compute_economics, market_implied_probability
from nhl_edge.features.build import build_game_inputs, resolve_goalie_ids
from nhl_edge.features.ratings import inv_logit, logit
from nhl_edge.identity.teams import registry
from nhl_edge.kalshi.contracts import build_contract, game_key
from nhl_edge.kalshi.fees import DEFAULT_SCHEDULE, FeeSchedule
from nhl_edge.kalshi.ontology import Ontology
from nhl_edge.log import get_logger, kv
from nhl_edge.players import PLAYER_MODEL_VERSION
from nhl_edge.pricing.price import price_contract
from nhl_edge.schemas.core import GameStatus
from nhl_edge.schemas.prediction import Authority, ContractPrediction, Gate
from nhl_edge.sim.engine import SimConfig, ladder_violations, simulate_game
from nhl_edge.timeutil import et_date, iso, parse_iso, utcnow

log = get_logger(__name__)

MARKET_ANCHOR_WEIGHT = 0.80  # prior; MARKET_ANCHORED_V1 = inv_logit(w*logit(p_mkt) + (1-w)*logit(p_data))
HORIZONS_MIN = ((1440, "T-24h"), (720, "T-12h"), (360, "T-6h"), (180, "T-3h"), (90, "T-90m"), (60, "T-60m"), (30, "T-30m"), (10, "T-10m"))
MAX_MARKET_AGE_MIN = 30.0
MAX_CONTEXT_AGE_MIN = 24 * 60.0


def _read_latest(ledger: Ledger, kind: str, cutoff: datetime) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Rows of the newest partition of ``kind`` observed at or before ``cutoff`` (never a later one)."""
    entries = [e for e in ledger.manifest() if e.kind == kind and entry_observed_at(e) <= cutoff]
    if not entries:
        return [], {"kind": kind, "path": None, "observed_at_utc": None}
    e = max(entries, key=entry_observed_at)
    rows = []
    with gzip.open(ledger.root / e.path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows, {"kind": kind, "path": e.path, "observed_at_utc": e.observed_at_utc, "age_min": (cutoff - entry_observed_at(e)).total_seconds() / 60}


def _read_all(ledger: Ledger, kind: str, cutoff: datetime) -> list[dict[str, Any]]:
    """All rows of a kind observed at or before cutoff (for append-only observation kinds like goalie observations)."""
    out = []
    for e in ledger.manifest():
        if e.kind != kind or entry_observed_at(e) > cutoff:
            continue
        with gzip.open(ledger.root / e.path, "rt", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    out.append(json.loads(line))
    return out


def horizon_label(minutes: float) -> str:
    for m, lab in HORIZONS_MIN:
        if minutes >= m:
            return lab
    return "T-<10m"


def _pred_id(ticker: str, ts: str, model: str, run_id: str) -> str:
    return hashlib.sha256(f"{ticker}|{ts}|{model}|{run_id}".encode()).hexdigest()[:32]


def market_anchored(p_data: float | None, p_mkt: float | None, w: float = MARKET_ANCHOR_WEIGHT) -> float | None:
    if p_data is None or p_mkt is None:
        return None
    return inv_logit(w * logit(p_mkt) + (1 - w) * logit(p_data))


def seed_for(game_id: str, date: str) -> int:
    return int(hashlib.sha256(f"{game_id}|{date}|{SIM_VERSION}|{DATA_ONLY_MODEL_VERSION}".encode()).hexdigest()[:8], 16)


def _series_fee(series_rows: dict[str, dict[str, Any]], m: dict[str, Any]) -> FeeSchedule:
    s = series_rows.get(str(m.get("series_ticker") or str(m.get("ticker", "")).split("-")[0]))
    return FeeSchedule.from_series(s) if s else DEFAULT_SCHEDULE


def run_simulate(out_root: Path, data_root: Path, date: str | None = None, n_sims: int = 0, seed: int | None = None, now: datetime | None = None,
                 write: bool = True) -> int:
    now = now or utcnow()
    target = date or et_date(now)
    ledger = Ledger(out_root)
    onto = Ontology.load()
    reg = registry()
    sched, sched_meta = _read_latest(ledger, "context/schedule", now)
    if not sched:
        print(json.dumps({"error": "no schedule snapshot at or before now; run `nhl context` first", "date": target}))
        return 2
    games = [g for g in sched if g["game_date_et"] == target]
    not_started = [g for g in games if parse_iso(g["start_time_utc"]) > now and g.get("status") in (GameStatus.NOT_STARTED.value, None)]
    skipped = [{"game_id": g["game_id"], "status": g.get("status"), "start_time_utc": g["start_time_utc"]} for g in games if g not in not_started]
    team_games, tg_meta = _read_latest(ledger, "context/team_games", now)
    goalie_stats, gs_meta = _read_latest(ledger, "context/goalie_stats", now)
    rosters, ro_meta = _read_latest(ledger, "context/rosters", now)
    goalie_obs = resolve_goalie_ids(_read_all(ledger, "context/goalie_observations", now), rosters, goalie_stats)
    injuries, inj_meta = _read_latest(ledger, "context/injuries", now)
    board = None
    board_note = None
    if any(e.kind == "kalshi/markets" and entry_observed_at(e) <= now for e in ledger.manifest()):
        try:
            board = reconstruct_at(out_root, now)  # the board as of the latest tick at or before the cutoff, never later
        except (DeltaChainError, ValueError) as e:  # a broken chain is a reason to refuse, not to guess
            board_note = f"market board unreadable: {str(e)[:160]}"
            log.warning(kv(event="board_unreadable", err=str(e)[:160]))
    markets: list[dict[str, Any]] = list(board.rows) if board is not None else []
    market_ts = parse_iso(board.observed_at_utc) if board is not None and board.observed_at_utc else None
    market_age = (now - market_ts).total_seconds() / 60 if market_ts else None
    series_rows: dict[str, dict[str, Any]] = {}
    cat = data_root / "catalog" / "discovery_summary.json"
    for root in (out_root / "catalog" / "discovery_summary.json", cat):
        if root.exists():
            try:
                for s in json.loads(root.read_text()).get("nhl_series", []):
                    series_rows.setdefault(s["ticker"], {"ticker": s["ticker"], "fee_type": s.get("fee_type"), "fee_multiplier": s.get("fee_multiplier")})
            except (json.JSONDecodeError, KeyError):
                pass
    # contracts for every market, joined to games by (date, {teams})
    contracts_by_game: dict[str, list[tuple[dict[str, Any], Any]]] = {}
    unjoined = 0
    game_keys = {(g["game_date_et"], frozenset({int(g["home_team_id"]), int(g["away_team_id"])})): g["game_id"] for g in sched}
    for m in markets:
        if not m.get("ticker") or m.get("_error"):
            continue
        c = build_contract(m, onto, reg)
        k = game_key(c)
        gid = game_keys.get(k) if k else None
        if gid is None:
            unjoined += 1
            continue
        contracts_by_game.setdefault(gid, []).append((m, c.model_copy(update={"game_id": gid})))
    season_id = season_id_for(target)
    mps = mp_season(target)
    cfg = SimConfig(n_sims=n_sims or SimConfig().n_sims)
    ts = iso(now)
    pred_rows: list[dict[str, Any]] = []
    contract_rows: list[dict[str, Any]] = []
    slate_games: list[dict[str, Any]] = []
    packet_games: list[dict[str, Any]] = []
    v2_items: list[dict[str, Any]] = []  # handed to the DATA_ONLY_V2 shadow arm AFTER every V1 row exists
    for g in not_started:
        gid = g["game_id"]
        gi = build_game_inputs(g, now, team_games, goalie_stats, goalie_obs, season_id, mps)
        home_p, away_p = gi.team_params()
        s = seed if seed is not None else seed_for(gid, target)
        res = simulate_game(home_p, away_p, seed=s, config=cfg)
        viol = ladder_violations(res)
        summ = res.summary()
        start = parse_iso(g["start_time_utc"])
        mins = (start - now).total_seconds() / 60
        gate_reasons_game: list[str] = list(gi.reasons)
        if market_age is None:
            gate_reasons_game.append("no market snapshot")
        elif market_age > MAX_MARKET_AGE_MIN:
            gate_reasons_game.append(f"market snapshot {market_age:.0f} min old")
        if tg_meta.get("age_min") is None or tg_meta["age_min"] > MAX_CONTEXT_AGE_MIN:
            gate_reasons_game.append("team game log missing or stale")
        rows_for_game: list[dict[str, Any]] = []
        for m, c in contracts_by_game.get(gid, []):
            pr = price_contract(c, res, gi.home_team_id, gi.away_team_id)
            mi = market_implied_probability(m)
            p_data = pr.p
            p_mkt = mi.p_mid
            p_anch = market_anchored(p_data, p_mkt)
            fee = _series_fee(series_rows, m)
            econ = compute_economics(m, p_data, pr.se or 0.0, schedule=fee, observed_at=market_ts, now=now) if p_data is not None else None
            reasons = list(gate_reasons_game) + ([] if pr.supported else [pr.reason])
            if not pr.supported:
                gate = Gate.UNSUPPORTED
            elif mins <= 0:
                gate = Gate.NOT_PREGAME
            elif any(r.startswith(("no market", "market snapshot", "team game log", "thin team")) for r in reasons) or (econ and (econ.stale or econ.crossed)):
                gate = Gate.CANNOT_TRUST_INPUTS
                if econ:
                    reasons += [r for r in econ.reasons if r.startswith(("stale", "crossed"))]
            elif econ is None or econ.best_side is None:
                gate = Gate.NO_EDGE
            else:
                gate = Gate.OK
            q = m.get("_quote_cents") or {}
            row = ContractPrediction(
                prediction_id=_pred_id(m["ticker"], ts, DATA_ONLY_MODEL_VERSION, ledger.run_id), ticker=m["ticker"], game_id=gid, family=c.family,
                predicted_at_utc=now, data_cutoff_utc=now, model_version=DATA_ONLY_MODEL_VERSION, sim_version=SIM_VERSION, feature_version=FEATURE_VERSION,
                n_sims=res.n_sims, seed=s, p_data_only=p_data, p_market=p_mkt, p_market_anchored=p_anch, p_data_only_se=pr.se,
                market_observed_at_utc=market_ts, market_yes_bid=q.get("yes_bid"), market_yes_ask=q.get("yes_ask"), market_no_bid=q.get("no_bid"), market_no_ask=q.get("no_ask"),
                executable_p_yes=(q.get("yes_ask") / 100 if q.get("yes_ask") else None), executable_p_no=(q.get("no_ask") / 100 if q.get("no_ask") else None),
                edge_yes_raw=econ.yes.gross_edge if econ else None, edge_yes_after_fee=econ.yes.ev_per_contract if econ else None,
                edge_no_raw=econ.no.gross_edge if econ else None, edge_no_after_fee=econ.no.ev_per_contract if econ else None,
                gate=gate, gate_reasons=reasons[:6], authority=Authority.RESEARCH_ONLY, support=c.support, pregame=mins > 0 and (market_ts is None or market_ts < start),
                minutes_to_start=round(mins, 1), horizon_label=horizon_label(mins), home_goalie_status=gi.home_goalie.status.value, away_goalie_status=gi.away_goalie.status.value,
                input_snapshot_ids={k: str(v.get("path")) for k, v in (("schedule", sched_meta), ("team_games", tg_meta), ("goalie_stats", gs_meta), ("rosters", ro_meta), ("injuries", inj_meta)) if v.get("path")} | ({"market_board": board.provenance()} if board is not None else {}),
            )
            d = row.model_dump(mode="json")
            d.update({
                "title": m.get("title"), "stat": c.stat, "period": c.period, "settles_on": c.settles_on, "team_id": c.team_id, "threshold": c.threshold, "comparator": c.comparator,
                "semantics_confidence": c.semantics_confidence, "market_anchor_weight": MARKET_ANCHOR_WEIGHT, "market_anchored_model_version": MARKET_ANCHORED_MODEL_VERSION,
                "best_side": econ.best_side if econ else None, "spread_cents": econ.spread_cents if econ else None, "fee_schedule": fee.source,
                "kalshi_status": m.get("status"), "volume": (m.get("_quote_cents") or {}).get("volume") or m.get("volume"), "liquidity_cents": (m.get("liquidity")),
                "close_time": m.get("close_time"), "expected_expiration_time": m.get("expected_expiration_time"), "price_reason": pr.reason,
            })
            pred_rows.append(d)
            contract_rows.append(c.model_dump(mode="json") | {"observed_market_at_utc": iso(market_ts) if market_ts else None})
            rows_for_game.append(d)
        gsum = {
            "game_id": gid, "date_et": target, "start_time_utc": g["start_time_utc"], "minutes_to_start": round(mins, 1), "horizon": horizon_label(mins),
            "home": gi.home_abbrev, "away": gi.away_abbrev, "home_team_id": gi.home_team_id, "away_team_id": gi.away_team_id, "venue": g.get("venue"),
            "p_home_win": summ["p_home_win"], "p_away_win": summ["p_away_win"], "p_home_reg_win": summ["p_home_reg_win"], "p_away_reg_win": summ["p_away_reg_win"],
            "p_reg_tie": summ["p_reg_tie"], "p_overtime": summ["p_overtime"], "p_shootout": summ["p_shootout"], "exp_home_goals": summ["home_goals_mean"],
            "exp_away_goals": summ["away_goals_mean"], "exp_total": summ["total_mean"], "total_sd": summ["total_sd"], "margin_sd": summ["margin_sd"],
            "lam_home": gi.lam_home, "lam_away": gi.lam_away, "n_sims": res.n_sims, "seed": s, "ladder_violations": viol, "inputs_trusted": gi.trusted,
            "input_reasons": gi.reasons, "home_goalie": gi.home_goalie.to_dict(), "away_goalie": gi.away_goalie.to_dict(),
            "n_contracts": len(rows_for_game), "n_supported": sum(1 for r in rows_for_game if r["gate"] != "UNSUPPORTED"),
            "n_unsupported": sum(1 for r in rows_for_game if r["gate"] == "UNSUPPORTED"), "families": dict(Counter(r["family"] for r in rows_for_game)),
        }
        slate_games.append(gsum)
        v2_items.append({"game": g, "gi": gi, "gsum": gsum, "contracts": contracts_by_game.get(gid, []), "v1_rows": rows_for_game, "seed": s,
                         "minutes": mins, "horizon": horizon_label(mins)})
        packet_games.append({
            "identity": {"game_id": gid, "sport": "NHL", "league": "NHL", "event_id": gid, "season": g.get("season"), "season_type": g.get("season_type"), "date_et": target,
                         "start_time_utc": g["start_time_utc"], "home": gi.home_abbrev, "away": gi.away_abbrev, "home_team_id": gi.home_team_id, "away_team_id": gi.away_team_id, "venue": g.get("venue")},
            "context": {"home_rest_days": gi.home_rest_days, "away_rest_days": gi.away_rest_days, "home_b2b": gi.home_b2b, "away_b2b": gi.away_b2b,
                        "injuries": [i for i in injuries if i.get("team_id") in (gi.home_team_id, gi.away_team_id)], "injury_snapshot": inj_meta, "line_changes": None},
            "goaltending": {"home": gi.home_goalie.to_dict() | {"factor": gi.home_goalie_factor, "detail": gi.home_goalie_detail},
                            "away": gi.away_goalie.to_dict() | {"factor": gi.away_goalie_factor, "detail": gi.away_goalie_detail},
                            "uncertainty_note": "factor is a confidence-weighted mixture over plausible starters; UNKNOWN == league-average net"},
            "team_state": {"home": gi.home_rating.to_dict(), "away": gi.away_rating.to_dict(), "league": gi.league.__dict__,
                           "special_teams": _special_teams(goalie_stats, team_games, gi)},
            "model": {"model_version": DATA_ONLY_MODEL_VERSION, "sim_version": SIM_VERSION, "feature_version": FEATURE_VERSION, "components": gi.components, "sim": summ, "ladder_violations": viol,
                      "inputs_trusted": gi.trusted, "input_reasons": gi.reasons, "market_anchored": {"model_version": MARKET_ANCHORED_MODEL_VERSION, "weight_on_market": MARKET_ANCHOR_WEIGHT,
                      "note": "logit blend of Kalshi midpoint and DATA_ONLY; NOT independent evidence"}},
            "kalshi": {"market_snapshot_at_utc": iso(market_ts) if market_ts else None, "market_age_min": market_age, "contracts": rows_for_game,
                       "coverage": {"n_contracts": len(rows_for_game), "by_gate": dict(Counter(r["gate"] for r in rows_for_game)), "by_family": dict(Counter(r["family"] for r in rows_for_game))}},
            "authority": AUTHORITY,
        })
        log.info(kv(event="game_simulated", game=gid, home=gi.home_abbrev, away=gi.away_abbrev, p_home=round(summ["p_home_win"], 3), contracts=len(rows_for_game), goalies=f"{gi.home_goalie.status.value}/{gi.away_goalie.status.value}"))

    slate = {
        "sport": "NHL", "generated_at_utc": ts, "date_et": target, "authority": AUTHORITY, "run_id": ledger.run_id,
        "authority_note": "RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists.",
        "model_version": DATA_ONLY_MODEL_VERSION, "market_anchored_model_version": MARKET_ANCHORED_MODEL_VERSION, "sim_version": SIM_VERSION, "feature_version": FEATURE_VERSION,
        "market_anchor_weight_prior": MARKET_ANCHOR_WEIGHT, "n_sims": cfg.n_sims,
        "snapshots": {"schedule": sched_meta, "team_games": tg_meta, "goalie_stats": gs_meta, "rosters": ro_meta, "injuries": inj_meta,
                      "market_board": {"observed_at_utc": iso(market_ts) if market_ts else None, "age_min": market_age, "n_markets": len(markets), "provenance": board.provenance() if board else None, "note": board_note}},
        "coverage": {"games_on_date": len(games), "games_simulated": len(not_started), "games_skipped": skipped, "markets_on_board": len(markets),
                     "contracts_joined": len(pred_rows), "contracts_unjoined_to_any_game": unjoined, "by_gate": dict(Counter(r["gate"] for r in pred_rows)),
                     "by_family": dict(Counter(r["family"] for r in pred_rows)), "by_support": dict(Counter(r["support"] for r in pred_rows))},
        "games": slate_games, "contracts": pred_rows,
    }
    v2 = _run_v2_shadow(ledger, v2_items, data_root, cfg.n_sims, now, market_ts, rosters) if v2_items else None
    if v2 is not None:
        slate["v2_shadow"] = {k: v for k, v in v2.items() if k != "rows"} | {"n_rows": len(v2.get("rows") or [])}
    player = _run_player_shadow(ledger, v2_items, v2, data_root, now, market_ts, rosters, injuries, series_rows) if (v2_items and v2 and not v2.get("error")) else None
    dists = (player.pop("distributions", None) or []) if player is not None else []
    thesis = _run_thesis_card(ledger, dists, now, player) if dists else None
    if thesis is not None:
        slate["thesis_card"] = thesis["slate_view"]
    if player is not None:
        slate["player_shadow"] = {k: v for k, v in player.items() if k != "rows"} | {"n_rows": len(player.get("rows") or [])}
        slate["_player_rows"] = player.get("rows") or []
        slate["coverage"]["player_shadow"] = {"player_contracts": len(player.get("rows") or []), "priced": sum(1 for r in player.get("rows") or [] if r.get("priced"))}
    if write:
        if pred_rows:
            ledger.append_rows("predictions", pred_rows, observed_at=now, meta={"date_et": target, "n_games": len(not_started)})
            ledger.append_rows("contracts", contract_rows, observed_at=now, meta={"date_et": target})
        if v2 is not None and v2.get("rows"):
            # a SEPARATE kind: V1's predictions partition is byte-for-byte what it was before V2 existed
            try:
                ledger.append_rows("predictions_v2", v2["rows"], observed_at=now, meta={"date_et": target, "role": "SHADOW", "model_version": DATA_ONLY_V2_MODEL_VERSION})
            except Exception as e:  # noqa: BLE001 - never block V1's slate on the shadow arm
                log.warning(kv(event="v2_shadow_archive_failed", err=str(e)[:300]))
                slate["v2_shadow"]["archive_error"] = f"{type(e).__name__}: {str(e)[:200]}"
        if player is not None and player.get("rows"):
            try:
                ledger.append_rows("predictions_player", player["rows"], observed_at=now, meta={"date_et": target, "role": "SHADOW", "model_version": PLAYER_MODEL_VERSION})
            except Exception as e:  # noqa: BLE001 - never block V1's slate on the shadow arm
                log.warning(kv(event="player_shadow_archive_failed", err=str(e)[:300]))
                slate["player_shadow"]["archive_error"] = f"{type(e).__name__}: {str(e)[:200]}"
        if thesis is not None and thesis.get("ledger"):
            for kind, rows in thesis["ledger"].items():
                if rows:
                    try:  # SEPARATE kinds: nothing V1 / V2 / PLAYER_SIM_V1 write changes
                        ledger.append_rows(kind, rows, observed_at=now, meta={"date_et": target, "role": "RESEARCH_ONLY", "thesis_version": thesis["packet"].get("thesis_version")})
                    except Exception as e:  # noqa: BLE001 - never block V1's slate on the thesis layer
                        log.warning(kv(event="thesis_archive_failed", kind=kind, err=str(e)[:300]))
                        slate["thesis_card"]["archive_error"] = f"{type(e).__name__}: {str(e)[:200]}"
        stamp = now.strftime("%Y%m%dT%H%M%SZ")
        out_dir = out_root / "slates" / f"dt={target}" / f"{stamp}_{ledger.run_id}"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "slate.json").write_text(json.dumps({k: v for k, v in slate.items() if k != "_player_rows"}, indent=1, default=str))
        (out_dir / "slate.md").write_text(slate_markdown(slate))
        (out_dir / "packet.json").write_text(json.dumps({"slate": {k: v for k, v in slate.items() if k not in ("contracts", "games", "v2_shadow", "player_shadow", "_player_rows")}, "games": packet_games}
                                                        | ({"v2_shadow": slate["v2_shadow"]} if "v2_shadow" in slate else {})
                                                        | ({"player_shadow": slate["player_shadow"] | {"contracts": player.get("rows") or []}} if player is not None else {})
                                                        | ({"thesis_card": thesis["packet"]} if thesis is not None else {}),
                                                        indent=1, default=str))
        names = ["slate.json", "slate.md", "packet.json"]
        if thesis is not None:
            (out_dir / "card.md").write_text(thesis["markdown"])
            names.append("card.md")
        latest = out_root / "slates" / "latest"
        latest.mkdir(parents=True, exist_ok=True)
        for name in names:
            (latest / name).write_text((out_dir / name).read_text())
        (out_root / "STATUS_simulate.json").write_text(json.dumps({"simulated_at_utc": ts, "date_et": target, "n_games": len(not_started), "n_contracts": len(pred_rows),
                                                                    "out_dir": str(out_dir.relative_to(out_root)), "run_id": ledger.run_id, "by_gate": slate["coverage"]["by_gate"]}, indent=1))
        print(slate_markdown(slate))
    return 0


def _run_v2_shadow(ledger: Ledger, items: list[dict[str, Any]], data_root: Path, n_sims: int, now: datetime, market_ts: datetime | None,
                   rosters: list[dict[str, Any]] | None = None) -> dict[str, Any] | None:
    """DATA_ONLY_V2 shadow arm (RESEARCH_ONLY). Never raises: a failure is recorded and V1 proceeds unchanged."""
    from nhl_edge.workflows import shadow_v2

    if not shadow_v2.enabled():
        return None
    try:
        live_st, st_meta = _read_latest(ledger, "context/team_games_st", now)
        out = shadow_v2.run_shadow(items, data_root, live_st, n_sims, now, market_ts, ledger.run_id, rosters)
        out["context"]["team_games_st_snapshot"] = st_meta
        out["model_version"] = DATA_ONLY_V2_MODEL_VERSION
        out["role"] = "SHADOW"
        out["authority"] = AUTHORITY
        out["note"] = ("DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and "
                       "carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT.")
        return out
    except Exception as e:  # noqa: BLE001 - the shadow arm must never take V1 down
        log.warning(kv(event="v2_shadow_failed", err=str(e)[:300]))
        return {"error": f"{type(e).__name__}: {str(e)[:300]}", "rows": [], "blocks": [], "model_version": DATA_ONLY_V2_MODEL_VERSION, "role": "SHADOW"}


PLAYER_EVENT_KINDS = ("players", "goalies", "goals", "shots", "coice", "team_states")


def _run_player_shadow(ledger: Ledger, items: list[dict[str, Any]], v2: dict[str, Any], data_root: Path, now: datetime, market_ts: datetime | None,
                       rosters: list[dict[str, Any]], injuries: list[dict[str, Any]], series_rows: dict[str, dict[str, Any]]) -> dict[str, Any] | None:
    """PLAYER_SIM_V1 shadow arm (RESEARCH_ONLY). Never raises: a failure is recorded and V1 / V2 proceed unchanged."""
    from nhl_edge.workflows import shadow_player

    if not shadow_player.enabled():
        return None
    try:
        lines, lines_meta = _read_latest(ledger, "context/lines", now)
        live = {k: _read_all(ledger, f"player_events/{k}", now) for k in PLAYER_EVENT_KINDS}
        gstates = {}
        for it in items:
            gi = it["gi"]
            gstates[f"{gi.game_id}|home"] = gi.home_goalie.to_dict()
            gstates[f"{gi.game_id}|away"] = gi.away_goalie.to_dict()
        out = shadow_player.run_player_shadow(items, v2.get("blocks") or [], data_root, now, market_ts, ledger.run_id, rosters, lines, injuries, live,
                                              lambda m: _series_fee(series_rows, m), gstates)
        out["context"]["lines_snapshot"] = lines_meta
        out.update({"model_version": PLAYER_MODEL_VERSION, "role": "SHADOW", "authority": AUTHORITY,
                    "note": ("PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. "
                             "It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing.")})
        return out
    except Exception as e:  # noqa: BLE001 - the shadow arm must never take V1 down
        log.warning(kv(event="player_shadow_failed", err=str(e)[:300]))
        return {"error": f"{type(e).__name__}: {str(e)[:300]}", "rows": [], "blocks": [], "model_version": PLAYER_MODEL_VERSION, "role": "SHADOW"}


def _run_thesis_card(ledger: Ledger, dists: list[Any], now: datetime, player: dict[str, Any] | None) -> dict[str, Any] | None:
    """Thesis / portfolio card (RESEARCH_ONLY) on the PLAYER_SIM_V1 joint draws. Never raises: a failure is recorded."""
    from nhl_edge.workflows import thesis_card

    if not thesis_card.enabled():
        return None
    try:
        odds, odds_meta = _read_latest(ledger, "context/sportsbook_odds", now)
        card = thesis_card.run_thesis_card(dists, ledger, now, odds, ledger.run_id)
        card["sportsbook_snapshot"] = odds_meta
        if player and player.get("distribution_errors"):
            card["distribution_errors"] = player["distribution_errors"]
        sv = thesis_card.slate_view(card) | {"sportsbook_snapshot": odds_meta, "card_file": "card.md"}
        return {"packet": thesis_card.packet_view(card), "slate_view": sv, "markdown": thesis_card.markdown(card), "ledger": card.get("_ledger") or {}}
    except Exception as e:  # noqa: BLE001 - the thesis layer must never take V1 / V2 / PLAYER_SIM_V1 down
        log.warning(kv(event="thesis_card_failed", err=str(e)[:300]))
        err = {"status": "ERROR", "error": f"{type(e).__name__}: {str(e)[:300]}", "authority": AUTHORITY}
        return {"packet": err, "slate_view": err, "markdown": f"# NHL THESIS CARD — ERROR\n\n{err['error']}\n", "ledger": {}}


def _special_teams(goalie_stats: list[dict[str, Any]], team_games: list[dict[str, Any]], gi) -> dict[str, Any]:
    """PP/PK context from the team_games snapshot is not carried (situation 'all' only); reported from the packet's
    team_summary when available. V1 folds special teams into all-situation xG rates (documented simplification)."""
    return {"note": "V1 folds power play / penalty kill into all-situation xG rates; explicit PP/PK modelling is roadmap item 1"}


def slate_markdown(s: dict[str, Any]) -> str:
    cov = s["coverage"]
    lines = [f"# NHL slate {s['date_et']} — {s['authority']}", "", f"generated {s['generated_at_utc']} · model {s['model_version']} · sim {s['sim_version']} · {s['n_sims']} sims/game", "",
             f"games on date: {cov['games_on_date']} · simulated (not started): {cov['games_simulated']} · markets on board: {cov['markets_on_board']} · contracts joined: {cov['contracts_joined']} (unjoined to any game: {cov['contracts_unjoined_to_any_game']})",
             f"gates: {cov['by_gate']}", f"families: {cov['by_family']}", "",
             "| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |", "|---|---|---|---:|---:|---:|---:|---:|---:|---|---|"]
    for g in s["games"]:
        lines.append(f"| {g['away']} @ {g['home']} | {g['start_time_utc']} | {g['horizon']} | {g['p_home_win']:.3f} | {g['p_away_win']:.3f} | {g['p_overtime']:.3f} | {g['exp_total']:.2f} | {g['exp_home_goals']:.2f} | {g['exp_away_goals']:.2f} | {g['n_contracts']} ({g['n_supported']}/{g['n_unsupported']}) | {g['home_goalie']['status']}/{g['away_goalie']['status']} |")
    lines += ["", "## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)", "",
              "| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |", "|---|---|---:|---:|---:|---:|---:|---|---:|---|"]
    rows = sorted(s["contracts"], key=lambda r: -max(r.get("edge_yes_after_fee") or -9, r.get("edge_no_after_fee") or -9))
    for r in rows[:80]:
        ev = max(r.get("edge_yes_after_fee") or -9, r.get("edge_no_after_fee") or -9)
        f = lambda x: "" if x is None else f"{x:.3f}"  # noqa: E731
        lines.append(f"| {r['ticker']} | {r['family']} | {f(r.get('p_data_only'))} | {f(r.get('p_market'))} | {f(r.get('p_market_anchored'))} | {r.get('market_yes_ask') or ''} | {r.get('market_no_ask') or ''} | {r.get('best_side') or ''} | {'' if ev == -9 else f'{ev:+.3f}'} | {r['gate']} |")
    if s["games"] == []:
        lines.append("(no not-started games on this date at run time)")
    v2 = s.get("v2_shadow")
    if v2:
        try:
            from nhl_edge.workflows.shadow_v2 import markdown as v2_markdown

            lines.append(v2_markdown(v2.get("blocks") or [], v2.get("error") or v2.get("note")))
        except Exception as e:  # noqa: BLE001 - the V1 slate renders regardless
            lines.append(f"\n(DATA_ONLY_V2 shadow section failed to render: {type(e).__name__})")
    tc = s.get("thesis_card")
    if tc:
        lines.append(f"\n## Thesis card (RESEARCH_ONLY): status {tc.get('status')} · gate {(tc.get('gate') or {}).get('status')} · "
                     f"{len(tc.get('recommended') or [])} recommended · full analysis in card.md / packet.json `thesis_card`\n")
        for r in tc.get("recommended") or []:
            lines.append(f"- {r['title']} {r['side']} @ {r.get('ask')}c · p {r['p']} (adj {r['p_adj']}) · ${r['stake']} · thesis {r['primary_thesis']}")
    ps = s.get("player_shadow")
    if ps:
        try:
            from nhl_edge.workflows.shadow_player import markdown as player_markdown

            lines.append(player_markdown(ps.get("blocks") or [], s.get("_player_rows") or [], ps.get("error") or ps.get("note")))
        except Exception as e:  # noqa: BLE001 - the V1 slate renders regardless
            lines.append(f"\n(PLAYER_SIM_V1 shadow section failed to render: {type(e).__name__})")
    lines += ["", f"_{s['authority_note']}_"]
    return "\n".join(lines) + "\n"
