# NHL slate 2026-10-01 — RESEARCH_ONLY

generated 2026-10-01T17:12:12Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 8 · simulated (not started): 8 · markets on board: 3431 · contracts joined: 1415 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 1215, 'NO_EDGE': 85, 'OK': 115}
families: {'period_winner': 72, 'period_spread': 48, 'period_total': 72, 'player_assists': 208, 'game_early_goal': 8, 'first_goal': 263, 'game_winner': 16, 'player_goals': 263, 'game_overtime': 8, 'player_points': 269, 'goalie_saves': 4, 'game_spread': 32, 'team_total': 80, 'game_total': 72}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 2026-10-01T23:00:00Z | T-3h | 0.623 | 0.377 | 0.176 | 5.81 | 3.28 | 2.53 | 161 (25/136) | CONFIRMED/PROJECTED |
| TBL @ NYR | 2026-10-01T23:00:00Z | T-3h | 0.508 | 0.492 | 0.187 | 5.59 | 2.82 | 2.77 | 177 (25/152) | CONFIRMED/PROBABLE |
| BUF @ CBJ | 2026-10-01T23:00:00Z | T-3h | 0.516 | 0.484 | 0.182 | 5.89 | 3.00 | 2.90 | 183 (25/158) | PROBABLE/CONFIRMED |
| MIN @ NSH | 2026-10-02T00:00:00Z | T-6h | 0.462 | 0.538 | 0.171 | 6.56 | 3.16 | 3.40 | 176 (25/151) | CONFIRMED/PROJECTED |
| SEA @ CGY | 2026-10-02T01:00:00Z | T-6h | 0.525 | 0.474 | 0.181 | 6.10 | 3.13 | 2.97 | 200 (25/175) | CONFIRMED/PROJECTED |
| CHI @ UTA | 2026-10-02T01:30:00Z | T-6h | 0.627 | 0.373 | 0.175 | 6.14 | 3.47 | 2.66 | 161 (25/136) | PROBABLE/PROJECTED |
| EDM @ VAN | 2026-10-02T02:00:00Z | T-6h | 0.424 | 0.576 | 0.171 | 6.65 | 3.08 | 3.57 | 172 (25/147) | PROJECTED/PROJECTED |
| FLA @ SJS | 2026-10-02T02:00:00Z | T-6h | 0.530 | 0.470 | 0.166 | 6.52 | 3.35 | 3.16 | 185 (25/160) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT01EDMVAN-EDM2 | game_spread | 0.358 | 0.465 | 0.443 | 47 | 54 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB4 | team_total | 0.311 | 0.425 | 0.401 | 44 | 59 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB3 | team_total | 0.533 | 0.640 | 0.619 | 65 | 37 | no | +0.081 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3 | game_spread | 0.231 | 0.325 | 0.305 | 33 | 68 | no | +0.074 | OK |
| KXNHLGAME-26OCT01FLASJ-SJ | game_winner | 0.530 | 0.435 | 0.454 | 44 | 57 | yes | +0.073 | OK |
| KXNHLGAME-26OCT01FLASJ-FLA | game_winner | 0.470 | 0.565 | 0.546 | 57 | 44 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA2 | game_spread | 0.266 | 0.355 | 0.336 | 36 | 65 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA3 | game_spread | 0.159 | 0.245 | 0.226 | 25 | 76 | no | +0.068 | OK |
| KXNHLGAME-26OCT01EDMVAN-EDM | game_winner | 0.576 | 0.665 | 0.648 | 67 | 34 | no | +0.068 | OK |
| KXNHLGAME-26OCT01EDMVAN-VAN | game_winner | 0.424 | 0.335 | 0.352 | 34 | 67 | yes | +0.068 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ2 | game_spread | 0.315 | 0.235 | 0.250 | 24 | 77 | yes | +0.062 | OK |
| KXNHLGAME-26OCT01TBNYR-TB | game_winner | 0.492 | 0.575 | 0.559 | 58 | 43 | no | +0.061 | OK |
| KXNHLGAME-26OCT01TBNYR-NYR | game_winner | 0.508 | 0.425 | 0.441 | 43 | 58 | yes | +0.061 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB3 | game_spread | 0.148 | 0.225 | 0.208 | 23 | 78 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB2 | game_spread | 0.265 | 0.345 | 0.328 | 35 | 66 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB5 | team_total | 0.149 | 0.225 | 0.208 | 23 | 78 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT01TBNYR-4 | game_total | 0.793 | 0.865 | 0.853 | 87 | 14 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT01TBNYR-6 | game_total | 0.455 | 0.535 | 0.519 | 54 | 47 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ5 | team_total | 0.255 | 0.180 | 0.194 | 19 | 83 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT01TBNYR-5 | game_total | 0.694 | 0.765 | 0.752 | 77 | 24 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB2 | team_total | 0.759 | 0.830 | 0.817 | 84 | 18 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT01TBNYR-7 | game_total | 0.342 | 0.415 | 0.400 | 42 | 59 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3 | team_total | 0.657 | 0.585 | 0.600 | 59 | 42 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT01MINNSH-7 | game_total | 0.510 | 0.445 | 0.458 | 45 | 56 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ4 | team_total | 0.438 | 0.365 | 0.379 | 38 | 65 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT01TBNYR-8 | game_total | 0.177 | 0.235 | 0.222 | 24 | 77 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 | team_total | 0.492 | 0.570 | 0.555 | 59 | 45 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN2 | game_spread | 0.229 | 0.175 | 0.185 | 18 | 83 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH3 | team_total | 0.615 | 0.550 | 0.563 | 56 | 46 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ3 | game_spread | 0.197 | 0.145 | 0.154 | 15 | 86 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN3 | team_total | 0.595 | 0.525 | 0.539 | 54 | 49 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF4 | team_total | 0.337 | 0.400 | 0.387 | 41 | 61 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN4 | team_total | 0.382 | 0.315 | 0.328 | 33 | 70 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA3 | game_spread | 0.261 | 0.315 | 0.304 | 32 | 69 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT01TBNYR-9 | game_total | 0.117 | 0.165 | 0.154 | 17 | 84 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT01MINNSH-8 | game_total | 0.307 | 0.255 | 0.265 | 26 | 75 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-6 | game_total | 0.509 | 0.570 | 0.558 | 58 | 44 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT01MINNSH-9 | game_total | 0.224 | 0.175 | 0.184 | 18 | 83 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-5 | game_total | 0.735 | 0.785 | 0.776 | 79 | 22 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT01TBNYR-NYR2 | game_spread | 0.275 | 0.225 | 0.234 | 23 | 78 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT01MINNSH-6 | game_total | 0.620 | 0.565 | 0.576 | 57 | 44 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH5 | team_total | 0.221 | 0.170 | 0.179 | 18 | 84 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 | team_total | 0.403 | 0.465 | 0.452 | 48 | 55 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ2 | team_total | 0.840 | 0.785 | 0.797 | 80 | 23 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM5 | team_total | 0.295 | 0.355 | 0.343 | 37 | 66 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT01MINNSH-10 | game_total | 0.114 | 0.075 | 0.082 | 8 | 93 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA3 | team_total | 0.616 | 0.675 | 0.664 | 69 | 34 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM3 | team_total | 0.698 | 0.750 | 0.740 | 76 | 26 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ6 | team_total | 0.122 | 0.075 | 0.083 | 9 | 94 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN5 | team_total | 0.206 | 0.155 | 0.164 | 17 | 86 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT01PHINJ-6 | game_total | 0.497 | 0.545 | 0.535 | 55 | 46 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN3 | game_spread | 0.132 | 0.095 | 0.102 | 10 | 91 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA2 | game_spread | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB6 | team_total | 0.059 | 0.100 | 0.090 | 11 | 91 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH4 | team_total | 0.401 | 0.345 | 0.356 | 36 | 67 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-7 | game_total | 0.399 | 0.450 | 0.440 | 46 | 56 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-4 | game_total | 0.829 | 0.870 | 0.863 | 88 | 14 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF3 | team_total | 0.562 | 0.610 | 0.600 | 62 | 40 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN2 | team_total | 0.803 | 0.760 | 0.769 | 77 | 25 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF5 | team_total | 0.169 | 0.215 | 0.205 | 23 | 80 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA5 | team_total | 0.218 | 0.265 | 0.255 | 28 | 75 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT01PHINJ-PHI3 | game_spread | 0.095 | 0.125 | 0.118 | 13 | 88 | no | +0.018 | OK |
| KXNHLGAME-26OCT01CHIUTA-CHI | game_winner | 0.373 | 0.335 | 0.342 | 34 | 67 | yes | +0.017 | OK |
| KXNHLGAME-26OCT01CHIUTA-UTA | game_winner | 0.627 | 0.665 | 0.658 | 67 | 34 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN6 | team_total | 0.092 | 0.060 | 0.065 | 7 | 95 | yes | +0.017 | OK |
| KXNHLSPREAD-26OCT01BUFCBJ-BUF3 | game_spread | 0.153 | 0.185 | 0.178 | 19 | 82 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT01PHINJ-4 | game_total | 0.815 | 0.845 | 0.839 | 85 | 16 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT01PHINJ-5 | game_total | 0.721 | 0.755 | 0.748 | 76 | 25 | no | +0.016 | OK |
| KXNHLGAME-26OCT01MINNSH-MIN | game_winner | 0.538 | 0.575 | 0.568 | 58 | 43 | no | +0.015 | OK |
| KXNHLGAME-26OCT01MINNSH-NSH | game_winner | 0.462 | 0.425 | 0.432 | 43 | 58 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH6 | team_total | 0.099 | 0.070 | 0.075 | 8 | 94 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT01FLASJ-10 | game_total | 0.110 | 0.085 | 0.089 | 9 | 92 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA2 | team_total | 0.817 | 0.855 | 0.848 | 87 | 16 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH2 | team_total | 0.815 | 0.775 | 0.783 | 79 | 24 | yes | +0.013 | OK |
| KXNHLSPREAD-26OCT01BUFCBJ-BUF2 | game_spread | 0.262 | 0.295 | 0.288 | 30 | 71 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA4 | team_total | 0.470 | 0.515 | 0.506 | 53 | 50 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA6 | team_total | 0.100 | 0.130 | 0.124 | 14 | 88 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT01TBNYR-3 | game_total | 0.945 | 0.965 | 0.962 | 97 | 4 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT01MINNSH-MIN3 | game_spread | 0.206 | 0.235 | 0.229 | 24 | 77 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT01FLASJ-9 | game_total | 0.223 | 0.195 | 0.200 | 20 | 81 | yes | +0.011 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 0.623 | 0.565 | 0.176 | 0.224 | 5.81 | 5.79 | 0.984/0.991 | KXNHLGAME-26OCT01PHINJ-NJ -0.058 |
| TBL @ NYR | 0.508 | 0.524 | 0.187 | 0.220 | 5.59 | 5.93 | 0.934/0.951 | KXNHLTOTAL-26OCT01TBNYR-7 +0.067 |
| BUF @ CBJ | 0.516 | 0.557 | 0.182 | 0.218 | 5.89 | 6.16 | 0.955/1.002 | KXNHLTEAMTOTAL-26OCT01BUFCBJ-CBJ4 +0.058 |
| MIN @ NSH | 0.462 | 0.478 | 0.171 | 0.219 | 6.56 | 6.53 | 1.004/1.003 | KXNHLSPREAD-26OCT01MINNSH-MIN2 -0.022 |
| SEA @ CGY | 0.525 | 0.512 | 0.181 | 0.225 | 6.10 | 6.12 | 1.005/1.005 | KXNHLSPREAD-26OCT01SEACGY-CGY2 -0.016 |
| CHI @ UTA | 0.627 | 0.652 | 0.175 | 0.205 | 6.14 | 6.49 | 0.990/1.003 | KXNHLTOTAL-26OCT01CHIUTA-7 +0.064 |
| EDM @ VAN | 0.424 | 0.450 | 0.171 | 0.213 | 6.65 | 6.51 | 1.021/0.994 | KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 -0.032 |
| FLA @ SJS | 0.530 | 0.556 | 0.166 | 0.219 | 6.52 | 6.42 | 1.034/0.998 | KXNHLSPREAD-26OCT01FLASJ-FLA2 -0.030 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 27 recommended · full analysis in card.md / packet.json `thesis_card`

