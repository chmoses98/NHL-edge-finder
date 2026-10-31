# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T15:46:20Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 4130 · contracts joined: 2219 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1969, 'NO_EDGE': 99, 'OK': 151}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 311, 'game_early_goal': 10, 'first_goal': 351, 'game_winner': 20, 'player_goals': 625, 'game_overtime': 10, 'player_points': 418, 'game_spread': 40, 'team_total': 100, 'game_total': 90, 'goalie_saves': 4}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BOS | 2026-10-31T17:00:00Z | T-60m | 0.700 | 0.300 | 0.152 | 6.13 | 3.72 | 2.41 | 231 (25/206) | PROJECTED/PROJECTED |
| STL @ DET | 2026-10-31T17:00:00Z | T-60m | 0.511 | 0.489 | 0.180 | 5.78 | 2.92 | 2.86 | 218 (25/193) | CONFIRMED/PROJECTED |
| TBL @ NSH | 2026-10-31T18:00:00Z | T-90m | 0.455 | 0.545 | 0.175 | 6.04 | 2.88 | 3.16 | 216 (25/191) | PROJECTED/PROJECTED |
| EDM @ NYI | 2026-10-31T18:00:00Z | T-90m | 0.497 | 0.503 | 0.166 | 6.41 | 3.19 | 3.22 | 214 (25/189) | PROJECTED/CONFIRMED |
| BUF @ LAK | 2026-10-31T20:00:00Z | T-3h | 0.518 | 0.482 | 0.176 | 6.02 | 3.07 | 2.95 | 226 (25/201) | PROJECTED/PROJECTED |
| OTT @ SJS | 2026-10-31T20:00:00Z | T-3h | 0.519 | 0.481 | 0.168 | 6.78 | 3.45 | 3.33 | 225 (25/200) | PROJECTED/PROJECTED |
| PIT @ MTL | 2026-10-31T23:00:00Z | T-6h | 0.617 | 0.383 | 0.164 | 6.37 | 3.56 | 2.82 | 228 (25/203) | CONFIRMED/PROJECTED |
| TOR @ VAN | 2026-10-31T23:00:00Z | T-6h | 0.448 | 0.552 | 0.160 | 7.23 | 3.45 | 3.79 | 225 (25/200) | PROJECTED/CONFIRMED |
| CBJ @ DAL | 2026-11-01T00:00:00Z | T-6h | 0.584 | 0.416 | 0.184 | 5.58 | 3.04 | 2.54 | 210 (25/185) | PROJECTED/PROJECTED |
| CGY @ COL | 2026-11-01T02:00:00Z | T-6h | 0.712 | 0.288 | 0.150 | 6.49 | 3.95 | 2.54 | 226 (25/201) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.349 | 0.475 | 0.449 | 48 | 53 | no | +0.104 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.498 | 0.605 | 0.584 | 61 | 40 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4 | team_total | 0.461 | 0.355 | 0.375 | 36 | 65 | yes | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB4 | team_total | 0.398 | 0.495 | 0.475 | 50 | 51 | no | +0.075 | OK |
| KXNHLGAME-26OCT31OTTSJ-SJ | game_winner | 0.519 | 0.425 | 0.444 | 43 | 58 | yes | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN5 | team_total | 0.271 | 0.180 | 0.196 | 19 | 83 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.574 | 0.670 | 0.652 | 68 | 34 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3 | team_total | 0.667 | 0.565 | 0.586 | 58 | 45 | yes | +0.070 | OK |
| KXNHLGAME-26OCT31PITMTL-MTL | game_winner | 0.617 | 0.525 | 0.544 | 53 | 48 | yes | +0.069 | OK |
| KXNHLGAME-26OCT31PITMTL-PIT | game_winner | 0.383 | 0.475 | 0.456 | 48 | 53 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ3 | team_total | 0.674 | 0.585 | 0.603 | 59 | 42 | yes | +0.067 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.288 | 0.205 | 0.220 | 21 | 80 | yes | +0.067 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.712 | 0.795 | 0.780 | 80 | 21 | no | +0.067 | OK |
| KXNHLTOTAL-26OCT31TORVAN-8 | game_total | 0.411 | 0.320 | 0.337 | 33 | 69 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT31TORVAN-9 | game_total | 0.318 | 0.235 | 0.250 | 24 | 77 | yes | +0.065 | OK |
| KXNHLGAME-26OCT31OTTSJ-OTT | game_winner | 0.481 | 0.570 | 0.552 | 58 | 44 | no | +0.062 | OK |
| KXNHLGAME-26OCT31TORVAN-TOR | game_winner | 0.552 | 0.635 | 0.619 | 64 | 37 | no | +0.061 | OK |
| KXNHLGAME-26OCT31TORVAN-VAN | game_winner | 0.448 | 0.365 | 0.381 | 37 | 64 | yes | +0.061 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ2 | game_spread | 0.313 | 0.235 | 0.249 | 24 | 77 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT4 | team_total | 0.324 | 0.405 | 0.388 | 41 | 60 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.365 | 0.450 | 0.432 | 46 | 56 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT3 | team_total | 0.536 | 0.615 | 0.599 | 62 | 39 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ4 | team_total | 0.464 | 0.380 | 0.396 | 39 | 63 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB3 | team_total | 0.621 | 0.700 | 0.685 | 71 | 31 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ5 | team_total | 0.275 | 0.200 | 0.214 | 21 | 81 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.708 | 0.635 | 0.650 | 64 | 37 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT31TORVAN-7 | game_total | 0.609 | 0.535 | 0.550 | 54 | 47 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB3 | game_spread | 0.196 | 0.265 | 0.250 | 27 | 74 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL2 | game_spread | 0.395 | 0.320 | 0.334 | 33 | 69 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN2 | team_total | 0.851 | 0.780 | 0.796 | 79 | 23 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN2 | game_spread | 0.260 | 0.195 | 0.207 | 20 | 81 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB5 | team_total | 0.218 | 0.285 | 0.271 | 29 | 72 | no | +0.048 | OK |
| KXNHLGAME-26OCT31TBNSH-NSH | game_winner | 0.455 | 0.385 | 0.399 | 39 | 62 | yes | +0.048 | OK |
| KXNHLGAME-26OCT31TBNSH-TB | game_winner | 0.545 | 0.615 | 0.601 | 62 | 39 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT31TORVAN-6 | game_total | 0.712 | 0.640 | 0.655 | 65 | 37 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN6 | team_total | 0.141 | 0.075 | 0.085 | 9 | 94 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT3 | game_spread | 0.173 | 0.235 | 0.221 | 24 | 77 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT2 | game_spread | 0.280 | 0.345 | 0.331 | 35 | 66 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT3 | game_spread | 0.108 | 0.165 | 0.152 | 17 | 84 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.205 | 0.265 | 0.252 | 27 | 74 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB2 | game_spread | 0.322 | 0.385 | 0.372 | 39 | 62 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT31BUFLA-BUF2 | game_spread | 0.264 | 0.325 | 0.312 | 33 | 68 | no | +0.040 | OK |
| KXNHLGAME-26OCT31BUFLA-BUF | game_winner | 0.482 | 0.545 | 0.533 | 55 | 46 | no | +0.040 | OK |
| KXNHLGAME-26OCT31BUFLA-LA | game_winner | 0.518 | 0.455 | 0.467 | 46 | 55 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT2 | team_total | 0.759 | 0.820 | 0.809 | 83 | 19 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ6 | team_total | 0.136 | 0.080 | 0.089 | 9 | 93 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.467 | 0.400 | 0.413 | 41 | 61 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.261 | 0.200 | 0.211 | 21 | 81 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT2 | game_spread | 0.198 | 0.255 | 0.243 | 26 | 75 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR3 | game_spread | 0.227 | 0.290 | 0.277 | 30 | 72 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT31TORVAN-10 | game_total | 0.176 | 0.120 | 0.130 | 13 | 89 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.689 | 0.745 | 0.734 | 75 | 26 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.200 | 0.260 | 0.247 | 27 | 75 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT5 | team_total | 0.162 | 0.225 | 0.211 | 24 | 79 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR2 | game_spread | 0.348 | 0.410 | 0.397 | 42 | 60 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT31BUFLA-BUF3 | game_spread | 0.155 | 0.205 | 0.194 | 21 | 80 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.371 | 0.430 | 0.418 | 44 | 58 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT31TBNSH-NSH2 | game_spread | 0.243 | 0.195 | 0.204 | 20 | 81 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB2 | team_total | 0.820 | 0.865 | 0.857 | 87 | 14 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL2 | game_spread | 0.342 | 0.395 | 0.384 | 40 | 61 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT31STLDET-4 | game_total | 0.810 | 0.860 | 0.851 | 87 | 15 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31BUFLA-BUF3 | team_total | 0.573 | 0.630 | 0.619 | 64 | 38 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.769 | 0.825 | 0.815 | 84 | 19 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31BUFLA-BUF4 | team_total | 0.354 | 0.405 | 0.395 | 41 | 60 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-8 | game_total | 0.344 | 0.295 | 0.304 | 30 | 71 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31BUFLA-BUF2 | team_total | 0.791 | 0.840 | 0.831 | 85 | 17 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT31STLDET-5 | game_total | 0.719 | 0.770 | 0.760 | 78 | 24 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ3 | game_spread | 0.196 | 0.150 | 0.158 | 16 | 86 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL3 | team_total | 0.598 | 0.650 | 0.640 | 66 | 36 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT31PITMTL-7 | game_total | 0.477 | 0.525 | 0.515 | 53 | 48 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.130 | 0.095 | 0.101 | 10 | 91 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL4 | team_total | 0.330 | 0.380 | 0.370 | 39 | 63 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT31TBNSH-7 | game_total | 0.419 | 0.465 | 0.456 | 47 | 54 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN3 | game_spread | 0.161 | 0.125 | 0.132 | 13 | 88 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-9 | game_total | 0.255 | 0.210 | 0.219 | 22 | 80 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT31BUFLA-LA2 | game_spread | 0.296 | 0.255 | 0.263 | 26 | 75 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT31TBNSH-4 | game_total | 0.840 | 0.875 | 0.869 | 88 | 13 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT31CHIBOS-CHI2 | team_total | 0.684 | 0.725 | 0.717 | 73 | 28 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL3 | team_total | 0.552 | 0.600 | 0.591 | 61 | 41 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT31TBNSH-6 | game_total | 0.532 | 0.575 | 0.567 | 58 | 43 | no | +0.020 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BOS | 0.700 | 0.673 | 0.152 | 0.199 | 6.13 | 6.49 | 0.969/1.026 | KXNHLTEAMTOTAL-26OCT31CHIBOS-CHI3 +0.069 |
| STL @ DET | 0.511 | 0.498 | 0.180 | 0.216 | 5.78 | 6.11 | 0.995/0.994 | KXNHLTOTAL-26OCT31STLDET-7 +0.054 |
| TBL @ NSH | 0.455 | 0.465 | 0.175 | 0.222 | 6.04 | 6.23 | 0.995/0.958 | KXNHLTOTAL-26OCT31TBNSH-7 +0.043 |
| EDM @ NYI | 0.497 | 0.483 | 0.166 | 0.216 | 6.41 | 6.70 | 0.957/1.023 | KXNHLTOTAL-26OCT31EDMNYI-7 +0.051 |
| BUF @ LAK | 0.518 | 0.545 | 0.176 | 0.217 | 6.02 | 6.19 | 0.990/0.998 | KXNHLTEAMTOTAL-26OCT31BUFLA-LA4 +0.040 |
| OTT @ SJS | 0.519 | 0.503 | 0.168 | 0.215 | 6.78 | 6.50 | 1.035/1.051 | KXNHLTOTAL-26OCT31OTTSJ-8 -0.045 |
| PIT @ MTL | 0.617 | 0.529 | 0.164 | 0.216 | 6.37 | 6.65 | 0.983/1.021 | KXNHLTEAMTOTAL-26OCT31PITMTL-PIT3 +0.098 |
| TOR @ VAN | 0.448 | 0.502 | 0.160 | 0.211 | 7.23 | 6.67 | 1.021/0.956 | KXNHLTEAMTOTAL-26OCT31TORVAN-TOR4 -0.096 |
| CBJ @ DAL | 0.584 | 0.549 | 0.184 | 0.220 | 5.58 | 5.95 | 0.987/0.965 | KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3 +0.071 |
| CGY @ COL | 0.712 | 0.698 | 0.150 | 0.191 | 6.49 | 6.57 | 0.977/0.998 | KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 +0.023 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 37 recommended · full analysis in card.md / packet.json `thesis_card`

- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.265 (adj 0.2475) · $4.31 · thesis CHI:OFFENSE_4PLUS
- Oliver Moore: 1+ goals YES @ 11c · p 0.1486 (adj 0.1365) · $2.53 · thesis CHI:OFFENSE_4PLUS
- Hampus Lindholm: 1+ assists YES @ 26c · p 0.3386 (adj 0.2943) · $3.16 · thesis BOS:OFFENSE_4PLUS
- Connor Bedard: 1+ assists NO @ 57c · p 0.6545 (adj 0.6073) · $8.16 · thesis CHI:SUPPRESSED
- Jimmy Snuggerud: 1+ goals YES @ 27c · p 0.3292 (adj 0.3131) · $4.53 · thesis STL:OFFENSE_4PLUS
- Lucas Raymond: 1+ assists NO @ 58c · p 0.6575 (adj 0.6162) · $6.02 · thesis DET:SUPPRESSED
- Dylan Holloway: 1+ assists YES @ 31c · p 0.3857 (adj 0.3404) · $1.34 · thesis STL:OFFENSE_4PLUS
- Charle-Edouard D'Astous: 1+ goals NO @ 88c · p 0.9288 (adj 0.9153) · $9.77 · thesis TBL:SUPPRESSED
- Ryan O'Reilly: 1+ goals YES @ 25c · p 0.3133 (adj 0.295) · $4.55 · thesis NSH:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 74c · p 0.8091 (adj 0.7721) · $6.74 · thesis NSH:WINS
- Mattias Ekholm: 1+ goals YES @ 7c · p 0.1232 (adj 0.1049) · $3.19 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 13c · p 0.1785 (adj 0.1651) · $3.44 · thesis EDM:OFFENSE_4PLUS
- Adam Pelech: 1+ goals YES @ 5c · p 0.0688 (adj 0.0641) · $1.25 · thesis NYI:OFFENSE_4PLUS
- Anthony Duclair: 1+ goals YES @ 15c · p 0.1873 (adj 0.1755) · $2.29 · thesis NYI:OFFENSE_4PLUS
- Andre Lee: 1+ goals YES @ 9c · p 0.1311 (adj 0.1196) · $2.76 · thesis LAK:OFFENSE_4PLUS
- Corey Perry: 1+ goals YES @ 14c · p 0.1826 (adj 0.1707) · $2.76 · thesis LAK:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0787 (adj 0.0665) · $1.3 · thesis LAK:WINS_BY_2PLUS
- Buffalo wins by over 1.5 goals NO @ 68c · p 0.7651 (adj 0.7201) · $7.72 · thesis LAK:WINS
- Tyler Toffoli: 1+ assists YES @ 24c · p 0.3249 (adj 0.2774) · $3.52 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 79c · p 0.8241 (adj 0.8143) · $8.69 · thesis SJS:SUPPRESSED
- Adam Gaudette: 1+ goals YES @ 14c · p 0.1693 (adj 0.1595) · $1.31 · thesis SJS:OFFENSE_4PLUS
- Collin Graf: 1+ goals YES @ 17c · p 0.2002 (adj 0.1914) · $1.46 · thesis SJS:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1291 (adj 0.1168) · $2.6 · thesis PIT:OFFENSE_4PLUS
- Phillip Danault: 1+ goals YES @ 12c · p 0.1647 (adj 0.1485) · $2.77 · thesis MTL:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1616 (adj 0.1512) · $1.76 · thesis PIT:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2694 (adj 0.2445) · $5.63 · thesis VAN:OFFENSE_4PLUS
- Vancouver wins by over 1.5 goals YES @ 20c · p 0.289 (adj 0.242) · $2.22 · thesis VAN:WINS_BY_2PLUS
- Gavin McKenna: 1+ goals NO @ 72c · p 0.7842 (adj 0.7644) · $9.77 · thesis TOR:SUPPRESSED
- Liam Ohgren: 1+ goals YES @ 16c · p 0.2113 (adj 0.1872) · $1.82 · thesis VAN:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 19c · p 0.2609 (adj 0.2407) · $5.46 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1838 (adj 0.1653) · $3.32 · thesis CBJ:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 74c · p 0.8053 (adj 0.7702) · $3.66 · thesis GAME:TIGHT
- Jason Robertson: 1+ goals NO @ 60c · p 0.6425 (adj 0.6306) · $4.05 · thesis DAL:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 8c · p 0.1097 (adj 0.0998) · $1.75 · thesis CGY:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 76c · p 0.805 (adj 0.7913) · $9.0 · thesis COL:SUPPRESSED
- Colorado over 3.5 goals scored NO @ 34c · p 0.4212 (adj 0.3756) · $2.93 · thesis COL:SUPPRESSED
- Mikael Backlund: 1+ goals YES @ 15c · p 0.1811 (adj 0.1721) · $1.82 · thesis CGY:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BOS** · priced 179/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 25.06, exp saves 22.16 (sd 6.06), pull risk 0.044
- CHI net: Arvid Soderblom (PROJECTED) exp shots 28.59, exp saves 24.0 (sd 6.9), pull risk 0.098

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Zadorov: 1+ points | 0.315 | 0.140 | 24/96 | +0.062 | STANDARD |
| Nikita Zadorov: 1+ assists | 0.261 | 0.135 | 16/89 | +0.092 | STANDARD |
| Mason Lohrei: 1+ points | 0.321 | 0.210 | 32/90 | -0.014 | STANDARD |
| Mason Lohrei: 1+ assists | 0.271 | 0.160 | 26/94 | -0.003 | STANDARD |
| Patrick Kane: 1+ assists | 0.288 | 0.395 | 40/61 | +0.085 | STANDARD |
| Hampus Lindholm: 1+ points | 0.398 | 0.295 | 32/73 | +0.063 | STANDARD |

