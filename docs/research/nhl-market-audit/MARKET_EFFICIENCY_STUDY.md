# Market-efficiency study (Phase C)

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

Two separate tiers, never pooled: **HIST** = 2025-26 regular season, Kalshi candle-close bid/ask (no depth), 1,312 games; **LIVE** = the 2026-27 archive, bid/ask board, 151 games.
"Gap" = realised frequency minus implied probability (the pre-friction efficiency diagnostic). "Net ROI" buys the displayed ask with the quadratic taker fee (verified to the cent on routed fills).
Every interval resamples whole games. Repeated snapshots, both legs of a market and several lines of one game are never treated as independent.

## 1. Calibration and returns by market (HIST, regular season, 95% CIs)

| market | min to start | games | contracts | Brier | calib. slope b | se(b) | gap | net ROI buy YES (95% CI) | net ROI buy NO (95% CI) | mean spread |
|---|---|---|---|---|---|---|---|---|---|---|
| spread | 0 | 1199 | 4753 | 0.1766 | 0.84 | 0.09 | -0.7% | -14.0% [-18.7%, -9.5%] | -3.0% [-4.6%, -1.3%] | 0.038 |
| spread | 60 | 1198 | 4736 | 0.1764 | 0.90 | 0.09 | -0.8% | -13.2% [-17.9%, -8.1%] | -2.4% [-4.2%, -0.7%] | 0.030 |
| spread | 1440 | 1161 | 4255 | 0.1852 | 0.57 | 0.08 | -3.1% | -32.0% [-36.1%, -27.7%] | -6.3% [-7.9%, -4.6%] | 0.142 |
| total | 0 | 1198 | 7068 | 0.1730 | 1.03 | 0.03 | +1.0% | -3.4% [-6.5%, -0.6%] | -8.7% [-12.3%, -4.8%] | 0.037 |
| total | 60 | 1198 | 6987 | 0.1735 | 1.03 | 0.03 | +1.0% | -3.2% [-6.2%, -0.3%] | -8.5% [-12.1%, -4.5%] | 0.034 |
| total | 1440 | 1148 | 5740 | 0.1808 | 1.09 | 0.04 | +2.7% | -7.9% [-10.9%, -4.7%] | -19.2% [-22.8%, -15.8%] | 0.127 |
| winner | 0 | 1312 | 2606 | 0.2443 | 0.78 | 0.14 | -0.0% | -4.3% [-4.7%, -4.0%] | -4.3% [-4.6%, -4.0%] | 0.011 |
| winner | 60 | 1312 | 2606 | 0.2441 | 0.80 | 0.14 | -0.0% | -4.3% [-4.7%, -4.0%] | -4.3% [-4.6%, -4.0%] | 0.011 |
| winner | 1440 | 1302 | 2585 | 0.2448 | 0.76 | 0.14 | +0.1% | -4.5% [-4.8%, -4.2%] | -4.7% [-5.1%, -4.4%] | 0.015 |

Reading it: a calibration slope b = 1 and intercept 0 mean the mid is a calibrated probability. Buying either side of the moneyline costs about the
spread plus the fee (-4.3% / -4.3% at T-60m): no mispricing is visible there.
Brier improves as puck drop approaches (price discovery): the T-24h mid is a noisier quote because the spread is wider, not because the market is "wrong". Moneyline slopes are about 1.5 standard errors below 1 in HIST and above 1 in LIVE, i.e. no stable direction.

### LIVE tier (151 games), same table

