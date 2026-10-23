# Retuned V1 vs opponent adjustment — preregistered evaluation

8996 games, seasons [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017] · negative Δ = challenger better · 95% intervals: game bootstrap | slate-clustered bootstrap · RESEARCH_ONLY, nothing is promoted

## FRESH2_2010_2016 (n=7725)

| arm | brier_win | logloss_win | brier_ot | rps_total | rps_margin | brier_over_5.5 | brier_over_6.5 | abs_err_total | ECE(win) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 0.2418 | 0.6766 | 0.1831 | 1.2131 | 1.2948 | 0.2445 | 0.2204 | 1.7382 | 0.0154 |
| V1_C1 | 0.2414 | 0.6756 | 0.1832 | 1.2124 | 1.2936 | 0.2446 | 0.2203 | 1.7425 | 0.0093 |
| V1_T | 0.2414 | 0.6757 | 0.1831 | 1.2134 | 1.2932 | 0.2445 | 0.2205 | 1.7361 | 0.0183 |
| V1_T_C1 | 0.2414 | 0.6756 | 0.1832 | 1.2117 | 1.2933 | 0.2442 | 0.2201 | 1.7411 | 0.0131 |
| V1_R | 0.2415 | 0.6759 | 0.1831 | 1.2134 | 1.2937 | 0.2444 | 0.2204 | 1.7363 | 0.0178 |
| V1_R_C1 | 0.2414 | 0.6757 | 0.1833 | 1.2116 | 1.2936 | 0.2442 | 0.2201 | 1.7412 | 0.0105 |
| V1_R_noB2B | 0.2420 | 0.6769 | 0.1830 | 1.2133 | 1.2954 | 0.2445 | 0.2204 | 1.7371 | 0.0160 |
| V1_R_noFIN | 0.2427 | 0.6783 | 0.1832 | 1.2128 | 1.2969 | 0.2445 | 0.2200 | 1.7367 | 0.0140 |
| OA_XG | 0.2416 | 0.6760 | 0.1832 | 1.2137 | 1.2941 | 0.2447 | 0.2204 | 1.7391 | 0.0127 |
| OA_SVA | 0.2414 | 0.6757 | 0.1832 | 1.2139 | 1.2937 | 0.2449 | 0.2207 | 1.7398 | 0.0136 |
| OA_SVA_C1 | 0.2413 | 0.6754 | 0.1832 | 1.2117 | 1.2936 | 0.2444 | 0.2201 | 1.7435 | 0.0110 |
| LEAGUE | 0.2481 | 0.6893 | 0.1832 | 1.2193 | 1.3192 | 0.2465 | 0.2218 | 1.7619 | 0.0030 |

Δ paired vs production V1:

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1_C1 | brier_win | -0.0005 | [-0.0008, -0.0001] | [-0.0008, -0.0001] | better, CI excludes 0 |
| V1_C1 | brier_ot | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0003] | indistinguishable |
| V1_C1 | rps_total | -0.0007 | [-0.0019, +0.0005] | [-0.0020, +0.0005] | indistinguishable |
| V1_C1 | rps_margin | -0.0012 | [-0.0025, +0.0001] | [-0.0024, +0.0001] | indistinguishable |
| V1_T | brier_win | -0.0004 | [-0.0008, -0.0001] | [-0.0008, -0.0001] | better, CI excludes 0 |
| V1_T | brier_ot | -0.0000 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_T | rps_total | +0.0003 | [-0.0009, +0.0014] | [-0.0009, +0.0014] | indistinguishable |
| V1_T | rps_margin | -0.0016 | [-0.0029, -0.0002] | [-0.0029, -0.0003] | better, CI excludes 0 |
| V1_T_C1 | brier_win | -0.0004 | [-0.0009, +0.0000] | [-0.0009, -0.0000] | indistinguishable |
| V1_T_C1 | brier_ot | +0.0000 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| V1_T_C1 | rps_total | -0.0014 | [-0.0029, +0.0001] | [-0.0029, +0.0001] | indistinguishable |
| V1_T_C1 | rps_margin | -0.0014 | [-0.0031, +0.0004] | [-0.0032, +0.0003] | indistinguishable |
| V1_R | brier_win | -0.0003 | [-0.0007, +0.0001] | [-0.0007, +0.0001] | indistinguishable |
| V1_R | brier_ot | -0.0000 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_R | rps_total | +0.0003 | [-0.0008, +0.0014] | [-0.0009, +0.0015] | indistinguishable |
| V1_R | rps_margin | -0.0011 | [-0.0024, +0.0003] | [-0.0024, +0.0002] | indistinguishable |
| V1_R_C1 | brier_win | -0.0004 | [-0.0009, +0.0001] | [-0.0009, +0.0000] | indistinguishable |
| V1_R_C1 | brier_ot | +0.0001 | [-0.0000, +0.0003] | [-0.0000, +0.0003] | indistinguishable |
| V1_R_C1 | rps_total | -0.0014 | [-0.0030, +0.0001] | [-0.0030, +0.0001] | indistinguishable |
| V1_R_C1 | rps_margin | -0.0012 | [-0.0029, +0.0006] | [-0.0029, +0.0005] | indistinguishable |
| V1_R_noB2B | brier_win | +0.0001 | [-0.0003, +0.0006] | [-0.0003, +0.0006] | indistinguishable |
| V1_R_noB2B | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_R_noB2B | rps_total | +0.0002 | [-0.0009, +0.0014] | [-0.0010, +0.0014] | indistinguishable |
| V1_R_noB2B | rps_margin | +0.0006 | [-0.0011, +0.0023] | [-0.0011, +0.0022] | indistinguishable |
| V1_R_noFIN | brier_win | +0.0008 | [+0.0000, +0.0016] | [+0.0000, +0.0016] | worse, CI excludes 0 |
| V1_R_noFIN | brier_ot | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0003] | indistinguishable |
| V1_R_noFIN | rps_total | -0.0003 | [-0.0030, +0.0024] | [-0.0030, +0.0023] | indistinguishable |
| V1_R_noFIN | rps_margin | +0.0021 | [-0.0007, +0.0051] | [-0.0007, +0.0050] | indistinguishable |
| OA_XG | brier_win | -0.0003 | [-0.0007, +0.0001] | [-0.0006, +0.0001] | indistinguishable |
| OA_XG | brier_ot | +0.0001 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| OA_XG | rps_total | +0.0006 | [-0.0010, +0.0021] | [-0.0009, +0.0022] | indistinguishable |
| OA_XG | rps_margin | -0.0007 | [-0.0021, +0.0007] | [-0.0020, +0.0007] | indistinguishable |
| OA_SVA | brier_win | -0.0004 | [-0.0008, -0.0000] | [-0.0008, -0.0000] | better, CI excludes 0 |
| OA_SVA | brier_ot | +0.0000 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| OA_SVA | rps_total | +0.0009 | [-0.0006, +0.0024] | [-0.0005, +0.0024] | indistinguishable |
| OA_SVA | rps_margin | -0.0011 | [-0.0025, +0.0004] | [-0.0025, +0.0003] | indistinguishable |
| OA_SVA_C1 | brier_win | -0.0006 | [-0.0011, -0.0001] | [-0.0010, -0.0001] | better, CI excludes 0 |
| OA_SVA_C1 | brier_ot | +0.0001 | [-0.0000, +0.0003] | [-0.0000, +0.0003] | indistinguishable |
| OA_SVA_C1 | rps_total | -0.0013 | [-0.0029, +0.0003] | [-0.0029, +0.0002] | indistinguishable |
| OA_SVA_C1 | rps_margin | -0.0012 | [-0.0029, +0.0005] | [-0.0028, +0.0005] | indistinguishable |
| LEAGUE | brier_win | +0.0063 | [+0.0050, +0.0075] | [+0.0050, +0.0075] | WORSE (meaningful) |
| LEAGUE | brier_ot | +0.0000 | [-0.0002, +0.0002] | [-0.0002, +0.0002] | indistinguishable |
| LEAGUE | rps_total | +0.0062 | [+0.0025, +0.0099] | [+0.0024, +0.0102] | WORSE (meaningful) |
| LEAGUE | rps_margin | +0.0244 | [+0.0198, +0.0292] | [+0.0197, +0.0289] | WORSE (meaningful) |

