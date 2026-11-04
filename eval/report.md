# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-04T04:37:07Z · rows 843848 · pregame 843848 · new 2801

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 138500 | 0.1662 | 0.5007 | 0.0211 | 0.4499 | 0.4710 |
| ALL | MARKET_BASELINE | 727285 | 0.1435 | 0.4434 | 0.0118 | 0.2725 | 0.2827 |
| ALL | MARKET_ANCHORED_V1 | 138467 | 0.1637 | 0.4941 | 0.0144 | 0.4567 | 0.4711 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 53765 | 0.0336 | 0.1469 | 0.0016 | 0.0342 | 0.0350 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 22160 | 0.1837 | 0.5516 | 0.0264 | 0.2314 | 0.2569 |
| game_spread | MARKET_BASELINE | 22160 | 0.1791 | 0.5392 | 0.0213 | 0.2436 | 0.2569 |
| game_spread | MARKET_ANCHORED_V1 | 22160 | 0.1797 | 0.5407 | 0.0184 | 0.2407 | 0.2569 |
| game_total | DATA_ONLY_V1 | 49860 | 0.1303 | 0.4054 | 0.0282 | 0.5686 | 0.5925 |
| game_total | MARKET_BASELINE | 49860 | 0.1285 | 0.4005 | 0.0224 | 0.5780 | 0.5925 |
| game_total | MARKET_ANCHORED_V1 | 49860 | 0.1287 | 0.4010 | 0.0232 | 0.5761 | 0.5925 |
| game_winner | DATA_ONLY_V1 | 11080 | 0.2336 | 0.6597 | 0.0675 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 11080 | 0.2293 | 0.6500 | 0.0259 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 11080 | 0.2295 | 0.6508 | 0.0279 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 3250 | 0.2480 | 0.6897 | 0.0339 | 0.4464 | 0.4375 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 31688 | 0.1330 | 0.4366 | 0.0306 | 0.1288 | 0.1590 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 49641 | 0.1779 | 0.5309 | 0.0282 | 0.5996 | 0.6256 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 49689 | 0.2171 | 0.6248 | 0.0211 | 0.3284 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 103725 | 0.1581 | 0.4834 | 0.0184 | 0.2296 | 0.2380 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 160681 | 0.1009 | 0.3371 | 0.0088 | 0.1190 | 0.1258 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 136379 | 0.1665 | 0.5022 | 0.0139 | 0.2811 | 0.2899 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 55400 | 0.1782 | 0.5342 | 0.0233 | 0.4204 | 0.4415 |
| team_total | MARKET_BASELINE | 55367 | 0.1754 | 0.5274 | 0.0175 | 0.4288 | 0.4417 |
| team_total | MARKET_ANCHORED_V1 | 55367 | 0.1757 | 0.5280 | 0.0180 | 0.4271 | 0.4417 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
