# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-27T04:58:59Z · rows 615227 · pregame 615227 · new 4636

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 104225 | 0.1651 | 0.4977 | 0.0208 | 0.4492 | 0.4687 |
| ALL | MARKET_BASELINE | 515427 | 0.1470 | 0.4525 | 0.0098 | 0.2824 | 0.2915 |
| ALL | MARKET_ANCHORED_V1 | 104200 | 0.1630 | 0.4922 | 0.0157 | 0.4558 | 0.4688 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 28279 | 0.0366 | 0.1584 | 0.0016 | 0.0375 | 0.0383 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 16676 | 0.1862 | 0.5579 | 0.0300 | 0.2311 | 0.2598 |
| game_spread | MARKET_BASELINE | 16676 | 0.1824 | 0.5471 | 0.0236 | 0.2429 | 0.2598 |
| game_spread | MARKET_ANCHORED_V1 | 16676 | 0.1828 | 0.5483 | 0.0205 | 0.2400 | 0.2598 |
| game_total | DATA_ONLY_V1 | 37521 | 0.1272 | 0.3973 | 0.0303 | 0.5677 | 0.5900 |
| game_total | MARKET_BASELINE | 37521 | 0.1257 | 0.3932 | 0.0288 | 0.5767 | 0.5900 |
| game_total | MARKET_ANCHORED_V1 | 37521 | 0.1258 | 0.3935 | 0.0272 | 0.5749 | 0.5900 |
| game_winner | DATA_ONLY_V1 | 8338 | 0.2342 | 0.6611 | 0.0888 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 8338 | 0.2310 | 0.6537 | 0.0226 | 0.4992 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 8338 | 0.2310 | 0.6540 | 0.0332 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2359 | 0.2521 | 0.6980 | 0.0447 | 0.4444 | 0.4553 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 23773 | 0.1363 | 0.4458 | 0.0355 | 0.1289 | 0.1633 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 37332 | 0.1812 | 0.5392 | 0.0267 | 0.5992 | 0.6256 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 37350 | 0.2179 | 0.6267 | 0.0158 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 73140 | 0.1576 | 0.4818 | 0.0132 | 0.2318 | 0.2359 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 113694 | 0.1024 | 0.3404 | 0.0086 | 0.1216 | 0.1280 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 95300 | 0.1665 | 0.5016 | 0.0090 | 0.2865 | 0.2912 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 41690 | 0.1770 | 0.5313 | 0.0195 | 0.4196 | 0.4369 |
| team_total | MARKET_BASELINE | 41665 | 0.1749 | 0.5260 | 0.0194 | 0.4277 | 0.4371 |
| team_total | MARKET_ANCHORED_V1 | 41665 | 0.1750 | 0.5263 | 0.0161 | 0.4260 | 0.4371 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
