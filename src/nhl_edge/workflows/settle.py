"""Settlement job: fetch final results for finished games and settle every contract we captured.

Archive contract (append-only ledger kinds under ``out_root``):
* reads  ``context/schedule``, ``contracts``, ``predictions``, ``kalshi/markets`` (+deltas; ``result`` field),
         ``results`` and ``settlements`` (our own earlier output)
* writes ``results`` (FinalResult rows), ``settlements`` (SettlementRecord rows), ``context/goalie_observations``
         (CONFIRMED starters from the boxscore, post-start), and the pointer ``STATUS_settle.json``

Rules
- A game is a candidate once its scheduled start is older than ``SETTLE_GRACE`` (3h), it is not postponed/canceled in
  the latest schedule row, it has at least one prediction or contract row, and we do not already hold a FINAL result.
- Kalshi's ``result`` (newest observation with a non-empty value) is passed to the engine, which never lets it override
  our computed outcome; disagreements are surfaced in the status file.
- Tickers with a Kalshi result but no Contract row get a market-only record (engine 'kalshi') so market calibration
  covers the whole universe.
- Idempotent: records are keyed by ``idempotency_key``; a re-run with no new data appends nothing.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from nhl_edge.archive.ledger import Ledger
from nhl_edge.archive.reconstruct import iter_market_rows
from nhl_edge.data.goalies import observations_from_boxscore
from nhl_edge.data.nhl_api import fetch_boxscore
from nhl_edge.log import get_logger, kv
from nhl_edge.schemas.core import FinalResult, GameStatus
from nhl_edge.schemas.market import Contract
from nhl_edge.settlement.engine import (
    DISAGREE_PREFIX,
    SettlementOutcome,
    SettlementRecord,
    _kalshi_outcome,
    final_result_from_boxscore,
    idempotency_key,
    settle_many,
)
from nhl_edge.timeutil import iso, parse_iso, utcnow

PLAYER_FAMILIES = ("player_goals", "player_points", "player_assists", "goalie_saves", "first_goal")
PERIOD_FAMILIES = ("period_winner", "period_spread", "period_total")
OFFICIAL_EVENT_FAMILIES = PLAYER_FAMILIES + PERIOD_FAMILIES

log = get_logger(__name__)

SETTLE_GRACE = timedelta(hours=3)
KALSHI_ENGINE_VERSION = "kalshi"
MARKET_ONLY_REASON = "kalshi_result_only"
_SKIP_STATUSES = {GameStatus.POSTPONED.value, GameStatus.CANCELED.value}

FetchResult = Callable[[str], tuple[FinalResult, list[dict[str, Any]]]]
FetchPlayerEvents = Callable[[str, dict[str, Any]], tuple[dict[str, Any], list[str]]]
PLAYER_EVENT_TABLES = ("players", "goalies", "goals", "shots", "coice", "team_states")


def strip_meta(row: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in row.items() if not k.startswith("_")}


def coerce(model: type, row: dict[str, Any]):
    fields = set(model.model_fields)
    return model.model_validate({k: v for k, v in strip_meta(row).items() if k in fields})


def latest_schedule(ledger: Ledger) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for row in ledger.iter_rows("context/schedule"):
        out[str(row["game_id"])] = row  # partitions iterate in time order; last wins
    return out


def load_contracts(ledger: Ledger) -> dict[str, Contract]:
    out: dict[str, Contract] = {}
    for row in ledger.iter_rows("contracts"):
        try:
            c = coerce(Contract, row)
        except Exception as e:  # noqa: BLE001
            log.warning(kv(event="bad_contract_row", ticker=row.get("ticker"), err=str(e)[:100]))
            continue
        if c.game_id:
            out[c.ticker] = c
    return out


def load_settlements(ledger: Ledger) -> dict[str, SettlementRecord]:
    out: dict[str, SettlementRecord] = {}
    for row in ledger.iter_rows("settlements"):
        try:
            rec = coerce(SettlementRecord, row)
        except Exception:  # noqa: BLE001
            continue
        out[rec.idempotency_key] = rec
    return out


def load_final_results(ledger: Ledger) -> dict[str, FinalResult]:
    out: dict[str, FinalResult] = {}
    for row in ledger.iter_rows("results"):
        try:
            r = coerce(FinalResult, row)
        except Exception:  # noqa: BLE001
            continue
        if not r.is_final:
            continue
        prior = out.get(r.game_id)
        if prior is None or r.stat_correction_version >= prior.stat_correction_version:
            out[r.game_id] = r
    return out


def kalshi_results(ledger: Ledger) -> dict[str, str]:
    """ticker -> newest non-empty Kalshi ``result`` across every market observation."""
    out: dict[str, tuple[datetime, str]] = {}
    for row in iter_market_rows(ledger):
        res = row.get("result")
        tk = row.get("ticker")
        if not res or not tk:
            continue
        try:
            ts = parse_iso(row["_observed_at_utc"])
        except (KeyError, ValueError):
            continue
        if tk not in out or ts > out[tk][0]:
            out[tk] = (ts, str(res))
    return {k: v[1] for k, v in out.items()}


def game_ids_with_activity(ledger: Ledger, contracts: dict[str, Contract]) -> set[str]:
    ids = {c.game_id for c in contracts.values() if c.game_id}
    for row in ledger.iter_rows("predictions"):
        if row.get("game_id"):
            ids.add(str(row["game_id"]))
    return ids


def default_fetch_result(game_id: str) -> tuple[FinalResult, list[dict[str, Any]]]:
    box, meta = fetch_boxscore(game_id)
    res = final_result_from_boxscore(box, fetched_at_utc=meta["fetched_at_utc"])
    obs = [o.model_dump(mode="json") for o in observations_from_boxscore(box, parse_iso(meta["fetched_at_utc"]))]
    return res, obs


def default_fetch_player_events(game_id: str, meta: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    """Official boxscore + play-by-play + shift charts -> PLAYER_SIM_V1 tables (``data.player_events``) for one game."""
    from nhl_edge.data.player_history import fetch_game

    tables, rep = fetch_game(int(game_id), meta)
    if tables is None:
        raise RuntimeError(rep.get("error") or "player events unavailable")
    return tables, list(rep.get("issues") or []) + ([f"shifts: {rep['shifts_error']}"] if rep.get("shifts_error") else [])


def _jsonable(df: Any) -> list[dict[str, Any]]:
    import math

    out = []
    for r in df.to_dict("records"):
        rec = {}
        for k, v in r.items():
            if hasattr(v, "tolist"):
                v = v.tolist()
            if isinstance(v, float) and math.isnan(v):
                v = None
            rec[k] = v
        out.append(rec)
    return out


def ingested_player_games(ledger: Ledger) -> set[str]:
    return {str(r.get("game_id")) for r in ledger.iter_rows("player_events/players")}


def market_only_record(ticker: str, result: str, game_id: str, now: datetime) -> SettlementRecord:
    k = _kalshi_outcome(result) or SettlementOutcome.UNSETTLEABLE
    return SettlementRecord(ticker=ticker, game_id=game_id, outcome=k, value=None, reason=f"{MARKET_ONLY_REASON}: kalshi_result={result}",
                            settled_at_utc=now, result_source="kalshi", stat_correction_version=0, engine_version=KALSHI_ENGINE_VERSION,
                            idempotency_key=idempotency_key(ticker, game_id, KALSHI_ENGINE_VERSION, 0, None), settles_on="KALSHI")


def _record_row(rec: SettlementRecord) -> dict[str, Any]:
    d = rec.model_dump(mode="json")
    d["settled_at_utc"] = iso(rec.settled_at_utc)
    return d


def run_settle(out_root: Path, data_root: Path, fetch_result: FetchResult | None = None, now: datetime | None = None,
               fetch_player_events: FetchPlayerEvents | None = None) -> int:
    now = now or utcnow()
    fetch_result = fetch_result or default_fetch_result
    fetch_player_events = fetch_player_events or default_fetch_player_events
    ledger = Ledger(out_root)
    schedule = latest_schedule(ledger)
    contracts = load_contracts(ledger)
    existing = load_settlements(ledger)
    finals = load_final_results(ledger)
    kres = kalshi_results(ledger)
    candidates: list[str] = []
    for gid in sorted(game_ids_with_activity(ledger, contracts)):
        g = schedule.get(gid)
        if not g or g.get("status") in _SKIP_STATUSES:
            continue
        try:
            start = parse_iso(g["start_time_utc"])
        except (KeyError, ValueError):
            continue
        if now - start >= SETTLE_GRACE:
            candidates.append(gid)
    new_results: list[dict[str, Any]] = []
    new_goalie_obs: list[dict[str, Any]] = []
    new_records: list[SettlementRecord] = []
    errors: list[str] = []
    disagreements: list[str] = []
    not_final: list[str] = []
    for gid in candidates:
        res = finals.get(gid)
        if res is None:
            try:
                res, obs = fetch_result(gid)
            except Exception as e:  # noqa: BLE001
                errors.append(f"{gid}: {str(e)[:160]}")
                continue
            if not res.is_final:
                not_final.append(gid)
                continue
            finals[gid] = res
            d = res.model_dump(mode="json")
            new_results.append(d)
            new_goalie_obs += obs
        cs = [c for c in contracts.values() if c.game_id == gid and c.family not in OFFICIAL_EVENT_FAMILIES]
        recs = settle_many(cs, res, existing, kres, now=now)
        for r in recs:
            if r.idempotency_key not in existing:
                existing[r.idempotency_key] = r
                new_records.append(r)
                if r.reason.startswith(DISAGREE_PREFIX):
                    disagreements.append(f"{r.ticker}: {r.reason[:160]}")
    # PLAYER_SIM_V1: official player events for every final game (live point-in-time history for later games) and player
    # prop settlement from the same official lines. Failures here are recorded and never block game settlement.
    player_status = _settle_players(ledger, candidates, finals, contracts, existing, kres, now, fetch_player_events, schedule, new_records, disagreements)
    # market-only records for tickers with a Kalshi result and no contract (needs a game id from an archived contract's event)
    for tk, result in kres.items():
        if tk in contracts:
            continue
        key = idempotency_key(tk, "kalshi", KALSHI_ENGINE_VERSION, 0, None)
        if key in existing:
            continue
        rec = market_only_record(tk, result, "kalshi", now)
        existing[rec.idempotency_key] = rec
        new_records.append(rec)
    if new_results:
        ledger.append_rows("results", new_results, observed_at=now)
    if new_goalie_obs:
        ledger.append_rows("context/goalie_observations", new_goalie_obs, observed_at=now, meta={"source": "boxscore_starters"})
    if new_records:
        ledger.append_rows("settlements", [_record_row(r) for r in new_records], observed_at=now)
    status = {
        "settled_at_utc": iso(now), "run_id": ledger.run_id, "n_candidates": len(candidates), "n_new_results": len(new_results), "n_new_records": len(new_records),
        "n_unsettleable": sum(1 for r in new_records if r.outcome == SettlementOutcome.UNSETTLEABLE), "n_market_only": sum(1 for r in new_records if r.engine_version == KALSHI_ENGINE_VERSION),
        "by_outcome": {o.value: sum(1 for r in new_records if r.outcome == o) for o in SettlementOutcome}, "not_final_yet": not_final, "errors": errors, "disagreements": disagreements,
        "player": player_status,
    }
    (out_root / "STATUS_settle.json").write_text(json.dumps(status, indent=1, default=str))
    print(json.dumps(status, indent=1, default=str))
    return 0


def _settle_players(ledger: Ledger, candidates: list[str], finals: dict[str, FinalResult], contracts: dict[str, Contract], existing: dict[str, SettlementRecord],
                    kres: dict[str, str], now: datetime, fetch_player_events: FetchPlayerEvents, schedule: dict[str, dict[str, Any]],
                    new_records: list[SettlementRecord], disagreements: list[str]) -> dict[str, Any]:
    import pandas as pd

    from nhl_edge.settlement.period import PERIOD_ENGINE_VERSION, settle_period_contract
    from nhl_edge.settlement.player import PLAYER_ENGINE_VERSION, settle_player_contract

    status: dict[str, Any] = {"engine": [PLAYER_ENGINE_VERSION, PERIOD_ENGINE_VERSION], "games_ingested": [], "errors": [], "n_records": 0, "n_period_records": 0,
                              "issues": {}}
    try:
        have = ingested_player_games(ledger)
    except Exception as e:  # noqa: BLE001
        status["errors"].append(f"reading ingested games: {str(e)[:160]}")
        return status
    done_tickers = {r.ticker for r in existing.values() if r.engine_version in (PLAYER_ENGINE_VERSION, PERIOD_ENGINE_VERSION)}
    for gid in candidates:
        res = finals.get(gid)
        if res is None or not res.is_final:
            continue
        pcs = [c for c in contracts.values() if c.game_id == gid and c.family in OFFICIAL_EVENT_FAMILIES]
        if gid in have and all(c.ticker in done_tickers for c in pcs):
            continue  # already ingested and every player contract already has a record: no network
        g = schedule.get(gid) or {}
        meta = {"season": int(str(gid)[:4]), "game_date": g.get("game_date_et") or str(getattr(res, "game_date", "") or "")[:10], "game_type": int(str(gid)[4:6])}
        try:
            tables, issues = fetch_player_events(gid, meta)
        except Exception as e:  # noqa: BLE001
            status["errors"].append(f"{gid}: {str(e)[:160]}")
            continue
        if issues:
            status["issues"][gid] = issues[:5]
        if gid not in have:
            for t in PLAYER_EVENT_TABLES:
                df = tables.get(t)
                if df is not None and len(df):
                    ledger.append_rows(f"player_events/{t}", _jsonable(df), observed_at=now, meta={"game_id": gid, "source": "nhl official boxscore+pbp+shiftcharts"})
            have.add(gid)
            status["games_ingested"].append(gid)
        sk, gl, goals = tables["players"], tables["goalies"], tables["goals"]
        if len(goals):
            goals = goals[goals["period_type"] != "SO"]
        for c in pcs:
            if c.family in PERIOD_FAMILIES:
                rec = settle_period_contract(c, goals, res.home_team_id, res.away_team_id, True, not [i for i in issues if not i.startswith("shifts")],
                                             kres.get(c.ticker), now, res.stat_correction_version)
                status["n_period_records"] += 1
            else:
                rec = settle_player_contract(c, sk if len(sk) else pd.DataFrame(columns=["team_id", "sweater", "name"]),
                                             gl if len(gl) else pd.DataFrame(columns=["team_id", "sweater", "name"]), goals, True, kres.get(c.ticker), now,
                                             "nhl_boxscore+pbp", res.stat_correction_version)
            if rec.idempotency_key not in existing:
                existing[rec.idempotency_key] = rec
                new_records.append(rec)
                status["n_records"] += 1
                if rec.reason.startswith("DISAGREES_WITH_KALSHI"):
                    disagreements.append(f"{rec.ticker}: {rec.reason[:160]}")
    return status
