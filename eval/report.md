# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-29T03:36:34Z · rows 674640 · pregame 674640 · new 4521

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 112925 | 0.1663 | 0.5009 | 0.0145 | 0.4491 | 0.4617 |
| ALL | MARKET_BASELINE | 572983 | 0.1445 | 0.4460 | 0.0078 | 0.2779 | 0.2826 |
| ALL | MARKET_ANCHORED_V1 | 112900 | 0.1643 | 0.4958 | 0.0110 | 0.4559 | 0.4618 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 35643 | 0.0353 | 0.1538 | 0.0017 | 0.0360 | 0.0369 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 18068 | 0.1852 | 0.5553 | 0.0293 | 0.2310 | 0.2591 |
| game_spread | MARKET_BASELINE | 18068 | 0.1809 | 0.5432 | 0.0193 | 0.2429 | 0.2591 |
| game_spread | MARKET_ANCHORED_V1 | 18068 | 0.1814 | 0.5446 | 0.0200 | 0.2401 | 0.2591 |
| game_total | DATA_ONLY_V1 | 40653 | 0.1301 | 0.4056 | 0.0218 | 0.5675 | 0.5793 |
| game_total | MARKET_BASELINE | 40653 | 0.1292 | 0.4032 | 0.0213 | 0.5770 | 0.5793 |
| game_total | MARKET_ANCHORED_V1 | 40653 | 0.1292 | 0.4032 | 0.0185 | 0.5751 | 0.5793 |
| game_winner | DATA_ONLY_V1 | 9034 | 0.2353 | 0.6633 | 0.0774 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 9034 | 0.2308 | 0.6533 | 0.0237 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 9034 | 0.2311 | 0.6541 | 0.0311 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2631 | 0.2502 | 0.6940 | 0.0348 | 0.4460 | 0.4493 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 25831 | 0.1336 | 0.4385 | 0.0314 | 0.1288 | 0.1596 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 40464 | 0.1823 | 0.5416 | 0.0208 | 0.5995 | 0.6159 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 40482 | 0.2167 | 0.6241 | 0.0239 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 81605 | 0.1551 | 0.4759 | 0.0139 | 0.2303 | 0.2306 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 126573 | 0.0994 | 0.3324 | 0.0066 | 0.1198 | 0.1237 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 106854 | 0.1640 | 0.4953 | 0.0079 | 0.2831 | 0.2835 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 45170 | 0.1776 | 0.5326 | 0.0154 | 0.4195 | 0.4293 |
| team_total | MARKET_BASELINE | 45145 | 0.1756 | 0.5276 | 0.0171 | 0.4280 | 0.4295 |
| team_total | MARKET_ANCHORED_V1 | 45145 | 0.1758 | 0.5279 | 0.0146 | 0.4262 | 0.4295 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
