# Decision report — NHL research sprint, 2026-10-23

RESEARCH_ONLY. Nothing here promotes a model, changes a published projection, a price, a stake, a cap, routing or the app contract. One published projection per target; no automatic promotion; PASS-only; the sealed-ledger workflows stay dormant. Every statement below points to a merged document; where a result is a hypothesis it is labelled one.

## 1. Which targets are materially improved?

| target | best candidate evidence | materially improved? | status |
|---|---|---|---|
| **Overtime probability** | V2 simulator (`nhl-sim-2.0`): Brier(OT) −0.0025 [−0.0033, −0.0017] vs V1 on the untouched 2010–2016 tier, favourable in 7/7 seasons; the same with retuned rates (J2: `v2-joint-retuned/RESULTS.md`). V1 predicts 18.7% overtime games, V2 22.6%, observed 23.7%. | **Yes** — the only target that clears every historical gate (G1–G6b, J1) | `SHADOW_MORE`: G7–G10 (runtime, reproducibility, contract, live non-inferiority) need live data. Awaiting an explicit human decision. |
| Win probability | Retuned+recalibrated V1: −0.0004 [−0.0009, +0.0002] on the untouched tier; −0.0017 pooled 2017–2025 but nearly all of it 2020–2023, ≈ 0 in 2025 | **No** (below the 0.0010 threshold on the untouched tier; regime-dependent) | `RETAIN_INCUMBENT` |
| Goal margin | RC_SIM2: RPS −0.0007 [−0.0026, +0.0012] | No | `RETAIN_INCUMBENT` |
| Total goals | RC_SIM2: RPS −0.0015 [−0.0033, +0.0003]; worse than V1 in exposed 2018 and 2021 | No | `RETAIN_INCUMBENT` |
| Regulation 3-class, joint (margin × OT, total × OT) scores | RC_SIM2 vs V1: −0.0044, −0.0011, −0.0010 (all intervals exclude 0) | Yes in the descriptive sense, but entirely the overtime component of the V2 simulator (SIM2 alone: −0.0036, −0.0006, −0.0007); no registered scorecard for these | descriptive |
| Team totals, puck lines | team-total Brier −0.0003 [−0.0005, −0.0001]; puck line −0.0002 (ns) | Immaterial | descriptive; no market history for team totals |
| Skater shots | WORKLOAD_V1: fixes the level (−2.5…−5.5% shots, −14…−19% PP minutes in the incumbent) but fails the frozen bias rule in 2023 by 0.003; `WORKLOAD_V1_LC` meets the development checks | Level errors yes; **the frozen rule has not been met** | `WORKLOAD_V1_LC` is under a clean prospective test (§3); WORKLOAD_V2 rejected (2023 tier bias) |
| Skater assists / points | PLAYER_SIM_V1 is unbiased and at the count-noise floor (MSE ÷ mean 1.00); calibration slope 1.09/1.12 | No improvement available beyond small recalibration | no candidate |
| Market comparison (2025, Kalshi midpoint, T−60) | no forecaster beats the market on any contract; totals: market better than V1, "indistinguishable" for RC_SIM2 (not a tested difference) | — | **PASS-only stands** |

## 2. Which candidates fail?

* **Opponent adjustment (`OA_RIDGE`, `OA_SVA`, `OA_SVA_C1`)**: adds nothing detectable once V1 is retuned and recalibrated (−0.0003 [−0.0007, +0.0002] pooled; −0.0002 on the untouched tier); tiny overtime penalty. Not preferred.
* **Retuned V1 as a general upgrade**: fails on the untouched 2010–2016 tier (below threshold) and is ≈ 0 in 2025 — the regime map (`regime/RESULTS.md`) shows the production constants were already at their season optimum in 2025 (oracle headroom 0.0004) while they were far off in 2020–2023 (0.0026–0.0048), when true team-strength spread was unusually large.
* **Retuned rates through the V2 simulator**: additive with the simulator's overtime gain (J2-A, J2-C pass) but not practically better than the best single fix for win, margin or total (J2-B).
* **WORKLOAD_V2**: rejected under its frozen rule (2023 tier bias 0.092 > 0.06).
* **WORKLOAD_V1 against its frozen rule**: failed on 2023 (|bias| 0.053 > 0.05); that result is preserved and not relabelled.
* **Goalie context and announced line assignment for skaters**: not testable — no point-in-time source before 2026-09-30. The lagged proxies show nothing (goalie) or a very small effect (line-mates).

