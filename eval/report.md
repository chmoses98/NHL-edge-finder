# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-01T23:02:18Z · rows 21943 · pregame 21943 · new 3014

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 3450 | 0.2196 | 0.6435 | 0.0929 | 0.4484 | 0.4759 |
| ALL | MARKET_BASELINE | 18546 | 0.1525 | 0.4688 | 0.0361 | 0.2732 | 0.2610 |
| ALL | MARKET_ANCHORED_V1 | 3450 | 0.2125 | 0.6235 | 0.0797 | 0.4549 | 0.4759 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 1609 | 0.0245 | 0.1227 | 0.0081 | 0.0323 | 0.0242 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 552 | 0.1945 | 0.5727 | 0.0800 | 0.2334 | 0.2826 |
| game_spread | MARKET_BASELINE | 552 | 0.1870 | 0.5522 | 0.1230 | 0.2439 | 0.2826 |
| game_spread | MARKET_ANCHORED_V1 | 552 | 0.1879 | 0.5551 | 0.1091 | 0.2413 | 0.2826 |
| game_total | DATA_ONLY_V1 | 1242 | 0.2053 | 0.6201 | 0.1123 | 0.5662 | 0.5821 |
| game_total | MARKET_BASELINE | 1242 | 0.1983 | 0.5936 | 0.1017 | 0.5739 | 0.5821 |
| game_total | MARKET_ANCHORED_V1 | 1242 | 0.1996 | 0.5986 | 0.1016 | 0.5724 | 0.5821 |
| game_winner | DATA_ONLY_V1 | 276 | 0.2624 | 0.7188 | 0.1047 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 276 | 0.2490 | 0.6937 | 0.1977 | 0.5001 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 276 | 0.2511 | 0.6972 | 0.2231 | 0.5001 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 112 | 0.2824 | 0.7615 | 0.2352 | 0.3900 | 0.4732 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 776 | 0.1499 | 0.4845 | 0.0809 | 0.1307 | 0.1753 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 1227 | 0.2012 | 0.5929 | 0.0913 | 0.5947 | 0.6218 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 1230 | 0.2175 | 0.6251 | 0.0589 | 0.3294 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 2622 | 0.1422 | 0.4495 | 0.0666 | 0.2355 | 0.1808 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 4438 | 0.1060 | 0.3549 | 0.0389 | 0.1242 | 0.1237 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 3082 | 0.1802 | 0.5350 | 0.0871 | 0.3213 | 0.2515 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 1380 | 0.2340 | 0.6779 | 0.1022 | 0.4180 | 0.4529 |
| team_total | MARKET_BASELINE | 1380 | 0.2244 | 0.6548 | 0.1302 | 0.4276 | 0.4529 |
| team_total | MARKET_ANCHORED_V1 | 1380 | 0.2261 | 0.6586 | 0.1246 | 0.4256 | 0.4529 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
