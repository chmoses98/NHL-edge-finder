# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-07T17:21:32Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4365 · contracts joined: 2687 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2387, 'OK': 154, 'NO_EDGE': 146}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 384, 'game_early_goal': 12, 'first_goal': 429, 'game_winner': 24, 'player_goals': 739, 'game_overtime': 12, 'player_points': 513, 'goalie_saves': 10, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ WSH | 2026-11-07T17:30:00Z | T-<10m | 0.595 | 0.405 | 0.168 | 6.32 | 3.47 | 2.85 | 229 (25/204) | CONFIRMED/CONFIRMED |
| STL @ NSH | 2026-11-07T18:00:00Z | T-30m | 0.477 | 0.523 | 0.179 | 6.16 | 3.01 | 3.15 | 213 (25/188) | PROJECTED/CONFIRMED |
| NYR @ SEA | 2026-11-07T22:00:00Z | T-3h | 0.503 | 0.496 | 0.177 | 6.35 | 3.19 | 3.16 | 224 (25/199) | PROJECTED/PROJECTED |
| MTL @ TOR | 2026-11-08T00:00:00Z | T-6h | 0.459 | 0.541 | 0.165 | 6.72 | 3.22 | 3.50 | 216 (25/191) | CONFIRMED/CONFIRMED |
| UTA @ OTT | 2026-11-08T00:00:00Z | T-6h | 0.446 | 0.554 | 0.163 | 6.70 | 3.18 | 3.52 | 224 (25/199) | CONFIRMED/PROJECTED |
| NJD @ NYI | 2026-11-08T00:00:00Z | T-6h | 0.496 | 0.504 | 0.179 | 5.80 | 2.89 | 2.92 | 220 (25/195) | PROBABLE/PROBABLE |
| CHI @ CAR | 2026-11-08T01:00:00Z | T-6h | 0.737 | 0.263 | 0.151 | 6.02 | 3.77 | 2.24 | 234 (25/209) | PROBABLE/PROBABLE |
| SJS @ DAL | 2026-11-08T01:00:00Z | T-6h | 0.679 | 0.321 | 0.165 | 5.93 | 3.52 | 2.40 | 226 (25/201) | PROBABLE/PROJECTED |
| TBL @ MIN | 2026-11-08T01:00:00Z | T-6h | 0.441 | 0.559 | 0.173 | 6.36 | 3.01 | 3.35 | 224 (25/199) | CONFIRMED/PROJECTED |
| DET @ COL | 2026-11-08T02:00:00Z | T-6h | 0.626 | 0.374 | 0.170 | 6.25 | 3.53 | 2.72 | 237 (25/212) | PROJECTED/PROJECTED |
| PIT @ LAK | 2026-11-08T02:00:00Z | T-6h | 0.564 | 0.436 | 0.164 | 6.53 | 3.46 | 3.07 | 219 (25/194) | PROJECTED/PROJECTED |
| VAN @ EDM | 2026-11-08T03:00:00Z | T-6h | 0.730 | 0.270 | 0.134 | 7.16 | 4.38 | 2.78 | 221 (25/196) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV07CHICAR-CAR3 | game_spread | 0.361 | 0.465 | 0.444 | 47 | 54 | no | +0.082 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CAR2 | game_spread | 0.512 | 0.605 | 0.587 | 61 | 40 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4 | team_total | 0.485 | 0.575 | 0.557 | 58 | 43 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR4 | team_total | 0.536 | 0.630 | 0.612 | 64 | 38 | no | +0.067 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL3 | game_spread | 0.296 | 0.385 | 0.366 | 39 | 62 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ4 | team_total | 0.347 | 0.440 | 0.421 | 45 | 57 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR5 | team_total | 0.330 | 0.415 | 0.397 | 42 | 59 | no | +0.063 | OK |
| KXNHLGAME-26NOV07NJNYI-NJ | game_winner | 0.504 | 0.585 | 0.569 | 59 | 42 | no | +0.059 | OK |
| KXNHLGAME-26NOV07NJNYI-NYI | game_winner | 0.496 | 0.415 | 0.431 | 42 | 59 | yes | +0.059 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ3 | game_spread | 0.165 | 0.235 | 0.219 | 24 | 77 | no | +0.053 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ2 | game_spread | 0.282 | 0.355 | 0.340 | 36 | 65 | no | +0.052 | OK |
| KXNHLGAME-26NOV07CHICAR-CAR | game_winner | 0.737 | 0.805 | 0.793 | 81 | 20 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL5 | team_total | 0.283 | 0.355 | 0.340 | 36 | 65 | no | +0.051 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR2 | game_spread | 0.281 | 0.345 | 0.332 | 35 | 66 | no | +0.044 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NYI2 | game_spread | 0.275 | 0.215 | 0.226 | 22 | 79 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ5 | team_total | 0.175 | 0.240 | 0.226 | 25 | 77 | no | +0.043 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL2 | game_spread | 0.450 | 0.520 | 0.506 | 53 | 49 | no | +0.043 | OK |
| KXNHLGAME-26NOV07CHICAR-CHI | game_winner | 0.263 | 0.205 | 0.216 | 21 | 80 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL3 | team_total | 0.696 | 0.765 | 0.752 | 78 | 25 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ2 | team_total | 0.780 | 0.845 | 0.833 | 86 | 17 | no | +0.040 | OK |
| KXNHLTOTAL-26NOV07SJDAL-5 | game_total | 0.739 | 0.795 | 0.785 | 80 | 21 | no | +0.039 | OK |
| KXNHLGAME-26NOV07FLAWSH-WSH | game_winner | 0.595 | 0.535 | 0.547 | 54 | 47 | yes | +0.038 | OK |
| KXNHLGAME-26NOV07SJDAL-SJ | game_winner | 0.321 | 0.265 | 0.276 | 27 | 74 | yes | +0.037 | OK |
| KXNHLGAME-26NOV07SJDAL-DAL | game_winner | 0.679 | 0.735 | 0.724 | 74 | 27 | no | +0.037 | OK |
| KXNHLTOTAL-26NOV07CHICAR-6 | game_total | 0.537 | 0.600 | 0.588 | 61 | 41 | no | +0.037 | OK |
| KXNHLTOTAL-26NOV07NJNYI-5 | game_total | 0.721 | 0.780 | 0.769 | 79 | 23 | no | +0.036 | OK |
| KXNHLGAME-26NOV07NYRSEA-NYR | game_winner | 0.496 | 0.555 | 0.543 | 56 | 45 | no | +0.036 | OK |
| KXNHLGAME-26NOV07NYRSEA-SEA | game_winner | 0.503 | 0.445 | 0.457 | 45 | 56 | yes | +0.036 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-FLA2 | game_spread | 0.211 | 0.265 | 0.254 | 27 | 74 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-FLA3 | game_spread | 0.116 | 0.165 | 0.154 | 17 | 84 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA4 | team_total | 0.330 | 0.385 | 0.374 | 39 | 62 | no | +0.034 | OK |
| KXNHLTOTAL-26NOV07SJDAL-6 | game_total | 0.520 | 0.575 | 0.564 | 58 | 43 | no | +0.033 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL3 | game_spread | 0.263 | 0.315 | 0.304 | 32 | 69 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR6 | team_total | 0.168 | 0.225 | 0.213 | 24 | 79 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR3 | game_spread | 0.168 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV07SJDAL-4 | game_total | 0.832 | 0.880 | 0.871 | 89 | 13 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR2 | team_total | 0.896 | 0.945 | 0.937 | 96 | 7 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV07FLAWSH-WSH2 | game_spread | 0.375 | 0.325 | 0.335 | 33 | 68 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH6 | team_total | 0.135 | 0.090 | 0.098 | 10 | 92 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.526 | 0.470 | 0.481 | 48 | 54 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV07NJNYI-7 | game_total | 0.385 | 0.440 | 0.429 | 45 | 57 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV07UTAOTT-8 | game_total | 0.332 | 0.285 | 0.294 | 29 | 72 | yes | +0.028 | OK |
| KXNHLGAME-26NOV07FLAWSH-FLA | game_winner | 0.405 | 0.460 | 0.449 | 47 | 55 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV07CHICAR-7 | game_total | 0.415 | 0.465 | 0.455 | 47 | 54 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-SEA2 | game_spread | 0.290 | 0.245 | 0.254 | 25 | 76 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH3 | team_total | 0.682 | 0.630 | 0.641 | 64 | 38 | yes | +0.026 | OK |
| KXNHLGAME-26NOV07PITLA-LA | game_winner | 0.564 | 0.515 | 0.525 | 52 | 49 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL2 | team_total | 0.868 | 0.910 | 0.903 | 92 | 10 | no | +0.025 | OK |
| KXNHLTOTAL-26NOV07SJDAL-8 | game_total | 0.222 | 0.265 | 0.256 | 27 | 74 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR3 | team_total | 0.744 | 0.805 | 0.794 | 83 | 22 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV07SJDAL-7 | game_total | 0.399 | 0.445 | 0.436 | 45 | 56 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-WSH5 | team_total | 0.276 | 0.235 | 0.243 | 24 | 77 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV07CHICAR-4 | game_total | 0.839 | 0.880 | 0.873 | 89 | 13 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV07STLNSH-STL6 | team_total | 0.097 | 0.060 | 0.066 | 7 | 95 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.408 | 0.365 | 0.373 | 37 | 64 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA3 | team_total | 0.677 | 0.630 | 0.640 | 64 | 38 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV07SJDAL-9 | game_total | 0.149 | 0.185 | 0.177 | 19 | 82 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV07CHICAR-5 | game_total | 0.748 | 0.795 | 0.786 | 81 | 22 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 | team_total | 0.482 | 0.535 | 0.525 | 55 | 48 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV07CHICAR-8 | game_total | 0.236 | 0.280 | 0.271 | 29 | 73 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN5 | team_total | 0.157 | 0.115 | 0.122 | 13 | 90 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV07UTAOTT-10 | game_total | 0.125 | 0.095 | 0.100 | 10 | 91 | yes | +0.019 | OK |
| KXNHLGAME-26NOV07DETCOL-COL | game_winner | 0.626 | 0.665 | 0.657 | 67 | 34 | no | +0.018 | OK |
| KXNHLGAME-26NOV07DETCOL-DET | game_winner | 0.374 | 0.335 | 0.343 | 34 | 67 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV07NJNYI-6 | game_total | 0.495 | 0.535 | 0.527 | 54 | 47 | no | +0.018 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CHI2 | game_spread | 0.113 | 0.085 | 0.090 | 9 | 92 | yes | +0.017 | OK |
| KXNHLGAME-26NOV07VANEDM-EDM | game_winner | 0.730 | 0.765 | 0.758 | 77 | 24 | no | +0.017 | OK |
| KXNHLGAME-26NOV07VANEDM-VAN | game_winner | 0.270 | 0.235 | 0.242 | 24 | 77 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV07STLNSH-10 | game_total | 0.081 | 0.055 | 0.060 | 6 | 95 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN4 | team_total | 0.311 | 0.265 | 0.274 | 28 | 75 | yes | +0.017 | OK |
| KXNHLGAME-26NOV07PITLA-PIT | game_winner | 0.436 | 0.475 | 0.467 | 48 | 53 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL6 | team_total | 0.135 | 0.170 | 0.162 | 18 | 84 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ3 | team_total | 0.568 | 0.620 | 0.610 | 64 | 40 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT2 | game_spread | 0.241 | 0.275 | 0.268 | 28 | 73 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-SEA4 | team_total | 0.411 | 0.370 | 0.378 | 38 | 64 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07MTLTOR-MTL6 | team_total | 0.142 | 0.110 | 0.116 | 12 | 90 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA3 | team_total | 0.549 | 0.585 | 0.578 | 59 | 42 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA5 | team_total | 0.165 | 0.195 | 0.189 | 20 | 81 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV07UTAOTT-UTA6 | team_total | 0.141 | 0.110 | 0.116 | 12 | 90 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV07DETCOL-5 | game_total | 0.775 | 0.810 | 0.803 | 82 | 20 | no | +0.014 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ WSH | 0.595 | 0.578 | 0.168 | 0.220 | 6.32 | 6.43 | 0.938/0.991 | KXNHLTEAMTOTAL-26NOV07FLAWSH-FLA4 +0.029 |
| STL @ NSH | 0.477 | 0.498 | 0.179 | 0.220 | 6.16 | 6.36 | 1.000/0.977 | KXNHLTEAMTOTAL-26NOV07STLNSH-NSH3 +0.036 |
| NYR @ SEA | 0.503 | 0.541 | 0.177 | 0.220 | 6.35 | 6.34 | 1.005/0.983 | KXNHLGAME-26NOV07NYRSEA-SEA +0.038 |
| MTL @ TOR | 0.459 | 0.532 | 0.165 | 0.210 | 6.72 | 6.78 | 0.988/0.983 | KXNHLGAME-26NOV07MTLTOR-TOR +0.073 |
| UTA @ OTT | 0.446 | 0.521 | 0.163 | 0.213 | 6.70 | 6.58 | 1.071/0.993 | KXNHLGAME-26NOV07UTAOTT-OTT +0.074 |
| NJD @ NYI | 0.496 | 0.517 | 0.179 | 0.220 | 5.80 | 6.18 | 0.952/0.979 | KXNHLTOTAL-26NOV07NJNYI-7 +0.062 |
| CHI @ CAR | 0.737 | 0.685 | 0.151 | 0.193 | 6.02 | 6.53 | 1.000/0.995 | KXNHLTEAMTOTAL-26NOV07CHICAR-CHI3 +0.106 |
| SJS @ DAL | 0.679 | 0.631 | 0.165 | 0.214 | 5.93 | 6.19 | 0.990/1.027 | KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3 +0.073 |
| TBL @ MIN | 0.441 | 0.470 | 0.173 | 0.218 | 6.36 | 6.35 | 1.033/0.958 | KXNHLGAME-26NOV07TBMIN-TB -0.029 |
| DET @ COL | 0.626 | 0.658 | 0.170 | 0.196 | 6.25 | 6.48 | 0.976/1.015 | KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 +0.054 |
| PIT @ LAK | 0.564 | 0.556 | 0.164 | 0.217 | 6.53 | 6.37 | 0.993/1.021 | KXNHLTOTAL-26NOV07PITLA-6 -0.031 |
| VAN @ EDM | 0.730 | 0.663 | 0.134 | 0.192 | 7.16 | 7.00 | 1.009/1.021 | KXNHLSPREAD-26NOV07VANEDM-EDM2 -0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 42 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2455 (adj 0.2279) · $4.58 · thesis WSH:OFFENSE_4PLUS
- Sandis Vilmanis: 1+ goals YES @ 12c · p 0.1717 (adj 0.1575) · $3.47 · thesis FLA:OFFENSE_4PLUS
- Pierre-Luc Dubois: 1+ goals YES @ 17c · p 0.2252 (adj 0.2102) · $3.76 · thesis WSH:OFFENSE_4PLUS
- Justin Sourdif: 1+ goals YES @ 13c · p 0.1666 (adj 0.155) · $1.93 · thesis WSH:OFFENSE_4PLUS
- Adam Edstrom: 2+ goals YES @ 1c · p 0.0237 (adj 0.0228) · $1.19 · thesis NSH:OFFENSE_4PLUS
- Justin Barron: 1+ goals YES @ 5c · p 0.0841 (adj 0.0756) · $2.13 · thesis STL:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 25c · p 0.3056 (adj 0.2904) · $3.74 · thesis NSH:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 30c · p 0.351 (adj 0.3357) · $3.17 · thesis STL:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1501 (adj 0.1363) · $3.1 · thesis SEA:OFFENSE_4PLUS
- New York R wins by over 1.5 goals NO @ 66c · p 0.7527 (adj 0.7039) · $7.49 · thesis SEA:WINS
- Pavel Dorofeyev: 1+ goals NO @ 66c · p 0.7115 (adj 0.6961) · $5.63 · thesis NYR:SUPPRESSED
- Jani Nyman: 1+ goals YES @ 12c · p 0.1535 (adj 0.1414) · $1.4 · thesis SEA:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1621 (adj 0.1478) · $2.19 · thesis TOR:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 48c · p 0.6174 (adj 0.5216) · $5.21 · thesis MTL:SUPPRESSED
- Colton Sissons: 1+ goals YES @ 11c · p 0.1398 (adj 0.1299) · $1.36 · thesis TOR:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 16c · p 0.2123 (adj 0.198) · $3.45 · thesis UTA:OFFENSE_4PLUS
- Dylan Cozens: 1+ goals YES @ 25c · p 0.2979 (adj 0.2834) · $2.86 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 16c · p 0.2013 (adj 0.186) · $2.01 · thesis OTT:OFFENSE_4PLUS
- Fabian Zetterlund: 1+ goals YES @ 20c · p 0.2399 (adj 0.2262) · $1.91 · thesis OTT:OFFENSE_4PLUS
- New Jersey wins by over 1.5 goals NO @ 65c · p 0.7387 (adj 0.6919) · $8.58 · thesis NYI:WINS
- Jean-Gabriel Pageau: 1+ goals YES @ 13c · p 0.1665 (adj 0.1536) · $1.55 · thesis NYI:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 11c · p 0.1385 (adj 0.1301) · $1.75 · thesis NJD:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 64c · p 0.6828 (adj 0.6708) · $3.11 · thesis NJD:SUPPRESSED
- Dillon Boucher: 1+ goals YES @ 5c · p 0.0895 (adj 0.0771) · $2.22 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 63c · p 0.7034 (adj 0.6813) · $8.58 · thesis CAR:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 19c · p 0.243 (adj 0.2248) · $3.03 · thesis CHI:OFFENSE_4PLUS
- Oliver Moore: 1+ goals YES @ 12c · p 0.1534 (adj 0.1426) · $1.78 · thesis CHI:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 63c · p 0.684 (adj 0.6693) · $7.1 · thesis DAL:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 72c · p 0.7939 (adj 0.7494) · $8.56 · thesis SJS:SUPPRESSED
- San Jose over 3.5 goals scored YES @ 23c · p 0.293 (adj 0.2565) · $2.13 · thesis SJS:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1384 (adj 0.125) · $3.16 · thesis MIN:OFFENSE_4PLUS
- Bobby Brink: 1+ goals YES @ 14c · p 0.184 (adj 0.168) · $2.4 · thesis MIN:OFFENSE_4PLUS
- Quinn Hughes: 1+ assists NO @ 37c · p 0.4577 (adj 0.4113) · $5.33 · thesis MIN:SUPPRESSED
- Blake Coleman: 1+ goals YES @ 20c · p 0.2494 (adj 0.2321) · $2.86 · thesis MIN:OFFENSE_4PLUS
- Sheldon Dries: 1+ goals YES @ 7c · p 0.1069 (adj 0.0952) · $2.09 · thesis DET:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0756 (adj 0.0692) · $1.64 · thesis LAK:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.1586 (adj 0.1464) · $2.11 · thesis PIT:WINS_BY_2PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.124 (adj 0.1118) · $1.74 · thesis PIT:WINS_BY_2PLUS
- Brendan Gallagher: 1+ goals YES @ 9c · p 0.1463 (adj 0.126) · $2.84 · thesis VAN:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3368 (adj 0.3126) · $4.88 · thesis EDM:OFFENSE_4PLUS
- Edmonton wins by over 2.5 goals NO @ 58c · p 0.6695 (adj 0.6222) · $8.29 · thesis GAME:TIGHT
- Mattias Ekholm: 1+ goals YES @ 12c · p 0.1536 (adj 0.1414) · $1.9 · thesis EDM:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ WSH** · priced 171/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 27.35, exp saves 23.73 (sd 6.52), pull risk 0.057
- FLA net: Akira Schmid (CONFIRMED) exp shots 26.43, exp saves 22.55 (sd 6.39), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Ovechkin: 1+ assists | 0.316 | 0.210 | 22/80 | +0.084 | STANDARD |
| Ryan Leonard: 1+ assists | 0.317 | 0.215 | 22/79 | +0.085 | STANDARD |
| Aliaksei Protas: 1+ points | 0.459 | 0.375 | 38/63 | +0.063 | STANDARD |
| Alex Ovechkin: 1+ points | 0.492 | 0.410 | 42/60 | +0.055 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.324 | 0.395 | 40/61 | +0.049 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.245 | 0.175 | 18/83 | +0.055 | STANDARD |

