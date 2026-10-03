# NHL slate 2026-10-03 — RESEARCH_ONLY

generated 2026-10-03T22:14:41Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 13 · simulated (not started): 13 · markets on board: 4134 · contracts joined: 2235 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 1910, 'OK': 188, 'NO_EDGE': 137}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'player_assists': 297, 'game_early_goal': 13, 'first_goal': 452, 'game_winner': 26, 'player_goals': 451, 'game_overtime': 13, 'player_points': 357, 'goalie_saves': 15, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 2026-10-03T23:00:00Z | T-30m | 0.654 | 0.346 | 0.171 | 6.07 | 3.53 | 2.54 | 160 (25/135) | PROBABLE/CONFIRMED |
| OTT @ TOR | 2026-10-03T23:00:00Z | T-30m | 0.462 | 0.538 | 0.170 | 6.70 | 3.22 | 3.48 | 184 (25/159) | PROBABLE/PROBABLE |
| WSH @ TBL | 2026-10-03T23:00:00Z | T-30m | 0.631 | 0.369 | 0.176 | 6.19 | 3.50 | 2.68 | 182 (25/157) | PROBABLE/CONFIRMED |
| CAR @ PHI | 2026-10-03T23:00:00Z | T-30m | 0.469 | 0.531 | 0.182 | 5.84 | 2.83 | 3.01 | 189 (25/164) | CONFIRMED/CONFIRMED |
| MTL @ PIT | 2026-10-03T23:00:00Z | T-30m | 0.545 | 0.455 | 0.168 | 6.53 | 3.40 | 3.13 | 167 (25/142) | CONFIRMED/CONFIRMED |
| UTA @ CBJ | 2026-10-03T23:00:00Z | T-30m | 0.540 | 0.460 | 0.182 | 6.10 | 3.16 | 2.94 | 173 (25/148) | PROJECTED/PROJECTED |
| SEA @ EDM | 2026-10-03T23:00:00Z | T-30m | 0.616 | 0.384 | 0.169 | 6.65 | 3.72 | 2.94 | 180 (25/155) | PROJECTED/PROJECTED |
| NJD @ NYI | 2026-10-03T23:30:00Z | T-60m | 0.537 | 0.463 | 0.190 | 5.65 | 2.94 | 2.70 | 172 (25/147) | CONFIRMED/CONFIRMED |
| DAL @ NSH | 2026-10-04T00:00:00Z | T-90m | 0.490 | 0.510 | 0.181 | 5.96 | 2.95 | 3.01 | 165 (25/140) | PROBABLE/CONFIRMED |
| BOS @ MIN | 2026-10-04T00:00:00Z | T-90m | 0.638 | 0.362 | 0.165 | 6.31 | 3.59 | 2.72 | 171 (25/146) | CONFIRMED/PROJECTED |
| STL @ COL | 2026-10-04T01:00:00Z | T-90m | 0.665 | 0.335 | 0.153 | 6.73 | 3.93 | 2.80 | 169 (25/144) | PROBABLE/PROBABLE |
| CGY @ VAN | 2026-10-04T02:00:00Z | T-3h | 0.468 | 0.532 | 0.174 | 6.29 | 3.04 | 3.25 | 160 (25/135) | PROBABLE/CONFIRMED |
| LAK @ SJS | 2026-10-04T02:00:00Z | T-3h | 0.490 | 0.510 | 0.174 | 6.11 | 3.02 | 3.09 | 163 (25/138) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ3 | team_total | 0.514 | 0.625 | 0.603 | 63 | 38 | no | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4 | team_total | 0.295 | 0.405 | 0.382 | 41 | 60 | no | +0.089 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ2 | game_spread | 0.233 | 0.335 | 0.313 | 34 | 67 | no | +0.081 | OK |
| KXNHLGAME-26OCT03NJNYI-NJ | game_winner | 0.463 | 0.565 | 0.545 | 57 | 44 | no | +0.079 | OK |
| KXNHLGAME-26OCT03NJNYI-NYI | game_winner | 0.537 | 0.435 | 0.455 | 44 | 57 | yes | +0.079 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ3 | game_spread | 0.130 | 0.215 | 0.195 | 22 | 79 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT4 | team_total | 0.473 | 0.385 | 0.402 | 39 | 62 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ2 | team_total | 0.746 | 0.830 | 0.815 | 84 | 18 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5 | team_total | 0.140 | 0.215 | 0.198 | 22 | 79 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT03NJNYI-6 | game_total | 0.465 | 0.545 | 0.529 | 55 | 46 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-8 | game_total | 0.331 | 0.255 | 0.269 | 26 | 75 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL4 | team_total | 0.318 | 0.240 | 0.255 | 25 | 77 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-6 | game_total | 0.639 | 0.565 | 0.580 | 57 | 44 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-7 | game_total | 0.529 | 0.455 | 0.470 | 46 | 55 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT03NJNYI-5 | game_total | 0.697 | 0.765 | 0.752 | 77 | 24 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL3 | team_total | 0.525 | 0.450 | 0.465 | 46 | 56 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT03STLCOL-8 | game_total | 0.341 | 0.275 | 0.288 | 28 | 73 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT5 | team_total | 0.277 | 0.210 | 0.222 | 22 | 80 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT2 | game_spread | 0.329 | 0.265 | 0.277 | 27 | 74 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL5 | team_total | 0.162 | 0.105 | 0.115 | 11 | 90 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT03NJNYI-7 | game_total | 0.359 | 0.425 | 0.411 | 43 | 58 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-6 | game_total | 0.539 | 0.605 | 0.592 | 61 | 40 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-9 | game_total | 0.245 | 0.185 | 0.196 | 19 | 82 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT3 | team_total | 0.680 | 0.605 | 0.621 | 62 | 41 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL4 | team_total | 0.369 | 0.435 | 0.422 | 44 | 57 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF3 | team_total | 0.695 | 0.755 | 0.744 | 76 | 25 | no | +0.042 | OK |
| KXNHLGAME-26OCT03UTACBJ-UTA | game_winner | 0.460 | 0.525 | 0.512 | 53 | 48 | no | +0.042 | OK |
| KXNHLGAME-26OCT03UTACBJ-CBJ | game_winner | 0.540 | 0.475 | 0.488 | 48 | 53 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NYI2 | game_spread | 0.305 | 0.245 | 0.256 | 25 | 76 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF4 | team_total | 0.481 | 0.545 | 0.532 | 55 | 46 | no | +0.041 | OK |
| KXNHLGAME-26OCT03STLCOL-COL | game_winner | 0.665 | 0.725 | 0.713 | 73 | 28 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL3 | team_total | 0.586 | 0.650 | 0.638 | 66 | 36 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-5 | game_total | 0.751 | 0.805 | 0.795 | 81 | 20 | no | +0.037 | OK |
| KXNHLGAME-26OCT03MTLPIT-MTL | game_winner | 0.455 | 0.515 | 0.503 | 52 | 49 | no | +0.037 | OK |
| KXNHLGAME-26OCT03MTLPIT-PIT | game_winner | 0.545 | 0.485 | 0.497 | 49 | 52 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT03STLCOL-9 | game_total | 0.247 | 0.190 | 0.201 | 20 | 82 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT03STLCOL-6 | game_total | 0.643 | 0.585 | 0.597 | 59 | 42 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-7 | game_total | 0.427 | 0.490 | 0.477 | 50 | 52 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT03STLCOL-7 | game_total | 0.533 | 0.475 | 0.487 | 48 | 53 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL2 | game_spread | 0.458 | 0.515 | 0.503 | 52 | 49 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT03STLCOL-10 | game_total | 0.131 | 0.085 | 0.093 | 9 | 92 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT6 | team_total | 0.141 | 0.085 | 0.094 | 10 | 93 | yes | +0.035 | OK |
| KXNHLGAME-26OCT03CGYVAN-VAN | game_winner | 0.468 | 0.525 | 0.514 | 53 | 48 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT03NJNYI-4 | game_total | 0.797 | 0.850 | 0.840 | 86 | 16 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-OTT2 | game_spread | 0.328 | 0.275 | 0.285 | 28 | 73 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL3 | game_spread | 0.320 | 0.375 | 0.364 | 38 | 63 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL2 | team_total | 0.757 | 0.700 | 0.712 | 71 | 31 | yes | +0.033 | OK |
| KXNHLGAME-26OCT03DALNSH-DAL | game_winner | 0.510 | 0.565 | 0.554 | 57 | 44 | no | +0.033 | OK |
| KXNHLGAME-26OCT03DALNSH-NSH | game_winner | 0.490 | 0.435 | 0.446 | 44 | 57 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF5 | team_total | 0.283 | 0.340 | 0.328 | 35 | 67 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL2 | game_spread | 0.254 | 0.305 | 0.294 | 31 | 70 | no | +0.032 | OK |
| KXNHLGAME-26OCT03STLCOL-STL | game_winner | 0.335 | 0.285 | 0.295 | 29 | 72 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT03UTACBJ-UTA2 | game_spread | 0.254 | 0.305 | 0.294 | 31 | 70 | no | +0.031 | OK |
| KXNHLGAME-26OCT03OTTTOR-OTT | game_winner | 0.538 | 0.485 | 0.496 | 49 | 52 | yes | +0.031 | OK |
| KXNHLGAME-26OCT03OTTTOR-TOR | game_winner | 0.462 | 0.515 | 0.504 | 52 | 49 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-10 | game_total | 0.126 | 0.080 | 0.088 | 9 | 93 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL3 | game_spread | 0.168 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL2 | game_spread | 0.285 | 0.335 | 0.325 | 34 | 67 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ6 | team_total | 0.055 | 0.095 | 0.085 | 10 | 91 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT03STLCOL-STL2 | game_spread | 0.167 | 0.125 | 0.133 | 13 | 88 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL5 | team_total | 0.189 | 0.240 | 0.229 | 25 | 77 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT03DALNSH-5 | game_total | 0.741 | 0.785 | 0.777 | 79 | 22 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-TOR3 | game_spread | 0.152 | 0.195 | 0.186 | 20 | 81 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL3 | game_spread | 0.152 | 0.195 | 0.186 | 20 | 81 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL6 | team_total | 0.069 | 0.035 | 0.040 | 4 | 97 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT3 | game_spread | 0.206 | 0.165 | 0.173 | 17 | 84 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT03NJNYI-9 | game_total | 0.125 | 0.165 | 0.156 | 17 | 84 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL2 | team_total | 0.795 | 0.840 | 0.832 | 85 | 17 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT03CARPHI-6 | game_total | 0.498 | 0.545 | 0.536 | 55 | 46 | no | +0.025 | OK |
| KXNHLGAME-26OCT03CGYVAN-CGY | game_winner | 0.532 | 0.485 | 0.494 | 49 | 52 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT6 | team_total | 0.130 | 0.095 | 0.101 | 10 | 91 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT03NJNYI-8 | game_total | 0.185 | 0.230 | 0.220 | 24 | 78 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT03UTACBJ-UTA4 | team_total | 0.350 | 0.405 | 0.394 | 42 | 61 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT03DALNSH-4 | game_total | 0.829 | 0.865 | 0.858 | 87 | 14 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT03CARPHI-5 | game_total | 0.726 | 0.765 | 0.757 | 77 | 24 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-4 | game_total | 0.841 | 0.880 | 0.873 | 89 | 13 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT03CHIBUF-BUF3 | game_spread | 0.284 | 0.325 | 0.316 | 33 | 68 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT03UTACBJ-UTA3 | game_spread | 0.149 | 0.185 | 0.177 | 19 | 82 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT3 | team_total | 0.667 | 0.625 | 0.634 | 63 | 38 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-OTT3 | game_spread | 0.211 | 0.175 | 0.182 | 18 | 83 | yes | +0.020 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 0.654 | 0.629 | 0.171 | 0.208 | 6.07 | 6.31 | 1.000/0.987 | KXNHLTOTAL-26OCT03CHIBUF-7 +0.046 |
| OTT @ TOR | 0.462 | 0.451 | 0.170 | 0.217 | 6.70 | 6.11 | 0.983/0.982 | KXNHLTOTAL-26OCT03OTTTOR-6 -0.099 |
| WSH @ TBL | 0.631 | 0.606 | 0.176 | 0.209 | 6.19 | 6.25 | 0.951/1.015 | KXNHLTEAMTOTAL-26OCT03WSHTB-WSH3 +0.032 |
| CAR @ PHI | 0.469 | 0.540 | 0.182 | 0.219 | 5.84 | 5.93 | 0.990/1.002 | KXNHLGAME-26OCT03CARPHI-PHI +0.071 |
| MTL @ PIT | 0.545 | 0.559 | 0.168 | 0.213 | 6.53 | 6.60 | 1.042/0.942 | KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4 +0.022 |
| UTA @ CBJ | 0.540 | 0.544 | 0.182 | 0.219 | 6.10 | 6.32 | 0.964/0.992 | KXNHLTOTAL-26OCT03UTACBJ-7 +0.040 |
| SEA @ EDM | 0.616 | 0.620 | 0.169 | 0.202 | 6.65 | 6.55 | 1.009/1.005 | KXNHLTOTAL-26OCT03SEAEDM-8 -0.020 |
| NJD @ NYI | 0.537 | 0.535 | 0.190 | 0.223 | 5.65 | 5.87 | 0.947/0.995 | KXNHLTOTAL-26OCT03NJNYI-5 +0.040 |
| DAL @ NSH | 0.490 | 0.527 | 0.181 | 0.222 | 5.96 | 6.07 | 1.002/0.968 | KXNHLTEAMTOTAL-26OCT03DALNSH-NSH4 +0.043 |
| BOS @ MIN | 0.638 | 0.624 | 0.165 | 0.208 | 6.31 | 6.40 | 0.991/0.986 | KXNHLTEAMTOTAL-26OCT03BOSMIN-BOS4 +0.021 |
| STL @ COL | 0.665 | 0.634 | 0.153 | 0.200 | 6.73 | 6.42 | 0.977/1.024 | KXNHLTEAMTOTAL-26OCT03STLCOL-COL5 -0.062 |
| CGY @ VAN | 0.468 | 0.555 | 0.174 | 0.218 | 6.29 | 6.33 | 1.030/0.978 | KXNHLGAME-26OCT03CGYVAN-CGY -0.086 |
| LAK @ SJS | 0.490 | 0.522 | 0.174 | 0.222 | 6.11 | 6.12 | 1.039/0.988 | KXNHLSPREAD-26OCT03LASJ-LA2 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 46 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Greene: 1+ goals YES @ 12c · p 0.1722 (adj 0.1579) · $2.11 · thesis CHI:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 57c · p 0.6512 (adj 0.6297) · $5.46 · thesis BUF:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 62c · p 0.7506 (adj 0.6592) · $5.35 · thesis CHI:SUPPRESSED
- Stephen Halliday: 1+ goals YES @ 9c · p 0.1341 (adj 0.1218) · $1.82 · thesis OTT:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 9c · p 0.1284 (adj 0.1175) · $1.48 · thesis TOR:OFFENSE_4PLUS
- Auston Matthews: 1+ goals NO @ 64c · p 0.6911 (adj 0.6771) · $4.27 · thesis TOR:SUPPRESSED
- William Eklund: 1+ assists NO @ 66c · p 0.7355 (adj 0.6953) · $4.99 · thesis OTT:SUPPRESSED
- John Carlson: 1+ assists NO @ 48c · p 0.7462 (adj 0.5667) · $5.48 · thesis TBL:SUPPRESSED
- John Carlson: 1+ points NO @ 40c · p 0.6572 (adj 0.4606) · $1.64 · thesis TBL:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 16c · p 0.2112 (adj 0.1971) · $2.08 · thesis WSH:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 9c · p 0.1743 (adj 0.152) · $3.5 · thesis PHI:OFFENSE_4PLUS
- Noel Acciari: 1+ goals YES @ 8c · p 0.1347 (adj 0.1198) · $2.18 · thesis PHI:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 17c · p 0.2147 (adj 0.2023) · $1.69 · thesis PHI:OFFENSE_4PLUS
- William Carrier: 1+ goals YES @ 9c · p 0.1218 (adj 0.1126) · $1.16 · thesis CAR:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.2013 (adj 0.1797) · $3.49 · thesis PIT:WINS_BY_2PLUS
- Filip Hallander: 1+ goals YES @ 13c · p 0.2022 (adj 0.1829) · $3.08 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 29c · p 0.3739 (adj 0.3517) · $4.2 · thesis PIT:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 66c · p 0.8619 (adj 0.7274) · $5.48 · thesis UTA:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 20c · p 0.2706 (adj 0.2517) · $3.29 · thesis CBJ:OFFENSE_4PLUS
- Danton Heinen: 1+ goals YES @ 9c · p 0.1317 (adj 0.12) · $1.65 · thesis CBJ:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 18c · p 0.2202 (adj 0.2089) · $1.5 · thesis UTA:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 17c · p 0.2346 (adj 0.2172) · $3.14 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 32c · p 0.4807 (adj 0.373) · $3.98 · thesis EDM:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 10c · p 0.141 (adj 0.1295) · $1.54 · thesis SEA:OFFENSE_4PLUS
- Freddy Gaudreau: 1+ goals YES @ 9c · p 0.1234 (adj 0.1138) · $1.26 · thesis SEA:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 63c · p 0.695 (adj 0.6775) · $4.82 · thesis NJD:SUPPRESSED
- New Jersey wins NO @ 44c · p 0.5332 (adj 0.489) · $3.51 · thesis NYI:WINS
- Kyle Palmieri: 1+ assists NO @ 69c · p 0.8241 (adj 0.7304) · $5.35 · thesis NYI:SUPPRESSED
- Miro Heiskanen: 1+ goals NO @ 86c · p 0.9035 (adj 0.8914) · $5.12 · thesis DAL:SUPPRESSED
- Dallas wins by over 1.5 goals NO @ 67c · p 0.745 (adj 0.705) · $3.31 · thesis NSH:WINS
- Mavrik Bourque: 1+ goals YES @ 18c · p 0.2161 (adj 0.2058) · $1.09 · thesis NSH:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 71c · p 0.7519 (adj 0.7402) · $3.09 · thesis DAL:SUPPRESSED
- Yakov Trenin: 1+ goals YES @ 11c · p 0.1544 (adj 0.1421) · $1.79 · thesis MIN:OFFENSE_4PLUS
- JJ Peterka: 1+ assists NO @ 71c · p 0.8301 (adj 0.7455) · $5.48 · thesis BOS:SUPPRESSED
- Elias Lindholm: 1+ goals YES @ 19c · p 0.2232 (adj 0.2137) · $1.31 · thesis BOS:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 52c · p 0.6063 (adj 0.5835) · $5.48 · thesis COL:SUPPRESSED
- Pius Suter: 1+ goals YES @ 10c · p 0.1483 (adj 0.135) · $1.88 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 24c · p 0.2883 (adj 0.275) · $1.81 · thesis STL:OFFENSE_4PLUS
- Colorado wins by over 2.5 goals NO @ 63c · p 0.7154 (adj 0.6702) · $1.91 · thesis GAME:TIGHT
- Paul Cotter: 1+ goals NO @ 82c · p 0.8723 (adj 0.858) · $5.48 · thesis VAN:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 17c · p 0.2226 (adj 0.2082) · $2.25 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 25c · p 0.3095 (adj 0.2934) · $2.74 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 22c · p 0.2631 (adj 0.2511) · $1.64 · thesis VAN:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 58c · p 0.8194 (adj 0.6605) · $5.4 · thesis LAK:SUPPRESSED
- Mats Zuccarello: 2+ assists NO @ 89c · p 0.9841 (adj 0.9345) · $5.4 · thesis DIFFUSE
- Kiefer Sherwood: 1+ goals YES @ 13c · p 0.1968 (adj 0.1789) · $2.89 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BUF** · priced 101/109 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 24.71, exp saves 21.76 (sd 6.01), pull risk 0.051
- CHI net: Spencer Knight (CONFIRMED) exp shots 30.42, exp saves 25.7 (sd 7.15), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.249 | 0.390 | 40/62 | +0.114 | STANDARD |
| Ukko-Pekka Luukkonen: 21+ saves | 0.575 | 0.460 | 90/98 | -0.332 |  |
| Tage Thompson: 2+ points | 0.216 | 0.325 | 33/68 | +0.089 | STANDARD |
| Patrick Kane: 1+ points | 0.434 | 0.525 | 54/49 | +0.059 | STANDARD |
| Tage Thompson: 1+ points | 0.580 | 0.670 | 68/34 | +0.064 | STANDARD |
| Tage Thompson: 1+ goals | 0.349 | 0.435 | 44/57 | +0.064 | STANDARD |

