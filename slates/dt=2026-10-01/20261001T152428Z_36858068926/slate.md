# NHL slate 2026-10-01 — RESEARCH_ONLY

generated 2026-10-01T15:24:28Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 8 · simulated (not started): 8 · markets on board: 3430 · contracts joined: 1414 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 1214, 'NO_EDGE': 85, 'OK': 115}
families: {'period_winner': 72, 'period_spread': 48, 'period_total': 72, 'player_assists': 208, 'game_early_goal': 8, 'first_goal': 263, 'game_winner': 16, 'player_goals': 263, 'game_overtime': 8, 'player_points': 269, 'goalie_saves': 3, 'game_spread': 32, 'team_total': 80, 'game_total': 72}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 2026-10-01T23:00:00Z | T-6h | 0.620 | 0.380 | 0.176 | 5.83 | 3.29 | 2.54 | 161 (25/136) | PROBABLE/PROJECTED |
| TBL @ NYR | 2026-10-01T23:00:00Z | T-6h | 0.519 | 0.481 | 0.187 | 5.64 | 2.87 | 2.77 | 177 (25/152) | CONFIRMED/PROJECTED |
| BUF @ CBJ | 2026-10-01T23:00:00Z | T-6h | 0.519 | 0.481 | 0.182 | 5.92 | 3.02 | 2.90 | 182 (25/157) | PROBABLE/PROBABLE |
| MIN @ NSH | 2026-10-02T00:00:00Z | T-6h | 0.462 | 0.538 | 0.171 | 6.56 | 3.16 | 3.40 | 176 (25/151) | CONFIRMED/PROJECTED |
| SEA @ CGY | 2026-10-02T01:00:00Z | T-6h | 0.525 | 0.474 | 0.181 | 6.10 | 3.13 | 2.97 | 200 (25/175) | CONFIRMED/PROJECTED |
| CHI @ UTA | 2026-10-02T01:30:00Z | T-6h | 0.625 | 0.374 | 0.168 | 6.14 | 3.47 | 2.67 | 161 (25/136) | PROJECTED/PROJECTED |
| EDM @ VAN | 2026-10-02T02:00:00Z | T-6h | 0.424 | 0.576 | 0.171 | 6.65 | 3.08 | 3.57 | 172 (25/147) | PROJECTED/PROJECTED |
| FLA @ SJS | 2026-10-02T02:00:00Z | T-6h | 0.530 | 0.470 | 0.166 | 6.52 | 3.35 | 3.16 | 185 (25/160) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB4 | team_total | 0.312 | 0.435 | 0.409 | 45 | 58 | no | +0.091 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM2 | game_spread | 0.358 | 0.465 | 0.443 | 47 | 54 | no | +0.085 | OK |
| KXNHLGAME-26OCT01TBNYR-TB | game_winner | 0.481 | 0.585 | 0.564 | 59 | 42 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB3 | team_total | 0.533 | 0.640 | 0.619 | 65 | 37 | no | +0.080 | OK |
| KXNHLGAME-26OCT01EDMVAN-VAN | game_winner | 0.424 | 0.325 | 0.344 | 33 | 68 | yes | +0.078 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3 | game_spread | 0.231 | 0.325 | 0.305 | 33 | 68 | no | +0.074 | OK |
| KXNHLGAME-26OCT01FLASJ-SJ | game_winner | 0.530 | 0.435 | 0.454 | 44 | 57 | yes | +0.073 | OK |
| KXNHLGAME-26OCT01FLASJ-FLA | game_winner | 0.470 | 0.565 | 0.546 | 57 | 44 | no | +0.073 | OK |
| KXNHLGAME-26OCT01TBNYR-NYR | game_winner | 0.519 | 0.425 | 0.444 | 43 | 58 | yes | +0.072 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB2 | game_spread | 0.254 | 0.345 | 0.326 | 35 | 66 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA2 | game_spread | 0.266 | 0.355 | 0.336 | 36 | 65 | no | +0.069 | OK |
| KXNHLGAME-26OCT01EDMVAN-EDM | game_winner | 0.576 | 0.665 | 0.648 | 67 | 34 | no | +0.068 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ2 | game_spread | 0.315 | 0.235 | 0.250 | 24 | 77 | yes | +0.062 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB3 | game_spread | 0.147 | 0.225 | 0.207 | 23 | 78 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT01TBNYR-6 | game_total | 0.463 | 0.545 | 0.529 | 55 | 46 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA3 | game_spread | 0.159 | 0.240 | 0.222 | 25 | 77 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB5 | team_total | 0.151 | 0.230 | 0.212 | 24 | 78 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT01TBNYR-5 | game_total | 0.701 | 0.775 | 0.761 | 78 | 23 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT01TBNYR-7 | game_total | 0.359 | 0.435 | 0.419 | 44 | 57 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT01TBNYR-4 | game_total | 0.798 | 0.865 | 0.853 | 87 | 14 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB2 | team_total | 0.759 | 0.835 | 0.821 | 85 | 18 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3 | team_total | 0.657 | 0.585 | 0.600 | 59 | 42 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ5 | team_total | 0.255 | 0.185 | 0.198 | 20 | 83 | yes | +0.044 | OK |
| KXNHLTOTAL-26OCT01MINNSH-8 | game_total | 0.307 | 0.245 | 0.257 | 25 | 76 | yes | +0.044 | OK |
| KXNHLTOTAL-26OCT01MINNSH-7 | game_total | 0.510 | 0.445 | 0.458 | 45 | 56 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT01TBNYR-8 | game_total | 0.185 | 0.245 | 0.232 | 25 | 76 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ4 | team_total | 0.438 | 0.365 | 0.379 | 38 | 65 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT01TBNYR-NYR2 | game_spread | 0.282 | 0.225 | 0.236 | 23 | 78 | yes | +0.040 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN2 | game_spread | 0.229 | 0.175 | 0.185 | 18 | 83 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN3 | team_total | 0.595 | 0.525 | 0.539 | 54 | 49 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN4 | team_total | 0.382 | 0.315 | 0.328 | 33 | 70 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB6 | team_total | 0.059 | 0.110 | 0.097 | 12 | 90 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF4 | team_total | 0.339 | 0.400 | 0.388 | 41 | 61 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT01MINNSH-9 | game_total | 0.224 | 0.175 | 0.184 | 18 | 83 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT01MINNSH-6 | game_total | 0.620 | 0.560 | 0.572 | 57 | 45 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH5 | team_total | 0.221 | 0.170 | 0.179 | 18 | 84 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 | team_total | 0.492 | 0.555 | 0.543 | 57 | 46 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-5 | game_total | 0.738 | 0.785 | 0.776 | 79 | 22 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 | team_total | 0.403 | 0.465 | 0.452 | 48 | 55 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ2 | team_total | 0.840 | 0.785 | 0.797 | 80 | 23 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-6 | game_total | 0.514 | 0.570 | 0.559 | 58 | 44 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM5 | team_total | 0.295 | 0.355 | 0.343 | 37 | 66 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA3 | team_total | 0.616 | 0.675 | 0.664 | 69 | 34 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM3 | team_total | 0.698 | 0.750 | 0.740 | 76 | 26 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH3 | team_total | 0.615 | 0.555 | 0.567 | 57 | 46 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-7 | game_total | 0.405 | 0.455 | 0.445 | 46 | 55 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT01TBNYR-9 | game_total | 0.123 | 0.165 | 0.156 | 17 | 84 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ3 | game_spread | 0.197 | 0.155 | 0.163 | 16 | 85 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN5 | team_total | 0.206 | 0.155 | 0.164 | 17 | 86 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA3 | game_spread | 0.259 | 0.305 | 0.295 | 31 | 70 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN3 | game_spread | 0.132 | 0.095 | 0.102 | 10 | 91 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH4 | team_total | 0.401 | 0.345 | 0.356 | 36 | 67 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF3 | team_total | 0.561 | 0.610 | 0.600 | 62 | 40 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT01BUFCBJ-BUF3 | game_spread | 0.148 | 0.185 | 0.177 | 19 | 82 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN2 | team_total | 0.803 | 0.760 | 0.769 | 77 | 25 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT01PHINJ-6 | game_total | 0.502 | 0.545 | 0.536 | 55 | 46 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF5 | team_total | 0.169 | 0.215 | 0.205 | 23 | 80 | no | +0.020 | OK |
| KXNHLGAME-26OCT01CHIUTA-UTA | game_winner | 0.625 | 0.665 | 0.657 | 67 | 34 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA5 | team_total | 0.218 | 0.265 | 0.255 | 28 | 75 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT01MINNSH-10 | game_total | 0.114 | 0.080 | 0.086 | 9 | 93 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN6 | team_total | 0.092 | 0.060 | 0.065 | 7 | 95 | yes | +0.017 | OK |
| KXNHLSPREAD-26OCT01PHINJ-PHI3 | game_spread | 0.095 | 0.125 | 0.119 | 13 | 88 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT01PHINJ-5 | game_total | 0.720 | 0.755 | 0.748 | 76 | 25 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ6 | team_total | 0.122 | 0.080 | 0.087 | 10 | 94 | yes | +0.016 | OK |
| KXNHLGAME-26OCT01MINNSH-MIN | game_winner | 0.538 | 0.575 | 0.568 | 58 | 43 | no | +0.015 | OK |
| KXNHLGAME-26OCT01MINNSH-NSH | game_winner | 0.462 | 0.425 | 0.432 | 43 | 58 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA4 | team_total | 0.468 | 0.510 | 0.502 | 52 | 50 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH6 | team_total | 0.099 | 0.070 | 0.075 | 8 | 94 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA2 | team_total | 0.817 | 0.855 | 0.848 | 87 | 16 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH2 | team_total | 0.815 | 0.775 | 0.783 | 79 | 24 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT01PHINJ-4 | game_total | 0.818 | 0.850 | 0.844 | 86 | 16 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA2 | game_spread | 0.400 | 0.435 | 0.428 | 44 | 57 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT01BUFCBJ-BUF2 | game_spread | 0.263 | 0.295 | 0.288 | 30 | 71 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT01TBNYR-3 | game_total | 0.945 | 0.965 | 0.962 | 97 | 4 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-4 | game_total | 0.829 | 0.865 | 0.858 | 88 | 15 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT01FLASJ-9 | game_total | 0.223 | 0.195 | 0.200 | 20 | 81 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT01MINNSH-NSH2 | game_spread | 0.264 | 0.230 | 0.237 | 24 | 78 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT01SEACGY-CGY5 | team_total | 0.212 | 0.185 | 0.190 | 19 | 82 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT01MINNSH-5 | game_total | 0.812 | 0.785 | 0.791 | 79 | 22 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT01SEACGY-SEA3 | game_spread | 0.150 | 0.175 | 0.170 | 18 | 83 | no | +0.011 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 0.620 | 0.565 | 0.176 | 0.222 | 5.83 | 5.80 | 0.985/0.991 | KXNHLGAME-26OCT01PHINJ-NJ -0.055 |
| TBL @ NYR | 0.519 | 0.525 | 0.187 | 0.221 | 5.64 | 5.96 | 0.934/0.957 | KXNHLTOTAL-26OCT01TBNYR-7 +0.056 |
| BUF @ CBJ | 0.519 | 0.554 | 0.182 | 0.215 | 5.92 | 6.15 | 0.955/1.000 | KXNHLTEAMTOTAL-26OCT01BUFCBJ-CBJ4 +0.053 |
| MIN @ NSH | 0.462 | 0.478 | 0.171 | 0.219 | 6.56 | 6.53 | 1.004/1.003 | KXNHLSPREAD-26OCT01MINNSH-MIN2 -0.022 |
| SEA @ CGY | 0.525 | 0.512 | 0.181 | 0.225 | 6.10 | 6.12 | 1.005/1.005 | KXNHLSPREAD-26OCT01SEACGY-CGY2 -0.016 |
| CHI @ UTA | 0.625 | 0.649 | 0.168 | 0.199 | 6.14 | 6.49 | 0.992/1.003 | KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA4 +0.068 |
| EDM @ VAN | 0.424 | 0.450 | 0.171 | 0.213 | 6.65 | 6.51 | 1.021/0.994 | KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 -0.032 |
| FLA @ SJS | 0.530 | 0.556 | 0.166 | 0.219 | 6.52 | 6.42 | 1.034/0.998 | KXNHLSPREAD-26OCT01FLASJ-FLA2 -0.030 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 27 recommended · full analysis in card.md / packet.json `thesis_card`

