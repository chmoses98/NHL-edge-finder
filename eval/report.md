# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-09T03:54:43Z · rows 176074 · pregame 176074 · new 3040

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 33300 | 0.1664 | 0.5004 | 0.0089 | 0.4500 | 0.4558 |
| ALL | MARKET_BASELINE | 150046 | 0.1514 | 0.4646 | 0.0092 | 0.2929 | 0.2986 |
| ALL | MARKET_ANCHORED_V1 | 33290 | 0.1642 | 0.4949 | 0.0100 | 0.4530 | 0.4559 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 8423 | 0.0409 | 0.1749 | 0.0077 | 0.0371 | 0.0427 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 5328 | 0.1821 | 0.5453 | 0.0389 | 0.2312 | 0.2633 |
| game_spread | MARKET_BASELINE | 5328 | 0.1782 | 0.5356 | 0.0398 | 0.2413 | 0.2633 |
| game_spread | MARKET_ANCHORED_V1 | 5328 | 0.1786 | 0.5366 | 0.0306 | 0.2388 | 0.2633 |
| game_total | DATA_ONLY_V1 | 11988 | 0.1253 | 0.3933 | 0.0270 | 0.5688 | 0.5654 |
| game_total | MARKET_BASELINE | 11988 | 0.1235 | 0.3879 | 0.0313 | 0.5718 | 0.5654 |
| game_total | MARKET_ANCHORED_V1 | 11988 | 0.1237 | 0.3886 | 0.0311 | 0.5712 | 0.5654 |
| game_winner | DATA_ONLY_V1 | 2664 | 0.2332 | 0.6588 | 0.0755 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2664 | 0.2310 | 0.6537 | 0.0575 | 0.4992 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2664 | 0.2308 | 0.6534 | 0.0290 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 577 | 0.2547 | 0.7036 | 0.0749 | 0.4135 | 0.4558 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 7578 | 0.1517 | 0.4841 | 0.0560 | 0.1308 | 0.1850 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 11827 | 0.1818 | 0.5411 | 0.0280 | 0.5942 | 0.6131 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 11850 | 0.2168 | 0.6243 | 0.0283 | 0.3284 | 0.3335 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 19636 | 0.1581 | 0.4840 | 0.0185 | 0.2366 | 0.2363 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 32798 | 0.1095 | 0.3616 | 0.0079 | 0.1326 | 0.1369 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 24067 | 0.1744 | 0.5215 | 0.0201 | 0.3067 | 0.3023 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 13320 | 0.1837 | 0.5470 | 0.0255 | 0.4205 | 0.4252 |
| team_total | MARKET_BASELINE | 13310 | 0.1815 | 0.5418 | 0.0308 | 0.4236 | 0.4255 |
| team_total | MARKET_ANCHORED_V1 | 13310 | 0.1817 | 0.5422 | 0.0292 | 0.4230 | 0.4255 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
