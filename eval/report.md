# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-15T03:07:58Z · rows 307157 · pregame 307157 · new 3727

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 56050 | 0.1662 | 0.5007 | 0.0206 | 0.4496 | 0.4651 |
| ALL | MARKET_BASELINE | 257487 | 0.1496 | 0.4599 | 0.0104 | 0.2909 | 0.2978 |
| ALL | MARKET_ANCHORED_V1 | 56036 | 0.1639 | 0.4948 | 0.0164 | 0.4533 | 0.4652 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 12099 | 0.0404 | 0.1724 | 0.0050 | 0.0392 | 0.0422 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 8968 | 0.1891 | 0.5625 | 0.0437 | 0.2314 | 0.2710 |
| game_spread | MARKET_BASELINE | 8968 | 0.1851 | 0.5525 | 0.0356 | 0.2414 | 0.2710 |
| game_spread | MARKET_ANCHORED_V1 | 8968 | 0.1855 | 0.5536 | 0.0351 | 0.2390 | 0.2710 |
| game_total | DATA_ONLY_V1 | 20178 | 0.1281 | 0.4013 | 0.0203 | 0.5682 | 0.5815 |
| game_total | MARKET_BASELINE | 20178 | 0.1255 | 0.3940 | 0.0269 | 0.5725 | 0.5815 |
| game_total | MARKET_ANCHORED_V1 | 20178 | 0.1259 | 0.3950 | 0.0258 | 0.5717 | 0.5815 |
| game_winner | DATA_ONLY_V1 | 4484 | 0.2300 | 0.6526 | 0.1151 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 4484 | 0.2292 | 0.6500 | 0.0287 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 4484 | 0.2287 | 0.6493 | 0.0433 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1084 | 0.2457 | 0.6854 | 0.0888 | 0.4245 | 0.3958 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 12941 | 0.1438 | 0.4643 | 0.0448 | 0.1298 | 0.1736 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 19989 | 0.1816 | 0.5403 | 0.0295 | 0.5951 | 0.6202 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 20007 | 0.2170 | 0.6246 | 0.0220 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 35168 | 0.1532 | 0.4707 | 0.0179 | 0.2320 | 0.2299 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 55764 | 0.1059 | 0.3516 | 0.0107 | 0.1275 | 0.1320 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 44399 | 0.1679 | 0.5050 | 0.0136 | 0.2949 | 0.2906 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 22420 | 0.1786 | 0.5351 | 0.0182 | 0.4200 | 0.4311 |
| team_total | MARKET_BASELINE | 22406 | 0.1764 | 0.5297 | 0.0170 | 0.4241 | 0.4313 |
| team_total | MARKET_ANCHORED_V1 | 22406 | 0.1766 | 0.5301 | 0.0195 | 0.4232 | 0.4313 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
