# V2 simulator: joint game-distribution validation

incumbent `V1` (nhl-sim-1.1 on V1 rates) · unexposed seasons 2010–2022 (14841 games) · exposed [2023, 2024, 2025] · negative Δ = challenger better

## Scorecards (promotion gates G1–G10 + added J1; the scorecard recommends, a human decides)

### SIM2|overtime / regulation tie: **SHADOW_MORE**

| gate | result | detail |
|---|---|---|
| G1_primary_improvement | PASS | delta -0.0023 games[-0.0029,-0.0018] slates[-0.0029,-0.0018] |
| G2_practically_meaningful | PASS | |delta| 0.0023 vs required 0.0010 |
| G3_no_material_regression | PASS | 5 secondary metrics within margin |
| G4a_calibration | PASS | ECE challenger 0.0089 vs incumbent 0.0494 |
| G5_sample | PASS | 13 unexposed seasons, 14841 games |
| G6_season_stability | PASS | favourable in 13/13 seasons; significantly worse in none |
| G6b_exposed_not_contradicting | PASS | significantly worse in exposed seasons: none |
| G7_runtime | PASS | 2s per slate (limit 300s) |
| G8_reproducible | PASS | frozen params + seed regenerate predictions bit-for-bit |
| G9_sift_contract | pending | not yet verified |
| G10_live_non_inferior | pending | needs live shadow games |
| J1_joint_non_inferiority | PASS | joint margin and joint total Brier within 0.0020 |

### SIM2|goal-margin distribution: **RETAIN_INCUMBENT**

| gate | result | detail |
|---|---|---|
| G1_primary_improvement | FAIL | delta +0.0010 games[+0.0002,+0.0018] slates[+0.0002,+0.0018] |
| G2_practically_meaningful | FAIL | |delta| 0.0010 vs required 0.0050 |
| G3_no_material_regression | PASS | 5 secondary metrics within margin |
| G4a_calibration | PASS | ECE challenger 0.0089 vs incumbent 0.0494 |
| G5_sample | PASS | 13 unexposed seasons, 14841 games |
| G6_season_stability | FAIL | favourable in 0/13 seasons; significantly worse in none |
| G6b_exposed_not_contradicting | PASS | significantly worse in exposed seasons: none |
| G7_runtime | PASS | 2s per slate (limit 300s) |
| G8_reproducible | PASS | frozen params + seed regenerate predictions bit-for-bit |
| G9_sift_contract | pending | not yet verified |
| G10_live_non_inferior | pending | needs live shadow games |
| J1_joint_non_inferiority | PASS | joint margin and joint total Brier within 0.0020 |

### SIM2_ST|overtime / regulation tie: **SHADOW_MORE**

| gate | result | detail |
|---|---|---|
| G1_primary_improvement | PASS | delta -0.0024 games[-0.0029,-0.0018] slates[-0.0029,-0.0018] |
| G2_practically_meaningful | PASS | |delta| 0.0024 vs required 0.0010 |
| G3_no_material_regression | PASS | 5 secondary metrics within margin |
| G4a_calibration | PASS | ECE challenger 0.0087 vs incumbent 0.0494 |
| G5_sample | PASS | 13 unexposed seasons, 14841 games |
| G6_season_stability | PASS | favourable in 13/13 seasons; significantly worse in none |
| G6b_exposed_not_contradicting | PASS | significantly worse in exposed seasons: none |
| G7_runtime | PASS | 2s per slate (limit 300s) |
| G8_reproducible | PASS | frozen params + seed regenerate predictions bit-for-bit |
| G9_sift_contract | pending | not yet verified |
| G10_live_non_inferior | pending | needs live shadow games |
| J1_joint_non_inferiority | PASS | joint margin and joint total Brier within 0.0020 |

### SIM2_ST|goal-margin distribution: **RETAIN_INCUMBENT**

| gate | result | detail |
|---|---|---|
| G1_primary_improvement | FAIL | delta +0.0020 games[+0.0009,+0.0031] slates[+0.0008,+0.0032] |
| G2_practically_meaningful | FAIL | |delta| 0.0020 vs required 0.0050 |
| G3_no_material_regression | PASS | 5 secondary metrics within margin |
| G4a_calibration | PASS | ECE challenger 0.0087 vs incumbent 0.0494 |
| G5_sample | PASS | 13 unexposed seasons, 14841 games |
| G6_season_stability | FAIL | favourable in 0/13 seasons; significantly worse in none |
| G6b_exposed_not_contradicting | PASS | significantly worse in exposed seasons: none |
| G7_runtime | PASS | 2s per slate (limit 300s) |
| G8_reproducible | PASS | frozen params + seed regenerate predictions bit-for-bit |
| G9_sift_contract | pending | not yet verified |
| G10_live_non_inferior | pending | needs live shadow games |
| J1_joint_non_inferiority | PASS | joint margin and joint total Brier within 0.0020 |

