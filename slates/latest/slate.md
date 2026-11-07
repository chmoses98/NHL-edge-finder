# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-07T17:46:23Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 11 · markets on board: 4340 · contracts joined: 2457 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2182, 'NO_EDGE': 141, 'OK': 134}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 351, 'game_early_goal': 11, 'first_goal': 393, 'game_winner': 22, 'player_goals': 676, 'game_overtime': 11, 'player_points': 466, 'goalie_saves': 10, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| STL @ NSH | 2026-11-07T18:00:00Z | T-10m | 0.480 | 0.520 | 0.175 | 6.17 | 3.01 | 3.16 | 213 (25/188) | CONFIRMED/CONFIRMED |
| NYR @ SEA | 2026-11-07T22:00:00Z | T-3h | 0.503 | 0.496 | 0.177 | 6.35 | 3.19 | 3.16 | 224 (25/199) | PROJECTED/PROJECTED |
| MTL @ TOR | 2026-11-08T00:00:00Z | T-6h | 0.459 | 0.541 | 0.165 | 6.72 | 3.22 | 3.50 | 213 (25/188) | CONFIRMED/CONFIRMED |
| UTA @ OTT | 2026-11-08T00:00:00Z | T-6h | 0.446 | 0.554 | 0.163 | 6.70 | 3.18 | 3.52 | 225 (25/200) | CONFIRMED/PROJECTED |
| NJD @ NYI | 2026-11-08T00:00:00Z | T-6h | 0.492 | 0.508 | 0.180 | 5.80 | 2.88 | 2.92 | 220 (25/195) | PROBABLE/CONFIRMED |
| CHI @ CAR | 2026-11-08T01:00:00Z | T-6h | 0.737 | 0.263 | 0.151 | 6.02 | 3.77 | 2.24 | 234 (25/209) | PROBABLE/PROBABLE |
| SJS @ DAL | 2026-11-08T01:00:00Z | T-6h | 0.681 | 0.319 | 0.167 | 5.91 | 3.52 | 2.39 | 227 (25/202) | CONFIRMED/PROJECTED |
| TBL @ MIN | 2026-11-08T01:00:00Z | T-6h | 0.439 | 0.561 | 0.174 | 6.33 | 2.97 | 3.36 | 224 (25/199) | CONFIRMED/CONFIRMED |
| DET @ COL | 2026-11-08T02:00:00Z | T-6h | 0.626 | 0.374 | 0.170 | 6.25 | 3.53 | 2.72 | 237 (25/212) | PROJECTED/PROJECTED |
| PIT @ LAK | 2026-11-08T02:00:00Z | T-6h | 0.564 | 0.436 | 0.164 | 6.53 | 3.46 | 3.07 | 219 (25/194) | PROJECTED/PROJECTED |
| VAN @ EDM | 2026-11-08T03:00:00Z | T-6h | 0.730 | 0.270 | 0.134 | 7.16 | 4.38 | 2.78 | 221 (25/196) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV07CHICAR-CAR3 | game_spread | 0.361 | 0.465 | 0.444 | 47 | 54 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4 | team_total | 0.483 | 0.590 | 0.569 | 60 | 42 | no | +0.080 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CAR2 | game_spread | 0.512 | 0.605 | 0.587 | 61 | 40 | no | +0.071 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL3 | game_spread | 0.296 | 0.390 | 0.370 | 40 | 62 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR4 | team_total | 0.536 | 0.630 | 0.612 | 64 | 38 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR5 | team_total | 0.330 | 0.420 | 0.401 | 43 | 59 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ4 | team_total | 0.345 | 0.435 | 0.416 | 45 | 58 | no | +0.058 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL2 | game_spread | 0.446 | 0.525 | 0.509 | 53 | 48 | no | +0.057 | OK |
| KXNHLGAME-26NOV07NJNYI-NJ | game_winner | 0.508 | 0.585 | 0.570 | 59 | 42 | no | +0.055 | OK |
| KXNHLGAME-26NOV07NJNYI-NYI | game_winner | 0.492 | 0.415 | 0.430 | 42 | 59 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL5 | team_total | 0.282 | 0.360 | 0.344 | 37 | 65 | no | +0.052 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ3 | game_spread | 0.167 | 0.235 | 0.220 | 24 | 77 | no | +0.051 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ2 | game_spread | 0.285 | 0.355 | 0.340 | 36 | 65 | no | +0.049 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR2 | game_spread | 0.281 | 0.345 | 0.332 | 35 | 66 | no | +0.044 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NYI2 | game_spread | 0.275 | 0.215 | 0.226 | 22 | 79 | yes | +0.043 | OK |
| KXNHLTOTAL-26NOV07SJDAL-5 | game_total | 0.736 | 0.795 | 0.784 | 80 | 21 | no | +0.043 | OK |
| KXNHLGAME-26NOV07CHICAR-CAR | game_winner | 0.737 | 0.800 | 0.788 | 81 | 21 | no | +0.041 | OK |
| KXNHLGAME-26NOV07CHICAR-CHI | game_winner | 0.263 | 0.205 | 0.216 | 21 | 80 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ2 | team_total | 0.781 | 0.845 | 0.834 | 86 | 17 | no | +0.039 | OK |
| KXNHLTOTAL-26NOV07SJDAL-6 | game_total | 0.516 | 0.575 | 0.563 | 58 | 43 | no | +0.037 | OK |
| KXNHLTOTAL-26NOV07CHICAR-6 | game_total | 0.537 | 0.600 | 0.588 | 61 | 41 | no | +0.037 | OK |
| KXNHLGAME-26NOV07NYRSEA-NYR | game_winner | 0.496 | 0.555 | 0.543 | 56 | 45 | no | +0.036 | OK |
| KXNHLGAME-26NOV07NYRSEA-SEA | game_winner | 0.503 | 0.445 | 0.457 | 45 | 56 | yes | +0.036 | OK |
| KXNHLTOTAL-26NOV07NJNYI-5 | game_total | 0.722 | 0.780 | 0.769 | 79 | 23 | no | +0.035 | OK |
| KXNHLGAME-26NOV07SJDAL-DAL | game_winner | 0.681 | 0.735 | 0.725 | 74 | 27 | no | +0.035 | OK |
| KXNHLGAME-26NOV07SJDAL-SJ | game_winner | 0.319 | 0.265 | 0.275 | 27 | 74 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR3 | team_total | 0.744 | 0.810 | 0.798 | 83 | 21 | no | +0.034 | OK |
| KXNHLTOTAL-26NOV07NJNYI-7 | game_total | 0.381 | 0.440 | 0.428 | 45 | 57 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ5 | team_total | 0.176 | 0.235 | 0.222 | 25 | 78 | no | +0.032 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL3 | game_spread | 0.263 | 0.315 | 0.304 | 32 | 69 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV07SJDAL-4 | game_total | 0.831 | 0.880 | 0.871 | 89 | 13 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR6 | team_total | 0.168 | 0.225 | 0.213 | 24 | 79 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR3 | game_spread | 0.168 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR2 | team_total | 0.896 | 0.945 | 0.937 | 96 | 7 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.526 | 0.465 | 0.477 | 48 | 55 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV07UTAOTT-8 | game_total | 0.332 | 0.285 | 0.294 | 29 | 72 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV07CHICAR-7 | game_total | 0.415 | 0.465 | 0.455 | 47 | 54 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-SEA2 | game_spread | 0.290 | 0.245 | 0.254 | 25 | 76 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV07SJDAL-8 | game_total | 0.220 | 0.265 | 0.256 | 27 | 74 | no | +0.027 | OK |
| KXNHLGAME-26NOV07PITLA-LA | game_winner | 0.564 | 0.515 | 0.525 | 52 | 49 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL2 | team_total | 0.869 | 0.910 | 0.903 | 92 | 10 | no | +0.025 | OK |
| KXNHLTOTAL-26NOV07SJDAL-7 | game_total | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT2 | game_spread | 0.241 | 0.285 | 0.276 | 29 | 72 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV07STLNSH-STL6 | team_total | 0.099 | 0.065 | 0.071 | 7 | 94 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV07SJDAL-9 | game_total | 0.146 | 0.185 | 0.177 | 19 | 82 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV07CHICAR-4 | game_total | 0.839 | 0.880 | 0.873 | 89 | 13 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.408 | 0.365 | 0.373 | 37 | 64 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV07CHICAR-5 | game_total | 0.748 | 0.795 | 0.786 | 81 | 22 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 | team_total | 0.482 | 0.535 | 0.525 | 55 | 48 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV07CHICAR-8 | game_total | 0.236 | 0.280 | 0.271 | 29 | 73 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN5 | team_total | 0.157 | 0.115 | 0.122 | 13 | 90 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV07UTAOTT-10 | game_total | 0.125 | 0.095 | 0.100 | 10 | 91 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV07STLNSH-10 | game_total | 0.082 | 0.055 | 0.060 | 6 | 95 | yes | +0.018 | OK |
| KXNHLGAME-26NOV07DETCOL-COL | game_winner | 0.626 | 0.665 | 0.657 | 67 | 34 | no | +0.018 | OK |
| KXNHLGAME-26NOV07DETCOL-DET | game_winner | 0.374 | 0.335 | 0.343 | 34 | 67 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV07NJNYI-6 | game_total | 0.495 | 0.535 | 0.527 | 54 | 47 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CHI2 | game_spread | 0.113 | 0.085 | 0.090 | 9 | 92 | yes | +0.017 | OK |
| KXNHLGAME-26NOV07VANEDM-EDM | game_winner | 0.730 | 0.765 | 0.758 | 77 | 24 | no | +0.017 | OK |
| KXNHLGAME-26NOV07VANEDM-VAN | game_winner | 0.270 | 0.235 | 0.242 | 24 | 77 | yes | +0.017 | OK |
| KXNHLGAME-26NOV07UTAOTT-UTA | game_winner | 0.554 | 0.515 | 0.523 | 52 | 49 | yes | +0.016 | OK |
| KXNHLGAME-26NOV07PITLA-PIT | game_winner | 0.436 | 0.475 | 0.467 | 48 | 53 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ3 | team_total | 0.568 | 0.630 | 0.618 | 66 | 40 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-SEA4 | team_total | 0.411 | 0.365 | 0.374 | 38 | 65 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV07NJNYI-8 | game_total | 0.203 | 0.235 | 0.228 | 24 | 77 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07MTLTOR-MTL6 | team_total | 0.142 | 0.110 | 0.116 | 12 | 90 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV07NJNYI-4 | game_total | 0.816 | 0.850 | 0.844 | 86 | 16 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV07UTAOTT-UTA6 | team_total | 0.141 | 0.105 | 0.112 | 12 | 91 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV07DETCOL-5 | game_total | 0.775 | 0.810 | 0.803 | 82 | 20 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM3 | game_spread | 0.389 | 0.425 | 0.418 | 43 | 58 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV07PITLA-LA2 | game_spread | 0.349 | 0.310 | 0.318 | 32 | 70 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN6 | team_total | 0.066 | 0.040 | 0.044 | 5 | 97 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV07PITLA-8 | game_total | 0.307 | 0.270 | 0.277 | 28 | 74 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL5 | team_total | 0.282 | 0.325 | 0.316 | 34 | 69 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07UTAOTT-UTA4 | team_total | 0.480 | 0.435 | 0.444 | 45 | 58 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV07NJNYI-9 | game_total | 0.138 | 0.165 | 0.159 | 17 | 84 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV07UTAOTT-9 | game_total | 0.244 | 0.210 | 0.216 | 22 | 80 | yes | +0.012 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL2 | game_spread | 0.402 | 0.435 | 0.428 | 44 | 57 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV07STLNSH-STL3 | team_total | 0.618 | 0.585 | 0.592 | 59 | 42 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV07STLNSH-8 | game_total | 0.253 | 0.225 | 0.230 | 23 | 78 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV07STLNSH-6 | game_total | 0.558 | 0.525 | 0.532 | 53 | 48 | yes | +0.010 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| STL @ NSH | 0.480 | 0.492 | 0.175 | 0.217 | 6.17 | 6.37 | 1.004/0.977 | KXNHLTOTAL-26NOV07STLNSH-7 +0.037 |
| NYR @ SEA | 0.503 | 0.541 | 0.177 | 0.220 | 6.35 | 6.34 | 1.005/0.983 | KXNHLGAME-26NOV07NYRSEA-SEA +0.038 |
| MTL @ TOR | 0.459 | 0.532 | 0.165 | 0.210 | 6.72 | 6.78 | 0.988/0.983 | KXNHLGAME-26NOV07MTLTOR-TOR +0.073 |
| UTA @ OTT | 0.446 | 0.521 | 0.163 | 0.213 | 6.70 | 6.58 | 1.071/0.993 | KXNHLGAME-26NOV07UTAOTT-OTT +0.074 |
| NJD @ NYI | 0.492 | 0.516 | 0.180 | 0.216 | 5.80 | 6.19 | 0.952/0.983 | KXNHLTOTAL-26NOV07NJNYI-7 +0.071 |
| CHI @ CAR | 0.737 | 0.685 | 0.151 | 0.193 | 6.02 | 6.53 | 1.000/0.995 | KXNHLTEAMTOTAL-26NOV07CHICAR-CHI3 +0.106 |
| SJS @ DAL | 0.681 | 0.628 | 0.167 | 0.214 | 5.91 | 6.21 | 0.994/1.027 | KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3 +0.079 |
| TBL @ MIN | 0.439 | 0.486 | 0.174 | 0.214 | 6.33 | 6.43 | 1.033/0.985 | KXNHLGAME-26NOV07TBMIN-MIN +0.048 |
| DET @ COL | 0.626 | 0.658 | 0.170 | 0.196 | 6.25 | 6.48 | 0.976/1.015 | KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 +0.054 |
| PIT @ LAK | 0.564 | 0.556 | 0.164 | 0.217 | 6.53 | 6.37 | 0.993/1.021 | KXNHLTOTAL-26NOV07PITLA-6 -0.031 |
| VAN @ EDM | 0.730 | 0.663 | 0.134 | 0.192 | 7.16 | 7.00 | 1.009/1.021 | KXNHLSPREAD-26NOV07VANEDM-EDM2 -0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 39 recommended · full analysis in card.md / packet.json `thesis_card`

