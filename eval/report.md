# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-08T02:34:57Z · rows 150607 · pregame 150607 · new 6391

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 28450 | 0.1668 | 0.5020 | 0.0112 | 0.4491 | 0.4590 |
| ALL | MARKET_BASELINE | 127985 | 0.1530 | 0.4693 | 0.0104 | 0.2957 | 0.3027 |
| ALL | MARKET_ANCHORED_V1 | 28450 | 0.1651 | 0.4975 | 0.0094 | 0.4527 | 0.4590 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 7285 | 0.0400 | 0.1720 | 0.0075 | 0.0365 | 0.0417 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 4552 | 0.1744 | 0.5266 | 0.0274 | 0.2308 | 0.2511 |
| game_spread | MARKET_BASELINE | 4552 | 0.1723 | 0.5215 | 0.0251 | 0.2409 | 0.2511 |
| game_spread | MARKET_ANCHORED_V1 | 4552 | 0.1723 | 0.5215 | 0.0305 | 0.2384 | 0.2511 |
| game_total | DATA_ONLY_V1 | 10242 | 0.1291 | 0.4033 | 0.0254 | 0.5676 | 0.5711 |
| game_total | MARKET_BASELINE | 10242 | 0.1269 | 0.3971 | 0.0272 | 0.5718 | 0.5711 |
| game_total | MARKET_ANCHORED_V1 | 10242 | 0.1272 | 0.3979 | 0.0262 | 0.5710 | 0.5711 |
| game_winner | DATA_ONLY_V1 | 2276 | 0.2323 | 0.6570 | 0.0724 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2276 | 0.2328 | 0.6576 | 0.0726 | 0.4995 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2276 | 0.2321 | 0.6562 | 0.0402 | 0.4996 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 481 | 0.2546 | 0.7030 | 0.0831 | 0.4006 | 0.4553 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 6498 | 0.1509 | 0.4819 | 0.0558 | 0.1304 | 0.1841 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 10187 | 0.1792 | 0.5337 | 0.0309 | 0.5938 | 0.6178 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 10230 | 0.2156 | 0.6216 | 0.0351 | 0.3283 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 17117 | 0.1579 | 0.4826 | 0.0152 | 0.2367 | 0.2363 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 26935 | 0.1154 | 0.3788 | 0.0082 | 0.1395 | 0.1452 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 20802 | 0.1758 | 0.5257 | 0.0196 | 0.3086 | 0.3030 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 11380 | 0.1845 | 0.5500 | 0.0238 | 0.4196 | 0.4331 |
| team_total | MARKET_BASELINE | 11380 | 0.1828 | 0.5456 | 0.0297 | 0.4234 | 0.4331 |
| team_total | MARKET_ANCHORED_V1 | 11380 | 0.1829 | 0.5458 | 0.0273 | 0.4225 | 0.4331 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
