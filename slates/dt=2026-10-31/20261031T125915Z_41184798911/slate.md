# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T12:59:15Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 3891 · contracts joined: 1980 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1730, 'NO_EDGE': 105, 'OK': 145}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 260, 'game_early_goal': 10, 'first_goal': 306, 'game_winner': 20, 'player_goals': 561, 'game_overtime': 10, 'player_points': 343, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BOS | 2026-10-31T17:00:00Z | T-3h | 0.700 | 0.300 | 0.152 | 6.13 | 3.72 | 2.41 | 220 (25/195) | PROJECTED/PROJECTED |
| STL @ DET | 2026-10-31T17:00:00Z | T-3h | 0.511 | 0.489 | 0.180 | 5.78 | 2.92 | 2.86 | 199 (25/174) | CONFIRMED/PROJECTED |
| TBL @ NSH | 2026-10-31T18:00:00Z | T-3h | 0.455 | 0.545 | 0.175 | 6.04 | 2.88 | 3.16 | 216 (25/191) | PROJECTED/PROJECTED |
| EDM @ NYI | 2026-10-31T18:00:00Z | T-3h | 0.497 | 0.503 | 0.166 | 6.41 | 3.19 | 3.22 | 215 (25/190) | PROJECTED/CONFIRMED |
| BUF @ LAK | 2026-10-31T20:00:00Z | T-6h | 0.518 | 0.482 | 0.176 | 6.02 | 3.07 | 2.95 | 216 (25/191) | PROJECTED/PROJECTED |
| OTT @ SJS | 2026-10-31T20:00:00Z | T-6h | 0.519 | 0.481 | 0.168 | 6.78 | 3.45 | 3.33 | 219 (25/194) | PROJECTED/PROJECTED |
| PIT @ MTL | 2026-10-31T23:00:00Z | T-6h | 0.600 | 0.400 | 0.166 | 6.50 | 3.56 | 2.94 | 219 (25/194) | PROJECTED/PROJECTED |
| TOR @ VAN | 2026-10-31T23:00:00Z | T-6h | 0.448 | 0.552 | 0.160 | 7.23 | 3.45 | 3.79 | 218 (25/193) | PROJECTED/CONFIRMED |
| CBJ @ DAL | 2026-11-01T00:00:00Z | T-6h | 0.584 | 0.416 | 0.184 | 5.58 | 3.04 | 2.54 | 207 (25/182) | PROJECTED/PROJECTED |
| CGY @ COL | 2026-11-01T02:00:00Z | T-12h | 0.712 | 0.288 | 0.150 | 6.49 | 3.95 | 2.54 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.349 | 0.475 | 0.449 | 48 | 53 | no | +0.104 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.498 | 0.600 | 0.580 | 61 | 41 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3 | team_total | 0.667 | 0.570 | 0.590 | 58 | 44 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ3 | team_total | 0.674 | 0.585 | 0.603 | 59 | 42 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT31TORVAN-8 | game_total | 0.411 | 0.320 | 0.337 | 33 | 69 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT31TORVAN-9 | game_total | 0.318 | 0.235 | 0.250 | 24 | 77 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4 | team_total | 0.461 | 0.370 | 0.388 | 38 | 64 | yes | +0.064 | OK |
| KXNHLGAME-26OCT31OTTSJ-SJ | game_winner | 0.519 | 0.435 | 0.452 | 44 | 57 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ4 | team_total | 0.464 | 0.385 | 0.400 | 39 | 62 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ5 | team_total | 0.275 | 0.195 | 0.209 | 21 | 82 | yes | +0.053 | OK |
| KXNHLGAME-26OCT31OTTSJ-OTT | game_winner | 0.481 | 0.555 | 0.540 | 56 | 45 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.708 | 0.630 | 0.646 | 64 | 38 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB3 | game_spread | 0.196 | 0.265 | 0.250 | 27 | 74 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ2 | game_spread | 0.313 | 0.245 | 0.258 | 25 | 76 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.574 | 0.655 | 0.639 | 67 | 36 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN5 | team_total | 0.271 | 0.195 | 0.209 | 21 | 82 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT31TORVAN-10 | game_total | 0.176 | 0.115 | 0.126 | 12 | 89 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.365 | 0.445 | 0.429 | 46 | 57 | no | +0.048 | OK |
| KXNHLGAME-26OCT31TBNSH-NSH | game_winner | 0.455 | 0.385 | 0.399 | 39 | 62 | yes | +0.048 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.288 | 0.225 | 0.237 | 23 | 78 | yes | +0.046 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.712 | 0.775 | 0.763 | 78 | 23 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT31TORVAN-6 | game_total | 0.712 | 0.640 | 0.655 | 65 | 37 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB4 | team_total | 0.398 | 0.465 | 0.451 | 47 | 54 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN6 | team_total | 0.141 | 0.080 | 0.090 | 9 | 93 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT3 | game_spread | 0.173 | 0.235 | 0.221 | 24 | 77 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT2 | game_spread | 0.280 | 0.345 | 0.331 | 35 | 66 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.371 | 0.440 | 0.426 | 45 | 57 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.205 | 0.270 | 0.256 | 28 | 74 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB2 | game_spread | 0.322 | 0.385 | 0.372 | 39 | 62 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT31TORVAN-7 | game_total | 0.609 | 0.545 | 0.558 | 55 | 46 | yes | +0.041 | OK |
| KXNHLGAME-26OCT31TORVAN-TOR | game_winner | 0.552 | 0.615 | 0.603 | 62 | 39 | no | +0.041 | OK |
| KXNHLGAME-26OCT31TORVAN-VAN | game_winner | 0.448 | 0.385 | 0.397 | 39 | 62 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ6 | team_total | 0.136 | 0.080 | 0.089 | 9 | 93 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.467 | 0.395 | 0.409 | 41 | 62 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.261 | 0.200 | 0.211 | 21 | 81 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT31STLDET-5 | game_total | 0.719 | 0.775 | 0.764 | 78 | 23 | no | +0.039 | OK |
| KXNHLGAME-26OCT31TBNSH-TB | game_winner | 0.545 | 0.610 | 0.597 | 62 | 40 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.689 | 0.745 | 0.734 | 75 | 26 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.200 | 0.260 | 0.247 | 27 | 75 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL3 | team_total | 0.598 | 0.655 | 0.644 | 66 | 35 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL4 | team_total | 0.330 | 0.390 | 0.378 | 40 | 62 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB3 | team_total | 0.621 | 0.685 | 0.673 | 70 | 33 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT31BUFLA-BUF3 | game_spread | 0.155 | 0.205 | 0.194 | 21 | 80 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL2 | game_spread | 0.342 | 0.395 | 0.384 | 40 | 61 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT31STLDET-4 | game_total | 0.810 | 0.860 | 0.851 | 87 | 15 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31BUFLA-BUF3 | team_total | 0.573 | 0.625 | 0.615 | 63 | 38 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL3 | team_total | 0.552 | 0.610 | 0.599 | 62 | 40 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.769 | 0.820 | 0.810 | 83 | 19 | no | +0.031 | OK |
| KXNHLGAME-26OCT31BUFLA-LA | game_winner | 0.518 | 0.465 | 0.476 | 47 | 54 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-8 | game_total | 0.344 | 0.295 | 0.304 | 30 | 71 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR3 | game_spread | 0.227 | 0.275 | 0.265 | 28 | 73 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB5 | team_total | 0.218 | 0.270 | 0.259 | 28 | 74 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT31STLDET-STL3 | game_spread | 0.151 | 0.195 | 0.185 | 20 | 81 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN2 | game_spread | 0.260 | 0.215 | 0.223 | 22 | 79 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5 | team_total | 0.122 | 0.080 | 0.087 | 9 | 93 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR2 | game_spread | 0.348 | 0.395 | 0.385 | 40 | 61 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI5 | team_total | 0.226 | 0.175 | 0.184 | 19 | 84 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.130 | 0.095 | 0.101 | 10 | 91 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL2 | team_total | 0.808 | 0.850 | 0.842 | 86 | 16 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-9 | game_total | 0.255 | 0.210 | 0.219 | 22 | 80 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT31STLDET-7 | game_total | 0.380 | 0.425 | 0.416 | 43 | 58 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT31TBNSH-NSH2 | game_spread | 0.243 | 0.205 | 0.212 | 21 | 80 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-6 | game_total | 0.648 | 0.605 | 0.614 | 61 | 40 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT31BUFLA-BUF2 | game_spread | 0.264 | 0.305 | 0.297 | 31 | 70 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB2 | team_total | 0.820 | 0.855 | 0.849 | 86 | 15 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT31TBNSH-6 | game_total | 0.532 | 0.575 | 0.567 | 58 | 43 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN2 | team_total | 0.851 | 0.810 | 0.819 | 82 | 20 | yes | +0.020 | OK |
| KXNHLGAME-26OCT31BUFLA-BUF | game_winner | 0.482 | 0.525 | 0.516 | 53 | 48 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI4 | team_total | 0.406 | 0.365 | 0.373 | 37 | 64 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI6 | team_total | 0.105 | 0.070 | 0.076 | 8 | 94 | yes | +0.020 | OK |
| KXNHLGAME-26OCT31CBJDAL-CBJ | game_winner | 0.416 | 0.375 | 0.383 | 38 | 63 | yes | +0.020 | OK |
| KXNHLGAME-26OCT31CBJDAL-DAL | game_winner | 0.584 | 0.625 | 0.617 | 63 | 38 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT31BUFLA-BUF4 | team_total | 0.354 | 0.400 | 0.391 | 41 | 61 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT31BUFLA-BUF5 | team_total | 0.179 | 0.220 | 0.211 | 23 | 79 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ2 | team_total | 0.850 | 0.810 | 0.819 | 82 | 20 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT31BUFLA-5 | game_total | 0.749 | 0.785 | 0.778 | 79 | 22 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL5 | team_total | 0.161 | 0.200 | 0.192 | 21 | 81 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL2 | team_total | 0.908 | 0.940 | 0.935 | 95 | 7 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL5 | team_total | 0.191 | 0.235 | 0.226 | 25 | 78 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT31EDMNYI-EDM3 | game_spread | 0.181 | 0.220 | 0.212 | 23 | 79 | no | +0.017 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BOS | 0.700 | 0.673 | 0.152 | 0.199 | 6.13 | 6.49 | 0.969/1.026 | KXNHLTEAMTOTAL-26OCT31CHIBOS-CHI3 +0.069 |
| STL @ DET | 0.511 | 0.498 | 0.180 | 0.216 | 5.78 | 6.11 | 0.995/0.994 | KXNHLTOTAL-26OCT31STLDET-7 +0.054 |
| TBL @ NSH | 0.455 | 0.465 | 0.175 | 0.222 | 6.04 | 6.23 | 0.995/0.958 | KXNHLTOTAL-26OCT31TBNSH-7 +0.043 |
| EDM @ NYI | 0.497 | 0.483 | 0.166 | 0.216 | 6.41 | 6.70 | 0.957/1.023 | KXNHLTOTAL-26OCT31EDMNYI-7 +0.051 |
| BUF @ LAK | 0.518 | 0.545 | 0.176 | 0.217 | 6.02 | 6.19 | 0.990/0.998 | KXNHLTEAMTOTAL-26OCT31BUFLA-LA4 +0.040 |
| OTT @ SJS | 0.519 | 0.503 | 0.168 | 0.215 | 6.78 | 6.50 | 1.035/1.051 | KXNHLTOTAL-26OCT31OTTSJ-8 -0.045 |
| PIT @ MTL | 0.600 | 0.528 | 0.166 | 0.212 | 6.50 | 6.63 | 0.976/1.021 | KXNHLGAME-26OCT31PITMTL-MTL -0.072 |
| TOR @ VAN | 0.448 | 0.502 | 0.160 | 0.211 | 7.23 | 6.67 | 1.021/0.956 | KXNHLTEAMTOTAL-26OCT31TORVAN-TOR4 -0.096 |
| CBJ @ DAL | 0.584 | 0.549 | 0.184 | 0.220 | 5.58 | 5.95 | 0.987/0.965 | KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3 +0.071 |
| CGY @ COL | 0.712 | 0.698 | 0.150 | 0.191 | 6.49 | 6.57 | 0.977/0.998 | KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 +0.023 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 31 recommended · full analysis in card.md / packet.json `thesis_card`