- Adam Edstrom: 1+ goals YES @ 15c · p 0.1998 (adj 0.1861) · $3.14 · thesis NSH:OFFENSE_4PLUS
- Justin Barron: 1+ goals YES @ 5c · p 0.0729 (adj 0.0672) · $1.33 · thesis STL:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 25c · p 0.3044 (adj 0.2895) · $4.08 · thesis NSH:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 70c · p 0.7772 (adj 0.7311) · $8.3 · thesis NSH:SUPPRESSED
- Ben Meyers: 1+ goals YES @ 10c · p 0.1501 (adj 0.1363) · $3.0 · thesis SEA:OFFENSE_4PLUS
- New York R wins by over 1.5 goals NO @ 66c · p 0.7527 (adj 0.7039) · $7.25 · thesis SEA:WINS
- Pavel Dorofeyev: 1+ goals NO @ 66c · p 0.7115 (adj 0.6961) · $5.44 · thesis NYR:SUPPRESSED
- Jani Nyman: 1+ goals YES @ 12c · p 0.1535 (adj 0.1414) · $1.35 · thesis SEA:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1621 (adj 0.1428) · $2.65 · thesis TOR:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 48c · p 0.6174 (adj 0.5216) · $3.93 · thesis MTL:SUPPRESSED
- Nick Suzuki: 2+ assists NO @ 85c · p 0.9168 (adj 0.8734) · $8.3 · thesis MTL:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 16c · p 0.2123 (adj 0.1967) · $3.17 · thesis UTA:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 16c · p 0.2013 (adj 0.1872) · $2.1 · thesis OTT:OFFENSE_4PLUS
- Dylan Cozens: 1+ goals YES @ 25c · p 0.2979 (adj 0.2834) · $2.77 · thesis OTT:OFFENSE_4PLUS
- Fabian Zetterlund: 1+ goals YES @ 20c · p 0.2399 (adj 0.2274) · $2.01 · thesis OTT:OFFENSE_4PLUS
- New York I wins by over 1.5 goals YES @ 22c · p 0.2981 (adj 0.2566) · $2.05 · thesis NYI:WINS_BY_2PLUS
- New Jersey wins by over 1.5 goals NO @ 65c · p 0.739 (adj 0.692) · $7.04 · thesis NYI:WINS
- Cody Glass: 1+ goals YES @ 11c · p 0.1403 (adj 0.1315) · $2.0 · thesis NJD:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2526 (adj 0.2394) · $1.56 · thesis NYI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 61c · p 0.7034 (adj 0.6788) · $8.3 · thesis CAR:SUPPRESSED
- Dillon Boucher: 1+ goals YES @ 5c · p 0.0895 (adj 0.0771) · $2.15 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 18c · p 0.243 (adj 0.2248) · $4.13 · thesis CHI:OFFENSE_4PLUS
- Oliver Moore: 1+ goals YES @ 12c · p 0.1534 (adj 0.1426) · $1.73 · thesis CHI:OFFENSE_4PLUS
- Adam Gaudette: 1+ goals YES @ 9c · p 0.1248 (adj 0.1123) · $1.6 · thesis SJS:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 63c · p 0.6875 (adj 0.6719) · $6.83 · thesis DAL:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 72c · p 0.7971 (adj 0.751) · $8.17 · thesis SJS:SUPPRESSED
- Dallas wins by over 1.5 goals NO @ 48c · p 0.5921 (adj 0.516) · $3.25 · thesis GAME:TIGHT
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1383 (adj 0.125) · $2.97 · thesis MIN:OFFENSE_4PLUS
- Bobby Brink: 1+ goals YES @ 14c · p 0.1867 (adj 0.17) · $2.4 · thesis MIN:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ assists NO @ 53c · p 0.6149 (adj 0.5675) · $5.68 · thesis MIN:SUPPRESSED
- Ryan Hartman: 1+ goals YES @ 15c · p 0.183 (adj 0.1723) · $1.75 · thesis MIN:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0756 (adj 0.0692) · $1.58 · thesis LAK:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.1586 (adj 0.1477) · $2.19 · thesis PIT:WINS_BY_2PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.124 (adj 0.1118) · $1.7 · thesis PIT:WINS_BY_2PLUS
- Ben Kindel: 1+ goals NO @ 77c · p 0.8093 (adj 0.7982) · $7.94 · thesis PIT:SUPPRESSED
- Brendan Gallagher: 1+ goals YES @ 10c · p 0.1463 (adj 0.1322) · $2.44 · thesis VAN:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3368 (adj 0.3164) · $5.39 · thesis EDM:OFFENSE_4PLUS
- Edmonton wins by over 1.5 goals NO @ 45c · p 0.5425 (adj 0.4937) · $6.44 · thesis GAME:TIGHT
- Mattias Ekholm: 1+ goals YES @ 12c · p 0.1536 (adj 0.1414) · $1.88 · thesis EDM:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**STL @ NSH** · priced 158/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 27.66, exp saves 23.82 (sd 6.59), pull risk 0.068
- STL net: Joel Hofer (CONFIRMED) exp shots 27.8, exp saves 24.04 (sd 6.64), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.223 | 0.315 | 33/70 | +0.063 | STANDARD |
| Mavrik Bourque: 1+ points | 0.380 | 0.445 | 45/56 | +0.042 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.304 | 0.245 | 25/76 | +0.041 | STANDARD |
| Ross Colton: 1+ assists | 0.217 | 0.160 | 17/85 | +0.037 | STANDARD |
| Mason McTavish: 1+ assists | 0.269 | 0.325 | 34/69 | +0.026 | STANDARD |
| Adam Edstrom: 1+ goals | 0.200 | 0.145 | 15/86 | +0.041 | STANDARD |

