# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-07T14:42:37Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4137 · contracts joined: 2459 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2159, 'OK': 146, 'NO_EDGE': 154}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 331, 'game_early_goal': 12, 'first_goal': 396, 'game_winner': 24, 'player_goals': 682, 'game_overtime': 12, 'player_points': 438, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ WSH | 2026-11-07T17:30:00Z | T-90m | 0.583 | 0.417 | 0.175 | 6.42 | 3.47 | 2.95 | 233 (25/208) | PROJECTED/PROJECTED |
| STL @ NSH | 2026-11-07T18:00:00Z | T-3h | 0.492 | 0.508 | 0.176 | 6.23 | 3.08 | 3.15 | 209 (25/184) | PROJECTED/PROJECTED |
| NYR @ SEA | 2026-11-07T22:00:00Z | T-6h | 0.503 | 0.496 | 0.177 | 6.35 | 3.19 | 3.16 | 220 (25/195) | PROJECTED/PROJECTED |
| MTL @ TOR | 2026-11-08T00:00:00Z | T-6h | 0.488 | 0.512 | 0.171 | 6.80 | 3.35 | 3.45 | 212 (25/187) | PROJECTED/PROJECTED |
| UTA @ OTT | 2026-11-08T00:00:00Z | T-6h | 0.496 | 0.504 | 0.172 | 6.40 | 3.19 | 3.21 | 221 (25/196) | PROJECTED/PROJECTED |
| NJD @ NYI | 2026-11-08T00:00:00Z | T-6h | 0.498 | 0.502 | 0.183 | 5.81 | 2.89 | 2.92 | 218 (25/193) | PROBABLE/PROJECTED |
| CHI @ CAR | 2026-11-08T01:00:00Z | T-6h | 0.733 | 0.267 | 0.152 | 6.07 | 3.79 | 2.27 | 217 (25/192) | PROJECTED/PROJECTED |
| SJS @ DAL | 2026-11-08T01:00:00Z | T-6h | 0.673 | 0.327 | 0.165 | 5.94 | 3.52 | 2.42 | 211 (25/186) | PROJECTED/PROJECTED |
| TBL @ MIN | 2026-11-08T01:00:00Z | T-6h | 0.441 | 0.559 | 0.173 | 6.36 | 3.01 | 3.35 | 217 (25/192) | CONFIRMED/PROJECTED |
| DET @ COL | 2026-11-08T02:00:00Z | T-6h | 0.626 | 0.374 | 0.170 | 6.25 | 3.53 | 2.72 | 234 (25/209) | PROJECTED/PROJECTED |
| PIT @ LAK | 2026-11-08T02:00:00Z | T-6h | 0.564 | 0.436 | 0.164 | 6.53 | 3.46 | 3.07 | 216 (25/191) | PROJECTED/PROJECTED |
| VAN @ EDM | 2026-11-08T03:00:00Z | T-12h | 0.730 | 0.270 | 0.134 | 7.16 | 4.38 | 2.78 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV07CHICAR-CAR3 | game_spread | 0.358 | 0.480 | 0.455 | 49 | 53 | no | +0.094 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CAR2 | game_spread | 0.508 | 0.615 | 0.594 | 62 | 39 | no | +0.085 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL3 | game_spread | 0.292 | 0.385 | 0.366 | 39 | 62 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ4 | team_total | 0.346 | 0.435 | 0.417 | 44 | 57 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR4 | team_total | 0.539 | 0.635 | 0.616 | 65 | 38 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4 | team_total | 0.481 | 0.570 | 0.552 | 58 | 44 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR5 | team_total | 0.332 | 0.420 | 0.402 | 43 | 59 | no | +0.061 | OK |
| KXNHLGAME-26NOV07NJNYI-NJ | game_winner | 0.502 | 0.585 | 0.569 | 59 | 42 | no | +0.061 | OK |
| KXNHLGAME-26NOV07NJNYI-NYI | game_winner | 0.498 | 0.415 | 0.431 | 42 | 59 | yes | +0.061 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL2 | game_spread | 0.446 | 0.525 | 0.509 | 53 | 48 | no | +0.056 | OK |
| KXNHLGAME-26NOV07CHICAR-CAR | game_winner | 0.733 | 0.805 | 0.792 | 81 | 20 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ3 | team_total | 0.568 | 0.650 | 0.634 | 66 | 36 | no | +0.056 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ2 | game_spread | 0.281 | 0.355 | 0.339 | 36 | 65 | no | +0.053 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ3 | game_spread | 0.165 | 0.240 | 0.223 | 25 | 77 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR3 | team_total | 0.747 | 0.820 | 0.807 | 83 | 19 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL5 | team_total | 0.282 | 0.355 | 0.340 | 36 | 65 | no | +0.052 | OK |
| KXNHLTOTAL-26NOV07SJDAL-6 | game_total | 0.515 | 0.585 | 0.571 | 59 | 42 | no | +0.048 | OK |
| KXNHLGAME-26NOV07CHICAR-CHI | game_winner | 0.267 | 0.205 | 0.217 | 21 | 80 | yes | +0.045 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NYI2 | game_spread | 0.276 | 0.215 | 0.226 | 22 | 79 | yes | +0.044 | OK |
| KXNHLGAME-26NOV07SJDAL-DAL | game_winner | 0.673 | 0.735 | 0.723 | 74 | 27 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ5 | team_total | 0.175 | 0.240 | 0.226 | 25 | 77 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL3 | team_total | 0.695 | 0.760 | 0.748 | 77 | 25 | no | +0.042 | OK |
| KXNHLTOTAL-26NOV07SJDAL-5 | game_total | 0.739 | 0.800 | 0.789 | 81 | 21 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ2 | team_total | 0.782 | 0.845 | 0.834 | 86 | 17 | no | +0.038 | OK |
| KXNHLGAME-26NOV07NYRSEA-NYR | game_winner | 0.496 | 0.555 | 0.543 | 56 | 45 | no | +0.036 | OK |
| KXNHLGAME-26NOV07NYRSEA-SEA | game_winner | 0.503 | 0.445 | 0.457 | 45 | 56 | yes | +0.036 | OK |
| KXNHLGAME-26NOV07FLAWSH-FLA | game_winner | 0.417 | 0.475 | 0.463 | 48 | 53 | no | +0.036 | OK |
| KXNHLGAME-26NOV07FLAWSH-WSH | game_winner | 0.583 | 0.525 | 0.537 | 53 | 48 | yes | +0.036 | OK |
| KXNHLTOTAL-26NOV07SJDAL-7 | game_total | 0.398 | 0.455 | 0.443 | 46 | 55 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV07CHICAR-6 | game_total | 0.539 | 0.600 | 0.588 | 61 | 41 | no | +0.034 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR2 | game_spread | 0.281 | 0.335 | 0.324 | 34 | 67 | no | +0.034 | OK |
| KXNHLGAME-26NOV07SJDAL-SJ | game_winner | 0.327 | 0.275 | 0.285 | 28 | 73 | yes | +0.033 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL3 | game_spread | 0.263 | 0.315 | 0.304 | 32 | 69 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV07CHICAR-7 | game_total | 0.421 | 0.475 | 0.464 | 48 | 53 | no | +0.031 | OK |
| KXNHLTOTAL-26NOV07NJNYI-7 | game_total | 0.385 | 0.435 | 0.425 | 44 | 57 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR6 | team_total | 0.171 | 0.225 | 0.213 | 24 | 79 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL2 | team_total | 0.866 | 0.910 | 0.902 | 92 | 10 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR2 | team_total | 0.898 | 0.940 | 0.933 | 95 | 7 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV07NJNYI-5 | game_total | 0.721 | 0.770 | 0.761 | 78 | 24 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH3 | team_total | 0.680 | 0.635 | 0.644 | 64 | 37 | yes | +0.024 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-FLA2 | game_spread | 0.224 | 0.265 | 0.256 | 27 | 74 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-FLA3 | game_spread | 0.128 | 0.170 | 0.161 | 18 | 84 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV07CHICAR-8 | game_total | 0.243 | 0.285 | 0.276 | 29 | 72 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV07SJDAL-8 | game_total | 0.225 | 0.265 | 0.257 | 27 | 74 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.408 | 0.365 | 0.373 | 37 | 64 | yes | +0.021 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR3 | game_spread | 0.168 | 0.210 | 0.201 | 22 | 80 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV07CHICAR-5 | game_total | 0.758 | 0.805 | 0.796 | 82 | 21 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 | team_total | 0.482 | 0.530 | 0.521 | 54 | 48 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV07MTLTOR-8 | game_total | 0.345 | 0.300 | 0.309 | 31 | 71 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.526 | 0.480 | 0.489 | 49 | 53 | yes | +0.018 | OK |
| KXNHLGAME-26NOV07VANEDM-EDM | game_winner | 0.730 | 0.765 | 0.758 | 77 | 24 | no | +0.017 | OK |
| KXNHLGAME-26NOV07VANEDM-VAN | game_winner | 0.270 | 0.235 | 0.242 | 24 | 77 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH6 | team_total | 0.134 | 0.100 | 0.106 | 11 | 91 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-SEA2 | game_spread | 0.290 | 0.255 | 0.262 | 26 | 75 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CHI2 | game_spread | 0.112 | 0.085 | 0.090 | 9 | 92 | yes | +0.017 | OK |
| KXNHLGAME-26NOV07PITLA-LA | game_winner | 0.564 | 0.525 | 0.533 | 53 | 48 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV07SJDAL-9 | game_total | 0.154 | 0.185 | 0.178 | 19 | 82 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV07UTAOTT-UTA3 | game_spread | 0.173 | 0.210 | 0.202 | 22 | 80 | no | +0.016 | OK |
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
| KXNHLTOTAL-26NOV07PITLA-8 | game_total | 0.307 | 0.275 | 0.281 | 28 | 73 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL5 | team_total | 0.282 | 0.325 | 0.316 | 34 | 69 | no | +0.013 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 40 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2508 (adj 0.2294) · $5.95 · thesis WSH:OFFENSE_4PLUS
- Ryan Leonard: 1+ assists YES @ 22c · p 0.3132 (adj 0.2641) · $3.71 · thesis WSH:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 7c · p 0.1006 (adj 0.0917) · $1.92 · thesis FLA:OFFENSE_4PLUS
- Alex Ovechkin: 1+ assists YES @ 23c · p 0.3108 (adj 0.2679) · $2.98 · thesis WSH:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 68c · p 0.7671 (adj 0.721) · $9.07 · thesis NSH:SUPPRESSED
- Adam Edstrom: 1+ goals YES @ 16c · p 0.2025 (adj 0.1881) · $2.41 · thesis NSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3036 (adj 0.2902) · $3.04 · thesis NSH:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1501 (adj 0.1326) · $2.8 · thesis SEA:OFFENSE_4PLUS
- New York R wins by over 1.5 goals NO @ 67c · p 0.7527 (adj 0.7088) · $6.78 · thesis SEA:WINS
- Jani Nyman: 1+ goals YES @ 12c · p 0.1535 (adj 0.1414) · $1.53 · thesis SEA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 11c · p 0.142 (adj 0.1302) · $1.43 · thesis SEA:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1772 (adj 0.1567) · $3.25 · thesis TOR:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 48c · p 0.635 (adj 0.531) · $7.71 · thesis MTL:SUPPRESSED
- Easton Cowan: 1+ assists YES @ 31c · p 0.3925 (adj 0.3488) · $3.4 · thesis TOR:OFFENSE_4PLUS
- Easton Cowan: 1+ goals YES @ 22c · p 0.2577 (adj 0.2445) · $1.76 · thesis TOR:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 15c · p 0.2073 (adj 0.188) · $3.43 · thesis OTT:OFFENSE_4PLUS
- Dylan Cozens: 1+ goals YES @ 24c · p 0.2895 (adj 0.2734) · $2.7 · thesis OTT:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 16c · p 0.1984 (adj 0.1863) · $2.54 · thesis UTA:OFFENSE_4PLUS
- Utah wins by over 1.5 goals NO @ 70c · p 0.7672 (adj 0.7311) · $5.78 · thesis OTT:WINS
- Jean-Gabriel Pageau: 1+ goals YES @ 13c · p 0.1698 (adj 0.1573) · $2.4 · thesis NYI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2539 (adj 0.2404) · $2.61 · thesis NYI:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 11c · p 0.1435 (adj 0.1314) · $1.73 · thesis NJD:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 64c · p 0.6818 (adj 0.6688) · $4.21 · thesis NJD:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 18c · p 0.2373 (adj 0.2217) · $3.98 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 63c · p 0.7039 (adj 0.6817) · $9.07 · thesis CAR:SUPPRESSED
- Frank Nazar: 1+ goals YES @ 18c · p 0.2218 (adj 0.2088) · $2.23 · thesis CHI:OFFENSE_4PLUS
- Chicago over 1.5 goals scored YES @ 63c · p 0.7411 (adj 0.6656) · $3.0 · thesis CHI:WINS
- Ivar Stenberg: 1+ assists NO @ 71c · p 0.7948 (adj 0.7449) · $8.02 · thesis SJS:SUPPRESSED
- Macklin Celebrini: 1+ assists NO @ 53c · p 0.6143 (adj 0.5696) · $5.58 · thesis SJS:SUPPRESSED
- Dallas wins by over 1.5 goals NO @ 48c · p 0.5906 (adj 0.5155) · $4.57 · thesis GAME:TIGHT
- Dallas wins by over 2.5 goals NO @ 62c · p 0.7168 (adj 0.6506) · $2.11 · thesis GAME:TIGHT
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1389 (adj 0.1242) · $3.26 · thesis MIN:OFFENSE_4PLUS
- Bobby Brink: 1+ goals YES @ 14c · p 0.1854 (adj 0.1691) · $2.7 · thesis MIN:OFFENSE_4PLUS
- Quinn Hughes: 1+ assists NO @ 37c · p 0.4633 (adj 0.4142) · $6.23 · thesis MIN:SUPPRESSED
- Ryan Hartman: 1+ goals YES @ 15c · p 0.1879 (adj 0.1759) · $2.58 · thesis MIN:OFFENSE_4PLUS
- Sheldon Dries: 1+ goals YES @ 8c · p 0.1069 (adj 0.0952) · $1.11 · thesis DET:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0756 (adj 0.0642) · $1.09 · thesis LAK:OFFENSE_4PLUS
- Sidney Crosby: 1+ assists NO @ 58c · p 0.6465 (adj 0.6107) · $4.02 · thesis PIT:SUPPRESSED
- Edmonton wins by over 1.5 goals NO @ 45c · p 0.5425 (adj 0.4937) · $2.5 · thesis GAME:TIGHT
- Edmonton wins by over 2.5 goals NO @ 58c · p 0.6695 (adj 0.6222) · $4.15 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ WSH** · priced 175/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 27.36, exp saves 23.67 (sd 6.45), pull risk 0.059
- FLA net: Akira Schmid (PROJECTED) exp shots 26.44, exp saves 22.54 (sd 6.39), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.313 | 0.215 | 22/79 | +0.081 | STANDARD |
| Sam Reinhart: 1+ points | 0.510 | 0.605 | 62/41 | +0.063 | STANDARD |
| Aliaksei Protas: 1+ points | 0.465 | 0.375 | 39/64 | +0.059 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.311 | 0.225 | 23/78 | +0.068 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.251 | 0.165 | 17/84 | +0.071 | STANDARD |
| Alex Ovechkin: 1+ points | 0.497 | 0.415 | 43/60 | +0.050 | STANDARD |

