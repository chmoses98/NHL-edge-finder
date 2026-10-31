# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T16:43:25Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 4194 · contracts joined: 2283 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2033, 'NO_EDGE': 95, 'OK': 155}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 335, 'game_early_goal': 10, 'first_goal': 357, 'game_winner': 20, 'player_goals': 620, 'game_overtime': 10, 'player_points': 454, 'goalie_saves': 7, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BOS | 2026-10-31T17:00:00Z | T-10m | 0.692 | 0.308 | 0.153 | 6.19 | 3.72 | 2.47 | 224 (25/199) | CONFIRMED/PROJECTED |
| STL @ DET | 2026-10-31T17:00:00Z | T-10m | 0.505 | 0.495 | 0.188 | 5.76 | 2.89 | 2.87 | 224 (25/199) | CONFIRMED/PROBABLE |
| TBL @ NSH | 2026-10-31T18:00:00Z | T-60m | 0.455 | 0.545 | 0.175 | 6.04 | 2.88 | 3.16 | 216 (25/191) | PROJECTED/PROJECTED |
| EDM @ NYI | 2026-10-31T18:00:00Z | T-60m | 0.497 | 0.503 | 0.166 | 6.41 | 3.19 | 3.22 | 214 (25/189) | PROJECTED/CONFIRMED |
| BUF @ LAK | 2026-10-31T20:00:00Z | T-3h | 0.485 | 0.515 | 0.181 | 6.24 | 3.07 | 3.17 | 251 (25/226) | PROJECTED/PROJECTED |
| OTT @ SJS | 2026-10-31T20:00:00Z | T-3h | 0.519 | 0.481 | 0.168 | 6.78 | 3.45 | 3.33 | 225 (25/200) | PROJECTED/PROJECTED |
| PIT @ MTL | 2026-10-31T23:00:00Z | T-6h | 0.628 | 0.372 | 0.167 | 6.44 | 3.63 | 2.82 | 254 (25/229) | CONFIRMED/CONFIRMED |
| TOR @ VAN | 2026-10-31T23:00:00Z | T-6h | 0.448 | 0.552 | 0.160 | 7.23 | 3.45 | 3.79 | 225 (25/200) | PROJECTED/CONFIRMED |
| CBJ @ DAL | 2026-11-01T00:00:00Z | T-6h | 0.589 | 0.411 | 0.183 | 5.54 | 3.04 | 2.50 | 221 (25/196) | CONFIRMED/PROJECTED |
| CGY @ COL | 2026-11-01T02:00:00Z | T-6h | 0.712 | 0.288 | 0.150 | 6.49 | 3.95 | 2.54 | 229 (25/204) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.349 | 0.475 | 0.449 | 48 | 53 | no | +0.104 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.498 | 0.605 | 0.584 | 61 | 40 | no | +0.085 | OK |
| KXNHLGAME-26OCT31PITMTL-MTL | game_winner | 0.628 | 0.525 | 0.546 | 53 | 48 | yes | +0.081 | OK |
| KXNHLGAME-26OCT31PITMTL-PIT | game_winner | 0.372 | 0.475 | 0.454 | 48 | 53 | no | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB4 | team_total | 0.398 | 0.495 | 0.475 | 50 | 51 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4 | team_total | 0.461 | 0.360 | 0.379 | 37 | 65 | yes | +0.074 | OK |
| KXNHLGAME-26OCT31OTTSJ-OTT | game_winner | 0.481 | 0.575 | 0.556 | 58 | 43 | no | +0.072 | OK |
| KXNHLGAME-26OCT31OTTSJ-SJ | game_winner | 0.519 | 0.425 | 0.444 | 43 | 58 | yes | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN5 | team_total | 0.271 | 0.180 | 0.196 | 19 | 83 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.574 | 0.670 | 0.652 | 68 | 34 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3 | team_total | 0.667 | 0.570 | 0.590 | 58 | 44 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ3 | team_total | 0.674 | 0.585 | 0.603 | 59 | 42 | yes | +0.067 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.288 | 0.205 | 0.220 | 21 | 80 | yes | +0.067 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.712 | 0.795 | 0.780 | 80 | 21 | no | +0.067 | OK |
| KXNHLTOTAL-26OCT31TORVAN-8 | game_total | 0.411 | 0.320 | 0.337 | 33 | 69 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ5 | team_total | 0.275 | 0.190 | 0.205 | 20 | 82 | yes | +0.064 | OK |
| KXNHLGAME-26OCT31TORVAN-TOR | game_winner | 0.552 | 0.635 | 0.619 | 64 | 37 | no | +0.061 | OK |
| KXNHLGAME-26OCT31TORVAN-VAN | game_winner | 0.448 | 0.365 | 0.381 | 37 | 64 | yes | +0.061 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ2 | game_spread | 0.313 | 0.235 | 0.249 | 24 | 77 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT4 | team_total | 0.323 | 0.405 | 0.388 | 41 | 60 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL2 | game_spread | 0.405 | 0.325 | 0.340 | 33 | 68 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.365 | 0.455 | 0.436 | 47 | 56 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ4 | team_total | 0.464 | 0.380 | 0.396 | 39 | 63 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT3 | team_total | 0.537 | 0.615 | 0.600 | 62 | 39 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN6 | team_total | 0.141 | 0.070 | 0.081 | 8 | 94 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT31TORVAN-9 | game_total | 0.318 | 0.240 | 0.255 | 25 | 77 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB3 | team_total | 0.621 | 0.700 | 0.685 | 71 | 31 | no | +0.054 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT2 | game_spread | 0.280 | 0.355 | 0.339 | 36 | 65 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.708 | 0.635 | 0.650 | 64 | 37 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB2 | game_spread | 0.322 | 0.395 | 0.380 | 40 | 61 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT31TORVAN-7 | game_total | 0.609 | 0.535 | 0.550 | 54 | 47 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB3 | game_spread | 0.196 | 0.265 | 0.250 | 27 | 74 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.467 | 0.395 | 0.409 | 40 | 61 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT31TORVAN-10 | game_total | 0.176 | 0.115 | 0.126 | 12 | 89 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR3 | game_spread | 0.227 | 0.295 | 0.281 | 30 | 71 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN2 | game_spread | 0.260 | 0.195 | 0.207 | 20 | 81 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB5 | team_total | 0.218 | 0.285 | 0.271 | 29 | 72 | no | +0.048 | OK |
| KXNHLGAME-26OCT31TBNSH-NSH | game_winner | 0.455 | 0.385 | 0.399 | 39 | 62 | yes | +0.048 | OK |
| KXNHLGAME-26OCT31TBNSH-TB | game_winner | 0.545 | 0.615 | 0.601 | 62 | 39 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT2 | game_spread | 0.190 | 0.260 | 0.245 | 27 | 75 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT3 | game_spread | 0.105 | 0.165 | 0.151 | 17 | 84 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT31TORVAN-6 | game_total | 0.712 | 0.645 | 0.659 | 65 | 36 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.681 | 0.745 | 0.733 | 75 | 26 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR2 | game_spread | 0.348 | 0.415 | 0.401 | 42 | 59 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT3 | game_spread | 0.173 | 0.235 | 0.221 | 24 | 77 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ6 | team_total | 0.136 | 0.080 | 0.089 | 9 | 93 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.261 | 0.200 | 0.211 | 21 | 81 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN2 | team_total | 0.851 | 0.795 | 0.807 | 80 | 21 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.200 | 0.260 | 0.247 | 27 | 75 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT5 | team_total | 0.161 | 0.220 | 0.207 | 23 | 79 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ3 | game_spread | 0.196 | 0.145 | 0.154 | 15 | 86 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT2 | team_total | 0.762 | 0.820 | 0.809 | 83 | 19 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.369 | 0.430 | 0.417 | 44 | 58 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.213 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT31TBNSH-NSH2 | game_spread | 0.243 | 0.195 | 0.204 | 20 | 81 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB2 | team_total | 0.820 | 0.865 | 0.857 | 87 | 14 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.769 | 0.825 | 0.815 | 84 | 19 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT31STLDET-4 | game_total | 0.811 | 0.855 | 0.847 | 86 | 15 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-8 | game_total | 0.344 | 0.295 | 0.304 | 30 | 71 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ2 | team_total | 0.850 | 0.805 | 0.815 | 81 | 20 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT31STLDET-5 | game_total | 0.721 | 0.765 | 0.757 | 77 | 24 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5 | team_total | 0.122 | 0.080 | 0.087 | 9 | 93 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL3 | team_total | 0.599 | 0.650 | 0.640 | 66 | 36 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT31TBNSH-5 | game_total | 0.753 | 0.795 | 0.787 | 80 | 21 | no | +0.025 | OK |
| KXNHLGAME-26OCT31CBJDAL-CBJ | game_winner | 0.411 | 0.365 | 0.374 | 37 | 64 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL2 | game_spread | 0.349 | 0.395 | 0.386 | 40 | 61 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.130 | 0.095 | 0.101 | 10 | 91 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL3 | game_spread | 0.266 | 0.220 | 0.229 | 23 | 79 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-7 | game_total | 0.340 | 0.385 | 0.376 | 39 | 62 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT31TBNSH-7 | game_total | 0.419 | 0.465 | 0.456 | 47 | 54 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN3 | game_spread | 0.161 | 0.125 | 0.132 | 13 | 88 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-9 | game_total | 0.255 | 0.210 | 0.219 | 22 | 80 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL2 | team_total | 0.808 | 0.845 | 0.838 | 85 | 16 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT31TBNSH-4 | game_total | 0.840 | 0.875 | 0.869 | 88 | 13 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT31CHIBOS-5 | game_total | 0.767 | 0.810 | 0.802 | 82 | 20 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT31CHIBOS-CHI3 | team_total | 0.451 | 0.495 | 0.486 | 50 | 51 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT31CHIBOS-6 | game_total | 0.562 | 0.605 | 0.596 | 61 | 40 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT31TBNSH-6 | game_total | 0.532 | 0.575 | 0.567 | 58 | 43 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT31BUFLA-BUF3 | game_spread | 0.180 | 0.215 | 0.208 | 22 | 79 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT3 | team_total | 0.647 | 0.690 | 0.682 | 70 | 32 | no | +0.018 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BOS | 0.692 | 0.661 | 0.153 | 0.199 | 6.19 | 6.56 | 0.999/1.026 | KXNHLTEAMTOTAL-26OCT31CHIBOS-CHI3 +0.074 |
| STL @ DET | 0.505 | 0.495 | 0.188 | 0.221 | 5.76 | 6.09 | 0.995/0.985 | KXNHLTOTAL-26OCT31STLDET-7 +0.055 |
| TBL @ NSH | 0.455 | 0.465 | 0.175 | 0.222 | 6.04 | 6.23 | 0.995/0.958 | KXNHLTOTAL-26OCT31TBNSH-7 +0.043 |
| EDM @ NYI | 0.497 | 0.483 | 0.166 | 0.216 | 6.41 | 6.70 | 0.957/1.023 | KXNHLTOTAL-26OCT31EDMNYI-7 +0.051 |
| BUF @ LAK | 0.485 | 0.542 | 0.181 | 0.223 | 6.24 | 6.19 | 0.993/0.998 | KXNHLGAME-26OCT31BUFLA-BUF -0.057 |
| OTT @ SJS | 0.519 | 0.503 | 0.168 | 0.215 | 6.78 | 6.50 | 1.035/1.051 | KXNHLTOTAL-26OCT31OTTSJ-8 -0.045 |
| PIT @ MTL | 0.628 | 0.520 | 0.167 | 0.213 | 6.44 | 6.62 | 0.983/1.012 | KXNHLGAME-26OCT31PITMTL-MTL -0.109 |
| TOR @ VAN | 0.448 | 0.502 | 0.160 | 0.211 | 7.23 | 6.67 | 1.021/0.956 | KXNHLTEAMTOTAL-26OCT31TORVAN-TOR4 -0.096 |
| CBJ @ DAL | 0.589 | 0.543 | 0.183 | 0.224 | 5.54 | 5.97 | 0.995/0.965 | KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3 +0.089 |
| CGY @ COL | 0.712 | 0.698 | 0.150 | 0.191 | 6.49 | 6.57 | 0.977/0.998 | KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 +0.023 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 38 recommended · full analysis in card.md / packet.json `thesis_card`

- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.2693 (adj 0.252) · $4.92 · thesis CHI:OFFENSE_4PLUS
- Oliver Moore: 1+ goals YES @ 11c · p 0.1495 (adj 0.1346) · $2.45 · thesis CHI:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 17c · p 0.2118 (adj 0.2001) · $2.79 · thesis BOS:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 60c · p 0.7137 (adj 0.6365) · $9.69 · thesis CHI:SUPPRESSED
- Jimmy Snuggerud: 1+ goals YES @ 26c · p 0.3231 (adj 0.3061) · $4.53 · thesis STL:OFFENSE_4PLUS
- Dylan Holloway: 1+ assists YES @ 30c · p 0.3885 (adj 0.3393) · $2.78 · thesis STL:OFFENSE_4PLUS
- Lucas Raymond: 1+ assists NO @ 58c · p 0.6586 (adj 0.6168) · $5.47 · thesis DET:SUPPRESSED
- Moritz Seider: 1+ assists NO @ 54c · p 0.6009 (adj 0.5679) · $2.09 · thesis DET:SUPPRESSED
- Charle-Edouard D'Astous: 1+ goals NO @ 89c · p 0.9288 (adj 0.9166) · $7.85 · thesis TBL:SUPPRESSED
- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3133 (adj 0.2962) · $3.37 · thesis NSH:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 74c · p 0.8091 (adj 0.7721) · $5.28 · thesis NSH:WINS
- Tampa Bay over 3.5 goals scored NO @ 51c · p 0.5792 (adj 0.5421) · $1.41 · thesis TBL:SUPPRESSED
- Mattias Ekholm: 1+ goals YES @ 7c · p 0.1232 (adj 0.1062) · $3.53 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 13c · p 0.1785 (adj 0.1651) · $3.46 · thesis EDM:OFFENSE_4PLUS
- Jason Dickinson: 1+ goals YES @ 9c · p 0.1202 (adj 0.1114) · $1.99 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 34c · p 0.4492 (adj 0.375) · $4.62 · thesis EDM:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0799 (adj 0.0674) · $1.4 · thesis LAK:WINS_BY_2PLUS
- Buffalo wins by over 1.5 goals NO @ 68c · p 0.7646 (adj 0.7198) · $8.84 · thesis LAK:WINS
- Andre Lee: 1+ goals YES @ 9c · p 0.1247 (adj 0.1085) · $1.31 · thesis LAK:OFFENSE_4PLUS
- Rasmus Dahlin: 1+ goals NO @ 81c · p 0.8444 (adj 0.8333) · $6.66 · thesis BUF:SUPPRESSED
- Tyler Toffoli: 1+ assists YES @ 24c · p 0.3249 (adj 0.2774) · $3.59 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 79c · p 0.8241 (adj 0.8143) · $8.62 · thesis SJS:SUPPRESSED
- Adam Gaudette: 1+ goals YES @ 14c · p 0.1693 (adj 0.1595) · $1.32 · thesis SJS:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1208 (adj 0.1106) · $1.79 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1592 (adj 0.1494) · $1.47 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 30c · p 0.3369 (adj 0.3264) · $2.02 · thesis PIT:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2694 (adj 0.2458) · $6.13 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 18c · p 0.2467 (adj 0.2275) · $5.12 · thesis VAN:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 72c · p 0.7837 (adj 0.7653) · $9.69 · thesis TOR:SUPPRESSED
- Liam Ohgren: 1+ goals YES @ 16c · p 0.2113 (adj 0.1935) · $3.07 · thesis VAN:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1805 (adj 0.1641) · $3.3 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 20c · p 0.2578 (adj 0.2383) · $3.85 · thesis CBJ:OFFENSE_4PLUS
- Ryan Lomberg: 1+ goals YES @ 5c · p 0.0717 (adj 0.065) · $1.26 · thesis CBJ:OFFENSE_4PLUS
- Cole Sillinger: 1+ goals YES @ 12c · p 0.1501 (adj 0.1413) · $1.77 · thesis CBJ:OFFENSE_4PLUS
- Colorado wins by over 2.5 goals NO @ 53c · p 0.6499 (adj 0.5687) · $3.59 · thesis GAME:TIGHT
- Colorado over 3.5 goals scored NO @ 34c · p 0.4212 (adj 0.3756) · $1.83 · thesis COL:SUPPRESSED
- Brock Nelson: 1+ goals NO @ 71c · p 0.7531 (adj 0.7411) · $5.91 · thesis COL:SUPPRESSED
- Joel Farabee: 1+ goals YES @ 20c · p 0.2301 (adj 0.2213) · $1.22 · thesis CGY:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BOS** · priced 168/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Michael DiPietro (CONFIRMED) exp shots 25.06, exp saves 22.15 (sd 6.07), pull risk 0.043
- CHI net: Arvid Soderblom (PROJECTED) exp shots 28.59, exp saves 24.02 (sd 7.01), pull risk 0.098

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.286 | 0.405 | 41/60 | +0.097 | STANDARD |
| Nikita Zadorov: 1+ points | 0.307 | 0.205 | 23/82 | +0.064 | STANDARD |
| Nikita Zadorov: 1+ assists | 0.255 | 0.155 | 17/86 | +0.075 | STANDARD |
| William Borgen: 1+ points | 0.275 | 0.180 | 23/87 | +0.033 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.339 | 0.250 | 26/76 | +0.065 | STANDARD |
| Hampus Lindholm: 1+ points | 0.392 | 0.305 | 32/71 | +0.057 | STANDARD |

