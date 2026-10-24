# WORKLOAD_V1_LC prospective collection — does it run before puck drop? (audit and hardening, 2026-10-24)

RESEARCH_ONLY. The registered test (`LC_PROSPECTIVE_REGISTRATION.md` + Amendment 1) is **unchanged**: 30,000 paired player-games at the decision look, 60,000 at the final, the original seven-check rule, no back-filling. This page audits whether the *collection* that feeds it actually executes before each drop and adds unattended dispatch and a coverage alert for the case where it does not.

## What was measured (live, since activation 2026-10-23T20:58:20Z)
| fact | value |
|---|---|
| Regular-season games on the schedule since activation | 66 (2 started, 64 pending at the time of the audit) |
| Started games with a countable pregame record | **2 of 2** (lead before the drop 241.7 and 181.7 min; registered minimum 10 min) |
| Runs so far | 2 `workflow_dispatch` runs (20:51Z → records written 20:58:23Z, 22:21Z → nothing to add); both succeeded, 7 min each (queue + run) |
| Scheduled (cron) runs delivered | **0 so far** — the first slot after the merge (08:23Z) had not yet arrived at the time of writing. GitHub delivered this repository's other cron workflows 2–6.5 h late on 2026-10-22 (`PROJECTION_DELIVERY.md`), and that is the reason cron alone is not trusted here |
| Games whose first eligible run would be after their drop under cron-only | not measurable yet; 10-24 has games at 17:00Z and 19:30Z, i.e. before the 13:23Z slot can be expected to arrive with a 2–6 h delay |

The collection did execute before the drop for every game that started, but both of those runs were **manual** dispatches. Nothing in the repository guaranteed a run for the next game.

## What changed (operational only; no model, record format, rule or threshold touched)
* **`worker/lc_dispatch.py`** — the same pattern as the projection-refresh dispatcher, driven by the platform's own run record: a game is *covered* by a queued/running/successful `workload_shadow` run that started inside its 14-hour horizon (and, once finished, ≥ 10 min before the drop). A run is requested when an **uncovered** game starts within **4 h** and ≥ 20 min ahead, nothing is in flight, spacing (12 min), a 24/day cap and a failure back-off allow. An unreadable run list means *no* dispatch (never blind). A lost run (in flight > 3 h) stops blocking.
* **Three triggers, one policy:** the capture worker (every 15-min cycle, fail-soft, `NHL_EDGE_LC_DISPATCH=0` disables), `slate-watch` (every 30 min on game days), and the cron slots (now four a day) as the fallback. Records are write-once and the job is idempotent, so two triggers cannot double-record a game.
* **Coverage alert on a real gap only:** `slate-watch` opens one de-duplicated issue *"NHL workload shadow collection gap"* when an uncovered game starts within 90 min and nothing is queued or running; it closes itself when every game within 90 min is covered. An unchanged prediction value is never an alert, and a missing record is **never back-filled**.
* **Ground-truth coverage in the scoreboard:** `coverage_audit` lists, for every regular-season game scheduled after activation, `recorded` / `pending` / `missed` with the lead time, and the coverage share of started games, median and shortest lead; it appears in `scoreboard/latest.{json,md}` after every run.

## Limits, stated plainly
* Dispatch can ask for a runner but cannot make one start sooner; a game whose request waits in the queue past its drop (the worst queue observed was 24 min on 2026-10-23) would be missed and listed as such. The 4-hour window leaves several attempts for that reason.
* The first uses of the new triggers happen after this merges; the worker picks up the change on its next handover.