Δ paired vs the retuned+recalibrated V1 (`V1_R_C1`):

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1 | brier_win | +0.0004 | [-0.0001, +0.0009] | [-0.0000, +0.0009] | indistinguishable |
| V1 | rps_total | +0.0014 | [-0.0001, +0.0030] | [-0.0001, +0.0030] | indistinguishable |
| V1 | brier_ot | -0.0001 | [-0.0003, +0.0000] | [-0.0003, +0.0000] | indistinguishable |
| V1 | rps_margin | +0.0012 | [-0.0006, +0.0029] | [-0.0005, +0.0029] | indistinguishable |
| V1_C1 | brier_win | -0.0001 | [-0.0005, +0.0004] | [-0.0005, +0.0003] | indistinguishable |
| V1_C1 | rps_total | +0.0007 | [-0.0001, +0.0015] | [-0.0001, +0.0015] | indistinguishable |
| V1_C1 | brier_ot | -0.0000 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_C1 | rps_margin | -0.0000 | [-0.0015, +0.0014] | [-0.0014, +0.0014] | indistinguishable |
| V1_T | brier_win | -0.0000 | [-0.0003, +0.0002] | [-0.0003, +0.0002] | indistinguishable |
| V1_T | rps_total | +0.0017 | [+0.0001, +0.0034] | [+0.0001, +0.0034] | worse, CI excludes 0 |
| V1_T | brier_ot | -0.0002 | [-0.0003, -0.0000] | [-0.0003, -0.0000] | better, CI excludes 0 |
| V1_T | rps_margin | -0.0004 | [-0.0012, +0.0004] | [-0.0012, +0.0004] | indistinguishable |
| V1_T_C1 | brier_win | -0.0000 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_T_C1 | rps_total | +0.0001 | [-0.0003, +0.0004] | [-0.0002, +0.0004] | indistinguishable |
| V1_T_C1 | brier_ot | -0.0001 | [-0.0002, +0.0000] | [-0.0002, +0.0000] | indistinguishable |
| V1_T_C1 | rps_margin | -0.0003 | [-0.0007, +0.0002] | [-0.0007, +0.0002] | indistinguishable |
| V1_R | brier_win | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0003] | indistinguishable |
| V1_R | rps_total | +0.0017 | [+0.0002, +0.0033] | [+0.0002, +0.0033] | worse, CI excludes 0 |
| V1_R | brier_ot | -0.0002 | [-0.0003, -0.0000] | [-0.0004, -0.0000] | better, CI excludes 0 |
| V1_R | rps_margin | +0.0001 | [-0.0007, +0.0009] | [-0.0007, +0.0008] | indistinguishable |
| V1_R_noB2B | brier_win | +0.0006 | [+0.0002, +0.0010] | [+0.0001, +0.0009] | worse, CI excludes 0 |
| V1_R_noB2B | rps_total | +0.0017 | [+0.0001, +0.0032] | [+0.0001, +0.0032] | worse, CI excludes 0 |
| V1_R_noB2B | brier_ot | -0.0002 | [-0.0004, -0.0000] | [-0.0004, -0.0000] | better, CI excludes 0 |
| V1_R_noB2B | rps_margin | +0.0018 | [+0.0003, +0.0032] | [+0.0003, +0.0032] | worse, CI excludes 0 |
| V1_R_noFIN | brier_win | +0.0012 | [+0.0003, +0.0021] | [+0.0003, +0.0021] | WORSE (meaningful) |
| V1_R_noFIN | rps_total | +0.0012 | [-0.0014, +0.0036] | [-0.0011, +0.0035] | indistinguishable |
| V1_R_noFIN | brier_ot | -0.0001 | [-0.0003, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_R_noFIN | rps_margin | +0.0033 | [+0.0001, +0.0067] | [+0.0000, +0.0066] | worse, CI excludes 0 |
| OA_XG | brier_win | +0.0001 | [-0.0003, +0.0006] | [-0.0003, +0.0006] | indistinguishable |
| OA_XG | rps_total | +0.0020 | [-0.0001, +0.0041] | [-0.0000, +0.0041] | indistinguishable |
| OA_XG | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| OA_XG | rps_margin | +0.0005 | [-0.0012, +0.0022] | [-0.0011, +0.0021] | indistinguishable |
| OA_SVA | brier_win | -0.0000 | [-0.0004, +0.0004] | [-0.0005, +0.0004] | indistinguishable |
| OA_SVA | rps_total | +0.0023 | [+0.0003, +0.0043] | [+0.0003, +0.0044] | worse, CI excludes 0 |
| OA_SVA | brier_ot | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| OA_SVA | rps_margin | +0.0001 | [-0.0015, +0.0016] | [-0.0014, +0.0016] | indistinguishable |
| OA_SVA_C1 | brier_win | -0.0002 | [-0.0006, +0.0003] | [-0.0006, +0.0003] | indistinguishable |
| OA_SVA_C1 | rps_total | +0.0001 | [-0.0009, +0.0012] | [-0.0009, +0.0011] | indistinguishable |
| OA_SVA_C1 | brier_ot | -0.0000 | [-0.0002, +0.0002] | [-0.0002, +0.0002] | indistinguishable |
| OA_SVA_C1 | rps_margin | -0.0000 | [-0.0015, +0.0015] | [-0.0015, +0.0015] | indistinguishable |
| LEAGUE | brier_win | +0.0067 | [+0.0051, +0.0081] | [+0.0051, +0.0082] | WORSE (meaningful) |
| LEAGUE | rps_total | +0.0077 | [+0.0048, +0.0105] | [+0.0048, +0.0106] | WORSE (meaningful) |
| LEAGUE | brier_ot | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| LEAGUE | rps_margin | +0.0256 | [+0.0198, +0.0314] | [+0.0198, +0.0310] | WORSE (meaningful) |

## FRESH2_3V3_2015_2016 (n=2460)

| arm | brier_win | logloss_win | brier_ot | rps_total | rps_margin | brier_over_5.5 | brier_over_6.5 | abs_err_total | ECE(win) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 0.2427 | 0.6783 | 0.1784 | 1.2029 | 1.2958 | 0.2445 | 0.2174 | 1.7254 | 0.0120 |
| V1_C1 | 0.2423 | 0.6777 | 0.1785 | 1.2014 | 1.2953 | 0.2443 | 0.2170 | 1.7263 | 0.0068 |
| V1_T | 0.2417 | 0.6764 | 0.1784 | 1.2020 | 1.2929 | 0.2441 | 0.2169 | 1.7196 | 0.0063 |
| V1_T_C1 | 0.2420 | 0.6769 | 0.1784 | 1.2001 | 1.2936 | 0.2438 | 0.2166 | 1.7223 | 0.0059 |
| V1_R | 0.2417 | 0.6764 | 0.1784 | 1.2020 | 1.2929 | 0.2441 | 0.2169 | 1.7196 | 0.0063 |
| V1_R_C1 | 0.2419 | 0.6767 | 0.1786 | 1.1997 | 1.2935 | 0.2437 | 0.2164 | 1.7220 | 0.0056 |
| V1_R_noB2B | 0.2421 | 0.6772 | 0.1784 | 1.2022 | 1.2939 | 0.2442 | 0.2169 | 1.7208 | 0.0087 |
| V1_R_noFIN | 0.2429 | 0.6787 | 0.1785 | 1.1993 | 1.2949 | 0.2439 | 0.2165 | 1.7188 | 0.0210 |
| OA_XG | 0.2422 | 0.6773 | 0.1784 | 1.2053 | 1.2937 | 0.2451 | 0.2179 | 1.7250 | 0.0067 |
| OA_SVA | 0.2422 | 0.6773 | 0.1784 | 1.2057 | 1.2938 | 0.2454 | 0.2180 | 1.7255 | 0.0051 |
| OA_SVA_C1 | 0.2420 | 0.6770 | 0.1783 | 1.2018 | 1.2940 | 0.2443 | 0.2171 | 1.7259 | 0.0104 |
| LEAGUE | 0.2479 | 0.6889 | 0.1784 | 1.2075 | 1.3170 | 0.2460 | 0.2187 | 1.7419 | 0.0039 |

Δ paired vs production V1:

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1_C1 | brier_win | -0.0003 | [-0.0010, +0.0003] | [-0.0010, +0.0003] | indistinguishable |
| V1_C1 | brier_ot | +0.0001 | [-0.0002, +0.0004] | [-0.0002, +0.0004] | indistinguishable |
| V1_C1 | rps_total | -0.0015 | [-0.0035, +0.0005] | [-0.0037, +0.0005] | indistinguishable |
| V1_C1 | rps_margin | -0.0005 | [-0.0029, +0.0019] | [-0.0028, +0.0018] | indistinguishable |
| V1_T | brier_win | -0.0009 | [-0.0016, -0.0002] | [-0.0016, -0.0003] | better, CI excludes 0 |
| V1_T | brier_ot | -0.0001 | [-0.0003, +0.0002] | [-0.0003, +0.0002] | indistinguishable |
| V1_T | rps_total | -0.0009 | [-0.0029, +0.0012] | [-0.0032, +0.0013] | indistinguishable |
| V1_T | rps_margin | -0.0029 | [-0.0053, -0.0005] | [-0.0052, -0.0006] | better, CI excludes 0 |
| V1_T_C1 | brier_win | -0.0007 | [-0.0016, +0.0003] | [-0.0016, +0.0002] | indistinguishable |
| V1_T_C1 | brier_ot | -0.0000 | [-0.0003, +0.0003] | [-0.0003, +0.0003] | indistinguishable |
| V1_T_C1 | rps_total | -0.0028 | [-0.0054, -0.0001] | [-0.0055, -0.0002] | better, CI excludes 0 |
| V1_T_C1 | rps_margin | -0.0022 | [-0.0057, +0.0013] | [-0.0055, +0.0011] | indistinguishable |
| V1_R | brier_win | -0.0009 | [-0.0016, -0.0002] | [-0.0016, -0.0003] | better, CI excludes 0 |
| V1_R | brier_ot | -0.0001 | [-0.0003, +0.0002] | [-0.0003, +0.0002] | indistinguishable |
| V1_R | rps_total | -0.0009 | [-0.0029, +0.0012] | [-0.0032, +0.0013] | indistinguishable |
| V1_R | rps_margin | -0.0029 | [-0.0053, -0.0005] | [-0.0052, -0.0006] | better, CI excludes 0 |
| V1_R_C1 | brier_win | -0.0008 | [-0.0018, +0.0002] | [-0.0017, +0.0001] | indistinguishable |
| V1_R_C1 | brier_ot | +0.0001 | [-0.0002, +0.0004] | [-0.0002, +0.0004] | indistinguishable |
| V1_R_C1 | rps_total | -0.0032 | [-0.0058, -0.0006] | [-0.0058, -0.0006] | better, CI excludes 0 |
| V1_R_C1 | rps_margin | -0.0023 | [-0.0060, +0.0011] | [-0.0056, +0.0010] | indistinguishable |
| V1_R_noB2B | brier_win | -0.0005 | [-0.0014, +0.0004] | [-0.0013, +0.0002] | indistinguishable |
| V1_R_noB2B | brier_ot | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0002] | indistinguishable |
| V1_R_noB2B | rps_total | -0.0007 | [-0.0027, +0.0014] | [-0.0030, +0.0016] | indistinguishable |
| V1_R_noB2B | rps_margin | -0.0019 | [-0.0049, +0.0012] | [-0.0047, +0.0008] | indistinguishable |
| V1_R_noFIN | brier_win | +0.0002 | [-0.0012, +0.0016] | [-0.0012, +0.0016] | indistinguishable |
| V1_R_noFIN | brier_ot | +0.0001 | [-0.0003, +0.0004] | [-0.0002, +0.0004] | indistinguishable |
| V1_R_noFIN | rps_total | -0.0036 | [-0.0086, +0.0014] | [-0.0085, +0.0012] | indistinguishable |
| V1_R_noFIN | rps_margin | -0.0008 | [-0.0059, +0.0043] | [-0.0059, +0.0042] | indistinguishable |
| OA_XG | brier_win | -0.0005 | [-0.0013, +0.0003] | [-0.0013, +0.0003] | indistinguishable |
| OA_XG | brier_ot | -0.0000 | [-0.0003, +0.0003] | [-0.0003, +0.0003] | indistinguishable |
| OA_XG | rps_total | +0.0024 | [-0.0005, +0.0053] | [-0.0003, +0.0051] | indistinguishable |
| OA_XG | rps_margin | -0.0021 | [-0.0050, +0.0006] | [-0.0046, +0.0005] | indistinguishable |
| OA_SVA | brier_win | -0.0005 | [-0.0013, +0.0003] | [-0.0012, +0.0003] | indistinguishable |
| OA_SVA | brier_ot | -0.0000 | [-0.0003, +0.0003] | [-0.0003, +0.0002] | indistinguishable |
| OA_SVA | rps_total | +0.0028 | [+0.0001, +0.0057] | [+0.0002, +0.0054] | worse, CI excludes 0 |
| OA_SVA | rps_margin | -0.0020 | [-0.0048, +0.0008] | [-0.0045, +0.0007] | indistinguishable |
| OA_SVA_C1 | brier_win | -0.0006 | [-0.0016, +0.0003] | [-0.0016, +0.0003] | indistinguishable |
| OA_SVA_C1 | brier_ot | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0002] | indistinguishable |
| OA_SVA_C1 | rps_total | -0.0011 | [-0.0035, +0.0014] | [-0.0037, +0.0014] | indistinguishable |
| OA_SVA_C1 | rps_margin | -0.0018 | [-0.0054, +0.0016] | [-0.0051, +0.0017] | indistinguishable |
| LEAGUE | brier_win | +0.0052 | [+0.0031, +0.0074] | [+0.0031, +0.0073] | WORSE (meaningful) |
| LEAGUE | brier_ot | +0.0000 | [-0.0003, +0.0004] | [-0.0003, +0.0004] | indistinguishable |
| LEAGUE | rps_total | +0.0046 | [-0.0014, +0.0106] | [-0.0021, +0.0112] | indistinguishable |
| LEAGUE | rps_margin | +0.0212 | [+0.0132, +0.0294] | [+0.0132, +0.0287] | WORSE (meaningful) |