**STL @ NSH** · priced 151/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.66, exp saves 23.84 (sd 6.58), pull risk 0.066
- STL net: Joel Hofer (CONFIRMED) exp shots 27.8, exp saves 24.05 (sd 6.61), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Holloway: 1+ points | 0.603 | 0.500 | 51/51 | +0.075 | STANDARD |
| Dylan Holloway: 1+ assists | 0.418 | 0.330 | 34/68 | +0.063 | STANDARD |
| Dylan Holloway: 2+ points | 0.237 | 0.150 | 16/86 | +0.067 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.240 | 0.315 | 33/70 | +0.045 | STANDARD |
| Robert Thomas: 1+ goals | 0.312 | 0.240 | 25/77 | +0.049 | STANDARD |
| Jimmy Snuggerud: 1+ points | 0.605 | 0.535 | 55/48 | +0.038 | STANDARD |

**NYR @ SEA** · priced 172/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.17, exp saves 23.64 (sd 6.44), pull risk 0.057
- NYR net: Dylan Garand (PROJECTED) exp shots 27.28, exp saves 23.37 (sd 6.57), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ goals | 0.183 | 0.105 | 17/96 | +0.003 | STANDARD |
| Bobby McMann: 1+ assists | 0.308 | 0.240 | 25/77 | +0.045 | STANDARD |
| Pavel Dorofeyev: 1+ goals | 0.288 | 0.350 | 36/66 | +0.036 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.370 | 0.310 | 33/71 | +0.024 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.315 | 0.255 | 27/76 | +0.031 | STANDARD |
| Ben Meyers: 1+ goals | 0.150 | 0.095 | 10/91 | +0.044 | STANDARD |

