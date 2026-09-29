# DATA_ONLY_V2 candidate walk-forward (WALK_FORWARD_V2)

> **HISTORICAL, NOT PROSPECTIVE. Walk-forward replay on past seasons with every V2 parameter fitted on earlier seasons only. Goalie arms use the actual starter (retrospective oracle), not a pregame backtest.**

Run `wf2_20260929` · 2026-09-29T15:15:34+00:00 · authority `RESEARCH_ONLY` · n = 2624 regular-season games (test seasons [2024, 2025], identical games for every arm) · 4000 draws per arm per game · 459.6 s

Arms: `V1` = DATA_ONLY_V1 (nhl-sim-1.1) · `SIM2` = V1 lambdas + nhl-sim-2.0 · `SIM2_ST` = special-teams lambdas + nhl-sim-2.0 (goalie 1.0; **valid pregame arm**) · `V1_G1` = V1 + V1-style goalie factor of the actual starter · `SIM2_ST_GTT` = SIM2_ST + goalie true talent of the actual starter. **The two goalie arms are retrospective oracle-style analysis** (actual starters), not a pregame backtest.

## Moneyline (P(home win) incl. OT/SO)

| arm | Brier | log loss | ECE | mean p | hit rate |
|---|---:|---:|---:|---:|---:|
| V1 | 0.2419 | 0.6766 | 0.0225 | 0.545 | 0.542 |
| SIM2 | 0.2418 | 0.6763 | 0.0278 | 0.545 | 0.542 |
| SIM2_ST | 0.2417 | 0.6763 | 0.0254 | 0.545 | 0.542 |
| V1_G1 | 0.2420 | 0.6767 | 0.0091 | 0.546 | 0.542 |
| SIM2_ST_GTT | 0.2415 | 0.6758 | 0.0330 | 0.546 | 0.542 |

## Regulation tie / OT

| arm | predicted P(OT) | observed | Brier | log loss | ECE |
|---|---:|---:|---:|---:|---:|
| V1 | 0.1742 | 0.2275 | 0.1786 | 0.5456 | 0.0533 |
| SIM2 | 0.2123 | 0.2275 | 0.1761 | 0.5374 | 0.0152 |
| SIM2_ST | 0.2126 | 0.2275 | 0.1759 | 0.5368 | 0.0149 |
| V1_G1 | 0.1740 | 0.2275 | 0.1788 | 0.5464 | 0.0536 |
| SIM2_ST_GTT | 0.2127 | 0.2275 | 0.1761 | 0.5372 | 0.0161 |

## Regulation winner (3-way home regulation win; and home win given no OT)

| arm | 3-way Brier | 3-way LL | given-no-OT Brier | given-no-OT LL |
|---|---:|---:|---:|---:|
| V1 | 0.2392 | 0.6712 | 0.2378 | 0.6682 |
| SIM2 | 0.2385 | 0.6698 | 0.2377 | 0.6679 |
| SIM2_ST | 0.2385 | 0.6698 | 0.2377 | 0.6679 |
| V1_G1 | 0.2400 | 0.6728 | 0.2380 | 0.6685 |
| SIM2_ST_GTT | 0.2384 | 0.6695 | 0.2374 | 0.6673 |

## Totals

| arm | exp total | actual | bias | MAE | exact-total log-lik/game | O4.5 Brier | O5.5 Brier | O6.5 Brier | O7.5 Brier | O5.5 ECE | O6.5 ECE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V1 | 6.210 | 6.167 | 0.042 | 1.868 | -2.1813 | 0.1707 | 0.2467 | 0.2472 | 0.1874 | 0.0147 | 0.0188 |
| SIM2 | 6.243 | 6.167 | 0.076 | 1.871 | -2.1822 | 0.1708 | 0.2470 | 0.2475 | 0.1876 | 0.0202 | 0.0285 |
| SIM2_ST | 6.234 | 6.167 | 0.067 | 1.871 | -2.1806 | 0.1705 | 0.2467 | 0.2474 | 0.1875 | 0.0143 | 0.0201 |
| V1_G1 | 6.150 | 6.167 | -0.017 | 1.867 | -2.1843 | 0.1718 | 0.2474 | 0.2478 | 0.1872 | 0.0235 | 0.0280 |
| SIM2_ST_GTT | 6.205 | 6.167 | 0.038 | 1.865 | -2.1793 | 0.1705 | 0.2462 | 0.2469 | 0.1871 | 0.0041 | 0.0125 |

## Puck line and team totals (Brier)

