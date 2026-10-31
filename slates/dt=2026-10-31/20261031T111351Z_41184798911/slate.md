# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T11:13:51Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 3735 · contracts joined: 1824 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1574, 'NO_EDGE': 123, 'OK': 127}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 233, 'game_early_goal': 10, 'first_goal': 270, 'game_winner': 20, 'player_goals': 500, 'game_overtime': 10, 'player_points': 311, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BOS | 2026-10-31T17:00:00Z | T-3h | 0.671 | 0.329 | 0.164 | 5.88 | 3.49 | 2.40 | 220 (25/195) | PROJECTED/PROJECTED |
| STL @ DET | 2026-10-31T17:00:00Z | T-3h | 0.510 | 0.490 | 0.185 | 5.78 | 2.92 | 2.86 | 199 (25/174) | CONFIRMED/PROJECTED |
| TBL @ NSH | 2026-10-31T18:00:00Z | T-6h | 0.427 | 0.573 | 0.177 | 6.21 | 2.87 | 3.33 | 216 (25/191) | PROJECTED/PROJECTED |
| EDM @ NYI | 2026-10-31T18:00:00Z | T-6h | 0.494 | 0.506 | 0.173 | 6.40 | 3.19 | 3.22 | 215 (25/190) | PROJECTED/CONFIRMED |
| BUF @ LAK | 2026-10-31T20:00:00Z | T-6h | 0.482 | 0.518 | 0.174 | 6.21 | 3.06 | 3.16 | 216 (25/191) | PROJECTED/PROJECTED |
| OTT @ SJS | 2026-10-31T20:00:00Z | T-6h | 0.502 | 0.498 | 0.171 | 6.65 | 3.32 | 3.33 | 219 (25/194) | PROJECTED/PROJECTED |
| PIT @ MTL | 2026-10-31T23:00:00Z | T-6h | 0.566 | 0.434 | 0.173 | 6.65 | 3.53 | 3.12 | 219 (25/194) | PROJECTED/PROJECTED |
| TOR @ VAN | 2026-10-31T23:00:00Z | T-6h | 0.456 | 0.544 | 0.161 | 7.18 | 3.44 | 3.74 | 218 (25/193) | PROJECTED/CONFIRMED |
| CBJ @ DAL | 2026-11-01T00:00:00Z | T-12h | 0.584 | 0.416 | 0.183 | 5.56 | 3.03 | 2.53 | 51 (25/26) | PROJECTED/PROJECTED |
| CGY @ COL | 2026-11-01T02:00:00Z | T-12h | 0.696 | 0.304 | 0.158 | 6.43 | 3.88 | 2.55 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.485 | 0.605 | 0.582 | 61 | 40 | no | +0.098 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.342 | 0.455 | 0.432 | 46 | 55 | no | +0.091 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.696 | 0.785 | 0.769 | 79 | 22 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3 | team_total | 0.663 | 0.570 | 0.589 | 58 | 44 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.559 | 0.650 | 0.632 | 66 | 36 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.348 | 0.450 | 0.429 | 47 | 57 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT31TORVAN-8 | game_total | 0.409 | 0.325 | 0.341 | 33 | 68 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4 | team_total | 0.459 | 0.370 | 0.387 | 38 | 64 | yes | +0.062 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.304 | 0.225 | 0.240 | 23 | 78 | yes | +0.062 | OK |
| KXNHLTOTAL-26OCT31TORVAN-9 | game_total | 0.310 | 0.235 | 0.249 | 24 | 77 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.471 | 0.385 | 0.402 | 40 | 63 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.708 | 0.635 | 0.650 | 64 | 37 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN5 | team_total | 0.273 | 0.200 | 0.213 | 21 | 81 | yes | +0.051 | OK |
| KXNHLGAME-26OCT31TORVAN-TOR | game_winner | 0.544 | 0.615 | 0.601 | 62 | 39 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.188 | 0.265 | 0.248 | 28 | 75 | no | +0.049 | OK |
| KXNHLGAME-26OCT31OTTSJ-SJ | game_winner | 0.502 | 0.435 | 0.448 | 44 | 57 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT31TORVAN-10 | game_total | 0.171 | 0.115 | 0.125 | 12 | 89 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT31CHIBOS-6 | game_total | 0.510 | 0.575 | 0.562 | 58 | 43 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ3 | team_total | 0.647 | 0.585 | 0.598 | 59 | 42 | yes | +0.040 | OK |
| KXNHLGAME-26OCT31TORVAN-VAN | game_winner | 0.456 | 0.390 | 0.403 | 40 | 62 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.761 | 0.820 | 0.809 | 83 | 19 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT31TORVAN-6 | game_total | 0.704 | 0.640 | 0.653 | 65 | 37 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.689 | 0.745 | 0.734 | 75 | 26 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT3 | game_spread | 0.180 | 0.235 | 0.223 | 24 | 77 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.209 | 0.270 | 0.257 | 28 | 74 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL4 | team_total | 0.328 | 0.390 | 0.377 | 40 | 62 | no | +0.035 | OK |
| KXNHLGAME-26OCT31OTTSJ-OTT | game_winner | 0.498 | 0.555 | 0.544 | 56 | 45 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR3 | game_spread | 0.223 | 0.275 | 0.264 | 28 | 73 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR2 | game_spread | 0.341 | 0.395 | 0.384 | 40 | 61 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT31TORVAN-7 | game_total | 0.599 | 0.545 | 0.556 | 55 | 46 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.371 | 0.440 | 0.426 | 46 | 58 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.264 | 0.200 | 0.212 | 22 | 82 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL3 | team_total | 0.552 | 0.610 | 0.599 | 62 | 40 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.137 | 0.095 | 0.102 | 10 | 91 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN6 | team_total | 0.137 | 0.085 | 0.094 | 10 | 93 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT2 | game_spread | 0.294 | 0.345 | 0.334 | 35 | 66 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT31STLDET-STL3 | game_spread | 0.149 | 0.200 | 0.189 | 21 | 81 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ2 | game_spread | 0.293 | 0.245 | 0.254 | 25 | 76 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT31STLDET-4 | game_total | 0.811 | 0.860 | 0.851 | 87 | 15 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN2 | game_spread | 0.261 | 0.210 | 0.220 | 22 | 80 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT31CHIBOS-5 | game_total | 0.729 | 0.780 | 0.770 | 79 | 23 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ4 | team_total | 0.436 | 0.385 | 0.395 | 39 | 62 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT31CHIBOS-7 | game_total | 0.395 | 0.445 | 0.435 | 45 | 56 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT31STLDET-5 | game_total | 0.720 | 0.770 | 0.761 | 78 | 24 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT31STLDET-7 | game_total | 0.377 | 0.430 | 0.419 | 44 | 58 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT31EDMNYI-EDM2 | game_spread | 0.289 | 0.335 | 0.325 | 34 | 67 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT31EDMNYI-EDM3 | game_spread | 0.173 | 0.220 | 0.210 | 23 | 79 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ6 | team_total | 0.121 | 0.080 | 0.087 | 9 | 93 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI5 | team_total | 0.225 | 0.175 | 0.184 | 19 | 84 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL2 | team_total | 0.778 | 0.820 | 0.812 | 83 | 19 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-7 | game_total | 0.342 | 0.385 | 0.376 | 39 | 62 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT31CHIBOS-BOS4 | team_total | 0.472 | 0.515 | 0.506 | 52 | 49 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI4 | team_total | 0.407 | 0.365 | 0.373 | 37 | 64 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT31EDMNYI-NYI2 | game_spread | 0.283 | 0.245 | 0.252 | 25 | 76 | yes | +0.020 | OK |
| KXNHLGAME-26OCT31TBNSH-NSH | game_winner | 0.427 | 0.385 | 0.393 | 39 | 62 | yes | +0.020 | OK |
| KXNHLGAME-26OCT31TBNSH-TB | game_winner | 0.573 | 0.615 | 0.607 | 62 | 39 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB3 | game_spread | 0.217 | 0.260 | 0.251 | 27 | 75 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL2 | game_spread | 0.344 | 0.390 | 0.381 | 40 | 62 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN2 | team_total | 0.850 | 0.810 | 0.819 | 82 | 20 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ5 | team_total | 0.251 | 0.205 | 0.214 | 22 | 81 | yes | +0.019 | OK |
| KXNHLGAME-26OCT31CBJDAL-CBJ | game_winner | 0.416 | 0.375 | 0.383 | 38 | 63 | yes | +0.019 | OK |
| KXNHLGAME-26OCT31CBJDAL-DAL | game_winner | 0.584 | 0.625 | 0.617 | 63 | 38 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5 | team_total | 0.125 | 0.085 | 0.092 | 10 | 93 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL5 | team_total | 0.190 | 0.235 | 0.225 | 25 | 78 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT31TORVAN-5 | game_total | 0.868 | 0.830 | 0.838 | 84 | 18 | yes | +0.018 | OK |
| KXNHLGAME-26OCT31EDMNYI-NYI | game_winner | 0.494 | 0.455 | 0.463 | 46 | 55 | yes | +0.017 | OK |
| KXNHLGAME-26OCT31EDMNYI-EDM | game_winner | 0.506 | 0.545 | 0.537 | 55 | 46 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT31CHIBOS-4 | game_total | 0.825 | 0.860 | 0.853 | 87 | 15 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT31CHIBOS-BOS3 | team_total | 0.690 | 0.730 | 0.722 | 74 | 28 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT31STLDET-STL5 | team_total | 0.164 | 0.200 | 0.192 | 21 | 81 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT31CHIBOS-CHI2 | team_total | 0.681 | 0.720 | 0.712 | 73 | 29 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL2 | team_total | 0.805 | 0.845 | 0.838 | 86 | 17 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL2 | team_total | 0.900 | 0.935 | 0.929 | 95 | 8 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT31STLDET-8 | game_total | 0.204 | 0.235 | 0.228 | 24 | 77 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT31STLDET-6 | game_total | 0.489 | 0.530 | 0.522 | 54 | 48 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT31TBNSH-TB2 | game_spread | 0.350 | 0.385 | 0.378 | 39 | 62 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN3 | game_spread | 0.161 | 0.135 | 0.140 | 14 | 87 | yes | +0.012 | OK |
| KXNHLSPREAD-26OCT31STLDET-STL2 | game_spread | 0.264 | 0.295 | 0.289 | 30 | 71 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI3 | team_total | 0.618 | 0.580 | 0.588 | 59 | 43 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-5 | game_total | 0.798 | 0.825 | 0.820 | 83 | 18 | no | +0.011 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 19 recommended · full analysis in card.md / packet.json `thesis_card`