- Sean Couturier: 1+ goals YES @ 11c · p 0.1437 (adj 0.134) · $2.62 · thesis PHI:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 12c · p 0.1547 (adj 0.1448) · $2.74 · thesis NJD:OFFENSE_4PLUS
- Anthony Mantha: 1+ assists NO @ 74c · p 0.8607 (adj 0.7725) · $11.56 · thesis NJD:SUPPRESSED
- Noel Acciari: 1+ goals YES @ 9c · p 0.1153 (adj 0.1077) · $1.8 · thesis PHI:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 54c · p 0.7488 (adj 0.6001) · $11.56 · thesis TBL:SUPPRESSED
- Tye Kartye: 1+ goals YES @ 10c · p 0.1361 (adj 0.1246) · $2.5 · thesis NYR:OFFENSE_4PLUS
- Tampa Bay wins by over 1.5 goals NO @ 66c · p 0.749 (adj 0.702) · $6.29 · thesis NYR:WINS
- Tampa Bay wins by over 2.5 goals NO @ 78c · p 0.8493 (adj 0.8122) · $5.66 · thesis NYR:WINS
- Charlie Coyle: 1+ goals YES @ 22c · p 0.2684 (adj 0.2538) · $3.89 · thesis CBJ:OFFENSE_4PLUS
- Sean Monahan: 1+ goals YES @ 20c · p 0.243 (adj 0.2285) · $3.03 · thesis CBJ:OFFENSE_4PLUS
- Owen Power: 1+ goals NO @ 90c · p 0.9269 (adj 0.9177) · $11.51 · thesis BUF:SUPPRESSED
- Conor Garland: 1+ goals NO @ 82c · p 0.853 (adj 0.8422) · $10.46 · thesis CBJ:SUPPRESSED
- Ryan Hartman: 1+ goals YES @ 23c · p 0.2714 (adj 0.2573) · $2.72 · thesis MIN:OFFENSE_4PLUS
- Mavrik Bourque: 1+ goals YES @ 18c · p 0.2161 (adj 0.2033) · $2.19 · thesis NSH:OFFENSE_4PLUS
- Brandon Montour: 1+ goals NO @ 84c · p 0.8928 (adj 0.8759) · $11.56 · thesis SEA:SUPPRESSED
- Freddy Gaudreau: 1+ goals YES @ 10c · p 0.1329 (adj 0.1234) · $2.62 · thesis SEA:OFFENSE_4PLUS
- Adam Klapka: 1+ goals YES @ 10c · p 0.1308 (adj 0.1206) · $2.18 · thesis CGY:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 12c · p 0.17 (adj 0.155) · $4.19 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 62c · p 0.7413 (adj 0.6527) · $7.71 · thesis CHI:SUPPRESSED
- Mattias Ekholm: 1+ goals YES @ 9c · p 0.1209 (adj 0.1119) · $2.42 · thesis EDM:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 17c · p 0.2134 (adj 0.2001) · $3.36 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 22c · p 0.2608 (adj 0.2468) · $2.69 · thesis VAN:OFFENSE_4PLUS
- Leon Draisaitl: 2+ points NO @ 55c · p 0.7424 (adj 0.5831) · $6.97 · thesis EDM:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 15c · p 0.2241 (adj 0.2006) · $5.78 · thesis SJS:OFFENSE_4PLUS
- San Jose wins by over 1.5 goals YES @ 24c · p 0.3336 (adj 0.2843) · $2.65 · thesis SJS:WINS_BY_2PLUS
- Aleksander Barkov: 1+ assists NO @ 52c · p 0.6974 (adj 0.5723) · $9.8 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 77c · p 0.8522 (adj 0.8061) · $9.53 · thesis SJS:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ NJD** · priced 110/110 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROBABLE) exp shots 24.74, exp saves 21.74 (sd 5.94), pull risk 0.045
- PHI net: Joseph Woll (PROJECTED) exp shots 28.45, exp saves 24.53 (sd 6.67), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anthony Mantha: 1+ assists | 0.139 | 0.275 | 29/74 | +0.107 | STANDARD |
| Luke Evangelista: 1+ assists | 0.222 | 0.345 | 36/67 | +0.093 | STANDARD |
| Anthony Mantha: 1+ points | 0.323 | 0.445 | 46/57 | +0.089 | STANDARD |
| Luke Evangelista: 1+ points | 0.364 | 0.485 | 50/53 | +0.088 | STANDARD |
| Luke Evangelista: 2+ points | 0.076 | 0.155 | 17/86 | +0.056 | STANDARD |
| Anthony Mantha: 2+ points | 0.061 | 0.130 | 15/89 | +0.042 | STANDARD |

