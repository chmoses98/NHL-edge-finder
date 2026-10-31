# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-31T04:51:14Z · rows 734448 · pregame 734448 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 122350 | 0.1664 | 0.5011 | 0.0193 | 0.4492 | 0.4686 |
| ALL | MARKET_BASELINE | 628511 | 0.1444 | 0.4456 | 0.0099 | 0.2755 | 0.2839 |
| ALL | MARKET_ANCHORED_V1 | 122317 | 0.1643 | 0.4956 | 0.0128 | 0.4563 | 0.4687 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 42560 | 0.0344 | 0.1500 | 0.0017 | 0.0350 | 0.0359 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 19576 | 0.1843 | 0.5532 | 0.0269 | 0.2311 | 0.2568 |
| game_spread | MARKET_BASELINE | 19576 | 0.1801 | 0.5413 | 0.0204 | 0.2431 | 0.2568 |
| game_spread | MARKET_ANCHORED_V1 | 19576 | 0.1806 | 0.5428 | 0.0182 | 0.2402 | 0.2568 |
| game_total | DATA_ONLY_V1 | 44046 | 0.1300 | 0.4056 | 0.0269 | 0.5678 | 0.5887 |
| game_total | MARKET_BASELINE | 44046 | 0.1288 | 0.4022 | 0.0220 | 0.5775 | 0.5887 |
| game_total | MARKET_ANCHORED_V1 | 44046 | 0.1289 | 0.4024 | 0.0215 | 0.5756 | 0.5887 |
| game_winner | DATA_ONLY_V1 | 9788 | 0.2341 | 0.6608 | 0.0788 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 9788 | 0.2301 | 0.6520 | 0.0298 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 9788 | 0.2303 | 0.6526 | 0.0312 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2872 | 0.2485 | 0.6907 | 0.0421 | 0.4464 | 0.4345 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 28004 | 0.1336 | 0.4386 | 0.0316 | 0.1286 | 0.1597 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 43857 | 0.1801 | 0.5360 | 0.0248 | 0.5997 | 0.6233 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 43875 | 0.2165 | 0.6236 | 0.0254 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 89168 | 0.1567 | 0.4798 | 0.0156 | 0.2297 | 0.2335 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 138986 | 0.1004 | 0.3353 | 0.0074 | 0.1192 | 0.1252 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 116872 | 0.1662 | 0.5014 | 0.0102 | 0.2824 | 0.2883 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 48940 | 0.1784 | 0.5343 | 0.0206 | 0.4197 | 0.4388 |
| team_total | MARKET_BASELINE | 48907 | 0.1762 | 0.5289 | 0.0180 | 0.4285 | 0.4391 |
| team_total | MARKET_ANCHORED_V1 | 48907 | 0.1764 | 0.5293 | 0.0162 | 0.4267 | 0.4391 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