**NYR @ SEA** · priced 172/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.17, exp saves 23.64 (sd 6.44), pull risk 0.057
- NYR net: Dylan Garand (PROJECTED) exp shots 27.28, exp saves 23.37 (sd 6.57), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ goals | 0.183 | 0.105 | 17/96 | +0.003 | STANDARD |
| Bobby McMann: 1+ assists | 0.308 | 0.240 | 25/77 | +0.045 | STANDARD |
| Pavel Dorofeyev: 1+ goals | 0.288 | 0.350 | 36/66 | +0.036 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.370 | 0.310 | 33/71 | +0.024 | STANDARD |
| Ben Meyers: 1+ goals | 0.150 | 0.095 | 10/91 | +0.044 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.315 | 0.260 | 28/76 | +0.020 | STANDARD |

**MTL @ TOR** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 29.0, exp saves 25.08 (sd 6.96), pull risk 0.07
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.71, exp saves 24.71 (sd 6.94), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.383 | 0.530 | 54/48 | +0.120 | STANDARD |
| Morgan Rielly: 1+ assists | 0.358 | 0.265 | 29/76 | +0.053 | STANDARD |
| Nick Suzuki: 1+ points | 0.581 | 0.670 | 69/35 | +0.054 | STANDARD |
| Morgan Rielly: 1+ points | 0.413 | 0.325 | 35/70 | +0.047 | STANDARD |
| Easton Cowan: 1+ points | 0.517 | 0.430 | 45/59 | +0.050 | STANDARD |
| Nick Suzuki: 2+ assists | 0.083 | 0.170 | 19/85 | +0.058 | STANDARD |