**STL @ NSH** · priced 154/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.66, exp saves 23.86 (sd 6.58), pull risk 0.065
- STL net: Joel Hofer (PROJECTED) exp shots 27.81, exp saves 24.0 (sd 6.68), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.233 | 0.325 | 33/68 | +0.072 | STANDARD |
| Ross Colton: 1+ points | 0.358 | 0.290 | 31/73 | +0.033 | STANDARD |
| Mason McTavish: 1+ assists | 0.274 | 0.335 | 35/68 | +0.031 | STANDARD |
| Adam Edstrom: 1+ goals | 0.203 | 0.145 | 16/87 | +0.033 | STANDARD |
| Mavrik Bourque: 1+ points | 0.390 | 0.445 | 45/56 | +0.033 | STANDARD |
| Jimmy Snuggerud: 1+ points | 0.584 | 0.530 | 55/49 | +0.016 | STANDARD |

**NYR @ SEA** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.18, exp saves 23.61 (sd 6.44), pull risk 0.059
- NYR net: Dylan Garand (PROJECTED) exp shots 27.29, exp saves 23.38 (sd 6.61), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ goals | 0.183 | 0.105 | 17/96 | +0.003 | STANDARD |
| Ben Meyers: 1+ goals | 0.150 | 0.080 | 10/94 | +0.044 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.470 | 0.540 | 57/49 | +0.022 | STANDARD |
| Bobby McMann: 1+ assists | 0.308 | 0.245 | 25/76 | +0.045 | STANDARD |
| Pavel Dorofeyev: 1+ goals | 0.288 | 0.345 | 36/67 | +0.026 | STANDARD |
| Kaapo Kakko: 1+ points | 0.455 | 0.400 | 42/62 | +0.018 | STANDARD |

