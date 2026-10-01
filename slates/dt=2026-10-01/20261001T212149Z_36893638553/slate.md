# NHL slate 2026-10-01 — RESEARCH_ONLY

generated 2026-10-01T21:21:49Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 8 · simulated (not started): 8 · markets on board: 3446 · contracts joined: 1417 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 1217, 'NO_EDGE': 84, 'OK': 116}
families: {'period_winner': 72, 'period_spread': 48, 'period_total': 72, 'player_assists': 208, 'game_early_goal': 8, 'first_goal': 262, 'game_winner': 16, 'player_goals': 262, 'game_overtime': 8, 'player_points': 269, 'goalie_saves': 8, 'game_spread': 32, 'team_total': 80, 'game_total': 72}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 2026-10-01T23:00:00Z | T-90m | 0.627 | 0.373 | 0.174 | 5.85 | 3.32 | 2.53 | 161 (25/136) | CONFIRMED/CONFIRMED |
| TBL @ NYR | 2026-10-01T23:00:00Z | T-90m | 0.508 | 0.492 | 0.187 | 5.59 | 2.82 | 2.77 | 177 (25/152) | CONFIRMED/PROBABLE |
| BUF @ CBJ | 2026-10-01T23:00:00Z | T-90m | 0.516 | 0.484 | 0.182 | 5.89 | 3.00 | 2.90 | 181 (25/156) | PROBABLE/CONFIRMED |
| MIN @ NSH | 2026-10-02T00:00:00Z | T-90m | 0.462 | 0.538 | 0.171 | 6.56 | 3.16 | 3.40 | 176 (25/151) | CONFIRMED/PROJECTED |
| SEA @ CGY | 2026-10-02T01:00:00Z | T-3h | 0.525 | 0.474 | 0.181 | 6.10 | 3.13 | 2.97 | 201 (25/176) | CONFIRMED/PROJECTED |
| CHI @ UTA | 2026-10-02T01:30:00Z | T-3h | 0.627 | 0.373 | 0.175 | 6.14 | 3.47 | 2.66 | 162 (25/137) | PROBABLE/PROJECTED |
| EDM @ VAN | 2026-10-02T02:00:00Z | T-3h | 0.412 | 0.588 | 0.168 | 6.71 | 3.07 | 3.63 | 173 (25/148) | PROBABLE/CONFIRMED |
| FLA @ SJS | 2026-10-02T02:00:00Z | T-3h | 0.514 | 0.486 | 0.170 | 6.62 | 3.36 | 3.25 | 186 (25/161) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB4 | team_total | 0.311 | 0.425 | 0.401 | 43 | 58 | no | +0.091 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB3 | team_total | 0.533 | 0.640 | 0.619 | 65 | 37 | no | +0.081 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3 | game_spread | 0.241 | 0.325 | 0.307 | 33 | 68 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA3 | game_spread | 0.164 | 0.245 | 0.227 | 25 | 76 | no | +0.063 | OK |
| KXNHLGAME-26OCT01TBNYR-TB | game_winner | 0.492 | 0.575 | 0.559 | 58 | 43 | no | +0.061 | OK |
| KXNHLGAME-26OCT01TBNYR-NYR | game_winner | 0.508 | 0.425 | 0.441 | 43 | 58 | yes | +0.061 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB3 | game_spread | 0.148 | 0.225 | 0.208 | 23 | 78 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB2 | game_spread | 0.265 | 0.345 | 0.328 | 35 | 66 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB5 | team_total | 0.149 | 0.230 | 0.212 | 24 | 78 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT01TBNYR-4 | game_total | 0.793 | 0.865 | 0.853 | 87 | 14 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT01TBNYR-6 | game_total | 0.455 | 0.535 | 0.519 | 54 | 47 | no | +0.058 | OK |
| KXNHLGAME-26OCT01FLASJ-FLA | game_winner | 0.486 | 0.565 | 0.549 | 57 | 44 | no | +0.057 | OK |
| KXNHLGAME-26OCT01FLASJ-SJ | game_winner | 0.514 | 0.435 | 0.451 | 44 | 57 | yes | +0.057 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA2 | game_spread | 0.278 | 0.355 | 0.339 | 36 | 65 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ4 | team_total | 0.441 | 0.360 | 0.376 | 37 | 65 | yes | +0.055 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM2 | game_spread | 0.369 | 0.450 | 0.433 | 46 | 56 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT01TBNYR-5 | game_total | 0.694 | 0.765 | 0.752 | 77 | 24 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ2 | game_spread | 0.305 | 0.235 | 0.248 | 24 | 77 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB2 | team_total | 0.759 | 0.835 | 0.821 | 85 | 18 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT01TBNYR-7 | game_total | 0.342 | 0.415 | 0.400 | 42 | 59 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3 | team_total | 0.656 | 0.585 | 0.600 | 59 | 42 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN3 | team_total | 0.595 | 0.525 | 0.539 | 53 | 48 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ5 | team_total | 0.258 | 0.190 | 0.202 | 20 | 82 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF4 | team_total | 0.337 | 0.405 | 0.391 | 41 | 60 | no | +0.047 | OK |
| KXNHLGAME-26OCT01EDMVAN-EDM | game_winner | 0.588 | 0.655 | 0.642 | 66 | 35 | no | +0.047 | OK |
| KXNHLGAME-26OCT01EDMVAN-VAN | game_winner | 0.412 | 0.345 | 0.358 | 35 | 66 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT01MINNSH-7 | game_total | 0.510 | 0.445 | 0.458 | 45 | 56 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH5 | team_total | 0.221 | 0.165 | 0.175 | 17 | 84 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT01TBNYR-8 | game_total | 0.177 | 0.235 | 0.222 | 24 | 77 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH3 | team_total | 0.615 | 0.550 | 0.563 | 56 | 46 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN4 | team_total | 0.382 | 0.315 | 0.328 | 33 | 70 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH4 | team_total | 0.401 | 0.335 | 0.348 | 35 | 68 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN5 | team_total | 0.203 | 0.150 | 0.160 | 16 | 86 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-7 | game_total | 0.399 | 0.455 | 0.444 | 46 | 55 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA3 | game_spread | 0.261 | 0.315 | 0.304 | 32 | 69 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT01TBNYR-9 | game_total | 0.117 | 0.165 | 0.154 | 17 | 84 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT01MINNSH-8 | game_total | 0.307 | 0.255 | 0.265 | 26 | 75 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-6 | game_total | 0.509 | 0.565 | 0.554 | 57 | 44 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT01MINNSH-9 | game_total | 0.224 | 0.175 | 0.184 | 18 | 83 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ3 | game_spread | 0.192 | 0.145 | 0.154 | 15 | 86 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT01TBNYR-NYR2 | game_spread | 0.275 | 0.225 | 0.234 | 23 | 78 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN2 | game_spread | 0.223 | 0.175 | 0.184 | 18 | 83 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT01MINNSH-6 | game_total | 0.620 | 0.565 | 0.576 | 57 | 44 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ6 | team_total | 0.128 | 0.080 | 0.088 | 9 | 93 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF3 | team_total | 0.562 | 0.620 | 0.609 | 63 | 39 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT01MINNSH-10 | game_total | 0.114 | 0.075 | 0.082 | 8 | 93 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ2 | team_total | 0.839 | 0.790 | 0.801 | 80 | 22 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT01FLASJ-10 | game_total | 0.122 | 0.085 | 0.091 | 9 | 92 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT01PHINJ-PHI2 | team_total | 0.711 | 0.755 | 0.747 | 76 | 25 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA2 | game_spread | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT01FLASJ-8 | game_total | 0.319 | 0.275 | 0.283 | 28 | 73 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH2 | team_total | 0.815 | 0.770 | 0.780 | 78 | 24 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT01PHINJ-4 | game_total | 0.818 | 0.855 | 0.848 | 86 | 15 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-4 | game_total | 0.829 | 0.865 | 0.858 | 87 | 14 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-5 | game_total | 0.735 | 0.775 | 0.767 | 78 | 23 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA4 | team_total | 0.470 | 0.515 | 0.506 | 52 | 49 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT01FLASJ-9 | game_total | 0.234 | 0.195 | 0.202 | 20 | 81 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT01MINNSH-NSH2 | game_spread | 0.264 | 0.225 | 0.232 | 23 | 78 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 | team_total | 0.422 | 0.465 | 0.456 | 47 | 54 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-8 | game_total | 0.216 | 0.255 | 0.247 | 26 | 75 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA3 | team_total | 0.634 | 0.685 | 0.675 | 70 | 33 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN2 | team_total | 0.802 | 0.760 | 0.769 | 77 | 25 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF5 | team_total | 0.169 | 0.215 | 0.205 | 23 | 80 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT01PHINJ-PHI3 | game_spread | 0.093 | 0.125 | 0.118 | 13 | 88 | no | +0.019 | OK |
| KXNHLGAME-26OCT01CHIUTA-CHI | game_winner | 0.373 | 0.335 | 0.342 | 34 | 67 | yes | +0.017 | OK |
| KXNHLGAME-26OCT01CHIUTA-UTA | game_winner | 0.627 | 0.665 | 0.658 | 67 | 34 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT01BUFCBJ-BUF3 | game_spread | 0.153 | 0.185 | 0.178 | 19 | 82 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN6 | team_total | 0.091 | 0.060 | 0.065 | 7 | 95 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM3 | team_total | 0.711 | 0.750 | 0.742 | 76 | 26 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT01PHINJ-6 | game_total | 0.507 | 0.545 | 0.537 | 55 | 46 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB6 | team_total | 0.059 | 0.095 | 0.087 | 11 | 92 | no | +0.015 | OK |
| KXNHLGAME-26OCT01MINNSH-MIN | game_winner | 0.538 | 0.575 | 0.568 | 58 | 43 | no | +0.015 | OK |
| KXNHLGAME-26OCT01MINNSH-NSH | game_winner | 0.462 | 0.425 | 0.432 | 43 | 58 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA5 | team_total | 0.232 | 0.270 | 0.262 | 28 | 74 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH6 | team_total | 0.099 | 0.070 | 0.075 | 8 | 94 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA5 | team_total | 0.272 | 0.310 | 0.302 | 32 | 70 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT01PHINJ-5 | game_total | 0.724 | 0.755 | 0.749 | 76 | 25 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA3 | team_total | 0.683 | 0.720 | 0.713 | 73 | 29 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT01TBNYR-3 | game_total | 0.945 | 0.965 | 0.962 | 97 | 4 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT01MINNSH-MIN3 | game_spread | 0.206 | 0.235 | 0.229 | 24 | 77 | no | +0.012 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 0.627 | 0.561 | 0.174 | 0.228 | 5.85 | 5.79 | 0.984/0.990 | KXNHLGAME-26OCT01PHINJ-NJ -0.066 |
| TBL @ NYR | 0.508 | 0.524 | 0.187 | 0.220 | 5.59 | 5.93 | 0.934/0.951 | KXNHLTOTAL-26OCT01TBNYR-7 +0.067 |
| BUF @ CBJ | 0.516 | 0.557 | 0.182 | 0.218 | 5.89 | 6.16 | 0.955/1.002 | KXNHLTEAMTOTAL-26OCT01BUFCBJ-CBJ4 +0.058 |
| MIN @ NSH | 0.462 | 0.478 | 0.171 | 0.219 | 6.56 | 6.53 | 1.004/1.003 | KXNHLSPREAD-26OCT01MINNSH-MIN2 -0.022 |
| SEA @ CGY | 0.525 | 0.512 | 0.181 | 0.225 | 6.10 | 6.12 | 1.005/1.005 | KXNHLSPREAD-26OCT01SEACGY-CGY2 -0.016 |
| CHI @ UTA | 0.627 | 0.652 | 0.175 | 0.205 | 6.14 | 6.49 | 0.990/1.003 | KXNHLTOTAL-26OCT01CHIUTA-7 +0.064 |
| EDM @ VAN | 0.412 | 0.446 | 0.168 | 0.214 | 6.71 | 6.52 | 1.026/0.994 | KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 -0.040 |
| FLA @ SJS | 0.514 | 0.549 | 0.170 | 0.216 | 6.62 | 6.41 | 1.039/0.991 | KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 -0.049 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 30 recommended · full analysis in card.md / packet.json `thesis_card`

