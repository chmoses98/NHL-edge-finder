# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-03T03:34:29Z · rows 52577 · pregame 52577 · new 2686

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 9525 | 0.1947 | 0.5761 | 0.0658 | 0.4434 | 0.4890 |
| ALL | MARKET_BASELINE | 45222 | 0.1590 | 0.4843 | 0.0217 | 0.2885 | 0.3027 |
| ALL | MARKET_ANCHORED_V1 | 9525 | 0.1919 | 0.5689 | 0.0528 | 0.4511 | 0.4890 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 3101 | 0.0301 | 0.1381 | 0.0024 | 0.0334 | 0.0310 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 1524 | 0.1985 | 0.5839 | 0.0729 | 0.2289 | 0.2900 |
| game_spread | MARKET_BASELINE | 1524 | 0.1959 | 0.5780 | 0.1162 | 0.2412 | 0.2900 |
| game_spread | MARKET_ANCHORED_V1 | 1524 | 0.1960 | 0.5782 | 0.1062 | 0.2383 | 0.2900 |
| game_total | DATA_ONLY_V1 | 3429 | 0.1575 | 0.4848 | 0.0606 | 0.5600 | 0.5955 |
| game_total | MARKET_BASELINE | 3429 | 0.1518 | 0.4690 | 0.0543 | 0.5705 | 0.5955 |
| game_total | MARKET_ANCHORED_V1 | 3429 | 0.1528 | 0.4717 | 0.0570 | 0.5685 | 0.5955 |
| game_winner | DATA_ONLY_V1 | 762 | 0.2390 | 0.6710 | 0.0840 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 762 | 0.2413 | 0.6755 | 0.3251 | 0.4999 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 762 | 0.2403 | 0.6735 | 0.2866 | 0.4999 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 195 | 0.2631 | 0.7208 | 0.1253 | 0.3847 | 0.4821 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 2180 | 0.1599 | 0.5081 | 0.0844 | 0.1290 | 0.1922 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 3414 | 0.1920 | 0.5638 | 0.0526 | 0.5925 | 0.6415 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 3417 | 0.2147 | 0.6194 | 0.0515 | 0.3284 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 6379 | 0.1551 | 0.4745 | 0.0398 | 0.2301 | 0.2226 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 9359 | 0.1207 | 0.3957 | 0.0248 | 0.1385 | 0.1487 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 7652 | 0.1785 | 0.5286 | 0.0500 | 0.3086 | 0.2978 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 3810 | 0.2178 | 0.6362 | 0.0944 | 0.4130 | 0.4706 |
| team_total | MARKET_BASELINE | 3810 | 0.2156 | 0.6315 | 0.1351 | 0.4228 | 0.4706 |
| team_total | MARKET_ANCHORED_V1 | 3810 | 0.2158 | 0.6317 | 0.1210 | 0.4208 | 0.4706 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
