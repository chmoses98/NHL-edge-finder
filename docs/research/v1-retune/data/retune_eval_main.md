# Retuned V1 vs opponent adjustment — preregistered evaluation

11052 games, seasons [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025] · negative Δ = challenger better · 95% intervals: game bootstrap | slate-clustered bootstrap · RESEARCH_ONLY, nothing is promoted

## FRESH_2017 (n=1271)

| arm | brier_win | logloss_win | brier_ot | rps_total | rps_margin | brier_over_5.5 | brier_over_6.5 | abs_err_total | ECE(win) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 0.2405 | 0.6740 | 0.1818 | 1.3050 | 1.3738 | 0.2503 | 0.2432 | 1.8923 | 0.0420 |
| V1_C1 | 0.2406 | 0.6742 | 0.1818 | 1.3031 | 1.3733 | 0.2501 | 0.2436 | 1.8928 | 0.0525 |
| V1_T | 0.2399 | 0.6728 | 0.1816 | 1.3070 | 1.3720 | 0.2509 | 0.2438 | 1.8936 | 0.0419 |
| V1_T_C1 | 0.2402 | 0.6735 | 0.1815 | 1.3043 | 1.3725 | 0.2506 | 0.2440 | 1.8943 | 0.0489 |
| V1_R | 0.2399 | 0.6728 | 0.1816 | 1.3070 | 1.3720 | 0.2509 | 0.2438 | 1.8936 | 0.0419 |
| V1_R_C1 | 0.2402 | 0.6735 | 0.1815 | 1.3043 | 1.3725 | 0.2506 | 0.2440 | 1.8943 | 0.0489 |
| V1_R_noB2B | 0.2406 | 0.6743 | 0.1816 | 1.3070 | 1.3737 | 0.2509 | 0.2437 | 1.8944 | 0.0372 |
| V1_R_noFIN | 0.2412 | 0.6754 | 0.1814 | 1.3085 | 1.3763 | 0.2519 | 0.2450 | 1.9026 | 0.0310 |
| OA_XG | 0.2405 | 0.6739 | 0.1820 | 1.3046 | 1.3738 | 0.2497 | 0.2427 | 1.8909 | 0.0343 |
| OA_SVA | 0.2403 | 0.6736 | 0.1819 | 1.3039 | 1.3727 | 0.2495 | 0.2428 | 1.8908 | 0.0366 |
| OA_SVA_C1 | 0.2407 | 0.6744 | 0.1817 | 1.3035 | 1.3736 | 0.2501 | 0.2430 | 1.8932 | 0.0500 |
| LEAGUE | 0.2466 | 0.6862 | 0.1817 | 1.3049 | 1.3928 | 0.2505 | 0.2440 | 1.8984 | 0.0211 |

Δ paired vs production V1:

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1_C1 | brier_win | +0.0001 | [-0.0004, +0.0005] | [-0.0005, +0.0006] | indistinguishable |
| V1_C1 | brier_ot | -0.0000 | [-0.0004, +0.0004] | [-0.0004, +0.0003] | indistinguishable |
| V1_C1 | rps_total | -0.0020 | [-0.0075, +0.0034] | [-0.0067, +0.0030] | indistinguishable |
| V1_C1 | rps_margin | -0.0005 | [-0.0020, +0.0011] | [-0.0021, +0.0011] | indistinguishable |
| V1_T | brier_win | -0.0006 | [-0.0013, +0.0001] | [-0.0013, +0.0001] | indistinguishable |
| V1_T | brier_ot | -0.0002 | [-0.0006, +0.0002] | [-0.0006, +0.0002] | indistinguishable |
| V1_T | rps_total | +0.0020 | [-0.0005, +0.0046] | [-0.0003, +0.0043] | indistinguishable |
| V1_T | rps_margin | -0.0018 | [-0.0044, +0.0008] | [-0.0042, +0.0007] | indistinguishable |
| V1_T_C1 | brier_win | -0.0003 | [-0.0010, +0.0004] | [-0.0010, +0.0004] | indistinguishable |
| V1_T_C1 | brier_ot | -0.0004 | [-0.0008, +0.0001] | [-0.0008, +0.0001] | indistinguishable |
| V1_T_C1 | rps_total | -0.0007 | [-0.0064, +0.0051] | [-0.0061, +0.0047] | indistinguishable |
| V1_T_C1 | rps_margin | -0.0012 | [-0.0038, +0.0013] | [-0.0037, +0.0011] | indistinguishable |
| V1_R | brier_win | -0.0006 | [-0.0013, +0.0001] | [-0.0013, +0.0001] | indistinguishable |
| V1_R | brier_ot | -0.0002 | [-0.0006, +0.0002] | [-0.0006, +0.0002] | indistinguishable |
| V1_R | rps_total | +0.0020 | [-0.0005, +0.0046] | [-0.0003, +0.0043] | indistinguishable |
| V1_R | rps_margin | -0.0018 | [-0.0044, +0.0008] | [-0.0042, +0.0007] | indistinguishable |
| V1_R_C1 | brier_win | -0.0003 | [-0.0010, +0.0004] | [-0.0010, +0.0004] | indistinguishable |
| V1_R_C1 | brier_ot | -0.0004 | [-0.0008, +0.0001] | [-0.0008, +0.0001] | indistinguishable |
| V1_R_C1 | rps_total | -0.0007 | [-0.0064, +0.0051] | [-0.0061, +0.0047] | indistinguishable |
| V1_R_C1 | rps_margin | -0.0012 | [-0.0038, +0.0013] | [-0.0037, +0.0011] | indistinguishable |
| V1_R_noB2B | brier_win | +0.0001 | [-0.0009, +0.0012] | [-0.0009, +0.0011] | indistinguishable |
| V1_R_noB2B | brier_ot | -0.0002 | [-0.0006, +0.0002] | [-0.0006, +0.0002] | indistinguishable |
| V1_R_noB2B | rps_total | +0.0019 | [-0.0005, +0.0044] | [-0.0004, +0.0043] | indistinguishable |
| V1_R_noB2B | rps_margin | -0.0000 | [-0.0039, +0.0039] | [-0.0037, +0.0034] | indistinguishable |
| V1_R_noFIN | brier_win | +0.0007 | [-0.0015, +0.0028] | [-0.0013, +0.0025] | indistinguishable |
| V1_R_noFIN | brier_ot | -0.0004 | [-0.0008, +0.0001] | [-0.0008, +0.0000] | indistinguishable |
| V1_R_noFIN | rps_total | +0.0035 | [-0.0039, +0.0109] | [-0.0041, +0.0112] | indistinguishable |
| V1_R_noFIN | rps_margin | +0.0025 | [-0.0058, +0.0107] | [-0.0047, +0.0096] | indistinguishable |
| OA_XG | brier_win | -0.0000 | [-0.0009, +0.0008] | [-0.0008, +0.0008] | indistinguishable |
| OA_XG | brier_ot | +0.0002 | [-0.0002, +0.0006] | [-0.0002, +0.0006] | indistinguishable |
| OA_XG | rps_total | -0.0004 | [-0.0055, +0.0045] | [-0.0049, +0.0040] | indistinguishable |
| OA_XG | rps_margin | +0.0000 | [-0.0031, +0.0032] | [-0.0030, +0.0031] | indistinguishable |
| OA_SVA | brier_win | -0.0002 | [-0.0011, +0.0007] | [-0.0010, +0.0007] | indistinguishable |
| OA_SVA | brier_ot | +0.0001 | [-0.0003, +0.0005] | [-0.0003, +0.0005] | indistinguishable |
| OA_SVA | rps_total | -0.0011 | [-0.0061, +0.0037] | [-0.0057, +0.0034] | indistinguishable |
| OA_SVA | rps_margin | -0.0010 | [-0.0043, +0.0023] | [-0.0042, +0.0021] | indistinguishable |
| OA_SVA_C1 | brier_win | +0.0002 | [-0.0008, +0.0011] | [-0.0008, +0.0012] | indistinguishable |
| OA_SVA_C1 | brier_ot | -0.0001 | [-0.0005, +0.0003] | [-0.0005, +0.0003] | indistinguishable |
| OA_SVA_C1 | rps_total | -0.0016 | [-0.0089, +0.0055] | [-0.0079, +0.0054] | indistinguishable |
| OA_SVA_C1 | rps_margin | -0.0001 | [-0.0036, +0.0035] | [-0.0036, +0.0033] | indistinguishable |
| LEAGUE | brier_win | +0.0060 | [+0.0033, +0.0089] | [+0.0034, +0.0087] | WORSE (meaningful) |
| LEAGUE | brier_ot | -0.0001 | [-0.0006, +0.0003] | [-0.0006, +0.0003] | indistinguishable |
| LEAGUE | rps_total | -0.0002 | [-0.0100, +0.0092] | [-0.0080, +0.0083] | indistinguishable |
| LEAGUE | rps_margin | +0.0191 | [+0.0083, +0.0298] | [+0.0085, +0.0291] | WORSE (meaningful) |

