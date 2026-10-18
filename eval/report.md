# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-18T01:07:54Z · rows 364066 · pregame 364066 · new 3264

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 65275 | 0.1623 | 0.4909 | 0.0182 | 0.4499 | 0.4639 |
| ALL | MARKET_BASELINE | 302336 | 0.1486 | 0.4576 | 0.0104 | 0.2912 | 0.2979 |
| ALL | MARKET_ANCHORED_V1 | 65257 | 0.1595 | 0.4837 | 0.0170 | 0.4540 | 0.4640 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 14017 | 0.0403 | 0.1718 | 0.0045 | 0.0397 | 0.0421 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 10444 | 0.1803 | 0.5418 | 0.0298 | 0.2318 | 0.2568 |
| game_spread | MARKET_BASELINE | 10444 | 0.1760 | 0.5304 | 0.0210 | 0.2423 | 0.2568 |
| game_spread | MARKET_ANCHORED_V1 | 10444 | 0.1765 | 0.5317 | 0.0210 | 0.2397 | 0.2568 |
| game_total | DATA_ONLY_V1 | 23499 | 0.1267 | 0.3969 | 0.0238 | 0.5686 | 0.5844 |
| game_total | MARKET_BASELINE | 23499 | 0.1242 | 0.3901 | 0.0271 | 0.5735 | 0.5844 |
| game_total | MARKET_ANCHORED_V1 | 23499 | 0.1246 | 0.3911 | 0.0270 | 0.5726 | 0.5844 |
| game_winner | DATA_ONLY_V1 | 5222 | 0.2272 | 0.6468 | 0.1151 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5222 | 0.2232 | 0.6372 | 0.0427 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5222 | 0.2234 | 0.6379 | 0.0537 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1298 | 0.2438 | 0.6812 | 0.0888 | 0.4323 | 0.3867 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 15038 | 0.1411 | 0.4564 | 0.0422 | 0.1298 | 0.1711 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 23310 | 0.1814 | 0.5397 | 0.0312 | 0.5962 | 0.6219 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 23328 | 0.2157 | 0.6220 | 0.0211 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 41272 | 0.1559 | 0.4779 | 0.0180 | 0.2350 | 0.2339 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 66029 | 0.1052 | 0.3499 | 0.0105 | 0.1270 | 0.1309 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 52787 | 0.1687 | 0.5071 | 0.0137 | 0.2962 | 0.2948 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 26110 | 0.1741 | 0.5240 | 0.0195 | 0.4203 | 0.4310 |
| team_total | MARKET_BASELINE | 26092 | 0.1710 | 0.5162 | 0.0168 | 0.4248 | 0.4313 |
| team_total | MARKET_ANCHORED_V1 | 26092 | 0.1714 | 0.5171 | 0.0189 | 0.4239 | 0.4313 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