Δ paired vs the retuned+recalibrated V1 (`V1_R_C1`):

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1 | brier_win | +0.0008 | [-0.0002, +0.0018] | [-0.0001, +0.0017] | indistinguishable |
| V1 | rps_total | +0.0032 | [+0.0006, +0.0058] | [+0.0006, +0.0058] | worse, CI excludes 0 |
| V1 | brier_ot | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0002] | indistinguishable |
| V1 | rps_margin | +0.0023 | [-0.0011, +0.0060] | [-0.0010, +0.0056] | indistinguishable |
| V1_C1 | brier_win | +0.0005 | [-0.0003, +0.0012] | [-0.0002, +0.0012] | indistinguishable |
| V1_C1 | rps_total | +0.0017 | [+0.0003, +0.0031] | [+0.0002, +0.0032] | worse, CI excludes 0 |
| V1_C1 | brier_ot | -0.0000 | [-0.0003, +0.0003] | [-0.0003, +0.0002] | indistinguishable |
| V1_C1 | rps_margin | +0.0018 | [-0.0007, +0.0043] | [-0.0006, +0.0043] | indistinguishable |
| V1_T | brier_win | -0.0001 | [-0.0006, +0.0004] | [-0.0006, +0.0003] | indistinguishable |
| V1_T | rps_total | +0.0023 | [-0.0001, +0.0048] | [-0.0002, +0.0050] | indistinguishable |
| V1_T | brier_ot | -0.0002 | [-0.0005, +0.0001] | [-0.0005, +0.0001] | indistinguishable |
| V1_T | rps_margin | -0.0006 | [-0.0023, +0.0011] | [-0.0022, +0.0010] | indistinguishable |
| V1_T_C1 | brier_win | +0.0001 | [-0.0001, +0.0004] | [-0.0001, +0.0004] | indistinguishable |
| V1_T_C1 | rps_total | +0.0004 | [-0.0001, +0.0009] | [-0.0001, +0.0009] | indistinguishable |
| V1_T_C1 | brier_ot | -0.0002 | [-0.0004, +0.0001] | [-0.0004, +0.0001] | indistinguishable |
| V1_T_C1 | rps_margin | +0.0002 | [-0.0004, +0.0008] | [-0.0004, +0.0008] | indistinguishable |
| V1_R | brier_win | -0.0001 | [-0.0006, +0.0004] | [-0.0006, +0.0003] | indistinguishable |
| V1_R | rps_total | +0.0023 | [-0.0001, +0.0048] | [-0.0002, +0.0050] | indistinguishable |
| V1_R | brier_ot | -0.0002 | [-0.0005, +0.0001] | [-0.0005, +0.0001] | indistinguishable |
| V1_R | rps_margin | -0.0006 | [-0.0023, +0.0011] | [-0.0022, +0.0010] | indistinguishable |
| V1_R_noB2B | brier_win | +0.0003 | [-0.0005, +0.0010] | [-0.0005, +0.0010] | indistinguishable |
| V1_R_noB2B | rps_total | +0.0025 | [-0.0000, +0.0050] | [-0.0001, +0.0052] | indistinguishable |
| V1_R_noB2B | brier_ot | -0.0002 | [-0.0005, +0.0001] | [-0.0005, +0.0001] | indistinguishable |
| V1_R_noB2B | rps_margin | +0.0004 | [-0.0023, +0.0031] | [-0.0023, +0.0032] | indistinguishable |
| V1_R_noFIN | brier_win | +0.0010 | [-0.0007, +0.0026] | [-0.0007, +0.0026] | indistinguishable |
| V1_R_noFIN | rps_total | -0.0004 | [-0.0047, +0.0041] | [-0.0046, +0.0038] | indistinguishable |
| V1_R_noFIN | brier_ot | -0.0000 | [-0.0004, +0.0003] | [-0.0004, +0.0003] | indistinguishable |
| V1_R_noFIN | rps_margin | +0.0015 | [-0.0045, +0.0077] | [-0.0047, +0.0076] | indistinguishable |
| OA_XG | brier_win | +0.0003 | [-0.0005, +0.0010] | [-0.0005, +0.0010] | indistinguishable |
| OA_XG | rps_total | +0.0056 | [+0.0017, +0.0097] | [+0.0018, +0.0093] | WORSE (meaningful) |
| OA_XG | brier_ot | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0002] | indistinguishable |
| OA_XG | rps_margin | +0.0002 | [-0.0026, +0.0030] | [-0.0024, +0.0029] | indistinguishable |
| OA_SVA | brier_win | +0.0003 | [-0.0004, +0.0010] | [-0.0004, +0.0010] | indistinguishable |
| OA_SVA | rps_total | +0.0060 | [+0.0021, +0.0101] | [+0.0022, +0.0098] | WORSE (meaningful) |
| OA_SVA | brier_ot | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0001] | indistinguishable |
| OA_SVA | rps_margin | +0.0003 | [-0.0023, +0.0029] | [-0.0022, +0.0030] | indistinguishable |
| OA_SVA_C1 | brier_win | +0.0001 | [-0.0005, +0.0008] | [-0.0005, +0.0009] | indistinguishable |
| OA_SVA_C1 | rps_total | +0.0021 | [+0.0003, +0.0040] | [+0.0005, +0.0037] | worse, CI excludes 0 |
| OA_SVA_C1 | brier_ot | -0.0002 | [-0.0005, +0.0000] | [-0.0005, +0.0000] | indistinguishable |
| OA_SVA_C1 | rps_margin | +0.0005 | [-0.0020, +0.0028] | [-0.0019, +0.0030] | indistinguishable |
| LEAGUE | brier_win | +0.0060 | [+0.0032, +0.0090] | [+0.0033, +0.0088] | WORSE (meaningful) |
| LEAGUE | rps_total | +0.0078 | [+0.0025, +0.0132] | [+0.0022, +0.0134] | WORSE (meaningful) |
| LEAGUE | brier_ot | -0.0001 | [-0.0005, +0.0003] | [-0.0005, +0.0003] | indistinguishable |
| LEAGUE | rps_margin | +0.0235 | [+0.0130, +0.0343] | [+0.0128, +0.0336] | WORSE (meaningful) |

