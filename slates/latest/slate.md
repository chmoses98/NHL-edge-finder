# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-07T15:37:58Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4355 · contracts joined: 2677 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2377, 'OK': 141, 'NO_EDGE': 159}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 381, 'game_early_goal': 12, 'first_goal': 432, 'game_winner': 24, 'player_goals': 743, 'game_overtime': 12, 'player_points': 507, 'goalie_saves': 2, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ WSH | 2026-11-07T17:30:00Z | T-90m | 0.595 | 0.405 | 0.168 | 6.32 | 3.47 | 2.85 | 234 (25/209) | CONFIRMED/CONFIRMED |
| STL @ NSH | 2026-11-07T18:00:00Z | T-90m | 0.492 | 0.508 | 0.176 | 6.23 | 3.08 | 3.15 | 212 (25/187) | PROJECTED/PROJECTED |
| NYR @ SEA | 2026-11-07T22:00:00Z | T-6h | 0.503 | 0.496 | 0.177 | 6.35 | 3.19 | 3.16 | 224 (25/199) | PROJECTED/PROJECTED |
| MTL @ TOR | 2026-11-08T00:00:00Z | T-6h | 0.482 | 0.518 | 0.172 | 6.82 | 3.35 | 3.48 | 212 (25/187) | PROBABLE/PROJECTED |
| UTA @ OTT | 2026-11-08T00:00:00Z | T-6h | 0.469 | 0.531 | 0.176 | 6.61 | 3.20 | 3.41 | 221 (25/196) | PROJECTED/PROJECTED |
| NJD @ NYI | 2026-11-08T00:00:00Z | T-6h | 0.498 | 0.502 | 0.183 | 5.81 | 2.89 | 2.92 | 218 (25/193) | PROBABLE/PROJECTED |
| CHI @ CAR | 2026-11-08T01:00:00Z | T-6h | 0.738 | 0.262 | 0.148 | 6.03 | 3.79 | 2.25 | 234 (25/209) | PROBABLE/PROJECTED |
| SJS @ DAL | 2026-11-08T01:00:00Z | T-6h | 0.673 | 0.327 | 0.165 | 5.94 | 3.52 | 2.42 | 221 (25/196) | PROJECTED/PROJECTED |
| TBL @ MIN | 2026-11-08T01:00:00Z | T-6h | 0.441 | 0.559 | 0.173 | 6.36 | 3.01 | 3.35 | 224 (25/199) | CONFIRMED/PROJECTED |
| DET @ COL | 2026-11-08T02:00:00Z | T-6h | 0.626 | 0.374 | 0.170 | 6.25 | 3.53 | 2.72 | 237 (25/212) | PROJECTED/PROJECTED |
| PIT @ LAK | 2026-11-08T02:00:00Z | T-6h | 0.564 | 0.436 | 0.164 | 6.53 | 3.46 | 3.07 | 216 (25/191) | PROJECTED/PROJECTED |
| VAN @ EDM | 2026-11-08T03:00:00Z | T-6h | 0.730 | 0.270 | 0.134 | 7.16 | 4.38 | 2.78 | 224 (25/199) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV07CHICAR-CAR3 | game_spread | 0.365 | 0.475 | 0.452 | 48 | 53 | no | +0.088 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CAR2 | game_spread | 0.516 | 0.615 | 0.596 | 62 | 39 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR4 | team_total | 0.539 | 0.645 | 0.625 | 66 | 37 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4 | team_total | 0.481 | 0.575 | 0.556 | 58 | 43 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ4 | team_total | 0.346 | 0.440 | 0.421 | 45 | 57 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR5 | team_total | 0.328 | 0.425 | 0.405 | 44 | 59 | no | +0.065 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ2 | game_spread | 0.281 | 0.365 | 0.347 | 37 | 64 | no | +0.063 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL3 | game_spread | 0.292 | 0.380 | 0.362 | 39 | 63 | no | +0.061 | OK |
| KXNHLGAME-26NOV07NJNYI-NJ | game_winner | 0.502 | 0.585 | 0.569 | 59 | 42 | no | +0.061 | OK |
| KXNHLGAME-26NOV07NJNYI-NYI | game_winner | 0.498 | 0.415 | 0.431 | 42 | 59 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ3 | team_total | 0.568 | 0.650 | 0.634 | 66 | 36 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR3 | team_total | 0.745 | 0.820 | 0.807 | 83 | 19 | no | +0.054 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ3 | game_spread | 0.165 | 0.240 | 0.223 | 25 | 77 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL5 | team_total | 0.282 | 0.360 | 0.344 | 37 | 65 | no | +0.052 | OK |
| KXNHLGAME-26NOV07CHICAR-CAR | game_winner | 0.738 | 0.805 | 0.793 | 81 | 20 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ2 | team_total | 0.782 | 0.850 | 0.838 | 86 | 16 | no | +0.049 | OK |
| KXNHLTOTAL-26NOV07CHICAR-6 | game_total | 0.534 | 0.605 | 0.591 | 61 | 40 | no | +0.049 | OK |
| KXNHLTOTAL-26NOV07SJDAL-6 | game_total | 0.515 | 0.590 | 0.575 | 60 | 42 | no | +0.048 | OK |
| KXNHLGAME-26NOV07FLAWSH-WSH | game_winner | 0.595 | 0.525 | 0.539 | 53 | 48 | yes | +0.047 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL2 | game_spread | 0.446 | 0.515 | 0.501 | 52 | 49 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA4 | team_total | 0.330 | 0.395 | 0.382 | 40 | 61 | no | +0.043 | OK |
| KXNHLGAME-26NOV07SJDAL-SJ | game_winner | 0.327 | 0.265 | 0.277 | 27 | 74 | yes | +0.043 | OK |
| KXNHLGAME-26NOV07SJDAL-DAL | game_winner | 0.673 | 0.735 | 0.723 | 74 | 27 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ5 | team_total | 0.175 | 0.240 | 0.226 | 25 | 77 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL3 | team_total | 0.695 | 0.765 | 0.752 | 78 | 25 | no | +0.042 | OK |
| KXNHLGAME-26NOV07CHICAR-CHI | game_winner | 0.262 | 0.205 | 0.216 | 21 | 80 | yes | +0.041 | OK |
| KXNHLTOTAL-26NOV07SJDAL-5 | game_total | 0.739 | 0.800 | 0.789 | 81 | 21 | no | +0.039 | OK |
| KXNHLTOTAL-26NOV07CHICAR-7 | game_total | 0.414 | 0.475 | 0.463 | 48 | 53 | no | +0.039 | OK |
| KXNHLGAME-26NOV07FLAWSH-FLA | game_winner | 0.405 | 0.465 | 0.453 | 47 | 54 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR6 | team_total | 0.171 | 0.230 | 0.217 | 24 | 78 | no | +0.037 | OK |
| KXNHLGAME-26NOV07NYRSEA-NYR | game_winner | 0.496 | 0.555 | 0.543 | 56 | 45 | no | +0.036 | OK |
| KXNHLGAME-26NOV07NYRSEA-SEA | game_winner | 0.503 | 0.445 | 0.457 | 45 | 56 | yes | +0.036 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-FLA2 | game_spread | 0.211 | 0.265 | 0.254 | 27 | 74 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-FLA3 | game_spread | 0.116 | 0.170 | 0.158 | 18 | 84 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV07SJDAL-7 | game_total | 0.398 | 0.455 | 0.443 | 46 | 55 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR2 | game_spread | 0.281 | 0.335 | 0.324 | 34 | 67 | no | +0.034 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NYI2 | game_spread | 0.276 | 0.225 | 0.235 | 23 | 78 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA2 | team_total | 0.767 | 0.815 | 0.806 | 82 | 19 | no | +0.032 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL3 | game_spread | 0.263 | 0.315 | 0.304 | 32 | 69 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV07CHICAR-8 | game_total | 0.236 | 0.290 | 0.279 | 30 | 72 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 | team_total | 0.482 | 0.545 | 0.533 | 56 | 47 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-WSH2 | game_spread | 0.375 | 0.325 | 0.335 | 33 | 68 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV07NJNYI-7 | game_total | 0.385 | 0.435 | 0.425 | 44 | 57 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL2 | team_total | 0.866 | 0.910 | 0.902 | 92 | 10 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR2 | team_total | 0.899 | 0.940 | 0.933 | 95 | 7 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV07NJNYI-5 | game_total | 0.721 | 0.770 | 0.761 | 78 | 24 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH3 | team_total | 0.682 | 0.630 | 0.641 | 64 | 38 | yes | +0.026 | OK |
| KXNHLTOTAL-26NOV07CHICAR-5 | game_total | 0.754 | 0.805 | 0.795 | 82 | 21 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA3 | team_total | 0.549 | 0.600 | 0.590 | 61 | 41 | no | +0.024 | OK |
| KXNHLSPREAD-26NOV07PITLA-LA2 | game_spread | 0.349 | 0.305 | 0.313 | 31 | 70 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV07SJDAL-8 | game_total | 0.225 | 0.270 | 0.261 | 28 | 74 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.408 | 0.365 | 0.373 | 37 | 64 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV07MTLTOR-8 | game_total | 0.346 | 0.300 | 0.309 | 31 | 71 | yes | +0.021 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR3 | game_spread | 0.168 | 0.210 | 0.201 | 22 | 80 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.526 | 0.480 | 0.489 | 49 | 53 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH6 | team_total | 0.135 | 0.100 | 0.106 | 11 | 91 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV07CHICAR-4 | game_total | 0.844 | 0.880 | 0.874 | 89 | 13 | no | +0.018 | OK |
| KXNHLGAME-26NOV07VANEDM-EDM | game_winner | 0.730 | 0.765 | 0.758 | 77 | 24 | no | +0.017 | OK |
| KXNHLGAME-26NOV07VANEDM-VAN | game_winner | 0.270 | 0.235 | 0.242 | 24 | 77 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CHI2 | game_spread | 0.113 | 0.085 | 0.090 | 9 | 92 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-SEA2 | game_spread | 0.290 | 0.255 | 0.262 | 26 | 75 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN4 | team_total | 0.311 | 0.265 | 0.274 | 28 | 75 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV07MTLTOR-9 | game_total | 0.259 | 0.215 | 0.223 | 23 | 80 | yes | +0.016 | OK |
| KXNHLGAME-26NOV07PITLA-LA | game_winner | 0.564 | 0.525 | 0.533 | 53 | 48 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV07SJDAL-9 | game_total | 0.154 | 0.185 | 0.178 | 19 | 82 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV07DETCOL-9 | game_total | 0.183 | 0.215 | 0.208 | 22 | 79 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV07SJDAL-4 | game_total | 0.836 | 0.870 | 0.864 | 88 | 14 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT2 | game_spread | 0.241 | 0.275 | 0.268 | 28 | 73 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-SEA4 | team_total | 0.411 | 0.370 | 0.378 | 38 | 64 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV07NJNYI-4 | game_total | 0.816 | 0.850 | 0.844 | 86 | 16 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV07NJNYI-6 | game_total | 0.498 | 0.535 | 0.528 | 54 | 47 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA5 | team_total | 0.165 | 0.205 | 0.196 | 22 | 81 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV07DETCOL-5 | game_total | 0.775 | 0.810 | 0.803 | 82 | 20 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM3 | game_spread | 0.389 | 0.425 | 0.418 | 43 | 58 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH4 | team_total | 0.471 | 0.430 | 0.438 | 44 | 58 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV07STLNSH-10 | game_total | 0.088 | 0.060 | 0.065 | 7 | 95 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07STLNSH-STL6 | team_total | 0.098 | 0.070 | 0.075 | 8 | 94 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL3 | team_total | 0.693 | 0.735 | 0.727 | 75 | 28 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV07NJNYI-8 | game_total | 0.205 | 0.235 | 0.229 | 24 | 77 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN6 | team_total | 0.066 | 0.040 | 0.044 | 5 | 97 | yes | +0.013 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ WSH | 0.595 | 0.578 | 0.168 | 0.220 | 6.32 | 6.43 | 0.938/0.991 | KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA4 +0.029 |
| STL @ NSH | 0.492 | 0.500 | 0.176 | 0.215 | 6.23 | 6.39 | 1.000/0.993 | KXNHLTOTAL-26NOV07STLNSH-7 +0.039 |
| NYR @ SEA | 0.503 | 0.541 | 0.177 | 0.220 | 6.35 | 6.34 | 1.005/0.983 | KXNHLGAME-26NOV07NYRSEA-SEA +0.038 |
| MTL @ TOR | 0.482 | 0.530 | 0.172 | 0.215 | 6.82 | 6.76 | 0.984/0.976 | KXNHLGAME-26NOV07MTLTOR-MTL -0.048 |
| UTA @ OTT | 0.469 | 0.529 | 0.176 | 0.216 | 6.61 | 6.52 | 1.051/0.993 | KXNHLGAME-26NOV07UTAOTT-OTT +0.059 |
| NJD @ NYI | 0.498 | 0.515 | 0.183 | 0.224 | 5.81 | 6.17 | 0.952/0.973 | KXNHLTOTAL-26NOV07NJNYI-7 +0.064 |
| CHI @ CAR | 0.738 | 0.690 | 0.148 | 0.196 | 6.03 | 6.57 | 1.000/1.004 | KXNHLTEAMTOTAL-26NOV07CHICAR-CHI3 +0.107 |
| SJS @ DAL | 0.673 | 0.632 | 0.165 | 0.215 | 5.94 | 6.19 | 0.986/1.027 | KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3 +0.064 |
| TBL @ MIN | 0.441 | 0.470 | 0.173 | 0.218 | 6.36 | 6.35 | 1.033/0.958 | KXNHLGAME-26NOV07TBMIN-TB -0.029 |
| DET @ COL | 0.626 | 0.658 | 0.170 | 0.196 | 6.25 | 6.48 | 0.976/1.015 | KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 +0.054 |
| PIT @ LAK | 0.564 | 0.556 | 0.164 | 0.217 | 6.53 | 6.37 | 0.993/1.021 | KXNHLTOTAL-26NOV07PITLA-6 -0.031 |
| VAN @ EDM | 0.730 | 0.663 | 0.134 | 0.192 | 7.16 | 7.00 | 1.009/1.021 | KXNHLSPREAD-26NOV07VANEDM-EDM2 -0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 40 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2455 (adj 0.2254) · $5.15 · thesis WSH:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 6c · p 0.097 (adj 0.0853) · $1.99 · thesis FLA:OFFENSE_4PLUS
- Alex Ovechkin: 1+ goals YES @ 21c · p 0.2584 (adj 0.2451) · $2.81 · thesis WSH:OFFENSE_4PLUS
- Pierre-Luc Dubois: 1+ goals YES @ 18c · p 0.2252 (adj 0.2102) · $2.29 · thesis WSH:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 16c · p 0.2025 (adj 0.1881) · $2.11 · thesis NSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3036 (adj 0.2902) · $2.2 · thesis NSH:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1501 (adj 0.1313) · $2.36 · thesis SEA:OFFENSE_4PLUS
- New York R wins by over 1.5 goals NO @ 67c · p 0.7527 (adj 0.7088) · $5.82 · thesis SEA:WINS
- Ryan Winterton: 1+ goals YES @ 11c · p 0.142 (adj 0.1315) · $1.43 · thesis SEA:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 66c · p 0.7115 (adj 0.6961) · $5.6 · thesis NYR:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1803 (adj 0.159) · $3.12 · thesis TOR:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 48c · p 0.6416 (adj 0.5301) · $6.7 · thesis MTL:SUPPRESSED
- William Nylander: 2+ goals YES @ 6c · p 0.0849 (adj 0.0762) · $1.16 · thesis TOR:OFFENSE_4PLUS
- Colton Sissons: 1+ goals YES @ 11c · p 0.1463 (adj 0.131) · $1.35 · thesis TOR:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 16c · p 0.2107 (adj 0.1955) · $3.04 · thesis UTA:OFFENSE_4PLUS
- Dylan Cozens: 1+ goals YES @ 24c · p 0.293 (adj 0.2785) · $3.38 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 16c · p 0.2011 (adj 0.1846) · $1.69 · thesis OTT:OFFENSE_4PLUS
- Logan Cooley: 1+ goals NO @ 68c · p 0.7216 (adj 0.71) · $4.94 · thesis UTA:SUPPRESSED
- New Jersey wins by over 1.5 goals NO @ 64c · p 0.7322 (adj 0.6836) · $8.15 · thesis NYI:WINS
- Jean-Gabriel Pageau: 1+ goals YES @ 13c · p 0.1698 (adj 0.1561) · $1.74 · thesis NYI:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 11c · p 0.1435 (adj 0.1326) · $1.97 · thesis NJD:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2539 (adj 0.2404) · $1.91 · thesis NYI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 62c · p 0.7005 (adj 0.6766) · $8.15 · thesis CAR:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 18c · p 0.2346 (adj 0.2197) · $3.52 · thesis CHI:OFFENSE_4PLUS
- Frank Nazar: 1+ goals YES @ 18c · p 0.2256 (adj 0.2117) · $2.51 · thesis CHI:OFFENSE_4PLUS
- Roman Kantserov: 1+ goals YES @ 21c · p 0.2529 (adj 0.2397) · $2.33 · thesis CHI:OFFENSE_4PLUS
- San Jose over 4.5 goals scored YES @ 9c · p 0.1362 (adj 0.1106) · $1.34 · thesis SJS:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 63c · p 0.7168 (adj 0.6684) · $6.41 · thesis GAME:TIGHT
- Ivar Stenberg: 1+ assists NO @ 72c · p 0.8004 (adj 0.7527) · $7.29 · thesis SJS:SUPPRESSED
- Macklin Celebrini: 1+ assists NO @ 53c · p 0.6102 (adj 0.5651) · $4.92 · thesis SJS:SUPPRESSED
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1384 (adj 0.1238) · $2.84 · thesis MIN:OFFENSE_4PLUS
- Blake Coleman: 1+ goals YES @ 19c · p 0.2494 (adj 0.2308) · $3.75 · thesis MIN:OFFENSE_4PLUS
- Bobby Brink: 1+ goals YES @ 14c · p 0.184 (adj 0.168) · $2.27 · thesis MIN:OFFENSE_4PLUS
- Quinn Hughes: 1+ assists NO @ 37c · p 0.4577 (adj 0.4113) · $5.18 · thesis MIN:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 12c · p 0.1586 (adj 0.1464) · $2.04 · thesis PIT:WINS_BY_2PLUS
- Ben Kindel: 1+ goals NO @ 77c · p 0.8093 (adj 0.7982) · $7.66 · thesis PIT:SUPPRESSED
- Edmonton wins by over 1.5 goals NO @ 45c · p 0.5425 (adj 0.4937) · $5.11 · thesis GAME:TIGHT
- Leon Draisaitl: 2+ assists NO @ 73c · p 0.837 (adj 0.761) · $8.15 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3148 (adj 0.3011) · $3.52 · thesis EDM:OFFENSE_4PLUS
- Leon Draisaitl: 1+ goals NO @ 49c · p 0.5325 (adj 0.5181) · $1.14 · thesis EDM:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ WSH** · priced 176/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 27.35, exp saves 23.73 (sd 6.52), pull risk 0.057
- FLA net: Akira Schmid (CONFIRMED) exp shots 26.43, exp saves 22.55 (sd 6.39), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.317 | 0.215 | 22/79 | +0.085 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.316 | 0.215 | 22/79 | +0.084 | STANDARD |
| Alex Ovechkin: 1+ points | 0.492 | 0.405 | 42/61 | +0.055 | STANDARD |
| Brady Tkachuk: 1+ points | 0.510 | 0.595 | 61/42 | +0.053 | STANDARD |
| Aliaksei Protas: 1+ points | 0.459 | 0.375 | 38/63 | +0.063 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.245 | 0.165 | 17/84 | +0.066 | STANDARD |