**TBL @ NYR** · priced 126/126 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (CONFIRMED) exp shots 28.0, exp saves 24.25 (sd 6.58), pull risk 0.051
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 24.5, exp saves 21.17 (sd 5.96), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.251 | 0.480 | 50/54 | +0.191 | STANDARD |
| John Carlson: 1+ points | 0.330 | 0.550 | 57/47 | +0.183 | STANDARD |
| Gabe Perreault: 1+ assists | 0.323 | 0.190 | 23/85 | +0.081 | STANDARD |
| John Carlson: 2+ points | 0.064 | 0.195 | 22/83 | +0.096 | STANDARD |
| Gabe Perreault: 1+ points | 0.463 | 0.345 | 36/67 | +0.087 | STANDARD |
| John Carlson: 2+ assists | 0.036 | 0.145 | 17/88 | +0.076 | STANDARD |

**BUF @ CBJ** · priced 129/131 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROBABLE) exp shots 27.66, exp saves 24.19 (sd 6.49), pull risk 0.052
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 28.58, exp saves 24.57 (sd 6.71), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tage Thompson: 1+ assists | 0.321 | 0.430 | 44/58 | +0.082 | STANDARD |
| Tage Thompson: 1+ points | 0.530 | 0.620 | 64/40 | +0.053 | STANDARD |
| Tage Thompson: 2+ points | 0.181 | 0.270 | 29/75 | +0.056 | STANDARD |
| Charlie Coyle: 1+ points | 0.550 | 0.465 | 48/55 | +0.053 | STANDARD |
| Sean Monahan: 1+ points | 0.462 | 0.395 | 41/62 | +0.035 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.228 | 0.295 | 31/72 | +0.037 | STANDARD |