## 3. What is new and running

* **`WORKLOAD_V1_LC` prospective shadow test** (`workload_v1/LC_PROSPECTIVE_REGISTRATION.md` + Amendment 1): frozen model, original seven-check rule unchanged, write-once pregame records on an orphan branch (`workload-shadow-data`), decision look at 30,000 paired player-games, final at 60,000. Seasons 2021–2025 remain exposed development data; they are not used as validation. An independent adversarial review before merge found a blocker (duplicate live-archive rows would have prevented any record) and seven should-fix items; all were fixed and a dry run against the real archive wrote records. **The test is live:** activated 2026-10-23T20:58:20Z; pregame records for the first two games were written before their drops (84 rows); the workflow's first scheduled slots were not delivered by GitHub within hours, so manual dispatch is used to cover days when cron is late (coverage gaps are listed, never back-filled).
* **Integrity guard** (`INTEGRITY.md`): sha256 registry of every historical data file, parameter file, frozen preregistration/result and the literal evaluation cohorts; pinned seasons for every production/frozen reader; tests prove that newly imported seasons cannot reach the production shadow arms, the frozen walk-forward datasets or earlier cohorts, and fail if anyone edits a registered file.
* **Player diagnosis** (`player_diagnosis/RESULTS.md`): the incumbent's expected power-play minutes run 13–16% low; 64–67% of a player's squared PP error is the (unpredictable) game-level penalty count; opponent shot suppression (coefficient ≈ 1), recent usage (≈ 4% of TOI MSE) and lagged line-mates carry stable, mostly small signal. All hypotheses on already-exposed seasons.

## 4. How fresh is pregame publication, actually?

Measured on the full slate of 2026-10-23 (two games, 00:00Z and 01:00Z on 10-24); every refresh is listed in `slates/2026-10-23_delivery_timeline.md` and discussed in `slates/2026-10-23_delivery_verification.md`.

* **Ten refreshes were requested (all by dispatch), ten ran, ten published a `projection-data` commit; none failed.** The six cron fallback runs cancelled themselves by design.
* **Request → runner start:** median 3.7 min, worst 24.1 min (one slow runner queue at 21:58Z). **Request → published:** median 6.0 min, worst 25.1 min. Runner start → completion: 1.1–3.4 min.
* **Last refresh before each drop:** 12.7 min before game 1 and 17.7 min before game 2. Requests came every 25–50 min in the last two hours, so the 24-minute queue left no gap.
* The core V1/V2 predictions were refreshed to 0.1 and 11.8 min before the drops with both goalies confirmed. The PF player forecasts are written only on change; they were last *changed* 4–5 h before the drops although they were re-evaluated 13 and 18 min before: no skater lineup confirmation (only the four goalies) reached the player layer before either drop. That is an input limitation, not a delivery delay.
* On 10-22 only one of three pregame refreshes finished before the first drop (cron slots 2–6.5 h late); on 10-23 every refresh finished before its game. **This is one slate** — the residual risk is a runner queue longer than the request interval in the last 30 minutes, which the design hedges (early requests, previous snapshot as fallback) but cannot remove.


## 5. What has to happen before any promotion

No promotion is requested. For each candidate, in order:

1. **Overtime (V2 simulator)** — the only candidate with historical evidence on every gate. Needed: G7 runtime measured, G8 bit-for-bit reproducibility demonstrated, G9 contract compatibility verified (published fields unchanged/additive), and G10 live non-inferiority from the existing live shadow arm over a pre-stated number of games; then a human approves the one-line champion-registry change. Rollback is the registry line.
2. **Skater shots (`WORKLOAD_V1_LC`)** — the prospective test must reach its 30,000-game decision look and meet the frozen rule; coverage of the incumbent comparator ≥ 80%; then a human decides, with the same G7–G10 gates. Failure is reported, not retried with a looser rule.
3. **Anything built from the diagnosis (opponent term, recent usage, minutes)** — a new pre-registration with a frozen candidate, tested on records written after activation (every historical player season is exposed); minutes must be added to the write-once records first, because they are not currently scored.
4. **An adaptive V1 prior** — a pre-registration with a prospective shadow; not needed for the current regime.
5. **Betting** — nothing in this sprint supports any wager, stake, cap or routing change; the market comparison shows no edge.
