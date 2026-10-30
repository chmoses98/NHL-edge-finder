# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-30T02:07:51Z · rows 693531 · pregame 693531 · new 10052

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 115900 | 0.1657 | 0.4996 | 0.0163 | 0.4492 | 0.4642 |
| ALL | MARKET_BASELINE | 590695 | 0.1444 | 0.4458 | 0.0085 | 0.2771 | 0.2832 |
| ALL | MARKET_ANCHORED_V1 | 115875 | 0.1637 | 0.4943 | 0.0117 | 0.4562 | 0.4643 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 37948 | 0.0349 | 0.1521 | 0.0016 | 0.0356 | 0.0364 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 18544 | 0.1836 | 0.5513 | 0.0265 | 0.2311 | 0.2565 |
| game_spread | MARKET_BASELINE | 18544 | 0.1793 | 0.5395 | 0.0183 | 0.2431 | 0.2565 |
| game_spread | MARKET_ANCHORED_V1 | 18544 | 0.1799 | 0.5408 | 0.0176 | 0.2403 | 0.2565 |
| game_total | DATA_ONLY_V1 | 41724 | 0.1303 | 0.4063 | 0.0231 | 0.5677 | 0.5834 |
| game_total | MARKET_BASELINE | 41724 | 0.1292 | 0.4033 | 0.0219 | 0.5774 | 0.5834 |
| game_total | MARKET_ANCHORED_V1 | 41724 | 0.1292 | 0.4034 | 0.0199 | 0.5755 | 0.5834 |
| game_winner | DATA_ONLY_V1 | 9272 | 0.2335 | 0.6597 | 0.0859 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 9272 | 0.2295 | 0.6508 | 0.0264 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 9272 | 0.2297 | 0.6514 | 0.0356 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2727 | 0.2506 | 0.6949 | 0.0387 | 0.4474 | 0.4452 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 26498 | 0.1337 | 0.4390 | 0.0315 | 0.1288 | 0.1598 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 41535 | 0.1816 | 0.5396 | 0.0219 | 0.5998 | 0.6184 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 41553 | 0.2165 | 0.6237 | 0.0252 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 84005 | 0.1562 | 0.4788 | 0.0133 | 0.2302 | 0.2322 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 130588 | 0.0997 | 0.3334 | 0.0072 | 0.1195 | 0.1240 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 109966 | 0.1650 | 0.4979 | 0.0083 | 0.2830 | 0.2855 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 46360 | 0.1770 | 0.5309 | 0.0158 | 0.4196 | 0.4329 |
| team_total | MARKET_BASELINE | 46335 | 0.1749 | 0.5256 | 0.0154 | 0.4284 | 0.4330 |
| team_total | MARKET_ANCHORED_V1 | 46335 | 0.1750 | 0.5260 | 0.0134 | 0.4266 | 0.4330 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
