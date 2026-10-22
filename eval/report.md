# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-22T03:38:15Z · rows 463204 · pregame 463204 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 81575 | 0.1611 | 0.4881 | 0.0161 | 0.4488 | 0.4592 |
| ALL | MARKET_BASELINE | 380385 | 0.1479 | 0.4553 | 0.0084 | 0.2916 | 0.2955 |
| ALL | MARKET_ANCHORED_V1 | 81557 | 0.1591 | 0.4829 | 0.0183 | 0.4545 | 0.4593 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 16747 | 0.0392 | 0.1681 | 0.0025 | 0.0404 | 0.0410 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 13052 | 0.1811 | 0.5448 | 0.0237 | 0.2314 | 0.2533 |
| game_spread | MARKET_BASELINE | 13052 | 0.1773 | 0.5346 | 0.0280 | 0.2427 | 0.2533 |
| game_spread | MARKET_ANCHORED_V1 | 13052 | 0.1777 | 0.5357 | 0.0176 | 0.2400 | 0.2533 |
| game_total | DATA_ONLY_V1 | 29367 | 0.1238 | 0.3902 | 0.0284 | 0.5671 | 0.5785 |
| game_total | MARKET_BASELINE | 29367 | 0.1224 | 0.3868 | 0.0306 | 0.5749 | 0.5785 |
| game_total | MARKET_ANCHORED_V1 | 29367 | 0.1225 | 0.3870 | 0.0292 | 0.5734 | 0.5785 |
| game_winner | DATA_ONLY_V1 | 6526 | 0.2307 | 0.6540 | 0.1020 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 6526 | 0.2282 | 0.6476 | 0.0321 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 6526 | 0.2281 | 0.6477 | 0.0439 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1730 | 0.2497 | 0.6929 | 0.0491 | 0.4411 | 0.4353 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 18671 | 0.1363 | 0.4438 | 0.0361 | 0.1290 | 0.1643 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 29178 | 0.1808 | 0.5383 | 0.0276 | 0.5974 | 0.6201 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 29196 | 0.2170 | 0.6247 | 0.0226 | 0.3278 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 52294 | 0.1552 | 0.4758 | 0.0198 | 0.2370 | 0.2320 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 83332 | 0.1034 | 0.3442 | 0.0095 | 0.1259 | 0.1290 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 67680 | 0.1671 | 0.5027 | 0.0144 | 0.2953 | 0.2914 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 32630 | 0.1726 | 0.5202 | 0.0184 | 0.4191 | 0.4260 |
| team_total | MARKET_BASELINE | 32612 | 0.1706 | 0.5149 | 0.0186 | 0.4257 | 0.4263 |
| team_total | MARKET_ANCHORED_V1 | 32612 | 0.1707 | 0.5152 | 0.0206 | 0.4243 | 0.4263 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