- Casey Mittelstadt: 1+ goals YES @ 16c · p 0.2122 (adj 0.1979) · $5.24 · thesis BOS:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 22c · p 0.265 (adj 0.2513) · $3.8 · thesis CHI:OFFENSE_4PLUS
- Oliver Moore: 1+ goals YES @ 11c · p 0.1486 (adj 0.1315) · $2.36 · thesis CHI:OFFENSE_4PLUS
- Roman Kantserov: 1+ goals NO @ 76c · p 0.7937 (adj 0.784) · $8.12 · thesis CHI:SUPPRESSED
- Sheldon Dries: 1+ goals YES @ 7c · p 0.1046 (adj 0.091) · $2.5 · thesis DET:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 28c · p 0.3292 (adj 0.3144) · $4.62 · thesis STL:OFFENSE_4PLUS
- Lucas Raymond: 1+ assists NO @ 58c · p 0.6575 (adj 0.6162) · $9.96 · thesis DET:SUPPRESSED
- Alex DeBrincat: 1+ goals YES @ 36c · p 0.4085 (adj 0.3939) · $5.52 · thesis DET:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3133 (adj 0.2975) · $4.66 · thesis NSH:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 74c · p 0.8091 (adj 0.7721) · $11.7 · thesis NSH:WINS
- Mattias Ekholm: 1+ goals YES @ 7c · p 0.1232 (adj 0.1049) · $4.54 · thesis EDM:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 12c · p 0.1822 (adj 0.1604) · $5.21 · thesis NYI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 22c · p 0.2738 (adj 0.2591) · $5.32 · thesis NYI:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 33c · p 0.4492 (adj 0.3685) · $6.49 · thesis EDM:SUPPRESSED
- Alex Laferriere: 2+ goals YES @ 3c · p 0.0541 (adj 0.0468) · $2.06 · thesis LAK:OFFENSE_4PLUS
- Corey Perry: 1+ goals YES @ 14c · p 0.1826 (adj 0.1645) · $2.81 · thesis LAK:OFFENSE_4PLUS
- Andre Lee: 1+ goals YES @ 10c · p 0.1311 (adj 0.1183) · $1.98 · thesis LAK:OFFENSE_4PLUS
- Scott Laughton: 1+ goals YES @ 13c · p 0.1618 (adj 0.1513) · $2.46 · thesis LAK:OFFENSE_4PLUS
- Claude Giroux: 1+ goals YES @ 18c · p 0.2148 (adj 0.2011) · $2.04 · thesis OTT:OFFENSE_4PLUS
- Tyler Toffoli: 1+ assists YES @ 25c · p 0.3249 (adj 0.275) · $2.34 · thesis SJS:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.1656 (adj 0.1454) · $2.99 · thesis PIT:OFFENSE_4PLUS
- Toronto wins by over 2.5 goals NO @ 73c · p 0.8211 (adj 0.7731) · $13.09 · thesis VAN:WINS
- Linus Karlsson: 1+ goals YES @ 21c · p 0.2694 (adj 0.2458) · $4.28 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 20c · p 0.2467 (adj 0.2313) · $3.44 · thesis VAN:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 74c · p 0.7842 (adj 0.7669) · $7.3 · thesis TOR:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 21c · p 0.2609 (adj 0.2457) · $4.34 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 14c · p 0.1838 (adj 0.1641) · $2.37 · thesis CBJ:OFFENSE_4PLUS
- Dallas wins by over 1.5 goals NO @ 61c · p 0.6904 (adj 0.6477) · $6.63 · thesis GAME:TIGHT
- Calgary over 3.5 goals scored YES @ 21c · p 0.2795 (adj 0.2398) · $2.14 · thesis CGY:OFFENSE_4PLUS
- Colorado wins by over 2.5 goals NO @ 53c · p 0.6499 (adj 0.5687) · $4.31 · thesis GAME:TIGHT
- Colorado over 5.5 goals scored NO @ 75c · p 0.8074 (adj 0.7737) · $4.62 · thesis CGY:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BOS** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 25.06, exp saves 22.16 (sd 6.06), pull risk 0.044
- CHI net: Arvid Soderblom (PROJECTED) exp shots 28.59, exp saves 24.0 (sd 6.9), pull risk 0.098

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.288 | 0.410 | 43/61 | +0.085 | STANDARD |
| Connor Bedard: 1+ assists | 0.345 | 0.445 | 46/57 | +0.067 | STANDARD |
| David Pastrnak: 2+ points | 0.339 | 0.425 | 44/59 | +0.054 | STANDARD |
| Patrick Kane: 1+ points | 0.435 | 0.520 | 53/49 | +0.058 | STANDARD |
| Connor Bedard: 1+ points | 0.525 | 0.605 | 62/41 | +0.048 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.436 | 0.505 | 52/51 | +0.037 | STANDARD |

