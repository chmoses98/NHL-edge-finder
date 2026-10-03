# NHL slate 2026-10-03 — RESEARCH_ONLY

generated 2026-10-03T16:23:59Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 13 · simulated (not started): 13 · markets on board: 4116 · contracts joined: 2225 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 1900, 'NO_EDGE': 160, 'OK': 165}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'player_assists': 297, 'game_early_goal': 13, 'first_goal': 454, 'game_winner': 26, 'player_goals': 453, 'game_overtime': 13, 'player_points': 357, 'goalie_saves': 1, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 2026-10-03T23:00:00Z | T-6h | 0.658 | 0.342 | 0.164 | 6.08 | 3.54 | 2.54 | 160 (25/135) | PROBABLE/PROBABLE |
| OTT @ TOR | 2026-10-03T23:00:00Z | T-6h | 0.462 | 0.538 | 0.170 | 6.70 | 3.22 | 3.48 | 182 (25/157) | PROBABLE/PROBABLE |
| WSH @ TBL | 2026-10-03T23:00:00Z | T-6h | 0.631 | 0.369 | 0.176 | 6.19 | 3.50 | 2.68 | 180 (25/155) | PROBABLE/CONFIRMED |
| CAR @ PHI | 2026-10-03T23:00:00Z | T-6h | 0.473 | 0.527 | 0.182 | 5.84 | 2.83 | 3.00 | 188 (25/163) | CONFIRMED/PROJECTED |
| MTL @ PIT | 2026-10-03T23:00:00Z | T-6h | 0.545 | 0.455 | 0.168 | 6.53 | 3.40 | 3.13 | 167 (25/142) | CONFIRMED/CONFIRMED |
| UTA @ CBJ | 2026-10-03T23:00:00Z | T-6h | 0.540 | 0.460 | 0.182 | 6.10 | 3.16 | 2.94 | 173 (25/148) | PROJECTED/PROJECTED |
| SEA @ EDM | 2026-10-03T23:00:00Z | T-6h | 0.616 | 0.384 | 0.169 | 6.65 | 3.72 | 2.94 | 180 (25/155) | PROJECTED/PROJECTED |
| NJD @ NYI | 2026-10-03T23:30:00Z | T-6h | 0.537 | 0.463 | 0.190 | 5.65 | 2.94 | 2.70 | 171 (25/146) | CONFIRMED/CONFIRMED |
| DAL @ NSH | 2026-10-04T00:00:00Z | T-6h | 0.505 | 0.495 | 0.182 | 6.00 | 3.01 | 2.98 | 164 (25/139) | PROJECTED/PROJECTED |
| BOS @ MIN | 2026-10-04T00:00:00Z | T-6h | 0.638 | 0.362 | 0.165 | 6.31 | 3.59 | 2.72 | 170 (25/145) | CONFIRMED/PROJECTED |
| STL @ COL | 2026-10-04T01:00:00Z | T-6h | 0.694 | 0.306 | 0.148 | 6.55 | 3.93 | 2.62 | 170 (25/145) | PROJECTED/PROBABLE |
| CGY @ VAN | 2026-10-04T02:00:00Z | T-6h | 0.493 | 0.507 | 0.174 | 6.33 | 3.15 | 3.19 | 159 (25/134) | PROJECTED/PROJECTED |
| LAK @ SJS | 2026-10-04T02:00:00Z | T-6h | 0.550 | 0.450 | 0.176 | 6.32 | 3.31 | 3.02 | 161 (25/136) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4 | team_total | 0.295 | 0.420 | 0.393 | 43 | 59 | no | +0.098 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ3 | team_total | 0.514 | 0.630 | 0.607 | 64 | 38 | no | +0.090 | OK |
| KXNHLGAME-26OCT03NJNYI-NJ | game_winner | 0.463 | 0.565 | 0.545 | 57 | 44 | no | +0.079 | OK |
| KXNHLGAME-26OCT03NJNYI-NYI | game_winner | 0.537 | 0.435 | 0.455 | 44 | 57 | yes | +0.079 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ2 | game_spread | 0.233 | 0.325 | 0.305 | 33 | 68 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ3 | game_spread | 0.130 | 0.215 | 0.195 | 22 | 79 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5 | team_total | 0.140 | 0.225 | 0.205 | 23 | 78 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT03NJNYI-6 | game_total | 0.465 | 0.555 | 0.537 | 56 | 45 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT4 | team_total | 0.473 | 0.385 | 0.402 | 39 | 62 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ2 | team_total | 0.746 | 0.835 | 0.820 | 85 | 18 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT03NJNYI-5 | game_total | 0.697 | 0.775 | 0.761 | 78 | 23 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT5 | team_total | 0.277 | 0.205 | 0.218 | 21 | 80 | yes | +0.056 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT2 | game_spread | 0.329 | 0.255 | 0.269 | 26 | 75 | yes | +0.056 | OK |
| KXNHLTOTAL-26OCT03NJNYI-7 | game_total | 0.359 | 0.435 | 0.419 | 44 | 57 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-6 | game_total | 0.639 | 0.565 | 0.580 | 57 | 44 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-7 | game_total | 0.529 | 0.450 | 0.466 | 46 | 56 | yes | +0.051 | OK |
| KXNHLGAME-26OCT03DALNSH-DAL | game_winner | 0.495 | 0.565 | 0.551 | 57 | 44 | no | +0.047 | OK |
| KXNHLGAME-26OCT03DALNSH-NSH | game_winner | 0.505 | 0.435 | 0.449 | 44 | 57 | yes | +0.047 | OK |
| KXNHLGAME-26OCT03MTLPIT-PIT | game_winner | 0.545 | 0.475 | 0.489 | 48 | 53 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-8 | game_total | 0.331 | 0.260 | 0.273 | 27 | 75 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT03NJNYI-4 | game_total | 0.797 | 0.855 | 0.845 | 86 | 15 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-9 | game_total | 0.245 | 0.180 | 0.192 | 19 | 83 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT3 | team_total | 0.680 | 0.610 | 0.625 | 62 | 40 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL4 | team_total | 0.359 | 0.430 | 0.416 | 44 | 58 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT03NJNYI-8 | game_total | 0.185 | 0.245 | 0.232 | 25 | 76 | no | +0.042 | OK |
| KXNHLGAME-26OCT03UTACBJ-CBJ | game_winner | 0.540 | 0.475 | 0.488 | 48 | 53 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NYI2 | game_spread | 0.305 | 0.245 | 0.256 | 25 | 76 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL2 | game_spread | 0.254 | 0.315 | 0.302 | 32 | 69 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL3 | game_spread | 0.158 | 0.215 | 0.202 | 22 | 79 | no | +0.041 | OK |
| KXNHLGAME-26OCT03MTLPIT-MTL | game_winner | 0.455 | 0.515 | 0.503 | 52 | 49 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT3 | game_spread | 0.206 | 0.155 | 0.164 | 16 | 85 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL3 | game_spread | 0.152 | 0.205 | 0.194 | 21 | 80 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-OTT2 | game_spread | 0.328 | 0.275 | 0.285 | 28 | 73 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL3 | team_total | 0.581 | 0.640 | 0.628 | 65 | 37 | no | +0.033 | OK |
| KXNHLGAME-26OCT03UTACBJ-UTA | game_winner | 0.460 | 0.515 | 0.504 | 52 | 49 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL2 | game_spread | 0.273 | 0.325 | 0.314 | 33 | 68 | no | +0.032 | OK |
| KXNHLGAME-26OCT03OTTTOR-OTT | game_winner | 0.538 | 0.485 | 0.496 | 49 | 52 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-10 | game_total | 0.126 | 0.080 | 0.088 | 9 | 93 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ6 | team_total | 0.055 | 0.100 | 0.089 | 11 | 91 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-6 | game_total | 0.544 | 0.595 | 0.585 | 60 | 41 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4 | team_total | 0.456 | 0.405 | 0.415 | 41 | 60 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF3 | team_total | 0.698 | 0.745 | 0.736 | 75 | 26 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-TOR3 | game_spread | 0.152 | 0.195 | 0.186 | 20 | 81 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-7 | game_total | 0.426 | 0.475 | 0.465 | 48 | 53 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT03NJNYI-9 | game_total | 0.125 | 0.165 | 0.156 | 17 | 84 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF4 | team_total | 0.488 | 0.535 | 0.526 | 54 | 47 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT03DALNSH-5 | game_total | 0.744 | 0.785 | 0.777 | 79 | 22 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT6 | team_total | 0.141 | 0.090 | 0.099 | 11 | 93 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-5 | game_total | 0.825 | 0.785 | 0.794 | 79 | 22 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT03UTACBJ-UTA4 | team_total | 0.350 | 0.400 | 0.390 | 41 | 61 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT2 | team_total | 0.853 | 0.815 | 0.823 | 82 | 19 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT03CARPHI-6 | game_total | 0.500 | 0.545 | 0.536 | 55 | 46 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL5 | team_total | 0.186 | 0.235 | 0.224 | 25 | 78 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL2 | team_total | 0.808 | 0.845 | 0.838 | 85 | 16 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT03SEAEDM-SEA2 | game_spread | 0.201 | 0.165 | 0.172 | 17 | 84 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-5 | game_total | 0.757 | 0.795 | 0.788 | 80 | 21 | no | +0.021 | OK |
| KXNHLGAME-26OCT03OTTTOR-TOR | game_winner | 0.462 | 0.505 | 0.496 | 51 | 50 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT03UTACBJ-UTA3 | game_spread | 0.149 | 0.185 | 0.177 | 19 | 82 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT03CARPHI-5 | game_total | 0.727 | 0.765 | 0.758 | 77 | 24 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF5 | team_total | 0.284 | 0.335 | 0.325 | 35 | 68 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT3 | team_total | 0.667 | 0.620 | 0.630 | 63 | 39 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-OTT3 | game_spread | 0.211 | 0.175 | 0.182 | 18 | 83 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT03CARPHI-CAR3 | game_spread | 0.178 | 0.215 | 0.207 | 22 | 79 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT5 | team_total | 0.262 | 0.220 | 0.228 | 23 | 79 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-4 | game_total | 0.843 | 0.880 | 0.873 | 89 | 13 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT03CHIBUF-BUF3 | game_spread | 0.286 | 0.325 | 0.317 | 33 | 68 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT03UTACBJ-UTA3 | team_total | 0.565 | 0.610 | 0.601 | 62 | 40 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT03UTACBJ-CBJ2 | game_spread | 0.312 | 0.275 | 0.282 | 28 | 73 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT03STLCOL-8 | game_total | 0.312 | 0.275 | 0.282 | 28 | 73 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT03DALNSH-NSH2 | game_spread | 0.281 | 0.245 | 0.252 | 25 | 76 | yes | +0.018 | OK |
| KXNHLGAME-26OCT03SEAEDM-SEA | game_winner | 0.384 | 0.345 | 0.353 | 35 | 66 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL2 | team_total | 0.792 | 0.835 | 0.827 | 85 | 18 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-8 | game_total | 0.248 | 0.285 | 0.277 | 29 | 72 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-TOR2 | game_spread | 0.259 | 0.295 | 0.288 | 30 | 71 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-4 | game_total | 0.894 | 0.865 | 0.871 | 87 | 14 | yes | +0.016 | OK |
| KXNHLSPREAD-26OCT03LASJ-LA3 | game_spread | 0.145 | 0.175 | 0.169 | 18 | 83 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT03CARPHI-7 | game_total | 0.388 | 0.425 | 0.417 | 43 | 58 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL4 | team_total | 0.278 | 0.245 | 0.251 | 25 | 76 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT2 | team_total | 0.845 | 0.815 | 0.821 | 82 | 19 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT03MTLPIT-8 | game_total | 0.308 | 0.275 | 0.281 | 28 | 73 | yes | +0.014 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 0.658 | 0.638 | 0.164 | 0.206 | 6.08 | 6.34 | 1.000/0.995 | KXNHLTEAMTOTAL-26OCT03CHIBUF-CHI3 +0.053 |
| OTT @ TOR | 0.462 | 0.451 | 0.170 | 0.217 | 6.70 | 6.11 | 0.983/0.982 | KXNHLTOTAL-26OCT03OTTTOR-6 -0.099 |
| WSH @ TBL | 0.631 | 0.606 | 0.176 | 0.209 | 6.19 | 6.25 | 0.951/1.015 | KXNHLTEAMTOTAL-26OCT03WSHTB-WSH3 +0.032 |
| CAR @ PHI | 0.473 | 0.538 | 0.182 | 0.226 | 5.84 | 5.93 | 0.990/0.997 | KXNHLGAME-26OCT03CARPHI-PHI +0.065 |
| MTL @ PIT | 0.545 | 0.559 | 0.168 | 0.213 | 6.53 | 6.60 | 1.042/0.942 | KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4 +0.022 |
| UTA @ CBJ | 0.540 | 0.544 | 0.182 | 0.219 | 6.10 | 6.32 | 0.964/0.992 | KXNHLTOTAL-26OCT03UTACBJ-7 +0.040 |
| SEA @ EDM | 0.616 | 0.620 | 0.169 | 0.202 | 6.65 | 6.55 | 1.009/1.005 | KXNHLTOTAL-26OCT03SEAEDM-8 -0.020 |
| NJD @ NYI | 0.537 | 0.535 | 0.190 | 0.223 | 5.65 | 5.87 | 0.947/0.995 | KXNHLTOTAL-26OCT03NJNYI-5 +0.040 |
| DAL @ NSH | 0.505 | 0.530 | 0.182 | 0.228 | 6.00 | 6.09 | 1.000/0.976 | KXNHLTEAMTOTAL-26OCT03DALNSH-NSH3 +0.027 |
| BOS @ MIN | 0.638 | 0.624 | 0.165 | 0.208 | 6.31 | 6.40 | 0.991/0.986 | KXNHLTEAMTOTAL-26OCT03BOSMIN-BOS4 +0.021 |
| STL @ COL | 0.694 | 0.634 | 0.148 | 0.205 | 6.55 | 6.42 | 0.973/1.024 | KXNHLSPREAD-26OCT03STLCOL-COL2 -0.070 |
| CGY @ VAN | 0.493 | 0.561 | 0.174 | 0.217 | 6.33 | 6.34 | 1.025/0.986 | KXNHLGAME-26OCT03CGYVAN-VAN +0.068 |
| LAK @ SJS | 0.550 | 0.521 | 0.176 | 0.222 | 6.32 | 6.12 | 1.034/0.992 | KXNHLTEAMTOTAL-26OCT03LASJ-SJ4 -0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 47 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Greene: 1+ goals YES @ 12c · p 0.1675 (adj 0.1544) · $1.99 · thesis CHI:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 59c · p 0.6492 (adj 0.6306) · $4.28 · thesis BUF:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 64c · p 0.7517 (adj 0.6758) · $4.77 · thesis CHI:SUPPRESSED
- Tage Thompson: 1+ assists NO @ 57c · p 0.6458 (adj 0.6054) · $3.09 · thesis BUF:SUPPRESSED
- Stephen Halliday: 1+ goals YES @ 9c · p 0.1341 (adj 0.1218) · $1.89 · thesis OTT:OFFENSE_4PLUS
- Easton Cowan: 1+ goals NO @ 80c · p 0.8384 (adj 0.8263) · $5.65 · thesis TOR:SUPPRESSED
- William Eklund: 1+ assists NO @ 66c · p 0.7355 (adj 0.6927) · $4.68 · thesis OTT:SUPPRESSED
- Easton Cowan: 1+ assists YES @ 26c · p 0.3289 (adj 0.2894) · $1.4 · thesis TOR:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 48c · p 0.7462 (adj 0.5634) · $5.65 · thesis TBL:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2112 (adj 0.1996) · $1.58 · thesis WSH:OFFENSE_4PLUS
- Boone Jenner: 1+ goals YES @ 11c · p 0.1439 (adj 0.1329) · $1.19 · thesis WSH:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 10c · p 0.1761 (adj 0.1546) · $3.23 · thesis PHI:OFFENSE_4PLUS
- Noel Acciari: 1+ goals YES @ 9c · p 0.1354 (adj 0.1215) · $1.79 · thesis PHI:OFFENSE_4PLUS
- Mark Jankowski: 1+ goals NO @ 84c · p 0.8839 (adj 0.8717) · $5.65 · thesis CAR:SUPPRESSED
- Christian Dvorak: 1+ goals YES @ 18c · p 0.2186 (adj 0.2064) · $1.25 · thesis PHI:OFFENSE_4PLUS
- Filip Hallander: 1+ goals YES @ 13c · p 0.2022 (adj 0.1816) · $3.13 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.2013 (adj 0.181) · $3.08 · thesis PIT:WINS_BY_2PLUS
- Rickard Rakell: 1+ goals YES @ 31c · p 0.3739 (adj 0.3529) · $2.67 · thesis PIT:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 67c · p 0.8619 (adj 0.7274) · $5.33 · thesis UTA:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 21c · p 0.2706 (adj 0.253) · $2.45 · thesis CBJ:OFFENSE_4PLUS
- Conor Garland: 1+ goals NO @ 82c · p 0.8634 (adj 0.8513) · $5.33 · thesis CBJ:SUPPRESSED
- Danton Heinen: 1+ goals YES @ 10c · p 0.1317 (adj 0.1213) · $1.01 · thesis CBJ:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 17c · p 0.2444 (adj 0.2221) · $3.61 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 68c · p 0.8167 (adj 0.7246) · $5.65 · thesis EDM:SUPPRESSED
- Mattias Ekholm: 1+ goals YES @ 10c · p 0.133 (adj 0.1235) · $1.52 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 33c · p 0.4616 (adj 0.3696) · $2.23 · thesis EDM:SUPPRESSED
- Luke Evangelista: 1+ assists NO @ 67c · p 0.8394 (adj 0.7163) · $5.65 · thesis NJD:SUPPRESSED
- New Jersey wins NO @ 44c · p 0.5332 (adj 0.489) · $3.52 · thesis NYI:WINS
- Dougie Hamilton: 2+ assists YES @ 5c · p 0.0721 (adj 0.066) · $1.05 · thesis NJD:OFFENSE_4PLUS
- New Jersey over 3.5 goals scored NO @ 59c · p 0.6783 (adj 0.6292) · $2.11 · thesis NJD:SUPPRESSED
- Mavrik Bourque: 1+ goals YES @ 17c · p 0.2115 (adj 0.1999) · $1.51 · thesis NSH:OFFENSE_4PLUS
- Dallas wins by over 1.5 goals NO @ 68c · p 0.7527 (adj 0.7139) · $1.92 · thesis NSH:WINS
- Mikko Rantanen: 1+ goals NO @ 70c · p 0.7488 (adj 0.7329) · $4.2 · thesis DAL:SUPPRESSED
- Dallas wins by over 2.5 goals NO @ 79c · p 0.8484 (adj 0.8167) · $2.58 · thesis NSH:WINS
- Olli Maatta: 1+ goals YES @ 5c · p 0.0768 (adj 0.0701) · $1.12 · thesis MIN:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 12c · p 0.1544 (adj 0.1421) · $1.09 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 24c · p 0.2786 (adj 0.2652) · $1.11 · thesis MIN:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 53c · p 0.6055 (adj 0.5841) · $5.41 · thesis COL:SUPPRESSED
- Pius Suter: 1+ goals YES @ 11c · p 0.1453 (adj 0.134) · $1.21 · thesis STL:OFFENSE_4PLUS
- Colorado wins by over 2.5 goals NO @ 64c · p 0.7171 (adj 0.6761) · $1.98 · thesis GAME:TIGHT
- Dylan Holloway: 1+ goals YES @ 25c · p 0.2928 (adj 0.2796) · $1.34 · thesis STL:OFFENSE_4PLUS
- Zayne Parekh: 1+ goals NO @ 85c · p 0.903 (adj 0.886) · $5.65 · thesis CGY:SUPPRESSED
- Zeev Buium: 1+ goals NO @ 88c · p 0.9226 (adj 0.9082) · $5.65 · thesis VAN:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 17c · p 0.2199 (adj 0.2037) · $1.93 · thesis VAN:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 13c · p 0.1991 (adj 0.1793) · $3.0 · thesis SJS:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 58c · p 0.8257 (adj 0.653) · $5.57 · thesis LAK:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 67c · p 0.8121 (adj 0.7132) · $5.57 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BUF** · priced 109/109 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 24.71, exp saves 21.76 (sd 6.09), pull risk 0.05
- CHI net: Spencer Knight (PROBABLE) exp shots 30.42, exp saves 25.66 (sd 7.16), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ points | 0.428 | 0.545 | 56/47 | +0.085 | STANDARD |
| Patrick Kane: 1+ assists | 0.248 | 0.365 | 37/64 | +0.096 | STANDARD |
| Tage Thompson: 2+ points | 0.218 | 0.325 | 33/68 | +0.087 | STANDARD |
| Tage Thompson: 1+ points | 0.582 | 0.665 | 68/35 | +0.052 | STANDARD |
| Tage Thompson: 1+ assists | 0.354 | 0.435 | 44/57 | +0.059 | STANDARD |
| Patrick Kane: 2+ points | 0.110 | 0.185 | 20/83 | +0.051 | STANDARD |