**MTL @ TOR** · priced 161/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 29.0, exp saves 25.08 (sd 6.96), pull risk 0.07
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.71, exp saves 24.71 (sd 6.94), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.383 | 0.530 | 54/48 | +0.120 | STANDARD |
| Morgan Rielly: 1+ assists | 0.358 | 0.265 | 29/76 | +0.053 | STANDARD |
| Auston Matthews: 1+ assists | 0.404 | 0.495 | 51/52 | +0.058 | STANDARD |
| Nick Suzuki: 1+ points | 0.581 | 0.670 | 69/35 | +0.054 | STANDARD |
| Easton Cowan: 1+ points | 0.517 | 0.430 | 45/59 | +0.050 | STANDARD |
| Easton Cowan: 1+ assists | 0.377 | 0.290 | 31/73 | +0.052 | STANDARD |

**UTA @ OTT** · priced 167/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (CONFIRMED) exp shots 26.39, exp saves 22.89 (sd 6.44), pull risk 0.067
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.47, exp saves 23.56 (sd 6.6), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Fabian Zetterlund: 1+ points | 0.474 | 0.375 | 40/65 | +0.057 | STANDARD |
| Fabian Zetterlund: 1+ assists | 0.307 | 0.210 | 23/81 | +0.065 | STANDARD |
| Mikhail Sergachev: 1+ points | 0.506 | 0.585 | 60/43 | +0.047 | STANDARD |
| Jack McBain: 1+ goals | 0.153 | 0.080 | 12/96 | +0.026 | STANDARD |
| Dylan Guenther: 1+ points | 0.522 | 0.595 | 61/42 | +0.041 | STANDARD |
| Clayton Keller: 1+ points | 0.588 | 0.660 | 67/35 | +0.047 | STANDARD |

