# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T08:58:22Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 3363 · contracts joined: 1452 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1202, 'NO_EDGE': 123, 'OK': 127}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 172, 'game_early_goal': 10, 'first_goal': 192, 'game_winner': 20, 'player_goals': 372, 'game_overtime': 10, 'player_points': 206, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BOS | 2026-10-31T17:00:00Z | T-6h | 0.671 | 0.329 | 0.164 | 5.88 | 3.49 | 2.40 | 220 (25/195) | PROJECTED/PROJECTED |
| STL @ DET | 2026-10-31T17:00:00Z | T-6h | 0.510 | 0.490 | 0.185 | 5.78 | 2.92 | 2.86 | 181 (25/156) | CONFIRMED/PROJECTED |
| TBL @ NSH | 2026-10-31T18:00:00Z | T-6h | 0.427 | 0.573 | 0.177 | 6.21 | 2.87 | 3.33 | 205 (25/180) | PROJECTED/PROJECTED |
| EDM @ NYI | 2026-10-31T18:00:00Z | T-6h | 0.494 | 0.506 | 0.173 | 6.40 | 3.19 | 3.22 | 207 (25/182) | PROJECTED/CONFIRMED |
| BUF @ LAK | 2026-10-31T20:00:00Z | T-6h | 0.482 | 0.518 | 0.174 | 6.21 | 3.06 | 3.16 | 216 (25/191) | PROJECTED/PROJECTED |
| OTT @ SJS | 2026-10-31T20:00:00Z | T-6h | 0.502 | 0.498 | 0.171 | 6.65 | 3.32 | 3.33 | 219 (25/194) | PROJECTED/PROJECTED |
| PIT @ MTL | 2026-10-31T23:00:00Z | T-12h | 0.566 | 0.434 | 0.173 | 6.65 | 3.53 | 3.12 | 51 (25/26) | PROJECTED/PROJECTED |
| TOR @ VAN | 2026-10-31T23:00:00Z | T-12h | 0.456 | 0.544 | 0.161 | 7.18 | 3.44 | 3.74 | 51 (25/26) | PROJECTED/CONFIRMED |
| CBJ @ DAL | 2026-11-01T00:00:00Z | T-12h | 0.584 | 0.416 | 0.183 | 5.56 | 3.03 | 2.53 | 51 (25/26) | PROJECTED/PROJECTED |
| CGY @ COL | 2026-11-01T02:00:00Z | T-12h | 0.696 | 0.304 | 0.158 | 6.43 | 3.88 | 2.55 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.485 | 0.605 | 0.582 | 61 | 40 | no | +0.098 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.342 | 0.455 | 0.432 | 46 | 55 | no | +0.091 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.696 | 0.785 | 0.769 | 79 | 22 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.559 | 0.655 | 0.637 | 67 | 36 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.348 | 0.440 | 0.421 | 45 | 57 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT31TORVAN-8 | game_total | 0.409 | 0.325 | 0.341 | 33 | 68 | yes | +0.064 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.304 | 0.225 | 0.240 | 23 | 78 | yes | +0.062 | OK |
| KXNHLTOTAL-26OCT31TORVAN-9 | game_total | 0.310 | 0.235 | 0.249 | 24 | 77 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4 | team_total | 0.459 | 0.375 | 0.391 | 39 | 64 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN5 | team_total | 0.273 | 0.200 | 0.213 | 21 | 81 | yes | +0.051 | OK |
| KXNHLGAME-26OCT31TORVAN-TOR | game_winner | 0.544 | 0.615 | 0.601 | 62 | 39 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN6 | team_total | 0.137 | 0.080 | 0.089 | 9 | 93 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ3 | team_total | 0.647 | 0.585 | 0.598 | 59 | 42 | yes | +0.040 | OK |
| KXNHLTOTAL-26OCT31CHIBOS-5 | game_total | 0.729 | 0.785 | 0.774 | 79 | 22 | no | +0.039 | OK |
| KXNHLGAME-26OCT31TORVAN-VAN | game_winner | 0.456 | 0.390 | 0.403 | 40 | 62 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.188 | 0.250 | 0.237 | 26 | 76 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.761 | 0.820 | 0.809 | 83 | 19 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT31TORVAN-6 | game_total | 0.704 | 0.640 | 0.653 | 65 | 37 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT31STLDET-5 | game_total | 0.720 | 0.775 | 0.765 | 78 | 23 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.689 | 0.745 | 0.734 | 75 | 26 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.209 | 0.270 | 0.257 | 28 | 74 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3 | team_total | 0.663 | 0.595 | 0.609 | 61 | 42 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL4 | team_total | 0.328 | 0.390 | 0.377 | 40 | 62 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT31EDMNYI-EDM3 | game_spread | 0.173 | 0.225 | 0.214 | 23 | 78 | no | +0.035 | OK |
| KXNHLGAME-26OCT31OTTSJ-SJ | game_winner | 0.502 | 0.445 | 0.456 | 45 | 56 | yes | +0.034 | OK |
| KXNHLGAME-26OCT31OTTSJ-OTT | game_winner | 0.498 | 0.555 | 0.544 | 56 | 45 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.471 | 0.405 | 0.418 | 42 | 61 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT31CHIBOS-6 | game_total | 0.510 | 0.565 | 0.554 | 57 | 44 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT31TORVAN-10 | game_total | 0.171 | 0.120 | 0.129 | 13 | 89 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR2 | game_spread | 0.341 | 0.395 | 0.384 | 40 | 61 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT31TORVAN-7 | game_total | 0.599 | 0.540 | 0.552 | 55 | 47 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.371 | 0.435 | 0.422 | 45 | 58 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL2 | team_total | 0.778 | 0.825 | 0.816 | 83 | 18 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.264 | 0.205 | 0.216 | 22 | 81 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL3 | team_total | 0.552 | 0.610 | 0.599 | 62 | 40 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.137 | 0.095 | 0.102 | 10 | 91 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT2 | game_spread | 0.294 | 0.345 | 0.334 | 35 | 66 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ2 | game_spread | 0.293 | 0.245 | 0.254 | 25 | 76 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT31STLDET-4 | game_total | 0.811 | 0.860 | 0.851 | 87 | 15 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5 | team_total | 0.125 | 0.080 | 0.088 | 9 | 93 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN2 | game_spread | 0.261 | 0.215 | 0.224 | 22 | 79 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ4 | team_total | 0.436 | 0.385 | 0.395 | 39 | 62 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL3 | team_total | 0.595 | 0.655 | 0.643 | 67 | 36 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT31CHIBOS-7 | game_total | 0.395 | 0.450 | 0.439 | 46 | 56 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT31TORVAN-5 | game_total | 0.868 | 0.825 | 0.834 | 83 | 18 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT3 | game_spread | 0.180 | 0.225 | 0.216 | 23 | 78 | no | +0.027 | OK |
| KXNHLGAME-26OCT31EDMNYI-EDM | game_winner | 0.506 | 0.555 | 0.545 | 56 | 45 | no | +0.027 | OK |
| KXNHLGAME-26OCT31EDMNYI-NYI | game_winner | 0.494 | 0.445 | 0.455 | 45 | 56 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT31STLDET-7 | game_total | 0.377 | 0.430 | 0.419 | 44 | 58 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT31EDMNYI-EDM2 | game_spread | 0.289 | 0.335 | 0.325 | 34 | 67 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL2 | team_total | 0.805 | 0.850 | 0.842 | 86 | 16 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL2 | team_total | 0.900 | 0.940 | 0.933 | 95 | 7 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ6 | team_total | 0.121 | 0.080 | 0.087 | 9 | 93 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT31STLDET-6 | game_total | 0.489 | 0.535 | 0.526 | 54 | 47 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR3 | game_spread | 0.223 | 0.270 | 0.260 | 28 | 74 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI3 | team_total | 0.618 | 0.575 | 0.584 | 58 | 43 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT31STLDET-STL3 | game_spread | 0.149 | 0.190 | 0.181 | 20 | 82 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT31CHIBOS-BOS4 | team_total | 0.472 | 0.515 | 0.506 | 52 | 49 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI4 | team_total | 0.407 | 0.365 | 0.373 | 37 | 64 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT31EDMNYI-NYI2 | game_spread | 0.283 | 0.245 | 0.252 | 25 | 76 | yes | +0.020 | OK |
| KXNHLGAME-26OCT31TBNSH-TB | game_winner | 0.573 | 0.615 | 0.607 | 62 | 39 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB3 | game_spread | 0.217 | 0.260 | 0.251 | 27 | 75 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL2 | game_spread | 0.344 | 0.390 | 0.381 | 40 | 62 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN2 | team_total | 0.850 | 0.810 | 0.819 | 82 | 20 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ5 | team_total | 0.251 | 0.205 | 0.214 | 22 | 81 | yes | +0.019 | OK |
| KXNHLGAME-26OCT31CBJDAL-CBJ | game_winner | 0.416 | 0.375 | 0.383 | 38 | 63 | yes | +0.019 | OK |
| KXNHLGAME-26OCT31CBJDAL-DAL | game_winner | 0.584 | 0.625 | 0.617 | 63 | 38 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL5 | team_total | 0.190 | 0.235 | 0.225 | 25 | 78 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI6 | team_total | 0.102 | 0.070 | 0.076 | 8 | 94 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT31CHIBOS-4 | game_total | 0.825 | 0.860 | 0.853 | 87 | 15 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL5 | team_total | 0.164 | 0.200 | 0.192 | 21 | 81 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT31CHIBOS-CHI2 | team_total | 0.681 | 0.725 | 0.716 | 74 | 29 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT2 | team_total | 0.837 | 0.865 | 0.860 | 87 | 14 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB2 | game_spread | 0.350 | 0.385 | 0.378 | 39 | 62 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI5 | team_total | 0.225 | 0.185 | 0.192 | 20 | 83 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT31STLDET-9 | game_total | 0.137 | 0.165 | 0.159 | 17 | 84 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.708 | 0.670 | 0.678 | 68 | 34 | yes | +0.013 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN3 | game_spread | 0.161 | 0.135 | 0.140 | 14 | 87 | yes | +0.012 | OK |
| KXNHLSPREAD-26OCT31STLDET-STL2 | game_spread | 0.264 | 0.295 | 0.289 | 30 | 71 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-7 | game_total | 0.342 | 0.375 | 0.368 | 38 | 63 | no | +0.011 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BOS | 0.671 | 0.663 | 0.164 | 0.198 | 5.88 | 6.41 | 0.969/1.004 | KXNHLTOTAL-26OCT31CHIBOS-7 +0.092 |
| STL @ DET | 0.510 | 0.497 | 0.185 | 0.215 | 5.78 | 6.11 | 0.995/0.994 | KXNHLTOTAL-26OCT31STLDET-7 +0.062 |
| TBL @ NSH | 0.427 | 0.471 | 0.177 | 0.223 | 6.21 | 6.26 | 1.001/0.958 | KXNHLGAME-26OCT31TBNSH-NSH +0.044 |
| EDM @ NYI | 0.494 | 0.483 | 0.173 | 0.216 | 6.40 | 6.69 | 0.957/1.023 | KXNHLTOTAL-26OCT31EDMNYI-7 +0.052 |
| BUF @ LAK | 0.482 | 0.545 | 0.174 | 0.225 | 6.21 | 6.19 | 0.993/0.998 | KXNHLGAME-26OCT31BUFLA-BUF -0.063 |
| OTT @ SJS | 0.502 | 0.496 | 0.171 | 0.221 | 6.65 | 6.46 | 1.035/1.034 | KXNHLTOTAL-26OCT31OTTSJ-6 -0.034 |
| PIT @ MTL | 0.566 | 0.549 | 0.173 | 0.213 | 6.65 | 6.61 | 0.953/1.034 | KXNHLGAME-26OCT31PITMTL-MTL -0.017 |
| TOR @ VAN | 0.456 | 0.499 | 0.161 | 0.210 | 7.18 | 6.67 | 1.026/0.956 | KXNHLTOTAL-26OCT31TORVAN-8 -0.088 |
| CBJ @ DAL | 0.584 | 0.544 | 0.183 | 0.224 | 5.56 | 5.95 | 0.987/0.965 | KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3 +0.077 |
| CGY @ COL | 0.696 | 0.686 | 0.158 | 0.196 | 6.43 | 6.50 | 0.977/0.998 | KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 +0.028 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 23 recommended · full analysis in card.md / packet.json `thesis_card`

