# NHL slate 2026-10-03 — RESEARCH_ONLY

generated 2026-10-03T13:24:02Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 13 · simulated (not started): 13 · markets on board: 3897 · contracts joined: 2006 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 1681, 'NO_EDGE': 160, 'OK': 165}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'player_assists': 255, 'game_early_goal': 13, 'first_goal': 385, 'game_winner': 26, 'player_goals': 385, 'game_overtime': 13, 'player_points': 318, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 2026-10-03T23:00:00Z | T-6h | 0.664 | 0.336 | 0.164 | 6.12 | 3.57 | 2.55 | 159 (25/134) | PROJECTED/PROJECTED |
| OTT @ TOR | 2026-10-03T23:00:00Z | T-6h | 0.459 | 0.541 | 0.172 | 6.64 | 3.18 | 3.45 | 182 (25/157) | PROJECTED/PROJECTED |
| WSH @ TBL | 2026-10-03T23:00:00Z | T-6h | 0.623 | 0.377 | 0.171 | 6.22 | 3.50 | 2.72 | 180 (25/155) | PROJECTED/CONFIRMED |
| CAR @ PHI | 2026-10-03T23:00:00Z | T-6h | 0.475 | 0.525 | 0.184 | 5.81 | 2.83 | 2.98 | 188 (25/163) | PROJECTED/PROJECTED |
| MTL @ PIT | 2026-10-03T23:00:00Z | T-6h | 0.563 | 0.437 | 0.169 | 6.56 | 3.49 | 3.07 | 167 (25/142) | PROJECTED/PROJECTED |
| UTA @ CBJ | 2026-10-03T23:00:00Z | T-6h | 0.540 | 0.460 | 0.182 | 6.10 | 3.16 | 2.94 | 173 (25/148) | PROJECTED/PROJECTED |
| SEA @ EDM | 2026-10-03T23:00:00Z | T-6h | 0.616 | 0.384 | 0.169 | 6.65 | 3.72 | 2.94 | 180 (25/155) | PROJECTED/PROJECTED |
| NJD @ NYI | 2026-10-03T23:30:00Z | T-6h | 0.538 | 0.462 | 0.186 | 5.59 | 2.90 | 2.70 | 171 (25/146) | CONFIRMED/PROJECTED |
| DAL @ NSH | 2026-10-04T00:00:00Z | T-6h | 0.505 | 0.495 | 0.182 | 6.00 | 3.01 | 2.98 | 164 (25/139) | PROJECTED/PROJECTED |
| BOS @ MIN | 2026-10-04T00:00:00Z | T-6h | 0.632 | 0.368 | 0.170 | 6.35 | 3.60 | 2.75 | 170 (25/145) | PROJECTED/PROJECTED |
| STL @ COL | 2026-10-04T01:00:00Z | T-6h | 0.694 | 0.306 | 0.148 | 6.55 | 3.93 | 2.62 | 170 (25/145) | PROJECTED/PROBABLE |
| CGY @ VAN | 2026-10-04T02:00:00Z | T-12h | 0.493 | 0.507 | 0.174 | 6.33 | 3.15 | 3.19 | 51 (25/26) | PROJECTED/PROJECTED |
| LAK @ SJS | 2026-10-04T02:00:00Z | T-12h | 0.550 | 0.450 | 0.176 | 6.32 | 3.31 | 3.02 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4 | team_total | 0.293 | 0.410 | 0.385 | 42 | 60 | no | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ3 | team_total | 0.514 | 0.630 | 0.608 | 64 | 38 | no | +0.089 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT2 | game_spread | 0.350 | 0.255 | 0.273 | 26 | 75 | yes | +0.077 | OK |
| KXNHLGAME-26OCT03MTLPIT-MTL | game_winner | 0.437 | 0.535 | 0.515 | 54 | 47 | no | +0.076 | OK |
| KXNHLGAME-26OCT03MTLPIT-PIT | game_winner | 0.563 | 0.465 | 0.485 | 47 | 54 | yes | +0.076 | OK |
| KXNHLTOTAL-26OCT03NJNYI-6 | game_total | 0.457 | 0.555 | 0.536 | 56 | 45 | no | +0.075 | OK |
| KXNHLGAME-26OCT03NJNYI-NJ | game_winner | 0.462 | 0.555 | 0.536 | 56 | 45 | no | +0.071 | OK |
| KXNHLGAME-26OCT03NJNYI-NYI | game_winner | 0.538 | 0.445 | 0.464 | 45 | 56 | yes | +0.071 | OK |
| KXNHLTOTAL-26OCT03NJNYI-5 | game_total | 0.690 | 0.775 | 0.759 | 78 | 23 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ2 | team_total | 0.744 | 0.830 | 0.815 | 84 | 18 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT03NJNYI-7 | game_total | 0.349 | 0.435 | 0.417 | 44 | 57 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ2 | game_spread | 0.244 | 0.325 | 0.308 | 33 | 68 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5 | team_total | 0.138 | 0.220 | 0.201 | 23 | 79 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4 | team_total | 0.475 | 0.395 | 0.411 | 40 | 61 | yes | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT4 | team_total | 0.464 | 0.385 | 0.401 | 39 | 62 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT3 | game_spread | 0.225 | 0.155 | 0.167 | 16 | 85 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT3 | team_total | 0.680 | 0.605 | 0.621 | 61 | 40 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ3 | game_spread | 0.136 | 0.205 | 0.189 | 21 | 80 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL2 | game_spread | 0.242 | 0.315 | 0.299 | 32 | 69 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT5 | team_total | 0.283 | 0.215 | 0.228 | 22 | 79 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT03NJNYI-4 | game_total | 0.791 | 0.855 | 0.844 | 86 | 15 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT03NJNYI-8 | game_total | 0.180 | 0.245 | 0.231 | 25 | 76 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL3 | game_spread | 0.142 | 0.205 | 0.191 | 21 | 80 | no | +0.046 | OK |
| KXNHLGAME-26OCT03OTTTOR-TOR | game_winner | 0.459 | 0.525 | 0.512 | 53 | 48 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL3 | team_total | 0.591 | 0.655 | 0.643 | 66 | 35 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT5 | team_total | 0.273 | 0.210 | 0.222 | 22 | 80 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-6 | game_total | 0.627 | 0.565 | 0.578 | 57 | 44 | yes | +0.040 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-8 | game_total | 0.322 | 0.260 | 0.272 | 27 | 75 | yes | +0.038 | OK |
| KXNHLGAME-26OCT03DALNSH-NSH | game_winner | 0.505 | 0.445 | 0.457 | 45 | 56 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-9 | game_total | 0.237 | 0.180 | 0.191 | 19 | 83 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT3 | team_total | 0.673 | 0.615 | 0.627 | 62 | 39 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NYI2 | game_spread | 0.298 | 0.245 | 0.255 | 25 | 76 | yes | +0.035 | OK |
| KXNHLGAME-26OCT03OTTTOR-OTT | game_winner | 0.541 | 0.485 | 0.496 | 49 | 52 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-OTT2 | game_spread | 0.328 | 0.275 | 0.285 | 28 | 73 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL4 | team_total | 0.359 | 0.425 | 0.412 | 44 | 59 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT03CARPHI-5 | game_total | 0.724 | 0.775 | 0.765 | 78 | 23 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL3 | team_total | 0.581 | 0.645 | 0.633 | 66 | 37 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL4 | team_total | 0.380 | 0.440 | 0.428 | 45 | 57 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT6 | team_total | 0.139 | 0.085 | 0.094 | 10 | 93 | yes | +0.032 | OK |
| KXNHLGAME-26OCT03UTACBJ-UTA | game_winner | 0.460 | 0.515 | 0.504 | 52 | 49 | no | +0.032 | OK |
| KXNHLGAME-26OCT03UTACBJ-CBJ | game_winner | 0.540 | 0.485 | 0.496 | 49 | 52 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL2 | game_spread | 0.273 | 0.325 | 0.314 | 33 | 68 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL3 | game_spread | 0.158 | 0.205 | 0.195 | 21 | 80 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT03NJNYI-9 | game_total | 0.120 | 0.165 | 0.155 | 17 | 84 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT03CARPHI-7 | game_total | 0.383 | 0.435 | 0.424 | 44 | 57 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL2 | team_total | 0.800 | 0.845 | 0.837 | 85 | 16 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT03CARPHI-6 | game_total | 0.493 | 0.545 | 0.535 | 55 | 46 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-7 | game_total | 0.517 | 0.460 | 0.471 | 47 | 55 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ6 | team_total | 0.055 | 0.100 | 0.089 | 11 | 91 | no | +0.029 | OK |
| KXNHLGAME-26OCT03DALNSH-DAL | game_winner | 0.495 | 0.545 | 0.535 | 55 | 46 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-TOR3 | game_spread | 0.153 | 0.195 | 0.186 | 20 | 81 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-10 | game_total | 0.120 | 0.080 | 0.087 | 9 | 93 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT03SEAEDM-SEA5 | team_total | 0.183 | 0.145 | 0.152 | 15 | 86 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT03CARPHI-CAR4 | team_total | 0.359 | 0.415 | 0.404 | 43 | 60 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT03CARPHI-CAR3 | game_spread | 0.174 | 0.215 | 0.206 | 22 | 79 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT03CARPHI-4 | game_total | 0.817 | 0.855 | 0.848 | 86 | 15 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT03CARPHI-CAR3 | team_total | 0.580 | 0.630 | 0.620 | 64 | 38 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT03STLCOL-7 | game_total | 0.500 | 0.455 | 0.464 | 46 | 55 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-6 | game_total | 0.550 | 0.595 | 0.586 | 60 | 41 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL5 | team_total | 0.186 | 0.235 | 0.224 | 25 | 78 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT03MTLPIT-8 | game_total | 0.316 | 0.275 | 0.283 | 28 | 73 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT03CARPHI-8 | game_total | 0.206 | 0.245 | 0.237 | 25 | 76 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT03SEAEDM-SEA2 | game_spread | 0.201 | 0.165 | 0.172 | 17 | 84 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT2 | team_total | 0.851 | 0.815 | 0.823 | 82 | 19 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT03WSHTB-WSH3 | game_spread | 0.102 | 0.135 | 0.128 | 14 | 87 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT6 | team_total | 0.137 | 0.090 | 0.098 | 11 | 93 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-7 | game_total | 0.432 | 0.475 | 0.466 | 48 | 53 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL5 | team_total | 0.207 | 0.245 | 0.237 | 25 | 76 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-5 | game_total | 0.759 | 0.795 | 0.788 | 80 | 21 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT03STLCOL-6 | game_total | 0.617 | 0.575 | 0.583 | 58 | 43 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF4 | team_total | 0.493 | 0.540 | 0.531 | 55 | 47 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT03UTACBJ-UTA3 | team_total | 0.565 | 0.610 | 0.601 | 62 | 40 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT03UTACBJ-CBJ2 | game_spread | 0.312 | 0.275 | 0.282 | 28 | 73 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT03STLCOL-8 | game_total | 0.312 | 0.275 | 0.282 | 28 | 73 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT03DALNSH-NSH2 | game_spread | 0.281 | 0.245 | 0.252 | 25 | 76 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT03NJNYI-3 | game_total | 0.939 | 0.965 | 0.961 | 97 | 4 | no | +0.018 | OK |
| KXNHLGAME-26OCT03SEAEDM-EDM | game_winner | 0.616 | 0.655 | 0.647 | 66 | 35 | no | +0.018 | OK |
| KXNHLGAME-26OCT03SEAEDM-SEA | game_winner | 0.384 | 0.345 | 0.353 | 35 | 66 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL2 | team_total | 0.792 | 0.835 | 0.827 | 85 | 18 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT03CARPHI-CAR5 | team_total | 0.181 | 0.220 | 0.212 | 23 | 79 | no | +0.017 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 0.664 | 0.644 | 0.164 | 0.206 | 6.12 | 6.36 | 0.997/1.003 | KXNHLTEAMTOTAL-26OCT03CHIBUF-CHI3 +0.047 |
| OTT @ TOR | 0.459 | 0.456 | 0.172 | 0.219 | 6.64 | 6.13 | 0.978/0.998 | KXNHLTOTAL-26OCT03OTTTOR-6 -0.081 |
| WSH @ TBL | 0.623 | 0.606 | 0.171 | 0.214 | 6.22 | 6.27 | 0.957/1.015 | KXNHLTEAMTOTAL-26OCT03WSHTB-WSH3 +0.027 |
| CAR @ PHI | 0.475 | 0.543 | 0.184 | 0.224 | 5.81 | 5.93 | 0.991/0.997 | KXNHLGAME-26OCT03CARPHI-PHI +0.068 |
| MTL @ PIT | 0.563 | 0.569 | 0.169 | 0.215 | 6.56 | 6.62 | 1.033/0.952 | KXNHLTOTAL-26OCT03MTLPIT-5 +0.018 |
| UTA @ CBJ | 0.540 | 0.544 | 0.182 | 0.219 | 6.10 | 6.32 | 0.964/0.992 | KXNHLTOTAL-26OCT03UTACBJ-7 +0.040 |
| SEA @ EDM | 0.616 | 0.620 | 0.169 | 0.202 | 6.65 | 6.55 | 1.009/1.005 | KXNHLTOTAL-26OCT03SEAEDM-8 -0.020 |
| NJD @ NYI | 0.538 | 0.536 | 0.186 | 0.228 | 5.59 | 5.86 | 0.947/0.987 | KXNHLTOTAL-26OCT03NJNYI-5 +0.046 |
| DAL @ NSH | 0.505 | 0.530 | 0.182 | 0.228 | 6.00 | 6.09 | 1.000/0.976 | KXNHLTEAMTOTAL-26OCT03DALNSH-NSH3 +0.027 |
| BOS @ MIN | 0.632 | 0.615 | 0.170 | 0.208 | 6.35 | 6.44 | 1.003/0.986 | KXNHLTEAMTOTAL-26OCT03BOSMIN-BOS2 +0.023 |
| STL @ COL | 0.694 | 0.634 | 0.148 | 0.205 | 6.55 | 6.42 | 0.973/1.024 | KXNHLSPREAD-26OCT03STLCOL-COL2 -0.070 |
| CGY @ VAN | 0.493 | 0.561 | 0.174 | 0.217 | 6.33 | 6.34 | 1.025/0.986 | KXNHLGAME-26OCT03CGYVAN-VAN +0.068 |
| LAK @ SJS | 0.550 | 0.521 | 0.176 | 0.222 | 6.32 | 6.12 | 1.034/0.992 | KXNHLTEAMTOTAL-26OCT03LASJ-SJ4 -0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 37 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Greene: 1+ goals YES @ 12c · p 0.1628 (adj 0.1446) · $2.11 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 64c · p 0.747 (adj 0.6742) · $7.4 · thesis CHI:SUPPRESSED
- Tage Thompson: 1+ goals NO @ 60c · p 0.6436 (adj 0.6277) · $3.43 · thesis BUF:SUPPRESSED
- Stephen Halliday: 1+ goals YES @ 9c · p 0.1413 (adj 0.1197) · $2.59 · thesis OTT:OFFENSE_4PLUS
- Nick Cousins: 1+ goals YES @ 11c · p 0.1427 (adj 0.1295) · $1.54 · thesis OTT:OFFENSE_4PLUS
- Darren Raddysh: 1+ assists NO @ 58c · p 0.7102 (adj 0.6158) · $6.38 · thesis TOR:SUPPRESSED
- Claude Giroux: 1+ assists YES @ 27c · p 0.3706 (adj 0.2955) · $1.04 · thesis OTT:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 51c · p 0.7404 (adj 0.5711) · $6.87 · thesis TBL:SUPPRESSED
- John Carlson: 2+ assists NO @ 86c · p 0.9655 (adj 0.8872) · $6.87 · thesis TBL:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2143 (adj 0.1995) · $2.67 · thesis WSH:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 10c · p 0.1801 (adj 0.1563) · $5.42 · thesis PHI:OFFENSE_4PLUS
- Carl Grundstrom: 1+ goals YES @ 8c · p 0.1373 (adj 0.1192) · $3.6 · thesis PHI:OFFENSE_4PLUS
- Noel Acciari: 1+ goals YES @ 9c · p 0.1331 (adj 0.1186) · $2.61 · thesis PHI:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 18c · p 0.227 (adj 0.2102) · $2.65 · thesis PHI:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.2096 (adj 0.1872) · $5.77 · thesis PIT:WINS_BY_2PLUS
- Trevor van Riemsdyk: 1+ goals YES @ 4c · p 0.0718 (adj 0.0614) · $1.83 · thesis PIT:OFFENSE_4PLUS
- Pittsburgh wins by over 1.5 goals YES @ 26c · p 0.3477 (adj 0.3014) · $1.13 · thesis PIT:WINS_BY_2PLUS
- Sidney Crosby: 1+ goals YES @ 31c · p 0.3619 (adj 0.3464) · $3.23 · thesis PIT:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 21c · p 0.2706 (adj 0.248) · $3.73 · thesis CBJ:OFFENSE_4PLUS
- Vincent Trocheck: 2+ assists NO @ 94c · p 0.991 (adj 0.958) · $9.52 · thesis DIFFUSE
- Danton Heinen: 1+ goals YES @ 10c · p 0.1317 (adj 0.12) · $1.69 · thesis CBJ:OFFENSE_4PLUS
- Conor Garland: 1+ goals NO @ 83c · p 0.8634 (adj 0.8513) · $8.7 · thesis CBJ:SUPPRESSED
- Connor McDavid: 2+ assists NO @ 69c · p 0.8167 (adj 0.7278) · $8.64 · thesis EDM:SUPPRESSED
- Mattias Ekholm: 1+ assists YES @ 26c · p 0.3879 (adj 0.295) · $3.31 · thesis EDM:OFFENSE_4PLUS
- Kasperi Kapanen: 1+ goals NO @ 77c · p 0.8052 (adj 0.7939) · $5.64 · thesis EDM:SUPPRESSED
- New Jersey wins by over 1.5 goals NO @ 68c · p 0.7587 (adj 0.7168) · $6.78 · thesis NYI:WINS
- New Jersey wins NO @ 45c · p 0.5294 (adj 0.4872) · $2.24 · thesis NYI:WINS
- New Jersey wins by over 2.5 goals NO @ 80c · p 0.8559 (adj 0.8255) · $2.15 · thesis NYI:WINS
- Kyle Palmieri: 1+ assists NO @ 70c · p 0.816 (adj 0.7276) · $8.7 · thesis NYI:SUPPRESSED
- Nashville wins YES @ 45c · p 0.5364 (adj 0.4907) · $3.4 · thesis NSH:WINS
- Dallas wins by over 1.5 goals NO @ 68c · p 0.7527 (adj 0.7139) · $3.51 · thesis NSH:WINS
- Roope Hintz: 1+ assists NO @ 66c · p 0.7624 (adj 0.6861) · $2.87 · thesis DAL:SUPPRESSED
- Mikko Rantanen: 1+ assists NO @ 52c · p 0.6361 (adj 0.5476) · $1.34 · thesis DAL:SUPPRESSED
- Elias Lindholm: 1+ goals YES @ 17c · p 0.2274 (adj 0.2081) · $3.77 · thesis BOS:OFFENSE_4PLUS
- Olli Maatta: 1+ goals YES @ 5c · p 0.0809 (adj 0.0694) · $1.67 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 24c · p 0.2792 (adj 0.2631) · $1.64 · thesis MIN:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 56c · p 0.6055 (adj 0.5879) · $3.03 · thesis COL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BUF** · priced 108/108 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 24.71, exp saves 21.79 (sd 6.0), pull risk 0.048
- CHI net: Spencer Knight (PROJECTED) exp shots 30.42, exp saves 25.66 (sd 7.17), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.253 | 0.365 | 37/64 | +0.091 | STANDARD |
| Patrick Kane: 1+ points | 0.431 | 0.530 | 55/49 | +0.062 | STANDARD |
| Rasmus Dahlin: 2+ points | 0.242 | 0.155 | 29/98 | -0.063 | STANDARD |
| Tage Thompson: 2+ points | 0.222 | 0.305 | 33/72 | +0.044 | STANDARD |
| Tage Thompson: 1+ points | 0.586 | 0.665 | 68/35 | +0.048 | STANDARD |
| Ryan Greene: 1+ goals | 0.163 | 0.090 | 12/94 | +0.035 | STANDARD |