| market | min to start | games | contracts | Brier | calib. slope b | se(b) | gap | net ROI buy YES (95% CI) | net ROI buy NO (95% CI) | mean spread |
|---|---|---|---|---|---|---|---|---|---|---|
| early_goal | 0 | 151 | 151 | 0.2474 | 1.92 | 2.11 | -3.1% | -9.6% [-22.5%, +3.1%] | +0.7% [-16.8%, +18.2%] | 0.021 |
| early_goal | 60 | 151 | 151 | 0.2468 | 2.95 | 2.28 | -2.8% | -9.1% [-22.0%, +3.9%] | +0.1% [-17.4%, +17.6%] | 0.021 |
| first_goal | 0 | 128 | 394 | 0.0528 | 0.43 | 0.43 | +1.3% | -2.9% [-32.4%, +25.9%] | -2.8% [-4.7%, -1.1%] | 0.023 |
| first_goal | 60 | 115 | 319 | 0.0591 | 0.45 | 0.39 | +1.8% | +7.2% [-25.5%, +47.5%] | -3.2% [-5.8%, -1.2%] | 0.021 |
| overtime | 0 | 151 | 151 | 0.1783 | 0.77 | 2.55 | +1.6% | -1.4% [-29.5%, +27.0%] | -4.4% [-12.8%, +3.7%] | 0.015 |
| overtime | 60 | 140 | 140 | 0.1763 | 1.20 | 2.63 | +1.4% | -2.5% [-33.0%, +28.0%] | -4.1% [-13.0%, +4.7%] | 0.015 |
| overtime | 1440 | 85 | 85 | 0.1403 | 1.22 | 4.17 | -5.4% | -32.3% [-61.6%, +2.3%] | +3.8% [-6.5%, +12.8%] | 0.024 |
| period_spread | 0 | 151 | 897 | 0.1299 | 0.98 | 0.21 | +3.1% | +3.9% [-9.4%, +17.5%] | -6.1% [-8.4%, -3.9%] | 0.034 |
| period_spread | 60 | 151 | 891 | 0.1321 | 1.03 | 0.20 | +3.5% | +8.3% [-5.5%, +22.2%] | -6.4% [-8.6%, -4.1%] | 0.030 |
| period_spread | 1440 | 101 | 244 | 0.1427 | 0.62 | 0.48 | +1.8% | -40.1% [-54.5%, -24.0%] | -14.5% [-19.0%, -10.5%] | 0.241 |
| period_total | 0 | 151 | 1333 | 0.1818 | 1.04 | 0.07 | +1.3% | -2.3% [-7.5%, +3.0%] | -9.8% [-17.7%, -2.1%] | 0.030 |
| period_total | 60 | 151 | 1285 | 0.1815 | 1.03 | 0.07 | +1.5% | -1.9% [-7.2%, +3.5%] | -9.8% [-17.8%, -1.9%] | 0.027 |
| period_total | 1440 | 141 | 701 | 0.2034 | 1.05 | 0.09 | +0.3% | -12.0% [-18.7%, -5.2%] | -15.4% [-23.2%, -7.5%] | 0.129 |
| period_winner | 0 | 151 | 1321 | 0.2174 | 1.24 | 0.25 | +0.5% | -6.8% [-7.8%, -5.8%] | -4.9% [-5.4%, -4.3%] | 0.028 |
| period_winner | 60 | 151 | 1275 | 0.2177 | 1.17 | 0.26 | +0.4% | -6.9% [-8.2%, -5.5%] | -4.6% [-5.3%, -3.9%] | 0.026 |
| period_winner | 1440 | 141 | 953 | 0.2192 | 1.49 | 0.32 | +1.4% | -11.4% [-14.5%, -8.1%] | -9.6% [-11.2%, -8.2%] | 0.084 |
| player_stat | 0 | 151 | 15526 | 0.1477 | 0.97 | 0.03 | +0.1% | -10.6% [-16.0%, -5.3%] | -3.4% [-5.0%, -1.7%] | 0.033 |
| player_stat | 60 | 151 | 15268 | 0.1466 | 1.00 | 0.03 | -0.2% | -10.5% [-16.3%, -5.1%] | -2.5% [-4.2%, -0.8%] | 0.026 |
| spread | 0 | 151 | 604 | 0.1741 | 1.15 | 0.23 | +0.5% | -5.0% [-19.1%, +8.8%] | -2.8% [-7.5%, +1.9%] | 0.011 |
| spread | 60 | 151 | 604 | 0.1740 | 1.17 | 0.23 | +0.5% | -4.8% [-18.9%, +8.9%] | -2.9% [-7.5%, +1.9%] | 0.010 |
| spread | 1440 | 145 | 549 | 0.1811 | 1.08 | 0.25 | +1.5% | -2.1% [-15.5%, +12.0%] | -4.4% [-9.2%, +0.1%] | 0.015 |
| team_total | 0 | 151 | 1489 | 0.1706 | 1.03 | 0.06 | -0.2% | -4.8% [-12.1%, +2.3%] | -3.0% [-8.5%, +2.6%] | 0.015 |
| team_total | 60 | 151 | 1468 | 0.1705 | 1.03 | 0.06 | -0.2% | -5.0% [-12.3%, +2.1%] | -3.0% [-8.4%, +2.5%] | 0.016 |
| team_total | 1440 | 146 | 1304 | 0.1691 | 1.09 | 0.07 | -0.6% | -7.1% [-14.2%, -0.9%] | -3.6% [-8.7%, +2.0%] | 0.030 |
| total | 0 | 151 | 1323 | 0.1268 | 1.14 | 0.09 | -0.1% | -2.8% [-9.5%, +3.7%] | -3.3% [-11.6%, +5.3%] | 0.012 |
| total | 60 | 151 | 1287 | 0.1284 | 1.16 | 0.09 | +0.1% | -2.5% [-9.4%, +4.1%] | -3.7% [-11.9%, +4.9%] | 0.011 |
| total | 1440 | 146 | 1259 | 0.1229 | 1.20 | 0.10 | +0.3% | -2.7% [-9.0%, +3.3%] | -4.8% [-12.6%, +3.5%] | 0.018 |
| winner | 0 | 151 | 302 | 0.2275 | 1.48 | 0.39 | +0.0% | -4.1% [-4.2%, -4.0%] | -4.2% [-4.3%, -4.1%] | 0.010 |
| winner | 60 | 151 | 302 | 0.2268 | 1.54 | 0.40 | +0.1% | -4.0% [-4.1%, -3.9%] | -4.3% [-4.4%, -4.2%] | 0.010 |
| winner | 1440 | 146 | 291 | 0.2274 | 1.70 | 0.42 | +0.1% | -4.1% [-4.4%, -3.4%] | -4.5% [-5.1%, -4.1%] | 0.011 |

