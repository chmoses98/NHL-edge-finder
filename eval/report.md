# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-05T23:59:25Z · rows 105286 · pregame 105286 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 20275 | 0.1700 | 0.5117 | 0.0125 | 0.4491 | 0.4518 |
| ALL | MARKET_BASELINE | 89992 | 0.1563 | 0.4785 | 0.0130 | 0.2992 | 0.3050 |
| ALL | MARKET_ANCHORED_V1 | 20275 | 0.1694 | 0.5102 | 0.0199 | 0.4534 | 0.4518 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 5063 | 0.0375 | 0.1642 | 0.0059 | 0.0359 | 0.0389 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 3244 | 0.1758 | 0.5309 | 0.0286 | 0.2309 | 0.2512 |
| game_spread | MARKET_BASELINE | 3244 | 0.1764 | 0.5334 | 0.0531 | 0.2414 | 0.2512 |
| game_spread | MARKET_ANCHORED_V1 | 3244 | 0.1758 | 0.5318 | 0.0414 | 0.2388 | 0.2512 |
| game_total | DATA_ONLY_V1 | 7299 | 0.1318 | 0.4124 | 0.0245 | 0.5676 | 0.5583 |
| game_total | MARKET_BASELINE | 7299 | 0.1288 | 0.4045 | 0.0276 | 0.5728 | 0.5583 |
| game_total | MARKET_ANCHORED_V1 | 7299 | 0.1292 | 0.4057 | 0.0257 | 0.5718 | 0.5583 |
| game_winner | DATA_ONLY_V1 | 1622 | 0.2250 | 0.6422 | 0.1196 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 1622 | 0.2331 | 0.6578 | 0.1343 | 0.4997 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 1622 | 0.2308 | 0.6534 | 0.1385 | 0.4998 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 352 | 0.2571 | 0.7084 | 0.1012 | 0.3901 | 0.4659 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 4618 | 0.1577 | 0.4961 | 0.0648 | 0.1312 | 0.1960 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 7244 | 0.1837 | 0.5453 | 0.0194 | 0.5938 | 0.6081 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 7287 | 0.2167 | 0.6243 | 0.0310 | 0.3281 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 12441 | 0.1573 | 0.4808 | 0.0175 | 0.2325 | 0.2380 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 18218 | 0.1204 | 0.3951 | 0.0158 | 0.1468 | 0.1494 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 14494 | 0.1769 | 0.5281 | 0.0261 | 0.3120 | 0.3107 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 8110 | 0.1911 | 0.5671 | 0.0367 | 0.4195 | 0.4266 |
| team_total | MARKET_BASELINE | 8110 | 0.1910 | 0.5678 | 0.0595 | 0.4245 | 0.4266 |
| team_total | MARKET_ANCHORED_V1 | 8110 | 0.1907 | 0.5670 | 0.0520 | 0.4234 | 0.4266 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
