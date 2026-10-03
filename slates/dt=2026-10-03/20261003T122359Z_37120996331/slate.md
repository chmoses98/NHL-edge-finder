# NHL slate 2026-10-03 — RESEARCH_ONLY

generated 2026-10-03T12:23:59Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 13 · simulated (not started): 13 · markets on board: 3778 · contracts joined: 1887 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 1562, 'NO_EDGE': 132, 'OK': 193}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'player_assists': 227, 'game_early_goal': 13, 'first_goal': 353, 'game_winner': 26, 'player_goals': 353, 'game_overtime': 13, 'player_points': 291, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 2026-10-03T23:00:00Z | T-6h | 0.664 | 0.336 | 0.164 | 6.12 | 3.57 | 2.55 | 159 (25/134) | PROJECTED/PROJECTED |
| OTT @ TOR | 2026-10-03T23:00:00Z | T-6h | 0.470 | 0.530 | 0.172 | 6.58 | 3.19 | 3.39 | 182 (25/157) | PROJECTED/PROJECTED |
| WSH @ TBL | 2026-10-03T23:00:00Z | T-6h | 0.623 | 0.377 | 0.171 | 6.22 | 3.50 | 2.72 | 180 (25/155) | PROJECTED/CONFIRMED |
| CAR @ PHI | 2026-10-03T23:00:00Z | T-6h | 0.478 | 0.522 | 0.184 | 5.80 | 2.82 | 2.98 | 188 (25/163) | PROJECTED/PROJECTED |
| MTL @ PIT | 2026-10-03T23:00:00Z | T-6h | 0.563 | 0.437 | 0.169 | 6.56 | 3.49 | 3.07 | 167 (25/142) | PROJECTED/PROJECTED |
| UTA @ CBJ | 2026-10-03T23:00:00Z | T-6h | 0.540 | 0.460 | 0.182 | 6.10 | 3.16 | 2.94 | 173 (25/148) | PROJECTED/PROJECTED |
| SEA @ EDM | 2026-10-03T23:00:00Z | T-6h | 0.614 | 0.386 | 0.161 | 6.67 | 3.71 | 2.95 | 180 (25/155) | PROJECTED/PROJECTED |
| NJD @ NYI | 2026-10-03T23:30:00Z | T-6h | 0.538 | 0.462 | 0.186 | 5.59 | 2.90 | 2.70 | 171 (25/146) | CONFIRMED/PROJECTED |
| DAL @ NSH | 2026-10-04T00:00:00Z | T-6h | 0.518 | 0.482 | 0.180 | 6.10 | 3.11 | 2.99 | 164 (25/139) | PROJECTED/PROJECTED |
| BOS @ MIN | 2026-10-04T00:00:00Z | T-6h | 0.582 | 0.418 | 0.175 | 6.05 | 3.28 | 2.77 | 170 (25/145) | PROJECTED/PROJECTED |
| STL @ COL | 2026-10-04T01:00:00Z | T-12h | 0.663 | 0.337 | 0.154 | 6.75 | 3.93 | 2.81 | 51 (25/26) | PROJECTED/PROBABLE |
| CGY @ VAN | 2026-10-04T02:00:00Z | T-12h | 0.551 | 0.449 | 0.170 | 6.56 | 3.44 | 3.12 | 51 (25/26) | PROJECTED/PROJECTED |
| LAK @ SJS | 2026-10-04T02:00:00Z | T-12h | 0.550 | 0.450 | 0.176 | 6.32 | 3.31 | 3.02 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4 | team_total | 0.293 | 0.410 | 0.385 | 42 | 60 | no | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ3 | team_total | 0.514 | 0.630 | 0.608 | 64 | 38 | no | +0.089 | OK |
| KXNHLGAME-26OCT03MTLPIT-MTL | game_winner | 0.437 | 0.535 | 0.515 | 54 | 47 | no | +0.076 | OK |
| KXNHLGAME-26OCT03MTLPIT-PIT | game_winner | 0.563 | 0.465 | 0.485 | 47 | 54 | yes | +0.076 | OK |
| KXNHLTOTAL-26OCT03NJNYI-6 | game_total | 0.457 | 0.555 | 0.536 | 56 | 45 | no | +0.075 | OK |
| KXNHLGAME-26OCT03NJNYI-NYI | game_winner | 0.538 | 0.445 | 0.464 | 45 | 56 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5 | team_total | 0.138 | 0.225 | 0.205 | 23 | 78 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4 | team_total | 0.475 | 0.385 | 0.403 | 39 | 62 | yes | +0.068 | OK |
| KXNHLTOTAL-26OCT03NJNYI-5 | game_total | 0.690 | 0.775 | 0.759 | 78 | 23 | no | +0.067 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT2 | game_spread | 0.350 | 0.265 | 0.281 | 27 | 74 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ2 | team_total | 0.744 | 0.830 | 0.815 | 84 | 18 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT03NJNYI-7 | game_total | 0.349 | 0.435 | 0.417 | 44 | 57 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL3 | team_total | 0.529 | 0.445 | 0.462 | 45 | 56 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL4 | team_total | 0.324 | 0.240 | 0.256 | 25 | 77 | yes | +0.061 | OK |
| KXNHLGAME-26OCT03NJNYI-NJ | game_winner | 0.462 | 0.545 | 0.528 | 55 | 46 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ2 | game_spread | 0.244 | 0.325 | 0.308 | 33 | 68 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT03STLCOL-7 | game_total | 0.534 | 0.455 | 0.471 | 46 | 55 | yes | +0.057 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT3 | game_spread | 0.225 | 0.155 | 0.167 | 16 | 85 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-MIN4 | team_total | 0.428 | 0.510 | 0.494 | 52 | 50 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT3 | team_total | 0.680 | 0.605 | 0.621 | 61 | 40 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ3 | game_spread | 0.136 | 0.205 | 0.189 | 21 | 80 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL2 | game_spread | 0.242 | 0.315 | 0.299 | 32 | 69 | no | +0.053 | OK |
| KXNHLGAME-26OCT03BOSMIN-BOS | game_winner | 0.418 | 0.345 | 0.359 | 35 | 66 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT03NJNYI-4 | game_total | 0.791 | 0.855 | 0.844 | 86 | 15 | no | +0.050 | OK |
| KXNHLGAME-26OCT03DALNSH-NSH | game_winner | 0.518 | 0.445 | 0.459 | 45 | 56 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT03BOSMIN-MIN3 | game_spread | 0.226 | 0.295 | 0.280 | 30 | 71 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT03STLCOL-9 | game_total | 0.250 | 0.180 | 0.193 | 19 | 83 | yes | +0.049 | OK |
| KXNHLTOTAL-26OCT03STLCOL-8 | game_total | 0.342 | 0.275 | 0.288 | 28 | 73 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL5 | team_total | 0.164 | 0.100 | 0.111 | 11 | 91 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL3 | game_spread | 0.142 | 0.205 | 0.191 | 21 | 80 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT03STLCOL-6 | game_total | 0.643 | 0.575 | 0.589 | 58 | 43 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT4 | team_total | 0.450 | 0.380 | 0.394 | 39 | 63 | yes | +0.043 | OK |
| KXNHLGAME-26OCT03STLCOL-COL | game_winner | 0.663 | 0.725 | 0.713 | 73 | 28 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL2 | team_total | 0.757 | 0.695 | 0.708 | 70 | 31 | yes | +0.042 | OK |
| KXNHLGAME-26OCT03BOSMIN-MIN | game_winner | 0.582 | 0.645 | 0.633 | 65 | 36 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL2 | game_spread | 0.263 | 0.325 | 0.312 | 33 | 68 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT5 | team_total | 0.283 | 0.215 | 0.228 | 23 | 80 | yes | +0.040 | OK |
| KXNHLGAME-26OCT03DALNSH-DAL | game_winner | 0.482 | 0.545 | 0.533 | 55 | 46 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT03BOSMIN-MIN2 | game_spread | 0.353 | 0.415 | 0.402 | 42 | 59 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT03NJNYI-8 | game_total | 0.180 | 0.240 | 0.227 | 25 | 77 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT03CARPHI-5 | game_total | 0.720 | 0.775 | 0.765 | 78 | 23 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-MIN5 | team_total | 0.238 | 0.305 | 0.291 | 32 | 71 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-MIN3 | team_total | 0.648 | 0.705 | 0.694 | 71 | 30 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT03DALNSH-NSH2 | game_spread | 0.298 | 0.245 | 0.255 | 25 | 76 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NYI2 | game_spread | 0.298 | 0.245 | 0.255 | 25 | 76 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL4 | team_total | 0.359 | 0.425 | 0.412 | 44 | 59 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT03CARPHI-6 | game_total | 0.489 | 0.545 | 0.534 | 55 | 46 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL3 | game_spread | 0.155 | 0.205 | 0.194 | 21 | 80 | no | +0.033 | OK |
| KXNHLGAME-26OCT03OTTTOR-TOR | game_winner | 0.470 | 0.525 | 0.514 | 53 | 48 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL3 | team_total | 0.591 | 0.650 | 0.638 | 66 | 36 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL4 | team_total | 0.380 | 0.440 | 0.428 | 45 | 57 | no | +0.032 | OK |
| KXNHLGAME-26OCT03STLCOL-STL | game_winner | 0.337 | 0.285 | 0.295 | 29 | 72 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT6 | team_total | 0.139 | 0.085 | 0.094 | 10 | 93 | yes | +0.032 | OK |
| KXNHLGAME-26OCT03UTACBJ-CBJ | game_winner | 0.540 | 0.485 | 0.496 | 49 | 52 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-8 | game_total | 0.315 | 0.265 | 0.275 | 27 | 74 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-7 | game_total | 0.508 | 0.455 | 0.466 | 46 | 55 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT03CARPHI-7 | game_total | 0.382 | 0.435 | 0.424 | 44 | 57 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL3 | team_total | 0.583 | 0.645 | 0.633 | 66 | 37 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT03STLCOL-STL2 | game_spread | 0.168 | 0.125 | 0.133 | 13 | 88 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT03NJNYI-9 | game_total | 0.120 | 0.165 | 0.155 | 17 | 84 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-9 | game_total | 0.231 | 0.180 | 0.189 | 19 | 83 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ6 | team_total | 0.055 | 0.100 | 0.089 | 11 | 91 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL6 | team_total | 0.072 | 0.035 | 0.040 | 4 | 97 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT5 | team_total | 0.261 | 0.205 | 0.215 | 22 | 81 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-6 | game_total | 0.616 | 0.565 | 0.575 | 57 | 44 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN5 | team_total | 0.271 | 0.220 | 0.230 | 23 | 79 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN4 | team_total | 0.465 | 0.405 | 0.417 | 42 | 61 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL2 | game_spread | 0.455 | 0.505 | 0.495 | 51 | 50 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT03CARPHI-CAR4 | team_total | 0.356 | 0.415 | 0.403 | 43 | 60 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT03BOSMIN-BOS2 | game_spread | 0.217 | 0.175 | 0.183 | 18 | 83 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL3 | game_spread | 0.319 | 0.365 | 0.356 | 37 | 64 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT03CGYVAN-8 | game_total | 0.309 | 0.265 | 0.273 | 27 | 74 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT3 | team_total | 0.661 | 0.610 | 0.621 | 62 | 40 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT03SEAEDM-SEA5 | team_total | 0.184 | 0.145 | 0.152 | 15 | 86 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-VAN2 | game_spread | 0.339 | 0.290 | 0.299 | 30 | 72 | yes | +0.024 | OK |
| KXNHLGAME-26OCT03OTTTOR-OTT | game_winner | 0.530 | 0.485 | 0.494 | 49 | 52 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT03CARPHI-CAR3 | team_total | 0.581 | 0.630 | 0.620 | 64 | 38 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT03SEAEDM-SEA2 | game_spread | 0.202 | 0.165 | 0.172 | 17 | 84 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT03STLCOL-10 | game_total | 0.129 | 0.085 | 0.093 | 10 | 93 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-OTT2 | game_spread | 0.317 | 0.275 | 0.283 | 28 | 73 | yes | +0.022 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 0.664 | 0.644 | 0.164 | 0.206 | 6.12 | 6.36 | 0.997/1.003 | KXNHLTEAMTOTAL-26OCT03CHIBUF-CHI3 +0.047 |
| OTT @ TOR | 0.470 | 0.463 | 0.172 | 0.220 | 6.58 | 6.10 | 0.965/0.998 | KXNHLTOTAL-26OCT03OTTTOR-8 -0.077 |
| WSH @ TBL | 0.623 | 0.606 | 0.171 | 0.214 | 6.22 | 6.27 | 0.957/1.015 | KXNHLTEAMTOTAL-26OCT03WSHTB-WSH3 +0.027 |
| CAR @ PHI | 0.478 | 0.535 | 0.184 | 0.224 | 5.80 | 5.92 | 0.991/0.989 | KXNHLTEAMTOTAL-26OCT03CARPHI-PHI3 +0.060 |
| MTL @ PIT | 0.563 | 0.569 | 0.169 | 0.215 | 6.56 | 6.62 | 1.033/0.952 | KXNHLTOTAL-26OCT03MTLPIT-5 +0.018 |
| UTA @ CBJ | 0.540 | 0.544 | 0.182 | 0.219 | 6.10 | 6.32 | 0.964/0.992 | KXNHLTOTAL-26OCT03UTACBJ-7 +0.040 |
| SEA @ EDM | 0.614 | 0.624 | 0.161 | 0.212 | 6.67 | 6.52 | 0.994/1.005 | KXNHLTOTAL-26OCT03SEAEDM-6 -0.028 |
| NJD @ NYI | 0.538 | 0.536 | 0.186 | 0.228 | 5.59 | 5.86 | 0.947/0.987 | KXNHLTOTAL-26OCT03NJNYI-5 +0.046 |
| DAL @ NSH | 0.518 | 0.536 | 0.180 | 0.224 | 6.10 | 6.10 | 1.000/0.986 | KXNHLGAME-26OCT03DALNSH-DAL -0.019 |
| BOS @ MIN | 0.582 | 0.608 | 0.175 | 0.211 | 6.05 | 6.38 | 1.003/0.968 | KXNHLTEAMTOTAL-26OCT03BOSMIN-MIN4 +0.061 |
| STL @ COL | 0.663 | 0.633 | 0.154 | 0.204 | 6.75 | 6.42 | 0.976/1.024 | KXNHLTEAMTOTAL-26OCT03STLCOL-COL5 -0.067 |
| CGY @ VAN | 0.551 | 0.572 | 0.170 | 0.212 | 6.56 | 6.36 | 1.021/0.997 | KXNHLTOTAL-26OCT03CGYVAN-6 -0.036 |
| LAK @ SJS | 0.550 | 0.521 | 0.176 | 0.222 | 6.32 | 6.12 | 1.034/0.992 | KXNHLTEAMTOTAL-26OCT03LASJ-SJ4 -0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 30 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Greene: 1+ goals YES @ 11c · p 0.1628 (adj 0.1446) · $3.93 · thesis CHI:OFFENSE_4PLUS
- Stephen Halliday: 1+ goals YES @ 9c · p 0.1386 (adj 0.1177) · $2.91 · thesis OTT:OFFENSE_4PLUS
- Hayden Hodgson: 1+ goals YES @ 8c · p 0.1202 (adj 0.1027) · $2.31 · thesis OTT:OFFENSE_4PLUS
- Darren Raddysh: 1+ assists NO @ 59c · p 0.7081 (adj 0.6183) · $4.51 · thesis TOR:SUPPRESSED
- John Carlson: 2+ assists NO @ 86c · p 0.9655 (adj 0.8872) · $11.32 · thesis TBL:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2143 (adj 0.197) · $2.76 · thesis WSH:OFFENSE_4PLUS
- John Carlson: 1+ points NO @ 43c · p 0.648 (adj 0.4657) · $4.44 · thesis TBL:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 9c · p 0.1711 (adj 0.1471) · $6.48 · thesis PHI:OFFENSE_4PLUS
- Carl Grundstrom: 1+ goals YES @ 8c · p 0.1368 (adj 0.1189) · $4.25 · thesis PHI:OFFENSE_4PLUS
- Noel Acciari: 1+ goals YES @ 9c · p 0.1312 (adj 0.1172) · $2.82 · thesis PHI:OFFENSE_4PLUS
- Nikolaj Ehlers: 1+ goals NO @ 75c · p 0.7954 (adj 0.7803) · $9.94 · thesis CAR:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 13c · p 0.2096 (adj 0.1847) · $6.33 · thesis PIT:WINS_BY_2PLUS
- Pittsburgh wins by over 2.5 goals YES @ 16c · p 0.2295 (adj 0.1923) · $1.44 · thesis PIT:WINS_BY_2PLUS
- Montreal wins by over 1.5 goals NO @ 69c · p 0.7625 (adj 0.7238) · $3.21 · thesis PIT:WINS
- Sidney Crosby: 1+ goals YES @ 31c · p 0.3619 (adj 0.3427) · $2.71 · thesis PIT:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 69c · p 0.8619 (adj 0.7274) · $11.32 · thesis UTA:SUPPRESSED
- Danton Heinen: 1+ goals YES @ 10c · p 0.1317 (adj 0.12) · $1.99 · thesis CBJ:OFFENSE_4PLUS
- Conor Garland: 1+ goals NO @ 83c · p 0.8634 (adj 0.8513) · $11.08 · thesis CBJ:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 18c · p 0.2469 (adj 0.2239) · $5.87 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 33c · p 0.4617 (adj 0.3663) · $3.66 · thesis EDM:SUPPRESSED
- Connor McDavid: 2+ assists NO @ 69c · p 0.8207 (adj 0.7227) · $9.58 · thesis EDM:SUPPRESSED
- Kasperi Kapanen: 1+ assists YES @ 27c · p 0.3781 (adj 0.2948) · $2.24 · thesis EDM:OFFENSE_4PLUS
- New Jersey wins by over 1.5 goals NO @ 68c · p 0.7587 (adj 0.7168) · $6.57 · thesis NYI:WINS
- New Jersey over 4.5 goals scored NO @ 78c · p 0.8437 (adj 0.8094) · $8.15 · thesis NJD:SUPPRESSED
- New York I wins YES @ 45c · p 0.5294 (adj 0.4872) · $1.45 · thesis NYI:WINS
- Nashville wins YES @ 45c · p 0.537 (adj 0.491) · $4.42 · thesis NSH:WINS
- Dallas wins by over 1.5 goals NO @ 68c · p 0.7536 (adj 0.7143) · $5.02 · thesis NSH:WINS
- Colorado wins NO @ 28c · p 0.3716 (adj 0.3233) · $1.12 · thesis STL:WINS
- Colorado wins by over 2.5 goals NO @ 64c · p 0.7232 (adj 0.6791) · $1.65 · thesis GAME:TIGHT
- Calgary wins by over 1.5 goals NO @ 72c · p 0.7759 (adj 0.7454) · $6.54 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BUF** · priced 108/108 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 24.71, exp saves 21.79 (sd 6.0), pull risk 0.048
- CHI net: Spencer Knight (PROJECTED) exp shots 30.42, exp saves 25.66 (sd 7.17), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tage Thompson: 1+ points | 0.586 | 0.350 | 68/98 | -0.110 | STANDARD |
| Josh Norris: 1+ assists | 0.350 | 0.185 | 35/98 | -0.016 | STANDARD |
| Patrick Kane: 1+ points | 0.431 | 0.530 | 55/49 | +0.062 | STANDARD |
| Tage Thompson: 2+ points | 0.222 | 0.320 | 34/70 | +0.064 | STANDARD |
| Tage Thompson: 1+ assists | 0.352 | 0.440 | 46/58 | +0.051 | STANDARD |
| Patrick Kane: 2+ points | 0.109 | 0.185 | 21/84 | +0.041 | STANDARD |

