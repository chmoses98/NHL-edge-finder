# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-07T22:29:17Z · rows 144216 · pregame 144216 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 27400 | 0.1688 | 0.5069 | 0.0116 | 0.4488 | 0.4590 |
| ALL | MARKET_BASELINE | 122628 | 0.1539 | 0.4719 | 0.0120 | 0.2963 | 0.3048 |
| ALL | MARKET_ANCHORED_V1 | 27400 | 0.1666 | 0.5015 | 0.0108 | 0.4520 | 0.4590 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 6919 | 0.0411 | 0.1757 | 0.0088 | 0.0364 | 0.0429 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 4384 | 0.1775 | 0.5339 | 0.0326 | 0.2307 | 0.2559 |
| game_spread | MARKET_BASELINE | 4384 | 0.1750 | 0.5279 | 0.0353 | 0.2407 | 0.2559 |
| game_spread | MARKET_ANCHORED_V1 | 4384 | 0.1750 | 0.5280 | 0.0323 | 0.2382 | 0.2559 |
| game_total | DATA_ONLY_V1 | 9864 | 0.1306 | 0.4071 | 0.0259 | 0.5672 | 0.5695 |
| game_total | MARKET_BASELINE | 9864 | 0.1279 | 0.4000 | 0.0233 | 0.5708 | 0.5695 |
| game_total | MARKET_ANCHORED_V1 | 9864 | 0.1283 | 0.4010 | 0.0223 | 0.5701 | 0.5695 |
| game_winner | DATA_ONLY_V1 | 2192 | 0.2316 | 0.6558 | 0.0783 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2192 | 0.2307 | 0.6532 | 0.0956 | 0.4995 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2192 | 0.2302 | 0.6524 | 0.0617 | 0.4996 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 465 | 0.2549 | 0.7037 | 0.0853 | 0.3974 | 0.4710 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 6258 | 0.1559 | 0.4946 | 0.0632 | 0.1301 | 0.1911 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 9809 | 0.1777 | 0.5306 | 0.0319 | 0.5930 | 0.6160 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 9852 | 0.2151 | 0.6205 | 0.0388 | 0.3283 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 16389 | 0.1585 | 0.4839 | 0.0140 | 0.2365 | 0.2397 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 25660 | 0.1161 | 0.3815 | 0.0086 | 0.1405 | 0.1458 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 19876 | 0.1760 | 0.5265 | 0.0219 | 0.3087 | 0.3062 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 10960 | 0.1871 | 0.5562 | 0.0289 | 0.4192 | 0.4325 |
| team_total | MARKET_BASELINE | 10960 | 0.1848 | 0.5507 | 0.0338 | 0.4225 | 0.4325 |
| team_total | MARKET_ANCHORED_V1 | 10960 | 0.1850 | 0.5511 | 0.0324 | 0.4218 | 0.4325 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
