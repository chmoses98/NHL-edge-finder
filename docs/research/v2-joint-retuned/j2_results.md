# J2 — retuned + recalibrated V1 rates through the V2 simulator: joint results

18777 games, seasons 2010–2025 · incumbent `V1` · negative Δ = better · 95% intervals (games | slates) · RESEARCH_ONLY, nothing is promoted

## Registered rules (decision tier CLEAN2 = 2010–2016)

* **J2-A additive: True** — keeps the win gain True (Δwin RC_SIM2 -0.0004 vs RC_SIM1 -0.0004); keeps the overtime gain True (ΔOT RC_SIM2 -0.0025 vs SIM2 -0.0025)
* **J2-C complementary: True** — joint scores not worse than both single fixes: {'brier_joint_margin': True, 'brier_joint_total': True}

| metric | RC_SIM2 Δ vs V1 | best single fix Δ | gap |
|---|---:|---:|---:|
| brier_win | -0.0004 | -0.0004 | +0.0000 |
| brier_ot | -0.0025 | -0.0025 | -0.0001 |
| rps_total | -0.0015 | -0.0014 | -0.0000 |
| rps_margin | -0.0007 | -0.0012 | +0.0005 |

### Paired RC_SIM2 against the single fixes (CLEAN2)

| comparison | metric | Δ | 95% games | 95% slates |
|---|---|---:|---|---|
| RC_SIM2_minus_RC_SIM1 | brier_win | +0.0000 | [-0.0002, +0.0003] | [-0.0002, +0.0003] |
| RC_SIM2_minus_RC_SIM1 | brier_ot | -0.0026 | [-0.0034, -0.0018] | [-0.0034, -0.0018] |
| RC_SIM2_minus_RC_SIM1 | rps_total | -0.0000 | [-0.0009, +0.0008] | [-0.0009, +0.0008] |
| RC_SIM2_minus_RC_SIM1 | rps_margin | +0.0005 | [-0.0007, +0.0016] | [-0.0007, +0.0017] |
| RC_SIM2_minus_RC_SIM1 | brier_joint_margin | -0.0009 | [-0.0016, -0.0001] | [-0.0016, -0.0001] |
| RC_SIM2_minus_RC_SIM1 | brier_joint_total | -0.0008 | [-0.0011, -0.0005] | [-0.0011, -0.0005] |
| RC_SIM2_minus_SIM2 | brier_win | -0.0004 | [-0.0009, +0.0001] | [-0.0009, +0.0001] |
| RC_SIM2_minus_SIM2 | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] |
| RC_SIM2_minus_SIM2 | rps_total | -0.0011 | [-0.0027, +0.0004] | [-0.0027, +0.0004] |
| RC_SIM2_minus_SIM2 | rps_margin | -0.0017 | [-0.0033, +0.0001] | [-0.0034, -0.0000] |
| RC_SIM2_minus_SIM2 | brier_joint_margin | -0.0005 | [-0.0010, -0.0001] | [-0.0010, -0.0001] |
| RC_SIM2_minus_SIM2 | brier_joint_total | -0.0003 | [-0.0006, +0.0000] | [-0.0006, +0.0000] |
| RC_SIM2_minus_R_SIM2 | brier_win | -0.0002 | [-0.0004, +0.0001] | [-0.0004, +0.0000] |
| RC_SIM2_minus_R_SIM2 | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] |
| RC_SIM2_minus_R_SIM2 | rps_total | -0.0012 | [-0.0028, +0.0004] | [-0.0028, +0.0004] |
| RC_SIM2_minus_R_SIM2 | rps_margin | -0.0009 | [-0.0017, -0.0001] | [-0.0017, -0.0001] |
| RC_SIM2_minus_R_SIM2 | brier_joint_margin | -0.0004 | [-0.0007, -0.0000] | [-0.0007, -0.0000] |
| RC_SIM2_minus_R_SIM2 | brier_joint_total | -0.0003 | [-0.0005, -0.0000] | [-0.0005, -0.0000] |

## Promotion scorecards for RC_SIM2 vs V1 (unchanged gates; unexposed = CLEAN2; the scorecard recommends, a human decides)

### overtime / regulation tie: **SHADOW_MORE**

| gate | result | detail |
|---|---|---|
| G1_primary_improvement | PASS | delta -0.0025 games[-0.0033,-0.0017] slates[-0.0033,-0.0017] |
| G2_practically_meaningful | PASS | |delta| 0.0025 vs required 0.0010 |
| G3_no_material_regression | PASS | 5 secondary metrics within margin |
| G4a_calibration | PASS | ECE challenger 0.0112 vs incumbent 0.0498 |
| G5_sample | PASS | 7 unexposed seasons, 7725 games |
| G6_season_stability | PASS | favourable in 7/7 seasons; significantly worse in none |
| G6b_exposed_not_contradicting | PASS | significantly worse in exposed seasons: none |
| G7_runtime | pending | not measured |
| G8_reproducible | pending | not yet demonstrated |
| G9_sift_contract | pending | not yet verified |
| G10_live_non_inferior | pending | needs live shadow games |
| J1_joint_non_inferiority | PASS | joint margin and joint total Brier within 0.0020 |

### goal-margin distribution: **RETAIN_INCUMBENT**

| gate | result | detail |
|---|---|---|
| G1_primary_improvement | FAIL | delta -0.0007 games[-0.0026,+0.0012] slates[-0.0025,+0.0011] |
| G2_practically_meaningful | FAIL | |delta| 0.0007 vs required 0.0050 |
| G3_no_material_regression | PASS | 5 secondary metrics within margin |
| G4a_calibration | PASS | ECE challenger 0.0119 vs incumbent 0.0154 |
| G5_sample | PASS | 7 unexposed seasons, 7725 games |
| G6_season_stability | FAIL | favourable in 4/7 seasons; significantly worse in none |
| G6b_exposed_not_contradicting | PASS | significantly worse in exposed seasons: none |
| G7_runtime | pending | not measured |
| G8_reproducible | pending | not yet demonstrated |
| G9_sift_contract | pending | not yet verified |
| G10_live_non_inferior | pending | needs live shadow games |
| J1_joint_non_inferiority | PASS | joint margin and joint total Brier within 0.0020 |

### win probability: **RETAIN_INCUMBENT**

| gate | result | detail |
|---|---|---|
| G1_primary_improvement | FAIL | delta -0.0004 games[-0.0009,+0.0002] slates[-0.0009,+0.0001] |
| G2_practically_meaningful | FAIL | |delta| 0.0004 vs required 0.0010 |
| G3_no_material_regression | PASS | 5 secondary metrics within margin |
| G4a_calibration | PASS | ECE challenger 0.0119 vs incumbent 0.0154 |
| G5_sample | PASS | 7 unexposed seasons, 7725 games |
| G6_season_stability | PASS | favourable in 5/7 seasons; significantly worse in none |
| G6b_exposed_not_contradicting | PASS | significantly worse in exposed seasons: none |
| G7_runtime | pending | not measured |
| G8_reproducible | pending | not yet demonstrated |
| G9_sift_contract | pending | not yet verified |
| G10_live_non_inferior | pending | needs live shadow games |
| J1_joint_non_inferiority | PASS | joint margin and joint total Brier within 0.0020 |

### total goals: **RETAIN_INCUMBENT**

| gate | result | detail |
|---|---|---|
| G1_primary_improvement | FAIL | delta -0.0015 games[-0.0033,+0.0003] slates[-0.0033,+0.0003] |
| G2_practically_meaningful | FAIL | |delta| 0.0015 vs required 0.0050 |
| G3_no_material_regression | PASS | 5 secondary metrics within margin |
| G4a_calibration | PASS | ECE challenger 0.0053 vs incumbent 0.0062 |
| G5_sample | PASS | 7 unexposed seasons, 7725 games |
| G6_season_stability | PASS | favourable in 5/7 seasons; significantly worse in none |
| G6b_exposed_not_contradicting | FAIL | significantly worse in exposed seasons: ['2018', '2021'] |
| G7_runtime | pending | not measured |
| G8_reproducible | pending | not yet demonstrated |
| G9_sift_contract | pending | not yet verified |
| G10_live_non_inferior | pending | needs live shadow games |
| J1_joint_non_inferiority | PASS | joint margin and joint total Brier within 0.0020 |

