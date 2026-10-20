# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-20T07:38:52Z · rows 418465 · pregame 418465 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 74350 | 0.1616 | 0.4893 | 0.0172 | 0.4499 | 0.4584 |
| ALL | MARKET_BASELINE | 344218 | 0.1484 | 0.4568 | 0.0082 | 0.2924 | 0.2961 |
| ALL | MARKET_ANCHORED_V1 | 74332 | 0.1598 | 0.4848 | 0.0167 | 0.4547 | 0.4585 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 15335 | 0.0388 | 0.1668 | 0.0023 | 0.0402 | 0.0404 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 11896 | 0.1810 | 0.5433 | 0.0300 | 0.2316 | 0.2571 |
| game_spread | MARKET_BASELINE | 11896 | 0.1776 | 0.5343 | 0.0243 | 0.2426 | 0.2571 |
| game_spread | MARKET_ANCHORED_V1 | 11896 | 0.1779 | 0.5351 | 0.0212 | 0.2400 | 0.2571 |
| game_total | DATA_ONLY_V1 | 26766 | 0.1256 | 0.3955 | 0.0253 | 0.5686 | 0.5762 |
| game_total | MARKET_BASELINE | 26766 | 0.1245 | 0.3926 | 0.0314 | 0.5749 | 0.5762 |
| game_total | MARKET_ANCHORED_V1 | 26766 | 0.1246 | 0.3927 | 0.0301 | 0.5737 | 0.5762 |
| game_winner | DATA_ONLY_V1 | 5948 | 0.2281 | 0.6485 | 0.1155 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5948 | 0.2256 | 0.6425 | 0.0439 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5948 | 0.2255 | 0.6425 | 0.0507 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1522 | 0.2483 | 0.6901 | 0.0520 | 0.4383 | 0.4225 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 17030 | 0.1353 | 0.4409 | 0.0345 | 0.1294 | 0.1631 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 26577 | 0.1824 | 0.5419 | 0.0281 | 0.5974 | 0.6194 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 26595 | 0.2164 | 0.6234 | 0.0234 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 46684 | 0.1571 | 0.4807 | 0.0188 | 0.2383 | 0.2351 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 75790 | 0.1039 | 0.3460 | 0.0105 | 0.1262 | 0.1294 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 60353 | 0.1680 | 0.5050 | 0.0132 | 0.2977 | 0.2932 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 29740 | 0.1729 | 0.5204 | 0.0143 | 0.4204 | 0.4245 |
| team_total | MARKET_BASELINE | 29722 | 0.1711 | 0.5158 | 0.0167 | 0.4258 | 0.4247 |
| team_total | MARKET_ANCHORED_V1 | 29722 | 0.1712 | 0.5160 | 0.0172 | 0.4247 | 0.4247 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
