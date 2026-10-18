# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-18T04:17:22Z · rows 390756 · pregame 390756 · new 3476

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 69775 | 0.1619 | 0.4904 | 0.0163 | 0.4489 | 0.4582 |
| ALL | MARKET_BASELINE | 322549 | 0.1483 | 0.4566 | 0.0085 | 0.2916 | 0.2955 |
| ALL | MARKET_ANCHORED_V1 | 69757 | 0.1598 | 0.4851 | 0.0145 | 0.4536 | 0.4583 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 14441 | 0.0392 | 0.1684 | 0.0030 | 0.0399 | 0.0409 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 11164 | 0.1818 | 0.5452 | 0.0319 | 0.2312 | 0.2587 |
| game_spread | MARKET_BASELINE | 11164 | 0.1782 | 0.5361 | 0.0305 | 0.2421 | 0.2587 |
| game_spread | MARKET_ANCHORED_V1 | 11164 | 0.1786 | 0.5370 | 0.0230 | 0.2394 | 0.2587 |
| game_total | DATA_ONLY_V1 | 25119 | 0.1262 | 0.3975 | 0.0245 | 0.5673 | 0.5754 |
| game_total | MARKET_BASELINE | 25119 | 0.1246 | 0.3934 | 0.0278 | 0.5733 | 0.5754 |
| game_total | MARKET_ANCHORED_V1 | 25119 | 0.1248 | 0.3938 | 0.0267 | 0.5721 | 0.5754 |
| game_winner | DATA_ONLY_V1 | 5582 | 0.2276 | 0.6475 | 0.1213 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5582 | 0.2243 | 0.6395 | 0.0503 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5582 | 0.2243 | 0.6399 | 0.0538 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1397 | 0.2463 | 0.6862 | 0.0704 | 0.4354 | 0.4066 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 16030 | 0.1371 | 0.4454 | 0.0378 | 0.1292 | 0.1661 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 24930 | 0.1827 | 0.5429 | 0.0271 | 0.5961 | 0.6150 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 24948 | 0.2161 | 0.6228 | 0.0231 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 43799 | 0.1559 | 0.4779 | 0.0182 | 0.2366 | 0.2333 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 70987 | 0.1037 | 0.3455 | 0.0094 | 0.1263 | 0.1292 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 56260 | 0.1678 | 0.5047 | 0.0143 | 0.2968 | 0.2929 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 27910 | 0.1730 | 0.5207 | 0.0111 | 0.4192 | 0.4242 |
| team_total | MARKET_BASELINE | 27892 | 0.1708 | 0.5152 | 0.0159 | 0.4245 | 0.4245 |
| team_total | MARKET_ANCHORED_V1 | 27892 | 0.1710 | 0.5157 | 0.0155 | 0.4234 | 0.4245 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
