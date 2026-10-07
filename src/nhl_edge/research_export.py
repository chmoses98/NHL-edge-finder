"""Edge Finder research explorer (contract 1.1.0): the archive + committed history -> ``app/latest/explorer``.

An adapter beside :mod:`nhl_edge.app_export`, run AFTER it. It reads only what this repository already commits
or captures and publishes the navigable research graph the app explores: team and player profiles, rankings over
the full league, per-game series, event research, per-event market history and the capability manifest.

Inputs (all read-only, nothing fetched):
    ``<app_root>``                         the v1 publication just written: manifest (run id), events, markets,
                                           model prices, wagers -- identities are reused, never re-derived
    ``data/history`` on ``main``           MoneyPuck team game logs, official NHL results, official player and
                                           goalie game logs (the one-off history pulls the audit names)
    the archive (``data-archive``)         live team game logs, official team summaries, rosters, lines, injuries,
                                           goalie observations, results, player events, DATA_ONLY_V1 predictions,
                                           evaluation reports, the Kalshi board checkpoints + deltas, the latest
                                           slate packet (point-in-time team ratings, game distributions)

Nothing here fits a model. Season totals, per-game rates, trailing means over the last N stored games and the
rank of a value inside its universe are arithmetic over stored values; every such number says which window and
universe produced it. Opponent adjustment and schedule strength do not exist in this repository and are published
as UNAVAILABLE (audit 2026-10-03, §6).

Statuses follow ``scratchpad/phase2/audit_nhl.md`` §4/§10 (see :data:`CAPABILITY_STATUS`). A capability whose
source is absent from the archive being exported is published UNAVAILABLE with the reason, never claimed.
"""

from __future__ import annotations

import gzip
import json
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from nhl_edge.config import REPO_ROOT
from nhl_edge.timeutil import ET

CONTRACT_DIR = REPO_ROOT / "contract"
if str(CONTRACT_DIR) not in sys.path:
    sys.path.insert(0, str(CONTRACT_DIR))

# The vendored contract package is not installed; CONTRACT_DIR is put on sys.path above, hence the E402 markers.
from edge_finder_contract import build, ids, timeutil  # noqa: E402
from edge_finder_contract import research as R  # noqa: E402

from nhl_edge import research_sift as RS  # noqa: E402

SPORT = "NHL"
METHODOLOGY_VERSION = "nhl-research-export-1.0"
AUDIT_DATE = "2026-10-03"
HISTORY_ROOT = REPO_ROOT / "data" / "history"
EVENT_SOURCE = "nhl_game_id"
TEAM_SOURCE = "nhl_team_id"
PLAYER_SOURCE = "nhl_player_id"
AUTHORITY = "RESEARCH_ONLY"

GAME_LOG_CAP = 82          # per-team and per-player game logs and per-game series keep the last 82 games
FORM_N = 10                # the trailing window computed by this export (labelled L10)
SKATER_MIN_GP = 20         # skater ranking universe: >= 20 regular-season games in the season
GOALIE_MIN_STARTS = 15     # goalie ranking universe: >= 15 regular-season starts in the season
CURRENT_MIN_GP = 10        # current-season player rankings only once >= 50 players reach 10 games
MIN_PLAYER_UNIVERSE = 50
INDEX_BUDGET = 295_000  # bytes; explorer/index.json budget is 300 KB
MARKET_HISTORY_BUDGET = 380_000  # bytes; the contract budget per market_history document is 400 KB

SRC_MP_HISTORY = "MoneyPuck team game log (data/history/moneypuck, one-off pull)"
SRC_MP_LIVE = "MoneyPuck team game log (archive context/team_games)"
SRC_MP_ST = "MoneyPuck team game log by situation (archive context/team_games_st)"
SRC_SUMMARY = "NHL stats team summary (archive context/team_summary)"
SRC_PLAYERS = "official NHL boxscore + play-by-play + shift charts (data/history/players + archive player_events)"
SRC_PACKET = "latest slate packet team_state (features/ratings.py, nhl-features-1.0)"
SRC_SIM = "latest slate packet model.sim (DATA_ONLY_V1, nhl-sim-1.1)"
SRC_PRED = "archive predictions (DATA_ONLY_V1 per contract per run)"
SRC_EXPORT = "computed by nhl research-export from the stored game logs"

# ------------------------------------------------------------------------------------------- audit limitations
# Verbatim (or verbatim fragments) from audit_nhl.md §4 / §6 / §10 / §11.
LIM_TEAM_RATINGS = "no opponent adjustment; EW half-life 20 games, prior 20 games, prev season x0.6"
LIM_TEAM_LOG_HISTORY = ("Team game logs: PARTIAL (history one-off) / VERIFIED (live kind); the historical parquet pulls are "
                        "one-off manual-dispatch workflows, not scheduled")
LIM_PLAYER_LOG = ("Player game logs (official): VERIFIED (live) / PARTIAL (history one-off); `shifts_ok` flag (57 of 1,398 "
                  "games in 2024-25 lack shift charts)")
LIM_RESULTS = "Historical opponents / results: PARTIAL; official scores, period count, last_period_type"
LIM_NO_OPP_ADJ = ("raw metrics and DATA_ONLY_V1 ratings are NOT opponent-adjusted (opponent enters the model only as a multiplicative factor at game "
                  "time); the only opponent-adjusted numbers are the met_nhl.oa_* 5v5 metrics (nhl-oppadj-1.0, RESEARCH)")
LIM_SVA = "MoneyPuck provides score/venue-adjusted xG columns, not opponent-adjusted"
LIM_LINES = "no historical source; backtests use shift-derived deployment (lines, injuries and goalie-status history are only 4-5 days deep)"
LIM_INJURIES = "name-only; not modelled in V1; removes players from projected lineups"
LIM_MATCHUP = "Matchup metrics: RESEARCH (lambda decomposition per game per run; shadow and thesis layers are RESEARCH_ONLY)"
LIM_DISTRIBUTIONS = "Projection distributions: PARTIAL; 20,000 team draws / 10,000 player draws, draws not persisted"
LIM_FORM = ("fixed recent-form windows are not stored by the repository (UNAVAILABLE as stored; RESEARCH as EW weights); "
            "L10 here is a plain trailing mean computed by the research export, not a model input")
LIM_RANKINGS = "rankings/percentiles (none exist) in the repository; these are computed by the research export as arithmetic over stored values"
LIM_SPLITS = "Situational splits: VERIFIED (strength state) / PARTIAL (others); home/away splits of ratings are not stored"
LIM_ADVANCED = "Advanced stats: PARTIAL (history one-off) / VERIFIED (live team rows)"


def _season_label(season: int) -> str:
    return f"{season}-{(season + 1) % 100:02d}"


def _f(v: Any) -> float | None:
    if v is None or v == "":
        return None
    try:
        out = float(v)
    except (TypeError, ValueError):
        return None
    return None if out != out else out  # NaN -> None


def _r(v: float | None, nd: int = 4) -> float | None:
    return None if v is None else round(float(v), nd)


def _div(a: float | None, b: float | None) -> float | None:
    if a is None or b in (None, 0):
        return None
    return a / b


def _ts(v: Any) -> str | None:
    if v in (None, ""):
        return None
    try:
        return timeutil.to_iso(v)
    except Exception:  # noqa: BLE001 - an unparseable stamp is treated as absent, never guessed
        return None


def _et_to_utc(local: Any) -> str | None:
    """``start_time_et`` in the history parquet is a naive Eastern wall-clock time; attach ET, convert to UTC."""
    if not local:
        return None
    try:
        dt = datetime.fromisoformat(str(local)[:19]).replace(tzinfo=ET)
    except ValueError:
        return None
    return timeutil.to_iso(dt)


def _date_from_int(v: Any) -> str:
    s = str(v).replace("-", "")[:8]
    return f"{s[:4]}-{s[4:6]}-{s[6:8]}"


def _norm_name(text: Any) -> str:
    s = unicodedata.normalize("NFKD", str(text or "")).encode("ascii", "ignore").decode().lower()
    return " ".join("".join(c if c.isalnum() else " " for c in s).split())


def _read_gz_rows(path: Path) -> list[dict]:
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def _read_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


# ============================================================================================ inputs
@dataclass
class ResearchInputs:
    """Everything the explorer is built from, loaded once so :func:`build_explorer` is a pure function of it."""

    app_root: Path
    archive_root: Path
    history_root: Path
    manifest: dict
    events: list[dict]
    markets: list[dict]
    model_prices: list[dict]
    wagers: list[dict]
    packet: dict | None = None
    slate: dict | None = None
    hist_season: int | None = None
    current_season: int | None = None
    history_retrieved_at: str | None = None
    players_retrieved_at: str | None = None
    team_games: list[dict] = field(default_factory=list)
    live_team_games_at: str | None = None
    team_summary: list[dict] = field(default_factory=list)
    team_summary_at: str | None = None
    games: dict[str, dict] = field(default_factory=dict)
    skater_games: list[dict] = field(default_factory=list)
    goalie_games: list[dict] = field(default_factory=list)
    live_player_events_at: str | None = None
    rosters: list[dict] = field(default_factory=list)
    rosters_at: str | None = None
    lines: list[dict] = field(default_factory=list)
    injuries: list[dict] = field(default_factory=list)
    injuries_at: str | None = None
    goalie_obs: list[dict] = field(default_factory=list)
    predictions: list[dict] = field(default_factory=list)
    eval_report: dict | None = None
    eval_report_player: dict | None = None
    learning: dict | None = None
    eval_status: dict | None = None
    ticks: dict[str, list[dict]] = field(default_factory=dict)
    ticks_last_at: str | None = None
    n_ticks: int = 0
    warnings: list[str] = field(default_factory=list)


TEAM_LOG_COLUMNS = {  # normalized key -> MoneyPuck column
    "toi": "iceTime", "xgf": "xGoalsFor", "xga": "xGoalsAgainst", "gf": "goalsFor", "ga": "goalsAgainst",
    "cf": "shotAttemptsFor", "ca": "shotAttemptsAgainst", "ff": "unblockedShotAttemptsFor", "fa": "unblockedShotAttemptsAgainst",
    "sf": "shotsOnGoalFor", "sa": "shotsOnGoalAgainst", "hdxgf": "highDangerxGoalsFor", "hdxga": "highDangerxGoalsAgainst",
    "svxgf": "scoreVenueAdjustedxGoalsFor", "svxga": "scoreVenueAdjustedxGoalsAgainst",
}
SKATER_COLUMNS = ["game_id", "season", "game_date", "game_type", "player_id", "team_id", "is_home", "home_team_id", "away_team_id",
                  "name", "position", "goals", "assists", "points", "sog", "pp_goals", "toi_s", "toi_ev_s", "toi_pp_s", "toi_sh_s",
                  "plus_minus", "shifts_ok"]
GOALIE_COLUMNS = ["game_id", "season", "game_date", "game_type", "player_id", "team_id", "is_home", "home_team_id", "away_team_id",
                  "name", "starter", "toi_s", "saves", "shots_against", "goals_against", "decision", "ev_saves", "ev_sa",
                  "pp_saves", "pp_sa", "sh_saves", "sh_sa"]


def _parquet_rows(path: Path, columns: list[str]) -> list[dict]:
    import pyarrow.parquet as pq

    if not path.exists():
        return []
    have = set(pq.read_schema(path).names)
    return pq.read_table(path, columns=[c for c in columns if c in have]).to_pylist()


def _available(folder: Path, prefix: str) -> list[int]:
    out = []
    for p in folder.glob(f"{prefix}_*.parquet") if folder.exists() else []:
        tail = p.stem[len(prefix) + 1:]
        if tail.isdigit():
            out.append(int(tail))
    return sorted(out)


def _team_game_row(r: dict, *, season: int, game_id: str, date: str, game_type: int, team_id: int, opp_id: int, home: bool,
                   situation: str, src: str) -> dict:
    out = {"game_id": game_id, "season": season, "date": date, "game_type": game_type, "team_id": team_id, "opp_team_id": opp_id,
           "home": home, "situation": situation, "src": src}
    for key, col in TEAM_LOG_COLUMNS.items():
        out[key] = _f(r.get(col))
    return out


