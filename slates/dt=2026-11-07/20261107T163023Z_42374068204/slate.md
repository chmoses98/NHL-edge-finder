# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-07T16:30:23Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4365 · contracts joined: 2687 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2387, 'OK': 154, 'NO_EDGE': 146}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 385, 'game_early_goal': 12, 'first_goal': 430, 'game_winner': 24, 'player_goals': 742, 'game_overtime': 12, 'player_points': 515, 'goalie_saves': 3, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ WSH | 2026-11-07T17:30:00Z | T-30m | 0.595 | 0.405 | 0.168 | 6.32 | 3.47 | 2.85 | 235 (25/210) | CONFIRMED/CONFIRMED |
| STL @ NSH | 2026-11-07T18:00:00Z | T-60m | 0.492 | 0.508 | 0.176 | 6.23 | 3.08 | 3.15 | 212 (25/187) | PROJECTED/PROJECTED |
| NYR @ SEA | 2026-11-07T22:00:00Z | T-3h | 0.503 | 0.496 | 0.177 | 6.35 | 3.19 | 3.16 | 224 (25/199) | PROJECTED/PROJECTED |
| MTL @ TOR | 2026-11-08T00:00:00Z | T-6h | 0.478 | 0.522 | 0.170 | 6.84 | 3.34 | 3.50 | 215 (25/190) | CONFIRMED/PROJECTED |
| UTA @ OTT | 2026-11-08T00:00:00Z | T-6h | 0.446 | 0.554 | 0.163 | 6.70 | 3.18 | 3.52 | 224 (25/199) | CONFIRMED/PROJECTED |
| NJD @ NYI | 2026-11-08T00:00:00Z | T-6h | 0.498 | 0.502 | 0.183 | 5.81 | 2.89 | 2.92 | 218 (25/193) | PROBABLE/PROJECTED |
| CHI @ CAR | 2026-11-08T01:00:00Z | T-6h | 0.737 | 0.263 | 0.151 | 6.02 | 3.77 | 2.24 | 228 (25/203) | PROBABLE/PROBABLE |
| SJS @ DAL | 2026-11-08T01:00:00Z | T-6h | 0.673 | 0.327 | 0.165 | 5.94 | 3.52 | 2.42 | 224 (25/199) | PROJECTED/PROJECTED |
| TBL @ MIN | 2026-11-08T01:00:00Z | T-6h | 0.441 | 0.559 | 0.173 | 6.36 | 3.01 | 3.35 | 224 (25/199) | CONFIRMED/PROJECTED |
| DET @ COL | 2026-11-08T02:00:00Z | T-6h | 0.626 | 0.374 | 0.170 | 6.25 | 3.53 | 2.72 | 237 (25/212) | PROJECTED/PROJECTED |
| PIT @ LAK | 2026-11-08T02:00:00Z | T-6h | 0.564 | 0.436 | 0.164 | 6.53 | 3.46 | 3.07 | 219 (25/194) | PROJECTED/PROJECTED |
| VAN @ EDM | 2026-11-08T03:00:00Z | T-6h | 0.730 | 0.270 | 0.134 | 7.16 | 4.38 | 2.78 | 227 (25/202) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV07CHICAR-CAR3 | game_spread | 0.361 | 0.465 | 0.444 | 47 | 54 | no | +0.082 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CAR2 | game_spread | 0.512 | 0.615 | 0.595 | 62 | 39 | no | +0.081 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR4 | team_total | 0.536 | 0.640 | 0.620 | 65 | 37 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4 | team_total | 0.481 | 0.575 | 0.556 | 58 | 43 | no | +0.072 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL3 | game_spread | 0.292 | 0.385 | 0.366 | 39 | 62 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ4 | team_total | 0.346 | 0.445 | 0.425 | 46 | 57 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR5 | team_total | 0.330 | 0.415 | 0.397 | 42 | 59 | no | +0.063 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ2 | game_spread | 0.281 | 0.365 | 0.347 | 37 | 64 | no | +0.063 | OK |
| KXNHLGAME-26NOV07NJNYI-NJ | game_winner | 0.502 | 0.585 | 0.569 | 59 | 42 | no | +0.061 | OK |
| KXNHLGAME-26NOV07NJNYI-NYI | game_winner | 0.498 | 0.415 | 0.431 | 42 | 59 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ3 | team_total | 0.568 | 0.645 | 0.630 | 65 | 36 | no | +0.056 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ3 | game_spread | 0.165 | 0.235 | 0.219 | 24 | 77 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL5 | team_total | 0.282 | 0.360 | 0.344 | 37 | 65 | no | +0.052 | OK |
| KXNHLGAME-26NOV07CHICAR-CAR | game_winner | 0.737 | 0.805 | 0.793 | 81 | 20 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ2 | team_total | 0.782 | 0.850 | 0.838 | 86 | 16 | no | +0.049 | OK |
| KXNHLTOTAL-26NOV07SJDAL-6 | game_total | 0.515 | 0.590 | 0.575 | 60 | 42 | no | +0.048 | OK |
| KXNHLGAME-26NOV07FLAWSH-WSH | game_winner | 0.595 | 0.525 | 0.539 | 53 | 48 | yes | +0.047 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL2 | game_spread | 0.446 | 0.515 | 0.501 | 52 | 49 | no | +0.046 | OK |
| KXNHLGAME-26NOV07SJDAL-SJ | game_winner | 0.327 | 0.265 | 0.277 | 27 | 74 | yes | +0.043 | OK |
| KXNHLGAME-26NOV07SJDAL-DAL | game_winner | 0.673 | 0.735 | 0.723 | 74 | 27 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ5 | team_total | 0.175 | 0.240 | 0.226 | 25 | 77 | no | +0.042 | OK |
| KXNHLGAME-26NOV07CHICAR-CHI | game_winner | 0.263 | 0.205 | 0.216 | 21 | 80 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR6 | team_total | 0.168 | 0.230 | 0.216 | 24 | 78 | no | +0.040 | OK |
| KXNHLTOTAL-26NOV07SJDAL-5 | game_total | 0.739 | 0.800 | 0.789 | 81 | 21 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH6 | team_total | 0.135 | 0.070 | 0.080 | 9 | 95 | yes | +0.039 | OK |
| KXNHLGAME-26NOV07FLAWSH-FLA | game_winner | 0.405 | 0.465 | 0.453 | 47 | 54 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV07CHICAR-6 | game_total | 0.537 | 0.600 | 0.588 | 61 | 41 | no | +0.037 | OK |
| KXNHLGAME-26NOV07NYRSEA-NYR | game_winner | 0.496 | 0.555 | 0.543 | 56 | 45 | no | +0.036 | OK |
| KXNHLGAME-26NOV07NYRSEA-SEA | game_winner | 0.503 | 0.445 | 0.457 | 45 | 56 | yes | +0.036 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-FLA2 | game_spread | 0.211 | 0.265 | 0.254 | 27 | 74 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-FLA3 | game_spread | 0.116 | 0.165 | 0.154 | 17 | 84 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV07SJDAL-7 | game_total | 0.398 | 0.455 | 0.443 | 46 | 55 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR2 | game_spread | 0.281 | 0.335 | 0.324 | 34 | 67 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA4 | team_total | 0.330 | 0.385 | 0.374 | 39 | 62 | no | +0.034 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NYI2 | game_spread | 0.276 | 0.225 | 0.235 | 23 | 78 | yes | +0.033 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL3 | game_spread | 0.263 | 0.320 | 0.308 | 33 | 69 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL3 | team_total | 0.695 | 0.760 | 0.748 | 78 | 26 | no | +0.032 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR3 | game_spread | 0.168 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR2 | team_total | 0.896 | 0.945 | 0.937 | 96 | 7 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-WSH2 | game_spread | 0.375 | 0.325 | 0.335 | 33 | 68 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV07NJNYI-7 | game_total | 0.385 | 0.435 | 0.425 | 44 | 57 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV07MTLTOR-8 | game_total | 0.353 | 0.305 | 0.314 | 31 | 70 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV07UTAOTT-8 | game_total | 0.332 | 0.285 | 0.294 | 29 | 72 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL2 | team_total | 0.866 | 0.910 | 0.902 | 92 | 10 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV07CHICAR-7 | game_total | 0.415 | 0.465 | 0.455 | 47 | 54 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-SEA2 | game_spread | 0.290 | 0.245 | 0.254 | 25 | 76 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV07NJNYI-5 | game_total | 0.721 | 0.770 | 0.761 | 78 | 24 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV07SJDAL-4 | game_total | 0.836 | 0.880 | 0.872 | 89 | 13 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH3 | team_total | 0.682 | 0.630 | 0.641 | 64 | 38 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH5 | team_total | 0.276 | 0.235 | 0.243 | 24 | 77 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV07CHICAR-4 | game_total | 0.839 | 0.885 | 0.877 | 90 | 13 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL5 | team_total | 0.282 | 0.330 | 0.320 | 34 | 68 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA2 | team_total | 0.767 | 0.810 | 0.802 | 82 | 20 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV07MTLTOR-10 | game_total | 0.138 | 0.105 | 0.111 | 11 | 90 | yes | +0.022 | OK |
| KXNHLTOTAL-26NOV07SJDAL-8 | game_total | 0.225 | 0.270 | 0.261 | 28 | 74 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.408 | 0.365 | 0.373 | 37 | 64 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV07CHICAR-5 | game_total | 0.748 | 0.795 | 0.786 | 81 | 22 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 | team_total | 0.482 | 0.530 | 0.521 | 54 | 48 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV07CHICAR-8 | game_total | 0.236 | 0.280 | 0.271 | 29 | 73 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN5 | team_total | 0.157 | 0.115 | 0.122 | 13 | 90 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV07STLNSH-9 | game_total | 0.188 | 0.155 | 0.161 | 16 | 85 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.526 | 0.470 | 0.481 | 49 | 55 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV07STLNSH-8 | game_total | 0.261 | 0.220 | 0.228 | 23 | 79 | yes | +0.018 | OK |
| KXNHLGAME-26NOV07DETCOL-COL | game_winner | 0.626 | 0.665 | 0.657 | 67 | 34 | no | +0.018 | OK |
| KXNHLGAME-26NOV07DETCOL-DET | game_winner | 0.374 | 0.335 | 0.343 | 34 | 67 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV07MTLTOR-9 | game_total | 0.260 | 0.220 | 0.228 | 23 | 79 | yes | +0.018 | OK |
| KXNHLGAME-26NOV07VANEDM-EDM | game_winner | 0.730 | 0.765 | 0.758 | 77 | 24 | no | +0.017 | OK |
| KXNHLGAME-26NOV07VANEDM-VAN | game_winner | 0.270 | 0.235 | 0.242 | 24 | 77 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN4 | team_total | 0.311 | 0.265 | 0.274 | 28 | 75 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV07MTLTOR-MTL6 | team_total | 0.143 | 0.110 | 0.116 | 12 | 90 | yes | +0.016 | OK |
| KXNHLGAME-26NOV07PITLA-LA | game_winner | 0.564 | 0.525 | 0.533 | 53 | 48 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV07SJDAL-9 | game_total | 0.154 | 0.185 | 0.178 | 19 | 82 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT2 | game_spread | 0.241 | 0.275 | 0.268 | 28 | 73 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-SEA4 | team_total | 0.411 | 0.370 | 0.378 | 38 | 64 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV07NJNYI-4 | game_total | 0.816 | 0.850 | 0.844 | 86 | 16 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV07NJNYI-6 | game_total | 0.498 | 0.535 | 0.528 | 54 | 47 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA3 | team_total | 0.549 | 0.590 | 0.582 | 60 | 42 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV07DETCOL-5 | game_total | 0.775 | 0.810 | 0.803 | 82 | 20 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM3 | game_spread | 0.389 | 0.425 | 0.418 | 43 | 58 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH4 | team_total | 0.471 | 0.430 | 0.438 | 44 | 58 | yes | +0.013 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ WSH | 0.595 | 0.578 | 0.168 | 0.220 | 6.32 | 6.43 | 0.938/0.991 | KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA4 +0.029 |
| STL @ NSH | 0.492 | 0.500 | 0.176 | 0.215 | 6.23 | 6.39 | 1.000/0.993 | KXNHLTOTAL-26NOV07STLNSH-7 +0.039 |
| NYR @ SEA | 0.503 | 0.541 | 0.177 | 0.220 | 6.35 | 6.34 | 1.005/0.983 | KXNHLGAME-26NOV07NYRSEA-SEA +0.038 |
| MTL @ TOR | 0.478 | 0.533 | 0.170 | 0.208 | 6.84 | 6.76 | 0.988/0.976 | KXNHLGAME-26NOV07MTLTOR-TOR +0.055 |
| UTA @ OTT | 0.446 | 0.521 | 0.163 | 0.213 | 6.70 | 6.58 | 1.071/0.993 | KXNHLGAME-26NOV07UTAOTT-OTT +0.074 |
| NJD @ NYI | 0.498 | 0.515 | 0.183 | 0.224 | 5.81 | 6.17 | 0.952/0.973 | KXNHLTOTAL-26NOV07NJNYI-7 +0.064 |
| CHI @ CAR | 0.737 | 0.685 | 0.151 | 0.193 | 6.02 | 6.53 | 1.000/0.995 | KXNHLTEAMTOTAL-26NOV07CHICAR-CHI3 +0.106 |
| SJS @ DAL | 0.673 | 0.632 | 0.165 | 0.215 | 5.94 | 6.19 | 0.986/1.027 | KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3 +0.064 |
| TBL @ MIN | 0.441 | 0.470 | 0.173 | 0.218 | 6.36 | 6.35 | 1.033/0.958 | KXNHLGAME-26NOV07TBMIN-TB -0.029 |
| DET @ COL | 0.626 | 0.658 | 0.170 | 0.196 | 6.25 | 6.48 | 0.976/1.015 | KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 +0.054 |
| PIT @ LAK | 0.564 | 0.556 | 0.164 | 0.217 | 6.53 | 6.37 | 0.993/1.021 | KXNHLTOTAL-26NOV07PITLA-6 -0.031 |
| VAN @ EDM | 0.730 | 0.663 | 0.134 | 0.192 | 7.16 | 7.00 | 1.009/1.021 | KXNHLSPREAD-26NOV07VANEDM-EDM2 -0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 41 recommended · full analysis in card.md / packet.json `thesis_card`

