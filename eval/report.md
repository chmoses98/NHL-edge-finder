# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-05T04:34:40Z · rows 854038 · pregame 854038 · new 7367

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 140175 | 0.1662 | 0.5005 | 0.0206 | 0.4503 | 0.4709 |
| ALL | MARKET_BASELINE | 736400 | 0.1435 | 0.4432 | 0.0119 | 0.2726 | 0.2827 |
| ALL | MARKET_ANCHORED_V1 | 140142 | 0.1637 | 0.4940 | 0.0141 | 0.4570 | 0.4710 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 54656 | 0.0336 | 0.1471 | 0.0016 | 0.0341 | 0.0351 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 22428 | 0.1825 | 0.5489 | 0.0242 | 0.2315 | 0.2549 |
| game_spread | MARKET_BASELINE | 22428 | 0.1779 | 0.5365 | 0.0211 | 0.2436 | 0.2549 |
| game_spread | MARKET_ANCHORED_V1 | 22428 | 0.1785 | 0.5380 | 0.0164 | 0.2408 | 0.2549 |
| game_total | DATA_ONLY_V1 | 50463 | 0.1308 | 0.4066 | 0.0285 | 0.5692 | 0.5929 |
| game_total | MARKET_BASELINE | 50463 | 0.1291 | 0.4020 | 0.0223 | 0.5782 | 0.5929 |
| game_total | MARKET_ANCHORED_V1 | 50463 | 0.1293 | 0.4025 | 0.0236 | 0.5765 | 0.5929 |
| game_winner | DATA_ONLY_V1 | 11214 | 0.2336 | 0.6597 | 0.0675 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 11214 | 0.2287 | 0.6488 | 0.0285 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 11214 | 0.2291 | 0.6498 | 0.0281 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 3304 | 0.2478 | 0.6892 | 0.0377 | 0.4468 | 0.4337 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 32073 | 0.1327 | 0.4357 | 0.0300 | 0.1289 | 0.1585 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 50243 | 0.1779 | 0.5308 | 0.0292 | 0.5999 | 0.6265 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 50292 | 0.2171 | 0.6248 | 0.0216 | 0.3284 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 105040 | 0.1579 | 0.4828 | 0.0188 | 0.2296 | 0.2378 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 162560 | 0.1009 | 0.3371 | 0.0088 | 0.1191 | 0.1258 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 138090 | 0.1665 | 0.5023 | 0.0141 | 0.2812 | 0.2902 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 56070 | 0.1780 | 0.5338 | 0.0225 | 0.4209 | 0.4417 |
| team_total | MARKET_BASELINE | 56037 | 0.1753 | 0.5269 | 0.0176 | 0.4291 | 0.4420 |
| team_total | MARKET_ANCHORED_V1 | 56037 | 0.1756 | 0.5276 | 0.0181 | 0.4274 | 0.4420 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