**UTA @ OTT** · priced 168/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (CONFIRMED) exp shots 26.39, exp saves 22.89 (sd 6.44), pull risk 0.067
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.47, exp saves 23.56 (sd 6.6), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Fabian Zetterlund: 1+ assists | 0.307 | 0.205 | 23/82 | +0.065 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.474 | 0.380 | 40/64 | +0.057 | STANDARD |
| Mikhail Sergachev: 1+ points | 0.506 | 0.585 | 60/43 | +0.047 | STANDARD |
| Clayton Keller: 1+ points | 0.588 | 0.665 | 68/35 | +0.047 | STANDARD |
| Jack McBain: 1+ goals | 0.153 | 0.080 | 12/96 | +0.026 | STANDARD |
| Dylan Guenther: 1+ points | 0.522 | 0.595 | 61/42 | +0.041 | STANDARD |

**NJD @ NYI** · priced 166/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 28.65, exp saves 24.91 (sd 6.74), pull risk 0.057
- NJD net: Jake Allen (CONFIRMED) exp shots 26.66, exp saves 23.05 (sd 6.42), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.381 | 0.510 | 52/50 | +0.102 | STANDARD |
| Jake Allen: 25+ saves | 0.405 | 0.290 | 47/89 | -0.082 |  |
| Jack Hughes: 2+ points | 0.214 | 0.325 | 34/69 | +0.081 | STANDARD |
| Emil Heineman: 1+ assists | 0.300 | 0.195 | 20/81 | +0.089 | STANDARD |
| Luke Evangelista: 1+ assists | 0.228 | 0.330 | 34/68 | +0.077 | STANDARD |
| Jack Hughes: 1+ points | 0.580 | 0.665 | 69/36 | +0.044 | STANDARD |

