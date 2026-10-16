# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-16T03:11:21Z · rows 338992 · pregame 338992 · new 12937

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 61200 | 0.1641 | 0.4954 | 0.0156 | 0.4490 | 0.4606 |
| ALL | MARKET_BASELINE | 283084 | 0.1488 | 0.4579 | 0.0090 | 0.2906 | 0.2954 |
| ALL | MARKET_ANCHORED_V1 | 61183 | 0.1616 | 0.4888 | 0.0132 | 0.4531 | 0.4607 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 13045 | 0.0402 | 0.1715 | 0.0045 | 0.0395 | 0.0420 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 9792 | 0.1805 | 0.5432 | 0.0253 | 0.2312 | 0.2522 |
| game_spread | MARKET_BASELINE | 9792 | 0.1770 | 0.5340 | 0.0242 | 0.2415 | 0.2522 |
| game_spread | MARKET_ANCHORED_V1 | 9792 | 0.1774 | 0.5349 | 0.0190 | 0.2390 | 0.2522 |
| game_total | DATA_ONLY_V1 | 22032 | 0.1285 | 0.4013 | 0.0203 | 0.5675 | 0.5801 |
| game_total | MARKET_BASELINE | 22032 | 0.1256 | 0.3935 | 0.0266 | 0.5724 | 0.5801 |
| game_total | MARKET_ANCHORED_V1 | 22032 | 0.1260 | 0.3946 | 0.0262 | 0.5714 | 0.5801 |
| game_winner | DATA_ONLY_V1 | 4896 | 0.2298 | 0.6522 | 0.1078 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 4896 | 0.2278 | 0.6470 | 0.0377 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 4896 | 0.2276 | 0.6468 | 0.0404 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1214 | 0.2451 | 0.6839 | 0.0867 | 0.4297 | 0.3913 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 14110 | 0.1405 | 0.4561 | 0.0406 | 0.1294 | 0.1690 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 21843 | 0.1821 | 0.5420 | 0.0256 | 0.5952 | 0.6155 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 21861 | 0.2170 | 0.6248 | 0.0190 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 38843 | 0.1539 | 0.4727 | 0.0169 | 0.2330 | 0.2298 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 61491 | 0.1049 | 0.3488 | 0.0107 | 0.1273 | 0.1304 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 49494 | 0.1676 | 0.5045 | 0.0136 | 0.2944 | 0.2897 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 24480 | 0.1765 | 0.5297 | 0.0168 | 0.4194 | 0.4284 |
| team_total | MARKET_BASELINE | 24463 | 0.1738 | 0.5230 | 0.0156 | 0.4239 | 0.4286 |
| team_total | MARKET_ANCHORED_V1 | 24463 | 0.1741 | 0.5236 | 0.0161 | 0.4229 | 0.4286 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
