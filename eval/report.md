# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-07T03:51:10Z · rows 137660 · pregame 137660 · new 2998

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 26175 | 0.1672 | 0.5032 | 0.0136 | 0.4485 | 0.4620 |
| ALL | MARKET_BASELINE | 117178 | 0.1545 | 0.4734 | 0.0136 | 0.2969 | 0.3070 |
| ALL | MARKET_ANCHORED_V1 | 26175 | 0.1659 | 0.4998 | 0.0123 | 0.4522 | 0.4620 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 6610 | 0.0404 | 0.1737 | 0.0082 | 0.0364 | 0.0422 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 4188 | 0.1771 | 0.5327 | 0.0340 | 0.2307 | 0.2564 |
| game_spread | MARKET_BASELINE | 4188 | 0.1762 | 0.5309 | 0.0415 | 0.2408 | 0.2564 |
| game_spread | MARKET_ANCHORED_V1 | 4188 | 0.1759 | 0.5302 | 0.0327 | 0.2383 | 0.2564 |
| game_total | DATA_ONLY_V1 | 9423 | 0.1287 | 0.4030 | 0.0303 | 0.5669 | 0.5731 |
| game_total | MARKET_BASELINE | 9423 | 0.1260 | 0.3958 | 0.0275 | 0.5713 | 0.5731 |
| game_total | MARKET_ANCHORED_V1 | 9423 | 0.1264 | 0.3969 | 0.0270 | 0.5704 | 0.5731 |
| game_winner | DATA_ONLY_V1 | 2094 | 0.2295 | 0.6515 | 0.0927 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2094 | 0.2327 | 0.6572 | 0.1026 | 0.4996 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2094 | 0.2314 | 0.6548 | 0.0807 | 0.4997 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 454 | 0.2571 | 0.7082 | 0.0971 | 0.3973 | 0.4824 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 5964 | 0.1570 | 0.4981 | 0.0643 | 0.1305 | 0.1925 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 9368 | 0.1787 | 0.5333 | 0.0295 | 0.5932 | 0.6165 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 9411 | 0.2154 | 0.6212 | 0.0355 | 0.3283 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 15779 | 0.1588 | 0.4846 | 0.0129 | 0.2362 | 0.2422 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 24325 | 0.1176 | 0.3856 | 0.0100 | 0.1421 | 0.1478 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 19092 | 0.1765 | 0.5282 | 0.0226 | 0.3088 | 0.3091 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 10470 | 0.1854 | 0.5519 | 0.0262 | 0.4189 | 0.4366 |
| team_total | MARKET_BASELINE | 10470 | 0.1843 | 0.5496 | 0.0370 | 0.4229 | 0.4366 |
| team_total | MARKET_ANCHORED_V1 | 10470 | 0.1843 | 0.5493 | 0.0328 | 0.4220 | 0.4366 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
