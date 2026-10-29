# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-29T15:34:05Z · rows 683479 · pregame 683479 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 114325 | 0.1661 | 0.5002 | 0.0155 | 0.4493 | 0.4634 |
| ALL | MARKET_BASELINE | 581427 | 0.1445 | 0.4459 | 0.0079 | 0.2775 | 0.2829 |
| ALL | MARKET_ANCHORED_V1 | 114300 | 0.1641 | 0.4951 | 0.0117 | 0.4561 | 0.4635 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 36753 | 0.0349 | 0.1524 | 0.0014 | 0.0358 | 0.0364 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 18292 | 0.1850 | 0.5546 | 0.0290 | 0.2311 | 0.2589 |
| game_spread | MARKET_BASELINE | 18292 | 0.1806 | 0.5424 | 0.0186 | 0.2430 | 0.2589 |
| game_spread | MARKET_ANCHORED_V1 | 18292 | 0.1811 | 0.5439 | 0.0198 | 0.2401 | 0.2589 |
| game_total | DATA_ONLY_V1 | 41157 | 0.1299 | 0.4050 | 0.0235 | 0.5679 | 0.5818 |
| game_total | MARKET_BASELINE | 41157 | 0.1290 | 0.4027 | 0.0223 | 0.5773 | 0.5818 |
| game_total | MARKET_ANCHORED_V1 | 41157 | 0.1290 | 0.4027 | 0.0201 | 0.5754 | 0.5818 |
| game_winner | DATA_ONLY_V1 | 9146 | 0.2346 | 0.6620 | 0.0817 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 9146 | 0.2308 | 0.6535 | 0.0260 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 9146 | 0.2310 | 0.6540 | 0.0310 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2680 | 0.2504 | 0.6946 | 0.0387 | 0.4470 | 0.4455 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 26134 | 0.1336 | 0.4385 | 0.0314 | 0.1288 | 0.1597 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 40968 | 0.1819 | 0.5405 | 0.0211 | 0.5998 | 0.6172 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 40986 | 0.2166 | 0.6238 | 0.0246 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 82788 | 0.1556 | 0.4772 | 0.0131 | 0.2302 | 0.2313 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 128447 | 0.0996 | 0.3328 | 0.0068 | 0.1197 | 0.1238 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 108371 | 0.1645 | 0.4965 | 0.0086 | 0.2830 | 0.2842 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 45730 | 0.1773 | 0.5317 | 0.0161 | 0.4197 | 0.4315 |
| team_total | MARKET_BASELINE | 45705 | 0.1753 | 0.5268 | 0.0157 | 0.4282 | 0.4317 |
| team_total | MARKET_ANCHORED_V1 | 45705 | 0.1755 | 0.5271 | 0.0139 | 0.4265 | 0.4317 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
