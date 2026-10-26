"""NHL lineup-publication probe: schedule of polls, no retroactive polling, change detection, summary."""

from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta

from nhl_edge.research import nhl_lineup_probe as P

START = datetime(2026, 10, 25, 23, 0, tzinfo=UTC)
SCHED = {"gameWeek": [{"date": "2026-10-25", "games": [{"id": 2026020180, "gameType": 2, "startTimeUTC": "2026-10-25T23:00:00Z", "season": 20262027},
                                                      {"id": 2026020181, "gameType": 1, "startTimeUTC": "2026-10-25T23:00:00Z"}]}]}


class Clock:
    def __init__(self, t: datetime) -> None:
        self.t = t

    def now(self) -> datetime:
        return self.t

    def sleep(self, s: float) -> None:
        self.t += timedelta(seconds=s)


def make_get(clock: Clock, log: list):
    def get(url: str):
        log.append((url, clock.t))
        if "/schedule/" in url:
            return 200, json.dumps(SCHED).encode()
        lead = (START - clock.t).total_seconds() / 60
        if url.endswith("right-rail"):
            scratches = [{"playerId": 1}, {"playerId": 2}] if lead <= 75 else []
            return 200, json.dumps({"gameInfo": {"homeTeam": {"scratches": scratches}, "awayTeam": {"scratches": []}}}).encode()
        return 200, json.dumps({"gameState": "FUT", "matchup": {"skaterSeasonStats": [1, 2, 3]}}).encode()
    return get


def test_polls_each_regular_game_at_the_registered_offsets_and_records_first_publication(tmp_path):
    clock, log = Clock(START - timedelta(minutes=140)), []
    rep = P.watch(tmp_path, "2026-10-25", get=make_get(clock, log), now_fn=clock.now, sleep_fn=clock.sleep, tick_s=30)
    assert rep["games"] == 1 and rep["skipped_late"] == 0 and rep["polls"] == len(P.OFFSETS_MIN)             # the preseason game is not probed
    assert not any("2026020181" in u for u, _ in log)
    rows = P.load_obs(tmp_path)
    rr = [r for r in rows if r["endpoint"] == "right-rail"]
    assert len(rr) == len(P.OFFSETS_MIN) and all(abs(r["lead_min"] - r["offset_min"]) <= 1.0 for r in rr)       # each poll happened at its offset
    s = P.summarize(rows)
    row = next(x for x in s["per_game_endpoint"] if x["endpoint"] == "right-rail")
    first = row["first_nonempty_lead_min"]["gameInfo.homeTeam.scratches"]
    assert 74 <= first <= 75 and row["changed_after_first_nonempty"] is True                                   # empty until T-75, then populated
    assert "gameInfo.awayTeam.scratches" not in row["first_nonempty_lead_min"]
    assert "first non-empty" in P.render(s)


def test_an_offset_that_is_already_late_is_skipped_not_polled_retroactively(tmp_path):
    clock, log = Clock(START - timedelta(minutes=50)), []              # the run starts at T-50: offsets 120, 90, 75 and 60 are in the past
    rep = P.watch(tmp_path, "2026-10-25", get=make_get(clock, log), now_fn=clock.now, sleep_fn=clock.sleep, tick_s=30)
    rows = P.load_obs(tmp_path)
    polled = [r for r in rows if r["endpoint"] != "skipped_late"]
    assert rep["skipped_late"] == 4 and {r["offset_min"] for r in polled} == {45, 30, 20, 12, 8, 5}
    assert all(r["lead_min"] <= 50 for r in polled)
    assert {r["offset_min"] for r in rows if r["endpoint"] == "skipped_late"} == {120, 90, 75, 60}           # the gap is visible in the data, not only in the log


def test_raw_bodies_are_not_stored_by_default(tmp_path):
    clock, log = Clock(START - timedelta(minutes=140)), []
    P.watch(tmp_path, "2026-10-25", get=make_get(clock, log), now_fn=clock.now, sleep_fn=clock.sleep, tick_s=30)
    assert not (tmp_path / "raw").exists() and P.load_obs(tmp_path)


