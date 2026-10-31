# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T15:22:18Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 4122 · contracts joined: 2211 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1961, 'NO_EDGE': 98, 'OK': 152}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 308, 'game_early_goal': 10, 'first_goal': 352, 'game_winner': 20, 'player_goals': 624, 'game_overtime': 10, 'player_points': 414, 'game_spread': 40, 'team_total': 100, 'game_total': 90, 'goalie_saves': 3}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BOS | 2026-10-31T17:00:00Z | T-90m | 0.700 | 0.300 | 0.152 | 6.13 | 3.72 | 2.41 | 226 (25/201) | PROJECTED/PROJECTED |
| STL @ DET | 2026-10-31T17:00:00Z | T-90m | 0.511 | 0.489 | 0.180 | 5.78 | 2.92 | 2.86 | 218 (25/193) | CONFIRMED/PROJECTED |
| TBL @ NSH | 2026-10-31T18:00:00Z | T-90m | 0.455 | 0.545 | 0.175 | 6.04 | 2.88 | 3.16 | 216 (25/191) | PROJECTED/PROJECTED |
| EDM @ NYI | 2026-10-31T18:00:00Z | T-90m | 0.497 | 0.503 | 0.166 | 6.41 | 3.19 | 3.22 | 214 (25/189) | PROJECTED/CONFIRMED |
| BUF @ LAK | 2026-10-31T20:00:00Z | T-3h | 0.518 | 0.482 | 0.176 | 6.02 | 3.07 | 2.95 | 226 (25/201) | PROJECTED/PROJECTED |
| OTT @ SJS | 2026-10-31T20:00:00Z | T-3h | 0.519 | 0.481 | 0.168 | 6.78 | 3.45 | 3.33 | 225 (25/200) | PROJECTED/PROJECTED |
| PIT @ MTL | 2026-10-31T23:00:00Z | T-6h | 0.617 | 0.383 | 0.164 | 6.37 | 3.56 | 2.82 | 225 (25/200) | CONFIRMED/PROJECTED |
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
| KXNHLGAME-26OCT31TORVAN-TOR | game_winner | 0.552 | 0.645 | 0.627 | 65 | 36 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3 | team_total | 0.667 | 0.570 | 0.590 | 58 | 44 | yes | +0.070 | OK |
| KXNHLGAME-26OCT31PITMTL-MTL | game_winner | 0.617 | 0.525 | 0.544 | 53 | 48 | yes | +0.069 | OK |
| KXNHLGAME-26OCT31PITMTL-PIT | game_winner | 0.383 | 0.475 | 0.456 | 48 | 53 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ3 | team_total | 0.674 | 0.585 | 0.603 | 59 | 42 | yes | +0.067 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.288 | 0.205 | 0.220 | 21 | 80 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT31TORVAN-8 | game_total | 0.411 | 0.325 | 0.341 | 33 | 68 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT31TORVAN-9 | game_total | 0.318 | 0.235 | 0.250 | 24 | 77 | yes | +0.065 | OK |
| KXNHLGAME-26OCT31OTTSJ-OTT | game_winner | 0.481 | 0.565 | 0.548 | 57 | 44 | no | +0.062 | OK |
| KXNHLGAME-26OCT31TORVAN-VAN | game_winner | 0.448 | 0.365 | 0.381 | 37 | 64 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN5 | team_total | 0.271 | 0.185 | 0.200 | 20 | 83 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.574 | 0.665 | 0.648 | 68 | 35 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT4 | team_total | 0.324 | 0.405 | 0.388 | 41 | 60 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.365 | 0.450 | 0.432 | 46 | 56 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ4 | team_total | 0.464 | 0.380 | 0.396 | 39 | 63 | yes | +0.057 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.712 | 0.785 | 0.772 | 79 | 22 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ5 | team_total | 0.275 | 0.200 | 0.214 | 21 | 81 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.708 | 0.635 | 0.650 | 64 | 37 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT31TORVAN-7 | game_total | 0.609 | 0.535 | 0.550 | 54 | 47 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB3 | game_spread | 0.196 | 0.265 | 0.250 | 27 | 74 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.467 | 0.395 | 0.409 | 40 | 61 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ2 | game_spread | 0.313 | 0.245 | 0.258 | 25 | 76 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL2 | game_spread | 0.395 | 0.320 | 0.334 | 33 | 69 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR3 | game_spread | 0.227 | 0.295 | 0.281 | 30 | 71 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN2 | game_spread | 0.260 | 0.195 | 0.207 | 20 | 81 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB5 | team_total | 0.218 | 0.285 | 0.271 | 29 | 72 | no | +0.048 | OK |
| KXNHLGAME-26OCT31TBNSH-NSH | game_winner | 0.455 | 0.385 | 0.399 | 39 | 62 | yes | +0.048 | OK |
| KXNHLGAME-26OCT31TBNSH-TB | game_winner | 0.545 | 0.615 | 0.601 | 62 | 39 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT3 | team_total | 0.536 | 0.610 | 0.595 | 62 | 40 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT31TORVAN-6 | game_total | 0.712 | 0.640 | 0.655 | 65 | 37 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN6 | team_total | 0.141 | 0.075 | 0.085 | 9 | 94 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT3 | game_spread | 0.173 | 0.235 | 0.221 | 24 | 77 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT2 | game_spread | 0.280 | 0.345 | 0.331 | 35 | 66 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB3 | team_total | 0.621 | 0.695 | 0.681 | 71 | 32 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT3 | game_spread | 0.108 | 0.165 | 0.152 | 17 | 84 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.371 | 0.440 | 0.426 | 45 | 57 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.205 | 0.265 | 0.252 | 27 | 74 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB2 | game_spread | 0.322 | 0.385 | 0.372 | 39 | 62 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT31BUFLA-BUF2 | game_spread | 0.264 | 0.325 | 0.312 | 33 | 68 | no | +0.040 | OK |
| KXNHLGAME-26OCT31BUFLA-BUF | game_winner | 0.482 | 0.545 | 0.533 | 55 | 46 | no | +0.040 | OK |
| KXNHLGAME-26OCT31BUFLA-LA | game_winner | 0.518 | 0.455 | 0.467 | 46 | 55 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT2 | team_total | 0.759 | 0.820 | 0.809 | 83 | 19 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.261 | 0.200 | 0.211 | 21 | 81 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN2 | team_total | 0.851 | 0.790 | 0.803 | 80 | 22 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT2 | game_spread | 0.198 | 0.255 | 0.243 | 26 | 75 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT31STLDET-5 | game_total | 0.719 | 0.775 | 0.764 | 78 | 23 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT31TORVAN-10 | game_total | 0.176 | 0.120 | 0.130 | 13 | 89 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.689 | 0.745 | 0.734 | 75 | 26 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.200 | 0.260 | 0.247 | 27 | 75 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL3 | team_total | 0.598 | 0.655 | 0.644 | 66 | 35 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT5 | team_total | 0.162 | 0.225 | 0.211 | 24 | 79 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR2 | game_spread | 0.348 | 0.410 | 0.397 | 42 | 60 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL4 | team_total | 0.330 | 0.385 | 0.374 | 39 | 62 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT31BUFLA-BUF3 | game_spread | 0.155 | 0.205 | 0.194 | 21 | 80 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT31TBNSH-NSH2 | game_spread | 0.243 | 0.195 | 0.204 | 20 | 81 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT31TBNSH-TB2 | team_total | 0.820 | 0.865 | 0.857 | 87 | 14 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL2 | game_spread | 0.342 | 0.395 | 0.384 | 40 | 61 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT31STLDET-4 | game_total | 0.810 | 0.855 | 0.847 | 86 | 15 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31BUFLA-BUF3 | team_total | 0.573 | 0.630 | 0.619 | 64 | 38 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL3 | team_total | 0.552 | 0.605 | 0.595 | 61 | 40 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.769 | 0.825 | 0.815 | 84 | 19 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31BUFLA-BUF4 | team_total | 0.354 | 0.405 | 0.395 | 41 | 60 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ6 | team_total | 0.136 | 0.085 | 0.094 | 10 | 93 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-8 | game_total | 0.344 | 0.295 | 0.304 | 30 | 71 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31BUFLA-BUF2 | team_total | 0.791 | 0.840 | 0.831 | 85 | 17 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT31STLDET-STL3 | game_spread | 0.151 | 0.195 | 0.185 | 20 | 81 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ3 | game_spread | 0.196 | 0.155 | 0.163 | 16 | 85 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5 | team_total | 0.122 | 0.080 | 0.087 | 9 | 93 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT31PITMTL-7 | game_total | 0.477 | 0.525 | 0.515 | 53 | 48 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.130 | 0.095 | 0.101 | 10 | 91 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN3 | game_spread | 0.161 | 0.125 | 0.132 | 13 | 88 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL2 | team_total | 0.776 | 0.820 | 0.812 | 83 | 19 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL2 | team_total | 0.808 | 0.845 | 0.838 | 85 | 16 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-9 | game_total | 0.255 | 0.210 | 0.219 | 22 | 80 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT31STLDET-7 | game_total | 0.380 | 0.425 | 0.416 | 43 | 58 | no | +0.023 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 36 recommended · full analysis in card.md / packet.json `thesis_card`

- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.265 (adj 0.2488) · $4.17 · thesis CHI:OFFENSE_4PLUS
- Oliver Moore: 1+ goals YES @ 11c · p 0.1486 (adj 0.1377) · $2.78 · thesis CHI:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 17c · p 0.2122 (adj 0.2004) · $3.05 · thesis BOS:OFFENSE_4PLUS
- Roman Kantserov: 1+ goals NO @ 76c · p 0.7937 (adj 0.784) · $6.35 · thesis CHI:SUPPRESSED
- Jimmy Snuggerud: 1+ goals YES @ 27c · p 0.3292 (adj 0.3131) · $4.8 · thesis STL:OFFENSE_4PLUS
- Lucas Raymond: 1+ assists NO @ 58c · p 0.6575 (adj 0.6162) · $6.38 · thesis DET:SUPPRESSED
- Dylan Holloway: 1+ assists YES @ 31c · p 0.3857 (adj 0.3404) · $1.42 · thesis STL:OFFENSE_4PLUS
- Charle-Edouard D'Astous: 1+ goals NO @ 88c · p 0.9288 (adj 0.9153) · $8.38 · thesis TBL:SUPPRESSED
- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3133 (adj 0.2962) · $3.53 · thesis NSH:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 74c · p 0.8091 (adj 0.7721) · $5.44 · thesis NSH:WINS
- Tampa Bay over 3.5 goals scored NO @ 51c · p 0.5792 (adj 0.5421) · $1.23 · thesis TBL:SUPPRESSED
- Mattias Ekholm: 1+ goals YES @ 7c · p 0.1232 (adj 0.1049) · $3.57 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 13c · p 0.1785 (adj 0.1651) · $3.72 · thesis EDM:OFFENSE_4PLUS
- Anthony Duclair: 1+ goals YES @ 15c · p 0.1873 (adj 0.1755) · $2.4 · thesis NYI:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 71c · p 0.8075 (adj 0.7376) · $10.36 · thesis EDM:SUPPRESSED
- Andre Lee: 1+ goals YES @ 9c · p 0.1311 (adj 0.1196) · $3.05 · thesis LAK:OFFENSE_4PLUS
- Corey Perry: 1+ goals YES @ 14c · p 0.1826 (adj 0.1707) · $3.17 · thesis LAK:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0787 (adj 0.0665) · $1.46 · thesis LAK:WINS_BY_2PLUS
- Alex Laferriere: 2+ goals YES @ 4c · p 0.0541 (adj 0.0531) · $1.35 · thesis LAK:OFFENSE_4PLUS
- Claude Giroux: 1+ goals YES @ 18c · p 0.2158 (adj 0.2056) · $2.54 · thesis OTT:OFFENSE_4PLUS
- Thomas Chabot: 1+ assists NO @ 68c · p 0.7454 (adj 0.7102) · $7.34 · thesis OTT:SUPPRESSED
- Ivar Stenberg: 1+ goals NO @ 79c · p 0.8241 (adj 0.8143) · $8.43 · thesis SJS:SUPPRESSED
- Adam Gaudette: 1+ goals YES @ 14c · p 0.1693 (adj 0.1595) · $1.6 · thesis SJS:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1291 (adj 0.1168) · $2.77 · thesis PIT:OFFENSE_4PLUS
- Phillip Danault: 1+ goals YES @ 12c · p 0.1647 (adj 0.1485) · $2.91 · thesis MTL:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1616 (adj 0.1512) · $1.9 · thesis PIT:OFFENSE_4PLUS
- Jake Evans: 1+ goals YES @ 12c · p 0.1519 (adj 0.1377) · $1.42 · thesis MTL:WINS_BY_2PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2694 (adj 0.2458) · $6.61 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 18c · p 0.2467 (adj 0.2263) · $5.23 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 16c · p 0.2113 (adj 0.1897) · $2.67 · thesis VAN:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 73c · p 0.7842 (adj 0.7656) · $10.36 · thesis TOR:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 19c · p 0.2609 (adj 0.2419) · $6.04 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 12c · p 0.1838 (adj 0.1603) · $4.11 · thesis CBJ:OFFENSE_4PLUS
- Damon Severson: 1+ goals YES @ 7c · p 0.105 (adj 0.0912) · $1.93 · thesis CBJ:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 70c · p 0.7354 (adj 0.7253) · $4.75 · thesis DAL:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 8c · p 0.1097 (adj 0.0985) · $1.13 · thesis CGY:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BOS** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 25.06, exp saves 22.16 (sd 6.06), pull risk 0.044
- CHI net: Arvid Soderblom (PROJECTED) exp shots 28.59, exp saves 24.0 (sd 6.9), pull risk 0.098

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.288 | 0.400 | 41/61 | +0.085 | STANDARD |
| Connor Bedard: 1+ assists | 0.345 | 0.445 | 46/57 | +0.067 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.339 | 0.240 | 26/78 | +0.065 | STANDARD |
| Hampus Lindholm: 1+ points | 0.398 | 0.300 | 32/72 | +0.063 | STANDARD |
| David Pastrnak: 2+ points | 0.339 | 0.420 | 44/60 | +0.044 | STANDARD |
| Connor Bedard: 1+ points | 0.525 | 0.605 | 62/41 | +0.048 | STANDARD |