**NJD @ NYI** · priced 166/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 28.65, exp saves 24.89 (sd 6.68), pull risk 0.057
- NJD net: Jake Allen (PROBABLE) exp shots 26.66, exp saves 23.05 (sd 6.36), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.391 | 0.510 | 52/50 | +0.092 | STANDARD |
| Jack Hughes: 2+ points | 0.218 | 0.325 | 34/69 | +0.077 | STANDARD |
| Emil Heineman: 1+ assists | 0.301 | 0.195 | 20/81 | +0.089 | STANDARD |
| Luke Evangelista: 1+ assists | 0.231 | 0.330 | 34/68 | +0.074 | STANDARD |
| Nico Hischier: 1+ assists | 0.290 | 0.370 | 39/65 | +0.044 | STANDARD |
| Emil Heineman: 1+ points | 0.428 | 0.350 | 36/66 | +0.052 | STANDARD |

**CHI @ CAR** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 21.81, exp saves 19.44 (sd 5.57), pull risk 0.045
- CHI net: Spencer Knight (PROBABLE) exp shots 33.1, exp saves 27.69 (sd 7.63), pull risk 0.097

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.204 | 0.315 | 34/71 | +0.071 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.465 | 0.355 | 36/65 | +0.089 | STANDARD |
| Sebastian Aho: 1+ assists | 0.380 | 0.490 | 51/53 | +0.073 | STANDARD |
| Sebastian Aho: 1+ points | 0.561 | 0.660 | 70/38 | +0.042 | STANDARD |
| Sebastian Aho: 1+ goals | 0.297 | 0.385 | 40/63 | +0.057 | STANDARD |
| Nikolaj Ehlers: 1+ points | 0.540 | 0.620 | 65/41 | +0.033 | STANDARD |