**STL @ DET** · priced 154/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.58, exp saves 22.11 (sd 6.22), pull risk 0.06
- STL net: Joel Hofer (PROJECTED) exp shots 28.81, exp saves 24.9 (sd 6.7), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Holloway: 1+ assists | 0.386 | 0.295 | 31/72 | +0.061 | STANDARD |
| Lucas Raymond: 1+ assists | 0.343 | 0.425 | 43/58 | +0.060 | STANDARD |
| Dylan Holloway: 1+ points | 0.550 | 0.470 | 49/55 | +0.042 | STANDARD |
| Moritz Seider: 1+ points | 0.464 | 0.535 | 54/47 | +0.049 | STANDARD |
| Moritz Seider: 1+ assists | 0.399 | 0.465 | 48/55 | +0.033 | STANDARD |
| Jimmy Snuggerud: 1+ goals | 0.329 | 0.265 | 27/74 | +0.045 | STANDARD |

**TBL @ NSH** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROJECTED) exp shots 29.61, exp saves 25.47 (sd 6.86), pull risk 0.063
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.75, exp saves 22.29 (sd 6.24), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.466 | 0.610 | 63/41 | +0.107 | STANDARD |
| Nikita Kucherov: 2+ points | 0.284 | 0.410 | 42/60 | +0.099 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.134 | 0.250 | 27/77 | +0.084 | STANDARD |
| Nikita Kucherov: 1+ points | 0.642 | 0.730 | 75/29 | +0.054 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.313 | 0.240 | 25/77 | +0.050 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.181 | 0.245 | 26/77 | +0.036 | STANDARD |

