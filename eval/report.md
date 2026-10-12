# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-12T23:18:01Z · rows 250719 · pregame 250719 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 45550 | 0.1681 | 0.5056 | 0.0103 | 0.4507 | 0.4539 |
| ALL | MARKET_BASELINE | 209141 | 0.1496 | 0.4601 | 0.0086 | 0.2914 | 0.2927 |
| ALL | MARKET_ANCHORED_V1 | 45536 | 0.1650 | 0.4978 | 0.0095 | 0.4534 | 0.4540 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 10161 | 0.0396 | 0.1698 | 0.0051 | 0.0384 | 0.0413 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 7288 | 0.1871 | 0.5575 | 0.0444 | 0.2319 | 0.2715 |
| game_spread | MARKET_BASELINE | 7288 | 0.1808 | 0.5414 | 0.0363 | 0.2420 | 0.2715 |
| game_spread | MARKET_ANCHORED_V1 | 7288 | 0.1817 | 0.5436 | 0.0352 | 0.2394 | 0.2715 |
| game_total | DATA_ONLY_V1 | 16398 | 0.1303 | 0.4078 | 0.0215 | 0.5697 | 0.5635 |
| game_total | MARKET_BASELINE | 16398 | 0.1278 | 0.4007 | 0.0258 | 0.5722 | 0.5635 |
| game_total | MARKET_ANCHORED_V1 | 16398 | 0.1281 | 0.4018 | 0.0256 | 0.5717 | 0.5635 |
| game_winner | DATA_ONLY_V1 | 3644 | 0.2293 | 0.6512 | 0.1117 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3644 | 0.2254 | 0.6420 | 0.0471 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3644 | 0.2255 | 0.6426 | 0.0446 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 787 | 0.2521 | 0.6986 | 0.0976 | 0.4229 | 0.4130 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 10421 | 0.1480 | 0.4752 | 0.0503 | 0.1306 | 0.1795 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 16209 | 0.1855 | 0.5509 | 0.0257 | 0.5947 | 0.6047 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 16227 | 0.2167 | 0.6241 | 0.0245 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 28290 | 0.1531 | 0.4708 | 0.0206 | 0.2355 | 0.2282 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 46284 | 0.1058 | 0.3512 | 0.0095 | 0.1291 | 0.1313 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 35226 | 0.1677 | 0.5039 | 0.0164 | 0.3002 | 0.2890 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 18220 | 0.1822 | 0.5439 | 0.0325 | 0.4213 | 0.4190 |
| team_total | MARKET_BASELINE | 18206 | 0.1791 | 0.5361 | 0.0286 | 0.4239 | 0.4193 |
| team_total | MARKET_ANCHORED_V1 | 18206 | 0.1795 | 0.5370 | 0.0276 | 0.4233 | 0.4193 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
