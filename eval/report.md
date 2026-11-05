# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-05T14:02:19Z · rows 862835 · pregame 862835 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 141525 | 0.1665 | 0.5012 | 0.0200 | 0.4504 | 0.4704 |
| ALL | MARKET_BASELINE | 744186 | 0.1436 | 0.4435 | 0.0118 | 0.2725 | 0.2825 |
| ALL | MARKET_ANCHORED_V1 | 141492 | 0.1640 | 0.4947 | 0.0136 | 0.4570 | 0.4705 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 55344 | 0.0337 | 0.1473 | 0.0018 | 0.0341 | 0.0351 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 22644 | 0.1823 | 0.5484 | 0.0241 | 0.2316 | 0.2549 |
| game_spread | MARKET_BASELINE | 22644 | 0.1777 | 0.5359 | 0.0203 | 0.2436 | 0.2549 |
| game_spread | MARKET_ANCHORED_V1 | 22644 | 0.1783 | 0.5374 | 0.0164 | 0.2407 | 0.2549 |
| game_total | DATA_ONLY_V1 | 50949 | 0.1316 | 0.4084 | 0.0279 | 0.5693 | 0.5925 |
| game_total | MARKET_BASELINE | 50949 | 0.1299 | 0.4038 | 0.0213 | 0.5782 | 0.5925 |
| game_total | MARKET_ANCHORED_V1 | 50949 | 0.1301 | 0.4042 | 0.0226 | 0.5765 | 0.5925 |
| game_winner | DATA_ONLY_V1 | 11322 | 0.2329 | 0.6583 | 0.0707 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 11322 | 0.2282 | 0.6478 | 0.0265 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 11322 | 0.2286 | 0.6488 | 0.0318 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 3354 | 0.2477 | 0.6890 | 0.0333 | 0.4473 | 0.4383 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 32379 | 0.1321 | 0.4342 | 0.0292 | 0.1289 | 0.1577 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 50729 | 0.1784 | 0.5321 | 0.0285 | 0.5999 | 0.6263 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 50778 | 0.2170 | 0.6246 | 0.0216 | 0.3284 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 106343 | 0.1581 | 0.4833 | 0.0194 | 0.2295 | 0.2376 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 164021 | 0.1009 | 0.3370 | 0.0089 | 0.1191 | 0.1258 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 139746 | 0.1667 | 0.5029 | 0.0137 | 0.2810 | 0.2902 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 56610 | 0.1783 | 0.5344 | 0.0218 | 0.4210 | 0.4409 |
| team_total | MARKET_BASELINE | 56577 | 0.1755 | 0.5275 | 0.0172 | 0.4291 | 0.4411 |
| team_total | MARKET_ANCHORED_V1 | 56577 | 0.1758 | 0.5282 | 0.0167 | 0.4274 | 0.4411 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
