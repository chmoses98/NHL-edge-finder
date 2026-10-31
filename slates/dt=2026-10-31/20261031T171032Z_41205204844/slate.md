# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T17:10:32Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 8 · markets on board: 4218 · contracts joined: 1853 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1653, 'OK': 127, 'NO_EDGE': 73}
families: {'period_winner': 72, 'period_spread': 48, 'period_total': 72, 'player_assists': 276, 'game_early_goal': 8, 'first_goal': 287, 'game_winner': 16, 'player_goals': 499, 'game_overtime': 8, 'player_points': 376, 'game_spread': 32, 'team_total': 80, 'game_total': 72, 'goalie_saves': 7}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ NSH | 2026-10-31T18:00:00Z | T-30m | 0.455 | 0.545 | 0.175 | 6.04 | 2.88 | 3.16 | 216 (25/191) | PROJECTED/PROJECTED |
| EDM @ NYI | 2026-10-31T18:00:00Z | T-30m | 0.511 | 0.489 | 0.179 | 6.32 | 3.20 | 3.12 | 217 (25/192) | CONFIRMED/CONFIRMED |
| BUF @ LAK | 2026-10-31T20:00:00Z | T-90m | 0.485 | 0.515 | 0.181 | 6.24 | 3.07 | 3.17 | 262 (25/237) | PROJECTED/PROJECTED |
| OTT @ SJS | 2026-10-31T20:00:00Z | T-90m | 0.519 | 0.481 | 0.168 | 6.78 | 3.45 | 3.33 | 225 (25/200) | PROJECTED/PROJECTED |
| PIT @ MTL | 2026-10-31T23:00:00Z | T-3h | 0.628 | 0.372 | 0.167 | 6.44 | 3.63 | 2.82 | 257 (25/232) | CONFIRMED/CONFIRMED |
| TOR @ VAN | 2026-10-31T23:00:00Z | T-3h | 0.448 | 0.552 | 0.160 | 7.23 | 3.45 | 3.79 | 225 (25/200) | PROJECTED/CONFIRMED |
| CBJ @ DAL | 2026-11-01T00:00:00Z | T-6h | 0.589 | 0.411 | 0.183 | 5.54 | 3.04 | 2.50 | 221 (25/196) | CONFIRMED/PROJECTED |
| CGY @ COL | 2026-11-01T02:00:00Z | T-6h | 0.716 | 0.284 | 0.152 | 6.47 | 3.95 | 2.52 | 230 (25/205) | PROBABLE/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.348 | 0.475 | 0.449 | 48 | 53 | no | +0.104 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.496 | 0.605 | 0.584 | 61 | 40 | no | +0.088 | OK |
| KXNHLGAME-26OCT31OTTSJ-SJ | game_winner | 0.519 | 0.415 | 0.436 | 42 | 59 | yes | +0.082 | OK |
| KXNHLGAME-26OCT31PITMTL-MTL | game_winner | 0.628 | 0.525 | 0.546 | 53 | 48 | yes | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB4 | team_total | 0.398 | 0.495 | 0.475 | 50 | 51 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4 | team_total | 0.461 | 0.360 | 0.379 | 37 | 65 | yes | +0.074 | OK |
| KXNHLGAME-26OCT31OTTSJ-OTT | game_winner | 0.481 | 0.575 | 0.556 | 58 | 43 | no | +0.072 | OK |
| KXNHLGAME-26OCT31PITMTL-PIT | game_winner | 0.372 | 0.465 | 0.446 | 47 | 54 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.574 | 0.670 | 0.652 | 68 | 34 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN5 | team_total | 0.271 | 0.180 | 0.196 | 19 | 83 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3 | team_total | 0.667 | 0.570 | 0.590 | 58 | 44 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ3 | team_total | 0.674 | 0.585 | 0.603 | 59 | 42 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT31TORVAN-8 | game_total | 0.411 | 0.320 | 0.337 | 33 | 69 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT31TORVAN-9 | game_total | 0.318 | 0.235 | 0.250 | 24 | 77 | yes | +0.065 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.716 | 0.795 | 0.781 | 80 | 21 | no | +0.062 | OK |
| KXNHLGAME-26OCT31TORVAN-TOR | game_winner | 0.552 | 0.635 | 0.619 | 64 | 37 | no | +0.061 | OK |
| KXNHLGAME-26OCT31TORVAN-VAN | game_winner | 0.448 | 0.365 | 0.381 | 37 | 64 | yes | +0.061 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ2 | game_spread | 0.313 | 0.235 | 0.249 | 24 | 77 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.363 | 0.455 | 0.436 | 47 | 56 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT4 | team_total | 0.323 | 0.405 | 0.388 | 41 | 60 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL2 | game_spread | 0.405 | 0.325 | 0.340 | 33 | 68 | yes | +0.059 | OK |
| KXNHLGAME-26OCT31TBNSH-NSH | game_winner | 0.455 | 0.375 | 0.391 | 38 | 63 | yes | +0.058 | OK |
| KXNHLGAME-26OCT31TBNSH-TB | game_winner | 0.545 | 0.625 | 0.609 | 63 | 38 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ4 | team_total | 0.464 | 0.380 | 0.396 | 39 | 63 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT3 | team_total | 0.537 | 0.615 | 0.600 | 62 | 39 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB3 | team_total | 0.621 | 0.700 | 0.685 | 71 | 31 | no | +0.054 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT2 | game_spread | 0.280 | 0.355 | 0.339 | 36 | 65 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ5 | team_total | 0.275 | 0.195 | 0.209 | 21 | 82 | yes | +0.053 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.284 | 0.215 | 0.228 | 22 | 79 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB2 | game_spread | 0.322 | 0.395 | 0.380 | 40 | 61 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT31TORVAN-7 | game_total | 0.609 | 0.535 | 0.550 | 54 | 47 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB3 | game_spread | 0.196 | 0.265 | 0.250 | 27 | 74 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT31TORVAN-10 | game_total | 0.176 | 0.115 | 0.126 | 12 | 89 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.705 | 0.635 | 0.650 | 64 | 37 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR3 | game_spread | 0.227 | 0.295 | 0.281 | 30 | 71 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN2 | game_spread | 0.260 | 0.195 | 0.207 | 20 | 81 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB5 | team_total | 0.218 | 0.290 | 0.274 | 30 | 72 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT2 | game_spread | 0.190 | 0.255 | 0.241 | 26 | 75 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT3 | game_spread | 0.105 | 0.165 | 0.151 | 17 | 84 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT31TORVAN-6 | game_total | 0.712 | 0.645 | 0.659 | 65 | 36 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.462 | 0.395 | 0.408 | 40 | 61 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.681 | 0.745 | 0.733 | 75 | 26 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN6 | team_total | 0.141 | 0.075 | 0.085 | 9 | 94 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR2 | game_spread | 0.348 | 0.415 | 0.401 | 42 | 59 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT3 | game_spread | 0.173 | 0.235 | 0.221 | 24 | 77 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.369 | 0.435 | 0.421 | 44 | 57 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN2 | team_total | 0.851 | 0.795 | 0.807 | 80 | 21 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.199 | 0.260 | 0.247 | 27 | 75 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT5 | team_total | 0.161 | 0.220 | 0.207 | 23 | 79 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ3 | game_spread | 0.196 | 0.145 | 0.154 | 15 | 86 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT2 | team_total | 0.762 | 0.820 | 0.809 | 83 | 19 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.258 | 0.200 | 0.211 | 21 | 81 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.213 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT31TBNSH-NSH2 | game_spread | 0.243 | 0.195 | 0.204 | 20 | 81 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB2 | team_total | 0.820 | 0.865 | 0.857 | 87 | 14 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ6 | team_total | 0.136 | 0.085 | 0.094 | 10 | 93 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-8 | game_total | 0.344 | 0.295 | 0.304 | 30 | 71 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ2 | team_total | 0.850 | 0.800 | 0.811 | 81 | 21 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.770 | 0.825 | 0.815 | 84 | 19 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL3 | team_total | 0.599 | 0.650 | 0.640 | 66 | 36 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT31TBNSH-5 | game_total | 0.753 | 0.795 | 0.787 | 80 | 21 | no | +0.025 | OK |
| KXNHLGAME-26OCT31CBJDAL-CBJ | game_winner | 0.411 | 0.365 | 0.374 | 37 | 64 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL2 | game_spread | 0.349 | 0.395 | 0.386 | 40 | 61 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL3 | game_spread | 0.266 | 0.220 | 0.229 | 23 | 79 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-7 | game_total | 0.340 | 0.385 | 0.376 | 39 | 62 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN3 | game_spread | 0.161 | 0.125 | 0.132 | 13 | 88 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.129 | 0.095 | 0.101 | 10 | 91 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-9 | game_total | 0.255 | 0.210 | 0.219 | 22 | 80 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL2 | team_total | 0.808 | 0.845 | 0.838 | 85 | 16 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT31TBNSH-4 | game_total | 0.840 | 0.875 | 0.869 | 88 | 13 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT31TBNSH-6 | game_total | 0.532 | 0.575 | 0.567 | 58 | 43 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT3 | team_total | 0.647 | 0.690 | 0.682 | 70 | 32 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL5 | team_total | 0.190 | 0.235 | 0.225 | 25 | 78 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL4 | team_total | 0.505 | 0.465 | 0.473 | 47 | 54 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI3 | team_total | 0.624 | 0.585 | 0.593 | 59 | 42 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL6 | team_total | 0.154 | 0.125 | 0.130 | 13 | 88 | yes | +0.016 | OK |
| KXNHLSPREAD-26OCT31EDMNYI-EDM3 | game_spread | 0.164 | 0.200 | 0.192 | 21 | 81 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-7 | game_total | 0.543 | 0.505 | 0.513 | 51 | 50 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT2 | team_total | 0.836 | 0.865 | 0.860 | 87 | 14 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-10 | game_total | 0.132 | 0.100 | 0.106 | 11 | 91 | yes | +0.015 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ NSH | 0.455 | 0.465 | 0.175 | 0.222 | 6.04 | 6.23 | 0.995/0.958 | KXNHLTOTAL-26OCT31TBNSH-7 +0.043 |
| EDM @ NYI | 0.511 | 0.484 | 0.179 | 0.219 | 6.32 | 6.67 | 0.948/1.023 | KXNHLTOTAL-26OCT31EDMNYI-7 +0.063 |
| BUF @ LAK | 0.485 | 0.542 | 0.181 | 0.223 | 6.24 | 6.19 | 0.993/0.998 | KXNHLGAME-26OCT31BUFLA-BUF -0.057 |
| OTT @ SJS | 0.519 | 0.503 | 0.168 | 0.215 | 6.78 | 6.50 | 1.035/1.051 | KXNHLTOTAL-26OCT31OTTSJ-8 -0.045 |
| PIT @ MTL | 0.628 | 0.520 | 0.167 | 0.213 | 6.44 | 6.62 | 0.983/1.012 | KXNHLGAME-26OCT31PITMTL-MTL -0.109 |
| TOR @ VAN | 0.448 | 0.502 | 0.160 | 0.211 | 7.23 | 6.67 | 1.021/0.956 | KXNHLTEAMTOTAL-26OCT31TORVAN-TOR4 -0.096 |
| CBJ @ DAL | 0.589 | 0.543 | 0.183 | 0.224 | 5.54 | 5.97 | 0.995/0.965 | KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3 +0.089 |
| CGY @ COL | 0.716 | 0.699 | 0.152 | 0.184 | 6.47 | 6.56 | 0.978/0.998 | KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 +0.028 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 28 recommended · full analysis in card.md / packet.json `thesis_card`

