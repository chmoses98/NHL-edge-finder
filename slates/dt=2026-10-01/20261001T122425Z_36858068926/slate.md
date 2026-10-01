# NHL slate 2026-10-01 — RESEARCH_ONLY

generated 2026-10-01T12:24:25Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 8 · simulated (not started): 8 · markets on board: 2913 · contracts joined: 897 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 697, 'NO_EDGE': 83, 'OK': 117}
families: {'period_winner': 72, 'period_spread': 48, 'period_total': 72, 'player_assists': 96, 'game_early_goal': 8, 'first_goal': 134, 'game_winner': 16, 'player_goals': 134, 'game_overtime': 8, 'player_points': 125, 'game_spread': 32, 'team_total': 80, 'game_total': 72}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 2026-10-01T23:00:00Z | T-6h | 0.589 | 0.411 | 0.182 | 5.64 | 3.09 | 2.56 | 160 (25/135) | PROJECTED/PROJECTED |
| TBL @ NYR | 2026-10-01T23:00:00Z | T-6h | 0.503 | 0.497 | 0.191 | 5.72 | 2.87 | 2.85 | 176 (25/151) | PROJECTED/PROJECTED |
| BUF @ CBJ | 2026-10-01T23:00:00Z | T-6h | 0.514 | 0.485 | 0.183 | 5.95 | 3.02 | 2.93 | 182 (25/157) | PROJECTED/PROBABLE |
| MIN @ NSH | 2026-10-02T00:00:00Z | T-6h | 0.471 | 0.529 | 0.170 | 6.51 | 3.16 | 3.36 | 175 (25/150) | PROJECTED/PROJECTED |
| SEA @ CGY | 2026-10-02T01:00:00Z | T-12h | 0.525 | 0.474 | 0.181 | 6.10 | 3.13 | 2.97 | 51 (25/26) | CONFIRMED/PROJECTED |
| CHI @ UTA | 2026-10-02T01:30:00Z | T-12h | 0.625 | 0.374 | 0.168 | 6.14 | 3.47 | 2.67 | 51 (25/26) | PROJECTED/PROJECTED |
| EDM @ VAN | 2026-10-02T02:00:00Z | T-12h | 0.424 | 0.576 | 0.171 | 6.65 | 3.08 | 3.57 | 51 (25/26) | PROJECTED/PROJECTED |
| FLA @ SJS | 2026-10-02T02:00:00Z | T-12h | 0.530 | 0.470 | 0.166 | 6.52 | 3.35 | 3.16 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT01EDMVAN-EDM2 | game_spread | 0.358 | 0.455 | 0.435 | 46 | 55 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3 | game_spread | 0.231 | 0.325 | 0.305 | 33 | 68 | no | +0.074 | OK |
| KXNHLGAME-26OCT01FLASJ-SJ | game_winner | 0.530 | 0.435 | 0.454 | 44 | 57 | yes | +0.073 | OK |
| KXNHLGAME-26OCT01FLASJ-FLA | game_winner | 0.470 | 0.565 | 0.546 | 57 | 44 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA2 | game_spread | 0.266 | 0.355 | 0.336 | 36 | 65 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA3 | game_spread | 0.159 | 0.245 | 0.226 | 25 | 76 | no | +0.068 | OK |
| KXNHLGAME-26OCT01EDMVAN-EDM | game_winner | 0.576 | 0.665 | 0.648 | 67 | 34 | no | +0.068 | OK |
| KXNHLGAME-26OCT01EDMVAN-VAN | game_winner | 0.424 | 0.335 | 0.352 | 34 | 67 | yes | +0.068 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ2 | game_spread | 0.315 | 0.235 | 0.250 | 24 | 77 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB4 | team_total | 0.331 | 0.425 | 0.406 | 44 | 59 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB3 | team_total | 0.553 | 0.640 | 0.623 | 65 | 37 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB2 | game_spread | 0.268 | 0.345 | 0.329 | 35 | 66 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT01PHINJ-6 | game_total | 0.467 | 0.545 | 0.529 | 55 | 46 | no | +0.056 | OK |
| KXNHLGAME-26OCT01TBNYR-NYR | game_winner | 0.503 | 0.425 | 0.440 | 43 | 58 | yes | +0.056 | OK |
| KXNHLGAME-26OCT01TBNYR-TB | game_winner | 0.497 | 0.575 | 0.560 | 58 | 43 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ4 | team_total | 0.438 | 0.360 | 0.375 | 37 | 65 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3 | team_total | 0.657 | 0.575 | 0.592 | 59 | 44 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT01PHINJ-7 | game_total | 0.356 | 0.425 | 0.411 | 43 | 58 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB5 | team_total | 0.162 | 0.230 | 0.215 | 24 | 78 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT01TBNYR-4 | game_total | 0.808 | 0.865 | 0.855 | 87 | 14 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT01TBNYR-6 | game_total | 0.479 | 0.545 | 0.532 | 55 | 46 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT01TBNYR-7 | game_total | 0.370 | 0.435 | 0.422 | 44 | 57 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB3 | game_spread | 0.157 | 0.215 | 0.202 | 22 | 79 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT01PHINJ-NJ4 | team_total | 0.382 | 0.445 | 0.432 | 45 | 56 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT01PHINJ-5 | game_total | 0.698 | 0.755 | 0.744 | 76 | 25 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN2 | game_spread | 0.229 | 0.175 | 0.185 | 18 | 83 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ3 | game_spread | 0.197 | 0.145 | 0.154 | 15 | 86 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN3 | team_total | 0.595 | 0.525 | 0.539 | 54 | 49 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT01TBNYR-5 | game_total | 0.711 | 0.770 | 0.759 | 78 | 24 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT01TBNYR-8 | game_total | 0.193 | 0.245 | 0.234 | 25 | 76 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT01PHINJ-4 | game_total | 0.796 | 0.850 | 0.840 | 86 | 16 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ5 | team_total | 0.255 | 0.195 | 0.206 | 21 | 82 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT01MINNSH-8 | game_total | 0.307 | 0.250 | 0.261 | 26 | 76 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT01TBNYR-NYR2 | game_spread | 0.274 | 0.225 | 0.234 | 23 | 78 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT01PHINJ-8 | game_total | 0.186 | 0.235 | 0.225 | 24 | 77 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT01MINNSH-9 | game_total | 0.221 | 0.175 | 0.184 | 18 | 83 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 | team_total | 0.492 | 0.555 | 0.543 | 57 | 46 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 | team_total | 0.403 | 0.465 | 0.452 | 48 | 55 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ2 | team_total | 0.840 | 0.785 | 0.797 | 80 | 23 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH5 | team_total | 0.219 | 0.170 | 0.179 | 18 | 84 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM5 | team_total | 0.295 | 0.350 | 0.339 | 36 | 66 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH3 | team_total | 0.615 | 0.555 | 0.567 | 57 | 46 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB6 | team_total | 0.066 | 0.110 | 0.099 | 12 | 90 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB2 | team_total | 0.772 | 0.825 | 0.815 | 84 | 19 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN4 | team_total | 0.382 | 0.320 | 0.332 | 34 | 70 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA3 | game_spread | 0.259 | 0.305 | 0.295 | 31 | 70 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT01MINNSH-10 | game_total | 0.111 | 0.075 | 0.081 | 8 | 93 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN3 | game_spread | 0.132 | 0.095 | 0.102 | 10 | 91 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-5 | game_total | 0.743 | 0.785 | 0.777 | 79 | 22 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-7 | game_total | 0.408 | 0.460 | 0.449 | 47 | 55 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-6 | game_total | 0.518 | 0.565 | 0.556 | 57 | 44 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH4 | team_total | 0.400 | 0.345 | 0.356 | 36 | 67 | yes | +0.024 | OK |
| KXNHLGAME-26OCT01MINNSH-MIN | game_winner | 0.529 | 0.575 | 0.566 | 58 | 43 | no | +0.024 | OK |
| KXNHLGAME-26OCT01MINNSH-NSH | game_winner | 0.471 | 0.425 | 0.434 | 43 | 58 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT01MINNSH-6 | game_total | 0.610 | 0.560 | 0.570 | 57 | 45 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT01MINNSH-7 | game_total | 0.499 | 0.455 | 0.464 | 46 | 55 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT01TBNYR-9 | game_total | 0.131 | 0.170 | 0.162 | 18 | 84 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-4 | game_total | 0.832 | 0.865 | 0.859 | 87 | 14 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA5 | team_total | 0.218 | 0.265 | 0.255 | 28 | 75 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF4 | team_total | 0.345 | 0.390 | 0.381 | 40 | 62 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA3 | team_total | 0.616 | 0.670 | 0.659 | 69 | 35 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT01PHINJ-9 | game_total | 0.123 | 0.160 | 0.152 | 17 | 85 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM3 | team_total | 0.698 | 0.745 | 0.736 | 76 | 27 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN6 | team_total | 0.092 | 0.060 | 0.065 | 7 | 95 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT01PHINJ-NJ5 | team_total | 0.201 | 0.240 | 0.232 | 25 | 77 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF3 | team_total | 0.567 | 0.610 | 0.601 | 62 | 40 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN5 | team_total | 0.206 | 0.160 | 0.169 | 18 | 86 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ6 | team_total | 0.122 | 0.080 | 0.087 | 10 | 94 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM2 | team_total | 0.868 | 0.900 | 0.894 | 91 | 11 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-9 | game_total | 0.155 | 0.185 | 0.179 | 19 | 82 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF5 | team_total | 0.174 | 0.215 | 0.206 | 23 | 80 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT01PHINJ-3 | game_total | 0.943 | 0.965 | 0.961 | 97 | 4 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT01PHINJ-NJ3 | game_spread | 0.213 | 0.250 | 0.242 | 26 | 76 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT01MINNSH-NSH2 | game_spread | 0.267 | 0.235 | 0.241 | 24 | 77 | yes | +0.014 | OK |
| KXNHLSPREAD-26OCT01PHINJ-NJ2 | game_spread | 0.350 | 0.385 | 0.378 | 39 | 62 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA2 | team_total | 0.817 | 0.855 | 0.848 | 87 | 16 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH6 | team_total | 0.098 | 0.070 | 0.075 | 8 | 94 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-8 | game_total | 0.224 | 0.255 | 0.249 | 26 | 75 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA2 | game_spread | 0.400 | 0.435 | 0.428 | 44 | 57 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA6 | team_total | 0.100 | 0.130 | 0.124 | 14 | 88 | no | +0.012 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 0.589 | 0.563 | 0.182 | 0.226 | 5.64 | 5.81 | 0.987/0.993 | KXNHLTEAMTOTAL-26OCT01PHINJ-PHI3 +0.040 |
| TBL @ NYR | 0.503 | 0.516 | 0.191 | 0.227 | 5.72 | 6.02 | 0.958/0.957 | KXNHLTOTAL-26OCT01TBNYR-7 +0.054 |
| BUF @ CBJ | 0.514 | 0.552 | 0.183 | 0.216 | 5.95 | 6.17 | 0.964/1.000 | KXNHLTEAMTOTAL-26OCT01BUFCBJ-CBJ4 +0.058 |
| MIN @ NSH | 0.471 | 0.484 | 0.170 | 0.211 | 6.51 | 6.51 | 1.000/1.003 | KXNHLSPREAD-26OCT01MINNSH-NSH3 +0.017 |
| SEA @ CGY | 0.525 | 0.512 | 0.181 | 0.225 | 6.10 | 6.12 | 1.005/1.005 | KXNHLSPREAD-26OCT01SEACGY-CGY2 -0.016 |
| CHI @ UTA | 0.625 | 0.649 | 0.168 | 0.199 | 6.14 | 6.49 | 0.992/1.003 | KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA4 +0.068 |
| EDM @ VAN | 0.424 | 0.450 | 0.171 | 0.213 | 6.65 | 6.51 | 1.021/0.994 | KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 -0.032 |
| FLA @ SJS | 0.530 | 0.556 | 0.166 | 0.219 | 6.52 | 6.42 | 1.034/0.998 | KXNHLSPREAD-26OCT01FLASJ-FLA2 -0.030 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 15 recommended · full analysis in card.md / packet.json `thesis_card`

