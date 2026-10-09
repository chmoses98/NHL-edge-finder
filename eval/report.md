# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-09T22:36:47Z · rows 182876 · pregame 182876 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 34500 | 0.1664 | 0.5010 | 0.0124 | 0.4505 | 0.4613 |
| ALL | MARKET_BASELINE | 156036 | 0.1511 | 0.4642 | 0.0107 | 0.2923 | 0.3001 |
| ALL | MARKET_ANCHORED_V1 | 34486 | 0.1638 | 0.4940 | 0.0097 | 0.4535 | 0.4614 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 8597 | 0.0404 | 0.1731 | 0.0071 | 0.0372 | 0.0421 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 5520 | 0.1818 | 0.5441 | 0.0379 | 0.2316 | 0.2625 |
| game_spread | MARKET_BASELINE | 5520 | 0.1764 | 0.5310 | 0.0366 | 0.2416 | 0.2625 |
| game_spread | MARKET_ANCHORED_V1 | 5520 | 0.1771 | 0.5327 | 0.0330 | 0.2391 | 0.2625 |
| game_total | DATA_ONLY_V1 | 12420 | 0.1274 | 0.3993 | 0.0220 | 0.5695 | 0.5745 |
| game_total | MARKET_BASELINE | 12420 | 0.1251 | 0.3921 | 0.0253 | 0.5723 | 0.5745 |
| game_total | MARKET_ANCHORED_V1 | 12420 | 0.1254 | 0.3931 | 0.0252 | 0.5718 | 0.5745 |
| game_winner | DATA_ONLY_V1 | 2760 | 0.2299 | 0.6520 | 0.0857 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2760 | 0.2274 | 0.6461 | 0.0678 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2760 | 0.2272 | 0.6460 | 0.0404 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 602 | 0.2557 | 0.7057 | 0.0674 | 0.4157 | 0.4651 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 7850 | 0.1535 | 0.4887 | 0.0581 | 0.1312 | 0.1875 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 12231 | 0.1830 | 0.5442 | 0.0319 | 0.5947 | 0.6165 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 12249 | 0.2163 | 0.6234 | 0.0287 | 0.3284 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 20475 | 0.1571 | 0.4809 | 0.0165 | 0.2366 | 0.2365 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 34406 | 0.1094 | 0.3625 | 0.0092 | 0.1311 | 0.1367 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 25140 | 0.1737 | 0.5197 | 0.0163 | 0.3062 | 0.3034 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 13800 | 0.1827 | 0.5450 | 0.0250 | 0.4211 | 0.4312 |
| team_total | MARKET_BASELINE | 13786 | 0.1800 | 0.5382 | 0.0281 | 0.4241 | 0.4315 |
| team_total | MARKET_ANCHORED_V1 | 13786 | 0.1803 | 0.5389 | 0.0273 | 0.4235 | 0.4315 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
