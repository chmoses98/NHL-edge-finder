# NHL slate 2026-10-01 — RESEARCH_ONLY

generated 2026-10-01T18:51:49Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 8 · simulated (not started): 8 · markets on board: 3433 · contracts joined: 1417 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 1217, 'NO_EDGE': 86, 'OK': 114}
families: {'period_winner': 72, 'period_spread': 48, 'period_total': 72, 'player_assists': 208, 'game_early_goal': 8, 'first_goal': 262, 'game_winner': 16, 'player_goals': 262, 'game_overtime': 8, 'player_points': 269, 'goalie_saves': 8, 'game_spread': 32, 'team_total': 80, 'game_total': 72}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 2026-10-01T23:00:00Z | T-3h | 0.626 | 0.374 | 0.176 | 5.83 | 3.30 | 2.53 | 161 (25/136) | CONFIRMED/PROBABLE |
| TBL @ NYR | 2026-10-01T23:00:00Z | T-3h | 0.508 | 0.492 | 0.187 | 5.59 | 2.82 | 2.77 | 177 (25/152) | CONFIRMED/PROBABLE |
| BUF @ CBJ | 2026-10-01T23:00:00Z | T-3h | 0.516 | 0.484 | 0.182 | 5.89 | 3.00 | 2.90 | 181 (25/156) | PROBABLE/CONFIRMED |
| MIN @ NSH | 2026-10-02T00:00:00Z | T-3h | 0.462 | 0.538 | 0.171 | 6.56 | 3.16 | 3.40 | 176 (25/151) | CONFIRMED/PROJECTED |
| SEA @ CGY | 2026-10-02T01:00:00Z | T-6h | 0.525 | 0.474 | 0.181 | 6.10 | 3.13 | 2.97 | 201 (25/176) | CONFIRMED/PROJECTED |
| CHI @ UTA | 2026-10-02T01:30:00Z | T-6h | 0.627 | 0.373 | 0.175 | 6.14 | 3.47 | 2.66 | 162 (25/137) | PROBABLE/PROJECTED |
| EDM @ VAN | 2026-10-02T02:00:00Z | T-6h | 0.412 | 0.588 | 0.168 | 6.71 | 3.07 | 3.63 | 173 (25/148) | PROBABLE/PROJECTED |
| FLA @ SJS | 2026-10-02T02:00:00Z | T-6h | 0.514 | 0.486 | 0.167 | 6.60 | 3.35 | 3.25 | 186 (25/161) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB4 | team_total | 0.311 | 0.420 | 0.397 | 43 | 59 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB3 | team_total | 0.533 | 0.635 | 0.615 | 65 | 38 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3 | game_spread | 0.241 | 0.325 | 0.307 | 33 | 68 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM2 | game_spread | 0.369 | 0.455 | 0.437 | 46 | 55 | no | +0.063 | OK |
| KXNHLGAME-26OCT01TBNYR-TB | game_winner | 0.492 | 0.575 | 0.559 | 58 | 43 | no | +0.061 | OK |
| KXNHLGAME-26OCT01TBNYR-NYR | game_winner | 0.508 | 0.425 | 0.441 | 43 | 58 | yes | +0.061 | OK |
| KXNHLTOTAL-26OCT01TBNYR-7 | game_total | 0.342 | 0.425 | 0.408 | 43 | 58 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB3 | game_spread | 0.148 | 0.225 | 0.208 | 23 | 78 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB2 | game_spread | 0.265 | 0.345 | 0.328 | 35 | 66 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB5 | team_total | 0.149 | 0.225 | 0.208 | 23 | 78 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT01TBNYR-4 | game_total | 0.793 | 0.865 | 0.853 | 87 | 14 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT01TBNYR-6 | game_total | 0.455 | 0.535 | 0.519 | 54 | 47 | no | +0.058 | OK |
| KXNHLGAME-26OCT01FLASJ-FLA | game_winner | 0.486 | 0.565 | 0.549 | 57 | 44 | no | +0.057 | OK |
| KXNHLGAME-26OCT01FLASJ-SJ | game_winner | 0.514 | 0.435 | 0.451 | 44 | 57 | yes | +0.057 | OK |
| KXNHLGAME-26OCT01EDMVAN-EDM | game_winner | 0.588 | 0.665 | 0.650 | 67 | 34 | no | +0.057 | OK |
| KXNHLGAME-26OCT01EDMVAN-VAN | game_winner | 0.412 | 0.335 | 0.350 | 34 | 67 | yes | +0.057 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA3 | game_spread | 0.172 | 0.245 | 0.229 | 25 | 76 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ4 | team_total | 0.441 | 0.360 | 0.376 | 37 | 65 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA2 | game_spread | 0.280 | 0.355 | 0.339 | 36 | 65 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT01TBNYR-5 | game_total | 0.694 | 0.765 | 0.752 | 77 | 24 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ2 | game_spread | 0.304 | 0.235 | 0.248 | 24 | 77 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN3 | team_total | 0.595 | 0.520 | 0.535 | 53 | 49 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN4 | team_total | 0.382 | 0.310 | 0.324 | 32 | 70 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT01MINNSH-8 | game_total | 0.307 | 0.245 | 0.257 | 25 | 76 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3 | team_total | 0.651 | 0.585 | 0.598 | 59 | 42 | yes | +0.044 | OK |
| KXNHLTOTAL-26OCT01MINNSH-7 | game_total | 0.510 | 0.445 | 0.458 | 45 | 56 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ5 | team_total | 0.253 | 0.180 | 0.193 | 20 | 84 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH5 | team_total | 0.221 | 0.165 | 0.175 | 17 | 84 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT01TBNYR-8 | game_total | 0.177 | 0.235 | 0.222 | 24 | 77 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB2 | team_total | 0.759 | 0.830 | 0.817 | 85 | 19 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF4 | team_total | 0.337 | 0.400 | 0.387 | 41 | 61 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH4 | team_total | 0.401 | 0.335 | 0.348 | 35 | 68 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN5 | team_total | 0.203 | 0.145 | 0.155 | 16 | 87 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-7 | game_total | 0.399 | 0.455 | 0.444 | 46 | 55 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA3 | game_spread | 0.261 | 0.315 | 0.304 | 32 | 69 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT01TBNYR-9 | game_total | 0.117 | 0.165 | 0.154 | 17 | 84 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-6 | game_total | 0.509 | 0.565 | 0.554 | 57 | 44 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT01MINNSH-9 | game_total | 0.224 | 0.175 | 0.184 | 18 | 83 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-5 | game_total | 0.735 | 0.785 | 0.776 | 79 | 22 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT01TBNYR-NYR2 | game_spread | 0.275 | 0.225 | 0.234 | 23 | 78 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN2 | game_spread | 0.223 | 0.175 | 0.184 | 18 | 83 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT01MINNSH-6 | game_total | 0.620 | 0.565 | 0.576 | 57 | 44 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN2 | team_total | 0.802 | 0.755 | 0.765 | 76 | 25 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT01FLASJ-9 | game_total | 0.230 | 0.185 | 0.193 | 19 | 82 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH3 | team_total | 0.615 | 0.555 | 0.567 | 57 | 46 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ3 | game_spread | 0.187 | 0.145 | 0.153 | 15 | 86 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ6 | team_total | 0.124 | 0.075 | 0.083 | 9 | 94 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ2 | team_total | 0.838 | 0.785 | 0.797 | 80 | 23 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT01PHINJ-6 | game_total | 0.500 | 0.545 | 0.536 | 55 | 46 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF3 | team_total | 0.562 | 0.615 | 0.605 | 63 | 40 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN3 | game_spread | 0.126 | 0.095 | 0.101 | 10 | 91 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF5 | team_total | 0.169 | 0.215 | 0.205 | 23 | 80 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT01MINNSH-10 | game_total | 0.114 | 0.080 | 0.086 | 9 | 93 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 | team_total | 0.505 | 0.550 | 0.541 | 56 | 46 | no | +0.018 | OK |
| KXNHLGAME-26OCT01CHIUTA-CHI | game_winner | 0.373 | 0.335 | 0.342 | 34 | 67 | yes | +0.017 | OK |
| KXNHLGAME-26OCT01CHIUTA-UTA | game_winner | 0.627 | 0.665 | 0.658 | 67 | 34 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT01BUFCBJ-BUF3 | game_spread | 0.153 | 0.185 | 0.178 | 19 | 82 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN6 | team_total | 0.091 | 0.055 | 0.061 | 7 | 96 | yes | +0.016 | OK |
| KXNHLSPREAD-26OCT01PHINJ-PHI3 | game_spread | 0.097 | 0.125 | 0.119 | 13 | 88 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB6 | team_total | 0.059 | 0.090 | 0.083 | 10 | 92 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA2 | game_spread | 0.398 | 0.435 | 0.427 | 44 | 57 | no | +0.015 | OK |
| KXNHLGAME-26OCT01MINNSH-MIN | game_winner | 0.538 | 0.575 | 0.568 | 58 | 43 | no | +0.015 | OK |
| KXNHLGAME-26OCT01MINNSH-NSH | game_winner | 0.462 | 0.425 | 0.432 | 43 | 58 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH6 | team_total | 0.099 | 0.065 | 0.071 | 8 | 95 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH2 | team_total | 0.815 | 0.780 | 0.787 | 79 | 23 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA4 | team_total | 0.470 | 0.520 | 0.510 | 54 | 50 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT01FLASJ-10 | game_total | 0.119 | 0.090 | 0.095 | 10 | 92 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-MIN6 | team_total | 0.129 | 0.100 | 0.105 | 11 | 91 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA3 | team_total | 0.683 | 0.715 | 0.709 | 72 | 29 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-4 | game_total | 0.829 | 0.865 | 0.858 | 88 | 15 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT01TBNYR-3 | game_total | 0.945 | 0.965 | 0.962 | 97 | 4 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT01PHINJ-5 | game_total | 0.725 | 0.755 | 0.749 | 76 | 25 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 | team_total | 0.421 | 0.460 | 0.452 | 47 | 55 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT01FLASJ-8 | game_total | 0.316 | 0.280 | 0.287 | 29 | 73 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT01PHINJ-4 | game_total | 0.819 | 0.850 | 0.844 | 86 | 16 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-8 | game_total | 0.216 | 0.245 | 0.239 | 25 | 76 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA2 | team_total | 0.830 | 0.860 | 0.854 | 87 | 15 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-9 | game_total | 0.149 | 0.180 | 0.173 | 19 | 83 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT01MINNSH-NSH2 | game_spread | 0.264 | 0.230 | 0.237 | 24 | 78 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT01SEACGY-CGY5 | team_total | 0.212 | 0.180 | 0.186 | 19 | 83 | yes | +0.011 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 0.626 | 0.560 | 0.176 | 0.221 | 5.83 | 5.79 | 0.984/0.991 | KXNHLGAME-26OCT01PHINJ-PHI +0.066 |
| TBL @ NYR | 0.508 | 0.524 | 0.187 | 0.220 | 5.59 | 5.93 | 0.934/0.951 | KXNHLTOTAL-26OCT01TBNYR-7 +0.067 |
| BUF @ CBJ | 0.516 | 0.557 | 0.182 | 0.218 | 5.89 | 6.16 | 0.955/1.002 | KXNHLTEAMTOTAL-26OCT01BUFCBJ-CBJ4 +0.058 |
| MIN @ NSH | 0.462 | 0.478 | 0.171 | 0.219 | 6.56 | 6.53 | 1.004/1.003 | KXNHLSPREAD-26OCT01MINNSH-MIN2 -0.022 |
| SEA @ CGY | 0.525 | 0.512 | 0.181 | 0.225 | 6.10 | 6.12 | 1.005/1.005 | KXNHLSPREAD-26OCT01SEACGY-CGY2 -0.016 |
| CHI @ UTA | 0.627 | 0.652 | 0.175 | 0.205 | 6.14 | 6.49 | 0.990/1.003 | KXNHLTOTAL-26OCT01CHIUTA-7 +0.064 |
| EDM @ VAN | 0.412 | 0.449 | 0.168 | 0.210 | 6.71 | 6.53 | 1.026/0.994 | KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 -0.041 |
| FLA @ SJS | 0.514 | 0.552 | 0.167 | 0.215 | 6.60 | 6.44 | 1.039/0.998 | KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 -0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 27 recommended · full analysis in card.md / packet.json `thesis_card`

