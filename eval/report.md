# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-16T04:13:57Z · rows 342383 · pregame 342383 · new 3391

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 61750 | 0.1639 | 0.4948 | 0.0150 | 0.4493 | 0.4604 |
| ALL | MARKET_BASELINE | 285752 | 0.1486 | 0.4576 | 0.0089 | 0.2908 | 0.2954 |
| ALL | MARKET_ANCHORED_V1 | 61733 | 0.1613 | 0.4881 | 0.0129 | 0.4533 | 0.4605 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 13095 | 0.0400 | 0.1710 | 0.0043 | 0.0396 | 0.0418 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 9880 | 0.1806 | 0.5433 | 0.0251 | 0.2313 | 0.2522 |
| game_spread | MARKET_BASELINE | 9880 | 0.1770 | 0.5339 | 0.0233 | 0.2416 | 0.2522 |
| game_spread | MARKET_ANCHORED_V1 | 9880 | 0.1774 | 0.5348 | 0.0168 | 0.2390 | 0.2522 |
| game_total | DATA_ONLY_V1 | 22230 | 0.1279 | 0.4000 | 0.0193 | 0.5679 | 0.5799 |
| game_total | MARKET_BASELINE | 22230 | 0.1251 | 0.3922 | 0.0272 | 0.5727 | 0.5799 |
| game_total | MARKET_ANCHORED_V1 | 22230 | 0.1255 | 0.3934 | 0.0268 | 0.5718 | 0.5799 |
| game_winner | DATA_ONLY_V1 | 4940 | 0.2306 | 0.6537 | 0.1019 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 4940 | 0.2281 | 0.6477 | 0.0393 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 4940 | 0.2280 | 0.6477 | 0.0378 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1237 | 0.2439 | 0.6814 | 0.0895 | 0.4292 | 0.3840 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 14240 | 0.1393 | 0.4532 | 0.0391 | 0.1294 | 0.1675 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 22041 | 0.1818 | 0.5410 | 0.0263 | 0.5954 | 0.6160 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 22059 | 0.2172 | 0.6252 | 0.0179 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 39236 | 0.1541 | 0.4733 | 0.0166 | 0.2333 | 0.2305 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 62099 | 0.1048 | 0.3485 | 0.0106 | 0.1272 | 0.1303 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 50012 | 0.1675 | 0.5042 | 0.0137 | 0.2946 | 0.2904 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 24700 | 0.1762 | 0.5289 | 0.0184 | 0.4197 | 0.4281 |
| team_total | MARKET_BASELINE | 24683 | 0.1734 | 0.5220 | 0.0159 | 0.4242 | 0.4284 |
| team_total | MARKET_ANCHORED_V1 | 24683 | 0.1737 | 0.5227 | 0.0166 | 0.4232 | 0.4284 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