Δ paired vs the retuned+recalibrated V1 (`V1_R_C1`):

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1 | brier_win | +0.0003 | [-0.0004, +0.0010] | [-0.0004, +0.0010] | indistinguishable |
| V1 | rps_total | +0.0007 | [-0.0051, +0.0064] | [-0.0047, +0.0061] | indistinguishable |
| V1 | brier_ot | +0.0004 | [-0.0001, +0.0008] | [-0.0001, +0.0008] | indistinguishable |
| V1 | rps_margin | +0.0012 | [-0.0013, +0.0038] | [-0.0011, +0.0037] | indistinguishable |
| V1_C1 | brier_win | +0.0004 | [-0.0002, +0.0010] | [-0.0002, +0.0010] | indistinguishable |
| V1_C1 | rps_total | -0.0012 | [-0.0035, +0.0009] | [-0.0032, +0.0009] | indistinguishable |
| V1_C1 | brier_ot | +0.0003 | [-0.0001, +0.0007] | [-0.0001, +0.0007] | indistinguishable |
| V1_C1 | rps_margin | +0.0007 | [-0.0014, +0.0028] | [-0.0012, +0.0028] | indistinguishable |
| V1_T | brier_win | -0.0003 | [-0.0008, +0.0002] | [-0.0009, +0.0002] | indistinguishable |
| V1_T | rps_total | +0.0027 | [-0.0036, +0.0090] | [-0.0028, +0.0084] | indistinguishable |
| V1_T | brier_ot | +0.0001 | [-0.0003, +0.0005] | [-0.0003, +0.0005] | indistinguishable |
| V1_T | rps_margin | -0.0005 | [-0.0023, +0.0012] | [-0.0023, +0.0013] | indistinguishable |
| V1_T_C1 | brier_win | +0.0000 | [+0.0000, +0.0000] | [+0.0000, +0.0000] | indistinguishable |
| V1_T_C1 | rps_total | +0.0000 | [+0.0000, +0.0000] | [+0.0000, +0.0000] | indistinguishable |
| V1_T_C1 | brier_ot | +0.0000 | [+0.0000, +0.0000] | [+0.0000, +0.0000] | indistinguishable |
| V1_T_C1 | rps_margin | +0.0000 | [+0.0000, +0.0000] | [+0.0000, +0.0000] | indistinguishable |
| V1_R | brier_win | -0.0003 | [-0.0008, +0.0002] | [-0.0009, +0.0002] | indistinguishable |
| V1_R | rps_total | +0.0027 | [-0.0036, +0.0090] | [-0.0028, +0.0084] | indistinguishable |
| V1_R | brier_ot | +0.0001 | [-0.0003, +0.0005] | [-0.0003, +0.0005] | indistinguishable |
| V1_R | rps_margin | -0.0005 | [-0.0023, +0.0012] | [-0.0023, +0.0013] | indistinguishable |
| V1_R_noB2B | brier_win | +0.0004 | [-0.0005, +0.0012] | [-0.0004, +0.0012] | indistinguishable |
| V1_R_noB2B | rps_total | +0.0027 | [-0.0036, +0.0089] | [-0.0030, +0.0084] | indistinguishable |
| V1_R_noB2B | brier_ot | +0.0002 | [-0.0002, +0.0006] | [-0.0002, +0.0006] | indistinguishable |
| V1_R_noB2B | rps_margin | +0.0012 | [-0.0019, +0.0043] | [-0.0016, +0.0040] | indistinguishable |
| V1_R_noFIN | brier_win | +0.0010 | [-0.0009, +0.0029] | [-0.0008, +0.0027] | indistinguishable |
| V1_R_noFIN | rps_total | +0.0042 | [-0.0031, +0.0114] | [-0.0035, +0.0115] | indistinguishable |
| V1_R_noFIN | brier_ot | -0.0000 | [-0.0005, +0.0004] | [-0.0005, +0.0004] | indistinguishable |
| V1_R_noFIN | rps_margin | +0.0038 | [-0.0038, +0.0110] | [-0.0027, +0.0104] | indistinguishable |
| OA_XG | brier_win | +0.0003 | [-0.0008, +0.0014] | [-0.0008, +0.0013] | indistinguishable |
| OA_XG | rps_total | +0.0003 | [-0.0083, +0.0089] | [-0.0080, +0.0083] | indistinguishable |
| OA_XG | brier_ot | +0.0006 | [+0.0002, +0.0010] | [+0.0002, +0.0010] | worse, CI excludes 0 |
| OA_XG | rps_margin | +0.0012 | [-0.0029, +0.0055] | [-0.0026, +0.0050] | indistinguishable |
| OA_SVA | brier_win | +0.0001 | [-0.0010, +0.0013] | [-0.0010, +0.0012] | indistinguishable |
| OA_SVA | rps_total | -0.0004 | [-0.0089, +0.0082] | [-0.0085, +0.0077] | indistinguishable |
| OA_SVA | brier_ot | +0.0005 | [+0.0000, +0.0009] | [-0.0000, +0.0010] | indistinguishable |
| OA_SVA | rps_margin | +0.0002 | [-0.0040, +0.0045] | [-0.0036, +0.0041] | indistinguishable |
| OA_SVA_C1 | brier_win | +0.0005 | [-0.0006, +0.0016] | [-0.0006, +0.0017] | indistinguishable |
| OA_SVA_C1 | rps_total | -0.0009 | [-0.0079, +0.0059] | [-0.0075, +0.0060] | indistinguishable |
| OA_SVA_C1 | brier_ot | +0.0002 | [-0.0002, +0.0006] | [-0.0002, +0.0007] | indistinguishable |
| OA_SVA_C1 | rps_margin | +0.0011 | [-0.0029, +0.0051] | [-0.0027, +0.0051] | indistinguishable |
| LEAGUE | brier_win | +0.0063 | [+0.0032, +0.0095] | [+0.0033, +0.0093] | WORSE (meaningful) |
| LEAGUE | rps_total | +0.0006 | [-0.0086, +0.0094] | [-0.0075, +0.0083] | indistinguishable |
| LEAGUE | brier_ot | +0.0002 | [-0.0002, +0.0007] | [-0.0003, +0.0007] | indistinguishable |
| LEAGUE | rps_margin | +0.0203 | [+0.0084, +0.0320] | [+0.0086, +0.0312] | WORSE (meaningful) |

## FAMILY_SEEN_2018_2023 (n=7157)

| arm | brier_win | logloss_win | brier_ot | rps_total | rps_margin | brier_over_5.5 | brier_over_6.5 | abs_err_total | ECE(win) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 0.2395 | 0.6717 | 0.1739 | 1.2783 | 1.4260 | 0.2438 | 0.2449 | 1.8415 | 0.0284 |
| V1_C1 | 0.2381 | 0.6687 | 0.1740 | 1.2791 | 1.4210 | 0.2441 | 0.2453 | 1.8425 | 0.0177 |
| V1_T | 0.2376 | 0.6678 | 0.1739 | 1.2822 | 1.4188 | 0.2445 | 0.2458 | 1.8427 | 0.0229 |
| V1_T_C1 | 0.2370 | 0.6665 | 0.1740 | 1.2813 | 1.4164 | 0.2445 | 0.2459 | 1.8431 | 0.0159 |
| V1_R | 0.2377 | 0.6679 | 0.1738 | 1.2823 | 1.4192 | 0.2445 | 0.2458 | 1.8437 | 0.0236 |
| V1_R_C1 | 0.2371 | 0.6668 | 0.1739 | 1.2813 | 1.4168 | 0.2446 | 0.2459 | 1.8435 | 0.0169 |
| V1_R_noB2B | 0.2383 | 0.6692 | 0.1738 | 1.2822 | 1.4216 | 0.2445 | 0.2458 | 1.8437 | 0.0205 |
| V1_R_noFIN | 0.2381 | 0.6690 | 0.1738 | 1.2898 | 1.4202 | 0.2460 | 0.2478 | 1.8546 | 0.0239 |
| OA_XG | 0.2371 | 0.6668 | 0.1740 | 1.2803 | 1.4165 | 0.2441 | 0.2455 | 1.8440 | 0.0236 |
| OA_SVA | 0.2369 | 0.6662 | 0.1740 | 1.2799 | 1.4156 | 0.2439 | 0.2453 | 1.8434 | 0.0201 |
| OA_SVA_C1 | 0.2367 | 0.6657 | 0.1742 | 1.2786 | 1.4150 | 0.2440 | 0.2452 | 1.8430 | 0.0150 |
| LEAGUE | 0.2489 | 0.6910 | 0.1738 | 1.2864 | 1.4683 | 0.2460 | 0.2471 | 1.8599 | 0.0085 |