**MTL @ TOR** · priced 160/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 29.0, exp saves 25.17 (sd 6.92), pull risk 0.065
- MTL net: Jacob Fowler (PROJECTED) exp shots 28.71, exp saves 24.72 (sd 6.93), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.365 | 0.525 | 53/48 | +0.138 | STANDARD |
| Easton Cowan: 1+ points | 0.551 | 0.435 | 45/58 | +0.083 | STANDARD |
| Morgan Rielly: 1+ assists | 0.366 | 0.270 | 29/75 | +0.062 | STANDARD |
| Morgan Rielly: 1+ points | 0.426 | 0.330 | 35/69 | +0.060 | STANDARD |
| Nick Suzuki: 1+ points | 0.562 | 0.655 | 68/37 | +0.051 | STANDARD |
| Nick Suzuki: 2+ points | 0.207 | 0.295 | 33/74 | +0.040 | STANDARD |

**UTA @ OTT** · priced 164/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 26.39, exp saves 23.01 (sd 6.33), pull risk 0.056
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.47, exp saves 23.57 (sd 6.64), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikhail Sergachev: 1+ points | 0.478 | 0.565 | 59/46 | +0.045 | STANDARD |
| Mikhail Sergachev: 1+ assists | 0.413 | 0.495 | 51/52 | +0.050 | STANDARD |
| Clayton Keller: 2+ points | 0.202 | 0.280 | 31/75 | +0.035 | STANDARD |
| Michael Amadio: 1+ goals | 0.207 | 0.130 | 15/89 | +0.048 | STANDARD |
| Logan Cooley: 1+ points | 0.513 | 0.590 | 61/43 | +0.039 | STANDARD |
| Clayton Keller: 1+ assists | 0.430 | 0.505 | 52/51 | +0.043 | STANDARD |

