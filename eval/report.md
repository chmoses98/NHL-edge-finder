# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-11T01:09:57Z · rows 206874 · pregame 206874 · new 3141

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 38250 | 0.1671 | 0.5025 | 0.0113 | 0.4509 | 0.4573 |
| ALL | MARKET_BASELINE | 175552 | 0.1490 | 0.4587 | 0.0098 | 0.2905 | 0.2935 |
| ALL | MARKET_ANCHORED_V1 | 38236 | 0.1643 | 0.4951 | 0.0106 | 0.4536 | 0.4574 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 9384 | 0.0398 | 0.1711 | 0.0061 | 0.0378 | 0.0416 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 6120 | 0.1874 | 0.5574 | 0.0482 | 0.2316 | 0.2730 |
| game_spread | MARKET_BASELINE | 6120 | 0.1821 | 0.5446 | 0.0399 | 0.2414 | 0.2730 |
| game_spread | MARKET_ANCHORED_V1 | 6120 | 0.1828 | 0.5462 | 0.0404 | 0.2389 | 0.2730 |
| game_total | DATA_ONLY_V1 | 13770 | 0.1263 | 0.3959 | 0.0290 | 0.5701 | 0.5673 |
| game_total | MARKET_BASELINE | 13770 | 0.1235 | 0.3876 | 0.0300 | 0.5725 | 0.5673 |
| game_total | MARKET_ANCHORED_V1 | 13770 | 0.1240 | 0.3889 | 0.0298 | 0.5720 | 0.5673 |
| game_winner | DATA_ONLY_V1 | 3060 | 0.2298 | 0.6519 | 0.0880 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3060 | 0.2273 | 0.6459 | 0.0654 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3060 | 0.2271 | 0.6458 | 0.0407 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 656 | 0.2524 | 0.6989 | 0.0656 | 0.4183 | 0.4451 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 8694 | 0.1491 | 0.4773 | 0.0521 | 0.1310 | 0.1815 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 13581 | 0.1816 | 0.5412 | 0.0288 | 0.5949 | 0.6092 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 13599 | 0.2165 | 0.6237 | 0.0268 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 23444 | 0.1524 | 0.4694 | 0.0197 | 0.2348 | 0.2289 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 38924 | 0.1075 | 0.3572 | 0.0096 | 0.1298 | 0.1332 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 29034 | 0.1683 | 0.5056 | 0.0194 | 0.3017 | 0.2901 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 15300 | 0.1832 | 0.5465 | 0.0249 | 0.4216 | 0.4233 |
| team_total | MARKET_BASELINE | 15286 | 0.1805 | 0.5394 | 0.0324 | 0.4242 | 0.4237 |
| team_total | MARKET_ANCHORED_V1 | 15286 | 0.1808 | 0.5402 | 0.0324 | 0.4236 | 0.4237 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
