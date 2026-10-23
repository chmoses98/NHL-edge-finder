# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-23T02:23:37Z · rows 479514 · pregame 479514 · new 16310

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 84325 | 0.1620 | 0.4901 | 0.0155 | 0.4495 | 0.4609 |
| ALL | MARKET_BASELINE | 393979 | 0.1483 | 0.4563 | 0.0081 | 0.2915 | 0.2955 |
| ALL | MARKET_ANCHORED_V1 | 84305 | 0.1600 | 0.4850 | 0.0156 | 0.4550 | 0.4610 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 17329 | 0.0394 | 0.1685 | 0.0025 | 0.0405 | 0.0411 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 13492 | 0.1834 | 0.5499 | 0.0283 | 0.2315 | 0.2581 |
| game_spread | MARKET_BASELINE | 13492 | 0.1794 | 0.5391 | 0.0278 | 0.2428 | 0.2581 |
| game_spread | MARKET_ANCHORED_V1 | 13492 | 0.1798 | 0.5403 | 0.0221 | 0.2401 | 0.2581 |
| game_total | DATA_ONLY_V1 | 30357 | 0.1238 | 0.3899 | 0.0278 | 0.5680 | 0.5792 |
| game_total | MARKET_BASELINE | 30357 | 0.1226 | 0.3868 | 0.0283 | 0.5755 | 0.5792 |
| game_total | MARKET_ANCHORED_V1 | 30357 | 0.1227 | 0.3870 | 0.0271 | 0.5741 | 0.5792 |
| game_winner | DATA_ONLY_V1 | 6746 | 0.2309 | 0.6543 | 0.0998 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 6746 | 0.2279 | 0.6470 | 0.0346 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 6746 | 0.2279 | 0.6473 | 0.0436 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1810 | 0.2498 | 0.6931 | 0.0470 | 0.4419 | 0.4365 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 19293 | 0.1372 | 0.4459 | 0.0374 | 0.1289 | 0.1656 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 30168 | 0.1802 | 0.5369 | 0.0291 | 0.5979 | 0.6223 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 30186 | 0.2168 | 0.6242 | 0.0231 | 0.3278 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 54452 | 0.1554 | 0.4766 | 0.0195 | 0.2364 | 0.2305 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 85804 | 0.1035 | 0.3444 | 0.0097 | 0.1259 | 0.1290 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 70632 | 0.1676 | 0.5042 | 0.0125 | 0.2939 | 0.2891 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 33730 | 0.1740 | 0.5235 | 0.0176 | 0.4198 | 0.4278 |
| team_total | MARKET_BASELINE | 33710 | 0.1720 | 0.5183 | 0.0173 | 0.4263 | 0.4280 |
| team_total | MARKET_ANCHORED_V1 | 33710 | 0.1721 | 0.5187 | 0.0179 | 0.4250 | 0.4280 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