**OTT @ TOR** · priced 131/133 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 31.35, exp saves 27.01 (sd 7.12), pull risk 0.066
- OTT net: Linus Ullmark (PROBABLE) exp shots 24.74, exp saves 21.69 (sd 5.97), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darren Raddysh: 1+ points | 0.383 | 0.525 | 53/48 | +0.119 | STANDARD |
| Darren Raddysh: 1+ assists | 0.290 | 0.425 | 43/58 | +0.113 | STANDARD |
| Kirill Marchenko: 1+ points | 0.461 | 0.575 | 59/44 | +0.082 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.272 | 0.385 | 39/62 | +0.091 | STANDARD |
| Auston Matthews: 1+ assists | 0.304 | 0.415 | 43/60 | +0.079 | STANDARD |
| Auston Matthews: 1+ points | 0.516 | 0.615 | 63/40 | +0.067 | STANDARD |

**WSH @ TBL** · priced 129/131 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 25.03, exp saves 21.89 (sd 6.08), pull risk 0.05
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.7, exp saves 24.45 (sd 6.85), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.254 | 0.530 | 54/48 | +0.249 | STANDARD |
| John Carlson: 1+ points | 0.343 | 0.605 | 61/40 | +0.240 | STANDARD |
| John Carlson: 2+ points | 0.069 | 0.240 | 26/78 | +0.139 | STANDARD |
| Andrei Vasilevskiy: 24+ saves | 0.389 | 0.255 | 49/98 | -0.118 |  |
| John Carlson: 2+ assists | 0.035 | 0.165 | 17/84 | +0.116 | STANDARD |
| Nikita Kucherov: 2+ points | 0.357 | 0.430 | 44/58 | +0.046 | STANDARD |

