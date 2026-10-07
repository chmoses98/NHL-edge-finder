# NHL slate 2026-10-07 — RESEARCH_ONLY

generated 2026-10-07T23:53:40Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 1 · markets on board: 2879 · contracts joined: 209 (unjoined to any game: 1560)
gates: {'UNSUPPORTED': 184, 'OK': 12, 'NO_EDGE': 13}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 25, 'game_early_goal': 1, 'first_goal': 35, 'game_winner': 2, 'player_goals': 63, 'game_overtime': 1, 'player_points': 33, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| EDM @ ANA | 2026-10-08T02:00:00Z | T-90m | 0.497 | 0.503 | 0.165 | 6.91 | 3.44 | 3.47 | 209 (25/184) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT07EDMANA-ANA | game_winner | 0.497 | 0.445 | 0.455 | 45 | 56 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT07EDMANA-EDM2 | game_spread | 0.299 | 0.345 | 0.335 | 35 | 66 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT07EDMANA-ANA2 | game_spread | 0.294 | 0.255 | 0.263 | 26 | 75 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT07EDMANA-EDM3 | game_spread | 0.189 | 0.225 | 0.217 | 23 | 78 | no | +0.019 | OK |
| KXNHLGAME-26OCT07EDMANA-EDM | game_winner | 0.503 | 0.545 | 0.537 | 55 | 46 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM2 | team_total | 0.851 | 0.875 | 0.871 | 88 | 13 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT07EDMANA-10 | game_total | 0.147 | 0.125 | 0.129 | 13 | 88 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT07EDMANA-5 | game_total | 0.844 | 0.865 | 0.861 | 87 | 14 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA6 | team_total | 0.135 | 0.115 | 0.119 | 12 | 89 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA5 | team_total | 0.271 | 0.245 | 0.250 | 25 | 76 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA4 | team_total | 0.464 | 0.435 | 0.441 | 44 | 57 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT07EDMANA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM3 | team_total | 0.676 | 0.695 | 0.691 | 70 | 31 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-4 | game_total | 0.906 | 0.915 | 0.913 | 92 | 9 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-3 | game_total | 0.979 | 0.975 | 0.976 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-8 | game_total | 0.363 | 0.345 | 0.349 | 35 | 66 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA3 | team_total | 0.671 | 0.650 | 0.654 | 66 | 36 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA2 | team_total | 0.853 | 0.845 | 0.847 | 85 | 16 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT07EDMANA-ANA3 | game_spread | 0.182 | 0.170 | 0.172 | 18 | 84 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM6 | team_total | 0.140 | 0.150 | 0.148 | 16 | 86 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-9 | game_total | 0.274 | 0.265 | 0.267 | 27 | 74 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM5 | team_total | 0.277 | 0.285 | 0.283 | 29 | 72 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-6 | game_total | 0.668 | 0.675 | 0.674 | 68 | 33 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM4 | team_total | 0.467 | 0.475 | 0.473 | 48 | 53 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-7 | game_total | 0.564 | 0.565 | 0.565 | 57 | 44 |  | -0.021 | NO_EDGE |
| KXNHL1P-26OCT07EDMANA-ANA | period_winner |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT07EDMANA-EDM | period_winner |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT07EDMANA-TIE | period_winner |  | 0.310 |  | 33 | 71 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT07EDMANA-ANA2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT07EDMANA-EDM2 | period_spread |  | 0.125 |  | 13 | 88 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT07EDMANA-1 | period_total |  | 0.865 |  | 87 | 14 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT07EDMANA-2 | period_total |  | 0.605 |  | 61 | 40 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT07EDMANA-3 | period_total |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT07EDMANA-ANA | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT07EDMANA-EDM | period_winner |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT07EDMANA-TIE | period_winner |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT07EDMANA-ANA2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT07EDMANA-EDM2 | period_spread |  | 0.160 |  | 17 | 85 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT07EDMANA-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT07EDMANA-2 | period_total |  | 0.660 |  | 67 | 35 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT07EDMANA-3 | period_total |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT07EDMANA-ANA | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT07EDMANA-EDM | period_winner |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT07EDMANA-TIE | period_winner |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT07EDMANA-ANA2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT07EDMANA-EDM2 | period_spread |  | 0.190 |  | 20 | 82 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT07EDMANA-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT07EDMANA-2 | period_total |  | 0.705 |  | 72 | 31 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT07EDMANA-3 | period_total |  | 0.425 |  | 44 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-ANAAKILLORN17-1 | player_assists |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-ANABSENNECKE45-1 | player_assists |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-ANABSENNECKE45-2 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-ANACGAUTHIER61-1 | player_assists |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-ANACGAUTHIER61-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-ANAJLACOMBE2-1 | player_assists |  | 0.485 |  | 49 | 52 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-ANAJLACOMBE2-2 | player_assists |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-ANALCARLSSON91-1 | player_assists |  | 0.445 |  | 45 | 56 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-ANALCARLSSON91-2 | player_assists |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-ANAMGRANLUND64-1 | player_assists |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-ANAMGRANLUND64-2 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-1 | player_assists |  | 0.675 |  | 68 | 33 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-2 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMCMCDAVID97-3 | player_assists |  | 0.100 |  | 11 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMEBOUCHARD2-1 | player_assists |  | 0.600 |  | 61 | 41 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMEBOUCHARD2-2 | player_assists |  | 0.230 |  | 25 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMEBOUCHARD2-3 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMKKAPANEN42-1 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMKKAPANEN42-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMLDRAISAITL29-1 | player_assists |  | 0.575 |  | 58 | 43 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMLDRAISAITL29-2 | player_assists |  | 0.220 |  | 23 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMLDRAISAITL29-3 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMMEKHOLM14-1 | player_assists |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMVPODKOLZIN92-1 | player_assists |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT07EDMANA-EDMVPODKOLZIN92-2 | player_assists |  | 0.075 |  | 8 | 93 |  |  | UNSUPPORTED |
| KXNHLF10G-26OCT07EDMANA-Y | game_early_goal |  | 0.620 |  | 63 | 39 |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26OCT07EDMANA-ANAAGREER18 | first_goal |  | 0.030 |  | 3 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26OCT07EDMANA-ANAAKILLORN17 | first_goal |  | 0.040 |  | 4 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26OCT07EDMANA-ANABSENNECKE45 | first_goal |  | 0.060 |  | 6 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26OCT07EDMANA-ANACGAUTHIER61 | first_goal |  | 0.070 |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26OCT07EDMANA-ANAJCAULFIELD28 | first_goal |  |  |  | 2 |  |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| EDM @ ANA | 0.497 | 0.498 | 0.165 | 0.210 | 6.91 | 6.83 | 1.016/0.994 | KXNHLTOTAL-26OCT07EDMANA-6 -0.019 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Alex Formenton: 1+ goals YES @ 12c · p 0.2143 (adj 0.1895) · $15.81 · thesis EDM:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 17c · p 0.2459 (adj 0.2244) · $12.15 · thesis ANA:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 33c · p 0.4912 (adj 0.3832) · $14.79 · thesis EDM:SUPPRESSED
- Judd Caulfield: 1+ goals YES @ 8c · p 0.1193 (adj 0.107) · $5.14 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**EDM @ ANA** · priced 155/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 28.22, exp saves 24.35 (sd 6.8), pull risk 0.073
- EDM net: Devon Levi (CONFIRMED) exp shots 29.57, exp saves 25.37 (sd 6.92), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.158 | 0.335 | 34/67 | +0.156 | STANDARD |
| Connor McDavid: 1+ assists | 0.509 | 0.675 | 68/33 | +0.146 | STANDARD |
| Connor McDavid: 2+ points | 0.370 | 0.520 | 53/49 | +0.123 | STANDARD |
| Leon Draisaitl: 2+ points | 0.308 | 0.450 | 47/57 | +0.105 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.435 | 0.575 | 58/43 | +0.118 | STANDARD |
| Devon Levi: 24+ saves | 0.613 | 0.495 | 50/51 | +0.095 |  |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