**OTT @ TOR** · priced 129/131 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 31.35, exp saves 27.01 (sd 7.12), pull risk 0.066
- OTT net: Linus Ullmark (PROBABLE) exp shots 24.74, exp saves 21.69 (sd 5.97), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darren Raddysh: 1+ points | 0.383 | 0.530 | 54/48 | +0.119 | STANDARD |
| Darren Raddysh: 1+ assists | 0.290 | 0.430 | 45/59 | +0.103 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.272 | 0.390 | 40/62 | +0.091 | STANDARD |
| Auston Matthews: 1+ points | 0.516 | 0.630 | 65/39 | +0.077 | STANDARD |
| Auston Matthews: 1+ assists | 0.304 | 0.415 | 43/60 | +0.079 | STANDARD |
| Kirill Marchenko: 1+ points | 0.461 | 0.565 | 59/46 | +0.062 | STANDARD |

**WSH @ TBL** · priced 127/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 25.03, exp saves 21.89 (sd 6.08), pull risk 0.05
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.7, exp saves 24.45 (sd 6.85), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.254 | 0.535 | 55/48 | +0.249 | STANDARD |
| John Carlson: 1+ points | 0.343 | 0.595 | 61/42 | +0.220 | STANDARD |
| John Carlson: 2+ points | 0.069 | 0.245 | 27/78 | +0.139 | STANDARD |
| John Carlson: 2+ assists | 0.035 | 0.180 | 19/83 | +0.126 | STANDARD |
| Anthony Cirelli: 1+ points | 0.494 | 0.420 | 44/60 | +0.037 | STANDARD |
| Nikita Kucherov: 2+ points | 0.357 | 0.425 | 44/59 | +0.036 | STANDARD |

