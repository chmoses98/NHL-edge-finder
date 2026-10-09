# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-09T02:54:33Z · rows 173034 · pregame 173034 · new 3173

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 32750 | 0.1672 | 0.5023 | 0.0096 | 0.4498 | 0.4580 |
| ALL | MARKET_BASELINE | 147371 | 0.1522 | 0.4668 | 0.0098 | 0.2935 | 0.3007 |
| ALL | MARKET_ANCHORED_V1 | 32742 | 0.1652 | 0.4972 | 0.0111 | 0.4531 | 0.4581 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 8303 | 0.0411 | 0.1758 | 0.0081 | 0.0370 | 0.0430 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 5240 | 0.1840 | 0.5497 | 0.0435 | 0.2311 | 0.2677 |
| game_spread | MARKET_BASELINE | 5240 | 0.1802 | 0.5400 | 0.0415 | 0.2414 | 0.2677 |
| game_spread | MARKET_ANCHORED_V1 | 5240 | 0.1806 | 0.5410 | 0.0350 | 0.2389 | 0.2677 |
| game_total | DATA_ONLY_V1 | 11790 | 0.1260 | 0.3951 | 0.0246 | 0.5686 | 0.5674 |
| game_total | MARKET_BASELINE | 11790 | 0.1244 | 0.3901 | 0.0286 | 0.5721 | 0.5674 |
| game_total | MARKET_ANCHORED_V1 | 11790 | 0.1246 | 0.3907 | 0.0281 | 0.5714 | 0.5674 |
| game_winner | DATA_ONLY_V1 | 2620 | 0.2308 | 0.6540 | 0.0870 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2620 | 0.2292 | 0.6500 | 0.0487 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2620 | 0.2289 | 0.6495 | 0.0294 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 565 | 0.2548 | 0.7038 | 0.0759 | 0.4122 | 0.4549 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 7453 | 0.1540 | 0.4899 | 0.0591 | 0.1309 | 0.1881 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 11637 | 0.1828 | 0.5433 | 0.0295 | 0.5944 | 0.6155 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 11665 | 0.2163 | 0.6234 | 0.0303 | 0.3284 | 0.3332 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 19324 | 0.1587 | 0.4858 | 0.0192 | 0.2368 | 0.2381 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 32031 | 0.1102 | 0.3638 | 0.0078 | 0.1335 | 0.1381 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 23651 | 0.1752 | 0.5238 | 0.0220 | 0.3073 | 0.3054 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 13100 | 0.1847 | 0.5495 | 0.0266 | 0.4204 | 0.4273 |
| team_total | MARKET_BASELINE | 13092 | 0.1827 | 0.5447 | 0.0314 | 0.4238 | 0.4275 |
| team_total | MARKET_ANCHORED_V1 | 13092 | 0.1828 | 0.5450 | 0.0308 | 0.4231 | 0.4275 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