Δ paired vs production V1:

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1_C1 | brier_win | -0.0014 | [-0.0019, -0.0009] | [-0.0019, -0.0009] | BETTER (meaningful) |
| V1_C1 | brier_ot | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0003] | indistinguishable |
| V1_C1 | rps_total | +0.0008 | [-0.0007, +0.0022] | [-0.0006, +0.0022] | indistinguishable |
| V1_C1 | rps_margin | -0.0050 | [-0.0071, -0.0030] | [-0.0071, -0.0030] | BETTER (meaningful) |
| V1_T | brier_win | -0.0018 | [-0.0023, -0.0013] | [-0.0023, -0.0013] | BETTER (meaningful) |
| V1_T | brier_ot | -0.0000 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_T | rps_total | +0.0039 | [+0.0021, +0.0056] | [+0.0021, +0.0056] | worse, CI excludes 0 |
| V1_T | rps_margin | -0.0073 | [-0.0092, -0.0053] | [-0.0093, -0.0053] | BETTER (meaningful) |
| V1_T_C1 | brier_win | -0.0024 | [-0.0032, -0.0017] | [-0.0032, -0.0017] | BETTER (meaningful) |
| V1_T_C1 | brier_ot | +0.0001 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| V1_T_C1 | rps_total | +0.0030 | [+0.0007, +0.0052] | [+0.0008, +0.0051] | worse, CI excludes 0 |
| V1_T_C1 | rps_margin | -0.0096 | [-0.0126, -0.0067] | [-0.0127, -0.0065] | BETTER (meaningful) |
| V1_R | brier_win | -0.0018 | [-0.0023, -0.0013] | [-0.0023, -0.0013] | BETTER (meaningful) |
| V1_R | brier_ot | -0.0001 | [-0.0003, +0.0000] | [-0.0003, +0.0000] | indistinguishable |
| V1_R | rps_total | +0.0039 | [+0.0022, +0.0057] | [+0.0020, +0.0057] | worse, CI excludes 0 |
| V1_R | rps_margin | -0.0068 | [-0.0087, -0.0049] | [-0.0088, -0.0049] | BETTER (meaningful) |
| V1_R_C1 | brier_win | -0.0023 | [-0.0030, -0.0016] | [-0.0031, -0.0016] | BETTER (meaningful) |
| V1_R_C1 | brier_ot | -0.0000 | [-0.0002, +0.0002] | [-0.0002, +0.0002] | indistinguishable |
| V1_R_C1 | rps_total | +0.0030 | [+0.0007, +0.0053] | [+0.0007, +0.0052] | worse, CI excludes 0 |
| V1_R_C1 | rps_margin | -0.0092 | [-0.0122, -0.0064] | [-0.0123, -0.0063] | BETTER (meaningful) |
| V1_R_noB2B | brier_win | -0.0012 | [-0.0018, -0.0006] | [-0.0018, -0.0006] | BETTER (meaningful) |
| V1_R_noB2B | brier_ot | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| V1_R_noB2B | rps_total | +0.0039 | [+0.0021, +0.0056] | [+0.0020, +0.0056] | worse, CI excludes 0 |
| V1_R_noB2B | rps_margin | -0.0044 | [-0.0067, -0.0021] | [-0.0067, -0.0022] | better, CI excludes 0 |
| V1_R_noFIN | brier_win | -0.0013 | [-0.0022, -0.0004] | [-0.0022, -0.0004] | BETTER (meaningful) |
| V1_R_noFIN | brier_ot | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| V1_R_noFIN | rps_total | +0.0115 | [+0.0076, +0.0152] | [+0.0077, +0.0152] | WORSE (meaningful) |
| V1_R_noFIN | rps_margin | -0.0058 | [-0.0094, -0.0020] | [-0.0095, -0.0021] | BETTER (meaningful) |
| OA_XG | brier_win | -0.0023 | [-0.0029, -0.0017] | [-0.0029, -0.0018] | BETTER (meaningful) |
| OA_XG | brier_ot | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0002] | indistinguishable |
| OA_XG | rps_total | +0.0020 | [-0.0003, +0.0042] | [-0.0003, +0.0044] | indistinguishable |
| OA_XG | rps_margin | -0.0096 | [-0.0121, -0.0071] | [-0.0121, -0.0072] | BETTER (meaningful) |
| OA_SVA | brier_win | -0.0026 | [-0.0032, -0.0019] | [-0.0032, -0.0019] | BETTER (meaningful) |
| OA_SVA | brier_ot | +0.0001 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| OA_SVA | rps_total | +0.0016 | [-0.0006, +0.0038] | [-0.0007, +0.0039] | indistinguishable |
| OA_SVA | rps_margin | -0.0104 | [-0.0132, -0.0076] | [-0.0132, -0.0076] | BETTER (meaningful) |
| OA_SVA_C1 | brier_win | -0.0028 | [-0.0036, -0.0019] | [-0.0037, -0.0020] | BETTER (meaningful) |
| OA_SVA_C1 | brier_ot | +0.0003 | [+0.0001, +0.0005] | [+0.0001, +0.0005] | worse, CI excludes 0 |
| OA_SVA_C1 | rps_total | +0.0003 | [-0.0016, +0.0023] | [-0.0017, +0.0023] | indistinguishable |
| OA_SVA_C1 | rps_margin | -0.0111 | [-0.0147, -0.0074] | [-0.0149, -0.0075] | BETTER (meaningful) |
| LEAGUE | brier_win | +0.0095 | [+0.0080, +0.0110] | [+0.0079, +0.0110] | WORSE (meaningful) |
| LEAGUE | brier_ot | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| LEAGUE | rps_total | +0.0081 | [+0.0040, +0.0120] | [+0.0041, +0.0123] | WORSE (meaningful) |
| LEAGUE | rps_margin | +0.0423 | [+0.0362, +0.0484] | [+0.0362, +0.0484] | WORSE (meaningful) |

Δ paired vs the retuned+recalibrated V1 (`V1_R_C1`):

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1 | brier_win | +0.0023 | [+0.0016, +0.0030] | [+0.0016, +0.0031] | WORSE (meaningful) |
| V1 | rps_total | -0.0030 | [-0.0053, -0.0007] | [-0.0052, -0.0007] | better, CI excludes 0 |
| V1 | brier_ot | +0.0000 | [-0.0002, +0.0002] | [-0.0002, +0.0002] | indistinguishable |
| V1 | rps_margin | +0.0092 | [+0.0064, +0.0122] | [+0.0063, +0.0123] | WORSE (meaningful) |
| V1_C1 | brier_win | +0.0009 | [+0.0005, +0.0014] | [+0.0005, +0.0014] | worse, CI excludes 0 |
| V1_C1 | rps_total | -0.0022 | [-0.0035, -0.0009] | [-0.0035, -0.0008] | better, CI excludes 0 |
| V1_C1 | brier_ot | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0003] | indistinguishable |
| V1_C1 | rps_margin | +0.0042 | [+0.0024, +0.0061] | [+0.0025, +0.0061] | worse, CI excludes 0 |
| V1_T | brier_win | +0.0005 | [+0.0001, +0.0008] | [+0.0001, +0.0008] | worse, CI excludes 0 |
| V1_T | rps_total | +0.0009 | [-0.0014, +0.0032] | [-0.0015, +0.0033] | indistinguishable |
| V1_T | brier_ot | -0.0000 | [-0.0002, +0.0002] | [-0.0002, +0.0002] | indistinguishable |
| V1_T | rps_margin | +0.0020 | [+0.0006, +0.0033] | [+0.0006, +0.0034] | worse, CI excludes 0 |
| V1_T_C1 | brier_win | -0.0001 | [-0.0003, +0.0000] | [-0.0003, +0.0001] | indistinguishable |
| V1_T_C1 | rps_total | -0.0000 | [-0.0004, +0.0004] | [-0.0004, +0.0004] | indistinguishable |
| V1_T_C1 | brier_ot | +0.0001 | [-0.0000, +0.0002] | [-0.0000, +0.0002] | indistinguishable |
| V1_T_C1 | rps_margin | -0.0004 | [-0.0009, +0.0002] | [-0.0010, +0.0002] | indistinguishable |
| V1_R | brier_win | +0.0005 | [+0.0002, +0.0009] | [+0.0002, +0.0009] | worse, CI excludes 0 |
| V1_R | rps_total | +0.0009 | [-0.0013, +0.0031] | [-0.0013, +0.0031] | indistinguishable |
| V1_R | brier_ot | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| V1_R | rps_margin | +0.0024 | [+0.0010, +0.0038] | [+0.0010, +0.0039] | worse, CI excludes 0 |
| V1_R_noB2B | brier_win | +0.0011 | [+0.0007, +0.0016] | [+0.0007, +0.0016] | WORSE (meaningful) |
| V1_R_noB2B | rps_total | +0.0009 | [-0.0013, +0.0031] | [-0.0013, +0.0031] | indistinguishable |
| V1_R_noB2B | brier_ot | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| V1_R_noB2B | rps_margin | +0.0048 | [+0.0031, +0.0067] | [+0.0030, +0.0067] | worse, CI excludes 0 |
| V1_R_noFIN | brier_win | +0.0010 | [+0.0000, +0.0020] | [-0.0000, +0.0020] | indistinguishable |
| V1_R_noFIN | rps_total | +0.0085 | [+0.0053, +0.0116] | [+0.0054, +0.0114] | WORSE (meaningful) |
| V1_R_noFIN | brier_ot | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| V1_R_noFIN | rps_margin | +0.0035 | [-0.0004, +0.0075] | [-0.0007, +0.0075] | indistinguishable |
| OA_XG | brier_win | -0.0000 | [-0.0005, +0.0005] | [-0.0006, +0.0005] | indistinguishable |
| OA_XG | rps_total | -0.0010 | [-0.0045, +0.0026] | [-0.0042, +0.0026] | indistinguishable |
| OA_XG | brier_ot | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0003] | indistinguishable |
| OA_XG | rps_margin | -0.0003 | [-0.0024, +0.0018] | [-0.0027, +0.0018] | indistinguishable |
| OA_SVA | brier_win | -0.0003 | [-0.0008, +0.0003] | [-0.0008, +0.0003] | indistinguishable |
| OA_SVA | rps_total | -0.0014 | [-0.0048, +0.0021] | [-0.0047, +0.0021] | indistinguishable |
| OA_SVA | brier_ot | +0.0001 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| OA_SVA | rps_margin | -0.0011 | [-0.0032, +0.0009] | [-0.0034, +0.0009] | indistinguishable |
| OA_SVA_C1 | brier_win | -0.0005 | [-0.0010, +0.0001] | [-0.0010, +0.0000] | indistinguishable |
| OA_SVA_C1 | rps_total | -0.0027 | [-0.0046, -0.0008] | [-0.0045, -0.0006] | better, CI excludes 0 |
| OA_SVA_C1 | brier_ot | +0.0003 | [+0.0001, +0.0005] | [+0.0001, +0.0005] | worse, CI excludes 0 |
| OA_SVA_C1 | rps_margin | -0.0018 | [-0.0041, +0.0004] | [-0.0041, +0.0004] | indistinguishable |
| LEAGUE | brier_win | +0.0118 | [+0.0098, +0.0139] | [+0.0097, +0.0140] | WORSE (meaningful) |
| LEAGUE | rps_total | +0.0050 | [+0.0015, +0.0086] | [+0.0014, +0.0087] | WORSE (meaningful) |
| LEAGUE | brier_ot | -0.0001 | [-0.0003, +0.0002] | [-0.0003, +0.0002] | indistinguishable |
| LEAGUE | rps_margin | +0.0516 | [+0.0432, +0.0601] | [+0.0430, +0.0601] | WORSE (meaningful) |

