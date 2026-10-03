"""A small REAL slice of the production archive for the research explorer tests.

``tests/fixtures/research_slice.json.gz`` holds rows copied (fields trimmed, values untouched) from the
``data-archive`` branch for the five opening-night games the v1 test archive schedules (2026020001-2026020005,
2026-09-29): rosters, injuries, line combinations, goalie observations, official team summaries, live team game
logs by situation, results, official player / goalie game logs, DATA_ONLY_V1 predictions, the Kalshi board ticks of
the FLA @ CAR tickers captured before the test archive's own checkpoint, the evaluation reports, and one slate
packet game block (``team_state`` + ``model``), which :func:`install_slice` re-labels onto each test game exactly as
``tests/archive_fixture.py`` re-labels the real sample markets. The committed history under ``data/history`` is read
directly by the export, so it is not copied here.

Regenerate (needs the archive checked out):  ``python -m tests.research_fixture <archive_root>``
"""

from __future__ import annotations

import gzip
import json
import sys
from pathlib import Path

from nhl_edge.archive.ledger import Ledger
from nhl_edge.timeutil import parse_iso

SLICE = Path(__file__).resolve().parent / "fixtures" / "research_slice.json.gz"
GAMES = ("2026020001", "2026020002", "2026020003", "2026020004", "2026020005")
TEAM_IDS = (12, 13, 10, 8, 6, 3, 22, 23, 54, 16)  # CAR FLA TOR MTL BOS NYR EDM VAN VGK CHI
TICK_CUTOFF = "2026-09-29T14:55:00Z"  # the v1 test archive's own checkpoint is observed at 14:55Z
TICKERS_PREFIX = ("KXNHLGAME-26SEP29FLACAR", "KXNHLSPREAD-26SEP29FLACAR", "KXNHLTOTAL-26SEP29FLACAR")

KEEP = {
    "context/rosters": ["player_id", "team_id", "team_abbrev", "position", "first_name", "last_name", "sweater", "shoots_catches", "birth_date"],
    "context/injuries": ["team_name", "team_id", "player_name", "position", "status", "type", "detail", "return_date", "source"],
    "context/lines": ["team_abbrev", "team_id", "category", "unit", "slot", "jersey", "name", "player_id", "injury_status",
                      "lines_updated_at_utc", "lines_source", "observed_at_utc", "resolution"],
    "context/goalie_observations": ["game_id", "team_id", "player_id", "player_name", "status", "observed_at_utc", "source", "confidence"],
    "context/team_summary": ["teamId", "seasonId", "teamFullName", "gamesPlayed", "wins", "losses", "otLosses", "points", "pointPct",
                             "powerPlayPct", "penaltyKillPct", "goalsForPerGame", "goalsAgainstPerGame"],
    "context/team_games": ["team", "team_abbrev", "opposingTeam", "gameId", "gameDate", "season", "home_or_away", "situation", "iceTime",
                           "xGoalsFor", "xGoalsAgainst", "goalsFor", "goalsAgainst", "shotAttemptsFor", "shotAttemptsAgainst",
                           "unblockedShotAttemptsFor", "unblockedShotAttemptsAgainst", "shotsOnGoalFor", "shotsOnGoalAgainst",
                           "highDangerxGoalsFor", "highDangerxGoalsAgainst", "scoreVenueAdjustedxGoalsFor", "scoreVenueAdjustedxGoalsAgainst"],
    "context/team_games_st": ["team", "team_abbrev", "opposingTeam", "gameId", "gameDate", "season", "home_or_away", "situation", "iceTime",
                              "xGoalsFor", "xGoalsAgainst", "goalsFor", "goalsAgainst"],
    "results": ["game_id", "status", "home_team_id", "away_team_id", "home_final", "away_final", "home_reg", "away_reg", "last_period_type",
                "source"],
    "predictions": ["ticker", "game_id", "family", "predicted_at_utc", "model_version", "p_data_only", "p_data_only_se", "p_market", "gate"],
}


def _rows(path: Path) -> list[dict]:
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        return [json.loads(x) for x in fh if x.strip()]