**OTT @ TOR** · priced 123/131 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 31.35, exp saves 27.01 (sd 7.16), pull risk 0.065
- OTT net: Linus Ullmark (PROJECTED) exp shots 24.74, exp saves 21.67 (sd 6.03), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Drake Batherson: 1+ assists | 0.388 | 0.220 | 39/95 | -0.019 | STANDARD |
| Darren Raddysh: 1+ assists | 0.292 | 0.430 | 45/59 | +0.101 | STANDARD |
| Darren Raddysh: 1+ points | 0.387 | 0.515 | 53/50 | +0.096 | STANDARD |
| Claude Giroux: 1+ assists | 0.369 | 0.250 | 27/77 | +0.085 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.279 | 0.395 | 42/63 | +0.075 | STANDARD |
| Kirill Marchenko: 1+ points | 0.465 | 0.575 | 59/44 | +0.078 | STANDARD |

**WSH @ TBL** · priced 127/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.03, exp saves 21.9 (sd 6.13), pull risk 0.05
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.7, exp saves 24.51 (sd 6.84), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brandon Hagel: 1+ points | 0.632 | 0.315 | 61/98 | +0.005 | STANDARD |
| Brayden Point: 1+ points | 0.618 | 0.310 | 60/98 | +0.001 | STANDARD |
| John Carlson: 1+ points | 0.352 | 0.595 | 62/43 | +0.201 | STANDARD |
| Brayden Point: 1+ assists | 0.431 | 0.220 | 42/98 | -0.006 | STANDARD |
| Charle-Edouard D'Astous: 1+ assists | 0.309 | 0.145 | 27/98 | +0.026 | STANDARD |
| John Carlson: 2+ points | 0.073 | 0.235 | 27/80 | +0.115 | STANDARD |

