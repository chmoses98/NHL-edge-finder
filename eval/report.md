# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-03T04:16:26Z · rows 812088 · pregame 812088 · new 4060

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 133275 | 0.1658 | 0.4994 | 0.0227 | 0.4498 | 0.4725 |
| ALL | MARKET_BASELINE | 698044 | 0.1438 | 0.4441 | 0.0124 | 0.2731 | 0.2840 |
| ALL | MARKET_ANCHORED_V1 | 133242 | 0.1636 | 0.4937 | 0.0159 | 0.4567 | 0.4726 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 50376 | 0.0338 | 0.1474 | 0.0016 | 0.0344 | 0.0353 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 21324 | 0.1852 | 0.5546 | 0.0310 | 0.2314 | 0.2610 |
| game_spread | MARKET_BASELINE | 21324 | 0.1807 | 0.5425 | 0.0235 | 0.2436 | 0.2610 |
| game_spread | MARKET_ANCHORED_V1 | 21324 | 0.1812 | 0.5440 | 0.0224 | 0.2407 | 0.2610 |
| game_total | DATA_ONLY_V1 | 47979 | 0.1293 | 0.4029 | 0.0310 | 0.5685 | 0.5935 |
| game_total | MARKET_BASELINE | 47979 | 0.1278 | 0.3989 | 0.0243 | 0.5779 | 0.5935 |
| game_total | MARKET_ANCHORED_V1 | 47979 | 0.1279 | 0.3993 | 0.0257 | 0.5761 | 0.5935 |
| game_winner | DATA_ONLY_V1 | 10662 | 0.2318 | 0.6560 | 0.0740 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 10662 | 0.2285 | 0.6485 | 0.0267 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 10662 | 0.2286 | 0.6488 | 0.0340 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 3122 | 0.2482 | 0.6901 | 0.0360 | 0.4463 | 0.4388 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 30487 | 0.1346 | 0.4406 | 0.0330 | 0.1287 | 0.1612 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 47760 | 0.1783 | 0.5315 | 0.0292 | 0.5996 | 0.6277 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 47808 | 0.2164 | 0.6234 | 0.0266 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 99696 | 0.1581 | 0.4833 | 0.0191 | 0.2297 | 0.2380 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 154537 | 0.1009 | 0.3368 | 0.0081 | 0.1191 | 0.1260 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 131016 | 0.1666 | 0.5027 | 0.0134 | 0.2814 | 0.2910 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 53310 | 0.1778 | 0.5329 | 0.0235 | 0.4203 | 0.4427 |
| team_total | MARKET_BASELINE | 53277 | 0.1754 | 0.5271 | 0.0182 | 0.4288 | 0.4429 |
| team_total | MARKET_ANCHORED_V1 | 53277 | 0.1756 | 0.5276 | 0.0184 | 0.4270 | 0.4429 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