## Pooled paired differences on the unexposed seasons

| challenger | metric | Δ | 95% games | 95% slates |
|---|---|---:|---|---|
| SIM2 | brier_ot | -0.0023 | [-0.0029, -0.0018] | [-0.0029, -0.0018] |
| SIM2 | brier_win | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] |
| SIM2 | rps_total | -0.0005 | [-0.0012, +0.0001] | [-0.0011, +0.0001] |
| SIM2 | rps_margin | +0.0010 | [+0.0002, +0.0018] | [+0.0002, +0.0018] |
| SIM2 | brier_over_5.5 | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0000] |
| SIM2 | brier_over_6.5 | -0.0000 | [-0.0003, +0.0002] | [-0.0003, +0.0002] |
| SIM2 | rps_margin | +0.0010 | [+0.0002, +0.0018] | [+0.0002, +0.0018] |
| SIM2 | brier_joint_margin | -0.0008 | [-0.0012, -0.0003] | [-0.0013, -0.0003] |
| SIM2 | brier_joint_total | -0.0006 | [-0.0008, -0.0004] | [-0.0008, -0.0004] |
| SIM2_ST | brier_ot | -0.0024 | [-0.0029, -0.0018] | [-0.0029, -0.0018] |
| SIM2_ST | brier_win | +0.0002 | [-0.0001, +0.0004] | [-0.0001, +0.0004] |
| SIM2_ST | rps_total | -0.0005 | [-0.0015, +0.0005] | [-0.0016, +0.0006] |
| SIM2_ST | rps_margin | +0.0020 | [+0.0009, +0.0031] | [+0.0008, +0.0032] |
| SIM2_ST | brier_over_5.5 | -0.0000 | [-0.0003, +0.0002] | [-0.0003, +0.0002] |
| SIM2_ST | brier_over_6.5 | +0.0000 | [-0.0003, +0.0003] | [-0.0003, +0.0003] |
| SIM2_ST | rps_margin | +0.0020 | [+0.0009, +0.0031] | [+0.0008, +0.0032] |
| SIM2_ST | brier_joint_margin | -0.0006 | [-0.0010, -0.0001] | [-0.0011, -0.0001] |
| SIM2_ST | brier_joint_total | -0.0005 | [-0.0008, -0.0003] | [-0.0008, -0.0003] |

## Joint-distribution levels (pooled, all seasons)

| arm | brier_joint_margin | logscore_joint_margin | brier_joint_total | logscore_joint_total |
|---|---:|---:|---:|---:|
| V1 | 0.8737 | 2.1937 | 0.9408 | 3.0387 |
| SIM2 | 0.8726 | 2.1818 | 0.9403 | 3.0275 |
| SIM2_ST | 0.8729 | 2.1823 | 0.9404 | 3.0276 |

## Overtime conditionals (predicted vs observed, pooled)

| arm | P(OT or SO) pred / obs | P(SO given tie) pred / obs |
|---|---|---|
| V1 | 0.1800 / 0.2290 | 0.3401 / 0.4035 |
| SIM2 | 0.2205 / 0.2290 | 0.4420 / 0.4035 |
| SIM2_ST | 0.2207 / 0.2290 | 0.4422 / 0.4035 |

## Per-cell reliability, joint margin partition (z of observed vs expected, pooled)

| cell | V1 | SIM2 | SIM2_ST |
|---|---:|---:|---:|
| REG_H_1 | 2545 vs 2017 (z -11.3) | 2438 vs 2017 (z -9.1) | 2441 vs 2017 (z -9.2) |
| REG_H_2 | 2341 vs 2048 (z -6.5) | 2240 vs 2048 (z -4.3) | 2244 vs 2048 (z -4.4) |
| REG_H_3+ | 3596 vs 3905 (z +5.8) | 3421 vs 3905 (z +9.2) | 3414 vs 3905 (z +9.4) |
| REG_A_1 | 2341 vs 1823 (z -11.5) | 2239 vs 1823 (z -9.4) | 2241 vs 1823 (z -9.4) |
| REG_A_2 | 1984 vs 1796 (z -4.5) | 1877 vs 1796 (z -2.0) | 1877 vs 1796 (z -2.0) |
| REG_A_3+ | 2591 vs 2888 (z +6.3) | 2423 vs 2888 (z +10.2) | 2416 vs 2888 (z +10.4) |
| OT_H | 1143 vs 1337 (z +5.9) | 1184 vs 1337 (z +4.6) | 1185 vs 1337 (z +4.6) |
| OT_A | 1087 vs 1228 (z +4.4) | 1126 vs 1228 (z +3.1) | 1127 vs 1228 (z +3.1) |
| SO_H | 581 vs 852 (z +11.4) | 925 vs 852 (z -2.5) | 926 vs 852 (z -2.5) |
| SO_A | 569 vs 883 (z +13.4) | 905 vs 883 (z -0.7) | 906 vs 883 (z -0.8) |
