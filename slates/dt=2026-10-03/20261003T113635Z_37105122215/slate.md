# NHL slate 2026-10-03 — RESEARCH_ONLY

generated 2026-10-03T11:36:35Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 13 · simulated (not started): 13 · markets on board: 3511 · contracts joined: 1620 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 1295, 'NO_EDGE': 134, 'OK': 191}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'player_assists': 189, 'game_early_goal': 13, 'first_goal': 248, 'game_winner': 26, 'player_goals': 283, 'game_overtime': 13, 'player_points': 237, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 2026-10-03T23:00:00Z | T-6h | 0.664 | 0.336 | 0.164 | 6.12 | 3.57 | 2.55 | 159 (25/134) | PROJECTED/PROJECTED |
| OTT @ TOR | 2026-10-03T23:00:00Z | T-6h | 0.470 | 0.530 | 0.172 | 6.58 | 3.19 | 3.39 | 182 (25/157) | PROJECTED/PROJECTED |
| WSH @ TBL | 2026-10-03T23:00:00Z | T-6h | 0.623 | 0.377 | 0.171 | 6.22 | 3.50 | 2.72 | 180 (25/155) | PROJECTED/CONFIRMED |
| CAR @ PHI | 2026-10-03T23:00:00Z | T-6h | 0.478 | 0.522 | 0.184 | 5.80 | 2.82 | 2.98 | 188 (25/163) | PROJECTED/PROJECTED |
| MTL @ PIT | 2026-10-03T23:00:00Z | T-6h | 0.563 | 0.437 | 0.169 | 6.56 | 3.49 | 3.07 | 167 (25/142) | PROJECTED/PROJECTED |
| UTA @ CBJ | 2026-10-03T23:00:00Z | T-6h | 0.540 | 0.460 | 0.182 | 6.10 | 3.16 | 2.94 | 173 (25/148) | PROJECTED/PROJECTED |
| SEA @ EDM | 2026-10-03T23:00:00Z | T-6h | 0.614 | 0.386 | 0.161 | 6.67 | 3.71 | 2.95 | 180 (25/155) | PROJECTED/PROJECTED |
| NJD @ NYI | 2026-10-03T23:30:00Z | T-6h | 0.538 | 0.462 | 0.186 | 5.59 | 2.90 | 2.70 | 136 (25/111) | CONFIRMED/PROJECTED |
| DAL @ NSH | 2026-10-04T00:00:00Z | T-12h | 0.518 | 0.482 | 0.180 | 6.10 | 3.11 | 2.99 | 51 (25/26) | PROJECTED/PROJECTED |
| BOS @ MIN | 2026-10-04T00:00:00Z | T-12h | 0.582 | 0.418 | 0.175 | 6.05 | 3.28 | 2.77 | 51 (25/26) | PROJECTED/PROJECTED |
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
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4 | team_total | 0.475 | 0.385 | 0.403 | 39 | 62 | yes | +0.068 | OK |
| KXNHLTOTAL-26OCT03NJNYI-5 | game_total | 0.690 | 0.775 | 0.759 | 78 | 23 | no | +0.067 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT2 | game_spread | 0.350 | 0.260 | 0.277 | 27 | 75 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ2 | team_total | 0.744 | 0.830 | 0.815 | 84 | 18 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT03NJNYI-7 | game_total | 0.349 | 0.435 | 0.417 | 44 | 57 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL3 | team_total | 0.529 | 0.440 | 0.458 | 45 | 57 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL4 | team_total | 0.324 | 0.240 | 0.256 | 25 | 77 | yes | +0.061 | OK |
| KXNHLGAME-26OCT03NJNYI-NJ | game_winner | 0.462 | 0.545 | 0.528 | 55 | 46 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ2 | game_spread | 0.244 | 0.325 | 0.308 | 33 | 68 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5 | team_total | 0.138 | 0.220 | 0.201 | 23 | 79 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT03STLCOL-7 | game_total | 0.534 | 0.455 | 0.471 | 46 | 55 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT3 | team_total | 0.680 | 0.595 | 0.613 | 61 | 42 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ3 | game_spread | 0.136 | 0.205 | 0.189 | 21 | 80 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL2 | game_spread | 0.242 | 0.315 | 0.299 | 32 | 69 | no | +0.053 | OK |
| KXNHLGAME-26OCT03BOSMIN-BOS | game_winner | 0.418 | 0.345 | 0.359 | 35 | 66 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT03NJNYI-4 | game_total | 0.791 | 0.855 | 0.844 | 86 | 15 | no | +0.050 | OK |
| KXNHLGAME-26OCT03DALNSH-NSH | game_winner | 0.518 | 0.445 | 0.459 | 45 | 56 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT03STLCOL-8 | game_total | 0.342 | 0.270 | 0.284 | 28 | 74 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT03NJNYI-8 | game_total | 0.180 | 0.245 | 0.231 | 25 | 76 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL5 | team_total | 0.164 | 0.100 | 0.111 | 11 | 91 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL3 | game_spread | 0.142 | 0.205 | 0.191 | 21 | 80 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT03STLCOL-6 | game_total | 0.643 | 0.575 | 0.589 | 58 | 43 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT3 | game_spread | 0.225 | 0.160 | 0.172 | 17 | 85 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-MIN4 | team_total | 0.428 | 0.505 | 0.490 | 52 | 51 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT4 | team_total | 0.450 | 0.385 | 0.398 | 39 | 62 | yes | +0.043 | OK |
| KXNHLGAME-26OCT03STLCOL-COL | game_winner | 0.663 | 0.725 | 0.713 | 73 | 28 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL2 | team_total | 0.757 | 0.690 | 0.704 | 70 | 32 | yes | +0.042 | OK |
| KXNHLGAME-26OCT03BOSMIN-MIN | game_winner | 0.582 | 0.645 | 0.633 | 65 | 36 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL2 | game_spread | 0.263 | 0.325 | 0.312 | 33 | 68 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT5 | team_total | 0.283 | 0.215 | 0.228 | 23 | 80 | yes | +0.040 | OK |
| KXNHLGAME-26OCT03DALNSH-DAL | game_winner | 0.482 | 0.545 | 0.533 | 55 | 46 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT03BOSMIN-MIN2 | game_spread | 0.353 | 0.415 | 0.402 | 42 | 59 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN5 | team_total | 0.271 | 0.215 | 0.225 | 22 | 79 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT03STLCOL-9 | game_total | 0.250 | 0.185 | 0.197 | 20 | 83 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT03CARPHI-5 | game_total | 0.720 | 0.775 | 0.765 | 78 | 23 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-MIN5 | team_total | 0.238 | 0.305 | 0.291 | 32 | 71 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT03DALNSH-NSH2 | game_spread | 0.298 | 0.240 | 0.251 | 25 | 77 | yes | +0.035 | OK |
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
| KXNHLTOTAL-26OCT03CARPHI-7 | game_total | 0.382 | 0.435 | 0.424 | 44 | 57 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT03BOSMIN-MIN3 | game_spread | 0.226 | 0.275 | 0.265 | 28 | 73 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL3 | team_total | 0.583 | 0.645 | 0.633 | 66 | 37 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT03STLCOL-STL2 | game_spread | 0.168 | 0.125 | 0.133 | 13 | 88 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT03NJNYI-9 | game_total | 0.120 | 0.165 | 0.155 | 17 | 84 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-9 | game_total | 0.231 | 0.180 | 0.189 | 19 | 83 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ6 | team_total | 0.055 | 0.100 | 0.089 | 11 | 91 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL6 | team_total | 0.072 | 0.035 | 0.040 | 4 | 97 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-6 | game_total | 0.616 | 0.565 | 0.575 | 57 | 44 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN4 | team_total | 0.465 | 0.405 | 0.417 | 42 | 61 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL2 | game_spread | 0.455 | 0.505 | 0.495 | 51 | 50 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT03CARPHI-CAR4 | team_total | 0.356 | 0.415 | 0.403 | 43 | 60 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-MIN3 | team_total | 0.648 | 0.700 | 0.690 | 71 | 31 | no | +0.027 | OK |
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
| KXNHLTOTAL-26OCT03CARPHI-8 | game_total | 0.205 | 0.245 | 0.237 | 25 | 76 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-TOR3 | game_spread | 0.157 | 0.195 | 0.187 | 20 | 81 | no | +0.022 | OK |
| KXNHLGAME-26OCT03UTACBJ-UTA | game_winner | 0.460 | 0.505 | 0.496 | 51 | 50 | no | +0.022 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 18 recommended · full analysis in card.md / packet.json `thesis_card`