- Sean Couturier: 1+ goals YES @ 11c · p 0.152 (adj 0.139) · $2.87 · thesis PHI:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 12c · p 0.1528 (adj 0.1433) · $2.15 · thesis NJD:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 72c · p 0.7688 (adj 0.7541) · $9.5 · thesis NJD:SUPPRESSED
- Porter Martone: 1+ goals NO @ 77c · p 0.8106 (adj 0.7979) · $9.44 · thesis PHI:SUPPRESSED
- New York R wins YES @ 43c · p 0.5246 (adj 0.4798) · $6.4 · thesis NYR:WINS
- Pavel Dorofeyev: 1+ assists NO @ 76c · p 0.8424 (adj 0.7937) · $9.1 · thesis NYR:SUPPRESSED
- Victor Hedman: 1+ assists NO @ 71c · p 0.8218 (adj 0.7459) · $9.1 · thesis TBL:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 20c · p 0.273 (adj 0.251) · $5.75 · thesis CBJ:OFFENSE_4PLUS
- Sean Monahan: 1+ goals YES @ 20c · p 0.2397 (adj 0.2273) · $2.35 · thesis CBJ:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 65c · p 0.6906 (adj 0.6792) · $4.54 · thesis BUF:SUPPRESSED
- Ryan O'Reilly: 1+ goals YES @ 25c · p 0.3042 (adj 0.2844) · $2.95 · thesis NSH:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 23c · p 0.2714 (adj 0.2598) · $2.75 · thesis MIN:OFFENSE_4PLUS
- Nashville over 4.5 goals scored YES @ 17c · p 0.2233 (adj 0.1941) · $1.25 · thesis NSH:OFFENSE_4PLUS
- Jonathan Marchessault: 1+ assists YES @ 26c · p 0.3582 (adj 0.2846) · $1.03 · thesis NSH:OFFENSE_4PLUS
- Brandon Montour: 1+ goals NO @ 84c · p 0.8928 (adj 0.8759) · $9.84 · thesis SEA:SUPPRESSED
- Jacob Melanson: 1+ goals YES @ 9c · p 0.1227 (adj 0.112) · $2.02 · thesis SEA:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 12c · p 0.1664 (adj 0.1535) · $3.46 · thesis CHI:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 66c · p 0.7762 (adj 0.6942) · $8.54 · thesis UTA:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 22c · p 0.2591 (adj 0.2468) · $2.55 · thesis UTA:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 63c · p 0.7454 (adj 0.6606) · $6.16 · thesis CHI:SUPPRESSED
- Leon Draisaitl: 1+ goals NO @ 54c · p 0.6332 (adj 0.6087) · $8.75 · thesis EDM:SUPPRESSED
- Edmonton wins by over 2.5 goals NO @ 68c · p 0.7735 (adj 0.7243) · $8.89 · thesis VAN:WINS
- Connor McDavid: 2+ assists NO @ 69c · p 0.8059 (adj 0.7273) · $6.01 · thesis EDM:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 15c · p 0.2227 (adj 0.2033) · $4.74 · thesis SJS:OFFENSE_4PLUS
- Florida wins by over 2.5 goals NO @ 76c · p 0.8498 (adj 0.8024) · $8.88 · thesis SJS:WINS
- San Jose wins by over 1.5 goals YES @ 24c · p 0.3304 (adj 0.2827) · $2.1 · thesis SJS:WINS_BY_2PLUS
- Aleksander Barkov: 1+ goals NO @ 73c · p 0.7893 (adj 0.772) · $8.88 · thesis FLA:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ NJD** · priced 110/110 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 24.74, exp saves 21.77 (sd 6.0), pull risk 0.043
- PHI net: Joseph Woll (PROBABLE) exp shots 28.45, exp saves 24.56 (sd 6.6), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ points | 0.362 | 0.495 | 52/53 | +0.091 | STANDARD |
| Jake Allen: 23+ saves | 0.439 | 0.310 | 54/92 | -0.119 |  |
| Anthony Mantha: 1+ points | 0.327 | 0.455 | 47/56 | +0.096 | STANDARD |
| Luke Evangelista: 1+ assists | 0.223 | 0.350 | 36/66 | +0.101 | STANDARD |
| Anthony Mantha: 1+ assists | 0.141 | 0.265 | 28/75 | +0.096 | STANDARD |
| Porter Martone: 1+ points | 0.378 | 0.455 | 47/56 | +0.044 | STANDARD |

