# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-16T12:04:16Z · rows 345917 · pregame 345917 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 62350 | 0.1639 | 0.4947 | 0.0162 | 0.4494 | 0.4621 |
| ALL | MARKET_BASELINE | 288485 | 0.1488 | 0.4579 | 0.0093 | 0.2910 | 0.2966 |
| ALL | MARKET_ANCHORED_V1 | 62333 | 0.1611 | 0.4876 | 0.0140 | 0.4534 | 0.4622 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 13164 | 0.0401 | 0.1713 | 0.0043 | 0.0396 | 0.0419 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 9976 | 0.1809 | 0.5436 | 0.0277 | 0.2314 | 0.2546 |
| game_spread | MARKET_BASELINE | 9976 | 0.1768 | 0.5331 | 0.0226 | 0.2419 | 0.2546 |
| game_spread | MARKET_ANCHORED_V1 | 9976 | 0.1773 | 0.5342 | 0.0192 | 0.2393 | 0.2546 |
| game_total | DATA_ONLY_V1 | 22446 | 0.1279 | 0.3998 | 0.0215 | 0.5679 | 0.5818 |
| game_total | MARKET_BASELINE | 22446 | 0.1251 | 0.3920 | 0.0273 | 0.5728 | 0.5818 |
| game_total | MARKET_ANCHORED_V1 | 22446 | 0.1255 | 0.3932 | 0.0270 | 0.5718 | 0.5818 |
| game_winner | DATA_ONLY_V1 | 4988 | 0.2294 | 0.6513 | 0.1041 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 4988 | 0.2266 | 0.6444 | 0.0414 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 4988 | 0.2265 | 0.6446 | 0.0401 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1253 | 0.2435 | 0.6805 | 0.0843 | 0.4307 | 0.3919 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 14372 | 0.1402 | 0.4547 | 0.0407 | 0.1295 | 0.1693 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 22257 | 0.1812 | 0.5397 | 0.0275 | 0.5956 | 0.6176 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 22275 | 0.2168 | 0.6243 | 0.0176 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 39591 | 0.1548 | 0.4750 | 0.0166 | 0.2336 | 0.2318 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 62747 | 0.1049 | 0.3489 | 0.0103 | 0.1272 | 0.1305 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 50493 | 0.1679 | 0.5050 | 0.0123 | 0.2948 | 0.2918 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 24940 | 0.1763 | 0.5292 | 0.0214 | 0.4198 | 0.4298 |
| team_total | MARKET_BASELINE | 24923 | 0.1733 | 0.5216 | 0.0174 | 0.4242 | 0.4300 |
| team_total | MARKET_ANCHORED_V1 | 24923 | 0.1736 | 0.5225 | 0.0188 | 0.4233 | 0.4300 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