**CAR @ PHI** · priced 137/137 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.3 (sd 6.77), pull risk 0.05
- CAR net: Brandon Bussi (PROJECTED) exp shots 23.27, exp saves 20.06 (sd 5.73), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.294 | 0.395 | 41/62 | +0.069 | STANDARD |
| Sebastian Aho: 1+ points | 0.466 | 0.565 | 59/46 | +0.057 | STANDARD |
| Sean Couturier: 1+ goals | 0.171 | 0.075 | 9/94 | +0.075 | STANDARD |
| Sebastian Aho: 2+ points | 0.134 | 0.210 | 24/82 | +0.036 | STANDARD |
| Carl Grundstrom: 1+ goals | 0.137 | 0.065 | 8/95 | +0.052 | STANDARD |
| Christian Dvorak: 1+ points | 0.462 | 0.395 | 42/63 | +0.025 | STANDARD |

**MTL @ PIT** · priced 112/116 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- PIT net: Arturs Silovs (PROJECTED) exp shots 24.51, exp saves 21.3 (sd 6.12), pull risk 0.06
- MTL net: Jakub Dobes (PROJECTED) exp shots 29.53, exp saves 25.22 (sd 6.93), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Erik Karlsson: 1+ assists | 0.491 | 0.225 | 43/98 | +0.044 | STANDARD |
| Egor Chinakhov: 1+ goals | 0.274 | 0.155 | 25/94 | +0.011 | STANDARD |
| Filip Hallander: 1+ goals | 0.218 | 0.105 | 13/92 | +0.080 | STANDARD |
| Rickard Rakell: 1+ goals | 0.388 | 0.275 | 30/75 | +0.073 | STANDARD |
| Rickard Rakell: 1+ points | 0.648 | 0.540 | 57/49 | +0.060 | STANDARD |
| Nick Suzuki: 1+ assists | 0.457 | 0.560 | 58/46 | +0.066 | STANDARD |