- Anton Lundell: First Goalscorer YES @ 1c · p 0.0322 (adj 0.0361) · $2.55 · thesis FLA:SCORES_FIRST
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2455 (adj 0.2279) · $5.06 · thesis WSH:OFFENSE_4PLUS
- Pierre-Luc Dubois: 1+ goals YES @ 17c · p 0.2252 (adj 0.2102) · $4.12 · thesis WSH:OFFENSE_4PLUS
- Sandis Vilmanis: 1+ goals YES @ 13c · p 0.167 (adj 0.1565) · $2.59 · thesis FLA:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 15c · p 0.2025 (adj 0.1881) · $3.72 · thesis NSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 25c · p 0.3036 (adj 0.2889) · $3.81 · thesis NSH:OFFENSE_4PLUS
- Justin Barron: 1+ goals YES @ 5c · p 0.0717 (adj 0.0663) · $1.43 · thesis STL:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 12c · p 0.1505 (adj 0.1416) · $1.86 · thesis STL:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 9c · p 0.1501 (adj 0.1326) · $3.98 · thesis SEA:OFFENSE_4PLUS
- New York R wins by over 1.5 goals NO @ 67c · p 0.7527 (adj 0.7088) · $6.06 · thesis SEA:WINS
- Pavel Dorofeyev: 1+ goals NO @ 66c · p 0.7115 (adj 0.6961) · $6.39 · thesis NYR:SUPPRESSED
- Jani Nyman: 1+ goals YES @ 12c · p 0.1535 (adj 0.1414) · $1.58 · thesis SEA:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1659 (adj 0.1469) · $2.29 · thesis TOR:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 48c · p 0.6249 (adj 0.5242) · $6.35 · thesis MTL:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 16c · p 0.2123 (adj 0.198) · $3.75 · thesis UTA:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 16c · p 0.2013 (adj 0.1872) · $2.35 · thesis OTT:OFFENSE_4PLUS
- Dylan Cozens: 1+ goals YES @ 25c · p 0.2979 (adj 0.2834) · $3.1 · thesis OTT:OFFENSE_4PLUS
- Fabian Zetterlund: 1+ goals YES @ 20c · p 0.2399 (adj 0.2249) · $1.89 · thesis OTT:OFFENSE_4PLUS
- New Jersey wins by over 1.5 goals NO @ 64c · p 0.7322 (adj 0.6836) · $9.31 · thesis NYI:WINS
- Jean-Gabriel Pageau: 1+ goals YES @ 13c · p 0.1698 (adj 0.1548) · $1.82 · thesis NYI:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 11c · p 0.1435 (adj 0.1326) · $2.25 · thesis NJD:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2539 (adj 0.2404) · $2.19 · thesis NYI:OFFENSE_4PLUS
- Dillon Boucher: 1+ goals YES @ 5c · p 0.0895 (adj 0.0771) · $2.39 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 62c · p 0.7034 (adj 0.6813) · $9.31 · thesis CAR:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 18c · p 0.243 (adj 0.2223) · $4.21 · thesis CHI:OFFENSE_4PLUS
- Anton Frondell: 1+ goals YES @ 18c · p 0.2199 (adj 0.2087) · $2.41 · thesis CHI:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 72c · p 0.8004 (adj 0.7527) · $9.31 · thesis SJS:SUPPRESSED
- Dallas over 3.5 goals scored NO @ 43c · p 0.5007 (adj 0.4629) · $1.29 · thesis DAL:SUPPRESSED
- Dallas wins by over 2.5 goals NO @ 62c · p 0.7168 (adj 0.6506) · $4.39 · thesis GAME:TIGHT
- Wyatt Johnston: 1+ goals NO @ 60c · p 0.6414 (adj 0.6285) · $2.59 · thesis DAL:SUPPRESSED
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1384 (adj 0.1238) · $3.25 · thesis MIN:OFFENSE_4PLUS
- Blake Coleman: 1+ goals YES @ 19c · p 0.2494 (adj 0.2308) · $4.28 · thesis MIN:OFFENSE_4PLUS
- Bobby Brink: 1+ goals YES @ 14c · p 0.184 (adj 0.1705) · $2.94 · thesis MIN:OFFENSE_4PLUS
- Quinn Hughes: 1+ assists NO @ 37c · p 0.4577 (adj 0.4113) · $5.96 · thesis MIN:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 12c · p 0.1586 (adj 0.1477) · $2.47 · thesis PIT:WINS_BY_2PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.124 (adj 0.1118) · $1.87 · thesis PIT:WINS_BY_2PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0756 (adj 0.0642) · $1.14 · thesis LAK:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 13c · p 0.1672 (adj 0.1566) · $2.01 · thesis VAN:OFFENSE_4PLUS
- Edmonton wins by over 1.5 goals NO @ 45c · p 0.5425 (adj 0.4937) · $3.75 · thesis GAME:TIGHT
- Edmonton wins by over 2.5 goals NO @ 58c · p 0.6695 (adj 0.6222) · $4.41 · thesis GAME:TIGHT
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3148 (adj 0.3011) · $3.58 · thesis EDM:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ WSH** · priced 177/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 27.35, exp saves 23.73 (sd 6.52), pull risk 0.057
- FLA net: Akira Schmid (CONFIRMED) exp shots 26.43, exp saves 22.55 (sd 6.39), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.317 | 0.215 | 22/79 | +0.085 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.316 | 0.215 | 22/79 | +0.084 | STANDARD |
| Aliaksei Protas: 1+ points | 0.459 | 0.375 | 38/63 | +0.063 | STANDARD |
| Alex Ovechkin: 1+ points | 0.492 | 0.410 | 42/60 | +0.055 | STANDARD |
| Sam Reinhart: 1+ points | 0.515 | 0.595 | 61/42 | +0.048 | STANDARD |
| Brady Tkachuk: 1+ points | 0.510 | 0.590 | 60/42 | +0.053 | STANDARD |

