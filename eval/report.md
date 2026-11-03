# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-03T08:22:21Z · rows 816800 · pregame 816800 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 133975 | 0.1661 | 0.4999 | 0.0210 | 0.4499 | 0.4709 |
| ALL | MARKET_BASELINE | 702424 | 0.1436 | 0.4437 | 0.0116 | 0.2730 | 0.2829 |
| ALL | MARKET_ANCHORED_V1 | 133942 | 0.1638 | 0.4941 | 0.0143 | 0.4567 | 0.4710 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 50845 | 0.0339 | 0.1478 | 0.0017 | 0.0344 | 0.0353 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 21436 | 0.1845 | 0.5531 | 0.0296 | 0.2314 | 0.2597 |
| game_spread | MARKET_BASELINE | 21436 | 0.1801 | 0.5411 | 0.0230 | 0.2435 | 0.2597 |
| game_spread | MARKET_ANCHORED_V1 | 21436 | 0.1806 | 0.5426 | 0.0211 | 0.2407 | 0.2597 |
| game_total | DATA_ONLY_V1 | 48231 | 0.1299 | 0.4045 | 0.0289 | 0.5687 | 0.5916 |
| game_total | MARKET_BASELINE | 48231 | 0.1284 | 0.4002 | 0.0232 | 0.5780 | 0.5916 |
| game_total | MARKET_ANCHORED_V1 | 48231 | 0.1285 | 0.4006 | 0.0237 | 0.5761 | 0.5916 |
| game_winner | DATA_ONLY_V1 | 10718 | 0.2321 | 0.6565 | 0.0709 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 10718 | 0.2288 | 0.6491 | 0.0294 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 10718 | 0.2289 | 0.6494 | 0.0311 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 3149 | 0.2480 | 0.6896 | 0.0397 | 0.4465 | 0.4351 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 30635 | 0.1340 | 0.4391 | 0.0323 | 0.1286 | 0.1605 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 48012 | 0.1785 | 0.5322 | 0.0279 | 0.5996 | 0.6261 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 48060 | 0.2166 | 0.6238 | 0.0251 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 100402 | 0.1576 | 0.4821 | 0.0180 | 0.2296 | 0.2367 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 155447 | 0.1006 | 0.3362 | 0.0082 | 0.1191 | 0.1255 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 131932 | 0.1663 | 0.5018 | 0.0126 | 0.2813 | 0.2893 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 53590 | 0.1780 | 0.5332 | 0.0229 | 0.4205 | 0.4409 |
| team_total | MARKET_BASELINE | 53557 | 0.1755 | 0.5274 | 0.0171 | 0.4288 | 0.4412 |
| team_total | MARKET_ANCHORED_V1 | 53557 | 0.1758 | 0.5279 | 0.0170 | 0.4271 | 0.4412 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