def build_slice(archive_root: Path, out: Path = SLICE) -> dict:
    """Copy the slice out of a checked-out archive (run by hand; the result is committed)."""
    from nhl_edge.archive.reconstruct import iter_board_ticks

    root = Path(archive_root)
    ledger = Ledger(root)
    entries = ledger.manifest()
    kinds: dict[str, list[dict]] = {}

    def pick(kind: str, rows: list[dict]) -> list[dict]:
        cols = KEEP.get(kind)
        return [{k: r.get(k) for k in cols} | {"_observed_at_utc": r.get("_observed_at_utc")} if cols else r for r in rows]

    def latest_before(kind: str, before: str | None) -> list[dict]:
        es = [e for e in entries if e.kind == kind and (before is None or (e.observed_at_utc or "") <= before)]
        if not es:
            return []
        e = max(es, key=lambda e: e.observed_at_utc or e.written_at_utc)
        return _rows(root / e.path)

    start = "2026-09-29T21:00:00Z"
    kinds["context/rosters"] = pick("context/rosters", [r for r in latest_before("context/rosters", start) if r.get("team_id") in TEAM_IDS])
    kinds["context/injuries"] = pick("context/injuries", [r for r in latest_before("context/injuries", start) if r.get("team_id") in TEAM_IDS])
    first_lines: dict[int, str] = {}
    lines = []
    for e in sorted((e for e in entries if e.kind == "context/lines"), key=lambda e: e.observed_at_utc or ""):
        for r in _rows(root / e.path):
            tid = r.get("team_id")
            if tid in TEAM_IDS and first_lines.setdefault(tid, e.path) == e.path:
                lines.append(r)
    kinds["context/lines"] = pick("context/lines", lines)
    kinds["context/goalie_observations"] = pick("context/goalie_observations", [r for r in ledger.iter_rows("context/goalie_observations")
                                                                                if str(r.get("game_id")) in GAMES])
    kinds["context/team_summary"] = pick("context/team_summary", [r for r in latest_before("context/team_summary", None) if r.get("teamId") in TEAM_IDS])
    kinds["context/team_games"] = pick("context/team_games", [r for r in latest_before("context/team_games", None) if str(r.get("gameId")) in GAMES])
    kinds["context/team_games_st"] = pick("context/team_games_st", [r for r in latest_before("context/team_games_st", None)
                                                                    if str(r.get("gameId")) in GAMES])
    kinds["results"] = pick("results", [r for r in ledger.iter_rows("results") if str(r.get("game_id")) in GAMES])
    kinds["player_events/players"] = [r for r in ledger.iter_rows("player_events/players") if str(r.get("game_id")) in GAMES]
    kinds["player_events/goalies"] = [r for r in ledger.iter_rows("player_events/goalies") if str(r.get("game_id")) in GAMES]
    kinds["predictions"] = pick("predictions", [r for r in ledger.iter_rows("predictions")
                                                if str(r.get("game_id")) in GAMES and r.get("p_data_only") is not None])
    ticks = []
    for at, _run, board, _raw in iter_board_ticks(ledger):
        stamp = at.isoformat().replace("+00:00", "Z")
        if stamp >= TICK_CUTOFF:
            break
        rows = [{k: r.get(k) for k in ("ticker", "event_ticker", "series_ticker", "status", "volume_fp", "open_interest_fp", "_quote_cents",
                                       "_family", "_support")} for t, r in sorted(board.items()) if t.startswith(TICKERS_PREFIX)]
        if rows:
            ticks.append({"observed_at_utc": stamp, "rows": rows})
    packet = json.loads((root / "slates" / "latest" / "packet.json").read_text())
    g = packet["games"][0]
    sim_keys = ("sim_version", "n_sims", "home_lambda", "away_lambda", "total_mean", "total_sd", "margin_mean", "margin_sd", "p_home_win",
                "p_away_win", "p_overtime", "p_shootout", "total_quantiles", "margin_quantiles", "total_ladder", "home_puckline_ladder")
    model = {k: g["model"][k] for k in ("model_version", "sim_version", "feature_version", "components")}
    model["sim"] = {k: g["model"]["sim"][k] for k in sim_keys}

    def trim_report(rep: dict) -> dict:
        fams = {}
        for f, d in (rep.get("families") or {}).items():
            fams[f] = {"n": d.get("n"), "n_pregame": d.get("n_pregame"), "authority": d.get("authority"),
                       "views": {v: {k: x for k, x in (dv or {}).items() if k != "calibration"} for v, dv in (d.get("views") or {}).items()}}
        return {k: rep.get(k) for k in ("evaluated_at_utc", "authority", "n_rows", "n_pregame", "note", "model_version")} | {
            "overall": rep.get("overall"), "families": fams}

    data = {"source": "chmoses98/NHL-edge-finder data-archive (real rows, fields trimmed)", "kinds": kinds, "ticks": ticks,
            "packet_game": {"identity": g["identity"], "team_state": g["team_state"], "model": model},
            "slate_generated_at_utc": packet["slate"].get("generated_at_utc"),
            "eval_report": trim_report(json.loads((root / "eval" / "report.json").read_text())),
            "eval_report_player": trim_report(json.loads((root / "eval" / "report_player.json").read_text()))}
    out.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(out, "wt", encoding="utf-8", compresslevel=9) as fh:
        json.dump(data, fh, sort_keys=True, separators=(",", ":"))
    return {k: len(v) for k, v in kinds.items()} | {"ticks": len(ticks), "bytes": out.stat().st_size}


def load_slice() -> dict:
    with gzip.open(SLICE, "rt", encoding="utf-8") as fh:
        return json.load(fh)


def install_slice(root: Path) -> dict:
    """Append the slice to a test archive built by ``tests/archive_fixture.build_archive`` (+ the v1 test's slate/packet)."""
    data = load_slice()
    ledger = Ledger(root, run_id="slice")
    by_obs: dict[tuple[str, str], list[dict]] = {}
    for kind, rows in sorted(data["kinds"].items()):
        for r in rows:
            by_obs.setdefault((kind, r.get("_observed_at_utc") or "2026-09-29T12:00:00Z"), []).append(r)
    for i, ((kind, at), rows) in enumerate(sorted(by_obs.items())):
        ledger.append_rows(kind, rows, observed_at=parse_iso(at), part=f"s{i}")
    for i, tick in enumerate(data["ticks"]):
        ledger.append_rows("kalshi/markets", tick["rows"], observed_at=parse_iso(tick["observed_at_utc"]), meta={"encoding": "checkpoint"},
                           part=f"t{i}")
    (root / "eval").mkdir(parents=True, exist_ok=True)
    (root / "eval" / "report.json").write_text(json.dumps(data["eval_report"]))
    (root / "eval" / "report_player.json").write_text(json.dumps(data["eval_report_player"]))
    pk_path = root / "slates" / "latest" / "packet.json"
    packet = json.loads(pk_path.read_text())
    src = data["packet_game"]
    for g in packet.get("games", []):
        ident = g["identity"]
        ts = json.loads(json.dumps(src["team_state"]))
        ts["home"]["team"], ts["away"]["team"] = ident["home"], ident["away"]
        g["team_state"], g["model"] = ts, json.loads(json.dumps(src["model"]))
    pk_path.write_text(json.dumps(packet, indent=1))
    return data


if __name__ == "__main__":
    print(json.dumps(build_slice(Path(sys.argv[1])), indent=1))
