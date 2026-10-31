# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T17:38:32Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 8 · markets on board: 4166 · contracts joined: 1861 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1661, 'OK': 129, 'NO_EDGE': 71}
families: {'period_winner': 72, 'period_spread': 48, 'period_total': 72, 'player_assists': 280, 'game_early_goal': 8, 'first_goal': 287, 'game_winner': 16, 'player_goals': 499, 'game_overtime': 8, 'player_points': 380, 'game_spread': 32, 'team_total': 80, 'game_total': 72, 'goalie_saves': 7}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ NSH | 2026-10-31T18:00:00Z | T-10m | 0.446 | 0.554 | 0.179 | 5.93 | 2.81 | 3.12 | 216 (25/191) | CONFIRMED/CONFIRMED |
| EDM @ NYI | 2026-10-31T18:00:00Z | T-10m | 0.511 | 0.489 | 0.179 | 6.32 | 3.20 | 3.12 | 217 (25/192) | CONFIRMED/CONFIRMED |
| BUF @ LAK | 2026-10-31T20:00:00Z | T-90m | 0.485 | 0.515 | 0.181 | 6.24 | 3.07 | 3.17 | 262 (25/237) | PROJECTED/PROJECTED |
| OTT @ SJS | 2026-10-31T20:00:00Z | T-90m | 0.519 | 0.481 | 0.168 | 6.78 | 3.45 | 3.33 | 225 (25/200) | PROJECTED/PROJECTED |
| PIT @ MTL | 2026-10-31T23:00:00Z | T-3h | 0.628 | 0.372 | 0.167 | 6.44 | 3.63 | 2.82 | 257 (25/232) | CONFIRMED/CONFIRMED |
| TOR @ VAN | 2026-10-31T23:00:00Z | T-3h | 0.448 | 0.552 | 0.160 | 7.23 | 3.45 | 3.79 | 225 (25/200) | PROJECTED/CONFIRMED |
| CBJ @ DAL | 2026-11-01T00:00:00Z | T-6h | 0.589 | 0.411 | 0.183 | 5.54 | 3.04 | 2.50 | 229 (25/204) | CONFIRMED/PROJECTED |
| CGY @ COL | 2026-11-01T02:00:00Z | T-6h | 0.716 | 0.284 | 0.150 | 6.47 | 3.95 | 2.52 | 230 (25/205) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.355 | 0.475 | 0.450 | 48 | 53 | no | +0.098 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB4 | team_total | 0.392 | 0.505 | 0.482 | 51 | 50 | no | +0.090 | OK |
| KXNHLGAME-26OCT31OTTSJ-SJ | game_winner | 0.519 | 0.415 | 0.436 | 42 | 59 | yes | +0.082 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.502 | 0.605 | 0.585 | 61 | 40 | no | +0.081 | OK |
| KXNHLGAME-26OCT31PITMTL-MTL | game_winner | 0.628 | 0.525 | 0.546 | 53 | 48 | yes | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4 | team_total | 0.461 | 0.360 | 0.379 | 37 | 65 | yes | +0.074 | OK |
| KXNHLGAME-26OCT31OTTSJ-OTT | game_winner | 0.481 | 0.575 | 0.556 | 58 | 43 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.573 | 0.670 | 0.651 | 68 | 34 | no | +0.071 | OK |
| KXNHLGAME-26OCT31PITMTL-PIT | game_winner | 0.372 | 0.465 | 0.446 | 47 | 54 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN5 | team_total | 0.271 | 0.180 | 0.196 | 19 | 83 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB3 | team_total | 0.615 | 0.705 | 0.688 | 71 | 30 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3 | team_total | 0.667 | 0.570 | 0.590 | 58 | 44 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB5 | team_total | 0.206 | 0.295 | 0.276 | 30 | 71 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ3 | team_total | 0.674 | 0.585 | 0.603 | 59 | 42 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT31TORVAN-8 | game_total | 0.411 | 0.320 | 0.337 | 33 | 69 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT31TORVAN-9 | game_total | 0.318 | 0.235 | 0.250 | 24 | 77 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ5 | team_total | 0.275 | 0.190 | 0.205 | 20 | 82 | yes | +0.064 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.716 | 0.795 | 0.781 | 80 | 21 | no | +0.062 | OK |
| KXNHLGAME-26OCT31TORVAN-TOR | game_winner | 0.552 | 0.635 | 0.619 | 64 | 37 | no | +0.061 | OK |
| KXNHLGAME-26OCT31TORVAN-VAN | game_winner | 0.448 | 0.365 | 0.381 | 37 | 64 | yes | +0.061 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ2 | game_spread | 0.313 | 0.235 | 0.249 | 24 | 77 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT4 | team_total | 0.323 | 0.405 | 0.388 | 41 | 60 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL2 | game_spread | 0.405 | 0.325 | 0.340 | 33 | 68 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.365 | 0.455 | 0.437 | 47 | 56 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ4 | team_total | 0.464 | 0.380 | 0.396 | 39 | 63 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT3 | team_total | 0.537 | 0.615 | 0.600 | 62 | 39 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN6 | team_total | 0.141 | 0.070 | 0.081 | 8 | 94 | yes | +0.055 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT2 | game_spread | 0.280 | 0.355 | 0.339 | 36 | 65 | no | +0.054 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.284 | 0.215 | 0.228 | 22 | 79 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT31TBNSH-6 | game_total | 0.512 | 0.585 | 0.571 | 59 | 42 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT31TORVAN-7 | game_total | 0.609 | 0.535 | 0.550 | 54 | 47 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ6 | team_total | 0.136 | 0.070 | 0.080 | 8 | 94 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB3 | game_spread | 0.196 | 0.265 | 0.250 | 27 | 74 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB2 | game_spread | 0.323 | 0.395 | 0.380 | 40 | 61 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT31TBNSH-7 | game_total | 0.403 | 0.475 | 0.460 | 48 | 53 | no | +0.050 | OK |
| KXNHLGAME-26OCT31TBNSH-NSH | game_winner | 0.446 | 0.375 | 0.389 | 38 | 63 | yes | +0.049 | OK |
| KXNHLGAME-26OCT31TBNSH-TB | game_winner | 0.554 | 0.625 | 0.611 | 63 | 38 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR3 | game_spread | 0.227 | 0.295 | 0.281 | 30 | 71 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN2 | game_spread | 0.260 | 0.195 | 0.207 | 20 | 81 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT2 | game_spread | 0.190 | 0.255 | 0.241 | 26 | 75 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT3 | game_spread | 0.105 | 0.165 | 0.151 | 17 | 84 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT31TORVAN-6 | game_total | 0.712 | 0.645 | 0.659 | 65 | 36 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.681 | 0.745 | 0.733 | 75 | 26 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT3 | game_spread | 0.173 | 0.235 | 0.221 | 24 | 77 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.701 | 0.635 | 0.649 | 64 | 37 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.369 | 0.435 | 0.421 | 44 | 57 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.459 | 0.390 | 0.404 | 40 | 62 | yes | +0.042 | OK |
| KXNHLTOTAL-26OCT31TBNSH-5 | game_total | 0.739 | 0.795 | 0.785 | 80 | 21 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN2 | team_total | 0.851 | 0.790 | 0.803 | 80 | 22 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT31TORVAN-10 | game_total | 0.176 | 0.120 | 0.130 | 13 | 89 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.259 | 0.200 | 0.211 | 21 | 81 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT5 | team_total | 0.161 | 0.220 | 0.207 | 23 | 79 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ3 | game_spread | 0.196 | 0.145 | 0.154 | 15 | 86 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT2 | team_total | 0.762 | 0.820 | 0.809 | 83 | 19 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.200 | 0.260 | 0.247 | 27 | 75 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR2 | game_spread | 0.348 | 0.410 | 0.397 | 42 | 60 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB2 | team_total | 0.817 | 0.865 | 0.856 | 87 | 14 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.213 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB6 | team_total | 0.089 | 0.145 | 0.132 | 16 | 87 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT31TBNSH-4 | game_total | 0.830 | 0.875 | 0.867 | 88 | 13 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-8 | game_total | 0.344 | 0.295 | 0.304 | 30 | 71 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ2 | team_total | 0.850 | 0.800 | 0.811 | 81 | 21 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.771 | 0.825 | 0.815 | 84 | 19 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT31TBNSH-NSH2 | game_spread | 0.238 | 0.195 | 0.203 | 20 | 81 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL3 | team_total | 0.599 | 0.650 | 0.640 | 66 | 36 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT31TBNSH-8 | game_total | 0.222 | 0.265 | 0.256 | 27 | 74 | no | +0.025 | OK |
| KXNHLGAME-26OCT31CBJDAL-CBJ | game_winner | 0.411 | 0.365 | 0.374 | 37 | 64 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL2 | game_spread | 0.349 | 0.395 | 0.386 | 40 | 61 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.130 | 0.095 | 0.101 | 10 | 91 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL3 | game_spread | 0.266 | 0.220 | 0.229 | 23 | 79 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-7 | game_total | 0.340 | 0.385 | 0.376 | 39 | 62 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN3 | game_spread | 0.161 | 0.125 | 0.132 | 13 | 88 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-9 | game_total | 0.255 | 0.210 | 0.219 | 22 | 80 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL2 | team_total | 0.808 | 0.845 | 0.838 | 85 | 16 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT3 | team_total | 0.647 | 0.690 | 0.682 | 70 | 32 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT31TBNSH-9 | game_total | 0.152 | 0.185 | 0.178 | 19 | 82 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL5 | team_total | 0.190 | 0.235 | 0.225 | 25 | 78 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL4 | team_total | 0.505 | 0.465 | 0.473 | 47 | 54 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL2 | team_total | 0.908 | 0.940 | 0.935 | 95 | 7 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI3 | team_total | 0.624 | 0.585 | 0.593 | 59 | 42 | yes | +0.017 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ NSH | 0.446 | 0.463 | 0.179 | 0.216 | 5.93 | 6.19 | 0.990/0.947 | KXNHLTOTAL-26OCT31TBNSH-7 +0.047 |
| EDM @ NYI | 0.511 | 0.484 | 0.179 | 0.219 | 6.32 | 6.67 | 0.948/1.023 | KXNHLTOTAL-26OCT31EDMNYI-7 +0.063 |
| BUF @ LAK | 0.485 | 0.542 | 0.181 | 0.223 | 6.24 | 6.19 | 0.993/0.998 | KXNHLGAME-26OCT31BUFLA-BUF -0.057 |
| OTT @ SJS | 0.519 | 0.503 | 0.168 | 0.215 | 6.78 | 6.50 | 1.035/1.051 | KXNHLTOTAL-26OCT31OTTSJ-8 -0.045 |
| PIT @ MTL | 0.628 | 0.520 | 0.167 | 0.213 | 6.44 | 6.62 | 0.983/1.012 | KXNHLGAME-26OCT31PITMTL-MTL -0.109 |
| TOR @ VAN | 0.448 | 0.502 | 0.160 | 0.211 | 7.23 | 6.67 | 1.021/0.956 | KXNHLTEAMTOTAL-26OCT31TORVAN-TOR4 -0.096 |
| CBJ @ DAL | 0.589 | 0.543 | 0.183 | 0.224 | 5.54 | 5.97 | 0.995/0.965 | KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3 +0.089 |
| CGY @ COL | 0.716 | 0.701 | 0.150 | 0.189 | 6.47 | 6.58 | 0.979/0.998 | KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 +0.034 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 31 recommended · full analysis in card.md / packet.json `thesis_card`