**EDM @ NYI** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.15, exp saves 23.23 (sd 6.5), pull risk 0.077
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.76, exp saves 23.98 (sd 6.67), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.551 | 0.660 | 67/35 | +0.083 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.377 | 0.270 | 29/75 | +0.072 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.462 | 0.565 | 58/45 | +0.071 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.568 | 0.465 | 48/55 | +0.070 | STANDARD |
| Connor McDavid: 2+ assists | 0.193 | 0.295 | 31/72 | +0.073 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.276 | 0.370 | 39/65 | +0.058 | STANDARD |

**BUF @ LAK** · priced 168/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 27.66, exp saves 24.12 (sd 6.48), pull risk 0.054
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 28.05, exp saves 24.01 (sd 6.58), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tage Thompson: 1+ assists | 0.317 | 0.405 | 42/61 | +0.056 | STANDARD |
| Trevor Moore: 1+ assists | 0.330 | 0.245 | 26/77 | +0.056 | STANDARD |
| Trevor Moore: 1+ points | 0.480 | 0.400 | 42/62 | +0.043 | STANDARD |
| Alex Laferriere: 1+ points | 0.598 | 0.520 | 54/50 | +0.040 | STANDARD |
| Tage Thompson: 1+ points | 0.537 | 0.605 | 62/41 | +0.036 | STANDARD |
| Tage Thompson: 2+ points | 0.185 | 0.250 | 27/77 | +0.033 | STANDARD |

