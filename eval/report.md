# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-31T01:12:36Z · rows 726310 · pregame 726310 · new 3938

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 121150 | 0.1662 | 0.5008 | 0.0182 | 0.4492 | 0.4673 |
| ALL | MARKET_BASELINE | 621215 | 0.1443 | 0.4454 | 0.0095 | 0.2757 | 0.2835 |
| ALL | MARKET_ANCHORED_V1 | 121117 | 0.1642 | 0.4955 | 0.0122 | 0.4562 | 0.4674 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 41694 | 0.0346 | 0.1507 | 0.0017 | 0.0351 | 0.0361 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 19384 | 0.1832 | 0.5508 | 0.0245 | 0.2310 | 0.2544 |
| game_spread | MARKET_BASELINE | 19384 | 0.1792 | 0.5395 | 0.0188 | 0.2431 | 0.2544 |
| game_spread | MARKET_ANCHORED_V1 | 19384 | 0.1797 | 0.5408 | 0.0156 | 0.2402 | 0.2544 |
| game_total | DATA_ONLY_V1 | 43614 | 0.1303 | 0.4064 | 0.0253 | 0.5677 | 0.5874 |
| game_total | MARKET_BASELINE | 43614 | 0.1291 | 0.4031 | 0.0215 | 0.5774 | 0.5874 |
| game_total | MARKET_ANCHORED_V1 | 43614 | 0.1292 | 0.4033 | 0.0199 | 0.5755 | 0.5874 |
| game_winner | DATA_ONLY_V1 | 9692 | 0.2343 | 0.6612 | 0.0805 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 9692 | 0.2305 | 0.6528 | 0.0259 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 9692 | 0.2307 | 0.6534 | 0.0325 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2846 | 0.2494 | 0.6924 | 0.0410 | 0.4469 | 0.4385 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 27726 | 0.1335 | 0.4382 | 0.0315 | 0.1286 | 0.1596 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 43425 | 0.1804 | 0.5367 | 0.0248 | 0.5997 | 0.6218 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 43443 | 0.2168 | 0.6242 | 0.0239 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 88134 | 0.1562 | 0.4788 | 0.0152 | 0.2297 | 0.2326 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 137334 | 0.1003 | 0.3351 | 0.0069 | 0.1190 | 0.1250 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 115496 | 0.1655 | 0.4994 | 0.0102 | 0.2824 | 0.2872 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 48460 | 0.1781 | 0.5336 | 0.0196 | 0.4196 | 0.4377 |
| team_total | MARKET_BASELINE | 48427 | 0.1760 | 0.5284 | 0.0175 | 0.4284 | 0.4380 |
| team_total | MARKET_ANCHORED_V1 | 48427 | 0.1762 | 0.5288 | 0.0157 | 0.4266 | 0.4380 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
