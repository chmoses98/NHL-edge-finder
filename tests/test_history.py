"""History ingestion: MoneyPuck CSV / NHL stats parsers, Parquet + MANIFEST writing, on synthetic fixtures.

The fixture builders here (``synthetic_moneypuck_csv`` / ``synthetic_nhl_payload``) are shared with
``tests/test_walk_forward.py``. They produce a tiny 3-team, 2-season league using the real MoneyPuck column names
(a subset of ``docs/probe/samples/mp_all_teams_gbg.json``) and the real NHL stats ``/game`` shape.
"""

from __future__ import annotations

import csv
import io
import json
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pytest

from nhl_edge.config import REPO_ROOT
from nhl_edge.data import history as H
from nhl_edge.features.ratings import prepare_gamelog

SAMPLES = REPO_ROOT / "docs" / "probe" / "samples"

# MoneyPuck raw codes -> (NHL team id, canonical abbrev). T.B is deliberately an alias to prove normalisation.
TEAMS = {"TOR": (10, "TOR"), "BOS": (6, "BOS"), "T.B": (14, "TBL")}
STRENGTH = {"TOR": 3.6, "BOS": 3.0, "T.B": 2.4}  # expected goals per 60 (for) -- TOR strong, T.B weak
SITUATIONS = ("all", "5on5", "5on4", "4on5", "other")
ICE = {"all": 3600.0, "5on5": 2900.0, "5on4": 300.0, "4on5": 300.0, "other": 100.0}

MP_COLUMNS = [
    "team", "season", "name", "gameId", "playerTeam", "opposingTeam", "home_or_away", "gameDate", "position", "situation",
    "xGoalsPercentage", "corsiPercentage", "fenwickPercentage", "iceTime", "xOnGoalFor", "xGoalsFor", "shotsOnGoalFor",
    "goalsFor", "xOnGoalAgainst", "xGoalsAgainst", "shotsOnGoalAgainst", "goalsAgainst", "playoffGame",
]


def synthetic_schedule(seasons=(2023, 2024), games_per_pair: int = 10, seed: int = 7, playoff_game: bool = True) -> list[dict[str, Any]]:
    """Deterministic list of games: {season, game_id, game_type, date, home, away, hs, as, period}."""
    rng = np.random.default_rng(seed)
    teams = list(TEAMS)
    pairs = [(a, b) for i, a in enumerate(teams) for b in teams[i + 1:]]
    games: list[dict[str, Any]] = []
    for season in seasons:
        n = 0
        d = date(season, 10, 10)
        slots = []
        for k in range(games_per_pair):
            for a, b in pairs:
                home, away = (a, b) if k % 2 == 0 else (b, a)
                slots.append((home, away))
        rng.shuffle(slots)
        for home, away in slots:
            n += 1
            lam_h = STRENGTH[home] * 1.05 * (3.0 / STRENGTH[away]) ** 0.5
            lam_a = STRENGTH[away] / 1.05 * (3.0 / STRENGTH[home]) ** 0.5
            hs, as_ = int(rng.poisson(lam_h)), int(rng.poisson(lam_a))
            period = 3
            if hs == as_:
                period = 4 if rng.random() < 0.66 else 5
                if rng.random() < 0.5 + 0.2 * (lam_h / (lam_h + lam_a) - 0.5):
                    hs += 1
                else:
                    as_ += 1
            games.append({"season": season, "game_id": season * 1_000_000 + 20_000 + n, "game_type": 2, "date": d,
                          "home": home, "away": away, "hs": hs, "as": as_, "period": period})
            d += timedelta(days=2)
        if playoff_game:
            games.append({"season": season, "game_id": season * 1_000_000 + 30_111, "game_type": 3, "date": d + timedelta(days=30),
                          "home": "TOR", "away": "BOS", "hs": 2, "as": 3, "period": 5})
    return games