**OTT @ TOR** · priced 123/131 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 31.35, exp saves 27.08 (sd 7.18), pull risk 0.062
- OTT net: Linus Ullmark (PROJECTED) exp shots 24.74, exp saves 21.66 (sd 5.97), pull risk 0.052

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darren Raddysh: 1+ assists | 0.290 | 0.435 | 45/58 | +0.113 | STANDARD |
| Darren Raddysh: 1+ points | 0.383 | 0.520 | 53/49 | +0.110 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.273 | 0.390 | 41/63 | +0.081 | STANDARD |
| Claude Giroux: 1+ assists | 0.371 | 0.255 | 27/76 | +0.087 | STANDARD |
| Kirill Marchenko: 1+ points | 0.460 | 0.570 | 59/45 | +0.073 | STANDARD |
| Claude Giroux: 1+ points | 0.495 | 0.390 | 41/63 | +0.069 | STANDARD |

**WSH @ TBL** · priced 127/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.03, exp saves 21.9 (sd 6.13), pull risk 0.05
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.7, exp saves 24.51 (sd 6.84), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.260 | 0.520 | 55/51 | +0.213 | STANDARD |
| John Carlson: 1+ points | 0.352 | 0.600 | 62/42 | +0.211 | STANDARD |
| John Carlson: 2+ points | 0.073 | 0.235 | 27/80 | +0.115 | STANDARD |
| John Carlson: 2+ assists | 0.035 | 0.155 | 17/86 | +0.097 | STANDARD |
| Alex Tuch: 1+ goals | 0.246 | 0.155 | 26/95 | -0.027 | STANDARD |
| Anthony Cirelli: 1+ points | 0.502 | 0.420 | 44/60 | +0.044 | STANDARD |

