# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T18:01:26Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 6 · markets on board: 4150 · contracts joined: 1430 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1280, 'NO_EDGE': 50, 'OK': 100}
families: {'period_winner': 54, 'period_spread': 36, 'period_total': 54, 'player_assists': 226, 'game_early_goal': 6, 'first_goal': 214, 'game_winner': 12, 'player_goals': 371, 'game_overtime': 6, 'player_points': 308, 'game_spread': 24, 'team_total': 60, 'game_total': 54, 'goalie_saves': 5}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ LAK | 2026-10-31T20:00:00Z | T-90m | 0.485 | 0.515 | 0.181 | 6.24 | 3.07 | 3.17 | 262 (25/237) | PROJECTED/PROJECTED |
| OTT @ SJS | 2026-10-31T20:00:00Z | T-90m | 0.546 | 0.454 | 0.171 | 6.62 | 3.45 | 3.16 | 224 (25/199) | CONFIRMED/PROJECTED |
| PIT @ MTL | 2026-10-31T23:00:00Z | T-3h | 0.628 | 0.372 | 0.167 | 6.44 | 3.63 | 2.82 | 257 (25/232) | CONFIRMED/CONFIRMED |
| TOR @ VAN | 2026-10-31T23:00:00Z | T-3h | 0.448 | 0.552 | 0.160 | 7.23 | 3.45 | 3.79 | 225 (25/200) | PROJECTED/CONFIRMED |
| CBJ @ DAL | 2026-11-01T00:00:00Z | T-3h | 0.584 | 0.416 | 0.185 | 5.49 | 2.99 | 2.50 | 232 (25/207) | CONFIRMED/CONFIRMED |
| CGY @ COL | 2026-11-01T02:00:00Z | T-6h | 0.716 | 0.284 | 0.150 | 6.47 | 3.95 | 2.52 | 230 (25/205) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT31OTTSJ-OTT | game_winner | 0.454 | 0.585 | 0.559 | 59 | 42 | no | +0.109 | OK |
| KXNHLGAME-26OCT31OTTSJ-SJ | game_winner | 0.546 | 0.415 | 0.441 | 42 | 59 | yes | +0.109 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.355 | 0.475 | 0.450 | 48 | 53 | no | +0.098 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ2 | game_spread | 0.334 | 0.235 | 0.253 | 24 | 77 | yes | +0.082 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.502 | 0.605 | 0.585 | 61 | 40 | no | +0.081 | OK |
| KXNHLGAME-26OCT31PITMTL-MTL | game_winner | 0.628 | 0.525 | 0.546 | 53 | 48 | yes | +0.081 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT2 | game_spread | 0.255 | 0.355 | 0.333 | 36 | 65 | no | +0.079 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4 | team_total | 0.461 | 0.360 | 0.379 | 37 | 65 | yes | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.573 | 0.670 | 0.651 | 68 | 34 | no | +0.071 | OK |
| KXNHLGAME-26OCT31PITMTL-PIT | game_winner | 0.372 | 0.465 | 0.446 | 47 | 54 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN5 | team_total | 0.271 | 0.180 | 0.196 | 19 | 83 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3 | team_total | 0.667 | 0.570 | 0.590 | 58 | 44 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ3 | team_total | 0.676 | 0.585 | 0.604 | 59 | 42 | yes | +0.069 | OK |
| KXNHLTOTAL-26OCT31TORVAN-8 | game_total | 0.411 | 0.320 | 0.337 | 33 | 69 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT31TORVAN-9 | game_total | 0.318 | 0.235 | 0.250 | 24 | 77 | yes | +0.065 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-OTT3 | game_spread | 0.154 | 0.240 | 0.220 | 25 | 77 | no | +0.064 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.716 | 0.795 | 0.781 | 80 | 21 | no | +0.062 | OK |
| KXNHLGAME-26OCT31TORVAN-TOR | game_winner | 0.552 | 0.635 | 0.619 | 64 | 37 | no | +0.061 | OK |
| KXNHLGAME-26OCT31TORVAN-VAN | game_winner | 0.448 | 0.365 | 0.381 | 37 | 64 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ5 | team_total | 0.272 | 0.190 | 0.205 | 20 | 82 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT4 | team_total | 0.323 | 0.405 | 0.388 | 41 | 60 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL2 | game_spread | 0.405 | 0.325 | 0.340 | 33 | 68 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.365 | 0.455 | 0.437 | 47 | 56 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT3 | team_total | 0.537 | 0.615 | 0.600 | 62 | 39 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ4 | team_total | 0.463 | 0.380 | 0.396 | 39 | 63 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN6 | team_total | 0.141 | 0.070 | 0.081 | 8 | 94 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT4 | team_total | 0.398 | 0.475 | 0.459 | 48 | 53 | no | +0.054 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.284 | 0.215 | 0.228 | 22 | 79 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT31TORVAN-7 | game_total | 0.609 | 0.535 | 0.550 | 54 | 47 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.675 | 0.745 | 0.732 | 75 | 26 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT3 | team_total | 0.614 | 0.690 | 0.675 | 70 | 32 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.363 | 0.435 | 0.420 | 44 | 57 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT31OTTSJ-SJ3 | game_spread | 0.208 | 0.145 | 0.156 | 15 | 86 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR3 | game_spread | 0.227 | 0.295 | 0.281 | 30 | 71 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN2 | game_spread | 0.260 | 0.195 | 0.207 | 20 | 81 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT2 | game_spread | 0.190 | 0.255 | 0.241 | 26 | 75 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT3 | game_spread | 0.105 | 0.165 | 0.151 | 17 | 84 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.701 | 0.635 | 0.649 | 64 | 37 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.459 | 0.390 | 0.404 | 40 | 62 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.206 | 0.265 | 0.252 | 27 | 74 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN2 | team_total | 0.851 | 0.790 | 0.803 | 80 | 22 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT31TORVAN-10 | game_total | 0.176 | 0.120 | 0.130 | 13 | 89 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL3 | team_total | 0.586 | 0.650 | 0.638 | 66 | 36 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.259 | 0.200 | 0.211 | 21 | 81 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT5 | team_total | 0.161 | 0.220 | 0.207 | 23 | 79 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT2 | team_total | 0.762 | 0.820 | 0.809 | 83 | 19 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.200 | 0.260 | 0.247 | 27 | 75 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT31TORVAN-6 | game_total | 0.712 | 0.650 | 0.663 | 66 | 36 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR2 | game_spread | 0.348 | 0.405 | 0.393 | 41 | 60 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT2 | team_total | 0.817 | 0.865 | 0.856 | 87 | 14 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL2 | game_spread | 0.341 | 0.395 | 0.384 | 40 | 61 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ6 | team_total | 0.137 | 0.080 | 0.089 | 10 | 94 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-SJ2 | team_total | 0.851 | 0.800 | 0.811 | 81 | 21 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL2 | team_total | 0.800 | 0.845 | 0.837 | 85 | 16 | no | +0.030 | OK |
| KXNHLGAME-26OCT31CBJDAL-CBJ | game_winner | 0.416 | 0.365 | 0.375 | 37 | 64 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL5 | team_total | 0.179 | 0.235 | 0.223 | 25 | 78 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.771 | 0.825 | 0.815 | 84 | 19 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT31OTTSJ-OTT5 | team_total | 0.221 | 0.275 | 0.264 | 29 | 74 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5 | team_total | 0.120 | 0.080 | 0.087 | 9 | 93 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-6 | game_total | 0.438 | 0.485 | 0.476 | 49 | 52 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.130 | 0.095 | 0.101 | 10 | 91 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL3 | game_spread | 0.266 | 0.220 | 0.229 | 23 | 79 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-7 | game_total | 0.330 | 0.375 | 0.366 | 38 | 63 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN3 | game_spread | 0.161 | 0.125 | 0.132 | 13 | 88 | yes | +0.023 | OK |
| KXNHLGAME-26OCT31CBJDAL-DAL | game_winner | 0.584 | 0.625 | 0.617 | 63 | 38 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-4 | game_total | 0.780 | 0.820 | 0.812 | 83 | 19 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL4 | team_total | 0.505 | 0.465 | 0.473 | 47 | 54 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL2 | team_total | 0.908 | 0.940 | 0.935 | 95 | 7 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-8 | game_total | 0.164 | 0.195 | 0.188 | 20 | 81 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-9 | game_total | 0.107 | 0.135 | 0.129 | 14 | 87 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT31PITMTL-8 | game_total | 0.291 | 0.325 | 0.318 | 33 | 68 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT31PITMTL-7 | game_total | 0.490 | 0.525 | 0.518 | 53 | 48 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT31TORVAN-5 | game_total | 0.870 | 0.840 | 0.847 | 85 | 17 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT31BUFLA-LA5 | team_total | 0.202 | 0.175 | 0.180 | 18 | 83 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-3 | game_total | 0.936 | 0.960 | 0.956 | 97 | 5 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT31PITMTL-5 | game_total | 0.800 | 0.830 | 0.824 | 84 | 18 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT31BUFLA-BUF3 | game_spread | 0.180 | 0.205 | 0.200 | 21 | 80 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT31PITMTL-6 | game_total | 0.605 | 0.635 | 0.629 | 64 | 37 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL6 | team_total | 0.075 | 0.100 | 0.095 | 11 | 91 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT31BUFLA-BUF2 | game_spread | 0.296 | 0.325 | 0.319 | 33 | 68 | no | +0.009 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ LAK | 0.485 | 0.542 | 0.181 | 0.223 | 6.24 | 6.19 | 0.993/0.998 | KXNHLGAME-26OCT31BUFLA-BUF -0.057 |
| OTT @ SJS | 0.546 | 0.507 | 0.171 | 0.216 | 6.62 | 6.46 | 1.022/1.051 | KXNHLSPREAD-26OCT31OTTSJ-SJ2 -0.044 |
| PIT @ MTL | 0.628 | 0.520 | 0.167 | 0.213 | 6.44 | 6.62 | 0.983/1.012 | KXNHLGAME-26OCT31PITMTL-MTL -0.109 |
| TOR @ VAN | 0.448 | 0.502 | 0.160 | 0.211 | 7.23 | 6.67 | 1.021/0.956 | KXNHLTEAMTOTAL-26OCT31TORVAN-TOR4 -0.096 |
| CBJ @ DAL | 0.584 | 0.534 | 0.185 | 0.224 | 5.49 | 5.92 | 0.995/0.947 | KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3 +0.090 |
| CGY @ COL | 0.716 | 0.701 | 0.150 | 0.189 | 6.47 | 6.58 | 0.979/0.998 | KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 +0.034 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 24 recommended · full analysis in card.md / packet.json `thesis_card`