**STL @ NSH** · priced 157/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.66, exp saves 23.85 (sd 6.6), pull risk 0.066
- STL net: Joel Hofer (PROJECTED) exp shots 27.8, exp saves 24.02 (sd 6.68), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.233 | 0.315 | 33/70 | +0.052 | STANDARD |
| Ross Colton: 1+ points | 0.358 | 0.290 | 31/73 | +0.033 | STANDARD |
| Mason McTavish: 1+ assists | 0.274 | 0.340 | 35/67 | +0.041 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.304 | 0.245 | 25/76 | +0.040 | STANDARD |
| Adam Edstrom: 1+ goals | 0.203 | 0.145 | 15/86 | +0.044 | STANDARD |
| Ross Colton: 1+ assists | 0.219 | 0.165 | 17/84 | +0.039 | STANDARD |

**NYR @ SEA** · priced 172/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.17, exp saves 23.64 (sd 6.44), pull risk 0.057
- NYR net: Dylan Garand (PROJECTED) exp shots 27.28, exp saves 23.37 (sd 6.57), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ goals | 0.183 | 0.105 | 17/96 | +0.003 | STANDARD |
| Ben Meyers: 1+ goals | 0.150 | 0.080 | 9/93 | +0.054 | STANDARD |
| Bobby McMann: 1+ assists | 0.308 | 0.245 | 25/76 | +0.045 | STANDARD |
| Pavel Dorofeyev: 1+ goals | 0.288 | 0.350 | 36/66 | +0.036 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.370 | 0.310 | 33/71 | +0.024 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.315 | 0.255 | 27/76 | +0.031 | STANDARD |

