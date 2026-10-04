# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-04T02:19:13Z · rows 76181 · pregame 76181 · new 17879

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 14225 | 0.1780 | 0.5328 | 0.0276 | 0.4470 | 0.4629 |
| ALL | MARKET_BASELINE | 65383 | 0.1575 | 0.4809 | 0.0165 | 0.2949 | 0.3066 |
| ALL | MARKET_ANCHORED_V1 | 14225 | 0.1775 | 0.5317 | 0.0252 | 0.4537 | 0.4629 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 4033 | 0.0324 | 0.1464 | 0.0017 | 0.0344 | 0.0335 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 2276 | 0.1799 | 0.5424 | 0.0400 | 0.2304 | 0.2496 |
| game_spread | MARKET_BASELINE | 2276 | 0.1806 | 0.5459 | 0.0816 | 0.2415 | 0.2496 |
| game_spread | MARKET_ANCHORED_V1 | 2276 | 0.1801 | 0.5443 | 0.0717 | 0.2388 | 0.2496 |
| game_total | DATA_ONLY_V1 | 5121 | 0.1443 | 0.4464 | 0.0263 | 0.5647 | 0.5704 |
| game_total | MARKET_BASELINE | 5121 | 0.1408 | 0.4373 | 0.0252 | 0.5739 | 0.5704 |
| game_total | MARKET_ANCHORED_V1 | 5121 | 0.1414 | 0.4387 | 0.0242 | 0.5721 | 0.5704 |
| game_winner | DATA_ONLY_V1 | 1138 | 0.2338 | 0.6602 | 0.0767 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 1138 | 0.2435 | 0.6799 | 0.1900 | 0.4997 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 1138 | 0.2411 | 0.6748 | 0.1773 | 0.4998 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 271 | 0.2511 | 0.6962 | 0.0909 | 0.3904 | 0.4391 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 3282 | 0.1569 | 0.4981 | 0.0612 | 0.1310 | 0.1923 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 5106 | 0.1766 | 0.5264 | 0.0404 | 0.5950 | 0.6261 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 5109 | 0.2157 | 0.6219 | 0.0322 | 0.3278 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 9189 | 0.1600 | 0.4877 | 0.0256 | 0.2313 | 0.2385 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 13275 | 0.1209 | 0.3957 | 0.0192 | 0.1437 | 0.1507 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 10893 | 0.1816 | 0.5381 | 0.0323 | 0.3106 | 0.3196 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 5690 | 0.1964 | 0.5812 | 0.0580 | 0.4171 | 0.4441 |
| team_total | MARKET_BASELINE | 5690 | 0.1965 | 0.5826 | 0.0741 | 0.4257 | 0.4441 |
| team_total | MARKET_ANCHORED_V1 | 5690 | 0.1962 | 0.5817 | 0.0682 | 0.4238 | 0.4441 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