**STL @ DET** · priced 154/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.58, exp saves 22.11 (sd 6.22), pull risk 0.06
- STL net: Joel Hofer (PROJECTED) exp shots 28.81, exp saves 24.9 (sd 6.7), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Holloway: 1+ assists | 0.386 | 0.295 | 31/72 | +0.061 | STANDARD |
| Lucas Raymond: 1+ assists | 0.343 | 0.425 | 43/58 | +0.060 | STANDARD |
| Dylan Holloway: 1+ points | 0.550 | 0.470 | 49/55 | +0.042 | STANDARD |
| Moritz Seider: 1+ points | 0.464 | 0.540 | 55/47 | +0.049 | STANDARD |
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
| Nikita Kucherov: 1+ points | 0.642 | 0.755 | 77/26 | +0.085 | STANDARD |
| Nikita Kucherov: 3+ points | 0.094 | 0.170 | 19/85 | +0.047 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.313 | 0.245 | 26/77 | +0.040 | STANDARD |

**EDM @ NYI** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.15, exp saves 23.23 (sd 6.5), pull risk 0.077
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.76, exp saves 23.98 (sd 6.67), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tristan Jarry: 26+ saves | 0.405 | 0.555 | 98/87 | -0.283 |  |
| Leon Draisaitl: 1+ assists | 0.462 | 0.570 | 59/45 | +0.071 | STANDARD |
| Connor McDavid: 2+ assists | 0.193 | 0.300 | 31/71 | +0.083 | STANDARD |
| Connor McDavid: 1+ assists | 0.551 | 0.655 | 67/36 | +0.073 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.568 | 0.465 | 49/56 | +0.060 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.377 | 0.275 | 30/75 | +0.062 | STANDARD |