- Charle-Edouard D'Astous: 1+ goals NO @ 89c · p 0.9288 (adj 0.9166) · $12.36 · thesis TBL:SUPPRESSED
- Nils Hoglander: 1+ goals YES @ 11c · p 0.1429 (adj 0.1334) · $2.54 · thesis NSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3133 (adj 0.2962) · $4.16 · thesis NSH:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 74c · p 0.8091 (adj 0.7721) · $9.18 · thesis NSH:WINS
- Mattias Ekholm: 1+ goals YES @ 6c · p 0.1135 (adj 0.0964) · $4.47 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 13c · p 0.1785 (adj 0.1651) · $4.51 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 34c · p 0.4601 (adj 0.3788) · $7.76 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 26c · p 0.3017 (adj 0.29) · $4.97 · thesis EDM:OFFENSE_4PLUS
- Andre Lee: 1+ goals YES @ 9c · p 0.1247 (adj 0.1148) · $2.75 · thesis LAK:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0799 (adj 0.0674) · $1.79 · thesis LAK:WINS_BY_2PLUS
- Buffalo wins by over 1.5 goals NO @ 68c · p 0.7646 (adj 0.7198) · $10.84 · thesis LAK:WINS
- Rasmus Dahlin: 1+ goals NO @ 81c · p 0.8444 (adj 0.8333) · $8.35 · thesis BUF:SUPPRESSED
- Adam Gaudette: 1+ goals YES @ 13c · p 0.1693 (adj 0.1582) · $3.23 · thesis SJS:OFFENSE_4PLUS
- Tyler Toffoli: 1+ assists YES @ 24c · p 0.3249 (adj 0.2774) · $4.31 · thesis SJS:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1208 (adj 0.1106) · $2.29 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1592 (adj 0.1494) · $1.88 · thesis PIT:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2694 (adj 0.247) · $8.07 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 18c · p 0.2467 (adj 0.2263) · $6.28 · thesis VAN:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 72c · p 0.7837 (adj 0.764) · $12.36 · thesis TOR:SUPPRESSED
- Liam Ohgren: 1+ goals YES @ 16c · p 0.2113 (adj 0.1935) · $3.91 · thesis VAN:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.187 (adj 0.169) · $4.87 · thesis CBJ:OFFENSE_4PLUS
- Ryan Lomberg: 1+ goals YES @ 5c · p 0.077 (adj 0.069) · $2.18 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 20c · p 0.2534 (adj 0.2351) · $4.17 · thesis CBJ:OFFENSE_4PLUS
- Dallas wins by over 1.5 goals NO @ 61c · p 0.6892 (adj 0.6471) · $3.96 · thesis CBJ:WINS
- Jonathan Castagna: 1+ goals YES @ 8c · p 0.1113 (adj 0.101) · $2.34 · thesis CGY:OFFENSE_4PLUS
- Colorado wins by over 2.5 goals NO @ 53c · p 0.6539 (adj 0.5701) · $7.55 · thesis GAME:TIGHT
- Maxim Tsyplakov: 1+ goals YES @ 7c · p 0.0941 (adj 0.0856) · $1.57 · thesis CGY:OFFENSE_4PLUS
- Mackenzie Blackwood: 22+ saves YES @ 50c · p 0.6054 (adj 0.5369) · $7.35 · thesis COL:NET_HIGH_VOLUME

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TBL @ NSH** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROJECTED) exp shots 29.61, exp saves 25.47 (sd 6.86), pull risk 0.063
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.75, exp saves 22.29 (sd 6.24), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.466 | 0.625 | 63/38 | +0.138 | STANDARD |
| Nikita Kucherov: 2+ points | 0.284 | 0.415 | 42/59 | +0.109 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.134 | 0.245 | 27/78 | +0.074 | STANDARD |
| Nikita Kucherov: 1+ points | 0.642 | 0.730 | 76/30 | +0.044 | STANDARD |
| Nikita Kucherov: 3+ points | 0.094 | 0.180 | 19/83 | +0.066 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.313 | 0.245 | 26/77 | +0.040 | STANDARD |

