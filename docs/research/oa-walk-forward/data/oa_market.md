# Independent models vs Kalshi mid at matched timestamp

horizon T-60m · seasons [2025] · Kalshi candle-close midpoint; no depth, fee or slippage. A midpoint advantage is not an execution edge.

## home_win (n=1312; market Brier 0.2442)

| forecaster | kind | Brier | Δ vs market | 95% CI games | 95% CI slates | verdict |
|---|---|---:|---:|---|---|---|
| V1 | INDEPENDENT | 0.2459 | +0.0017 | [-0.0014, +0.0047] | [-0.0014, +0.0048] | indistinguishable |
| V1+mkt(w=0.8) | MARKET-INFORMED | 0.2440 | -0.0002 | [-0.0008, +0.0004] | [-0.0008, +0.0004] | indistinguishable |
| V1+mkt(w=0.9) | MARKET-INFORMED | 0.2441 | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0002] | indistinguishable |
| V1_C1 | INDEPENDENT | 0.2464 | +0.0022 | [-0.0007, +0.0051] | [-0.0008, +0.0052] | indistinguishable |
| V1_C1+mkt(w=0.8) | MARKET-INFORMED | 0.2441 | -0.0000 | [-0.0006, +0.0005] | [-0.0007, +0.0006] | indistinguishable |
| V1_C1+mkt(w=0.9) | MARKET-INFORMED | 0.2441 | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0002] | indistinguishable |
| OA_XG | INDEPENDENT | 0.2446 | +0.0004 | [-0.0024, +0.0031] | [-0.0025, +0.0032] | indistinguishable |
| OA_XG+mkt(w=0.8) | MARKET-INFORMED | 0.2438 | -0.0004 | [-0.0009, +0.0002] | [-0.0009, +0.0002] | indistinguishable |
| OA_XG+mkt(w=0.9) | MARKET-INFORMED | 0.2440 | -0.0002 | [-0.0005, +0.0001] | [-0.0005, +0.0001] | indistinguishable |
| OA_SVA | INDEPENDENT | 0.2448 | +0.0006 | [-0.0021, +0.0032] | [-0.0022, +0.0033] | indistinguishable |
| OA_SVA+mkt(w=0.8) | MARKET-INFORMED | 0.2439 | -0.0003 | [-0.0008, +0.0002] | [-0.0008, +0.0002] | indistinguishable |
| OA_SVA+mkt(w=0.9) | MARKET-INFORMED | 0.2440 | -0.0002 | [-0.0004, +0.0001] | [-0.0004, +0.0001] | indistinguishable |
| OA_SVA_C1 | INDEPENDENT | 0.2452 | +0.0010 | [-0.0018, +0.0036] | [-0.0017, +0.0036] | indistinguishable |
| OA_SVA_C1+mkt(w=0.8) | MARKET-INFORMED | 0.2440 | -0.0002 | [-0.0008, +0.0003] | [-0.0008, +0.0003] | indistinguishable |
| OA_SVA_C1+mkt(w=0.9) | MARKET-INFORMED | 0.2441 | -0.0001 | [-0.0004, +0.0001] | [-0.0004, +0.0001] | indistinguishable |
| LEAGUE | INDEPENDENT | 0.2499 | +0.0057 | [+0.0011, +0.0104] | [+0.0008, +0.0106] | market better |
| LEAGUE+mkt(w=0.8) | MARKET-INFORMED | 0.2439 | -0.0003 | [-0.0011, +0.0007] | [-0.0012, +0.0007] | indistinguishable |
| LEAGUE+mkt(w=0.9) | MARKET-INFORMED | 0.2440 | -0.0002 | [-0.0006, +0.0002] | [-0.0007, +0.0002] | indistinguishable |

## total_over_5.5 (n=1196; market Brier 0.2419)

