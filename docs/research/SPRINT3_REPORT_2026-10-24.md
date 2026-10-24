# Sprint report 2026-10-24: overtime promotion readiness and player input quality (research only)

Baseline: `DECISION_REPORT_2026-10-23.md`. Nothing is promoted, activated, staked or routed; betting stays PASS-only; the sealed ledger stays dormant; production models, stakes and caps are unchanged.

## 1. Overtime (V2) promotion readiness
| gate | status |
|---|---|
| G7 runtime | passes on the scorecard's definition (inference time per slate, 300 s) and on direct measurement (≈ 34 s for a 16-game slate). The whole-cycle proxy I registered fails (p95 1,081 s; 17 % of cycles over 300 s) because unrelated slow jobs share those cycles. **Owner call:** confirm the scorecard definition; I reported the registered proxy as failed rather than redefine it. |
| G8 reproducibility | pass: three hash seeds identical; 400 archived live blocks re-simulate exactly (0 mismatches); training regenerates the V2 parameter files. |
| G9 publication contract | pass: default output byte-identical to no-V2; approved switch moves the five fields together with an `overtime_model` provenance block; any V2 failure falls back to V1 per game; a switch without a complete approval record is ignored. |
| G10 live non-inferiority | **open by design.** Registered sample starts with games on 2026-10-26, primary look 1,050 paired settled games (margin 0.0010, harm looks at 250/500/750), earliest decision ≈ late March 2027. Descriptive only (pre-T0, 167 pairs since 2026-09-29): paired Brier(OT) V2 − V1 = −0.0026, P(OT) V1 0.173 / V2 0.216 / observed 0.228. |

`data/registry/projection-registry.json` is merged at the V1 default with no approval; the exact reversible change is drafted in `docs/research/overtime_promotion/RECOMMENDATION.md`. No promotion PR exists and none will be opened before G10 passes and you approve.

## 2. Prospective shots test (WORKLOAD_V1_LC): unchanged, collection hardened
Test unchanged (30,000 paired player-games at the decision look, 60,000 final). Audit: GitHub cron arrives hours late, so pregame coverage cannot rely on it. Added unattended dispatch from the capture worker and `slate-watch`, a gap alert that fires only when a game is within 90 minutes with no covering run, and a ground-truth coverage audit in the scoreboard. Nothing is back-filled. Status at writing: 2 of 2 started games recorded pregame (84 rows); the first cron/dispatched runs on the 2026-10-24 slate are the live test (follow-up scheduled). A latent shell bug found in review (a failed day skipped publishing the other days) is fixed in a separate PR.

## 3. Lineup / role source feasibility (`docs/research/lineup_sources/FEASIBILITY.md`)
Best credible free source is what we already archive: DailyFaceoff lines, PP/PK units, scratches/GTD, with the source's own `updatedAt` and a source label, from 2026-09-30 only (no history exists anywhere for "who was PP1 before the game"). Paid options (SportsDataIO $99–149/month, Sportradar by quote) are unverified for confirmed PP units. Verification was limited by this environment's egress policy. **Owner questions:** terms and permission for DailyFaceoff (and stop spoofing a browser User-Agent), budget ceiling, polling NHL right-rail/game sheets before the drop, accepting prospective-only evaluation, MoneyPuck approval.

## 4. Player records (`player-minutes-1.0`, PR #86)
Separate schema, orphan branch and preregistration (H1 WORKLOAD_V1 vs production total ice time ≤ −2 %, H2 power-play time ≤ −3 %, H3 recent-usage term ≤ −0.5 %; looks 10k/30k/60k). Each record stores predictions, observed inputs (last-3 minutes, line/PP-unit rows with source timestamps, injuries, incumbent minutes as captured), provenance and fingerprints; official outcomes are appended later. Own workflow, requested together with the LC run. Dry run on the real archive: 10 games / 419 records in 17 s; 89.5 % carry line rows.

## 5. Challengers (`docs/research/player_challengers/RESULTS.md`, development evidence only)
Ice time: WORKLOAD_V1 beats the production minutes by −4.5 % (total) and −8.0 % (power play) MSE with the bias removed. On top of it only a recent-usage term helps total ice time (−1.1 %, coefficient 0.23); nothing helps power-play time. Shots: the level fix is the gain; opponent suppression and usage add ≈ 0.04 % CRPS on top of LC, so the registered LC test stays as is. Role-change and linemate terms do not earn a hypothesis.

## 6. Delivery monitoring (PR #85)
The monitor alerts only on a forecast that is missing, or whose evaluating run or lineup capture is stale, never on unchanged values; replayed on the 2026-10-23 slate with no false alert; a daily timeline records request-to-publication latency, lineup freshness and fallbacks. 2026-10-23: 10/10 refreshes published, last pregame forecasts 12.7/17.7 minutes before the drops.

## Highest-value improvement
Use WORKLOAD_V1 minutes (with the small usage term) for ice time and power-play time, validated prospectively through `player-minutes-1.0` before any promotion decision. Lineup inputs are the next candidate but can only be judged prospectively.