**CAR @ PHI** · priced 135/137 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (CONFIRMED) exp shots 29.07, exp saves 25.27 (sd 6.78), pull risk 0.052
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.27, exp saves 20.0 (sd 5.71), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ points | 0.465 | 0.565 | 58/45 | +0.067 | STANDARD |
| Sebastian Aho: 1+ assists | 0.297 | 0.395 | 41/62 | +0.066 | STANDARD |
| Sean Couturier: 1+ goals | 0.176 | 0.090 | 10/92 | +0.070 | STANDARD |
| Sebastian Aho: 2+ points | 0.126 | 0.205 | 22/81 | +0.053 | STANDARD |
| Porter Martone: 1+ points | 0.391 | 0.465 | 48/55 | +0.042 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.363 | 0.430 | 45/59 | +0.030 | STANDARD |

**MTL @ PIT** · priced 114/116 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- PIT net: Arturs Silovs (CONFIRMED) exp shots 24.51, exp saves 21.32 (sd 6.07), pull risk 0.061
- MTL net: Jakub Dobes (CONFIRMED) exp shots 29.53, exp saves 25.27 (sd 7.0), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 2+ points | 0.275 | 0.165 | 21/88 | +0.053 | STANDARD |
| Rickard Rakell: 1+ points | 0.640 | 0.535 | 55/48 | +0.073 | STANDARD |
| Nick Suzuki: 1+ assists | 0.458 | 0.545 | 56/47 | +0.055 | STANDARD |
| Nick Suzuki: 2+ points | 0.243 | 0.330 | 35/69 | +0.052 | STANDARD |
| Rickard Rakell: 1+ goals | 0.374 | 0.290 | 31/73 | +0.049 | STANDARD |
| Filip Hallander: 1+ goals | 0.202 | 0.120 | 13/89 | +0.064 | STANDARD |

