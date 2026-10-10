# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-10T22:47:14Z · rows 200777 · pregame 200777 · new 2994

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 37300 | 0.1670 | 0.5022 | 0.0133 | 0.4503 | 0.4602 |
| ALL | MARKET_BASELINE | 170830 | 0.1494 | 0.4598 | 0.0102 | 0.2905 | 0.2956 |
| ALL | MARKET_ANCHORED_V1 | 37286 | 0.1641 | 0.4946 | 0.0122 | 0.4533 | 0.4603 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 9244 | 0.0394 | 0.1701 | 0.0057 | 0.0376 | 0.0411 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 5968 | 0.1863 | 0.5550 | 0.0457 | 0.2315 | 0.2703 |
| game_spread | MARKET_BASELINE | 5968 | 0.1803 | 0.5402 | 0.0390 | 0.2414 | 0.2703 |
| game_spread | MARKET_ANCHORED_V1 | 5968 | 0.1811 | 0.5422 | 0.0378 | 0.2390 | 0.2703 |
| game_total | DATA_ONLY_V1 | 13428 | 0.1262 | 0.3958 | 0.0264 | 0.5692 | 0.5718 |
| game_total | MARKET_BASELINE | 13428 | 0.1237 | 0.3882 | 0.0286 | 0.5723 | 0.5718 |
| game_total | MARKET_ANCHORED_V1 | 13428 | 0.1241 | 0.3893 | 0.0276 | 0.5717 | 0.5718 |
| game_winner | DATA_ONLY_V1 | 2984 | 0.2300 | 0.6523 | 0.0782 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2984 | 0.2270 | 0.6452 | 0.0646 | 0.4992 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2984 | 0.2269 | 0.6454 | 0.0396 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 640 | 0.2525 | 0.6990 | 0.0682 | 0.4176 | 0.4437 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 8502 | 0.1506 | 0.4807 | 0.0545 | 0.1310 | 0.1838 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 13239 | 0.1815 | 0.5407 | 0.0307 | 0.5948 | 0.6119 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 13257 | 0.2163 | 0.6233 | 0.0288 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 22685 | 0.1542 | 0.4739 | 0.0184 | 0.2349 | 0.2317 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 37943 | 0.1081 | 0.3589 | 0.0101 | 0.1297 | 0.1342 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 28034 | 0.1694 | 0.5086 | 0.0184 | 0.3025 | 0.2937 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 14920 | 0.1833 | 0.5468 | 0.0265 | 0.4209 | 0.4277 |
| team_total | MARKET_BASELINE | 14906 | 0.1803 | 0.5393 | 0.0316 | 0.4240 | 0.4280 |
| team_total | MARKET_ANCHORED_V1 | 14906 | 0.1807 | 0.5402 | 0.0293 | 0.4233 | 0.4280 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