## FRESH_ALL_2010_2017 (n=8996)

| arm | brier_win | logloss_win | brier_ot | rps_total | rps_margin | brier_over_5.5 | brier_over_6.5 | abs_err_total | ECE(win) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 0.2417 | 0.6762 | 0.1829 | 1.2261 | 1.3059 | 0.2453 | 0.2236 | 1.7600 | 0.0183 |
| V1_C1 | 0.2413 | 0.6754 | 0.1830 | 1.2252 | 1.3048 | 0.2454 | 0.2236 | 1.7637 | 0.0111 |
| V1_T | 0.2412 | 0.6752 | 0.1829 | 1.2266 | 1.3043 | 0.2454 | 0.2237 | 1.7584 | 0.0145 |
| V1_T_C1 | 0.2412 | 0.6753 | 0.1829 | 1.2248 | 1.3045 | 0.2451 | 0.2235 | 1.7627 | 0.0115 |
| V1_R | 0.2413 | 0.6755 | 0.1829 | 1.2266 | 1.3048 | 0.2454 | 0.2237 | 1.7585 | 0.0141 |
| V1_R_C1 | 0.2413 | 0.6754 | 0.1830 | 1.2247 | 1.3047 | 0.2451 | 0.2235 | 1.7629 | 0.0089 |
| V1_R_noB2B | 0.2418 | 0.6765 | 0.1828 | 1.2265 | 1.3064 | 0.2454 | 0.2237 | 1.7593 | 0.0118 |
| V1_R_noFIN | 0.2424 | 0.6779 | 0.1829 | 1.2263 | 1.3081 | 0.2456 | 0.2236 | 1.7602 | 0.0109 |
| OA_XG | 0.2414 | 0.6757 | 0.1830 | 1.2265 | 1.3054 | 0.2454 | 0.2236 | 1.7606 | 0.0134 |
| OA_SVA | 0.2413 | 0.6754 | 0.1830 | 1.2267 | 1.3049 | 0.2455 | 0.2238 | 1.7611 | 0.0121 |
| OA_SVA_C1 | 0.2412 | 0.6752 | 0.1830 | 1.2247 | 1.3049 | 0.2452 | 0.2234 | 1.7647 | 0.0110 |
| LEAGUE | 0.2479 | 0.6889 | 0.1829 | 1.2314 | 1.3296 | 0.2470 | 0.2249 | 1.7812 | 0.0056 |