- Tampa Bay over 3.5 goals scored NO @ 50c · p 0.5903 (adj 0.5427) · $7.01 · thesis TBL:SUPPRESSED
- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3079 (adj 0.2947) · $3.87 · thesis NSH:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 74c · p 0.8031 (adj 0.7691) · $1.15 · thesis NSH:WINS
- Nils Hoglander: 1+ goals YES @ 11c · p 0.1403 (adj 0.1277) · $1.59 · thesis NSH:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 6c · p 0.1135 (adj 0.0976) · $4.24 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 12c · p 0.1785 (adj 0.1626) · $5.09 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 34c · p 0.4601 (adj 0.3788) · $7.11 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 26c · p 0.3017 (adj 0.29) · $4.53 · thesis EDM:OFFENSE_4PLUS
- Andre Lee: 1+ goals YES @ 9c · p 0.1247 (adj 0.1148) · $2.5 · thesis LAK:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0799 (adj 0.0674) · $1.62 · thesis LAK:WINS_BY_2PLUS
- Buffalo wins by over 1.5 goals NO @ 68c · p 0.7646 (adj 0.7198) · $9.82 · thesis LAK:WINS
- Rasmus Dahlin: 1+ goals NO @ 81c · p 0.8444 (adj 0.8333) · $7.57 · thesis BUF:SUPPRESSED
- Tyler Toffoli: 1+ assists YES @ 24c · p 0.3249 (adj 0.28) · $4.46 · thesis SJS:OFFENSE_4PLUS
- Adam Gaudette: 1+ goals YES @ 13c · p 0.1693 (adj 0.1582) · $2.89 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 79c · p 0.8241 (adj 0.8143) · $9.98 · thesis SJS:SUPPRESSED
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1208 (adj 0.1069) · $1.54 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1592 (adj 0.1494) · $1.71 · thesis PIT:OFFENSE_4PLUS
- Zachary Bolduc: 1+ assists YES @ 24c · p 0.3028 (adj 0.2664) · $2.42 · thesis MTL:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 30c · p 0.3369 (adj 0.3264) · $2.31 · thesis PIT:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2694 (adj 0.2483) · $7.56 · thesis VAN:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 71c · p 0.7837 (adj 0.7628) · $11.2 · thesis TOR:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 18c · p 0.2467 (adj 0.2238) · $5.25 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 16c · p 0.2113 (adj 0.1935) · $3.55 · thesis VAN:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.187 (adj 0.169) · $4.38 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 20c · p 0.2534 (adj 0.2351) · $3.79 · thesis CBJ:OFFENSE_4PLUS
- Dallas wins by over 1.5 goals NO @ 61c · p 0.6892 (adj 0.6471) · $3.84 · thesis CBJ:WINS
- Mikko Rantanen: 1+ goals NO @ 69c · p 0.7322 (adj 0.7179) · $5.24 · thesis DAL:SUPPRESSED
- Calgary over 1.5 goals scored YES @ 64c · p 0.7293 (adj 0.6822) · $8.25 · thesis CGY:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 15c · p 0.1928 (adj 0.1784) · $2.52 · thesis CGY:OFFENSE_4PLUS
- Jonathan Castagna: 1+ goals YES @ 8c · p 0.1099 (adj 0.0999) · $1.79 · thesis CGY:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 75c · p 0.7988 (adj 0.7841) · $11.2 · thesis COL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TBL @ NSH** · priced 160/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (CONFIRMED) exp shots 29.61, exp saves 25.46 (sd 6.87), pull risk 0.066
- TBL net: Andrei Vasilevskiy (CONFIRMED) exp shots 25.75, exp saves 22.33 (sd 6.14), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.467 | 0.615 | 62/39 | +0.126 | STANDARD |
| Nikita Kucherov: 2+ points | 0.275 | 0.415 | 42/59 | +0.118 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.130 | 0.235 | 27/80 | +0.059 | STANDARD |
| Nikita Kucherov: 3+ points | 0.083 | 0.160 | 19/87 | +0.040 | STANDARD |
| Nikita Kucherov: 1+ points | 0.642 | 0.705 | 73/32 | +0.023 | STANDARD |
| Brayden Point: 1+ assists | 0.382 | 0.440 | 45/57 | +0.031 | STANDARD |