| forecaster | kind | Brier | Δ vs market | 95% CI games | 95% CI slates | verdict |
|---|---|---:|---:|---|---|---|
| V1 | INDEPENDENT | 0.2444 | +0.0025 | [+0.0004, +0.0047] | [+0.0003, +0.0046] | market better |
| V1+mkt(w=0.8) | MARKET-INFORMED | 0.2421 | +0.0003 | [-0.0002, +0.0007] | [-0.0002, +0.0007] | indistinguishable |
| V1+mkt(w=0.9) | MARKET-INFORMED | 0.2420 | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0003] | indistinguishable |
| V1_C1 | INDEPENDENT | 0.2442 | +0.0024 | [+0.0004, +0.0044] | [+0.0005, +0.0042] | market better |
| V1_C1+mkt(w=0.8) | MARKET-INFORMED | 0.2421 | +0.0003 | [-0.0001, +0.0006] | [-0.0001, +0.0006] | indistinguishable |
| V1_C1+mkt(w=0.9) | MARKET-INFORMED | 0.2420 | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0003] | indistinguishable |
| OA_XG | INDEPENDENT | 0.2444 | +0.0025 | [-0.0002, +0.0052] | [-0.0001, +0.0050] | indistinguishable |
| OA_XG+mkt(w=0.8) | MARKET-INFORMED | 0.2420 | +0.0001 | [-0.0004, +0.0007] | [-0.0004, +0.0006] | indistinguishable |
| OA_XG+mkt(w=0.9) | MARKET-INFORMED | 0.2419 | +0.0000 | [-0.0002, +0.0003] | [-0.0002, +0.0003] | indistinguishable |
| OA_SVA | INDEPENDENT | 0.2444 | +0.0025 | [-0.0001, +0.0052] | [+0.0000, +0.0049] | indistinguishable |
| OA_SVA+mkt(w=0.8) | MARKET-INFORMED | 0.2420 | +0.0001 | [-0.0004, +0.0007] | [-0.0004, +0.0006] | indistinguishable |
| OA_SVA+mkt(w=0.9) | MARKET-INFORMED | 0.2419 | +0.0000 | [-0.0002, +0.0003] | [-0.0002, +0.0003] | indistinguishable |
| OA_SVA_C1 | INDEPENDENT | 0.2438 | +0.0019 | [-0.0002, +0.0040] | [-0.0001, +0.0038] | indistinguishable |
| OA_SVA_C1+mkt(w=0.8) | MARKET-INFORMED | 0.2420 | +0.0001 | [-0.0003, +0.0005] | [-0.0003, +0.0005] | indistinguishable |
| OA_SVA_C1+mkt(w=0.9) | MARKET-INFORMED | 0.2419 | +0.0001 | [-0.0002, +0.0003] | [-0.0001, +0.0002] | indistinguishable |
| LEAGUE | INDEPENDENT | 0.2447 | +0.0028 | [+0.0003, +0.0054] | [+0.0004, +0.0053] | market better |
| LEAGUE+mkt(w=0.8) | MARKET-INFORMED | 0.2421 | +0.0002 | [-0.0003, +0.0007] | [-0.0003, +0.0007] | indistinguishable |
| LEAGUE+mkt(w=0.9) | MARKET-INFORMED | 0.2419 | +0.0001 | [-0.0002, +0.0003] | [-0.0002, +0.0003] | indistinguishable |

## total_over_6.5 (n=1194; market Brier 0.2466)

| forecaster | kind | Brier | Δ vs market | 95% CI games | 95% CI slates | verdict |
|---|---|---:|---:|---|---|---|
| V1 | INDEPENDENT | 0.2501 | +0.0035 | [+0.0012, +0.0058] | [+0.0014, +0.0057] | market better |
| V1+mkt(w=0.8) | MARKET-INFORMED | 0.2470 | +0.0004 | [-0.0000, +0.0009] | [+0.0000, +0.0009] | indistinguishable |
| V1+mkt(w=0.9) | MARKET-INFORMED | 0.2468 | +0.0002 | [-0.0000, +0.0004] | [-0.0000, +0.0004] | indistinguishable |
| V1_C1 | INDEPENDENT | 0.2498 | +0.0032 | [+0.0010, +0.0053] | [+0.0013, +0.0052] | market better |
| V1_C1+mkt(w=0.8) | MARKET-INFORMED | 0.2470 | +0.0004 | [-0.0000, +0.0008] | [+0.0000, +0.0008] | indistinguishable |
| V1_C1+mkt(w=0.9) | MARKET-INFORMED | 0.2468 | +0.0002 | [-0.0000, +0.0004] | [+0.0000, +0.0004] | indistinguishable |
| OA_XG | INDEPENDENT | 0.2495 | +0.0029 | [+0.0001, +0.0056] | [+0.0003, +0.0055] | market better |
| OA_XG+mkt(w=0.8) | MARKET-INFORMED | 0.2468 | +0.0002 | [-0.0004, +0.0008] | [-0.0003, +0.0007] | indistinguishable |
| OA_XG+mkt(w=0.9) | MARKET-INFORMED | 0.2467 | +0.0001 | [-0.0002, +0.0004] | [-0.0002, +0.0003] | indistinguishable |
| OA_SVA | INDEPENDENT | 0.2500 | +0.0034 | [+0.0006, +0.0061] | [+0.0009, +0.0060] | market better |
| OA_SVA+mkt(w=0.8) | MARKET-INFORMED | 0.2469 | +0.0003 | [-0.0002, +0.0009] | [-0.0002, +0.0008] | indistinguishable |
| OA_SVA+mkt(w=0.9) | MARKET-INFORMED | 0.2467 | +0.0001 | [-0.0001, +0.0004] | [-0.0001, +0.0004] | indistinguishable |
| OA_SVA_C1 | INDEPENDENT | 0.2491 | +0.0025 | [+0.0003, +0.0047] | [+0.0005, +0.0045] | market better |
| OA_SVA_C1+mkt(w=0.8) | MARKET-INFORMED | 0.2469 | +0.0003 | [-0.0002, +0.0007] | [-0.0001, +0.0007] | indistinguishable |
| OA_SVA_C1+mkt(w=0.9) | MARKET-INFORMED | 0.2467 | +0.0001 | [-0.0001, +0.0003] | [-0.0001, +0.0003] | indistinguishable |
| LEAGUE | INDEPENDENT | 0.2503 | +0.0037 | [+0.0011, +0.0064] | [+0.0013, +0.0064] | market better |
| LEAGUE+mkt(w=0.8) | MARKET-INFORMED | 0.2470 | +0.0004 | [-0.0001, +0.0009] | [-0.0001, +0.0009] | indistinguishable |
| LEAGUE+mkt(w=0.9) | MARKET-INFORMED | 0.2468 | +0.0002 | [-0.0001, +0.0004] | [-0.0001, +0.0004] | indistinguishable |

