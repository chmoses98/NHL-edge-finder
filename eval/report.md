# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-17T18:14:22Z · rows 352469 · pregame 352469 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 63475 | 0.1631 | 0.4927 | 0.0161 | 0.4499 | 0.4627 |
| ALL | MARKET_BASELINE | 294155 | 0.1486 | 0.4574 | 0.0097 | 0.2909 | 0.2972 |
| ALL | MARKET_ANCHORED_V1 | 63458 | 0.1603 | 0.4856 | 0.0155 | 0.4538 | 0.4629 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 13603 | 0.0401 | 0.1714 | 0.0042 | 0.0396 | 0.0419 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 10156 | 0.1810 | 0.5436 | 0.0297 | 0.2316 | 0.2567 |
| game_spread | MARKET_BASELINE | 10156 | 0.1769 | 0.5330 | 0.0213 | 0.2419 | 0.2567 |
| game_spread | MARKET_ANCHORED_V1 | 10156 | 0.1774 | 0.5342 | 0.0212 | 0.2394 | 0.2567 |
| game_total | DATA_ONLY_V1 | 22851 | 0.1268 | 0.3971 | 0.0222 | 0.5686 | 0.5823 |
| game_total | MARKET_BASELINE | 22851 | 0.1240 | 0.3894 | 0.0272 | 0.5733 | 0.5823 |
| game_total | MARKET_ANCHORED_V1 | 22851 | 0.1244 | 0.3905 | 0.0269 | 0.5724 | 0.5823 |
| game_winner | DATA_ONLY_V1 | 5078 | 0.2288 | 0.6499 | 0.1069 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5078 | 0.2258 | 0.6427 | 0.0394 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5078 | 0.2258 | 0.6429 | 0.0448 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1285 | 0.2439 | 0.6814 | 0.0862 | 0.4317 | 0.3891 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 14642 | 0.1412 | 0.4572 | 0.0421 | 0.1296 | 0.1708 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 22662 | 0.1811 | 0.5392 | 0.0293 | 0.5960 | 0.6194 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 22680 | 0.2165 | 0.6236 | 0.0191 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 40286 | 0.1552 | 0.4761 | 0.0165 | 0.2339 | 0.2335 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 64027 | 0.1049 | 0.3488 | 0.0094 | 0.1274 | 0.1305 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 51512 | 0.1679 | 0.5050 | 0.0130 | 0.2949 | 0.2934 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 25390 | 0.1754 | 0.5270 | 0.0214 | 0.4203 | 0.4301 |
| team_total | MARKET_BASELINE | 25373 | 0.1723 | 0.5193 | 0.0165 | 0.4247 | 0.4304 |
| team_total | MARKET_ANCHORED_V1 | 25373 | 0.1727 | 0.5202 | 0.0189 | 0.4237 | 0.4304 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
