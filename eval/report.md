# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-29T02:37:10Z · rows 670119 · pregame 670119 · new 4135

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 112275 | 0.1663 | 0.5009 | 0.0150 | 0.4490 | 0.4623 |
| ALL | MARKET_BASELINE | 568613 | 0.1449 | 0.4468 | 0.0081 | 0.2781 | 0.2835 |
| ALL | MARKET_ANCHORED_V1 | 112250 | 0.1643 | 0.4958 | 0.0114 | 0.4558 | 0.4624 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 35082 | 0.0354 | 0.1539 | 0.0017 | 0.0361 | 0.0370 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 17964 | 0.1848 | 0.5544 | 0.0279 | 0.2310 | 0.2577 |
| game_spread | MARKET_BASELINE | 17964 | 0.1807 | 0.5429 | 0.0187 | 0.2429 | 0.2577 |
| game_spread | MARKET_ANCHORED_V1 | 17964 | 0.1812 | 0.5443 | 0.0186 | 0.2400 | 0.2577 |
| game_total | DATA_ONLY_V1 | 40419 | 0.1300 | 0.4054 | 0.0232 | 0.5674 | 0.5807 |
| game_total | MARKET_BASELINE | 40419 | 0.1289 | 0.4028 | 0.0225 | 0.5768 | 0.5807 |
| game_total | MARKET_ANCHORED_V1 | 40419 | 0.1290 | 0.4028 | 0.0198 | 0.5750 | 0.5807 |
| game_winner | DATA_ONLY_V1 | 8982 | 0.2357 | 0.6640 | 0.0755 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 8982 | 0.2314 | 0.6545 | 0.0217 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 8982 | 0.2316 | 0.6553 | 0.0292 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2609 | 0.2503 | 0.6944 | 0.0349 | 0.4456 | 0.4492 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 25693 | 0.1336 | 0.4388 | 0.0314 | 0.1287 | 0.1595 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 40230 | 0.1826 | 0.5422 | 0.0213 | 0.5994 | 0.6169 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 40248 | 0.2170 | 0.6248 | 0.0223 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 80900 | 0.1557 | 0.4773 | 0.0133 | 0.2305 | 0.2316 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 125662 | 0.0996 | 0.3327 | 0.0062 | 0.1199 | 0.1240 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 105939 | 0.1644 | 0.4964 | 0.0078 | 0.2832 | 0.2847 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 44910 | 0.1778 | 0.5329 | 0.0167 | 0.4194 | 0.4301 |
| team_total | MARKET_BASELINE | 44885 | 0.1758 | 0.5280 | 0.0174 | 0.4278 | 0.4303 |
| team_total | MARKET_ANCHORED_V1 | 44885 | 0.1759 | 0.5283 | 0.0146 | 0.4261 | 0.4303 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