Δ paired vs production V1:

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1_C1 | brier_win | -0.0004 | [-0.0007, -0.0001] | [-0.0007, -0.0001] | better, CI excludes 0 |
| V1_C1 | brier_ot | +0.0001 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| V1_C1 | rps_total | -0.0009 | [-0.0021, +0.0005] | [-0.0021, +0.0004] | indistinguishable |
| V1_C1 | rps_margin | -0.0011 | [-0.0022, -0.0000] | [-0.0022, -0.0001] | better, CI excludes 0 |
| V1_T | brier_win | -0.0005 | [-0.0008, -0.0001] | [-0.0008, -0.0001] | better, CI excludes 0 |
| V1_T | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_T | rps_total | +0.0005 | [-0.0005, +0.0016] | [-0.0006, +0.0015] | indistinguishable |
| V1_T | rps_margin | -0.0016 | [-0.0028, -0.0004] | [-0.0028, -0.0004] | better, CI excludes 0 |
| V1_T_C1 | brier_win | -0.0004 | [-0.0008, -0.0000] | [-0.0008, -0.0000] | better, CI excludes 0 |
| V1_T_C1 | brier_ot | -0.0000 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_T_C1 | rps_total | -0.0013 | [-0.0028, +0.0002] | [-0.0027, +0.0002] | indistinguishable |
| V1_T_C1 | rps_margin | -0.0014 | [-0.0029, +0.0001] | [-0.0028, -0.0000] | indistinguishable |
| V1_R | brier_win | -0.0003 | [-0.0007, -0.0000] | [-0.0007, -0.0000] | better, CI excludes 0 |
| V1_R | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_R | rps_total | +0.0005 | [-0.0005, +0.0015] | [-0.0006, +0.0016] | indistinguishable |
| V1_R | rps_margin | -0.0012 | [-0.0024, +0.0000] | [-0.0024, -0.0000] | indistinguishable |
| V1_R_C1 | brier_win | -0.0004 | [-0.0008, +0.0000] | [-0.0008, +0.0000] | indistinguishable |
| V1_R_C1 | brier_ot | +0.0001 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| V1_R_C1 | rps_total | -0.0013 | [-0.0029, +0.0002] | [-0.0029, +0.0002] | indistinguishable |
| V1_R_C1 | rps_margin | -0.0012 | [-0.0027, +0.0004] | [-0.0026, +0.0003] | indistinguishable |
| V1_R_noB2B | brier_win | +0.0001 | [-0.0003, +0.0006] | [-0.0003, +0.0006] | indistinguishable |
| V1_R_noB2B | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_R_noB2B | rps_total | +0.0005 | [-0.0006, +0.0015] | [-0.0006, +0.0015] | indistinguishable |
| V1_R_noB2B | rps_margin | +0.0005 | [-0.0010, +0.0020] | [-0.0010, +0.0020] | indistinguishable |
| V1_R_noFIN | brier_win | +0.0008 | [+0.0000, +0.0015] | [+0.0001, +0.0015] | worse, CI excludes 0 |
| V1_R_noFIN | brier_ot | +0.0000 | [-0.0002, +0.0002] | [-0.0002, +0.0002] | indistinguishable |
| V1_R_noFIN | rps_total | +0.0003 | [-0.0023, +0.0028] | [-0.0023, +0.0028] | indistinguishable |
| V1_R_noFIN | rps_margin | +0.0022 | [-0.0006, +0.0048] | [-0.0006, +0.0048] | indistinguishable |
| OA_XG | brier_win | -0.0002 | [-0.0006, +0.0001] | [-0.0006, +0.0001] | indistinguishable |
| OA_XG | brier_ot | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0003] | indistinguishable |
| OA_XG | rps_total | +0.0004 | [-0.0010, +0.0019] | [-0.0009, +0.0019] | indistinguishable |
| OA_XG | rps_margin | -0.0006 | [-0.0018, +0.0007] | [-0.0018, +0.0006] | indistinguishable |
| OA_SVA | brier_win | -0.0004 | [-0.0007, -0.0000] | [-0.0008, -0.0001] | better, CI excludes 0 |
| OA_SVA | brier_ot | +0.0001 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| OA_SVA | rps_total | +0.0006 | [-0.0008, +0.0020] | [-0.0007, +0.0020] | indistinguishable |
| OA_SVA | rps_margin | -0.0011 | [-0.0024, +0.0002] | [-0.0023, +0.0002] | indistinguishable |
| OA_SVA_C1 | brier_win | -0.0005 | [-0.0009, -0.0000] | [-0.0009, -0.0001] | better, CI excludes 0 |
| OA_SVA_C1 | brier_ot | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0002] | indistinguishable |
| OA_SVA_C1 | rps_total | -0.0014 | [-0.0031, +0.0003] | [-0.0030, +0.0003] | indistinguishable |
| OA_SVA_C1 | rps_margin | -0.0011 | [-0.0026, +0.0005] | [-0.0025, +0.0005] | indistinguishable |
| LEAGUE | brier_win | +0.0062 | [+0.0051, +0.0074] | [+0.0051, +0.0073] | WORSE (meaningful) |
| LEAGUE | brier_ot | +0.0000 | [-0.0002, +0.0002] | [-0.0002, +0.0002] | indistinguishable |
| LEAGUE | rps_total | +0.0053 | [+0.0021, +0.0087] | [+0.0019, +0.0088] | WORSE (meaningful) |
| LEAGUE | rps_margin | +0.0237 | [+0.0193, +0.0280] | [+0.0195, +0.0279] | WORSE (meaningful) |