**UTA @ CBJ** · priced 122/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.84, exp saves 23.33 (sd 6.36), pull risk 0.055
- UTA net: Karel Vejmelka (PROJECTED) exp shots 28.0, exp saves 23.96 (sd 6.66), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.138 | 0.345 | 38/69 | +0.157 | STANDARD |
| Clayton Keller: 1+ assists | 0.446 | 0.265 | 51/98 | -0.082 | STANDARD |
| Vincent Trocheck: 1+ points | 0.315 | 0.490 | 51/53 | +0.137 | STANDARD |
| Charlie Coyle: 1+ goals | 0.271 | 0.115 | 21/98 | +0.049 | STANDARD |
| Charlie Coyle: 1+ points | 0.557 | 0.445 | 49/60 | +0.049 | STANDARD |
| Matthew Knies: 1+ assists | 0.245 | 0.355 | 37/66 | +0.079 | STANDARD |

**SEA @ EDM** · priced 129/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 25.57, exp saves 22.44 (sd 6.23), pull risk 0.052
- SEA net: Joey Daccord (PROJECTED) exp shots 30.84, exp saves 26.07 (sd 7.2), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Shea: 2+ assists | 0.037 | 0.335 | 64/97 | -0.009 | STANDARD |
| Matty Beniers: 1+ points | 0.483 | 0.240 | 46/98 | +0.006 | STANDARD |
| Vince Dunn: 1+ points | 0.421 | 0.240 | 46/98 | -0.056 | STANDARD |
| Connor McDavid: 2+ assists | 0.179 | 0.330 | 35/69 | +0.116 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.461 | 0.610 | 63/41 | +0.112 | STANDARD |
| Connor McDavid: 1+ assists | 0.538 | 0.685 | 70/33 | +0.116 | STANDARD |