- Stephen Halliday: 1+ goals YES @ 10c · p 0.1386 (adj 0.119) · $3.05 · thesis OTT:OFFENSE_4PLUS
- Noel Acciari: 1+ goals YES @ 9c · p 0.1312 (adj 0.1134) · $3.81 · thesis PHI:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 79c · p 0.8576 (adj 0.8213) · $17.97 · thesis PHI:WINS
- Carolina wins by over 1.5 goals NO @ 68c · p 0.7598 (adj 0.7174) · $7.17 · thesis PHI:WINS
- Carl Grundstrom: 1+ goals YES @ 10c · p 0.1368 (adj 0.1176) · $2.29 · thesis PHI:OFFENSE_4PLUS
- Pittsburgh over 3.5 goals scored YES @ 39c · p 0.484 (adj 0.4345) · $5.5 · thesis PIT:OFFENSE_4PLUS
- Sidney Crosby: 1+ goals YES @ 31c · p 0.3619 (adj 0.3452) · $4.13 · thesis PIT:OFFENSE_4PLUS
- Montreal wins by over 1.5 goals NO @ 69c · p 0.7625 (adj 0.7238) · $3.89 · thesis PIT:WINS
- Montreal wins by over 2.5 goals NO @ 80c · p 0.8533 (adj 0.8241) · $1.05 · thesis PIT:WINS
- Vasily Podkolzin: 1+ assists YES @ 37c · p 0.4451 (adj 0.3975) · $4.42 · thesis EDM:OFFENSE_4PLUS
- New Jersey wins by over 1.5 goals NO @ 68c · p 0.7587 (adj 0.7168) · $9.44 · thesis NYI:WINS
- New York I wins YES @ 45c · p 0.5294 (adj 0.4872) · $2.16 · thesis NYI:WINS
- New Jersey wins by over 2.5 goals NO @ 80c · p 0.8559 (adj 0.8255) · $2.1 · thesis NYI:WINS
- Nashville wins YES @ 45c · p 0.537 (adj 0.491) · $7.82 · thesis NSH:WINS
- Dallas wins by over 1.5 goals NO @ 68c · p 0.7536 (adj 0.7143) · $8.86 · thesis NSH:WINS
- Colorado wins NO @ 28c · p 0.3716 (adj 0.3233) · $1.96 · thesis STL:WINS
- Colorado wins by over 2.5 goals NO @ 64c · p 0.7232 (adj 0.6791) · $2.92 · thesis GAME:TIGHT
- Calgary wins by over 1.5 goals NO @ 72c · p 0.7759 (adj 0.7454) · $11.56 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BUF** · priced 108/108 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 24.71, exp saves 21.79 (sd 6.0), pull risk 0.048
- CHI net: Spencer Knight (PROJECTED) exp shots 30.42, exp saves 25.66 (sd 7.17), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tage Thompson: 1+ assists | 0.352 | 0.440 | 47/59 | +0.041 | STANDARD |
| Patrick Kane: 1+ points | 0.431 | 0.515 | 56/53 | +0.022 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.522 | 0.440 | 50/62 | +0.005 | STANDARD |
| Tage Thompson: 2+ points | 0.222 | 0.300 | 34/74 | +0.025 | STANDARD |
| Patrick Kane: 1+ assists | 0.253 | 0.330 | 40/74 | -0.006 | STANDARD |
| Ryan Greene: 1+ goals | 0.163 | 0.090 | 13/95 | +0.025 | STANDARD |