**CAR @ PHI** · priced 137/137 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.35 (sd 6.7), pull risk 0.048
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.27, exp saves 20.0 (sd 5.76), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ points | 0.467 | 0.570 | 59/45 | +0.065 | STANDARD |
| Sebastian Aho: 1+ assists | 0.295 | 0.395 | 41/62 | +0.068 | STANDARD |
| Sean Couturier: 1+ goals | 0.180 | 0.085 | 10/93 | +0.074 | STANDARD |
| Trevor Zegras: 2+ points | 0.166 | 0.090 | 16/98 | -0.003 | STANDARD |
| Sebastian Aho: 2+ points | 0.131 | 0.205 | 22/81 | +0.048 | STANDARD |
| Carl Grundstrom: 1+ goals | 0.137 | 0.065 | 8/95 | +0.052 | STANDARD |

**MTL @ PIT** · priced 112/116 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- PIT net: Arturs Silovs (PROJECTED) exp shots 24.51, exp saves 21.3 (sd 6.12), pull risk 0.06
- MTL net: Jakub Dobes (PROJECTED) exp shots 29.53, exp saves 25.22 (sd 6.93), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Egor Chinakhov: 1+ goals | 0.274 | 0.155 | 25/94 | +0.011 | STANDARD |
| Rickard Rakell: 1+ goals | 0.388 | 0.275 | 29/74 | +0.083 | STANDARD |
| Rickard Rakell: 1+ points | 0.648 | 0.535 | 56/49 | +0.070 | STANDARD |
| Filip Hallander: 1+ goals | 0.218 | 0.110 | 14/92 | +0.070 | STANDARD |
| Rickard Rakell: 2+ points | 0.287 | 0.180 | 20/84 | +0.076 | STANDARD |
| Nick Suzuki: 1+ assists | 0.457 | 0.560 | 58/46 | +0.066 | STANDARD |

