# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-02T01:10:55Z · rows 790288 · pregame 790288 · new 11505

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 129975 | 0.1661 | 0.5002 | 0.0217 | 0.4494 | 0.4711 |
| ALL | MARKET_BASELINE | 678162 | 0.1439 | 0.4444 | 0.0118 | 0.2735 | 0.2838 |
| ALL | MARKET_ANCHORED_V1 | 129942 | 0.1635 | 0.4937 | 0.0148 | 0.4564 | 0.4712 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 48111 | 0.0345 | 0.1500 | 0.0023 | 0.0346 | 0.0361 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 20796 | 0.1842 | 0.5525 | 0.0282 | 0.2313 | 0.2583 |
| game_spread | MARKET_BASELINE | 20796 | 0.1791 | 0.5388 | 0.0196 | 0.2435 | 0.2583 |
| game_spread | MARKET_ANCHORED_V1 | 20796 | 0.1798 | 0.5406 | 0.0195 | 0.2406 | 0.2583 |
| game_total | DATA_ONLY_V1 | 46791 | 0.1299 | 0.4046 | 0.0290 | 0.5680 | 0.5920 |
| game_total | MARKET_BASELINE | 46791 | 0.1283 | 0.4004 | 0.0230 | 0.5776 | 0.5920 |
| game_total | MARKET_ANCHORED_V1 | 46791 | 0.1284 | 0.4008 | 0.0237 | 0.5757 | 0.5920 |
| game_winner | DATA_ONLY_V1 | 10398 | 0.2323 | 0.6571 | 0.0731 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 10398 | 0.2277 | 0.6468 | 0.0287 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 10398 | 0.2280 | 0.6477 | 0.0394 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 3024 | 0.2486 | 0.6909 | 0.0348 | 0.4465 | 0.4425 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 29751 | 0.1333 | 0.4372 | 0.0315 | 0.1286 | 0.1596 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 46575 | 0.1789 | 0.5330 | 0.0275 | 0.5993 | 0.6258 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 46620 | 0.2165 | 0.6235 | 0.0257 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 96858 | 0.1578 | 0.4827 | 0.0184 | 0.2294 | 0.2368 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 150252 | 0.1010 | 0.3370 | 0.0082 | 0.1191 | 0.1263 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 127029 | 0.1663 | 0.5015 | 0.0134 | 0.2815 | 0.2900 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 51990 | 0.1783 | 0.5339 | 0.0239 | 0.4199 | 0.4416 |
| team_total | MARKET_BASELINE | 51957 | 0.1754 | 0.5270 | 0.0180 | 0.4285 | 0.4418 |
| team_total | MARKET_ANCHORED_V1 | 51957 | 0.1757 | 0.5277 | 0.0166 | 0.4267 | 0.4418 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