## CLEAN2_2010_2016 (n=7725)

Levels:

| arm | brier_win | logloss_win | brier_ot | rps_total | rps_margin | brier_over_5.5 | brier_over_6.5 | abs_err_total | brier_reg3 | brier_puck_line | brier_team_total | brier_joint_margin | logscore_joint_margin | brier_joint_total | logscore_joint_total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 0.2418 | 0.6766 | 0.1831 | 1.2131 | 1.2948 | 0.2445 | 0.2204 | 1.7382 | 0.6417 | 0.1902 | 0.1884 | 0.8820 | 2.2327 | 0.9436 | 3.0730 |
| SIM2 | 0.2419 | 0.6766 | 0.1807 | 1.2127 | 1.2957 | 0.2444 | 0.2205 | 1.7432 | 0.6381 | 0.1903 | 0.1883 | 0.8814 | 2.2168 | 0.9429 | 3.0541 |
| SIM2_ST | 0.2422 | 0.6773 | 0.1807 | 1.2130 | 1.2970 | 0.2447 | 0.2206 | 1.7451 | 0.6388 | 0.1905 | 0.1885 | 0.8818 | 2.2178 | 0.9430 | 3.0547 |
| R_SIM1 | 0.2415 | 0.6759 | 0.1831 | 1.2134 | 1.2937 | 0.2444 | 0.2204 | 1.7363 | 0.6414 | 0.1900 | 0.1883 | 0.8817 | 2.2317 | 0.9435 | 3.0721 |
| R_SIM2 | 0.2417 | 0.6762 | 0.1807 | 1.2128 | 1.2950 | 0.2444 | 0.2205 | 1.7407 | 0.6378 | 0.1902 | 0.1883 | 0.8812 | 2.2164 | 0.9429 | 3.0534 |
| RC_SIM1 | 0.2414 | 0.6757 | 0.1833 | 1.2116 | 1.2936 | 0.2442 | 0.2201 | 1.7412 | 0.6414 | 0.1900 | 0.1882 | 0.8817 | 2.2325 | 0.9435 | 3.0739 |
| RC_SIM2 | 0.2415 | 0.6758 | 0.1806 | 1.2116 | 1.2941 | 0.2442 | 0.2202 | 1.7467 | 0.6373 | 0.1900 | 0.1881 | 0.8809 | 2.2155 | 0.9426 | 3.0519 |

Δ vs V1:

| arm | metric | Δ | 95% games | 95% slates |
|---|---|---:|---|---|
| SIM2 | brier_win | +0.0000 | [-0.0002, +0.0003] | [-0.0002, +0.0003] |
| SIM2 | brier_ot | -0.0025 | [-0.0033, -0.0016] | [-0.0032, -0.0016] |
| SIM2 | rps_total | -0.0003 | [-0.0012, +0.0005] | [-0.0012, +0.0005] |
| SIM2 | rps_margin | +0.0010 | [-0.0002, +0.0021] | [-0.0002, +0.0022] |
| SIM2 | brier_reg3 | -0.0036 | [-0.0049, -0.0023] | [-0.0049, -0.0024] |
| SIM2 | brier_puck_line | +0.0002 | [-0.0001, +0.0004] | [-0.0001, +0.0004] |
| SIM2 | brier_team_total | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] |
| SIM2 | brier_over_5.5 | -0.0001 | [-0.0003, +0.0002] | [-0.0003, +0.0002] |
| SIM2 | brier_over_6.5 | +0.0001 | [-0.0002, +0.0004] | [-0.0002, +0.0004] |
| SIM2 | logloss_win | +0.0000 | [-0.0004, +0.0005] | [-0.0004, +0.0005] |
| SIM2 | brier_joint_margin | -0.0006 | [-0.0013, +0.0001] | [-0.0013, +0.0002] |
| SIM2 | brier_joint_total | -0.0007 | [-0.0010, -0.0004] | [-0.0010, -0.0004] |
| SIM2 | logscore_joint_margin | -0.0159 | [-0.0219, -0.0101] | [-0.0216, -0.0100] |
| SIM2 | logscore_joint_total | -0.0189 | [-0.0252, -0.0130] | [-0.0249, -0.0129] |
| R_SIM2 | brier_win | -0.0002 | [-0.0006, +0.0003] | [-0.0006, +0.0003] |
| R_SIM2 | brier_ot | -0.0024 | [-0.0033, -0.0016] | [-0.0032, -0.0016] |
| R_SIM2 | rps_total | -0.0003 | [-0.0016, +0.0011] | [-0.0016, +0.0011] |
| R_SIM2 | rps_margin | +0.0002 | [-0.0014, +0.0019] | [-0.0013, +0.0019] |
| R_SIM2 | brier_reg3 | -0.0039 | [-0.0052, -0.0025] | [-0.0052, -0.0025] |
| R_SIM2 | brier_puck_line | +0.0000 | [-0.0003, +0.0004] | [-0.0003, +0.0004] |
| R_SIM2 | brier_team_total | -0.0001 | [-0.0003, +0.0000] | [-0.0003, +0.0000] |
| R_SIM2 | brier_over_5.5 | -0.0001 | [-0.0005, +0.0003] | [-0.0005, +0.0003] |
| R_SIM2 | brier_over_6.5 | +0.0001 | [-0.0003, +0.0005] | [-0.0003, +0.0005] |
| R_SIM2 | logloss_win | -0.0004 | [-0.0013, +0.0005] | [-0.0013, +0.0005] |
| R_SIM2 | brier_joint_margin | -0.0007 | [-0.0015, +0.0000] | [-0.0015, -0.0000] |
| R_SIM2 | brier_joint_total | -0.0007 | [-0.0010, -0.0004] | [-0.0010, -0.0004] |
| R_SIM2 | logscore_joint_margin | -0.0164 | [-0.0226, -0.0104] | [-0.0220, -0.0106] |
| R_SIM2 | logscore_joint_total | -0.0197 | [-0.0261, -0.0135] | [-0.0258, -0.0135] |
| RC_SIM1 | brier_win | -0.0004 | [-0.0009, +0.0001] | [-0.0009, +0.0000] |
| RC_SIM1 | brier_ot | +0.0001 | [-0.0000, +0.0003] | [-0.0000, +0.0003] |
| RC_SIM1 | rps_total | -0.0014 | [-0.0030, +0.0001] | [-0.0030, +0.0001] |
| RC_SIM1 | rps_margin | -0.0012 | [-0.0029, +0.0006] | [-0.0029, +0.0005] |
| RC_SIM1 | brier_reg3 | -0.0002 | [-0.0011, +0.0006] | [-0.0010, +0.0005] |
| RC_SIM1 | brier_puck_line | -0.0002 | [-0.0005, +0.0001] | [-0.0005, +0.0001] |
| RC_SIM1 | brier_team_total | -0.0002 | [-0.0004, -0.0000] | [-0.0004, -0.0000] |
| RC_SIM1 | brier_over_5.5 | -0.0003 | [-0.0008, +0.0002] | [-0.0008, +0.0002] |
| RC_SIM1 | brier_over_6.5 | -0.0003 | [-0.0008, +0.0001] | [-0.0008, +0.0001] |
| RC_SIM1 | logloss_win | -0.0009 | [-0.0019, +0.0001] | [-0.0019, +0.0001] |
| RC_SIM1 | brier_joint_margin | -0.0002 | [-0.0007, +0.0002] | [-0.0007, +0.0002] |
| RC_SIM1 | brier_joint_total | -0.0001 | [-0.0004, +0.0001] | [-0.0004, +0.0001] |
| RC_SIM1 | logscore_joint_margin | -0.0002 | [-0.0021, +0.0017] | [-0.0021, +0.0015] |
| RC_SIM1 | logscore_joint_total | +0.0009 | [-0.0020, +0.0039] | [-0.0021, +0.0038] |
| RC_SIM2 | brier_win | -0.0004 | [-0.0009, +0.0002] | [-0.0009, +0.0001] |
| RC_SIM2 | brier_ot | -0.0025 | [-0.0033, -0.0017] | [-0.0033, -0.0017] |
| RC_SIM2 | rps_total | -0.0015 | [-0.0033, +0.0003] | [-0.0033, +0.0003] |
| RC_SIM2 | rps_margin | -0.0007 | [-0.0026, +0.0012] | [-0.0025, +0.0011] |
| RC_SIM2 | brier_reg3 | -0.0044 | [-0.0058, -0.0030] | [-0.0058, -0.0030] |
| RC_SIM2 | brier_puck_line | -0.0002 | [-0.0005, +0.0002] | [-0.0005, +0.0002] |
| RC_SIM2 | brier_team_total | -0.0003 | [-0.0005, -0.0001] | [-0.0005, -0.0001] |
| RC_SIM2 | brier_over_5.5 | -0.0003 | [-0.0008, +0.0002] | [-0.0008, +0.0002] |
| RC_SIM2 | brier_over_6.5 | -0.0002 | [-0.0007, +0.0003] | [-0.0007, +0.0002] |
| RC_SIM2 | logloss_win | -0.0008 | [-0.0019, +0.0003] | [-0.0019, +0.0003] |
| RC_SIM2 | brier_joint_margin | -0.0011 | [-0.0019, -0.0003] | [-0.0019, -0.0004] |
| RC_SIM2 | brier_joint_total | -0.0010 | [-0.0013, -0.0006] | [-0.0013, -0.0006] |
| RC_SIM2 | logscore_joint_margin | -0.0172 | [-0.0234, -0.0113] | [-0.0230, -0.0116] |
| RC_SIM2 | logscore_joint_total | -0.0211 | [-0.0274, -0.0149] | [-0.0272, -0.0150] |