**UTA @ CBJ** · priced 122/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.84, exp saves 23.33 (sd 6.36), pull risk 0.055
- UTA net: Karel Vejmelka (PROJECTED) exp shots 28.0, exp saves 23.96 (sd 6.66), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.138 | 0.345 | 36/67 | +0.176 | STANDARD |
| Vincent Trocheck: 1+ points | 0.315 | 0.465 | 48/55 | +0.118 | STANDARD |
| Matthew Knies: 1+ assists | 0.245 | 0.360 | 38/66 | +0.079 | STANDARD |
| Charlie Coyle: 1+ points | 0.557 | 0.460 | 48/56 | +0.059 | STANDARD |
| Matthew Knies: 1+ points | 0.460 | 0.550 | 57/47 | +0.053 | STANDARD |
| Vincent Trocheck: 2+ points | 0.056 | 0.140 | 15/87 | +0.066 | STANDARD |

**SEA @ EDM** · priced 129/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 25.57, exp saves 22.39 (sd 6.13), pull risk 0.054
- SEA net: Joey Daccord (PROJECTED) exp shots 30.84, exp saves 26.05 (sd 7.23), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mattias Ekholm: 1+ points | 0.468 | 0.320 | 33/69 | +0.123 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.460 | 0.605 | 61/40 | +0.123 | STANDARD |
| Connor McDavid: 2+ assists | 0.183 | 0.325 | 33/68 | +0.121 | STANDARD |
| Connor McDavid: 1+ assists | 0.538 | 0.680 | 69/33 | +0.116 | STANDARD |
| Leon Draisaitl: 2+ points | 0.338 | 0.475 | 49/54 | +0.104 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.388 | 0.255 | 27/76 | +0.104 | STANDARD |