**CHI @ CAR** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 21.81, exp saves 19.44 (sd 5.57), pull risk 0.045
- CHI net: Spencer Knight (PROBABLE) exp shots 33.1, exp saves 27.69 (sd 7.63), pull risk 0.097

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.204 | 0.330 | 35/69 | +0.091 | STANDARD |
| Pyotr Kochetkov: 20+ saves | 0.482 | 0.370 | 50/76 | -0.035 |  |
| Tyler Bertuzzi: 1+ points | 0.465 | 0.355 | 36/65 | +0.089 | STANDARD |
| Sebastian Aho: 1+ assists | 0.380 | 0.490 | 51/53 | +0.073 | STANDARD |
| Sebastian Aho: 1+ points | 0.561 | 0.660 | 70/38 | +0.042 | STANDARD |
| Sebastian Aho: 1+ goals | 0.297 | 0.395 | 40/61 | +0.077 | STANDARD |

**SJS @ DAL** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.49, exp saves 21.6 (sd 5.9), pull risk 0.045
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.67, exp saves 23.5 (sd 6.65), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Oettinger: 23+ saves | 0.430 | 0.295 | 50/91 | -0.088 |  |
| Mikko Rantanen: 2+ points | 0.284 | 0.390 | 41/63 | +0.070 | STANDARD |
| Ivar Stenberg: 1+ points | 0.331 | 0.425 | 45/60 | +0.052 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.203 | 0.295 | 31/72 | +0.063 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.489 | 0.580 | 60/44 | +0.054 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.396 | 0.470 | 49/55 | +0.036 | STANDARD |

