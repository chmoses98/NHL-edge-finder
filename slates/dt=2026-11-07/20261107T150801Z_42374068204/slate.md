# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-07T15:08:01Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4303 · contracts joined: 2625 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2325, 'OK': 146, 'NO_EDGE': 154}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 361, 'game_early_goal': 12, 'first_goal': 432, 'game_winner': 24, 'player_goals': 743, 'game_overtime': 12, 'player_points': 477, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ WSH | 2026-11-07T17:30:00Z | T-90m | 0.583 | 0.417 | 0.175 | 6.42 | 3.47 | 2.95 | 233 (25/208) | PROJECTED/PROJECTED |
| STL @ NSH | 2026-11-07T18:00:00Z | T-90m | 0.492 | 0.508 | 0.176 | 6.23 | 3.08 | 3.15 | 209 (25/184) | PROJECTED/PROJECTED |
| NYR @ SEA | 2026-11-07T22:00:00Z | T-6h | 0.503 | 0.496 | 0.177 | 6.35 | 3.19 | 3.16 | 220 (25/195) | PROJECTED/PROJECTED |
| MTL @ TOR | 2026-11-08T00:00:00Z | T-6h | 0.488 | 0.512 | 0.171 | 6.80 | 3.35 | 3.45 | 212 (25/187) | PROJECTED/PROJECTED |
| UTA @ OTT | 2026-11-08T00:00:00Z | T-6h | 0.496 | 0.504 | 0.172 | 6.40 | 3.19 | 3.21 | 221 (25/196) | PROJECTED/PROJECTED |
| NJD @ NYI | 2026-11-08T00:00:00Z | T-6h | 0.498 | 0.502 | 0.183 | 5.81 | 2.89 | 2.92 | 218 (25/193) | PROBABLE/PROJECTED |
| CHI @ CAR | 2026-11-08T01:00:00Z | T-6h | 0.733 | 0.267 | 0.152 | 6.07 | 3.79 | 2.27 | 217 (25/192) | PROJECTED/PROJECTED |
| SJS @ DAL | 2026-11-08T01:00:00Z | T-6h | 0.673 | 0.327 | 0.165 | 5.94 | 3.52 | 2.42 | 211 (25/186) | PROJECTED/PROJECTED |
| TBL @ MIN | 2026-11-08T01:00:00Z | T-6h | 0.441 | 0.559 | 0.173 | 6.36 | 3.01 | 3.35 | 217 (25/192) | CONFIRMED/PROJECTED |
| DET @ COL | 2026-11-08T02:00:00Z | T-6h | 0.626 | 0.374 | 0.170 | 6.25 | 3.53 | 2.72 | 234 (25/209) | PROJECTED/PROJECTED |
| PIT @ LAK | 2026-11-08T02:00:00Z | T-6h | 0.564 | 0.436 | 0.164 | 6.53 | 3.46 | 3.07 | 216 (25/191) | PROJECTED/PROJECTED |
| VAN @ EDM | 2026-11-08T03:00:00Z | T-6h | 0.730 | 0.270 | 0.134 | 7.16 | 4.38 | 2.78 | 217 (25/192) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV07CHICAR-CAR3 | game_spread | 0.358 | 0.480 | 0.455 | 49 | 53 | no | +0.094 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CAR2 | game_spread | 0.508 | 0.615 | 0.594 | 62 | 39 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4 | team_total | 0.481 | 0.575 | 0.556 | 58 | 43 | no | +0.072 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL3 | game_spread | 0.292 | 0.385 | 0.366 | 39 | 62 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ4 | team_total | 0.346 | 0.440 | 0.421 | 45 | 57 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR4 | team_total | 0.539 | 0.635 | 0.616 | 65 | 38 | no | +0.064 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ2 | game_spread | 0.281 | 0.365 | 0.347 | 37 | 64 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR5 | team_total | 0.332 | 0.420 | 0.402 | 43 | 59 | no | +0.061 | OK |
| KXNHLGAME-26NOV07NJNYI-NJ | game_winner | 0.502 | 0.585 | 0.569 | 59 | 42 | no | +0.061 | OK |
| KXNHLGAME-26NOV07NJNYI-NYI | game_winner | 0.498 | 0.415 | 0.431 | 42 | 59 | yes | +0.061 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL2 | game_spread | 0.446 | 0.525 | 0.509 | 53 | 48 | no | +0.056 | OK |
| KXNHLGAME-26NOV07CHICAR-CAR | game_winner | 0.733 | 0.805 | 0.792 | 81 | 20 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ3 | team_total | 0.568 | 0.650 | 0.634 | 66 | 36 | no | +0.056 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ3 | game_spread | 0.165 | 0.240 | 0.223 | 25 | 77 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL5 | team_total | 0.282 | 0.355 | 0.340 | 36 | 65 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ2 | team_total | 0.782 | 0.850 | 0.838 | 86 | 16 | no | +0.049 | OK |
| KXNHLTOTAL-26NOV07SJDAL-6 | game_total | 0.515 | 0.585 | 0.571 | 59 | 42 | no | +0.048 | OK |
| KXNHLGAME-26NOV07CHICAR-CHI | game_winner | 0.267 | 0.205 | 0.217 | 21 | 80 | yes | +0.045 | OK |
| KXNHLGAME-26NOV07SJDAL-DAL | game_winner | 0.673 | 0.735 | 0.723 | 74 | 27 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ5 | team_total | 0.175 | 0.240 | 0.226 | 25 | 77 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL3 | team_total | 0.695 | 0.760 | 0.748 | 77 | 25 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR3 | team_total | 0.747 | 0.815 | 0.803 | 83 | 20 | no | +0.042 | OK |
| KXNHLTOTAL-26NOV07SJDAL-5 | game_total | 0.739 | 0.800 | 0.789 | 81 | 21 | no | +0.039 | OK |
| KXNHLGAME-26NOV07NYRSEA-NYR | game_winner | 0.496 | 0.555 | 0.543 | 56 | 45 | no | +0.036 | OK |
| KXNHLGAME-26NOV07NYRSEA-SEA | game_winner | 0.503 | 0.445 | 0.457 | 45 | 56 | yes | +0.036 | OK |
| KXNHLGAME-26NOV07FLAWSH-FLA | game_winner | 0.417 | 0.475 | 0.463 | 48 | 53 | no | +0.036 | OK |
| KXNHLGAME-26NOV07FLAWSH-WSH | game_winner | 0.583 | 0.525 | 0.537 | 53 | 48 | yes | +0.036 | OK |
| KXNHLTOTAL-26NOV07SJDAL-7 | game_total | 0.398 | 0.455 | 0.443 | 46 | 55 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV07CHICAR-6 | game_total | 0.539 | 0.600 | 0.588 | 61 | 41 | no | +0.034 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR2 | game_spread | 0.281 | 0.335 | 0.324 | 34 | 67 | no | +0.034 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NYI2 | game_spread | 0.276 | 0.225 | 0.235 | 23 | 78 | yes | +0.033 | OK |
| KXNHLGAME-26NOV07SJDAL-SJ | game_winner | 0.327 | 0.275 | 0.285 | 28 | 73 | yes | +0.033 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL3 | game_spread | 0.263 | 0.315 | 0.304 | 32 | 69 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV07CHICAR-7 | game_total | 0.421 | 0.475 | 0.464 | 48 | 53 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 | team_total | 0.482 | 0.540 | 0.529 | 55 | 47 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV07NJNYI-7 | game_total | 0.385 | 0.435 | 0.425 | 44 | 57 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR6 | team_total | 0.171 | 0.225 | 0.213 | 24 | 79 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL2 | team_total | 0.866 | 0.910 | 0.902 | 92 | 10 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR2 | team_total | 0.898 | 0.940 | 0.933 | 95 | 7 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV07NJNYI-5 | game_total | 0.721 | 0.770 | 0.761 | 78 | 24 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH3 | team_total | 0.680 | 0.635 | 0.644 | 64 | 37 | yes | +0.024 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-FLA2 | game_spread | 0.224 | 0.265 | 0.256 | 27 | 74 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-FLA3 | game_spread | 0.128 | 0.170 | 0.161 | 18 | 84 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV07CHICAR-8 | game_total | 0.243 | 0.285 | 0.276 | 29 | 72 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV07SJDAL-8 | game_total | 0.225 | 0.270 | 0.261 | 28 | 74 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.408 | 0.365 | 0.373 | 37 | 64 | yes | +0.021 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR3 | game_spread | 0.168 | 0.210 | 0.201 | 22 | 80 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV07CHICAR-5 | game_total | 0.758 | 0.805 | 0.796 | 82 | 21 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV07MTLTOR-8 | game_total | 0.345 | 0.300 | 0.309 | 31 | 71 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.526 | 0.480 | 0.489 | 49 | 53 | yes | +0.018 | OK |
| KXNHLGAME-26NOV07VANEDM-EDM | game_winner | 0.730 | 0.765 | 0.758 | 77 | 24 | no | +0.017 | OK |
| KXNHLGAME-26NOV07VANEDM-VAN | game_winner | 0.270 | 0.235 | 0.242 | 24 | 77 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH6 | team_total | 0.134 | 0.100 | 0.106 | 11 | 91 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-SEA2 | game_spread | 0.290 | 0.255 | 0.262 | 26 | 75 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN4 | team_total | 0.311 | 0.265 | 0.274 | 28 | 75 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CHI2 | game_spread | 0.112 | 0.085 | 0.090 | 9 | 92 | yes | +0.017 | OK |
| KXNHLGAME-26NOV07PITLA-LA | game_winner | 0.564 | 0.525 | 0.533 | 53 | 48 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV07SJDAL-9 | game_total | 0.154 | 0.185 | 0.178 | 19 | 82 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV07UTAOTT-UTA3 | game_spread | 0.173 | 0.210 | 0.202 | 22 | 80 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV07DETCOL-9 | game_total | 0.183 | 0.215 | 0.208 | 22 | 79 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV07SJDAL-4 | game_total | 0.836 | 0.870 | 0.864 | 88 | 14 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-SEA3 | team_total | 0.622 | 0.580 | 0.589 | 59 | 43 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA2 | team_total | 0.784 | 0.820 | 0.813 | 83 | 19 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV07CHICAR-4 | game_total | 0.847 | 0.880 | 0.874 | 89 | 13 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07UTAOTT-UTA4 | team_total | 0.408 | 0.445 | 0.437 | 45 | 56 | no | +0.015 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT2 | game_spread | 0.241 | 0.275 | 0.268 | 28 | 73 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-SEA4 | team_total | 0.411 | 0.370 | 0.378 | 38 | 64 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV07NJNYI-4 | game_total | 0.816 | 0.850 | 0.844 | 86 | 16 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-WSH2 | game_spread | 0.360 | 0.320 | 0.328 | 33 | 69 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV07NJNYI-6 | game_total | 0.498 | 0.535 | 0.528 | 54 | 47 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV07DETCOL-5 | game_total | 0.775 | 0.810 | 0.803 | 82 | 20 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM3 | game_spread | 0.389 | 0.425 | 0.418 | 43 | 58 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV07PITLA-LA2 | game_spread | 0.349 | 0.310 | 0.318 | 32 | 70 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV07STLNSH-10 | game_total | 0.088 | 0.060 | 0.065 | 7 | 95 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07STLNSH-STL6 | team_total | 0.098 | 0.070 | 0.075 | 8 | 94 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL3 | team_total | 0.693 | 0.735 | 0.727 | 75 | 28 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV07NJNYI-8 | game_total | 0.205 | 0.235 | 0.229 | 24 | 77 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5 | team_total | 0.087 | 0.065 | 0.069 | 7 | 94 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN6 | team_total | 0.066 | 0.040 | 0.044 | 5 | 97 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV07MTLTOR-9 | game_total | 0.255 | 0.215 | 0.223 | 23 | 80 | yes | +0.013 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ WSH | 0.583 | 0.572 | 0.175 | 0.211 | 6.42 | 6.49 | 0.961/0.998 | KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA3 +0.020 |
| STL @ NSH | 0.492 | 0.500 | 0.176 | 0.215 | 6.23 | 6.39 | 1.000/0.993 | KXNHLTOTAL-26NOV07STLNSH-7 +0.039 |
| NYR @ SEA | 0.503 | 0.541 | 0.177 | 0.220 | 6.35 | 6.34 | 1.005/0.983 | KXNHLGAME-26NOV07NYRSEA-SEA +0.038 |
| MTL @ TOR | 0.488 | 0.531 | 0.171 | 0.217 | 6.80 | 6.75 | 0.979/0.976 | KXNHLGAME-26NOV07MTLTOR-TOR +0.044 |
| UTA @ OTT | 0.496 | 0.555 | 0.172 | 0.215 | 6.40 | 6.38 | 0.994/0.993 | KXNHLGAME-26NOV07UTAOTT-OTT +0.060 |
| NJD @ NYI | 0.498 | 0.515 | 0.183 | 0.224 | 5.81 | 6.17 | 0.952/0.973 | KXNHLTOTAL-26NOV07NJNYI-7 +0.064 |
| CHI @ CAR | 0.733 | 0.689 | 0.152 | 0.196 | 6.07 | 6.56 | 0.997/1.004 | KXNHLTEAMTOTAL-26NOV07CHICAR-CHI3 +0.094 |
| SJS @ DAL | 0.673 | 0.632 | 0.165 | 0.215 | 5.94 | 6.19 | 0.986/1.027 | KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3 +0.064 |
| TBL @ MIN | 0.441 | 0.470 | 0.173 | 0.218 | 6.36 | 6.35 | 1.033/0.958 | KXNHLGAME-26NOV07TBMIN-TB -0.029 |
| DET @ COL | 0.626 | 0.658 | 0.170 | 0.196 | 6.25 | 6.48 | 0.976/1.015 | KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 +0.054 |
| PIT @ LAK | 0.564 | 0.556 | 0.164 | 0.217 | 6.53 | 6.37 | 0.993/1.021 | KXNHLTOTAL-26NOV07PITLA-6 -0.031 |
| VAN @ EDM | 0.730 | 0.663 | 0.134 | 0.192 | 7.16 | 7.00 | 1.009/1.021 | KXNHLSPREAD-26NOV07VANEDM-EDM2 -0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 41 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2508 (adj 0.2294) · $5.44 · thesis WSH:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 6c · p 0.1006 (adj 0.0867) · $2.13 · thesis FLA:OFFENSE_4PLUS
- Ryan Leonard: 1+ assists YES @ 22c · p 0.3132 (adj 0.2641) · $3.4 · thesis WSH:OFFENSE_4PLUS
- Alex Ovechkin: 1+ assists YES @ 22c · p 0.3108 (adj 0.2629) · $3.31 · thesis WSH:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 16c · p 0.2025 (adj 0.1881) · $2.16 · thesis NSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3036 (adj 0.2902) · $2.26 · thesis NSH:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1501 (adj 0.1313) · $2.42 · thesis SEA:OFFENSE_4PLUS
- New York R wins by over 1.5 goals NO @ 67c · p 0.7527 (adj 0.7088) · $5.97 · thesis SEA:WINS
- Ryan Winterton: 1+ goals YES @ 11c · p 0.142 (adj 0.1315) · $1.47 · thesis SEA:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 66c · p 0.7115 (adj 0.6961) · $5.75 · thesis NYR:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1772 (adj 0.1592) · $3.3 · thesis TOR:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 48c · p 0.635 (adj 0.531) · $7.1 · thesis MTL:SUPPRESSED
- Easton Cowan: 1+ assists YES @ 31c · p 0.3925 (adj 0.3488) · $3.11 · thesis TOR:OFFENSE_4PLUS
- Easton Cowan: 1+ goals YES @ 22c · p 0.2577 (adj 0.2458) · $1.79 · thesis TOR:OFFENSE_4PLUS
- Dylan Cozens: 1+ goals YES @ 24c · p 0.2895 (adj 0.2759) · $2.84 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 16c · p 0.2073 (adj 0.1892) · $2.15 · thesis OTT:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 16c · p 0.1984 (adj 0.1863) · $2.34 · thesis UTA:OFFENSE_4PLUS
- Utah wins by over 1.5 goals NO @ 70c · p 0.7672 (adj 0.7311) · $5.73 · thesis OTT:WINS
- New Jersey wins by over 1.5 goals NO @ 64c · p 0.7322 (adj 0.6836) · $8.36 · thesis NYI:WINS
- Jean-Gabriel Pageau: 1+ goals YES @ 13c · p 0.1698 (adj 0.1561) · $1.79 · thesis NYI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2539 (adj 0.2404) · $1.96 · thesis NYI:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 11c · p 0.1435 (adj 0.1301) · $1.73 · thesis NJD:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 18c · p 0.2373 (adj 0.2217) · $3.66 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 63c · p 0.7039 (adj 0.6817) · $8.36 · thesis CAR:SUPPRESSED
- Frank Nazar: 1+ goals YES @ 18c · p 0.2218 (adj 0.2088) · $2.06 · thesis CHI:OFFENSE_4PLUS
- Chicago over 1.5 goals scored YES @ 63c · p 0.7411 (adj 0.6656) · $2.76 · thesis CHI:WINS
- Macklin Celebrini: 1+ assists NO @ 53c · p 0.6102 (adj 0.5676) · $5.73 · thesis SJS:SUPPRESSED
- Dallas wins by over 1.5 goals NO @ 48c · p 0.5906 (adj 0.5155) · $4.21 · thesis GAME:TIGHT
- Dallas wins by over 2.5 goals NO @ 62c · p 0.7168 (adj 0.6506) · $1.93 · thesis GAME:TIGHT
- Ivar Stenberg: 1+ assists NO @ 71c · p 0.8004 (adj 0.7351) · $5.56 · thesis SJS:SUPPRESSED
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1384 (adj 0.1238) · $2.93 · thesis MIN:OFFENSE_4PLUS
- Bobby Brink: 1+ goals YES @ 14c · p 0.184 (adj 0.1705) · $2.66 · thesis MIN:OFFENSE_4PLUS
- Quinn Hughes: 1+ assists NO @ 37c · p 0.4577 (adj 0.4113) · $5.2 · thesis MIN:SUPPRESSED
- Blake Coleman: 1+ goals YES @ 20c · p 0.2494 (adj 0.2308) · $2.63 · thesis MIN:OFFENSE_4PLUS
- Sheldon Dries: 1+ goals YES @ 8c · p 0.1069 (adj 0.0964) · $1.17 · thesis DET:OFFENSE_4PLUS
- Lucas Raymond: 1+ assists NO @ 61c · p 0.6825 (adj 0.6387) · $3.64 · thesis DET:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 12c · p 0.1586 (adj 0.1464) · $2.11 · thesis PIT:WINS_BY_2PLUS
- Ben Kindel: 1+ goals NO @ 77c · p 0.8093 (adj 0.7982) · $7.58 · thesis PIT:SUPPRESSED
- Sidney Crosby: 1+ assists NO @ 58c · p 0.6465 (adj 0.6107) · $3.59 · thesis PIT:SUPPRESSED
- Edmonton wins by over 1.5 goals NO @ 45c · p 0.5425 (adj 0.4937) · $2.3 · thesis GAME:TIGHT
- Edmonton wins by over 2.5 goals NO @ 58c · p 0.6695 (adj 0.6222) · $3.82 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ WSH** · priced 175/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 27.35, exp saves 23.66 (sd 6.42), pull risk 0.058
- FLA net: Akira Schmid (PROJECTED) exp shots 26.43, exp saves 22.54 (sd 6.41), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.313 | 0.215 | 22/79 | +0.081 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.311 | 0.215 | 22/79 | +0.079 | STANDARD |
| Aliaksei Protas: 1+ points | 0.465 | 0.375 | 39/64 | +0.059 | STANDARD |
| Sam Reinhart: 1+ points | 0.510 | 0.600 | 61/41 | +0.063 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.251 | 0.165 | 17/84 | +0.071 | STANDARD |
| Alex Ovechkin: 1+ points | 0.497 | 0.415 | 43/60 | +0.050 | STANDARD |

