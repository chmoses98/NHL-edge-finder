# Pregame forecast delivery monitoring (RESEARCH_ONLY, read-only)

## What is alerted, and what is not
The projection-foundation archive writes a player-forecast row **only when its content changed**. "No new row for hours" is therefore normal when nothing changed, and an alert on it would be noise. The monitor (`research/delivery_monitor.py`, run by `slate-watch` every 30 min on game days) judges only games that start within **90 minutes** and raises **one de-duplicated issue** ("NHL pregame forecast missing or stale") only for:

| status | meaning | limit |
|---|---|---|
| `MISSING` | no pregame forecast row exists for the game (archived at or before now, and before its own start) | — |
| `STALE_EVAL` | the newest projection run that *evaluated* the game (`runs/nhl/…_project.json`, whether or not it changed a value) is too old | 120 min |
| `STALE_LINEUP` | the lineup capture that evaluation used was too old when it ran | 60 min |

It closes itself when every judged game is `OK`. A forecast whose values did not change but which was re-evaluated minutes ago is `OK` by construction.

## Validation by replay (real archive, slate of 2026-10-23)
| replay instant | games judged | result |
|---|---|---|
| 22:50Z | 1 (70 min to drop) | OK — evaluated 2.9 min earlier, lineup capture 8.2 min old; newest forecast *row* 183 min old (unchanged values) |
| 23:30Z | 2 | OK — evaluated 9.2 min earlier, lineup 13.8 min old; rows 223 min old |
| 00:30Z | 1 | OK — evaluated 13.1 min earlier, lineup 16.9 min old; rows 283 min old |
A rule based on the age of the newest *row* would have alerted at each of these instants although delivery was healthy.

## What is recorded over time
* Every `research-weekly` run (daily) writes the **delivery timeline of the last ET game day** to the job summary and its artifact: for every projection-foundation refresh, request time, runner start, completion, publication commit, request→runner and request→publication latency, minutes from publication to the next puck drop and how many games had already started (`research/delivery_timeline.py`; first full-slate result: `slates/2026-10-23_delivery_verification.md`).
* `slate-watch` writes the per-game monitor statuses (evaluation age, lineup age at evaluation, number and age of pregame rows) to its job summary every half hour.
* Fallback behaviour: a cron fallback run that finds nothing due cancels itself and is listed as `cancelled` in the timeline (not counted as a refresh); the previous published snapshot is what is served until the next publication, and the timeline's "publication → next drop" column shows how old it was.

## Whole-cycle runtime (operational metric, not a promotion gate)
The capture worker's whole-cycle duration (`STATUS_worker.json` `cycles[].duration_s`, per-job list in `jobs_run`) is tracked as an end-to-end delivery metric. The registered G7 proxy result is preserved as recorded: 655 `simulate` cycles since 2026-09-29, median 127 s, p95 1,081 s, max 1,539 s, 17 % over 300 s. That does **not** pass the 300 s threshold, which applies only to V2 *inference time per slate* (≈ 34 s, passed; `docs/research/overtime_promotion/OWNER_DECISION_G7.md`). Do not read the one as evidence about the other.

## Limits
Alerts are only as timely as `slate-watch`'s own schedule (GitHub delivered scheduled runs hours late on 2026-10-22), which is why the capture worker also records its own dispatch decisions each cycle (`pf`, `lc` fields of `STATUS_worker.json`). The monitor cannot make a runner start sooner; it makes a real gap visible while there is still time to act.
