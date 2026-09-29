# DATA_ONLY_V1 walk-forward evaluation (WALK_FORWARD_V1)

> **HISTORICAL, NOT PROSPECTIVE. These numbers are a walk-forward replay on past seasons and use NO market data (no Kalshi NHL prices have been ingested). They say nothing about edge versus a market.**

Run `36567059940` generated 2026-09-29T12:17:52Z -- authority `RESEARCH_ONLY` -- model `DATA_ONLY_V1` / features `nhl-features-1.0` / sim `nhl-sim-1.0` -- machine-readable: `walk_forward_36567059940.json`.

## Setup

- Test seasons: 2024, 2025 (MoneyPuck start year (2024 == NHL 2024-25)).
- Training data: every MoneyPuck 'all'-situation row dated strictly before each game's date (walk-forward); regular-season rows only. MoneyPuck seasons on disk: [2022, 2023, 2024, 2025]; NHL result seasons on disk: [2022, 2023, 2024, 2025]; team-game rows in the log: 10496.
- Simulation: 4000 draws per game, seed = base 20240101 + game id.
- Goalies: Goalie factors are fixed at 1.0 for every game: the history archive has no point-in-time starting-goalie data, so the goalie term of DATA_ONLY_V1 is switched off in this replay. Live predictions include it.
- Markets: No market comparison: no historical Kalshi NHL prices have been ingested.
- Baselines: constant_home = walk-forward home-win rate over prior final regular-season games; league_poisson = same simulator with league-average lambdas (as_of game date) and the home adjustment only.
- Sample: **2624 regular-season games scored**; games with a team that had no prior MoneyPuck rows: 82. Skipped: not_regular_season=210, not_final=0, missing_score_or_period=0, unresolved_team=0.
- Elapsed: 28.5 s.

## Moneyline (P(home win) incl. OT/SO)

| forecaster | n | Brier | log loss | ECE | mean p | hit rate |
|---|---:|---:|---:|---:|---:|---:|
| DATA_ONLY_V1 | 2624 | 0.2420 | 0.6768 | 0.0261 | 0.5463 | 0.5423 |
| league_poisson | 2624 | 0.2483 | 0.6897 | 0.0020 | 0.5443 | 0.5423 |
| constant_home | 2624 | 0.2483 | 0.6898 | 0.0049 | 0.5374 | 0.5423 |

### Calibration (DATA_ONLY_V1 moneyline, 10 equal-width bins)

| bin | n | mean p | hit rate | gap |
|---|---:|---:|---:|---:|
| 0.0-0.1 | 0 | - | - | - |
| 0.1-0.2 | 0 | - | - | - |
| 0.2-0.3 | 0 | - | - | - |
| 0.3-0.4 | 20 | 0.377 | 0.300 | -0.077 |
| 0.4-0.5 | 586 | 0.468 | 0.461 | -0.008 |
| 0.5-0.6 | 1500 | 0.549 | 0.527 | -0.022 |
| 0.6-0.7 | 506 | 0.631 | 0.688 | 0.057 |
| 0.7-0.8 | 12 | 0.716 | 0.750 | 0.034 |
| 0.8-0.9 | 0 | - | - | - |
| 0.9-1.0 | 0 | - | - | - |

## Overtime (P(regulation tie))

| forecaster | n | Brier | log loss | ECE | mean p | OT rate |
|---|---:|---:|---:|---:|---:|---:|
| DATA_ONLY_V1 | 2624 | 0.1792 | 0.5478 | 0.0591 | 0.1684 | 0.2275 |
| league_poisson | 2624 | 0.1791 | 0.5471 | 0.0574 | 0.1701 | 0.2275 |

## Totals

| line | forecaster | n | Brier | log loss | ECE | mean p(over) | over rate |
|---|---|---:|---:|---:|---:|---:|---:|
| 5.5 | DATA_ONLY_V1 | 2624 | 0.2496 | 0.6928 | 0.0570 | 0.6098 | 0.5553 |
| 5.5 | league_poisson | 2624 | 0.2501 | 0.6936 | 0.0557 | 0.6110 | 0.5553 |
| 6.5 | DATA_ONLY_V1 | 2624 | 0.2498 | 0.6928 | 0.0541 | 0.4971 | 0.4459 |
| 6.5 | league_poisson | 2624 | 0.2503 | 0.6937 | 0.0524 | 0.4983 | 0.4459 |

| forecaster | n | total MAE | bias (exp - actual) | mean expected | mean actual | sd actual |
|---|---:|---:|---:|---:|---:|---:|
| DATA_ONLY_V1 | 2624 | 1.896 | 0.346 | 6.514 | 6.167 | 2.310 |
| league_poisson | 2624 | 1.906 | 0.348 | 6.515 | 6.167 | 2.310 |

## By season (moneyline Brier / log loss; total MAE)

| season | n | model Brier | model LL | league_poisson Brier | constant_home Brier | model OT Brier | model total MAE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2024 | 1312 | 0.2379 | 0.6685 | 0.2465 | 0.2468 | 0.1652 | 1.928 |
| 2025 | 1312 | 0.2461 | 0.6851 | 0.2501 | 0.2499 | 0.1932 | 1.865 |

## Reading this

- Lower Brier / log loss is better; ECE near 0 with gaps near 0 in every populated bin means calibrated. A model that cannot beat `league_poisson` on the moneyline carries no team information; one that cannot beat `constant_home` is worse than knowing nothing but home ice.
- Everything above is in-sample for the *constants* of DATA_ONLY_V1 only in the sense that they were chosen before this replay from public priors; they were not fitted to these results and must not be tuned to them.
- The first weeks of each test season lean on the previous season at a discount (`PREV_SEASON_DISCOUNT`); the first test season (2024) has two prior seasons of history, the second has three.
- Utah (2024-) is treated as a new club with no Arizona history, matching the identity registry.

> HISTORICAL, NOT PROSPECTIVE. These numbers are a walk-forward replay on past seasons and use NO market data (no Kalshi NHL prices have been ingested). They say nothing about edge versus a market.