- Casey Mittelstadt: 1+ goals YES @ 16c · p 0.2219 (adj 0.2052) · $10.0 · thesis BOS:OFFENSE_4PLUS
- Sheldon Dries: 1+ goals YES @ 7c · p 0.1134 (adj 0.0963) · $4.85 · thesis DET:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 35c · p 0.4077 (adj 0.387) · $8.06 · thesis DET:OFFENSE_4PLUS
- Tampa Bay wins by over 1.5 goals NO @ 62c · p 0.694 (adj 0.6545) · $13.08 · thesis NSH:WINS
- Mattias Ekholm: 1+ goals YES @ 7c · p 0.1092 (adj 0.0932) · $4.11 · thesis EDM:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 13c · p 0.1778 (adj 0.1571) · $4.76 · thesis NYI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 22c · p 0.2631 (adj 0.2486) · $4.82 · thesis NYI:OFFENSE_4PLUS
- Full Game: Over 6.5 goals scored YES @ 46c · p 0.5323 (adj 0.4937) · $3.58 · thesis GAME:HIGH_EVENT
- Scott Laughton: 1+ goals YES @ 13c · p 0.1597 (adj 0.1498) · $2.87 · thesis LAK:OFFENSE_4PLUS
- Buffalo wins by over 2.5 goals NO @ 80c · p 0.8535 (adj 0.8242) · $15.5 · thesis LAK:WINS
- Buffalo wins by over 1.5 goals NO @ 70c · p 0.7609 (adj 0.728) · $2.4 · thesis LAK:WINS
- Thomas Chabot: 1+ assists NO @ 71c · p 0.789 (adj 0.742) · $18.06 · thesis OTT:SUPPRESSED
- Toronto wins by over 2.5 goals NO @ 73c · p 0.8128 (adj 0.7689) · $20.0 · thesis VAN:WINS
- Vancouver wins by over 1.5 goals YES @ 22c · p 0.2864 (adj 0.2482) · $2.84 · thesis VAN:WINS_BY_2PLUS
- Columbus over 3.5 goals scored YES @ 26c · p 0.3247 (adj 0.2873) · $3.54 · thesis CBJ:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 74c · p 0.7989 (adj 0.7645) · $8.95 · thesis CBJ:WINS
- Colorado wins by over 1.5 goals NO @ 40c · p 0.5343 (adj 0.4438) · $8.32 · thesis GAME:TIGHT
- Colorado wins by over 2.5 goals NO @ 55c · p 0.6738 (adj 0.5901) · $4.0 · thesis GAME:TIGHT
- Colorado over 5.5 goals scored NO @ 75c · p 0.8172 (adj 0.7761) · $4.61 · thesis CGY:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BOS** · priced 168/169 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- BOS net: Jeremy Swayman (PROJECTED) exp shots 25.06, exp saves 22.13 (sd 6.08), pull risk 0.043
- CHI net: Spencer Knight (PROJECTED) exp shots 28.59, exp saves 24.14 (sd 6.84), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.299 | 0.405 | 42/61 | +0.074 | STANDARD |
| David Pastrnak: 1+ points | 0.702 | 0.600 | 76/56 | -0.070 | STANDARD |
| Connor Bedard: 1+ assists | 0.361 | 0.440 | 46/58 | +0.041 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.433 | 0.510 | 53/51 | +0.040 | STANDARD |
| David Pastrnak: 2+ points | 0.338 | 0.410 | 44/62 | +0.026 | STANDARD |
| Casey Mittelstadt: 1+ points | 0.474 | 0.405 | 42/61 | +0.037 | STANDARD |