def synthetic_moneypuck_csv(games: list[dict[str, Any]], seed: int = 11, situations=SITUATIONS) -> str:
    """One row per team per game per situation, MoneyPuck column names, values as strings like the real CSV."""
    rng = np.random.default_rng(seed)
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(MP_COLUMNS)
    for g in games:
        for side, opp, gf, ga in ((g["home"], g["away"], g["hs"], g["as"]), (g["away"], g["home"], g["as"], g["hs"])):
            ha = "HOME" if side == g["home"] else "AWAY"
            for sit in situations:
                share = ICE[sit] / 3600.0
                xgf = max(0.0, STRENGTH[side] * share + rng.normal(0, 0.3 * share))
                xga = max(0.0, STRENGTH[opp] * share + rng.normal(0, 0.3 * share))
                gfs = gf if sit == "all" else int(rng.binomial(gf, share)) if gf else 0
                gas = ga if sit == "all" else int(rng.binomial(ga, share)) if ga else 0
                w.writerow([side, str(g["season"]), side, str(g["game_id"]), side, opp, ha, g["date"].strftime("%Y%m%d"), "Team Level", sit,
                            f"{xgf / max(xgf + xga, 1e-9):.3f}", "0.5", "0.5", f"{ICE[sit]:.1f}", f"{xgf * 10:.3f}", f"{xgf:.3f}", f"{xgf * 12:.0f}",
                            f"{gfs:.1f}", f"{xga * 10:.3f}", f"{xga:.3f}", f"{xga * 12:.0f}", f"{gas:.1f}", "1" if g["game_type"] == 3 else "0"])
    return buf.getvalue()


def synthetic_nhl_payload(games: list[dict[str, Any]], season: int, game_type: int, unfinished_last: bool = False) -> dict[str, Any]:
    data = []
    sel = [g for g in games if g["season"] == season and g["game_type"] == game_type]
    for i, g in enumerate(sel):
        final = not (unfinished_last and i == len(sel) - 1)
        data.append({
            "id": g["game_id"], "easternStartTime": f"{g['date'].isoformat()}T19:00:00", "gameDate": g["date"].isoformat(),
            "gameNumber": i + 1, "gameScheduleStateId": 1, "gameStateId": 7 if final else 1, "gameType": game_type,
            "homeScore": g["hs"] if final else 0, "homeTeamId": TEAMS[g["home"]][0], "period": g["period"] if final else None,
            "season": H.season_id(season), "visitingScore": g["as"] if final else 0, "visitingTeamId": TEAMS[g["away"]][0],
        })
    return {"data": data, "total": len(data)}


def install_fake_fetch(monkeypatch: pytest.MonkeyPatch, games: list[dict[str, Any]], csv_text: str | None = None,
                       fail_moneypuck: bool = False, seasons=(2023, 2024)) -> dict[str, int]:
    """Route ``history.fetch_bytes`` to the synthetic sources. Returns a call counter by source."""
    csv_text = csv_text if csv_text is not None else synthetic_moneypuck_csv(games)
    calls = {"moneypuck": 0, "nhl": 0}

    def fake(url: str, timeout_s: float) -> tuple[bytes, str]:
        if url == H.MONEYPUCK_ALL_TEAMS_URL:
            calls["moneypuck"] += 1
            if fail_moneypuck:
                raise RuntimeError("simulated MoneyPuck outage")
            return csv_text.encode("utf-8"), "2026-01-01T00:00:00Z"
        for s in seasons:
            for gt in (2, 3):
                if url == H.nhl_games_url(s, gt):
                    calls["nhl"] += 1
                    return json.dumps(synthetic_nhl_payload(games, s, gt)).encode("utf-8"), "2026-01-01T00:00:01Z"
        raise AssertionError(f"unexpected url {url}")

    monkeypatch.setattr(H, "fetch_bytes", fake)
    return calls


# --------------------------------------------------------------------------------------------------------------
@pytest.fixture(scope="module")
def games() -> list[dict[str, Any]]:
    return synthetic_schedule()


@pytest.fixture(scope="module")
def mp_csv(games) -> str:
    return synthetic_moneypuck_csv(games)


