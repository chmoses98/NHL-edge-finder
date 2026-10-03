# NHL slate 2026-10-03 — RESEARCH_ONLY

generated 2026-10-03T14:23:59Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 13 · simulated (not started): 13 · markets on board: 4115 · contracts joined: 2224 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 1899, 'NO_EDGE': 160, 'OK': 165}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'player_assists': 297, 'game_early_goal': 13, 'first_goal': 454, 'game_winner': 26, 'player_goals': 453, 'game_overtime': 13, 'player_points': 357, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

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
| CGY @ VAN | 2026-10-04T02:00:00Z | T-6h | 0.493 | 0.507 | 0.174 | 6.33 | 3.15 | 3.19 | 159 (25/134) | PROJECTED/PROJECTED |
| LAK @ SJS | 2026-10-04T02:00:00Z | T-6h | 0.550 | 0.450 | 0.176 | 6.32 | 3.31 | 3.02 | 161 (25/136) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4 | team_total | 0.293 | 0.420 | 0.393 | 43 | 59 | no | +0.100 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ3 | team_total | 0.514 | 0.625 | 0.604 | 63 | 38 | no | +0.089 | OK |
| KXNHLGAME-26OCT03NJNYI-NYI | game_winner | 0.538 | 0.435 | 0.456 | 44 | 57 | yes | +0.081 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT2 | game_spread | 0.350 | 0.255 | 0.273 | 26 | 75 | yes | +0.077 | OK |
| KXNHLGAME-26OCT03MTLPIT-MTL | game_winner | 0.437 | 0.535 | 0.515 | 54 | 47 | no | +0.076 | OK |
| KXNHLGAME-26OCT03MTLPIT-PIT | game_winner | 0.563 | 0.465 | 0.485 | 47 | 54 | yes | +0.076 | OK |
| KXNHLTOTAL-26OCT03NJNYI-6 | game_total | 0.457 | 0.555 | 0.536 | 56 | 45 | no | +0.075 | OK |
| KXNHLGAME-26OCT03NJNYI-NJ | game_winner | 0.462 | 0.555 | 0.536 | 56 | 45 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5 | team_total | 0.138 | 0.230 | 0.209 | 24 | 78 | no | +0.070 | OK |
| KXNHLTOTAL-26OCT03NJNYI-5 | game_total | 0.690 | 0.775 | 0.759 | 78 | 23 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ2 | team_total | 0.744 | 0.835 | 0.819 | 85 | 18 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT03NJNYI-7 | game_total | 0.349 | 0.435 | 0.417 | 44 | 57 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ3 | game_spread | 0.136 | 0.215 | 0.197 | 22 | 79 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ2 | game_spread | 0.244 | 0.325 | 0.308 | 33 | 68 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4 | team_total | 0.475 | 0.395 | 0.411 | 40 | 61 | yes | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT4 | team_total | 0.464 | 0.385 | 0.401 | 39 | 62 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT3 | game_spread | 0.225 | 0.155 | 0.167 | 16 | 85 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT3 | team_total | 0.680 | 0.605 | 0.621 | 61 | 40 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL2 | game_spread | 0.242 | 0.315 | 0.299 | 32 | 69 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT5 | team_total | 0.273 | 0.205 | 0.217 | 21 | 80 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT5 | team_total | 0.283 | 0.215 | 0.228 | 22 | 79 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT03NJNYI-4 | game_total | 0.791 | 0.855 | 0.844 | 86 | 15 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL3 | game_spread | 0.142 | 0.205 | 0.191 | 21 | 80 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT3 | team_total | 0.673 | 0.600 | 0.615 | 61 | 41 | yes | +0.046 | OK |
| KXNHLGAME-26OCT03OTTTOR-TOR | game_winner | 0.459 | 0.525 | 0.512 | 53 | 48 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL3 | team_total | 0.591 | 0.655 | 0.643 | 66 | 35 | no | +0.043 | OK |
| KXNHLGAME-26OCT03UTACBJ-CBJ | game_winner | 0.540 | 0.475 | 0.488 | 48 | 53 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL3 | game_spread | 0.158 | 0.215 | 0.202 | 22 | 79 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-6 | game_total | 0.627 | 0.565 | 0.578 | 57 | 44 | yes | +0.040 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-7 | game_total | 0.517 | 0.455 | 0.467 | 46 | 55 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-8 | game_total | 0.322 | 0.260 | 0.272 | 27 | 75 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT03NJNYI-8 | game_total | 0.180 | 0.240 | 0.227 | 25 | 77 | no | +0.038 | OK |
| KXNHLGAME-26OCT03DALNSH-NSH | game_winner | 0.505 | 0.445 | 0.457 | 45 | 56 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-9 | game_total | 0.237 | 0.180 | 0.191 | 19 | 83 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NYI2 | game_spread | 0.298 | 0.245 | 0.255 | 25 | 76 | yes | +0.035 | OK |
| KXNHLGAME-26OCT03OTTTOR-OTT | game_winner | 0.541 | 0.485 | 0.496 | 49 | 52 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-OTT2 | game_spread | 0.328 | 0.275 | 0.285 | 28 | 73 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL4 | team_total | 0.359 | 0.425 | 0.412 | 44 | 59 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT03CARPHI-5 | game_total | 0.724 | 0.775 | 0.765 | 78 | 23 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL3 | team_total | 0.581 | 0.645 | 0.633 | 66 | 37 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL4 | team_total | 0.380 | 0.440 | 0.428 | 45 | 57 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT6 | team_total | 0.139 | 0.085 | 0.094 | 10 | 93 | yes | +0.032 | OK |
| KXNHLGAME-26OCT03UTACBJ-UTA | game_winner | 0.460 | 0.515 | 0.504 | 52 | 49 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL2 | game_spread | 0.273 | 0.325 | 0.314 | 33 | 68 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT03NJNYI-9 | game_total | 0.120 | 0.165 | 0.155 | 17 | 84 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT03CARPHI-7 | game_total | 0.383 | 0.435 | 0.424 | 44 | 57 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT03CARPHI-6 | game_total | 0.493 | 0.545 | 0.535 | 55 | 46 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ6 | team_total | 0.055 | 0.100 | 0.089 | 11 | 91 | no | +0.029 | OK |
| KXNHLGAME-26OCT03DALNSH-DAL | game_winner | 0.495 | 0.545 | 0.535 | 55 | 46 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-TOR3 | game_spread | 0.153 | 0.195 | 0.186 | 20 | 81 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-4 | game_total | 0.847 | 0.885 | 0.878 | 89 | 12 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-10 | game_total | 0.120 | 0.080 | 0.087 | 9 | 93 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT03SEAEDM-SEA5 | team_total | 0.183 | 0.145 | 0.152 | 15 | 86 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT03CARPHI-CAR4 | team_total | 0.359 | 0.405 | 0.396 | 41 | 60 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT03CARPHI-CAR3 | game_spread | 0.174 | 0.215 | 0.206 | 22 | 79 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT03CARPHI-4 | game_total | 0.817 | 0.855 | 0.848 | 86 | 15 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-6 | game_total | 0.550 | 0.595 | 0.586 | 60 | 41 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL5 | team_total | 0.186 | 0.235 | 0.224 | 25 | 78 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT03MTLPIT-8 | game_total | 0.316 | 0.275 | 0.283 | 28 | 73 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT03SEAEDM-SEA2 | game_spread | 0.201 | 0.165 | 0.172 | 17 | 84 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT2 | team_total | 0.851 | 0.815 | 0.823 | 82 | 19 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT03UTACBJ-UTA3 | game_spread | 0.149 | 0.185 | 0.177 | 19 | 82 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT03WSHTB-WSH3 | game_spread | 0.102 | 0.135 | 0.128 | 14 | 87 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT6 | team_total | 0.137 | 0.090 | 0.098 | 11 | 93 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-7 | game_total | 0.432 | 0.475 | 0.466 | 48 | 53 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL5 | team_total | 0.207 | 0.245 | 0.237 | 25 | 76 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT03DALNSH-6 | game_total | 0.523 | 0.565 | 0.557 | 57 | 44 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL2 | team_total | 0.800 | 0.845 | 0.837 | 86 | 17 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-5 | game_total | 0.759 | 0.795 | 0.788 | 80 | 21 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF4 | team_total | 0.493 | 0.540 | 0.531 | 55 | 47 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT03UTACBJ-CBJ2 | game_spread | 0.312 | 0.275 | 0.282 | 28 | 73 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT03STLCOL-8 | game_total | 0.312 | 0.275 | 0.282 | 28 | 73 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT03DALNSH-NSH2 | game_spread | 0.281 | 0.245 | 0.252 | 25 | 76 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT03NJNYI-3 | game_total | 0.939 | 0.965 | 0.961 | 97 | 4 | no | +0.018 | OK |
| KXNHLGAME-26OCT03SEAEDM-SEA | game_winner | 0.384 | 0.345 | 0.353 | 35 | 66 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL2 | team_total | 0.792 | 0.835 | 0.827 | 85 | 18 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT03CARPHI-CAR5 | team_total | 0.181 | 0.220 | 0.212 | 23 | 79 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-8 | game_total | 0.249 | 0.285 | 0.278 | 29 | 72 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-OTT3 | game_spread | 0.206 | 0.175 | 0.181 | 18 | 83 | yes | +0.016 | OK |
| KXNHLSPREAD-26OCT03LASJ-LA3 | game_spread | 0.145 | 0.175 | 0.169 | 18 | 83 | no | +0.015 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 44 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Greene: 1+ goals YES @ 12c · p 0.1628 (adj 0.1496) · $2.06 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 64c · p 0.747 (adj 0.6742) · $5.46 · thesis CHI:SUPPRESSED
- Tage Thompson: 1+ goals NO @ 60c · p 0.6436 (adj 0.6277) · $2.49 · thesis BUF:SUPPRESSED
- Stephen Halliday: 1+ goals YES @ 9c · p 0.1413 (adj 0.1272) · $2.7 · thesis OTT:OFFENSE_4PLUS
- Hayden Hodgson: 1+ goals YES @ 8c · p 0.1097 (adj 0.1023) · $1.51 · thesis OTT:OFFENSE_4PLUS
- Nick Cousins: 1+ goals YES @ 11c · p 0.1427 (adj 0.1308) · $1.28 · thesis OTT:OFFENSE_4PLUS
- Easton Cowan: 1+ assists YES @ 27c · p 0.3371 (adj 0.2961) · $1.46 · thesis TOR:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 50c · p 0.7404 (adj 0.5711) · $6.98 · thesis TBL:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2143 (adj 0.202) · $2.25 · thesis WSH:OFFENSE_4PLUS
- Boone Jenner: 1+ goals YES @ 11c · p 0.144 (adj 0.1305) · $1.24 · thesis WSH:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 10c · p 0.1801 (adj 0.1576) · $4.17 · thesis PHI:OFFENSE_4PLUS
- Carl Grundstrom: 1+ goals YES @ 9c · p 0.1373 (adj 0.123) · $2.24 · thesis PHI:OFFENSE_4PLUS
- Mark Jankowski: 1+ goals NO @ 83c · p 0.8851 (adj 0.8701) · $6.98 · thesis CAR:SUPPRESSED
- Noel Acciari: 1+ goals YES @ 9c · p 0.1331 (adj 0.1186) · $1.94 · thesis PHI:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.2096 (adj 0.1872) · $4.35 · thesis PIT:WINS_BY_2PLUS
- Filip Hallander: 1+ goals YES @ 14c · p 0.2182 (adj 0.1949) · $4.25 · thesis PIT:OFFENSE_4PLUS
- Trevor van Riemsdyk: 1+ goals YES @ 4c · p 0.0718 (adj 0.0639) · $1.63 · thesis PIT:OFFENSE_4PLUS
- Sidney Crosby: 1+ goals YES @ 31c · p 0.3619 (adj 0.3452) · $2.42 · thesis PIT:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 67c · p 0.8619 (adj 0.7274) · $6.98 · thesis UTA:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 21c · p 0.2706 (adj 0.2517) · $3.17 · thesis CBJ:OFFENSE_4PLUS
- Vincent Trocheck: 2+ assists NO @ 94c · p 0.991 (adj 0.958) · $6.98 · thesis DIFFUSE
- Alex Formenton: 1+ goals YES @ 18c · p 0.2444 (adj 0.2208) · $3.29 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 69c · p 0.8167 (adj 0.7278) · $6.98 · thesis EDM:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 11c · p 0.1418 (adj 0.1314) · $1.36 · thesis SEA:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 34c · p 0.4616 (adj 0.3728) · $1.29 · thesis EDM:SUPPRESSED
- New York I wins YES @ 44c · p 0.5294 (adj 0.4822) · $2.24 · thesis NYI:WINS
- New Jersey wins by over 2.5 goals NO @ 79c · p 0.8559 (adj 0.8205) · $5.59 · thesis NYI:WINS
- New Jersey over 3.5 goals scored NO @ 59c · p 0.6751 (adj 0.6276) · $1.35 · thesis NJD:SUPPRESSED
- Nashville wins YES @ 45c · p 0.5364 (adj 0.4907) · $2.64 · thesis NSH:WINS
- Dallas wins by over 2.5 goals NO @ 79c · p 0.8484 (adj 0.8167) · $4.08 · thesis NSH:WINS
- Roope Hintz: 1+ assists NO @ 66c · p 0.7624 (adj 0.6861) · $2.05 · thesis DAL:SUPPRESSED
- Elias Lindholm: 1+ goals YES @ 17c · p 0.2274 (adj 0.2081) · $2.76 · thesis BOS:OFFENSE_4PLUS
- Olli Maatta: 1+ goals YES @ 5c · p 0.0809 (adj 0.0694) · $1.22 · thesis MIN:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 12c · p 0.1522 (adj 0.1404) · $1.17 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 24c · p 0.2792 (adj 0.2656) · $1.5 · thesis MIN:OFFENSE_4PLUS
- Colorado wins NO @ 28c · p 0.3687 (adj 0.3219) · $2.44 · thesis STL:WINS
- Nathan MacKinnon: 3+ assists NO @ 91c · p 0.9698 (adj 0.9324) · $6.98 · thesis COL:SUPPRESSED
- Pius Suter: 1+ goals YES @ 11c · p 0.1453 (adj 0.1327) · $1.26 · thesis STL:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 55c · p 0.6055 (adj 0.5866) · $2.93 · thesis COL:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 18c · p 0.2199 (adj 0.2062) · $1.63 · thesis VAN:OFFENSE_4PLUS
- Zeev Buium: 1+ goals NO @ 89c · p 0.9226 (adj 0.9069) · $6.98 · thesis VAN:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 59c · p 0.8257 (adj 0.653) · $6.98 · thesis LAK:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 14c · p 0.1991 (adj 0.1743) · $2.37 · thesis SJS:OFFENSE_4PLUS
- Mason Marchment: 1+ assists NO @ 68c · p 0.8121 (adj 0.7132) · $6.9 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BUF** · priced 108/108 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 24.71, exp saves 21.79 (sd 6.0), pull risk 0.048
- CHI net: Spencer Knight (PROJECTED) exp shots 30.42, exp saves 25.66 (sd 7.17), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.253 | 0.365 | 37/64 | +0.091 | STANDARD |
| Patrick Kane: 1+ points | 0.431 | 0.530 | 55/49 | +0.062 | STANDARD |
| Tage Thompson: 2+ points | 0.222 | 0.305 | 33/72 | +0.044 | STANDARD |
| Patrick Kane: 2+ points | 0.109 | 0.185 | 21/84 | +0.041 | STANDARD |
| Tage Thompson: 1+ points | 0.586 | 0.660 | 68/36 | +0.038 | STANDARD |
| Tage Thompson: 1+ assists | 0.352 | 0.425 | 44/59 | +0.041 | STANDARD |