**NJD @ NYI** · priced 120/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.14, exp saves 24.54 (sd 6.48), pull risk 0.046
- NJD net: Nico Daws (CONFIRMED) exp shots 27.75, exp saves 24.0 (sd 6.52), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.161 | 0.350 | 37/67 | +0.154 | STANDARD |
| Luke Evangelista: 1+ points | 0.300 | 0.475 | 50/55 | +0.133 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.176 | 0.325 | 35/70 | +0.109 | STANDARD |
| Anthony Mantha: 1+ assists | 0.154 | 0.295 | 31/72 | +0.112 | STANDARD |
| Anthony Mantha: 1+ points | 0.329 | 0.465 | 48/55 | +0.104 | STANDARD |
| Jack Hughes: 1+ assists | 0.377 | 0.495 | 51/52 | +0.086 | STANDARD |

**DAL @ NSH** · priced 113/113 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.51, exp saves 23.94 (sd 6.5), pull risk 0.052
- DAL net: Casey DeSmith (PROJECTED) exp shots 26.36, exp saves 22.74 (sd 6.39), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 1+ assists | 0.364 | 0.500 | 52/52 | +0.099 | STANDARD |
| Roope Hintz: 1+ assists | 0.239 | 0.355 | 37/66 | +0.085 | STANDARD |
| Mikko Rantanen: 1+ points | 0.522 | 0.635 | 64/37 | +0.092 | STANDARD |
| Miro Heiskanen: 1+ points | 0.470 | 0.570 | 59/45 | +0.063 | STANDARD |
| Mikko Rantanen: 2+ points | 0.176 | 0.275 | 28/73 | +0.080 | STANDARD |
| Roope Hintz: 1+ points | 0.433 | 0.525 | 55/50 | +0.049 | STANDARD |