**NJD @ NYI** · priced 164/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 28.66, exp saves 24.88 (sd 6.71), pull risk 0.058
- NJD net: Jake Allen (PROJECTED) exp shots 26.66, exp saves 23.09 (sd 6.4), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.384 | 0.505 | 51/50 | +0.099 | STANDARD |
| Luke Evangelista: 1+ assists | 0.216 | 0.335 | 34/67 | +0.099 | STANDARD |
| Emil Heineman: 1+ assists | 0.296 | 0.195 | 20/81 | +0.085 | STANDARD |
| Jack Hughes: 1+ points | 0.577 | 0.660 | 69/37 | +0.037 | STANDARD |
| Nico Hischier: 1+ assists | 0.285 | 0.365 | 38/65 | +0.049 | STANDARD |
| Emil Heineman: 1+ points | 0.426 | 0.350 | 37/67 | +0.040 | STANDARD |

**CHI @ CAR** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 21.81, exp saves 19.44 (sd 5.47), pull risk 0.045
- CHI net: Spencer Knight (PROJECTED) exp shots 33.11, exp saves 27.6 (sd 7.72), pull risk 0.101

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.205 | 0.325 | 35/70 | +0.080 | STANDARD |
| Sebastian Aho: 1+ assists | 0.380 | 0.495 | 51/52 | +0.082 | STANDARD |
| Sebastian Aho: 1+ goals | 0.296 | 0.385 | 40/63 | +0.058 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.466 | 0.380 | 40/64 | +0.049 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.357 | 0.440 | 45/57 | +0.055 | STANDARD |
| Nikolaj Ehlers: 1+ assists | 0.400 | 0.475 | 48/53 | +0.053 | STANDARD |

