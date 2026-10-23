# Projection delivery: audit, architecture, and what is (and is not) guaranteed

> RESEARCH_ONLY. Nothing here changes a model, price, stake, cap, recommendation or contract. All timestamps UTC. Evidence: GitHub Actions run and job records for `projection-foundation`, `capture-worker` and `slate-watch` (2026-10-20 … 2026-10-23), and the immutable archives (`docs/research/slates/2026-10-22_snapshot_audit.md`).

## 1. What was measured (2026-10-22)

| observation | evidence | consequence |
|---|---|---|
| Cron slots arrive hours late. Matching the day's eight scheduled runs to the eight cron entries in order, the pregame slots were created 2.2–4.4 h after their cron time (14:07 → 18:28, 15:07 → 19:08, 20:07 → 23:16, 21:07 → 23:56, 22:07 → 00:30, 23:07 → 01:22) and the two settle slots (10:37, 11:37) at 15:36 and 15:59; the mapping is inferred from the run times. | run `created_at` vs the cron expression | A cron-driven "pregame" slot can arrive after the puck drop it was meant to precede. Cron cannot be the primary trigger. |
| Each run needed **two** runner requests (`gate`, then `live`). Run 51 (manual dispatch 21:27:53): `gate` created 21:27:53, started **22:18:38 (51 min)**; `live` created 22:18:41, started **22:40:48 (22 min)**; the chain itself ran **5.4 min**. Run 50: `gate` waited **78 min** (19:25:47 → 20:43:24) and then decided "no-op". | job `created_at` / `started_at` | 73 of 79 minutes were queue time, and the extra `gate` hop doubled the exposure to it. |
| The EDT/EST duplicate of every slot started a no-op run. | `gate` jobs that skipped `live` | Extra runner requests at the worst time, and a no-op *pending* run replaces a real pending run in a shared concurrency group (GitHub keeps one running + one pending; a newer pending run cancels the older). |
| Normal days are fast: runs on 10-20 and 10-21 took 5–10 min end to end. | runs 28–42 | The platform incident is real but not the steady state; the design must degrade, not assume the incident. |
| The capture-worker handover at 21:08Z waited 23 min for a runner (last capture 20:48 → first 21:39). | handoff note, `STATUS_worker`, run 358 | Single point of delay; mitigated, not removable (a successor needs a runner). Pregame jobs run inside the worker, so only the *player layer* depends on dispatch. |
| `latest.json` is rewritten only when content changed; forecast rows are written only when changed. | `publish_stage`, `forecasts/` | "File timestamp" is not freshness. The platform's run record (and the run report) is the freshness source. |

## 2. Architecture (this change)

**Primary: the capture worker asks.** `worker/pf_dispatch.py` (stdlib only) runs inside every worker cycle, never blocks it, and never raises into it. Policy (all in `decide`, pure and unit-tested):

* nothing is wanted more than 9 h before the next puck drop;
* otherwise a run is wanted when the newest *successful* run's data is older than 180 / 90 / 45 / 25 min at T-9…6 h / 6…3 h / 3…1.5 h / < 1.5 h;
* **never dispatch while a run is queued or in progress** (a second pending run replaces the first and loses its place in the runner queue — the definition of "a cancelled run that worsens queue delays"); a run "in flight" for more than 6 h is treated as lost;
* at most one dispatch per 12 min and 18 per 24 h, counted from the platform's own record (so a restarted worker cannot double-count);
* a request that cannot finish before the puck drop (lead = 8 min runtime + min(median observed request-to-completion, 20 min), at least 15 min) is not made: the previous run is the final one;
* one settle-oriented run (`capture,results,settle,score,guard`) 3.75 h after the last start of a slate, unless a later run already covers it;
* an unreadable run list means *no* dispatch (never blind).

**Second: `slate-watch` asks too** (every 30 min on game days, `actions: write` only for this dispatch) with the same policy, so a dead worker does not silence the player layer. It also opens **one** de-duplicated issue, "NHL projection delivery late", when a puck drop is within 90 min, nothing is in flight and the newest successful run is older than 4 h (or absent); it closes it on recovery.

**Third: cron** (`projection-foundation.yml`) is a fallback only: 11 UTC slots a day, no DST duplicates, own concurrency group (`…-cron`), and a **gate step inside the single job** — a cron run asks the same policy (excluding itself) and exits in about a minute when nothing is due; explicit requests (worker, watchdog, human, PR dry run) always run. The `gate` job, and with it one runner request per run, is gone. If the gate itself cannot decide, the chain runs (it is idempotent: forecasts are write-once, `ci_publish.sh` re-applies on a moved remote, `archive_guard` runs before and after).

**Idempotency and duplicates.** The three triggers share one decision function and the platform's run list; the worker and watchdog dispatch into one concurrency group (one running + one pending), cron into another, so a fallback can never cancel a worker request. Re-running the chain cannot rewrite history: forecast files are additions, unchanged rows are skipped, late rows are rejected (`late_rejected`), and `archive_guard` blocks any change to an immutable path.

**What is observable.** Every worker cycle records the decision (`pf` in `STATUS_worker.json` cycles: action, code, hours to tip, last-success age, median request-to-completion). Run titles carry the event and stages (`run-name`). Slate-watch writes the decision JSON to its job summary.

## 3. What this does and does not guarantee

* **Does:** a refresh is *requested* at the right horizon without cron; at most one is queued at a time; a missing worker, a missing cron and an API hiccup each fall back to something else; a late delivery is visible in one issue.
* **Does not:** make GitHub runners start sooner. A requested run can still wait 20–80 min on a bad day (as on 10-22). The design therefore requests early (the 25-minute cadence inside 1.5 h means a request is already in flight when the last useful moment arrives) and treats the previous successful run as the final pregame snapshot when a late one cannot finish. Games whose last run is older than the lineup news (official dressed rosters appear ~20–60 min before the drop) will show older inputs; the audit labels this rather than hiding it.
* **Not done here (next, higher risk):** running the projection chain *inside* the worker process would remove the runner-queue dependency entirely (the chain took 0.6 min with a cached model table and 5.4 min when it had to compute one), at the cost of a second Python (3.13), the PF requirements and a model-table cache inside the production capture job. It is left as a separate, flagged change because it puts a heavy job in the production capture loop.

## 4. Rollback

`NHL_EDGE_PF_DISPATCH=0` in the worker environment disables the worker's dispatching without a deploy; removing the two steps from `slate_watch.yml` disables the second trigger; reverting this change restores the previous workflow. No data format changed.