**CAR @ PHI** · priced 134/138 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (CONFIRMED) exp shots 29.07, exp saves 25.36 (sd 6.73), pull risk 0.049
- CAR net: Pyotr Kochetkov (CONFIRMED) exp shots 23.27, exp saves 20.02 (sd 5.74), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sean Couturier: 1+ goals | 0.174 | 0.085 | 9/92 | +0.079 | STANDARD |
| Sebastian Aho: 1+ points | 0.469 | 0.555 | 56/45 | +0.064 | STANDARD |
| Sebastian Aho: 1+ assists | 0.300 | 0.385 | 39/62 | +0.064 | STANDARD |
| Sebastian Aho: 2+ points | 0.133 | 0.210 | 22/80 | +0.056 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.461 | 0.525 | 54/49 | +0.031 | STANDARD |
| Noel Acciari: 1+ goals | 0.135 | 0.075 | 8/93 | +0.050 | STANDARD |

**MTL @ PIT** · priced 116/116 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- PIT net: Arturs Silovs (CONFIRMED) exp shots 24.51, exp saves 21.32 (sd 6.07), pull risk 0.061
- MTL net: Jakub Dobes (CONFIRMED) exp shots 29.53, exp saves 25.27 (sd 7.0), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jakub Dobes: 24+ saves | 0.606 | 0.445 | 51/62 | +0.078 |  |
| Arturs Silovs: 26+ saves | 0.235 | 0.370 | 46/72 | +0.031 |  |
| Rickard Rakell: 1+ points | 0.640 | 0.540 | 55/47 | +0.073 | STANDARD |
| Rickard Rakell: 1+ goals | 0.374 | 0.285 | 29/72 | +0.069 | STANDARD |
| Connor Dewar: 1+ goals | 0.201 | 0.115 | 12/89 | +0.074 | STANDARD |
| Nick Suzuki: 2+ points | 0.243 | 0.325 | 34/69 | +0.052 | STANDARD |