**OTT @ TOR** · priced 123/131 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 31.35, exp saves 27.08 (sd 7.18), pull risk 0.062
- OTT net: Linus Ullmark (PROJECTED) exp shots 24.74, exp saves 21.66 (sd 5.97), pull risk 0.052

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darren Raddysh: 1+ assists | 0.290 | 0.430 | 45/59 | +0.103 | STANDARD |
| Darren Raddysh: 1+ points | 0.383 | 0.520 | 53/49 | +0.110 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.273 | 0.385 | 40/63 | +0.081 | STANDARD |
| Claude Giroux: 1+ assists | 0.371 | 0.260 | 28/76 | +0.076 | STANDARD |
| Claude Giroux: 1+ points | 0.495 | 0.390 | 41/63 | +0.069 | STANDARD |
| Kirill Marchenko: 1+ points | 0.460 | 0.560 | 58/46 | +0.063 | STANDARD |

**WSH @ TBL** · priced 127/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.03, exp saves 21.9 (sd 6.13), pull risk 0.05
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.7, exp saves 24.51 (sd 6.84), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.260 | 0.520 | 54/50 | +0.223 | STANDARD |
| John Carlson: 1+ points | 0.352 | 0.595 | 62/43 | +0.201 | STANDARD |
| John Carlson: 2+ points | 0.073 | 0.235 | 27/80 | +0.115 | STANDARD |
| John Carlson: 2+ assists | 0.035 | 0.170 | 19/85 | +0.107 | STANDARD |
| Anthony Cirelli: 1+ points | 0.502 | 0.420 | 44/60 | +0.044 | STANDARD |
| Alex Tuch: 1+ goals | 0.246 | 0.165 | 26/93 | -0.027 | STANDARD |