- Anthony Mantha: 1+ assists NO @ 73c · p 0.8598 (adj 0.7722) · $9.8 · thesis NJD:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 11c · p 0.1457 (adj 0.1355) · $2.38 · thesis PHI:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 12c · p 0.1534 (adj 0.1438) · $2.32 · thesis NJD:OFFENSE_4PLUS
- Noel Acciari: 1+ goals YES @ 9c · p 0.1176 (adj 0.1094) · $1.72 · thesis PHI:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 56c · p 0.7415 (adj 0.6138) · $8.48 · thesis TBL:SUPPRESSED
- Tampa Bay wins by over 1.5 goals NO @ 66c · p 0.7457 (adj 0.7004) · $7.55 · thesis NYR:WINS
- Pavel Dorofeyev: 1+ assists NO @ 77c · p 0.8424 (adj 0.7987) · $8.48 · thesis NYR:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 21c · p 0.273 (adj 0.256) · $5.11 · thesis CBJ:OFFENSE_4PLUS
- Noah Ostlund: 1+ goals NO @ 83c · p 0.8646 (adj 0.8547) · $9.8 · thesis BUF:SUPPRESSED
- Sean Monahan: 1+ goals YES @ 20c · p 0.2397 (adj 0.2273) · $2.4 · thesis CBJ:OFFENSE_4PLUS
- Tage Thompson: 1+ assists NO @ 60c · p 0.6797 (adj 0.6323) · $4.82 · thesis BUF:SUPPRESSED
- Nicolas Hague: 1+ goals YES @ 3c · p 0.052 (adj 0.0452) · $1.4 · thesis DIFFUSE
- Ryan O'Reilly: 1+ goals YES @ 25c · p 0.3042 (adj 0.2894) · $4.19 · thesis NSH:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 23c · p 0.2714 (adj 0.2598) · $2.74 · thesis MIN:OFFENSE_4PLUS
- Mavrik Bourque: 1+ goals YES @ 18c · p 0.2161 (adj 0.2058) · $2.25 · thesis NSH:OFFENSE_4PLUS
- Brandon Montour: 1+ goals NO @ 84c · p 0.8924 (adj 0.8768) · $9.8 · thesis SEA:SUPPRESSED
- Freddy Gaudreau: 1+ goals YES @ 10c · p 0.1359 (adj 0.1257) · $2.5 · thesis SEA:OFFENSE_4PLUS
- Adam Klapka: 1+ goals YES @ 10c · p 0.1308 (adj 0.1218) · $2.04 · thesis CGY:OFFENSE_4PLUS
- Morgan Frost: 1+ goals YES @ 24c · p 0.2766 (adj 0.2662) · $2.25 · thesis CGY:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 12c · p 0.1664 (adj 0.1535) · $3.54 · thesis CHI:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 21c · p 0.2593 (adj 0.2457) · $3.79 · thesis UTA:OFFENSE_4PLUS
- Anders Lee: 1+ goals YES @ 23c · p 0.2736 (adj 0.2615) · $3.16 · thesis UTA:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 62c · p 0.7454 (adj 0.6574) · $8.53 · thesis CHI:SUPPRESSED
- Connor McDavid: 1+ assists NO @ 31c · p 0.4762 (adj 0.3649) · $6.93 · thesis EDM:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 16c · p 0.2153 (adj 0.2002) · $4.29 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 21c · p 0.257 (adj 0.244) · $3.35 · thesis VAN:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 10c · p 0.1263 (adj 0.1185) · $2.05 · thesis EDM:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 15c · p 0.2154 (adj 0.1978) · $5.01 · thesis SJS:OFFENSE_4PLUS
- Florida wins by over 2.5 goals NO @ 76c · p 0.852 (adj 0.8035) · $9.8 · thesis SJS:WINS
- Aleksander Barkov: 1+ assists NO @ 52c · p 0.6916 (adj 0.5703) · $8.54 · thesis FLA:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ NJD** · priced 110/110 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 24.74, exp saves 21.75 (sd 5.93), pull risk 0.043
- PHI net: Joseph Woll (CONFIRMED) exp shots 28.45, exp saves 24.54 (sd 6.65), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ points | 0.362 | 0.505 | 52/51 | +0.111 | STANDARD |
| Luke Evangelista: 1+ assists | 0.219 | 0.355 | 36/65 | +0.115 | STANDARD |
| Anthony Mantha: 1+ assists | 0.140 | 0.275 | 28/73 | +0.116 | STANDARD |
| Anthony Mantha: 1+ points | 0.326 | 0.455 | 47/56 | +0.097 | STANDARD |
| Luke Evangelista: 2+ points | 0.076 | 0.175 | 19/84 | +0.074 | STANDARD |
| Anthony Mantha: 2+ points | 0.059 | 0.135 | 15/88 | +0.053 | STANDARD |