## puck_away_-1.5 (n=1181; market Brier 0.1926)

| forecaster | kind | Brier | Δ vs market | 95% CI games | 95% CI slates | verdict |
|---|---|---:|---:|---|---|---|
| V1 | INDEPENDENT | 0.1939 | +0.0012 | [-0.0014, +0.0038] | [-0.0011, +0.0036] | indistinguishable |
| V1+mkt(w=0.8) | MARKET-INFORMED | 0.1925 | -0.0002 | [-0.0007, +0.0004] | [-0.0007, +0.0003] | indistinguishable |
| V1+mkt(w=0.9) | MARKET-INFORMED | 0.1925 | -0.0001 | [-0.0004, +0.0002] | [-0.0004, +0.0001] | indistinguishable |
| V1_C1 | INDEPENDENT | 0.1939 | +0.0013 | [-0.0011, +0.0037] | [-0.0010, +0.0035] | indistinguishable |
| V1_C1+mkt(w=0.8) | MARKET-INFORMED | 0.1925 | -0.0001 | [-0.0006, +0.0004] | [-0.0006, +0.0004] | indistinguishable |
| V1_C1+mkt(w=0.9) | MARKET-INFORMED | 0.1926 | -0.0001 | [-0.0003, +0.0002] | [-0.0003, +0.0002] | indistinguishable |
| OA_XG | INDEPENDENT | 0.1928 | +0.0001 | [-0.0021, +0.0024] | [-0.0020, +0.0022] | indistinguishable |
| OA_XG+mkt(w=0.8) | MARKET-INFORMED | 0.1923 | -0.0003 | [-0.0008, +0.0001] | [-0.0008, +0.0001] | indistinguishable |
| OA_XG+mkt(w=0.9) | MARKET-INFORMED | 0.1925 | -0.0002 | [-0.0004, +0.0001] | [-0.0004, +0.0000] | indistinguishable |
| OA_SVA | INDEPENDENT | 0.1927 | +0.0000 | [-0.0022, +0.0023] | [-0.0020, +0.0021] | indistinguishable |
| OA_SVA+mkt(w=0.8) | MARKET-INFORMED | 0.1923 | -0.0003 | [-0.0008, +0.0001] | [-0.0008, +0.0001] | indistinguishable |
| OA_SVA+mkt(w=0.9) | MARKET-INFORMED | 0.1925 | -0.0002 | [-0.0004, +0.0000] | [-0.0004, +0.0000] | indistinguishable |
| OA_SVA_C1 | INDEPENDENT | 0.1929 | +0.0002 | [-0.0020, +0.0025] | [-0.0018, +0.0023] | indistinguishable |
| OA_SVA_C1+mkt(w=0.8) | MARKET-INFORMED | 0.1924 | -0.0003 | [-0.0008, +0.0002] | [-0.0007, +0.0001] | indistinguishable |
| OA_SVA_C1+mkt(w=0.9) | MARKET-INFORMED | 0.1925 | -0.0002 | [-0.0004, +0.0001] | [-0.0004, +0.0001] | indistinguishable |
| LEAGUE | INDEPENDENT | 0.1967 | +0.0040 | [+0.0002, +0.0080] | [+0.0004, +0.0075] | market better |
| LEAGUE+mkt(w=0.8) | MARKET-INFORMED | 0.1925 | -0.0002 | [-0.0010, +0.0007] | [-0.0009, +0.0006] | indistinguishable |
| LEAGUE+mkt(w=0.9) | MARKET-INFORMED | 0.1925 | -0.0001 | [-0.0005, +0.0003] | [-0.0005, +0.0002] | indistinguishable |

