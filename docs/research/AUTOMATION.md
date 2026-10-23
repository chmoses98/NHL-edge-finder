# Hands-off research automation (RESEARCH_ONLY)

No keys, no witnesses, no manual approvals, no recurring owner task. Everything below runs on existing GitHub infrastructure with the job token only; none of it can reach a price, stake, cap, order or SIFT contract.

| capability | mechanism | cadence | alerts |
|---|---|---|---|
| Collect & validate pregame snapshots | `capture_worker` (Kalshi board/depth, context: schedule, goalies, lines, injuries) + `projection-foundation` capture | every 5–15 min / hourly→20 min in the last 3 h | worker health state `DEGRADED`/`FAILED` in `STATUS_worker.json` |
| Produce projections before games | worker `simulate` (V1 + V2/PLAYER_SIM shadows, scripts, packet); `projection-foundation` project/publish | hourly→20 min in the last 3 h | `slate-watch` |
| Record version + timestamp | every prediction row carries `model_version`, `sim_version`, `feature_version`, `predicted_at_utc`, `data_cutoff_utc`, input snapshot ids, market state; archive manifest has sha256 per file | each run | archive guard |
| Settle completed games | worker `settle` (official finals; regulation vs OT/SO semantics); `projection-foundation` results/settle | after games, backlog 72 h | `research-weekly` (`SETTLE_PROBLEM`) |
| Evaluate vs outcomes and market | worker `evaluate` -> `eval/report*.json` (V1 / market / market-anchored / PLAYER_SIM by family) | after settlement, never inside the last 3 h before puck drop | `research-weekly` |
| Rolling calibration and proper scores | the same reports + `research-weekly` scoreboard; walk-forward tools for history | daily summary, 90-day retention Mondays/1st (= weekly/monthly summaries) | `CALIBRATION_COLLAPSE` only on large samples |
| Missing data, stale forecasts, pipeline failures | `slate-watch` (pregame, per game) and `research-weekly` (heartbeats, failed evaluate steps) | every 30 min on game days / daily | **one de-duplicated issue**, closed on recovery |
| Challengers: controlled retrain / test | historical: `oa_walk_forward` / `oa_evaluate` + `promotion.py` (run via workflow dispatch on a runner with network); live: shadow arms recorded by the production pipeline | on demand / after each preregistration | promotion decisions are PRs, never silent |
| Weekly & monthly summaries | `research-weekly` artifact (`summary.md`, `alerts.json`) | Mondays and the 1st | none unless an integrity alert |

## What alerts and what never does

* **Alerts (issue):** slate NOT_READY with a puck drop inside 4 h; stale/failed heartbeat; settlement errors/disagreements; failed evaluation step; calibration collapse (ECE > 0.15 on ≥ 5,000 contracts); projection-scorecard `ALERT`.
* **Never alerts:** a goalie still unconfirmed (DEGRADED), the market beating V1, a challenger not qualifying. Those are findings in the summary.

## Known platform risk (observed 2026-10-22)

GitHub delayed *scheduled* workflow runs by up to ~5 hours that day (the 06:37 ET settle slot of `projection-foundation` ran at ~11:45 ET) and runner start-up queues were long. The continuous `capture_worker` is unaffected once running, but anything driven by a cron slot is best-effort. Mitigations in place: horizon-aware conductor decisions rather than wall-clock slots, `workflow_dispatch` for every job, and `slate-watch` surfacing staleness. Not solved: the `projection-foundation` pregame slots are still cron-driven.

## Rollback

Each workflow is read-only; disable it in the Actions tab or delete the file. Reverting the PR removes everything. The dormant sealed-ledger workflows are untouched.

## Projection-foundation delivery (2026-10-23)

Audit of the last 40 scheduled `projection-foundation` runs (2026-10-18 … 10-22): every cron slot fired **2–6.5 h late** (median 3 h 18 min; 20 of 20 real-work slots > 30 min late); no slot was omitted. On 2026-10-22 only the 14:07 Z-slot refresh finished before the first puck drop (23:00 Z); the 20:07 Z and 22:07 Z slots finished 01:29 and 02:06 *after* it. The workflow-level concurrency group also made the four gate-only cron entries per day (which do no work) compete for the single pending slot, queueing real refreshes behind them or cancelling a pending one.

Changes (all operational, no model or betting change):

* **Worker-driven refresh** (`worker/pf.py`, called once per capture cycle): if the published `projection-data` tip is older than the allowed age for the next reachable puck drop (≤ 90 min away: 40 min; ≤ 3 h: 75 min; ≤ 6 h: 150 min) the worker dispatches the same workflow (`stages=all`, live). Freshness is the commit time of `projection-data`, not run metadata; nothing is dispatched while a run is executing or a dispatched run is queued, within 15 min of the last run, or after 8 dispatches/day; API failures are recorded and never stop capture. Kill-switch `NHL_EDGE_PF_DISPATCH=0`. Cron slots remain as the backstop.
* **Watchdog**: queued > 45 min, running > 90 min, or a publication older than 2 h within the hour before a puck drop appear as `pf` alerts in each cycle record and degrade (never fail) the worker health verdict.
* **Concurrency**: the workflow-level group is now per-run; serialisation moved to the `live` job so gate-only runs can no longer occupy or cancel the pending refresh.