**SJS @ DAL** · priced 172/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROBABLE) exp shots 24.49, exp saves 21.65 (sd 6.03), pull risk 0.045
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.67, exp saves 23.5 (sd 6.68), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Nedeljkovic: 25+ saves | 0.437 | 0.270 | 46/92 | -0.041 |  |
| Mikko Rantanen: 2+ points | 0.282 | 0.385 | 41/64 | +0.061 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.485 | 0.580 | 60/44 | +0.058 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.206 | 0.295 | 31/72 | +0.060 | STANDARD |
| Ivar Stenberg: 1+ points | 0.336 | 0.425 | 45/60 | +0.047 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.390 | 0.470 | 49/55 | +0.042 | STANDARD |

**TBL @ MIN** · priced 161/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.08, exp saves 24.1 (sd 6.75), pull risk 0.07
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 27.46, exp saves 23.87 (sd 6.53), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.487 | 0.620 | 63/39 | +0.106 | STANDARD |
| Matt Boldy: 1+ assists | 0.359 | 0.485 | 49/52 | +0.104 | STANDARD |
| Bobby Brink: 1+ points | 0.419 | 0.310 | 34/72 | +0.063 | STANDARD |
| Bobby Brink: 1+ assists | 0.291 | 0.190 | 20/82 | +0.080 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.270 | 0.365 | 38/65 | +0.064 | STANDARD |
| Quinn Hughes: 1+ assists | 0.542 | 0.635 | 64/37 | +0.071 | STANDARD |