def load_research_inputs(app_root: Path, archive_root: Path, *, history_root: Path | None = None) -> ResearchInputs:
    """Read the v1 publication, the committed history and the archive. Raises when the v1 publication is absent."""
    from nhl_edge.archive.ledger import Ledger
    from nhl_edge.identity.teams import TeamIdentityError, registry

    app_root, archive_root = Path(app_root), Path(archive_root)
    history_root = Path(history_root) if history_root else HISTORY_ROOT
    manifest = _read_json(app_root / "manifest.json")
    if manifest is None:
        raise FileNotFoundError(f"no v1 manifest.json under {app_root}: run the app export first")

    def items(name: str) -> list[dict]:
        doc = _read_json(app_root / f"{name}.json")
        return list(doc["items"]) if doc else []

    inp = ResearchInputs(app_root=app_root, archive_root=archive_root, history_root=history_root, manifest=manifest,
                         events=items("events"), markets=items("markets"), model_prices=items("model_prices"), wagers=items("wagers"))
    inp.packet = _read_json(archive_root / "slates" / "latest" / "packet.json")
    inp.slate = _read_json(archive_root / "slates" / "latest" / "slate.json")
    reg = registry()
    ledger = Ledger(archive_root) if archive_root.is_dir() else None
    if ledger is None:
        inp.warnings.append(f"archive root {archive_root} not found: archive-backed sections are empty")

    def latest(kind: str) -> tuple[list[dict], str | None]:
        if ledger is None:
            return [], None
        e = ledger.latest(kind)
        if e is None or not (archive_root / e.path).exists():
            return [], None
        return _read_gz_rows(archive_root / e.path), _ts(e.observed_at_utc or e.written_at_utc)

    def every(kind: str) -> list[dict]:
        return list(ledger.iter_rows(kind)) if ledger is not None else []

    # -- seasons ------------------------------------------------------------------------------------------
    mp_seasons = _available(history_root / "moneypuck", "team_games")
    inp.hist_season = mp_seasons[-1] if mp_seasons else None
    ev_seasons = [int(str(e.get("season") or "")[:4]) for e in inp.events if str(e.get("season") or "")[:4].isdigit()]
    inp.current_season = max(ev_seasons) if ev_seasons else ((inp.hist_season + 1) if inp.hist_season else None)
    hist_manifest = _read_json(history_root / "MANIFEST.json") or {}
    if inp.hist_season is not None:
        inp.history_retrieved_at = _ts(((hist_manifest.get("moneypuck") or {}).get("seasons") or {}).get(str(inp.hist_season), {}).get("retrieved_at_utc"))

    # -- team game logs: history (last complete season) + live rows of later seasons ------------------------
    if inp.hist_season is not None:
        cols = ["season", "game_id", "game_date", "game_type", "team_id", "opp_team_id", "home", "situation"] + list(TEAM_LOG_COLUMNS.values())
        for r in _parquet_rows(history_root / "moneypuck" / f"team_games_{inp.hist_season}.parquet", cols):
            if r.get("team_id") is None or r.get("opp_team_id") is None:
                continue
            inp.team_games.append(_team_game_row(r, season=int(r["season"]), game_id=str(r["game_id"]), date=str(r["game_date"])[:10],
                                                 game_type=int(r.get("game_type") or 2), team_id=int(r["team_id"]),
                                                 opp_id=int(r["opp_team_id"]), home=bool(r.get("home")), situation=str(r["situation"]),
                                                 src="history"))
    else:
        inp.warnings.append("no MoneyPuck history parquet under data/history/moneypuck")

    def live_rows(rows: list[dict], src: str) -> None:
        for r in rows:
            try:
                season = int(r.get("season"))
            except (TypeError, ValueError):
                continue
            if inp.hist_season is not None and season <= inp.hist_season:
                continue  # the committed history is the record for completed seasons
            try:
                team, opp = reg.by_abbrev(str(r.get("team") or r.get("team_abbrev"))), reg.by_abbrev(str(r.get("opposingTeam")))
            except TeamIdentityError:
                inp.warnings.append(f"team_games: unresolved abbreviation in {r.get('team')}/{r.get('opposingTeam')}")
                continue
            gid = str(r.get("gameId"))
            inp.team_games.append(_team_game_row(r, season=season, game_id=gid, date=_date_from_int(r.get("gameDate")),
                                                 game_type=int(gid[4:6]) if len(gid) >= 6 and gid[4:6].isdigit() else 2,
                                                 team_id=team.team_id, opp_id=opp.team_id, home=str(r.get("home_or_away")).upper() == "HOME",
                                                 situation=str(r.get("situation") or "all"), src=src))

    rows, inp.live_team_games_at = latest("context/team_games")
    live_rows([r for r in rows if str(r.get("situation") or "all") == "all"], "live")
    rows, _st_at = latest("context/team_games_st")
    live_rows([r for r in rows if str(r.get("situation")) in ("5on5", "5on4", "4on5")], "live_st")
    inp.team_summary, inp.team_summary_at = latest("context/team_summary")

    # -- official results: history games parquet + archive schedule + archive results ----------------------
    if inp.hist_season is not None:
        for r in _parquet_rows(history_root / "nhl" / f"games_{inp.hist_season}.parquet",
                               ["game_id", "season", "game_type", "game_date", "start_time_et", "home_team_id", "away_team_id",
                                "home_score", "away_score", "last_period_type", "final"]):
            inp.games[str(r["game_id"])] = {
                "start_utc": _et_to_utc(r.get("start_time_et")), "date": str(r.get("game_date"))[:10], "season": int(r["season"]),
                "game_type": int(r.get("game_type") or 2), "home_team_id": r.get("home_team_id"), "away_team_id": r.get("away_team_id"),
                "home_score": r.get("home_score"), "away_score": r.get("away_score"), "last_period_type": r.get("last_period_type"),
                "final": bool(r.get("final")), "source": "data/history/nhl"}
    sched: dict[str, dict] = {}
    for r in every("context/schedule"):
        gid = str(r.get("game_id") or "")
        if gid and (gid not in sched or str(r.get("_observed_at_utc") or "") >= str(sched[gid].get("_observed_at_utc") or "")):
            sched[gid] = r
    for gid, r in sched.items():
        g = inp.games.setdefault(gid, {"source": "archive context/schedule"})
        g.update({k: v for k, v in {
            "start_utc": _ts(r.get("start_time_utc")), "date": r.get("game_date_et"), "home_team_id": r.get("home_team_id"),
            "away_team_id": r.get("away_team_id"), "season": int(str(r.get("season") or "0")[:4] or 0) or None,
            "game_type": int(gid[4:6]) if gid[4:6].isdigit() else 2}.items() if v is not None})
        if str(r.get("status") or "").lower() == "final" and r.get("home_score") is not None:
            g.update({"home_score": r.get("home_score"), "away_score": r.get("away_score"),
                      "last_period_type": r.get("last_period_type"), "final": True})
    for r in every("results"):
        gid = str(r.get("game_id") or "")
        if not gid or str(r.get("status") or "final").lower() != "final":
            continue
        g = inp.games.setdefault(gid, {"source": "archive results"})
        g.update({"home_team_id": r.get("home_team_id"), "away_team_id": r.get("away_team_id"), "home_score": r.get("home_final"),
                  "away_score": r.get("away_final"), "last_period_type": r.get("last_period_type"), "final": True,
                  "source": "archive results"})
        g.setdefault("game_type", int(gid[4:6]) if gid[4:6].isdigit() else 2)

    # -- official player and goalie game logs ----------------------------------------------------------------
    pl_seasons = _available(history_root / "players", "players")
    keep = [s for s in pl_seasons if inp.hist_season is None or s >= inp.hist_season - 1]
    skaters: dict[tuple, dict] = {}
    goalies: dict[tuple, dict] = {}
    for s in keep:
        for r in _parquet_rows(history_root / "players" / f"players_{s}.parquet", SKATER_COLUMNS):
            skaters[(str(r["game_id"]), int(r["player_id"]))] = r | {"src": "history"}
        for r in _parquet_rows(history_root / "players" / f"goalies_{s}.parquet", GOALIE_COLUMNS):
            goalies[(str(r["game_id"]), int(r["player_id"]))] = r | {"src": "history"}
    pm = _read_json(history_root / "players" / f"MANIFEST_{inp.hist_season}.json") or {}
    inp.players_retrieved_at = _ts(pm.get("pulled_at_utc"))
    live_at = []
    for kind, store, cols in (("player_events/players", skaters, SKATER_COLUMNS), ("player_events/goalies", goalies, GOALIE_COLUMNS)):
        for r in every(kind):
            store[(str(r["game_id"]), int(r["player_id"]))] = {c: r.get(c) for c in cols} | {"src": "live"}
            live_at.append(str(r.get("_observed_at_utc") or ""))
    inp.live_player_events_at = _ts(max(live_at)) if live_at else None
    inp.skater_games = sorted(skaters.values(), key=lambda r: (str(r["game_date"]), str(r["game_id"]), int(r["player_id"])))
    inp.goalie_games = sorted(goalies.values(), key=lambda r: (str(r["game_date"]), str(r["game_id"]), int(r["player_id"])))

    # -- rosters, lines, injuries, goalie observations ---------------------------------------------------------
    inp.rosters, inp.rosters_at = latest("context/rosters")
    newest_lines: dict[int, str] = {}
    all_lines = every("context/lines")
    for r in all_lines:
        tid = r.get("team_id")
        if tid is not None and str(r.get("_observed_at_utc") or "") > newest_lines.get(int(tid), ""):
            newest_lines[int(tid)] = str(r.get("_observed_at_utc") or "")
    inp.lines = [r for r in all_lines if r.get("team_id") is not None and str(r.get("_observed_at_utc") or "") == newest_lines[int(r["team_id"])]]
    inp.injuries, inp.injuries_at = latest("context/injuries")
    event_games = {str(e["source_ids"].get(EVENT_SOURCE)) for e in inp.events if e.get("source_ids", {}).get(EVENT_SOURCE)}
    inp.goalie_obs = [r for r in every("context/goalie_observations") if str(r.get("game_id")) in event_games]

    # -- model-probability history (DATA_ONLY_V1, priced rows of the published events) -------------------------
    event_tickers = {m["kalshi_ticker"] for m in inp.markets if m.get("event_id")}
    for r in every("predictions"):
        if str(r.get("game_id")) in event_games and r.get("ticker") in event_tickers and r.get("p_data_only") is not None:
            inp.predictions.append({k: r.get(k) for k in ("ticker", "game_id", "predicted_at_utc", "p_data_only", "p_data_only_se",
                                                          "p_market", "gate", "model_version", "_run_id", "family")})

    inp.eval_report = _read_json(archive_root / "eval" / "report.json")
    inp.eval_report_player = _read_json(archive_root / "eval" / "report_player.json")
    inp.learning = _read_json(archive_root / "eval" / "report_learning.json")
    inp.eval_status = _read_json(archive_root / "STATUS_evaluate.json")

    # -- market quote history from checkpoints + deltas (archive.reconstruct) ----------------------------------
    if ledger is not None and event_tickers:
        from nhl_edge.archive.reconstruct import iter_board_ticks

        last: dict[str, tuple] = {}
        last_seen: dict[str, tuple] = {}
        for at, _run, board, raw in iter_board_ticks(ledger):
            inp.n_ticks += 1
            at_iso = timeutil.to_iso(at)
            src = "kalshi/markets checkpoint" if raw is not None else "kalshi/markets_delta"
            for t in event_tickers:
                row = board.get(t)
                if row is None:
                    continue
                q = row.get("_quote_cents") or {}
                key = (q.get("yes_bid"), q.get("yes_ask"), q.get("last_price"))
                pt = {"captured_at": at_iso, "yes_bid": q.get("yes_bid"), "yes_ask": q.get("yes_ask"), "last_price": q.get("last_price"),
                      "volume": _f(row.get("volume_fp") if row.get("volume_fp") is not None else row.get("volume")),
                      "open_interest": _f(row.get("open_interest_fp") if row.get("open_interest_fp") is not None else row.get("open_interest")),
                      "source": src}
                if last.get(t) != key:
                    last[t] = key
                    inp.ticks.setdefault(t, []).append(pt)
                last_seen[t] = (at_iso, pt)
            inp.ticks_last_at = at_iso
        for t, (at_iso, pt) in last_seen.items():
            if inp.ticks[t][-1]["captured_at"] != at_iso:
                inp.ticks[t].append(pt | {"source": pt["source"] + " (last observation, quote unchanged)"})
    return inp


# ============================================================================================ arithmetic
def _team_agg(rows: list[dict]) -> dict:
    out: dict[str, Any] = {"games": len(rows)}
    for k in TEAM_LOG_COLUMNS:
        vals = [r[k] for r in rows if r.get(k) is not None]
        out[k] = sum(vals) if vals else None
    return out


def _share(a: float | None, b: float | None) -> float | None:
    if a is None or b is None or (a + b) == 0:
        return None
    return a / (a + b)


def _per60(x: float | None, toi: float | None) -> float | None:
    return None if x is None or not toi else x * 3600.0 / toi


#: TEAM metrics computed from MoneyPuck game logs (situation 'all' unless a split says otherwise).
TEAM_LOG_METRICS = [
    # slug, name, short, description, stat_type, unit, higher_is_better, value(agg)
    ("xgf_pct", "Expected-goals share", "xGF%", "Share of all expected goals (MoneyPuck xG) in the team's games that were the team's: "
     "sum xGF / (sum xGF + sum xGA).", "PERCENT", "share", True, lambda a: _share(a["xgf"], a["xga"])),
    ("xgf_per60", "Expected goals for per 60", "xGF/60", "MoneyPuck expected goals for per 60 minutes of the situation's ice time.",
     "RATE", "xG per 60", True, lambda a: _per60(a["xgf"], a["toi"])),
    ("xga_per60", "Expected goals against per 60", "xGA/60", "MoneyPuck expected goals against per 60 minutes of the situation's ice time.",
     "RATE", "xG per 60", False, lambda a: _per60(a["xga"], a["toi"])),
    ("corsi_pct", "Shot-attempt share (Corsi)", "CF%", "Share of all shot attempts (on goal, missed, blocked): sum CF / (sum CF + sum CA).",
     "PERCENT", "share", True, lambda a: _share(a["cf"], a["ca"])),
    ("fenwick_pct", "Unblocked-attempt share (Fenwick)", "FF%", "Share of unblocked shot attempts: sum FF / (sum FF + sum FA).",
     "PERCENT", "share", True, lambda a: _share(a["ff"], a["fa"])),
    ("hd_xgf_pct", "High-danger expected-goals share", "HDxGF%", "Share of MoneyPuck high-danger expected goals: sum HDxGF / (HDxGF + HDxGA).",
     "PERCENT", "share", True, lambda a: _share(a["hdxgf"], a["hdxga"])),
    ("sva_xgf_pct", "Score- and venue-adjusted xG share", "saxGF%", "Share of MoneyPuck score- and venue-adjusted expected goals. "
     "The adjustment is MoneyPuck's (score state and rink), NOT an opponent or schedule adjustment.",
     "PERCENT", "share", True, lambda a: _share(a["svxgf"], a["svxga"])),
    ("gf_per_game", "Goals for per game", "GF/GP", "Goals scored per game (MoneyPuck goalsFor, shootout goals excluded).",
     "RATE", "goals per game", True, lambda a: _div(a["gf"], a["games"])),
    ("ga_per_game", "Goals against per game", "GA/GP", "Goals allowed per game (MoneyPuck goalsAgainst, shootout goals excluded).",
     "RATE", "goals per game", False, lambda a: _div(a["ga"], a["games"])),
]
SERIES_METRICS = ("xgf_pct", "corsi_pct")
#: model-probability series priority when the explorer index would exceed its budget (lower first is kept)
MODEL_SERIES_PRIORITY = {"game_winner": 0, "game_spread": 1, "game_total": 2, "team_total": 3}
#: situation / home-away splits published per season: (dimension, value, metric slug)
TEAM_SPLITS = [("situation", "5on5", "xgf_pct"), ("situation", "5on5", "corsi_pct"), ("situation", "5on4", "xgf_per60"),
               ("situation", "4on5", "xga_per60"), ("home_away", "HOME", "xgf_pct"), ("home_away", "AWAY", "xgf_pct")]
#: official NHL team summary fields: slug, name, short, description, unit, higher_is_better, field
SUMMARY_METRICS = [
    ("points_pct", "Points percentage (official)", "PTS%", "NHL official points percentage (points / (2 x games played)).", "share", True, "pointPct"),
    ("pp_pct", "Power-play percentage (official)", "PP%", "NHL official power-play goals per power-play opportunity.", "share", True, "powerPlayPct"),
    ("pk_pct", "Penalty-kill percentage (official)", "PK%", "NHL official share of times shorthanded without allowing a goal.", "share", True, "penaltyKillPct"),
]
#: point-in-time ratings from the packet's team_state: slug, name, short, description, higher_is_better, key, status
RATING_METRICS = [
    ("rating_off_xg60", "Offensive rating (xG/60, shrunk)", "OFF", "DATA_ONLY_V1 offensive rating: exponentially weighted xG for per 60 "
     "(half-life 20 games, prior 20 games, previous season x0.6), shrunk toward the league rate. Point-in-time at the slate run.", True, "off_xg60"),
    ("rating_def_xg60", "Defensive rating (xGA/60, shrunk)", "DEF", "DATA_ONLY_V1 defensive rating: exponentially weighted xG against per 60, "
     "same construction. Lower allows fewer expected goals.", False, "def_xg60"),
    ("rating_finish", "Finishing multiplier", "FIN", "DATA_ONLY_V1 finishing multiplier: (GF + 60 r) / (xGF + 60) / r with r the league "
     "goals-per-xG ratio. Above 1 converts chances better than xG.", True, "finish"),
    ("rating_stop", "Goal-prevention multiplier", "STOP", "DATA_ONLY_V1 goal-prevention multiplier on expected goals against; below 1 "
     "allows fewer goals than xG.", False, "stop"),
]
SKATER_METRICS = [
    # slug, name, short, description, stat_type, unit, higher_is_better, value(agg), ranked
    ("games_played", "Games played", "GP", "Games with a boxscore line in the window.", "COUNT", "games", None, lambda a: a["gp"], False),
    ("goals", "Goals", "G", "Official goals (shootout excluded).", "COUNT", "goals", True, lambda a: a["goals"], True),
    ("assists", "Assists", "A", "Official assists (A1 + A2).", "COUNT", "assists", True, lambda a: a["assists"], True),
    ("points", "Points", "P", "Official points (goals + assists).", "COUNT", "points", True, lambda a: a["points"], True),
    ("shots_on_goal", "Shots on goal", "SOG", "Official shots on goal.", "COUNT", "shots", True, lambda a: a["sog"], True),
    ("toi_per_game", "Time on ice per game", "TOI/GP", "Average ice time per game in minutes (split by strength state from shift charts).",
     "DURATION", "minutes", True, lambda a: _div(a["toi"], 60.0 * a["gp"]) if a["gp"] else None, True),
    ("points_per60", "Points per 60", "P/60", "Points per 60 minutes of all-situation ice time.", "RATE", "points per 60", True,
     lambda a: _per60(a["points"], a["toi"]), True),
]
GOALIE_METRICS = [
    ("goalie_games", "Goalie appearances", "GP", "Games with ice time in the window.", "COUNT", "games", None, lambda a: a["gp"], False),
    ("goalie_starts", "Starts", "GS", "Games the goalie started (boxscore starter flag).", "COUNT", "games", None, lambda a: a["starts"], False),
    ("save_pct", "Save percentage", "SV%", "Saves / shots against, all situations (official boxscore).", "PERCENT", "share", True,
     lambda a: _div(a["saves"], a["sa"]), True),
    ("ev_save_pct", "Even-strength save percentage", "EV SV%", "Even-strength saves / even-strength shots against (official boxscore).",
     "PERCENT", "share", True, lambda a: _div(a["ev_saves"], a["ev_sa"]), True),
    ("gaa", "Goals-against average", "GAA", "Goals against per 60 minutes of goalie ice time.", "RATE", "goals per 60", False,
     lambda a: _per60(a["ga"], a["toi"]), True),
]


def _skater_agg(rows: list[dict]) -> dict:
    toi = sum(int(r.get("toi_s") or 0) for r in rows)
    st = [r for r in rows if r.get("shifts_ok")]
    return {"gp": len(rows), "goals": sum(int(r.get("goals") or 0) for r in rows), "assists": sum(int(r.get("assists") or 0) for r in rows),
            "points": sum(int(r.get("points") or 0) for r in rows), "sog": sum(int(r.get("sog") or 0) for r in rows), "toi": toi,
            "gp_states": len(st), "toi_ev": sum(_f(r.get("toi_ev_s")) or 0 for r in st), "toi_pp": sum(_f(r.get("toi_pp_s")) or 0 for r in st),
            "toi_sh": sum(_f(r.get("toi_sh_s")) or 0 for r in st)}


def _goalie_agg(rows: list[dict]) -> dict:
    played = [r for r in rows if int(r.get("toi_s") or 0) > 0]
    s = lambda k: sum(int(r.get(k) or 0) for r in played)  # noqa: E731
    return {"gp": len(played), "starts": sum(1 for r in played if r.get("starter")), "wins": sum(1 for r in played if r.get("decision") == "W"),
            "saves": s("saves"), "sa": s("shots_against"), "ga": s("goals_against"), "toi": s("toi_s"), "ev_saves": s("ev_saves"),
            "ev_sa": s("ev_sa")}