**OTT @ SJS** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.35, exp saves 24.29 (sd 6.78), pull risk 0.071
- OTT net: Samuel Ersson (PROJECTED) exp shots 25.93, exp saves 22.44 (sd 6.25), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.445 | 0.545 | 56/47 | +0.068 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.325 | 0.230 | 24/78 | +0.072 | STANDARD |
| Macklin Celebrini: 2+ points | 0.293 | 0.380 | 40/64 | +0.051 | STANDARD |
| Collin Graf: 1+ points | 0.421 | 0.335 | 36/69 | +0.045 | STANDARD |
| Jake Sanderson: 1+ assists | 0.372 | 0.450 | 46/56 | +0.050 | STANDARD |
| Tyler Toffoli: 1+ points | 0.464 | 0.390 | 41/63 | +0.037 | STANDARD |

**PIT @ MTL** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.16, exp saves 24.48 (sd 6.71), pull risk 0.065
- PIT net: Sergei Murashov (PROJECTED) exp shots 26.26, exp saves 22.51 (sd 6.48), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.619 | 0.495 | 54/55 | +0.062 |  |
| Egor Chinakhov: 1+ assists | 0.289 | 0.210 | 23/81 | +0.047 | STANDARD |
| Phillip Danault: 1+ goals | 0.165 | 0.100 | 12/92 | +0.037 | STANDARD |
| Alex Newhook: 1+ assists | 0.317 | 0.255 | 29/78 | +0.012 | STANDARD |
| Josh Anderson: 1+ assists | 0.216 | 0.155 | 19/88 | +0.015 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.300 | 0.240 | 26/78 | +0.027 | STANDARD |