- Casey Mittelstadt: 1+ goals YES @ 17c · p 0.2219 (adj 0.2052) · $6.47 · thesis BOS:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 59c · p 0.6336 (adj 0.6215) · $6.23 · thesis BOS:SUPPRESSED
- Connor Bedard: 1+ assists NO @ 56c · p 0.6385 (adj 0.5917) · $7.68 · thesis CHI:SUPPRESSED
- Pavel Zacha: 1+ assists NO @ 54c · p 0.6101 (adj 0.57) · $6.79 · thesis BOS:SUPPRESSED
- Sheldon Dries: 1+ goals YES @ 8c · p 0.1134 (adj 0.0975) · $2.53 · thesis DET:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 36c · p 0.4077 (adj 0.392) · $5.41 · thesis DET:OFFENSE_4PLUS
- Dylan Holloway: 1+ assists YES @ 31c · p 0.3773 (adj 0.3362) · $3.4 · thesis STL:OFFENSE_4PLUS
- Charle-Edouard D'Astous: 1+ goals NO @ 88c · p 0.9356 (adj 0.918) · $17.42 · thesis TBL:SUPPRESSED
- Tampa Bay wins by over 1.5 goals NO @ 62c · p 0.694 (adj 0.6545) · $9.31 · thesis NSH:WINS
- Nikita Kucherov: 1+ goals NO @ 63c · p 0.6753 (adj 0.6602) · $6.62 · thesis TBL:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 22c · p 0.2631 (adj 0.2498) · $4.45 · thesis NYI:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1092 (adj 0.0957) · $2.38 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 33c · p 0.4436 (adj 0.3633) · $6.93 · thesis EDM:SUPPRESSED
- Full Game: Over 6.5 goals scored YES @ 47c · p 0.5323 (adj 0.4986) · $4.87 · thesis GAME:HIGH_EVENT
- Andre Lee: 1+ goals YES @ 10c · p 0.1284 (adj 0.12) · $2.85 · thesis LAK:OFFENSE_4PLUS
- Scott Laughton: 1+ goals YES @ 13c · p 0.1597 (adj 0.1498) · $2.32 · thesis LAK:OFFENSE_4PLUS
- Buffalo wins by over 2.5 goals NO @ 80c · p 0.8535 (adj 0.8242) · $12.62 · thesis LAK:WINS
- Los Angeles wins by over 1.5 goals YES @ 26c · p 0.3189 (adj 0.287) · $1.56 · thesis LAK:WINS_BY_2PLUS
- Thomas Chabot: 1+ assists NO @ 72c · p 0.789 (adj 0.747) · $11.86 · thesis OTT:SUPPRESSED
- Vancouver wins by over 1.5 goals YES @ 22c · p 0.2864 (adj 0.2507) · $3.6 · thesis VAN:WINS_BY_2PLUS
- Toronto wins by over 2.5 goals NO @ 74c · p 0.8128 (adj 0.7714) · $14.11 · thesis VAN:WINS
- Columbus wins by over 1.5 goals YES @ 19c · p 0.239 (adj 0.212) · $2.17 · thesis CBJ:WINS_BY_2PLUS
- Dallas wins by over 2.5 goals NO @ 74c · p 0.7989 (adj 0.7645) · $8.43 · thesis CBJ:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BOS** · priced 168/169 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- BOS net: Jeremy Swayman (PROJECTED) exp shots 25.06, exp saves 22.13 (sd 6.08), pull risk 0.043
- CHI net: Spencer Knight (PROJECTED) exp shots 28.59, exp saves 24.14 (sd 6.84), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.299 | 0.400 | 41/61 | +0.074 | STANDARD |
| Connor Bedard: 1+ assists | 0.361 | 0.455 | 47/56 | +0.061 | STANDARD |
| David Pastrnak: 2+ points | 0.338 | 0.430 | 45/59 | +0.055 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.433 | 0.525 | 54/49 | +0.060 | STANDARD |
| Pavel Zacha: 1+ assists | 0.390 | 0.470 | 48/54 | +0.053 | STANDARD |
| Charlie McAvoy: 2+ points | 0.159 | 0.235 | 25/78 | +0.049 | STANDARD |