**EDM @ NYI** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 27.15, exp saves 23.21 (sd 6.56), pull risk 0.075
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.76, exp saves 23.97 (sd 6.71), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.540 | 0.665 | 67/34 | +0.104 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.268 | 0.385 | 39/62 | +0.096 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.451 | 0.565 | 57/44 | +0.092 | STANDARD |
| Leon Draisaitl: 2+ points | 0.324 | 0.425 | 43/58 | +0.079 | STANDARD |
| Connor McDavid: 2+ points | 0.391 | 0.485 | 49/52 | +0.071 | STANDARD |
| Connor McDavid: 2+ assists | 0.189 | 0.275 | 30/75 | +0.047 | STANDARD |

**BUF @ LAK** · priced 210/211 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.66, exp saves 24.15 (sd 6.48), pull risk 0.054
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 28.05, exp saves 24.03 (sd 6.55), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ points | 0.291 | 0.095 | 17/98 | +0.111 | STANDARD |
| Mikey Anderson: 1+ points | 0.276 | 0.100 | 18/98 | +0.085 | STANDARD |
| Brian Dumoulin: 1+ points | 0.270 | 0.095 | 17/98 | +0.091 | STANDARD |
| Joel Edmundson: 1+ assists | 0.227 | 0.075 | 13/98 | +0.089 | STANDARD |
| Brian Dumoulin: 1+ assists | 0.237 | 0.100 | 14/94 | +0.089 | STANDARD |
| Mikey Anderson: 1+ assists | 0.233 | 0.100 | 15/95 | +0.074 | STANDARD |

