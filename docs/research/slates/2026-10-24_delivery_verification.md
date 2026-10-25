# Slate 2026-10-24 — delivery and collection verification (12 games, research only)

Sources: GitHub Actions run/job records, `projection-data` runs and forecasts, `data-archive`, the two prospective data branches. Full per-run table: `2026-10-24_delivery_timeline.md`.

## Projection refresh (projection-foundation)
- 20 runs, 18 successful publications, 2 cancelled by newer requests (by design). **Every one of the 12 games had a final pregame evaluation 18.5–47.7 minutes before its drop**, with the lineup capture used ≤ 19.6 minutes old at that evaluation (median 8.2). No game was missing or stale; no `NHL pregame forecast missing or stale` issue was raised.
- Runner queue (request → runner start): median 5.9 min, p90 17.7 min, **max 22.6 min**; request → publication: median 8.7 min, p90 19.9 min, max 27.1 min. Queues were longest late in the evening (17–19 min on the 23:22, 00:07 requests). The tightest margin for the large cluster was the 22:34:38 publication, 25.4 minutes before the seven 23:00 drops; the tightest overall was 18.5 minutes before the 17:00 drop (the 16:41:47 publication, queue 5.3 min).
- A forecast row is written only when values change, so the last forecast row for a game can be hours before the drop (e.g. 169–258 minutes for the late games) while its last *evaluation* was 33–48 minutes before it: this is the case the monitor deliberately does not alert on.

## Scheduled workflows vs the dispatch path
- Cron arrives late: `workload-shadow` ran 4h24m, 3h20m, 2h11m, 2h11m after its four slots (08:23, 13:23, 17:23, 20:23 UTC); `player-minutes` 4h22m, 3h18m, 2h10m, 2h09m after its slots; `slate-watch` and `projection-foundation` schedules likewise. Unattended coverage therefore depends on dispatch from the capture worker / `slate-watch`, whose decisions are in `STATUS_worker.json` (`cycles[].lc`).
- On 2026-10-24 the LC dispatcher never had to fire: the (late) 12:47Z cron run still preceded every eligible drop by ≥ 252 minutes, and every later worker cycle reported `OUTSIDE_WINDOW` with the next uncovered game ≥ 24 h away. The dispatch path was therefore exercised only in its "idle" branches on live data (and by unit tests); a live "dispatch" decision has not yet been observed.
- CI runners: pull-request and push runs queued 10–25 minutes at times during this period.

## Prospective collection (details: `2026-10-24_collection_verification.md`)
