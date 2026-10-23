# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-23T08:33:41Z · rows 508156 · pregame 508156 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 88850 | 0.1616 | 0.4890 | 0.0175 | 0.4491 | 0.4622 |
| ALL | MARKET_BASELINE | 417413 | 0.1484 | 0.4565 | 0.0078 | 0.2906 | 0.2958 |
| ALL | MARKET_ANCHORED_V1 | 88825 | 0.1602 | 0.4854 | 0.0146 | 0.4549 | 0.4623 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 18043 | 0.0397 | 0.1694 | 0.0027 | 0.0408 | 0.0416 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 14216 | 0.1812 | 0.5447 | 0.0248 | 0.2312 | 0.2544 |
| game_spread | MARKET_BASELINE | 14216 | 0.1783 | 0.5366 | 0.0257 | 0.2428 | 0.2544 |
| game_spread | MARKET_ANCHORED_V1 | 14216 | 0.1785 | 0.5372 | 0.0186 | 0.2400 | 0.2544 |
| game_total | DATA_ONLY_V1 | 31986 | 0.1238 | 0.3897 | 0.0302 | 0.5675 | 0.5815 |
| game_total | MARKET_BASELINE | 31986 | 0.1229 | 0.3874 | 0.0279 | 0.5754 | 0.5815 |
| game_total | MARKET_ANCHORED_V1 | 31986 | 0.1230 | 0.3874 | 0.0277 | 0.5738 | 0.5815 |
| game_winner | DATA_ONLY_V1 | 7108 | 0.2313 | 0.6551 | 0.0956 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 7108 | 0.2303 | 0.6520 | 0.0348 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 7108 | 0.2299 | 0.6514 | 0.0270 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1917 | 0.2510 | 0.6954 | 0.0579 | 0.4440 | 0.4450 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 20304 | 0.1376 | 0.4484 | 0.0385 | 0.1287 | 0.1655 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 31797 | 0.1801 | 0.5365 | 0.0276 | 0.5979 | 0.6225 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 31815 | 0.2172 | 0.6252 | 0.0208 | 0.3278 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 58335 | 0.1555 | 0.4767 | 0.0191 | 0.2344 | 0.2311 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 90633 | 0.1032 | 0.3433 | 0.0078 | 0.1255 | 0.1290 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 75744 | 0.1671 | 0.5027 | 0.0111 | 0.2915 | 0.2890 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 35540 | 0.1738 | 0.5229 | 0.0127 | 0.4194 | 0.4303 |
| team_total | MARKET_BASELINE | 35515 | 0.1725 | 0.5199 | 0.0157 | 0.4262 | 0.4306 |
| team_total | MARKET_ANCHORED_V1 | 35515 | 0.1725 | 0.5198 | 0.0187 | 0.4248 | 0.4306 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
