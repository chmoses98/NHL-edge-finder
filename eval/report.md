# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-13T22:58:12Z · rows 257514 · pregame 257514 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 46625 | 0.1675 | 0.5043 | 0.0096 | 0.4504 | 0.4531 |
| ALL | MARKET_BASELINE | 214909 | 0.1491 | 0.4587 | 0.0084 | 0.2907 | 0.2916 |
| ALL | MARKET_ANCHORED_V1 | 46611 | 0.1646 | 0.4967 | 0.0094 | 0.4531 | 0.4532 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 10414 | 0.0395 | 0.1693 | 0.0049 | 0.0385 | 0.0413 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 7460 | 0.1886 | 0.5610 | 0.0467 | 0.2317 | 0.2739 |
| game_spread | MARKET_BASELINE | 7460 | 0.1825 | 0.5456 | 0.0387 | 0.2417 | 0.2739 |
| game_spread | MARKET_ANCHORED_V1 | 7460 | 0.1834 | 0.5477 | 0.0377 | 0.2392 | 0.2739 |
| game_total | DATA_ONLY_V1 | 16785 | 0.1288 | 0.4042 | 0.0246 | 0.5693 | 0.5620 |
| game_total | MARKET_BASELINE | 16785 | 0.1263 | 0.3973 | 0.0287 | 0.5719 | 0.5620 |
| game_total | MARKET_ANCHORED_V1 | 16785 | 0.1267 | 0.3983 | 0.0285 | 0.5714 | 0.5620 |
| game_winner | DATA_ONLY_V1 | 3730 | 0.2298 | 0.6521 | 0.1086 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3730 | 0.2263 | 0.6440 | 0.0511 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3730 | 0.2264 | 0.6444 | 0.0420 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 813 | 0.2515 | 0.6973 | 0.0954 | 0.4231 | 0.4108 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 10679 | 0.1480 | 0.4755 | 0.0500 | 0.1305 | 0.1792 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 16596 | 0.1855 | 0.5509 | 0.0243 | 0.5944 | 0.6049 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 16614 | 0.2170 | 0.6248 | 0.0228 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 29154 | 0.1523 | 0.4687 | 0.0205 | 0.2351 | 0.2273 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 47706 | 0.1053 | 0.3496 | 0.0100 | 0.1285 | 0.1306 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 36322 | 0.1665 | 0.5009 | 0.0171 | 0.2997 | 0.2870 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 18650 | 0.1815 | 0.5420 | 0.0309 | 0.4209 | 0.4174 |
| team_total | MARKET_BASELINE | 18636 | 0.1786 | 0.5347 | 0.0293 | 0.4236 | 0.4177 |
| team_total | MARKET_ANCHORED_V1 | 18636 | 0.1789 | 0.5355 | 0.0277 | 0.4230 | 0.4177 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
