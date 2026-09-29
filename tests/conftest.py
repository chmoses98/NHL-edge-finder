"""Shared fixtures: a synthetic archive built from the REAL probe samples (schedule, Kalshi markets) plus a synthetic
MoneyPuck-shaped team game log. No network anywhere in the test suite."""

from __future__ import annotations

import json
import random
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

from nhl_edge.archive.ledger import Ledger
from nhl_edge.config import REPO_ROOT
from nhl_edge.data.context import game_rows
from nhl_edge.data.nhl_api import parse_schedule
from nhl_edge.identity.teams import registry
from nhl_edge.kalshi.normalize import quote_cents
from nhl_edge.kalshi.ontology import Ontology, classify_market

SAMPLES = REPO_ROOT / "docs" / "probe" / "samples"
NOW = datetime(2026, 9, 29, 15, 0, tzinfo=UTC)  # 6h before the first opening-night start (21:00Z)


def sample(name: str):
    return json.loads((SAMPLES / f"{name}.json").read_text())


def sample_markets() -> list[dict]:
    onto = Ontology.load()
    rows = []
    for n in ("kalshi_api_markets_kxnhlgame_open", "kalshi_api_markets_kxnhlspread_open", "kalshi_api_markets_kxnhltotal_open"):
        for m in sample(n)["markets"]:
            if not isinstance(m, dict):
                continue
            m = dict(m)
            m.setdefault("series_ticker", m["ticker"].split("-")[0])
            cls = classify_market(m, onto)
            m["_family"], m["_support"], m["_quote_cents"] = cls.family, str(cls.support), quote_cents(m)
            rows.append(m)
    return rows


def opening_night_markets() -> list[dict]:
    """The real Oct 1 / Oct 5 sample markets re-labelled onto opening night (FLA @ CAR, 2026-09-29): identical shapes."""
    subs = [("San Jose", "Florida"), ("Dallas", "Carolina"), ("Oct 5, 2026", "Sep 29, 2026"), ("26OCT05SJDAL", "26SEP29FLACAR"), ("-SJ", "-FLA"), ("-DAL", "-CAR"),
            ("SJ vs DAL", "FLA vs CAR"), ("Edmonton", "Florida"), ("Vancouver", "Carolina"), ("Oct 1, 2026", "Sep 29, 2026"), ("26OCT01EDMVAN", "26SEP29FLACAR"),
            ("-VAN", "-CAR"), ("-EDM", "-FLA")]
    out = []
    for m in sample_markets():
        if "26OCT05SJDAL" not in m["ticker"] and "26OCT01EDMVAN" not in m["ticker"]:
            continue
        txt = json.dumps(m)
        for a, b in subs:
            txt = txt.replace(a, b)
        out.append(json.loads(txt))
    return out


def synthetic_team_games(seed: int = 7, seasons=(2024, 2025), games_per_team: int = 82) -> list[dict]:
    """MoneyPuck all_teams.csv-shaped rows (situation 'all') with team-specific true strengths."""
    rng = random.Random(seed)
    teams = [t.abbrev for t in registry().active_teams]
    strength = {t: rng.gauss(0, 0.12) for t in teams}
    rows = []
    gid = 1
    for season in seasons:
        d0 = datetime(season, 10, 8)
        for i in range(games_per_team * len(teams) // 2):
            a, h = rng.sample(teams, 2)
            date = d0 + timedelta(days=i // 16)
            for team, opp, ha in ((h, a, "HOME"), (a, h, "AWAY")):
                xgf = max(0.8, 3.0 * (1 + strength[team] - strength[opp]) + rng.gauss(0, 0.6))
                xga = max(0.8, 3.0 * (1 - strength[team] + strength[opp]) + rng.gauss(0, 0.6))
                rows.append({"team": team, "season": season, "name": team, "gameId": int(f"{season}02{gid:04d}"), "playerTeam": team, "opposingTeam": opp,
                             "home_or_away": ha, "gameDate": int(date.strftime("%Y%m%d")), "position": "Team Level", "situation": "all",
                             "xGoalsFor": round(xgf, 2), "xGoalsAgainst": round(xga, 2), "goalsFor": rng.choice([max(0, round(xgf + rng.gauss(0, 1)))]),
                             "goalsAgainst": max(0, round(xga + rng.gauss(0, 1))), "iceTime": 3600.0, "team_abbrev": team, "opp_abbrev": opp})
            gid += 1
    return rows


def build_archive(root: Path, now: datetime = NOW, with_markets: bool = True, with_goalies: bool = True) -> Ledger:
    ledger = Ledger(root, run_id="test-run")
    games = parse_schedule(sample("nhl_schedule_date"))
    t0 = now - timedelta(minutes=20)
    ledger.append_rows("context/schedule", game_rows(games), observed_at=t0)
    ledger.append_rows("context/team_games", synthetic_team_games(), observed_at=t0)
    ledger.append_rows("context/goalie_stats", [
        {"_source": "nhl_stats", "playerId": 8475683, "goalieFullName": "Sergei Bobrovsky", "shotsAgainst": 1500, "saves": 1370, "_season_id": 20252026},
        {"_source": "nhl_stats", "playerId": 8480382, "goalieFullName": "Frederik Andersen", "shotsAgainst": 900, "saves": 820, "_season_id": 20252026},
        {"_source": "moneypuck", "playerId": 8475683, "name": "Sergei Bobrovsky", "situation": "all", "goals": 120, "xGoals": 135, "games_played": 55},
        {"_source": "moneypuck", "playerId": 8480382, "name": "Frederik Andersen", "situation": "all", "goals": 80, "xGoals": 78, "games_played": 35},
    ], observed_at=t0)
    ledger.append_rows("context/rosters", [
        {"player_id": 8475683, "team_id": 13, "position": "G", "first_name": "Sergei", "last_name": "Bobrovsky"},
        {"player_id": 8480382, "team_id": 12, "position": "G", "first_name": "Frederik", "last_name": "Andersen"},
    ], observed_at=t0)
    if with_goalies:
        t_obs = now - timedelta(minutes=15)
        ledger.append_rows("context/goalie_observations", [
            {"game_id": "2026020001", "team_id": 13, "player_id": None, "player_name": "Sergei Bobrovsky", "status": "CONFIRMED", "observed_at_utc": t_obs.isoformat().replace("+00:00", "Z"), "source": "dailyfaceoff", "confidence": 0.985, "alternatives": []},
            {"game_id": "2026020001", "team_id": 12, "player_id": None, "player_name": "Frederik Andersen", "status": "PROJECTED", "observed_at_utc": t_obs.isoformat().replace("+00:00", "Z"), "source": "dailyfaceoff", "confidence": 0.7, "alternatives": []},
        ], observed_at=t_obs)
        # a LATER confirmation that a simulation at `now` must NOT see
        t_late = now + timedelta(hours=2)
        ledger.append_rows("context/goalie_observations", [
            {"game_id": "2026020001", "team_id": 12, "player_id": 8480382, "player_name": "Frederik Andersen", "status": "CONFIRMED", "observed_at_utc": t_late.isoformat().replace("+00:00", "Z"), "source": "dailyfaceoff", "confidence": 0.985, "alternatives": []},
        ], observed_at=t_late)
    if with_markets:
        ledger.append_rows("kalshi/markets", sample_markets() + opening_night_markets(), observed_at=now - timedelta(minutes=5), meta={"encoding": "checkpoint"})
    return ledger


@pytest.fixture
def archive(tmp_path: Path) -> Ledger:
    return build_archive(tmp_path / "archive")