**TBL @ NYR** · priced 126/126 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (CONFIRMED) exp shots 28.0, exp saves 24.27 (sd 6.55), pull risk 0.055
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 24.5, exp saves 21.2 (sd 5.88), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.338 | 0.550 | 57/47 | +0.175 | STANDARD |
| John Carlson: 1+ assists | 0.259 | 0.455 | 47/56 | +0.164 | STANDARD |
| Gabe Perreault: 1+ points | 0.467 | 0.340 | 36/68 | +0.091 | STANDARD |
| Gabe Perreault: 1+ assists | 0.326 | 0.205 | 22/81 | +0.094 | STANDARD |
| Victor Hedman: 1+ points | 0.235 | 0.340 | 35/67 | +0.079 | STANDARD |
| Victor Hedman: 1+ assists | 0.178 | 0.275 | 29/74 | +0.068 | STANDARD |

**BUF @ CBJ** · priced 130/130 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROBABLE) exp shots 27.66, exp saves 24.13 (sd 6.52), pull risk 0.057
- BUF net: Ukko-Pekka Luukkonen (CONFIRMED) exp shots 28.58, exp saves 24.65 (sd 6.71), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jet Greaves: 26+ saves | 0.406 | 0.275 | 53/98 | -0.141 |  |
| Tage Thompson: 1+ assists | 0.320 | 0.415 | 43/60 | +0.063 | STANDARD |
| Charlie Coyle: 1+ points | 0.547 | 0.460 | 47/55 | +0.059 | STANDARD |
| Tage Thompson: 1+ points | 0.530 | 0.610 | 62/40 | +0.053 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.224 | 0.295 | 31/72 | +0.042 | STANDARD |
| Charlie Coyle: 1+ goals | 0.273 | 0.205 | 21/80 | +0.051 | STANDARD |