**STL @ NSH** · priced 157/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.66, exp saves 23.85 (sd 6.6), pull risk 0.066
- STL net: Joel Hofer (PROJECTED) exp shots 27.8, exp saves 24.02 (sd 6.68), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.233 | 0.310 | 33/71 | +0.043 | STANDARD |
| Ross Colton: 1+ points | 0.358 | 0.290 | 31/73 | +0.033 | STANDARD |
| Adam Edstrom: 1+ goals | 0.203 | 0.145 | 16/87 | +0.033 | STANDARD |
| Mason McTavish: 1+ assists | 0.274 | 0.330 | 35/69 | +0.021 | STANDARD |
| Jimmy Snuggerud: 1+ points | 0.584 | 0.530 | 55/49 | +0.016 | STANDARD |
| Ross Colton: 1+ assists | 0.219 | 0.165 | 17/84 | +0.039 | STANDARD |

**NYR @ SEA** · priced 172/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.17, exp saves 23.64 (sd 6.44), pull risk 0.057
- NYR net: Dylan Garand (PROJECTED) exp shots 27.28, exp saves 23.37 (sd 6.57), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ goals | 0.183 | 0.105 | 17/96 | +0.003 | STANDARD |
| Ben Meyers: 1+ goals | 0.150 | 0.075 | 10/95 | +0.044 | STANDARD |
| Bobby McMann: 1+ assists | 0.308 | 0.245 | 25/76 | +0.045 | STANDARD |
| Pavel Dorofeyev: 1+ goals | 0.288 | 0.350 | 36/66 | +0.036 | STANDARD |
| Kaapo Kakko: 1+ points | 0.455 | 0.400 | 42/62 | +0.018 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.370 | 0.315 | 34/71 | +0.014 | STANDARD |