**STL @ DET** · priced 140/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.58, exp saves 22.11 (sd 6.22), pull risk 0.06
- STL net: Joel Hofer (PROJECTED) exp shots 28.81, exp saves 24.9 (sd 6.7), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Holloway: 1+ assists | 0.386 | 0.295 | 31/72 | +0.061 | STANDARD |
| Lucas Raymond: 1+ assists | 0.343 | 0.425 | 43/58 | +0.060 | STANDARD |
| Dylan Holloway: 1+ points | 0.550 | 0.470 | 50/56 | +0.032 | STANDARD |
| Moritz Seider: 1+ assists | 0.399 | 0.470 | 49/55 | +0.033 | STANDARD |
| Dylan Holloway: 2+ points | 0.200 | 0.130 | 17/91 | +0.020 | STANDARD |
| Lucas Raymond: 1+ points | 0.516 | 0.585 | 60/43 | +0.037 | STANDARD |

**TBL @ NSH** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROJECTED) exp shots 29.61, exp saves 25.47 (sd 6.86), pull risk 0.063
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.75, exp saves 22.29 (sd 6.24), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.466 | 0.605 | 63/42 | +0.097 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.134 | 0.250 | 27/77 | +0.084 | STANDARD |
| Nikita Kucherov: 2+ points | 0.284 | 0.395 | 42/63 | +0.069 | STANDARD |
| Ryan O'Reilly: 2+ points | 0.236 | 0.160 | 20/88 | +0.025 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.313 | 0.250 | 26/76 | +0.040 | STANDARD |
| Nikita Kucherov: 1+ points | 0.642 | 0.705 | 73/32 | +0.023 | STANDARD |