**MIN @ NSH** · priced 123/125 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 29.81, exp saves 25.53 (sd 7.12), pull risk 0.076
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 25.29 (sd 6.82), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonathan Marchessault: 1+ points | 0.487 | 0.375 | 39/64 | +0.080 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.358 | 0.250 | 27/77 | +0.074 | STANDARD |
| Max Shabanov: 1+ points | 0.376 | 0.455 | 49/58 | +0.027 | STANDARD |
| Juuse Saros: 26+ saves | 0.505 | 0.435 | 51/64 | -0.022 |  |
| Jonathan Marchessault: 2+ points | 0.153 | 0.090 | 11/93 | +0.036 | STANDARD |
| Steven Stamkos: 1+ assists | 0.391 | 0.330 | 34/68 | +0.035 | STANDARD |

**SEA @ CGY** · priced 150/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.7, exp saves 24.08 (sd 6.54), pull risk 0.055
- SEA net: Joey Daccord (PROJECTED) exp shots 28.94, exp saves 24.93 (sd 6.8), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Whitecloud: 1+ assists | 0.255 | 0.105 | 20/99 | +0.043 | STANDARD |
| Connor Zary: 1+ assists | 0.267 | 0.130 | 25/99 | +0.004 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.260 | 0.135 | 26/99 | -0.013 | STANDARD |
| Jared McCann: 1+ points | 0.447 | 0.555 | 57/46 | +0.076 | STANDARD |
| Kevin Bahl: 1+ assists | 0.211 | 0.125 | 24/99 | -0.042 | STANDARD |
| Jared McCann: 1+ assists | 0.269 | 0.355 | 37/66 | +0.055 | STANDARD |