**TOR @ VAN** · priced 158/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.88, exp saves 24.85 (sd 6.73), pull risk 0.069
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 28.15, exp saves 24.18 (sd 6.78), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Linus Karlsson: 1+ points | 0.494 | 0.370 | 40/66 | +0.077 | STANDARD |
| Liam Ohgren: 1+ points | 0.429 | 0.315 | 34/71 | +0.073 | STANDARD |
| Auston Matthews: 2+ points | 0.288 | 0.400 | 42/62 | +0.076 | STANDARD |
| Auston Matthews: 1+ assists | 0.408 | 0.520 | 54/50 | +0.075 | STANDARD |
| Anthony Stolarz: 25+ saves | 0.480 | 0.370 | 44/70 | +0.022 |  |
| William Nylander: 1+ assists | 0.415 | 0.520 | 54/50 | +0.067 | STANDARD |

**CBJ @ DAL** · priced 158/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.99, exp saves 21.81 (sd 6.06), pull risk 0.047
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.69, exp saves 23.03 (sd 6.41), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Valeri Nichushkin: 1+ assists | 0.211 | 0.315 | 33/70 | +0.074 | STANDARD |
| Charlie Coyle: 1+ goals | 0.261 | 0.180 | 19/83 | +0.060 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.184 | 0.110 | 13/91 | +0.046 | STANDARD |
| Charlie Coyle: 1+ points | 0.521 | 0.450 | 47/57 | +0.034 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.449 | 0.520 | 54/50 | +0.033 | STANDARD |
| Miro Heiskanen: 1+ points | 0.481 | 0.550 | 57/47 | +0.032 | STANDARD |

**CGY @ COL** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.33, exp saves 23.34 (sd 6.28), pull risk 0.043
- CGY net: Dustin Wolf (PROJECTED) exp shots 33.08, exp saves 27.67 (sd 7.88), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 2+ points | 0.211 | 0.325 | 33/68 | +0.094 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.532 | 0.645 | 66/37 | +0.081 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.401 | 0.510 | 53/51 | +0.071 | STANDARD |
| Cale Makar: 1+ assists | 0.480 | 0.580 | 60/44 | +0.063 | STANDARD |
| Cale Makar: 2+ assists | 0.134 | 0.225 | 24/79 | +0.064 | STANDARD |
| Martin Necas: 2+ points | 0.299 | 0.385 | 41/64 | +0.045 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