**OTT @ SJS** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.35, exp saves 24.29 (sd 6.78), pull risk 0.071
- OTT net: Samuel Ersson (PROJECTED) exp shots 25.93, exp saves 22.44 (sd 6.25), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 2+ points | 0.293 | 0.395 | 40/61 | +0.080 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.445 | 0.545 | 56/47 | +0.068 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.325 | 0.235 | 24/77 | +0.072 | STANDARD |
| Jake Sanderson: 1+ assists | 0.372 | 0.455 | 47/56 | +0.050 | STANDARD |
| Tim Stutzle: 2+ points | 0.268 | 0.350 | 36/66 | +0.056 | STANDARD |
| Ivar Stenberg: 1+ points | 0.402 | 0.480 | 49/53 | +0.051 | STANDARD |

**PIT @ MTL** · priced 203/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.16, exp saves 24.42 (sd 6.68), pull risk 0.067
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.26, exp saves 22.49 (sd 6.49), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sergei Murashov: 27+ saves | 0.259 | 0.375 | 41/66 | +0.065 |  |
| Spencer Stastney: 1+ points | 0.217 | 0.120 | 22/98 | -0.015 | STANDARD |
| Samuel Girard: 1+ assists | 0.231 | 0.135 | 25/98 | -0.032 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.303 | 0.230 | 24/78 | +0.050 | STANDARD |
| Jacob Fowler: 23+ saves | 0.617 | 0.555 | 57/46 | +0.030 |  |
| Egor Chinakhov: 1+ assists | 0.277 | 0.215 | 23/80 | +0.034 | STANDARD |