## 2. Price bands, all full-game markets pooled (HIST, T-60m)

| implied band | contracts | games | mean implied | frequency | gap (freq - implied) | gap 95% CI | net ROI buy YES | net ROI buy NO |
|---|---|---|---|---|---|---|---|---|
| (-0.001, 0.1] | 445 | 400 | 0.072 | 0.072 | +0.0% | [-2.4%, +2.4%] | -20.8% | -1.8% |
| (0.1, 0.2] | 1845 | 1163 | 0.162 | 0.174 | +1.2% | [-0.6%, +3.1%] | -7.0% | -4.2% |
| (0.2, 0.3] | 3003 | 1190 | 0.250 | 0.244 | -0.6% | [-2.1%, +1.0%] | -13.1% | -3.1% |
| (0.3, 0.4] | 1612 | 1144 | 0.348 | 0.339 | -0.9% | [-2.9%, +1.2%] | -9.4% | -2.4% |
| (0.4, 0.5] | 2056 | 1242 | 0.451 | 0.454 | +0.3% | [-1.9%, +2.4%] | -4.5% | -4.9% |
| (0.5, 0.6] | 1976 | 1215 | 0.551 | 0.552 | +0.1% | [-2.1%, +2.3%] | -4.3% | -5.7% |
| (0.6, 0.7] | 639 | 548 | 0.633 | 0.620 | -1.3% | [-5.0%, +2.4%] | -5.6% | -2.7% |
| (0.7, 0.8] | 832 | 792 | 0.765 | 0.791 | +2.6% | [-0.3%, +5.2%] | -0.9% | -22.2% |
| (0.8, 0.9] | 1446 | 1158 | 0.852 | 0.859 | +0.7% | [-1.5%, +2.8%] | -2.7% | -22.0% |
| (0.9, 1.0] | 475 | 419 | 0.934 | 0.956 | +2.1% | [+0.4%, +3.9%] | -1.0% | -55.7% |

The largest pooled-band gap is +2.6% in band (0.7, 0.8] (832 contracts, CI [-0.3%, +5.2%]). A favourite-longshot pattern would show NEGATIVE gaps at low implied
probability and POSITIVE gaps at high; the low bands are within noise, and the high-probability bands are mildly positive (high-probability YES contracts, mostly low-line Overs, hit slightly more often than
priced). Gaps of one to three points are smaller than the round-trip cost on any contract, so they cannot be monetised.

### Totals by line

| line | games | implied P(Over) | Over frequency | gap | 95% CI | net ROI Over | net ROI Under |
|---|---|---|---|---|---|---|---|
| 2.5 | 349 | 0.943 | 0.977 | +3.4% | [+1.5%, +4.8%] | -0.3% | -76.6% |
| 3.5 | 1165 | 0.868 | 0.872 | +0.4% | [-1.6%, +2.3%] | -3.0% | -23.3% |
| 4.5 | 1176 | 0.787 | 0.810 | +2.4% | [+0.2%, +4.7%] | -0.9% | -23.0% |
| 5.5 | 1193 | 0.572 | 0.576 | +0.4% | [-2.4%, +3.1%] | -3.7% | -6.5% |
| 6.5 | 1189 | 0.456 | 0.474 | +1.8% | [-1.1%, +4.8%] | -1.6% | -7.6% |
| 7.5 | 1185 | 0.260 | 0.257 | -0.3% | [-2.8%, +2.2%] | -12.7% | -3.8% |
| 8.5 | 361 | 0.179 | 0.199 | +2.0% | [-1.8%, +6.2%] | -0.6% | -4.9% |
| 9.5 | 369 | 0.075 | 0.073 | -0.2% | [-2.7%, +2.7%] | -19.6% | -1.4% |

