# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-02T23:16:17Z · rows 44633 · pregame 44633 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 7950 | 0.1990 | 0.5869 | 0.0754 | 0.4479 | 0.5057 |
| ALL | MARKET_BASELINE | 38238 | 0.1596 | 0.4857 | 0.0258 | 0.2879 | 0.3066 |
| ALL | MARKET_ANCHORED_V1 | 7950 | 0.1951 | 0.5764 | 0.0635 | 0.4531 | 0.5057 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 2526 | 0.0316 | 0.1445 | 0.0019 | 0.0338 | 0.0325 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 1272 | 0.1992 | 0.5837 | 0.0821 | 0.2308 | 0.2987 |
| game_spread | MARKET_BASELINE | 1272 | 0.1945 | 0.5723 | 0.1049 | 0.2424 | 0.2987 |
| game_spread | MARKET_ANCHORED_V1 | 1272 | 0.1949 | 0.5735 | 0.1031 | 0.2396 | 0.2987 |
| game_total | DATA_ONLY_V1 | 2862 | 0.1577 | 0.4842 | 0.0625 | 0.5660 | 0.6164 |
| game_total | MARKET_BASELINE | 2862 | 0.1520 | 0.4653 | 0.0527 | 0.5724 | 0.6164 |
| game_total | MARKET_ANCHORED_V1 | 2862 | 0.1530 | 0.4687 | 0.0538 | 0.5711 | 0.6164 |
| game_winner | DATA_ONLY_V1 | 636 | 0.2324 | 0.6578 | 0.1362 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 636 | 0.2293 | 0.6514 | 0.2807 | 0.5000 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 636 | 0.2294 | 0.6514 | 0.2357 | 0.5000 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 173 | 0.2651 | 0.7253 | 0.1559 | 0.3825 | 0.4509 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 1805 | 0.1721 | 0.5387 | 0.1050 | 0.1301 | 0.2094 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 2847 | 0.1879 | 0.5547 | 0.0633 | 0.5938 | 0.6572 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 2850 | 0.2135 | 0.6165 | 0.0593 | 0.3292 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 5465 | 0.1530 | 0.4693 | 0.0469 | 0.2300 | 0.2199 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 8053 | 0.1199 | 0.3914 | 0.0237 | 0.1363 | 0.1490 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 6569 | 0.1792 | 0.5310 | 0.0511 | 0.3081 | 0.2955 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 3180 | 0.2294 | 0.6665 | 0.1076 | 0.4181 | 0.4899 |
| team_total | MARKET_BASELINE | 3180 | 0.2257 | 0.6585 | 0.1350 | 0.4243 | 0.4899 |
| team_total | MARKET_ANCHORED_V1 | 3180 | 0.2262 | 0.6594 | 0.1245 | 0.4230 | 0.4899 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