- Sean Couturier: 1+ goals YES @ 11c · p 0.1496 (adj 0.1372) · $2.31 · thesis PHI:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 12c · p 0.1535 (adj 0.1439) · $1.95 · thesis NJD:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 72c · p 0.7692 (adj 0.7531) · $8.04 · thesis NJD:SUPPRESSED
- Porter Martone: 1+ goals NO @ 77c · p 0.8102 (adj 0.7976) · $8.04 · thesis PHI:SUPPRESSED
- John Carlson: 1+ assists NO @ 54c · p 0.7415 (adj 0.5975) · $8.37 · thesis TBL:SUPPRESSED
- New York R wins YES @ 43c · p 0.5246 (adj 0.4798) · $5.33 · thesis NYR:WINS
- Pavel Dorofeyev: 1+ assists NO @ 76c · p 0.8424 (adj 0.7937) · $8.37 · thesis NYR:SUPPRESSED
- Zach Metsa: 1+ goals NO @ 94c · p 0.967 (adj 0.9577) · $8.81 · thesis DIFFUSE
- Kent Johnson: 1+ goals NO @ 78c · p 0.8231 (adj 0.8111) · $8.81 · thesis CBJ:SUPPRESSED
- Sean Monahan: 1+ goals YES @ 20c · p 0.2397 (adj 0.2273) · $2.19 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 23c · p 0.273 (adj 0.2585) · $2.25 · thesis CBJ:OFFENSE_4PLUS
- Jared Spurgeon: 1+ goals NO @ 91c · p 0.9343 (adj 0.927) · $8.82 · thesis DIFFUSE
- Ryan Hartman: 1+ goals YES @ 23c · p 0.2714 (adj 0.2598) · $2.44 · thesis MIN:OFFENSE_4PLUS
- Brandon Montour: 1+ goals NO @ 84c · p 0.8928 (adj 0.8759) · $8.34 · thesis SEA:SUPPRESSED
- Jacob Melanson: 1+ goals YES @ 9c · p 0.1227 (adj 0.112) · $1.82 · thesis SEA:OFFENSE_4PLUS
- Jared McCann: 1+ goals NO @ 72c · p 0.7569 (adj 0.7464) · $4.9 · thesis SEA:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 12c · p 0.1664 (adj 0.1535) · $3.13 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 62c · p 0.7454 (adj 0.6574) · $7.62 · thesis CHI:SUPPRESSED
- Vincent Trocheck: 1+ assists NO @ 66c · p 0.7716 (adj 0.6926) · $7.26 · thesis UTA:SUPPRESSED
- Anders Lee: 1+ goals YES @ 24c · p 0.2804 (adj 0.2678) · $2.47 · thesis UTA:OFFENSE_4PLUS
- Leon Draisaitl: 1+ goals NO @ 54c · p 0.6319 (adj 0.6077) · $8.82 · thesis EDM:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 21c · p 0.2608 (adj 0.2468) · $3.42 · thesis VAN:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 17c · p 0.2134 (adj 0.2001) · $2.63 · thesis VAN:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 33c · p 0.4407 (adj 0.3655) · $2.29 · thesis EDM:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 15c · p 0.2241 (adj 0.2018) · $4.79 · thesis SJS:OFFENSE_4PLUS
- Florida wins by over 2.5 goals NO @ 76c · p 0.8522 (adj 0.8036) · $8.82 · thesis SJS:WINS
- Aleksander Barkov: 1+ assists NO @ 52c · p 0.6974 (adj 0.5723) · $7.99 · thesis FLA:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ NJD** · priced 110/110 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 24.74, exp saves 21.76 (sd 6.0), pull risk 0.045
- PHI net: Joseph Woll (PROJECTED) exp shots 28.45, exp saves 24.53 (sd 6.64), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ points | 0.361 | 0.495 | 51/52 | +0.102 | STANDARD |
| Anthony Mantha: 1+ points | 0.325 | 0.455 | 47/56 | +0.098 | STANDARD |
| Anthony Mantha: 1+ assists | 0.136 | 0.265 | 28/75 | +0.100 | STANDARD |
| Luke Evangelista: 1+ assists | 0.219 | 0.345 | 36/67 | +0.095 | STANDARD |
| Jake Allen: 23+ saves | 0.438 | 0.540 | 54/ | -0.119 |  |
| Luke Evangelista: 2+ points | 0.076 | 0.155 | 18/87 | +0.046 | STANDARD |