**TBL @ NYR** · priced 126/126 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (CONFIRMED) exp shots 28.0, exp saves 24.27 (sd 6.55), pull risk 0.055
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 24.5, exp saves 21.2 (sd 5.88), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.338 | 0.540 | 56/48 | +0.165 | STANDARD |
| John Carlson: 1+ assists | 0.259 | 0.455 | 49/58 | +0.144 | STANDARD |
| Igor Shesterkin: 26+ saves | 0.416 | 0.270 | 52/98 | -0.121 |  |
| Gabe Perreault: 1+ assists | 0.326 | 0.200 | 22/82 | +0.094 | STANDARD |
| Gabe Perreault: 1+ points | 0.467 | 0.350 | 37/67 | +0.081 | STANDARD |
| Victor Hedman: 1+ assists | 0.178 | 0.295 | 30/71 | +0.097 | STANDARD |

**BUF @ CBJ** · priced 130/130 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROBABLE) exp shots 27.66, exp saves 24.13 (sd 6.52), pull risk 0.057
- BUF net: Ukko-Pekka Luukkonen (CONFIRMED) exp shots 28.58, exp saves 24.65 (sd 6.71), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jet Greaves: 26+ saves | 0.406 | 0.275 | 53/98 | -0.141 |  |
| Charlie Coyle: 1+ points | 0.547 | 0.455 | 47/56 | +0.059 | STANDARD |
| Charlie Coyle: 1+ goals | 0.273 | 0.185 | 20/83 | +0.062 | STANDARD |
| Tage Thompson: 1+ assists | 0.320 | 0.405 | 43/62 | +0.043 | STANDARD |
| Tage Thompson: 1+ points | 0.530 | 0.615 | 63/40 | +0.053 | STANDARD |
| Charlie Coyle: 2+ points | 0.190 | 0.115 | 16/93 | +0.021 | STANDARD |

