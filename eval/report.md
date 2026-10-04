# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-04T23:15:59Z · rows 94056 · pregame 94056 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 18000 | 0.1751 | 0.5240 | 0.0195 | 0.4471 | 0.4573 |
| ALL | MARKET_BASELINE | 80328 | 0.1583 | 0.4830 | 0.0153 | 0.2985 | 0.3071 |
| ALL | MARKET_ANCHORED_V1 | 18000 | 0.1747 | 0.5233 | 0.0256 | 0.4532 | 0.4573 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 4589 | 0.0358 | 0.1579 | 0.0047 | 0.0356 | 0.0370 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 2880 | 0.1806 | 0.5424 | 0.0385 | 0.2305 | 0.2597 |
| game_spread | MARKET_BASELINE | 2880 | 0.1806 | 0.5444 | 0.0693 | 0.2414 | 0.2597 |
| game_spread | MARKET_ANCHORED_V1 | 2880 | 0.1802 | 0.5431 | 0.0578 | 0.2388 | 0.2597 |
| game_total | DATA_ONLY_V1 | 6480 | 0.1375 | 0.4272 | 0.0168 | 0.5649 | 0.5623 |
| game_total | MARKET_BASELINE | 6480 | 0.1349 | 0.4203 | 0.0264 | 0.5731 | 0.5623 |
| game_total | MARKET_ANCHORED_V1 | 6480 | 0.1352 | 0.4213 | 0.0247 | 0.5715 | 0.5623 |
| game_winner | DATA_ONLY_V1 | 1440 | 0.2296 | 0.6514 | 0.0799 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 1440 | 0.2377 | 0.6675 | 0.1537 | 0.4998 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 1440 | 0.2356 | 0.6632 | 0.1555 | 0.4998 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 311 | 0.2589 | 0.7119 | 0.1040 | 0.3928 | 0.4855 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 4136 | 0.1600 | 0.5031 | 0.0671 | 0.1318 | 0.1990 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 6460 | 0.1831 | 0.5435 | 0.0222 | 0.5941 | 0.6147 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 6468 | 0.2161 | 0.6228 | 0.0369 | 0.3279 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 11122 | 0.1592 | 0.4862 | 0.0241 | 0.2324 | 0.2385 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 16392 | 0.1212 | 0.3972 | 0.0191 | 0.1458 | 0.1507 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 12850 | 0.1805 | 0.5356 | 0.0349 | 0.3136 | 0.3145 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 7200 | 0.1958 | 0.5782 | 0.0444 | 0.4172 | 0.4333 |
| team_total | MARKET_BASELINE | 7200 | 0.1961 | 0.5803 | 0.0732 | 0.4249 | 0.4333 |
| team_total | MARKET_ANCHORED_V1 | 7200 | 0.1958 | 0.5792 | 0.0655 | 0.4233 | 0.4333 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