**BUF @ LAK** · priced 168/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 27.66, exp saves 24.12 (sd 6.48), pull risk 0.054
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 28.05, exp saves 24.01 (sd 6.58), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Laferriere: 1+ points | 0.598 | 0.510 | 54/52 | +0.040 | STANDARD |
| Trevor Moore: 1+ points | 0.480 | 0.395 | 42/63 | +0.043 | STANDARD |
| Trevor Moore: 1+ assists | 0.330 | 0.245 | 26/77 | +0.056 | STANDARD |
| Tage Thompson: 1+ assists | 0.317 | 0.400 | 42/62 | +0.046 | STANDARD |
| Alex Laferriere: 2+ points | 0.235 | 0.170 | 18/84 | +0.045 | STANDARD |
| Tage Thompson: 1+ points | 0.537 | 0.600 | 62/42 | +0.026 | STANDARD |

**OTT @ SJS** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.35, exp saves 24.29 (sd 6.78), pull risk 0.071
- OTT net: Samuel Ersson (PROJECTED) exp shots 25.93, exp saves 22.44 (sd 6.25), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.445 | 0.540 | 56/48 | +0.058 | STANDARD |
| Macklin Celebrini: 2+ points | 0.293 | 0.385 | 40/63 | +0.060 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.325 | 0.240 | 25/77 | +0.062 | STANDARD |
| Collin Graf: 1+ assists | 0.278 | 0.200 | 23/83 | +0.036 | STANDARD |
| Collin Graf: 1+ points | 0.421 | 0.345 | 36/67 | +0.045 | STANDARD |
| Ivar Stenberg: 1+ points | 0.402 | 0.475 | 50/55 | +0.031 | STANDARD |

