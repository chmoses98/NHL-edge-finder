"""Season rollover: the NHL pipeline must not be pinned to 2026-27.

A season is named by its start year and its game ids begin with that year. The loader reads archive-only seasons (2026 onward)
from the data-archive, so a new season needs no code change: it must appear in the default season set, be merged from the
archive, and must not leak into a frame that asked for earlier seasons.
"""
import os
import sys
from datetime import date, datetime

import pandas as pd
import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from nhl import data  # noqa: E402


@pytest.mark.parametrize("day,season", [
    (date(2026, 9, 30), 2026), (date(2026, 10, 17), 2026), (date(2026, 12, 31), 2026), (date(2027, 1, 1), 2026),
    (date(2027, 6, 30), 2026), (date(2027, 8, 31), 2026),          # offseason: still 2026-27 until September
    (date(2027, 9, 1), 2027), (date(2027, 10, 12), 2027), (date(2028, 4, 1), 2027), (date(2028, 10, 1), 2028),
    (datetime(2031, 11, 5, 3, 0), 2031),
])
def test_current_season_follows_the_calendar(day, season):
    assert data.current_season(day) == season


def test_default_season_set_is_contiguous_and_never_shorter_than_the_study():
    assert data.SEASONS[0] == data.FIRST_SEASON and data.SEASONS == list(range(data.FIRST_SEASON, data.SEASONS[-1] + 1))
    assert data.SEASONS[-1] >= 2026
    assert data.seasons_through(2029) == [2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029]


def test_the_frozen_study_keeps_its_own_season_set():
    assert data.STUDY_SEASONS == (2021, 2022, 2023, 2024, 2025, 2026)
    import nhl.run_walkforward as W
    assert W.SPLIT_SEASONS == {"development": [2022], "validation": [2023], "holdout": [2024, 2025], "prospective": [2026]}


def _archive(games):
    rows = [{"game_id": g, "player_id": 100 + i, "game_date": d, "game_type": 2, "season": g // 1_000_000, "_observed_at_utc": "x"}
            for i, (g, d) in enumerate(games)]
    return pd.DataFrame(rows)


@pytest.fixture
def archive(monkeypatch, tmp_path):
    games = [(2026020001, "2026-10-08"), (2027020001, "2027-10-07"), (2028020001, "2028-10-05")]
    monkeypatch.setattr(data, "HIST", tmp_path)                      # no committed parquet at all
    monkeypatch.setattr(data, "_read_archive", lambda kind: _archive(games))
    monkeypatch.setattr(data, "EXTRA", {})
    data.load_kind.cache_clear()
    yield
    data.load_kind.cache_clear()


def _ids(seasons=None):
    return sorted(data.load_kind("players", seasons)["game_id"].tolist())


def test_a_new_season_is_merged_from_the_archive_without_a_code_change(archive, monkeypatch):
    # asked for explicitly
    assert _ids((2026, 2027)) == [2026020001, 2027020001]
    # and through the default set once the calendar reaches it
    monkeypatch.setattr(data, "SEASONS", data.seasons_through(2027))
    data.load_kind.cache_clear()
    assert _ids() == [2026020001, 2027020001]
    monkeypatch.setattr(data, "SEASONS", data.seasons_through(2028))
    data.load_kind.cache_clear()
    assert _ids() == [2026020001, 2027020001, 2028020001]


def test_a_frame_for_earlier_seasons_does_not_gain_later_games(archive):
    assert _ids((2026,)) == [2026020001]
    assert _ids(tuple(data.STUDY_SEASONS)) == [2026020001]            # the frozen study never sees 2027 or 2028


def test_seasons_before_the_archive_never_read_it(archive, monkeypatch):
    called = []
    monkeypatch.setattr(data, "_read_archive", lambda kind: called.append(kind) or _archive([(2026020001, "2026-10-08")]))
    data.load_kind.cache_clear()
    data.load_kind("players", (2021, 2022, 2023, 2024, 2025))
    assert called == []


def test_default_argument_is_resolved_at_call_time_not_import_time(monkeypatch):
    monkeypatch.setattr(data, "SEASONS", data.seasons_through(2030))
    assert data._seasons(None) == tuple(range(2021, 2031))
    assert data._seasons([2024]) == (2024,)
    import inspect
    for fn in (data.load_kind.__wrapped__, data.shot_frame, data.team_games, data.skater_games, data.goalie_games):
        assert inspect.signature(fn).parameters["seasons"].default is None
