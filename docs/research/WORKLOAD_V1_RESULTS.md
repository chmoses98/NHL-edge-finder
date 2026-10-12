# WORKLOAD_V1 held-out results (2025-26 regular season)

**Authority: RESEARCH_ONLY. Nothing is promoted or wired into production; no wagering, staking or routing change.**
Preregistration: `WORKLOAD_V1_PREREGISTRATION.md` + `workload_v1/preregistration.json`, committed in 841d443 before
this run. Full output: `workload_v1/results_2025.json` (run 2026-10-12 02:25-02:30 UTC). Audit: `WORKLOAD_AUDIT.md`.
Everything below is HISTORICAL (walk-forward on 2025-26); there is no prospective result yet.

## Verdict

| target | verdict | sample |
|---|---|---|
| skater shots on goal | **ACCEPTED** by the preregistered rule (all 7 checks pass): eligible for a prospective shadow test only | 47,231 skater-games, 1,312 games |
| goalie saves | **REJECTED** (CRPS, RMSE and ladder Brier CIs all include 0) | 2,624 starts, 1,312 games; CONDITIONAL_ON_ACTUAL_STARTER |

## Skater shots on goal

| arm | MAE | RMSE | bias | CRPS | ladder Brier 1+..5+ | cov50 | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| BASELINE (EW SOG/game, Poisson) | 1.0334 | 1.3300 | +0.041 | 0.6941 | 0.13302 | 0.482 | 0.784 |
| CHAMPION (production mean, Poisson) | **1.0110** | 1.3249 | -0.079 | 0.6896 | 0.13211 | 0.478 | 0.777 |
| CHAMPION_NB | 1.0110 | 1.3249 | -0.079 | 0.6896 | 0.13214 | 0.497 | 0.795 |
| WORKLOAD_ONLY (new minutes, champion rates) | 1.0130 | 1.3227 | -0.051 | 0.6883 | 0.13189 | 0.496 | 0.796 |
| EFFICIENCY_ONLY (champion minutes, new rates) | 1.0079 | 1.3194 | -0.068 | 0.6860 | 0.13144 | 0.502 | 0.801 |
| **WORKLOAD_V1** | 1.0158 | **1.3128** | **+0.030** | **0.6830** | **0.13087** | 0.497 | 0.798 |

Differences, challenger minus reference, 95% game-clustered bootstrap CI (2,000 resamples of 1,312 games):

| comparison | CRPS | RMSE | ladder Brier | MAE |
|---|---|---|---|---|
| WORKLOAD_V1 - CHAMPION | -0.00656 [-0.00771, -0.00541] | -0.0122 [-0.0143, -0.0101] | -0.00124 [-0.00146, -0.00101] | +0.0048 [+0.0030, +0.0065] |
| WORKLOAD_V1 - CHAMPION_NB | -0.00656 [-0.00775, -0.00537] | -0.0122 [-0.0143, -0.0101] | -0.00128 [-0.00151, -0.00104] | +0.0048 [+0.0030, +0.0065] |
| WORKLOAD_V1 - BASELINE | -0.01108 [-0.01234, -0.00980] | -0.0172 [-0.0195, -0.0149] | -0.00215 [-0.00239, -0.00190] | -0.0176 [-0.0195, -0.0156] |
| WORKLOAD_ONLY - CHAMPION_NB | -0.00130 [-0.00163, -0.00097] | -0.0022 [-0.0029, -0.0016] | -0.00026 [-0.00032, -0.00019] | +0.0020 [+0.0015, +0.0025] |
| EFFICIENCY_ONLY - CHAMPION_NB | -0.00359 [-0.00446, -0.00271] | -0.0055 [-0.0072, -0.0038] | -0.00070 [-0.00087, -0.00053] | -0.0030 [-0.0044, -0.0017] |

Acceptance checks (all required): CRPS vs CHAMPION and vs CHAMPION_NB CI upper < 0 (yes, yes); RMSE vs CHAMPION CI
upper < 0 (yes); ladder Brier vs CHAMPION_NB CI upper < 0 (yes); |bias| 0.030 <= 0.05 (yes); 80% coverage 0.798 in
[0.77, 0.83] (yes); CRPS no worse for forwards (0.7240 vs 0.7318, n 31,370) and defence (0.6021 vs 0.6061, n 15,861)
(yes).

Honest reading:
* The gain is real but small: CRPS -0.95%, RMSE -0.92% relative to production. Most SOG error is count noise no
  pregame model removes (audit section 4).
* **MAE is worse** (+0.0048, CI excludes 0). MAE rewards the median; the champion's -0.08 under-prediction moves its mean
  toward the median of a right-skewed count. MAE is reported as asked but is not a proper score for a mean forecast.
* Separately evaluated, efficiency (rates) contributes more than workload (minutes): EFFICIENCY_ONLY -0.0036 CRPS,
  WORKLOAD_ONLY -0.0013; together -0.0066.
* Overtime: in OT games (326 games, 11,736 skater-games) the challenger's bias is -0.008 vs the champion's -0.119; CRPS
  0.6915 vs 0.7000. Regulation games: 0.6802 vs 0.6862.
* Distribution shape is not the driver: CHAMPION_NB (alpha 0.082 fit on 2024-25) ties CHAMPION (CRPS diff 0.0000
  [-0.0002, +0.0002]).

