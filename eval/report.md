# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-17T04:11:29Z · rows 349171 · pregame 349171 · new 3254

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 62900 | 0.1635 | 0.4937 | 0.0163 | 0.4497 | 0.4630 |
| ALL | MARKET_BASELINE | 291295 | 0.1487 | 0.4576 | 0.0092 | 0.2910 | 0.2973 |
| ALL | MARKET_ANCHORED_V1 | 62883 | 0.1607 | 0.4865 | 0.0148 | 0.4537 | 0.4631 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 13342 | 0.0403 | 0.1718 | 0.0044 | 0.0397 | 0.0421 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 10064 | 0.1812 | 0.5440 | 0.0298 | 0.2316 | 0.2568 |
| game_spread | MARKET_BASELINE | 10064 | 0.1771 | 0.5334 | 0.0216 | 0.2420 | 0.2568 |
| game_spread | MARKET_ANCHORED_V1 | 10064 | 0.1775 | 0.5346 | 0.0213 | 0.2394 | 0.2568 |
| game_total | DATA_ONLY_V1 | 22644 | 0.1274 | 0.3985 | 0.0221 | 0.5684 | 0.5825 |
| game_total | MARKET_BASELINE | 22644 | 0.1245 | 0.3907 | 0.0268 | 0.5732 | 0.5825 |
| game_total | MARKET_ANCHORED_V1 | 22644 | 0.1250 | 0.3919 | 0.0265 | 0.5722 | 0.5825 |
| game_winner | DATA_ONLY_V1 | 5032 | 0.2285 | 0.6495 | 0.1063 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5032 | 0.2257 | 0.6424 | 0.0441 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5032 | 0.2256 | 0.6426 | 0.0428 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1269 | 0.2441 | 0.6817 | 0.0832 | 0.4312 | 0.3940 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 14504 | 0.1400 | 0.4541 | 0.0406 | 0.1297 | 0.1693 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 22455 | 0.1814 | 0.5399 | 0.0292 | 0.5959 | 0.6190 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 22473 | 0.2166 | 0.6238 | 0.0181 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 39965 | 0.1551 | 0.4758 | 0.0167 | 0.2339 | 0.2331 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 63395 | 0.1048 | 0.3485 | 0.0096 | 0.1271 | 0.1306 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 51009 | 0.1680 | 0.5053 | 0.0125 | 0.2950 | 0.2935 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 25160 | 0.1759 | 0.5281 | 0.0215 | 0.4201 | 0.4304 |
| team_total | MARKET_BASELINE | 25143 | 0.1728 | 0.5205 | 0.0167 | 0.4246 | 0.4307 |
| team_total | MARKET_ANCHORED_V1 | 25143 | 0.1732 | 0.5213 | 0.0190 | 0.4236 | 0.4307 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