**UTA @ CBJ** · priced 122/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.84, exp saves 23.33 (sd 6.36), pull risk 0.055
- UTA net: Karel Vejmelka (PROJECTED) exp shots 28.0, exp saves 23.96 (sd 6.66), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.138 | 0.345 | 35/66 | +0.186 | STANDARD |
| Vincent Trocheck: 1+ points | 0.315 | 0.485 | 50/53 | +0.137 | STANDARD |
| Matthew Knies: 1+ assists | 0.245 | 0.365 | 37/64 | +0.099 | STANDARD |
| Charlie Coyle: 1+ points | 0.557 | 0.465 | 48/55 | +0.059 | STANDARD |
| Matthew Knies: 1+ points | 0.460 | 0.540 | 55/47 | +0.053 | STANDARD |
| Charlie Coyle: 1+ goals | 0.271 | 0.195 | 20/81 | +0.059 | STANDARD |

**SEA @ EDM** · priced 129/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 25.57, exp saves 22.4 (sd 6.15), pull risk 0.054
- SEA net: Joey Daccord (PROJECTED) exp shots 30.84, exp saves 26.05 (sd 7.23), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.519 | 0.685 | 69/32 | +0.145 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.441 | 0.605 | 61/40 | +0.142 | STANDARD |
| Leon Draisaitl: 2+ points | 0.320 | 0.475 | 49/54 | +0.123 | STANDARD |
| Connor McDavid: 2+ assists | 0.174 | 0.325 | 33/68 | +0.131 | STANDARD |
| Connor McDavid: 2+ points | 0.401 | 0.545 | 56/47 | +0.111 | STANDARD |
| Mattias Ekholm: 1+ points | 0.447 | 0.315 | 33/70 | +0.102 | STANDARD |

