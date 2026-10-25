# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-25T10:10:01Z · rows 580030 · pregame 580030 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 99050 | 0.1643 | 0.4953 | 0.0199 | 0.4492 | 0.4668 |
| ALL | MARKET_BASELINE | 481770 | 0.1480 | 0.4552 | 0.0091 | 0.2853 | 0.2932 |
| ALL | MARKET_ANCHORED_V1 | 99025 | 0.1622 | 0.4899 | 0.0162 | 0.4555 | 0.4669 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 24125 | 0.0388 | 0.1663 | 0.0029 | 0.0386 | 0.0407 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 15848 | 0.1846 | 0.5534 | 0.0293 | 0.2312 | 0.2586 |
| game_spread | MARKET_BASELINE | 15848 | 0.1804 | 0.5416 | 0.0227 | 0.2426 | 0.2586 |
| game_spread | MARKET_ANCHORED_V1 | 15848 | 0.1809 | 0.5430 | 0.0225 | 0.2399 | 0.2586 |
| game_total | DATA_ONLY_V1 | 35658 | 0.1268 | 0.3966 | 0.0297 | 0.5678 | 0.5875 |
| game_total | MARKET_BASELINE | 35658 | 0.1256 | 0.3932 | 0.0295 | 0.5764 | 0.5875 |
| game_total | MARKET_ANCHORED_V1 | 35658 | 0.1257 | 0.3934 | 0.0283 | 0.5747 | 0.5875 |
| game_winner | DATA_ONLY_V1 | 7924 | 0.2322 | 0.6570 | 0.0913 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 7924 | 0.2291 | 0.6498 | 0.0273 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 7924 | 0.2291 | 0.6501 | 0.0404 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2218 | 0.2533 | 0.7002 | 0.0568 | 0.4448 | 0.4617 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 22630 | 0.1362 | 0.4447 | 0.0355 | 0.1288 | 0.1636 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 35469 | 0.1818 | 0.5410 | 0.0260 | 0.5989 | 0.6221 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 35487 | 0.2173 | 0.6254 | 0.0206 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 68305 | 0.1571 | 0.4805 | 0.0148 | 0.2325 | 0.2340 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 105609 | 0.1032 | 0.3433 | 0.0076 | 0.1232 | 0.1292 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 88902 | 0.1672 | 0.5030 | 0.0086 | 0.2878 | 0.2903 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 39620 | 0.1763 | 0.5286 | 0.0168 | 0.4197 | 0.4350 |
| team_total | MARKET_BASELINE | 39595 | 0.1740 | 0.5232 | 0.0183 | 0.4273 | 0.4352 |
| team_total | MARKET_ANCHORED_V1 | 39595 | 0.1742 | 0.5236 | 0.0167 | 0.4257 | 0.4352 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