**CAR @ PHI** · priced 137/137 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.35 (sd 6.7), pull risk 0.048
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.27, exp saves 20.0 (sd 5.76), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ points | 0.467 | 0.565 | 59/46 | +0.055 | STANDARD |
| Sebastian Aho: 1+ assists | 0.295 | 0.390 | 41/63 | +0.059 | STANDARD |
| Sean Couturier: 1+ goals | 0.180 | 0.090 | 10/92 | +0.074 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.294 | 0.360 | 38/66 | +0.030 | STANDARD |
| Christian Dvorak: 1+ points | 0.464 | 0.400 | 42/62 | +0.027 | STANDARD |
| Sebastian Aho: 2+ points | 0.131 | 0.195 | 22/83 | +0.029 | STANDARD |

**MTL @ PIT** · priced 112/116 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- PIT net: Arturs Silovs (PROJECTED) exp shots 24.51, exp saves 21.3 (sd 6.12), pull risk 0.06
- MTL net: Jakub Dobes (PROJECTED) exp shots 29.53, exp saves 25.22 (sd 6.93), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 1+ points | 0.648 | 0.525 | 55/50 | +0.080 | STANDARD |
| Rickard Rakell: 1+ goals | 0.388 | 0.270 | 29/75 | +0.083 | STANDARD |
| Nick Suzuki: 1+ assists | 0.457 | 0.555 | 58/47 | +0.056 | STANDARD |
| Rickard Rakell: 2+ points | 0.287 | 0.190 | 21/83 | +0.065 | STANDARD |
| Filip Hallander: 1+ goals | 0.218 | 0.125 | 14/89 | +0.070 | STANDARD |
| Nick Suzuki: 2+ points | 0.238 | 0.330 | 36/70 | +0.047 | STANDARD |