**TBL @ MIN** · priced 161/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.08, exp saves 24.13 (sd 6.68), pull risk 0.068
- TBL net: Dennis Hildeby (CONFIRMED) exp shots 27.46, exp saves 23.81 (sd 6.5), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.491 | 0.625 | 64/39 | +0.102 | STANDARD |
| Matt Boldy: 1+ assists | 0.373 | 0.485 | 49/52 | +0.090 | STANDARD |
| Bobby Brink: 1+ points | 0.418 | 0.310 | 34/72 | +0.063 | STANDARD |
| Nikita Kucherov: 2+ points | 0.295 | 0.395 | 42/63 | +0.058 | STANDARD |
| Bobby Brink: 1+ assists | 0.287 | 0.190 | 20/82 | +0.076 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.385 | 0.480 | 49/53 | +0.067 | STANDARD |

**DET @ COL** · priced 177/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.53, exp saves 23.53 (sd 6.32), pull risk 0.044
- DET net: Daniil Tarasov (PROJECTED) exp shots 30.11, exp saves 25.24 (sd 7.1), pull risk 0.099

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Malinski: 1+ points | 0.386 | 0.295 | 32/73 | +0.050 | STANDARD |
| Lucas Raymond: 1+ assists | 0.318 | 0.405 | 43/62 | +0.046 | STANDARD |
| Sam Malinski: 1+ assists | 0.325 | 0.240 | 26/78 | +0.051 | STANDARD |
| Lucas Raymond: 1+ points | 0.491 | 0.565 | 60/47 | +0.021 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.372 | 0.445 | 46/57 | +0.040 | STANDARD |
| Moritz Seider: 1+ points | 0.424 | 0.485 | 50/53 | +0.028 | STANDARD |

