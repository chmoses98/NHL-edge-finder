# NHL slate 2026-10-17 — RESEARCH_ONLY

generated 2026-10-18T01:37:25Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 2 · markets on board: 3998 · contracts joined: 436 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 386, 'OK': 22, 'NO_EDGE': 28}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 58, 'game_early_goal': 2, 'first_goal': 74, 'game_winner': 4, 'player_goals': 127, 'game_overtime': 2, 'player_points': 72, 'goalie_saves': 3, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| EDM @ UTA | 2026-10-18T02:00:00Z | T-10m | 0.560 | 0.440 | 0.169 | 6.72 | 3.56 | 3.16 | 221 (25/196) | PROBABLE/CONFIRMED |
| PIT @ VGK | 2026-10-18T02:00:00Z | T-10m | 0.600 | 0.400 | 0.156 | 6.86 | 3.78 | 3.09 | 215 (25/190) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT17PITVGK-PIT | game_winner | 0.400 | 0.335 | 0.348 | 34 | 67 | yes | +0.044 | OK |
| KXNHLSPREAD-26OCT17PITVGK-VGK3 | game_spread | 0.262 | 0.325 | 0.312 | 33 | 68 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT5 | team_total | 0.209 | 0.155 | 0.165 | 16 | 85 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT4 | team_total | 0.382 | 0.325 | 0.336 | 33 | 68 | yes | +0.036 | OK |
| KXNHLGAME-26OCT17PITVGK-VGK | game_winner | 0.600 | 0.655 | 0.644 | 66 | 35 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT17PITVGK-VGK2 | game_spread | 0.395 | 0.445 | 0.435 | 45 | 56 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT3 | team_total | 0.594 | 0.545 | 0.555 | 55 | 46 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT17PITVGK-PIT2 | game_spread | 0.212 | 0.175 | 0.182 | 18 | 83 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT2 | team_total | 0.804 | 0.765 | 0.773 | 77 | 24 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT6 | team_total | 0.095 | 0.065 | 0.070 | 7 | 94 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT17PITVGK-PIT3 | game_spread | 0.124 | 0.095 | 0.100 | 10 | 91 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT17PITVGK-10 | game_total | 0.138 | 0.115 | 0.119 | 12 | 89 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-VGK4 | team_total | 0.533 | 0.565 | 0.559 | 57 | 44 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT17PITVGK-9 | game_total | 0.263 | 0.235 | 0.240 | 24 | 77 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT17EDMUTA-8 | game_total | 0.333 | 0.305 | 0.310 | 31 | 70 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-VGK2 | team_total | 0.888 | 0.910 | 0.906 | 92 | 10 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-VGK3 | team_total | 0.732 | 0.760 | 0.754 | 77 | 25 | no | +0.005 | OK |
| KXNHLGAME-26OCT17EDMUTA-EDM | game_winner | 0.440 | 0.415 | 0.420 | 42 | 59 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT17EDMUTA-9 | game_total | 0.245 | 0.225 | 0.229 | 23 | 78 | yes | +0.003 | OK |
| KXNHLSPREAD-26OCT17EDMUTA-EDM3 | game_spread | 0.148 | 0.165 | 0.162 | 17 | 84 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT17EDMUTA-10 | game_total | 0.129 | 0.115 | 0.118 | 12 | 89 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT17PITVGK-8 | game_total | 0.356 | 0.335 | 0.339 | 34 | 67 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT17EDMUTA-2 | game_total | 0.990 | 0.990 | 0.990 |  | 1 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT17EDMUTA-4 | game_total | 0.895 | 0.905 | 0.903 | 91 | 10 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17PITVGK-VGK5 | team_total | 0.336 | 0.360 | 0.355 | 37 | 65 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM6 | team_total | 0.104 | 0.090 | 0.093 | 10 | 92 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT17PITVGK-2 | game_total | 0.992 | 0.990 | 0.990 |  | 1 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT17PITVGK-3 | game_total | 0.978 | 0.975 | 0.976 | 98 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT17PITVGK-6 | game_total | 0.662 | 0.645 | 0.648 | 65 | 36 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT17EDMUTA-5 | game_total | 0.825 | 0.835 | 0.833 | 84 | 17 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT17EDMUTA-6 | game_total | 0.640 | 0.625 | 0.628 | 63 | 38 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT17EDMUTA-UTA3 | game_spread | 0.224 | 0.235 | 0.233 | 24 | 77 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT17PITVGK-5 | game_total | 0.843 | 0.835 | 0.837 | 84 | 17 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26OCT17EDMUTA-UTA | game_winner | 0.560 | 0.575 | 0.572 | 58 | 43 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM5 | team_total | 0.224 | 0.215 | 0.217 | 22 | 79 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT17EDMUTA-3 | game_total | 0.977 | 0.980 | 0.979 | 99 | 3 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-UTA6 | team_total | 0.149 | 0.140 | 0.142 | 15 | 87 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT17PITVGK-4 | game_total | 0.906 | 0.905 | 0.905 | 91 | 10 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17PITVGK-VGK6 | team_total | 0.180 | 0.185 | 0.184 | 19 | 82 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM2 | team_total | 0.812 | 0.820 | 0.818 | 83 | 19 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-UTA2 | team_total | 0.865 | 0.870 | 0.869 | 88 | 14 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT17PITVGK-7 | game_total | 0.553 | 0.545 | 0.547 | 55 | 46 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT17EDMUTA-UTA2 | game_spread | 0.349 | 0.355 | 0.354 | 36 | 65 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26OCT17EDMUTA-EDM2 | game_spread | 0.243 | 0.245 | 0.245 | 25 | 76 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-UTA5 | team_total | 0.287 | 0.285 | 0.285 | 29 | 72 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26OCT17EDMUTA-7 | game_total | 0.530 | 0.525 | 0.526 | 53 | 48 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-UTA3 | team_total | 0.698 | 0.690 | 0.692 | 70 | 32 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM4 | team_total | 0.399 | 0.395 | 0.396 | 40 | 61 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM3 | team_total | 0.612 | 0.615 | 0.614 | 62 | 39 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-UTA4 | team_total | 0.488 | 0.485 | 0.486 | 49 | 52 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT17EDMUTA-EDM | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT17EDMUTA-TIE | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT17EDMUTA-UTA | period_winner |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT17EDMUTA-EDM2 | period_spread |  | 0.095 |  | 10 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT17EDMUTA-UTA2 | period_spread |  | 0.120 |  | 14 | 90 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT17EDMUTA-1 | period_total |  | 0.845 |  | 85 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT17EDMUTA-2 | period_total |  | 0.585 |  | 60 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT17EDMUTA-3 | period_total |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT17EDMUTA-EDM | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT17EDMUTA-TIE | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT17EDMUTA-UTA | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT17EDMUTA-EDM2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT17EDMUTA-UTA2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT17EDMUTA-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT17EDMUTA-2 | period_total |  | 0.630 |  | 64 | 38 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT17EDMUTA-3 | period_total |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT17EDMUTA-EDM | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT17EDMUTA-TIE | period_winner |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT17EDMUTA-UTA | period_winner |  | 0.405 |  | 42 | 61 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT17EDMUTA-EDM2 | period_spread |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT17EDMUTA-UTA2 | period_spread |  | 0.190 |  | 20 | 82 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT17EDMUTA-1 | period_total |  | 0.920 |  | 94 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT17EDMUTA-2 | period_total |  | 0.680 |  | 69 | 33 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT17EDMUTA-3 | period_total |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-1 | player_assists |  | 0.655 |  | 66 | 35 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-3 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT17EDMUTA-EDMEBOUCHARD2-1 | player_assists |  | 0.575 |  | 58 | 43 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT17EDMUTA-EDMEBOUCHARD2-2 | player_assists |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT17EDMUTA-EDMEBOUCHARD2-3 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| EDM @ UTA | 0.560 | 0.528 | 0.169 | 0.214 | 6.72 | 6.89 | 0.991/1.023 | KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM4 +0.047 |
| PIT @ VGK | 0.600 | 0.630 | 0.156 | 0.204 | 6.86 | 6.49 | 1.004/1.021 | KXNHLTOTAL-26OCT17PITVGK-6 -0.061 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Nate Schmidt: 1+ goals YES @ 4c · p 0.0666 (adj 0.0587) · $3.59 · thesis UTA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 12c · p 0.1626 (adj 0.1507) · $6.23 · thesis UTA:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 71c · p 0.7978 (adj 0.7514) · $20.0 · thesis EDM:SUPPRESSED
- Zach Hyman: 1+ goals YES @ 31c · p 0.358 (adj 0.3448) · $8.77 · thesis EDM:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 68c · p 0.7344 (adj 0.7196) · $18.34 · thesis VGK:SUPPRESSED
- Evgeni Malkin: 1+ assists NO @ 63c · p 0.7155 (adj 0.6703) · $16.04 · thesis PIT:SUPPRESSED
- Bryan Rust: 1+ goals YES @ 24c · p 0.286 (adj 0.272) · $6.04 · thesis PIT:OFFENSE_4PLUS
- Adin Hill: 22+ saves YES @ 49c · p 0.6173 (adj 0.5281) · $9.58 · thesis VGK:NET_HIGH_VOLUME

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**EDM @ UTA** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 27.03, exp saves 23.36 (sd 6.59), pull risk 0.068
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.83, exp saves 23.77 (sd 6.81), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mattias Ekholm: 1+ points | 0.432 | 0.310 | 32/70 | +0.097 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.229 | 0.350 | 36/66 | +0.095 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.450 | 0.570 | 58/44 | +0.093 | STANDARD |
| Connor McDavid: 2+ points | 0.380 | 0.490 | 50/52 | +0.082 | STANDARD |
| Leon Draisaitl: 2+ points | 0.286 | 0.390 | 40/62 | +0.077 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.363 | 0.270 | 28/74 | +0.069 | STANDARD |

**PIT @ VGK** · priced 163/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (CONFIRMED) exp shots 26.53, exp saves 23.38 (sd 6.31), pull risk 0.049
- PIT net: Sergei Murashov (PROJECTED) exp shots 28.1, exp saves 23.73 (sd 6.77), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.469 | 0.615 | 62/39 | +0.125 | STANDARD |
| Jack Eichel: 2+ points | 0.277 | 0.420 | 43/59 | +0.116 | STANDARD |
| Adin Hill: 22+ saves | 0.617 | 0.480 | 49/53 | +0.110 |  |
| Mitch Marner: 2+ points | 0.227 | 0.345 | 36/67 | +0.087 | STANDARD |
| Jack Eichel: 1+ points | 0.639 | 0.755 | 76/25 | +0.097 | STANDARD |
| Jack Eichel: 2+ assists | 0.139 | 0.250 | 26/76 | +0.088 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