**EDM @ NYI** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 27.15, exp saves 23.21 (sd 6.56), pull risk 0.075
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.76, exp saves 23.97 (sd 6.71), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.540 | 0.665 | 67/34 | +0.104 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.451 | 0.560 | 58/46 | +0.071 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.268 | 0.375 | 39/64 | +0.076 | STANDARD |
| Connor McDavid: 2+ assists | 0.189 | 0.295 | 30/71 | +0.086 | STANDARD |
| Leon Draisaitl: 2+ points | 0.324 | 0.430 | 44/58 | +0.079 | STANDARD |
| Connor McDavid: 2+ points | 0.391 | 0.485 | 49/52 | +0.071 | STANDARD |

**BUF @ LAK** · priced 210/211 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.66, exp saves 24.15 (sd 6.48), pull risk 0.054
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 28.05, exp saves 24.03 (sd 6.55), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ points | 0.291 | 0.095 | 17/98 | +0.111 | STANDARD |
| Mikey Anderson: 1+ points | 0.276 | 0.100 | 18/98 | +0.085 | STANDARD |
| Brian Dumoulin: 1+ points | 0.270 | 0.100 | 18/98 | +0.080 | STANDARD |
| Brian Dumoulin: 1+ assists | 0.237 | 0.085 | 15/98 | +0.078 | STANDARD |
| Joel Edmundson: 1+ assists | 0.227 | 0.075 | 13/98 | +0.089 | STANDARD |
| Mikey Anderson: 1+ assists | 0.233 | 0.090 | 16/98 | +0.063 | STANDARD |