def test_parse_seasons_and_ids():
    assert H.parse_seasons("2024, 2022,2023") == [2022, 2023, 2024]
    assert H.parse_seasons([2025, "2025"]) == [2025]
    assert H.season_id(2025) == 20252026
    with pytest.raises(ValueError):
        H.parse_seasons("2024-25")
    assert "season=20242025" in H.nhl_games_url(2024, 2) and "gameType=3" in H.nhl_games_url(2024, 3)


def test_last_period_type_mapping():
    assert H.last_period_type(3, 2) == "REG"
    assert H.last_period_type(4, 2) == "OT"
    assert H.last_period_type(5, 2) == "SO"
    assert H.last_period_type(6, 2) == "SO"
    assert H.last_period_type(5, 3) == "OT"  # playoffs never reach a shootout
    assert H.last_period_type(None, 2) is None
    assert H.last_period_type(2, 2) is None


def test_parse_moneypuck_csv_normalises(mp_csv, games):
    df = H.parse_moneypuck_csv(mp_csv)
    assert set(df["situation"]) == set(H.KEEP_SITUATIONS)  # 'other' dropped
    n_games = len(games)
    assert len(df) == n_games * 2 * len(H.KEEP_SITUATIONS)
    assert set(df["season"]) == {2023, 2024}
    # identity normalisation: raw code kept, canonical added, ids resolved
    tb = df[df["mp_team"] == "T.B"]
    assert len(tb) and (tb["team_abbrev"] == "TBL").all() and (tb["team_id"] == 14).all()
    assert (df.loc[df["mp_opposing_team"] == "T.B", "opp_abbrev"] == "TBL").all()
    assert (df["team"] == df["mp_team"]).all()  # raw MoneyPuck column untouched
    assert set(df["team_id"].dropna().astype(int)) == {6, 10, 14}
    # derived columns
    assert df["game_type"].isin([2, 3]).all() and (df["game_type"] == 3).sum() == 2 * len(H.KEEP_SITUATIONS) * 2
    assert df["game_date"].str.match(r"\d{4}-\d{2}-\d{2}").all()
    assert df["home"].dtype == bool and df["home"].sum() == len(df) / 2
    assert (df["schema_version"] == H.SCHEMA_VERSION).all()
    assert df["xGoalsFor"].dtype.kind == "f" and df["goalsFor"].dtype.kind == "f"
    assert H.unresolved_abbrevs(df) == {}
    # season / situation filters
    d23 = H.parse_moneypuck_csv(mp_csv, seasons=[2023], situations=("all",))
    assert set(d23["season"]) == {2023} and set(d23["situation"]) == {"all"}
    # prepare_gamelog accepts the frame directly (the ratings' contract)
    lg = prepare_gamelog(df)
    assert len(lg) == n_games * 2 and (lg["situation"] == "all").all()


def test_parse_moneypuck_csv_unknown_team_and_dupes(mp_csv):
    extra = mp_csv + mp_csv.splitlines()[1].replace("TOR", "ZZZ", 1) + "\n"
    df = H.parse_moneypuck_csv(extra)
    assert H.unresolved_abbrevs(df) == {"ZZZ": 1}
    assert df.loc[df["mp_team"] == "ZZZ", "team_abbrev"].isna().all()
    dup = mp_csv + "\n".join(mp_csv.splitlines()[1:6]) + "\n"
    assert len(H.parse_moneypuck_csv(dup)) == len(H.parse_moneypuck_csv(mp_csv))
    with pytest.raises(ValueError):
        H.parse_moneypuck_csv("team,season\nTOR,2024\n")


def test_parse_moneypuck_real_sample_header():
    """The probe sample carries the real all_teams.csv header + first rows (2008, situation 'other' etc.)."""
    rows = json.loads((SAMPLES / "mp_all_teams_gbg.json").read_text())
    buf = io.StringIO()
    csv.writer(buf).writerows(rows)
    df = H.parse_moneypuck_csv(buf.getvalue(), seasons=None, situations=None)
    assert len(df) == len(rows) - 1
    assert (df["team_abbrev"] == "NYR").all() and (df["opp_abbrev"] == "TBL").all()
    assert (df["season"] == 2008).all() and (df["game_type"] == 2).all()
    assert "name" not in df.columns and "xGoalsFor" in df.columns and "playoffGame" in df.columns