**TBL @ NYR** · priced 126/126 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (CONFIRMED) exp shots 28.0, exp saves 24.27 (sd 6.55), pull risk 0.055
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 24.5, exp saves 21.2 (sd 5.88), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.259 | 0.480 | 50/54 | +0.184 | STANDARD |
| John Carlson: 1+ points | 0.338 | 0.545 | 56/47 | +0.175 | STANDARD |
| John Carlson: 2+ points | 0.065 | 0.205 | 22/81 | +0.114 | STANDARD |
| Gabe Perreault: 1+ assists | 0.326 | 0.200 | 23/83 | +0.084 | STANDARD |
| Victor Hedman: 1+ assists | 0.178 | 0.295 | 30/71 | +0.097 | STANDARD |
| Gabe Perreault: 1+ points | 0.467 | 0.355 | 37/66 | +0.081 | STANDARD |

**BUF @ CBJ** · priced 130/132 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROBABLE) exp shots 27.66, exp saves 24.13 (sd 6.52), pull risk 0.057
- BUF net: Ukko-Pekka Luukkonen (CONFIRMED) exp shots 28.58, exp saves 24.65 (sd 6.71), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tage Thompson: 1+ assists | 0.320 | 0.420 | 44/60 | +0.063 | STANDARD |
| Tage Thompson: 1+ points | 0.530 | 0.620 | 64/40 | +0.053 | STANDARD |
| Charlie Coyle: 1+ points | 0.547 | 0.460 | 47/55 | +0.059 | STANDARD |
| Tage Thompson: 2+ points | 0.182 | 0.260 | 29/77 | +0.035 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.224 | 0.295 | 31/72 | +0.042 | STANDARD |
| Charlie Coyle: 1+ goals | 0.273 | 0.215 | 23/80 | +0.031 | STANDARD |

