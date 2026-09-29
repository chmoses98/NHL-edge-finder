# DATA_ONLY_V1 walk-forward evaluation (WALK_FORWARD_V1)

> **HISTORICAL, NOT PROSPECTIVE. These numbers are a walk-forward replay on past seasons and use NO market data (no Kalshi NHL prices have been ingested). They say nothing about edge versus a market.**

Run `36570274279` generated 2026-09-29T12:46:43Z -- authority `RESEARCH_ONLY` -- model `DATA_ONLY_V1` / features `nhl-features-1.0` / sim `nhl-sim-1.1` -- machine-readable: `walk_forward_36570274279.json`.

## Setup

- Test seasons: 2024, 2025 (MoneyPuck start year (2024 == NHL 2024-25)).
- Training data: every MoneyPuck 'all'-situation row dated strictly before each game's date (walk-forward); regular-season rows only. MoneyPuck seasons on disk: [2022, 2023, 2024, 2025]; NHL result seasons on disk: [2022, 2023, 2024, 2025]; team-game rows in the log: 10496.
- Simulation: 4000 draws per game, seed = base 20240101 + game id.
- Goalies: Goalie factors are fixed at 1.0 for every game: the history archive has no point-in-time starting-goalie data, so the goalie term of DATA_ONLY_V1 is switched off in this replay. Live predictions include it.
- Markets: No market comparison: no historical Kalshi NHL prices have been ingested.
- Baselines: constant_home = walk-forward home-win rate over prior final regular-season games; league_poisson = same simulator with league-average lambdas (as_of game date) and the home adjustment only.
- Sample: **2624 regular-season games scored**; games with a team that had no prior MoneyPuck rows: 82. Skipped: not_regular_season=210, not_final=0, missing_score_or_period=0, unresolved_team=0.
- Elapsed: 29.1 s.

## Moneyline (P(home win) incl. OT/SO)

| forecaster | n | Brier | log loss | ECE | mean p | hit rate |
|---|---:|---:|---:|---:|---:|---:|
| DATA_ONLY_V1 | 2624 | 0.2419 | 0.6766 | 0.0225 | 0.5449 | 0.5423 |
| league_poisson | 2624 | 0.2483 | 0.6897 | 0.0005 | 0.5428 | 0.5423 |
| constant_home | 2624 | 0.2483 | 0.6898 | 0.0049 | 0.5374 | 0.5423 |

### Calibration (DATA_ONLY_V1 moneyline, 10 equal-width bins)

| bin | n | mean p | hit rate | gap |
|---|---:|---:|---:|---:|
| 0.0-0.1 | 0 | - | - | - |
| 0.1-0.2 | 0 | - | - | - |
| 0.2-0.3 | 0 | - | - | - |
| 0.3-0.4 | 19 | 0.380 | 0.368 | -0.011 |
| 0.4-0.5 | 575 | 0.469 | 0.457 | -0.011 |
| 0.5-0.6 | 1537 | 0.548 | 0.531 | -0.017 |
| 0.6-0.7 | 485 | 0.629 | 0.680 | 0.051 |
| 0.7-0.8 | 8 | 0.714 | 0.875 | 0.161 |
| 0.8-0.9 | 0 | - | - | - |
| 0.9-1.0 | 0 | - | - | - |

## Overtime (P(regulation tie))

| forecaster | n | Brier | log loss | ECE | mean p | OT rate |
|---|---:|---:|---:|---:|---:|---:|
| DATA_ONLY_V1 | 2624 | 0.1786 | 0.5456 | 0.0533 | 0.1742 | 0.2275 |
| league_poisson | 2624 | 0.1785 | 0.5452 | 0.0515 | 0.1761 | 0.2275 |

## Totals

| line | forecaster | n | Brier | log loss | ECE | mean p(over) | over rate |
|---|---|---:|---:|---:|---:|---:|---:|
| 5.5 | DATA_ONLY_V1 | 2624 | 0.2467 | 0.6865 | 0.0147 | 0.5612 | 0.5553 |
| 5.5 | league_poisson | 2624 | 0.2469 | 0.6870 | 0.0068 | 0.5621 | 0.5553 |
| 6.5 | DATA_ONLY_V1 | 2624 | 0.2472 | 0.6875 | 0.0188 | 0.4491 | 0.4459 |
| 6.5 | league_poisson | 2624 | 0.2475 | 0.6882 | 0.0041 | 0.4500 | 0.4459 |

| forecaster | n | total MAE | bias (exp - actual) | mean expected | mean actual | sd actual |
|---|---:|---:|---:|---:|---:|---:|
| DATA_ONLY_V1 | 2624 | 1.868 | 0.042 | 6.210 | 6.167 | 2.310 |
| league_poisson | 2624 | 1.873 | 0.043 | 6.210 | 6.167 | 2.310 |

## By season (moneyline Brier / log loss; total MAE)

| season | n | model Brier | model LL | league_poisson Brier | constant_home Brier | model OT Brier | model total MAE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2024 | 1312 | 0.2379 | 0.6685 | 0.2466 | 0.2468 | 0.1649 | 1.886 |
| 2025 | 1312 | 0.2459 | 0.6847 | 0.2499 | 0.2499 | 0.1923 | 1.850 |

## Reading this

- Lower Brier / log loss is better; ECE near 0 with gaps near 0 in every populated bin means calibrated. A model that cannot beat `league_poisson` on the moneyline carries no team information; one that cannot beat `constant_home` is worse than knowing nothing but home ice.
- Everything above is in-sample for the *constants* of DATA_ONLY_V1 only in the sense that they were chosen before this replay from public priors; they were not fitted to these results and must not be tuned to them.
- The first weeks of each test season lean on the previous season at a discount (`PREV_SEASON_DISCOUNT`); the first test season (2024) has two prior seasons of history, the second has three.
- Utah (2024-) is treated as a new club with no Arizona history, matching the identity registry.

> HISTORICAL, NOT PROSPECTIVE. These numbers are a walk-forward replay on past seasons and use NO market data (no Kalshi NHL prices have been ingested). They say nothing about edge versus a market.
