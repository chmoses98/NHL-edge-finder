# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-29T04:37:27Z · rows 678974 · pregame 678974 · new 4334

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 113600 | 0.1662 | 0.5006 | 0.0148 | 0.4490 | 0.4623 |
| ALL | MARKET_BASELINE | 577163 | 0.1443 | 0.4454 | 0.0075 | 0.2776 | 0.2822 |
| ALL | MARKET_ANCHORED_V1 | 113575 | 0.1642 | 0.4954 | 0.0113 | 0.4559 | 0.4624 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 36198 | 0.0350 | 0.1526 | 0.0014 | 0.0359 | 0.0365 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 18176 | 0.1858 | 0.5563 | 0.0307 | 0.2310 | 0.2605 |
| game_spread | MARKET_BASELINE | 18176 | 0.1813 | 0.5441 | 0.0203 | 0.2430 | 0.2605 |
| game_spread | MARKET_ANCHORED_V1 | 18176 | 0.1819 | 0.5455 | 0.0215 | 0.2401 | 0.2605 |
| game_total | DATA_ONLY_V1 | 40896 | 0.1297 | 0.4048 | 0.0227 | 0.5675 | 0.5798 |
| game_total | MARKET_BASELINE | 40896 | 0.1288 | 0.4023 | 0.0216 | 0.5770 | 0.5798 |
| game_total | MARKET_ANCHORED_V1 | 40896 | 0.1288 | 0.4023 | 0.0183 | 0.5752 | 0.5798 |
| game_winner | DATA_ONLY_V1 | 9088 | 0.2349 | 0.6626 | 0.0795 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 9088 | 0.2304 | 0.6526 | 0.0233 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 9088 | 0.2307 | 0.6535 | 0.0334 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2656 | 0.2501 | 0.6939 | 0.0342 | 0.4463 | 0.4495 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 25975 | 0.1336 | 0.4383 | 0.0315 | 0.1288 | 0.1598 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 40707 | 0.1822 | 0.5412 | 0.0205 | 0.5996 | 0.6155 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 40725 | 0.2166 | 0.6239 | 0.0240 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 82194 | 0.1550 | 0.4754 | 0.0130 | 0.2303 | 0.2299 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 127493 | 0.0993 | 0.3319 | 0.0065 | 0.1197 | 0.1235 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 107640 | 0.1639 | 0.4952 | 0.0078 | 0.2830 | 0.2828 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 45440 | 0.1775 | 0.5322 | 0.0154 | 0.4194 | 0.4298 |
| team_total | MARKET_BASELINE | 45415 | 0.1754 | 0.5271 | 0.0162 | 0.4280 | 0.4299 |
| team_total | MARKET_ANCHORED_V1 | 45415 | 0.1756 | 0.5274 | 0.0142 | 0.4262 | 0.4299 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