**UTA @ CBJ** · priced 122/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.84, exp saves 23.33 (sd 6.36), pull risk 0.055
- UTA net: Karel Vejmelka (PROJECTED) exp shots 28.0, exp saves 23.96 (sd 6.66), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.138 | 0.320 | 36/72 | +0.128 | STANDARD |
| Adam Fantilli: 1+ assists | 0.364 | 0.205 | 39/98 | -0.043 | STANDARD |
| Vincent Trocheck: 1+ points | 0.315 | 0.470 | 48/54 | +0.128 | STANDARD |
| Matthew Knies: 1+ assists | 0.245 | 0.355 | 37/66 | +0.079 | STANDARD |
| Charlie Coyle: 1+ points | 0.557 | 0.460 | 48/56 | +0.059 | STANDARD |
| Charlie Coyle: 1+ goals | 0.271 | 0.180 | 21/85 | +0.049 | STANDARD |

**SEA @ EDM** · priced 129/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 25.57, exp saves 22.39 (sd 6.13), pull risk 0.054
- SEA net: Joey Daccord (PROJECTED) exp shots 30.84, exp saves 26.05 (sd 7.23), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mattias Ekholm: 1+ points | 0.468 | 0.320 | 34/70 | +0.113 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.388 | 0.245 | 26/77 | +0.114 | STANDARD |
| Leon Draisaitl: 2+ points | 0.338 | 0.480 | 50/54 | +0.104 | STANDARD |
| Connor McDavid: 2+ assists | 0.183 | 0.320 | 33/69 | +0.112 | STANDARD |
| Connor McDavid: 1+ assists | 0.538 | 0.665 | 69/36 | +0.085 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.373 | 0.250 | 27/77 | +0.089 | STANDARD |

