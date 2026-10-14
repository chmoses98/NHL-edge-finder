# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-14T05:06:05Z · rows 295855 · pregame 295855 · new 3336

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 54250 | 0.1657 | 0.4998 | 0.0177 | 0.4495 | 0.4611 |
| ALL | MARKET_BASELINE | 247825 | 0.1493 | 0.4591 | 0.0099 | 0.2915 | 0.2965 |
| ALL | MARKET_ANCHORED_V1 | 54236 | 0.1633 | 0.4934 | 0.0148 | 0.4530 | 0.4612 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 11544 | 0.0395 | 0.1695 | 0.0043 | 0.0390 | 0.0413 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 8680 | 0.1882 | 0.5608 | 0.0410 | 0.2314 | 0.2682 |
| game_spread | MARKET_BASELINE | 8680 | 0.1835 | 0.5489 | 0.0335 | 0.2415 | 0.2682 |
| game_spread | MARKET_ANCHORED_V1 | 8680 | 0.1841 | 0.5503 | 0.0325 | 0.2390 | 0.2682 |
| game_total | DATA_ONLY_V1 | 19530 | 0.1272 | 0.3996 | 0.0226 | 0.5681 | 0.5764 |
| game_total | MARKET_BASELINE | 19530 | 0.1248 | 0.3928 | 0.0278 | 0.5722 | 0.5764 |
| game_total | MARKET_ANCHORED_V1 | 19530 | 0.1251 | 0.3938 | 0.0265 | 0.5713 | 0.5764 |
| game_winner | DATA_ONLY_V1 | 4340 | 0.2312 | 0.6550 | 0.1043 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 4340 | 0.2295 | 0.6507 | 0.0433 | 0.4990 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 4340 | 0.2293 | 0.6503 | 0.0330 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1032 | 0.2441 | 0.6821 | 0.0825 | 0.4240 | 0.3924 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 12509 | 0.1466 | 0.4715 | 0.0486 | 0.1300 | 0.1776 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 19341 | 0.1811 | 0.5397 | 0.0259 | 0.5947 | 0.6137 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 19359 | 0.2171 | 0.6250 | 0.0219 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 33587 | 0.1525 | 0.4687 | 0.0190 | 0.2329 | 0.2290 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 53903 | 0.1058 | 0.3510 | 0.0109 | 0.1277 | 0.1317 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 42314 | 0.1673 | 0.5035 | 0.0147 | 0.2961 | 0.2896 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 21700 | 0.1783 | 0.5345 | 0.0232 | 0.4199 | 0.4268 |
| team_total | MARKET_BASELINE | 21686 | 0.1759 | 0.5285 | 0.0218 | 0.4238 | 0.4270 |
| team_total | MARKET_ANCHORED_V1 | 21686 | 0.1762 | 0.5290 | 0.0260 | 0.4229 | 0.4270 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