**TOR @ VAN** · priced 160/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.88, exp saves 24.85 (sd 6.73), pull risk 0.069
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 28.15, exp saves 24.18 (sd 6.78), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.406 | 0.530 | 54/48 | +0.096 | STANDARD |
| Linus Karlsson: 1+ points | 0.494 | 0.370 | 39/65 | +0.087 | STANDARD |
| William Nylander: 1+ assists | 0.411 | 0.530 | 55/49 | +0.081 | STANDARD |
| Auston Matthews: 2+ points | 0.289 | 0.405 | 42/61 | +0.084 | STANDARD |
| Gavin McKenna: 1+ assists | 0.312 | 0.420 | 43/59 | +0.081 | STANDARD |
| William Nylander: 2+ points | 0.252 | 0.360 | 38/66 | +0.072 | STANDARD |

**CBJ @ DAL** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.99, exp saves 21.76 (sd 6.03), pull risk 0.051
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.69, exp saves 23.04 (sd 6.37), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nils Lundkvist: 1+ assists | 0.228 | 0.100 | 19/99 | +0.028 | STANDARD |
| Cole Sillinger: 1+ points | 0.348 | 0.255 | 27/76 | +0.065 | STANDARD |
| Damon Severson: 1+ assists | 0.315 | 0.225 | 26/81 | +0.041 | STANDARD |
| Mikko Rantanen: 2+ points | 0.215 | 0.300 | 33/73 | +0.041 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.221 | 0.305 | 33/72 | +0.045 | STANDARD |
| Damon Severson: 1+ points | 0.384 | 0.300 | 32/72 | +0.049 | STANDARD |

**CGY @ COL** · priced 175/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.33, exp saves 23.33 (sd 6.32), pull risk 0.042
- CGY net: Dustin Wolf (PROJECTED) exp shots 33.08, exp saves 27.66 (sd 7.79), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mackenzie Blackwood: 22+ saves | 0.610 | 0.280 | 50/94 | +0.092 |  |
| Cale Makar: 1+ points | 0.587 | 0.705 | 72/31 | +0.088 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.408 | 0.525 | 53/48 | +0.095 | STANDARD |
| Cale Makar: 1+ assists | 0.480 | 0.590 | 61/43 | +0.072 | STANDARD |
| Cale Makar: 2+ points | 0.226 | 0.320 | 33/69 | +0.069 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.540 | 0.620 | 66/42 | +0.023 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