### Totals gap by month (HIST) -- descriptive, post hoc

| month | games | Over gap | net ROI Under |
|---|---|---|---|
| 2025-10 | 70 | +10.5% | -33.4% |
| 2025-11 | 225 | -1.8% | -5.2% |
| 2025-12 | 222 | +0.2% | -7.3% |
| 2026-01 | 240 | +2.8% | -12.2% |
| 2026-02 | 74 | +1.0% | -8.2% |
| 2026-03 | 242 | +0.8% | -6.4% |
| 2026-04 | 125 | +0.3% | -4.8% |

October 2025 shows a large Over gap. This was noticed AFTER looking at the full season, so it is a hypothesis (registered as M6) and the HIST tier cannot validate it; the 2026 October archive tested it once (see CANDIDATE_SIGNAL_REGISTRY.md).

### Puck line (alternate spreads) by line

| line | games | implied | frequency | gap | net ROI buy YES | net ROI buy NO |
|---|---|---|---|---|---|---|
| 1.5 | 1198 | 0.299 | 0.285 | -1.4% | -12.8% | -1.7% |
| 2.5 | 1197 | 0.198 | 0.196 | -0.2% | -13.7% | -3.0% |

### Moneyline: home / favourite (HIST, T-60m)

| home | favourite | contracts | implied | win frequency | gap |
|---|---|---|---|---|---|
| False | False | 834 | 0.411 | 0.434 | +2.3% |
| False | True | 473 | 0.563 | 0.558 | -0.5% |
| True | False | 461 | 0.438 | 0.447 | +0.8% |
| True | True | 838 | 0.590 | 0.564 | -2.6% |

### Does a late price move predict the outcome? (HIST, T-24h to T-60m)

| mid move T-24h to T-60m | contracts | games | mean (outcome - mid) |
|---|---|---|---|
| (-1.0, -0.05] | 708 | 290 | -1.3% |
| (-0.05, -0.02] | 1406 | 729 | -1.4% |
| (-0.02, 0.02] | 7684 | 1255 | +0.1% |
| (0.02, 0.05] | 1998 | 848 | +2.0% |
| (0.05, 1.0] | 704 | 428 | +1.1% |

## 3. Friction dominates

Typical full-game spread is 1 to 4 cents and the taker fee is `0.07 p (1-p)` per contract (1.75c at 50c). Sensitivity of the registered one-sided strategies to fees, slippage and decision time is in STRATEGY_ROBUSTNESS.md:
before the fee, the best live strategy is about break-even; after it, essentially every strategy is negative.

## 4. How much evidence would an edge need?

Independent GAMES needed to detect a true net ROI of the stated size (one-sided alpha 0.05, 80% power), from the empirical per-game dispersion of returns:

| strategy | bets/game | sd of per-game ROI | games to detect 1% | games to detect 2% | games to detect 3% | games to detect 5% | games to detect 10% |
|---|---|---|---|---|---|---|---|
| M1 | 2.1 | 0.89 | 49,342 | 12,336 | 5,483 | 1,974 | 494 |
| M2 | 2.1 | 0.88 | 48,117 | 12,030 | 5,347 | 1,925 | 482 |
| M3 | 2.0 | 0.35 | 7,776 | 1,944 | 864 | 312 | 78 |
| M4 | 1.6 | 0.35 | 7,455 | 1,864 | 829 | 299 | 75 |
| M5 | 2.0 | 0.30 | 5,541 | 1,386 | 616 | 222 | 56 |

A season has about 1,312 games. Detecting a true +3% net ROI needs about 616 games for the lowest-variance (high-priced) strategies and about 5,483 for even-money bets - from most of a season to several seasons of one league, and only if the edge persists. Small edges are not discoverable from one season of Kalshi NHL data.

## Conclusion

* Moneylines: efficiently priced (HIST and LIVE); no statistically significant directional, favourite/underdog or home bias. The largest moneyline deviation is home favourites winning 2.6 points less often than priced (838 contracts; about 1.5 standard errors). The away-underdog row covers the same games, so it is one observation counted twice, not two.
* Full-game totals and puck lines: calibrated within about two to three points; the visible gaps are smaller than friction.
* Period, team-total, overtime, first-10-minutes and prop markets: only the LIVE tier exists (151 games); it can falsify large inefficiencies but not detect small ones.
* "Price discovery" (the mid improving toward puck drop) is not "forecastability": nothing here shows the pregame price is beatable before costs, let alone after.
