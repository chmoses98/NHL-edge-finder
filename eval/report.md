# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-27T02:59:15Z · rows 606519 · pregame 606519 · new 3707

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 102900 | 0.1655 | 0.4988 | 0.0207 | 0.4490 | 0.4681 |
| ALL | MARKET_BASELINE | 506810 | 0.1474 | 0.4536 | 0.0099 | 0.2829 | 0.2920 |
| ALL | MARKET_ANCHORED_V1 | 102875 | 0.1633 | 0.4929 | 0.0154 | 0.4554 | 0.4682 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 27159 | 0.0370 | 0.1597 | 0.0017 | 0.0378 | 0.0386 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 16464 | 0.1864 | 0.5583 | 0.0304 | 0.2311 | 0.2601 |
| game_spread | MARKET_BASELINE | 16464 | 0.1819 | 0.5459 | 0.0230 | 0.2428 | 0.2601 |
| game_spread | MARKET_ANCHORED_V1 | 16464 | 0.1825 | 0.5474 | 0.0209 | 0.2399 | 0.2601 |
| game_total | DATA_ONLY_V1 | 37044 | 0.1279 | 0.3991 | 0.0290 | 0.5674 | 0.5890 |
| game_total | MARKET_BASELINE | 37044 | 0.1265 | 0.3952 | 0.0282 | 0.5762 | 0.5890 |
| game_total | MARKET_ANCHORED_V1 | 37044 | 0.1266 | 0.3955 | 0.0265 | 0.5745 | 0.5890 |
| game_winner | DATA_ONLY_V1 | 8232 | 0.2334 | 0.6595 | 0.0913 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 8232 | 0.2295 | 0.6506 | 0.0281 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 8232 | 0.2296 | 0.6512 | 0.0411 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2309 | 0.2531 | 0.7000 | 0.0495 | 0.4444 | 0.4604 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 23455 | 0.1370 | 0.4474 | 0.0362 | 0.1288 | 0.1644 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 36855 | 0.1817 | 0.5406 | 0.0278 | 0.5989 | 0.6251 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 36873 | 0.2176 | 0.6261 | 0.0178 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 71862 | 0.1575 | 0.4814 | 0.0126 | 0.2320 | 0.2352 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 111760 | 0.1027 | 0.3417 | 0.0083 | 0.1219 | 0.1284 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 93662 | 0.1667 | 0.5020 | 0.0092 | 0.2866 | 0.2911 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 41160 | 0.1774 | 0.5325 | 0.0195 | 0.4193 | 0.4361 |
| team_total | MARKET_BASELINE | 41135 | 0.1751 | 0.5266 | 0.0193 | 0.4272 | 0.4363 |
| team_total | MARKET_ANCHORED_V1 | 41135 | 0.1753 | 0.5271 | 0.0169 | 0.4256 | 0.4363 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