**STL @ DET** · priced 161/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.58, exp saves 22.1 (sd 6.24), pull risk 0.063
- STL net: Joel Hofer (PROBABLE) exp shots 28.81, exp saves 24.9 (sd 6.68), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Hofer: 26+ saves | 0.458 | 0.350 | 52/82 | -0.080 |  |
| Dylan Holloway: 1+ assists | 0.389 | 0.290 | 30/72 | +0.074 | STANDARD |
| Lucas Raymond: 1+ assists | 0.341 | 0.425 | 43/58 | +0.062 | STANDARD |
| Dylan Holloway: 1+ points | 0.551 | 0.475 | 49/54 | +0.044 | STANDARD |
| Moritz Seider: 1+ points | 0.460 | 0.535 | 54/47 | +0.053 | STANDARD |
| Jimmy Snuggerud: 1+ goals | 0.323 | 0.255 | 26/75 | +0.050 | STANDARD |

**TBL @ NSH** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROJECTED) exp shots 29.61, exp saves 25.47 (sd 6.86), pull risk 0.063
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.75, exp saves 22.29 (sd 6.24), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.466 | 0.625 | 63/38 | +0.138 | STANDARD |
| Nikita Kucherov: 2+ points | 0.284 | 0.415 | 42/59 | +0.109 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.134 | 0.250 | 27/77 | +0.084 | STANDARD |
| Nikita Kucherov: 3+ points | 0.094 | 0.180 | 19/83 | +0.066 | STANDARD |
| Nikita Kucherov: 1+ points | 0.642 | 0.715 | 73/30 | +0.044 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.313 | 0.245 | 26/77 | +0.040 | STANDARD |