**CHI @ UTA** · priced 111/111 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 24.86, exp saves 21.8 (sd 6.05), pull risk 0.051
- CHI net: Spencer Knight (PROJECTED) exp shots 29.49, exp saves 24.89 (sd 7.0), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Karel Vejmelka: 22+ saves | 0.513 | 0.280 | 54/98 | -0.044 |  |
| Patrick Kane: 1+ assists | 0.255 | 0.390 | 40/62 | +0.109 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.224 | 0.350 | 36/66 | +0.100 | STANDARD |
| Frank Nazar: 1+ assists | 0.334 | 0.215 | 23/80 | +0.091 | STANDARD |
| Frank Nazar: 1+ points | 0.472 | 0.365 | 38/65 | +0.075 | STANDARD |
| Patrick Kane: 1+ points | 0.436 | 0.525 | 54/49 | +0.056 | STANDARD |

**EDM @ VAN** · priced 115/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROBABLE) exp shots 30.37, exp saves 25.96 (sd 7.2), pull risk 0.076
- EDM net: Devon Levi (CONFIRMED) exp shots 26.05, exp saves 22.59 (sd 6.28), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.524 | 0.695 | 70/31 | +0.151 | STANDARD |
| Leon Draisaitl: 2+ points | 0.309 | 0.475 | 50/55 | +0.124 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.439 | 0.595 | 60/41 | +0.134 | STANDARD |
| Connor McDavid: 2+ points | 0.392 | 0.545 | 56/47 | +0.121 | STANDARD |
| Connor McDavid: 2+ assists | 0.169 | 0.315 | 32/69 | +0.126 | STANDARD |
| Mattias Ekholm: 1+ points | 0.458 | 0.330 | 35/69 | +0.092 | STANDARD |

**FLA @ SJS** · priced 135/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.16, exp saves 23.68 (sd 6.49), pull risk 0.061
- FLA net: Akira Schmid (CONFIRMED) exp shots 26.2, exp saves 22.42 (sd 6.35), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aleksander Barkov: 1+ assists | 0.308 | 0.495 | 51/52 | +0.154 | STANDARD |
| Aleksander Barkov: 1+ points | 0.459 | 0.630 | 64/38 | +0.144 | STANDARD |
| Brady Tkachuk: 1+ points | 0.466 | 0.625 | 64/39 | +0.128 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.251 | 0.385 | 40/63 | +0.102 | STANDARD |
| Aleksander Barkov: 2+ points | 0.122 | 0.235 | 27/80 | +0.066 | STANDARD |
| Sam Reinhart: 1+ points | 0.505 | 0.615 | 63/40 | +0.078 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
