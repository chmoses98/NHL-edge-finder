# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T22:59:54Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 4 · markets on board: 3036 · contracts joined: 940 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 840, 'OK': 80, 'NO_EDGE': 20}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 143, 'game_early_goal': 4, 'first_goal': 140, 'game_winner': 8, 'player_goals': 249, 'game_overtime': 4, 'player_points': 197, 'goalie_saves': 7, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ MTL | 2026-10-31T23:00:00Z | T-<10m | 0.628 | 0.372 | 0.172 | 6.44 | 3.63 | 2.81 | 251 (25/226) | CONFIRMED/CONFIRMED |
| TOR @ VAN | 2026-10-31T23:00:00Z | T-<10m | 0.437 | 0.563 | 0.155 | 7.32 | 3.45 | 3.87 | 225 (25/200) | CONFIRMED/CONFIRMED |
| CBJ @ DAL | 2026-11-01T00:00:00Z | T-60m | 0.584 | 0.416 | 0.180 | 5.48 | 2.98 | 2.50 | 234 (25/209) | CONFIRMED/CONFIRMED |
| CGY @ COL | 2026-11-01T02:00:00Z | T-3h | 0.681 | 0.319 | 0.164 | 6.21 | 3.68 | 2.53 | 230 (25/205) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.308 | 0.465 | 0.432 | 47 | 54 | no | +0.134 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.454 | 0.605 | 0.575 | 61 | 40 | no | +0.129 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.515 | 0.660 | 0.632 | 67 | 35 | no | +0.119 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.312 | 0.440 | 0.413 | 45 | 57 | no | +0.101 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.319 | 0.215 | 0.234 | 22 | 79 | yes | +0.086 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.681 | 0.785 | 0.766 | 79 | 22 | no | +0.086 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4 | team_total | 0.460 | 0.355 | 0.375 | 36 | 65 | yes | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3 | team_total | 0.663 | 0.560 | 0.581 | 57 | 45 | yes | +0.076 | OK |
| KXNHLTOTAL-26OCT31TORVAN-9 | game_total | 0.327 | 0.235 | 0.252 | 24 | 77 | yes | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN5 | team_total | 0.273 | 0.180 | 0.196 | 19 | 83 | yes | +0.072 | OK |
| KXNHLGAME-26OCT31PITMTL-PIT | game_winner | 0.372 | 0.465 | 0.446 | 47 | 54 | no | +0.071 | OK |
| KXNHLGAME-26OCT31PITMTL-MTL | game_winner | 0.628 | 0.535 | 0.554 | 54 | 47 | yes | +0.071 | OK |
| KXNHLTOTAL-26OCT31TORVAN-8 | game_total | 0.426 | 0.330 | 0.348 | 34 | 68 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.729 | 0.825 | 0.808 | 84 | 19 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT3 | team_total | 0.534 | 0.625 | 0.607 | 63 | 38 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.160 | 0.250 | 0.230 | 26 | 76 | no | +0.067 | OK |
| KXNHLGAME-26OCT31TORVAN-VAN | game_winner | 0.437 | 0.355 | 0.371 | 36 | 65 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT4 | team_total | 0.322 | 0.410 | 0.392 | 42 | 60 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL2 | game_spread | 0.402 | 0.325 | 0.340 | 33 | 68 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT31TORVAN-10 | game_total | 0.183 | 0.115 | 0.127 | 12 | 89 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.360 | 0.435 | 0.420 | 44 | 57 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.205 | 0.275 | 0.260 | 28 | 73 | no | +0.051 | OK |
| KXNHLGAME-26OCT31TORVAN-TOR | game_winner | 0.563 | 0.635 | 0.621 | 64 | 37 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT2 | game_spread | 0.187 | 0.255 | 0.240 | 26 | 75 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.677 | 0.745 | 0.732 | 75 | 26 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT31PITMTL-PIT3 | game_spread | 0.101 | 0.165 | 0.150 | 17 | 84 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-6 | game_total | 0.564 | 0.635 | 0.621 | 64 | 37 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT31TORVAN-7 | game_total | 0.617 | 0.545 | 0.560 | 55 | 46 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.260 | 0.195 | 0.207 | 20 | 81 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL3 | team_total | 0.585 | 0.660 | 0.645 | 67 | 35 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT31TORVAN-6 | game_total | 0.724 | 0.655 | 0.670 | 66 | 35 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN2 | team_total | 0.850 | 0.785 | 0.799 | 79 | 22 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.465 | 0.395 | 0.409 | 40 | 61 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-VAN6 | team_total | 0.141 | 0.075 | 0.085 | 9 | 94 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN2 | game_spread | 0.256 | 0.195 | 0.206 | 20 | 81 | yes | +0.044 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.149 | 0.095 | 0.104 | 10 | 91 | yes | +0.043 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR2 | game_spread | 0.362 | 0.425 | 0.412 | 43 | 58 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL2 | team_total | 0.886 | 0.940 | 0.932 | 95 | 7 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT31TORVAN-TOR3 | game_spread | 0.239 | 0.295 | 0.283 | 30 | 71 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT5 | team_total | 0.162 | 0.225 | 0.211 | 24 | 79 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL5 | team_total | 0.181 | 0.240 | 0.227 | 25 | 77 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-PIT2 | team_total | 0.764 | 0.825 | 0.814 | 84 | 19 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL2 | team_total | 0.798 | 0.845 | 0.836 | 85 | 16 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL2 | game_spread | 0.342 | 0.395 | 0.384 | 40 | 61 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT31PITMTL-MTL3 | game_spread | 0.264 | 0.215 | 0.224 | 22 | 79 | yes | +0.032 | OK |
| KXNHLGAME-26OCT31CBJDAL-CBJ | game_winner | 0.416 | 0.365 | 0.375 | 37 | 64 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-4 | game_total | 0.781 | 0.825 | 0.817 | 83 | 18 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.703 | 0.650 | 0.661 | 66 | 36 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-7 | game_total | 0.446 | 0.495 | 0.485 | 50 | 51 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-8 | game_total | 0.259 | 0.305 | 0.295 | 31 | 70 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-5 | game_total | 0.773 | 0.825 | 0.815 | 84 | 19 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-8 | game_total | 0.163 | 0.205 | 0.196 | 21 | 80 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-7 | game_total | 0.329 | 0.375 | 0.366 | 38 | 63 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-6 | game_total | 0.438 | 0.485 | 0.476 | 49 | 52 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-4 | game_total | 0.859 | 0.900 | 0.893 | 91 | 11 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5 | team_total | 0.120 | 0.080 | 0.087 | 9 | 93 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT31TORVAN-5 | game_total | 0.879 | 0.845 | 0.852 | 85 | 16 | yes | +0.020 | OK |
| KXNHLGAME-26OCT31CBJDAL-DAL | game_winner | 0.584 | 0.625 | 0.617 | 63 | 38 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-9 | game_total | 0.103 | 0.135 | 0.128 | 14 | 87 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL3 | team_total | 0.714 | 0.670 | 0.679 | 68 | 34 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT31PITMTL-5 | game_total | 0.802 | 0.835 | 0.829 | 84 | 17 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT31TORVAN-VAN3 | game_spread | 0.156 | 0.125 | 0.131 | 13 | 88 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL4 | team_total | 0.505 | 0.465 | 0.473 | 47 | 54 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL6 | team_total | 0.152 | 0.120 | 0.126 | 13 | 89 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT31PITMTL-6 | game_total | 0.601 | 0.635 | 0.628 | 64 | 37 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY3 | game_spread | 0.076 | 0.050 | 0.054 | 6 | 96 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT31PITMTL-8 | game_total | 0.293 | 0.325 | 0.318 | 33 | 68 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL6 | team_total | 0.074 | 0.100 | 0.094 | 11 | 91 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-3 | game_total | 0.938 | 0.955 | 0.952 | 96 | 5 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-10 | game_total | 0.085 | 0.105 | 0.101 | 11 | 90 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT31PITMTL-4 | game_total | 0.876 | 0.900 | 0.896 | 91 | 11 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-9 | game_total | 0.182 | 0.210 | 0.204 | 22 | 80 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT31PITMTL-7 | game_total | 0.486 | 0.515 | 0.509 | 52 | 49 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT31TORVAN-TOR6 | team_total | 0.197 | 0.170 | 0.175 | 18 | 84 | yes | +0.006 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-CBJ2 | game_spread | 0.206 | 0.185 | 0.189 | 19 | 82 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-10 | game_total | 0.041 | 0.055 | 0.052 | 6 | 95 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT31TORVAN-2 | game_total | 0.994 | 0.985 | 0.987 | 99 | 2 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT31TORVAN-4 | game_total | 0.928 | 0.915 | 0.918 | 92 | 9 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY6 | team_total | 0.045 | 0.025 | 0.028 | 4 | 99 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT31PITMTL-MTL2 | team_total | 0.880 | 0.865 | 0.868 | 87 | 14 | yes | +0.002 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ MTL | 0.628 | 0.520 | 0.172 | 0.213 | 6.44 | 6.62 | 0.983/1.012 | KXNHLGAME-26OCT31PITMTL-MTL -0.109 |
| TOR @ VAN | 0.437 | 0.492 | 0.155 | 0.212 | 7.32 | 6.71 | 1.035/0.956 | KXNHLTEAMTOTAL-26OCT31TORVAN-TOR5 -0.103 |
| CBJ @ DAL | 0.584 | 0.534 | 0.180 | 0.224 | 5.48 | 5.92 | 0.995/0.947 | KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3 +0.089 |
| CGY @ COL | 0.681 | 0.694 | 0.164 | 0.189 | 6.21 | 6.54 | 0.979/0.992 | KXNHLTOTAL-26OCT31CGYCOL-7 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Connor Dewar: 1+ goals YES @ 12c · p 0.1592 (adj 0.1482) · $5.38 · thesis PIT:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1208 (adj 0.1119) · $4.07 · thesis PIT:OFFENSE_4PLUS
- Phillip Danault: 1+ goals YES @ 13c · p 0.1671 (adj 0.1528) · $4.05 · thesis MTL:OFFENSE_4PLUS
- Jake Evans: 1+ goals YES @ 13c · p 0.1623 (adj 0.148) · $2.65 · thesis MTL:WINS_BY_2PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2579 (adj 0.2397) · $10.13 · thesis VAN:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 73c · p 0.7926 (adj 0.7757) · $17.58 · thesis TOR:SUPPRESSED
- Auston Matthews: 1+ goals NO @ 53c · p 0.5944 (adj 0.5758) · $11.91 · thesis TOR:SUPPRESSED
- Toronto wins by over 1.5 goals NO @ 58c · p 0.7082 (adj 0.6216) · $7.23 · thesis VAN:WINS
- Damon Severson: 1+ goals YES @ 6c · p 0.1066 (adj 0.0937) · $6.76 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1869 (adj 0.1714) · $8.72 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 19c · p 0.2535 (adj 0.2364) · $10.56 · thesis CBJ:OFFENSE_4PLUS
- Valeri Nichushkin: 1+ assists NO @ 71c · p 0.7868 (adj 0.7459) · $19.66 · thesis CBJ:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 7c · p 0.1124 (adj 0.1006) · $5.5 · thesis CGY:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 73c · p 0.803 (adj 0.7835) · $19.66 · thesis COL:SUPPRESSED
- Calgary over 3.5 goals scored YES @ 20c · p 0.2829 (adj 0.2389) · $6.19 · thesis CGY:OFFENSE_4PLUS
- Mackenzie Blackwood: 22+ saves YES @ 53c · p 0.6077 (adj 0.5614) · $9.94 · thesis COL:NET_HIGH_VOLUME

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ MTL** · priced 197/200 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.16, exp saves 24.42 (sd 6.68), pull risk 0.067
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.26, exp saves 22.49 (sd 6.49), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sergei Murashov: 27+ saves | 0.259 | 0.380 | 41/65 | +0.075 |  |
| Spencer Stastney: 1+ points | 0.217 | 0.120 | 22/98 | -0.015 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.277 | 0.210 | 23/81 | +0.034 | STANDARD |
| Josh Anderson: 1+ assists | 0.216 | 0.155 | 17/86 | +0.036 | STANDARD |
| Juraj Slafkovský: 2+ points | 0.225 | 0.165 | 21/88 | +0.003 | STANDARD |
| Alex Newhook: 1+ assists | 0.345 | 0.285 | 29/72 | +0.040 | STANDARD |