**UTA @ CBJ** · priced 122/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.84, exp saves 23.33 (sd 6.36), pull risk 0.055
- UTA net: Karel Vejmelka (PROJECTED) exp shots 28.0, exp saves 23.96 (sd 6.66), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.138 | 0.345 | 36/67 | +0.176 | STANDARD |
| Vincent Trocheck: 1+ points | 0.315 | 0.475 | 48/53 | +0.137 | STANDARD |
| Charlie Coyle: 1+ points | 0.557 | 0.450 | 47/57 | +0.069 | STANDARD |
| Matthew Knies: 1+ assists | 0.245 | 0.350 | 37/67 | +0.069 | STANDARD |
| Vincent Trocheck: 2+ points | 0.056 | 0.140 | 15/87 | +0.066 | STANDARD |
| Matthew Knies: 1+ points | 0.460 | 0.540 | 56/48 | +0.043 | STANDARD |

**SEA @ EDM** · priced 129/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 25.57, exp saves 22.39 (sd 6.13), pull risk 0.054
- SEA net: Joey Daccord (PROJECTED) exp shots 30.84, exp saves 26.05 (sd 7.23), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mattias Ekholm: 1+ points | 0.468 | 0.315 | 34/71 | +0.113 | STANDARD |
| Leon Draisaitl: 2+ points | 0.338 | 0.480 | 50/54 | +0.104 | STANDARD |
| Connor McDavid: 2+ assists | 0.183 | 0.320 | 33/69 | +0.112 | STANDARD |
| Connor McDavid: 1+ assists | 0.538 | 0.675 | 69/34 | +0.106 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.460 | 0.595 | 61/42 | +0.103 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.388 | 0.260 | 28/76 | +0.094 | STANDARD |

