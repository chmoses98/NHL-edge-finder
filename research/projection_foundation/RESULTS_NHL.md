# NHL Projection Foundation — results

*Generated 2026-10-17T07:38:15Z from `results/nhl_full_results.json` by `nhl/report.py` (code 322f533262, pf_core 1.0.0). Research only: nothing here changes betting authority.*

## 1. Bottom line for a bettor

Every number below is a walk-forward, point-in-time forecast: each game was projected using only games that had finished before it, with parameters fitted on 2021-22/2022-23, models chosen on 2023-24, and 2024-25 + 2025-26 scored once as a holdout. 2026-27 (games 1-120) is a prospective check against the archived PLAYER_SIM_V1 forecasts.

| Family | Best model | Holdout n | Holdout MAE | Holdout CRPS | vs baseline (CRPS, 95% CI) | vs incumbent (holdout) | vs incumbent (2026-27 prospective) | Readiness |
|---|---|---:|---:|---:|---|---|---|---|
| Shots on goal | F_stack | 94,228 | 1.019 | 0.6847 | -0.0063 [-0.0070, -0.0057] (better) | -0.0019 [-0.0026, -0.0012] (better; WORKLOAD_V1 (reproduced, frozen PR #28 params) 2025-26) | -0.0082 [-0.0128, -0.0037] (better) | **SHADOW VALIDATION** |
| Goals | F_stack | 94,228 | 0.265 | 0.1369 | -0.0012 [-0.0013, -0.0010] (better) | -0.0002 [-0.0004, -0.0000] (better; PLAYER_SIM_V1 walk-forward 2025-26) | -0.0002 [-0.0008, +0.0004] (tie) | **SHADOW VALIDATION** |
| Assists | F_stack | 94,228 | 0.399 | 0.2117 | -0.0020 [-0.0023, -0.0018] (better) | -0.0020 [-0.0025, -0.0016] (better; PLAYER_SIM_V1 walk-forward 2025-26) | -0.0041 [-0.0070, -0.0014] (better) | **SHADOW VALIDATION** |
| Points | F_stack | 94,228 | 0.521 | 0.2958 | -0.0029 [-0.0034, -0.0025] (better) | -0.0021 [-0.0027, -0.0015] (better; PLAYER_SIM_V1 walk-forward 2025-26) | -0.0032 [-0.0061, -0.0004] (better) | **SHADOW VALIDATION** |
| Goalie saves | F_stack | 5,222 | 5.350 | 3.8267 | -0.0867 [-0.1121, -0.0584] (better) | +0.0278 [+0.0118, +0.0432] (worse; PLAYER_SIM_V1 walk-forward 2024-25 + 2025-26) | +0.0237 [-2.3464, +2.2486] (tie) | **NEEDS IMPROVEMENT** |
| Team goals | F_stack | 5,246 | 1.379 | 0.9533 | -0.0086 [-0.0127, -0.0042] (better) | -0.0013 [-0.0038, +0.0009] (tie; DATA_ONLY_V2 SIM2_ST walk-forward 2024-25 + 2025-26) | n/a (-) | **SHADOW VALIDATION** |

Negative differences mean our model is better. CIs are 95% game-clustered bootstraps (games resampled, 1,000 draws). The incumbent metric differs by family (see section 5): CRPS for shots, rung RPS / Brier for goals-assists-points-saves because PLAYER_SIM_V1 only published ladder probabilities.

What this means in plain terms:

* **Shots on goal**: the new stack beats both the reproduced WORKLOAD_V1 (PR #28's accepted challenger) on 2025-26 and PLAYER_SIM_V1's expected shots on 2026-27, and is calibrated at the 2+/3+/4+/5+ rungs. The gain over a shrunk season average is about 0.9% of CRPS: real, but small. Shots are mostly noise once you know role and minutes.
* **Goals / assists / points**: the models sit within about 0.2-1% of a pure Poisson-noise floor. Against PLAYER_SIM_V1 they are better on assists and points (holdout and the 2026-27 prospective sample) and essentially tied on goals. The market was already as good as or better than PLAYER_SIM_V1 on these families (PR #10), so do not read this as edge.
* **Goalie saves**: improved over our baseline after fixing a league-level drift defect, but PLAYER_SIM_V1's game-script/pull-hazard saves model is still better on holdout. Not ready.
* **Team goals**: tied with DATA_ONLY_V2 per team, better on the game total's squared error, but the total's distribution is too wide (independent team draws ignore OT/shootout structure).

## 2. Data inventory and point-in-time status

| Dataset | Seasons | Rows | PIT class | Notes |
|---|---|---:|---|---|
| skater/goalie box scores (official boxscore) | 2021-22..2026-27 | 240,421 | reconstructable | regular-season games by season 2021-22: 1312, 2022-23: 1312, 2023-24: 1312, 2024-25: 1312, 2025-26: 1312, 2026-27: 120; 2026-27 = 120 games from the data-archive player_events (through 2026-10-16) superseding 3 committed games. Post-game facts used only as history. |
| TOI by strength (EV / PP / SH / EA / EN / OT from shift charts) | 2021-22..2026-27 | 238,372 | reconstructable | share of games with shift charts: 2021: 1.000, 2022: 1.000, 2023: 1.000, 2024: 0.957, 2025: 1.000, 2026: 1.000. 2024-25 lacks shift charts for 57 games (strength split NaN there). |
| line combinations (pairwise shared ice, coice) | 2021-22..2026-27 | 1,489,660 | reconstructable | post-game deployment; the PIT role used for game g is the previous game's lines / PP unit. Tonight's lines are NOT known historically. |
| pregame projected lines / PP units (DailyFaceoff) | 2026-27 only (from 2026-09-30) | 306 | archived | archived hourly snapshots (context/lines); none for 2021-22..2025-26, so the value of confirmed lines cannot be backtested. See lineup_accuracy. |
| starting goalie (actual, boxscore starter flag) | 2021-22..2026-27 | 13,236 | retrospective | saves projections are CONDITIONAL_ON_ACTUAL_STARTER; no PIT starter source exists before 2026-27. |
| pregame starting-goalie observations (DailyFaceoff status) | 2026-27 only | 360 | archived | PROJECTED / PROBABLE / CONFIRMED with observation time; see starter_accuracy. |
| shot events with x/y, type, strength (xG possible) | 2021-22..2026-27 | 783,648 | reconstructable | own logistic xG fitted on development seasons; used as lagged player/team shot quality. |
| schedule, rest days, back-to-backs | 2021-22..2026-27 | 6,680 | reconstructable | game dates are known in advance; derived from the game list. |
| travel distance / time zones | 2021-22..2026-27 | 6,680 | reconstructable | previous venue -> current venue haversine on approximate arena coordinates. |
| injury reports (ESPN) | 2026-27 only | 324 | archived | historical injury status missing; scratches are inferred post hoc. |
| archived prospective forecasts PLAYER_SIM_V1 (predictions_player) | 2026-27 only | 225,485 | archived | goals / assists / points / first-goal / saves ladders + expected TOI, PP TOI, SOG, G, A, P per player snapshot; incumbent on the 2026-27 overlap (last pregame snapshot per player-game). |
| PLAYER_SIM_V1 walk-forward predictions (docs/research/player_sim_v1) | skaters 2025-26; goalies 2024-25, 2025-26 | 52,479 | reconstructable | historical walk-forward (deployment from recent shifts, actual dressed lineup and starters); incumbent on holdout. |
| DATA_ONLY_V2 walk-forward game lambdas (docs/research/walk_forward_v2_*_games.csv) | 2024-25, 2025-26 | 2,624 | reconstructable | SIM2_ST expected home/away goals = team-goals incumbent on holdout (valid pregame arm). |
| dressed lineup / scratches | 2021-22..2026-27 | 240,421 | retrospective | evaluation is conditional on playing (Kalshi settles a non-entering player at fair price). |

**What is conditioned on, and what it costs.** Skater projections are conditional on the player dressing (Kalshi settles a non-entering player at the pre-game fair price) and saves are conditional on the actual starter. The 2026-27 archive lets us measure how much pregame information that assumes:

* Starting goalie: the last archived DailyFaceoff observation before puck drop named the actual starter in 100.0% of 116 team-games; at 1 h / 3 h / 6 h before: 99.1% / 98.3% / 98.3%. So a saves projection published 1-6 h before the game carries a ~1-2% chance of describing a goalie who does not start; no PIT starter source exists for 2021-26.
* Lineups: 98.3% of DailyFaceoff-projected skaters dressed and 97.6% of dressed skaters were projected (230 team-games). PP1 membership: precision 87.2%, recall 87.6%. Historical lines do not exist, so backtests use the previous game's shift-derived role (line rank, PP unit) — the forward projector reads DailyFaceoff lineups for who plays.

## 3. Splits and method

* **development**: 2021-22, 2022-23 regular seasons (fit shrinkage, betas, dispersion, stack weights)
* **validation**: 2023-24 regular season (model and distribution selection)
* **holdout**: 2024-25 and 2025-26 regular seasons (evaluated once for frozen candidates) (saves re-scored once after a validation-motivated drift fix; disclosed)
* **prospective**: 2026-27 regular season to date (games 2026020001-2026020120, archived; overlaps PLAYER_SIM_V1)

Ladder per family: **A** season-to-date + last season mean shrunk to a point-in-time role prior; **B** EWMA (halflife chosen on development) shrunk; **C** projected TOI x per-minute rates, non-PP and PP separately, empirical-Bayes shrinkage measured in minutes; **D** C x schedule-adjusted opponent factor^beta x venue (beta fitted on development); **E** LightGBM on PIT features (shot quality/xG, role, linemates' rates from co-ice, schedule, opponent ratings, D's mean) refitted each season on all earlier seasons; **F** non-negative stack of A..E fitted on 2022-23. Saves: A/B on saves; C = team shots allowed x goalie shrunk save% ; D = ridge shots-against (opponent generation + own suppression + venue) x save%. Team goals: C = attack x opponent defence (log5); D = ridge goals/xG blend. Distributions: NB with mean-binned dispersion fitted on development residuals.

## 4. Opportunity: time on ice

| Split | Model | Target | MAE (min) | RMSE | Bias |
|---|---|---|---:|---:|---:|
| validation | toi_A | toi | 1.980 | 2.611 | +0.021 |
| validation | toi_B | toi | 1.872 | 2.490 | +0.021 |
| validation | toi_C | toi | 1.871 | 2.488 | +0.046 |
| validation | toi_C | toi_pp | 0.789 | 1.154 | +0.035 |
| validation | toi_E | toi | 1.854 | 2.462 | -0.098 |
| validation | toi_E | toi_pp | 0.788 | 1.153 | +0.007 |
| holdout | toi_A | toi | 1.969 | 2.582 | -0.024 |
| holdout | toi_B | toi | 1.844 | 2.440 | +0.004 |
| holdout | toi_C | toi | 1.845 | 2.442 | +0.012 |
| holdout | toi_C | toi_pp | 0.767 | 1.141 | +0.023 |
| holdout | toi_E | toi | 1.821 | 2.405 | -0.049 |
| holdout | toi_E | toi_pp | 0.768 | 1.134 | +0.016 |
| prospective | toi_A | toi | 2.020 | 2.650 | +0.092 |
| prospective | toi_B | toi | 1.969 | 2.594 | +0.031 |
| prospective | toi_C | toi | 1.962 | 2.588 | +0.079 |
| prospective | toi_C | toi_pp | 0.816 | 1.206 | -0.124 |
| prospective | toi_E | toi | 1.885 | 2.494 | -0.021 |
| prospective | toi_E | toi_pp | 0.817 | 1.176 | +0.037 |

**Against incumbents (paired, same player-games):**

| Incumbent | n | Our TOI MAE | Incumbent TOI MAE | Diff (95% CI) | Our PP MAE | Incumbent PP MAE | PP diff (95% CI) |
|---|---:|---:|---:|---|---:|---:|---|
| PLAYER_SIM_V1 walk-forward 2025-26 | 47,114 | 1.842 (bias -0.11) | 1.939 (bias -0.39) | -0.098 [-0.106, -0.089] | 0.778 | 0.788 | -0.010 [-0.017, -0.004] |
| PLAYER_SIM_V1 prospective archive 2026-27 | 3,798 | 1.859 (bias -0.03) | 1.932 (bias -0.20) | -0.073 [-0.107, -0.038] | 0.815 | 0.857 | -0.042 [-0.084, +0.001] |

WORKLOAD_V1's published 2025-26 TOI MAE was 1.875 (RMSE 2.484); ours on the same season is in the first row above. The PLAYER_SIM_V1 prospective rows used DailyFaceoff projected lines; our model used only the previous game's shift data and still had lower TOI error.

**Bias by role (validation, T_E):**

| Role (previous game) | n | MAE | Bias | Mean TOI |
|---|---:|---:|---:|---:|
| D1 | 5,248 | 1.925 | -0.091 | 22.07 |
| D2 | 5,242 | 1.996 | -0.104 | 19.73 |
| D3 | 5,399 | 2.124 | -0.054 | 15.95 |
| F1 | 7,867 | 1.820 | -0.268 | 18.40 |
| F2 | 7,865 | 1.745 | -0.140 | 16.47 |
| F3 | 7,869 | 1.706 | -0.067 | 14.23 |
| F4 | 7,617 | 1.817 | +0.058 | 11.27 |

| PP role (previous game) | n | PP MAE | PP bias | Mean PP TOI |
|---|---:|---:|---:|---:|
| PP1 | 12,820 | 1.316 | +0.003 | 3.06 |
| PP2 | 17,894 | 0.792 | -0.009 | 1.34 |
| noPP | 16,393 | 0.372 | +0.028 | 0.38 |

Top-line forwards are under-projected by about a quarter-minute and fourth-liners slightly over-projected (shrinkage toward the role mean); PP minutes are unbiased by unit.

## 5. Families

### Shots on goal

Population: skaters who dressed (TOI > 0) with >= 1 prior NHL game since 2021-22; regular season; conditional on playing.

| Split | Model | n | MAE | RMSE | Bias | CRPS | 80% cover / PIT var | vs A: CRPS diff (95% CI) | vs incumbent | Verdict |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| validation | A_season_avg_shrunk | 47,107 | 1.0648 | 1.3694 | +0.0418 | 0.71703 | 0.806 / 0.990 | baseline |  | baseline |
| validation | B_ewma_shrunk | 47,107 | 1.0660 | 1.3685 | +0.0539 | 0.71669 | 0.807 / 0.989 | -0.00034 [-0.00100, +0.00030] |  | rejected |
| validation | C_toi_x_rate | 47,107 | 1.0589 | 1.3627 | +0.0373 | 0.71313 | 0.806 / 0.990 | -0.00390 [-0.00477, -0.00306] |  | rejected |
| validation | D_opp_adjusted | 47,107 | 1.0537 | 1.3591 | +0.0152 | 0.71117 | 0.805 / 0.993 | -0.00587 [-0.00695, -0.00480] |  | competitive |
| validation | E_lightgbm | 47,107 | 1.0541 | 1.3579 | +0.0340 | 0.71056 | 0.804 / 0.994 | -0.00647 [-0.00751, -0.00539] |  | competitive |
| validation | F_stack | 47,107 | 1.0531 | 1.3576 | +0.0218 | 0.71035 | 0.806 / 0.991 | -0.00669 [-0.00769, -0.00568] |  | best |
| holdout | A_season_avg_shrunk | 94,228 | 1.0295 | 1.3265 | +0.0458 | 0.69102 | 0.804 / 0.992 | baseline |  | baseline |
| holdout | B_ewma_shrunk | 94,228 | 1.0291 | 1.3251 | +0.0603 | 0.69006 | 0.804 / 0.989 | -0.00096 [-0.00140, -0.00052] |  | rejected |
| holdout | C_toi_x_rate | 94,228 | 1.0257 | 1.3199 | +0.0641 | 0.68691 | 0.805 / 0.987 | -0.00411 [-0.00462, -0.00356] |  | rejected |
| holdout | D_opp_adjusted | 94,228 | 1.0207 | 1.3167 | +0.0432 | 0.68516 | 0.804 / 0.990 | -0.00586 [-0.00654, -0.00518] |  | competitive |
| holdout | E_lightgbm | 94,228 | 1.0182 | 1.3169 | +0.0330 | 0.68504 | 0.801 / 0.997 | -0.00598 [-0.00672, -0.00528] |  | competitive |
| holdout | F_stack | 94,228 | 1.0193 | 1.3160 | +0.0396 | 0.68468 | 0.804 / 0.991 | -0.00634 [-0.00703, -0.00567] | -0.00187 [-0.00257, -0.00119] | best |
| prospective | A_season_avg_shrunk | 4,295 | 1.0218 | 1.3041 | +0.0795 | 0.67885 | 0.810 / 0.985 | baseline |  | baseline |
| prospective | B_ewma_shrunk | 4,295 | 1.0169 | 1.2978 | +0.0821 | 0.67570 | 0.812 / 0.986 | -0.00315 [-0.00575, -0.00056] |  | rejected |
| prospective | C_toi_x_rate | 4,295 | 1.0141 | 1.2951 | +0.0884 | 0.67379 | 0.811 / 0.986 | -0.00506 [-0.00809, -0.00213] |  | rejected |
| prospective | D_opp_adjusted | 4,295 | 1.0084 | 1.2900 | +0.0666 | 0.67152 | 0.809 / 0.991 | -0.00733 [-0.01057, -0.00413] |  | competitive |
| prospective | E_lightgbm | 4,295 | 0.9984 | 1.2860 | +0.0340 | 0.66891 | 0.809 / 0.998 | -0.00994 [-0.01329, -0.00661] |  | competitive |
| prospective | F_stack | 4,295 | 1.0046 | 1.2880 | +0.0552 | 0.67024 | 0.810 / 0.992 | -0.00861 [-0.01189, -0.00541] | -0.00820 [-0.01282, -0.00369] | best |

*Incumbent, holdout* — WORKLOAD_V1 (reproduced, frozen PR #28 params) 2025-26 (47,114 rows, 1312 games): 
  mean MAE/RMSE/bias ours 1.0115 / 1.3111 / +0.0080 vs incumbent 1.0155 / 1.3126 / +0.0284; squared-error diff -0.0041 [-0.0073, -0.0011].
  CRPS ours 0.6817 vs incumbent-mean-as-Poisson 0.6835, diff -0.0019 [-0.0026, -0.0012].

*Incumbent, prospective* — PLAYER_SIM_V1 prospective archive 2026-27 (3,798 rows, 115 games): 
  mean MAE/RMSE/bias ours 1.0207 / 1.3055 / +0.0508 vs incumbent 1.0170 / 1.3206 / -0.0636; squared-error diff -0.0398 [-0.0644, -0.0156].
  CRPS ours 0.6823 vs incumbent-mean-as-Poisson 0.6905, diff -0.0082 [-0.0128, -0.0037].

### Goals

Population: same skater population.

| Split | Model | n | MAE | RMSE | Bias | CRPS | 80% cover / PIT var | vs A: CRPS diff (95% CI) | vs incumbent | Verdict |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| validation | A_season_avg_shrunk | 47,107 | 0.2727 | 0.4183 | +0.0040 | 0.13955 | 0.799 / 0.992 | baseline |  | baseline |
| validation | B_ewma_shrunk | 47,107 | 0.2720 | 0.4178 | +0.0053 | 0.13926 | 0.800 / 0.992 | -0.00028 [-0.00045, -0.00012] |  | rejected |
| validation | C_toi_x_rate | 47,107 | 0.2722 | 0.4173 | +0.0042 | 0.13896 | 0.801 / 0.990 | -0.00059 [-0.00075, -0.00042] |  | rejected |
| validation | D_opp_adjusted | 47,107 | 0.2711 | 0.4169 | +0.0034 | 0.13880 | 0.800 / 0.991 | -0.00075 [-0.00096, -0.00053] |  | rejected |
| validation | E_lightgbm | 47,107 | 0.2704 | 0.4167 | +0.0048 | 0.13864 | 0.800 / 0.992 | -0.00090 [-0.00121, -0.00060] |  | competitive |
| validation | F_stack | 47,107 | 0.2708 | 0.4164 | +0.0041 | 0.13851 | 0.800 / 0.991 | -0.00103 [-0.00128, -0.00079] |  | best |
| holdout | A_season_avg_shrunk | 94,228 | 0.2690 | 0.4122 | +0.0022 | 0.13805 | 0.799 / 0.996 | baseline |  | baseline |
| holdout | B_ewma_shrunk | 94,228 | 0.2681 | 0.4116 | +0.0031 | 0.13766 | 0.800 / 0.995 | -0.00039 [-0.00050, -0.00028] |  | rejected |
| holdout | C_toi_x_rate | 94,228 | 0.2687 | 0.4108 | +0.0031 | 0.13727 | 0.801 / 0.992 | -0.00078 [-0.00090, -0.00066] |  | rejected |
| holdout | D_opp_adjusted | 94,228 | 0.2678 | 0.4108 | +0.0022 | 0.13721 | 0.801 / 0.994 | -0.00084 [-0.00098, -0.00070] |  | rejected |
| holdout | E_lightgbm | 94,228 | 0.2628 | 0.4102 | -0.0042 | 0.13687 | 0.797 / 1.001 | -0.00118 [-0.00137, -0.00098] |  | competitive |
| holdout | F_stack | 94,228 | 0.2652 | 0.4102 | -0.0012 | 0.13687 | 0.799 / 0.997 | -0.00117 [-0.00134, -0.00102] | -0.00021 [-0.00039, -0.00003] | best |
| prospective | A_season_avg_shrunk | 4,295 | 0.2784 | 0.4278 | +0.0010 | 0.14304 | 0.798 / 1.001 | baseline |  | baseline |
| prospective | B_ewma_shrunk | 4,295 | 0.2768 | 0.4262 | +0.0041 | 0.14244 | 0.795 / 1.003 | -0.00060 [-0.00147, +0.00038] |  | rejected |
| prospective | C_toi_x_rate | 4,295 | 0.2776 | 0.4251 | +0.0055 | 0.14186 | 0.799 / 0.999 | -0.00119 [-0.00197, -0.00029] |  | rejected |
| prospective | D_opp_adjusted | 4,295 | 0.2764 | 0.4245 | +0.0046 | 0.14157 | 0.799 / 1.000 | -0.00147 [-0.00231, -0.00057] |  | rejected |
| prospective | E_lightgbm | 4,295 | 0.2720 | 0.4240 | -0.0008 | 0.14123 | 0.797 / 1.007 | -0.00182 [-0.00281, -0.00076] |  | competitive |
| prospective | F_stack | 4,295 | 0.2741 | 0.4240 | +0.0017 | 0.14124 | 0.800 / 1.003 | -0.00180 [-0.00267, -0.00084] | -0.00015 [-0.00078, +0.00040] | best |

*Incumbent, holdout* — PLAYER_SIM_V1 walk-forward 2025-26 (47,114 rows, 1312 games): 
  mean MAE/RMSE/bias ours 0.2673 / 0.4140 / -0.0025 vs incumbent 0.2696 / 0.4144 / +0.0009; squared-error diff -0.0003 [-0.0006, -0.0000].
  Rung RPS over 1+..3+: ours 0.13844 vs 0.13865, diff -0.00021 [-0.00039, -0.00003].
  Rung Brier (ours vs incumbent, diff CI): 1+ n=47,114: 0.1198 vs 0.1200 -0.0002 [-0.0004, -0.0000]; 2+ n=47,114: 0.0166 vs 0.0167 -0.0000 [-0.0000, +0.0000]; 3+ n=47,114: 0.0020 vs 0.0020 -0.0000 [-0.0000, +0.0000].

*Incumbent, prospective* — PLAYER_SIM_V1 prospective archive 2026-27 (3,798 rows, 115 games): 
  mean MAE/RMSE/bias ours 0.2814 / 0.4307 / +0.0011 vs incumbent 0.2820 / 0.4314 / -0.0002; squared-error diff -0.0006 [-0.0017, +0.0005].
  Rung RPS over 1+..1+: ours 0.12161 vs 0.12177, diff -0.00015 [-0.00078, +0.00040].
  Rung Brier (ours vs incumbent, diff CI): 1+ n=3,797: 0.1216 vs 0.1218 -0.0002 [-0.0008, +0.0004]; 2+ n=1,656: 0.0358 vs 0.0360 -0.0002 [-0.0004, +0.0000]; 3+ n=302: 0.0228 vs 0.0229 -0.0000 [-0.0001, +0.0000].

### Assists

Population: same skater population.

| Split | Model | n | MAE | RMSE | Bias | CRPS | 80% cover / PIT var | vs A: CRPS diff (95% CI) | vs incumbent | Verdict |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| validation | A_season_avg_shrunk | 47,107 | 0.4079 | 0.5410 | +0.0061 | 0.21526 | 0.801 / 0.988 | baseline |  | baseline |
| validation | B_ewma_shrunk | 47,107 | 0.4056 | 0.5398 | +0.0077 | 0.21458 | 0.801 / 0.989 | -0.00067 [-0.00091, -0.00042] |  | rejected |
| validation | C_toi_x_rate | 47,107 | 0.4054 | 0.5387 | +0.0063 | 0.21384 | 0.802 / 0.986 | -0.00141 [-0.00169, -0.00112] |  | rejected |
| validation | D_opp_adjusted | 47,107 | 0.4036 | 0.5379 | +0.0050 | 0.21350 | 0.802 / 0.988 | -0.00176 [-0.00217, -0.00133] |  | competitive |
| validation | E_lightgbm | 47,107 | 0.4010 | 0.5379 | +0.0034 | 0.21334 | 0.801 / 0.992 | -0.00191 [-0.00245, -0.00140] |  | competitive |
| validation | F_stack | 47,107 | 0.4025 | 0.5374 | +0.0043 | 0.21316 | 0.802 / 0.989 | -0.00209 [-0.00252, -0.00168] |  | best |
| holdout | A_season_avg_shrunk | 94,228 | 0.4042 | 0.5364 | +0.0032 | 0.21375 | 0.798 / 0.997 | baseline |  | baseline |
| holdout | B_ewma_shrunk | 94,228 | 0.4017 | 0.5352 | +0.0038 | 0.21309 | 0.798 / 0.998 | -0.00066 [-0.00084, -0.00049] |  | rejected |
| holdout | C_toi_x_rate | 94,228 | 0.4021 | 0.5341 | +0.0037 | 0.21237 | 0.800 / 0.995 | -0.00138 [-0.00158, -0.00119] |  | rejected |
| holdout | D_opp_adjusted | 94,228 | 0.4005 | 0.5337 | +0.0022 | 0.21216 | 0.799 / 0.996 | -0.00159 [-0.00185, -0.00134] |  | competitive |
| holdout | E_lightgbm | 94,228 | 0.3970 | 0.5331 | +0.0020 | 0.21169 | 0.798 / 0.999 | -0.00206 [-0.00239, -0.00175] |  | competitive |
| holdout | F_stack | 94,228 | 0.3990 | 0.5331 | +0.0021 | 0.21174 | 0.799 / 0.996 | -0.00201 [-0.00230, -0.00175] | -0.00203 [-0.00247, -0.00156] | best |
| prospective | A_season_avg_shrunk | 4,295 | 0.4184 | 0.5500 | +0.0017 | 0.22005 | 0.801 / 0.994 | baseline |  | baseline |
| prospective | B_ewma_shrunk | 4,295 | 0.4078 | 0.5427 | +0.0049 | 0.21649 | 0.803 / 0.996 | -0.00356 [-0.00537, -0.00175] |  | rejected |
| prospective | C_toi_x_rate | 4,295 | 0.4084 | 0.5419 | +0.0087 | 0.21577 | 0.804 / 0.991 | -0.00428 [-0.00608, -0.00248] |  | rejected |
| prospective | D_opp_adjusted | 4,295 | 0.4061 | 0.5405 | +0.0071 | 0.21498 | 0.803 / 0.991 | -0.00507 [-0.00713, -0.00305] |  | competitive |
| prospective | E_lightgbm | 4,295 | 0.3998 | 0.5395 | -0.0004 | 0.21460 | 0.798 / 1.001 | -0.00546 [-0.00764, -0.00314] |  | competitive |
| prospective | F_stack | 4,295 | 0.4036 | 0.5398 | +0.0041 | 0.21464 | 0.801 / 0.995 | -0.00541 [-0.00746, -0.00330] | -0.00409 [-0.00698, -0.00138] | best |

*Incumbent, holdout* — PLAYER_SIM_V1 walk-forward 2025-26 (47,114 rows, 1312 games): 
  mean MAE/RMSE/bias ours 0.4008 / 0.5368 / -0.0035 vs incumbent 0.4090 / 0.5407 / +0.0028; squared-error diff -0.0042 [-0.0051, -0.0033].
  Rung RPS over 1+..2+: ours 0.20747 vs 0.20950, diff -0.00203 [-0.00247, -0.00156].
  Rung Brier (ours vs incumbent, diff CI): 1+ n=47,114: 0.1694 vs 0.1711 -0.0017 [-0.0021, -0.0013]; 2+ n=47,114: 0.0380 vs 0.0384 -0.0003 [-0.0005, -0.0002].

*Incumbent, prospective* — PLAYER_SIM_V1 prospective archive 2026-27 (3,798 rows, 115 games): 
  mean MAE/RMSE/bias ours 0.4133 / 0.5513 / +0.0003 vs incumbent 0.4228 / 0.5578 / -0.0001; squared-error diff -0.0073 [-0.0119, -0.0027].
  Rung Brier (ours vs incumbent, diff CI): 1+ n=2,030: 0.1999 vs 0.2040 -0.0041 [-0.0070, -0.0014]; 2+ n=1,298: 0.0791 vs 0.0806 -0.0015 [-0.0030, -0.0001].

### Points

Population: same skater population.

| Split | Model | n | MAE | RMSE | Bias | CRPS | 80% cover / PIT var | vs A: CRPS diff (95% CI) | vs incumbent | Verdict |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| validation | A_season_avg_shrunk | 47,107 | 0.5335 | 0.6837 | +0.0099 | 0.30260 | 0.799 / 0.993 | baseline |  | baseline |
| validation | B_ewma_shrunk | 47,107 | 0.5317 | 0.6825 | +0.0128 | 0.30189 | 0.800 / 0.993 | -0.00071 [-0.00105, -0.00038] |  | rejected |
| validation | C_toi_x_rate | 47,107 | 0.5326 | 0.6811 | +0.0105 | 0.30095 | 0.802 / 0.989 | -0.00165 [-0.00207, -0.00122] |  | rejected |
| validation | D_opp_adjusted | 47,107 | 0.5307 | 0.6796 | +0.0083 | 0.30019 | 0.802 / 0.990 | -0.00241 [-0.00311, -0.00166] |  | competitive |
| validation | E_lightgbm | 47,107 | 0.5265 | 0.6798 | +0.0064 | 0.30017 | 0.800 / 0.997 | -0.00243 [-0.00327, -0.00154] |  | competitive |
| validation | F_stack | 47,107 | 0.5286 | 0.6789 | +0.0075 | 0.29973 | 0.802 / 0.992 | -0.00287 [-0.00362, -0.00210] |  | best |
| holdout | A_season_avg_shrunk | 94,228 | 0.5266 | 0.6744 | +0.0046 | 0.29879 | 0.800 / 0.995 | baseline |  | baseline |
| holdout | B_ewma_shrunk | 94,228 | 0.5242 | 0.6730 | +0.0063 | 0.29795 | 0.800 / 0.995 | -0.00084 [-0.00110, -0.00059] |  | rejected |
| holdout | C_toi_x_rate | 94,228 | 0.5256 | 0.6714 | +0.0068 | 0.29687 | 0.803 / 0.989 | -0.00192 [-0.00224, -0.00160] |  | rejected |
| holdout | D_opp_adjusted | 94,228 | 0.5240 | 0.6709 | +0.0044 | 0.29647 | 0.802 / 0.991 | -0.00232 [-0.00277, -0.00186] |  | competitive |
| holdout | E_lightgbm | 94,228 | 0.5177 | 0.6701 | +0.0010 | 0.29584 | 0.800 / 0.997 | -0.00295 [-0.00346, -0.00243] |  | competitive |
| holdout | F_stack | 94,228 | 0.5211 | 0.6699 | +0.0029 | 0.29585 | 0.801 / 0.992 | -0.00294 [-0.00341, -0.00249] | -0.00211 [-0.00269, -0.00152] | best |
| prospective | A_season_avg_shrunk | 4,295 | 0.5504 | 0.6998 | +0.0040 | 0.31062 | 0.792 / 0.995 | baseline |  | baseline |
| prospective | B_ewma_shrunk | 4,295 | 0.5382 | 0.6926 | +0.0091 | 0.30687 | 0.790 / 0.998 | -0.00375 [-0.00587, -0.00140] |  | rejected |
| prospective | C_toi_x_rate | 4,295 | 0.5389 | 0.6908 | +0.0140 | 0.30552 | 0.793 / 0.990 | -0.00511 [-0.00723, -0.00275] |  | rejected |
| prospective | D_opp_adjusted | 4,295 | 0.5367 | 0.6881 | +0.0115 | 0.30399 | 0.795 / 0.990 | -0.00663 [-0.00947, -0.00384] |  | competitive |
| prospective | E_lightgbm | 4,295 | 0.5290 | 0.6877 | -0.0044 | 0.30385 | 0.790 / 1.004 | -0.00677 [-0.00957, -0.00369] |  | competitive |
| prospective | F_stack | 4,295 | 0.5333 | 0.6874 | +0.0047 | 0.30363 | 0.794 / 0.995 | -0.00699 [-0.00970, -0.00417] | -0.00319 [-0.00607, -0.00037] | best |

*Incumbent, holdout* — PLAYER_SIM_V1 walk-forward 2025-26 (47,114 rows, 1312 games): 
  mean MAE/RMSE/bias ours 0.5239 / 0.6759 / -0.0066 vs incumbent 0.5320 / 0.6797 / +0.0037; squared-error diff -0.0052 [-0.0067, -0.0037].
  Rung RPS over 1+..3+: ours 0.29526 vs 0.29736, diff -0.00211 [-0.00269, -0.00152].
  Rung Brier (ours vs incumbent, diff CI): 1+ n=47,114: 0.2021 vs 0.2035 -0.0014 [-0.0019, -0.0009]; 2+ n=47,114: 0.0746 vs 0.0752 -0.0006 [-0.0008, -0.0004]; 3+ n=47,114: 0.0185 vs 0.0186 -0.0001 [-0.0002, -0.0001].

*Incumbent, prospective* — PLAYER_SIM_V1 prospective archive 2026-27 (3,798 rows, 115 games): 
  mean MAE/RMSE/bias ours 0.5427 / 0.6981 / +0.0003 vs incumbent 0.5542 / 0.7065 / -0.0003; squared-error diff -0.0118 [-0.0192, -0.0045].
  Rung Brier (ours vs incumbent, diff CI): 1+ n=1,986: 0.2279 vs 0.2311 -0.0032 [-0.0061, -0.0004]; 2+ n=1,832: 0.1200 vs 0.1223 -0.0023 [-0.0042, -0.0005]; 3+ n=626: 0.0780 vs 0.0796 -0.0017 [-0.0040, +0.0004].

### Goalie saves

Population: actual starting goalies with >= 1 prior start since 2021-22 (CONDITIONAL_ON_ACTUAL_STARTER).

| Split | Model | n | MAE | RMSE | Bias | CRPS | 80% cover / PIT var | vs A: CRPS diff (95% CI) | vs incumbent | Verdict |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| validation | A_season_avg_shrunk | 2,617 | 5.8189 | 7.5284 | +0.4484 | 4.18166 | 0.817 / 0.943 | baseline |  | baseline |
| validation | B_ewma_shrunk | 2,617 | 5.8364 | 7.5550 | +0.6312 | 4.19306 | 0.817 / 0.943 | +0.01139 [-0.00117, +0.02488] |  | rejected |
| validation | C_toi_x_rate | 2,617 | 5.8128 | 7.5480 | +0.8805 | 4.17617 | 0.821 / 0.935 | -0.00550 [-0.02769, +0.01721] |  | rejected |
| validation | D_opp_adjusted | 2,617 | 5.6464 | 7.3523 | +0.1397 | 4.07086 | 0.807 / 0.958 | -0.11080 [-0.15620, -0.05699] |  | rejected |
| validation | E_lightgbm | 2,617 | 5.7122 | 7.4463 | +0.3930 | 4.12135 | 0.820 / 0.943 | -0.06032 [-0.11689, +0.00637] |  | rejected |
| validation | F_stack | 2,617 | 5.6332 | 7.3405 | +0.2073 | 4.06220 | 0.807 / 0.960 | -0.11947 [-0.16222, -0.06917] |  | best |
| holdout | A_season_avg_shrunk | 5,222 | 5.4950 | 7.0286 | +0.5006 | 3.91334 | 0.826 / 0.931 | baseline |  | baseline |
| holdout | B_ewma_shrunk | 5,222 | 5.5427 | 7.0748 | +0.9495 | 3.92988 | 0.833 / 0.920 | +0.01654 [+0.00688, +0.02681] |  | rejected |
| holdout | C_toi_x_rate | 5,222 | 5.4870 | 7.0239 | +0.8487 | 3.89954 | 0.834 / 0.918 | -0.01380 [-0.02856, +0.00155] |  | rejected |
| holdout | D_opp_adjusted | 5,222 | 5.3602 | 6.9016 | +0.1078 | 3.83556 | 0.813 / 0.973 | -0.07778 [-0.10645, -0.04705] |  | rejected |
| holdout | E_lightgbm | 5,222 | 5.3957 | 6.9272 | -0.1664 | 3.86689 | 0.830 / 0.934 | -0.04645 [-0.07631, -0.01690] |  | rejected |
| holdout | F_stack | 5,222 | 5.3499 | 6.8894 | +0.1754 | 3.82667 | 0.810 / 0.985 | -0.08667 [-0.11210, -0.05844] | +0.02778 [+0.01179, +0.04317] | best |
| prospective | A_season_avg_shrunk | 116 | 5.0096 | 6.4678 | +0.6304 | 3.61134 | 0.836 / 0.885 | baseline |  | baseline |
| prospective | B_ewma_shrunk | 116 | 5.0204 | 6.4509 | +1.0268 | 3.60589 | 0.828 / 0.863 | -0.00544 [-0.10000, +0.08237] |  | rejected |
| prospective | C_toi_x_rate | 116 | 5.0897 | 6.5697 | +1.0741 | 3.64521 | 0.836 / 0.868 | +0.03387 [-0.09263, +0.15071] |  | rejected |
| prospective | D_opp_adjusted | 116 | 4.8403 | 6.2929 | +0.3499 | 3.48377 | 0.802 / 0.910 | -0.12756 [-0.28994, +0.02227] |  | rejected |
| prospective | E_lightgbm | 116 | 4.9052 | 6.3651 | +0.1914 | 3.54516 | 0.845 / 0.872 | -0.06617 [-0.24778, +0.12520] |  | rejected |
| prospective | F_stack | 116 | 4.8426 | 6.2947 | +0.4159 | 3.48474 | 0.802 / 0.925 | -0.12660 [-0.28547, +0.01627] | +0.02370 [-2.34639, +2.24858] | best |

*Incumbent, holdout* — PLAYER_SIM_V1 walk-forward 2024-25 + 2025-26 (5,222 rows, 2624 games): 
  mean MAE/RMSE/bias ours 5.3499 / 6.8894 / +0.1754 vs incumbent 5.3244 / 6.8455 / +0.1757; squared-error diff +0.6019 [+0.2160, +0.9833].
  Rung RPS over 14+..40+: ours 3.57556 vs 3.54777, diff +0.02778 [+0.01179, +0.04317].
  Rung Brier (ours vs incumbent, diff CI): 20+ n=5,222: 0.1714 vs 0.1700 +0.0014 [+0.0002, +0.0026]; 25+ n=5,222: 0.2393 vs 0.2380 +0.0013 [-0.0002, +0.0029]; 30+ n=5,222: 0.1691 vs 0.1678 +0.0013 [+0.0003, +0.0024].

*Incumbent, prospective* — PLAYER_SIM_V1 prospective archive 2026-27 (78 rows, 52 games): 
  mean MAE/RMSE/bias ours 4.6998 / 6.1684 / +0.7159 vs incumbent 4.7108 / 6.1665 / +0.7218; squared-error diff +0.0237 [-2.3464, +2.2486].

### Team goals

Population: every regular-season team-game after the team's first game in the data.

| Split | Model | n | MAE | RMSE | Bias | CRPS | 80% cover / PIT var | vs A: CRPS diff (95% CI) | vs incumbent | Verdict |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| validation | A_season_avg_shrunk | 2,624 | 1.4106 | 1.7505 | +0.0279 | 0.97449 | 0.803 / 1.020 | baseline |  | baseline |
| validation | B_ewma_shrunk | 2,624 | 1.4119 | 1.7502 | +0.0338 | 0.97427 | 0.798 / 1.014 | -0.00022 [-0.00276, +0.00212] |  | rejected |
| validation | C_toi_x_rate | 2,624 | 1.4025 | 1.7348 | +0.0324 | 0.96570 | 0.791 / 1.013 | -0.00879 [-0.01567, -0.00198] |  | rejected |
| validation | D_opp_adjusted | 2,624 | 1.3993 | 1.7273 | +0.0656 | 0.96157 | 0.794 / 1.009 | -0.01292 [-0.01965, -0.00680] |  | competitive |
| validation | E_lightgbm | 2,624 | 1.4010 | 1.7460 | -0.0502 | 0.97142 | 0.791 / 1.022 | -0.00307 [-0.01459, +0.00757] |  | rejected |
| validation | F_stack | 2,624 | 1.3962 | 1.7266 | +0.0346 | 0.96086 | 0.795 / 1.009 | -0.01363 [-0.02113, -0.00666] |  | best |
| holdout | A_season_avg_shrunk | 5,246 | 1.3825 | 1.7281 | +0.0154 | 0.96197 | 0.797 / 1.009 | baseline |  | baseline |
| holdout | B_ewma_shrunk | 5,246 | 1.3828 | 1.7278 | +0.0093 | 0.96170 | 0.799 / 1.002 | -0.00027 [-0.00177, +0.00133] |  | rejected |
| holdout | C_toi_x_rate | 5,246 | 1.3798 | 1.7200 | -0.0249 | 0.95741 | 0.796 / 1.010 | -0.00456 [-0.00817, -0.00051] |  | rejected |
| holdout | D_opp_adjusted | 5,246 | 1.3828 | 1.7161 | +0.0617 | 0.95481 | 0.797 / 1.002 | -0.00717 [-0.01141, -0.00269] |  | competitive |
| holdout | E_lightgbm | 5,246 | 1.3818 | 1.7189 | +0.0202 | 0.95644 | 0.799 / 1.008 | -0.00554 [-0.01093, -0.00024] |  | rejected |
| holdout | F_stack | 5,246 | 1.3793 | 1.7135 | +0.0433 | 0.95333 | 0.797 / 1.002 | -0.00864 [-0.01269, -0.00423] | -0.00134 [-0.00379, +0.00093] | best |
| prospective | A_season_avg_shrunk | 240 | 1.4570 | 1.7837 | -0.0144 | 0.99819 | 0.812 / 1.023 | baseline |  | baseline |
| prospective | B_ewma_shrunk | 240 | 1.4560 | 1.7742 | -0.0077 | 0.99218 | 0.808 / 1.012 | -0.00601 [-0.01823, +0.00519] |  | rejected |
| prospective | C_toi_x_rate | 240 | 1.4438 | 1.7481 | -0.0042 | 0.97687 | 0.825 / 0.995 | -0.02131 [-0.04276, +0.00105] |  | rejected |
| prospective | D_opp_adjusted | 240 | 1.4429 | 1.7466 | +0.0342 | 0.97534 | 0.825 / 0.997 | -0.02285 [-0.04504, -0.00298] |  | competitive |
| prospective | E_lightgbm | 240 | 1.4494 | 1.7585 | +0.0261 | 0.98133 | 0.808 / 1.003 | -0.01686 [-0.03889, +0.00530] |  | rejected |
| prospective | F_stack | 240 | 1.4437 | 1.7470 | +0.0285 | 0.97547 | 0.821 / 0.996 | -0.02272 [-0.04382, -0.00279] |  | best |

*Incumbent, holdout* — DATA_ONLY_V2 SIM2_ST walk-forward 2024-25 + 2025-26 (5,246 rows, 2624 games): 
  mean MAE/RMSE/bias ours 1.3793 / 1.7135 / +0.0433 vs incumbent 1.3819 / 1.7150 / +0.0708; squared-error diff -0.0052 [-0.0248, +0.0147].
  Rung RPS over 3+..4+: ours 0.46597 vs 0.46731, diff -0.00134 [-0.00379, +0.00093].
  Rung Brier (ours vs incumbent, diff CI): 3+ n=5,246: 0.2372 vs 0.2372 -0.0001 [-0.0014, +0.0012]; 4+ n=5,246: 0.2288 vs 0.2301 -0.0013 [-0.0026, +0.0000].

A note on MAE: MAE rewards the median, not the mean; for skewed counts a mean forecast can lose on MAE while winning on RMSE/CRPS (PR #28 saw the same). CRPS and log score are the decision metrics.

## 6. Opponent adjustment

Opponent strength is a schedule-adjusted ridge rating (y = mu + off + def + home, refitted before every game date on all earlier games, previous seasons weighted 0.5 per season; alpha chosen on development: shots 3, goals 30, xG 3). Skater factor = (mu + opponent defence) / mu, applied as factor^beta with beta fitted on development (shots 0.95; goals/assists/points 1.20/1.30/1.26 on the goal rating, which beat the xG rating on development likelihood). Paired D - C CRPS (validation / holdout): sog -0.00197 [-0.00266, -0.00128] / -0.00175 [-0.00217, -0.00132]; goals -0.00016 [-0.00030, -0.00002] / -0.00006 [-0.00015, +0.00001]; assists -0.00035 [-0.00065, -0.00002] / -0.00021 [-0.00038, -0.00003]; points -0.00076 [-0.00135, -0.00017] / -0.00040 [-0.00072, -0.00008]. The step is clearly useful for shots, smaller for assists/points, and not confirmed on holdout for goals. A raw shrunk 'allowed' factor performs the same as the schedule-adjusted one (CIs include 0). Saves D uses ridge shots-against recentred on the recent league level (dev scale 0.938); team goals D blends ridge goals and xG ratings (goal weight 0.75).

| Family | Factor | beta (dev) | Validation CRPS C -> D | D vs A (validation) |
|---|---|---:|---|---|
| sog | sog_for_oppf | 0.955 | 0.71313 -> 0.71117 | -0.00587 [-0.00695, -0.00480] |
| goals | goals_for_oppf | 1.198 | 0.13896 -> 0.13880 | -0.00075 [-0.00096, -0.00053] |
| assists | goals_for_oppf | 1.302 | 0.21384 -> 0.21350 | -0.00176 [-0.00217, -0.00133] |
| points | goals_for_oppf | 1.263 | 0.30095 -> 0.30019 | -0.00241 [-0.00311, -0.00166] |

* sog: ridge vs raw opponent factor CRPS diff +0.00007 [-0.00037, +0.00050] (tie); ridge vs no adjustment -0.00197 [-0.00266, -0.00128].
* points: ridge vs raw opponent factor CRPS diff -0.00008 [-0.00046, +0.00030] (tie); ridge vs no adjustment -0.00076 [-0.00135, -0.00017].

## 7. Distributions and calibration

| Family | Split | Distribution | CRPS | log score | 80% cover | PIT var ratio | P(0) pred / obs |
|---|---|---|---:|---:|---:|---:|---|
| Shots on goal | validation | poisson | 0.71097 | 1.5778 | 0.788 | 1.033 | 0.224 / 0.246 |
| Shots on goal | validation | nb | 0.71048 | 1.5761 | 0.804 | 0.995 | 0.236 / 0.246 |
| Shots on goal | validation | nb_binned | 0.71035 | 1.5759 | 0.806 | 0.991 | 0.239 / 0.246 |
| Shots on goal | holdout | poisson | 0.68550 | 1.5394 | 0.788 | 1.030 | 0.244 / 0.269 |
| Shots on goal | holdout | nb | 0.68479 | 1.5371 | 0.802 | 0.996 | 0.256 / 0.269 |
| Shots on goal | holdout | nb_binned | 0.68468 | 1.5368 | 0.804 | 0.991 | 0.259 / 0.269 |
| Goals | validation | poisson | 0.13851 | 0.4493 | 0.800 | 0.990 | 0.845 / 0.849 |
| Goals | validation | nb | 0.13851 | 0.4493 | 0.800 | 0.990 | 0.845 / 0.849 |
| Goals | validation | nb_binned | 0.13851 | 0.4494 | 0.800 | 0.991 | 0.845 / 0.849 |
| Goals | holdout | poisson | 0.13687 | 0.4454 | 0.800 | 0.997 | 0.850 / 0.849 |
| Goals | holdout | nb | 0.13687 | 0.4454 | 0.800 | 0.997 | 0.850 / 0.849 |
| Goals | holdout | nb_binned | 0.13687 | 0.4454 | 0.799 | 0.997 | 0.851 / 0.849 |
| Assists | validation | poisson | 0.21317 | 0.6383 | 0.802 | 0.989 | 0.755 / 0.760 |
| Assists | validation | nb | 0.21317 | 0.6383 | 0.802 | 0.989 | 0.756 / 0.760 |
| Assists | validation | nb_binned | 0.21316 | 0.6383 | 0.802 | 0.989 | 0.756 / 0.760 |
| Assists | holdout | poisson | 0.21174 | 0.6352 | 0.799 | 0.996 | 0.759 / 0.761 |
| Assists | holdout | nb | 0.21175 | 0.6352 | 0.799 | 0.996 | 0.759 / 0.761 |
| Assists | holdout | nb_binned | 0.21174 | 0.6352 | 0.799 | 0.996 | 0.760 / 0.761 |
| Points | validation | poisson | 0.29975 | 0.8336 | 0.802 | 0.992 | 0.647 / 0.654 |
| Points | validation | nb | 0.29975 | 0.8336 | 0.802 | 0.992 | 0.647 / 0.654 |
| Points | validation | nb_binned | 0.29973 | 0.8335 | 0.802 | 0.992 | 0.648 / 0.654 |
| Points | holdout | poisson | 0.29586 | 0.8270 | 0.801 | 0.992 | 0.652 / 0.655 |
| Points | holdout | nb | 0.29586 | 0.8270 | 0.801 | 0.992 | 0.652 / 0.655 |
| Points | holdout | nb_binned | 0.29585 | 0.8269 | 0.801 | 0.992 | 0.653 / 0.655 |
| Goalie saves | validation | poisson | 4.12152 | 3.6570 | 0.668 | 1.313 | 0.000 / 0.001 |
| Goalie saves | validation | nb | 4.06332 | 3.4776 | 0.810 | 0.956 | 0.000 / 0.001 |
| Goalie saves | validation | nb_binned | 4.06220 | 3.4775 | 0.807 | 0.960 | 0.000 / 0.001 |
| Goalie saves | validation | normal_binned | 4.05323 | 3.4074 | 0.814 | 0.949 | 0.000 / 0.001 |
| Goalie saves | holdout | poisson | 3.88618 | 3.5409 | 0.668 | 1.312 | 0.000 / 0.001 |
| Goalie saves | holdout | nb | 3.82690 | 3.3914 | 0.819 | 0.965 | 0.000 / 0.001 |
| Goalie saves | holdout | nb_binned | 3.82667 | 3.3927 | 0.810 | 0.985 | 0.000 / 0.001 |
| Goalie saves | holdout | normal_binned | 3.82480 | 3.3452 | 0.817 | 0.966 | 0.000 / 0.001 |
| Team goals | validation | poisson | 0.96085 | 1.9382 | 0.795 | 1.010 | 0.048 / 0.055 |
| Team goals | validation | nb | 0.96085 | 1.9382 | 0.795 | 1.010 | 0.048 / 0.055 |
| Team goals | validation | nb_binned | 0.96086 | 1.9382 | 0.795 | 1.009 | 0.048 / 0.055 |
| Team goals | holdout | poisson | 0.95335 | 1.9301 | 0.796 | 1.003 | 0.048 / 0.051 |
| Team goals | holdout | nb | 0.95335 | 1.9301 | 0.796 | 1.003 | 0.048 / 0.051 |
| Team goals | holdout | nb_binned | 0.95333 | 1.9301 | 0.797 | 1.002 | 0.048 / 0.051 |

PIT variance ratio > 1 = too narrow (overconfident), < 1 = too wide.

**Kalshi-style rungs (selected model, NB-binned), holdout:**

| Family | Rung | Brier | mean P | hit rate | ECE |
|---|---|---:|---:|---:|---:|
| Shots on goal | 2+ | 0.2098 | 0.441 | 0.430 | 0.0113 |
| Shots on goal | 3+ | 0.1467 | 0.229 | 0.220 | 0.0090 |
| Shots on goal | 4+ | 0.0814 | 0.108 | 0.102 | 0.0057 |
| Shots on goal | 5+ | 0.0398 | 0.048 | 0.045 | 0.0023 |
| Goals | 1+ | 0.1189 | 0.149 | 0.151 | 0.0038 |
| Goals | 2+ | 0.0161 | 0.017 | 0.017 | 0.0005 |
| Assists | 1+ | 0.1684 | 0.240 | 0.239 | 0.0046 |
| Assists | 2+ | 0.0373 | 0.041 | 0.041 | 0.0013 |
| Points | 1+ | 0.2014 | 0.347 | 0.345 | 0.0077 |
| Points | 2+ | 0.0733 | 0.088 | 0.088 | 0.0027 |
| Points | 3+ | 0.0177 | 0.019 | 0.019 | 0.0003 |
| Goalie saves | 20+ | 0.1714 | 0.755 | 0.771 | 0.0190 |
| Goalie saves | 25+ | 0.2393 | 0.473 | 0.485 | 0.0152 |
| Goalie saves | 30+ | 0.1691 | 0.228 | 0.227 | 0.0113 |
| Team goals | 2+ | 0.1585 | 0.809 | 0.800 | 0.0099 |
| Team goals | 3+ | 0.2372 | 0.593 | 0.594 | 0.0084 |
| Team goals | 4+ | 0.2288 | 0.373 | 0.371 | 0.0050 |
| Team goals | 5+ | 0.1572 | 0.203 | 0.199 | 0.0052 |

**Zero mass by predicted-mean quintile (validation)** — low-count families:

| Family | mean bin | n | P(0) predicted | P(0) observed |
|---|---|---:|---:|---:|
| Goals | (0.0179, 0.0702] | 9,422 | 0.953 | 0.954 |
| Goals | (0.0702, 0.12] | 9,421 | 0.910 | 0.919 |
| Goals | (0.12, 0.174] | 9,421 | 0.865 | 0.870 |
| Goals | (0.174, 0.27] | 9,421 | 0.807 | 0.811 |
| Goals | (0.27, 0.837] | 9,422 | 0.692 | 0.692 |
| Assists | (0.0543, 0.157] | 9,422 | 0.885 | 0.891 |
| Assists | (0.157, 0.216] | 9,421 | 0.832 | 0.840 |
| Assists | (0.216, 0.29] | 9,421 | 0.780 | 0.788 |
| Assists | (0.29, 0.416] | 9,421 | 0.705 | 0.712 |
| Assists | (0.416, 1.328] | 9,422 | 0.578 | 0.569 |
| Points | (0.0972, 0.241] | 9,422 | 0.826 | 0.833 |
| Points | (0.241, 0.331] | 9,421 | 0.756 | 0.767 |
| Points | (0.331, 0.472] | 9,421 | 0.674 | 0.691 |
| Points | (0.472, 0.682] | 9,421 | 0.568 | 0.574 |
| Points | (0.682, 1.881] | 9,422 | 0.416 | 0.407 |

## 8. Team goals, game totals and coherence

| Split | games | total MAE | RMSE | bias | CRPS | 80% cover | PIT var | vs DATA_ONLY_V2 total sq. error |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| development | 1,312 | 1.816 | 2.277 | +0.072 | 1.2708 | 0.843 | 0.882 | n/a |
| validation | 1,312 | 1.865 | 2.322 | +0.069 | 1.2994 | 0.837 | 0.922 | n/a |
| holdout | 2,622 | 1.858 | 2.310 | +0.086 | 1.2912 | 0.829 | 0.929 | -0.0562 [-0.0947, -0.0201] |
| prospective | 120 | 1.852 | 2.339 | +0.057 | 1.2828 | 0.858 | 0.875 | n/a |

The total is the convolution of two independent team distributions; a PIT variance ratio near 0.9 means it is too wide — real totals are less variable than two independent Poissons (regulation ties go to a sudden-death OT that adds at most one goal, shootout goals do not count). A joint model is a listed priority.

| Split | team-games | mean player goal sum | mean team model | actual | ratio mean (p10-p90) | corr | gate reconciliation |
|---|---:|---:|---:|---:|---|---:|---|
| development | 2,624 | 3.254 | 3.179 | 3.143 | 1.023 (0.94-1.11) | 0.886 | PASS 96.3%, REVIEW 3.6%, BLOCK 0.0% |
| validation | 2,624 | 3.155 | 3.116 | 3.082 | 1.012 (0.94-1.09) | 0.904 | PASS 97.4%, REVIEW 2.5%, BLOCK 0.0% |
| holdout | 5,248 | 3.026 | 3.090 | 3.046 | 0.979 (0.90-1.06) | 0.827 | PASS 96.9%, REVIEW 3.0%, BLOCK 0.1% |
| prospective | 240 | 3.135 | 3.129 | 3.100 | 1.002 (0.92-1.08) | 0.831 | PASS 98.8%, REVIEW 1.2% |

Player goal means are modelled independently of the team model and reconcile within 15% for ~97% of team-games; the forward projector reports both and flags disagreement through `pf_core.gate.team_reconciliation`.

## 9. Where the errors come from

| Pattern | Frequency | Impact | Cause | Status | Action |
|---|---|---|---|---|---|
| Pulled starting goalies | 6.4% of starts (validation) | 30% of saves squared error; bias +14.5 saves when pulled | Saves mean assumes a full game; the pull is a game-script event | verified defect | Mixture with a pull hazard driven by projected goals against (as PLAYER_SIM_V1 does) — priority 1 |
| League level drift (saves) | every start; league SOG/team-game 31.6 -> 27.7 (2021-26) | validation saves bias +0.68 before the fix, +0.21 after | expanding-mean priors and season-decayed ridge intercepts lag a moving league level | verified defect | fixed: rolling 1,200-start league level (nhl.ladder.recent_prior) |
| Opportunity misprojection (TOI off by > 3 min) | 18.6% of skater-games | 21% of SOG squared error; an oracle TOI would remove only 4.4% of SOG MSE | injuries in-game, penalties, blowouts, OT | hypothesis | small upside; archived PP-unit news is the realistic lever |
| Top-line TOI under-projection | F1 role, 7,867 validation skater-games | TOI bias -0.27 min | shrinkage toward the role prior | hypothesis | role-specific calibration of T_E (validation-only fit) |
| Blowouts (final margin >= 3) | 41% of skater-games | 47% of points squared error, bias -0.022 | outcome-driven (post-game); pregame models cannot see it | ruled out | none (variance, not bias) |
| Overtime games | 22% of skater-games | SOG bias -0.060, TOI bias -0.43 min | extra ~4 min of 3-on-3; the mean already carries the OT expectation | ruled out | none for means; matters for the game-total distribution |
| Line changes / PP-unit changes vs last game | 34% / 34% of skater-games | MAE lower than the rest (1.048 vs 1.071); PIT line-change factor CRPS -0.000050 [-0.000094, -0.000007] | changes concentrate on depth players with small means | ruled out | none (gain < 0.01% CRPS) |
| Back-to-backs | 15% of skater-games | SOG bias +0.057; dev-fitted factor 0.960 -> validation CRPS -0.000020 [-0.000167, +0.000146] | fatigue effect too small to estimate | ruled out | none (LightGBM sees b2b as a feature) |
| Injury returns / scratches (missed team games) | 4.6% | bias +0.046; fix CRPS -0.000030 [-0.000074, +0.000017] | returning players' role is slightly lower | ruled out | none |
| New team (trade/signing) | 0.6% | SOG bias +0.082, TOI bias +0.19 min | role on a new team is unknown from history | hypothesis | use archived DailyFaceoff lines for new-team players (2026-27 onward) |
| Game-total distribution too wide | every game | validation total PIT variance ratio 0.922, 80% coverage 0.837 | independent team draws ignore OT/shootout structure (negative dependence) | hypothesis | joint team-goals model (bivariate / simulation) before publishing totals ladders |
| pf_core group_prior_pit look-ahead fallback | rows on a group's first date | found by a poisoned-future unit test; no effect on scored rows | fallback = full-sample mean | verified defect | worked around (development-only fallback); reported to the pf_core owner |

Segment detail (validation + development 2022-24, selected model, shots and points):

| Family | Pattern | n | share | bias | MAE | MAE rest | share of sq. error | TOI bias |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Shots on goal | line_changed_vs_last_game (post-game) | 31,976 | 0.340 | +0.0325 | 1.0477 | 1.0708 | 0.330 | +0.03 |
| Shots on goal | pp_unit_changed (post-game) | 32,087 | 0.341 | +0.0314 | 1.0416 | 1.0740 | 0.322 | +0.05 |
| Shots on goal | returning_from_absence>=1 team game (PIT) | 4,292 | 0.046 | +0.0456 | 0.9019 | 1.0707 | 0.033 | +0.13 |
| Shots on goal | new_team (PIT) | 521 | 0.006 | +0.0817 | 0.9908 | 1.0634 | 0.005 | +0.19 |
| Shots on goal | team_back_to_back (PIT) | 13,811 | 0.147 | +0.0574 | 1.0549 | 1.0644 | 0.144 | +0.05 |
| Shots on goal | blowout \|margin\|>=3 (post-game) | 39,042 | 0.415 | +0.0412 | 1.0589 | 1.0659 | 0.407 | +0.13 |
| Shots on goal | overtime game (post-game) | 20,600 | 0.219 | -0.0601 | 1.0806 | 1.0580 | 0.232 | -0.43 |
| Shots on goal | toi_miss>3min (post-game) | 17,555 | 0.186 | +0.0241 | 1.1098 | 1.0523 | 0.206 | +0.11 |
| Shots on goal | early season <=10 player games (PIT) | 2,265 | 0.024 | +0.0854 | 0.8995 | 1.0670 | 0.017 | +0.12 |
| Points | line_changed_vs_last_game (post-game) | 31,976 | 0.340 | +0.0237 | 0.5097 | 0.5398 | 0.312 | +0.03 |
| Points | pp_unit_changed (post-game) | 32,087 | 0.341 | +0.0162 | 0.5109 | 0.5392 | 0.302 | +0.05 |
| Points | returning_from_absence>=1 team game (PIT) | 4,292 | 0.046 | +0.0147 | 0.4089 | 0.5354 | 0.030 | +0.13 |
| Points | new_team (PIT) | 521 | 0.006 | +0.0740 | 0.4272 | 0.5302 | 0.004 | +0.19 |
| Points | team_back_to_back (PIT) | 13,811 | 0.147 | +0.0334 | 0.5193 | 0.5314 | 0.139 | +0.05 |
| Points | blowout \|margin\|>=3 (post-game) | 39,042 | 0.415 | -0.0218 | 0.5530 | 0.5131 | 0.470 | +0.13 |
| Points | overtime game (post-game) | 20,600 | 0.219 | +0.0115 | 0.5194 | 0.5325 | 0.207 | -0.43 |
| Points | toi_miss>3min (post-game) | 17,555 | 0.186 | +0.0076 | 0.5189 | 0.5320 | 0.185 | +0.11 |
| Points | early season <=10 player games (PIT) | 2,265 | 0.024 | +0.0309 | 0.3952 | 0.5329 | 0.014 | +0.12 |

Saves: pulled starters are 6.4% of validation starts but 30% of squared error (bias +14.5 saves when pulled vs -0.77 otherwise). Knowing the realised shots against would cut saves MSE from 53.9 to 2.7: saves error is volume, not save percentage.

## 10. Experiments

**NHL-X01-xg** — *Does an own shot-quality (xG) model add information over shot counts?*  
Hypothesis: Distance/angle/type/strength/rebound logistic xG beats a constant goal rate out of sample.  
Method: Logistic regression on unblocked attempts, fitted on 2021-22 + 2022-23 only, frozen.  
Data: 114,836 validation attempts (2023-24); 224,318 holdout  
Result: log loss validation 0.2250 vs constant 0.2547; holdout 0.2298 vs 0.2569; holdout xG sum 16915 vs 15987 goals (league finishing fell).  
Interpretation: xG is informative and is used as lagged player/team shot-quality features (E) and as a team-goals rating input (D); its level drifts, so it is never used as an absolute rate.  
Decision: **adopt**

**NHL-X02-toi-ladder** — *Which time-on-ice model should drive every skater family?*  
Hypothesis: A role-aware model (previous game's line/PP unit from shift data) beats recency averages.  
Method: T_A season avg, T_B EWMA, T_C role share x team minutes, T_E LightGBM (season-blocked refits).  
Data: skater-games with >= 1 prior game; validation 2023-24, holdout 2024-26  
Result: validation total-TOI MAE A 1.980 / B 1.872 / C 1.871 / E 1.854 min; holdout E 1.821 vs B 1.844; PP-TOI MAE E 0.768 vs C 0.767.  
Interpretation: LightGBM on role features is best for total TOI; PP TOI is a tie between the share model and E.  
Decision: **adopt**

**NHL-X03-toi-source-sog** — *Does the better TOI forecast improve sog (model C)?*  
Hypothesis: Better opportunity -> better counts.  
Method: C with T_E minutes vs C with T_C minutes, paired CRPS on validation, game-clustered bootstrap.  
Data: validation 2023-24  
Result: CRPS(T_E) - CRPS(T_C) = -0.00084 [-0.00121, -0.00044]  
Interpretation: Helps shots (volume follows ice time).  
Decision: **adopt**

**NHL-X03-toi-source-points** — *Does the better TOI forecast improve points (model C)?*  
Hypothesis: Better opportunity -> better counts.  
Method: C with T_E minutes vs C with T_C minutes, paired CRPS on validation, game-clustered bootstrap.  
Data: validation 2023-24  
Result: CRPS(T_E) - CRPS(T_C) = -0.00004 [-0.00022, +0.00015]  
Interpretation: No measurable effect: point production is dominated by count noise, not minutes.  
Decision: **insufficient evidence**

**NHL-X04-opponent-sog** — *Does the schedule-adjusted opponent factor improve sog?*  
Hypothesis: Opponent suppression (ridge rating of shots / goals allowed) moves player outcomes.  
Method: D = C x factor^beta x venue; beta fitted on development (0.95, factor sog_for_oppf); validation CRPS vs A.  
Data: validation 2023-24 / holdout 2024-26  
Result: validation CRPS C 0.71313 -> D 0.71117; paired D - C validation -0.00197 [-0.00266, -0.00128], holdout -0.00175 [-0.00217, -0.00132]  
Interpretation: The opponent/venue step helps on validation and holdout. beta ~1 for shots, >1 for scoring (the ridge goal rating is heavily pooled, so its spread understates the true opponent effect).  
Decision: **adopt**

**NHL-X04-opponent-goals** — *Does the schedule-adjusted opponent factor improve goals?*  
Hypothesis: Opponent suppression (ridge rating of shots / goals allowed) moves player outcomes.  
Method: D = C x factor^beta x venue; beta fitted on development (1.20, factor goals_for_oppf); validation CRPS vs A.  
Data: validation 2023-24 / holdout 2024-26  
Result: validation CRPS C 0.13896 -> D 0.13880; paired D - C validation -0.00016 [-0.00030, -0.00002], holdout -0.00006 [-0.00015, +0.00001]  
Interpretation: The opponent/venue step helps on validation; not confirmed on holdout. beta ~1 for shots, >1 for scoring (the ridge goal rating is heavily pooled, so its spread understates the true opponent effect).  
Decision: **adopt**

**NHL-X04-opponent-assists** — *Does the schedule-adjusted opponent factor improve assists?*  
Hypothesis: Opponent suppression (ridge rating of shots / goals allowed) moves player outcomes.  
Method: D = C x factor^beta x venue; beta fitted on development (1.30, factor goals_for_oppf); validation CRPS vs A.  
Data: validation 2023-24 / holdout 2024-26  
Result: validation CRPS C 0.21384 -> D 0.21350; paired D - C validation -0.00035 [-0.00065, -0.00002], holdout -0.00021 [-0.00038, -0.00003]  
Interpretation: The opponent/venue step helps on validation and holdout. beta ~1 for shots, >1 for scoring (the ridge goal rating is heavily pooled, so its spread understates the true opponent effect).  
Decision: **adopt**

**NHL-X04-opponent-points** — *Does the schedule-adjusted opponent factor improve points?*  
Hypothesis: Opponent suppression (ridge rating of shots / goals allowed) moves player outcomes.  
Method: D = C x factor^beta x venue; beta fitted on development (1.26, factor goals_for_oppf); validation CRPS vs A.  
Data: validation 2023-24 / holdout 2024-26  
Result: validation CRPS C 0.30095 -> D 0.30019; paired D - C validation -0.00076 [-0.00135, -0.00017], holdout -0.00040 [-0.00072, -0.00008]  
Interpretation: The opponent/venue step helps on validation and holdout. beta ~1 for shots, >1 for scoring (the ridge goal rating is heavily pooled, so its spread understates the true opponent effect).  
Decision: **adopt**

**NHL-X05-ridge-vs-raw-sog** — *Is the schedule-adjusted (ridge) opponent rating better than a raw shrunk 'allowed' rate?*  
Hypothesis: Strength-of-schedule adjustment matters.  
Method: Same D model with pf_core.rolling_opponent_allowed (season-to-date, k=10) instead of ridge; beta refit on development.  
Data: validation 2023-24  
Result: CRPS ridge - raw = +0.00007 [-0.00037, +0.00050]; both beat C (-0.00197 [-0.00266, -0.00128] for ridge)  
Interpretation: The adjustment matters; how it is schedule-adjusted does not, at player level.  
Decision: **insufficient evidence**

**NHL-X05-ridge-vs-raw-points** — *Is the schedule-adjusted (ridge) opponent rating better than a raw shrunk 'allowed' rate?*  
Hypothesis: Strength-of-schedule adjustment matters.  
Method: Same D model with pf_core.rolling_opponent_allowed (season-to-date, k=10) instead of ridge; beta refit on development.  
Data: validation 2023-24  
Result: CRPS ridge - raw = -0.00008 [-0.00046, +0.00030]; both beat C (-0.00076 [-0.00135, -0.00017] for ridge)  
Interpretation: The adjustment matters; how it is schedule-adjusted does not, at player level.  
Decision: **insufficient evidence**

**NHL-X06-ml-stack-sog** — *Do LightGBM (E) and the stack (F) beat the structural model (D) for sog?*  
Hypothesis: Non-linear interactions of PIT features add accuracy beyond TOI x rate x opponent.  
Method: LightGBM Poisson, refitted walk-forward by season on all earlier seasons; F = NNLS weights on A..E fitted on 2022-23 only.  
Data: validation 2023-24  
Result: validation CRPS D 0.71117, E 0.71056, F 0.71035; F vs A -0.00669 [-0.00769, -0.00568]  
Interpretation: F is selected on validation; the gain over D is small for skaters (the outcome is mostly count noise).  
Decision: **adopt**

**NHL-X06-ml-stack-goals** — *Do LightGBM (E) and the stack (F) beat the structural model (D) for goals?*  
Hypothesis: Non-linear interactions of PIT features add accuracy beyond TOI x rate x opponent.  
Method: LightGBM Poisson, refitted walk-forward by season on all earlier seasons; F = NNLS weights on A..E fitted on 2022-23 only.  
Data: validation 2023-24  
Result: validation CRPS D 0.13880, E 0.13864, F 0.13851; F vs A -0.00103 [-0.00128, -0.00079]  
Interpretation: F is selected on validation; the gain over D is small for skaters (the outcome is mostly count noise).  
Decision: **adopt**

**NHL-X06-ml-stack-assists** — *Do LightGBM (E) and the stack (F) beat the structural model (D) for assists?*  
Hypothesis: Non-linear interactions of PIT features add accuracy beyond TOI x rate x opponent.  
Method: LightGBM Poisson, refitted walk-forward by season on all earlier seasons; F = NNLS weights on A..E fitted on 2022-23 only.  
Data: validation 2023-24  
Result: validation CRPS D 0.21350, E 0.21334, F 0.21316; F vs A -0.00209 [-0.00252, -0.00168]  
Interpretation: F is selected on validation; the gain over D is small for skaters (the outcome is mostly count noise).  
Decision: **adopt**

**NHL-X06-ml-stack-points** — *Do LightGBM (E) and the stack (F) beat the structural model (D) for points?*  
Hypothesis: Non-linear interactions of PIT features add accuracy beyond TOI x rate x opponent.  
Method: LightGBM Poisson, refitted walk-forward by season on all earlier seasons; F = NNLS weights on A..E fitted on 2022-23 only.  
Data: validation 2023-24  
Result: validation CRPS D 0.30019, E 0.30017, F 0.29973; F vs A -0.00287 [-0.00362, -0.00210]  
Interpretation: F is selected on validation; the gain over D is small for skaters (the outcome is mostly count noise).  
Decision: **adopt**

**NHL-X06-ml-stack-saves** — *Do LightGBM (E) and the stack (F) beat the structural model (D) for saves?*  
Hypothesis: Non-linear interactions of PIT features add accuracy beyond TOI x rate x opponent.  
Method: LightGBM Poisson, refitted walk-forward by season on all earlier seasons; F = NNLS weights on A..E fitted on 2022-23 only.  
Data: validation 2023-24  
Result: validation CRPS D 4.07086, E 4.12135, F 4.06220; F vs A -0.11947 [-0.16222, -0.06917]  
Interpretation: F is selected on validation; the gain over D is small for skaters (the outcome is mostly count noise).  
Decision: **adopt**

**NHL-X06-ml-stack-team_goals** — *Do LightGBM (E) and the stack (F) beat the structural model (D) for team_goals?*  
Hypothesis: Non-linear interactions of PIT features add accuracy beyond TOI x rate x opponent.  
Method: LightGBM Poisson, refitted walk-forward by season on all earlier seasons; F = NNLS weights on A..E fitted on 2022-23 only.  
Data: validation 2023-24  
Result: validation CRPS D 0.96157, E 0.97142, F 0.96086; F vs A -0.01363 [-0.02113, -0.00666]  
Interpretation: F is selected on validation; the gain over D is small for skaters (the outcome is mostly count noise).  
Decision: **adopt**

**NHL-X07-dist-sog** — *Which outcome distribution for sog?*  
Hypothesis: Over-dispersion matters for shots/saves; goals-type counts are near Poisson.  
Method: Poisson / NB (one alpha) / NB with mean-binned alpha, dispersion fitted on development residuals of the selected mean.  
Data: validation 2023-24  
Result: poisson: CRPS 0.71097, 80% cover 0.788, PIT var 1.033; nb: CRPS 0.71048, 80% cover 0.804, PIT var 0.995; nb_binned: CRPS 0.71035, 80% cover 0.806, PIT var 0.991  
Interpretation: NB-binned kept for all (it nests Poisson); it matters for SOG and saves only.  
Decision: **adopt**

**NHL-X07-dist-goals** — *Which outcome distribution for goals?*  
Hypothesis: Over-dispersion matters for shots/saves; goals-type counts are near Poisson.  
Method: Poisson / NB (one alpha) / NB with mean-binned alpha, dispersion fitted on development residuals of the selected mean.  
Data: validation 2023-24  
Result: poisson: CRPS 0.13851, 80% cover 0.800, PIT var 0.990; nb: CRPS 0.13851, 80% cover 0.800, PIT var 0.990; nb_binned: CRPS 0.13851, 80% cover 0.800, PIT var 0.991  
Interpretation: NB-binned kept for all (it nests Poisson); it matters for SOG and saves only.  
Decision: **adopt**

**NHL-X07-dist-assists** — *Which outcome distribution for assists?*  
Hypothesis: Over-dispersion matters for shots/saves; goals-type counts are near Poisson.  
Method: Poisson / NB (one alpha) / NB with mean-binned alpha, dispersion fitted on development residuals of the selected mean.  
Data: validation 2023-24  
Result: poisson: CRPS 0.21317, 80% cover 0.802, PIT var 0.989; nb: CRPS 0.21317, 80% cover 0.802, PIT var 0.989; nb_binned: CRPS 0.21316, 80% cover 0.802, PIT var 0.989  
Interpretation: NB-binned kept for all (it nests Poisson); it matters for SOG and saves only.  
Decision: **adopt**

**NHL-X07-dist-points** — *Which outcome distribution for points?*  
Hypothesis: Over-dispersion matters for shots/saves; goals-type counts are near Poisson.  
Method: Poisson / NB (one alpha) / NB with mean-binned alpha, dispersion fitted on development residuals of the selected mean.  
Data: validation 2023-24  
Result: poisson: CRPS 0.29975, 80% cover 0.802, PIT var 0.992; nb: CRPS 0.29975, 80% cover 0.802, PIT var 0.992; nb_binned: CRPS 0.29973, 80% cover 0.802, PIT var 0.992  
Interpretation: NB-binned kept for all (it nests Poisson); it matters for SOG and saves only.  
Decision: **adopt**

**NHL-X07-dist-saves** — *Which outcome distribution for saves?*  
Hypothesis: Over-dispersion matters for shots/saves; goals-type counts are near Poisson.  
Method: Poisson / NB (one alpha) / NB with mean-binned alpha / binned normal, dispersion fitted on development residuals of the selected mean.  
Data: validation 2023-24  
Result: poisson: CRPS 4.12152, 80% cover 0.668, PIT var 1.313; nb: CRPS 4.06332, 80% cover 0.810, PIT var 0.956; nb_binned: CRPS 4.06220, 80% cover 0.807, PIT var 0.960; normal_binned: CRPS 4.05323, 80% cover 0.814, PIT var 0.949  
Interpretation: NB-binned kept for all (it nests Poisson); it matters for SOG and saves only.  
Decision: **adopt**

**NHL-X07-dist-team_goals** — *Which outcome distribution for team_goals?*  
Hypothesis: Over-dispersion matters for shots/saves; goals-type counts are near Poisson.  
Method: Poisson / NB (one alpha) / NB with mean-binned alpha, dispersion fitted on development residuals of the selected mean.  
Data: validation 2023-24  
Result: poisson: CRPS 0.96085, 80% cover 0.795, PIT var 1.010; nb: CRPS 0.96085, 80% cover 0.795, PIT var 1.010; nb_binned: CRPS 0.96086, 80% cover 0.795, PIT var 1.009  
Interpretation: NB-binned kept for all (it nests Poisson); it matters for SOG and saves only.  
Decision: **adopt**

**NHL-X08-fix-sog-b2b** — *Does a b2b adjustment fix a recurring sog error?*  
Hypothesis: A PIT-known situation carries a systematic bias.  
Method: Multiplicative factor fitted on 2022-23 rows of the segment (0.960, n=7361), applied to validation; paired CRPS.  
Data: validation segment n=6450  
Result: all-row CRPS diff -0.000020 [-0.000167, +0.000146]; segment -0.00015 [-0.00118, +0.00101]  
Interpretation: No validated gain.  
Decision: **reject**

**NHL-X08-fix-sog-returning_from_absence** — *Does a returning_from_absence adjustment fix a recurring sog error?*  
Hypothesis: A PIT-known situation carries a systematic bias.  
Method: Multiplicative factor fitted on 2022-23 rows of the segment (0.972, n=2086), applied to validation; paired CRPS.  
Data: validation segment n=2206  
Result: all-row CRPS diff -0.000030 [-0.000074, +0.000017]; segment -0.00064 [-0.00159, +0.00029]  
Interpretation: No validated gain.  
Decision: **reject**

**NHL-X08-fix-sog-new_team** — *Does a new_team adjustment fix a recurring sog error?*  
Hypothesis: A PIT-known situation carries a systematic bias.  
Method: Multiplicative factor fitted on 2022-23 rows of the segment (0.933, n=260), applied to validation; paired CRPS.  
Data: validation segment n=261  
Result: all-row CRPS diff -0.000003 [-0.000039, +0.000037]; segment -0.00063 [-0.00757, +0.00608]  
Interpretation: No validated gain.  
Decision: **reject**

**NHL-X08-fix-sog-early_season** — *Does a early_season adjustment fix a recurring sog error?*  
Hypothesis: A PIT-known situation carries a systematic bias.  
Method: Multiplicative factor fitted on 2022-23 rows of the segment (0.955, n=1315), applied to validation; paired CRPS.  
Data: validation segment n=950  
Result: all-row CRPS diff -0.000060 [-0.000103, -0.000014]; segment -0.00296 [-0.00518, -0.00076]  
Interpretation: Statistically detectable but < 0.01% of CRPS: economically negligible.  
Decision: **reject**

**NHL-X08-fix-sog-line_changed_last_game_PIT** — *Does a line_changed_last_game_PIT adjustment fix a recurring sog error?*  
Hypothesis: A PIT-known situation carries a systematic bias.  
Method: Multiplicative factor fitted on 2022-23 rows of the segment (0.992, n=15876), applied to validation; paired CRPS.  
Data: validation segment n=15986  
Result: all-row CRPS diff -0.000050 [-0.000094, -0.000007]; segment -0.00015 [-0.00029, -0.00003]  
Interpretation: Statistically detectable but < 0.01% of CRPS: economically negligible.  
Decision: **reject**

**NHL-X08-fix-points-b2b** — *Does a b2b adjustment fix a recurring points error?*  
Hypothesis: A PIT-known situation carries a systematic bias.  
Method: Multiplicative factor fitted on 2022-23 rows of the segment (0.914, n=7361), applied to validation; paired CRPS.  
Data: validation segment n=6450  
Result: all-row CRPS diff -0.000030 [-0.000184, +0.000117]; segment -0.00022 [-0.00144, +0.00095]  
Interpretation: No validated gain.  
Decision: **reject**

**NHL-X08-fix-points-returning_from_absence** — *Does a returning_from_absence adjustment fix a recurring points error?*  
Hypothesis: A PIT-known situation carries a systematic bias.  
Method: Multiplicative factor fitted on 2022-23 rows of the segment (0.959, n=2086), applied to validation; paired CRPS.  
Data: validation segment n=2206  
Result: all-row CRPS diff -0.000011 [-0.000029, +0.000008]; segment -0.00024 [-0.00062, +0.00015]  
Interpretation: No validated gain.  
Decision: **reject**

**NHL-X08-fix-points-new_team** — *Does a new_team adjustment fix a recurring points error?*  
Hypothesis: A PIT-known situation carries a systematic bias.  
Method: Multiplicative factor fitted on 2022-23 rows of the segment (0.837, n=260), applied to validation; paired CRPS.  
Data: validation segment n=261  
Result: all-row CRPS diff -0.000029 [-0.000056, -0.000004]; segment -0.00521 [-0.00983, -0.00077]  
Interpretation: Statistically detectable but < 0.01% of CRPS: economically negligible.  
Decision: **reject**

**NHL-X08-fix-points-early_season** — *Does a early_season adjustment fix a recurring points error?*  
Hypothesis: A PIT-known situation carries a systematic bias.  
Method: Multiplicative factor fitted on 2022-23 rows of the segment (0.886, n=1315), applied to validation; paired CRPS.  
Data: validation segment n=950  
Result: all-row CRPS diff -0.000012 [-0.000046, +0.000021]; segment -0.00059 [-0.00225, +0.00112]  
Interpretation: No validated gain.  
Decision: **reject**

**NHL-X08-fix-points-line_changed_last_game_PIT** — *Does a line_changed_last_game_PIT adjustment fix a recurring points error?*  
Hypothesis: A PIT-known situation carries a systematic bias.  
Method: Multiplicative factor fitted on 2022-23 rows of the segment (0.975, n=15876), applied to validation; paired CRPS.  
Data: validation segment n=15986  
Result: all-row CRPS diff -0.000044 [-0.000107, +0.000011]; segment -0.00013 [-0.00029, +0.00004]  
Interpretation: No validated gain.  
Decision: **reject**

**NHL-X09-saves-league-level** — *Why were frozen-scalar saves models biased upward?*  
Hypothesis: Expanding-mean league priors and season-decayed ridge intercepts lag the falling league shot level.  
Method: Replace priors by the mean of the last 1,200 starts on earlier dates and recentre ridge shots-against on the recent team level; refit scalars on development; compare on validation.  
Data: validation 2023-24 (decision); holdout re-scored once afterwards and disclosed  
Result: validation F bias +0.684 -> +0.207, RMSE 7.371 -> 7.341, CRPS 4.0639 -> 4.0622  
Interpretation: Verified level-drift defect; the fix is mechanical, not tuned on holdout. The holdout was therefore scored twice for saves (before/after); both are reported.  
Decision: **adopt**

**NHL-X10-starter-conditioning** — *How much does conditioning saves on the ACTUAL starter assume?*  
Hypothesis: Pregame starter information is nearly complete by puck drop.  
Method: Archived DailyFaceoff goalie observations (2026-27) vs the boxscore starter, last snapshot before start and fixed horizons.  
Data: 116 team-games with an archived observation  
Result: last pregame snapshot correct 1.000; at T-60 / T-180 / T-360 min: 0.991 (0.62 confirmed), 0.983 (0.54 confirmed), 0.983 (0.48 confirmed)  
Interpretation: Conditioning on the actual starter overstates certainty by ~1-2% of starts at a 1-6 h horizon; at the final pregame snapshot it is exact in this sample. Historical seasons have no PIT source.  
Decision: **insufficient evidence**

**NHL-X11-lineup-pregame** — *How well are tonight's lineup and PP1 known before puck drop?*  
Hypothesis: Projected lines identify dressed skaters and PP units.  
Method: Last archived DailyFaceoff lines before start vs boxscore (dressed) and PP-TOI top five (PP1).  
Data: 230 team-games (2026-27)  
Result: projected skaters who dressed 0.983; dressed skaters in the projection 0.976; PP1 precision 0.872, recall 0.876; median snapshot 44 min before start  
Interpretation: Lineups are ~98% knowable; PP1 is ~87% knowable. The model's PIT role uses the previous game (lines are not archived historically), so PP-unit news is an untested upside.  
Decision: **investigate**

**NHL-X12-ceiling-sog** — *How much sog error is left to remove?*  
Hypothesis: Most error is count noise; opportunity misprojection is a minority.  
Method: Validation MSE of C with projected vs realised TOI (oracle), and the Poisson floor (mean of y).  
Data: validation 2023-24  
Result: MSE C 1.8571, C with actual TOI 1.7745, best 1.8430, Poisson floor 1.6837  
Interpretation: Knowing the minutes would remove ~4.4% of shots MSE; the best model is 9.5% above a pure Poisson floor.  
Decision: **adopt**

**NHL-X12-ceiling-points** — *How much points error is left to remove?*  
Hypothesis: Most error is count noise; opportunity misprojection is a minority.  
Method: Validation MSE of C with projected vs realised TOI (oracle), and the Poisson floor (mean of y).  
Data: validation 2023-24  
Result: MSE C 0.4638, C with actual TOI 0.4659, best 0.4609, Poisson floor 0.4600  
Interpretation: Knowing the minutes would remove ~-0.4% of shots MSE; the best model is 0.2% above a pure Poisson floor.  
Decision: **adopt**

**NHL-X12-ceiling-goals** — *How much goals error is left to remove?*  
Hypothesis: Most error is count noise; opportunity misprojection is a minority.  
Method: Validation MSE of C with projected vs realised TOI (oracle), and the Poisson floor (mean of y).  
Data: validation 2023-24  
Result: MSE C 0.1741, C with actual TOI 0.1744, best 0.1734, Poisson floor 0.1714  
Interpretation: Knowing the minutes would remove ~-0.1% of shots MSE; the best model is 1.2% above a pure Poisson floor.  
Decision: **adopt**

**NHL-X12-ceiling-assists** — *How much assists error is left to remove?*  
Hypothesis: Most error is count noise; opportunity misprojection is a minority.  
Method: Validation MSE of C with projected vs realised TOI (oracle), and the Poisson floor (mean of y).  
Data: validation 2023-24  
Result: MSE C 0.2902, C with actual TOI 0.2912, best 0.2888, Poisson floor 0.2886  
Interpretation: Knowing the minutes would remove ~-0.3% of shots MSE; the best model is 0.1% above a pure Poisson floor.  
Decision: **adopt**

## 11. Failed experiments

* **Back-to-back / injury-return / early-season multiplicative fixes** — learned: Dev-fitted factors (0.92-0.97) give no or < 0.01% validation CRPS gains. Future: Schedule fatigue is not a lever for NHL player props; stop iterating on it.
* **Schedule-adjusted (ridge) vs raw opponent factor** — learned: Identical at player level (shots +0.00007 [-0.00037, +0.00050]). Future: Keep ridge for team models; the simpler raw factor is an acceptable fallback.
* **Role-share TOI (T_C) feeding points** — learned: No difference vs LightGBM TOI for points (-0.00004 [-0.00022, +0.00015]). Future: Better minutes help shots, not scoring; spend effort on rates and team environment.
* **Saves C (team shots allowed x save%)** — learned: Not better than the saves average on validation; biased high because the starter faces ~1 fewer shot than the team allows (pulls, relief). Future: Model starter shots faced directly, with a pull mixture.
* **NB vs Poisson for goals / assists / points** — learned: Fitted dispersion ~0; identical CRPS. Future: Poisson is sufficient there.
* **Saves challenger vs PLAYER_SIM_V1** — learned: Still worse on holdout (+0.0278 [+0.0118, +0.0432] rung RPS). Future: Do not replace the incumbent saves model; borrow its game-script and pull hazard.

## 12. Quality gate

pf_core.gate run on every validation (2023-24) and holdout 2025-26 skater projection of the selected model (opportunity history = previous 10 games' TOI; stat history = previous 10 games; thresholds from the pmf; opponent sample = opponent's games this season). No projection was BLOCKed (no structural defects). REVIEW (1-3%) is driven by early-season opponent factors resting on < 3 games, role changes and thin own history; REVIEW rows have LOWER error than PASS rows because they are mostly low-volume or early-season players — the gate catches structural problems, it is not an accuracy predictor. Team reconciliation (player goal sum vs team goal model) is in section 8.

| Family / split | n | PASS | REVIEW | BLOCK | top findings | CRPS PASS / REVIEW | MAE PASS / REVIEW |
|---|---:|---:|---:|---:|---|---|---|
| sog / validation | 47,107 | 98.2% | 1.8% | 0.0% | opponent:REVIEW 640, role:REVIEW 208, confidence:REVIEW 204 | 0.7110 / 0.6748 | 1.0539 / 1.0089 |
| sog / holdout | 47,114 | 98.6% | 1.4% | 0.0% | opponent:REVIEW 427, role:REVIEW 234, confidence:REVIEW 233 | 0.6820 / 0.6604 | 1.0119 / 0.9815 |
| points / validation | 47,107 | 97.0% | 3.0% | 0.0% | opponent:REVIEW 1207, role:REVIEW 208, confidence:REVIEW 204 | 0.3005 / 0.2750 | 0.5291 / 0.5108 |
| points / holdout | 47,114 | 97.6% | 2.4% | 0.0% | opponent:REVIEW 924, role:REVIEW 234, confidence:REVIEW 233 | 0.2994 / 0.2825 | 0.5244 / 0.5047 |
| goals / validation | 47,107 | 97.1% | 2.9% | 0.0% | opponent:REVIEW 1172, role:REVIEW 208, confidence:REVIEW 204 | 0.1388 / 0.1287 | 0.2711 / 0.2591 |
| goals / holdout | 47,114 | 97.7% | 2.3% | 0.0% | opponent:REVIEW 888, role:REVIEW 234, confidence:REVIEW 233 | 0.1388 / 0.1262 | 0.2677 / 0.2520 |
| assists / validation | 47,107 | 97.0% | 3.0% | 0.0% | opponent:REVIEW 1207, role:REVIEW 208, confidence:REVIEW 204 | 0.2139 / 0.1882 | 0.4033 / 0.3758 |
| assists / holdout | 47,114 | 97.6% | 2.4% | 0.0% | opponent:REVIEW 942, role:REVIEW 234, confidence:REVIEW 233 | 0.2141 / 0.2074 | 0.4010 / 0.3899 |

## 13. Readiness

| Family | Readiness | Why |
|---|---|---|
| Shots on goal | **SHADOW VALIDATION** | Beats baseline on validation and holdout, calibrated (80% coverage 0.804, PIT var 0.991), better than the incumbent on holdout; prospective 2026-27 vs incumbent -0.0082 [-0.0128, -0.0037] (better). READY requires a live shadow record from the daily workflow (none yet: it is inert until merged). |
| Goals | **SHADOW VALIDATION** | Beats baseline on validation and holdout, calibrated (80% coverage 0.799, PIT var 0.997), better than the incumbent on holdout; prospective 2026-27 vs incumbent -0.0002 [-0.0008, +0.0004] (tie). READY requires a live shadow record from the daily workflow (none yet: it is inert until merged). |
| Assists | **SHADOW VALIDATION** | Beats baseline on validation and holdout, calibrated (80% coverage 0.799, PIT var 0.996), better than the incumbent on holdout; prospective 2026-27 vs incumbent -0.0041 [-0.0070, -0.0014] (better). READY requires a live shadow record from the daily workflow (none yet: it is inert until merged). |
| Points | **SHADOW VALIDATION** | Beats baseline on validation and holdout, calibrated (80% coverage 0.801, PIT var 0.992), better than the incumbent on holdout; prospective 2026-27 vs incumbent -0.0032 [-0.0061, -0.0004] (better). READY requires a live shadow record from the daily workflow (none yet: it is inert until merged). |
| Goalie saves | **NEEDS IMPROVEMENT** | Beats our own baseline but the incumbent (PLAYER_SIM_V1 walk-forward 2024-25 + 2025-26) is better on holdout (rung RPS over 14+..40+ (CRPS restricted to the incumbent's published rungs): +0.0278 [+0.0118, +0.0432]). |
| Team goals | **SHADOW VALIDATION** | Beats baseline on validation and holdout, calibrated (80% coverage 0.797, PIT var 1.002), statistically tied with the incumbent on holdout. READY requires a live shadow record from the daily workflow (none yet: it is inert until merged). |
| Time on ice (opportunity) | **SHADOW VALIDATION** | T_E holdout MAE 1.821 min, better than PLAYER_SIM_V1 and WORKLOAD_V1; no live record yet. |

## 14. Priorities

| Rank | Item | Impact | Evidence | Complexity | Data |
|---:|---|---|---|---|---|
| 1 | Saves: pull-hazard mixture + game-script (projected goals against) on starter shots faced | only family losing to its incumbent; pulls = 30% of saves squared error | section 9; incumbent comparison in section 5 | medium | available (goalies, goals) |
| 2 | Merge and run the daily projection-foundation workflow; score every published projection | turns SHADOW VALIDATION into a live record (path to READY) | prospective 2026-27 check in section 5 | low | data-archive (already captured) |
| 3 | Use archived DailyFaceoff PP units / lines as features once >= ~500 2026-27 games exist | PP TOI and new-team roles; PP1 precision 87% | NHL-X11 | medium | archived from 2026-09-30 |
| 4 | Joint team-goals model for game totals | total PIT var ~0.92 (too wide) | section 8 | medium | available |
| 5 | Role-specific TOI calibration (top-line under-projection) | F1 TOI bias -0.27 min | section 4 | low | available |
| 6 | Extend halflife grids beyond 30 games (selected at the grid edge for B and C) | small | development grid logs | low | available |
| 7 | Publish P(start) from DailyFaceoff status with saves | 1-2% wrong-starter risk at 1-6 h | NHL-X10 | low | archived |

## 15. Shared-library (pf_core 1.0.0) issues found — not edited, worked around

* `models.group_prior_pit`: when a group has no earlier dates the default fallback is `df[col].mean()` over the whole frame — future rows included (look-ahead). Caught by our poisoned-future test; we pass a development-only fallback (`nhl.ladder.gprior`). Impact here: only rows on a group's first date (2021-22 opening night, excluded from scoring).
* `pit.rolling_opponent_allowed`: same pattern — `_league` NaN is filled with the full-sample mean of `y_col`.
* `models.group_prior_pit` and the ridge intercept are expanding / season-decayed means: correct point-in-time but they lag a drifting league level (NHL shots per team-game fell ~12% 2021-26). Not a bug, a property; documented fix `nhl.ladder.recent_prior`.
* `lagged_features` adds columns one at a time (pandas fragmentation warnings, slow on 240k x 24 columns); harmless.

## 16. Forward projections (sift.projections.v1)

`results/projections_latest.json` — 2026-10-17 regular-season slate projected from final games through 2026-10-16; lineups/starters from the newest archived pregame observation at or before 2026-10-17T07:18Z. Generated 2026-10-17T07:18:32Z, newest input 2026-10-17T05:04:04Z; 14 games, 500 shots, 500 goals, 500 assists, 500 points, 28 saves projections. Gate: PASS 1701, REVIEW 323, BLOCK 4; top findings: identity:REVIEW 168, confidence:REVIEW 142, starter:REVIEW 27, injury:REVIEW 16, role:REVIEW 8, injury:BLOCK 4. BLOCK rows (e.g. a player DailyFaceoff lists in the lineup but ESPN lists OUT) are written with their reason and must not be displayed. Every row carries `authority: research_only`, the family readiness, its opportunity (TOI with a p10-p90 range from development residuals), the opponent factor and plain-English adjustments; team rows carry the player-goal reconciliation.

## 17. Automation

`.github/workflows/projection-foundation.yml` (inert until merged; schedules fire from the default branch only): daily at 20:47 UTC from October to June plus `workflow_dispatch` (optional slate date). It sparse-checks out the inputs from data-archive (final games' player_events, schedule, DailyFaceoff lines and goalie observations, ESPN injuries), runs `python -m nhl.project` (full walk-forward rebuild, ~30-40 min on a runner), and publishes to the orphan branch `projection-data`: `projections/nhl/latest.json`, a timestamped copy `projections/nhl/<YYYY-MM-DDTHHMMZ>.json`, and `summary/nhl/latest.json`. It commits only when the projection content (ignoring timestamps) changed, pushes with retries, needs no secrets beyond the job token, and never touches betting authority. The branch is created by the workflow on its first run (not from this session).


## 18. Reproduce

```
cd research/projection_foundation
# data-archive sparse worktree (player_events, predictions_player, context/*) at .cache/archive_wt
python -m nhl.pipeline all          # features, ratings, TOI, ladders (cached in .cache/)
python -m nhl.run_walkforward       # evaluation -> results/nhl_full_results.json + experiments/
python -m nhl.report                # summary.json + RESULTS_NHL.md
python -m nhl.project               # forward projections -> results/projections_latest.json
python -m pytest tests -q
```

Runtime on a shared 4-core box: pipeline ~45 min, evaluation ~4 min. Experiment records: `results/experiments/` (72 files).