- Andre Lee: 1+ goals YES @ 9c · p 0.1247 (adj 0.1148) · $3.07 · thesis LAK:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0799 (adj 0.0674) · $1.98 · thesis LAK:WINS_BY_2PLUS
- Buffalo wins by over 1.5 goals NO @ 68c · p 0.7646 (adj 0.7198) · $12.37 · thesis LAK:WINS
- Buffalo wins by over 2.5 goals NO @ 80c · p 0.8589 (adj 0.8269) · $1.02 · thesis LAK:WINS
- Tyler Toffoli: 1+ assists YES @ 24c · p 0.329 (adj 0.282) · $5.65 · thesis SJS:OFFENSE_4PLUS
- Claude Giroux: 1+ goals YES @ 18c · p 0.2245 (adj 0.2121) · $4.85 · thesis OTT:OFFENSE_4PLUS
- Ottawa wins by over 1.5 goals NO @ 65c · p 0.7131 (adj 0.679) · $8.16 · thesis SJS:WINS
- Ivar Stenberg: 1+ goals NO @ 79c · p 0.8212 (adj 0.8122) · $11.22 · thesis SJS:SUPPRESSED
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1208 (adj 0.1119) · $2.83 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1592 (adj 0.1494) · $2.05 · thesis PIT:OFFENSE_4PLUS
- Zachary Bolduc: 1+ assists YES @ 24c · p 0.3028 (adj 0.2664) · $3.01 · thesis MTL:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 30c · p 0.3369 (adj 0.3264) · $2.81 · thesis PIT:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2694 (adj 0.2483) · $8.86 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 18c · p 0.2467 (adj 0.2288) · $7.21 · thesis VAN:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 71c · p 0.7837 (adj 0.764) · $13.44 · thesis TOR:SUPPRESSED
- Liam Ohgren: 1+ goals YES @ 16c · p 0.2113 (adj 0.1947) · $4.42 · thesis VAN:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1869 (adj 0.1689) · $5.48 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 19c · p 0.2535 (adj 0.2339) · $6.55 · thesis CBJ:OFFENSE_4PLUS
- Ryan Lomberg: 1+ goals YES @ 5c · p 0.0771 (adj 0.0678) · $2.17 · thesis CBJ:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7373 (adj 0.7205) · $13.66 · thesis DAL:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 7c · p 0.1099 (adj 0.0987) · $3.67 · thesis CGY:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 74c · p 0.7988 (adj 0.7828) · $13.66 · thesis COL:SUPPRESSED
- Calgary over 1.5 goals scored YES @ 64c · p 0.7293 (adj 0.6822) · $8.93 · thesis CGY:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 15c · p 0.1928 (adj 0.1771) · $2.9 · thesis CGY:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ LAK** · priced 210/211 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.66, exp saves 24.15 (sd 6.48), pull risk 0.054
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 28.05, exp saves 24.03 (sd 6.55), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ points | 0.291 | 0.095 | 17/98 | +0.111 | STANDARD |
| Mikey Anderson: 1+ points | 0.276 | 0.100 | 18/98 | +0.085 | STANDARD |
| Brian Dumoulin: 1+ points | 0.270 | 0.095 | 17/98 | +0.091 | STANDARD |
| Joel Edmundson: 1+ assists | 0.227 | 0.075 | 13/98 | +0.089 | STANDARD |
| Beck Malenstyn: 1+ points | 0.217 | 0.090 | 16/98 | +0.047 | STANDARD |
| Mikey Anderson: 1+ assists | 0.233 | 0.125 | 15/90 | +0.074 | STANDARD |

