"""NHL lineup-publication probe: schedule of polls, no retroactive polling, change detection, summary."""

from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta
from pathlib import Path

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
    clock, log = Clock(START - timedelta(minutes=200)), []
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
    clock, log = Clock(START - timedelta(minutes=50)), []              # the run starts at T-50: offsets 180, 120, 90, 75 and 60 are in the past
    rep = P.watch(tmp_path, "2026-10-25", get=make_get(clock, log), now_fn=clock.now, sleep_fn=clock.sleep, tick_s=30)
    rows = P.load_obs(tmp_path)
    assert rep["skipped_late"] == 5 and {r["offset_min"] for r in rows} == {45, 30, 20, 12, 8, 5}
    assert all(r["lead_min"] <= 50 for r in rows)


def test_raw_bodies_are_stored_only_when_the_content_changes_and_files_are_write_once(tmp_path):
    clock, log = Clock(START - timedelta(minutes=200)), []
    P.watch(tmp_path, "2026-10-25", get=make_get(clock, log), now_fn=clock.now, sleep_fn=clock.sleep, tick_s=30)
    import gzip
    raws = []
    for f in sorted((tmp_path / "raw").rglob("*.jsonl.gz")):
        raws += [json.loads(line) for line in gzip.open(f, "rt")]
    assert sum(1 for r in raws if r["endpoint"] == "right-rail") == 2 and sum(1 for r in raws if r["endpoint"] == "landing") == 1
    assert LCR_guard_ok(tmp_path)


def LCR_guard_ok(out: Path) -> bool:
    manifest = [json.loads(line) for line in (out / "MANIFEST.jsonl").read_text().splitlines()]
    return all((out / m["path"]).exists() for m in manifest)


def test_interesting_finds_lineup_like_structures_and_ids():
    j = {"gameInfo": {"homeTeam": {"scratches": [{"id": 7}, {"id": 9}], "headCoach": {"default": "x"}}}, "lineup": {}, "other": [1]}
    f = P.interesting(j)
    assert f["gameInfo.homeTeam.scratches"] == {"n": 2, "ids": [7, 9]} and f["lineup"]["n"] == 0