**MTL @ TOR** · priced 163/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 29.0, exp saves 25.09 (sd 6.91), pull risk 0.07
- MTL net: Jacob Fowler (PROJECTED) exp shots 28.71, exp saves 24.69 (sd 6.91), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.375 | 0.530 | 54/48 | +0.127 | STANDARD |
| Nick Suzuki: 1+ points | 0.570 | 0.670 | 69/35 | +0.064 | STANDARD |
| Nick Suzuki: 2+ points | 0.206 | 0.305 | 34/73 | +0.050 | STANDARD |
| Morgan Rielly: 1+ assists | 0.353 | 0.265 | 29/76 | +0.049 | STANDARD |
| Easton Cowan: 1+ points | 0.516 | 0.430 | 45/59 | +0.049 | STANDARD |
| Morgan Rielly: 1+ points | 0.407 | 0.325 | 35/70 | +0.041 | STANDARD |

**UTA @ OTT** · priced 167/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (CONFIRMED) exp shots 26.39, exp saves 22.89 (sd 6.44), pull risk 0.067
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.47, exp saves 23.56 (sd 6.6), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Fabian Zetterlund: 1+ assists | 0.307 | 0.215 | 24/81 | +0.055 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.474 | 0.385 | 41/64 | +0.047 | STANDARD |
| Mikhail Sergachev: 1+ points | 0.506 | 0.590 | 61/43 | +0.047 | STANDARD |
| Clayton Keller: 1+ points | 0.588 | 0.660 | 68/36 | +0.036 | STANDARD |
| Clayton Keller: 1+ assists | 0.452 | 0.520 | 54/50 | +0.031 | STANDARD |
| Jack McBain: 1+ goals | 0.153 | 0.085 | 12/95 | +0.026 | STANDARD |