**OTT @ SJS** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.35, exp saves 24.29 (sd 6.78), pull risk 0.071
- OTT net: Samuel Ersson (PROJECTED) exp shots 25.93, exp saves 22.44 (sd 6.25), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 2+ points | 0.293 | 0.395 | 40/61 | +0.080 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.445 | 0.545 | 56/47 | +0.068 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.325 | 0.230 | 24/78 | +0.072 | STANDARD |
| Collin Graf: 1+ assists | 0.278 | 0.190 | 22/84 | +0.046 | STANDARD |
| Tim Stutzle: 2+ points | 0.268 | 0.350 | 36/66 | +0.056 | STANDARD |
| Ivar Stenberg: 1+ points | 0.402 | 0.480 | 49/53 | +0.051 | STANDARD |

**PIT @ MTL** · priced 203/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.16, exp saves 24.42 (sd 6.68), pull risk 0.067
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.26, exp saves 22.49 (sd 6.49), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Spencer Stastney: 1+ assists | 0.181 | 0.500 | 99/99 | -0.172 | STANDARD |
| Spencer Stastney: 1+ points | 0.217 | 0.500 | 99/99 | -0.208 | STANDARD |
| Sergei Murashov: 27+ saves | 0.259 | 0.395 | 50/71 | +0.016 |  |
| Samuel Girard: 1+ assists | 0.231 | 0.140 | 26/98 | -0.043 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.303 | 0.230 | 25/79 | +0.040 | STANDARD |
| Jacob Fowler: 23+ saves | 0.617 | 0.550 | 58/48 | +0.020 |  |

