# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-26T02:06:31Z · rows 592276 · pregame 592276 · new 12246

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 100775 | 0.1645 | 0.4960 | 0.0194 | 0.4487 | 0.4656 |
| ALL | MARKET_BASELINE | 493198 | 0.1475 | 0.4538 | 0.0090 | 0.2841 | 0.2919 |
| ALL | MARKET_ANCHORED_V1 | 100750 | 0.1623 | 0.4903 | 0.0151 | 0.4552 | 0.4657 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 25532 | 0.0384 | 0.1651 | 0.0027 | 0.0382 | 0.0402 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 16124 | 0.1838 | 0.5515 | 0.0280 | 0.2310 | 0.2571 |
| game_spread | MARKET_BASELINE | 16124 | 0.1794 | 0.5392 | 0.0207 | 0.2425 | 0.2571 |
| game_spread | MARKET_ANCHORED_V1 | 16124 | 0.1799 | 0.5407 | 0.0214 | 0.2397 | 0.2571 |
| game_total | DATA_ONLY_V1 | 36279 | 0.1278 | 0.3991 | 0.0266 | 0.5670 | 0.5862 |
| game_total | MARKET_BASELINE | 36279 | 0.1267 | 0.3957 | 0.0278 | 0.5759 | 0.5862 |
| game_total | MARKET_ANCHORED_V1 | 36279 | 0.1267 | 0.3959 | 0.0261 | 0.5742 | 0.5862 |
| game_winner | DATA_ONLY_V1 | 8062 | 0.2319 | 0.6565 | 0.0974 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 8062 | 0.2281 | 0.6478 | 0.0339 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 8062 | 0.2283 | 0.6483 | 0.0469 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2251 | 0.2541 | 0.7022 | 0.0587 | 0.4441 | 0.4625 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 22982 | 0.1359 | 0.4435 | 0.0353 | 0.1287 | 0.1633 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 36090 | 0.1825 | 0.5424 | 0.0256 | 0.5986 | 0.6222 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 36108 | 0.2171 | 0.6250 | 0.0213 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 69971 | 0.1571 | 0.4806 | 0.0132 | 0.2322 | 0.2338 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 108429 | 0.1028 | 0.3418 | 0.0074 | 0.1225 | 0.1286 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 91085 | 0.1666 | 0.5012 | 0.0093 | 0.2872 | 0.2899 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 40310 | 0.1763 | 0.5290 | 0.0162 | 0.4191 | 0.4337 |
| team_total | MARKET_BASELINE | 40285 | 0.1740 | 0.5232 | 0.0175 | 0.4270 | 0.4339 |
| team_total | MARKET_ANCHORED_V1 | 40285 | 0.1742 | 0.5236 | 0.0153 | 0.4253 | 0.4339 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