# ============================================================================================ build
class _Ctx:
    """Shared state of one build: ids, quality objects, the documents produced so far."""

    def __init__(self, inp: ResearchInputs, run_id: str, generated_at: str):
        from nhl_edge.app_export import _team_participant
        from nhl_edge.identity.teams import registry

        self.inp, self.run_id, self.now = inp, run_id, generated_at
        self.reg = registry()
        self.team_participant = _team_participant
        self.metrics: dict[str, dict] = {}
        self.rankings: dict[str, dict] = {}
        self.rank_by_key: dict[tuple, dict] = {}
        self.series: list[dict] = []
        self.docs: list[dict] = []
        self.search: list[dict] = []

    def mid(self, slug: str) -> str:
        return ids.metric_id(SPORT, slug)

    def q(self, status: str, source: str, *, data_as_of: Any = None, coverage: str | None = None, sample_size: int | None = None,
          limitations: list[str] | None = None, production: bool = True, missingness: float | None = None) -> dict:
        return R.quality(status=status, source=source, generated_at=self.now, production=production, data_as_of=data_as_of,
                         source_version=None, methodology_version=METHODOLOGY_VERSION, coverage=coverage, sample_size=sample_size,
                         missingness=missingness, limitations=limitations)


def _team_pid(team_id: int) -> str:
    return ids.participant_id(SPORT, "TEAM", TEAM_SOURCE, int(team_id))


def _player_pid(player_id: int) -> str:
    return ids.participant_id(SPORT, "PLAYER", PLAYER_SOURCE, int(player_id))


def _event_id(game_id: str) -> str:
    return ids.event_id(SPORT, EVENT_SOURCE, str(game_id))


def build_explorer(inp: ResearchInputs, *, run_id: str, generated_at: Any, index_budget: int = None) -> tuple[list[dict], dict]:
    """Every explorer document for ``inp`` (pure: same inputs + same ``generated_at`` -> same documents).

    ``explorer/index.json`` lists every file (it cannot be sharded), so when it would exceed ``index_budget`` bytes the
    DATA_ONLY_V1 probability series are trimmed, lowest-priority family first (team totals, then game totals, spreads),
    and the trim is recorded in the warnings and the capability limitations. Returns ``(documents, meta)``."""
    budget = INDEX_BUDGET if index_budget is None else index_budget
    docs, meta = _build(inp, run_id=run_id, generated_at=generated_at, allow_model_series=None)
    size = _index_bytes(docs, meta, run_id=run_id, generated_at=generated_at)
    if size <= budget:
        return docs, meta
    series = [d for d in docs if d["kind"] == "time_series" and d["entity_type"] == "MARKET"]
    fam = {m["market_id"]: m["market_family"] for m in inp.markets}
    series.sort(key=lambda d: (MODEL_SERIES_PRIORITY.get(fam.get(d["entity_id"]), 9), d["entity_id"]))
    entry = {d["series_id"]: len(json.dumps({R.path_for(d): {"bytes": 1000, "entity_id": d["series_id"], "kind": "time_series",
                                                               "sha256": "0" * 64}}, separators=(",", ":"))) for d in series}
    keep = [d["entity_id"] for d in series]
    excess = size - budget
    while keep and excess > 0:
        mid = keep.pop()
        excess -= entry[next(d["series_id"] for d in series if d["entity_id"] == mid)]
    docs, meta = _build(inp, run_id=run_id, generated_at=generated_at, allow_model_series=set(keep))
    return docs, meta


def _index_bytes(docs: list[dict], meta: dict, *, run_id: str, generated_at: Any) -> int:
    from edge_finder_contract.publish import dumps

    by_path = {R.path_for(d): d for d in docs}
    texts = {k: dumps(v) for k, v in by_path.items()}
    index = R.build_index(sport=SPORT, run_id=run_id, generated_at=generated_at, documents=by_path, texts=texts, quality=meta["quality"],
                          as_of=meta["as_of"], base_manifest_run_id=run_id, windows=meta["windows"], warnings=meta["warnings"])
    return len(dumps(index, compact=True).encode("utf-8"))  # contract 1.1.1 writes explorer/index.json compact