**OTT @ SJS** · priced 170/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 28.35, exp saves 24.3 (sd 6.74), pull risk 0.067
- OTT net: Samuel Ersson (PROJECTED) exp shots 25.93, exp saves 22.41 (sd 6.32), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 2+ points | 0.291 | 0.395 | 40/61 | +0.082 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.444 | 0.545 | 56/47 | +0.069 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.329 | 0.235 | 24/77 | +0.076 | STANDARD |
| Collin Graf: 1+ points | 0.422 | 0.335 | 36/69 | +0.046 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.111 | 0.190 | 21/83 | +0.049 | STANDARD |
| Tyler Toffoli: 1+ points | 0.472 | 0.395 | 41/62 | +0.046 | STANDARD |

**PIT @ MTL** · priced 203/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.16, exp saves 24.42 (sd 6.68), pull risk 0.067
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.26, exp saves 22.49 (sd 6.49), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sergei Murashov: 27+ saves | 0.259 | 0.385 | 41/64 | +0.084 |  |
| Spencer Stastney: 1+ points | 0.217 | 0.120 | 22/98 | -0.015 | STANDARD |
| Samuel Girard: 1+ assists | 0.231 | 0.135 | 25/98 | -0.032 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.303 | 0.230 | 24/78 | +0.050 | STANDARD |
| Spencer Stastney: 1+ assists | 0.181 | 0.110 | 20/98 | -0.030 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.277 | 0.215 | 23/80 | +0.034 | STANDARD |

