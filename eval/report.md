# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-21T03:58:53Z · rows 442036 · pregame 442036 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 78075 | 0.1610 | 0.4881 | 0.0161 | 0.4490 | 0.4565 |
| ALL | MARKET_BASELINE | 362541 | 0.1481 | 0.4561 | 0.0081 | 0.2922 | 0.2950 |
| ALL | MARKET_ANCHORED_V1 | 78057 | 0.1591 | 0.4831 | 0.0179 | 0.4544 | 0.4566 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 16006 | 0.0389 | 0.1675 | 0.0023 | 0.0403 | 0.0406 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 12492 | 0.1801 | 0.5426 | 0.0219 | 0.2314 | 0.2515 |
| game_spread | MARKET_BASELINE | 12492 | 0.1766 | 0.5330 | 0.0267 | 0.2426 | 0.2515 |
| game_spread | MARKET_ANCHORED_V1 | 12492 | 0.1770 | 0.5339 | 0.0157 | 0.2399 | 0.2515 |
| game_total | DATA_ONLY_V1 | 28107 | 0.1245 | 0.3923 | 0.0263 | 0.5674 | 0.5751 |
| game_total | MARKET_BASELINE | 28107 | 0.1231 | 0.3889 | 0.0324 | 0.5747 | 0.5751 |
| game_total | MARKET_ANCHORED_V1 | 28107 | 0.1232 | 0.3891 | 0.0302 | 0.5733 | 0.5751 |
| game_winner | DATA_ONLY_V1 | 6246 | 0.2308 | 0.6541 | 0.1029 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 6246 | 0.2277 | 0.6468 | 0.0403 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 6246 | 0.2277 | 0.6471 | 0.0440 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1640 | 0.2485 | 0.6905 | 0.0381 | 0.4399 | 0.4317 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 17880 | 0.1336 | 0.4368 | 0.0324 | 0.1290 | 0.1606 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 27918 | 0.1824 | 0.5422 | 0.0258 | 0.5973 | 0.6169 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 27936 | 0.2171 | 0.6250 | 0.0218 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 49469 | 0.1561 | 0.4782 | 0.0188 | 0.2380 | 0.2334 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 79589 | 0.1039 | 0.3460 | 0.0104 | 0.1263 | 0.1294 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 64046 | 0.1675 | 0.5036 | 0.0135 | 0.2968 | 0.2917 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 31230 | 0.1724 | 0.5194 | 0.0175 | 0.4193 | 0.4232 |
| team_total | MARKET_BASELINE | 31212 | 0.1703 | 0.5141 | 0.0200 | 0.4256 | 0.4234 |
| team_total | MARKET_ANCHORED_V1 | 31212 | 0.1705 | 0.5145 | 0.0205 | 0.4243 | 0.4234 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