**STL @ NSH** · priced 154/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.66, exp saves 23.85 (sd 6.6), pull risk 0.066
- STL net: Joel Hofer (PROJECTED) exp shots 27.8, exp saves 24.02 (sd 6.68), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.233 | 0.310 | 33/71 | +0.043 | STANDARD |
| Ross Colton: 1+ points | 0.358 | 0.290 | 31/73 | +0.033 | STANDARD |
| Mason McTavish: 1+ assists | 0.274 | 0.335 | 35/68 | +0.031 | STANDARD |
| Adam Edstrom: 1+ goals | 0.203 | 0.145 | 16/87 | +0.033 | STANDARD |
| Mavrik Bourque: 1+ points | 0.390 | 0.445 | 45/56 | +0.033 | STANDARD |
| Jimmy Snuggerud: 1+ points | 0.584 | 0.530 | 55/49 | +0.016 | STANDARD |

**NYR @ SEA** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.17, exp saves 23.64 (sd 6.44), pull risk 0.057
- NYR net: Dylan Garand (PROJECTED) exp shots 27.28, exp saves 23.37 (sd 6.57), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ goals | 0.183 | 0.105 | 17/96 | +0.003 | STANDARD |
| Ben Meyers: 1+ goals | 0.150 | 0.075 | 10/95 | +0.044 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.470 | 0.540 | 57/49 | +0.022 | STANDARD |
| Bobby McMann: 1+ assists | 0.308 | 0.245 | 25/76 | +0.045 | STANDARD |
| Pavel Dorofeyev: 1+ goals | 0.288 | 0.350 | 36/66 | +0.036 | STANDARD |
| Berkly Catton: 1+ goals | 0.224 | 0.165 | 19/86 | +0.023 | STANDARD |

