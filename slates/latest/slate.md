# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T19:27:15Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 6 · markets on board: 4066 · contracts joined: 1432 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1282, 'OK': 111, 'NO_EDGE': 39}
families: {'period_winner': 54, 'period_spread': 36, 'period_total': 54, 'player_assists': 226, 'game_early_goal': 6, 'first_goal': 214, 'game_winner': 12, 'player_goals': 371, 'game_overtime': 6, 'player_points': 308, 'game_spread': 24, 'team_total': 60, 'game_total': 54, 'goalie_saves': 7}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ LAK | 2026-10-31T20:00:00Z | T-30m | 0.485 | 0.515 | 0.181 | 6.24 | 3.07 | 3.17 | 262 (25/237) | PROJECTED/PROJECTED |
| OTT @ SJS | 2026-10-31T20:00:00Z | T-30m | 0.560 | 0.440 | 0.162 | 6.73 | 3.57 | 3.16 | 226 (25/201) | CONFIRMED/CONFIRMED |
| PIT @ MTL | 2026-10-31T23:00:00Z | T-3h | 0.628 | 0.372 | 0.167 | 6.44 | 3.63 | 2.82 | 257 (25/232) | CONFIRMED/CONFIRMED |
| TOR @ VAN | 2026-10-31T23:00:00Z | T-3h | 0.448 | 0.552 | 0.160 | 7.23 | 3.45 | 3.79 | 225 (25/200) | PROJECTED/CONFIRMED |
| CBJ @ DAL | 2026-11-01T00:00:00Z | T-3h | 0.584 | 0.416 | 0.185 | 5.49 | 2.99 | 2.50 | 232 (25/207) | CONFIRMED/CONFIRMED |
| CGY @ COL | 2026-11-01T02:00:00Z | T-6h | 0.677 | 0.323 | 0.163 | 6.21 | 3.68 | 2.53 | 230 (25/205) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.310 | 0.475 | 0.440 | 48 | 53 | no | +0.143 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.452 | 0.605 | 0.575 | 61 | 40 | no | +0.131 | OK |
| KXNHLGAME-26OCT31OTTSJ-OTT | game_winner | 0.440 | 0.585 | 0.556 | 59 | 42 | no | +0.123 | OK |
| KXNHLGAME-26OCT31OTTSJ-SJ | game_winner | 0.560 | 0.415 | 0.444 | 42 | 59 | yes | +0.123 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.514 | 0.660 | 0.632 | 67 | 35 | no | +0.120 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.310 | 0.445 | 0.417 | 45 | 56 | no | +0.113 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.677 | 0.795 | 0.774 | 80 | 21 | no | +0.102 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ2 | game_spread | 0.351 | 0.235 | 0.256 | 24 | 77 | yes | +0.099 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ3 | team_total | 0.695 | 0.575 | 0.600 | 58 | 43 | yes | +0.098 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.323 | 0.215 | 0.234 | 22 | 79 | yes | +0.091 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.158 | 0.265 | 0.240 | 27 | 74 | no | +0.088 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT3 | game_spread | 0.144 | 0.245 | 0.222 | 25 | 76 | no | +0.083 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ4 | team_total | 0.488 | 0.380 | 0.401 | 39 | 63 | yes | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3 | team_total | 0.667 | 0.560 | 0.582 | 57 | 45 | yes | +0.080 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT2 | game_spread | 0.245 | 0.350 | 0.327 | 36 | 66 | no | +0.079 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4 | team_total | 0.461 | 0.360 | 0.379 | 37 | 65 | yes | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ5 | team_total | 0.296 | 0.195 | 0.213 | 21 | 82 | yes | +0.074 | OK |
| KXNHLGAME-26OCT31PITMTL-MTL | game_winner | 0.628 | 0.535 | 0.554 | 54 | 47 | yes | +0.071 | OK |
| KXNHLGAME-26OCT31PITMTL-PIT | game_winner | 0.372 | 0.465 | 0.446 | 47 | 54 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ3 | game_spread | 0.227 | 0.145 | 0.159 | 15 | 86 | yes | +0.068 | OK |
| KXNHLTOTAL-26OCT31TORVAN-8 | game_total | 0.411 | 0.320 | 0.337 | 33 | 69 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT31TORVAN-9 | game_total | 0.318 | 0.235 | 0.250 | 24 | 77 | yes | +0.065 | OK |
| KXNHLGAME-26OCT31TORVAN-TOR | game_winner | 0.552 | 0.635 | 0.619 | 64 | 37 | no | +0.061 | OK |
| KXNHLGAME-26OCT31TORVAN-VAN | game_winner | 0.448 | 0.365 | 0.381 | 37 | 64 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN5 | team_total | 0.271 | 0.185 | 0.200 | 20 | 83 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT4 | team_total | 0.323 | 0.405 | 0.388 | 41 | 60 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL2 | game_spread | 0.405 | 0.325 | 0.340 | 33 | 68 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.730 | 0.820 | 0.804 | 84 | 20 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT3 | team_total | 0.537 | 0.620 | 0.604 | 63 | 39 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN6 | team_total | 0.141 | 0.070 | 0.081 | 8 | 94 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT31TORVAN-7 | game_total | 0.609 | 0.535 | 0.550 | 54 | 47 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.675 | 0.745 | 0.732 | 75 | 26 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT4 | team_total | 0.401 | 0.480 | 0.464 | 49 | 53 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.363 | 0.435 | 0.420 | 44 | 57 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.261 | 0.195 | 0.207 | 20 | 81 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.705 | 0.630 | 0.646 | 64 | 38 | yes | +0.049 | OK |
| KXNHLTOTAL-26OCT31TORVAN-10 | game_total | 0.176 | 0.115 | 0.126 | 12 | 89 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.465 | 0.390 | 0.405 | 40 | 62 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR3 | game_spread | 0.227 | 0.295 | 0.281 | 30 | 71 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT2 | game_spread | 0.190 | 0.255 | 0.241 | 26 | 75 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT3 | game_spread | 0.105 | 0.165 | 0.151 | 17 | 84 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT31TORVAN-6 | game_total | 0.712 | 0.645 | 0.659 | 65 | 36 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ2 | team_total | 0.866 | 0.805 | 0.819 | 81 | 20 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT3 | team_total | 0.609 | 0.685 | 0.670 | 70 | 33 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-6 | game_total | 0.559 | 0.625 | 0.612 | 63 | 38 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.150 | 0.095 | 0.104 | 10 | 91 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ6 | team_total | 0.149 | 0.080 | 0.091 | 10 | 94 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.206 | 0.265 | 0.252 | 27 | 74 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN2 | team_total | 0.851 | 0.790 | 0.803 | 80 | 22 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT2 | team_total | 0.814 | 0.870 | 0.860 | 88 | 14 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN2 | game_spread | 0.260 | 0.205 | 0.215 | 21 | 80 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL3 | team_total | 0.586 | 0.650 | 0.638 | 66 | 36 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT5 | team_total | 0.161 | 0.215 | 0.203 | 22 | 79 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT2 | team_total | 0.762 | 0.820 | 0.809 | 83 | 19 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT5 | team_total | 0.220 | 0.280 | 0.267 | 29 | 73 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR2 | game_spread | 0.348 | 0.405 | 0.393 | 41 | 60 | no | +0.035 | OK |
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
| KXNHLTOTAL-26OCT31PITMTL-5 | game_total | 0.800 | 0.835 | 0.828 | 84 | 17 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL2 | team_total | 0.800 | 0.840 | 0.833 | 85 | 17 | no | +0.020 | OK |
| KXNHLGAME-26OCT31CBJDAL-DAL | game_winner | 0.584 | 0.625 | 0.617 | 63 | 38 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-4 | game_total | 0.780 | 0.820 | 0.812 | 83 | 19 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT31BUFLA-BUF3 | game_spread | 0.180 | 0.215 | 0.208 | 22 | 79 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL4 | team_total | 0.505 | 0.460 | 0.469 | 47 | 55 | yes | +0.018 | OK |
| KXNHLGAME-26OCT31BUFLA-BUF | game_winner | 0.515 | 0.555 | 0.547 | 56 | 45 | no | +0.017 | OK |
| KXNHLGAME-26OCT31BUFLA-LA | game_winner | 0.485 | 0.445 | 0.453 | 45 | 56 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT31OTTSJ-8 | game_total | 0.331 | 0.295 | 0.302 | 30 | 71 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-8 | game_total | 0.164 | 0.195 | 0.188 | 20 | 81 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-9 | game_total | 0.183 | 0.220 | 0.212 | 23 | 79 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-9 | game_total | 0.107 | 0.135 | 0.129 | 14 | 87 | no | +0.015 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ LAK | 0.485 | 0.542 | 0.181 | 0.223 | 6.24 | 6.19 | 0.993/0.998 | KXNHLGAME-26OCT31BUFLA-BUF -0.057 |
| OTT @ SJS | 0.560 | 0.517 | 0.162 | 0.210 | 6.73 | 6.51 | 1.022/1.072 | KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ5 -0.052 |
| PIT @ MTL | 0.628 | 0.520 | 0.167 | 0.213 | 6.44 | 6.62 | 0.983/1.012 | KXNHLGAME-26OCT31PITMTL-MTL -0.109 |
| TOR @ VAN | 0.448 | 0.502 | 0.160 | 0.211 | 7.23 | 6.67 | 1.021/0.956 | KXNHLTEAMTOTAL-26OCT31TORVAN-TOR4 -0.096 |
| CBJ @ DAL | 0.584 | 0.534 | 0.185 | 0.224 | 5.49 | 5.92 | 0.995/0.947 | KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3 +0.090 |
| CGY @ COL | 0.677 | 0.694 | 0.163 | 0.189 | 6.21 | 6.54 | 0.979/0.992 | KXNHLTOTAL-26OCT31CGYCOL-7 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 24 recommended · full analysis in card.md / packet.json `thesis_card`