**BOS @ MIN** · priced 117/119 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.46, exp saves 24.14 (sd 6.54), pull risk 0.051
- BOS net: Michael DiPietro (PROJECTED) exp shots 30.36, exp saves 25.64 (sd 7.16), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Max Shabanov: 1+ assists | 0.206 | 0.320 | 35/71 | +0.069 | STANDARD |
| JJ Peterka: 1+ assists | 0.170 | 0.280 | 30/74 | +0.077 | STANDARD |
| JJ Peterka: 1+ points | 0.349 | 0.455 | 47/56 | +0.074 | STANDARD |
| Max Shabanov: 1+ points | 0.359 | 0.460 | 49/57 | +0.054 | STANDARD |
| Elias Lindholm: 1+ points | 0.453 | 0.360 | 38/66 | +0.057 | STANDARD |
| Elias Lindholm: 2+ points | 0.131 | 0.065 | 10/97 | +0.025 | STANDARD |

**STL @ COL** · priced 119/119 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Scott Wedgewood (PROJECTED) exp shots 24.45, exp saves 21.44 (sd 5.87), pull risk 0.049
- STL net: Jordan Binnington (PROBABLE) exp shots 31.38, exp saves 26.42 (sd 7.26), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.344 | 0.530 | 55/49 | +0.148 | STANDARD |
| Cale Makar: 1+ assists | 0.433 | 0.615 | 63/40 | +0.151 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.114 | 0.270 | 28/ | -0.180 | STANDARD |
| Cale Makar: 2+ points | 0.184 | 0.330 | 34/68 | +0.121 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.505 | 0.645 | 65/36 | +0.119 | STANDARD |
| Cale Makar: 1+ points | 0.536 | 0.670 | 70/36 | +0.088 | STANDARD |

