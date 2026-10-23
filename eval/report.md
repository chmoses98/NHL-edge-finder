# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-23T04:06:46Z · rows 499129 · pregame 499129 · new 7882

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 87400 | 0.1617 | 0.4894 | 0.0158 | 0.4489 | 0.4602 |
| ALL | MARKET_BASELINE | 410021 | 0.1483 | 0.4564 | 0.0081 | 0.2908 | 0.2952 |
| ALL | MARKET_ANCHORED_V1 | 87376 | 0.1603 | 0.4858 | 0.0142 | 0.4546 | 0.4603 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 17832 | 0.0396 | 0.1690 | 0.0026 | 0.0407 | 0.0414 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 13984 | 0.1804 | 0.5430 | 0.0228 | 0.2312 | 0.2524 |
| game_spread | MARKET_BASELINE | 13984 | 0.1774 | 0.5348 | 0.0249 | 0.2427 | 0.2524 |
| game_spread | MARKET_ANCHORED_V1 | 13984 | 0.1776 | 0.5354 | 0.0168 | 0.2399 | 0.2524 |
| game_total | DATA_ONLY_V1 | 31464 | 0.1243 | 0.3910 | 0.0289 | 0.5672 | 0.5792 |
| game_total | MARKET_BASELINE | 31464 | 0.1235 | 0.3888 | 0.0273 | 0.5750 | 0.5792 |
| game_total | MARKET_ANCHORED_V1 | 31464 | 0.1235 | 0.3888 | 0.0273 | 0.5735 | 0.5792 |
| game_winner | DATA_ONLY_V1 | 6992 | 0.2311 | 0.6548 | 0.0979 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 6992 | 0.2296 | 0.6506 | 0.0387 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 6992 | 0.2293 | 0.6503 | 0.0291 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1915 | 0.2510 | 0.6954 | 0.0580 | 0.4439 | 0.4449 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 19979 | 0.1385 | 0.4506 | 0.0388 | 0.1287 | 0.1668 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 31275 | 0.1801 | 0.5367 | 0.0264 | 0.5976 | 0.6208 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 31293 | 0.2168 | 0.6243 | 0.0235 | 0.3278 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 57103 | 0.1554 | 0.4765 | 0.0196 | 0.2350 | 0.2306 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 89157 | 0.1032 | 0.3434 | 0.0082 | 0.1255 | 0.1290 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 74091 | 0.1669 | 0.5022 | 0.0131 | 0.2923 | 0.2886 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 34960 | 0.1740 | 0.5236 | 0.0145 | 0.4192 | 0.4283 |
| team_total | MARKET_BASELINE | 34936 | 0.1727 | 0.5204 | 0.0166 | 0.4259 | 0.4286 |
| team_total | MARKET_ANCHORED_V1 | 34936 | 0.1727 | 0.5203 | 0.0187 | 0.4245 | 0.4286 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