**SJS @ DAL** · priced 157/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.52, exp saves 21.69 (sd 6.02), pull risk 0.044
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.69, exp saves 23.57 (sd 6.62), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.277 | 0.390 | 41/63 | +0.077 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.205 | 0.305 | 32/71 | +0.070 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.478 | 0.575 | 59/44 | +0.065 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.386 | 0.475 | 48/53 | +0.067 | STANDARD |
| Ivar Stenberg: 1+ points | 0.343 | 0.425 | 44/59 | +0.050 | STANDARD |
| Jason Robertson: 1+ assists | 0.452 | 0.525 | 54/49 | +0.041 | STANDARD |

**TBL @ MIN** · priced 154/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.15, exp saves 24.16 (sd 6.73), pull risk 0.071
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 27.48, exp saves 23.86 (sd 6.51), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.487 | 0.620 | 63/39 | +0.106 | STANDARD |
| Matt Boldy: 1+ assists | 0.356 | 0.485 | 49/52 | +0.106 | STANDARD |
| Bobby Brink: 1+ points | 0.418 | 0.305 | 33/72 | +0.072 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.377 | 0.485 | 50/53 | +0.076 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.263 | 0.370 | 39/65 | +0.071 | STANDARD |
| Quinn Hughes: 1+ assists | 0.537 | 0.635 | 64/37 | +0.077 | STANDARD |