**NJD @ NYI** · priced 121/121 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.14, exp saves 24.54 (sd 6.48), pull risk 0.046
- NJD net: Nico Daws (CONFIRMED) exp shots 27.75, exp saves 24.0 (sd 6.52), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nico Daws: 23+ saves | 0.588 | 0.380 | 56/80 | +0.010 |  |
| Luke Evangelista: 1+ points | 0.300 | 0.485 | 50/53 | +0.153 | STANDARD |
| Luke Evangelista: 1+ assists | 0.161 | 0.340 | 36/68 | +0.144 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.176 | 0.320 | 33/69 | +0.119 | STANDARD |
| Anthony Mantha: 1+ assists | 0.154 | 0.295 | 30/71 | +0.122 | STANDARD |
| Anthony Mantha: 1+ points | 0.329 | 0.465 | 48/55 | +0.104 | STANDARD |

**DAL @ NSH** · priced 114/114 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 27.51, exp saves 23.93 (sd 6.48), pull risk 0.053
- DAL net: Casey DeSmith (CONFIRMED) exp shots 26.36, exp saves 22.78 (sd 6.36), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.175 | 0.295 | 31/72 | +0.091 | STANDARD |
| Roope Hintz: 1+ assists | 0.244 | 0.360 | 37/65 | +0.090 | STANDARD |
| Mikko Rantanen: 1+ points | 0.532 | 0.645 | 66/37 | +0.082 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.377 | 0.490 | 50/52 | +0.085 | STANDARD |
| Miro Heiskanen: 1+ points | 0.464 | 0.565 | 58/45 | +0.069 | STANDARD |
| Roope Hintz: 1+ points | 0.433 | 0.530 | 55/49 | +0.059 | STANDARD |