**MTL @ TOR** · priced 160/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 29.0, exp saves 25.16 (sd 6.87), pull risk 0.067
- MTL net: Jacob Fowler (PROJECTED) exp shots 28.71, exp saves 24.72 (sd 6.92), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.365 | 0.525 | 53/48 | +0.138 | STANDARD |
| Easton Cowan: 1+ points | 0.551 | 0.435 | 45/58 | +0.083 | STANDARD |
| Nick Suzuki: 1+ points | 0.562 | 0.665 | 68/35 | +0.072 | STANDARD |
| Morgan Rielly: 1+ points | 0.426 | 0.325 | 35/70 | +0.060 | STANDARD |
| Nick Suzuki: 2+ assists | 0.077 | 0.175 | 19/84 | +0.074 | STANDARD |
| Morgan Rielly: 1+ assists | 0.366 | 0.270 | 29/75 | +0.062 | STANDARD |

**UTA @ OTT** · priced 164/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 26.39, exp saves 23.02 (sd 6.34), pull risk 0.056
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.47, exp saves 23.52 (sd 6.68), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikhail Sergachev: 1+ points | 0.478 | 0.570 | 60/46 | +0.045 | STANDARD |
| Clayton Keller: 1+ assists | 0.430 | 0.510 | 53/51 | +0.043 | STANDARD |
| Clayton Keller: 2+ points | 0.202 | 0.280 | 31/75 | +0.035 | STANDARD |
| Mikhail Sergachev: 1+ assists | 0.413 | 0.490 | 51/53 | +0.040 | STANDARD |
| Logan Cooley: 1+ points | 0.513 | 0.590 | 61/43 | +0.039 | STANDARD |
| Clayton Keller: 1+ points | 0.565 | 0.640 | 66/38 | +0.038 | STANDARD |