**OTT @ TOR** · priced 123/131 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 31.35, exp saves 27.01 (sd 7.16), pull risk 0.065
- OTT net: Linus Ullmark (PROJECTED) exp shots 24.74, exp saves 21.67 (sd 6.03), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Claude Giroux: 1+ points | 0.491 | 0.340 | 42/74 | +0.054 | STANDARD |
| Darren Raddysh: 1+ points | 0.387 | 0.525 | 55/50 | +0.096 | STANDARD |
| Claude Giroux: 1+ assists | 0.369 | 0.240 | 28/80 | +0.075 | STANDARD |
| Easton Cowan: 1+ assists | 0.331 | 0.205 | 30/89 | +0.017 | STANDARD |
| Kirill Marchenko: 1+ points | 0.465 | 0.365 | 61/88 | -0.162 | STANDARD |
| Darren Raddysh: 1+ assists | 0.292 | 0.390 | 47/69 | +0.003 | STANDARD |

**WSH @ TBL** · priced 127/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.03, exp saves 21.9 (sd 6.13), pull risk 0.05
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.7, exp saves 24.51 (sd 6.84), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ points | 0.726 | 0.400 | 78/98 | -0.067 | STANDARD |
| John Carlson: 1+ points | 0.352 | 0.585 | 63/46 | +0.171 | STANDARD |
| John Carlson: 1+ assists | 0.260 | 0.475 | 56/61 | +0.114 | STANDARD |
| Charle-Edouard D'Astous: 1+ points | 0.360 | 0.175 | 33/98 | +0.015 | STANDARD |
| Charle-Edouard D'Astous: 1+ assists | 0.309 | 0.145 | 27/98 | +0.026 | STANDARD |
| Anthony Cirelli: 1+ assists | 0.331 | 0.215 | 28/85 | +0.036 | STANDARD |