**STL @ DET** · priced 123/130 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- DET net: John Gibson (CONFIRMED) exp shots 25.58, exp saves 22.14 (sd 6.28), pull risk 0.06
- STL net: Joel Hofer (PROJECTED) exp shots 28.81, exp saves 24.9 (sd 6.67), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Moritz Seider: 1+ points | 0.456 | 0.540 | 56/48 | +0.046 | STANDARD |
| Dylan Holloway: 1+ assists | 0.377 | 0.295 | 31/72 | +0.052 | STANDARD |
| Moritz Seider: 1+ assists | 0.400 | 0.475 | 49/54 | +0.042 | STANDARD |
| Lucas Raymond: 2+ points | 0.173 | 0.245 | 26/77 | +0.045 | STANDARD |
| Lucas Raymond: 1+ assists | 0.344 | 0.415 | 43/60 | +0.040 | STANDARD |
| Moritz Seider: 2+ points | 0.127 | 0.195 | 21/82 | +0.043 | STANDARD |

**TBL @ NSH** · priced 153/154 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NSH net: Juuse Saros (PROJECTED) exp shots 29.61, exp saves 25.52 (sd 6.92), pull risk 0.063
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.75, exp saves 22.27 (sd 6.26), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.469 | 0.625 | 64/39 | +0.124 | STANDARD |
| Nikita Kucherov: 2+ points | 0.278 | 0.430 | 45/59 | +0.116 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.134 | 0.235 | 27/80 | +0.055 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.294 | 0.220 | 26/82 | +0.020 | STANDARD |
| Mavrik Bourque: 1+ points | 0.326 | 0.400 | 42/62 | +0.037 | STANDARD |
| Filip Forsberg: 2+ points | 0.248 | 0.175 | 28/93 | -0.046 | STANDARD |