**NJD @ NYI** · priced 164/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 28.65, exp saves 24.86 (sd 6.65), pull risk 0.059
- NJD net: Jake Allen (PROJECTED) exp shots 26.66, exp saves 23.1 (sd 6.41), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.384 | 0.510 | 52/50 | +0.099 | STANDARD |
| Luke Evangelista: 1+ assists | 0.216 | 0.330 | 34/68 | +0.089 | STANDARD |
| Emil Heineman: 1+ assists | 0.296 | 0.195 | 20/81 | +0.085 | STANDARD |
| Jack Hughes: 2+ points | 0.220 | 0.315 | 33/70 | +0.065 | STANDARD |
| Jack Hughes: 1+ points | 0.577 | 0.665 | 70/37 | +0.037 | STANDARD |
| Nico Hischier: 1+ assists | 0.285 | 0.370 | 39/65 | +0.049 | STANDARD |

**CHI @ CAR** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 21.81, exp saves 19.43 (sd 5.47), pull risk 0.045
- CHI net: Spencer Knight (PROJECTED) exp shots 33.1, exp saves 27.62 (sd 7.67), pull risk 0.1

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.205 | 0.330 | 35/69 | +0.090 | STANDARD |
| Sebastian Aho: 1+ assists | 0.380 | 0.495 | 51/52 | +0.082 | STANDARD |
| Sebastian Aho: 1+ goals | 0.296 | 0.385 | 40/63 | +0.058 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.466 | 0.380 | 40/64 | +0.049 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.357 | 0.440 | 45/57 | +0.055 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.557 | 0.635 | 65/38 | +0.047 | STANDARD |