**NJD @ NYI** · priced 120/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.14, exp saves 24.54 (sd 6.48), pull risk 0.046
- NJD net: Jake Allen (PROJECTED) exp shots 27.75, exp saves 24.0 (sd 6.61), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.153 | 0.340 | 37/69 | +0.142 | STANDARD |
| Luke Evangelista: 1+ points | 0.296 | 0.480 | 50/54 | +0.147 | STANDARD |
| Anthony Mantha: 1+ assists | 0.157 | 0.295 | 32/73 | +0.100 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.184 | 0.320 | 34/70 | +0.101 | STANDARD |
| Anthony Mantha: 1+ points | 0.332 | 0.460 | 48/56 | +0.091 | STANDARD |
| Jack Hughes: 1+ assists | 0.370 | 0.485 | 50/53 | +0.082 | STANDARD |

**DAL @ NSH** · priced 113/113 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.51, exp saves 23.94 (sd 6.5), pull risk 0.052
- DAL net: Casey DeSmith (PROJECTED) exp shots 26.36, exp saves 22.74 (sd 6.39), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 1+ assists | 0.364 | 0.500 | 52/52 | +0.099 | STANDARD |
| Roope Hintz: 1+ assists | 0.238 | 0.355 | 37/66 | +0.087 | STANDARD |
| Mikko Rantanen: 1+ points | 0.522 | 0.635 | 64/37 | +0.092 | STANDARD |
| Miro Heiskanen: 1+ points | 0.470 | 0.575 | 59/44 | +0.073 | STANDARD |
| Roope Hintz: 1+ points | 0.432 | 0.525 | 55/50 | +0.051 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.412 | 0.505 | 52/51 | +0.060 | STANDARD |

