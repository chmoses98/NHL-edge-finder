# Prediction-engine comparison (Phase E)

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

Same games, same instant (T-60 min), same outcomes for every forecaster. Model = last production prediction at or before the cut (asserted in code); HIST models = the walk-forward V1 / V2 (SIM2_ST) predictions
for the 2025-26 season; LIVE models = production V1 / V2 / PLAYER_SIM_V1 rows. "Market" = the mid at the same instant. Intervals resample games.

* `dBrier` = Brier(model) - Brier(market): **positive = the model is worse**.
* `c` = coefficient in `y ~ offset(logit(mid)) + c * (logit(p_model) - logit(mid))`: 0 means the model adds nothing beyond the market; 1 means its disagreements are fully right.
* "anchored" = the production 0.8-weight logit blend of model and market (labelled "not independent evidence"): it can only track the market.

| forecaster / market | games | contracts | Brier model | Brier market | dBrier | 95% CI | verdict | dBrier anchored | c | z(c) | mean |model - market| |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HIST V1 winner | 1312 | 2,606 | 0.2457 | 0.2441 | +0.0016 | [-0.0016, +0.0048] |  | -0.0002 | 0.27 | 1.17 | 0.047 |
| HIST V1 total | 1198 | 4,743 | 0.2104 | 0.2088 | +0.0016 | [+0.0001, +0.0032] | WORSE | +0.0001 | -0.02 | -0.06 | 0.029 |
| HIST V1 spread | 1198 | 2,377 | 0.1993 | 0.1978 | +0.0015 | [-0.0005, +0.0036] |  | -0.0001 | 0.10 | 0.42 | 0.038 |
| HIST V1 all | 1312 | 9,726 | 0.2172 | 0.2156 | +0.0016 | [+0.0002, +0.0030] | WORSE | -0.0000 | 0.15 | 0.88 | 0.036 |
| HIST V2 winner | 1312 | 2,606 | 0.2456 | 0.2441 | +0.0015 | [-0.0017, +0.0047] |  | -0.0003 | 0.30 | 1.30 | 0.048 |
| HIST V2 total | 1198 | 4,743 | 0.2102 | 0.2088 | +0.0014 | [+0.0000, +0.0028] | WORSE | +0.0001 | -0.07 | -0.21 | 0.026 |
| HIST V2 spread | 1198 | 2,377 | 0.1993 | 0.1978 | +0.0014 | [-0.0006, +0.0036] |  | -0.0002 | 0.12 | 0.55 | 0.040 |
| HIST V2 all | 1312 | 9,726 | 0.2170 | 0.2156 | +0.0014 | [+0.0000, +0.0028] | WORSE | -0.0001 | 0.17 | 1.03 | 0.035 |
| LIVE V1 winner | 151 | 302 | 0.2304 | 0.2268 | +0.0036 | [-0.0064, +0.0131] |  | +0.0000 | -0.01 | -0.01 | 0.052 |
| LIVE V2 winner | 151 | 302 | 0.2340 | 0.2268 | +0.0072 | [-0.0033, +0.0174] |  | +0.0006 | -0.32 | -0.56 | 0.055 |
| LIVE V1 spread | 151 | 604 | 0.1784 | 0.1740 | +0.0045 | [-0.0007, +0.0098] |  | +0.0005 | -0.44 | -0.80 | 0.039 |
| LIVE V2 spread | 151 | 604 | 0.1791 | 0.1740 | +0.0051 | [-0.0004, +0.0109] |  | +0.0006 | -0.40 | -0.80 | 0.040 |
| LIVE V1 total | 151 | 1,287 | 0.1309 | 0.1284 | +0.0026 | [-0.0002, +0.0054] |  | +0.0003 | -0.53 | -0.87 | 0.026 |
| LIVE V2 total | 151 | 1,287 | 0.1305 | 0.1284 | +0.0021 | [+0.0003, +0.0038] | WORSE | +0.0003 | -1.46 | -1.73 | 0.017 |
| LIVE V1 team_total | 151 | 1,468 | 0.1733 | 0.1705 | +0.0028 | [-0.0005, +0.0061] |  | +0.0002 | -0.21 | -0.49 | 0.033 |
| LIVE V2 team_total | 151 | 1,468 | 0.1736 | 0.1705 | +0.0031 | [+0.0001, +0.0062] | WORSE | +0.0003 | -0.35 | -0.83 | 0.033 |
| LIVE V2 period_winner | 151 | 1,275 | 0.2184 | 0.2177 | +0.0007 | [-0.0014, +0.0029] |  | -0.0000 | 0.16 | 0.32 | 0.025 |
| LIVE V2 period_spread | 151 | 891 | 0.1328 | 0.1321 | +0.0007 | [-0.0006, +0.0020] |  | +0.0000 | -0.01 | -0.02 | 0.023 |
| LIVE V2 period_total | 151 | 1,285 | 0.1812 | 0.1815 | -0.0002 | [-0.0016, +0.0012] |  | -0.0001 | 0.59 | 0.99 | 0.020 |
| LIVE PLAYER_SIM goalie_saves | 136 | 213 | 0.2460 | 0.2428 | +0.0032 | [-0.0098, +0.0161] |  | -0.0008 | 0.34 | 0.96 | 0.075 |
| LIVE PLAYER_SIM player_assists | 145 | 3,977 | 0.1588 | 0.1561 | +0.0027 | [+0.0009, +0.0046] | WORSE | +0.0001 | 0.14 | 0.92 | 0.042 |
| LIVE PLAYER_SIM player_goals | 146 | 5,102 | 0.1196 | 0.1189 | +0.0008 | [+0.0002, +0.0013] | WORSE | +0.0001 | -0.09 | -0.40 | 0.020 |
| LIVE PLAYER_SIM player_points | 145 | 5,265 | 0.1675 | 0.1643 | +0.0032 | [+0.0014, +0.0051] | WORSE | +0.0002 | -0.11 | -0.65 | 0.039 |
| LIVE V1 four_families | 151 | 3,661 | 0.1640 | 0.1609 | +0.0031 | [-0.0001, +0.0063] |  | +0.0003 | -0.31 | -0.74 | 0.033 |