**TOR @ VAN** · priced 160/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.88, exp saves 24.85 (sd 6.73), pull risk 0.069
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 28.15, exp saves 24.18 (sd 6.78), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Nylander: 4+ points | 0.018 | 0.240 | 47/99 | -0.009 | STANDARD |
| Auston Matthews: 1+ assists | 0.406 | 0.525 | 54/49 | +0.086 | STANDARD |
| Linus Karlsson: 1+ points | 0.494 | 0.375 | 40/65 | +0.077 | STANDARD |
| Auston Matthews: 2+ points | 0.289 | 0.400 | 42/62 | +0.074 | STANDARD |
| William Nylander: 1+ assists | 0.411 | 0.520 | 54/50 | +0.071 | STANDARD |
| Anthony Stolarz: 25+ saves | 0.480 | 0.375 | 44/69 | +0.022 |  |

**CBJ @ DAL** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.99, exp saves 21.76 (sd 6.03), pull risk 0.051
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.69, exp saves 23.04 (sd 6.37), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Sillinger: 1+ points | 0.348 | 0.250 | 27/77 | +0.065 | STANDARD |
| Miro Heiskanen: 1+ points | 0.456 | 0.545 | 57/48 | +0.046 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.436 | 0.520 | 54/50 | +0.047 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.221 | 0.305 | 33/72 | +0.045 | STANDARD |
| Mathieu Olivier: 1+ points | 0.343 | 0.265 | 29/76 | +0.039 | STANDARD |
| Cole Sillinger: 1+ assists | 0.243 | 0.165 | 19/86 | +0.042 | STANDARD |

**CGY @ COL** · priced 175/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROBABLE) exp shots 26.33, exp saves 23.36 (sd 6.32), pull risk 0.043
- CGY net: Dustin Wolf (PROJECTED) exp shots 33.08, exp saves 27.7 (sd 7.65), pull risk 0.101

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.417 | 0.525 | 53/48 | +0.086 | STANDARD |
| Cale Makar: 1+ assists | 0.482 | 0.585 | 61/44 | +0.061 | STANDARD |
| Artturi Lehkonen: 2+ points | 0.232 | 0.135 | 23/96 | -0.010 | STANDARD |
| Cale Makar: 1+ points | 0.588 | 0.680 | 70/34 | +0.056 | STANDARD |
| Cale Makar: 2+ assists | 0.139 | 0.230 | 25/79 | +0.059 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.544 | 0.635 | 66/39 | +0.049 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