**DET @ COL** · priced 177/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.53, exp saves 23.53 (sd 6.32), pull risk 0.044
- DET net: Daniil Tarasov (PROJECTED) exp shots 30.11, exp saves 25.24 (sd 7.1), pull risk 0.099

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Malinski: 1+ points | 0.386 | 0.295 | 32/73 | +0.050 | STANDARD |
| Lucas Raymond: 1+ assists | 0.318 | 0.405 | 43/62 | +0.046 | STANDARD |
| Sam Malinski: 1+ assists | 0.325 | 0.240 | 26/78 | +0.051 | STANDARD |
| Lucas Raymond: 1+ points | 0.491 | 0.565 | 60/47 | +0.021 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.372 | 0.435 | 45/58 | +0.030 | STANDARD |
| Moritz Seider: 1+ points | 0.424 | 0.485 | 50/53 | +0.028 | STANDARD |

**PIT @ LAK** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.28, exp saves 23.7 (sd 6.48), pull risk 0.055
- PIT net: Sergei Murashov (PROJECTED) exp shots 27.6, exp saves 23.54 (sd 6.64), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 2+ points | 0.246 | 0.340 | 35/67 | +0.069 | STANDARD |
| Artemi Panarin: 1+ assists | 0.434 | 0.525 | 53/48 | +0.068 | STANDARD |
| Trevor Moore: 1+ points | 0.432 | 0.355 | 37/66 | +0.045 | STANDARD |
| Erik Karlsson: 1+ assists | 0.410 | 0.485 | 49/52 | +0.053 | STANDARD |
| Sidney Crosby: 1+ assists | 0.353 | 0.425 | 44/59 | +0.040 | STANDARD |
| Artemi Panarin: 2+ assists | 0.105 | 0.175 | 19/84 | +0.045 | STANDARD |

**VAN @ EDM** · priced 160/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 24.17, exp saves 21.32 (sd 5.94), pull risk 0.05
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.14, exp saves 25.13 (sd 7.25), pull risk 0.109

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#25): 1+ goals | 0.058 | 0.355 | 70/99 | -0.049 | STANDARD |
| Connor McDavid: 2+ assists | 0.265 | 0.410 | 43/61 | +0.108 | STANDARD |
| Connor McDavid: 2+ points | 0.513 | 0.645 | 66/37 | +0.100 | STANDARD |
| Mattias Ekholm: 1+ points | 0.511 | 0.380 | 42/66 | +0.074 | STANDARD |
| Leon Draisaitl: 2+ points | 0.437 | 0.550 | 57/47 | +0.076 | STANDARD |
| Linus Karlsson: 1+ goals | 0.228 | 0.115 | 16/93 | +0.059 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