Δ paired vs the retuned+recalibrated V1 (`V1_R_C1`):

| challenger | metric | Δ | 95% games | 95% slates | verdict |
|---|---|---:|---|---|---|
| V1 | brier_win | +0.0004 | [-0.0000, +0.0008] | [-0.0000, +0.0008] | indistinguishable |
| V1 | rps_total | +0.0013 | [-0.0002, +0.0029] | [-0.0002, +0.0029] | indistinguishable |
| V1 | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1 | rps_margin | +0.0012 | [-0.0004, +0.0027] | [-0.0003, +0.0026] | indistinguishable |
| V1_C1 | brier_win | -0.0000 | [-0.0004, +0.0004] | [-0.0004, +0.0003] | indistinguishable |
| V1_C1 | rps_total | +0.0005 | [-0.0003, +0.0012] | [-0.0003, +0.0012] | indistinguishable |
| V1_C1 | brier_ot | +0.0000 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| V1_C1 | rps_margin | +0.0001 | [-0.0012, +0.0014] | [-0.0011, +0.0014] | indistinguishable |
| V1_T | brier_win | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| V1_T | rps_total | +0.0019 | [+0.0002, +0.0035] | [+0.0002, +0.0035] | worse, CI excludes 0 |
| V1_T | brier_ot | -0.0001 | [-0.0003, +0.0000] | [-0.0003, +0.0000] | indistinguishable |
| V1_T | rps_margin | -0.0004 | [-0.0012, +0.0004] | [-0.0011, +0.0003] | indistinguishable |
| V1_T_C1 | brier_win | -0.0000 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_T_C1 | rps_total | +0.0001 | [-0.0002, +0.0003] | [-0.0002, +0.0003] | indistinguishable |
| V1_T_C1 | brier_ot | -0.0001 | [-0.0002, +0.0000] | [-0.0002, +0.0000] | indistinguishable |
| V1_T_C1 | rps_margin | -0.0002 | [-0.0006, +0.0002] | [-0.0006, +0.0002] | indistinguishable |
| V1_R | brier_win | +0.0000 | [-0.0002, +0.0003] | [-0.0002, +0.0003] | indistinguishable |
| V1_R | rps_total | +0.0019 | [+0.0003, +0.0034] | [+0.0003, +0.0035] | worse, CI excludes 0 |
| V1_R | brier_ot | -0.0001 | [-0.0003, +0.0000] | [-0.0003, +0.0000] | indistinguishable |
| V1_R | rps_margin | +0.0000 | [-0.0008, +0.0007] | [-0.0007, +0.0007] | indistinguishable |
| V1_R_noB2B | brier_win | +0.0005 | [+0.0002, +0.0009] | [+0.0002, +0.0009] | worse, CI excludes 0 |
| V1_R_noB2B | rps_total | +0.0018 | [+0.0002, +0.0033] | [+0.0002, +0.0034] | worse, CI excludes 0 |
| V1_R_noB2B | brier_ot | -0.0002 | [-0.0003, -0.0000] | [-0.0003, +0.0000] | indistinguishable |
| V1_R_noB2B | rps_margin | +0.0017 | [+0.0004, +0.0030] | [+0.0003, +0.0031] | worse, CI excludes 0 |
| V1_R_noFIN | brier_win | +0.0012 | [+0.0004, +0.0020] | [+0.0004, +0.0020] | WORSE (meaningful) |
| V1_R_noFIN | rps_total | +0.0016 | [-0.0007, +0.0039] | [-0.0008, +0.0040] | indistinguishable |
| V1_R_noFIN | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| V1_R_noFIN | rps_margin | +0.0033 | [+0.0003, +0.0062] | [+0.0004, +0.0062] | worse, CI excludes 0 |
| OA_XG | brier_win | +0.0002 | [-0.0003, +0.0006] | [-0.0003, +0.0006] | indistinguishable |
| OA_XG | rps_total | +0.0018 | [-0.0004, +0.0039] | [-0.0004, +0.0038] | indistinguishable |
| OA_XG | brier_ot | +0.0000 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| OA_XG | rps_margin | +0.0006 | [-0.0009, +0.0022] | [-0.0009, +0.0021] | indistinguishable |
| OA_SVA | brier_win | -0.0000 | [-0.0004, +0.0004] | [-0.0004, +0.0004] | indistinguishable |
| OA_SVA | rps_total | +0.0019 | [-0.0002, +0.0040] | [-0.0001, +0.0040] | indistinguishable |
| OA_SVA | brier_ot | -0.0000 | [-0.0002, +0.0001] | [-0.0002, +0.0001] | indistinguishable |
| OA_SVA | rps_margin | +0.0001 | [-0.0013, +0.0016] | [-0.0013, +0.0015] | indistinguishable |
| OA_SVA_C1 | brier_win | -0.0001 | [-0.0005, +0.0003] | [-0.0005, +0.0003] | indistinguishable |
| OA_SVA_C1 | rps_total | -0.0000 | [-0.0013, +0.0013] | [-0.0014, +0.0012] | indistinguishable |
| OA_SVA_C1 | brier_ot | +0.0000 | [-0.0001, +0.0002] | [-0.0001, +0.0002] | indistinguishable |
| OA_SVA_C1 | rps_margin | +0.0001 | [-0.0013, +0.0016] | [-0.0012, +0.0016] | indistinguishable |
| LEAGUE | brier_win | +0.0066 | [+0.0052, +0.0081] | [+0.0052, +0.0080] | WORSE (meaningful) |
| LEAGUE | rps_total | +0.0067 | [+0.0041, +0.0094] | [+0.0040, +0.0094] | WORSE (meaningful) |
| LEAGUE | brier_ot | -0.0001 | [-0.0002, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| LEAGUE | rps_margin | +0.0248 | [+0.0195, +0.0301] | [+0.0198, +0.0299] | WORSE (meaningful) |

## Per season: Δ Brier(win) vs V1 (negative = better)

| season | n | V1_C1 | V1_T | V1_T_C1 | V1_R | V1_R_C1 | V1_R_noB2B | V1_R_noFIN | OA_XG | OA_SVA | OA_SVA_C1 | LEAGUE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2010 | 1067 | +0.0000 | +0.0004 | +0.0006 | +0.0004 | +0.0006 | +0.0004 | +0.0008 | +0.0000 | -0.0005 | -0.0002 | +0.0049 |
| 2011 | 1148 | -0.0001 | -0.0002 | -0.0002 | -0.0002 | -0.0002 | +0.0008 | -0.0006 | -0.0004 | -0.0003 | -0.0001 | +0.0051 |
| 2012 | 672 | -0.0005 | -0.0006 | -0.0006 | -0.0006 | -0.0006 | -0.0002 | +0.0012 | -0.0008 | -0.0012 | -0.0012 | +0.0056 |
| 2013 | 1148 | -0.0005 | -0.0008 | -0.0008 | +0.0001 | +0.0000 | +0.0001 | +0.0019 | +0.0001 | -0.0001 | -0.0005 | +0.0073 |
| 2014 | 1230 | -0.0015 | +0.0000 | -0.0006 | +0.0000 | -0.0009 | +0.0010 | +0.0022 | +0.0000 | -0.0002 | -0.0009 | +0.0100 |
| 2015 | 1230 | -0.0003 | -0.0005 | -0.0002 | -0.0005 | -0.0003 | +0.0002 | -0.0003 | -0.0004 | -0.0002 | -0.0002 | +0.0039 |
| 2016 | 1230 | -0.0003 | -0.0013 | -0.0011 | -0.0013 | -0.0013 | -0.0012 | +0.0007 | -0.0006 | -0.0007 | -0.0011 | +0.0066 |
| 2017 | 1271 | +0.0001 | -0.0006 | -0.0003 | -0.0006 | -0.0003 | +0.0001 | +0.0007 | -0.0000 | -0.0002 | +0.0002 | +0.0060 |

## Preregistered decision rules

**R1_retune_vs_V1** — `V1_R` vs `V1`: **NOT BETTER** (gate CIs fail; size ≥ threshold fail; favourable seasons 4/7; no primary metric worse ok)

| metric | Δ | 95% games | 95% slates |
|---|---:|---|---|
| brier_win | -0.0003 | [-0.0007, +0.0001] | [-0.0007, +0.0001] |
| rps_total | +0.0003 | [-0.0008, +0.0014] | [-0.0009, +0.0015] |
| brier_ot | -0.0000 | [-0.0002, +0.0001] | [-0.0002, +0.0001] |

**R2_recalibration_on_retuned** — `V1_R_C1` vs `V1_R`: **NOT BETTER** (gate CIs fail; size ≥ threshold fail; favourable seasons 3/7; no primary metric worse FAIL)

| metric | Δ | 95% games | 95% slates |
|---|---:|---|---|
| brier_win | -0.0001 | [-0.0003, +0.0001] | [-0.0003, +0.0001] |
| rps_total | -0.0017 | [-0.0033, -0.0002] | [-0.0033, -0.0002] |
| brier_ot | +0.0002 | [+0.0000, +0.0003] | [+0.0000, +0.0004] |

**R3_opponent_adjustment_incremental** — `OA_SVA_C1` vs `V1_R_C1`: **NOT BETTER** (gate CIs fail; size ≥ threshold fail; favourable seasons 3/7; no primary metric worse ok)

| metric | Δ | 95% games | 95% slates |
|---|---:|---|---|
| brier_win | -0.0002 | [-0.0006, +0.0003] | [-0.0006, +0.0003] |
| rps_total | +0.0001 | [-0.0009, +0.0012] | [-0.0009, +0.0011] |
| brier_ot | -0.0000 | [-0.0002, +0.0002] | [-0.0002, +0.0002] |

**R4_leading_candidate**: leads = `V1`; within the practical threshold of the best: ['V1', 'V1_R', 'V1_T', 'V1_R_C1', 'V1_T_C1', 'V1_C1', 'OA_SVA', 'OA_XG', 'OA_SVA_C1']; simplest of those: ['V1'] · 'leads' ranks historical evidence only; it is not a promotion

## Feature ablations (R5; ablation minus `V1_R`, positive = the feature helps)

| ablation | feature | metric | Δ | 95% games | 95% slates | informative |
|---|---|---|---:|---|---|---|
| V1_R_noB2B | back-to-back adjustment | brier_win | +0.0004 | [+0.0001, +0.0008] | [+0.0001, +0.0008] | yes |
| V1_R_noB2B | back-to-back adjustment | rps_total | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0002] | yes |
| V1_R_noB2B | back-to-back adjustment | brier_ot | -0.0000 | [-0.0001, +0.0001] | [-0.0001, +0.0001] | yes |
| V1_R_noFIN | finishing ratio | brier_win | +0.0011 | [+0.0003, +0.0019] | [+0.0004, +0.0019] | yes |
| V1_R_noFIN | finishing ratio | rps_total | -0.0006 | [-0.0032, +0.0019] | [-0.0033, +0.0019] | yes |
| V1_R_noFIN | finishing ratio | brier_ot | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0003] | yes |

## Tuning grid boundaries (V1_R)

* `half_life`: selected {'2010': 40.0, '2011': 20.0, '2012': 40.0, '2013': 160.0, '2014': 20.0, '2015': 40.0, '2016': 40.0}; at lower edge in []; at upper edge in [2013]
* `prior`: selected {'2010': 20.0, '2011': 10.0, '2012': 20.0, '2013': 40.0, '2014': 20.0, '2015': 20.0, '2016': 10.0}; at lower edge in []; at upper edge in []
* `home_adj`: selected {'2010': 1.06, '2011': 1.045, '2012': 1.045, '2013': 1.06, '2014': 1.045, '2015': 1.045, '2016': 1.045}; at lower edge in []; at upper edge in [2010, 2013]
