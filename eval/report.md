# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-10T23:43:37Z · rows 203733 · pregame 203733 · new 2956

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 37750 | 0.1672 | 0.5027 | 0.0124 | 0.4509 | 0.4580 |
| ALL | MARKET_BASELINE | 173138 | 0.1491 | 0.4589 | 0.0100 | 0.2906 | 0.2939 |
| ALL | MARKET_ANCHORED_V1 | 37736 | 0.1641 | 0.4946 | 0.0113 | 0.4537 | 0.4582 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 9297 | 0.0392 | 0.1694 | 0.0056 | 0.0377 | 0.0409 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 6040 | 0.1859 | 0.5540 | 0.0452 | 0.2316 | 0.2700 |
| game_spread | MARKET_BASELINE | 6040 | 0.1798 | 0.5388 | 0.0349 | 0.2415 | 0.2700 |
| game_spread | MARKET_ANCHORED_V1 | 6040 | 0.1806 | 0.5408 | 0.0374 | 0.2390 | 0.2700 |
| game_total | DATA_ONLY_V1 | 13590 | 0.1269 | 0.3974 | 0.0264 | 0.5700 | 0.5689 |
| game_total | MARKET_BASELINE | 13590 | 0.1243 | 0.3894 | 0.0277 | 0.5727 | 0.5689 |
| game_total | MARKET_ANCHORED_V1 | 13590 | 0.1247 | 0.3906 | 0.0274 | 0.5722 | 0.5689 |
| game_winner | DATA_ONLY_V1 | 3020 | 0.2300 | 0.6523 | 0.0830 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3020 | 0.2263 | 0.6438 | 0.0590 | 0.4992 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3020 | 0.2264 | 0.6442 | 0.0378 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 648 | 0.2518 | 0.6976 | 0.0709 | 0.4178 | 0.4383 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 8594 | 0.1492 | 0.4771 | 0.0524 | 0.1311 | 0.1819 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 13401 | 0.1823 | 0.5428 | 0.0287 | 0.5952 | 0.6099 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 13419 | 0.2162 | 0.6231 | 0.0280 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 23065 | 0.1531 | 0.4711 | 0.0196 | 0.2349 | 0.2295 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 38458 | 0.1077 | 0.3578 | 0.0102 | 0.1298 | 0.1334 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 28520 | 0.1686 | 0.5063 | 0.0191 | 0.3022 | 0.2908 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 15100 | 0.1833 | 0.5469 | 0.0274 | 0.4216 | 0.4250 |
| team_total | MARKET_BASELINE | 15086 | 0.1802 | 0.5389 | 0.0298 | 0.4244 | 0.4253 |
| team_total | MARKET_ANCHORED_V1 | 15086 | 0.1806 | 0.5398 | 0.0296 | 0.4238 | 0.4253 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