## EXPOSED_2024_2025 (n=2624)

| arm | brier_win | logloss_win | brier_ot | rps_total | rps_margin | brier_over_5.5 | brier_over_6.5 | abs_err_total | ECE(win) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 0.2419 | 0.6766 | 0.1786 | 1.2896 | 1.4335 | 0.2467 | 0.2472 | 1.8681 | 0.0225 |
| V1_C1 | 0.2414 | 0.6755 | 0.1789 | 1.2870 | 1.4308 | 0.2462 | 0.2466 | 1.8652 | 0.0252 |
| V1_T | 0.2412 | 0.6752 | 0.1787 | 1.2919 | 1.4307 | 0.2472 | 0.2476 | 1.8711 | 0.0259 |
| V1_T_C1 | 0.2413 | 0.6753 | 0.1786 | 1.2871 | 1.4308 | 0.2464 | 0.2468 | 1.8643 | 0.0283 |
| V1_R | 0.2410 | 0.6746 | 0.1787 | 1.2926 | 1.4304 | 0.2473 | 0.2479 | 1.8721 | 0.0278 |
| V1_R_C1 | 0.2412 | 0.6751 | 0.1788 | 1.2873 | 1.4317 | 0.2464 | 0.2468 | 1.8645 | 0.0289 |
| V1_R_noB2B | 0.2418 | 0.6763 | 0.1787 | 1.2928 | 1.4333 | 0.2474 | 0.2478 | 1.8726 | 0.0260 |
| V1_R_noFIN | 0.2416 | 0.6759 | 0.1786 | 1.2906 | 1.4354 | 0.2468 | 0.2472 | 1.8712 | 0.0208 |
| OA_XG | 0.2409 | 0.6744 | 0.1786 | 1.2933 | 1.4295 | 0.2474 | 0.2479 | 1.8710 | 0.0226 |
| OA_SVA | 0.2409 | 0.6744 | 0.1786 | 1.2937 | 1.4295 | 0.2475 | 0.2480 | 1.8718 | 0.0231 |
| OA_SVA_C1 | 0.2412 | 0.6751 | 0.1788 | 1.2869 | 1.4304 | 0.2462 | 0.2467 | 1.8651 | 0.0180 |
| LEAGUE | 0.2483 | 0.6897 | 0.1785 | 1.2895 | 1.4636 | 0.2469 | 0.2475 | 1.8726 | 0.0005 |

Δ paired vs production V1:

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1_C1 | brier_win | -0.0005 | [-0.0014, +0.0006] | [-0.0015, +0.0005] | indistinguishable |
| V1_C1 | brier_ot | +0.0003 | [-0.0000, +0.0006] | [+0.0000, +0.0006] | indistinguishable |
| V1_C1 | rps_total | -0.0026 | [-0.0045, -0.0006] | [-0.0044, -0.0006] | better, CI excludes 0 |
| V1_C1 | rps_margin | -0.0027 | [-0.0066, +0.0013] | [-0.0068, +0.0011] | indistinguishable |
| V1_T | brier_win | -0.0007 | [-0.0017, +0.0003] | [-0.0016, +0.0003] | indistinguishable |
| V1_T | brier_ot | +0.0001 | [-0.0002, +0.0004] | [-0.0002, +0.0004] | indistinguishable |
| V1_T | rps_total | +0.0023 | [+0.0001, +0.0046] | [+0.0001, +0.0044] | worse, CI excludes 0 |
| V1_T | rps_margin | -0.0028 | [-0.0068, +0.0010] | [-0.0066, +0.0011] | indistinguishable |
| V1_T_C1 | brier_win | -0.0006 | [-0.0020, +0.0010] | [-0.0020, +0.0009] | indistinguishable |
| V1_T_C1 | brier_ot | -0.0000 | [-0.0003, +0.0003] | [-0.0003, +0.0003] | indistinguishable |
| V1_T_C1 | rps_total | -0.0025 | [-0.0052, +0.0004] | [-0.0051, +0.0003] | indistinguishable |
| V1_T_C1 | rps_margin | -0.0027 | [-0.0087, +0.0034] | [-0.0085, +0.0032] | indistinguishable |
| V1_R | brier_win | -0.0009 | [-0.0021, +0.0003] | [-0.0020, +0.0002] | indistinguishable |
| V1_R | brier_ot | +0.0001 | [-0.0002, +0.0004] | [-0.0002, +0.0004] | indistinguishable |
| V1_R | rps_total | +0.0030 | [+0.0004, +0.0057] | [+0.0004, +0.0055] | worse, CI excludes 0 |
| V1_R | rps_margin | -0.0031 | [-0.0078, +0.0013] | [-0.0076, +0.0014] | indistinguishable |
| V1_R_C1 | brier_win | -0.0007 | [-0.0023, +0.0010] | [-0.0023, +0.0010] | indistinguishable |
| V1_R_C1 | brier_ot | +0.0002 | [-0.0001, +0.0005] | [-0.0001, +0.0006] | indistinguishable |
| V1_R_C1 | rps_total | -0.0023 | [-0.0051, +0.0007] | [-0.0049, +0.0006] | indistinguishable |
| V1_R_C1 | rps_margin | -0.0017 | [-0.0085, +0.0051] | [-0.0084, +0.0049] | indistinguishable |
| V1_R_noB2B | brier_win | -0.0002 | [-0.0014, +0.0012] | [-0.0014, +0.0011] | indistinguishable |
| V1_R_noB2B | brier_ot | +0.0001 | [-0.0002, +0.0004] | [-0.0002, +0.0004] | indistinguishable |
| V1_R_noB2B | rps_total | +0.0032 | [+0.0006, +0.0059] | [+0.0005, +0.0057] | worse, CI excludes 0 |
| V1_R_noB2B | rps_margin | -0.0002 | [-0.0054, +0.0051] | [-0.0054, +0.0047] | indistinguishable |
| V1_R_noFIN | brier_win | -0.0003 | [-0.0021, +0.0015] | [-0.0021, +0.0015] | indistinguishable |
| V1_R_noFIN | brier_ot | -0.0000 | [-0.0003, +0.0003] | [-0.0004, +0.0003] | indistinguishable |
| V1_R_noFIN | rps_total | +0.0010 | [-0.0044, +0.0063] | [-0.0040, +0.0062] | indistinguishable |
| V1_R_noFIN | rps_margin | +0.0020 | [-0.0051, +0.0090] | [-0.0053, +0.0090] | indistinguishable |
| OA_XG | brier_win | -0.0010 | [-0.0021, +0.0001] | [-0.0020, +0.0000] | indistinguishable |
| OA_XG | brier_ot | -0.0000 | [-0.0003, +0.0003] | [-0.0003, +0.0003] | indistinguishable |
| OA_XG | rps_total | +0.0037 | [+0.0001, +0.0074] | [+0.0004, +0.0070] | worse, CI excludes 0 |
| OA_XG | rps_margin | -0.0040 | [-0.0086, +0.0008] | [-0.0083, +0.0004] | indistinguishable |
| OA_SVA | brier_win | -0.0010 | [-0.0022, +0.0002] | [-0.0021, +0.0001] | indistinguishable |
| OA_SVA | brier_ot | -0.0000 | [-0.0003, +0.0003] | [-0.0003, +0.0003] | indistinguishable |
| OA_SVA | rps_total | +0.0041 | [+0.0006, +0.0078] | [+0.0008, +0.0074] | worse, CI excludes 0 |
| OA_SVA | rps_margin | -0.0040 | [-0.0088, +0.0012] | [-0.0087, +0.0007] | indistinguishable |
| OA_SVA_C1 | brier_win | -0.0007 | [-0.0022, +0.0009] | [-0.0020, +0.0008] | indistinguishable |
| OA_SVA_C1 | brier_ot | +0.0002 | [-0.0001, +0.0005] | [-0.0001, +0.0005] | indistinguishable |
| OA_SVA_C1 | rps_total | -0.0027 | [-0.0054, +0.0001] | [-0.0053, -0.0000] | indistinguishable |
| OA_SVA_C1 | rps_margin | -0.0031 | [-0.0093, +0.0035] | [-0.0091, +0.0030] | indistinguishable |
| LEAGUE | brier_win | +0.0064 | [+0.0041, +0.0085] | [+0.0042, +0.0086] | WORSE (meaningful) |
| LEAGUE | brier_ot | -0.0001 | [-0.0004, +0.0002] | [-0.0005, +0.0002] | indistinguishable |
| LEAGUE | rps_total | -0.0001 | [-0.0064, +0.0060] | [-0.0060, +0.0057] | indistinguishable |
| LEAGUE | rps_margin | +0.0301 | [+0.0213, +0.0388] | [+0.0214, +0.0395] | WORSE (meaningful) |

