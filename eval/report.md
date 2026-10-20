# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-20T02:11:15Z · rows 411264 · pregame 411264 · new 6749

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 73200 | 0.1617 | 0.4896 | 0.0159 | 0.4493 | 0.4582 |
| ALL | MARKET_BASELINE | 338528 | 0.1484 | 0.4568 | 0.0080 | 0.2921 | 0.2957 |
| ALL | MARKET_ANCHORED_V1 | 73182 | 0.1599 | 0.4850 | 0.0149 | 0.4542 | 0.4583 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 15137 | 0.0386 | 0.1661 | 0.0022 | 0.0401 | 0.0402 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 11712 | 0.1821 | 0.5459 | 0.0325 | 0.2314 | 0.2592 |
| game_spread | MARKET_BASELINE | 11712 | 0.1787 | 0.5368 | 0.0292 | 0.2425 | 0.2592 |
| game_spread | MARKET_ANCHORED_V1 | 11712 | 0.1790 | 0.5376 | 0.0236 | 0.2398 | 0.2592 |
| game_total | DATA_ONLY_V1 | 26352 | 0.1250 | 0.3942 | 0.0268 | 0.5678 | 0.5754 |
| game_total | MARKET_BASELINE | 26352 | 0.1238 | 0.3912 | 0.0324 | 0.5742 | 0.5754 |
| game_total | MARKET_ANCHORED_V1 | 26352 | 0.1239 | 0.3914 | 0.0311 | 0.5729 | 0.5754 |
| game_winner | DATA_ONLY_V1 | 5856 | 0.2288 | 0.6500 | 0.1107 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5856 | 0.2266 | 0.6444 | 0.0449 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5856 | 0.2264 | 0.6443 | 0.0451 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1489 | 0.2479 | 0.6893 | 0.0542 | 0.4377 | 0.4204 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 16782 | 0.1362 | 0.4432 | 0.0357 | 0.1293 | 0.1642 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 26163 | 0.1826 | 0.5427 | 0.0280 | 0.5968 | 0.6176 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 26181 | 0.2167 | 0.6240 | 0.0219 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 45853 | 0.1566 | 0.4797 | 0.0191 | 0.2380 | 0.2339 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 74544 | 0.1040 | 0.3463 | 0.0101 | 0.1262 | 0.1294 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 59197 | 0.1677 | 0.5042 | 0.0135 | 0.2975 | 0.2924 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 29280 | 0.1731 | 0.5208 | 0.0123 | 0.4196 | 0.4239 |
| team_total | MARKET_BASELINE | 29262 | 0.1713 | 0.5163 | 0.0151 | 0.4252 | 0.4242 |
| team_total | MARKET_ANCHORED_V1 | 29262 | 0.1714 | 0.5165 | 0.0140 | 0.4240 | 0.4242 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