**MIN @ NSH** · priced 123/125 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 29.81, exp saves 25.53 (sd 7.12), pull risk 0.076
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 25.29 (sd 6.82), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonathan Marchessault: 1+ assists | 0.358 | 0.240 | 26/78 | +0.085 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.487 | 0.375 | 39/64 | +0.080 | STANDARD |
| Max Shabanov: 1+ points | 0.376 | 0.440 | 47/59 | +0.017 | STANDARD |
| Steven Stamkos: 1+ points | 0.588 | 0.525 | 54/49 | +0.030 | STANDARD |
| Steven Stamkos: 1+ assists | 0.391 | 0.330 | 34/68 | +0.035 | STANDARD |
| Jonathan Marchessault: 2+ points | 0.153 | 0.095 | 11/92 | +0.036 | STANDARD |

**SEA @ CGY** · priced 149/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.7, exp saves 24.08 (sd 6.54), pull risk 0.055
- SEA net: Joey Daccord (PROJECTED) exp shots 28.94, exp saves 24.93 (sd 6.8), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Klapka: 1+ points | 0.304 | 0.135 | 26/99 | +0.030 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.255 | 0.115 | 22/99 | +0.023 | STANDARD |
| Connor Zary: 1+ assists | 0.267 | 0.140 | 27/99 | -0.017 | STANDARD |
| Kevin Bahl: 1+ points | 0.254 | 0.135 | 26/99 | -0.019 | STANDARD |
| Jared McCann: 1+ assists | 0.269 | 0.385 | 40/63 | +0.084 | STANDARD |
| Jared McCann: 1+ points | 0.446 | 0.560 | 58/46 | +0.077 | STANDARD |