- Sean Couturier: 1+ goals YES @ 11c · p 0.1511 (adj 0.1371) · $5.13 · thesis PHI:OFFENSE_4PLUS
- Anthony Mantha: 1+ assists NO @ 74c · p 0.8786 (adj 0.7723) · $17.21 · thesis NJD:SUPPRESSED
- Nico Hischier: 1+ goals NO @ 69c · p 0.7362 (adj 0.7234) · $12.79 · thesis NJD:SUPPRESSED
- Noel Acciari: 1+ goals YES @ 9c · p 0.1156 (adj 0.1067) · $2.76 · thesis PHI:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 53c · p 0.7421 (adj 0.588) · $20.0 · thesis TBL:SUPPRESSED
- Tampa Bay wins NO @ 43c · p 0.5136 (adj 0.4693) · $5.7 · thesis NYR:WINS
- Tampa Bay wins by over 1.5 goals NO @ 66c · p 0.7301 (adj 0.6925) · $3.09 · thesis NYR:WINS
- Victor Hedman: 1+ assists NO @ 72c · p 0.7949 (adj 0.745) · $8.42 · thesis TBL:SUPPRESSED
- Zach Metsa: 1+ goals NO @ 93c · p 0.962 (adj 0.9503) · $20.0 · thesis DIFFUSE
- Tage Thompson: 1+ assists NO @ 59c · p 0.6663 (adj 0.6181) · $7.26 · thesis BUF:SUPPRESSED
- Full Game: Over 6.5 goals scored YES @ 44c · p 0.5008 (adj 0.4679) · $4.87 · thesis GAME:HIGH_EVENT
- Vancouver wins by over 2.5 goals YES @ 10c · p 0.1485 (adj 0.1217) · $1.23 · thesis VAN:WINS_BY_2PLUS
- Edmonton over 4.5 goals scored NO @ 66c · p 0.7328 (adj 0.6914) · $1.09 · thesis VAN:WINS
- Florida wins by over 2.5 goals NO @ 76c · p 0.8522 (adj 0.8036) · $20.0 · thesis SJS:WINS
- San Jose wins by over 1.5 goals YES @ 24c · p 0.3336 (adj 0.2843) · $6.86 · thesis SJS:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ NJD** · priced 107/109 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.74, exp saves 21.77 (sd 5.94), pull risk 0.042
- PHI net: Dan Vladar (PROJECTED) exp shots 28.45, exp saves 24.55 (sd 6.69), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anthony Mantha: 1+ assists | 0.121 | 0.285 | 31/74 | +0.125 | STANDARD |
| Anthony Mantha: 1+ points | 0.307 | 0.455 | 48/57 | +0.106 | STANDARD |
| Luke Evangelista: 1+ points | 0.343 | 0.470 | 49/55 | +0.090 | STANDARD |
| Luke Evangelista: 1+ assists | 0.202 | 0.325 | 35/70 | +0.083 | STANDARD |
| Anthony Mantha: 2+ points | 0.051 | 0.135 | 16/89 | +0.052 | STANDARD |
| Porter Martone: 1+ points | 0.378 | 0.455 | 47/56 | +0.045 | STANDARD |