**MIN @ NSH** · priced 123/125 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 29.81, exp saves 25.53 (sd 7.12), pull risk 0.076
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 25.29 (sd 6.82), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Juuse Saros: 26+ saves | 0.505 | 0.295 | 51/92 | -0.022 |  |
| Jonathan Marchessault: 1+ points | 0.487 | 0.370 | 39/65 | +0.080 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.358 | 0.245 | 26/77 | +0.085 | STANDARD |
| Max Shabanov: 1+ points | 0.376 | 0.485 | 50/53 | +0.077 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.304 | 0.225 | 25/80 | +0.041 | STANDARD |
| Ryan O'Reilly: 2+ points | 0.241 | 0.165 | 21/88 | +0.019 | STANDARD |

**SEA @ CGY** · priced 150/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.7, exp saves 24.08 (sd 6.54), pull risk 0.055
- SEA net: Joey Daccord (PROJECTED) exp shots 28.94, exp saves 24.93 (sd 6.8), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dustin Wolf: 24+ saves | 0.527 | 0.280 | 55/99 | -0.041 |  |
| Adam Klapka: 1+ points | 0.304 | 0.130 | 23/97 | +0.061 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.255 | 0.105 | 20/99 | +0.043 | STANDARD |
| Connor Zary: 1+ assists | 0.267 | 0.130 | 25/99 | +0.004 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.260 | 0.135 | 26/99 | -0.013 | STANDARD |
| Kevin Bahl: 1+ assists | 0.211 | 0.105 | 20/99 | -0.000 | STANDARD |