**STL @ DET** · priced 141/148 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- DET net: John Gibson (CONFIRMED) exp shots 25.58, exp saves 22.14 (sd 6.28), pull risk 0.06
- STL net: Joel Hofer (PROJECTED) exp shots 28.81, exp saves 24.9 (sd 6.67), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Holloway: 1+ points | 0.552 | 0.305 | 55/94 | -0.015 | STANDARD |
| Jimmy Snuggerud: 1+ points | 0.559 | 0.320 | 58/94 | -0.038 | STANDARD |
| Philip Broberg: 1+ points | 0.463 | 0.265 | 47/94 | -0.024 | STANDARD |
| Robert Thomas: 1+ points | 0.569 | 0.375 | 69/94 | -0.136 | STANDARD |
| Mason McTavish: 1+ points | 0.442 | 0.290 | 52/94 | -0.096 | STANDARD |
| Jake Neighbours: 1+ points | 0.429 | 0.285 | 51/94 | -0.098 | STANDARD |

**TBL @ NSH** · priced 164/165 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NSH net: Juuse Saros (PROJECTED) exp shots 29.61, exp saves 25.52 (sd 6.92), pull risk 0.063
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.75, exp saves 22.27 (sd 6.26), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.469 | 0.605 | 64/43 | +0.084 | STANDARD |
| Nikita Kucherov: 2+ points | 0.278 | 0.405 | 44/63 | +0.076 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.134 | 0.250 | 27/77 | +0.084 | STANDARD |
| Filip Forsberg: 2+ points | 0.248 | 0.145 | 26/97 | -0.025 | STANDARD |
| Ryan O'Reilly: 2+ points | 0.222 | 0.120 | 22/98 | -0.010 | STANDARD |
| Charle-Edouard D'Astous: 1+ points | 0.374 | 0.455 | 49/58 | +0.029 | STANDARD |