**BOS @ MIN** · priced 118/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.46, exp saves 24.14 (sd 6.54), pull risk 0.051
- BOS net: Michael DiPietro (PROJECTED) exp shots 30.36, exp saves 25.64 (sd 7.16), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| JJ Peterka: 1+ assists | 0.170 | 0.300 | 31/71 | +0.106 | STANDARD |
| Max Shabanov: 1+ assists | 0.206 | 0.325 | 34/69 | +0.089 | STANDARD |
| JJ Peterka: 1+ points | 0.349 | 0.460 | 47/55 | +0.084 | STANDARD |
| Max Shabanov: 1+ points | 0.359 | 0.455 | 49/58 | +0.044 | STANDARD |
| Elias Lindholm: 1+ points | 0.453 | 0.385 | 40/63 | +0.036 | STANDARD |
| Jesper Wallstedt: 24+ saves | 0.532 | 0.470 | 54/60 | -0.025 |  |

**STL @ COL** · priced 118/118 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROBABLE) exp shots 24.45, exp saves 21.42 (sd 5.99), pull risk 0.051
- STL net: Jordan Binnington (PROBABLE) exp shots 31.38, exp saves 26.45 (sd 7.4), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mackenzie Blackwood: 21+ saves | 0.558 | 0.290 | 53/95 | +0.010 |  |
| Nathan MacKinnon: 2+ points | 0.343 | 0.520 | 54/50 | +0.140 | STANDARD |
| Cale Makar: 2+ points | 0.186 | 0.345 | 36/67 | +0.129 | STANDARD |
| Cale Makar: 1+ assists | 0.444 | 0.600 | 61/41 | +0.129 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.158 | 0.300 | 33/73 | +0.098 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.502 | 0.640 | 65/37 | +0.112 | STANDARD |