**CAR @ PHI** · priced 137/137 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.3 (sd 6.77), pull risk 0.05
- CAR net: Brandon Bussi (PROJECTED) exp shots 23.27, exp saves 20.06 (sd 5.73), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charles Alexis Legault: 1+ goals | 0.039 | 0.495 | 98/99 | -0.030 | STANDARD |
| K'Andre Miller: 1+ points | 0.366 | 0.230 | 36/90 | -0.010 | STANDARD |
| Sean Couturier: 1+ goals | 0.171 | 0.060 | 10/98 | +0.065 | STANDARD |
| K'Andre Miller: 1+ assists | 0.322 | 0.220 | 30/86 | +0.007 | STANDARD |
| Christian Dvorak: 1+ points | 0.462 | 0.370 | 43/69 | +0.015 | STANDARD |
| Christian Dvorak: 1+ goals | 0.219 | 0.140 | 19/91 | +0.019 | STANDARD |

**MTL @ PIT** · priced 112/116 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- PIT net: Arturs Silovs (PROJECTED) exp shots 24.51, exp saves 21.3 (sd 6.12), pull risk 0.06
- MTL net: Jakub Dobes (PROJECTED) exp shots 29.53, exp saves 25.22 (sd 6.93), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ points | 0.607 | 0.375 | 73/98 | -0.137 | STANDARD |
| Rickard Rakell: 1+ points | 0.648 | 0.465 | 55/62 | +0.080 | STANDARD |
| Evgeni Malkin: 1+ points | 0.594 | 0.470 | 55/61 | +0.027 | STANDARD |
| Sidney Crosby: 2+ points | 0.295 | 0.175 | 31/96 | -0.030 | STANDARD |
| Erik Karlsson: 1+ points | 0.585 | 0.465 | 55/62 | +0.017 | STANDARD |
| Erik Karlsson: 2+ points | 0.221 | 0.110 | 20/98 | +0.010 | STANDARD |

**UTA @ CBJ** · priced 122/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.84, exp saves 23.33 (sd 6.36), pull risk 0.055
- UTA net: Karel Vejmelka (PROJECTED) exp shots 28.0, exp saves 23.96 (sd 6.66), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dmitri Simashev: 1+ goals | 0.030 | 0.480 | 95/99 | -0.021 | STANDARD |
| Adam Fantilli: 1+ points | 0.556 | 0.320 | 62/98 | -0.080 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.138 | 0.310 | 38/76 | +0.089 | STANDARD |
| Vincent Trocheck: 1+ points | 0.315 | 0.485 | 52/55 | +0.118 | STANDARD |
| Charlie Coyle: 1+ points | 0.557 | 0.405 | 49/68 | +0.049 | STANDARD |
| Matthew Knies: 1+ points | 0.460 | 0.335 | 57/90 | -0.127 | STANDARD |

**SEA @ EDM** · priced 129/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 25.57, exp saves 22.44 (sd 6.23), pull risk 0.052
- SEA net: Joey Daccord (PROJECTED) exp shots 30.84, exp saves 26.07 (sd 7.2), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ points | 0.757 | 0.480 | 85/89 | -0.102 | STANDARD |
| Evan Bouchard: 1+ points | 0.691 | 0.430 | 74/88 | -0.063 | STANDARD |
| Leon Draisaitl: 1+ points | 0.699 | 0.495 | 81/82 | -0.122 | STANDARD |
| Mattias Ekholm: 1+ points | 0.454 | 0.275 | 35/80 | +0.088 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.378 | 0.205 | 27/86 | +0.094 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.378 | 0.210 | 28/86 | +0.084 | STANDARD |

**NJD @ NYI** · priced 85/85 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.14, exp saves 24.54 (sd 6.48), pull risk 0.046
- NJD net: Jake Allen (PROJECTED) exp shots 27.75, exp saves 24.0 (sd 6.61), pull risk 0.057

**DAL @ NSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.51, exp saves 23.92 (sd 6.5), pull risk 0.057
- DAL net: Jake Oettinger (PROJECTED) exp shots 26.36, exp saves 22.77 (sd 6.42), pull risk 0.062

**BOS @ MIN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.46, exp saves 24.13 (sd 6.56), pull risk 0.05
- BOS net: Jeremy Swayman (PROJECTED) exp shots 30.36, exp saves 25.72 (sd 7.2), pull risk 0.082

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