| arm | home -1.5 | away -1.5 | home o2.5 | home o3.5 | away o2.5 | away o3.5 |
|---|---:|---:|---:|---:|---:|---:|
| V1 | 0.2146 | 0.1913 | 0.2314 | 0.2374 | 0.2390 | 0.2294 |
| SIM2 | 0.2149 | 0.1915 | 0.2318 | 0.2378 | 0.2388 | 0.2295 |
| SIM2_ST | 0.2149 | 0.1914 | 0.2314 | 0.2373 | 0.2386 | 0.2293 |
| V1_G1 | 0.2153 | 0.1916 | 0.2304 | 0.2389 | 0.2399 | 0.2302 |
| SIM2_ST_GTT | 0.2147 | 0.1913 | 0.2309 | 0.2370 | 0.2388 | 0.2292 |

## Periods (nhl-sim-2.0 arms only; outcomes from MoneyPuck goal times)

| arm | period | exp total | actual | home-win Brier | tie Brier | over 1.5 Brier | tie mean p / rate |
|---|---|---:|---:|---:|---:|---:|---|
| SIM2 | P1 | 1.797 | 1.744 | 0.2257 | 0.2257 | 0.2486 | 0.342 / 0.344 |
| SIM2 | P2 | 2.128 | 2.040 | 0.2318 | 0.2075 | 0.2367 | 0.301 / 0.294 |
| SIM2 | P3 | 2.106 | 2.151 | 0.2352 | 0.1937 | 0.2278 | 0.287 / 0.261 |
| SIM2_ST | P1 | 1.794 | 1.744 | 0.2258 | 0.2257 | 0.2484 | 0.342 / 0.344 |
| SIM2_ST | P2 | 2.125 | 2.040 | 0.2318 | 0.2076 | 0.2365 | 0.301 / 0.294 |
| SIM2_ST | P3 | 2.103 | 2.151 | 0.2352 | 0.1937 | 0.2273 | 0.288 / 0.261 |
| SIM2_ST_GTT | P1 | 1.785 | 1.744 | 0.2254 | 0.2254 | 0.2482 | 0.343 / 0.344 |
| SIM2_ST_GTT | P2 | 2.115 | 2.040 | 0.2317 | 0.2075 | 0.2362 | 0.301 / 0.294 |
| SIM2_ST_GTT | P3 | 2.093 | 2.151 | 0.2353 | 0.1937 | 0.2281 | 0.288 / 0.261 |

## Subgroups (moneyline Brier)

- **goalie_sensitive_top_quartile** (n=656; |log home_gtt - log away_gtt| in top quartile (oracle starters)): V1 0.2472, SIM2 0.2474, SIM2_ST 0.2471, V1_G1 0.2493, SIM2_ST_GTT 0.2470
- **special_teams_extreme_top_quartile** (n=656; |log(lam ratio ST) - log(lam ratio V1)| in top quartile): V1 0.2414, SIM2 0.2420, SIM2_ST 0.2413, V1_G1 0.2414, SIM2_ST_GTT 0.2410

| season | V1 ML Brier | SIM2 ML Brier | SIM2_ST ML Brier | V1_G1 ML Brier | SIM2_ST_GTT ML Brier | V1 OT Brier | SIM2 OT Brier | SIM2_ST OT Brier | V1_G1 OT Brier | SIM2_ST_GTT OT Brier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2024 | 0.2379 | 0.2377 | 0.2377 | 0.2364 | 0.2375 | 0.1649 | 0.1644 | 0.1640 | 0.1654 | 0.1641 |
| 2025 | 0.2459 | 0.2458 | 0.2458 | 0.2475 | 0.2455 | 0.1923 | 0.1879 | 0.1878 | 0.1923 | 0.1881 |

## Fitted parameters (per test season; fitted on earlier seasons only)

- test 2024: hazards from shots seasons [2021, 2022, 2023], p(OT goal | OT) = 0.689, scale = 1.0102, env dispersion = 0.0 (validation 2023: {'0.0': -2.17963, '0.015': -2.18704, '0.03': -2.19391, '0.05': -2.20768}), goalie prior K = 1500.0 xG (validation log-lik {'300.0': -71.897, '700.0': -70.525, '1000.0': -70.388, '1500.0': -70.368, '2500.0': -70.426}), goalie back-to-back multiplier 0.9904 (95 starts).
- test 2025: hazards from shots seasons [2021, 2022, 2023, 2024], p(OT goal | OT) = 0.697, scale = 1.0088, env dispersion = 0.0 (validation 2024: {'0.0': -2.20455, '0.015': -2.20579, '0.03': -2.21108, '0.05': -2.22223}), goalie prior K = 300.0 xG (validation log-lik {'300.0': -231.373, '700.0': -232.683, '1000.0': -233.353, '1500.0': -234.056, '2500.0': -234.775}), goalie back-to-back multiplier 1.0167 (140 starts).

> HISTORICAL, NOT PROSPECTIVE. Walk-forward replay on past seasons with every V2 parameter fitted on earlier seasons only. Goalie arms use the actual starter (retrospective oracle), not a pregame backtest.