**MTL @ TOR** · priced 160/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 29.0, exp saves 25.15 (sd 6.9), pull risk 0.065
- MTL net: Jacob Fowler (PROJECTED) exp shots 28.71, exp saves 24.69 (sd 6.94), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.358 | 0.530 | 54/48 | +0.144 | STANDARD |
| Easton Cowan: 1+ points | 0.550 | 0.430 | 45/59 | +0.083 | STANDARD |
| Easton Cowan: 1+ assists | 0.393 | 0.290 | 31/73 | +0.068 | STANDARD |
| Nick Suzuki: 1+ points | 0.564 | 0.665 | 69/36 | +0.060 | STANDARD |
| Morgan Rielly: 1+ assists | 0.365 | 0.265 | 29/76 | +0.061 | STANDARD |
| Nick Suzuki: 2+ assists | 0.077 | 0.175 | 19/84 | +0.074 | STANDARD |

**UTA @ OTT** · priced 164/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 26.39, exp saves 22.93 (sd 6.37), pull risk 0.061
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.47, exp saves 23.59 (sd 6.67), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikhail Sergachev: 1+ points | 0.500 | 0.585 | 60/43 | +0.053 | STANDARD |
| Clayton Keller: 1+ assists | 0.443 | 0.515 | 53/50 | +0.040 | STANDARD |
| Michael Amadio: 1+ goals | 0.201 | 0.135 | 16/89 | +0.032 | STANDARD |
| Clayton Keller: 2+ points | 0.219 | 0.285 | 32/75 | +0.018 | STANDARD |
| Jack McBain: 1+ goals | 0.148 | 0.085 | 13/96 | +0.010 | STANDARD |
| Lawson Crouse: 1+ goals | 0.211 | 0.150 | 16/86 | +0.041 | STANDARD |

