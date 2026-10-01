# NHL slate 2026-10-01 — RESEARCH_ONLY

generated 2026-10-01T14:24:26Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 8 · simulated (not started): 8 · markets on board: 3428 · contracts joined: 1412 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 1212, 'NO_EDGE': 84, 'OK': 116}
families: {'period_winner': 72, 'period_spread': 48, 'period_total': 72, 'player_assists': 208, 'game_early_goal': 8, 'first_goal': 263, 'game_winner': 16, 'player_goals': 263, 'game_overtime': 8, 'player_points': 269, 'game_spread': 32, 'team_total': 80, 'game_total': 72, 'goalie_saves': 1}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 2026-10-01T23:00:00Z | T-6h | 0.617 | 0.383 | 0.172 | 5.83 | 3.28 | 2.55 | 160 (25/135) | PROJECTED/PROJECTED |
| TBL @ NYR | 2026-10-01T23:00:00Z | T-6h | 0.503 | 0.497 | 0.191 | 5.72 | 2.87 | 2.85 | 176 (25/151) | PROJECTED/PROJECTED |
| BUF @ CBJ | 2026-10-01T23:00:00Z | T-6h | 0.514 | 0.485 | 0.183 | 5.95 | 3.02 | 2.93 | 182 (25/157) | PROJECTED/PROBABLE |
| MIN @ NSH | 2026-10-02T00:00:00Z | T-6h | 0.462 | 0.538 | 0.171 | 6.56 | 3.16 | 3.40 | 176 (25/151) | CONFIRMED/PROJECTED |
| SEA @ CGY | 2026-10-02T01:00:00Z | T-6h | 0.525 | 0.474 | 0.181 | 6.10 | 3.13 | 2.97 | 200 (25/175) | CONFIRMED/PROJECTED |
| CHI @ UTA | 2026-10-02T01:30:00Z | T-6h | 0.625 | 0.374 | 0.168 | 6.14 | 3.47 | 2.67 | 161 (25/136) | PROJECTED/PROJECTED |
| EDM @ VAN | 2026-10-02T02:00:00Z | T-6h | 0.424 | 0.576 | 0.171 | 6.65 | 3.08 | 3.57 | 172 (25/147) | PROJECTED/PROJECTED |
| FLA @ SJS | 2026-10-02T02:00:00Z | T-6h | 0.530 | 0.470 | 0.166 | 6.52 | 3.35 | 3.16 | 185 (25/160) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT01EDMVAN-EDM2 | game_spread | 0.358 | 0.455 | 0.435 | 46 | 55 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3 | game_spread | 0.231 | 0.325 | 0.305 | 33 | 68 | no | +0.074 | OK |
| KXNHLGAME-26OCT01FLASJ-SJ | game_winner | 0.530 | 0.435 | 0.454 | 44 | 57 | yes | +0.073 | OK |
| KXNHLGAME-26OCT01FLASJ-FLA | game_winner | 0.470 | 0.565 | 0.546 | 57 | 44 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB4 | team_total | 0.331 | 0.430 | 0.409 | 44 | 58 | no | +0.072 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA2 | game_spread | 0.266 | 0.355 | 0.336 | 36 | 65 | no | +0.069 | OK |
| KXNHLGAME-26OCT01EDMVAN-EDM | game_winner | 0.576 | 0.665 | 0.648 | 67 | 34 | no | +0.068 | OK |
| KXNHLGAME-26OCT01EDMVAN-VAN | game_winner | 0.424 | 0.335 | 0.352 | 34 | 67 | yes | +0.068 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ2 | game_spread | 0.315 | 0.235 | 0.250 | 24 | 77 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB3 | team_total | 0.553 | 0.640 | 0.623 | 65 | 37 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA3 | game_spread | 0.159 | 0.240 | 0.222 | 25 | 77 | no | +0.058 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB2 | game_spread | 0.268 | 0.345 | 0.329 | 35 | 66 | no | +0.056 | OK |
| KXNHLGAME-26OCT01TBNYR-NYR | game_winner | 0.503 | 0.425 | 0.440 | 43 | 58 | yes | +0.056 | OK |
| KXNHLGAME-26OCT01TBNYR-TB | game_winner | 0.497 | 0.575 | 0.560 | 58 | 43 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB3 | game_spread | 0.157 | 0.225 | 0.210 | 23 | 78 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3 | team_total | 0.657 | 0.585 | 0.600 | 59 | 42 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB5 | team_total | 0.162 | 0.230 | 0.215 | 24 | 78 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ5 | team_total | 0.255 | 0.185 | 0.198 | 20 | 83 | yes | +0.044 | OK |
| KXNHLTOTAL-26OCT01TBNYR-4 | game_total | 0.808 | 0.865 | 0.855 | 87 | 14 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT01TBNYR-6 | game_total | 0.479 | 0.545 | 0.532 | 55 | 46 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT01MINNSH-7 | game_total | 0.510 | 0.445 | 0.458 | 45 | 56 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ4 | team_total | 0.438 | 0.370 | 0.383 | 38 | 64 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN2 | game_spread | 0.229 | 0.175 | 0.185 | 18 | 83 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN3 | team_total | 0.595 | 0.525 | 0.539 | 54 | 49 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB2 | team_total | 0.772 | 0.835 | 0.824 | 85 | 18 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN4 | team_total | 0.382 | 0.315 | 0.328 | 33 | 70 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT01TBNYR-5 | game_total | 0.711 | 0.770 | 0.759 | 78 | 24 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT01TBNYR-8 | game_total | 0.193 | 0.245 | 0.234 | 25 | 76 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT01MINNSH-8 | game_total | 0.307 | 0.250 | 0.261 | 26 | 76 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT01MINNSH-9 | game_total | 0.224 | 0.175 | 0.184 | 18 | 83 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT01TBNYR-7 | game_total | 0.370 | 0.430 | 0.418 | 44 | 58 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT01MINNSH-6 | game_total | 0.620 | 0.560 | 0.572 | 57 | 45 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT01TBNYR-NYR2 | game_spread | 0.274 | 0.225 | 0.234 | 23 | 78 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH5 | team_total | 0.221 | 0.170 | 0.179 | 18 | 84 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 | team_total | 0.492 | 0.555 | 0.543 | 57 | 46 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 | team_total | 0.403 | 0.465 | 0.452 | 48 | 55 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM5 | team_total | 0.295 | 0.355 | 0.343 | 37 | 66 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA3 | team_total | 0.616 | 0.675 | 0.664 | 69 | 34 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM3 | team_total | 0.698 | 0.750 | 0.740 | 76 | 26 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF4 | team_total | 0.345 | 0.400 | 0.389 | 41 | 61 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH3 | team_total | 0.615 | 0.555 | 0.567 | 57 | 46 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB6 | team_total | 0.066 | 0.110 | 0.099 | 12 | 90 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ3 | game_spread | 0.197 | 0.155 | 0.163 | 16 | 85 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN5 | team_total | 0.206 | 0.155 | 0.164 | 17 | 86 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA3 | game_spread | 0.259 | 0.305 | 0.295 | 31 | 70 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN3 | game_spread | 0.132 | 0.095 | 0.102 | 10 | 91 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-5 | game_total | 0.743 | 0.785 | 0.777 | 79 | 22 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-7 | game_total | 0.408 | 0.455 | 0.445 | 46 | 55 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-6 | game_total | 0.518 | 0.565 | 0.556 | 57 | 44 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH4 | team_total | 0.401 | 0.345 | 0.356 | 36 | 67 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT01PHINJ-6 | game_total | 0.499 | 0.545 | 0.536 | 55 | 46 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT01PHINJ-7 | game_total | 0.382 | 0.425 | 0.416 | 43 | 58 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN2 | team_total | 0.803 | 0.760 | 0.769 | 77 | 25 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ2 | team_total | 0.840 | 0.795 | 0.805 | 81 | 22 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT01TBNYR-9 | game_total | 0.131 | 0.170 | 0.162 | 18 | 84 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA5 | team_total | 0.218 | 0.265 | 0.255 | 28 | 75 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT01MINNSH-10 | game_total | 0.114 | 0.080 | 0.086 | 9 | 93 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT01BUFCBJ-BUF3 | game_spread | 0.152 | 0.185 | 0.178 | 19 | 82 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN6 | team_total | 0.092 | 0.060 | 0.065 | 7 | 95 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF3 | team_total | 0.567 | 0.610 | 0.601 | 62 | 40 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ6 | team_total | 0.122 | 0.080 | 0.087 | 10 | 94 | yes | +0.016 | OK |
| KXNHLGAME-26OCT01MINNSH-MIN | game_winner | 0.538 | 0.575 | 0.568 | 58 | 43 | no | +0.015 | OK |
| KXNHLGAME-26OCT01MINNSH-NSH | game_winner | 0.462 | 0.425 | 0.432 | 43 | 58 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT01PHINJ-5 | game_total | 0.722 | 0.760 | 0.753 | 77 | 25 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA4 | team_total | 0.468 | 0.510 | 0.502 | 52 | 50 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF5 | team_total | 0.174 | 0.215 | 0.206 | 23 | 80 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH6 | team_total | 0.099 | 0.070 | 0.075 | 8 | 94 | yes | +0.014 | OK |
| KXNHLSPREAD-26OCT01PHINJ-PHI3 | game_spread | 0.099 | 0.125 | 0.119 | 13 | 88 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA2 | team_total | 0.817 | 0.855 | 0.848 | 87 | 16 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH2 | team_total | 0.815 | 0.775 | 0.783 | 79 | 24 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-8 | game_total | 0.224 | 0.255 | 0.249 | 26 | 75 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT01PHINJ-4 | game_total | 0.818 | 0.850 | 0.844 | 86 | 16 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA2 | game_spread | 0.400 | 0.435 | 0.428 | 44 | 57 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA6 | team_total | 0.100 | 0.130 | 0.124 | 14 | 88 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT01PHINJ-PHI4 | team_total | 0.264 | 0.300 | 0.292 | 31 | 71 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT01MINNSH-NSH2 | game_spread | 0.264 | 0.235 | 0.241 | 24 | 77 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT01SEACGY-CGY5 | team_total | 0.212 | 0.180 | 0.186 | 19 | 83 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT01MINNSH-5 | game_total | 0.812 | 0.780 | 0.787 | 79 | 23 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM6 | team_total | 0.150 | 0.180 | 0.174 | 19 | 83 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT01PHINJ-8 | game_total | 0.209 | 0.235 | 0.230 | 24 | 77 | no | +0.009 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 0.617 | 0.560 | 0.172 | 0.221 | 5.83 | 5.80 | 0.987/0.991 | KXNHLGAME-26OCT01PHINJ-NJ -0.057 |
| TBL @ NYR | 0.503 | 0.516 | 0.191 | 0.227 | 5.72 | 6.02 | 0.958/0.957 | KXNHLTOTAL-26OCT01TBNYR-7 +0.054 |
| BUF @ CBJ | 0.514 | 0.552 | 0.183 | 0.216 | 5.95 | 6.17 | 0.964/1.000 | KXNHLTEAMTOTAL-26OCT01BUFCBJ-CBJ4 +0.058 |
| MIN @ NSH | 0.462 | 0.478 | 0.171 | 0.219 | 6.56 | 6.53 | 1.004/1.003 | KXNHLSPREAD-26OCT01MINNSH-MIN2 -0.022 |
| SEA @ CGY | 0.525 | 0.512 | 0.181 | 0.225 | 6.10 | 6.12 | 1.005/1.005 | KXNHLSPREAD-26OCT01SEACGY-CGY2 -0.016 |
| CHI @ UTA | 0.625 | 0.649 | 0.168 | 0.199 | 6.14 | 6.49 | 0.992/1.003 | KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA4 +0.068 |
| EDM @ VAN | 0.424 | 0.450 | 0.171 | 0.213 | 6.65 | 6.51 | 1.021/0.994 | KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 -0.032 |
| FLA @ SJS | 0.530 | 0.556 | 0.166 | 0.219 | 6.52 | 6.42 | 1.034/0.998 | KXNHLSPREAD-26OCT01FLASJ-FLA2 -0.030 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 23 recommended · full analysis in card.md / packet.json `thesis_card`

