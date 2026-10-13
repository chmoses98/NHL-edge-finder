# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-13T02:07:19Z · rows 254166 · pregame 254166 · new 3447

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 46075 | 0.1683 | 0.5060 | 0.0098 | 0.4505 | 0.4533 |
| ALL | MARKET_BASELINE | 212023 | 0.1495 | 0.4596 | 0.0081 | 0.2911 | 0.2919 |
| ALL | MARKET_ANCHORED_V1 | 46061 | 0.1652 | 0.4982 | 0.0093 | 0.4533 | 0.4534 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 10258 | 0.0393 | 0.1689 | 0.0048 | 0.0384 | 0.0410 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 7372 | 0.1890 | 0.5623 | 0.0470 | 0.2318 | 0.2741 |
| game_spread | MARKET_BASELINE | 7372 | 0.1828 | 0.5462 | 0.0389 | 0.2419 | 0.2741 |
| game_spread | MARKET_ANCHORED_V1 | 7372 | 0.1837 | 0.5484 | 0.0379 | 0.2394 | 0.2741 |
| game_total | DATA_ONLY_V1 | 16587 | 0.1296 | 0.4061 | 0.0237 | 0.5694 | 0.5621 |
| game_total | MARKET_BASELINE | 16587 | 0.1271 | 0.3991 | 0.0279 | 0.5720 | 0.5621 |
| game_total | MARKET_ANCHORED_V1 | 16587 | 0.1275 | 0.4001 | 0.0277 | 0.5715 | 0.5621 |
| game_winner | DATA_ONLY_V1 | 3686 | 0.2300 | 0.6525 | 0.1043 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3686 | 0.2261 | 0.6435 | 0.0527 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3686 | 0.2262 | 0.6440 | 0.0380 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 803 | 0.2521 | 0.6986 | 0.0951 | 0.4231 | 0.4134 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 10547 | 0.1480 | 0.4752 | 0.0501 | 0.1306 | 0.1794 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 16398 | 0.1857 | 0.5513 | 0.0258 | 0.5946 | 0.6042 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 16416 | 0.2168 | 0.6243 | 0.0249 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 28762 | 0.1525 | 0.4694 | 0.0201 | 0.2351 | 0.2276 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 46980 | 0.1055 | 0.3506 | 0.0097 | 0.1288 | 0.1308 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 35798 | 0.1671 | 0.5025 | 0.0165 | 0.2999 | 0.2875 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 18430 | 0.1824 | 0.5441 | 0.0342 | 0.4210 | 0.4176 |
| team_total | MARKET_BASELINE | 18416 | 0.1793 | 0.5364 | 0.0298 | 0.4237 | 0.4179 |
| team_total | MARKET_ANCHORED_V1 | 18416 | 0.1797 | 0.5373 | 0.0299 | 0.4231 | 0.4179 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