**NJD @ NYI** · priced 164/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 28.65, exp saves 24.86 (sd 6.65), pull risk 0.059
- NJD net: Jake Allen (PROJECTED) exp shots 26.66, exp saves 23.1 (sd 6.41), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.384 | 0.510 | 52/50 | +0.099 | STANDARD |
| Luke Evangelista: 1+ assists | 0.216 | 0.330 | 34/68 | +0.089 | STANDARD |
| Emil Heineman: 1+ assists | 0.296 | 0.185 | 19/82 | +0.095 | STANDARD |
| Jack Hughes: 2+ points | 0.220 | 0.325 | 34/69 | +0.075 | STANDARD |
| Jack Hughes: 1+ points | 0.577 | 0.665 | 70/37 | +0.037 | STANDARD |
| Emil Heineman: 1+ points | 0.426 | 0.345 | 37/68 | +0.040 | STANDARD |

**CHI @ CAR** · priced 176/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 21.81, exp saves 19.44 (sd 5.57), pull risk 0.045
- CHI net: Spencer Knight (PROBABLE) exp shots 33.1, exp saves 27.69 (sd 7.63), pull risk 0.097

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.204 | 0.315 | 33/70 | +0.081 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.465 | 0.355 | 36/65 | +0.089 | STANDARD |
| Sebastian Aho: 1+ assists | 0.380 | 0.490 | 51/53 | +0.073 | STANDARD |
| Sebastian Aho: 1+ points | 0.561 | 0.650 | 69/39 | +0.032 | STANDARD |
| Sebastian Aho: 1+ goals | 0.297 | 0.385 | 39/62 | +0.067 | STANDARD |
| Nikolaj Ehlers: 1+ assists | 0.392 | 0.480 | 49/53 | +0.060 | STANDARD |