**CHI @ UTA** · priced 111/111 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 24.86, exp saves 21.8 (sd 6.05), pull risk 0.051
- CHI net: Spencer Knight (PROJECTED) exp shots 29.49, exp saves 24.89 (sd 7.0), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Karel Vejmelka: 22+ saves | 0.513 | 0.275 | 54/99 | -0.044 |  |
| Patrick Kane: 1+ assists | 0.255 | 0.385 | 40/63 | +0.099 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.224 | 0.350 | 36/66 | +0.100 | STANDARD |
| Frank Nazar: 1+ assists | 0.334 | 0.210 | 23/81 | +0.091 | STANDARD |
| Frank Nazar: 1+ points | 0.472 | 0.365 | 38/65 | +0.075 | STANDARD |
| Patrick Kane: 1+ points | 0.436 | 0.535 | 56/49 | +0.056 | STANDARD |

**EDM @ VAN** · priced 122/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROBABLE) exp shots 30.37, exp saves 25.96 (sd 7.19), pull risk 0.077
- EDM net: Devon Levi (PROJECTED) exp shots 26.05, exp saves 22.63 (sd 6.31), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 2+ points | 0.257 | 0.490 | 51/53 | +0.196 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.404 | 0.575 | 60/45 | +0.128 | STANDARD |
| Leon Draisaitl: 1+ points | 0.626 | 0.770 | 82/28 | +0.080 | STANDARD |
| Connor McDavid: 2+ points | 0.382 | 0.525 | 54/49 | +0.110 | STANDARD |
| Connor McDavid: 1+ assists | 0.554 | 0.690 | 71/33 | +0.100 | STANDARD |
| Leon Draisaitl: 2+ assists | 0.099 | 0.225 | 24/79 | +0.099 | STANDARD |

**FLA @ SJS** · priced 135/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.16, exp saves 23.67 (sd 6.48), pull risk 0.06
- FLA net: Akira Schmid (PROJECTED) exp shots 26.2, exp saves 22.38 (sd 6.39), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aleksander Barkov: 1+ assists | 0.310 | 0.490 | 51/53 | +0.143 | STANDARD |
| Aleksander Barkov: 1+ points | 0.453 | 0.620 | 64/40 | +0.130 | STANDARD |
| Brady Tkachuk: 1+ points | 0.475 | 0.610 | 64/42 | +0.088 | STANDARD |
| Aleksander Barkov: 2+ points | 0.125 | 0.245 | 27/78 | +0.083 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.254 | 0.370 | 40/66 | +0.070 | STANDARD |
| Aleksander Barkov: 2+ assists | 0.054 | 0.155 | 17/86 | +0.078 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