## Findings

* Across 24 family/tier comparisons the model is **significantly worse than the market in 9** and significantly better in **0**; no family has an incremental-information coefficient significantly above zero.
* Caveat: the 9 "WORSE" verdicts are uncorrected 95% intervals over 24 overlapping comparisons (e.g. "V1 all" contains V1 winner, total and spread; the three player families are correlated), and their lower bounds are barely above zero (smallest lower bound +0.0000).
  Read them as "consistently not better, and possibly slightly worse", with effect sizes of at most 0.0072 Brier points - not as 9 independent discoveries.
* The anchored blend differs from the market by at most 0.0008 Brier in any comparison: it is the market with a little model noise, not an independent forecast.
* The model's point estimate is worse than the market in 23 of 24 comparisons: where model and market disagree (typically 2-5 points) the market is, on average, the more accurate.
* V1 and V2 disagree with each other in sign on a meaningful share of contracts (two of the four Oct-20 wagers), and neither beats the market, so their disagreement is better read as model uncertainty than as edge.
* PLAYER_SIM_V1 (assists / points / goals) is significantly worse than the market on the LIVE tier; goalie saves is not distinguishable.

**Statement required by the brief:** the existing projection engines are consistently no better than a market-based baseline, and in several families slightly but measurably worse (tiny effects; see the caveat above). They provide no demonstrated incremental predictive
value. No challenger improvement was manufactured; the one challenger tested (matchup factors) also failed.

Distribution-level metrics (CRPS, tail behaviour) were **not** computed: the archive stores probabilities for fixed thresholds, not full predictive distributions, so CRPS would require re-simulating from stored seeds - listed in the roadmap.