**TBL @ NYR** · priced 125/125 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (PROJECTED) exp shots 28.0, exp saves 24.19 (sd 6.55), pull risk 0.055
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 24.5, exp saves 21.19 (sd 5.96), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ points | 0.649 | 0.385 | 72/95 | -0.085 | STANDARD |
| John Carlson: 1+ assists | 0.258 | 0.495 | 52/53 | +0.195 | STANDARD |
| John Carlson: 1+ points | 0.341 | 0.565 | 58/45 | +0.192 | STANDARD |
| Gabe Perreault: 1+ assists | 0.323 | 0.120 | 23/99 | +0.081 | STANDARD |
| Victor Hedman: 1+ points | 0.267 | 0.385 | 41/64 | +0.077 | STANDARD |
| Gabe Perreault: 1+ points | 0.466 | 0.350 | 38/68 | +0.069 | STANDARD |

**BUF @ CBJ** · priced 129/131 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 27.66, exp saves 24.14 (sd 6.44), pull risk 0.054
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 28.58, exp saves 24.61 (sd 6.66), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie Coyle: 1+ goals | 0.271 | 0.155 | 24/93 | +0.018 | STANDARD |
| Tage Thompson: 1+ assists | 0.334 | 0.430 | 45/59 | +0.059 | STANDARD |
| Matthew Knies: 1+ goals | 0.290 | 0.200 | 27/87 | +0.006 | STANDARD |
| Charlie Coyle: 1+ points | 0.553 | 0.465 | 48/55 | +0.056 | STANDARD |
| Tage Thompson: 1+ points | 0.538 | 0.620 | 64/40 | +0.045 | STANDARD |
| Charlie Coyle: 2+ points | 0.199 | 0.120 | 18/94 | +0.009 | STANDARD |

