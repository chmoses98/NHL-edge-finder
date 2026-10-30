# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-30T15:32:16Z · rows 722372 · pregame 722372 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 120600 | 0.1662 | 0.5007 | 0.0180 | 0.4492 | 0.4668 |
| ALL | MARKET_BASELINE | 617474 | 0.1444 | 0.4457 | 0.0096 | 0.2760 | 0.2837 |
| ALL | MARKET_ANCHORED_V1 | 120567 | 0.1641 | 0.4954 | 0.0124 | 0.4563 | 0.4669 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 41181 | 0.0346 | 0.1507 | 0.0017 | 0.0352 | 0.0361 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 19296 | 0.1825 | 0.5491 | 0.0234 | 0.2311 | 0.2533 |
| game_spread | MARKET_BASELINE | 19296 | 0.1785 | 0.5378 | 0.0172 | 0.2431 | 0.2533 |
| game_spread | MARKET_ANCHORED_V1 | 19296 | 0.1790 | 0.5391 | 0.0144 | 0.2402 | 0.2533 |
| game_total | DATA_ONLY_V1 | 43416 | 0.1306 | 0.4071 | 0.0247 | 0.5677 | 0.5870 |
| game_total | MARKET_BASELINE | 43416 | 0.1294 | 0.4037 | 0.0214 | 0.5775 | 0.5870 |
| game_total | MARKET_ANCHORED_V1 | 43416 | 0.1295 | 0.4039 | 0.0199 | 0.5756 | 0.5870 |
| game_winner | DATA_ONLY_V1 | 9648 | 0.2341 | 0.6609 | 0.0828 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 9648 | 0.2304 | 0.6525 | 0.0236 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 9648 | 0.2305 | 0.6531 | 0.0350 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2845 | 0.2493 | 0.6922 | 0.0408 | 0.4469 | 0.4383 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 27594 | 0.1334 | 0.4380 | 0.0314 | 0.1286 | 0.1595 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 43227 | 0.1804 | 0.5367 | 0.0242 | 0.5997 | 0.6216 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 43245 | 0.2168 | 0.6242 | 0.0237 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 87589 | 0.1565 | 0.4795 | 0.0156 | 0.2298 | 0.2334 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 136461 | 0.1002 | 0.3349 | 0.0069 | 0.1191 | 0.1249 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 114765 | 0.1656 | 0.4997 | 0.0099 | 0.2825 | 0.2874 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 48240 | 0.1780 | 0.5335 | 0.0188 | 0.4196 | 0.4374 |
| team_total | MARKET_BASELINE | 48207 | 0.1760 | 0.5284 | 0.0173 | 0.4285 | 0.4377 |
| team_total | MARKET_ANCHORED_V1 | 48207 | 0.1761 | 0.5287 | 0.0155 | 0.4266 | 0.4377 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
