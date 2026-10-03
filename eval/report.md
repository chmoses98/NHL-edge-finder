# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-03T22:07:44Z · rows 58302 · pregame 58302 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 10725 | 0.1901 | 0.5636 | 0.0565 | 0.4440 | 0.4816 |
| ALL | MARKET_BASELINE | 50380 | 0.1584 | 0.4824 | 0.0170 | 0.2906 | 0.3011 |
| ALL | MARKET_ANCHORED_V1 | 10725 | 0.1897 | 0.5623 | 0.0454 | 0.4523 | 0.4816 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 3502 | 0.0304 | 0.1377 | 0.0023 | 0.0337 | 0.0314 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 1716 | 0.1991 | 0.5869 | 0.0729 | 0.2291 | 0.2844 |
| game_spread | MARKET_BASELINE | 1716 | 0.2013 | 0.5949 | 0.1124 | 0.2419 | 0.2844 |
| game_spread | MARKET_ANCHORED_V1 | 1716 | 0.2004 | 0.5923 | 0.1051 | 0.2388 | 0.2844 |
| game_total | DATA_ONLY_V1 | 3861 | 0.1504 | 0.4655 | 0.0475 | 0.5608 | 0.5856 |
| game_total | MARKET_BASELINE | 3861 | 0.1457 | 0.4523 | 0.0493 | 0.5725 | 0.5856 |
| game_total | MARKET_ANCHORED_V1 | 3861 | 0.1465 | 0.4545 | 0.0542 | 0.5702 | 0.5856 |
| game_winner | DATA_ONLY_V1 | 858 | 0.2482 | 0.6895 | 0.0450 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 858 | 0.2597 | 0.7134 | 0.2175 | 0.4999 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 858 | 0.2569 | 0.7074 | 0.1848 | 0.5000 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 225 | 0.2516 | 0.6973 | 0.1458 | 0.3892 | 0.4178 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 2465 | 0.1644 | 0.5208 | 0.0793 | 0.1304 | 0.1992 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 3846 | 0.1864 | 0.5501 | 0.0451 | 0.5938 | 0.6388 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 3849 | 0.2178 | 0.6265 | 0.0360 | 0.3280 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 7082 | 0.1520 | 0.4660 | 0.0371 | 0.2313 | 0.2180 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 10250 | 0.1224 | 0.3999 | 0.0270 | 0.1403 | 0.1504 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 8436 | 0.1767 | 0.5238 | 0.0459 | 0.3100 | 0.2946 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 4290 | 0.2106 | 0.6173 | 0.0951 | 0.4137 | 0.4632 |
| team_total | MARKET_BASELINE | 4290 | 0.2112 | 0.6193 | 0.1343 | 0.4244 | 0.4632 |
| team_total | MARKET_ANCHORED_V1 | 4290 | 0.2109 | 0.6182 | 0.1244 | 0.4222 | 0.4632 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