- Cody Glass: 1+ goals YES @ 11c · p 0.1593 (adj 0.1445) · $5.12 · thesis NJD:OFFENSE_4PLUS
- Noel Acciari: 1+ goals YES @ 9c · p 0.1198 (adj 0.1111) · $2.85 · thesis PHI:OFFENSE_4PLUS
- Anthony Mantha: 1+ assists NO @ 74c · p 0.8606 (adj 0.7725) · $14.29 · thesis NJD:SUPPRESSED
- Christian Dvorak: 1+ goals YES @ 15c · p 0.1828 (adj 0.1734) · $2.93 · thesis PHI:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 54c · p 0.7421 (adj 0.5912) · $14.29 · thesis TBL:SUPPRESSED
- Tye Kartye: 1+ goals YES @ 10c · p 0.1352 (adj 0.1239) · $2.98 · thesis NYR:OFFENSE_4PLUS
- Tampa Bay wins NO @ 43c · p 0.5136 (adj 0.4693) · $5.08 · thesis NYR:WINS
- Pavel Dorofeyev: 1+ assists NO @ 74c · p 0.8381 (adj 0.7646) · $12.33 · thesis NYR:SUPPRESSED
- Owen Power: 1+ goals NO @ 90c · p 0.9329 (adj 0.9222) · $14.29 · thesis BUF:SUPPRESSED
- Sean Monahan: 1+ goals YES @ 20c · p 0.2354 (adj 0.2228) · $2.52 · thesis CBJ:OFFENSE_4PLUS
- Tage Thompson: 1+ assists NO @ 59c · p 0.6663 (adj 0.6206) · $6.32 · thesis BUF:SUPPRESSED
- Ryan Hartman: 1+ goals YES @ 23c · p 0.2714 (adj 0.256) · $3.09 · thesis MIN:OFFENSE_4PLUS
- Adam Klapka: 1+ goals YES @ 10c · p 0.1308 (adj 0.1206) · $2.64 · thesis CGY:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 12c · p 0.17 (adj 0.155) · $5.18 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 62c · p 0.7413 (adj 0.6527) · $9.53 · thesis CHI:SUPPRESSED
- Vancouver wins by over 2.5 goals YES @ 10c · p 0.1485 (adj 0.1217) · $1.81 · thesis VAN:WINS_BY_2PLUS
- Drew O'Connor: 1+ goals YES @ 17c · p 0.2134 (adj 0.1963) · $3.02 · thesis VAN:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 11c · p 0.1405 (adj 0.1291) · $2.07 · thesis VAN:OFFENSE_4PLUS
- Leon Draisaitl: 2+ points NO @ 55c · p 0.7424 (adj 0.5831) · $6.85 · thesis EDM:SUPPRESSED
- San Jose wins by over 1.5 goals YES @ 24c · p 0.3336 (adj 0.2843) · $4.55 · thesis SJS:WINS_BY_2PLUS
- Aleksander Barkov: 1+ assists NO @ 52c · p 0.6974 (adj 0.5723) · $11.87 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 77c · p 0.8522 (adj 0.8061) · $13.87 · thesis SJS:WINS
- Brady Tkachuk: 1+ assists NO @ 63c · p 0.749 (adj 0.6586) · $2.5 · thesis FLA:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ NJD** · priced 109/109 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.74, exp saves 21.77 (sd 5.92), pull risk 0.045
- PHI net: Joseph Woll (PROJECTED) exp shots 28.45, exp saves 24.52 (sd 6.69), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anthony Mantha: 1+ assists | 0.139 | 0.275 | 29/74 | +0.107 | STANDARD |
| Luke Evangelista: 1+ assists | 0.216 | 0.335 | 35/68 | +0.089 | STANDARD |
| Anthony Mantha: 1+ points | 0.325 | 0.440 | 46/58 | +0.078 | STANDARD |
| Luke Evangelista: 1+ points | 0.360 | 0.475 | 49/54 | +0.083 | STANDARD |
| Porter Martone: 1+ points | 0.378 | 0.455 | 47/56 | +0.045 | STANDARD |
| Luke Evangelista: 2+ points | 0.077 | 0.145 | 17/88 | +0.036 | STANDARD |