**EDM @ NYI** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.15, exp saves 23.23 (sd 6.5), pull risk 0.077
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.76, exp saves 23.98 (sd 6.67), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.551 | 0.665 | 67/34 | +0.093 | STANDARD |
| Connor McDavid: 2+ assists | 0.193 | 0.295 | 30/71 | +0.083 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.377 | 0.275 | 29/74 | +0.072 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.276 | 0.375 | 39/64 | +0.068 | STANDARD |
| Leon Draisaitl: 2+ points | 0.331 | 0.430 | 44/58 | +0.072 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.462 | 0.560 | 58/46 | +0.061 | STANDARD |

**BUF @ LAK** · priced 199/200 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.66, exp saves 24.15 (sd 6.48), pull risk 0.054
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 28.05, exp saves 24.03 (sd 6.55), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ points | 0.291 | 0.100 | 19/99 | +0.090 | STANDARD |
| Mikey Anderson: 1+ points | 0.276 | 0.100 | 19/99 | +0.075 | STANDARD |
| Brian Dumoulin: 1+ points | 0.270 | 0.100 | 19/99 | +0.070 | STANDARD |
| Brian Dumoulin: 1+ assists | 0.237 | 0.080 | 15/99 | +0.078 | STANDARD |
| Joel Edmundson: 1+ assists | 0.227 | 0.075 | 14/99 | +0.079 | STANDARD |
| Mikey Anderson: 1+ assists | 0.233 | 0.085 | 16/99 | +0.063 | STANDARD |