def test_parse_nhl_games(games):
    payload = synthetic_nhl_payload(games, 2024, 2, unfinished_last=True)
    df = H.parse_nhl_games(payload)
    assert list(df.columns) == H.NHL_GAME_COLUMNS
    n = sum(1 for g in games if g["season"] == 2024 and g["game_type"] == 2)
    assert len(df) == n and df["final"].sum() == n - 1
    assert (df["season"] == 2024).all() and (df["season_id"] == 20242025).all() and (df["game_type"] == 2).all()
    fin = df[df["final"]]
    assert set(fin["last_period_type"]) <= {"REG", "OT", "SO"}
    assert fin["home_win"].notna().all() and (fin["total"] == fin["home_score"] + fin["away_score"]).all()
    assert set(fin["home_abbrev"]) <= {"TOR", "BOS", "TBL"} and set(fin["away_abbrev"]) <= {"TOR", "BOS", "TBL"}
    nf = df[~df["final"]]
    assert nf["last_period_type"].isna().all() and nf["home_win"].isna().all() and nf["total"].isna().all()
    # ordered by date then id; period mapping consistent with the source
    assert df["game_date"].is_monotonic_increasing
    src = {g["game_id"]: g["period"] for g in games}
    for r in fin.itertuples():
        assert r.last_period_type == {3: "REG", 4: "OT", 5: "SO"}[src[int(r.game_id)]]
    # playoffs: period 5 is OT, not SO
    po = H.parse_nhl_games(synthetic_nhl_payload(games, 2024, 3))
    assert len(po) == 1 and po.iloc[0]["last_period_type"] == "OT" and po.iloc[0]["game_type"] == 3


def test_parse_nhl_games_real_sample_and_empty():
    payload = json.loads((SAMPLES / "nhl_stats_game_prev.json").read_text())
    df = H.parse_nhl_games(payload)
    assert len(df) == 5 and (df["last_period_type"] == "REG").all() and df["final"].all()
    assert (df["season"] == 2025).all() and df.iloc[0]["home_abbrev"] == "FLA" and df.iloc[0]["away_abbrev"] == "CHI"
    assert df.iloc[0]["home_win"] and df.iloc[0]["total"] == 5
    empty = H.parse_nhl_games({"data": []})
    assert empty.empty and list(empty.columns) == H.NHL_GAME_COLUMNS
    # unknown team id does not drop the row
    weird = H.parse_nhl_games([{"id": 2025020999, "gameDate": "2025-11-01", "homeTeamId": 999, "visitingTeamId": 10, "gameStateId": 7,
                                "homeScore": 1, "visitingScore": 2, "period": 3, "gameType": 2, "season": 20252026}])
    assert len(weird) == 1 and weird.iloc[0]["home_abbrev"] is None and weird.iloc[0]["away_abbrev"] == "TOR"