def test_raw_bodies_are_stored_only_when_the_content_changes_and_files_are_write_once(tmp_path):
    clock, log = Clock(START - timedelta(minutes=140)), []
    P.watch(tmp_path, "2026-10-25", get=make_get(clock, log), now_fn=clock.now, sleep_fn=clock.sleep, tick_s=30, store_raw=True)
    import gzip
    raws = []
    for f in sorted((tmp_path / "raw").rglob("*.jsonl.gz")):
        raws += [json.loads(line) for line in gzip.open(f, "rt")]
    assert sum(1 for r in raws if r["endpoint"] == "right-rail") == 2 and sum(1 for r in raws if r["endpoint"] == "landing") == 1
    manifest = [json.loads(line) for line in (tmp_path / "MANIFEST.run.jsonl").read_text().splitlines()]
    assert manifest and all((tmp_path / m["path"]).exists() for m in manifest)
    import pytest
    with pytest.raises(FileExistsError):
        P.write_once(tmp_path, "run", manifest[0]["path"], [{}])


def test_parallel_runs_write_their_own_manifests_and_never_the_same_file(tmp_path):
    for tag in ("A", "B"):
        clock, log = Clock(START - timedelta(minutes=140)), []
        P.watch(tmp_path, "2026-10-25", get=make_get(clock, log), now_fn=clock.now, sleep_fn=clock.sleep, tag=tag)
    assert (tmp_path / "MANIFEST.A.jsonl").exists() and (tmp_path / "MANIFEST.B.jsonl").exists() and not (tmp_path / "MANIFEST.jsonl").exists()
    assert len(P.load_obs(tmp_path)) == 2 * 2 * len(P.OFFSETS_MIN)


def test_the_window_filter_selects_games_and_an_empty_selection_or_unreadable_schedule_fails_loudly(tmp_path):
    import pytest
    clock, log = Clock(START - timedelta(minutes=140)), []
    with pytest.raises(RuntimeError, match="no regular-season game"):
        P.watch(tmp_path, "2026-10-25", get=make_get(clock, log), now_fn=clock.now, sleep_fn=clock.sleep, start_from=START + timedelta(hours=1))
    with pytest.raises(RuntimeError, match="HTTP 503"):
        P.watch(tmp_path, "2026-10-25", get=lambda u: (503, b""), now_fn=clock.now, sleep_fn=lambda s: None)
    with pytest.raises(RuntimeError, match="not json"):
        P.watch(tmp_path, "2026-10-25", get=lambda u: (200, b"<html>"), now_fn=clock.now, sleep_fn=lambda s: None)


def test_timestamps_are_taken_when_the_response_arrives_even_if_requests_are_slow(tmp_path):
    clock = Clock(START - timedelta(minutes=140))
    base = make_get(clock, [])

    def slow(url):
        clock.t += timedelta(seconds=20)                              # every request takes 20 s
        return base(url)
    P.watch(tmp_path, "2026-10-25", get=slow, now_fn=clock.now, sleep_fn=clock.sleep)
    rows = [r for r in P.load_obs(tmp_path) if r["endpoint"] == "right-rail"]
    assert all(r["lead_min"] <= r["offset_min"] + 0.01 for r in rows)                  # never stamped earlier than the real moment (lead only shrinks)
    assert len({r["polled_at_utc"] for r in rows}) == len(rows)


def test_interesting_finds_lineup_like_structures_and_ids():
    j = {"gameInfo": {"homeTeam": {"scratches": [{"id": 7}, {"id": 9}], "headCoach": {"default": "x"}}}, "lineup": {}, "other": [1]}
    f = P.interesting(j)
    assert f["gameInfo.homeTeam.scratches"] == {"n": 2, "ids": [7, 9]} and f["lineup"]["n"] == 0