- Joel Edmundson: 1+ goals YES @ 5c · p 0.0859 (adj 0.0769) · $3.92 · thesis LAK:WINS_BY_2PLUS
- Alex Laferriere: 2+ goals YES @ 3c · p 0.0561 (adj 0.0471) · $2.25 · thesis LAK:OFFENSE_4PLUS
- Andre Lee: 1+ goals YES @ 9c · p 0.1371 (adj 0.1191) · $4.01 · thesis LAK:OFFENSE_4PLUS
- Scott Laughton: 1+ goals YES @ 13c · p 0.1658 (adj 0.1556) · $3.42 · thesis LAK:OFFENSE_4PLUS
- Mason Marchment: 1+ goals YES @ 22c · p 0.273 (adj 0.2573) · $5.25 · thesis SJS:OFFENSE_4PLUS
- Barclay Goodrow: 1+ goals YES @ 6c · p 0.0825 (adj 0.0744) · $1.67 · thesis SJS:WINS_BY_2PLUS
- Ottawa wins by over 2.5 goals NO @ 76c · p 0.8219 (adj 0.7884) · $12.37 · thesis SJS:WINS
- Ivar Stenberg: 1+ goals NO @ 79c · p 0.8236 (adj 0.8139) · $13.0 · thesis SJS:SUPPRESSED
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1208 (adj 0.1106) · $2.8 · thesis PIT:OFFENSE_4PLUS
- Zachary Bolduc: 1+ assists YES @ 24c · p 0.3028 (adj 0.2689) · $3.81 · thesis MTL:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1592 (adj 0.1494) · $2.22 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 30c · p 0.3369 (adj 0.3264) · $3.02 · thesis PIT:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2694 (adj 0.2483) · $10.04 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 18c · p 0.2467 (adj 0.2263) · $7.46 · thesis VAN:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 71c · p 0.7837 (adj 0.764) · $14.7 · thesis TOR:SUPPRESSED
- Arshdeep Bains: 1+ goals YES @ 8c · p 0.1178 (adj 0.1071) · $3.95 · thesis VAN:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 18c · p 0.2535 (adj 0.2339) · $9.09 · thesis CBJ:OFFENSE_4PLUS
- Damon Severson: 1+ goals YES @ 6c · p 0.1066 (adj 0.0912) · $4.32 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1869 (adj 0.1702) · $6.11 · thesis CBJ:OFFENSE_4PLUS
- Ryan Lomberg: 1+ goals YES @ 5c · p 0.0771 (adj 0.0691) · $2.53 · thesis CBJ:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 74c · p 0.803 (adj 0.786) · $14.7 · thesis COL:SUPPRESSED
- Calgary over 3.5 goals scored YES @ 20c · p 0.2829 (adj 0.2389) · $5.55 · thesis CGY:OFFENSE_4PLUS
- Colorado over 5.5 goals scored NO @ 74c · p 0.8105 (adj 0.7728) · $11.89 · thesis CGY:WINS
- Colorado over 4.5 goals scored NO @ 56c · p 0.6383 (adj 0.5966) · $1.91 · thesis CGY:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ LAK** · priced 201/211 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.66, exp saves 24.15 (sd 6.48), pull risk 0.054
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 28.05, exp saves 24.03 (sd 6.55), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikey Anderson: 1+ points | 0.292 | 0.095 | 17/98 | +0.112 | STANDARD |
| Joel Edmundson: 1+ points | 0.299 | 0.110 | 20/98 | +0.088 | STANDARD |
| Brian Dumoulin: 1+ points | 0.283 | 0.110 | 20/98 | +0.072 | STANDARD |
| Brian Dumoulin: 1+ assists | 0.248 | 0.080 | 14/98 | +0.099 | STANDARD |
| Mikey Anderson: 1+ assists | 0.247 | 0.085 | 15/98 | +0.088 | STANDARD |
| Samuel Helenius: 1+ points | 0.229 | 0.075 | 13/98 | +0.091 | STANDARD |

