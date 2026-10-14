# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-14T02:15:09Z · rows 269816 · pregame 269816 · new 7890

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 49175 | 0.1671 | 0.5036 | 0.0127 | 0.4493 | 0.4569 |
| ALL | MARKET_BASELINE | 225598 | 0.1491 | 0.4589 | 0.0093 | 0.2910 | 0.2935 |
| ALL | MARKET_ANCHORED_V1 | 49161 | 0.1638 | 0.4952 | 0.0121 | 0.4529 | 0.4570 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 10811 | 0.0394 | 0.1691 | 0.0045 | 0.0387 | 0.0412 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 7868 | 0.1859 | 0.5555 | 0.0398 | 0.2313 | 0.2674 |
| game_spread | MARKET_BASELINE | 7868 | 0.1799 | 0.5398 | 0.0321 | 0.2415 | 0.2674 |
| game_spread | MARKET_ANCHORED_V1 | 7868 | 0.1807 | 0.5420 | 0.0313 | 0.2390 | 0.2674 |
| game_total | DATA_ONLY_V1 | 17703 | 0.1300 | 0.4073 | 0.0205 | 0.5678 | 0.5696 |
| game_total | MARKET_BASELINE | 17703 | 0.1271 | 0.3991 | 0.0251 | 0.5719 | 0.5696 |
| game_total | MARKET_ANCHORED_V1 | 17703 | 0.1275 | 0.4003 | 0.0245 | 0.5711 | 0.5696 |
| game_winner | DATA_ONLY_V1 | 3934 | 0.2308 | 0.6541 | 0.1056 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3934 | 0.2265 | 0.6443 | 0.0561 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3934 | 0.2267 | 0.6450 | 0.0355 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 876 | 0.2506 | 0.6955 | 0.0876 | 0.4241 | 0.4178 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 11291 | 0.1472 | 0.4730 | 0.0496 | 0.1302 | 0.1785 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 17514 | 0.1832 | 0.5452 | 0.0289 | 0.5944 | 0.6069 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 17532 | 0.2168 | 0.6242 | 0.0250 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 30641 | 0.1522 | 0.4684 | 0.0199 | 0.2337 | 0.2272 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 49540 | 0.1055 | 0.3505 | 0.0106 | 0.1283 | 0.1309 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 38232 | 0.1675 | 0.5039 | 0.0172 | 0.2983 | 0.2875 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 19670 | 0.1802 | 0.5395 | 0.0274 | 0.4197 | 0.4226 |
| team_total | MARKET_BASELINE | 19656 | 0.1768 | 0.5308 | 0.0240 | 0.4236 | 0.4228 |
| team_total | MARKET_ANCHORED_V1 | 19656 | 0.1772 | 0.5319 | 0.0257 | 0.4227 | 0.4228 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