Δ paired vs the retuned+recalibrated V1 (`V1_R_C1`):

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1 | brier_win | +0.0007 | [-0.0010, +0.0023] | [-0.0010, +0.0023] | indistinguishable |
| V1 | rps_total | +0.0023 | [-0.0007, +0.0051] | [-0.0006, +0.0049] | indistinguishable |
| V1 | brier_ot | -0.0002 | [-0.0005, +0.0001] | [-0.0006, +0.0001] | indistinguishable |
| V1 | rps_margin | +0.0017 | [-0.0051, +0.0085] | [-0.0049, +0.0084] | indistinguishable |
| V1_C1 | brier_win | +0.0002 | [-0.0010, +0.0013] | [-0.0010, +0.0013] | indistinguishable |
| V1_C1 | rps_total | -0.0003 | [-0.0019, +0.0013] | [-0.0018, +0.0013] | indistinguishable |
| V1_C1 | brier_ot | +0.0001 | [-0.0002, +0.0004] | [-0.0002, +0.0004] | indistinguishable |
| V1_C1 | rps_margin | -0.0010 | [-0.0057, +0.0038] | [-0.0057, +0.0037] | indistinguishable |
| V1_T | brier_win | -0.0000 | [-0.0009, +0.0008] | [-0.0008, +0.0008] | indistinguishable |
| V1_T | rps_total | +0.0046 | [+0.0014, +0.0079] | [+0.0015, +0.0077] | worse, CI excludes 0 |
| V1_T | brier_ot | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0002] | indistinguishable |
| V1_T | rps_margin | -0.0011 | [-0.0044, +0.0023] | [-0.0043, +0.0023] | indistinguishable |
| V1_T_C1 | brier_win | +0.0001 | [-0.0002, +0.0004] | [-0.0003, +0.0005] | indistinguishable |
| V1_T_C1 | rps_total | -0.0002 | [-0.0008, +0.0004] | [-0.0009, +0.0004] | indistinguishable |
| V1_T_C1 | brier_ot | -0.0002 | [-0.0005, +0.0000] | [-0.0005, +0.0000] | indistinguishable |
| V1_T_C1 | rps_margin | -0.0009 | [-0.0022, +0.0003] | [-0.0022, +0.0003] | indistinguishable |
| V1_R | brier_win | -0.0002 | [-0.0009, +0.0004] | [-0.0009, +0.0005] | indistinguishable |
| V1_R | rps_total | +0.0052 | [+0.0017, +0.0087] | [+0.0019, +0.0086] | WORSE (meaningful) |
| V1_R | brier_ot | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0002] | indistinguishable |
| V1_R | rps_margin | -0.0014 | [-0.0040, +0.0013] | [-0.0040, +0.0013] | indistinguishable |
| V1_R_noB2B | brier_win | +0.0005 | [-0.0003, +0.0014] | [-0.0004, +0.0014] | indistinguishable |
| V1_R_noB2B | rps_total | +0.0055 | [+0.0019, +0.0091] | [+0.0021, +0.0088] | WORSE (meaningful) |
| V1_R_noB2B | brier_ot | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0002] | indistinguishable |
| V1_R_noB2B | rps_margin | +0.0015 | [-0.0019, +0.0050] | [-0.0020, +0.0052] | indistinguishable |
| V1_R_noFIN | brier_win | +0.0004 | [-0.0012, +0.0019] | [-0.0013, +0.0022] | indistinguishable |
| V1_R_noFIN | rps_total | +0.0032 | [-0.0014, +0.0078] | [-0.0011, +0.0075] | indistinguishable |
| V1_R_noFIN | brier_ot | -0.0002 | [-0.0005, +0.0001] | [-0.0005, +0.0001] | indistinguishable |
| V1_R_noFIN | rps_margin | +0.0037 | [-0.0027, +0.0102] | [-0.0024, +0.0107] | indistinguishable |
| OA_XG | brier_win | -0.0003 | [-0.0016, +0.0010] | [-0.0017, +0.0010] | indistinguishable |
| OA_XG | rps_total | +0.0060 | [+0.0011, +0.0110] | [+0.0017, +0.0102] | WORSE (meaningful) |
| OA_XG | brier_ot | -0.0002 | [-0.0005, +0.0001] | [-0.0005, +0.0001] | indistinguishable |
| OA_XG | rps_margin | -0.0023 | [-0.0073, +0.0029] | [-0.0076, +0.0031] | indistinguishable |
| OA_SVA | brier_win | -0.0004 | [-0.0016, +0.0009] | [-0.0017, +0.0009] | indistinguishable |
| OA_SVA | rps_total | +0.0064 | [+0.0016, +0.0114] | [+0.0020, +0.0106] | WORSE (meaningful) |
| OA_SVA | brier_ot | -0.0002 | [-0.0005, +0.0001] | [-0.0005, +0.0001] | indistinguishable |
| OA_SVA | rps_margin | -0.0023 | [-0.0070, +0.0026] | [-0.0075, +0.0027] | indistinguishable |
| OA_SVA_C1 | brier_win | -0.0000 | [-0.0012, +0.0012] | [-0.0012, +0.0012] | indistinguishable |
| OA_SVA_C1 | rps_total | -0.0005 | [-0.0026, +0.0018] | [-0.0024, +0.0015] | indistinguishable |
| OA_SVA_C1 | brier_ot | -0.0000 | [-0.0003, +0.0003] | [-0.0003, +0.0003] | indistinguishable |
| OA_SVA_C1 | rps_margin | -0.0014 | [-0.0060, +0.0033] | [-0.0064, +0.0034] | indistinguishable |
| LEAGUE | brier_win | +0.0070 | [+0.0033, +0.0106] | [+0.0036, +0.0106] | WORSE (meaningful) |
| LEAGUE | rps_total | +0.0022 | [-0.0028, +0.0070] | [-0.0024, +0.0069] | indistinguishable |
| LEAGUE | brier_ot | -0.0003 | [-0.0008, +0.0001] | [-0.0007, +0.0001] | indistinguishable |
| LEAGUE | rps_margin | +0.0318 | [+0.0174, +0.0464] | [+0.0179, +0.0467] | WORSE (meaningful) |