**NJD @ NYI** · priced 120/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.14, exp saves 24.54 (sd 6.48), pull risk 0.046
- NJD net: Jake Allen (PROJECTED) exp shots 27.75, exp saves 24.0 (sd 6.61), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.153 | 0.325 | 37/72 | +0.112 | STANDARD |
| Luke Evangelista: 1+ points | 0.296 | 0.460 | 50/58 | +0.107 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.184 | 0.310 | 34/72 | +0.082 | STANDARD |
| Jack Hughes: 2+ points | 0.200 | 0.315 | 36/73 | +0.056 | STANDARD |
| Anthony Mantha: 1+ assists | 0.157 | 0.270 | 31/77 | +0.061 | STANDARD |
| Anthony Mantha: 1+ points | 0.332 | 0.430 | 48/62 | +0.032 | STANDARD |

**DAL @ NSH** · priced 113/113 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.51, exp saves 23.92 (sd 6.5), pull risk 0.057
- DAL net: Jake Oettinger (PROJECTED) exp shots 26.36, exp saves 22.77 (sd 6.42), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan O'Reilly: 1+ points | 0.598 | 0.305 | 59/98 | -0.009 | STANDARD |
| Filip Forsberg: 1+ points | 0.614 | 0.325 | 63/98 | -0.032 | STANDARD |
| Wyatt Johnston: 1+ points | 0.572 | 0.330 | 64/98 | -0.085 | STANDARD |
| Jason Robertson: 1+ points | 0.592 | 0.360 | 70/98 | -0.123 | STANDARD |
| Roman Josi: 1+ points | 0.548 | 0.330 | 62/96 | -0.088 | STANDARD |
| Ryan O'Reilly: 1+ assists | 0.425 | 0.215 | 41/98 | -0.002 | STANDARD |

