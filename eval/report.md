# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-10T11:29:09Z · rows 195389 · pregame 195389 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 36525 | 0.1674 | 0.5034 | 0.0139 | 0.4505 | 0.4607 |
| ALL | MARKET_BASELINE | 166563 | 0.1497 | 0.4604 | 0.0104 | 0.2910 | 0.2962 |
| ALL | MARKET_ANCHORED_V1 | 36511 | 0.1646 | 0.4960 | 0.0120 | 0.4534 | 0.4608 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 9119 | 0.0392 | 0.1693 | 0.0056 | 0.0374 | 0.0408 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 5844 | 0.1850 | 0.5526 | 0.0405 | 0.2314 | 0.2654 |
| game_spread | MARKET_BASELINE | 5844 | 0.1794 | 0.5386 | 0.0410 | 0.2413 | 0.2654 |
| game_spread | MARKET_ANCHORED_V1 | 5844 | 0.1801 | 0.5404 | 0.0327 | 0.2389 | 0.2654 |
| game_total | DATA_ONLY_V1 | 13149 | 0.1272 | 0.3983 | 0.0235 | 0.5695 | 0.5734 |
| game_total | MARKET_BASELINE | 13149 | 0.1248 | 0.3908 | 0.0263 | 0.5724 | 0.5734 |
| game_total | MARKET_ANCHORED_V1 | 13149 | 0.1251 | 0.3919 | 0.0255 | 0.5718 | 0.5734 |
| game_winner | DATA_ONLY_V1 | 2922 | 0.2317 | 0.6557 | 0.0717 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2922 | 0.2290 | 0.6495 | 0.0669 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2922 | 0.2289 | 0.6495 | 0.0411 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 636 | 0.2525 | 0.6990 | 0.0670 | 0.4170 | 0.4450 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 8332 | 0.1509 | 0.4820 | 0.0547 | 0.1309 | 0.1839 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 12960 | 0.1807 | 0.5387 | 0.0313 | 0.5950 | 0.6131 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 12978 | 0.2167 | 0.6242 | 0.0265 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 22005 | 0.1545 | 0.4745 | 0.0181 | 0.2354 | 0.2314 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 36857 | 0.1081 | 0.3589 | 0.0096 | 0.1300 | 0.1343 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 27165 | 0.1700 | 0.5102 | 0.0198 | 0.3036 | 0.2946 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 14610 | 0.1835 | 0.5477 | 0.0281 | 0.4211 | 0.4294 |
| team_total | MARKET_BASELINE | 14596 | 0.1807 | 0.5404 | 0.0330 | 0.4241 | 0.4298 |
| team_total | MARKET_ANCHORED_V1 | 14596 | 0.1810 | 0.5412 | 0.0305 | 0.4235 | 0.4298 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
