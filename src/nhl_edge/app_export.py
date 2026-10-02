"""Edge Finder app export: the archive's current state -> ``edge_finder.app.v1`` documents.

A pure adapter. It reads what the production jobs already wrote (schedule snapshot, reconstructed
Kalshi board, ``slates/latest`` slate + thesis packet, STATUS/LEASE breadcrumbs, the routed-wager
accounting ledger) and maps each internal object onto the vendored contract constructors in
``contract/edge_finder_contract``. Nothing here prices, simulates, stakes or decides: every number is
copied from a record the repository produced, and every object keeps its research-only authority.

Three different things, never conflated:
    model price      one row per (run, Kalshi market) from the DATA_ONLY_V1 production slate
    recommendation   one thesis-card entry (RESEARCH_CANDIDATE, authority RESEARCH_ONLY)
    wager            one order the owner placed, as the router delivered it to ``accounting-data``

Failure policy: :func:`export` publishes atomically; if anything raises it writes ONLY ``health.json``
(``export_failed=True``), leaves the last-known-good payload untouched and returns non-zero.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from nhl_edge.config import REPO_ROOT

CONTRACT_DIR = REPO_ROOT / "contract"
if str(CONTRACT_DIR) not in sys.path:
    sys.path.insert(0, str(CONTRACT_DIR))

# The vendored contract package is not installed; CONTRACT_DIR is put on sys.path above, hence the E402 markers.
from edge_finder_contract import board as board_mod  # noqa: E402
from edge_finder_contract import build, freshness, ids, linkage, publish, timeutil  # noqa: E402
from edge_finder_contract import health as health_mod  # noqa: E402
from edge_finder_contract import performance as performance_mod  # noqa: E402

SPORT = "NHL"
SOURCE_REPO = "chmoses98/NHL-edge-finder"
SOURCE_BRANCH = "data-archive"
APP_ROOT_RELATIVE = Path("app") / "latest"
EVENT_SOURCE = "nhl_game_id"
TEAM_SOURCE = "nhl_team_id"
PLAYER_SOURCE = "nhl_player_id"
BET_AUTHORITY = "RESEARCH_ONLY"
WAGER_SOURCE = "KALSHI_ROUTER"
PRIMARY_MODEL_VERSION = "DATA_ONLY_V1"

#: Capture runs every 5-15 minutes while games are near; the slate is re-priced at most hourly.
THRESHOLDS = {
    "market_data": freshness.Thresholds(20 * 60, 60 * 60),
    "model": freshness.Thresholds(60 * 60, 6 * 60 * 60),
}

EVENT_STATUS = {
    "not_started": "SCHEDULED", "scheduled": "SCHEDULED", "pregame": "SCHEDULED", "fut": "SCHEDULED", "pre": "SCHEDULED",
    "live": "LIVE", "in_progress": "LIVE", "critical": "LIVE",
    "final": "FINAL", "off": "FINAL", "official": "FINAL",
    "postponed": "POSTPONED", "canceled": "CANCELLED", "cancelled": "CANCELLED",
}
MARKET_STATUS = {
    "active": "OPEN", "open": "OPEN", "closed": "CLOSED", "settled": "SETTLED", "finalized": "SETTLED",
    "determined": "CLOSED", "unopened": "UNOPENED", "initialized": "UNOPENED",
}
GATE_QUALITY = {"OK": "OK", "NO_EDGE": "OK", "CANNOT_TRUST_INPUTS": "CANNOT_TRUST_INPUTS", "UNSUPPORTED": "UNSUPPORTED",
                "NOT_PREGAME": "DEGRADED"}


class ExportInputError(RuntimeError):
    """An input the export cannot build from (missing root, naive timestamp, unreadable ledger ...)."""


# --------------------------------------------------------------------------------------------- helpers
def _read_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ExportInputError(f"{path.name}: {exc}") from exc


def _ts(value: Any, what: str) -> str:
    """Canonical UTC or a clear error naming the field: a naive timestamp never reaches the app."""
    try:
        return timeutil.to_iso(value)
    except timeutil.NaiveTimestampError as exc:
        raise ExportInputError(f"{what}: {exc}") from exc


def _ts_or_none(value: Any, what: str) -> str | None:
    return None if value in (None, "") else _ts(value, what)


def _f(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _compact(d: dict) -> dict:
    return {k: v for k, v in d.items() if v is not None}


def _event_status(row: dict) -> str:
    return EVENT_STATUS.get(str(row.get("status") or "").lower(), "UNKNOWN")


def _market_status(m: dict) -> str:
    return MARKET_STATUS.get(str(m.get("status") or "").lower(), "UNKNOWN")


def resolve_accounting_dir(path: Path | None) -> Path | None:
    """Accept the ``accounting-data`` checkout root or the ``data/accounting`` directory itself."""
    if path is None:
        return None
    path = Path(path)
    if (path / "data" / "accounting").is_dir():
        return path / "data" / "accounting"
    return path


# --------------------------------------------------------------------------------------------- inputs
@dataclass
class Inputs:
    """Everything the export reads, loaded once so the build is a pure function of this object."""

    root: Path
    schedule_rows: list[dict] = field(default_factory=list)
    schedule_path: str | None = None
    schedule_observed_at: str | None = None
    board_rows: list[dict] = field(default_factory=list)
    board_observed_at: str | None = None
    board_provenance: str | None = None
    slate: dict | None = None
    packet: dict | None = None
    status_capture: dict | None = None
    status_simulate: dict | None = None
    status_context: dict | None = None
    lease: dict | None = None
    wager_rows: list[dict] = field(default_factory=list)
    settlement_rows: list[dict] = field(default_factory=list)
    accounting_dir: Path | None = None
    warnings: list[str] = field(default_factory=list)


def load_inputs(root: Path, accounting_dir: Path | None = None) -> Inputs:
    from nhl_edge.accounting.ledger import SETTLEMENTS_FILE, WAGERS_FILE, read_jsonl
    from nhl_edge.archive.ledger import Ledger
    from nhl_edge.archive.reconstruct import latest_board
    from nhl_edge.workflows.conductor import _latest_schedule

    root = Path(root)
    if not root.is_dir():
        raise ExportInputError(f"archive root {root} does not exist")
    inp = Inputs(root=root)
    ledger = Ledger(root)
    entry = ledger.latest("context/schedule")
    if entry is not None:
        inp.schedule_rows = _latest_schedule(ledger)
        inp.schedule_path = entry.path
        inp.schedule_observed_at = entry.observed_at_utc or entry.written_at_utc
    else:
        inp.warnings.append("no context/schedule snapshot in the archive")
    rec = latest_board(ledger)
    if rec is not None:
        inp.board_rows = list(rec.rows)
        inp.board_observed_at = rec.observed_at_utc
        inp.board_provenance = rec.provenance()
    else:
        inp.warnings.append("no Kalshi board in the archive")
    inp.slate = _read_json(root / "slates" / "latest" / "slate.json")
    inp.packet = _read_json(root / "slates" / "latest" / "packet.json")
    if inp.slate is None:
        inp.warnings.append("no slates/latest/slate.json: no model prices or recommendations")
    inp.status_capture = _read_json(root / "STATUS_capture.json")
    inp.status_simulate = _read_json(root / "STATUS_simulate.json")
    inp.status_context = _read_json(root / "STATUS_context.json")
    inp.lease = _read_json(root / "LEASE_capture.json")
    acc = resolve_accounting_dir(accounting_dir)
    inp.accounting_dir = acc
    if acc is not None:
        if not acc.is_dir():
            inp.warnings.append(f"accounting dir {acc} not found: wagers/settlements empty")
        else:
            inp.wager_rows = read_jsonl(acc / WAGERS_FILE.name)
            inp.settlement_rows = read_jsonl(acc / SETTLEMENTS_FILE.name)
    else:
        inp.warnings.append("no accounting dir given: wagers/settlements empty")
    return inp


# ---------------------------------------------------------------------------------------------- build
def _team_participant(reg, team_id: int | None, abbrev: str | None) -> dict | None:
    if team_id is None:
        return None
    try:
        team = reg.by_id(team_id)
        name, short = team.name, team.abbrev
        meta = {"city": team.city, "nickname": team.nickname, "conference": team.conference, "division": team.division}
    except Exception:  # noqa: BLE001 - an identity gap must not drop the game
        name, short, meta = str(abbrev or team_id), abbrev, {}
    return build.participant(sport=SPORT, participant_type="TEAM", source=TEAM_SOURCE, source_id=int(team_id),
                             display_name=name, short_name=short, source_ids={"nhl_abbrev": short}, metadata=meta)


def _slate_date(inp: Inputs) -> str | None:
    for src in (inp.status_simulate, inp.slate):
        if src and src.get("date_et"):
            return str(src["date_et"])
    dates = sorted(str(r["game_date_et"]) for r in inp.schedule_rows if r.get("game_date_et") and _event_status(r) != "FINAL")
    return dates[0] if dates else None


def _contracts(inp: Inputs) -> list[tuple[dict, Any]]:
    from nhl_edge.identity.teams import registry
    from nhl_edge.kalshi.contracts import build_contract
    from nhl_edge.kalshi.ontology import Ontology

    onto, reg = Ontology.load(), registry()
    out = []
    for m in inp.board_rows:
        try:
            out.append((m, build_contract(m, onto, reg)))
        except Exception as exc:  # noqa: BLE001 - one unreadable market must not stop the export
            inp.warnings.append(f"contract {m.get('ticker')}: {type(exc).__name__}: {str(exc)[:120]}")
            out.append((m, None))
    return out


def _side(contract, row: dict | None) -> str | None:
    if contract is None:
        return None
    if contract.team_id is not None and row is not None:
        if int(row.get("home_team_id") or -1) == contract.team_id:
            return "HOME"
        if int(row.get("away_team_id") or -1) == contract.team_id:
            return "AWAY"
        return "PARTICIPANT"
    if contract.comparator in ("gt", "ge") and contract.threshold is not None and "total" in (contract.family or ""):
        return "OVER"
    if contract.comparator in ("lt", "le") and contract.threshold is not None and "total" in (contract.family or ""):
        return "UNDER"
    return None


def build_documents(root: Path, *, accounting_dir: Path | None = None, now: datetime | str | None = None,
                    commit_sha: str | None = None, workflow_run_id: str | None = None,
                    source_branch: str = SOURCE_BRANCH, inputs: Inputs | None = None) -> dict[str, Any]:
    """Every app document for the archive at ``root``. Pure: same inputs + same ``now`` -> same bytes.

    Returns ``{"documents": {...}, "health": ..., "run_id": ..., "generated_at": ..., "freshness": ...,
    "warnings": [...], "model_version": ..., "status": ...}`` ready for :func:`publish.publish`."""
    from nhl_edge.identity.teams import registry
    from nhl_edge.kalshi.contracts import game_key

    now_iso = timeutil.to_iso(now or timeutil.now_utc())
    inp = inputs or load_inputs(root, accounting_dir)
    reg = registry()
    warnings = list(inp.warnings)
    slate = inp.slate or {}
    packet = inp.packet or {}
    sim = inp.status_simulate or {}
    date_et = _slate_date(inp)

    # -- run identity --------------------------------------------------------------------------
    native_run = None
    if sim.get("run_id") or sim.get("simulated_at_utc"):
        native_run = f"{sim.get('run_id') or 'slate'}:{_ts(sim.get('simulated_at_utc') or slate.get('generated_at_utc'), 'STATUS_simulate.simulated_at_utc')}"
    elif slate.get("run_id"):
        native_run = f"{slate['run_id']}:{_ts(slate.get('generated_at_utc'), 'slate.generated_at_utc')}"
    elif inp.status_capture:
        native_run = f"capture:{inp.status_capture.get('run_id')}:{_ts_or_none(inp.status_capture.get('last_capture_utc'), 'STATUS_capture')}"
    model_version = slate.get("model_version") or PRIMARY_MODEL_VERSION
    run_id = ids.run_id(SPORT, SOURCE_REPO, native_run, generated_at=now_iso)

    # -- events ---------------------------------------------------------------------------------
    sched_by_game: dict[str, dict] = {}
    sched_key: dict[tuple, str] = {}
    for r in inp.schedule_rows:
        gid = str(r.get("game_id") or "")
        if not gid:
            continue
        sched_by_game[gid] = r
        try:
            sched_key[(str(r["game_date_et"]), frozenset({int(r["home_team_id"]), int(r["away_team_id"])}))] = gid
        except (KeyError, TypeError, ValueError):
            continue

    contracts = _contracts(inp)
    market_game: dict[str, str] = {}  # ticker -> nhl game id
    slate_game = {str(c.get("ticker")): str(c.get("game_id")) for c in slate.get("contracts", []) if c.get("game_id")}
    for m, c in contracts:
        gid = None
        if c is not None:
            key = game_key(c)
            gid = sched_key.get(key) if key else None
        gid = gid or slate_game.get(str(m.get("ticker")))
        if gid:
            market_game[str(m.get("ticker"))] = gid
    player_ids = {str(c.get("ticker")): c for c in (packet.get("player_shadow") or {}).get("contracts", []) if c.get("player_id")}

    exported_games: set[str] = set()
    if date_et:
        exported_games |= {g for g, r in sched_by_game.items() if str(r.get("game_date_et")) == date_et}
    for c in slate.get("contracts", []):
        if c.get("game_id") and str(c["game_id"]) in sched_by_game:
            exported_games.add(str(c["game_id"]))
    for w in inp.wager_rows:
        gid = market_game.get(str(w.get("market_ticker")))
        if gid:
            exported_games.add(gid)
    # The game-level Kalshi event ticker (KXNHLGAME-<date><tricodes>) names the game; player/period series carry
    # their own event tickers and are joined through the market rows, not listed on the event.
    game_event_ticker: dict[str, str] = {}
    for m, _c in contracts:
        gid = market_game.get(str(m.get("ticker")))
        if gid and str(m.get("series_ticker") or "") == "KXNHLGAME" and m.get("event_ticker"):
            game_event_ticker.setdefault(gid, str(m["event_ticker"]))

    events: dict[str, dict] = {}
    event_of_game: dict[str, str] = {}
    for gid in sorted(exported_games):
        r = sched_by_game[gid]
        home = _team_participant(reg, r.get("home_team_id"), r.get("home_abbrev"))
        away = _team_participant(reg, r.get("away_team_id"), r.get("away_abbrev"))
        observed = _ts_or_none(r.get("_observed_at_utc"), "schedule._observed_at_utc") or inp.schedule_observed_at
        ev = build.event(
            sport=SPORT, source=EVENT_SOURCE, source_id=gid, start_time_utc=_ts(r.get("start_time_utc"), f"schedule {gid}.start_time_utc"),
            participants=[p for p in (home, away) if p], home_participant=home["participant_id"] if home else None,
            away_participant=away["participant_id"] if away else None, league="NHL", season=r.get("season"),
            competition=r.get("season_type"), status=_event_status(r), start_time_source=r.get("source") or "nhl_api_schedule",
            start_time_confidence="SCHEDULED", venue=r.get("venue"),
            source_ids={"kalshi_event_ticker": game_event_ticker.get(gid)},
            schedule_updated_at=observed, last_updated_at=observed or now_iso,
            extensions=_compact({"game_date_et": r.get("game_date_et"), "source_game_state": r.get("source_game_state"),
                                 "home_abbrev": r.get("home_abbrev"), "away_abbrev": r.get("away_abbrev"),
                                 "home_score": r.get("home_score"), "away_score": r.get("away_score"),
                                 "neutral_site": r.get("neutral_site")}),
        )
        events[ev["event_id"]] = ev
        event_of_game[gid] = ev["event_id"]

    # -- markets --------------------------------------------------------------------------------
    markets: dict[str, dict] = {}
    captured_at = _ts_or_none(inp.board_observed_at, "board.observed_at")
    for m, c in contracts:
        ticker = str(m.get("ticker") or "")
        if not ticker:
            continue
        gid = market_game.get(ticker)
        row = sched_by_game.get(gid) if gid else None
        q = m.get("_quote_cents") or {}
        family = (c.family if c is not None else None) or m.get("_family") or "unknown"
        team_pid = ids.participant_id(SPORT, "TEAM", TEAM_SOURCE, c.team_id) if c is not None and c.team_id is not None else None
        pl = player_ids.get(ticker)
        player_pid = ids.participant_id(SPORT, "PLAYER", PLAYER_SOURCE, pl["player_id"]) if pl else None
        threshold = c.threshold if c is not None else _f(m.get("floor_strike"))
        try:
            mk = build.market(
                sport=SPORT, kalshi_ticker=ticker, market_family=family,
                yes_description=str(m.get("title") or m.get("yes_sub_title") or ticker), source="kalshi",
                event_id=event_of_game.get(gid) if gid else None, kalshi_event_ticker=m.get("event_ticker"),
                kalshi_series_ticker=m.get("series_ticker"), market_type=m.get("market_type"),
                period=c.period if c is not None else None, participant_id=team_pid, player_id=player_pid,
                side=_side(c, row), line=threshold if ("spread" in family or "total" in family) else None, threshold=threshold,
                no_description=m.get("no_sub_title"), yes_bid=build.from_cents(q.get("yes_bid")), yes_ask=build.from_cents(q.get("yes_ask")),
                no_bid=build.from_cents(q.get("no_bid")), no_ask=build.from_cents(q.get("no_ask")),
                last_price=build.from_cents(q.get("last_price")), volume=_f(m.get("volume") if m.get("volume") is not None else m.get("volume_fp")),
                open_interest=_f(m.get("open_interest") if m.get("open_interest") is not None else m.get("open_interest_fp")),
                market_status=_market_status(m), close_time_utc=_ts_or_none(m.get("close_time"), f"{ticker}.close_time"),
                captured_at=_ts_or_none(m.get("_observed_at_utc"), f"{ticker}._observed_at_utc") or captured_at,
                raw_market_reference=f"kalshi/markets@{captured_at}" if captured_at else None,
                extensions=_compact({
                    "nhl_game_id": gid, "support": c.support if c is not None else m.get("_support"),
                    "scope": c.scope if c is not None else None, "stat": c.stat if c is not None else None,
                    "settles_on": c.settles_on if c is not None else None, "comparator": c.comparator if c is not None else None,
                    "semantics_confidence": c.semantics_confidence if c is not None else None,
                    "nhl_team_id": c.team_id if c is not None else None, "nhl_player_id": pl["player_id"] if pl else None,
                    "entity_name": (c.entity_name if c is not None else None) or (pl.get("player_name") if pl else None),
                    "kalshi_entity_uuid": c.kalshi_entity_uuid if c is not None else None, "strike_type": m.get("strike_type"),
                }),
            )
        except Exception as exc:  # noqa: BLE001 - keep the rest of the board
            warnings.append(f"market {ticker} skipped: {type(exc).__name__}: {str(exc)[:120]}")
            continue
        markets[mk["market_id"]] = mk

    # -- model prices (DATA_ONLY_V1, the production model) ----------------------------------------
    model_prices: list[dict] = []
    skipped_unpriced = skipped_offboard = 0
    for c in slate.get("contracts", []):
        ticker = str(c.get("ticker") or "")
        if c.get("p_data_only") is None:
            skipped_unpriced += 1
            continue
        mid = ids.market_id(ticker)
        if mid not in markets:
            skipped_offboard += 1
            continue
        gen = _ts(c.get("predicted_at_utc") or slate.get("generated_at_utc"), f"{ticker}.predicted_at_utc")
        gate = str(c.get("gate") or "UNKNOWN")
        model_prices.append(build.model_price(
            run_id=run_id, market_id=mid, fair_probability=c["p_data_only"], generated_at=gen,
            event_id=event_of_game.get(str(c.get("game_id"))), model_version=c.get("model_version") or model_version,
            uncertainty=c.get("p_data_only_se"), market_probability=c.get("p_market"),
            inputs_as_of=_ts_or_none(c.get("market_observed_at_utc"), f"{ticker}.market_observed_at_utc"),
            freshness_status=freshness.status_for(gen, now=now_iso, thresholds=THRESHOLDS["model"]),
            data_quality_status=GATE_QUALITY.get(gate, "UNKNOWN"), support_status=gate,
            extensions=_compact({
                "p_data_only": c.get("p_data_only"), "p_market_anchored": c.get("p_market_anchored"),
                "executable_p_yes": c.get("executable_p_yes"), "executable_p_no": c.get("executable_p_no"),
                "edge_yes_after_fee": c.get("edge_yes_after_fee"), "edge_no_after_fee": c.get("edge_no_after_fee"),
                "best_side": c.get("best_side"), "gate": gate, "gate_reasons": list(c.get("gate_reasons") or []) or None,
                "prediction_id": c.get("prediction_id"), "support": c.get("support"), "pregame": c.get("pregame"),
                "horizon_label": c.get("horizon_label"), "sim_version": c.get("sim_version"),
                "feature_version": c.get("feature_version"), "market_anchored_model_version": c.get("market_anchored_model_version"),
                "data_cutoff_utc": _ts_or_none(c.get("data_cutoff_utc"), f"{ticker}.data_cutoff_utc"),
            }),
        ))
    if skipped_offboard:
        warnings.append(f"{skipped_offboard} slate contract(s) are no longer on the board; model prices skipped")

    # -- theses + recommendations (thesis card, RESEARCH_ONLY) --------------------------------------
    tc = packet.get("thesis_card") or slate.get("thesis_card") or {}
    tc_games = {str(g.get("game_id")): g for g in tc.get("games", []) if isinstance(g, dict)}
    card_at = _ts_or_none(tc.get("generated_at_utc") or slate.get("generated_at_utc"), "thesis_card.generated_at_utc")
    theses: dict[str, dict] = {}
    recommendations: list[dict] = []
    slate_games = {str(g.get("game_id")): g for g in slate.get("games", []) if isinstance(g, dict)}
    packet_games = {str((g.get("identity") or {}).get("game_id")): g for g in packet.get("games", []) if isinstance(g, dict)}

    def _scripts(g: dict) -> list[dict]:
        return sorted((s for s in g.get("scripts", []) if isinstance(s, dict)), key=lambda s: -(s.get("frequency") or 0))

    for gid, g in sorted(tc_games.items()):
        eid = event_of_game.get(gid)
        if not eid or not card_at:
            continue
        pg = packet_games.get(gid, {})
        ctx = pg.get("context") or {}
        goalies = pg.get("goaltending") or {}
        injuries = [f"{i.get('player_name')} ({i.get('status')}{': ' + str(i['detail']) if i.get('detail') else ''})"
                    for i in ctx.get("injuries", []) if isinstance(i, dict) and i.get("player_name")]
        lineup = "; ".join(f"{side} G {gl.get('player_name')} {gl.get('status')}" for side, gl in goalies.items()
                           if isinstance(gl, dict) and gl.get("player_name"))
        majors = [s for s in _scripts(g) if s.get("major")] or _scripts(g)
        sg = slate_games.get(gid, {})
        th = build.thesis(
            sport=SPORT, run_id=run_id, event_id=eid, generated_at=card_at, summary=None,
            primary_game_script=majors[0].get("name") if majors else None,
            context_notes={"injuries": ", ".join(injuries) or None, "lineups": lineup or None,
                           "usage": (g.get("meta") or {}).get("source"), "other": None},
            evidence=_compact({
                "thesis_events": [{"key": t.get("key"), "label": t.get("label"), "p": t.get("p")} for t in g.get("thesis_events", [])][:40],
                "scripts": [{"name": s.get("name"), "frequency": s.get("frequency"), "major": s.get("major")} for s in _scripts(g)[:8]],
                "matchup": g.get("matchup"), "n_sims": g.get("n_sims"),
                "p_home_win": sg.get("p_home_win"), "p_away_win": sg.get("p_away_win"), "exp_total": sg.get("exp_total"),
                "rest": _compact({k: ctx.get(k) for k in ("home_rest_days", "away_rest_days", "home_b2b", "away_b2b")}) or None,
            }),
        )
        theses[th["thesis_id"]] = th

    recommended_ids = {str(r.get("bet_id")) for r in tc.get("recommended", [])}
    cards = [e for g in tc.get("games", []) if isinstance(g, dict) for e in g.get("card", []) if isinstance(e, dict)]
    if not cards and tc.get("recommended"):
        warnings.append("thesis card lacks packet.json detail; recommendations built from slate.thesis_card.recommended only")
        cards = [{"bet_id": r.get("bet_id"), "contract": {"ticker": str(r.get("bet_id", "")).split("|")[0], "title": r.get("title"), "side": r.get("side")},
                  "executable_price": {"ask_cents": r.get("ask")}, "fair_probability": {"p_model_joint_draw": r.get("p"), "p_confidence_adjusted": r.get("p_adj")},
                  "recommended_stake": {"dollars": r.get("stake"), "nominal_bankroll": (tc.get("portfolio_config") or {}).get("bankroll")},
                  "primary_thesis": {"key": r.get("primary_thesis")}, "game_id": slate_game.get(str(r.get("bet_id", "")).split("|")[0])}
                 for r in tc["recommended"]]
    for e in cards:
        bet_id = str(e.get("bet_id") or "")
        if recommended_ids and bet_id not in recommended_ids:
            continue  # shortlisted but not recommended by the portfolio optimiser
        ct = e.get("contract") or {}
        ticker = str(ct.get("ticker") or bet_id.split("|")[0])
        gid = str(e.get("game_id") or market_game.get(ticker) or "")
        eid = event_of_game.get(gid)
        if not eid or not card_at:
            warnings.append(f"recommendation {bet_id}: game {gid or '?'} not on the exported board; skipped")
            continue
        mid = ids.market_id(ticker)
        if mid not in markets:
            stub = build.market_stub(sport=SPORT, kalshi_ticker=ticker, market_family=ct.get("family") or "unknown",
                                     yes_description=ct.get("title"), event_id=eid, source="thesis_card", market_status="UNKNOWN")
            markets[mid] = stub
            warnings.append(f"recommendation {bet_id}: market left the board; stub emitted")
        selection = str(ct.get("side") or bet_id.split("|")[-1]).upper()
        px = e.get("executable_price") or {}
        fair = e.get("fair_probability") or {}
        edge = e.get("estimated_edge") or {}
        upto = e.get("bet_up_to_price") or {}
        stake = e.get("recommended_stake") or {}
        rel = e.get("family_reliability") or {}
        prim = e.get("primary_thesis") or {}
        sec = e.get("secondary_thesis") or {}
        fail = e.get("failure_case") or {}
        conc = e.get("thesis_concentration") or {}
        proj = fair.get("projection") or {}
        mid_yes = fair.get("p_kalshi_mid")
        current_prob = None if mid_yes is None else (float(mid_yes) if selection == "YES" else round(1.0 - float(mid_yes), 6))
        row = sched_by_game.get(gid, {})
        thesis = build.thesis(
            sport=SPORT, run_id=run_id, event_id=eid, generated_at=card_at, scope=bet_id,
            summary=prim.get("label"), primary_game_script=((conc.get("main_scripts") or [{}])[0]).get("script"),
            supporting_factors=[x for x in (e.get("reason_chosen"), sec.get("label")) if x],
            opposing_factors=[x for x in ((fail.get("failure_thesis") or {}).get("label"), (fail.get("worst_major_script") or {}).get("script"), fail.get("note")) if x],
            key_dependencies=list(fail.get("scripts_needed") or []),
            context_notes={"lineups": proj.get("deployment_source"), "usage": proj.get("role_confidence"),
                           "injuries": ", ".join(proj.get("uncertainty_flags") or []) or None, "other": rel.get("family_evidence")},
            confidence_label=rel.get("label"),
            evidence=_compact({
                "primary_thesis": prim or None, "secondary_thesis": sec or None,
                "failure": _compact({"p_lose": fail.get("p_lose"), "worst_major_script": fail.get("worst_major_script")}) or None,
                "thesis_concentration": _compact({k: conc.get(k) for k in ("top1", "top2", "breadth_eff", "breadth_rel")}) or None,
                "estimated_edge": edge or None, "fair_probability": _compact({k: fair.get(k) for k in ("p_model_joint_draw", "p_confidence_adjusted", "confidence_k", "p_kalshi_mid", "p_v1", "p_sportsbook")}) or None,
                "bucket_calibration": rel.get("bucket_calibration"), "best_alternative": e.get("best_alternative"),
            }),
        )
        theses[thesis["thesis_id"]] = thesis
        native_id = f"{bet_id}|{tc.get('run_id') or slate.get('run_id') or ''}|{card_at}"
        recommendations.append(build.recommendation(
            sport=SPORT, source_repo=SOURCE_REPO, event_id=eid, market_id=mid, run_id=run_id, selection=selection,
            market_description=f"{selection} {ct.get('title') or ticker}", created_at=card_at, status="RESEARCH_CANDIDATE",
            authority=BET_AUTHORITY, research_only=True, native_id=native_id,
            current_probability=current_prob, current_price=build.from_cents(px.get("ask_cents")),
            fair_probability=fair.get("p_confidence_adjusted") if fair.get("p_confidence_adjusted") is not None else fair.get("p_model_joint_draw"),
            edge=edge.get("ev_adjusted_per_contract"), bet_up_to_probability=build.from_cents(upto.get("cents_adjusted")),
            bet_up_to_price=build.from_cents(upto.get("cents_adjusted")), confidence=rel.get("label"),
            stake_dollars=stake.get("dollars"), bankroll_basis=stake.get("nominal_bankroll") or (tc.get("portfolio_config") or {}).get("bankroll"),
            thesis_id=thesis["thesis_id"], expires_at=_ts_or_none(row.get("start_time_utc"), f"schedule {gid}.start_time_utc"),
            data_freshness=freshness.status_for(card_at, now=now_iso, thresholds=THRESHOLDS["model"]),
            lineup_status=proj.get("deployment_source"), injury_flags=proj.get("uncertainty_flags") or [],
            source_ids={"bet_id": bet_id, "kalshi_ticker": ticker, "nhl_game_id": gid, "thesis_run_id": tc.get("run_id")},
            extensions=_compact({
                "family": ct.get("family"), "team_opponent": e.get("team_opponent"),
                "fee_per_contract": px.get("fee_per_contract"), "cost_per_contract": px.get("cost_per_contract"),
                "price_observed_at_utc": _ts_or_none(px.get("observed_at_utc"), f"{bet_id}.observed_at_utc"),
                "p_model_joint_draw": fair.get("p_model_joint_draw"), "p_confidence_adjusted": fair.get("p_confidence_adjusted"),
                "p_kalshi_mid_yes": mid_yes, "ev_raw_per_contract": edge.get("ev_raw_per_contract"), "roi_adjusted": edge.get("roi_adjusted"),
                "growth_bp": edge.get("growth_bp"), "bet_up_to_cents_raw": upto.get("cents_raw"),
                "stake_fraction_of_bankroll": stake.get("fraction_of_bankroll"), "stake_contracts": stake.get("contracts"),
                "stake_authority": stake.get("authority"), "family_reliability": rel.get("label"), "reliability_flags": list(rel.get("flags") or []) or None,
                "primary_thesis_key": prim.get("key"), "secondary_thesis_key": sec.get("key"),
                "best_alternative_bet_id": (e.get("best_alternative") or {}).get("bet_id"),
                "recommended_portfolio": tc.get("recommended_portfolio"), "thesis_version": tc.get("thesis_version"),
                "card_version": tc.get("card_version"), "portfolio_impact": e.get("portfolio_impact"),
            }),
        ))

    # -- wagers + settlements (accounting-data ledger; empty is a valid state) -----------------------
    settle_rows = {str(s.get("source_bet_key")): s for s in inp.settlement_rows}
    wagers: list[dict] = []
    settlements: list[dict] = []
    for w in inp.wager_rows:
        ticker = str(w.get("market_ticker") or "")
        key = str(w.get("source_bet_key") or "")
        srow = settle_rows.get(key)
        mid = ids.market_id(ticker)
        gid = market_game.get(ticker)
        eid = event_of_game.get(gid) if gid else None
        if mid not in markets:
            markets[mid] = build.market_stub(sport=SPORT, kalshi_ticker=ticker, event_id=eid, source="accounting_ledger",
                                             market_status="SETTLED" if srow else "UNKNOWN")
        wg = build.wager(
            sport=SPORT, kalshi_ticker=ticker, selection=str(w.get("side")), contracts=w.get("contracts"), stake=w.get("stake"),
            average_price=w.get("execution_price"), placed_at=_ts(w.get("executed_at"), f"wager {w.get('wager_id')}.executed_at"),
            source=WAGER_SOURCE, destination_repo=SOURCE_REPO, source_bet_key=key or None, native_id=w.get("wager_id"),
            event_id=eid, side="BUY", fees=w.get("fees_paid"),
            source_ids={"wager_id": w.get("wager_id"), "import_batch_id": w.get("import_batch_id"), "nhl_game_id": gid},
            extensions=_compact({"game_date": w.get("game_date"), "venue": w.get("venue"), "entry_method": w.get("entry_method"),
                                 "fees_are_estimated": w.get("fees_are_estimated"), "schema_version": w.get("schema_version")}),
        )
        if srow is not None:
            established = srow.get("gross_return") is not None and srow.get("net_profit_loss") is not None
            result = str(srow.get("result") or "UNKNOWN")
            winning = None
            if result in ("WON", "LOST"):
                winning = wg["selection"] if result == "WON" else ("NO" if wg["selection"] == "YES" else "YES")
            st = build.settlement(
                wager_id=wg["wager_id"], market_id=mid, result=result if result in ("WON", "LOST") else "UNKNOWN",
                settled_at=_ts(srow.get("settled_at"), f"settlement {srow.get('settlement_id')}.settled_at"), source=WAGER_SOURCE,
                verification_status="EXCHANGE_CONFIRMED" if established else "REFUSED", winning_side=winning,
                gross_payout=srow.get("gross_return"), net_pnl=srow.get("net_profit_loss"), refusals=srow.get("refusals") or [],
                source_ids={"settlement_id": srow.get("settlement_id"), "source_bet_key": key},
                extensions=_compact({"economics_version": srow.get("economics_version"), "venue": srow.get("venue"),
                                     "schema_version": srow.get("schema_version")}),
            )
            settlements.append(st)
            wg["settlement_id"], wg["settlement_status"] = st["settlement_id"], "SETTLED"
            wg["payout"], wg["profit_loss"] = st["gross_payout"], st["net_pnl"]
        wagers.append(wg)
    market_list = list(markets.values())
    wagers = [linkage.apply_links(w, model_prices, recommendations, market_list) for w in wagers]
    for key in settle_rows.keys() - {str(w.get("source_bet_key")) for w in inp.wager_rows}:
        warnings.append(f"settlement for source_bet_key {key[:40]} has no wager row; skipped")

    # -- run, health, board, performance, detail ------------------------------------------------------
    last_capture = captured_at or _ts_or_none((inp.status_capture or {}).get("last_capture_utc"), "STATUS_capture.last_capture_utc")
    last_model = _ts_or_none(slate.get("generated_at_utc") or sim.get("simulated_at_utc"), "slate.generated_at_utc")
    context_at = _ts_or_none((inp.status_context or {}).get("refreshed_at_utc"), "STATUS_context.refreshed_at_utc")
    next_run = _ts_or_none((inp.lease or {}).get("expected_next_capture_at"), "LEASE_capture.expected_next_capture_at")
    settlement_as_of = max((s["settled_at"] for s in settlements), default=None)
    status = "PARTIAL" if (not inp.board_rows or inp.slate is None) else "SUCCESS"
    run = build.run(
        sport=SPORT, repo=SOURCE_REPO, completed_at=now_iso, scope=f"slate {date_et}" if date_et else "archive", status=status,
        native_run_id=native_run, commit_sha=commit_sha, workflow_run_id=workflow_run_id, model_version=model_version,
        started_at=last_model, events_requested=len([g for g, r in sched_by_game.items() if str(r.get("game_date_et")) == date_et]) if date_et else None,
        events_processed=len(events), markets_discovered=len(market_list), markets_priced=len(model_prices),
        recommendations_created=len(recommendations),
        data_sources=[s for s in (inp.board_provenance, inp.schedule_path, f"slates/{sim.get('out_dir')}" if sim.get("out_dir") else None,
                                  str(inp.accounting_dir) if inp.accounting_dir else None) if s],
        input_freshness={"kalshi": last_capture, "schedule": inp.schedule_observed_at, "model": last_model, "context": context_at,
                         "accounting": settlement_as_of},
        warnings=warnings,
        source_ids={"simulate_run_id": sim.get("run_id"), "capture_run_id": (inp.status_capture or {}).get("run_id"), "date_et": date_et,
                    "sim_version": slate.get("sim_version"), "feature_version": slate.get("feature_version")},
    )
    assert run["run_id"] == run_id
    health = health_mod.build_health(
        sport=SPORT, run_id=run_id, bet_authority=BET_AUTHORITY, last_market_capture=last_capture, last_model_generated=last_model,
        last_successful_run=now_iso, payload_run_id=run_id, payload_available=True, export_failed=False, commit_sha=commit_sha,
        next_scheduled_run=next_run, router_as_of=None, settlement_as_of=settlement_as_of, model_required=True,
        thresholds=THRESHOLDS, warnings=warnings, now=now_iso, generated_at=now_iso,
    )
    model_price_list = list(model_prices)
    rec_list = list(recommendations)
    thesis_list = list(theses.values())
    event_list = sorted(events.values(), key=lambda e: (e["start_time_utc"], e["event_id"]))
    docs: dict[str, Any] = {
        "events": build.collection("events", SPORT, run_id, now_iso, event_list),
        "markets": build.collection("markets", SPORT, run_id, now_iso, sorted(market_list, key=lambda m: m["market_id"])),
        "model_prices": build.collection("model_prices", SPORT, run_id, now_iso, model_price_list),
        "recommendations": build.collection("recommendations", SPORT, run_id, now_iso, rec_list),
        "theses": build.collection("theses", SPORT, run_id, now_iso, thesis_list),
        "wagers": build.collection("wagers", SPORT, run_id, now_iso, wagers),
        "settlements": build.collection("settlements", SPORT, run_id, now_iso, settlements),
        "runs": build.collection("runs", SPORT, run_id, now_iso, [run]),
    }
    docs["board"] = board_mod.build_board(sport=SPORT, run_id=run_id, generated_at=now_iso, events=event_list, markets=market_list,
                                          model_prices=model_price_list, recommendations=rec_list, wagers=wagers, health=health,
                                          thresholds=THRESHOLDS, now=now_iso)
    docs["performance"] = performance_mod.build_performance(
        sport=SPORT, run_id=run_id, generated_at=now_iso, wagers=wagers, settlements=settlements, markets=market_list,
        recommendations=rec_list, bankroll_basis=None,
        notes=["wagers are the owner's manual Kalshi orders as delivered by kalshi-bet-router to the accounting-data branch; "
               "no model placed or routed anything (RESEARCH_ONLY)"] + (["accounting ledger is empty"] if not wagers else []),
    )
    board_rows = {r["event_id"]: r for r in docs["board"]["items"]}
    for ev in event_list:
        gid = ev["source_ids"].get(EVENT_SOURCE)
        pg = packet_games.get(str(gid), {})
        sg = slate_games.get(str(gid), {})
        context = _compact({
            "nhl_game_id": gid, "matchup": (tc_games.get(str(gid)) or {}).get("matchup"),
            "goaltending": {side: _compact({k: gl.get(k) for k in ("team_id", "status", "player_id", "player_name", "confidence", "observed_at_utc", "source")})
                            for side, gl in (pg.get("goaltending") or {}).items() if isinstance(gl, dict)} or None,
            "rest": _compact({k: (pg.get("context") or {}).get(k) for k in ("home_rest_days", "away_rest_days", "home_b2b", "away_b2b")}) or None,
            "injuries": [_compact({k: i.get(k) for k in ("team_id", "player_name", "position", "status", "detail", "return_date")})
                         for i in (pg.get("context") or {}).get("injuries", []) if isinstance(i, dict)] or None,
            "model_game": _compact({k: sg.get(k) for k in ("p_home_win", "p_away_win", "p_home_reg_win", "p_away_reg_win", "p_overtime", "p_shootout",
                                                           "exp_home_goals", "exp_away_goals", "exp_total", "inputs_trusted", "input_reasons", "horizon")}) or None,
            "authority": BET_AUTHORITY,
        })
        docs[f"event_detail/{ev['event_id']}"] = board_mod.build_event_detail(
            sport=SPORT, run_id=run_id, generated_at=now_iso, event=ev, markets=market_list, model_prices=model_price_list,
            recommendations=rec_list, theses=thesis_list, wagers=wagers, settlements=settlements, context=context,
            data_freshness=board_rows.get(ev["event_id"], {}).get("data_freshness", "UNKNOWN"),
        )
    fresh = {
        "kalshi": {"as_of": last_capture, "status": freshness.status_for(last_capture, now=now_iso, thresholds=THRESHOLDS["market_data"])},
        "schedule": {"as_of": inp.schedule_observed_at, "status": freshness.status_for(inp.schedule_observed_at, component="schedule", now=now_iso)},
        "model": {"as_of": last_model, "status": freshness.status_for(last_model, now=now_iso, thresholds=THRESHOLDS["model"])},
        "context": {"as_of": context_at, "status": freshness.status_for(context_at, component="schedule", now=now_iso)},
        "accounting": {"as_of": settlement_as_of, "status": freshness.status_for(settlement_as_of, component="settlement", now=now_iso)},
    }
    return {"documents": docs, "health": health, "run_id": run_id, "generated_at": now_iso, "freshness": fresh, "warnings": warnings,
            "model_version": model_version, "status": status, "source_branch": source_branch,
            "counts": {"events": len(event_list), "markets": len(market_list), "model_prices": len(model_price_list), "recommendations": len(rec_list),
                       "theses": len(thesis_list), "wagers": len(wagers), "settlements": len(settlements), "slate_unpriced_skipped": skipped_unpriced}}


# --------------------------------------------------------------------------------------------- publish
def _failure_health(out: Path, exc: BaseException, *, now_iso: str, commit_sha: str | None, root: Path | None) -> dict:
    previous = None
    try:
        previous = publish.read_manifest(out)
    except (OSError, ValueError):
        previous = None
    run_id = (previous or {}).get("run_id") or ids.run_id(SPORT, SOURCE_REPO, "export-failed", generated_at=now_iso)
    capture = model = None
    if root is not None:
        try:
            capture = _ts_or_none((_read_json(root / "STATUS_capture.json") or {}).get("last_capture_utc"), "STATUS_capture")
            model = _ts_or_none((_read_json(root / "STATUS_simulate.json") or {}).get("simulated_at_utc"), "STATUS_simulate")
        except Exception:  # noqa: BLE001 - the breadcrumbs are optional in the failure path
            capture = model = None
    return health_mod.build_health(
        sport=SPORT, run_id=run_id, bet_authority=BET_AUTHORITY, last_market_capture=capture, last_model_generated=model,
        last_successful_run=(previous or {}).get("generated_at"), payload_run_id=(previous or {}).get("run_id"),
        payload_available=previous is not None, export_failed=True, commit_sha=commit_sha, model_required=True,
        thresholds=THRESHOLDS, errors=[f"{type(exc).__name__}: {str(exc)[:500]}"], now=now_iso, generated_at=now_iso,
    )


def export(root: Path, out: Path, *, accounting_dir: Path | None = None, now: datetime | str | None = None,
           commit_sha: str | None = None, workflow_run_id: str | None = None, source_branch: str = SOURCE_BRANCH) -> dict:
    """Build + publish ``out`` atomically. Returns ``{"ok": bool, "manifest"|"health": ..., "counts": ...}``.

    Never raises for a data problem: the failure path writes only ``health.json`` (export_failed=True) so the
    last-known-good payload stands, and ``ok`` is False so a caller can exit non-zero."""
    out = Path(out)
    now_iso = timeutil.to_iso(now or timeutil.now_utc())
    try:
        built = build_documents(Path(root), accounting_dir=accounting_dir, now=now_iso, commit_sha=commit_sha,
                                workflow_run_id=workflow_run_id, source_branch=source_branch)
        manifest = publish.publish(
            root=out, sport=SPORT, run_id=built["run_id"], generated_at=built["generated_at"], documents=built["documents"],
            source_repo=SOURCE_REPO, source_branch=source_branch, commit_sha=commit_sha, model_version=built["model_version"],
            status=built["status"], freshness=built["freshness"], warnings=built["warnings"], health=built["health"],
        )
        return {"ok": True, "manifest": manifest, "health": built["health"], "counts": built["counts"], "warnings": built["warnings"]}
    except Exception as exc:  # noqa: BLE001 - the failure path is the contract: health only, payload untouched
        hd = _failure_health(out, exc, now_iso=now_iso, commit_sha=commit_sha, root=Path(root) if root else None)
        publish.write_health_only(out, hd)
        return {"ok": False, "health": hd, "error": f"{type(exc).__name__}: {exc}", "counts": {}}


def add_arguments(ap) -> None:
    """The ``nhl app-export`` / ``scripts/app_export.py`` options (one definition, two entry points)."""
    import os

    ap.add_argument("--data-root", default="data/archive", help="archive root (a checkout of the data-archive branch)")
    ap.add_argument("--out", default=None, help="app root to publish into (default <data-root>/app/latest)")
    ap.add_argument("--accounting-dir", default=None, help="checkout of the accounting-data branch (optional; empty ledger otherwise)")
    ap.add_argument("--now", default=None, help="ISO-8601 UTC instant to stamp the export with (default: wall clock)")
    ap.add_argument("--commit-sha", default=os.environ.get("GITHUB_SHA") or None)
    ap.add_argument("--workflow-run-id", default=os.environ.get("GITHUB_RUN_ID") or None)
    ap.add_argument("--source-branch", default=SOURCE_BRANCH)


def run_from_args(a) -> int:
    root = Path(a.data_root)
    out = Path(a.out) if a.out else root / APP_ROOT_RELATIVE
    acc = Path(a.accounting_dir) if a.accounting_dir else None
    res = export(root, out, accounting_dir=acc, now=a.now, commit_sha=a.commit_sha, workflow_run_id=a.workflow_run_id,
                 source_branch=a.source_branch)
    if res["ok"]:
        print(json.dumps({"ok": True, "out": str(out), "run_id": res["manifest"]["run_id"], "overall_status": res["health"]["overall_status"],
                          "counts": res["counts"], "warnings": res["warnings"]}, indent=1))
        return 0
    print(json.dumps({"ok": False, "out": str(out), "error": res["error"], "overall_status": res["health"]["overall_status"]}, indent=1),
          file=sys.stderr)
    return 1


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="nhl app-export", description="publish the Edge Finder app documents (edge_finder.app.v1)")
    add_arguments(ap)
    return run_from_args(ap.parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