**MIN @ NSH** · priced 123/125 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 29.81, exp saves 25.53 (sd 7.12), pull risk 0.076
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 25.29 (sd 6.82), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Juuse Saros: 26+ saves | 0.505 | 0.310 | 54/92 | -0.052 |  |
| Jonathan Marchessault: 1+ points | 0.487 | 0.375 | 39/64 | +0.080 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.358 | 0.250 | 27/77 | +0.074 | STANDARD |
| Max Shabanov: 1+ points | 0.376 | 0.480 | 50/54 | +0.067 | STANDARD |
| Steven Stamkos: 1+ assists | 0.391 | 0.330 | 34/68 | +0.035 | STANDARD |
| Max Shabanov: 1+ assists | 0.244 | 0.305 | 34/73 | +0.012 | STANDARD |

**SEA @ CGY** · priced 149/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.7, exp saves 24.08 (sd 6.54), pull risk 0.055
- SEA net: Joey Daccord (PROJECTED) exp shots 28.94, exp saves 24.93 (sd 6.8), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Klapka: 1+ points | 0.304 | 0.130 | 23/97 | +0.061 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.255 | 0.105 | 20/99 | +0.043 | STANDARD |
| Connor Zary: 1+ assists | 0.267 | 0.130 | 25/99 | +0.004 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.260 | 0.135 | 26/99 | -0.013 | STANDARD |
| Jared McCann: 1+ points | 0.446 | 0.560 | 58/46 | +0.077 | STANDARD |
| Kevin Bahl: 1+ points | 0.254 | 0.145 | 25/96 | -0.009 | STANDARD |