**SJS @ DAL** · priced 170/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.49, exp saves 21.66 (sd 5.94), pull risk 0.041
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.67, exp saves 23.5 (sd 6.63), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.277 | 0.390 | 41/63 | +0.077 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.478 | 0.585 | 61/44 | +0.065 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.200 | 0.295 | 31/72 | +0.066 | STANDARD |
| Ivar Stenberg: 1+ points | 0.336 | 0.425 | 45/60 | +0.047 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.390 | 0.460 | 48/56 | +0.033 | STANDARD |
| Jason Robertson: 1+ assists | 0.452 | 0.520 | 55/51 | +0.021 | STANDARD |

**TBL @ MIN** · priced 161/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.08, exp saves 24.1 (sd 6.75), pull risk 0.07
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 27.46, exp saves 23.87 (sd 6.53), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Calvin Pickard: 25+ saves | 0.474 | 0.315 | 50/87 | -0.043 |  |
| Nikita Kucherov: 1+ assists | 0.487 | 0.620 | 63/39 | +0.106 | STANDARD |
| Matt Boldy: 1+ assists | 0.359 | 0.485 | 49/52 | +0.104 | STANDARD |
| Bobby Brink: 1+ points | 0.419 | 0.315 | 34/71 | +0.063 | STANDARD |
| Bobby Brink: 1+ assists | 0.291 | 0.190 | 20/82 | +0.080 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.383 | 0.480 | 49/53 | +0.069 | STANDARD |

