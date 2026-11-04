# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-04T13:59:07Z · rows 846671 · pregame 846671 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 139025 | 0.1661 | 0.5003 | 0.0215 | 0.4501 | 0.4717 |
| ALL | MARKET_BASELINE | 729888 | 0.1436 | 0.4435 | 0.0122 | 0.2726 | 0.2831 |
| ALL | MARKET_ANCHORED_V1 | 138992 | 0.1636 | 0.4938 | 0.0149 | 0.4569 | 0.4718 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 54077 | 0.0336 | 0.1469 | 0.0016 | 0.0342 | 0.0350 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 22244 | 0.1832 | 0.5506 | 0.0253 | 0.2315 | 0.2560 |
| game_spread | MARKET_BASELINE | 22244 | 0.1787 | 0.5383 | 0.0208 | 0.2436 | 0.2560 |
| game_spread | MARKET_ANCHORED_V1 | 22244 | 0.1792 | 0.5398 | 0.0174 | 0.2407 | 0.2560 |
| game_total | DATA_ONLY_V1 | 50049 | 0.1303 | 0.4053 | 0.0291 | 0.5689 | 0.5937 |
| game_total | MARKET_BASELINE | 50049 | 0.1286 | 0.4006 | 0.0234 | 0.5782 | 0.5937 |
| game_total | MARKET_ANCHORED_V1 | 50049 | 0.1287 | 0.4011 | 0.0242 | 0.5763 | 0.5937 |
| game_winner | DATA_ONLY_V1 | 11122 | 0.2334 | 0.6593 | 0.0689 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 11122 | 0.2290 | 0.6494 | 0.0253 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 11122 | 0.2293 | 0.6503 | 0.0293 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 3264 | 0.2478 | 0.6892 | 0.0356 | 0.4464 | 0.4357 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 31799 | 0.1326 | 0.4357 | 0.0300 | 0.1289 | 0.1584 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 49830 | 0.1779 | 0.5308 | 0.0295 | 0.5998 | 0.6271 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 49878 | 0.2170 | 0.6247 | 0.0216 | 0.3284 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 104043 | 0.1583 | 0.4837 | 0.0187 | 0.2296 | 0.2383 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 161218 | 0.1010 | 0.3375 | 0.0089 | 0.1190 | 0.1260 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 136787 | 0.1667 | 0.5028 | 0.0145 | 0.2811 | 0.2906 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 55610 | 0.1780 | 0.5337 | 0.0237 | 0.4207 | 0.4425 |
| team_total | MARKET_BASELINE | 55577 | 0.1753 | 0.5270 | 0.0180 | 0.4290 | 0.4427 |
| team_total | MARKET_ANCHORED_V1 | 55577 | 0.1756 | 0.5277 | 0.0186 | 0.4273 | 0.4427 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
