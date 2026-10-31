# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T20:14:26Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 4 · markets on board: 3703 · contracts joined: 945 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 845, 'OK': 79, 'NO_EDGE': 21}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 143, 'game_early_goal': 4, 'first_goal': 143, 'game_winner': 8, 'player_goals': 253, 'game_overtime': 4, 'player_points': 196, 'goalie_saves': 6, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ MTL | 2026-10-31T23:00:00Z | T-90m | 0.628 | 0.372 | 0.167 | 6.44 | 3.63 | 2.82 | 257 (25/232) | CONFIRMED/CONFIRMED |
| TOR @ VAN | 2026-10-31T23:00:00Z | T-90m | 0.448 | 0.552 | 0.160 | 7.23 | 3.45 | 3.79 | 225 (25/200) | PROJECTED/CONFIRMED |
| CBJ @ DAL | 2026-11-01T00:00:00Z | T-3h | 0.584 | 0.416 | 0.185 | 5.49 | 2.99 | 2.50 | 233 (25/208) | CONFIRMED/CONFIRMED |
| CGY @ COL | 2026-11-01T02:00:00Z | T-3h | 0.677 | 0.323 | 0.163 | 6.21 | 3.68 | 2.53 | 230 (25/205) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.310 | 0.475 | 0.440 | 48 | 53 | no | +0.143 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.452 | 0.605 | 0.575 | 61 | 40 | no | +0.131 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.514 | 0.660 | 0.632 | 67 | 35 | no | +0.120 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.310 | 0.450 | 0.420 | 46 | 56 | no | +0.113 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.677 | 0.795 | 0.774 | 80 | 21 | no | +0.102 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.323 | 0.215 | 0.234 | 22 | 79 | yes | +0.091 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.158 | 0.265 | 0.240 | 27 | 74 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3 | team_total | 0.667 | 0.565 | 0.586 | 57 | 44 | yes | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4 | team_total | 0.461 | 0.360 | 0.379 | 37 | 65 | yes | +0.074 | OK |
| KXNHLGAME-26OCT31PITMTL-MTL | game_winner | 0.628 | 0.535 | 0.554 | 54 | 47 | yes | +0.071 | OK |
| KXNHLGAME-26OCT31PITMTL-PIT | game_winner | 0.372 | 0.465 | 0.446 | 47 | 54 | no | +0.071 | OK |
| KXNHLTOTAL-26OCT31TORVAN-8 | game_total | 0.411 | 0.320 | 0.337 | 33 | 69 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT31TORVAN-9 | game_total | 0.318 | 0.235 | 0.250 | 24 | 77 | yes | +0.065 | OK |
| KXNHLGAME-26OCT31TORVAN-TOR | game_winner | 0.552 | 0.635 | 0.619 | 64 | 37 | no | +0.061 | OK |
| KXNHLGAME-26OCT31TORVAN-VAN | game_winner | 0.448 | 0.365 | 0.381 | 37 | 64 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN5 | team_total | 0.271 | 0.185 | 0.200 | 20 | 83 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT4 | team_total | 0.323 | 0.405 | 0.388 | 41 | 60 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL2 | game_spread | 0.405 | 0.325 | 0.340 | 33 | 68 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.730 | 0.820 | 0.804 | 84 | 20 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT3 | team_total | 0.537 | 0.620 | 0.604 | 63 | 39 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT31TORVAN-7 | game_total | 0.609 | 0.535 | 0.550 | 54 | 47 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.675 | 0.745 | 0.732 | 75 | 26 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.363 | 0.435 | 0.420 | 44 | 57 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.261 | 0.195 | 0.207 | 20 | 81 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.705 | 0.635 | 0.650 | 64 | 37 | yes | +0.049 | OK |
| KXNHLTOTAL-26OCT31TORVAN-10 | game_total | 0.176 | 0.115 | 0.126 | 12 | 89 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.465 | 0.390 | 0.405 | 40 | 62 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR3 | game_spread | 0.227 | 0.295 | 0.281 | 30 | 71 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT2 | game_spread | 0.190 | 0.255 | 0.241 | 26 | 75 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT3 | game_spread | 0.105 | 0.165 | 0.151 | 17 | 84 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT31TORVAN-6 | game_total | 0.712 | 0.645 | 0.659 | 65 | 36 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN6 | team_total | 0.141 | 0.075 | 0.085 | 9 | 94 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR2 | game_spread | 0.348 | 0.415 | 0.401 | 42 | 59 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-6 | game_total | 0.559 | 0.625 | 0.612 | 63 | 38 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.150 | 0.095 | 0.104 | 10 | 91 | yes | +0.044 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.206 | 0.265 | 0.252 | 27 | 74 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN2 | team_total | 0.851 | 0.790 | 0.803 | 80 | 22 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN2 | game_spread | 0.260 | 0.205 | 0.215 | 21 | 80 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL3 | team_total | 0.586 | 0.650 | 0.638 | 66 | 36 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT5 | team_total | 0.161 | 0.225 | 0.211 | 24 | 79 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT2 | team_total | 0.762 | 0.820 | 0.809 | 83 | 19 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL3 | game_spread | 0.266 | 0.215 | 0.225 | 22 | 79 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL2 | game_spread | 0.341 | 0.395 | 0.384 | 40 | 61 | no | +0.032 | OK |
| KXNHLGAME-26OCT31CBJDAL-CBJ | game_winner | 0.416 | 0.365 | 0.375 | 37 | 64 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL2 | team_total | 0.886 | 0.935 | 0.927 | 95 | 8 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL5 | team_total | 0.179 | 0.235 | 0.223 | 25 | 78 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-7 | game_total | 0.445 | 0.495 | 0.485 | 50 | 51 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-5 | game_total | 0.773 | 0.825 | 0.815 | 84 | 19 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-8 | game_total | 0.261 | 0.305 | 0.296 | 31 | 70 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-6 | game_total | 0.438 | 0.485 | 0.476 | 49 | 52 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-7 | game_total | 0.330 | 0.375 | 0.366 | 38 | 63 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN3 | game_spread | 0.161 | 0.125 | 0.132 | 13 | 88 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-4 | game_total | 0.862 | 0.900 | 0.893 | 91 | 11 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT31TORVAN-5 | game_total | 0.870 | 0.835 | 0.843 | 84 | 17 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT31PITMTL-5 | game_total | 0.800 | 0.835 | 0.828 | 84 | 17 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL2 | team_total | 0.800 | 0.840 | 0.833 | 85 | 17 | no | +0.020 | OK |
| KXNHLGAME-26OCT31CBJDAL-DAL | game_winner | 0.584 | 0.625 | 0.617 | 63 | 38 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-4 | game_total | 0.780 | 0.820 | 0.812 | 83 | 19 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL4 | team_total | 0.505 | 0.460 | 0.469 | 47 | 55 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-8 | game_total | 0.164 | 0.195 | 0.188 | 20 | 81 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-9 | game_total | 0.107 | 0.135 | 0.129 | 14 | 87 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT31PITMTL-8 | game_total | 0.291 | 0.325 | 0.318 | 33 | 68 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5 | team_total | 0.120 | 0.085 | 0.091 | 10 | 93 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT31PITMTL-7 | game_total | 0.490 | 0.525 | 0.518 | 53 | 48 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY3 | game_spread | 0.075 | 0.050 | 0.054 | 6 | 96 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-3 | game_total | 0.936 | 0.960 | 0.956 | 97 | 5 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT31PITMTL-6 | game_total | 0.605 | 0.635 | 0.629 | 64 | 37 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL6 | team_total | 0.075 | 0.105 | 0.098 | 12 | 91 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL5 | team_total | 0.302 | 0.265 | 0.272 | 28 | 75 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-10 | game_total | 0.087 | 0.105 | 0.101 | 11 | 90 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL3 | team_total | 0.711 | 0.675 | 0.682 | 69 | 34 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL6 | team_total | 0.154 | 0.130 | 0.134 | 14 | 88 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-9 | game_total | 0.183 | 0.215 | 0.208 | 23 | 80 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT31PITMTL-4 | game_total | 0.878 | 0.900 | 0.896 | 91 | 11 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-CBJ2 | game_spread | 0.205 | 0.185 | 0.189 | 19 | 82 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-10 | game_total | 0.043 | 0.055 | 0.052 | 6 | 95 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-3 | game_total | 0.965 | 0.980 | 0.978 | 99 | 3 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT31TORVAN-2 | game_total | 0.994 | 0.985 | 0.987 | 99 | 2 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT6 | team_total | 0.065 | 0.085 | 0.081 | 10 | 93 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT31TORVAN-4 | game_total | 0.925 | 0.915 | 0.917 | 92 | 9 |  | -0.000 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ MTL | 0.628 | 0.520 | 0.167 | 0.213 | 6.44 | 6.62 | 0.983/1.012 | KXNHLGAME-26OCT31PITMTL-MTL -0.109 |
| TOR @ VAN | 0.448 | 0.502 | 0.160 | 0.211 | 7.23 | 6.67 | 1.021/0.956 | KXNHLTEAMTOTAL-26OCT31TORVAN-TOR4 -0.096 |
| CBJ @ DAL | 0.584 | 0.534 | 0.185 | 0.224 | 5.49 | 5.92 | 0.995/0.947 | KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3 +0.090 |
| CGY @ COL | 0.677 | 0.694 | 0.163 | 0.189 | 6.21 | 6.54 | 0.979/0.992 | KXNHLTOTAL-26OCT31CGYCOL-7 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Blake Lizotte: 1+ goals YES @ 9c · p 0.1208 (adj 0.1106) · $3.77 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1592 (adj 0.1494) · $3.02 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 30c · p 0.3369 (adj 0.3264) · $4.13 · thesis PIT:OFFENSE_4PLUS
- Zachary Bolduc: 1+ assists YES @ 25c · p 0.3028 (adj 0.2739) · $3.64 · thesis MTL:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2694 (adj 0.247) · $12.95 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 18c · p 0.2467 (adj 0.2263) · $9.9 · thesis VAN:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 71c · p 0.7837 (adj 0.764) · $20.0 · thesis TOR:SUPPRESSED
- Toronto wins by over 1.5 goals NO @ 59c · p 0.7164 (adj 0.631) · $5.77 · thesis VAN:WINS
- Damon Severson: 1+ goals YES @ 6c · p 0.1066 (adj 0.0925) · $6.17 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 18c · p 0.2535 (adj 0.2339) · $12.22 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1869 (adj 0.1702) · $8.21 · thesis CBJ:OFFENSE_4PLUS
- Ryan Lomberg: 1+ goals YES @ 5c · p 0.0771 (adj 0.0691) · $3.4 · thesis CBJ:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 74c · p 0.803 (adj 0.786) · $20.0 · thesis COL:SUPPRESSED
- Calgary over 3.5 goals scored YES @ 20c · p 0.2829 (adj 0.2389) · $7.02 · thesis CGY:OFFENSE_4PLUS
- Colorado wins by over 1.5 goals NO @ 40c · p 0.5235 (adj 0.44) · $3.89 · thesis GAME:TIGHT
- Mackenzie Blackwood: 22+ saves YES @ 53c · p 0.6077 (adj 0.5614) · $10.16 · thesis COL:NET_HIGH_VOLUME

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ MTL** · priced 203/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.16, exp saves 24.42 (sd 6.68), pull risk 0.067
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.26, exp saves 22.49 (sd 6.49), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sergei Murashov: 27+ saves | 0.259 | 0.375 | 41/66 | +0.065 |  |
| Spencer Stastney: 1+ points | 0.217 | 0.120 | 22/98 | -0.015 | STANDARD |
| Samuel Girard: 1+ assists | 0.231 | 0.135 | 25/98 | -0.032 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.277 | 0.210 | 23/81 | +0.034 | STANDARD |
| Spencer Stastney: 1+ assists | 0.181 | 0.120 | 19/95 | -0.020 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.303 | 0.245 | 25/76 | +0.040 | STANDARD |