**EDM @ NYI** · priced 161/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.15, exp saves 23.23 (sd 6.5), pull risk 0.077
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.76, exp saves 23.98 (sd 6.67), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.551 | 0.675 | 68/33 | +0.104 | STANDARD |
| Connor McDavid: 2+ assists | 0.193 | 0.305 | 32/71 | +0.083 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.462 | 0.565 | 58/45 | +0.071 | STANDARD |
| Logan Stanley: 1+ points | 0.334 | 0.235 | 26/79 | +0.061 | STANDARD |
| Connor McDavid: 2+ points | 0.397 | 0.495 | 50/51 | +0.076 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.276 | 0.370 | 40/66 | +0.048 | STANDARD |

**BUF @ LAK** · priced 158/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 27.66, exp saves 24.12 (sd 6.48), pull risk 0.054
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 28.05, exp saves 24.01 (sd 6.58), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Laferriere: 2+ points | 0.235 | 0.145 | 20/91 | +0.024 | STANDARD |
| Trevor Moore: 1+ points | 0.480 | 0.390 | 42/64 | +0.043 | STANDARD |
| Trevor Moore: 1+ assists | 0.330 | 0.240 | 26/78 | +0.056 | STANDARD |
| Tage Thompson: 1+ points | 0.537 | 0.615 | 63/40 | +0.046 | STANDARD |
| Tage Thompson: 1+ assists | 0.317 | 0.395 | 42/63 | +0.036 | STANDARD |
| Corey Perry: 1+ goals | 0.183 | 0.110 | 14/92 | +0.034 | STANDARD |