**BOS @ MIN** · priced 117/119 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.46, exp saves 24.13 (sd 6.56), pull risk 0.05
- BOS net: Jeremy Swayman (PROJECTED) exp shots 30.36, exp saves 25.72 (sd 7.2), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Max Shabanov: 2+ points | 0.075 | 0.500 | 99/99 | -0.066 | STANDARD |
| Matt Boldy: 1+ points | 0.655 | 0.425 | 71/86 | -0.070 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.664 | 0.435 | 73/86 | -0.080 | STANDARD |
| Quinn Hughes: 1+ points | 0.659 | 0.435 | 72/85 | -0.075 | STANDARD |
| Max Shabanov: 1+ points | 0.358 | 0.500 | 99/99 | -0.348 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.442 | 0.315 | 53/90 | -0.105 | STANDARD |

**STL @ COL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.45, exp saves 21.45 (sd 5.93), pull risk 0.048
- STL net: Jordan Binnington (PROBABLE) exp shots 31.38, exp saves 26.4 (sd 7.37), pull risk 0.088

**CGY @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.38, exp saves 24.77 (sd 6.6), pull risk 0.052
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.2, exp saves 24.14 (sd 6.81), pull risk 0.077

**LAK @ SJS** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.98, exp saves 24.34 (sd 6.56), pull risk 0.055
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.75, exp saves 23.27 (sd 6.38), pull risk 0.057

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