**NJD @ NYI** · priced 164/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 28.65, exp saves 24.86 (sd 6.65), pull risk 0.059
- NJD net: Jake Allen (PROJECTED) exp shots 26.66, exp saves 23.1 (sd 6.41), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.384 | 0.510 | 52/50 | +0.099 | STANDARD |
| Luke Evangelista: 1+ assists | 0.216 | 0.330 | 34/68 | +0.089 | STANDARD |
| Emil Heineman: 1+ assists | 0.296 | 0.185 | 19/82 | +0.095 | STANDARD |
| Jack Hughes: 2+ points | 0.220 | 0.315 | 33/70 | +0.065 | STANDARD |
| Jack Hughes: 1+ points | 0.577 | 0.665 | 70/37 | +0.037 | STANDARD |
| Nico Hischier: 1+ assists | 0.285 | 0.370 | 39/65 | +0.049 | STANDARD |

**CHI @ CAR** · priced 177/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 21.81, exp saves 19.48 (sd 5.51), pull risk 0.042
- CHI net: Spencer Knight (PROJECTED) exp shots 33.1, exp saves 27.55 (sd 7.66), pull risk 0.106

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.203 | 0.325 | 35/70 | +0.082 | STANDARD |
| Sebastian Aho: 1+ assists | 0.379 | 0.490 | 51/53 | +0.074 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.464 | 0.355 | 36/65 | +0.088 | STANDARD |
| Sebastian Aho: 1+ goals | 0.299 | 0.395 | 41/62 | +0.064 | STANDARD |
| Nikolaj Ehlers: 1+ assists | 0.388 | 0.470 | 49/55 | +0.044 | STANDARD |
| Sebastian Aho: 1+ points | 0.566 | 0.645 | 70/41 | +0.007 | STANDARD |