**NJD @ NYI** · priced 120/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.14, exp saves 24.54 (sd 6.48), pull risk 0.046
- NJD net: Jake Allen (PROJECTED) exp shots 27.75, exp saves 24.0 (sd 6.61), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.153 | 0.345 | 37/68 | +0.151 | STANDARD |
| Luke Evangelista: 1+ points | 0.296 | 0.475 | 50/55 | +0.137 | STANDARD |
| Anthony Mantha: 1+ assists | 0.157 | 0.295 | 32/73 | +0.100 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.184 | 0.315 | 34/71 | +0.092 | STANDARD |
| Anthony Mantha: 1+ points | 0.332 | 0.455 | 48/57 | +0.081 | STANDARD |
| Jack Hughes: 1+ assists | 0.370 | 0.490 | 51/53 | +0.082 | STANDARD |

**DAL @ NSH** · priced 113/113 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.51, exp saves 23.94 (sd 6.5), pull risk 0.052
- DAL net: Casey DeSmith (PROJECTED) exp shots 26.36, exp saves 22.74 (sd 6.39), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 1+ assists | 0.364 | 0.500 | 52/52 | +0.099 | STANDARD |
| Roope Hintz: 1+ assists | 0.238 | 0.355 | 37/66 | +0.087 | STANDARD |
| Mikko Rantanen: 1+ points | 0.522 | 0.635 | 64/37 | +0.092 | STANDARD |
| Miro Heiskanen: 1+ points | 0.470 | 0.570 | 59/45 | +0.063 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.412 | 0.505 | 53/52 | +0.050 | STANDARD |
| Mikko Rantanen: 2+ points | 0.176 | 0.265 | 28/75 | +0.061 | STANDARD |