**SJS @ DAL** · priced 157/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.49, exp saves 21.66 (sd 5.94), pull risk 0.041
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.67, exp saves 23.5 (sd 6.63), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.277 | 0.390 | 41/63 | +0.077 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.200 | 0.300 | 31/71 | +0.076 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.478 | 0.575 | 59/44 | +0.065 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.390 | 0.475 | 48/53 | +0.063 | STANDARD |
| Ivar Stenberg: 1+ points | 0.336 | 0.420 | 44/60 | +0.047 | STANDARD |
| Jason Robertson: 1+ assists | 0.452 | 0.530 | 55/49 | +0.041 | STANDARD |

**TBL @ MIN** · priced 154/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.08, exp saves 24.1 (sd 6.75), pull risk 0.07
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 27.46, exp saves 23.87 (sd 6.53), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.487 | 0.620 | 63/39 | +0.106 | STANDARD |
| Matt Boldy: 1+ assists | 0.359 | 0.485 | 49/52 | +0.104 | STANDARD |
| Bobby Brink: 1+ points | 0.419 | 0.310 | 34/72 | +0.063 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.383 | 0.485 | 50/53 | +0.069 | STANDARD |
| Bobby Brink: 1+ assists | 0.291 | 0.195 | 20/81 | +0.080 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.270 | 0.365 | 38/65 | +0.064 | STANDARD |

