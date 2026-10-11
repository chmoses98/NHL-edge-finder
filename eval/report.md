# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-11T02:05:51Z · rows 226433 · pregame 226433 · new 19559

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 41400 | 0.1682 | 0.5052 | 0.0134 | 0.4516 | 0.4575 |
| ALL | MARKET_BASELINE | 189260 | 0.1494 | 0.4597 | 0.0107 | 0.2922 | 0.2950 |
| ALL | MARKET_ANCHORED_V1 | 41386 | 0.1648 | 0.4964 | 0.0131 | 0.4538 | 0.4576 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 9610 | 0.0397 | 0.1705 | 0.0056 | 0.0381 | 0.0414 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 6624 | 0.1908 | 0.5673 | 0.0460 | 0.2320 | 0.2745 |
| game_spread | MARKET_BASELINE | 6624 | 0.1839 | 0.5494 | 0.0389 | 0.2416 | 0.2745 |
| game_spread | MARKET_ANCHORED_V1 | 6624 | 0.1849 | 0.5520 | 0.0375 | 0.2392 | 0.2745 |
| game_total | DATA_ONLY_V1 | 14904 | 0.1267 | 0.3962 | 0.0284 | 0.5709 | 0.5678 |
| game_total | MARKET_BASELINE | 14904 | 0.1239 | 0.3879 | 0.0315 | 0.5727 | 0.5678 |
| game_total | MARKET_ANCHORED_V1 | 14904 | 0.1243 | 0.3892 | 0.0306 | 0.5723 | 0.5678 |
| game_winner | DATA_ONLY_V1 | 3312 | 0.2331 | 0.6590 | 0.0932 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3312 | 0.2292 | 0.6499 | 0.0444 | 0.4992 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3312 | 0.2293 | 0.6504 | 0.0282 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 706 | 0.2529 | 0.7003 | 0.0792 | 0.4185 | 0.4348 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 9438 | 0.1509 | 0.4835 | 0.0534 | 0.1308 | 0.1828 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 14715 | 0.1811 | 0.5400 | 0.0304 | 0.5950 | 0.6093 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 14733 | 0.2167 | 0.6241 | 0.0247 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 25212 | 0.1530 | 0.4709 | 0.0216 | 0.2381 | 0.2307 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 42093 | 0.1072 | 0.3558 | 0.0097 | 0.1299 | 0.1332 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 31367 | 0.1679 | 0.5047 | 0.0196 | 0.3041 | 0.2924 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 16560 | 0.1835 | 0.5476 | 0.0289 | 0.4223 | 0.4228 |
| team_total | MARKET_BASELINE | 16546 | 0.1799 | 0.5387 | 0.0302 | 0.4243 | 0.4231 |
| team_total | MARKET_ANCHORED_V1 | 16546 | 0.1804 | 0.5398 | 0.0331 | 0.4238 | 0.4231 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