## SEEN_2017_2022 (n=7116)

Levels:

| arm | brier_win | logloss_win | brier_ot | rps_total | rps_margin | brier_over_5.5 | brier_over_6.5 | abs_err_total | brier_reg3 | brier_puck_line | brier_team_total | brier_joint_margin | logscore_joint_margin | brier_joint_total | logscore_joint_total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 0.2400 | 0.6727 | 0.1768 | 1.2823 | 1.4106 | 0.2451 | 0.2443 | 1.8489 | 0.6357 | 0.2008 | 0.1955 | 0.8690 | 2.1714 | 0.9393 | 3.0193 |
| SIM2 | 0.2397 | 0.6722 | 0.1747 | 1.2816 | 1.4116 | 0.2449 | 0.2442 | 1.8498 | 0.6320 | 0.2012 | 0.1954 | 0.8680 | 2.1641 | 0.9387 | 3.0119 |
| SIM2_ST | 0.2399 | 0.6726 | 0.1745 | 1.2813 | 1.4123 | 0.2448 | 0.2441 | 1.8506 | 0.6320 | 0.2012 | 0.1954 | 0.8680 | 2.1633 | 0.9388 | 3.0118 |
| R_SIM1 | 0.2383 | 0.6693 | 0.1767 | 1.2868 | 1.4047 | 0.2459 | 0.2454 | 1.8518 | 0.6328 | 0.2000 | 0.1954 | 0.8678 | 2.1673 | 0.9392 | 3.0183 |
| R_SIM2 | 0.2381 | 0.6688 | 0.1745 | 1.2858 | 1.4050 | 0.2458 | 0.2452 | 1.8523 | 0.6291 | 0.2002 | 0.1952 | 0.8666 | 2.1598 | 0.9386 | 3.0105 |
| RC_SIM1 | 0.2379 | 0.6685 | 0.1767 | 1.2855 | 1.4027 | 0.2460 | 0.2454 | 1.8520 | 0.6321 | 0.1998 | 0.1952 | 0.8672 | 2.1663 | 0.9388 | 3.0165 |
| RC_SIM2 | 0.2377 | 0.6681 | 0.1744 | 1.2845 | 1.4035 | 0.2458 | 0.2450 | 1.8523 | 0.6285 | 0.2000 | 0.1951 | 0.8663 | 2.1596 | 0.9384 | 3.0095 |

Δ vs V1:

| arm | metric | Δ | 95% games | 95% slates |
|---|---|---:|---|---|
| SIM2 | brier_win | -0.0003 | [-0.0005, -0.0000] | [-0.0005, -0.0000] |
| SIM2 | brier_ot | -0.0021 | [-0.0029, -0.0014] | [-0.0029, -0.0014] |
| SIM2 | rps_total | -0.0007 | [-0.0017, +0.0002] | [-0.0017, +0.0002] |
| SIM2 | rps_margin | +0.0010 | [-0.0001, +0.0021] | [-0.0001, +0.0021] |
| SIM2 | brier_reg3 | -0.0037 | [-0.0049, -0.0024] | [-0.0049, -0.0024] |
| SIM2 | brier_puck_line | +0.0003 | [+0.0001, +0.0006] | [+0.0001, +0.0006] |
| SIM2 | brier_team_total | -0.0001 | [-0.0002, +0.0000] | [-0.0002, +0.0000] |
| SIM2 | brier_over_5.5 | -0.0002 | [-0.0005, +0.0000] | [-0.0005, +0.0001] |
| SIM2 | brier_over_6.5 | -0.0002 | [-0.0005, +0.0002] | [-0.0005, +0.0002] |
| SIM2 | logloss_win | -0.0006 | [-0.0011, -0.0000] | [-0.0011, -0.0001] |
| SIM2 | brier_joint_margin | -0.0010 | [-0.0015, -0.0005] | [-0.0015, -0.0005] |
| SIM2 | brier_joint_total | -0.0005 | [-0.0008, -0.0003] | [-0.0008, -0.0003] |
| SIM2 | logscore_joint_margin | -0.0073 | [-0.0105, -0.0042] | [-0.0104, -0.0041] |
| SIM2 | logscore_joint_total | -0.0074 | [-0.0113, -0.0034] | [-0.0112, -0.0035] |
| R_SIM2 | brier_win | -0.0019 | [-0.0024, -0.0014] | [-0.0024, -0.0014] |
| R_SIM2 | brier_ot | -0.0023 | [-0.0031, -0.0016] | [-0.0031, -0.0016] |
| R_SIM2 | rps_total | +0.0035 | [+0.0016, +0.0053] | [+0.0017, +0.0052] |
| R_SIM2 | rps_margin | -0.0056 | [-0.0076, -0.0036] | [-0.0076, -0.0037] |
| R_SIM2 | brier_reg3 | -0.0066 | [-0.0080, -0.0052] | [-0.0079, -0.0052] |
| R_SIM2 | brier_puck_line | -0.0006 | [-0.0010, -0.0003] | [-0.0010, -0.0003] |
| R_SIM2 | brier_team_total | -0.0003 | [-0.0005, -0.0001] | [-0.0005, -0.0001] |
| R_SIM2 | brier_over_5.5 | +0.0007 | [+0.0002, +0.0012] | [+0.0002, +0.0012] |
| R_SIM2 | brier_over_6.5 | +0.0008 | [+0.0003, +0.0014] | [+0.0003, +0.0014] |
| R_SIM2 | logloss_win | -0.0040 | [-0.0050, -0.0029] | [-0.0050, -0.0030] |
| R_SIM2 | brier_joint_margin | -0.0023 | [-0.0030, -0.0017] | [-0.0030, -0.0017] |
| R_SIM2 | brier_joint_total | -0.0007 | [-0.0011, -0.0003] | [-0.0011, -0.0003] |
| R_SIM2 | logscore_joint_margin | -0.0116 | [-0.0151, -0.0082] | [-0.0153, -0.0080] |
| R_SIM2 | logscore_joint_total | -0.0088 | [-0.0132, -0.0046] | [-0.0133, -0.0047] |
| RC_SIM1 | brier_win | -0.0020 | [-0.0026, -0.0014] | [-0.0027, -0.0015] |
| RC_SIM1 | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0003, +0.0001] |
| RC_SIM1 | rps_total | +0.0032 | [+0.0009, +0.0056] | [+0.0010, +0.0055] |
| RC_SIM1 | rps_margin | -0.0080 | [-0.0103, -0.0055] | [-0.0106, -0.0056] |
| RC_SIM1 | brier_reg3 | -0.0035 | [-0.0046, -0.0025] | [-0.0046, -0.0025] |
| RC_SIM1 | brier_puck_line | -0.0011 | [-0.0015, -0.0007] | [-0.0015, -0.0007] |
| RC_SIM1 | brier_team_total | -0.0003 | [-0.0006, -0.0000] | [-0.0006, -0.0000] |
| RC_SIM1 | brier_over_5.5 | +0.0009 | [+0.0002, +0.0016] | [+0.0003, +0.0016] |
| RC_SIM1 | brier_over_6.5 | +0.0011 | [+0.0004, +0.0018] | [+0.0005, +0.0018] |
| RC_SIM1 | logloss_win | -0.0043 | [-0.0055, -0.0030] | [-0.0056, -0.0030] |
| RC_SIM1 | brier_joint_margin | -0.0017 | [-0.0024, -0.0011] | [-0.0024, -0.0011] |
| RC_SIM1 | brier_joint_total | -0.0005 | [-0.0009, -0.0001] | [-0.0009, -0.0002] |
| RC_SIM1 | logscore_joint_margin | -0.0051 | [-0.0073, -0.0028] | [-0.0074, -0.0029] |
| RC_SIM1 | logscore_joint_total | -0.0028 | [-0.0061, +0.0008] | [-0.0063, +0.0006] |
| RC_SIM2 | brier_win | -0.0022 | [-0.0028, -0.0016] | [-0.0029, -0.0016] |
| RC_SIM2 | brier_ot | -0.0024 | [-0.0032, -0.0016] | [-0.0031, -0.0016] |
| RC_SIM2 | rps_total | +0.0022 | [-0.0002, +0.0046] | [-0.0002, +0.0044] |
| RC_SIM2 | rps_margin | -0.0071 | [-0.0096, -0.0045] | [-0.0097, -0.0045] |
| RC_SIM2 | brier_reg3 | -0.0072 | [-0.0087, -0.0057] | [-0.0087, -0.0057] |
| RC_SIM2 | brier_puck_line | -0.0009 | [-0.0013, -0.0004] | [-0.0013, -0.0004] |
| RC_SIM2 | brier_team_total | -0.0004 | [-0.0007, -0.0002] | [-0.0007, -0.0002] |
| RC_SIM2 | brier_over_5.5 | +0.0007 | [-0.0000, +0.0014] | [+0.0000, +0.0014] |
| RC_SIM2 | brier_over_6.5 | +0.0007 | [-0.0000, +0.0013] | [+0.0000, +0.0013] |
| RC_SIM2 | logloss_win | -0.0047 | [-0.0060, -0.0033] | [-0.0061, -0.0034] |
| RC_SIM2 | brier_joint_margin | -0.0026 | [-0.0034, -0.0019] | [-0.0034, -0.0019] |
| RC_SIM2 | brier_joint_total | -0.0009 | [-0.0013, -0.0005] | [-0.0013, -0.0004] |
| RC_SIM2 | logscore_joint_margin | -0.0118 | [-0.0155, -0.0083] | [-0.0158, -0.0081] |
| RC_SIM2 | logscore_joint_total | -0.0098 | [-0.0141, -0.0054] | [-0.0143, -0.0053] |

## EXPOSED_2023_2025 (n=3936)

Levels:

| arm | brier_win | logloss_win | brier_ot | rps_total | rps_margin | brier_over_5.5 | brier_over_6.5 | abs_err_total | brier_reg3 | brier_puck_line | brier_team_total | brier_joint_margin | logscore_joint_margin | brier_joint_total | logscore_joint_total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 0.2405 | 0.6738 | 0.1744 | 1.2873 | 1.4420 | 0.2455 | 0.2469 | 1.8624 | 0.6346 | 0.2039 | 0.1958 | 0.8659 | 2.1576 | 0.9383 | 3.0063 |
| SIM2 | 0.2402 | 0.6731 | 0.1721 | 1.2886 | 1.4427 | 0.2459 | 0.2473 | 1.8651 | 0.6312 | 0.2043 | 0.1959 | 0.8637 | 2.1449 | 0.9382 | 3.0037 |
| SIM2_ST | 0.2408 | 0.6745 | 0.1721 | 1.2882 | 1.4445 | 0.2458 | 0.2472 | 1.8665 | 0.6319 | 0.2044 | 0.1960 | 0.8641 | 2.1468 | 0.9381 | 3.0030 |
| R_SIM1 | 0.2394 | 0.6715 | 0.1744 | 1.2889 | 1.4377 | 0.2459 | 0.2474 | 1.8641 | 0.6325 | 0.2033 | 0.1955 | 0.8652 | 2.1564 | 0.9381 | 3.0051 |
| R_SIM2 | 0.2394 | 0.6714 | 0.1722 | 1.2898 | 1.4387 | 0.2462 | 0.2477 | 1.8663 | 0.6294 | 0.2036 | 0.1956 | 0.8627 | 2.1421 | 0.9378 | 2.9977 |
| RC_SIM1 | 0.2394 | 0.6714 | 0.1745 | 1.2852 | 1.4380 | 0.2453 | 0.2468 | 1.8587 | 0.6329 | 0.2033 | 0.1953 | 0.8651 | 2.1571 | 0.9377 | 3.0049 |
| RC_SIM2 | 0.2396 | 0.6718 | 0.1721 | 1.2856 | 1.4389 | 0.2455 | 0.2466 | 1.8614 | 0.6295 | 0.2036 | 0.1953 | 0.8628 | 2.1433 | 0.9374 | 2.9973 |

Δ vs V1:

| arm | metric | Δ | 95% games | 95% slates |
|---|---|---:|---|---|
| SIM2 | brier_win | -0.0003 | [-0.0007, +0.0000] | [-0.0007, +0.0000] |
| SIM2 | brier_ot | -0.0022 | [-0.0033, -0.0011] | [-0.0032, -0.0013] |
| SIM2 | rps_total | +0.0013 | [+0.0000, +0.0025] | [+0.0001, +0.0025] |
| SIM2 | rps_margin | +0.0007 | [-0.0006, +0.0020] | [-0.0006, +0.0020] |
| SIM2 | brier_reg3 | -0.0034 | [-0.0050, -0.0017] | [-0.0049, -0.0018] |
| SIM2 | brier_puck_line | +0.0003 | [+0.0001, +0.0006] | [+0.0001, +0.0006] |
| SIM2 | brier_team_total | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0003] |
| SIM2 | brier_over_5.5 | +0.0004 | [+0.0000, +0.0007] | [+0.0001, +0.0007] |
| SIM2 | brier_over_6.5 | +0.0003 | [-0.0002, +0.0008] | [-0.0001, +0.0007] |
| SIM2 | logloss_win | -0.0007 | [-0.0014, +0.0000] | [-0.0013, +0.0000] |
| SIM2 | brier_joint_margin | -0.0023 | [-0.0030, -0.0015] | [-0.0030, -0.0016] |
| SIM2 | brier_joint_total | -0.0001 | [-0.0005, +0.0003] | [-0.0005, +0.0003] |
| SIM2 | logscore_joint_margin | -0.0127 | [-0.0169, -0.0085] | [-0.0167, -0.0089] |
| SIM2 | logscore_joint_total | -0.0027 | [-0.0077, +0.0024] | [-0.0076, +0.0022] |
| R_SIM2 | brier_win | -0.0011 | [-0.0021, -0.0002] | [-0.0021, -0.0003] |
| R_SIM2 | brier_ot | -0.0022 | [-0.0032, -0.0011] | [-0.0031, -0.0012] |
| R_SIM2 | rps_total | +0.0025 | [+0.0003, +0.0046] | [+0.0003, +0.0045] |
| R_SIM2 | rps_margin | -0.0033 | [-0.0071, +0.0003] | [-0.0070, +0.0003] |
| R_SIM2 | brier_reg3 | -0.0052 | [-0.0072, -0.0030] | [-0.0073, -0.0031] |
| R_SIM2 | brier_puck_line | -0.0003 | [-0.0009, +0.0003] | [-0.0009, +0.0003] |
| R_SIM2 | brier_team_total | -0.0003 | [-0.0006, +0.0001] | [-0.0006, +0.0001] |
| R_SIM2 | brier_over_5.5 | +0.0006 | [+0.0000, +0.0012] | [+0.0000, +0.0012] |
| R_SIM2 | brier_over_6.5 | +0.0007 | [+0.0000, +0.0014] | [+0.0001, +0.0014] |
| R_SIM2 | logloss_win | -0.0024 | [-0.0044, -0.0005] | [-0.0043, -0.0006] |
| R_SIM2 | brier_joint_margin | -0.0033 | [-0.0044, -0.0021] | [-0.0043, -0.0022] |
| R_SIM2 | brier_joint_total | -0.0005 | [-0.0010, +0.0000] | [-0.0010, +0.0000] |
| R_SIM2 | logscore_joint_margin | -0.0155 | [-0.0204, -0.0106] | [-0.0199, -0.0110] |
| R_SIM2 | logscore_joint_total | -0.0087 | [-0.0142, -0.0031] | [-0.0140, -0.0033] |
| RC_SIM1 | brier_win | -0.0011 | [-0.0025, +0.0002] | [-0.0024, +0.0002] |
| RC_SIM1 | brier_ot | +0.0001 | [-0.0001, +0.0004] | [-0.0001, +0.0004] |
| RC_SIM1 | rps_total | -0.0021 | [-0.0045, +0.0001] | [-0.0044, -0.0000] |
| RC_SIM1 | rps_margin | -0.0040 | [-0.0095, +0.0012] | [-0.0094, +0.0013] |
| RC_SIM1 | brier_reg3 | -0.0017 | [-0.0041, +0.0006] | [-0.0040, +0.0006] |
| RC_SIM1 | brier_puck_line | -0.0006 | [-0.0016, +0.0003] | [-0.0016, +0.0002] |
| RC_SIM1 | brier_team_total | -0.0006 | [-0.0010, -0.0001] | [-0.0010, -0.0001] |
| RC_SIM1 | brier_over_5.5 | -0.0002 | [-0.0008, +0.0004] | [-0.0009, +0.0004] |
| RC_SIM1 | brier_over_6.5 | -0.0002 | [-0.0008, +0.0005] | [-0.0009, +0.0005] |
| RC_SIM1 | logloss_win | -0.0024 | [-0.0054, +0.0003] | [-0.0053, +0.0004] |
| RC_SIM1 | brier_joint_margin | -0.0008 | [-0.0021, +0.0005] | [-0.0021, +0.0005] |
| RC_SIM1 | brier_joint_total | -0.0006 | [-0.0012, +0.0000] | [-0.0011, -0.0000] |
| RC_SIM1 | logscore_joint_margin | -0.0005 | [-0.0046, +0.0035] | [-0.0046, +0.0038] |
| RC_SIM1 | logscore_joint_total | -0.0014 | [-0.0064, +0.0038] | [-0.0061, +0.0033] |
| RC_SIM2 | brier_win | -0.0009 | [-0.0023, +0.0004] | [-0.0023, +0.0004] |
| RC_SIM2 | brier_ot | -0.0022 | [-0.0032, -0.0012] | [-0.0032, -0.0013] |
| RC_SIM2 | rps_total | -0.0017 | [-0.0042, +0.0005] | [-0.0040, +0.0005] |
| RC_SIM2 | rps_margin | -0.0031 | [-0.0087, +0.0025] | [-0.0085, +0.0022] |
| RC_SIM2 | brier_reg3 | -0.0050 | [-0.0077, -0.0023] | [-0.0077, -0.0024] |
| RC_SIM2 | brier_puck_line | -0.0004 | [-0.0013, +0.0006] | [-0.0013, +0.0006] |
| RC_SIM2 | brier_team_total | -0.0006 | [-0.0011, -0.0000] | [-0.0011, -0.0001] |
| RC_SIM2 | brier_over_5.5 | -0.0000 | [-0.0007, +0.0007] | [-0.0007, +0.0006] |
| RC_SIM2 | brier_over_6.5 | -0.0003 | [-0.0010, +0.0003] | [-0.0010, +0.0003] |
| RC_SIM2 | logloss_win | -0.0020 | [-0.0050, +0.0009] | [-0.0049, +0.0008] |
| RC_SIM2 | brier_joint_margin | -0.0032 | [-0.0047, -0.0017] | [-0.0046, -0.0017] |
| RC_SIM2 | brier_joint_total | -0.0009 | [-0.0015, -0.0002] | [-0.0015, -0.0003] |
| RC_SIM2 | logscore_joint_margin | -0.0143 | [-0.0198, -0.0088] | [-0.0196, -0.0089] |
| RC_SIM2 | logscore_joint_total | -0.0090 | [-0.0152, -0.0028] | [-0.0149, -0.0030] |

## POOLED_2010_2025 (n=18777)

Levels:

| arm | brier_win | logloss_win | brier_ot | rps_total | rps_margin | brier_over_5.5 | brier_over_6.5 | abs_err_total | brier_reg3 | brier_puck_line | brier_team_total | brier_joint_margin | logscore_joint_margin | brier_joint_total | logscore_joint_total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 0.2408 | 0.6745 | 0.1789 | 1.2549 | 1.3695 | 0.2449 | 0.2350 | 1.8062 | 0.6379 | 0.1971 | 0.1927 | 0.8737 | 2.1937 | 0.9408 | 3.0387 |
| SIM2 | 0.2407 | 0.6742 | 0.1766 | 1.2547 | 1.3705 | 0.2449 | 0.2351 | 1.8091 | 0.6343 | 0.1974 | 0.1926 | 0.8726 | 2.1818 | 0.9403 | 3.0275 |
| SIM2_ST | 0.2410 | 0.6749 | 0.1766 | 1.2547 | 1.3716 | 0.2450 | 0.2351 | 1.8105 | 0.6347 | 0.1975 | 0.1927 | 0.8729 | 2.1823 | 0.9404 | 3.0276 |
| R_SIM1 | 0.2399 | 0.6725 | 0.1788 | 1.2570 | 1.3659 | 0.2453 | 0.2355 | 1.8068 | 0.6363 | 0.1966 | 0.1925 | 0.8730 | 2.1915 | 0.9407 | 3.0377 |
| R_SIM2 | 0.2398 | 0.6724 | 0.1765 | 1.2566 | 1.3668 | 0.2453 | 0.2355 | 1.8093 | 0.6327 | 0.1968 | 0.1924 | 0.8718 | 2.1794 | 0.9402 | 3.0254 |
| RC_SIM1 | 0.2397 | 0.6721 | 0.1790 | 1.2551 | 1.3652 | 0.2451 | 0.2353 | 1.8078 | 0.6361 | 0.1965 | 0.1923 | 0.8728 | 2.1916 | 0.9405 | 3.0377 |
| RC_SIM2 | 0.2397 | 0.6720 | 0.1765 | 1.2547 | 1.3659 | 0.2451 | 0.2351 | 1.8108 | 0.6323 | 0.1966 | 0.1922 | 0.8716 | 2.1792 | 0.9399 | 3.0244 |

