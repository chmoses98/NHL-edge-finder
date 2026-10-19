# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-19T13:59:32Z · rows 404515 · pregame 404515 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 72100 | 0.1622 | 0.4909 | 0.0153 | 0.4495 | 0.4585 |
| ALL | MARKET_BASELINE | 333307 | 0.1484 | 0.4569 | 0.0082 | 0.2921 | 0.2957 |
| ALL | MARKET_ANCHORED_V1 | 72082 | 0.1603 | 0.4860 | 0.0146 | 0.4542 | 0.4586 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 14829 | 0.0386 | 0.1661 | 0.0021 | 0.0400 | 0.0402 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 11536 | 0.1824 | 0.5466 | 0.0325 | 0.2314 | 0.2594 |
| game_spread | MARKET_BASELINE | 11536 | 0.1786 | 0.5369 | 0.0307 | 0.2424 | 0.2594 |
| game_spread | MARKET_ANCHORED_V1 | 11536 | 0.1790 | 0.5378 | 0.0236 | 0.2397 | 0.2594 |
| game_total | DATA_ONLY_V1 | 25956 | 0.1258 | 0.3963 | 0.0254 | 0.5681 | 0.5757 |
| game_total | MARKET_BASELINE | 25956 | 0.1246 | 0.3932 | 0.0310 | 0.5741 | 0.5757 |
| game_total | MARKET_ANCHORED_V1 | 25956 | 0.1247 | 0.3933 | 0.0299 | 0.5729 | 0.5757 |
| game_winner | DATA_ONLY_V1 | 5768 | 0.2281 | 0.6485 | 0.1139 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5768 | 0.2251 | 0.6413 | 0.0541 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5768 | 0.2251 | 0.6415 | 0.0476 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1455 | 0.2467 | 0.6869 | 0.0569 | 0.4367 | 0.4192 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 16544 | 0.1369 | 0.4452 | 0.0368 | 0.1293 | 0.1653 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 25767 | 0.1833 | 0.5444 | 0.0280 | 0.5967 | 0.6168 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 25785 | 0.2163 | 0.6232 | 0.0237 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 45167 | 0.1562 | 0.4786 | 0.0193 | 0.2375 | 0.2336 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 73423 | 0.1038 | 0.3456 | 0.0099 | 0.1262 | 0.1294 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 58255 | 0.1675 | 0.5038 | 0.0141 | 0.2971 | 0.2922 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 28840 | 0.1737 | 0.5224 | 0.0139 | 0.4199 | 0.4243 |
| team_total | MARKET_BASELINE | 28822 | 0.1717 | 0.5173 | 0.0165 | 0.4251 | 0.4245 |
| team_total | MARKET_ANCHORED_V1 | 28822 | 0.1718 | 0.5177 | 0.0160 | 0.4240 | 0.4245 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