## puck_home_-1.5 (n=1181; market Brier 0.2035)

| forecaster | kind | Brier | Δ vs market | 95% CI games | 95% CI slates | verdict |
|---|---|---:|---:|---|---|---|
| V1 | INDEPENDENT | 0.2050 | +0.0014 | [-0.0011, +0.0039] | [-0.0008, +0.0037] | indistinguishable |
| V1+mkt(w=0.8) | MARKET-INFORMED | 0.2034 | -0.0001 | [-0.0006, +0.0004] | [-0.0006, +0.0003] | indistinguishable |
| V1+mkt(w=0.9) | MARKET-INFORMED | 0.2035 | -0.0001 | [-0.0003, +0.0002] | [-0.0003, +0.0001] | indistinguishable |
| V1_C1 | INDEPENDENT | 0.2039 | +0.0003 | [-0.0021, +0.0028] | [-0.0017, +0.0024] | indistinguishable |
| V1_C1+mkt(w=0.8) | MARKET-INFORMED | 0.2032 | -0.0003 | [-0.0008, +0.0002] | [-0.0007, +0.0001] | indistinguishable |
| V1_C1+mkt(w=0.9) | MARKET-INFORMED | 0.2034 | -0.0002 | [-0.0004, +0.0001] | [-0.0004, +0.0000] | indistinguishable |
| OA_XG | INDEPENDENT | 0.2040 | +0.0004 | [-0.0019, +0.0027] | [-0.0017, +0.0024] | indistinguishable |
| OA_XG+mkt(w=0.8) | MARKET-INFORMED | 0.2033 | -0.0002 | [-0.0007, +0.0002] | [-0.0006, +0.0002] | indistinguishable |
| OA_XG+mkt(w=0.9) | MARKET-INFORMED | 0.2034 | -0.0001 | [-0.0004, +0.0001] | [-0.0003, +0.0001] | indistinguishable |
| OA_SVA | INDEPENDENT | 0.2037 | +0.0002 | [-0.0021, +0.0025] | [-0.0018, +0.0020] | indistinguishable |
| OA_SVA+mkt(w=0.8) | MARKET-INFORMED | 0.2033 | -0.0003 | [-0.0007, +0.0002] | [-0.0007, +0.0001] | indistinguishable |
| OA_SVA+mkt(w=0.9) | MARKET-INFORMED | 0.2034 | -0.0002 | [-0.0004, +0.0001] | [-0.0003, +0.0000] | indistinguishable |
| OA_SVA_C1 | INDEPENDENT | 0.2036 | +0.0001 | [-0.0023, +0.0024] | [-0.0019, +0.0019] | indistinguishable |
| OA_SVA_C1+mkt(w=0.8) | MARKET-INFORMED | 0.2032 | -0.0003 | [-0.0008, +0.0002] | [-0.0007, +0.0001] | indistinguishable |
| OA_SVA_C1+mkt(w=0.9) | MARKET-INFORMED | 0.2034 | -0.0002 | [-0.0004, +0.0001] | [-0.0004, +0.0000] | indistinguishable |
| LEAGUE | INDEPENDENT | 0.2112 | +0.0077 | [+0.0033, +0.0119] | [+0.0033, +0.0120] | market better |
| LEAGUE+mkt(w=0.8) | MARKET-INFORMED | 0.2040 | +0.0004 | [-0.0004, +0.0012] | [-0.0004, +0.0013] | indistinguishable |
| LEAGUE+mkt(w=0.9) | MARKET-INFORMED | 0.2037 | +0.0001 | [-0.0003, +0.0005] | [-0.0003, +0.0006] | indistinguishable |

