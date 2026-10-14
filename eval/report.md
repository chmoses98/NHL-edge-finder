# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-14T04:06:03Z · rows 292519 · pregame 292519 · new 11748

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 53650 | 0.1659 | 0.5002 | 0.0172 | 0.4495 | 0.4614 |
| ALL | MARKET_BASELINE | 244956 | 0.1494 | 0.4595 | 0.0099 | 0.2916 | 0.2967 |
| ALL | MARKET_ANCHORED_V1 | 53636 | 0.1634 | 0.4937 | 0.0136 | 0.4530 | 0.4615 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 11401 | 0.0400 | 0.1712 | 0.0048 | 0.0391 | 0.0418 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 8584 | 0.1878 | 0.5599 | 0.0411 | 0.2314 | 0.2684 |
| game_spread | MARKET_BASELINE | 8584 | 0.1830 | 0.5476 | 0.0332 | 0.2414 | 0.2684 |
| game_spread | MARKET_ANCHORED_V1 | 8584 | 0.1836 | 0.5491 | 0.0326 | 0.2389 | 0.2684 |
| game_total | DATA_ONLY_V1 | 19314 | 0.1279 | 0.4013 | 0.0206 | 0.5681 | 0.5766 |
| game_total | MARKET_BASELINE | 19314 | 0.1255 | 0.3945 | 0.0270 | 0.5721 | 0.5766 |
| game_total | MARKET_ANCHORED_V1 | 19314 | 0.1258 | 0.3954 | 0.0256 | 0.5713 | 0.5766 |
| game_winner | DATA_ONLY_V1 | 4292 | 0.2296 | 0.6516 | 0.1124 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 4292 | 0.2277 | 0.6469 | 0.0508 | 0.4990 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 4292 | 0.2275 | 0.6466 | 0.0403 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1014 | 0.2451 | 0.6839 | 0.0848 | 0.4228 | 0.3905 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 12365 | 0.1466 | 0.4713 | 0.0488 | 0.1300 | 0.1777 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 19125 | 0.1811 | 0.5400 | 0.0274 | 0.5946 | 0.6131 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 19143 | 0.2169 | 0.6245 | 0.0238 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 33171 | 0.1526 | 0.4690 | 0.0197 | 0.2334 | 0.2295 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 53354 | 0.1059 | 0.3513 | 0.0108 | 0.1278 | 0.1317 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 41747 | 0.1677 | 0.5045 | 0.0145 | 0.2966 | 0.2903 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 21460 | 0.1785 | 0.5351 | 0.0236 | 0.4199 | 0.4271 |
| team_total | MARKET_BASELINE | 21446 | 0.1760 | 0.5289 | 0.0216 | 0.4237 | 0.4273 |
| team_total | MARKET_ANCHORED_V1 | 21446 | 0.1763 | 0.5295 | 0.0254 | 0.4229 | 0.4273 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