Δ vs V1:

| arm | metric | Δ | 95% games | 95% slates |
|---|---|---:|---|---|
| SIM2 | brier_win | -0.0002 | [-0.0003, -0.0000] | [-0.0003, -0.0000] |
| SIM2 | brier_ot | -0.0023 | [-0.0028, -0.0018] | [-0.0028, -0.0018] |
| SIM2 | rps_total | -0.0001 | [-0.0007, +0.0004] | [-0.0007, +0.0004] |
| SIM2 | rps_margin | +0.0009 | [+0.0002, +0.0016] | [+0.0003, +0.0016] |
| SIM2 | brier_reg3 | -0.0036 | [-0.0044, -0.0028] | [-0.0044, -0.0028] |
| SIM2 | brier_puck_line | +0.0003 | [+0.0001, +0.0004] | [+0.0001, +0.0004] |
| SIM2 | brier_team_total | -0.0000 | [-0.0001, +0.0000] | [-0.0001, +0.0000] |
| SIM2 | brier_over_5.5 | -0.0000 | [-0.0002, +0.0001] | [-0.0002, +0.0001] |
| SIM2 | brier_over_6.5 | +0.0000 | [-0.0002, +0.0002] | [-0.0002, +0.0002] |
| SIM2 | logloss_win | -0.0003 | [-0.0007, -0.0000] | [-0.0006, -0.0000] |
| SIM2 | brier_joint_margin | -0.0011 | [-0.0015, -0.0007] | [-0.0015, -0.0007] |
| SIM2 | brier_joint_total | -0.0005 | [-0.0007, -0.0003] | [-0.0007, -0.0003] |
| SIM2 | logscore_joint_margin | -0.0120 | [-0.0148, -0.0091] | [-0.0149, -0.0090] |
| SIM2 | logscore_joint_total | -0.0111 | [-0.0143, -0.0081] | [-0.0143, -0.0080] |
| R_SIM2 | brier_win | -0.0010 | [-0.0014, -0.0007] | [-0.0013, -0.0007] |
| R_SIM2 | brier_ot | -0.0024 | [-0.0028, -0.0019] | [-0.0028, -0.0019] |
| R_SIM2 | rps_total | +0.0017 | [+0.0007, +0.0027] | [+0.0007, +0.0027] |
| R_SIM2 | rps_margin | -0.0027 | [-0.0040, -0.0014] | [-0.0040, -0.0014] |
| R_SIM2 | brier_reg3 | -0.0052 | [-0.0061, -0.0043] | [-0.0060, -0.0043] |
| R_SIM2 | brier_puck_line | -0.0003 | [-0.0005, -0.0000] | [-0.0005, -0.0000] |
| R_SIM2 | brier_team_total | -0.0002 | [-0.0004, -0.0001] | [-0.0004, -0.0001] |
| R_SIM2 | brier_over_5.5 | +0.0004 | [+0.0001, +0.0007] | [+0.0001, +0.0007] |
| R_SIM2 | brier_over_6.5 | +0.0005 | [+0.0002, +0.0008] | [+0.0002, +0.0008] |
| R_SIM2 | logloss_win | -0.0022 | [-0.0028, -0.0015] | [-0.0028, -0.0015] |
| R_SIM2 | brier_joint_margin | -0.0019 | [-0.0023, -0.0014] | [-0.0023, -0.0014] |
| R_SIM2 | brier_joint_total | -0.0006 | [-0.0009, -0.0004] | [-0.0009, -0.0004] |
| R_SIM2 | logscore_joint_margin | -0.0144 | [-0.0173, -0.0115] | [-0.0174, -0.0113] |
| R_SIM2 | logscore_joint_total | -0.0132 | [-0.0166, -0.0101] | [-0.0167, -0.0100] |
| RC_SIM1 | brier_win | -0.0012 | [-0.0016, -0.0007] | [-0.0016, -0.0007] |
| RC_SIM1 | brier_ot | +0.0001 | [-0.0001, +0.0002] | [-0.0000, +0.0002] |
| RC_SIM1 | rps_total | +0.0002 | [-0.0010, +0.0014] | [-0.0009, +0.0014] |
| RC_SIM1 | rps_margin | -0.0043 | [-0.0060, -0.0026] | [-0.0059, -0.0027] |
| RC_SIM1 | brier_reg3 | -0.0018 | [-0.0025, -0.0011] | [-0.0025, -0.0010] |
| RC_SIM1 | brier_puck_line | -0.0006 | [-0.0009, -0.0003] | [-0.0009, -0.0003] |
| RC_SIM1 | brier_team_total | -0.0003 | [-0.0005, -0.0002] | [-0.0005, -0.0002] |
| RC_SIM1 | brier_over_5.5 | +0.0002 | [-0.0002, +0.0005] | [-0.0002, +0.0005] |
| RC_SIM1 | brier_over_6.5 | +0.0002 | [-0.0001, +0.0006] | [-0.0001, +0.0006] |
| RC_SIM1 | logloss_win | -0.0025 | [-0.0033, -0.0016] | [-0.0034, -0.0016] |
| RC_SIM1 | brier_joint_margin | -0.0009 | [-0.0013, -0.0005] | [-0.0013, -0.0005] |
| RC_SIM1 | brier_joint_total | -0.0004 | [-0.0006, -0.0001] | [-0.0006, -0.0002] |
| RC_SIM1 | logscore_joint_margin | -0.0021 | [-0.0036, -0.0007] | [-0.0036, -0.0006] |
| RC_SIM1 | logscore_joint_total | -0.0010 | [-0.0030, +0.0011] | [-0.0030, +0.0010] |
| RC_SIM2 | brier_win | -0.0012 | [-0.0016, -0.0007] | [-0.0016, -0.0007] |
| RC_SIM2 | brier_ot | -0.0024 | [-0.0029, -0.0019] | [-0.0029, -0.0019] |
| RC_SIM2 | rps_total | -0.0002 | [-0.0014, +0.0011] | [-0.0014, +0.0011] |
| RC_SIM2 | rps_margin | -0.0036 | [-0.0053, -0.0019] | [-0.0052, -0.0018] |
| RC_SIM2 | brier_reg3 | -0.0056 | [-0.0066, -0.0046] | [-0.0066, -0.0045] |
| RC_SIM2 | brier_puck_line | -0.0005 | [-0.0008, -0.0002] | [-0.0008, -0.0002] |
| RC_SIM2 | brier_team_total | -0.0004 | [-0.0006, -0.0002] | [-0.0006, -0.0002] |
| RC_SIM2 | brier_over_5.5 | +0.0001 | [-0.0002, +0.0005] | [-0.0002, +0.0005] |
| RC_SIM2 | brier_over_6.5 | +0.0001 | [-0.0002, +0.0004] | [-0.0002, +0.0004] |
| RC_SIM2 | logloss_win | -0.0025 | [-0.0034, -0.0016] | [-0.0034, -0.0016] |
| RC_SIM2 | brier_joint_margin | -0.0021 | [-0.0026, -0.0016] | [-0.0027, -0.0016] |
| RC_SIM2 | brier_joint_total | -0.0009 | [-0.0012, -0.0006] | [-0.0012, -0.0007] |
| RC_SIM2 | logscore_joint_margin | -0.0146 | [-0.0175, -0.0115] | [-0.0177, -0.0114] |
| RC_SIM2 | logscore_joint_total | -0.0143 | [-0.0176, -0.0110] | [-0.0179, -0.0109] |

