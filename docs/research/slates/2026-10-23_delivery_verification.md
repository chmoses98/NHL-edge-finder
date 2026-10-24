# Delivery verification — slate of 2026-10-23 (two games: 00:00Z and 01:00Z on 10-24)

RESEARCH_ONLY. Read-only evidence from GitHub's run/job records, `projection-data` commits and the immutable pregame snapshots. Nothing was changed. Tables: `2026-10-23_delivery_timeline.md/json` (every refresh), `2026-10-23_snapshot_audit.md/json` (what was genuinely available before each drop; the audit reads two UTC partitions, so it also lists the previous evening's tail and 10-24 games — only the two games above belong to this slate).

## Every projection refresh of the slate window (10-23 08:00Z → 10-24 08:00Z)

16 `projection-foundation` runs: **10 refreshes, all `workflow_dispatch` requests, all succeeded and all published a `projection-data` commit; 6 cron fallback runs, all of which cancelled themselves by design** (nothing was due; none is counted as a refresh).

| requested | runner start | published | request→runner (min) | request→published (min) | minutes before the next drop |
|---|---|---|---:|---:|---:|
| 15:11:27 | 15:14:49 | 15:18:03 | 3.4 | 6.6 | 522 |
| 18:05:49 | 18:06:37 | 18:08:04 | 0.8 | 2.2 | 352 |
| 19:39:33 | 19:46:23 | 19:47:48 | 6.8 | 8.2 | 252 |
| 21:07:48 | 21:14:34 | 21:15:53 | 6.8 | 8.1 | 164 |
| 21:58:53 | **22:22:57** | 22:24:00 | **24.1** | **25.1** | 96 |
| 22:45:52 | 22:45:57 | 22:47:25 | 0.1 | 1.6 | 73 |
| 23:13:52 | 23:19:35 | 23:21:03 | 5.7 | 7.2 | 39 |
| 23:44:54 | 23:45:49 | **23:47:17** | 0.9 | 2.4 | **12.7** (game 1) |
| 00:11:48 | 00:15:45 | 00:17:10 | 4.0 | 5.4 | 43 (game 2) |
| 00:41:03 | 00:41:07 | **00:42:16** | 0.1 | 1.2 | **17.7** (game 2) |

* **Dispatch → runner start:** median 3.7 min, maximum 24.1 min (one slow runner queue at 21:58Z). **Request → publication:** median 6.0 min, maximum 25.1 min. Chain duration after runner start: 1.1–1.6 min every time (cached model table).
* **Time to puck drop:** the last refresh before game 1 (00:00Z) published **12.7 min** before the drop; the last before game 2 (01:00Z) **17.7 min** before. Inside the last two hours refreshes were requested every 25–50 minutes, so even the 24-minute queue at 21:58Z did not leave a gap (the next request was already running at 22:45Z).
* **Failures:** none. Nothing to fix; no freshness or provenance check was touched or relaxed.
* Compared with 10-22 (audit in `PROJECTION_DELIVERY.md`: cron slots 2–6.5 h late, one of three pregame refreshes finished before the first drop), **every** refresh requested on 10-23 finished before its game.
* Not distinguishable from the run record: whether a given request came from the capture worker or from `slate-watch` (both dispatch as `github-actions[bot]` with the same inputs). The worker's own decision log is written to `STATUS_worker.json` at the end of its shift.

## What was actually available before each drop (snapshot audit)

| game | drop (UTC) | V1/V2 last pregame snapshot | goalies | PF last content-changing write (min before) | PF last evaluation (min before) | lineup capture age at that run |
|---|---|---|---|---|---|---|
| 2026020166 | 00:00 | 23:59:57 (0.1 min) | CONFIRMED / CONFIRMED | 252 | 13 | 12 min |
| 2026020167 | 01:00 | 00:48:09 (11.8 min) | CONFIRMED / CONFIRMED | 312 | 18 | 16 min |

* The core V1/V2 predictions (the live job) were refreshed to within 0.1 and 11.8 minutes of the drop with both goalies confirmed.
* The PF player forecasts are written only when their content changes: their last write is at 19:47Z, but the runs at 22:24, 22:47, 23:21, 23:47, 00:17 and 00:42 re-evaluated the games (lineup captures 8–17 minutes old) and found nothing to change. In those runs the participation counts did not move (`CONFIRMED_ACTIVE` 4, `LIKELY_ACTIVE` 69, `UNCERTAIN` 3 from 19:47Z to 23:47Z): the only confirmed players were the four goalies, i.e. no skater lineup confirmation reached the player layer before either drop. That is an input limitation of the lineup sources, not a delivery delay; I could not tell from these records whether an earlier source for skaters exists.
* No row was archived after its game started (`rows archived after start` = 0).

## Conclusion
The worker/slate-watch-driven refresh from #67 delivered on a full slate: ten requested, ten published, none late, last pregame refresh 12.7 and 17.7 minutes before the drops, worst platform queue 24 minutes. One slate is one sample; the unaddressed risk remains a runner queue longer than the interval between requests in the final 30 minutes (the design requests early and keeps the previous snapshot as the fallback; it cannot make a runner start sooner).