**CGY @ VAN** · priced 106/109 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 28.38, exp saves 24.66 (sd 6.66), pull risk 0.058
- CGY net: Devin Cooley (CONFIRMED) exp shots 28.2, exp saves 24.23 (sd 6.63), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zayne Parekh: 1+ points | 0.389 | 0.455 | 47/56 | +0.033 | STANDARD |
| Marco Rossi: 1+ goals | 0.309 | 0.245 | 25/76 | +0.046 | STANDARD |
| Zayne Parekh: 1+ goals | 0.100 | 0.160 | 17/85 | +0.041 | STANDARD |
| Drew O'Connor: 1+ goals | 0.223 | 0.165 | 17/84 | +0.043 | STANDARD |
| Paul Cotter: 1+ goals | 0.128 | 0.185 | 19/82 | +0.042 | STANDARD |
| Joel Farabee: 1+ assists | 0.349 | 0.295 | 31/72 | +0.025 | STANDARD |

**LAK @ SJS** · priced 105/112 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.98, exp saves 24.31 (sd 6.6), pull risk 0.054
- LAK net: Anton Forsberg (PROBABLE) exp shots 26.75, exp saves 23.29 (sd 6.35), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.181 | 0.425 | 43/58 | +0.222 | STANDARD |
| Anton Forsberg: 26+ saves | 0.354 | 0.520 | 52/ | -0.183 |  |
| Artemi Panarin: 1+ assists | 0.369 | 0.515 | 52/49 | +0.124 | STANDARD |
| Mason Marchment: 1+ assists | 0.192 | 0.335 | 34/67 | +0.123 | STANDARD |
| Mats Zuccarello: 2+ assists | 0.016 | 0.115 | 12/89 | +0.087 | STANDARD |
| Alex Laferriere: 1+ assists | 0.377 | 0.280 | 29/73 | +0.072 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