**CHI @ UTA** · priced 108/110 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 24.86, exp saves 21.82 (sd 6.09), pull risk 0.05
- CHI net: Spencer Knight (PROJECTED) exp shots 29.49, exp saves 24.9 (sd 7.06), pull risk 0.09

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.259 | 0.395 | 41/62 | +0.105 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.228 | 0.350 | 37/67 | +0.087 | STANDARD |
| Frank Nazar: 1+ assists | 0.327 | 0.215 | 24/81 | +0.074 | STANDARD |
| Patrick Kane: 1+ points | 0.437 | 0.545 | 57/48 | +0.066 | STANDARD |
| Frank Nazar: 1+ points | 0.471 | 0.370 | 39/65 | +0.064 | STANDARD |
| Patrick Kane: 2+ points | 0.116 | 0.200 | 22/82 | +0.053 | STANDARD |

**EDM @ VAN** · priced 121/121 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.37, exp saves 26.02 (sd 7.13), pull risk 0.074
- EDM net: Devon Levi (PROJECTED) exp shots 26.05, exp saves 22.59 (sd 6.28), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 2+ points | 0.258 | 0.470 | 49/55 | +0.175 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.404 | 0.595 | 62/43 | +0.149 | STANDARD |
| Connor McDavid: 2+ points | 0.385 | 0.545 | 57/48 | +0.117 | STANDARD |
| Leon Draisaitl: 1+ points | 0.625 | 0.780 | 81/25 | +0.111 | STANDARD |
| Leon Draisaitl: 3+ points | 0.076 | 0.215 | 23/80 | +0.112 | STANDARD |
| Connor McDavid: 1+ assists | 0.559 | 0.690 | 71/33 | +0.095 | STANDARD |

**FLA @ SJS** · priced 134/134 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.16, exp saves 23.7 (sd 6.43), pull risk 0.06
- FLA net: Akira Schmid (PROJECTED) exp shots 26.2, exp saves 22.43 (sd 6.35), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aleksander Barkov: 1+ assists | 0.303 | 0.495 | 51/52 | +0.160 | STANDARD |
| Aleksander Barkov: 1+ points | 0.447 | 0.630 | 65/39 | +0.147 | STANDARD |
| Aleksander Barkov: 2+ points | 0.121 | 0.270 | 30/76 | +0.106 | STANDARD |
| Brady Tkachuk: 1+ points | 0.471 | 0.610 | 63/41 | +0.102 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.251 | 0.385 | 41/64 | +0.093 | STANDARD |
| Brady Tkachuk: 2+ points | 0.136 | 0.260 | 28/76 | +0.092 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