**CGY @ VAN** · priced 106/108 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 28.38, exp saves 24.72 (sd 6.61), pull risk 0.056
- CGY net: Devin Cooley (PROJECTED) exp shots 28.2, exp saves 24.24 (sd 6.68), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Linus Karlsson: 1+ goals | 0.254 | 0.140 | 22/94 | +0.021 | STANDARD |
| Brendan Gallagher: 1+ goals | 0.162 | 0.080 | 14/98 | +0.013 | STANDARD |
| Zayne Parekh: 1+ goals | 0.097 | 0.165 | 18/85 | +0.044 | STANDARD |
| Drew O'Connor: 1+ goals | 0.220 | 0.155 | 17/86 | +0.040 | STANDARD |
| Joel Farabee: 1+ assists | 0.344 | 0.285 | 30/73 | +0.029 | STANDARD |
| Zeev Buium: 1+ goals | 0.077 | 0.135 | 15/88 | +0.035 | STANDARD |

**LAK @ SJS** · priced 107/110 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.98, exp saves 24.34 (sd 6.56), pull risk 0.055
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.75, exp saves 23.27 (sd 6.38), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.174 | 0.440 | 46/58 | +0.229 | STANDARD |
| Mason Marchment: 1+ assists | 0.188 | 0.340 | 35/67 | +0.127 | STANDARD |
| Artemi Panarin: 1+ assists | 0.359 | 0.510 | 52/50 | +0.123 | STANDARD |
| Luca Cagnoni: 1+ points | 0.310 | 0.420 | 44/60 | +0.073 | PRIOR_HEAVY |
| Mats Zuccarello: 2+ assists | 0.017 | 0.110 | 13/91 | +0.067 | STANDARD |
| Luca Cagnoni: 1+ assists | 0.259 | 0.350 | 36/66 | +0.065 | PRIOR_HEAVY |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