**TOR @ VAN** · priced 160/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.88, exp saves 24.85 (sd 6.73), pull risk 0.069
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 28.15, exp saves 24.18 (sd 6.78), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Linus Karlsson: 1+ points | 0.494 | 0.370 | 39/65 | +0.087 | STANDARD |
| Auston Matthews: 1+ assists | 0.406 | 0.525 | 54/49 | +0.086 | STANDARD |
| Auston Matthews: 2+ points | 0.289 | 0.405 | 42/61 | +0.084 | STANDARD |
| William Nylander: 1+ assists | 0.411 | 0.525 | 54/49 | +0.081 | STANDARD |
| Gavin McKenna: 1+ points | 0.460 | 0.570 | 58/44 | +0.083 | STANDARD |
| Anthony Stolarz: 25+ saves | 0.480 | 0.370 | 43/69 | +0.033 |  |

**CBJ @ DAL** · priced 181/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.99, exp saves 21.79 (sd 6.04), pull risk 0.05
- CBJ net: Jet Greaves (CONFIRMED) exp shots 26.69, exp saves 23.11 (sd 6.39), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Sillinger: 1+ points | 0.354 | 0.250 | 27/77 | +0.070 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.213 | 0.295 | 30/71 | +0.062 | STANDARD |
| Charlie Coyle: 1+ points | 0.526 | 0.445 | 46/57 | +0.049 | STANDARD |
| Mathieu Olivier: 1+ points | 0.346 | 0.265 | 28/75 | +0.052 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.436 | 0.515 | 53/50 | +0.046 | STANDARD |
| Charlie Coyle: 1+ goals | 0.254 | 0.175 | 18/83 | +0.063 | STANDARD |

**CGY @ COL** · priced 178/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.33, exp saves 23.3 (sd 6.25), pull risk 0.043
- CGY net: Arsenii Sergeev (CONFIRMED) exp shots 33.08, exp saves 27.7 (sd 7.76), pull risk 0.103

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.399 | 0.525 | 53/48 | +0.104 | STANDARD |
| Cale Makar: 1+ assists | 0.474 | 0.590 | 60/42 | +0.089 | STANDARD |
| Cale Makar: 1+ points | 0.579 | 0.685 | 70/33 | +0.075 | STANDARD |
| Cale Makar: 2+ points | 0.209 | 0.310 | 32/70 | +0.077 | STANDARD |
| Mackenzie Blackwood: 22+ saves | 0.608 | 0.515 | 53/50 | +0.060 |  |
| Nathan MacKinnon: 2+ assists | 0.176 | 0.265 | 29/76 | +0.051 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