## POOLED_2017_2025 (n=11052)

| arm | brier_win | logloss_win | brier_ot | rps_total | rps_margin | brier_over_5.5 | brier_over_6.5 | abs_err_total | ECE(win) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 0.2402 | 0.6731 | 0.1759 | 1.2841 | 1.4218 | 0.2452 | 0.2453 | 1.8537 | 0.0228 |
| V1_C1 | 0.2392 | 0.6709 | 0.1761 | 1.2838 | 1.4178 | 0.2453 | 0.2454 | 1.8537 | 0.0136 |
| V1_T | 0.2387 | 0.6701 | 0.1759 | 1.2874 | 1.4162 | 0.2459 | 0.2460 | 1.8553 | 0.0166 |
| V1_T_C1 | 0.2384 | 0.6694 | 0.1759 | 1.2853 | 1.4148 | 0.2457 | 0.2459 | 1.8540 | 0.0108 |
| V1_R | 0.2387 | 0.6701 | 0.1759 | 1.2876 | 1.4164 | 0.2459 | 0.2461 | 1.8562 | 0.0174 |
| V1_R_C1 | 0.2385 | 0.6695 | 0.1759 | 1.2854 | 1.4152 | 0.2458 | 0.2459 | 1.8544 | 0.0110 |
| V1_R_noB2B | 0.2394 | 0.6715 | 0.1759 | 1.2876 | 1.4189 | 0.2459 | 0.2460 | 1.8564 | 0.0168 |
| V1_R_noFIN | 0.2393 | 0.6714 | 0.1758 | 1.2921 | 1.4188 | 0.2469 | 0.2473 | 1.8641 | 0.0174 |
| OA_XG | 0.2384 | 0.6694 | 0.1760 | 1.2862 | 1.4146 | 0.2455 | 0.2457 | 1.8558 | 0.0187 |
| OA_SVA | 0.2382 | 0.6690 | 0.1760 | 1.2860 | 1.4140 | 0.2454 | 0.2457 | 1.8556 | 0.0150 |
| OA_SVA_C1 | 0.2382 | 0.6690 | 0.1762 | 1.2834 | 1.4139 | 0.2452 | 0.2453 | 1.8540 | 0.0086 |
| LEAGUE | 0.2485 | 0.6901 | 0.1758 | 1.2893 | 1.4585 | 0.2467 | 0.2469 | 1.8674 | 0.0032 |

Δ paired vs production V1:

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1_C1 | brier_win | -0.0010 | [-0.0014, -0.0006] | [-0.0014, -0.0006] | better, CI excludes 0 |
| V1_C1 | brier_ot | +0.0001 | [-0.0000, +0.0003] | [-0.0000, +0.0003] | indistinguishable |
| V1_C1 | rps_total | -0.0003 | [-0.0015, +0.0009] | [-0.0015, +0.0008] | indistinguishable |
| V1_C1 | rps_margin | -0.0040 | [-0.0055, -0.0023] | [-0.0056, -0.0023] | better, CI excludes 0 |
| V1_T | brier_win | -0.0014 | [-0.0018, -0.0010] | [-0.0018, -0.0010] | BETTER (meaningful) |
| V1_T | brier_ot | -0.0000 | [-0.0002, +0.0001] | [-0.0001, +0.0001] | indistinguishable |
| V1_T | rps_total | +0.0033 | [+0.0020, +0.0046] | [+0.0020, +0.0046] | worse, CI excludes 0 |
| V1_T | rps_margin | -0.0056 | [-0.0071, -0.0039] | [-0.0072, -0.0040] | BETTER (meaningful) |
| V1_T_C1 | brier_win | -0.0017 | [-0.0023, -0.0012] | [-0.0023, -0.0012] | BETTER (meaningful) |
| V1_T_C1 | brier_ot | +0.0000 | [-0.0001, +0.0001] | [-0.0001, +0.0001] | indistinguishable |
| V1_T_C1 | rps_total | +0.0013 | [-0.0004, +0.0029] | [-0.0005, +0.0029] | indistinguishable |
| V1_T_C1 | rps_margin | -0.0070 | [-0.0093, -0.0046] | [-0.0094, -0.0046] | BETTER (meaningful) |
| V1_R | brier_win | -0.0014 | [-0.0018, -0.0010] | [-0.0019, -0.0010] | BETTER (meaningful) |
| V1_R | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_R | rps_total | +0.0035 | [+0.0022, +0.0049] | [+0.0021, +0.0049] | worse, CI excludes 0 |
| V1_R | rps_margin | -0.0054 | [-0.0070, -0.0036] | [-0.0070, -0.0037] | BETTER (meaningful) |
| V1_R_C1 | brier_win | -0.0017 | [-0.0023, -0.0011] | [-0.0023, -0.0011] | BETTER (meaningful) |
| V1_R_C1 | brier_ot | +0.0000 | [-0.0001, +0.0001] | [-0.0001, +0.0001] | indistinguishable |
| V1_R_C1 | rps_total | +0.0013 | [-0.0004, +0.0030] | [-0.0004, +0.0031] | indistinguishable |
| V1_R_C1 | rps_margin | -0.0065 | [-0.0090, -0.0040] | [-0.0090, -0.0041] | BETTER (meaningful) |
| V1_R_noB2B | brier_win | -0.0008 | [-0.0013, -0.0003] | [-0.0013, -0.0003] | better, CI excludes 0 |
| V1_R_noB2B | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_R_noB2B | rps_total | +0.0035 | [+0.0022, +0.0049] | [+0.0021, +0.0048] | worse, CI excludes 0 |
| V1_R_noB2B | rps_margin | -0.0029 | [-0.0049, -0.0009] | [-0.0049, -0.0009] | better, CI excludes 0 |
| V1_R_noFIN | brier_win | -0.0008 | [-0.0016, -0.0001] | [-0.0016, -0.0001] | better, CI excludes 0 |
| V1_R_noFIN | brier_ot | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| V1_R_noFIN | rps_total | +0.0081 | [+0.0052, +0.0109] | [+0.0052, +0.0110] | WORSE (meaningful) |
| V1_R_noFIN | rps_margin | -0.0030 | [-0.0061, +0.0002] | [-0.0060, +0.0001] | indistinguishable |
| OA_XG | brier_win | -0.0018 | [-0.0022, -0.0013] | [-0.0022, -0.0013] | BETTER (meaningful) |
| OA_XG | brier_ot | +0.0001 | [-0.0001, +0.0002] | [-0.0000, +0.0002] | indistinguishable |
| OA_XG | rps_total | +0.0021 | [+0.0004, +0.0040] | [+0.0004, +0.0039] | worse, CI excludes 0 |
| OA_XG | rps_margin | -0.0071 | [-0.0091, -0.0052] | [-0.0090, -0.0052] | BETTER (meaningful) |
| OA_SVA | brier_win | -0.0019 | [-0.0025, -0.0014] | [-0.0025, -0.0014] | BETTER (meaningful) |
| OA_SVA | brier_ot | +0.0000 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| OA_SVA | rps_total | +0.0019 | [+0.0002, +0.0037] | [+0.0002, +0.0036] | worse, CI excludes 0 |
| OA_SVA | rps_margin | -0.0078 | [-0.0100, -0.0056] | [-0.0099, -0.0056] | BETTER (meaningful) |
| OA_SVA_C1 | brier_win | -0.0019 | [-0.0026, -0.0013] | [-0.0026, -0.0013] | BETTER (meaningful) |
| OA_SVA_C1 | brier_ot | +0.0002 | [+0.0001, +0.0004] | [+0.0001, +0.0004] | worse, CI excludes 0 |
| OA_SVA_C1 | rps_total | -0.0006 | [-0.0022, +0.0010] | [-0.0022, +0.0010] | indistinguishable |
| OA_SVA_C1 | rps_margin | -0.0079 | [-0.0107, -0.0051] | [-0.0107, -0.0051] | BETTER (meaningful) |
| LEAGUE | brier_win | +0.0083 | [+0.0072, +0.0094] | [+0.0071, +0.0095] | WORSE (meaningful) |
| LEAGUE | brier_ot | -0.0001 | [-0.0003, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| LEAGUE | rps_total | +0.0052 | [+0.0020, +0.0083] | [+0.0021, +0.0084] | WORSE (meaningful) |
| LEAGUE | rps_margin | +0.0367 | [+0.0321, +0.0412] | [+0.0320, +0.0414] | WORSE (meaningful) |

Δ paired vs the retuned+recalibrated V1 (`V1_R_C1`):

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1 | brier_win | +0.0017 | [+0.0011, +0.0023] | [+0.0011, +0.0023] | WORSE (meaningful) |
| V1 | rps_total | -0.0013 | [-0.0030, +0.0004] | [-0.0031, +0.0004] | indistinguishable |
| V1 | brier_ot | -0.0000 | [-0.0001, +0.0001] | [-0.0001, +0.0001] | indistinguishable |
| V1 | rps_margin | +0.0065 | [+0.0040, +0.0090] | [+0.0041, +0.0090] | WORSE (meaningful) |
| V1_C1 | brier_win | +0.0007 | [+0.0003, +0.0011] | [+0.0003, +0.0011] | worse, CI excludes 0 |
| V1_C1 | rps_total | -0.0016 | [-0.0026, -0.0007] | [-0.0026, -0.0007] | better, CI excludes 0 |
| V1_C1 | brier_ot | +0.0001 | [-0.0000, +0.0003] | [+0.0000, +0.0003] | indistinguishable |
| V1_C1 | rps_margin | +0.0026 | [+0.0009, +0.0042] | [+0.0010, +0.0042] | worse, CI excludes 0 |
| V1_T | brier_win | +0.0003 | [-0.0000, +0.0006] | [-0.0000, +0.0006] | indistinguishable |
| V1_T | rps_total | +0.0020 | [+0.0001, +0.0038] | [+0.0002, +0.0038] | worse, CI excludes 0 |
| V1_T | brier_ot | -0.0000 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_T | rps_margin | +0.0010 | [-0.0002, +0.0021] | [-0.0002, +0.0021] | indistinguishable |
| V1_T_C1 | brier_win | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_T_C1 | rps_total | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0002] | indistinguishable |
| V1_T_C1 | brier_ot | +0.0000 | [-0.0001, +0.0001] | [-0.0001, +0.0001] | indistinguishable |
| V1_T_C1 | rps_margin | -0.0005 | [-0.0009, +0.0000] | [-0.0009, +0.0000] | indistinguishable |
| V1_R | brier_win | +0.0003 | [-0.0000, +0.0005] | [-0.0000, +0.0006] | indistinguishable |
| V1_R | rps_total | +0.0022 | [+0.0004, +0.0039] | [+0.0005, +0.0040] | worse, CI excludes 0 |
| V1_R | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0000] | indistinguishable |
| V1_R | rps_margin | +0.0012 | [+0.0001, +0.0022] | [+0.0000, +0.0023] | worse, CI excludes 0 |
| V1_R_noB2B | brier_win | +0.0009 | [+0.0005, +0.0013] | [+0.0005, +0.0013] | worse, CI excludes 0 |
| V1_R_noB2B | rps_total | +0.0022 | [+0.0004, +0.0040] | [+0.0004, +0.0040] | worse, CI excludes 0 |
| V1_R_noB2B | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_R_noB2B | rps_margin | +0.0036 | [+0.0021, +0.0050] | [+0.0021, +0.0051] | worse, CI excludes 0 |
| V1_R_noFIN | brier_win | +0.0008 | [+0.0001, +0.0016] | [+0.0001, +0.0016] | worse, CI excludes 0 |
| V1_R_noFIN | rps_total | +0.0067 | [+0.0042, +0.0093] | [+0.0044, +0.0091] | WORSE (meaningful) |
| V1_R_noFIN | brier_ot | -0.0001 | [-0.0003, +0.0000] | [-0.0003, +0.0000] | indistinguishable |
| V1_R_noFIN | rps_margin | +0.0036 | [+0.0006, +0.0067] | [+0.0004, +0.0067] | worse, CI excludes 0 |
| OA_XG | brier_win | -0.0001 | [-0.0005, +0.0004] | [-0.0005, +0.0004] | indistinguishable |
| OA_XG | rps_total | +0.0008 | [-0.0019, +0.0036] | [-0.0017, +0.0033] | indistinguishable |
| OA_XG | brier_ot | +0.0001 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| OA_XG | rps_margin | -0.0006 | [-0.0025, +0.0012] | [-0.0025, +0.0013] | indistinguishable |
| OA_SVA | brier_win | -0.0002 | [-0.0007, +0.0002] | [-0.0007, +0.0002] | indistinguishable |
| OA_SVA | rps_total | +0.0006 | [-0.0021, +0.0033] | [-0.0019, +0.0031] | indistinguishable |
| OA_SVA | brier_ot | +0.0000 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| OA_SVA | rps_margin | -0.0013 | [-0.0031, +0.0005] | [-0.0031, +0.0006] | indistinguishable |
| OA_SVA_C1 | brier_win | -0.0003 | [-0.0007, +0.0002] | [-0.0007, +0.0002] | indistinguishable |
| OA_SVA_C1 | rps_total | -0.0020 | [-0.0035, -0.0004] | [-0.0034, -0.0005] | better, CI excludes 0 |
| OA_SVA_C1 | brier_ot | +0.0002 | [+0.0001, +0.0003] | [+0.0001, +0.0003] | worse, CI excludes 0 |
| OA_SVA_C1 | rps_margin | -0.0014 | [-0.0033, +0.0004] | [-0.0033, +0.0005] | indistinguishable |
| LEAGUE | brier_win | +0.0100 | [+0.0085, +0.0116] | [+0.0083, +0.0117] | WORSE (meaningful) |
| LEAGUE | rps_total | +0.0039 | [+0.0010, +0.0065] | [+0.0012, +0.0066] | worse, CI excludes 0 |
| LEAGUE | brier_ot | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| LEAGUE | rps_margin | +0.0433 | [+0.0367, +0.0497] | [+0.0364, +0.0501] | WORSE (meaningful) |