**SJS @ DAL** · priced 167/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.49, exp saves 21.66 (sd 5.94), pull risk 0.041
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.67, exp saves 23.5 (sd 6.63), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.277 | 0.390 | 41/63 | +0.077 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.478 | 0.585 | 61/44 | +0.065 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.200 | 0.295 | 31/72 | +0.066 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.390 | 0.480 | 49/53 | +0.063 | STANDARD |
| Ivar Stenberg: 1+ points | 0.336 | 0.425 | 45/60 | +0.047 | STANDARD |
| Jason Robertson: 1+ assists | 0.452 | 0.530 | 55/49 | +0.041 | STANDARD |

**TBL @ MIN** · priced 161/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.08, exp saves 24.1 (sd 6.75), pull risk 0.07
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 27.46, exp saves 23.87 (sd 6.53), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Calvin Pickard: 25+ saves | 0.474 | 0.280 | 53/97 | -0.073 |  |
| Nikita Kucherov: 1+ assists | 0.487 | 0.620 | 63/39 | +0.106 | STANDARD |
| Matt Boldy: 1+ assists | 0.359 | 0.485 | 49/52 | +0.104 | STANDARD |
| Bobby Brink: 1+ points | 0.419 | 0.310 | 34/72 | +0.063 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.383 | 0.485 | 50/53 | +0.069 | STANDARD |
| Bobby Brink: 1+ assists | 0.291 | 0.190 | 20/82 | +0.080 | STANDARD |