**CHI @ UTA** · priced 108/110 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 24.86, exp saves 21.8 (sd 6.05), pull risk 0.051
- CHI net: Spencer Knight (PROJECTED) exp shots 29.49, exp saves 24.89 (sd 7.0), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.255 | 0.390 | 40/62 | +0.109 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.228 | 0.350 | 36/66 | +0.096 | STANDARD |
| Frank Nazar: 1+ assists | 0.334 | 0.215 | 24/81 | +0.081 | STANDARD |
| Patrick Kane: 1+ points | 0.436 | 0.545 | 56/47 | +0.076 | STANDARD |
| Frank Nazar: 1+ points | 0.472 | 0.365 | 38/65 | +0.075 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.542 | 0.455 | 47/56 | +0.055 | STANDARD |

**EDM @ VAN** · priced 121/121 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.37, exp saves 26.02 (sd 7.13), pull risk 0.074
- EDM net: Devon Levi (PROJECTED) exp shots 26.05, exp saves 22.59 (sd 6.28), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 2+ points | 0.258 | 0.465 | 48/55 | +0.175 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.404 | 0.585 | 60/43 | +0.149 | STANDARD |
| Leon Draisaitl: 1+ points | 0.625 | 0.775 | 80/25 | +0.111 | STANDARD |
| Connor McDavid: 2+ points | 0.385 | 0.535 | 55/48 | +0.117 | STANDARD |
| Leon Draisaitl: 3+ points | 0.076 | 0.215 | 23/80 | +0.112 | STANDARD |
| Connor McDavid: 2+ assists | 0.192 | 0.310 | 32/70 | +0.094 | STANDARD |

**FLA @ SJS** · priced 134/134 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.16, exp saves 23.7 (sd 6.43), pull risk 0.06
- FLA net: Akira Schmid (PROJECTED) exp shots 26.2, exp saves 22.43 (sd 6.35), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aleksander Barkov: 1+ assists | 0.303 | 0.495 | 51/52 | +0.160 | STANDARD |
| Aleksander Barkov: 1+ points | 0.447 | 0.630 | 64/38 | +0.157 | STANDARD |
| Brady Tkachuk: 1+ points | 0.471 | 0.615 | 64/41 | +0.102 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.251 | 0.385 | 40/63 | +0.103 | STANDARD |
| Aleksander Barkov: 2+ points | 0.121 | 0.255 | 27/76 | +0.106 | STANDARD |
| Brady Tkachuk: 2+ points | 0.136 | 0.250 | 28/78 | +0.072 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