## Per season: Δ Brier(win) vs V1 (negative = better)

| season | n | V1_C1 | V1_T | V1_T_C1 | V1_R | V1_R_C1 | V1_R_noB2B | V1_R_noFIN | OA_XG | OA_SVA | OA_SVA_C1 | LEAGUE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2017 | 1271 | +0.0001 | -0.0006 | -0.0003 | -0.0006 | -0.0003 | +0.0001 | +0.0007 | -0.0000 | -0.0002 | +0.0002 | +0.0060 |
| 2018 | 1271 | -0.0006 | -0.0010 | -0.0008 | -0.0010 | -0.0008 | -0.0004 | -0.0014 | -0.0015 | -0.0018 | -0.0015 | +0.0040 |
| 2019 | 1082 | -0.0004 | -0.0007 | -0.0009 | -0.0007 | -0.0009 | -0.0006 | +0.0006 | -0.0005 | -0.0009 | -0.0009 | +0.0043 |
| 2020 | 868 | -0.0013 | -0.0025 | -0.0032 | -0.0034 | -0.0036 | -0.0028 | -0.0011 | -0.0024 | -0.0028 | -0.0031 | +0.0119 |
| 2021 | 1312 | -0.0023 | -0.0036 | -0.0051 | -0.0027 | -0.0039 | -0.0016 | -0.0015 | -0.0027 | -0.0030 | -0.0039 | +0.0140 |
| 2022 | 1312 | -0.0019 | -0.0018 | -0.0028 | -0.0018 | -0.0029 | -0.0012 | -0.0026 | -0.0035 | -0.0037 | -0.0041 | +0.0118 |
| 2023 | 1312 | -0.0015 | -0.0013 | -0.0017 | -0.0013 | -0.0019 | -0.0009 | -0.0015 | -0.0030 | -0.0030 | -0.0029 | +0.0105 |
| 2024 | 1312 | -0.0013 | -0.0012 | -0.0013 | -0.0017 | -0.0015 | -0.0005 | -0.0002 | -0.0007 | -0.0009 | -0.0006 | +0.0087 |
| 2025 | 1312 | +0.0004 | -0.0002 | +0.0002 | -0.0002 | +0.0001 | +0.0002 | -0.0005 | -0.0013 | -0.0011 | -0.0007 | +0.0040 |

## Preregistered decision rules

**R1_retune_vs_V1** — `V1_R` vs `V1`: **NOT BETTER** (gate CIs ok; size ≥ threshold ok; favourable seasons 9/9; no primary metric worse FAIL)

| metric | Δ | 95% games | 95% slates |
|---|---:|---|---|
| brier_win | -0.0014 | [-0.0018, -0.0010] | [-0.0019, -0.0010] |
| rps_total | +0.0035 | [+0.0022, +0.0049] | [+0.0021, +0.0049] |
| brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] |

**R2_recalibration_on_retuned** — `V1_R_C1` vs `V1_R`: **NOT BETTER** (gate CIs fail; size ≥ threshold fail; favourable seasons 5/9; no primary metric worse ok)

| metric | Δ | 95% games | 95% slates |
|---|---:|---|---|
| brier_win | -0.0003 | [-0.0005, +0.0000] | [-0.0006, +0.0000] |
| rps_total | -0.0022 | [-0.0039, -0.0004] | [-0.0040, -0.0005] |
| brier_ot | +0.0001 | [-0.0001, +0.0002] | [-0.0000, +0.0002] |

**R3_opponent_adjustment_incremental** — `OA_SVA_C1` vs `V1_R_C1`: **NOT BETTER** (gate CIs fail; size ≥ threshold fail; favourable seasons 5/9; no primary metric worse FAIL)

