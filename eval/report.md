# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-07T04:51:21Z · rows 140772 · pregame 140772 · new 3112

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 26775 | 0.1683 | 0.5059 | 0.0175 | 0.4487 | 0.4660 |
| ALL | MARKET_BASELINE | 119735 | 0.1549 | 0.4745 | 0.0148 | 0.2967 | 0.3090 |
| ALL | MARKET_ANCHORED_V1 | 26775 | 0.1664 | 0.5011 | 0.0157 | 0.4522 | 0.4660 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 6747 | 0.0407 | 0.1746 | 0.0085 | 0.0364 | 0.0425 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 4284 | 0.1802 | 0.5401 | 0.0387 | 0.2307 | 0.2619 |
| game_spread | MARKET_BASELINE | 4284 | 0.1777 | 0.5339 | 0.0394 | 0.2408 | 0.2619 |
| game_spread | MARKET_ANCHORED_V1 | 4284 | 0.1778 | 0.5341 | 0.0342 | 0.2383 | 0.2619 |
| game_total | DATA_ONLY_V1 | 9639 | 0.1285 | 0.4024 | 0.0319 | 0.5671 | 0.5777 |
| game_total | MARKET_BASELINE | 9639 | 0.1261 | 0.3957 | 0.0242 | 0.5712 | 0.5777 |
| game_total | MARKET_ANCHORED_V1 | 9639 | 0.1264 | 0.3966 | 0.0254 | 0.5704 | 0.5777 |
| game_winner | DATA_ONLY_V1 | 2142 | 0.2298 | 0.6520 | 0.0932 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2142 | 0.2308 | 0.6533 | 0.1089 | 0.4995 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2142 | 0.2299 | 0.6518 | 0.0746 | 0.4996 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 458 | 0.2556 | 0.7051 | 0.0936 | 0.3965 | 0.4782 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 6108 | 0.1593 | 0.5036 | 0.0677 | 0.1304 | 0.1958 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 9584 | 0.1784 | 0.5322 | 0.0368 | 0.5932 | 0.6226 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 9627 | 0.2152 | 0.6207 | 0.0382 | 0.3283 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 16045 | 0.1599 | 0.4875 | 0.0131 | 0.2364 | 0.2439 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 24966 | 0.1177 | 0.3863 | 0.0094 | 0.1414 | 0.1482 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 19425 | 0.1770 | 0.5292 | 0.0223 | 0.3087 | 0.3105 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 10710 | 0.1870 | 0.5561 | 0.0285 | 0.4192 | 0.4402 |
| team_total | MARKET_BASELINE | 10710 | 0.1851 | 0.5516 | 0.0359 | 0.4228 | 0.4402 |
| team_total | MARKET_ANCHORED_V1 | 10710 | 0.1852 | 0.5518 | 0.0329 | 0.4220 | 0.4402 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