## 3V3_2015_2025 (n=13512)

Levels:

| arm | brier_win | logloss_win | brier_ot | rps_total | rps_margin | brier_over_5.5 | brier_over_6.5 | abs_err_total | brier_reg3 | brier_puck_line | brier_team_total | brier_joint_margin | logscore_joint_margin | brier_joint_total | logscore_joint_total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 0.2406 | 0.6741 | 0.1764 | 1.2693 | 1.3988 | 0.2451 | 0.2402 | 1.8303 | 0.6360 | 0.2002 | 0.1944 | 0.8699 | 2.1736 | 0.9396 | 3.0206 |
| SIM2 | 0.2404 | 0.6736 | 0.1743 | 1.2692 | 1.3997 | 0.2451 | 0.2402 | 1.8324 | 0.6325 | 0.2005 | 0.1943 | 0.8690 | 2.1680 | 0.9394 | 3.0174 |
| SIM2_ST | 0.2407 | 0.6743 | 0.1742 | 1.2689 | 1.4007 | 0.2450 | 0.2402 | 1.8334 | 0.6329 | 0.2005 | 0.1944 | 0.8693 | 2.1684 | 0.9394 | 3.0173 |
| R_SIM1 | 0.2393 | 0.6712 | 0.1763 | 1.2720 | 1.3939 | 0.2456 | 0.2408 | 1.8313 | 0.6336 | 0.1995 | 0.1942 | 0.8690 | 2.1705 | 0.9395 | 3.0188 |
| R_SIM2 | 0.2392 | 0.6711 | 0.1742 | 1.2714 | 1.3947 | 0.2455 | 0.2408 | 1.8329 | 0.6302 | 0.1997 | 0.1941 | 0.8680 | 2.1647 | 0.9391 | 3.0141 |
| RC_SIM1 | 0.2391 | 0.6708 | 0.1764 | 1.2698 | 1.3931 | 0.2454 | 0.2405 | 1.8303 | 0.6334 | 0.1993 | 0.1940 | 0.8687 | 2.1705 | 0.9392 | 3.0179 |
| RC_SIM2 | 0.2390 | 0.6707 | 0.1741 | 1.2693 | 1.3938 | 0.2453 | 0.2403 | 1.8321 | 0.6298 | 0.1996 | 0.1939 | 0.8678 | 2.1649 | 0.9388 | 3.0134 |

Δ vs V1:

| arm | metric | Δ | 95% games | 95% slates |
|---|---|---:|---|---|
| SIM2 | brier_win | -0.0002 | [-0.0004, -0.0001] | [-0.0004, -0.0001] |
| SIM2 | brier_ot | -0.0021 | [-0.0027, -0.0016] | [-0.0027, -0.0016] |
| SIM2 | rps_total | -0.0001 | [-0.0008, +0.0006] | [-0.0008, +0.0006] |
| SIM2 | rps_margin | +0.0009 | [+0.0001, +0.0017] | [+0.0001, +0.0017] |
| SIM2 | brier_reg3 | -0.0034 | [-0.0044, -0.0026] | [-0.0043, -0.0025] |
| SIM2 | brier_puck_line | +0.0003 | [+0.0002, +0.0005] | [+0.0002, +0.0005] |
| SIM2 | brier_team_total | -0.0000 | [-0.0001, +0.0000] | [-0.0001, +0.0000] |
| SIM2 | brier_over_5.5 | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] |
| SIM2 | brier_over_6.5 | +0.0000 | [-0.0002, +0.0003] | [-0.0002, +0.0003] |
| SIM2 | logloss_win | -0.0005 | [-0.0008, -0.0001] | [-0.0008, -0.0001] |
| SIM2 | brier_joint_margin | -0.0009 | [-0.0013, -0.0005] | [-0.0013, -0.0005] |
| SIM2 | brier_joint_total | -0.0003 | [-0.0005, -0.0001] | [-0.0005, -0.0001] |
| SIM2 | logscore_joint_margin | -0.0056 | [-0.0083, -0.0030] | [-0.0081, -0.0031] |
| SIM2 | logscore_joint_total | -0.0033 | [-0.0064, -0.0001] | [-0.0062, -0.0002] |
| R_SIM2 | brier_win | -0.0014 | [-0.0018, -0.0010] | [-0.0018, -0.0010] |
| R_SIM2 | brier_ot | -0.0022 | [-0.0028, -0.0017] | [-0.0028, -0.0017] |
| R_SIM2 | rps_total | +0.0021 | [+0.0009, +0.0034] | [+0.0009, +0.0034] |
| R_SIM2 | rps_margin | -0.0041 | [-0.0057, -0.0026] | [-0.0056, -0.0025] |
| R_SIM2 | brier_reg3 | -0.0058 | [-0.0068, -0.0048] | [-0.0068, -0.0047] |
| R_SIM2 | brier_puck_line | -0.0004 | [-0.0007, -0.0002] | [-0.0007, -0.0002] |
| R_SIM2 | brier_team_total | -0.0003 | [-0.0005, -0.0001] | [-0.0005, -0.0001] |
| R_SIM2 | brier_over_5.5 | +0.0004 | [+0.0001, +0.0008] | [+0.0001, +0.0008] |
| R_SIM2 | brier_over_6.5 | +0.0006 | [+0.0002, +0.0010] | [+0.0002, +0.0009] |
| R_SIM2 | logloss_win | -0.0029 | [-0.0038, -0.0021] | [-0.0038, -0.0021] |
| R_SIM2 | brier_joint_margin | -0.0019 | [-0.0025, -0.0014] | [-0.0025, -0.0014] |
| R_SIM2 | brier_joint_total | -0.0005 | [-0.0008, -0.0003] | [-0.0008, -0.0003] |
| R_SIM2 | logscore_joint_margin | -0.0089 | [-0.0117, -0.0061] | [-0.0116, -0.0062] |
| R_SIM2 | logscore_joint_total | -0.0066 | [-0.0099, -0.0030] | [-0.0098, -0.0033] |
| RC_SIM1 | brier_win | -0.0015 | [-0.0021, -0.0010] | [-0.0020, -0.0010] |
| RC_SIM1 | brier_ot | +0.0000 | [-0.0001, +0.0001] | [-0.0001, +0.0002] |
| RC_SIM1 | rps_total | +0.0005 | [-0.0011, +0.0021] | [-0.0010, +0.0020] |
| RC_SIM1 | rps_margin | -0.0058 | [-0.0080, -0.0037] | [-0.0079, -0.0037] |
| RC_SIM1 | brier_reg3 | -0.0026 | [-0.0035, -0.0017] | [-0.0035, -0.0017] |
| RC_SIM1 | brier_puck_line | -0.0008 | [-0.0012, -0.0005] | [-0.0012, -0.0005] |
| RC_SIM1 | brier_team_total | -0.0004 | [-0.0006, -0.0002] | [-0.0006, -0.0002] |
| RC_SIM1 | brier_over_5.5 | +0.0003 | [-0.0002, +0.0007] | [-0.0001, +0.0007] |
| RC_SIM1 | brier_over_6.5 | +0.0004 | [-0.0001, +0.0008] | [-0.0001, +0.0008] |
| RC_SIM1 | logloss_win | -0.0032 | [-0.0044, -0.0021] | [-0.0044, -0.0021] |
| RC_SIM1 | brier_joint_margin | -0.0012 | [-0.0018, -0.0007] | [-0.0018, -0.0007] |
| RC_SIM1 | brier_joint_total | -0.0005 | [-0.0008, -0.0002] | [-0.0007, -0.0002] |
| RC_SIM1 | logscore_joint_margin | -0.0030 | [-0.0048, -0.0013] | [-0.0048, -0.0012] |
| RC_SIM1 | logscore_joint_total | -0.0027 | [-0.0053, -0.0002] | [-0.0051, -0.0003] |
| RC_SIM2 | brier_win | -0.0016 | [-0.0022, -0.0010] | [-0.0021, -0.0010] |
| RC_SIM2 | brier_ot | -0.0023 | [-0.0028, -0.0017] | [-0.0028, -0.0017] |
| RC_SIM2 | rps_total | +0.0000 | [-0.0016, +0.0016] | [-0.0015, +0.0015] |
| RC_SIM2 | rps_margin | -0.0050 | [-0.0073, -0.0029] | [-0.0072, -0.0028] |
| RC_SIM2 | brier_reg3 | -0.0062 | [-0.0074, -0.0050] | [-0.0074, -0.0050] |
| RC_SIM2 | brier_puck_line | -0.0006 | [-0.0010, -0.0002] | [-0.0010, -0.0002] |
| RC_SIM2 | brier_team_total | -0.0005 | [-0.0007, -0.0003] | [-0.0007, -0.0003] |
| RC_SIM2 | brier_over_5.5 | +0.0002 | [-0.0003, +0.0006] | [-0.0003, +0.0006] |
| RC_SIM2 | brier_over_6.5 | +0.0001 | [-0.0003, +0.0006] | [-0.0003, +0.0005] |
| RC_SIM2 | logloss_win | -0.0034 | [-0.0046, -0.0022] | [-0.0045, -0.0022] |
| RC_SIM2 | brier_joint_margin | -0.0021 | [-0.0028, -0.0015] | [-0.0027, -0.0015] |
| RC_SIM2 | brier_joint_total | -0.0008 | [-0.0011, -0.0005] | [-0.0011, -0.0005] |
| RC_SIM2 | logscore_joint_margin | -0.0087 | [-0.0118, -0.0057] | [-0.0116, -0.0058] |
| RC_SIM2 | logscore_joint_total | -0.0073 | [-0.0109, -0.0035] | [-0.0106, -0.0039] |