def test_run_history_writes_parquet_and_manifest(tmp_path: Path, monkeypatch, games, mp_csv):
    calls = install_fake_fetch(monkeypatch, games, mp_csv)
    out = tmp_path / "history"
    manifest = H.run_history(out, [2023, 2024])
    assert calls == {"moneypuck": 1, "nhl": 4}
    assert manifest["n_errors"] == 0 and manifest["errors"] == []
    assert manifest["schema_version"] == H.SCHEMA_VERSION and manifest["seasons_requested"] == [2023, 2024]
    mp = manifest["moneypuck"]
    assert mp["source_url"] == H.MONEYPUCK_ALL_TEAMS_URL and mp["sha256"] == H.sha256_hex(mp_csv.encode("utf-8"))
    assert mp["retrieved_at_utc"] == "2026-01-01T00:00:00Z" and mp["situations_kept"] == list(H.KEEP_SITUATIONS)
    for s in (2023, 2024):
        assert H.moneypuck_path(out, s).exists() and H.nhl_path(out, s).exists()
        ms = mp["seasons"][str(s)]
        assert ms["rows"] == 31 * 2 * 4 and ms["games"] == 31 and ms["teams"] == 3 and ms["unresolved_abbrevs"] == {}
        assert ms["n_regular_team_games"] == 60 and ms["n_playoff_team_games"] == 2
        ns = manifest["nhl"]["seasons"][str(s)]
        assert ns["rows"] == 31 and ns["n_final"] == 31 and ns["game_types"] == {"2": 30, "3": 1}
        assert set(ns["fetches"]) == {"2", "3"} and all("sha256" in f and "url" in f for f in ns["fetches"].values())
    assert json.loads(H.manifest_path(out).read_text())["generated_at_utc"].endswith("Z")
    # loaders round-trip
    tg = H.load_team_games(out)
    ng = H.load_nhl_games(out)
    assert len(tg) == 2 * 31 * 2 * 4 and set(tg["season"]) == {2023, 2024}
    assert len(ng) == 62 and set(ng["season"]) == {2023, 2024}
    assert len(H.load_team_games(out, [2024])) == 31 * 2 * 4
    assert ng["home_score"].dtype.name == "Int64" and ng["final"].dtype == bool
    # a second run for one season keeps the other season's manifest entry
    manifest2 = H.run_history(out, [2024])
    assert set(manifest2["moneypuck"]["seasons"]) == {"2023", "2024"} and manifest2["seasons_requested"] == [2024]


def test_run_history_records_errors_without_losing_other_source(tmp_path: Path, monkeypatch, games, mp_csv):
    install_fake_fetch(monkeypatch, games, mp_csv, fail_moneypuck=True)
    out = tmp_path / "history"
    manifest = H.run_history(out, [2024])
    assert manifest["n_errors"] == 1 and manifest["errors"][0]["source"] == "moneypuck"
    assert "simulated MoneyPuck outage" in manifest["errors"][0]["error"]
    assert not H.moneypuck_path(out, 2024).exists() and H.nhl_path(out, 2024).exists()
    assert H.load_team_games(out).empty and len(H.load_nhl_games(out)) == 31
    # a season absent from the CSV is an error too, other seasons still written
    install_fake_fetch(monkeypatch, games, mp_csv)
    manifest = H.run_history(out, [2024, 2025], do_nhl=False)
    assert any(e.get("season") == 2025 for e in manifest["errors"]) and H.moneypuck_path(out, 2024).exists()


def test_cli_main(tmp_path: Path, monkeypatch, games, mp_csv, capsys):
    install_fake_fetch(monkeypatch, games, mp_csv)
    out = tmp_path / "h"
    rc = H.main(["--out", str(out), "--seasons", "2023,2024"])
    assert rc == 0
    printed = json.loads(capsys.readouterr().out)
    assert printed["n_errors"] == 0 and printed["seasons_requested"] == [2023, 2024]
    assert H.main(["--out", str(out), "--seasons", "2024", "--skip-nhl"]) == 0
    install_fake_fetch(monkeypatch, games, mp_csv, fail_moneypuck=True)
    assert H.main(["--out", str(out), "--seasons", "2024", "--skip-nhl"]) == 1


def test_parquet_roundtrip_preserves_nullable_ids(tmp_path: Path, mp_csv):
    df = H.parse_moneypuck_csv(mp_csv + mp_csv.splitlines()[1].replace("TOR", "ZZZ", 1) + "\n")
    p = tmp_path / "x.parquet"
    H.write_parquet(df, p)
    back = H.read_parquet(p)
    assert back["team_id"].isna().sum() == 1 and back["team_id"].dtype.name == "Int64"
    pd.testing.assert_frame_equal(back[["game_id", "mp_team", "situation"]], df[["game_id", "mp_team", "situation"]])
