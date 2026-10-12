# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-12T00:04:19Z · rows 243108 · pregame 243108 · new 3261

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 44175 | 0.1690 | 0.5081 | 0.0110 | 0.4507 | 0.4513 |
| ALL | MARKET_BASELINE | 202834 | 0.1496 | 0.4604 | 0.0096 | 0.2916 | 0.2914 |
| ALL | MARKET_ANCHORED_V1 | 44161 | 0.1657 | 0.4998 | 0.0113 | 0.4536 | 0.4514 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 9975 | 0.0397 | 0.1703 | 0.0054 | 0.0382 | 0.0414 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 7068 | 0.1867 | 0.5574 | 0.0388 | 0.2316 | 0.2664 |
| game_spread | MARKET_BASELINE | 7068 | 0.1804 | 0.5413 | 0.0345 | 0.2417 | 0.2664 |
| game_spread | MARKET_ANCHORED_V1 | 7068 | 0.1813 | 0.5435 | 0.0300 | 0.2392 | 0.2664 |
| game_total | DATA_ONLY_V1 | 15903 | 0.1313 | 0.4106 | 0.0219 | 0.5698 | 0.5608 |
| game_total | MARKET_BASELINE | 15903 | 0.1284 | 0.4027 | 0.0265 | 0.5726 | 0.5608 |
| game_total | MARKET_ANCHORED_V1 | 15903 | 0.1289 | 0.4039 | 0.0274 | 0.5721 | 0.5608 |
| game_winner | DATA_ONLY_V1 | 3534 | 0.2323 | 0.6574 | 0.1039 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3534 | 0.2280 | 0.6474 | 0.0416 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3534 | 0.2282 | 0.6482 | 0.0346 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 754 | 0.2537 | 0.7019 | 0.0862 | 0.4212 | 0.4310 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 10095 | 0.1488 | 0.4780 | 0.0507 | 0.1306 | 0.1799 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 15714 | 0.1850 | 0.5499 | 0.0224 | 0.5950 | 0.6011 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 15732 | 0.2177 | 0.6264 | 0.0193 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 27411 | 0.1525 | 0.4695 | 0.0199 | 0.2360 | 0.2271 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 44963 | 0.1059 | 0.3521 | 0.0103 | 0.1294 | 0.1312 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 34029 | 0.1672 | 0.5031 | 0.0176 | 0.3014 | 0.2880 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 17670 | 0.1831 | 0.5463 | 0.0333 | 0.4214 | 0.4169 |
| team_total | MARKET_BASELINE | 17656 | 0.1798 | 0.5379 | 0.0291 | 0.4242 | 0.4172 |
| team_total | MARKET_ANCHORED_V1 | 17656 | 0.1802 | 0.5389 | 0.0278 | 0.4236 | 0.4172 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