**OTT @ SJS** · priced 172/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 28.35, exp saves 24.36 (sd 6.74), pull risk 0.066
- OTT net: Samuel Ersson (CONFIRMED) exp shots 25.93, exp saves 22.35 (sd 6.35), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.442 | 0.545 | 56/47 | +0.070 | STANDARD |
| Macklin Celebrini: 2+ points | 0.298 | 0.395 | 40/61 | +0.075 | STANDARD |
| Collin Graf: 1+ points | 0.429 | 0.345 | 36/67 | +0.053 | STANDARD |
| Tim Stutzle: 2+ points | 0.262 | 0.335 | 34/67 | +0.053 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.318 | 0.245 | 26/77 | +0.044 | STANDARD |
| Jake Sanderson: 1+ assists | 0.372 | 0.445 | 46/57 | +0.041 | STANDARD |

**PIT @ MTL** · priced 203/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.16, exp saves 24.42 (sd 6.68), pull risk 0.067
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.26, exp saves 22.49 (sd 6.49), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sergei Murashov: 27+ saves | 0.259 | 0.375 | 39/64 | +0.084 |  |
| Spencer Stastney: 1+ points | 0.217 | 0.120 | 22/98 | -0.015 | STANDARD |
| Samuel Girard: 1+ assists | 0.231 | 0.135 | 25/98 | -0.032 | STANDARD |
| Spencer Stastney: 1+ assists | 0.181 | 0.110 | 20/98 | -0.030 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.303 | 0.235 | 24/77 | +0.050 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.277 | 0.215 | 24/81 | +0.024 | STANDARD |