## Mean total goals and overtime rate, predicted vs observed

| tier | observed total | V1 total | SIM2 total | RC_SIM1 total | RC_SIM2 total | observed OT | V1 OT | SIM2 OT | RC_SIM1 OT | RC_SIM2 OT |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CLEAN2 | 5.488 | 5.472 | 5.511 | 5.479 | 5.516 | 0.237 | 0.187 | 0.228 | 0.186 | 0.226 |
| SEEN | 6.105 | 6.091 | 6.126 | 6.017 | 6.051 | 0.225 | 0.176 | 0.216 | 0.175 | 0.215 |
| EXPOSED | 6.187 | 6.233 | 6.267 | 6.173 | 6.204 | 0.221 | 0.174 | 0.214 | 0.171 | 0.211 |

## Per season: Δ vs V1 on the primary metrics (RC_SIM2)

| season | Δ win | Δ OT | Δ RPS total | Δ RPS margin |
|---|---:|---:|---:|---:|
| 2010 | +0.0008 | -0.0024 | -0.0005 | +0.0037 |
| 2011 | +0.0003 | -0.0027 | +0.0002 | +0.0002 |
| 2012 | -0.0003 | -0.0004 | +0.0019 | -0.0002 |
| 2013 | -0.0002 | -0.0034 | -0.0017 | -0.0004 |
| 2014 | -0.0010 | -0.0036 | -0.0017 | -0.0028 |
| 2015 | -0.0005 | -0.0015 | -0.0038 | +0.0006 |
| 2016 | -0.0014 | -0.0026 | -0.0030 | -0.0052 |
| 2017 | -0.0000 | -0.0030 | -0.0023 | +0.0019 |
| 2018 | -0.0010 | -0.0014 | +0.0052 | -0.0009 |
| 2019 | -0.0009 | -0.0026 | -0.0015 | -0.0024 |
| 2020 | -0.0043 | -0.0028 | -0.0002 | -0.0140 |
| 2021 | -0.0042 | -0.0018 | +0.0101 | -0.0135 |
| 2022 | -0.0032 | -0.0028 | +0.0002 | -0.0147 |
| 2023 | -0.0015 | -0.0016 | -0.0007 | -0.0062 |
| 2024 | -0.0016 | -0.0007 | +0.0004 | -0.0011 |
| 2025 | +0.0004 | -0.0044 | -0.0049 | -0.0020 |

## Against the Kalshi midpoint at T-60m (season 2025; no depth, fee or slippage; a midpoint advantage is not an execution edge)

### home_win (n=1312; market Brier 0.2442)

| forecaster | Brier | Δ vs market | 95% games | verdict |
|---|---:|---:|---|---|
| V1 | 0.2459 | +0.0017 | [-0.0014, +0.0047] | indistinguishable |
| SIM2 | 0.2458 | +0.0016 | [-0.0015, +0.0046] | indistinguishable |
| RC_SIM1 | 0.2460 | +0.0018 | [-0.0008, +0.0043] | indistinguishable |
| RC_SIM2 | 0.2463 | +0.0021 | [-0.0005, +0.0046] | indistinguishable |

### total_over_5.5 (n=1196; market Brier 0.2419)

| forecaster | Brier | Δ vs market | 95% games | verdict |
|---|---:|---:|---|---|
| V1 | 0.2444 | +0.0025 | [+0.0004, +0.0047] | market better |
| SIM2 | 0.2445 | +0.0026 | [+0.0005, +0.0047] | market better |
| RC_SIM1 | 0.2438 | +0.0019 | [-0.0002, +0.0040] | indistinguishable |
| RC_SIM2 | 0.2437 | +0.0018 | [-0.0003, +0.0040] | indistinguishable |

### total_over_6.5 (n=1194; market Brier 0.2466)

| forecaster | Brier | Δ vs market | 95% games | verdict |
|---|---:|---:|---|---|
| V1 | 0.2501 | +0.0035 | [+0.0012, +0.0058] | market better |
| SIM2 | 0.2497 | +0.0031 | [+0.0008, +0.0054] | market better |
| RC_SIM1 | 0.2495 | +0.0029 | [+0.0007, +0.0051] | market better |
| RC_SIM2 | 0.2486 | +0.0020 | [-0.0002, +0.0041] | indistinguishable |

### puck_away_-1.5 (n=1181; market Brier 0.1926)

| forecaster | Brier | Δ vs market | 95% games | verdict |
|---|---:|---:|---|---|
| V1 | 0.1939 | +0.0012 | [-0.0014, +0.0038] | indistinguishable |
| SIM2 | 0.1943 | +0.0017 | [-0.0010, +0.0043] | indistinguishable |
| RC_SIM1 | 0.1939 | +0.0012 | [-0.0010, +0.0035] | indistinguishable |
| RC_SIM2 | 0.1942 | +0.0016 | [-0.0007, +0.0039] | indistinguishable |

### puck_home_-1.5 (n=1181; market Brier 0.2035)

| forecaster | Brier | Δ vs market | 95% games | verdict |
|---|---:|---:|---|---|
| V1 | 0.2050 | +0.0014 | [-0.0011, +0.0039] | indistinguishable |
| SIM2 | 0.2045 | +0.0010 | [-0.0016, +0.0035] | indistinguishable |
| RC_SIM1 | 0.2036 | +0.0001 | [-0.0021, +0.0023] | indistinguishable |
| RC_SIM2 | 0.2036 | +0.0000 | [-0.0022, +0.0022] | indistinguishable |

Unavailable: team totals (KXNHLTEAMTOTAL has no markets in the history); overtime (KXNHLOVERTIME has 49 playoff markets only)