**BOS @ MIN** · priced 117/119 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.46, exp saves 24.11 (sd 6.49), pull risk 0.054
- BOS net: Michael DiPietro (PROJECTED) exp shots 30.36, exp saves 25.68 (sd 7.13), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 1+ points | 0.668 | 0.355 | 69/98 | -0.037 | STANDARD |
| Quinn Hughes: 1+ points | 0.658 | 0.380 | 66/90 | -0.018 | STANDARD |
| Max Shabanov: 1+ assists | 0.206 | 0.335 | 40/73 | +0.050 | STANDARD |
| Elias Lindholm: 1+ points | 0.473 | 0.350 | 37/67 | +0.086 | STANDARD |
| Max Shabanov: 1+ points | 0.360 | 0.470 | 54/60 | +0.023 | STANDARD |
| Elias Lindholm: 1+ assists | 0.321 | 0.220 | 24/80 | +0.068 | STANDARD |

**STL @ COL** · priced 119/119 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Scott Wedgewood (PROJECTED) exp shots 24.45, exp saves 21.44 (sd 5.87), pull risk 0.049
- STL net: Jordan Binnington (PROBABLE) exp shots 31.38, exp saves 26.42 (sd 7.26), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Martin Necas: 1+ points | 0.653 | 0.370 | 72/98 | -0.081 | STANDARD |
| Nathan MacKinnon: 1+ points | 0.702 | 0.440 | 84/96 | -0.147 | STANDARD |
| Cale Makar: 1+ points | 0.536 | 0.360 | 70/98 | -0.178 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.344 | 0.520 | 54/50 | +0.138 | STANDARD |
| Cale Makar: 1+ assists | 0.433 | 0.605 | 63/42 | +0.130 | STANDARD |
| Cale Makar: 2+ points | 0.184 | 0.335 | 34/67 | +0.131 | STANDARD |

**CGY @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 28.38, exp saves 24.72 (sd 6.61), pull risk 0.056
- CGY net: Devin Cooley (PROJECTED) exp shots 28.2, exp saves 24.24 (sd 6.68), pull risk 0.071

**LAK @ SJS** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.98, exp saves 24.34 (sd 6.56), pull risk 0.055
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.75, exp saves 23.27 (sd 6.38), pull risk 0.057

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