**TOR @ VAN** · priced 162/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 28.88, exp saves 24.73 (sd 6.82), pull risk 0.074
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 28.15, exp saves 24.22 (sd 6.71), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 2+ points | 0.280 | 0.415 | 43/60 | +0.103 | STANDARD |
| Gavin McKenna: 1+ points | 0.439 | 0.570 | 59/45 | +0.094 | STANDARD |
| Gavin McKenna: 1+ assists | 0.295 | 0.425 | 44/59 | +0.098 | STANDARD |
| William Nylander: 1+ assists | 0.402 | 0.525 | 54/49 | +0.091 | STANDARD |
| Marco Rossi: 1+ goals | 0.242 | 0.120 | 18/94 | +0.052 | STANDARD |
| Linus Karlsson: 1+ points | 0.489 | 0.370 | 39/65 | +0.082 | STANDARD |

**CBJ @ DAL** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.99, exp saves 21.79 (sd 6.04), pull risk 0.05
- CBJ net: Jet Greaves (CONFIRMED) exp shots 26.69, exp saves 23.11 (sd 6.39), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Sillinger: 1+ points | 0.354 | 0.255 | 27/76 | +0.070 | STANDARD |
| Jet Greaves: 26+ saves | 0.341 | 0.435 | 44/57 | +0.072 |  |
| Miro Heiskanen: 1+ points | 0.447 | 0.535 | 54/47 | +0.066 | STANDARD |
| Mikko Rantanen: 2+ points | 0.218 | 0.305 | 33/72 | +0.048 | STANDARD |
| Jason Robertson: 2+ points | 0.245 | 0.330 | 35/69 | +0.050 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.436 | 0.520 | 53/49 | +0.056 | STANDARD |

**CGY @ COL** · priced 178/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.33, exp saves 23.3 (sd 6.25), pull risk 0.043
- CGY net: Arsenii Sergeev (CONFIRMED) exp shots 33.08, exp saves 27.7 (sd 7.76), pull risk 0.103

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 2+ points | 0.209 | 0.335 | 34/67 | +0.106 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.399 | 0.525 | 53/48 | +0.104 | STANDARD |
| Cale Makar: 1+ assists | 0.474 | 0.600 | 61/41 | +0.099 | STANDARD |
| Cale Makar: 1+ points | 0.579 | 0.690 | 70/32 | +0.086 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.536 | 0.640 | 65/37 | +0.077 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.156 | 0.255 | 27/76 | +0.071 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