### Workload, scored separately (minutes per skater-game; shift-chart rows, n 47,231)

| minutes | champion MAE / RMSE / bias | WORKLOAD_V1 MAE / RMSE / bias | MAE diff (95% CI) |
|---|---|---|---|
| total TOI | 1.934 / 2.545 / -0.336 | **1.875 / 2.484 / -0.008** | -0.059 [-0.065, -0.053] |
| PP TOI | 0.790 / 1.203 / -0.193 | 0.795 / **1.168 / -0.015** | +0.006 [-0.000, +0.012] |
| SH TOI | 0.665 / 1.020 / -0.179 | 0.671 / **0.987 / -0.016** | +0.005 [+0.000, +0.011] |
| EV incl. OT | 1.853 / 2.410 / -0.008 | **1.834 / 2.388** / -0.038 | -0.020 [-0.027, -0.012] |

The matchup team minutes (league-level PP / SH minutes from clean games, plus explicit OT minutes) remove the PP / SH / total-TOI bias and lower RMSE everywhere. Per PR #29, the PP / SH part comes from the team minutes, not from the OT-timeline repair. However, PP and SH MAE do not improve
(SH is marginally worse): the bias fix trades a little median accuracy. PP unit membership is still learned only from
recent shift shares; no historical line source exists to test tonight's PP1 / PP2 assignment.

### Efficiency, scored separately (SOG given the ACTUAL minutes)

| rates | MAE | RMSE | bias | Poisson deviance |
|---|---:|---:|---:|---:|
| champion (raw per-60) | 0.9928 | 1.2932 | -0.039 | 1.2289 |
| WORKLOAD_V1 (league-relative, shrunk, opponent, venue) | 0.9918 | **1.2803** | +0.033 | **1.1788** |

Squared-error difference -0.0332 [-0.0392, -0.0269].

## Goalie saves (CONDITIONAL_ON_ACTUAL_STARTER)

| arm | MAE | RMSE | bias | CRPS | ladder Brier 14+..40+ | cov50 | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| BASELINE | 5.490 | 6.977 | +0.29 | 3.9693 | 0.13759 | 0.373 | 0.658 |
| CHAMPION (production saves draws) | 5.350 | 6.822 | -0.08 | 3.7946 | 0.13132 | 0.473 | 0.800 |
| WORKLOAD_ONLY | 5.336 | 6.808 | -0.15 | 3.7958 | 0.13132 | 0.455 | 0.777 |
| EFFICIENCY_ONLY | **5.330** | **6.800** | +0.21 | **3.7863** | **0.13097** | 0.456 | 0.788 |
| WORKLOAD_V1 | 5.336 | 6.809 | +0.08 | 3.7942 | 0.13126 | 0.456 | 0.782 |

WORKLOAD_V1 - CHAMPION: CRPS -0.0005 [-0.0121, +0.0114]; RMSE -0.013 [-0.033, +0.007]; ladder Brier -0.00006
[-0.00049, +0.00037]; MAE -0.014 [-0.034, +0.005]. **REJECTED.**

Separately: shots faced by the starter, squared error -0.19 [-0.41, +0.03] (not significant; RMSE 6.786 vs 6.800);
saves given the actual shots, goalie-shrunk save fraction RMSE 1.583 vs champion implied 1.595 (squared-error diff
-0.041 [-0.080, -0.001]) but the plain league save fraction already scores 1.587, so most of that is level, not goalie
skill. EFFICIENCY_ONLY (champion shots x shrunk goalie save fraction) is the best arm by point estimate (CRPS -0.0083
[-0.0172, +0.0010] vs champion) but was not the preregistered challenger and its CI includes 0: a hypothesis for a
future preregistration, not a result. The challenger's 50% coverage (0.456) is lower than the champion's (0.473): its
saves distribution is too narrow in the middle.

## Limits

* One held-out season; the skater gain is about 1% and needs a prospective shadow test before anyone relies on it.
* Lineups are the actual dressed skaters (production reads warmup lines; Kalshi settles non-dressing players at the fair
  price). Starters are the actual starters; no point-in-time starter source exists for 2021-26 (audit section 6).
* The champion's PP-minute scaling uses the PLAYER_SIM_V1 walk-forward stand-in for the V2 goal components.
* The phantom-OT repair is inferred from shift presence (the timeline itself was not rebuilt); 2,880 of 2,918 OT
  team-game rows were repaired (the rest lack shift charts) and each repaired timeline sums to 3,600 s + the OT played.
* The live NHL API was not reachable from this session (egress policy); the committed official-API cache was used.

## Next steps (not done here)

1. Fix the `team_states` OT timeline at the source (`data.player_events.state_timeline` should stop at the game's last
   second) and rebuild the history; this changes production deployment shares, so it needs its own PR and a rerun of the
   PLAYER_SIM_V1 walk-forward.
2. Shadow WORKLOAD_V1 SOG prospectively next to `expected_shots` in the packet (no pricing use; no Kalshi SOG market).
3. Preregister the goalie EFFICIENCY_ONLY variant (champion shots x shrunk save fraction) on a new season.
4. Score DailyFaceoff starter accuracy prospectively from the archive (`research.goalie_status_eval`).