**OTT @ SJS** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.35, exp saves 24.29 (sd 6.78), pull risk 0.071
- OTT net: Samuel Ersson (PROJECTED) exp shots 25.93, exp saves 22.44 (sd 6.25), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tyler Toffoli: 1+ assists | 0.325 | 0.225 | 25/80 | +0.062 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.445 | 0.540 | 55/47 | +0.068 | STANDARD |
| Collin Graf: 1+ points | 0.421 | 0.335 | 37/70 | +0.035 | STANDARD |
| Tyler Toffoli: 1+ points | 0.464 | 0.380 | 41/65 | +0.037 | STANDARD |
| Collin Graf: 1+ assists | 0.278 | 0.205 | 23/82 | +0.036 | STANDARD |
| Ivar Stenberg: 1+ points | 0.402 | 0.475 | 50/55 | +0.031 | STANDARD |

**PIT @ MTL** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 28.16, exp saves 24.48 (sd 6.69), pull risk 0.065
- PIT net: Sergei Murashov (PROJECTED) exp shots 26.26, exp saves 22.49 (sd 6.46), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor Dewar: 1+ goals | 0.166 | 0.085 | 12/95 | +0.038 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.276 | 0.205 | 23/82 | +0.034 | STANDARD |
| Egor Chinakhov: 1+ points | 0.437 | 0.370 | 41/67 | +0.010 | STANDARD |
| Egor Chinakhov: 1+ goals | 0.220 | 0.155 | 21/90 | -0.002 | STANDARD |
| Nick Robertson: 1+ goals | 0.184 | 0.120 | 16/92 | +0.015 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.297 | 0.235 | 26/79 | +0.024 | STANDARD |