**TBL @ NYR** · priced 125/125 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (PROJECTED) exp shots 28.0, exp saves 24.19 (sd 6.55), pull risk 0.055
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 24.5, exp saves 21.19 (sd 5.96), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ points | 0.649 | 0.405 | 72/91 | -0.085 | STANDARD |
| John Carlson: 1+ assists | 0.258 | 0.490 | 52/54 | +0.185 | STANDARD |
| John Carlson: 1+ points | 0.341 | 0.560 | 57/45 | +0.192 | STANDARD |
| Gabe Perreault: 1+ assists | 0.323 | 0.120 | 23/99 | +0.081 | STANDARD |
| Gabe Perreault: 1+ points | 0.466 | 0.345 | 36/67 | +0.090 | STANDARD |
| John Carlson: 2+ points | 0.064 | 0.180 | 23/87 | +0.058 | STANDARD |

**BUF @ CBJ** · priced 129/131 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 27.66, exp saves 24.14 (sd 6.44), pull risk 0.054
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 28.58, exp saves 24.61 (sd 6.66), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie Coyle: 1+ goals | 0.271 | 0.170 | 23/89 | +0.028 | STANDARD |
| Charlie Coyle: 2+ points | 0.199 | 0.105 | 17/96 | +0.019 | STANDARD |
| Tage Thompson: 1+ assists | 0.334 | 0.425 | 44/59 | +0.059 | STANDARD |
| Charlie Coyle: 1+ points | 0.553 | 0.465 | 48/55 | +0.056 | STANDARD |
| Tage Thompson: 1+ points | 0.538 | 0.625 | 64/39 | +0.055 | STANDARD |
| Zach Werenski: 2+ points | 0.253 | 0.175 | 30/95 | -0.062 | STANDARD |