**EDM @ NYI** · priced 163/164 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.15, exp saves 23.17 (sd 6.5), pull risk 0.077
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.76, exp saves 23.97 (sd 6.69), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 1+ points | 0.701 | 0.585 | 78/61 | -0.091 | STANDARD |
| Connor McDavid: 2+ assists | 0.195 | 0.300 | 33/73 | +0.061 | STANDARD |
| Connor McDavid: 1+ assists | 0.556 | 0.660 | 68/36 | +0.067 | STANDARD |
| Evan Bouchard: 1+ points | 0.671 | 0.570 | 70/56 | -0.043 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.210 | 0.110 | 17/95 | +0.030 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.271 | 0.370 | 40/66 | +0.054 | STANDARD |

**BUF @ LAK** · priced 164/165 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.66, exp saves 24.12 (sd 6.57), pull risk 0.055
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 28.05, exp saves 24.01 (sd 6.64), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Laferriere: 2+ points | 0.205 | 0.110 | 20/98 | -0.006 | STANDARD |
| Tage Thompson: 1+ assists | 0.323 | 0.395 | 42/63 | +0.031 | STANDARD |
| Trevor Moore: 1+ points | 0.460 | 0.390 | 42/64 | +0.023 | STANDARD |
| Trevor Moore: 1+ assists | 0.312 | 0.245 | 27/78 | +0.028 | STANDARD |
| Adrian Kempe: 2+ points | 0.232 | 0.165 | 26/93 | -0.042 | STANDARD |
| Artemi Panarin: 2+ points | 0.240 | 0.180 | 29/93 | -0.064 | STANDARD |

