# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-18T21:59:14Z · rows 397935 · pregame 397935 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 71075 | 0.1626 | 0.4920 | 0.0172 | 0.4497 | 0.4616 |
| ALL | MARKET_BASELINE | 328182 | 0.1486 | 0.4574 | 0.0088 | 0.2921 | 0.2973 |
| ALL | MARKET_ANCHORED_V1 | 71057 | 0.1604 | 0.4865 | 0.0149 | 0.4541 | 0.4617 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 14566 | 0.0391 | 0.1679 | 0.0027 | 0.0400 | 0.0408 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 11372 | 0.1841 | 0.5505 | 0.0360 | 0.2314 | 0.2631 |
| game_spread | MARKET_BASELINE | 11372 | 0.1801 | 0.5403 | 0.0332 | 0.2423 | 0.2631 |
| game_spread | MARKET_ANCHORED_V1 | 11372 | 0.1805 | 0.5413 | 0.0273 | 0.2396 | 0.2631 |
| game_total | DATA_ONLY_V1 | 25587 | 0.1257 | 0.3961 | 0.0258 | 0.5683 | 0.5791 |
| game_total | MARKET_BASELINE | 25587 | 0.1242 | 0.3923 | 0.0298 | 0.5740 | 0.5791 |
| game_total | MARKET_ANCHORED_V1 | 25587 | 0.1244 | 0.3926 | 0.0287 | 0.5729 | 0.5791 |
| game_winner | DATA_ONLY_V1 | 5686 | 0.2277 | 0.6478 | 0.1176 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5686 | 0.2241 | 0.6390 | 0.0575 | 0.4990 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5686 | 0.2242 | 0.6396 | 0.0509 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1422 | 0.2464 | 0.6864 | 0.0646 | 0.4357 | 0.4114 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 16319 | 0.1385 | 0.4493 | 0.0391 | 0.1293 | 0.1675 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 25398 | 0.1824 | 0.5420 | 0.0305 | 0.5966 | 0.6200 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 25416 | 0.2160 | 0.6225 | 0.0245 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 44495 | 0.1563 | 0.4788 | 0.0191 | 0.2371 | 0.2344 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 72319 | 0.1041 | 0.3464 | 0.0098 | 0.1263 | 0.1299 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 57190 | 0.1679 | 0.5051 | 0.0137 | 0.2973 | 0.2939 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 28430 | 0.1742 | 0.5238 | 0.0138 | 0.4201 | 0.4274 |
| team_total | MARKET_BASELINE | 28412 | 0.1719 | 0.5180 | 0.0180 | 0.4251 | 0.4277 |
| team_total | MARKET_ANCHORED_V1 | 28412 | 0.1721 | 0.5185 | 0.0172 | 0.4240 | 0.4277 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