**EDM @ NYI** · priced 155/156 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.15, exp saves 23.17 (sd 6.5), pull risk 0.077
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.76, exp saves 23.97 (sd 6.69), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Logan Stanley: 1+ assists | 0.265 | 0.130 | 24/98 | +0.012 | STANDARD |
| Connor McDavid: 1+ assists | 0.556 | 0.680 | 69/33 | +0.098 | STANDARD |
| Evan Bouchard: 1+ points | 0.671 | 0.555 | 70/59 | -0.043 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.271 | 0.385 | 40/63 | +0.083 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.472 | 0.575 | 58/43 | +0.081 | STANDARD |
| Connor McDavid: 2+ assists | 0.195 | 0.295 | 32/73 | +0.061 | STANDARD |

**BUF @ LAK** · priced 164/165 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.66, exp saves 24.12 (sd 6.57), pull risk 0.055
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 28.05, exp saves 24.01 (sd 6.64), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Owen Power: 1+ points | 0.394 | 0.295 | 39/80 | -0.013 | STANDARD |
| Tage Thompson: 1+ points | 0.536 | 0.625 | 64/39 | +0.057 | STANDARD |
| Tage Thompson: 1+ assists | 0.323 | 0.405 | 42/61 | +0.051 | STANDARD |
| Alex Laferriere: 2+ points | 0.205 | 0.125 | 20/95 | -0.006 | STANDARD |
| Adrian Kempe: 2+ points | 0.232 | 0.160 | 26/94 | -0.042 | STANDARD |
| Trevor Moore: 1+ assists | 0.312 | 0.250 | 28/78 | +0.018 | STANDARD |