**PIT @ LAK** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.28, exp saves 23.7 (sd 6.48), pull risk 0.055
- PIT net: Sergei Murashov (PROJECTED) exp shots 27.6, exp saves 23.54 (sd 6.64), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 2+ points | 0.246 | 0.340 | 35/67 | +0.069 | STANDARD |
| Artemi Panarin: 1+ assists | 0.434 | 0.525 | 53/48 | +0.068 | STANDARD |
| Erik Karlsson: 1+ assists | 0.410 | 0.485 | 49/52 | +0.053 | STANDARD |
| Trevor Moore: 1+ points | 0.432 | 0.360 | 37/65 | +0.045 | STANDARD |
| Sidney Crosby: 1+ assists | 0.353 | 0.425 | 44/59 | +0.040 | STANDARD |
| Artemi Panarin: 2+ assists | 0.105 | 0.175 | 19/84 | +0.045 | STANDARD |

**VAN @ EDM** · priced 160/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 24.17, exp saves 21.32 (sd 5.94), pull risk 0.05
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.14, exp saves 25.13 (sd 7.25), pull risk 0.109

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#25): 1+ goals | 0.058 | 0.325 | 64/99 | -0.049 | STANDARD |
| Connor McDavid: 2+ assists | 0.265 | 0.410 | 44/62 | +0.099 | STANDARD |
| Mattias Ekholm: 1+ points | 0.511 | 0.385 | 41/64 | +0.084 | STANDARD |
| Linus Karlsson: 1+ goals | 0.228 | 0.115 | 16/93 | +0.059 | STANDARD |
| Connor McDavid: 2+ points | 0.513 | 0.625 | 65/40 | +0.070 | STANDARD |
| Connor McDavid: 3+ points | 0.245 | 0.345 | 37/68 | +0.060 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