**BOS @ MIN** · priced 117/119 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.46, exp saves 24.11 (sd 6.49), pull risk 0.054
- BOS net: Michael DiPietro (PROJECTED) exp shots 30.36, exp saves 25.68 (sd 7.13), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Max Shabanov: 1+ assists | 0.206 | 0.335 | 39/72 | +0.060 | STANDARD |
| Elias Lindholm: 1+ points | 0.473 | 0.350 | 37/67 | +0.086 | STANDARD |
| Max Shabanov: 1+ points | 0.360 | 0.470 | 54/60 | +0.023 | STANDARD |
| JJ Peterka: 1+ assists | 0.170 | 0.275 | 30/75 | +0.067 | STANDARD |
| JJ Peterka: 1+ points | 0.348 | 0.440 | 46/58 | +0.055 | STANDARD |
| Elias Lindholm: 1+ assists | 0.321 | 0.230 | 25/79 | +0.058 | STANDARD |

**STL @ COL** · priced 119/119 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Scott Wedgewood (PROJECTED) exp shots 24.45, exp saves 21.44 (sd 5.87), pull risk 0.049
- STL net: Jordan Binnington (PROBABLE) exp shots 31.38, exp saves 26.42 (sd 7.26), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.433 | 0.610 | 63/41 | +0.140 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.344 | 0.520 | 54/50 | +0.138 | STANDARD |
| Cale Makar: 2+ points | 0.184 | 0.335 | 34/67 | +0.131 | STANDARD |
| Cale Makar: 1+ points | 0.536 | 0.405 | 70/89 | -0.178 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.505 | 0.635 | 65/38 | +0.098 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.155 | 0.285 | 30/73 | +0.101 | STANDARD |

**CGY @ VAN** · priced 106/108 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 28.38, exp saves 24.72 (sd 6.61), pull risk 0.056
- CGY net: Devin Cooley (PROJECTED) exp shots 28.2, exp saves 24.24 (sd 6.68), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Linus Karlsson: 1+ goals | 0.254 | 0.140 | 23/95 | +0.011 | STANDARD |
| Brock Boeser: 1+ goals | 0.282 | 0.195 | 32/93 | -0.053 | STANDARD |
| Joel Farabee: 1+ assists | 0.344 | 0.275 | 30/75 | +0.029 | STANDARD |
| Brendan Gallagher: 1+ goals | 0.162 | 0.095 | 15/96 | +0.003 | STANDARD |
| Morgan Frost: 1+ goals | 0.255 | 0.190 | 28/90 | -0.039 | STANDARD |
| Marco Rossi: 1+ goals | 0.270 | 0.205 | 27/86 | -0.014 | STANDARD |

**LAK @ SJS** · priced 107/110 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.98, exp saves 24.34 (sd 6.56), pull risk 0.055
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.75, exp saves 23.27 (sd 6.38), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.174 | 0.440 | 47/59 | +0.219 | STANDARD |
| Macklin Celebrini: 1+ points | 0.671 | 0.435 | 72/85 | -0.063 | STANDARD |
| Mason Marchment: 1+ assists | 0.188 | 0.340 | 36/68 | +0.117 | STANDARD |
| Artemi Panarin: 1+ assists | 0.359 | 0.510 | 54/52 | +0.103 | STANDARD |
| Luca Cagnoni: 1+ points | 0.310 | 0.425 | 45/60 | +0.073 | PRIOR_HEAVY |
| Kiefer Sherwood: 1+ goals | 0.199 | 0.100 | 14/94 | +0.051 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
