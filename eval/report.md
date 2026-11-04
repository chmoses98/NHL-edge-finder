# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-04T03:46:07Z · rows 841047 · pregame 841047 · new 24247

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 138025 | 0.1661 | 0.5002 | 0.0214 | 0.4499 | 0.4713 |
| ALL | MARKET_BASELINE | 724712 | 0.1435 | 0.4434 | 0.0120 | 0.2726 | 0.2829 |
| ALL | MARKET_ANCHORED_V1 | 137992 | 0.1635 | 0.4936 | 0.0147 | 0.4567 | 0.4714 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 53449 | 0.0338 | 0.1476 | 0.0017 | 0.0342 | 0.0352 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 22084 | 0.1828 | 0.5494 | 0.0257 | 0.2314 | 0.2561 |
| game_spread | MARKET_BASELINE | 22084 | 0.1782 | 0.5369 | 0.0205 | 0.2435 | 0.2561 |
| game_spread | MARKET_ANCHORED_V1 | 22084 | 0.1788 | 0.5384 | 0.0176 | 0.2406 | 0.2561 |
| game_total | DATA_ONLY_V1 | 49689 | 0.1305 | 0.4058 | 0.0285 | 0.5686 | 0.5930 |
| game_total | MARKET_BASELINE | 49689 | 0.1286 | 0.4009 | 0.0224 | 0.5779 | 0.5930 |
| game_total | MARKET_ANCHORED_V1 | 49689 | 0.1288 | 0.4014 | 0.0235 | 0.5761 | 0.5930 |
| game_winner | DATA_ONLY_V1 | 11042 | 0.2331 | 0.6586 | 0.0699 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 11042 | 0.2286 | 0.6486 | 0.0282 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 11042 | 0.2289 | 0.6495 | 0.0302 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 3239 | 0.2480 | 0.6896 | 0.0344 | 0.4462 | 0.4369 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 31580 | 0.1330 | 0.4365 | 0.0307 | 0.1287 | 0.1590 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 49470 | 0.1781 | 0.5314 | 0.0283 | 0.5996 | 0.6259 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 49518 | 0.2169 | 0.6245 | 0.0224 | 0.3284 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 103401 | 0.1581 | 0.4834 | 0.0184 | 0.2295 | 0.2381 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 160175 | 0.1009 | 0.3370 | 0.0088 | 0.1190 | 0.1258 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 135888 | 0.1665 | 0.5023 | 0.0142 | 0.2812 | 0.2902 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 55210 | 0.1780 | 0.5337 | 0.0235 | 0.4204 | 0.4420 |
| team_total | MARKET_BASELINE | 55177 | 0.1752 | 0.5268 | 0.0181 | 0.4288 | 0.4422 |
| team_total | MARKET_ANCHORED_V1 | 55177 | 0.1755 | 0.5275 | 0.0185 | 0.4270 | 0.4422 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