**OTT @ SJS** · priced 167/168 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.35, exp saves 24.27 (sd 6.75), pull risk 0.069
- OTT net: Jonas Johansson (PROJECTED) exp shots 25.93, exp saves 22.44 (sd 6.27), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ points | 0.618 | 0.480 | 73/77 | -0.126 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.441 | 0.540 | 55/47 | +0.071 | STANDARD |
| Thomas Chabot: 1+ assists | 0.211 | 0.305 | 32/71 | +0.065 | STANDARD |
| Jake Sanderson: 1+ assists | 0.353 | 0.445 | 47/58 | +0.050 | STANDARD |
| Jake Sanderson: 1+ points | 0.439 | 0.530 | 54/48 | +0.064 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.315 | 0.230 | 26/80 | +0.042 | STANDARD |

**PIT @ MTL** · priced 167/168 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- MTL net: Jakub Dobes (PROJECTED) exp shots 28.16, exp saves 24.52 (sd 6.7), pull risk 0.065
- PIT net: Arturs Silovs (PROJECTED) exp shots 26.26, exp saves 22.48 (sd 6.52), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zachary Bolduc: 2+ goals | 0.021 | 0.485 | 96/99 | -0.011 | STANDARD |
| Thomas Novak: 2+ goals | 0.021 | 0.485 | 96/99 | -0.012 | STANDARD |
| Cole Caufield: 3+ goals | 0.016 | 0.480 | 95/99 | -0.007 | STANDARD |
| Egor Chinakhov: 2+ goals | 0.022 | 0.480 | 95/99 | -0.012 | STANDARD |
| Evgeni Malkin: 2+ goals | 0.031 | 0.480 | 95/99 | -0.021 | STANDARD |
| Egor Chinakhov: First Goalscorer | 0.035 | 0.475 | 94/99 | -0.026 | STANDARD |

**TOR @ VAN** · priced 151/167 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- VAN net: Leevi Merilainen (PROJECTED) exp shots 28.88, exp saves 24.83 (sd 6.77), pull risk 0.071
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 28.15, exp saves 24.21 (sd 6.71), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Nylander: 4+ points | 0.018 | 0.465 | 92/99 | -0.008 | STANDARD |
| Oliver Ekman-Larsson: 2+ points | 0.044 | 0.490 | 96/98 | -0.026 | STANDARD |
| Auston Matthews: 4+ points | 0.022 | 0.465 | 92/99 | -0.013 | STANDARD |
| Jake McCabe: 2+ points | 0.053 | 0.490 | 96/98 | -0.034 | STANDARD |
| Nick Paul: 2+ points | 0.072 | 0.490 | 96/98 | -0.053 | STANDARD |
| Zeev Buium: 2+ points | 0.079 | 0.490 | 96/98 | -0.061 | STANDARD |

**CBJ @ DAL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.99, exp saves 21.81 (sd 6.08), pull risk 0.048
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.69, exp saves 23.04 (sd 6.37), pull risk 0.061

**CGY @ COL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.33, exp saves 23.28 (sd 6.26), pull risk 0.044
- CGY net: Dustin Wolf (PROJECTED) exp shots 33.08, exp saves 27.77 (sd 7.8), pull risk 0.097

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