**PIT @ MTL** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.16, exp saves 24.48 (sd 6.71), pull risk 0.065
- PIT net: Sergei Murashov (PROJECTED) exp shots 26.26, exp saves 22.51 (sd 6.48), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Egor Chinakhov: 1+ assists | 0.289 | 0.210 | 23/81 | +0.047 | STANDARD |
| Phillip Danault: 1+ goals | 0.165 | 0.100 | 12/92 | +0.037 | STANDARD |
| Egor Chinakhov: 1+ points | 0.440 | 0.380 | 42/66 | +0.003 | STANDARD |
| Jake Evans: 1+ goals | 0.152 | 0.095 | 12/93 | +0.025 | STANDARD |
| Lane Hutson: 2+ assists | 0.149 | 0.205 | 23/82 | +0.020 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.300 | 0.245 | 27/78 | +0.017 | STANDARD |

**TOR @ VAN** · priced 158/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.88, exp saves 24.85 (sd 6.73), pull risk 0.069
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 28.15, exp saves 24.18 (sd 6.78), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anthony Stolarz: 25+ saves | 0.480 | 0.645 | 98/69 | -0.185 |  |
| Linus Karlsson: 1+ points | 0.494 | 0.360 | 40/68 | +0.077 | STANDARD |
| Auston Matthews: 2+ points | 0.288 | 0.410 | 42/60 | +0.095 | STANDARD |
| Auston Matthews: 1+ assists | 0.408 | 0.530 | 55/49 | +0.085 | STANDARD |
| William Nylander: 1+ assists | 0.415 | 0.530 | 55/49 | +0.077 | STANDARD |
| Liam Ohgren: 1+ points | 0.429 | 0.315 | 36/73 | +0.053 | STANDARD |

**CBJ @ DAL** · priced 158/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.99, exp saves 21.81 (sd 6.06), pull risk 0.047
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.69, exp saves 23.03 (sd 6.41), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Valeri Nichushkin: 1+ assists | 0.211 | 0.320 | 34/70 | +0.074 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.184 | 0.090 | 12/94 | +0.056 | STANDARD |
| Mikko Rantanen: 2+ points | 0.228 | 0.310 | 34/72 | +0.038 | STANDARD |
| Charlie Coyle: 1+ goals | 0.261 | 0.185 | 19/82 | +0.060 | STANDARD |
| Charlie Coyle: 1+ points | 0.521 | 0.450 | 47/57 | +0.034 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.449 | 0.520 | 54/50 | +0.033 | STANDARD |

**CGY @ COL** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.33, exp saves 23.34 (sd 6.28), pull risk 0.043
- CGY net: Dustin Wolf (PROJECTED) exp shots 33.08, exp saves 27.67 (sd 7.88), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ assists | 0.175 | 0.280 | 31/75 | +0.061 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.401 | 0.505 | 53/52 | +0.061 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.532 | 0.635 | 66/39 | +0.061 | STANDARD |
| Cale Makar: 2+ assists | 0.134 | 0.235 | 26/79 | +0.064 | STANDARD |
| Cale Makar: 1+ assists | 0.480 | 0.580 | 60/44 | +0.063 | STANDARD |
| Cale Makar: 2+ points | 0.211 | 0.310 | 33/71 | +0.065 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