**TOR @ VAN** · priced 151/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.88, exp saves 24.85 (sd 6.73), pull risk 0.069
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 28.15, exp saves 24.18 (sd 6.78), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 2+ points | 0.288 | 0.390 | 42/64 | +0.056 | STANDARD |
| Auston Matthews: 1+ assists | 0.408 | 0.510 | 54/52 | +0.055 | STANDARD |
| Troy Stecher: 1+ points | 0.306 | 0.205 | 23/82 | +0.064 | STANDARD |
| William Nylander: 1+ assists | 0.415 | 0.510 | 54/52 | +0.047 | STANDARD |
| Linus Karlsson: 1+ goals | 0.269 | 0.175 | 21/86 | +0.048 | STANDARD |
| Troy Stecher: 1+ assists | 0.254 | 0.160 | 18/86 | +0.063 | STANDARD |

**CBJ @ DAL** · priced 155/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.99, exp saves 21.81 (sd 6.06), pull risk 0.047
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.69, exp saves 23.03 (sd 6.41), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Valeri Nichushkin: 1+ assists | 0.211 | 0.315 | 34/71 | +0.065 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.449 | 0.530 | 54/48 | +0.054 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.184 | 0.105 | 14/93 | +0.035 | STANDARD |
| Charlie Coyle: 1+ points | 0.521 | 0.445 | 47/58 | +0.034 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.420 | 0.495 | 51/52 | +0.042 | STANDARD |
| Mikko Rantanen: 1+ points | 0.597 | 0.660 | 69/37 | +0.017 | STANDARD |

**CGY @ COL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.33, exp saves 23.35 (sd 6.28), pull risk 0.043
- CGY net: Dustin Wolf (PROJECTED) exp shots 33.08, exp saves 27.67 (sd 7.88), pull risk 0.104

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