**OTT @ SJS** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.35, exp saves 24.29 (sd 6.78), pull risk 0.071
- OTT net: Samuel Ersson (PROJECTED) exp shots 25.93, exp saves 22.44 (sd 6.25), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 2+ points | 0.293 | 0.395 | 40/61 | +0.080 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.445 | 0.545 | 56/47 | +0.068 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.325 | 0.230 | 24/78 | +0.072 | STANDARD |
| Tim Stutzle: 1+ assists | 0.448 | 0.535 | 55/48 | +0.054 | STANDARD |
| Collin Graf: 1+ assists | 0.278 | 0.195 | 22/83 | +0.046 | STANDARD |
| Jake Sanderson: 1+ assists | 0.372 | 0.455 | 47/56 | +0.050 | STANDARD |

**PIT @ MTL** · priced 200/203 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.16, exp saves 24.42 (sd 6.68), pull risk 0.067
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.26, exp saves 22.49 (sd 6.49), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Samuel Girard: 1+ assists | 0.231 | 0.140 | 26/98 | -0.043 | STANDARD |
| Jacob Fowler: 23+ saves | 0.617 | 0.530 | 57/51 | +0.030 |  |
| Jake Evans: 1+ assists | 0.206 | 0.130 | 24/98 | -0.047 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.303 | 0.230 | 25/79 | +0.040 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.277 | 0.210 | 23/81 | +0.034 | STANDARD |
| Hendrix Lapierre: 1+ points | 0.255 | 0.310 | 33/71 | +0.020 | STANDARD |

