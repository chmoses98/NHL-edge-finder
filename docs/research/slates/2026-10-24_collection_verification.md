# Prospective collection verification: slate 2026-10-24 (WORKLOAD_V1_LC and player-minutes-1.0; research only)

Checked on 2026-10-25 against the immutable data branches, their git history, GitHub run records, `STATUS_worker.json` and the archive. Frozen rules, samples and looks untouched.

## Coverage and timing (exact)
| | WORKLOAD_V1_LC | player-minutes-1.0 |
|---|---|---|
| activation | 2026-10-23T20:58:20Z | 2026-10-24T07:20:40Z |
| games eligible since activation (regular season, started) | 14 (2 on 10-23, 12 on 10-24) | 12 |
| games with a pregame record | **14 / 14** | **12 / 12** |
| games missed / retroactive / backfilled | 0 / 0 / 0 | 0 / 0 / 0 |
| records | 587 (84 + 503) | 503 |
| duplicate (game, player) rows; games recorded in more than one run | **0; 0** | **0; 0** |
| `pregame` flag | all true | all true |
| lead of the record before the drop (manifest write time) | 181.6 – 792.3 min (median ≈ 612) | 579 – 788 min (median 608.5) |
| git commit time of the first commit holding each game's records | 12:47:42Z for the 12 games (earliest drop 17:00Z); 20:58:25Z for the first two | 07:20:51Z (games 168, 169), 12:51:41Z (the other ten) |
| model fingerprint | `1eb5fd10…` (identical in both branches and in every record) | same |
| coverage-file errors, all runs | none (6 files) | none (5 files) |
| write-once guard | clean in every run | clean in every run |

No game was missed and no record was written after its drop; every record's `predicted_at_utc` matches its manifest write time to within seconds and its git commit.

## How the runs were triggered
All four LC runs and all four player-minutes runs on 10-24 were **cron (`schedule`) events, 2h09m – 4h24m after their slot**. The unattended-dispatch path (worker, `slate-watch`) never had to fire: the first, late, cron run was still ≥ 252 minutes before the earliest drop, and every worker cycle reported `OUTSIDE_WINDOW` with the next uncovered game ≥ 24 h away. The dispatch policy has therefore been exercised on live data only in its "idle" branches (plus unit tests); a live `dispatch` decision has not yet occurred. The player-minutes workflow's first run (07:20Z) was a manual dispatch to activate it.

## Comparisons (what the hypotheses need)
- **H1/LC incumbent forecasts** (PLAYER_SIM_V1 pregame forecast in `projection-data`): total-ice-time forecasts exist for **413 of 503** player-minutes candidates (82 %); among players who actually played in the settled games, 86 % in the first two games and **298 of 324 (92 %)** across the nine games settled by 03:00Z. LC: 362 of 386 dressed (94 %). A dressed player without an incumbent forecast is simply not paired (neither side is imputed).
- **H2 comparator (the incumbent's expected power-play minutes captured in the record)** exists for only **268 of 503 (53 %)** candidates, and for **none** in games 169, 177, 178, 179: the production engine prices those players later in the day than the record was written (records were made 10–13 hours before the drop). H2 as registered (captured at record time) will therefore accumulate roughly half the pairs it would with a last-pregame comparator, and not at all for games recorded before production priced them. Not changed (frozen). If wanted, a supplementary, clearly labelled descriptive comparison can use the last pre-drop `predictions_player` row computed offline from the immutable archive.
- **Candidate-set coverage:** in the two settled games with full shift data, 3 of 75 skaters who played were not candidates (4 %); not controllable and identical for LC and minutes.

## Settlement integrity
- The 22:41Z run settled games 168 and 169: 72 outcome rows, every `toi_s` and `toi_pp_s` equal to the archive's player events (0 mismatches), no zero-minute rows, candidates who did not play correctly have no outcome row, `settled_at_utc` stamped, outcome files listed in the manifest and covered by the guard.
- Nine games were final in the archive by ~02:50Z; the other three (late west-coast drops) follow. The archive ingests a final game roughly 75 minutes after its end and the next cron run settles it (next slot ≈ 12:30Z), so outcomes can lag by many hours; that delays nothing registered (outcomes are independent of the record).
- A local replay of `settle` + `score` on a copy of the branch against the 02:50Z archive: 324 outcome rows, 298 paired for H1/H3; descriptive only (H1 +1.3 % [−6.0 %, +11.0 %], H3 −4.1 % [−8.0 %, −0.03 %], n = 298): far too small to say anything; no look is near (10,000).

## Stored lineup/role inputs: what they are worth
Lines rows exist for 82–95 % of candidates, but at record time (≈ 10 h before the drop) DailyFaceoff's own label for most rows was **"Last Game (2026-10-22)"** (282 rows) — the previous game's lines, not a projection — with a median source `updatedAt` 17–42 h old. Records written this early cannot carry confirmed lines or power-play units; any lineup hypothesis needs the later `context/lines` snapshots already preserved, immutably and time-stamped, in the archive (joined by observation time ≤ drop − 10 min), not these stored inputs.

## Failures
None in collection. Findings: (1) LC scoreboard mislabelled records of unplayed games as non-dressers (fixed, display only, #92); (2) H2 comparator coverage as above; (3) settlement lag; (4) the dispatch path is untested live.