def _build(inp: ResearchInputs, *, run_id: str, generated_at: Any, allow_model_series: set[str] | None) -> tuple[list[dict], dict]:
    """One build pass; ``allow_model_series`` (market ids) limits the DATA_ONLY_V1 probability series."""
    now = timeutil.to_iso(generated_at)
    c = _Ctx(inp, run_id, now)
    reg = c.reg
    warnings = list(inp.warnings)
    events = sorted(inp.events, key=lambda e: (e["start_time_utc"], e["event_id"]))
    published_events = {e["event_id"] for e in events}
    game_of_event = {e["event_id"]: str(e["source_ids"].get(EVENT_SOURCE)) for e in events}
    active = [t for t in reg.active_teams]
    team_ids = [t.team_id for t in active]
    team_id_set = set(team_ids)
    event_team_ids: set[int] = set()
    participants: dict[int, dict] = {}
    for e in events:
        for p in e["participants"]:
            tid = p.get("source_ids", {}).get(TEAM_SOURCE)
            if tid is not None:
                participants[int(tid)] = p
                event_team_ids.add(int(tid))
    for t in active:
        participants.setdefault(t.team_id, c.team_participant(reg, t.team_id, t.abbrev))
    abbrev = {t.team_id: t.abbrev for t in reg.teams.values()}
    tname = {tid: participants[tid]["display_name"] if tid in participants else abbrev.get(tid, str(tid)) for tid in abbrev}

    hist, cur = inp.hist_season, inp.current_season
    seasons = [s for s in (hist, cur) if s is not None]
    seasons = sorted(set(seasons))
    data_as_of: list[str] = []

    # ---------------------------------------------------------------------------------------- team logs
    all_rows = [r for r in inp.team_games if r["situation"] == "all"]
    by_team: dict[int, list[dict]] = defaultdict(list)
    for r in all_rows:
        by_team[r["team_id"]].append(r)
    for tid in by_team:
        by_team[tid].sort(key=lambda r: (r["date"], r["game_id"]))
    split_rows: dict[tuple, list[dict]] = defaultdict(list)  # (season, team, dimension, value) -> rows
    for r in inp.team_games:
        if r["game_type"] != 2:
            continue
        if r["situation"] in ("5on5", "5on4", "4on5"):
            split_rows[(r["season"], r["team_id"], "situation", r["situation"])].append(r)
        elif r["situation"] == "all":
            split_rows[(r["season"], r["team_id"], "home_away", "HOME" if r["home"] else "AWAY")].append(r)
    season_status = {s: ("PARTIAL" if s == hist else "VERIFIED") for s in seasons}
    season_src = {s: (SRC_MP_HISTORY if s == hist else SRC_MP_LIVE) for s in seasons}
    season_as_of = {s: (inp.history_retrieved_at if s == hist else inp.live_team_games_at) or now for s in seasons}
    for s in seasons:
        if any(r["season"] == s for r in all_rows):
            data_as_of.append(season_as_of[s])
    team_seasons = [s for s in seasons if any(r["season"] == s and r["game_type"] == 2 for r in all_rows)]
    log_as_of = max((season_as_of[s] for s in team_seasons), default=now)

    lims_log = [LIM_TEAM_LOG_HISTORY, LIM_NO_OPP_ADJ]
    q_team_hist = c.q("PARTIAL", SRC_MP_HISTORY, data_as_of=inp.history_retrieved_at, limitations=lims_log,
                      coverage=f"{_season_label(hist)} regular season and playoffs" if hist else None, production=False)
    q_team_live = c.q("VERIFIED", SRC_MP_LIVE, data_as_of=inp.live_team_games_at,
                      coverage=f"{_season_label(cur)} to date" if cur else None)
    q_form = c.q("PARTIAL", SRC_EXPORT, data_as_of=log_as_of, limitations=[LIM_FORM, LIM_TEAM_LOG_HISTORY])

    def season_quality(s: int) -> dict:
        return q_team_hist if s == hist else q_team_live

    # --------------------------------------------------------------------------- metric registry (teams)
    def reg_metric(slug: str, *, name: str, short: str, description: str, entity_type: str, category: str, stat_type: str, source: str,
                   quality: dict, hib: Any, unit: str | None, supports: dict, windows: list[str], splits: list[str] | None = None,
                   subcategory: str | None = None, universe: str | None = None, freshness: str = "UNKNOWN", update: str | None = None,
                   start: Any = None, limitations: list[str] | None = None, related: list[str] | None = None, ext: dict | None = None) -> str:
        mid = c.mid(slug)
        c.metrics[mid] = R.metric(sport=SPORT, slug=slug, name=name, short_name=short, description=description, entity_type=entity_type,
                                  category=category, subcategory=subcategory, stat_type=stat_type, source=source, quality=quality,
                                  freshness=freshness, higher_is_better=hib, unit=unit, comparison_universe=universe, supports=supports,
                                  windows=windows, splits=splits or [], source_version=None, methodology_version=METHODOLOGY_VERSION,
                                  historical_start=start, update_frequency=update, known_limitations=limitations or [],
                                  related_metrics=related or [], extensions=ext or {})
        return mid

    def make_ranking(mid: str, *, universe: str, entity_type: str, window: dict, as_of: Any, hib: Any, values: list[dict],
                     quality: dict, season: Any = None, ufilter: str | None = None, split: dict | None = None) -> dict | None:
        if len([v for v in values if v.get("value") is not None]) < 2:
            return None
        rk = R.ranking(sport=SPORT, metric_id=mid, universe_label=universe, entity_type=entity_type, window=window, as_of=as_of,
                       higher_is_better=hib, values=values, run_id=c.run_id, generated_at=now, quality=quality, season=season,
                       universe_filter=ufilter, split=split,
                       links=[R.link(rel="METRIC", target_kind="metric_registry", label=c.metrics[mid]["name"], target_id=mid,
                                     path=R.app_path(R.METRICS_NAME))])
        c.rankings[rk["ranking_id"]] = rk
        c.rank_by_key[(mid, window["label"], R._split_label(split) if split else None, entity_type)] = rk
        return rk

    team_obs: dict[int, list[dict]] = defaultdict(list)
    team_split_obs: dict[int, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    team_rank_refs: dict[int, list[dict]] = defaultdict(list)

    def team_values(fn, rows_for) -> list[dict]:
        out = []
        for tid in team_ids:
            rows = rows_for(tid)
            if not rows:
                continue
            a = _team_agg(rows)
            out.append({"entity_id": _team_pid(tid), "display_name": tname[tid], "short_name": abbrev[tid], "value": _r(fn(a)),
                        "sample_size": a["games"], "path": R.team_path(_team_pid(tid)), "_tid": tid})
        return out

    def publish_team_metric(mid: str, values: list[dict], *, window: dict, universe: str, as_of: str, hib: Any, quality: dict,
                            season: Any, status: str, source: str, unit: str | None, split: dict | None = None,
                            ufilter: str = "every active NHL team with at least one game in the window",
                            display: dict | None = None) -> None:
        rk = make_ranking(mid, universe=universe, entity_type="TEAM", window=window, as_of=as_of, hib=hib, values=values,
                          quality=quality, season=season, ufilter=ufilter, split=split)
        for v in values:
            tid = v["_tid"]
            ctx = R.context_from_ranking(rk, v["entity_id"]) if rk and v.get("value") is not None else None
            o = R.observation(sport=SPORT, metric_id=mid, entity_id=v["entity_id"], entity_type="TEAM", value=v["value"], window=window,
                              as_of=as_of, source=source, quality_status=status, unit=unit, split=split, sample_size=v.get("sample_size"),
                              season=season, context=ctx, display_value=(display or {}).get(tid))
            if split:
                team_split_obs[tid][split["dimension"]].append(o)
            else:
                team_obs[tid].append(o)
            if rk and ctx:
                team_rank_refs[tid].append({"ranking_id": rk["ranking_id"], "metric_id": mid, "window_label": window["label"],
                                            "split": split, "path": R.ranking_path(rk["ranking_id"])})

    season_windows = {s: R.window("SEASON", label=_season_label(s)) for s in seasons}
    w_form = R.window("LAST_N", n=FORM_N)
    split_dims = {"situation": ["5on5", "5on4", "4on5"], "home_away": ["HOME", "AWAY"]}
    published_split_metrics: dict[str, set[str]] = defaultdict(set)
    first_date = min((r["date"] for r in all_rows), default=None)

    for slug, name, short, desc, stype, unit, hib, fn in TEAM_LOG_METRICS:
        mid = c.mid(slug)
        windows_pub = [season_windows[s]["label"] for s in team_seasons] + ([w_form["label"]] if all_rows else [])
        has_split = any(sl == slug for _, _, sl in TEAM_SPLITS)
        reg_metric(slug, name=name, short=short, description=desc + " Regular-season games for SEASON windows; the L10 window is the "
                   "team's last 10 games of any type (computed by this export).", entity_type="TEAM", category="advanced",
                   subcategory="moneypuck", stat_type=stype, source="MoneyPuck team game-by-game (history + live)",
                   quality=c.q("PARTIAL", "MoneyPuck team game-by-game", data_as_of=log_as_of, limitations=lims_log + [LIM_FORM],
                               coverage=", ".join(windows_pub)),
                   hib=hib, unit=unit, supports=R.supports(rank=True, percentile=True, time_series=slug in SERIES_METRICS, windows=True,
                                                           splits=has_split, home_away=slug == "xgf_pct"),
                   windows=windows_pub, splits=sorted({d for d, _, sl in TEAM_SPLITS if sl == slug}) if has_split else [],
                   universe="NHL teams (32 active clubs)", freshness="UNKNOWN", update="history: one-off pull; live: every context refresh",
                   start=first_date, limitations=lims_log + ([LIM_SVA] if slug == "sva_xgf_pct" else []))
        for s in team_seasons:
            vals = team_values(fn, lambda tid, s=s: [r for r in by_team.get(tid, []) if r["season"] == s and r["game_type"] == 2])
            publish_team_metric(mid, vals, window=season_windows[s], universe=f"NHL teams, {_season_label(s)} regular season",
                                as_of=season_as_of[s], hib=hib, quality=season_quality(s), season=_season_label(s), status=season_status[s],
                                source=season_src[s], unit=unit)
        if all_rows:
            vals = team_values(fn, lambda tid: by_team.get(tid, [])[-FORM_N:])
            publish_team_metric(mid, vals, window=w_form, universe=f"NHL teams, last {FORM_N} games", as_of=log_as_of, hib=hib, quality=q_form,
                                season=_season_label(cur) if cur else None, status="PARTIAL", source=SRC_EXPORT, unit=unit,
                                ufilter=f"every active NHL team; each team's own last {FORM_N} stored games (regular season + playoffs, across seasons)")
    for dim, val, slug in TEAM_SPLITS:
        fn = next(m[7] for m in TEAM_LOG_METRICS if m[0] == slug)
        unit = next(m[5] for m in TEAM_LOG_METRICS if m[0] == slug)
        hib = next(m[6] for m in TEAM_LOG_METRICS if m[0] == slug)
        sp = R.split(dim, val)
        for s in team_seasons:
            vals = team_values(fn, lambda tid, s=s, dim=dim, val=val: split_rows.get((s, tid, dim, val), []))
            if not vals:
                continue
            src = season_src[s] if dim == "home_away" or s == hist else SRC_MP_ST
            publish_team_metric(c.mid(slug), vals, window=season_windows[s], universe=f"NHL teams, {_season_label(s)} regular season, {dim}={val}",
                                as_of=season_as_of[s], hib=hib, quality=season_quality(s), season=_season_label(s),
                                status="PARTIAL" if dim == "home_away" else season_status[s], source=src, unit=unit, split=sp)
            published_split_metrics[dim].add(val)

    # official team summaries (VERIFIED snapshot)
    summ = defaultdict(dict)  # season -> team_id -> row
    for r in inp.team_summary:
        try:
            summ[int(str(r.get("seasonId"))[:4])][int(r.get("teamId"))] = r
        except (TypeError, ValueError):
            continue
    q_summary = c.q("VERIFIED", SRC_SUMMARY, data_as_of=inp.team_summary_at,
                    coverage=", ".join(_season_label(s) for s in sorted(summ)) or None)
    for slug, name, short, desc, unit, hib, fld in SUMMARY_METRICS:
        if not summ:
            break
        mid = reg_metric(slug, name=name, short=short, description=desc, entity_type="TEAM", category="official", subcategory="nhl_stats",
                         stat_type="PERCENT", source="NHL stats API team summary", quality=q_summary, hib=hib, unit=unit,
                         supports=R.supports(rank=True, percentile=True, windows=True), windows=[_season_label(s) for s in sorted(summ)],
                         universe="NHL teams (32 active clubs)", update="every context refresh (snapshot, current + previous season)")
        for s in sorted(summ):
            vals, display = [], {}
            for tid in team_ids:
                row = summ[s].get(tid)
                if row is None or _f(row.get(fld)) is None:
                    continue
                vals.append({"entity_id": _team_pid(tid), "display_name": tname[tid], "short_name": abbrev[tid], "value": _r(_f(row.get(fld))),
                             "sample_size": int(row.get("gamesPlayed") or 0), "path": R.team_path(_team_pid(tid)), "_tid": tid})
                if slug == "points_pct":
                    display[tid] = f"{row.get('wins')}-{row.get('losses')}-{row.get('otLosses')}"
            publish_team_metric(mid, vals, window=R.window("SEASON", label=_season_label(s)), universe=f"NHL teams, {_season_label(s)} (official)",
                                as_of=inp.team_summary_at or now, hib=hib, quality=q_summary, season=_season_label(s), status="VERIFIED",
                                source=SRC_SUMMARY, unit=unit, ufilter="every team in the official NHL team summary", display=display)
    if inp.team_summary_at:
        data_as_of.append(inp.team_summary_at)

    # point-in-time ratings + model expected goals (latest packet)
    packet = inp.packet or {}
    slate_at = _ts((inp.slate or {}).get("generated_at_utc")) or _ts((packet.get("slate") or {}).get("generated_at_utc"))
    pk_games = {str((g.get("identity") or {}).get("game_id")): g for g in packet.get("games", []) if isinstance(g, dict)}
    team_state: dict[int, dict] = {}
    lambdas: dict[int, tuple[float, int]] = {}
    for gid, g in sorted(pk_games.items()):
        ident = g.get("identity") or {}
        ts_ = g.get("team_state") or {}
        sim = (g.get("model") or {}).get("sim") or {}
        for side in ("home", "away"):
            tid = ident.get(f"{side}_team_id")
            if tid is None:
                continue
            if isinstance(ts_.get(side), dict):
                team_state[int(tid)] = ts_[side] | {"_game_id": gid}
            if _f(sim.get(f"{side}_lambda")) is not None:
                lambdas[int(tid)] = (float(sim[f"{side}_lambda"]), int(sim.get("n_sims") or 0))
    run_label = f"run {slate_at[:16]}Z" if slate_at else "run"
    w_run = R.window("RUN", label=run_label, start=slate_at, end=slate_at)
    rating_as_of = slate_at or now
    if team_state:
        data_as_of.append(rating_as_of)
        q_rating = c.q("PARTIAL", SRC_PACKET, data_as_of=rating_as_of, limitations=[LIM_TEAM_RATINGS],
                       coverage=f"{len(team_state)} teams on the {((inp.slate or {}).get('date_et')) or 'latest'} slate")
        for slug, name, short, desc, hib, key in RATING_METRICS:
            mid = reg_metric(slug, name=name, short=short, description=desc, entity_type="TEAM", category="model_inputs",
                             subcategory="ratings", stat_type="RATING", source="features/ratings.py via the slate packet", quality=q_rating,
                             hib=hib, unit="xG per 60" if "xg60" in slug else "multiplier",
                             supports=R.supports(rank=True, percentile=True), windows=[run_label],
                             universe="NHL teams on the latest slate", update="hourly while a game is within 26 h",
                             limitations=[LIM_TEAM_RATINGS])
            vals = [{"entity_id": _team_pid(tid), "display_name": tname.get(tid, str(tid)), "short_name": abbrev.get(tid),
                     "value": _r(_f(st.get(key))), "sample_size": int(round(_f(st.get("games_used")) or 0)),
                     "path": R.team_path(_team_pid(tid)), "_tid": tid} for tid, st in sorted(team_state.items()) if tid in abbrev]
            publish_team_metric(mid, vals, window=w_run, universe=f"NHL teams on the slate, {run_label}", as_of=rating_as_of, hib=hib,
                                quality=q_rating, season=_season_label(cur) if cur else None, status="PARTIAL", source=SRC_PACKET,
                                unit=c.metrics[mid]["unit"], ufilter="teams with a game in the latest slate run")
    if lambdas:
        q_lam = c.q("RESEARCH", SRC_SIM, data_as_of=rating_as_of, limitations=[LIM_MATCHUP, LIM_TEAM_RATINGS], production=True)
        mid = reg_metric("model_expected_goals", name="Model expected goals (lambda)", short="xG model",
                         description="DATA_ONLY_V1 Poisson rate for the team in its next game: league g/60 x (own offence / league) x "
                         "(opponent defence / league) x finishing x opponent goalie factor x home 1.045 (lambda decomposition, "
                         "features/ratings.py expected_goals). A matchup quantity: it depends on the opponent.",
                         entity_type="TEAM", category="matchup", subcategory="model", stat_type="RATE", source="slate packet model.sim",
                         quality=q_lam, hib=True, unit="goals per game", supports=R.supports(rank=True, percentile=True),
                         windows=[run_label], universe="NHL teams on the latest slate", update="hourly while a game is within 26 h",
                         limitations=[LIM_MATCHUP])
        vals = [{"entity_id": _team_pid(tid), "display_name": tname.get(tid, str(tid)), "short_name": abbrev.get(tid), "value": _r(lam),
                 "sample_size": n, "path": R.team_path(_team_pid(tid)), "_tid": tid} for tid, (lam, n) in sorted(lambdas.items()) if tid in abbrev]
        publish_team_metric(mid, vals, window=w_run, universe=f"NHL teams on the slate, {run_label} (matchup-dependent)", as_of=rating_as_of,
                            hib=True, quality=q_lam, season=_season_label(cur) if cur else None, status="RESEARCH", source=SRC_SIM,
                            unit="goals per game", ufilter="teams with a game in the latest slate run; each value depends on that game's opponent")

    # ------------------------------------------------------------------------------------ team series
    team_series_refs: dict[int, list[dict]] = defaultdict(list)
    for tid in sorted(event_team_ids):
        rows = by_team.get(tid, [])[-GAME_LOG_CAP:]
        if not rows:
            continue
        pid = _team_pid(tid)
        for slug in SERIES_METRICS:
            fn = next(m[7] for m in TEAM_LOG_METRICS if m[0] == slug)
            unit = next(m[5] for m in TEAM_LOG_METRICS if m[0] == slug)
            pts = []
            for r in rows:
                g = inp.games.get(r["game_id"], {})
                eid = _event_id(r["game_id"])
                pts.append(R.point(x=r["game_id"], t=g.get("start_utc") or f"{r['date']}T00:00:00Z", value=_r(fn(_team_agg([r]))),
                                   quality_status="PARTIAL" if r["src"] == "history" else "VERIFIED", event_id=eid,
                                   opponent_id=_team_pid(r["opp_team_id"]), sample_size=int(r["toi"] or 0) or None,
                                   source=SRC_MP_HISTORY if r["src"] == "history" else SRC_MP_LIVE,
                                   path=R.event_path(eid) if eid in published_events else None))
            ser = R.time_series(sport=SPORT, metric_id=c.mid(slug), entity_id=pid, entity_type="TEAM", x_axis="GAME",
                                points=R.rolling(pts, FORM_N), as_of=log_as_of, run_id=c.run_id, generated_at=now, unit=unit,
                                quality=c.q("PARTIAL", "MoneyPuck team game-by-game", data_as_of=log_as_of,
                                            limitations=lims_log + [f"last {GAME_LOG_CAP} games only; rolling_value = trailing {FORM_N}-game mean "
                                                                    "computed by the research export"],
                                            sample_size=len(pts)),
                                rolling_window=FORM_N,
                                links=[R.link(rel="TEAM", target_kind="entity_profile", label=tname[tid], target_id=pid, path=R.team_path(pid)),
                                       R.link(rel="METRIC", target_kind="metric_registry", label=c.metrics[c.mid(slug)]["name"],
                                              target_id=c.mid(slug), path=R.app_path(R.METRICS_NAME))])
            c.series.append(ser)
            team_series_refs[tid].append({"series_id": ser["series_id"], "metric_id": c.mid(slug), "x_axis": "GAME", "split": None,
                                          "path": R.series_path(ser["series_id"])})

    # ------------------------------------------------------------------------------------ players
    roster_by_team: dict[int, list[dict]] = defaultdict(list)
    roster_name: dict[int, str] = {}
    for r in inp.rosters:
        if r.get("player_id") is None or r.get("team_id") is None:
            continue
        roster_name[int(r["player_id"])] = f"{r.get('first_name') or ''} {r.get('last_name') or ''}".strip()
        roster_by_team[int(r["team_id"])].append(r)
    published_players = {int(r["player_id"]) for tid in event_team_ids for r in roster_by_team.get(tid, [])}
    sk_by_player: dict[int, list[dict]] = defaultdict(list)
    gk_by_player: dict[int, list[dict]] = defaultdict(list)
    for r in inp.skater_games:
        sk_by_player[int(r["player_id"])].append(r)
    for r in inp.goalie_games:
        gk_by_player[int(r["player_id"])].append(r)
    hist_name: dict[int, str] = {}
    for r in inp.skater_games + inp.goalie_games:
        hist_name[int(r["player_id"])] = str(r.get("name") or r["player_id"])

    def pname(pid: int) -> str:
        return roster_name.get(pid) or hist_name.get(pid) or str(pid)

    player_status = {s: ("PARTIAL" if s == hist else "VERIFIED") for s in seasons}
    player_as_of = {s: (inp.players_retrieved_at if s == hist else inp.live_player_events_at) or now for s in seasons}
    p_lims = [LIM_PLAYER_LOG]
    q_player_hist = c.q("PARTIAL", SRC_PLAYERS, data_as_of=inp.players_retrieved_at, limitations=p_lims, production=False,
                        coverage=f"{_season_label(hist)} regular season" if hist else None)
    q_player_live = c.q("VERIFIED", SRC_PLAYERS, data_as_of=inp.live_player_events_at, coverage=f"{_season_label(cur)} to date" if cur else None)
    q_player_form = c.q("PARTIAL", SRC_EXPORT, data_as_of=max(v for v in player_as_of.values()) if player_as_of else now,
                        limitations=[LIM_FORM, LIM_PLAYER_LOG])
    player_obs: dict[int, list[dict]] = defaultdict(list)
    player_split_obs: dict[int, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    player_rank_refs: dict[int, list[dict]] = defaultdict(list)
    player_first = min((str(r["game_date"]) for r in inp.skater_games), default=None)
    if inp.skater_games:
        data_as_of.extend(v for v in player_as_of.values() if v)

    def player_block(kind: str, metrics: list, by_player: dict[int, list[dict]], agg_fn, min_key: str, min_n: int, cur_min: int) -> None:
        etype_label = "skaters" if kind == "skater" else "goalies"
        for slug, name, short, desc, stype, unit, hib, _fn, ranked in metrics:
            windows_pub = [_season_label(s) for s in seasons] + [f"L{FORM_N}"]
            reg_metric(slug, name=name, short=short, description=desc + f" SEASON windows count regular-season games; L{FORM_N} is the player's "
                       f"last {FORM_N} games of any type (computed by this export).", entity_type="PLAYER", category=kind, subcategory="official",
                       stat_type=stype, source="official NHL player game logs", quality=c.q("PARTIAL", SRC_PLAYERS,
                       data_as_of=max(player_as_of.values()) if player_as_of else None, limitations=p_lims + [LIM_FORM]),
                       hib=hib, unit=unit, supports=R.supports(rank=ranked, percentile=ranked, windows=True,
                                                               splits=slug == "toi_per_game", game_state=slug == "toi_per_game"),
                       windows=windows_pub, splits=["strength_state"] if slug == "toi_per_game" else [],
                       universe=f"NHL {etype_label} (minimum games in the ranking's filter)" if ranked else None,
                       update="history: one-off pull; live: settle job after every final", start=player_first,
                       limitations=p_lims)
        for s in seasons:
            rows_s = {pid: [r for r in rows if int(r.get("season") or 0) == s and int(r.get("game_type") or 2) == 2] for pid, rows in by_player.items()}
            aggs = {pid: agg_fn(rows) for pid, rows in rows_s.items() if rows}
            min_req = min_n if s == hist else cur_min
            universe_ids = sorted(pid for pid, a in aggs.items() if a[min_key] >= min_req)
            rankable = len(universe_ids) >= MIN_PLAYER_UNIVERSE
            win = season_windows[s]
            q_s = q_player_hist if s == hist else q_player_live
            for slug, _name, _short, _desc, _stype, unit, hib, fn, ranked in metrics:
                mid = c.mid(slug)
                rk = None
                if ranked and rankable:
                    vals = [{"entity_id": _player_pid(pid), "display_name": pname(pid), "value": _r(fn(aggs[pid])),
                             "sample_size": aggs[pid][min_key], "path": R.player_path(_player_pid(pid)) if pid in published_players else None}
                            for pid in universe_ids]
                    rk = make_ranking(mid, universe=f"NHL {etype_label}, {_season_label(s)} regular season, >= {min_req} "
                                      f"{'games' if min_key == 'gp' else 'starts'}", entity_type="PLAYER", window=win,
                                      as_of=player_as_of[s], hib=hib, values=vals, quality=q_s, season=_season_label(s),
                                      ufilter=f"{etype_label} with >= {min_req} regular-season {'games' if min_key == 'gp' else 'starts'} in "
                                              f"{_season_label(s)}")
                for pid in published_players:
                    a = aggs.get(pid)
                    if a is None:
                        continue
                    ctx = R.context_from_ranking(rk, _player_pid(pid)) if rk else None
                    player_obs[pid].append(R.observation(
                        sport=SPORT, metric_id=mid, entity_id=_player_pid(pid), entity_type="PLAYER", value=_r(fn(a)), window=win,
                        as_of=player_as_of[s], source=SRC_PLAYERS, quality_status=player_status[s], unit=unit,
                        sample_size=a[min_key] if min_key in a else a["gp"], season=_season_label(s), context=ctx))
                    if ctx:
                        player_rank_refs[pid].append({"ranking_id": rk["ranking_id"], "metric_id": mid, "window_label": win["label"],
                                                      "split": None, "path": R.ranking_path(rk["ranking_id"])})
            if kind == "skater":
                for pid in published_players:
                    a = aggs.get(pid)
                    if a is None or not a["gp_states"]:
                        continue
                    for state, key in (("EV", "toi_ev"), ("PP", "toi_pp"), ("SH", "toi_sh")):
                        player_split_obs[pid]["strength_state"].append(R.observation(
                            sport=SPORT, metric_id=c.mid("toi_per_game"), entity_id=_player_pid(pid), entity_type="PLAYER",
                            value=_r(a[key] / 60.0 / a["gp_states"]), window=win, as_of=player_as_of[s], source=SRC_PLAYERS,
                            quality_status=player_status[s], unit="minutes", split=R.split("strength_state", state),
                            sample_size=a["gp_states"], season=_season_label(s)))
        form_metrics = [m for m in metrics if m[0] in ("points", "shots_on_goal", "toi_per_game", "save_pct", "gaa")]
        for pid in published_players:
            rows = by_player.get(pid, [])[-FORM_N:]
            if not rows:
                continue
            a = agg_fn(rows)
            for slug, _name, _short, _desc, _stype, unit, _hib, fn, _ranked in form_metrics:
                player_obs[pid].append(R.observation(
                    sport=SPORT, metric_id=c.mid(slug), entity_id=_player_pid(pid), entity_type="PLAYER", value=_r(fn(a)), window=w_form,
                    as_of=q_player_form["data_as_of"] or now, source=SRC_EXPORT, quality_status="PARTIAL", unit=unit, sample_size=len(rows),
                    season=_season_label(cur) if cur else None))

    if inp.skater_games:
        player_block("skater", SKATER_METRICS, sk_by_player, _skater_agg, "gp", SKATER_MIN_GP, CURRENT_MIN_GP)
    if inp.goalie_games:
        player_block("goalie", GOALIE_METRICS, gk_by_player, _goalie_agg, "starts", GOALIE_MIN_STARTS, max(3, CURRENT_MIN_GP // 2))

    # ------------------------------------------------------------------------------------ availability / lines / goalies
    injuries_by_team: dict[int, list[dict]] = defaultdict(list)
    for r in inp.injuries:
        if r.get("team_id") is not None:
            injuries_by_team[int(r["team_id"])].append(r)
    for tid in injuries_by_team:
        injuries_by_team[tid].sort(key=lambda r: _norm_name(r.get("player_name")))
    injury_by_player: dict[int, dict] = {}
    for tid, rows in roster_by_team.items():
        names = {_norm_name(f"{r.get('first_name')} {r.get('last_name')}"): int(r["player_id"]) for r in rows}
        for inj in injuries_by_team.get(tid, []):
            pid = names.get(_norm_name(inj.get("player_name")))
            if pid is not None:
                injury_by_player[pid] = inj
    if inp.injuries_at:
        data_as_of.append(inp.injuries_at)

    def avail_from_injury(inj: dict, event_id: str | None) -> dict:
        detail = f"{inj.get('player_name')} ({inj.get('position')}): {inj.get('status')}"
        if inj.get("detail"):
            detail += f", {inj['detail']}"
        if inj.get("return_date"):
            detail += f"; return {inj['return_date']}"
        return {"status": str(inj.get("status") or "UNKNOWN").upper().replace(" ", "_"), "detail": detail,
                "as_of": inp.injuries_at, "source": "ESPN injuries (archive context/injuries; name-matched)", "event_id": event_id}

    lines_by_team: dict[int, list[dict]] = defaultdict(list)
    for r in inp.lines:
        lines_by_team[int(r["team_id"])].append(r)
    lines_at = max((str(r.get("_observed_at_utc") or "") for r in inp.lines), default="") or None
    if lines_at:
        data_as_of.append(_ts(lines_at))
    obs_by_game_team: dict[tuple, list[dict]] = defaultdict(list)
    for r in inp.goalie_obs:
        if r.get("team_id") is not None:
            obs_by_game_team[(str(r["game_id"]), int(r["team_id"]))].append(r)
    for k in obs_by_game_team:
        obs_by_game_team[k].sort(key=lambda r: (str(r.get("observed_at_utc") or r.get("_observed_at_utc") or ""), str(r.get("source"))))

    # ------------------------------------------------------------------------------------ v1 markets / prices per event
    markets_by_event: dict[str, list[dict]] = defaultdict(list)
    for m in inp.markets:
        if m.get("event_id") in published_events:
            markets_by_event[m["event_id"]].append(m)
    for k in markets_by_event:
        markets_by_event[k].sort(key=lambda m: (m["market_family"], m["kalshi_ticker"]))
    prices_by_market = {mp["market_id"]: mp for mp in sorted(inp.model_prices, key=lambda r: (r["market_id"], r["generated_at"]))}
    wagers_by_event: dict[str, list[str]] = defaultdict(list)
    for w in inp.wagers:
        if w.get("event_id") in published_events:
            wagers_by_event[w["event_id"]].append(w["wager_id"])

    def projection(mp: dict) -> dict:
        return R.projection_ref(mp, research_only=True, authority=AUTHORITY, quality_status="VERIFIED", metric_id=c.mid("model_prob_v1"))

    # ------------------------------------------------------------------------------------ model-probability series (RUN)
    preds_by_ticker: dict[str, list[dict]] = defaultdict(list)
    for r in inp.predictions:
        preds_by_ticker[r["ticker"]].append(r)
    model_series_by_event: dict[str, list[dict]] = defaultdict(list)
    if preds_by_ticker:
        q_pred = c.q("VERIFIED", SRC_PRED, data_as_of=max(_ts(r["predicted_at_utc"]) or "" for r in inp.predictions) or None,
                     coverage=f"{len(preds_by_ticker)} tickers, {len(inp.predictions)} priced rows",
                     limitations=["model probabilities are research outputs (authority RESEARCH_ONLY); 81% of V1 rows are UNSUPPORTED "
                                  "(no p_data_only) and are not plotted"])
        data_as_of.append(q_pred["data_as_of"])
        reg_metric("model_prob_v1", name="Model probability (DATA_ONLY_V1)", short="P(model)",
                   description="DATA_ONLY_V1 fair probability of YES for one Kalshi contract, as frozen in each slate run (archive kind "
                   "`predictions`, p_data_only). One point per run; x is '<archive run id>@<prediction time>'.",
                   entity_type="MARKET", category="model", subcategory="DATA_ONLY_V1", stat_type="PROBABILITY", source=SRC_PRED,
                   quality=q_pred, hib=None, unit="probability", supports=R.supports(time_series=True), windows=["RUN"],
                   update="every slate run (hourly while a game is within 26 h)", limitations=q_pred["limitations"],
                   start=min(r["predicted_at_utc"][:10] for r in inp.predictions))
        market_of_ticker = {m["kalshi_ticker"]: m for m in inp.markets}
        dropped = 0
        for t, rows in sorted(preds_by_ticker.items()):
            m = market_of_ticker.get(t)
            if not m or m.get("event_id") not in published_events:
                continue
            if allow_model_series is not None and m["market_id"] not in allow_model_series:
                dropped += 1
                continue
            seen = set()
            pts = []
            for r in sorted(rows, key=lambda r: (r["predicted_at_utc"], str(r.get("_run_id")))):
                at = _ts(r["predicted_at_utc"])
                if at is None or at in seen:
                    continue
                seen.add(at)
                pts.append(R.point(x=f"{r.get('_run_id')}@{at}", t=at, value=_r(_f(r["p_data_only"]), 6), quality_status="VERIFIED",
                                   event_id=m["event_id"], sample_size=None, source=f"predictions ({r.get('model_version') or 'DATA_ONLY_V1'}, "
                                   f"gate {r.get('gate')})"))
            ser = R.time_series(sport=SPORT, metric_id=c.mid("model_prob_v1"), entity_id=m["market_id"], entity_type="MARKET", x_axis="RUN",
                                points=pts, as_of=pts[-1]["t"], run_id=c.run_id, generated_at=now, unit="probability", quality=q_pred,
                                links=[R.link(rel="EVENT_RESEARCH", target_kind="event_research", label="event", target_id=m["event_id"],
                                              path=R.event_path(m["event_id"])),
                                       R.link(rel="MARKET_HISTORY", target_kind="market_history", label="quote history",
                                              target_id=m["event_id"], path=R.market_history_path(m["event_id"]))])
            c.series.append(ser)
            model_series_by_event[m["event_id"]].append({"ser": ser, "ticker": t})
        if dropped:
            warnings.append(f"{dropped} DATA_ONLY_V1 probability series not published to keep explorer/index.json within "
                            f"{INDEX_BUDGET // 1000} KB (team totals first, then game totals, spreads)")
    n_model_dropped = dropped if preds_by_ticker else 0

    # ------------------------------------------------------------------------------------ calibration metrics (registry)
    fam_cal: dict[str, dict] = {}
    if inp.eval_report:
        rep = inp.eval_report
        ev_at = _ts(rep.get("evaluated_at_utc"))
        data_as_of.append(ev_at)
        overall = rep.get("overall") or {}
        for fam, d in sorted((rep.get("families") or {}).items()):
            views = d.get("views") or {}
            auth = d.get("authority") or {}
            v1 = views.get("DATA_ONLY_V1") or {}
            mk = views.get("MARKET_BASELINE") or {}
            fam_cal[fam] = {k: v for k, v in {
                "n_settled_pregame": d.get("n_pregame"), "v1_n": v1.get("n"), "v1_brier": _r(_f(v1.get("brier")), 6),
                "v1_log_loss": _r(_f(v1.get("log_loss")), 6), "v1_ece": _r(_f(v1.get("ece")), 6), "market_n": mk.get("n"),
                "market_brier": _r(_f(mk.get("brier")), 6), "market_brier_same_rows": _r(_f(auth.get("brier_market")), 6),
                "brier_skill_vs_market": _r(_f(auth.get("brier_skill_vs_market")), 6), "clv_mean": _r(_f(auth.get("clv_mean")), 6),
                "current_authority": auth.get("current_authority"), "eligible_for": auth.get("eligible_for")}.items() if v is not None}
        q_cal = c.q("VERIFIED", "archive eval/report.json (evaluation/metrics.py over settled pregame rows)", data_as_of=ev_at,
                    sample_size=rep.get("n_rows"), coverage=f"{rep.get('n_rows')} settled evaluation rows",
                    limitations=["prospective sample is days deep (audit: VERIFIED (prospective, 4 days)); small samples prove nothing"])
        reg_metric("calibration_v1", name="Calibration and accuracy (DATA_ONLY_V1 vs Kalshi)", short="Brier",
                   description="Prospective scoring of DATA_ONLY_V1 against settled outcomes, per market family and overall: Brier, log "
                   "loss, ECE and 10-bin reliability for the model, the Kalshi mid (MARKET_BASELINE) and the market-anchored blend. "
                   "Values are the repository's own evaluate job output, copied, not recomputed (extensions.by_family / overall).",
                   entity_type="MARKET", category="evaluation", stat_type="SCORE", source="eval/report.json", quality=q_cal, hib=False,
                   unit="Brier score", supports=R.supports(), windows=[], update="after every settle",
                   limitations=q_cal["limitations"],
                   ext={"evaluated_at_utc": ev_at, "n_rows": rep.get("n_rows"), "overall": {
                       k: {kk: (_r(_f(vv), 6) if isinstance(vv, float) else vv) for kk, vv in (v or {}).items()} for k, v in sorted(overall.items())},
                       "by_family": fam_cal, "note": rep.get("note")})
        reg_metric("clv_v1", name="Closing-line value (DATA_ONLY_V1 side)", short="CLV",
                   description="Mean signed closing-line value of the DATA_ONLY_V1 side per family: the move of the Kalshi probability "
                   "from prediction to the last tick strictly before the start (evaluations.clv_signed), averaged by the evaluate job.",
                   entity_type="MARKET", category="evaluation", stat_type="PROBABILITY", source="eval/report.json", quality=q_cal, hib=True,
                   unit="probability points", supports=R.supports(), windows=[], update="after every settle", limitations=q_cal["limitations"],
                   ext={"by_family": {f: v["clv_mean"] for f, v in fam_cal.items() if "clv_mean" in v}})
    if inp.eval_report_player:
        rp = inp.eval_report_player
        q_pc = c.q("RESEARCH", "archive eval/report_player.json", data_as_of=_ts(rp.get("evaluated_at_utc")), sample_size=rp.get("n_rows"),
                   limitations=["PLAYER_SIM_V1 is a SHADOW research arm (audit: player profiles / expected TOI RESEARCH)"])
        reg_metric("calibration_player_sim", name="Calibration (PLAYER_SIM_V1 shadow vs Kalshi)", short="Brier (player)",
                   description="Prospective scoring of the PLAYER_SIM_V1 shadow arm on settled player markets, per family, copied "
                   "from the evaluate job (extensions).", entity_type="MARKET", category="evaluation", stat_type="SCORE",
                   source="eval/report_player.json", quality=q_pc, hib=False, unit="Brier score", supports=R.supports(), windows=[],
                   update="after every settle", limitations=q_pc["limitations"],
                   ext={"evaluated_at_utc": _ts(rp.get("evaluated_at_utc")), "n_rows": rp.get("n_rows"),
                        "overall": {k: {kk: vv for kk, vv in (v or {}).items() if kk != "calibration"} for k, v in sorted((rp.get("overall") or {}).items())},
                        "by_family": {f: {k: v for k, v in (d.get("views") or d).items() if not isinstance(v, list)} if isinstance(d, dict) else d
                                      for f, d in sorted((rp.get("families") or {}).items())}})

    # ------------------------------------------------------------------------------------ market history docs
    q_mh = c.q("VERIFIED", "Kalshi board captures (archive kalshi/markets checkpoints + kalshi/markets_delta, archive/reconstruct.py)",
               data_as_of=inp.ticks_last_at, sample_size=inp.n_ticks, coverage=f"{inp.n_ticks} captured ticks",
               limitations=["one point per quote change (bid/ask/last) plus the last observation; volume and open interest are "
                            "read at those points", "live capture only (audit: VERIFIED, 4.5 days at audit time); historical candles "
                            "for 2025-26 are not included"])
    if inp.ticks_last_at:
        data_as_of.append(inp.ticks_last_at)
    mh_thinned: dict[str, int] = {}
    for e in events:
        eid = e["event_id"]
        series = []
        for m in markets_by_event.get(eid, []):
            pts = [R.price_point(captured_at=p["captured_at"], yes_bid=None if p["yes_bid"] is None else p["yes_bid"] / 100.0,
                                 yes_ask=None if p["yes_ask"] is None else p["yes_ask"] / 100.0,
                                 last_price=None if p["last_price"] is None else p["last_price"] / 100.0, volume=p["volume"],
                                 open_interest=p["open_interest"], source=p["source"]) for p in inp.ticks.get(m["kalshi_ticker"], [])]
            series.append({"market_id": m["market_id"], "kalshi_ticker": m["kalshi_ticker"], "points": pts})
        links = [R.link(rel="EVENT_RESEARCH", target_kind="event_research", label="event research", target_id=eid, path=R.event_path(eid))]
        doc = R.market_history(sport=SPORT, run_id=c.run_id, generated_at=now, event_id=eid, as_of=inp.ticks_last_at or now, series=series,
                               quality=q_mh, links=links)
        cap = None
        while len(json.dumps(doc, sort_keys=True, separators=(",", ":"))) > MARKET_HISTORY_BUDGET:
            longest = max(len(s["points"]) for s in series)
            cap = max(2, (cap or longest) * 3 // 4)
            for s in series:
                if len(s["points"]) > cap:
                    s["points"] = s["points"][-cap:]
            q_thin = c.q("VERIFIED", q_mh["source"], data_as_of=inp.ticks_last_at, sample_size=inp.n_ticks, coverage=q_mh["coverage"],
                         limitations=q_mh["limitations"] + [f"thinned to the most recent {cap} change points per ticker to stay within "
                                                            f"{MARKET_HISTORY_BUDGET // 1000} KB"])
            doc = R.market_history(sport=SPORT, run_id=c.run_id, generated_at=now, event_id=eid, as_of=inp.ticks_last_at or now,
                                   series=series, quality=q_thin, links=links)
            if cap == 2:
                break
        if cap:
            mh_thinned[eid] = cap
        c.docs.append(doc)

    # ------------------------------------------------------------------------------------ opponent adjustment (RESEARCH)
    oa_fits: dict = {}
    oa_ids: list[str] = []
    try:
        oa_fits = RS.adjusted_fits(inp.team_games, now, cur)
        oa_ids = RS.publish_adjusted(c, oa_fits, reg_metric=reg_metric, make_ranking=make_ranking, team_obs=team_obs, team_rank_refs=team_rank_refs,
                                     team_ids=team_ids, tname=tname, abbrev=abbrev, team_pid=_team_pid, now=now)
    except Exception as e:  # noqa: BLE001 - a research layer never costs the explorer
        warnings.append(f"opponent adjustment skipped: {type(e).__name__}: {str(e)[:160]}")
        oa_fits, oa_ids = {}, []
    thesis_games = {str(g.get("game_id")): g for g in ((packet.get("thesis_card") or {}).get("games") or []) if isinstance(g, dict)}
    thesis_at = _ts((packet.get("thesis_card") or {}).get("generated_at_utc")) or slate_at

    # ------------------------------------------------------------------------------------ event research
    q_event = c.q("PARTIAL", "v1 publication + archive context + slate packet + committed history", data_as_of=None,
                  limitations=[LIM_NO_OPP_ADJ, LIM_INJURIES, LIM_LINES, LIM_DISTRIBUTIONS, LIM_MATCHUP])
    matchup_metrics = [c.mid(m[0]) for m in TEAM_LOG_METRICS] + [c.mid(m[0]) for m in SUMMARY_METRICS] + \
        [c.mid(m[0]) for m in RATING_METRICS] + [c.mid("model_expected_goals")] + oa_ids
    event_players: dict[str, list[dict]] = {}
    n_distributions = 0
    for e in events:
        eid = e["event_id"]
        gid = game_of_event[eid]
        home, away = e.get("home_participant"), e.get("away_participant")
        tid_of = {p["participant_id"]: int(p["source_ids"][TEAM_SOURCE]) for p in e["participants"] if TEAM_SOURCE in p.get("source_ids", {})}
        parts = [{"participant_id": p["participant_id"], "display_name": p["display_name"],
                  "home_away": "HOME" if p["participant_id"] == home else ("AWAY" if p["participant_id"] == away else None),
                  "path": R.team_path(p["participant_id"])} for p in e["participants"]]
        # matchup rows: the current season when both teams have >= 5 regular-season games in it, else the last complete season; L10; run
        primary = hist
        if cur is not None and tid_of and all(sum(1 for r in by_team.get(t, []) if r["season"] == cur and r["game_type"] == 2) >= 5
                                               for t in tid_of.values()):
            primary = cur
        want_windows = {_season_label(primary) if primary else None, w_form["label"], run_label, RS.OA_WINDOW_LABEL}
        rows = []
        for mid in matchup_metrics:
            if mid not in c.metrics:
                continue
            for wl in sorted(w for w in want_windows if w):
                ho = next((o for o in team_obs.get(tid_of.get(home), []) if o["metric_id"] == mid and o["window"]["label"] == wl), None) if home else None
                ao = next((o for o in team_obs.get(tid_of.get(away), []) if o["metric_id"] == mid and o["window"]["label"] == wl), None) if away else None
                if ho or ao:
                    rows.append({"metric_id": mid, "name": c.metrics[mid]["name"], "home": ho, "away": ao, "note": f"window {wl}"})
        # players: projected / confirmed goalies + first power-play unit (from the newest line combinations)
        plist = []
        lineups = []
        for p in e["participants"]:
            tid = tid_of.get(p["participant_id"])
            if tid is None:
                continue
            tl = obs_by_game_team.get((gid, tid), [])
            if tl:
                last = dict(tl[-1])
                if last.get("player_id") is None and last.get("player_name"):
                    # DailyFaceoff rows are name-only; resolve against this team's own roster snapshot (exact normalised name only)
                    nm = _norm_name(last["player_name"])
                    hit = [r for r in roster_by_team.get(tid, []) if _norm_name(f"{r.get('first_name') or ''} {r.get('last_name') or ''}") == nm]
                    if len(hit) == 1:
                        last["player_id"] = int(hit[0]["player_id"])
                lineups.append({"kind": "goalie_status", "team_id": p["participant_id"], "team": abbrev.get(tid),
                                "current": {k: last.get(k) for k in ("status", "player_id", "player_name", "confidence", "source")},
                                "timeline": [{"observed_at": _ts(o.get("observed_at_utc") or o.get("_observed_at_utc")), "status": o.get("status"),
                                              "player_id": o.get("player_id"), "player_name": o.get("player_name"),
                                              "confidence": o.get("confidence"), "source": o.get("source")} for o in tl],
                                "source": "archive context/goalie_observations (DailyFaceoff + boxscore)"})
                gpid = last.get("player_id")
                if gpid is not None and int(gpid) in published_players:
                    plist.append({"participant_id": _player_pid(int(gpid)), "display_name": pname(int(gpid)), "team_id": p["participant_id"],
                                  "role": f"G ({last.get('status')})", "path": R.player_path(_player_pid(int(gpid)))})
            tlines = lines_by_team.get(tid, [])
            if tlines:
                units: dict[str, list[dict]] = defaultdict(list)
                for r in sorted(tlines, key=lambda r: (str(r.get("category")), str(r.get("unit")), str(r.get("slot")))):
                    units[f"{r.get('category')}:{r.get('unit')}"].append({"slot": r.get("slot"), "name": r.get("name"),
                                                                          "player_id": r.get("player_id"), "jersey": r.get("jersey"),
                                                                          "injury_status": r.get("injury_status")})
                lineups.append({"kind": "line_combinations", "team_id": p["participant_id"], "team": abbrev.get(tid),
                                "source": f"DailyFaceoff via archive context/lines ({tlines[0].get('lines_source')})",
                                "lines_updated_at": _ts(tlines[0].get("lines_updated_at_utc")),
                                "observed_at": _ts(tlines[0].get("_observed_at_utc")), "units": dict(sorted(units.items()))})
                for r in sorted((r for r in tlines if r.get("category") == "pp" and r.get("unit") == "pp1"), key=lambda r: str(r.get("slot"))):
                    if r.get("player_id") is not None and int(r["player_id"]) in published_players:
                        plist.append({"participant_id": _player_pid(int(r["player_id"])), "display_name": pname(int(r["player_id"])),
                                      "team_id": p["participant_id"], "role": f"PP1 {r.get('slot')}", "path": R.player_path(_player_pid(int(r["player_id"])))})
        dedup = {}
        for pl in plist:
            dedup.setdefault(pl["participant_id"], pl)
        event_players[eid] = list(dedup.values())
        injuries = [avail_from_injury(inj, eid) for t in tid_of.values() for inj in injuries_by_team.get(t, [])]
        pg = pk_games.get(gid, {})
        ctx = pg.get("context") or {}
        notes = []
        for side in ("home", "away"):
            if ctx.get(f"{side}_rest_days") is not None:
                notes.append(f"{side} rest days {ctx.get(f'{side}_rest_days')}{' (back-to-back)' if ctx.get(f'{side}_b2b') else ''} "
                             f"(slate packet {run_label})")
        distributions = []
        sim = (pg.get("model") or {}).get("sim") or {}
        for key, label, mean_k, sd_k in (("total_quantiles", "total goals (DATA_ONLY_V1 simulation)", "total_mean", "total_sd"),
                                         ("margin_quantiles", "home margin, goals (DATA_ONLY_V1 simulation)", "margin_mean", "margin_sd")):
            qs = sim.get(key)
            if isinstance(qs, dict) and qs and slate_at:
                distributions.append({"market_id": None, "metric_id": None, "entity_id": None, "label": label,
                                      "quantiles": {f"p{int(round(float(k) * 100)):02d}": float(v) for k, v in sorted(qs.items(), key=lambda kv: float(kv[0]))},
                                      "mean": _r(_f(sim.get(mean_k))), "stdev": _r(_f(sim.get(sd_k))), "samples": int(sim.get("n_sims") or 0) or None,
                                      "run_id": c.run_id, "generated_at": slate_at, "source": f"{SRC_SIM} {run_label}", "quality_status": "PARTIAL"})
        n_distributions += len(distributions)
        ev_markets = markets_by_event.get(eid, [])
        fams = sorted({m["market_family"] for m in ev_markets})
        ext = {"nhl_game_id": gid, "primary_season": _season_label(primary) if primary else None,
               "family_calibration": {f: fam_cal[f] for f in fams if f in fam_cal},
               "authority": AUTHORITY}
        if sim:
            ext["sim"] = {k: (_r(_f(v), 5) if isinstance(v, float) else v) for k, v in sim.items()
                          if k in ("p_home_win", "p_away_win", "p_home_reg_win", "p_away_reg_win", "p_overtime", "p_shootout", "p_btts",
                                   "home_lambda", "away_lambda", "total_mean", "margin_mean", "n_sims", "sim_version", "total_ladder",
                                   "home_puckline_ladder", "home_team_total_ladder", "away_team_total_ladder")}
            ext["model_components"] = (pg.get("model") or {}).get("components")
            ext["model_quality"] = "RESEARCH (matchup decomposition) / PARTIAL (distribution)"
        if eid in mh_thinned:
            ext["market_history_thinned_to"] = mh_thinned[eid]
        try:
            ev_tickers = {m["kalshi_ticker"] for m in ev_markets}
            sx = RS.scripts_extension((thesis_games.get(gid) or {}).get("scripts_v1"), generated_at=thesis_at, start_time_utc=e.get("start_time_utc"),
                                      event_tickers=ev_tickers)
            if (thesis_games.get(gid) or {}).get("scripts_v1_error"):
                sx = {"status": "FAILED", "script_version": "NHL_SCRIPT_V1", "reason": thesis_games[gid]["scripts_v1_error"]}
            ext["nhl_scripts_v1"] = sx
            notes += RS.script_notes(sx)
            inj_n = {abbrev.get(t): sum(1 for inj in injuries_by_team.get(t, []) if any(k in str(inj.get("status") or "").upper() for k in ("OUT", "IR", "DOUBT")))
                     for t in tid_of.values()}
            ext["nhl_matchup_v1"] = RS.matchup_findings(home=abbrev.get(tid_of.get(home)), away=abbrev.get(tid_of.get(away)), home_tid=tid_of.get(home),
                                                        away_tid=tid_of.get(away), team_obs=team_obs, mid=c.mid, packet_game=pg,
                                                        injuries={k: v for k, v in inj_n.items() if k}, scripts=sx if sx.get("status") == "OK" else None)
        except Exception as e:  # noqa: BLE001 - a research layer never costs the event document
            warnings.append(f"{eid}: NHL research layer skipped: {type(e).__name__}: {str(e)[:160]}")
            ext["nhl_scripts_v1"] = {"status": "FAILED", "script_version": "NHL_SCRIPT_V1", "reason": f"{type(e).__name__}: {str(e)[:160]}"}
        links = [R.link(rel="TEAM", target_kind="entity_profile", label=p["display_name"], target_id=p["participant_id"],
                        path=R.team_path(p["participant_id"])) for p in e["participants"]]
        links.append(R.link(rel="MARKET_HISTORY", target_kind="market_history", label="quote history", target_id=eid,
                            path=R.market_history_path(eid)))
        for ms in sorted(model_series_by_event.get(eid, []), key=lambda x: x["ticker"]):
            links.append(R.link(rel="SERIES", target_kind="time_series", label=f"model probability {ms['ticker']}",
                                target_id=ms["ser"]["series_id"], path=R.series_path(ms["ser"]["series_id"])))
        er = R.event_research(
            sport=SPORT, run_id=c.run_id, generated_at=now, event=e, quality=q_event, participants=parts, matchup=rows,
            players=event_players[eid], projections=[projection(prices_by_market[m["market_id"]]) for m in ev_markets
                                                     if m["market_id"] in prices_by_market],
            distributions=distributions, markets=[R.market_ref(m) for m in ev_markets], market_history_path=R.market_history_path(eid),
            context={"injuries": injuries, "lineups": lineups, "weather": None,
                     "venue": {"name": e.get("venue"), "neutral_site": (e.get("extensions") or {}).get("neutral_site"), "indoor": True}
                     if e.get("venue") else None, "notes": notes},
            wagers=sorted(wagers_by_event.get(eid, [])), links=links, extensions=ext)
        c.docs.append(er)

    # ------------------------------------------------------------------------------------ team profiles
    upcoming_by_team: dict[int, list[dict]] = defaultdict(list)
    for e in events:
        for p in e["participants"]:
            tid = p.get("source_ids", {}).get(TEAM_SOURCE)
            if tid is not None:
                upcoming_by_team[int(tid)].append(e)
    q_team_profile = c.q("PARTIAL", "MoneyPuck game logs + NHL official results/summaries + slate packet + archive context",
                         data_as_of=log_as_of, limitations=[LIM_NO_OPP_ADJ, LIM_TEAM_LOG_HISTORY,
                                                            f"game logs and series capped at the last {GAME_LOG_CAP} games"])
    log_cols = ["game_id", "date", "opp", "ha", "type", "gf", "ga", "xgf", "xga", "cf", "ca", "ff", "fa", "hdxgf", "hdxga", "src"]
    for t in active:
        tid = t.team_id
        pid = _team_pid(tid)
        ent = participants[tid]
        rows = by_team.get(tid, [])[-GAME_LOG_CAP:]
        games = []
        opps: dict[int, list[str]] = defaultdict(list)
        for r in rows:
            g = inp.games.get(r["game_id"], {})
            eid = _event_id(r["game_id"])
            res = None
            if g.get("final") and g.get("home_score") is not None:
                mine, theirs = (g["home_score"], g["away_score"]) if r["home"] else (g["away_score"], g["home_score"])
                res = {"for": float(mine), "against": float(theirs), "outcome": "W" if mine > theirs else "L"}
            games.append(R.game_ref(event_id=eid, start_time_utc=g.get("start_utc") or f"{r['date']}T00:00:00Z",
                                    status="FINAL" if res else "UNKNOWN", opponent_id=_team_pid(r["opp_team_id"]),
                                    opponent_name=tname.get(r["opp_team_id"]), home_away="HOME" if r["home"] else "AWAY", result=res,
                                    competition="playoffs" if r["game_type"] == 3 else "regular",
                                    path=R.event_path(eid) if eid in published_events else None))
            opps[r["opp_team_id"]].append(eid)
        for e in upcoming_by_team.get(tid, []):
            other = next((p for p in e["participants"] if p["participant_id"] != pid), None)
            if e["event_id"] in {g["event_id"] for g in games}:
                continue
            games.append(R.game_ref(event_id=e["event_id"], start_time_utc=e["start_time_utc"], status=e["status"],
                                    opponent_id=other["participant_id"] if other else None, opponent_name=other["display_name"] if other else None,
                                    home_away="HOME" if e.get("home_participant") == pid else "AWAY", result=None,
                                    competition=e.get("competition"), path=R.event_path(e["event_id"])))
            if other:
                otid = other.get("source_ids", {}).get(TEAM_SOURCE)
                if otid is not None:
                    opps[int(otid)].append(e["event_id"])
        upcoming_markets = [m for e in upcoming_by_team.get(tid, []) for m in markets_by_event.get(e["event_id"], []) if m.get("participant_id") == pid]
        links = []
        for e in upcoming_by_team.get(tid, []):
            links.append(R.link(rel="EVENT", target_kind="event_research", label=f"next game {e['start_time_utc'][:10]}",
                                target_id=e["event_id"], path=R.event_path(e["event_id"])))
            links.append(R.link(rel="MARKET_HISTORY", target_kind="market_history", label="quote history", target_id=e["event_id"],
                                path=R.market_history_path(e["event_id"])))
            for p in e["participants"]:
                if p["participant_id"] != pid:
                    links.append(R.link(rel="OPPONENT", target_kind="entity_profile", label=p["display_name"], target_id=p["participant_id"],
                                        path=R.team_path(p["participant_id"])))
        links.append(R.link(rel="CAPABILITIES", target_kind="capability_manifest", label="what this sport can show",
                            path=R.app_path(R.CAPABILITIES_NAME)))
        players_ref = [{"participant_id": _player_pid(int(r["player_id"])), "display_name": pname(int(r["player_id"])),
                        "role": r.get("position"), "path": R.player_path(_player_pid(int(r["player_id"]))) if int(r["player_id"]) in published_players else None}
                       for r in sorted(roster_by_team.get(tid, []), key=lambda r: (str(r.get("position")), pname(int(r["player_id"]))))]
        ext: dict[str, Any] = {"nhl_team_id": tid, "abbrev": t.abbrev, "game_log": {
            "columns": log_cols, "source": "MoneyPuck all-situation team game log (history for completed seasons, archive for the current one)",
            "cap": GAME_LOG_CAP, "rows": [[r["game_id"], r["date"], abbrev.get(r["opp_team_id"]), "H" if r["home"] else "A",
                                           "P" if r["game_type"] == 3 else "R"] + [_r(r[k], 3) for k in log_cols[5:-1]] + [r["src"]] for r in rows]}}
        if tid in team_state:
            ext["team_state"] = {k: (_r(v) if isinstance(v, float) else v) for k, v in team_state[tid].items() if not k.startswith("_")}
            ext["team_state_run"] = run_label
        prof = R.entity_profile(
            sport=SPORT, run_id=c.run_id, generated_at=now, entity=ent, entity_type="TEAM", quality=q_team_profile,
            season=_season_label(cur) if cur else None, league="NHL", team=None,
            metrics=sorted(team_obs.get(tid, []), key=lambda o: (o["metric_id"], o["window"]["label"])),
            splits={k: sorted(v, key=lambda o: (o["metric_id"], o["window"]["label"], o["split"]["value"])) for k, v in sorted(team_split_obs.get(tid, {}).items())},
            series=team_series_refs.get(tid, []), rankings=sorted(team_rank_refs.get(tid, []), key=lambda r: (r["metric_id"], r["window_label"], str(r["split"]))),
            games=games, players=players_ref,
            opponents=[{"participant_id": _team_pid(o), "display_name": tname.get(o, str(o)), "event_ids": sorted(set(v)),
                        "path": R.team_path(_team_pid(o)) if o in team_id_set else None}
                       for o, v in sorted(opps.items())],
            markets=[R.market_ref(m) for m in upcoming_markets],
            projections=[projection(prices_by_market[m["market_id"]]) for m in upcoming_markets if m["market_id"] in prices_by_market],
            availability=[avail_from_injury(inj, None) for inj in injuries_by_team.get(tid, [])], links=links, extensions=ext)
        c.docs.append(prof)
        c.search.append(R.search_entry(id=pid, kind="TEAM", label=ent["display_name"], path=R.team_path(pid), sport=SPORT,
                                       secondary=f"{(ent.get('metadata') or {}).get('division') or ''} division".strip(),
                                       aliases=[t.abbrev, t.city, t.nickname], league="NHL", season=_season_label(cur) if cur else None))

    # ------------------------------------------------------------------------------------ player profiles
    q_player_profile = c.q("PARTIAL", SRC_PLAYERS, data_as_of=max(player_as_of.values()) if player_as_of else None,
                           limitations=[LIM_PLAYER_LOG, f"game logs capped at the last {GAME_LOG_CAP} games within the seasons loaded "
                                        f"({', '.join(_season_label(s) for s in sorted({int(r['season']) for r in inp.skater_games}))})",
                                        LIM_INJURIES])
    sk_cols = ["game_id", "date", "opp", "ha", "type", "g", "a", "p", "sog", "toi_s", "toi_ev_s", "toi_pp_s", "toi_sh_s", "pm"]
    gk_cols = ["game_id", "date", "opp", "ha", "type", "start", "dec", "sa", "sv", "ga", "toi_s", "ev_sa", "ev_sv", "pp_sa", "pp_sv", "sh_sa", "sh_sv"]
    for tid in sorted(event_team_ids):
        team_pid = _team_pid(tid)
        team_ref = {"participant_id": team_pid, "display_name": tname[tid], "short_name": abbrev.get(tid), "path": R.team_path(team_pid)}
        for r in sorted(roster_by_team.get(tid, []), key=lambda r: int(r["player_id"])):
            plid = int(r["player_id"])
            ppid = _player_pid(plid)
            pos = r.get("position")
            ent = build.participant(sport=SPORT, participant_type="PLAYER", source=PLAYER_SOURCE, source_id=plid, display_name=pname(plid),
                                    short_name=r.get("last_name"), source_ids={"nhl_team_id": tid},
                                    metadata={k: v for k, v in {"position": pos, "sweater": r.get("sweater"), "shoots_catches": r.get("shoots_catches"),
                                                                "birth_date": r.get("birth_date"), "team": abbrev.get(tid)}.items() if v is not None})
            is_goalie = pos == "G"
            logs = (gk_by_player if is_goalie else sk_by_player).get(plid, [])[-GAME_LOG_CAP:]
            if is_goalie:
                log_rows = [[str(g["game_id"]), str(g["game_date"]), abbrev.get(int(g["away_team_id"] if g["is_home"] else g["home_team_id"])),
                             "H" if g["is_home"] else "A", "P" if int(g.get("game_type") or 2) == 3 else "R", bool(g.get("starter")), g.get("decision"),
                             g.get("shots_against"), g.get("saves"), g.get("goals_against"), g.get("toi_s"), g.get("ev_sa"), g.get("ev_saves"),
                             g.get("pp_sa"), g.get("pp_saves"), g.get("sh_sa"), g.get("sh_saves")] for g in logs]
            else:
                log_rows = [[str(g["game_id"]), str(g["game_date"]), abbrev.get(int(g["away_team_id"] if g["is_home"] else g["home_team_id"])),
                             "H" if g["is_home"] else "A", "P" if int(g.get("game_type") or 2) == 3 else "R", g.get("goals"), g.get("assists"),
                             g.get("points"), g.get("sog"), g.get("toi_s"), _r(_f(g.get("toi_ev_s")), 0) if g.get("shifts_ok") else None,
                             _r(_f(g.get("toi_pp_s")), 0) if g.get("shifts_ok") else None, _r(_f(g.get("toi_sh_s")), 0) if g.get("shifts_ok") else None,
                             g.get("plus_minus")] for g in logs]
            avail = []
            upcoming = upcoming_by_team.get(tid, [])
            if plid in injury_by_player:
                avail.append(avail_from_injury(injury_by_player[plid], upcoming[0]["event_id"] if upcoming else None))
            if is_goalie:
                for e in upcoming:
                    tl = obs_by_game_team.get((game_of_event[e["event_id"]], tid), [])
                    if tl and tl[-1].get("player_id") is not None:
                        last = tl[-1]
                        mine = int(last["player_id"]) == plid
                        avail.append({"status": f"{last.get('status')}_STARTER" if mine else "NOT_PROJECTED_STARTER",
                                      "detail": f"{last.get('player_name')} {last.get('status')} (confidence {last.get('confidence')})",
                                      "as_of": _ts(last.get("observed_at_utc") or last.get("_observed_at_utc")),
                                      "source": f"archive context/goalie_observations ({last.get('source')})", "event_id": e["event_id"]})
            games = []
            for e in upcoming:
                other = next((p for p in e["participants"] if p["participant_id"] != team_pid), None)
                games.append(R.game_ref(event_id=e["event_id"], start_time_utc=e["start_time_utc"], status=e["status"],
                                        opponent_id=other["participant_id"] if other else None, opponent_name=other["display_name"] if other else None,
                                        home_away="HOME" if e.get("home_participant") == team_pid else "AWAY", competition=e.get("competition"),
                                        path=R.event_path(e["event_id"])))
            links = [R.link(rel="TEAM", target_kind="entity_profile", label=tname[tid], target_id=team_pid, path=R.team_path(team_pid))]
            links += [R.link(rel="EVENT", target_kind="event_research", label=f"next game {e['start_time_utc'][:10]}", target_id=e["event_id"],
                             path=R.event_path(e["event_id"])) for e in upcoming]
            prof = R.entity_profile(
                sport=SPORT, run_id=c.run_id, generated_at=now, entity=ent, entity_type="PLAYER", quality=q_player_profile,
                season=_season_label(cur) if cur else None, league="NHL", team=team_ref,
                metrics=sorted(player_obs.get(plid, []), key=lambda o: (o["metric_id"], o["window"]["label"])),
                splits={k: v for k, v in sorted(player_split_obs.get(plid, {}).items())},
                rankings=sorted(player_rank_refs.get(plid, []), key=lambda r: (r["metric_id"], r["window_label"])),
                games=games, availability=avail, links=links,
                extensions={"nhl_player_id": plid, "position": pos, "game_log": {
                    "columns": gk_cols if is_goalie else sk_cols, "cap": GAME_LOG_CAP, "rows": log_rows,
                    "source": "official NHL boxscore + play-by-play + shift charts; toi_* by strength state null when shift charts are missing"}})
            c.docs.append(prof)
            c.search.append(R.search_entry(id=ppid, kind="PLAYER", label=ent["display_name"], path=R.player_path(ppid), sport=SPORT,
                                           secondary=f"{pos} {abbrev.get(tid)}", aliases=[str(r.get("last_name") or "")], team=abbrev.get(tid),
                                           position=pos, league="NHL", season=_season_label(cur) if cur else None))

    # ------------------------------------------------------------------------------------ remaining docs + search
    c.docs.extend(c.series)
    c.docs.extend(c.rankings.values())
    for e in events:
        names = {p["participant_id"]: p.get("short_name") or p["display_name"] for p in e["participants"]}
        label = f"{names.get(e.get('away_participant'), '?')} @ {names.get(e.get('home_participant'), '?')}"
        c.search.append(R.search_entry(id=e["event_id"], kind="EVENT", label=label, path=R.event_path(e["event_id"]), sport=SPORT,
                                       secondary=f"{e['start_time_utc'][:10]} {e.get('competition') or ''}".strip(),
                                       aliases=[p["display_name"] for p in e["participants"]], league="NHL", season=e.get("season")))
    for mid, m in sorted(c.metrics.items()):
        c.search.append(R.search_entry(id=mid, kind="METRIC", label=m["name"], path=R.app_path(R.METRICS_NAME), sport=SPORT,
                                       secondary=m["category"], aliases=[m["short_name"]]))
    for rid, rk in sorted(c.rankings.items()):
        sp = f" {rk['split']['dimension']}={rk['split']['value']}" if rk.get("split") else ""
        c.search.append(R.search_entry(id=rid, kind="RANKING", label=f"{c.metrics[rk['metric_id']]['name']} ranking",
                                       secondary=f"{rk['universe']['label']} [{rk['window']['label']}{sp}]", path=R.ranking_path(rid), sport=SPORT,
                                       season=rk["universe"]["season"]))

    try:
        RS.register_learning(reg_metric, c, RS.learning_extension(inp.learning, inp.eval_status), now)
    except Exception as e:  # noqa: BLE001
        warnings.append(f"learning scorecard skipped: {type(e).__name__}: {str(e)[:160]}")
    as_of = max((a for a in data_as_of if a), default=now)
    docs_by_kind = defaultdict(list)
    for d in c.docs:
        docs_by_kind[d["kind"] + (":" + d["entity_type"] if d["kind"] == "entity_profile" else "")].append(R.path_for(d))
    caps = _capabilities(c, inp, docs_by_kind=docs_by_kind, events=events, team_seasons=team_seasons, seasons=seasons,
                         split_dims=published_split_metrics, has_ratings=bool(team_state), has_lambdas=bool(lambdas),
                         lines_at=_ts(lines_at) if lines_at else None, fam_cal=fam_cal, first_date=first_date, player_first=player_first,
                         mh_thinned=mh_thinned, n_distributions=n_distributions, n_model_dropped=n_model_dropped, oa_ids=oa_ids)
    windows = [season_windows[s] for s in seasons] + [w_form] + ([w_run] if team_state or lambdas else [])
    manifest = R.capability_manifest(
        sport=SPORT, run_id=c.run_id, generated_at=now, capabilities=caps, audit_date=AUDIT_DATE,
        split_dimensions=[{"dimension": "situation", "values": sorted(split_dims["situation"]), "status": "PARTIAL"},
                          {"dimension": "home_away", "values": sorted(split_dims["home_away"]), "status": "PARTIAL"},
                          {"dimension": "strength_state", "values": ["EV", "PP", "SH"], "status": "PARTIAL"}],
        windows=windows,
        notes=[f"statuses follow the NHL research-data audit of {AUDIT_DATE} (§4 capability matrix, §10 recommendations); a mixed rating "
               "publishes the lower status unless only the higher-rated part is published",
               "every number is copied from a stored record or is plain arithmetic over stored records (totals, rates, shares, trailing "
               "means, ranks), except the met_nhl.oa_* metrics, which are opponent-adjusted by a documented RESEARCH model (nhl-oppadj-1.0)",
               "event_research.extensions.nhl_scripts_v1 carries NHL_SCRIPT_V1 game scripts, script-conditioned market pricing, script survival and "
               "research candidates (RESEARCH_ONLY); extensions.nhl_matchup_v1 carries basis-labelled findings",
               "model prices, projections and distributions are research outputs (authority RESEARCH_ONLY), never recommendations"])
    registry_doc = R.metric_registry(sport=SPORT, run_id=c.run_id, generated_at=now, metrics=list(c.metrics.values()))
    search = R.search_index(sport=SPORT, run_id=c.run_id, generated_at=now, entries=c.search)
    out = c.docs + [manifest, registry_doc, search]
    q_index = c.q("PARTIAL", "NHL-edge-finder: data-archive + data/history on main + the v1 publication", data_as_of=as_of,
                  limitations=[LIM_NO_OPP_ADJ, LIM_TEAM_LOG_HISTORY, LIM_PLAYER_LOG])
    meta = {"as_of": as_of, "quality": q_index, "windows": windows, "warnings": warnings}
    return out, meta


# ============================================================================================ capabilities
#: The audit's §4 matrix (as published by this export). A mixed audit rating publishes the lower status unless only the
#: higher-rated part is published (usage: only actual TOI; calibration: only the prospective evaluation).
CAPABILITY_STATUS = {
    "team_profiles": "PARTIAL", "player_profiles": "PARTIAL", "event_research": "PARTIAL", "team_metrics": "PARTIAL",
    "player_metrics": "PARTIAL", "team_game_logs": "PARTIAL", "player_game_logs": "PARTIAL", "historical_results": "PARTIAL",
    "opponents": "PARTIAL", "opponent_adjustment": "RESEARCH", "schedule_strength": "RESEARCH", "recent_form_windows": "PARTIAL",
    "usage": "VERIFIED", "lineups": "PARTIAL", "injuries": "PARTIAL", "matchup_metrics": "RESEARCH", "projection_distributions": "PARTIAL",
    "raw_projections": "VERIFIED", "market_prices": "VERIFIED", "market_price_history": "VERIFIED", "advanced_stats": "PARTIAL",
    "situational_splits": "PARTIAL", "player_props": "VERIFIED", "team_props": "VERIFIED", "game_markets": "VERIFIED",
    "play_by_play": "UNAVAILABLE", "weather": "UNAVAILABLE", "venue_effects": "UNAVAILABLE", "calibration": "VERIFIED",
    "historical_accuracy": "VERIFIED", "clv": "VERIFIED", "wager_history": "UNAVAILABLE", "rankings": "PARTIAL", "time_series": "PARTIAL",
    "comparisons": "PARTIAL", "search": "VERIFIED",
}


def _capabilities(c: _Ctx, inp: ResearchInputs, *, docs_by_kind: dict[str, list[str]], events: list[dict], team_seasons: list[int],
                  seasons: list[int], split_dims: dict, has_ratings: bool, has_lambdas: bool, lines_at: str | None, fam_cal: dict,
                  first_date: str | None, player_first: str | None, mh_thinned: dict, n_distributions: int, n_model_dropped: int = 0,
                  oa_ids: list[str] | None = None) -> list[dict]:
    teams = sorted(docs_by_kind.get("entity_profile:TEAM", []))
    players = sorted(docs_by_kind.get("entity_profile:PLAYER", []))
    evs = sorted(docs_by_kind.get("event_research", []))
    ranks = sorted(docs_by_kind.get("ranking", []))
    sers = sorted(docs_by_kind.get("time_series", []))
    mhs = sorted(docs_by_kind.get("market_history", []))
    ap = R.app_path
    team_ser = sorted(R.path_for(s) for s in c.series if s["entity_type"] == "TEAM")
    model_ser = sorted(R.path_for(s) for s in c.series if s["entity_type"] == "MARKET")
    ev_markets = [m for m in inp.markets if m.get("event_id") in {e["event_id"] for e in events}]
    fam = lambda pred: [m for m in ev_markets if pred(m["market_family"])]  # noqa: E731
    out: list[dict] = []

    def cap(name: str, summary: str, *, evidence: list[str], present: bool, absent_reason: str, limitations: list[str] | None = None,
            entity_types: list[str] | None = None, coverage: str | None = None, since: Any = None, metrics: list[str] | None = None,
            windows: list[str] | None = None, splits: list[str] | None = None, reasons: list[str] | None = None, status: str | None = None) -> None:
        status = status or CAPABILITY_STATUS[name]
        if status in ("VERIFIED", "PARTIAL", "RESEARCH") and (not present or not evidence):
            out.append(R.capability(capability=name, status="UNAVAILABLE", summary=summary, entity_types=entity_types,
                                    reasons=[absent_reason, f"audit {AUDIT_DATE} rates it {status}; nothing for it is in this publication"]))
            return
        if status in ("UNAVAILABLE", "UNKNOWN"):
            out.append(R.capability(capability=name, status=status, summary=summary, entity_types=entity_types, reasons=reasons or [absent_reason]))
            return
        out.append(R.capability(capability=name, status=status, summary=summary, entity_types=entity_types, reasons=reasons or [],
                                limitations=limitations or [], evidence=[ap(p) for p in evidence[:3]], coverage=coverage, since=since,
                                metrics=[m for m in (metrics or []) if m in c.metrics], windows=windows or [], splits=splits or []))

    mid = c.mid
    season_labels = [_season_label(s) for s in team_seasons]
    team_log_metrics = [mid(m[0]) for m in TEAM_LOG_METRICS]
    n_team_rows = sum(1 for r in inp.team_games if r["situation"] == "all")
    cap("team_profiles", "one profile per active NHL team: season and L10 metrics with league rank, splits, last-82-game log, upcoming "
        "games, markets and model prices", evidence=teams, present=bool(teams), absent_reason="no team profile could be built",
        limitations=[LIM_NO_OPP_ADJ, LIM_TEAM_LOG_HISTORY], entity_types=["TEAM"], coverage=f"{len(teams)} teams", since=first_date)
    cap("player_profiles", "one profile per rostered skater and goalie of the teams on the published slate: official season, current-season "
        "and L10 numbers, TOI by strength state, last-82-game log, injury / goalie-start status", evidence=players, present=bool(players),
        absent_reason="no roster snapshot or no player game logs in this archive", limitations=[LIM_PLAYER_LOG, LIM_INJURIES],
        entity_types=["PLAYER"], coverage=f"{len(players)} players on the rosters of {len(events)} published events' teams",
        since=player_first)
    cap("event_research", "one document per published event: matchup rows, market refs, DATA_ONLY_V1 projections, simulated distributions, "
        "goalie status timeline, line combinations, injuries, family calibration", evidence=evs, present=bool(evs),
        absent_reason="no events in the v1 publication", limitations=[LIM_NO_OPP_ADJ, LIM_INJURIES, LIM_LINES],
        entity_types=["EVENT"], coverage=f"{len(evs)} events")
    cap("team_metrics", "MoneyPuck xG / Corsi / Fenwick / danger shares and rates, official points / PP / PK percentages, point-in-time "
        "DATA_ONLY_V1 ratings", evidence=teams + [R.METRICS_NAME], present=bool(team_seasons or has_ratings),
        absent_reason="no team game logs and no packet ratings", limitations=[LIM_TEAM_RATINGS, LIM_NO_OPP_ADJ, LIM_TEAM_LOG_HISTORY],
        entity_types=["TEAM"], coverage=", ".join(season_labels), since=first_date,
        metrics=team_log_metrics + [mid(m[0]) for m in SUMMARY_METRICS + RATING_METRICS], windows=season_labels + [f"L{FORM_N}"])
    cap("player_metrics", "official goals, assists, points, shots, TOI, points/60; goalie save %, EV save %, GAA", evidence=players,
        present=bool(players), absent_reason="no player profiles", limitations=[LIM_PLAYER_LOG], entity_types=["PLAYER"],
        metrics=[mid(m[0]) for m in SKATER_METRICS + GOALIE_METRICS], windows=[_season_label(s) for s in seasons] + [f"L{FORM_N}"],
        since=player_first)
    cap("team_game_logs", f"per-game MoneyPuck rows (xG, Corsi, Fenwick, high-danger xG, goals) with opponent and home/away, last "
        f"{GAME_LOG_CAP} games per team, in each team profile's extensions.game_log", evidence=teams, present=n_team_rows > 0,
        absent_reason="no MoneyPuck rows", limitations=[LIM_TEAM_LOG_HISTORY, f"capped at the last {GAME_LOG_CAP} games per team"],
        entity_types=["TEAM"], coverage=f"{n_team_rows} team-game rows loaded (all situations)", since=first_date)
    cap("player_game_logs", f"official per-player-game rows (G, A, P, SOG, TOI by EV/PP/SH, +/-) and goalie rows (saves / shots against by "
        f"state, starter, decision), last {GAME_LOG_CAP} games, in each player profile's extensions.game_log", evidence=players,
        present=bool(players and (inp.skater_games or inp.goalie_games)), absent_reason="no player game logs",
        limitations=[LIM_PLAYER_LOG, f"capped at the last {GAME_LOG_CAP} games"], entity_types=["PLAYER"],
        coverage=f"{len(inp.skater_games)} skater-games + {len(inp.goalie_games)} goalie-games loaded", since=player_first)
    n_final = sum(1 for g in inp.games.values() if g.get("final"))
    cap("historical_results", "official final scores on every game reference (W/L, goals for/against)", evidence=teams,
        present=n_final > 0, absent_reason="no official results", limitations=[LIM_RESULTS], entity_types=["TEAM"],
        coverage=f"{n_final} final games (data/history/nhl + archive results)", since=first_date)
    cap("opponents", "opponent id, name and home/away on every game and series point; opponent lists per team", evidence=teams,
        present=n_team_rows > 0, absent_reason="no game logs", limitations=[LIM_RESULTS], entity_types=["TEAM"], since=first_date)
    if oa_ids:
        oa_lim = [RS.LIM_OA, "raw MoneyPuck metrics, official PP/PK and DATA_ONLY_V1 ratings remain raw and are labelled so",
                  "walk-forward evidence: docs/research/opponent_adjustment/eval.json (adjusted beats raw by 1.8-3.4% rate MSE on 2023-26)"]
        cap("opponent_adjustment", "opponent-adjusted 5v5 team metrics (met_nhl.oa_*): weighted ridge offense/defense effects fit on games before the "
            "cutoff; raw same-games values kept in each observation's extensions.raw_value", evidence=teams, present=bool(teams),
            absent_reason="no 5v5 team game logs", limitations=oa_lim, entity_types=["TEAM"], metrics=oa_ids, windows=[RS.OA_WINDOW_LABEL],
            status="RESEARCH", reasons=["computed fresh by this export from per-game 5v5 rows with opponent ids (point in time, ridge-regularised)",
                                        "RESEARCH, not VERIFIED: walk-forward sanity check only; not an input to DATA_ONLY_V1"])
        cap("schedule_strength", "schedule effect per team and metric = raw rate - opponent-adjusted rate (extensions.schedule_effect on every "
            "met_nhl.oa_* observation)", evidence=teams, present=bool(teams), absent_reason="no 5v5 team game logs", limitations=oa_lim,
            entity_types=["TEAM"], metrics=oa_ids, status="RESEARCH",
            reasons=["derived from the opponent adjustment (raw minus adjusted, same games and weights); RESEARCH like its source"])
    else:
        cap("opponent_adjustment", "not available", evidence=[], present=False, absent_reason=LIM_NO_OPP_ADJ,
            reasons=[LIM_NO_OPP_ADJ, LIM_SVA, "no 5v5 team game logs to fit the opponent adjustment on"])
        cap("schedule_strength", "not available", evidence=[], present=False, absent_reason="Schedule strength: not computed",
            reasons=["Schedule strength: not computed (no opponent adjustment in this build)"])
    cap("recent_form_windows", f"L{FORM_N}: each team's / player's last {FORM_N} stored games, plain means and shares computed by this export, "
        "ranked for teams", evidence=teams + players[:1], present=n_team_rows > 0, absent_reason="no game logs",
        limitations=[LIM_FORM], entity_types=["TEAM", "PLAYER"], windows=[f"L{FORM_N}"])
    cap("usage", "actual TOI per game by strength state (EV / PP / SH) from shift charts, per season", evidence=players,
        present=bool(players and inp.skater_games), absent_reason="no player game logs", entity_types=["PLAYER"],
        limitations=["projected TOI (PLAYER_SIM_V1 shadow, PARTIAL) is not published"], metrics=[mid("toi_per_game")],
        splits=["strength_state"])
    lineups_present = bool(inp.lines or inp.goalie_obs)
    cap("lineups", "goalie status timeline per game (UNKNOWN -> PROJECTED -> PROBABLE -> CONFIRMED) and the newest DailyFaceoff line "
        "combinations / PP-PK units per team, in event research context.lineups", evidence=evs, present=lineups_present,
        absent_reason="no lines or goalie observations in this archive", limitations=[LIM_LINES], entity_types=["EVENT"],
        coverage=f"{len(inp.lines)} line rows (newest snapshot per team, {lines_at or 'n/a'}), {len(inp.goalie_obs)} goalie observations",
        since=min((str(r.get("observed_at_utc") or r.get("_observed_at_utc") or "")[:10] for r in inp.goalie_obs), default=None) or None)
    cap("injuries", "current ESPN injury list per team (team profile availability, event research context.injuries), name-matched to "
        "rostered players", evidence=evs + teams[:1], present=bool(inp.injuries), absent_reason="no injury snapshot in this archive",
        limitations=[LIM_INJURIES, LIM_LINES], entity_types=["TEAM", "PLAYER", "EVENT"],
        coverage=f"{len(inp.injuries)} rows, snapshot {inp.injuries_at}")
    cap("matchup_metrics", "home/away rows of the same metric per event (raw and opponent-adjusted), DATA_ONLY_V1 expected goals (lambda) and its "
        "decomposition, NHL_SCRIPT_V1 game scripts with script-conditioned market pricing and survival (extensions.nhl_scripts_v1)",
        evidence=evs, present=bool(evs and (has_lambdas or team_seasons)), absent_reason="no events",
        limitations=[LIM_MATCHUP, LIM_NO_OPP_ADJ], entity_types=["EVENT", "TEAM"], metrics=[mid("model_expected_goals")])
    cap("projection_distributions", "total-goals and home-margin quantiles (p05..p95), mean and sd from the latest DATA_ONLY_V1 simulation; "
        "ladders in event extensions.sim", evidence=evs, present=n_distributions > 0,
        absent_reason="no simulated distribution for the published events in the slate packet", limitations=[LIM_DISTRIBUTIONS],
        entity_types=["EVENT"], coverage=f"{n_distributions} distributions")
    cap("raw_projections", "DATA_ONLY_V1 fair probability per contract per run: current values as projections, history as RUN series",
        evidence=model_ser + evs[:1], present=bool(model_ser), absent_reason="no priced DATA_ONLY_V1 rows for the published events",
        limitations=["research outputs (authority RESEARCH_ONLY); 81% of V1 rows are UNSUPPORTED (no p_data_only)"]
        + ([f"{n_model_dropped} probability series omitted to keep the explorer index within budget (team totals first)"]
           if n_model_dropped else []),
        entity_types=["MARKET"], metrics=[mid("model_prob_v1")], coverage=f"{len(model_ser)} tickers",
        since=min((r["predicted_at_utc"][:10] for r in inp.predictions), default=None))
    cap("market_prices", "current Kalshi bid / ask / last for every market of every published event (v1 markets, as market refs)",
        evidence=evs, present=bool(ev_markets), absent_reason="no markets joined to the published events", entity_types=["MARKET"],
        coverage=f"{len(ev_markets)} markets")
    cap("market_price_history", "per event, every ticker's quote-change series reconstructed from checkpoints + deltas",
        evidence=mhs, present=bool(mhs and inp.ticks), absent_reason="no captured board ticks for the published events' tickers",
        limitations=["one point per quote change plus the last observation"] + ([f"{len(mh_thinned)} event(s) thinned to stay within the "
                                                                              "400 KB document budget"] if mh_thinned else []),
        entity_types=["MARKET"], coverage=f"{inp.n_ticks} ticks, {len(inp.ticks)} tickers",
        since=min((p[0]["captured_at"][:10] for p in inp.ticks.values() if p), default=None))
    cap("advanced_stats", "expected goals, Corsi, Fenwick, high-danger xG, score/venue-adjusted xG (MoneyPuck)", evidence=teams,
        present=n_team_rows > 0, absent_reason="no MoneyPuck rows", limitations=[LIM_ADVANCED, LIM_SVA], entity_types=["TEAM"],
        metrics=team_log_metrics, since=first_date)
    cap("situational_splits", "team splits by situation (5on5 / 5on4 / 4on5) and home/away; player TOI by strength state",
        evidence=teams + players[:1], present=bool(split_dims.get("situation") or split_dims.get("home_away")),
        absent_reason="no situation rows", limitations=[LIM_SPLITS], entity_types=["TEAM", "PLAYER"],
        splits=sorted(k for k, v in split_dims.items() if v) + ["strength_state"])
    pp = fam(lambda f: f.startswith("player_") or f in ("first_goal", "goalie_saves"))
    cap("player_props", "player-prop markets (goals, points, assists, saves, first goal) as captured on the board for the published events",
        evidence=evs, present=bool(evs), absent_reason="no events", entity_types=["MARKET"],
        limitations=["capture VERIFIED; player pricing (PLAYER_SIM_V1) is RESEARCH and not published as projections"],
        coverage=f"{len(pp)} player-prop markets on the current board")
    cap("team_props", "team-total markets for the published events", evidence=evs, present=bool(evs), absent_reason="no events",
        entity_types=["MARKET"], coverage=f"{len(fam(lambda f: f == 'team_total'))} team-total markets")
    cap("game_markets", "moneyline, puck line, totals, period, overtime and early-goal markets for the published events", evidence=evs,
        present=bool(evs), absent_reason="no events", entity_types=["MARKET"],
        coverage=f"{len(fam(lambda f: f.startswith('game_') or f.startswith('period_')))} game-level markets")
    cap("play_by_play", "not published", evidence=[], present=False,
        absent_reason="the audit rates shots/goals PARTIAL (no faceoff/hit/penalty events); this export does not publish per-play rows "
        "(no explorer kind carries them); goals, assists, SOG and TOI by strength are in the player game logs",
        reasons=["Play-by-play: PARTIAL in the audit (official attempts and goals only); not exposed by the explorer"])
    cap("weather", "not applicable", evidence=[], present=False, absent_reason="Weather: UNAVAILABLE (indoor sport)")
    cap("venue_effects", "venue name and neutral-site flag only (event research context.venue)", evidence=[], present=False,
        absent_reason="Venue / park effects: UNAVAILABLE (effects) / PARTIAL (venue name, neutral_site); the model uses a constant "
        "HOME_ADJ=1.045")
    cal_ok = bool(fam_cal)
    cap("calibration", "per family: Brier, log loss, ECE, 10-bin reliability of DATA_ONLY_V1 vs the Kalshi mid on settled pregame rows "
        "(metrics.json calibration_v1; event research extensions.family_calibration)", evidence=[R.METRICS_NAME] + evs[:1], present=cal_ok,
        absent_reason="no eval/report.json in this archive", limitations=["prospective sample is days deep; small samples prove nothing"],
        entity_types=["MARKET"], metrics=[mid("calibration_v1"), mid("calibration_player_sim")],
        coverage=f"{(inp.eval_report or {}).get('n_rows')} settled evaluation rows")
    cap("historical_accuracy", "settled-outcome accuracy per family (Brier / log loss / hit rate) from the evaluate job",
        evidence=[R.METRICS_NAME], present=cal_ok, absent_reason="no eval/report.json in this archive",
        limitations=["prospective only; the historical walk-forwards under docs/research are RESEARCH and not published"],
        entity_types=["MARKET"], metrics=[mid("calibration_v1")])
    cap("clv", "mean signed closing-line value of the DATA_ONLY_V1 side per family", evidence=[R.METRICS_NAME], present=cal_ok and any(
        "clv_mean" in v for v in fam_cal.values()), absent_reason="no CLV in the evaluation report",
        limitations=["close = last tick strictly before start; 8.3% of rows lack a close (audit)"], entity_types=["MARKET"],
        metrics=[mid("clv_v1")])
    if inp.wagers:
        out.append(R.capability(capability="wager_history", status="PARTIAL", summary="routed wagers listed per event (ids into v1 wagers.json)",
                                entity_types=["EVENT"], limitations=["the router-delivered accounting ledger is the authority (v1 wagers.json)"],
                                evidence=[ap(p) for p in evs[:3]], coverage=f"{len(inp.wagers)} wagers"))
    else:
        cap("wager_history", "no wagers", evidence=[], present=False,
            absent_reason="Historical wager outcomes: UNAVAILABLE, accounting-data empty (0 wagers)")
    cap("rankings", "full-league rankings for every team metric and window (and slate-wide for ratings); skater / goalie season "
        "rankings with a minimum-games universe", evidence=ranks, present=bool(ranks), absent_reason="no values to rank",
        limitations=[LIM_RANKINGS, LIM_NO_OPP_ADJ], entity_types=["TEAM", "PLAYER"], coverage=f"{len(ranks)} rankings")
    cap("time_series", f"per-game team series (xGF%, xGF/60, xGA/60, CF%; last {GAME_LOG_CAP} games, rolling L{FORM_N}) for the "
        "teams on the slate; DATA_ONLY_V1 probability per run for every priced ticker", evidence=team_ser + model_ser,
        present=bool(sers), absent_reason="no series", limitations=[LIM_TEAM_LOG_HISTORY, f"team series only for teams on the published "
                                                                     f"slate, last {GAME_LOG_CAP} games"],
        entity_types=["TEAM", "MARKET"], metrics=[mid(s) for s in SERIES_METRICS] + [mid("model_prob_v1")], since=first_date)
    cap("comparisons", "observation context (rank, universe size, league average / median, best, worst) on every ranked number; "
        "home vs away matchup rows per event", evidence=ranks + evs[:1], present=bool(ranks), absent_reason="no rankings",
        limitations=[LIM_RANKINGS, LIM_NO_OPP_ADJ], entity_types=["TEAM", "PLAYER", "EVENT"])
    cap("search", "search index over every published team, player, event, metric and ranking", evidence=[R.SEARCH_NAME],
        present=True, absent_reason="", entity_types=["TEAM", "PLAYER", "EVENT"])
    return out


# ============================================================================================ publish
def export_explorer(app_root: Path, archive_root: Path, *, now: Any = None, history_root: Path | None = None,
                    commit_sha: str | None = None, inputs: ResearchInputs | None = None) -> dict:
    """Load, build and publish ``<app_root>/explorer`` atomically. ``run_id`` is the v1 manifest's; ``generated_at`` is
    ``now`` (default: the v1 manifest's ``generated_at``, i.e. the instant the v1 export used). Raises on failure; the
    previous explorer tree is then untouched (``research.publish_explorer``)."""
    app_root = Path(app_root)
    inp = inputs or load_research_inputs(app_root, Path(archive_root), history_root=history_root)
    run_id = inp.manifest["run_id"]
    generated_at = timeutil.to_iso(now) if now is not None else inp.manifest["generated_at"]
    docs, meta = build_explorer(inp, run_id=run_id, generated_at=generated_at)
    index = R.publish_explorer(app_root=app_root, sport=SPORT, run_id=run_id, generated_at=generated_at, documents=docs,
                               quality=meta["quality"], as_of=meta["as_of"], commit_sha=commit_sha or inp.manifest.get("commit_sha"),
                               base_manifest_run_id=run_id, windows=meta["windows"], warnings=meta["warnings"])
    return {"ok": True, "run_id": run_id, "generated_at": generated_at, "counts": index["counts"], "bytes": R.tree_bytes(app_root),
            "as_of": meta["as_of"], "warnings": meta["warnings"]}


def add_arguments(ap) -> None:
    """The ``nhl research-export`` / ``scripts/research_export.py`` options (mirrors ``nhl app-export``)."""
    import os

    ap.add_argument("--data-root", default="data/archive", help="archive root (a checkout of the data-archive branch)")
    ap.add_argument("--out", default=None, help="the v1 app root to publish explorer/ into (default <data-root>/app/latest)")
    ap.add_argument("--now", default=None, help="ISO-8601 UTC generation instant (default: the v1 manifest's generated_at)")
    ap.add_argument("--history-root", default=None, help="committed history (default <repo>/data/history)")
    ap.add_argument("--commit-sha", default=os.environ.get("GITHUB_SHA") or None)
    ap.add_argument("--min-interval-minutes", type=float, default=0.0,
                    help="rebuild only when research.refresh_due says so (explorer missing, v1 events changed, or older than this); "
                         "0 = always rebuild")


def run_from_args(a) -> int:
    from nhl_edge.app_export import APP_ROOT_RELATIVE

    root = Path(a.data_root)
    out = Path(a.out) if a.out else root / APP_ROOT_RELATIVE
    if a.min_interval_minutes and a.min_interval_minutes > 0:
        due, reason = R.refresh_due(out, now=a.now or timeutil.now_utc(), min_interval_seconds=a.min_interval_minutes * 60.0)
        if not due:
            print(json.dumps({"ok": True, "skipped": True, "out": str(out / R.EXPLORER_DIR), "reason": reason}, indent=1))
            return 0
        print(f"research-export: rebuilding ({reason})", file=sys.stderr)
    try:
        res = export_explorer(out, root, now=a.now, history_root=Path(a.history_root) if a.history_root else None, commit_sha=a.commit_sha)
    except Exception as exc:  # noqa: BLE001 - reported and turned into exit 1; the previous explorer tree stands
        problems = getattr(exc, "problems", None)
        print(json.dumps({"ok": False, "out": str(out), "error": f"{type(exc).__name__}: {str(exc)[:2000]}",
                          "problems": (problems or [])[:50]}, indent=1), file=sys.stderr)
        return 1
    print(json.dumps({"ok": True, "out": str(out / R.EXPLORER_DIR), "run_id": res["run_id"], "generated_at": res["generated_at"],
                      "as_of": res["as_of"], "counts": res["counts"], "bytes": res["bytes"], "warnings": res["warnings"][:20]}, indent=1))
    return 0


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="nhl research-export", description="publish the Edge Finder research explorer (contract 1.1.0)")
    add_arguments(ap)
    return run_from_args(ap.parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
