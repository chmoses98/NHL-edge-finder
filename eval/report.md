# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-14T07:51:02Z · rows 303430 · pregame 303430 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 55525 | 0.1662 | 0.5009 | 0.0196 | 0.4495 | 0.4635 |
| ALL | MARKET_BASELINE | 254361 | 0.1496 | 0.4600 | 0.0102 | 0.2911 | 0.2975 |
| ALL | MARKET_ANCHORED_V1 | 55511 | 0.1640 | 0.4951 | 0.0154 | 0.4531 | 0.4636 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 11795 | 0.0404 | 0.1724 | 0.0052 | 0.0391 | 0.0423 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 8884 | 0.1903 | 0.5653 | 0.0463 | 0.2314 | 0.2735 |
| game_spread | MARKET_BASELINE | 8884 | 0.1863 | 0.5551 | 0.0382 | 0.2414 | 0.2735 |
| game_spread | MARKET_ANCHORED_V1 | 8884 | 0.1867 | 0.5562 | 0.0378 | 0.2389 | 0.2735 |
| game_total | DATA_ONLY_V1 | 19989 | 0.1275 | 0.4000 | 0.0216 | 0.5681 | 0.5786 |
| game_total | MARKET_BASELINE | 19989 | 0.1251 | 0.3932 | 0.0269 | 0.5722 | 0.5786 |
| game_total | MARKET_ANCHORED_V1 | 19989 | 0.1254 | 0.3942 | 0.0256 | 0.5714 | 0.5786 |
| game_winner | DATA_ONLY_V1 | 4442 | 0.2303 | 0.6532 | 0.1119 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 4442 | 0.2293 | 0.6502 | 0.0334 | 0.4990 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 4442 | 0.2289 | 0.6496 | 0.0393 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1068 | 0.2459 | 0.6858 | 0.0908 | 0.4239 | 0.3942 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 12815 | 0.1451 | 0.4676 | 0.0464 | 0.1299 | 0.1753 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 19800 | 0.1817 | 0.5409 | 0.0288 | 0.5948 | 0.6176 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 19818 | 0.2169 | 0.6245 | 0.0231 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 34673 | 0.1531 | 0.4705 | 0.0194 | 0.2320 | 0.2299 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 55159 | 0.1059 | 0.3515 | 0.0106 | 0.1276 | 0.1320 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 43722 | 0.1673 | 0.5034 | 0.0152 | 0.2952 | 0.2904 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 22210 | 0.1787 | 0.5353 | 0.0185 | 0.4199 | 0.4285 |
| team_total | MARKET_BASELINE | 22196 | 0.1766 | 0.5303 | 0.0179 | 0.4238 | 0.4288 |
| team_total | MARKET_ANCHORED_V1 | 22196 | 0.1768 | 0.5306 | 0.0214 | 0.4230 | 0.4288 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