**MIN @ NSH** · priced 122/124 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 29.81, exp saves 25.56 (sd 7.04), pull risk 0.075
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 25.29 (sd 6.77), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Steven Stamkos: 1+ goals | 0.328 | 0.185 | 32/95 | -0.008 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.362 | 0.225 | 27/82 | +0.078 | STANDARD |
| Ryan Hartman: 1+ goals | 0.272 | 0.140 | 23/95 | +0.029 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.354 | 0.225 | 40/95 | -0.063 | STANDARD |
| Blake Coleman: 1+ goals | 0.275 | 0.150 | 25/95 | +0.012 | STANDARD |
| Matt Boldy: 1+ goals | 0.351 | 0.230 | 36/90 | -0.025 | STANDARD |

**SEA @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.7, exp saves 24.08 (sd 6.54), pull risk 0.055
- SEA net: Joey Daccord (PROJECTED) exp shots 28.94, exp saves 24.93 (sd 6.8), pull risk 0.064

**CHI @ UTA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 24.86, exp saves 21.82 (sd 6.09), pull risk 0.05
- CHI net: Spencer Knight (PROJECTED) exp shots 29.49, exp saves 24.9 (sd 7.06), pull risk 0.09

**EDM @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.37, exp saves 26.02 (sd 7.13), pull risk 0.074
- EDM net: Devon Levi (PROJECTED) exp shots 26.05, exp saves 22.59 (sd 6.28), pull risk 0.063

**FLA @ SJS** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.16, exp saves 23.7 (sd 6.43), pull risk 0.06
- FLA net: Akira Schmid (PROJECTED) exp shots 26.2, exp saves 22.43 (sd 6.35), pull risk 0.071

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
