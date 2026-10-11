# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-11T15:53:26Z · rows 239847 · pregame 239847 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 43725 | 0.1688 | 0.5078 | 0.0109 | 0.4509 | 0.4497 |
| ALL | MARKET_BASELINE | 200211 | 0.1495 | 0.4601 | 0.0102 | 0.2919 | 0.2910 |
| ALL | MARKET_ANCHORED_V1 | 43711 | 0.1654 | 0.4992 | 0.0113 | 0.4536 | 0.4499 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 9919 | 0.0397 | 0.1703 | 0.0055 | 0.0382 | 0.0414 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 6996 | 0.1865 | 0.5570 | 0.0390 | 0.2317 | 0.2666 |
| game_spread | MARKET_BASELINE | 6996 | 0.1798 | 0.5397 | 0.0346 | 0.2416 | 0.2666 |
| game_spread | MARKET_ANCHORED_V1 | 6996 | 0.1808 | 0.5422 | 0.0299 | 0.2391 | 0.2666 |
| game_total | DATA_ONLY_V1 | 15741 | 0.1312 | 0.4106 | 0.0233 | 0.5700 | 0.5585 |
| game_total | MARKET_BASELINE | 15741 | 0.1285 | 0.4031 | 0.0279 | 0.5725 | 0.5585 |
| game_total | MARKET_ANCHORED_V1 | 15741 | 0.1289 | 0.4042 | 0.0293 | 0.5720 | 0.5585 |
| game_winner | DATA_ONLY_V1 | 3498 | 0.2311 | 0.6550 | 0.1110 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3498 | 0.2259 | 0.6431 | 0.0487 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3498 | 0.2263 | 0.6442 | 0.0416 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 752 | 0.2538 | 0.7021 | 0.0852 | 0.4211 | 0.4322 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 9990 | 0.1501 | 0.4815 | 0.0527 | 0.1305 | 0.1818 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 15552 | 0.1848 | 0.5498 | 0.0226 | 0.5949 | 0.5993 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 15570 | 0.2173 | 0.6255 | 0.0209 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 26933 | 0.1521 | 0.4685 | 0.0203 | 0.2367 | 0.2269 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 44393 | 0.1056 | 0.3513 | 0.0105 | 0.1295 | 0.1306 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 33391 | 0.1676 | 0.5041 | 0.0198 | 0.3024 | 0.2883 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 17490 | 0.1830 | 0.5461 | 0.0321 | 0.4215 | 0.4150 |
| team_total | MARKET_BASELINE | 17476 | 0.1795 | 0.5373 | 0.0304 | 0.4241 | 0.4153 |
| team_total | MARKET_ANCHORED_V1 | 17476 | 0.1800 | 0.5384 | 0.0286 | 0.4236 | 0.4153 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