**TOR @ VAN** · priced 160/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.88, exp saves 24.85 (sd 6.73), pull risk 0.069
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 28.15, exp saves 24.18 (sd 6.78), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Linus Karlsson: 1+ points | 0.494 | 0.365 | 39/66 | +0.087 | STANDARD |
| Auston Matthews: 1+ assists | 0.406 | 0.525 | 54/49 | +0.086 | STANDARD |
| Auston Matthews: 2+ points | 0.289 | 0.400 | 42/62 | +0.074 | STANDARD |
| William Nylander: 1+ assists | 0.411 | 0.520 | 54/50 | +0.071 | STANDARD |
| Anthony Stolarz: 25+ saves | 0.480 | 0.375 | 44/69 | +0.022 |  |
| Liam Ohgren: 1+ points | 0.429 | 0.325 | 34/69 | +0.073 | STANDARD |

**CBJ @ DAL** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.99, exp saves 21.78 (sd 6.01), pull risk 0.049
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.69, exp saves 23.04 (sd 6.37), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Sillinger: 1+ points | 0.362 | 0.245 | 27/78 | +0.078 | STANDARD |
| Damon Severson: 1+ points | 0.392 | 0.300 | 34/74 | +0.036 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.209 | 0.300 | 33/73 | +0.047 | STANDARD |
| Cole Sillinger: 1+ assists | 0.251 | 0.160 | 20/88 | +0.040 | STANDARD |
| Mathieu Olivier: 1+ points | 0.338 | 0.255 | 29/78 | +0.033 | STANDARD |
| Damon Severson: 1+ assists | 0.323 | 0.240 | 27/79 | +0.039 | STANDARD |

**CGY @ COL** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.33, exp saves 23.34 (sd 6.28), pull risk 0.043
- CGY net: Dustin Wolf (PROJECTED) exp shots 33.08, exp saves 27.67 (sd 7.88), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.401 | 0.525 | 53/48 | +0.101 | STANDARD |
| Cale Makar: 2+ points | 0.211 | 0.320 | 33/69 | +0.084 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.532 | 0.640 | 66/38 | +0.071 | STANDARD |
| Cale Makar: 1+ assists | 0.480 | 0.580 | 60/44 | +0.063 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.175 | 0.275 | 29/74 | +0.071 | STANDARD |
| Cale Makar: 2+ assists | 0.134 | 0.225 | 24/79 | +0.064 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