**OTT @ SJS** · priced 167/168 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.35, exp saves 24.27 (sd 6.75), pull risk 0.069
- OTT net: Jonas Johansson (PROJECTED) exp shots 25.93, exp saves 22.44 (sd 6.27), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.353 | 0.455 | 47/56 | +0.070 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.441 | 0.540 | 55/47 | +0.071 | STANDARD |
| Jake Sanderson: 1+ points | 0.439 | 0.530 | 55/49 | +0.054 | STANDARD |
| Macklin Celebrini: 2+ points | 0.296 | 0.385 | 40/63 | +0.058 | STANDARD |
| Thomas Chabot: 1+ assists | 0.211 | 0.295 | 31/72 | +0.055 | STANDARD |
| Tim Stutzle: 2+ points | 0.254 | 0.335 | 35/68 | +0.050 | STANDARD |

**PIT @ MTL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- MTL net: Jakub Dobes (PROJECTED) exp shots 28.16, exp saves 24.52 (sd 6.7), pull risk 0.065
- PIT net: Arturs Silovs (PROJECTED) exp shots 26.26, exp saves 22.48 (sd 6.52), pull risk 0.078

**TOR @ VAN** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- VAN net: Leevi Merilainen (PROJECTED) exp shots 28.88, exp saves 24.83 (sd 6.77), pull risk 0.071
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 28.15, exp saves 24.21 (sd 6.71), pull risk 0.069

**CBJ @ DAL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.99, exp saves 21.81 (sd 6.08), pull risk 0.048
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.69, exp saves 23.04 (sd 6.37), pull risk 0.061

**CGY @ COL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.33, exp saves 23.28 (sd 6.26), pull risk 0.044
- CGY net: Dustin Wolf (PROJECTED) exp shots 33.08, exp saves 27.77 (sd 7.8), pull risk 0.097

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