**TOR @ VAN** · priced 160/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.88, exp saves 24.85 (sd 6.73), pull risk 0.069
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 28.15, exp saves 24.18 (sd 6.78), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.406 | 0.530 | 54/48 | +0.096 | STANDARD |
| Linus Karlsson: 1+ points | 0.494 | 0.370 | 39/65 | +0.087 | STANDARD |
| Auston Matthews: 2+ points | 0.289 | 0.410 | 42/60 | +0.094 | STANDARD |
| William Nylander: 1+ assists | 0.411 | 0.530 | 54/48 | +0.091 | STANDARD |
| Gavin McKenna: 1+ points | 0.460 | 0.565 | 58/45 | +0.073 | STANDARD |
| Anthony Stolarz: 25+ saves | 0.480 | 0.375 | 44/69 | +0.022 |  |

**CBJ @ DAL** · priced 180/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.99, exp saves 21.79 (sd 6.04), pull risk 0.05
- CBJ net: Jet Greaves (CONFIRMED) exp shots 26.69, exp saves 23.11 (sd 6.39), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Denton Mateychuk: 1+ points | 0.323 | 0.185 | 35/98 | -0.043 | STANDARD |
| Cole Sillinger: 1+ points | 0.354 | 0.245 | 27/78 | +0.070 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.213 | 0.305 | 32/71 | +0.062 | STANDARD |
| Charlie Coyle: 1+ points | 0.526 | 0.440 | 46/58 | +0.049 | STANDARD |
| Mathieu Olivier: 1+ points | 0.346 | 0.260 | 29/77 | +0.042 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.436 | 0.520 | 54/50 | +0.046 | STANDARD |

**CGY @ COL** · priced 175/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.33, exp saves 23.33 (sd 6.32), pull risk 0.042
- CGY net: Dustin Wolf (PROJECTED) exp shots 33.08, exp saves 27.66 (sd 7.79), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mackenzie Blackwood: 22+ saves | 0.610 | 0.320 | 50/86 | +0.092 |  |
| Nathan MacKinnon: 2+ points | 0.408 | 0.525 | 53/48 | +0.095 | STANDARD |
| Cale Makar: 1+ assists | 0.480 | 0.590 | 61/43 | +0.072 | STANDARD |
| Cale Makar: 1+ points | 0.587 | 0.690 | 71/33 | +0.068 | STANDARD |
| Cale Makar: 2+ points | 0.226 | 0.320 | 33/69 | +0.069 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.540 | 0.630 | 65/39 | +0.054 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