**TOR @ VAN** · priced 160/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.88, exp saves 24.85 (sd 6.73), pull risk 0.069
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 28.15, exp saves 24.18 (sd 6.78), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Linus Karlsson: 1+ points | 0.494 | 0.370 | 39/65 | +0.087 | STANDARD |
| Auston Matthews: 1+ assists | 0.406 | 0.525 | 54/49 | +0.086 | STANDARD |
| William Nylander: 1+ assists | 0.411 | 0.525 | 54/49 | +0.081 | STANDARD |
| Gavin McKenna: 1+ assists | 0.312 | 0.425 | 44/59 | +0.081 | STANDARD |
| Anthony Stolarz: 25+ saves | 0.480 | 0.370 | 43/69 | +0.033 |  |
| Auston Matthews: 2+ points | 0.289 | 0.395 | 42/63 | +0.064 | STANDARD |

**CBJ @ DAL** · priced 180/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.99, exp saves 21.79 (sd 6.04), pull risk 0.05
- CBJ net: Jet Greaves (CONFIRMED) exp shots 26.69, exp saves 23.11 (sd 6.39), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Sillinger: 1+ points | 0.354 | 0.250 | 27/77 | +0.070 | STANDARD |
| Mathieu Olivier: 1+ points | 0.346 | 0.250 | 27/77 | +0.062 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.213 | 0.300 | 31/71 | +0.062 | STANDARD |
| Charlie Coyle: 1+ points | 0.526 | 0.445 | 46/57 | +0.049 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.436 | 0.515 | 53/50 | +0.046 | STANDARD |
| Charlie Coyle: 1+ goals | 0.254 | 0.175 | 18/83 | +0.063 | STANDARD |

**CGY @ COL** · priced 178/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.33, exp saves 23.3 (sd 6.25), pull risk 0.043
- CGY net: Arsenii Sergeev (CONFIRMED) exp shots 33.08, exp saves 27.7 (sd 7.76), pull risk 0.103

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.399 | 0.525 | 53/48 | +0.104 | STANDARD |
| Cale Makar: 1+ assists | 0.474 | 0.595 | 61/42 | +0.089 | STANDARD |
| Cale Makar: 1+ points | 0.579 | 0.695 | 71/32 | +0.086 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.536 | 0.640 | 66/38 | +0.067 | STANDARD |
| Cale Makar: 2+ points | 0.209 | 0.310 | 32/70 | +0.077 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.176 | 0.275 | 31/76 | +0.051 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
