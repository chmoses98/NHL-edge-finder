# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-26T04:53:54Z · rows 597495 · pregame 597495 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 101500 | 0.1653 | 0.4980 | 0.0199 | 0.4487 | 0.4669 |
| ALL | MARKET_BASELINE | 498148 | 0.1479 | 0.4550 | 0.0099 | 0.2837 | 0.2924 |
| ALL | MARKET_ANCHORED_V1 | 101475 | 0.1632 | 0.4926 | 0.0150 | 0.4553 | 0.4670 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 26086 | 0.0383 | 0.1647 | 0.0028 | 0.0381 | 0.0401 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 16240 | 0.1855 | 0.5559 | 0.0292 | 0.2310 | 0.2589 |
| game_spread | MARKET_BASELINE | 16240 | 0.1814 | 0.5447 | 0.0202 | 0.2427 | 0.2589 |
| game_spread | MARKET_ANCHORED_V1 | 16240 | 0.1819 | 0.5459 | 0.0197 | 0.2399 | 0.2589 |
| game_total | DATA_ONLY_V1 | 36540 | 0.1279 | 0.3991 | 0.0283 | 0.5670 | 0.5875 |
| game_total | MARKET_BASELINE | 36540 | 0.1265 | 0.3952 | 0.0282 | 0.5762 | 0.5875 |
| game_total | MARKET_ANCHORED_V1 | 36540 | 0.1266 | 0.3955 | 0.0267 | 0.5744 | 0.5875 |
| game_winner | DATA_ONLY_V1 | 8120 | 0.2330 | 0.6586 | 0.0923 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 8120 | 0.2298 | 0.6514 | 0.0287 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 8120 | 0.2298 | 0.6516 | 0.0418 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2277 | 0.2538 | 0.7014 | 0.0533 | 0.4445 | 0.4629 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 23138 | 0.1369 | 0.4470 | 0.0361 | 0.1288 | 0.1642 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 36351 | 0.1820 | 0.5414 | 0.0269 | 0.5988 | 0.6233 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 36369 | 0.2175 | 0.6260 | 0.0184 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 70695 | 0.1579 | 0.4826 | 0.0131 | 0.2321 | 0.2353 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 109703 | 0.1028 | 0.3420 | 0.0078 | 0.1223 | 0.1286 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 92054 | 0.1675 | 0.5041 | 0.0092 | 0.2870 | 0.2914 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 40600 | 0.1774 | 0.5319 | 0.0184 | 0.4190 | 0.4349 |
| team_total | MARKET_BASELINE | 40575 | 0.1752 | 0.5266 | 0.0191 | 0.4272 | 0.4351 |
| team_total | MARKET_ANCHORED_V1 | 40575 | 0.1754 | 0.5270 | 0.0163 | 0.4255 | 0.4351 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