**DET @ COL** · priced 174/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.53, exp saves 23.51 (sd 6.29), pull risk 0.044
- DET net: Daniil Tarasov (PROJECTED) exp shots 30.12, exp saves 25.27 (sd 7.16), pull risk 0.099

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lucas Raymond: 1+ assists | 0.318 | 0.400 | 42/62 | +0.046 | STANDARD |
| Lucas Raymond: 1+ points | 0.491 | 0.560 | 59/47 | +0.021 | STANDARD |
| Lucas Raymond: 2+ points | 0.142 | 0.200 | 24/84 | +0.009 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.372 | 0.430 | 45/59 | +0.021 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.521 | 0.570 | 60/46 | +0.002 | STANDARD |
| Artturi Lehkonen: 1+ points | 0.557 | 0.510 | 54/52 | -0.000 | STANDARD |

**PIT @ LAK** · priced 164/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.29, exp saves 23.72 (sd 6.46), pull risk 0.056
- PIT net: Sergei Murashov (PROJECTED) exp shots 27.61, exp saves 23.54 (sd 6.64), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 2+ points | 0.246 | 0.340 | 35/67 | +0.069 | STANDARD |
| Artemi Panarin: 1+ assists | 0.434 | 0.515 | 53/50 | +0.048 | STANDARD |
| Ben Kindel: 1+ points | 0.386 | 0.460 | 47/55 | +0.047 | STANDARD |
| Sidney Crosby: 1+ assists | 0.353 | 0.425 | 43/58 | +0.049 | STANDARD |
| Erik Karlsson: 1+ assists | 0.410 | 0.475 | 49/54 | +0.033 | STANDARD |
| Artemi Panarin: 2+ assists | 0.105 | 0.170 | 19/85 | +0.036 | STANDARD |

**VAN @ EDM** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 24.18, exp saves 21.29 (sd 5.92), pull risk 0.054
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.14, exp saves 25.11 (sd 7.31), pull risk 0.108

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