**DET @ COL** · priced 177/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.53, exp saves 23.53 (sd 6.32), pull risk 0.044
- DET net: Daniil Tarasov (PROJECTED) exp shots 30.11, exp saves 25.24 (sd 7.1), pull risk 0.099

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lucas Raymond: 1+ assists | 0.318 | 0.405 | 43/62 | +0.046 | STANDARD |
| Lucas Raymond: 1+ points | 0.491 | 0.565 | 60/47 | +0.021 | STANDARD |
| Sheldon Dries: 1+ goals | 0.107 | 0.045 | 8/99 | +0.022 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.372 | 0.430 | 45/59 | +0.021 | STANDARD |
| Artturi Lehkonen: 1+ assists | 0.330 | 0.275 | 28/73 | +0.036 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.166 | 0.220 | 24/80 | +0.023 | STANDARD |

**PIT @ LAK** · priced 164/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.28, exp saves 23.7 (sd 6.48), pull risk 0.055
- PIT net: Sergei Murashov (PROJECTED) exp shots 27.6, exp saves 23.54 (sd 6.64), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 2+ points | 0.246 | 0.340 | 35/67 | +0.069 | STANDARD |
| Artemi Panarin: 1+ assists | 0.434 | 0.515 | 53/50 | +0.048 | STANDARD |
| Ben Kindel: 1+ points | 0.386 | 0.455 | 47/56 | +0.037 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.258 | 0.190 | 20/82 | +0.047 | STANDARD |
| Trevor Moore: 1+ points | 0.432 | 0.365 | 39/66 | +0.025 | STANDARD |
| Artemi Panarin: 1+ points | 0.608 | 0.670 | 72/38 | -0.004 | STANDARD |

**VAN @ EDM** · priced 165/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 24.17, exp saves 21.32 (sd 5.94), pull risk 0.05
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.14, exp saves 25.13 (sd 7.25), pull risk 0.109

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#25): 1+ goals | 0.060 | 0.490 | 97/99 | -0.050 | STANDARD |
| Elias Pettersson (#40): 1+ points | 0.517 | 0.280 | 54/98 | -0.040 | STANDARD |
| Connor McDavid: 2+ points | 0.471 | 0.640 | 65/37 | +0.142 | STANDARD |
| Connor McDavid: 2+ assists | 0.237 | 0.405 | 43/62 | +0.126 | STANDARD |
| Leon Draisaitl: 2+ points | 0.391 | 0.545 | 56/47 | +0.121 | STANDARD |
| Jake DeBrusk: 1+ goals | 0.312 | 0.165 | 29/96 | +0.008 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