**DET @ COL** · priced 177/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.53, exp saves 23.53 (sd 6.32), pull risk 0.044
- DET net: Daniil Tarasov (PROJECTED) exp shots 30.11, exp saves 25.24 (sd 7.1), pull risk 0.099

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lucas Raymond: 1+ assists | 0.318 | 0.405 | 43/62 | +0.046 | STANDARD |
| Sam Malinski: 1+ points | 0.386 | 0.300 | 32/72 | +0.050 | STANDARD |
| Sam Malinski: 1+ assists | 0.325 | 0.240 | 26/78 | +0.051 | STANDARD |
| Lucas Raymond: 1+ points | 0.491 | 0.565 | 60/47 | +0.021 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.372 | 0.440 | 46/58 | +0.030 | STANDARD |
| Artturi Lehkonen: 1+ assists | 0.330 | 0.270 | 28/74 | +0.036 | STANDARD |

**PIT @ LAK** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.28, exp saves 23.7 (sd 6.48), pull risk 0.055
- PIT net: Sergei Murashov (PROJECTED) exp shots 27.6, exp saves 23.54 (sd 6.64), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 2+ points | 0.246 | 0.340 | 35/67 | +0.069 | STANDARD |
| Artemi Panarin: 1+ assists | 0.434 | 0.525 | 53/48 | +0.068 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.258 | 0.185 | 20/83 | +0.047 | STANDARD |
| Artemi Panarin: 2+ assists | 0.105 | 0.175 | 19/84 | +0.045 | STANDARD |
| Ben Kindel: 1+ points | 0.386 | 0.455 | 47/56 | +0.037 | STANDARD |
| Trevor Moore: 1+ points | 0.432 | 0.365 | 39/66 | +0.025 | STANDARD |

**VAN @ EDM** · priced 168/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 24.17, exp saves 21.32 (sd 5.94), pull risk 0.05
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.14, exp saves 25.13 (sd 7.25), pull risk 0.109

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#25): 1+ goals | 0.060 | 0.425 | 84/99 | -0.050 | STANDARD |
| Connor McDavid: 2+ points | 0.471 | 0.650 | 67/37 | +0.142 | STANDARD |
| Connor McDavid: 2+ assists | 0.237 | 0.410 | 43/61 | +0.136 | STANDARD |
| Leon Draisaitl: 2+ points | 0.391 | 0.545 | 56/47 | +0.121 | STANDARD |
| Connor McDavid: 3+ points | 0.217 | 0.345 | 37/68 | +0.088 | STANDARD |
| Leon Draisaitl: 3+ points | 0.154 | 0.275 | 30/75 | +0.083 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