**MIN @ NSH** · priced 123/125 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 29.81, exp saves 25.53 (sd 7.12), pull risk 0.076
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 25.29 (sd 6.82), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Max Shabanov: 1+ points | 0.376 | 0.245 | 48/99 | -0.122 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.358 | 0.235 | 26/79 | +0.085 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.487 | 0.380 | 40/64 | +0.070 | STANDARD |
| Steven Stamkos: 2+ points | 0.225 | 0.130 | 21/95 | +0.003 | STANDARD |
| Ryan O'Reilly: 2+ points | 0.241 | 0.150 | 23/93 | -0.002 | STANDARD |
| Matt Boldy: 1+ goals | 0.348 | 0.275 | 35/80 | -0.017 | STANDARD |

**SEA @ CGY** · priced 149/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.7, exp saves 24.08 (sd 6.54), pull risk 0.055
- SEA net: Joey Daccord (PROJECTED) exp shots 28.94, exp saves 24.93 (sd 6.8), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Maxim Tsyplakov: 2+ points | 0.039 | 0.425 | 84/99 | -0.030 | STANDARD |
| Connor Zary: 1+ points | 0.421 | 0.220 | 38/94 | +0.024 | STANDARD |
| Adam Klapka: 1+ points | 0.304 | 0.135 | 26/99 | +0.030 | STANDARD |
| Zach Whitecloud: 1+ points | 0.291 | 0.160 | 27/95 | +0.008 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.255 | 0.125 | 24/99 | +0.002 | STANDARD |
| Kevin Bahl: 1+ points | 0.254 | 0.135 | 26/99 | -0.019 | STANDARD |