**DET @ COL** · priced 174/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.53, exp saves 23.53 (sd 6.32), pull risk 0.044
- DET net: Daniil Tarasov (PROJECTED) exp shots 30.11, exp saves 25.24 (sd 7.1), pull risk 0.099

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lucas Raymond: 1+ assists | 0.318 | 0.405 | 42/61 | +0.056 | STANDARD |
| Lucas Raymond: 1+ points | 0.491 | 0.565 | 60/47 | +0.021 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.372 | 0.430 | 45/59 | +0.021 | STANDARD |
| Artturi Lehkonen: 1+ assists | 0.330 | 0.275 | 29/74 | +0.026 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.166 | 0.220 | 24/80 | +0.023 | STANDARD |
| Moritz Seider: 1+ points | 0.424 | 0.475 | 49/54 | +0.018 | STANDARD |

**PIT @ LAK** · priced 164/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.28, exp saves 23.7 (sd 6.48), pull risk 0.055
- PIT net: Sergei Murashov (PROJECTED) exp shots 27.6, exp saves 23.54 (sd 6.64), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 2+ points | 0.246 | 0.340 | 35/67 | +0.069 | STANDARD |
| Artemi Panarin: 1+ assists | 0.434 | 0.515 | 53/50 | +0.048 | STANDARD |
| Ben Kindel: 1+ points | 0.386 | 0.460 | 47/55 | +0.047 | STANDARD |
| Sidney Crosby: 1+ assists | 0.353 | 0.425 | 43/58 | +0.049 | STANDARD |
| Trevor Moore: 1+ points | 0.432 | 0.365 | 39/66 | +0.025 | STANDARD |
| Erik Karlsson: 1+ assists | 0.410 | 0.475 | 49/54 | +0.033 | STANDARD |

**VAN @ EDM** · priced 158/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 24.17, exp saves 21.32 (sd 5.94), pull risk 0.05
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.14, exp saves 25.13 (sd 7.25), pull risk 0.109

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Shea: First Goalscorer | 0.011 | 0.500 | 97/97 | +0.017 | STANDARD |
| Connor McDavid: 4+ assists | 0.015 | 0.500 | 99/99 | -0.006 | STANDARD |
| Connor Murphy: 2+ points | 0.030 | 0.500 | 99/99 | -0.021 | STANDARD |
| Leon Draisaitl: 3+ assists | 0.034 | 0.500 | 99/99 | -0.024 | STANDARD |
| Elias Pettersson (#40): 3+ points | 0.040 | 0.500 | 99/99 | -0.030 | STANDARD |
| Ryan Shea: 2+ assists | 0.043 | 0.500 | 99/99 | -0.034 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
