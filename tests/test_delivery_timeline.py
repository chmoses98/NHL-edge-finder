from datetime import UTC, datetime

from nhl_edge.research import delivery_timeline as D


def _fake(path):
    if "/actions/workflows/" in path:
        return {
            "workflow_runs": [
                {
                    "id": 2,
                    "event": "workflow_dispatch",
                    "display_title": "projection-foundation workflow_dispatch [all]",
                    "conclusion": "success",
                    "created_at": "2026-10-23T18:05:49Z",
                    "updated_at": "2026-10-23T18:08:10Z",
                    "html_url": "u2",
                },
                {
                    "id": 1,
                    "event": "schedule",
                    "display_title": "projection-foundation schedule",
                    "conclusion": "cancelled",
                    "created_at": "2026-10-23T15:43:10Z",
                    "updated_at": "2026-10-23T15:47:34Z",
                    "html_url": "u1",
                },
                {
                    "id": 9,
                    "event": "pull_request",
                    "display_title": "x",
                    "conclusion": "success",
                    "created_at": "2026-10-23T16:00:00Z",
                    "updated_at": "2026-10-23T16:10:00Z",
                    "html_url": "u9",
                },
            ]
        }
    if path.startswith("repos/") and "/commits?" in path:
        return [
            {
                "sha": "a" * 40,
                "commit": {
                    "committer": {"date": "2026-10-23T18:08:04Z"},
                    "message": "NHL live shadow 2026-10-23T18:08Z (research_only)",
                },
            },
            {"sha": "b" * 40, "commit": {"committer": {"date": "2026-10-23T18:30:00Z"}, "message": "unrelated"}},
        ]
    if "/runs/2/jobs" in path:
        return {
            "jobs": [
                {
                    "name": "live",
                    "created_at": "2026-10-23T18:05:50Z",
                    "started_at": "2026-10-23T18:06:37Z",
                    "completed_at": "2026-10-23T18:08:09Z",
                    "steps": [
                        {
                            "name": "Run the chain",
                            "started_at": "2026-10-23T18:06:50Z",
                            "completed_at": "2026-10-23T18:07:40Z",
                            "conclusion": "success",
                        },
                        {
                            "name": "Commit to projection-data (only after every stage succeeded)",
                            "started_at": "2026-10-23T18:08:03Z",
                            "completed_at": "2026-10-23T18:08:05Z",
                            "conclusion": "success",
                        },
                    ],
                }
            ]
        }
    if "/runs/1/jobs" in path:
        return {
            "jobs": [
                {
                    "name": "live",
                    "created_at": "2026-10-23T15:43:11Z",
                    "started_at": "2026-10-23T15:47:16Z",
                    "completed_at": "2026-10-23T15:47:34Z",
                    "steps": [],
                }
            ]
        }
    raise AssertionError(path)


def test_timeline_matches_publication_to_run_and_measures_minutes_to_puck_drop():
    tl = D.collect("2026-10-23", _fake)
    assert [r["run_id"] for r in tl["runs"]] == [1, 2]  # pull_request runs are not refreshes
    gated, ok = tl["runs"]
    assert gated["publication"] is None and ok["publication"]["sha"] == "a" * 10
    D.attach_drops(tl, [datetime(2026, 10, 23, 23, 0, tzinfo=UTC), datetime(2026, 10, 23, 18, 0, tzinfo=UTC)])
    m = ok["minutes"]
    assert m["request_to_runner_start"] == 0.8 and m["request_to_publication"] == 2.2
    assert ok["games_already_started_at_publication"] == 1 and ok["publication_to_next_drop_min"] == 292.0
    assert "| 18:08:04 |" in D.markdown(tl)


def test_a_success_without_a_commit_is_not_credited_with_a_publication():
    def fake(path):
        r = _fake(path)
        if "/runs/2/jobs" in path:
            r["jobs"][0]["steps"][1]["conclusion"] = "skipped"
        return r

    assert D.collect("2026-10-23", fake)["runs"][1]["publication"] is None