**CHI @ UTA** · priced 108/110 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 24.86, exp saves 21.82 (sd 6.09), pull risk 0.05
- CHI net: Spencer Knight (PROJECTED) exp shots 29.49, exp saves 24.9 (sd 7.06), pull risk 0.09

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.259 | 0.395 | 41/62 | +0.105 | STANDARD |
| Nick Schmaltz: 1+ goals | 0.326 | 0.195 | 31/92 | +0.001 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.228 | 0.355 | 38/67 | +0.087 | STANDARD |
| Lawson Crouse: 1+ goals | 0.263 | 0.140 | 23/95 | +0.020 | STANDARD |
| Dylan Guenther: 1+ goals | 0.331 | 0.210 | 37/95 | -0.055 | STANDARD |
| Clayton Keller: 1+ goals | 0.325 | 0.205 | 33/92 | -0.020 | STANDARD |

**EDM @ VAN** · priced 121/121 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.37, exp saves 26.02 (sd 7.13), pull risk 0.074
- EDM net: Devon Levi (PROJECTED) exp shots 26.05, exp saves 22.59 (sd 6.28), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ points | 0.734 | 0.460 | 85/93 | -0.125 | STANDARD |
| Evan Bouchard: 1+ points | 0.666 | 0.450 | 77/87 | -0.116 | STANDARD |
| Leon Draisaitl: 2+ points | 0.258 | 0.470 | 49/55 | +0.175 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.404 | 0.600 | 63/43 | +0.149 | STANDARD |
| Leon Draisaitl: 1+ points | 0.625 | 0.435 | 80/93 | -0.186 | STANDARD |
| Connor McDavid: 2+ points | 0.385 | 0.545 | 57/48 | +0.117 | STANDARD |

**FLA @ SJS** · priced 134/134 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.16, exp saves 23.7 (sd 6.43), pull risk 0.06
- FLA net: Akira Schmid (PROJECTED) exp shots 26.2, exp saves 22.43 (sd 6.35), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ points | 0.680 | 0.395 | 74/95 | -0.074 | STANDARD |
| Aleksander Barkov: 1+ assists | 0.303 | 0.495 | 51/52 | +0.160 | STANDARD |
| Alexander Wennberg: 1+ points | 0.462 | 0.270 | 48/94 | -0.035 | STANDARD |
| Aleksander Barkov: 1+ points | 0.447 | 0.635 | 66/39 | +0.147 | STANDARD |
| Alexander Wennberg: 1+ assists | 0.331 | 0.185 | 36/99 | -0.045 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.251 | 0.390 | 41/63 | +0.103 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
