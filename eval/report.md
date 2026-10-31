# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-31T02:18:52Z · rows 730134 · pregame 730134 · new 3824

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 121725 | 0.1661 | 0.5004 | 0.0185 | 0.4492 | 0.4677 |
| ALL | MARKET_BASELINE | 624739 | 0.1442 | 0.4452 | 0.0097 | 0.2757 | 0.2835 |
| ALL | MARKET_ANCHORED_V1 | 121692 | 0.1640 | 0.4949 | 0.0126 | 0.4562 | 0.4678 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 42061 | 0.0345 | 0.1502 | 0.0016 | 0.0351 | 0.0360 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 19476 | 0.1835 | 0.5513 | 0.0256 | 0.2311 | 0.2556 |
| game_spread | MARKET_BASELINE | 19476 | 0.1793 | 0.5395 | 0.0185 | 0.2431 | 0.2556 |
| game_spread | MARKET_ANCHORED_V1 | 19476 | 0.1798 | 0.5409 | 0.0169 | 0.2403 | 0.2556 |
| game_total | DATA_ONLY_V1 | 43821 | 0.1301 | 0.4058 | 0.0259 | 0.5676 | 0.5878 |
| game_total | MARKET_BASELINE | 43821 | 0.1289 | 0.4024 | 0.0218 | 0.5774 | 0.5878 |
| game_total | MARKET_ANCHORED_V1 | 43821 | 0.1289 | 0.4026 | 0.0204 | 0.5755 | 0.5878 |
| game_winner | DATA_ONLY_V1 | 9738 | 0.2339 | 0.6604 | 0.0819 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 9738 | 0.2300 | 0.6517 | 0.0273 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 9738 | 0.2302 | 0.6523 | 0.0340 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2858 | 0.2490 | 0.6916 | 0.0417 | 0.4466 | 0.4367 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 27859 | 0.1329 | 0.4368 | 0.0307 | 0.1286 | 0.1588 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 43632 | 0.1804 | 0.5365 | 0.0248 | 0.5997 | 0.6225 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 43650 | 0.2165 | 0.6236 | 0.0252 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 88632 | 0.1562 | 0.4788 | 0.0152 | 0.2299 | 0.2327 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 138153 | 0.1003 | 0.3352 | 0.0072 | 0.1192 | 0.1250 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 116202 | 0.1657 | 0.5000 | 0.0102 | 0.2825 | 0.2873 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 48690 | 0.1779 | 0.5331 | 0.0196 | 0.4196 | 0.4380 |
| team_total | MARKET_BASELINE | 48657 | 0.1757 | 0.5278 | 0.0172 | 0.4284 | 0.4383 |
| team_total | MARKET_ANCHORED_V1 | 48657 | 0.1759 | 0.5281 | 0.0155 | 0.4266 | 0.4383 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