| metric | Δ | 95% games | 95% slates |
|---|---:|---|---|
| brier_win | -0.0003 | [-0.0007, +0.0002] | [-0.0007, +0.0002] |
| rps_total | -0.0020 | [-0.0035, -0.0004] | [-0.0034, -0.0005] |
| brier_ot | +0.0002 | [+0.0001, +0.0003] | [+0.0001, +0.0003] |

**R4_leading_candidate**: leads = `TIE: V1_R_C1, V1_T_C1, V1_C1`; within the practical threshold of the best: ['V1_R_C1', 'V1_T_C1', 'V1_C1']; simplest of those: ['V1_R_C1', 'V1_T_C1', 'V1_C1'] · 'leads' ranks historical evidence only; it is not a promotion

## Feature ablations (R5; ablation minus `V1_R`, positive = the feature helps)

| ablation | feature | metric | Δ | 95% games | 95% slates | informative |
|---|---|---|---:|---|---|---|
| V1_R_noB2B | back-to-back adjustment | brier_win | +0.0007 | [+0.0004, +0.0009] | [+0.0004, +0.0009] | yes |
| V1_R_noB2B | back-to-back adjustment | rps_total | +0.0000 | [-0.0003, +0.0003] | [-0.0002, +0.0003] | yes |
| V1_R_noB2B | back-to-back adjustment | brier_ot | +0.0000 | [-0.0000, +0.0001] | [-0.0000, +0.0001] | yes |
| V1_R_noFIN | finishing ratio | brier_win | +0.0006 | [-0.0001, +0.0013] | [-0.0001, +0.0013] | yes |
| V1_R_noFIN | finishing ratio | rps_total | +0.0046 | [+0.0021, +0.0070] | [+0.0022, +0.0071] | yes |
| V1_R_noFIN | finishing ratio | brier_ot | -0.0000 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | yes |

## V2 simulator (exploratory; 3936 games, seasons [2023, 2024, 2025]) — Δ vs V1

| arm | metric | Δ | 95% games | 95% slates |
|---|---|---:|---|---|
| V1_R | brier_win | -0.0011 | [-0.0020, -0.0002] | [-0.0019, -0.0002] |
| V1_R | brier_ot | -0.0000 | [-0.0002, +0.0002] | [-0.0002, +0.0002] |
| V1_R_C1 | brier_win | -0.0011 | [-0.0025, +0.0002] | [-0.0024, +0.0002] |
| V1_R_C1 | brier_ot | +0.0001 | [-0.0001, +0.0004] | [-0.0001, +0.0004] |
| OA_SVA_C1 | brier_win | -0.0014 | [-0.0027, -0.0002] | [-0.0027, -0.0002] |
| OA_SVA_C1 | brier_ot | +0.0002 | [-0.0001, +0.0004] | [-0.0001, +0.0004] |
| SIM2 | brier_win | -0.0002 | [-0.0005, +0.0001] | [-0.0005, +0.0001] |
| SIM2 | brier_ot | -0.0022 | [-0.0032, -0.0011] | [-0.0031, -0.0012] |
| SIM2_ST | brier_win | +0.0001 | [-0.0004, +0.0007] | [-0.0004, +0.0007] |
| SIM2_ST | brier_ot | -0.0022 | [-0.0033, -0.0011] | [-0.0032, -0.0013] |
| SIM2_ST_GTT | brier_win | -0.0004 | [-0.0011, +0.0003] | [-0.0011, +0.0004] |
| SIM2_ST_GTT | brier_ot | -0.0021 | [-0.0031, -0.0010] | [-0.0030, -0.0011] |

exploratory; V2 hazards need shots from 2021 so only 2023-2025 exist; the combination of retuned rates with the V2 simulator was NOT run

## Against the Kalshi midpoint at T-60m (season 2025); Kalshi candle-close midpoint; a midpoint advantage is not an execution edge

### home_win (n=1312; market Brier 0.2442)

| forecaster | kind | Brier | Δ vs market | 95% games | verdict |
|---|---|---:|---:|---|---|
| V1 | INDEPENDENT | 0.2459 | +0.0017 | [-0.0014, +0.0047] | indistinguishable |
| V1_R | INDEPENDENT | 0.2457 | +0.0015 | [-0.0011, +0.0041] | indistinguishable |
| V1_R_C1 | INDEPENDENT | 0.2460 | +0.0018 | [-0.0008, +0.0043] | indistinguishable |
| V1_T_C1 | INDEPENDENT | 0.2461 | +0.0019 | [-0.0008, +0.0044] | indistinguishable |
| OA_SVA_C1 | INDEPENDENT | 0.2452 | +0.0010 | [-0.0019, +0.0036] | indistinguishable |

### total_over_5.5 (n=1196; market Brier 0.2419)

| forecaster | kind | Brier | Δ vs market | 95% games | verdict |
|---|---|---:|---:|---|---|
| V1 | INDEPENDENT | 0.2444 | +0.0025 | [+0.0004, +0.0047] | market better |
| V1_R | INDEPENDENT | 0.2440 | +0.0021 | [-0.0004, +0.0045] | indistinguishable |
| V1_R_C1 | INDEPENDENT | 0.2438 | +0.0019 | [-0.0002, +0.0040] | indistinguishable |
| V1_T_C1 | INDEPENDENT | 0.2438 | +0.0020 | [-0.0002, +0.0041] | indistinguishable |
| OA_SVA_C1 | INDEPENDENT | 0.2436 | +0.0018 | [-0.0004, +0.0039] | indistinguishable |

### total_over_6.5 (n=1194; market Brier 0.2466)

| forecaster | kind | Brier | Δ vs market | 95% games | verdict |
|---|---|---:|---:|---|---|
| V1 | INDEPENDENT | 0.2501 | +0.0035 | [+0.0012, +0.0058] | market better |
| V1_R | INDEPENDENT | 0.2498 | +0.0032 | [+0.0007, +0.0057] | market better |
| V1_R_C1 | INDEPENDENT | 0.2495 | +0.0029 | [+0.0007, +0.0051] | market better |
| V1_T_C1 | INDEPENDENT | 0.2496 | +0.0030 | [+0.0007, +0.0052] | market better |
| OA_SVA_C1 | INDEPENDENT | 0.2494 | +0.0028 | [+0.0006, +0.0050] | market better |

### puck_away_-1.5 (n=1181; market Brier 0.1926)

| forecaster | kind | Brier | Δ vs market | 95% games | verdict |
|---|---|---:|---:|---|---|
| V1 | INDEPENDENT | 0.1939 | +0.0012 | [-0.0014, +0.0038] | indistinguishable |
| V1_R | INDEPENDENT | 0.1934 | +0.0008 | [-0.0014, +0.0030] | indistinguishable |
| V1_R_C1 | INDEPENDENT | 0.1939 | +0.0012 | [-0.0010, +0.0035] | indistinguishable |
| V1_T_C1 | INDEPENDENT | 0.1938 | +0.0012 | [-0.0010, +0.0034] | indistinguishable |
| OA_SVA_C1 | INDEPENDENT | 0.1932 | +0.0005 | [-0.0017, +0.0028] | indistinguishable |

### puck_home_-1.5 (n=1181; market Brier 0.2035)

| forecaster | kind | Brier | Δ vs market | 95% games | verdict |
|---|---|---:|---:|---|---|
| V1 | INDEPENDENT | 0.2050 | +0.0014 | [-0.0011, +0.0039] | indistinguishable |
| V1_R | INDEPENDENT | 0.2045 | +0.0009 | [-0.0013, +0.0031] | indistinguishable |
| V1_R_C1 | INDEPENDENT | 0.2036 | +0.0001 | [-0.0021, +0.0023] | indistinguishable |
| V1_T_C1 | INDEPENDENT | 0.2036 | +0.0000 | [-0.0021, +0.0022] | indistinguishable |
| OA_SVA_C1 | INDEPENDENT | 0.2034 | -0.0001 | [-0.0025, +0.0022] | indistinguishable |


## Tuning grid boundaries (V1_R)

* `half_life`: selected {'2017': 20.0, '2018': 20.0, '2019': 40.0, '2020': 40.0, '2021': 160.0, '2022': 20.0, '2023': 20.0, '2024': 40.0, '2025': 40.0}; at lower edge in []; at upper edge in [2021]
* `prior`: selected {'2017': 10.0, '2018': 10.0, '2019': 20.0, '2020': 5.0, '2021': 20.0, '2022': 10.0, '2023': 10.0, '2024': 5.0, '2025': 10.0}; at lower edge in []; at upper edge in []
* `home_adj`: selected {'2017': 1.045, '2018': 1.06, '2019': 1.045, '2020': 1.045, '2021': 1.045, '2022': 1.045, '2023': 1.03, '2024': 1.03, '2025': 1.045}; at lower edge in []; at upper edge in [2018]
