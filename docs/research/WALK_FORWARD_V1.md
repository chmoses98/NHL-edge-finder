# DATA_ONLY_V1 walk-forward evaluation (WALK_FORWARD_V1)

> **HISTORICAL, NOT PROSPECTIVE. These numbers are a walk-forward replay on past seasons and use NO market data (no Kalshi NHL prices have been ingested). They say nothing about edge versus a market.**

Run `39891401718` generated 2026-10-23T02:51:56Z -- authority `RESEARCH_ONLY` -- model `DATA_ONLY_V1` / features `nhl-features-1.0` / sim `nhl-sim-1.1` -- machine-readable: `walk_forward_39891401718.json`.

## Setup

- Test seasons: 2025 (MoneyPuck start year (2024 == NHL 2024-25)).
- Training data: every MoneyPuck 'all'-situation row dated strictly before each game's date (walk-forward); regular-season rows only. MoneyPuck seasons on disk: [2022, 2023, 2024, 2025]; NHL result seasons on disk: [2022, 2023, 2024, 2025]; team-game rows in the log: 10496.
- Simulation: 200 draws per game, seed = base 20240101 + game id.
- Goalies: Goalie factors are fixed at 1.0 for every game: the history archive has no point-in-time starting-goalie data, so the goalie term of DATA_ONLY_V1 is switched off in this replay. Live predictions include it.
- Markets: No market comparison: no historical Kalshi NHL prices have been ingested.
- Baselines: constant_home = walk-forward home-win rate over prior final regular-season games; league_poisson = same simulator with league-average lambdas (as_of game date) and the home adjustment only.
- Sample: **1312 regular-season games scored**; games with a team that had no prior MoneyPuck rows: 0. Skipped: not_regular_season=105, not_final=0, missing_score_or_period=0, unresolved_team=0.
- Elapsed: 12.3 s.

## Moneyline (P(home win) incl. OT/SO)

| forecaster | n | Brier | log loss | ECE | mean p | hit rate |
|---|---:|---:|---:|---:|---:|---:|
| DATA_ONLY_V1 | 1312 | 0.2467 | 0.6863 | 0.0241 | 0.5449 | 0.5221 |
| league_poisson | 1312 | 0.2518 | 0.6969 | 0.0228 | 0.5423 | 0.5221 |
| constant_home | 1312 | 0.2499 | 0.6929 | 0.0175 | 0.5396 | 0.5221 |

### Calibration (DATA_ONLY_V1 moneyline, 10 equal-width bins)

| bin | n | mean p | hit rate | gap |
|---|---:|---:|---:|---:|
| 0.0-0.1 | 0 | - | - | - |
| 0.1-0.2 | 0 | - | - | - |
| 0.2-0.3 | 0 | - | - | - |
| 0.3-0.4 | 14 | 0.371 | 0.214 | -0.156 |
| 0.4-0.5 | 286 | 0.462 | 0.462 | -0.001 |
| 0.5-0.6 | 740 | 0.546 | 0.518 | -0.029 |
| 0.6-0.7 | 255 | 0.632 | 0.604 | -0.028 |
| 0.7-0.8 | 17 | 0.717 | 0.765 | 0.048 |
| 0.8-0.9 | 0 | - | - | - |
| 0.9-1.0 | 0 | - | - | - |

## Overtime (P(regulation tie))

| forecaster | n | Brier | log loss | ECE | mean p | OT rate |
|---|---:|---:|---:|---:|---:|---:|
| DATA_ONLY_V1 | 1312 | 0.1922 | 0.5788 | 0.0753 | 0.1734 | 0.2485 |
| league_poisson | 1312 | 0.1942 | 0.5855 | 0.0783 | 0.1756 | 0.2485 |

## Totals

| line | forecaster | n | Brier | log loss | ECE | mean p(over) | over rate |
|---|---|---:|---:|---:|---:|---:|---:|
| 5.5 | DATA_ONLY_V1 | 1312 | 0.2451 | 0.6834 | 0.0419 | 0.5653 | 0.5732 |
| 5.5 | league_poisson | 1312 | 0.2446 | 0.6824 | 0.0216 | 0.5612 | 0.5732 |
| 6.5 | DATA_ONLY_V1 | 1312 | 0.2501 | 0.6934 | 0.0385 | 0.4546 | 0.4688 |
| 6.5 | league_poisson | 1312 | 0.2498 | 0.6928 | 0.0247 | 0.4480 | 0.4688 |

| forecaster | n | total MAE | bias (exp - actual) | mean expected | mean actual | sd actual |
|---|---:|---:|---:|---:|---:|---:|
| DATA_ONLY_V1 | 1312 | 1.848 | -0.013 | 6.240 | 6.254 | 2.297 |
| league_poisson | 1312 | 1.847 | -0.049 | 6.205 | 6.254 | 2.297 |

## By season (moneyline Brier / log loss; total MAE)

| season | n | model Brier | model LL | league_poisson Brier | constant_home Brier | model OT Brier | model total MAE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2025 | 1312 | 0.2467 | 0.6863 | 0.2518 | 0.2499 | 0.1922 | 1.848 |

## Reading this

- Lower Brier / log loss is better; ECE near 0 with gaps near 0 in every populated bin means calibrated. A model that cannot beat `league_poisson` on the moneyline carries no team information; one that cannot beat `constant_home` is worse than knowing nothing but home ice.
- Everything above is in-sample for the *constants* of DATA_ONLY_V1 only in the sense that they were chosen before this replay from public priors; they were not fitted to these results and must not be tuned to them.
- The first weeks of each test season lean on the previous season at a discount (`PREV_SEASON_DISCOUNT`); the first test season (2024) has two prior seasons of history, the second has three.
- Utah (2024-) is treated as a new club with no Arizona history, matching the identity registry.

> HISTORICAL, NOT PROSPECTIVE. These numbers are a walk-forward replay on past seasons and use NO market data (no Kalshi NHL prices have been ingested). They say nothing about edge versus a market.
