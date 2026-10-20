# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-20T16:48:08Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4334 · contracts joined: 2437 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2162, 'OK': 181, 'NO_EDGE': 94}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 355, 'game_early_goal': 11, 'first_goal': 380, 'game_winner': 22, 'player_goals': 689, 'game_overtime': 11, 'player_points': 442, 'game_spread': 44, 'team_total': 110, 'game_total': 99, 'goalie_saves': 10}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 2026-10-20T23:00:00Z | T-6h | 0.605 | 0.395 | 0.177 | 6.17 | 3.42 | 2.75 | 236 (25/211) | CONFIRMED/PROBABLE |
| COL @ NJD | 2026-10-20T23:00:00Z | T-6h | 0.456 | 0.544 | 0.180 | 5.79 | 2.77 | 3.02 | 239 (25/214) | CONFIRMED/CONFIRMED |
| ANA @ NYI | 2026-10-20T23:00:00Z | T-6h | 0.616 | 0.384 | 0.172 | 5.98 | 3.35 | 2.63 | 210 (25/185) | CONFIRMED/CONFIRMED |
| LAK @ WSH | 2026-10-20T23:00:00Z | T-6h | 0.656 | 0.344 | 0.171 | 5.82 | 3.39 | 2.43 | 233 (25/208) | CONFIRMED/PROBABLE |
| TOR @ CBJ | 2026-10-20T23:00:00Z | T-6h | 0.648 | 0.352 | 0.160 | 6.19 | 3.58 | 2.62 | 211 (25/186) | CONFIRMED/CONFIRMED |
| WPG @ STL | 2026-10-21T00:00:00Z | T-6h | 0.605 | 0.395 | 0.171 | 5.93 | 3.30 | 2.63 | 222 (25/197) | PROBABLE/PROJECTED |
| BOS @ DAL | 2026-10-21T00:00:00Z | T-6h | 0.520 | 0.480 | 0.187 | 5.65 | 2.89 | 2.76 | 216 (25/191) | CONFIRMED/PROJECTED |
| MIN @ EDM | 2026-10-21T01:00:00Z | T-6h | 0.568 | 0.432 | 0.171 | 6.42 | 3.42 | 3.00 | 229 (25/204) | PROJECTED/PROJECTED |
| DET @ SEA | 2026-10-21T01:40:00Z | T-6h | 0.581 | 0.419 | 0.176 | 6.02 | 3.26 | 2.77 | 209 (25/184) | PROJECTED/CONFIRMED |
| CAR @ VAN | 2026-10-21T02:00:00Z | T-6h | 0.349 | 0.651 | 0.162 | 6.44 | 2.72 | 3.72 | 211 (25/186) | PROJECTED/PROJECTED |
| TBL @ VGK | 2026-10-21T02:30:00Z | T-6h | 0.552 | 0.448 | 0.182 | 5.95 | 3.13 | 2.82 | 221 (25/196) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT20COLNJ-7 | game_total | 0.378 | 0.485 | 0.463 | 49 | 52 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ4 | team_total | 0.310 | 0.415 | 0.393 | 42 | 59 | no | +0.083 | OK |
| KXNHLTOTAL-26OCT20COLNJ-6 | game_total | 0.493 | 0.595 | 0.575 | 60 | 41 | no | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET3 | team_total | 0.523 | 0.630 | 0.609 | 64 | 38 | no | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 | team_total | 0.526 | 0.630 | 0.610 | 64 | 38 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3 | team_total | 0.487 | 0.585 | 0.566 | 59 | 42 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4 | team_total | 0.457 | 0.555 | 0.536 | 56 | 45 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL4 | team_total | 0.338 | 0.435 | 0.415 | 44 | 57 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET4 | team_total | 0.312 | 0.405 | 0.386 | 41 | 60 | no | +0.072 | OK |
| KXNHLTOTAL-26OCT20COLNJ-5 | game_total | 0.718 | 0.810 | 0.794 | 82 | 20 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5 | team_total | 0.266 | 0.360 | 0.340 | 37 | 65 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT20SJMTL-7 | game_total | 0.444 | 0.535 | 0.517 | 54 | 47 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4 | team_total | 0.278 | 0.365 | 0.347 | 37 | 64 | no | +0.065 | OK |
| KXNHLGAME-26OCT20CARVAN-CAR | game_winner | 0.651 | 0.735 | 0.719 | 74 | 27 | no | +0.065 | OK |
| KXNHLGAME-26OCT20DETSEA-DET | game_winner | 0.419 | 0.505 | 0.488 | 51 | 50 | no | +0.063 | OK |
| KXNHLGAME-26OCT20DETSEA-SEA | game_winner | 0.581 | 0.495 | 0.512 | 50 | 51 | yes | +0.063 | OK |
| KXNHLGAME-26OCT20BOSDAL-BOS | game_winner | 0.480 | 0.395 | 0.412 | 40 | 61 | yes | +0.063 | OK |
| KXNHLGAME-26OCT20BOSDAL-DAL | game_winner | 0.520 | 0.605 | 0.588 | 61 | 40 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3 | team_total | 0.674 | 0.760 | 0.744 | 77 | 25 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL3 | team_total | 0.561 | 0.650 | 0.633 | 66 | 36 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET2 | team_total | 0.758 | 0.835 | 0.821 | 84 | 17 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL2 | game_spread | 0.292 | 0.375 | 0.358 | 38 | 63 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ2 | team_total | 0.760 | 0.835 | 0.822 | 84 | 17 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT20SJMTL-6 | game_total | 0.553 | 0.635 | 0.619 | 64 | 37 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA3 | team_total | 0.443 | 0.525 | 0.508 | 53 | 48 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL3 | game_spread | 0.245 | 0.325 | 0.308 | 33 | 68 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT20COLNJ-4 | game_total | 0.814 | 0.885 | 0.873 | 89 | 12 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR2 | game_spread | 0.434 | 0.515 | 0.499 | 52 | 49 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET2 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.058 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL3 | game_spread | 0.170 | 0.250 | 0.232 | 26 | 76 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR3 | game_spread | 0.297 | 0.380 | 0.363 | 39 | 63 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ5 | team_total | 0.151 | 0.230 | 0.212 | 24 | 78 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET5 | team_total | 0.152 | 0.230 | 0.212 | 24 | 78 | no | +0.056 | OK |
| KXNHLGAME-26OCT20CARVAN-VAN | game_winner | 0.349 | 0.275 | 0.289 | 28 | 73 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT20COLNJ-8 | game_total | 0.203 | 0.280 | 0.263 | 29 | 73 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL2 | team_total | 0.779 | 0.850 | 0.837 | 86 | 16 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB4 | team_total | 0.322 | 0.405 | 0.388 | 42 | 61 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT20SJMTL-5 | game_total | 0.769 | 0.835 | 0.823 | 84 | 17 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ2 | game_spread | 0.244 | 0.315 | 0.300 | 32 | 69 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA2 | team_total | 0.686 | 0.755 | 0.742 | 76 | 25 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT20LAWSH-LA2 | game_spread | 0.159 | 0.225 | 0.210 | 23 | 78 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL5 | team_total | 0.169 | 0.240 | 0.224 | 25 | 77 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET3 | game_spread | 0.123 | 0.190 | 0.175 | 20 | 82 | no | +0.047 | OK |
| KXNHLGAME-26OCT20COLNJ-COL | game_winner | 0.544 | 0.475 | 0.489 | 48 | 53 | yes | +0.046 | OK |
| KXNHLGAME-26OCT20COLNJ-NJ | game_winner | 0.456 | 0.525 | 0.511 | 53 | 48 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB2 | team_total | 0.763 | 0.825 | 0.814 | 83 | 18 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT20DETSEA-7 | game_total | 0.417 | 0.490 | 0.475 | 50 | 52 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT20LAWSH-WSH2 | game_spread | 0.421 | 0.355 | 0.368 | 36 | 65 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ3 | game_spread | 0.135 | 0.200 | 0.185 | 21 | 81 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB3 | team_total | 0.539 | 0.610 | 0.596 | 62 | 40 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT20DETSEA-6 | game_total | 0.530 | 0.595 | 0.582 | 60 | 41 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR2 | team_total | 0.726 | 0.795 | 0.782 | 81 | 22 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL2 | game_spread | 0.381 | 0.445 | 0.432 | 45 | 56 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-5 | game_total | 0.696 | 0.755 | 0.744 | 76 | 25 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20SJMTL-8 | game_total | 0.254 | 0.315 | 0.302 | 32 | 69 | no | +0.041 | OK |
| KXNHLGAME-26OCT20LAWSH-LA | game_winner | 0.344 | 0.405 | 0.392 | 41 | 60 | no | +0.040 | OK |
| KXNHLGAME-26OCT20LAWSH-WSH | game_winner | 0.656 | 0.595 | 0.608 | 60 | 41 | yes | +0.040 | OK |
| KXNHLTOTAL-26OCT20TBVGK-5 | game_total | 0.739 | 0.800 | 0.789 | 81 | 21 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT20TBVGK-TB2 | game_spread | 0.237 | 0.295 | 0.283 | 30 | 71 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA4 | team_total | 0.237 | 0.305 | 0.291 | 32 | 71 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR2 | game_spread | 0.171 | 0.225 | 0.213 | 23 | 78 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT20DETSEA-5 | game_total | 0.752 | 0.810 | 0.799 | 82 | 20 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA2 | game_spread | 0.350 | 0.295 | 0.306 | 30 | 71 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT20TBVGK-7 | game_total | 0.408 | 0.470 | 0.457 | 48 | 54 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN3 | team_total | 0.512 | 0.455 | 0.466 | 46 | 55 | yes | +0.035 | OK |
| KXNHLGAME-26OCT20TBVGK-VGK | game_winner | 0.552 | 0.495 | 0.506 | 50 | 51 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT20LAWSH-LA3 | game_spread | 0.080 | 0.125 | 0.114 | 13 | 88 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-CBJ2 | game_spread | 0.429 | 0.375 | 0.386 | 38 | 63 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR3 | game_spread | 0.090 | 0.135 | 0.125 | 14 | 87 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT20COLNJ-9 | game_total | 0.138 | 0.190 | 0.178 | 20 | 82 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL6 | team_total | 0.128 | 0.180 | 0.168 | 19 | 83 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL2 | team_total | 0.851 | 0.900 | 0.892 | 91 | 11 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT20TBVGK-6 | game_total | 0.521 | 0.575 | 0.564 | 58 | 43 | no | +0.031 | OK |
| KXNHLGAME-26OCT20TORCBJ-CBJ | game_winner | 0.648 | 0.595 | 0.606 | 60 | 41 | yes | +0.031 | OK |
| KXNHLGAME-26OCT20TORCBJ-TOR | game_winner | 0.352 | 0.405 | 0.394 | 41 | 60 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT20SJMTL-4 | game_total | 0.852 | 0.900 | 0.892 | 91 | 11 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2 | team_total | 0.885 | 0.925 | 0.918 | 93 | 8 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-WPG3 | game_spread | 0.101 | 0.145 | 0.135 | 15 | 86 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-WPG2 | game_spread | 0.197 | 0.245 | 0.235 | 25 | 76 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT20SJMTL-9 | game_total | 0.178 | 0.230 | 0.219 | 24 | 78 | no | +0.030 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 0.605 | 0.610 | 0.177 | 0.206 | 6.17 | 6.25 | 0.943/1.024 | KXNHLTOTAL-26OCT20SJMTL-7 +0.016 |
| COL @ NJD | 0.456 | 0.483 | 0.180 | 0.219 | 5.79 | 6.15 | 0.984/0.971 | KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 +0.066 |
| ANA @ NYI | 0.616 | 0.578 | 0.172 | 0.215 | 5.98 | 6.36 | 0.947/1.016 | KXNHLTOTAL-26OCT20ANANYI-7 +0.074 |
| LAK @ WSH | 0.656 | 0.577 | 0.171 | 0.217 | 5.82 | 5.90 | 0.938/0.994 | KXNHLGAME-26OCT20LAWSH-LA +0.079 |
| TOR @ CBJ | 0.648 | 0.620 | 0.160 | 0.217 | 6.19 | 5.99 | 0.946/0.956 | KXNHLTEAMTOTAL-26OCT20TORCBJ-CBJ5 -0.049 |
| WPG @ STL | 0.605 | 0.590 | 0.171 | 0.215 | 5.93 | 6.20 | 0.984/0.988 | KXNHLTOTAL-26OCT20WPGSTL-7 +0.048 |
| BOS @ DAL | 0.520 | 0.531 | 0.187 | 0.216 | 5.65 | 6.24 | 0.994/0.968 | KXNHLTOTAL-26OCT20BOSDAL-7 +0.102 |
| MIN @ EDM | 0.568 | 0.595 | 0.171 | 0.206 | 6.42 | 6.68 | 0.994/0.995 | KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4 +0.054 |
| DET @ SEA | 0.581 | 0.575 | 0.176 | 0.210 | 6.02 | 6.24 | 1.015/1.024 | KXNHLTOTAL-26OCT20DETSEA-7 +0.041 |
| CAR @ VAN | 0.349 | 0.442 | 0.162 | 0.216 | 6.44 | 6.50 | 1.026/0.997 | KXNHLSPREAD-26OCT20CARVAN-CAR2 -0.097 |
| TBL @ VGK | 0.552 | 0.581 | 0.182 | 0.213 | 5.95 | 6.11 | 1.003/0.958 | KXNHLTEAMTOTAL-26OCT20TBVGK-VGK4 +0.047 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 41 recommended · full analysis in card.md / packet.json `thesis_card`

- Zachary Bolduc: 1+ goals NO @ 75c · p 0.8058 (adj 0.7906) · $6.08 · thesis MTL:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 18c · p 0.2285 (adj 0.2151) · $2.29 · thesis SJS:OFFENSE_4PLUS
- Cole Caufield: 1+ goals NO @ 55c · p 0.6055 (adj 0.5891) · $3.77 · thesis MTL:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 74c · p 0.7935 (adj 0.7642) · $3.92 · thesis SJS:SUPPRESSED
- Fedor Svechkov: 1+ goals YES @ 8c · p 0.1156 (adj 0.1042) · $1.57 · thesis COL:OFFENSE_4PLUS
- Cale Makar: 1+ assists NO @ 45c · p 0.6011 (adj 0.4996) · $5.22 · thesis COL:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 65c · p 0.7039 (adj 0.6892) · $5.92 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ assists NO @ 48c · p 0.611 (adj 0.5193) · $3.71 · thesis NJD:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 12c · p 0.2121 (adj 0.1457) · $1.24 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.129 (adj 0.1192) · $1.12 · thesis ANA:OFFENSE_4PLUS
- Jackson LaCombe: 1+ goals YES @ 11c · p 0.1365 (adj 0.1286) · $1.03 · thesis ANA:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 65c · p 0.8609 (adj 0.7076) · $6.56 · thesis LAK:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2403 (adj 0.2227) · $3.06 · thesis WSH:OFFENSE_4PLUS
- Mats Zuccarello: 2+ assists NO @ 93c · p 0.9897 (adj 0.9499) · $6.56 · thesis DIFFUSE
- Gavin McKenna: 1+ goals NO @ 80c · p 0.8464 (adj 0.8336) · $5.75 · thesis TOR:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 19c · p 0.2327 (adj 0.2183) · $1.9 · thesis CBJ:OFFENSE_4PLUS
- Full Game: Over 5.5 goals scored NO @ 40c · p 0.4777 (adj 0.4364) · $2.62 · thesis GAME:LOW_EVENT
- Jack Roslovic: 1+ goals NO @ 77c · p 0.81 (adj 0.7975) · $4.1 · thesis TOR:SUPPRESSED
- Morgan Barron: 1+ goals YES @ 8c · p 0.1213 (adj 0.1097) · $1.97 · thesis WPG:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 25c · p 0.2934 (adj 0.2801) · $1.7 · thesis STL:OFFENSE_4PLUS
- Philip Broberg: 1+ assists YES @ 33c · p 0.4022 (adj 0.3611) · $1.74 · thesis STL:OFFENSE_4PLUS
- Dalibor Dvorsky: 1+ goals NO @ 83c · p 0.8612 (adj 0.8509) · $6.41 · thesis STL:SUPPRESSED
- Matthew Poitras: 1+ goals YES @ 11c · p 0.1471 (adj 0.1366) · $1.67 · thesis BOS:OFFENSE_4PLUS
- Elias Lindholm: 1+ goals YES @ 19c · p 0.2379 (adj 0.2209) · $1.93 · thesis BOS:OFFENSE_4PLUS
- Morgan Geekie: 1+ goals YES @ 25c · p 0.2948 (adj 0.2823) · $2.13 · thesis BOS:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.727 (adj 0.7127) · $4.64 · thesis DAL:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 14c · p 0.1915 (adj 0.1761) · $2.56 · thesis EDM:OFFENSE_4PLUS
- Quinn Hughes: 1+ assists NO @ 39c · p 0.4831 (adj 0.434) · $3.74 · thesis MIN:SUPPRESSED
- Zach Hyman: 1+ goals YES @ 32c · p 0.3697 (adj 0.3548) · $2.83 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 68c · p 0.7811 (adj 0.7089) · $5.79 · thesis EDM:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 12c · p 0.1648 (adj 0.1523) · $2.06 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 11c · p 0.1526 (adj 0.1407) · $1.95 · thesis SEA:OFFENSE_4PLUS
- Moritz Seider: 1+ goals NO @ 85c · p 0.9022 (adj 0.8841) · $6.56 · thesis DET:SUPPRESSED
- Detroit wins by over 1.5 goals NO @ 71c · p 0.7832 (adj 0.7441) · $4.33 · thesis SEA:WINS
- Drew O'Connor: 1+ goals YES @ 11c · p 0.1732 (adj 0.1562) · $3.07 · thesis VAN:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 17c · p 0.2454 (adj 0.2228) · $3.63 · thesis VAN:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 49c · p 0.6564 (adj 0.545) · $3.33 · thesis VAN:WINS
- Sebastian Aho: 1+ goals NO @ 62c · p 0.6848 (adj 0.6661) · $5.93 · thesis CAR:SUPPRESSED
- Tampa Bay wins by over 1.5 goals NO @ 71c · p 0.7917 (adj 0.7484) · $6.56 · thesis VGK:WINS
- Brett Howden: 1+ goals YES @ 19c · p 0.2358 (adj 0.2218) · $1.77 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 71c · p 0.7596 (adj 0.746) · $6.56 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ MTL** · priced 175/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 27.0, exp saves 23.53 (sd 6.48), pull risk 0.053
- SJS net: Alex Nedeljkovic (PROBABLE) exp shots 27.29, exp saves 23.18 (sd 6.64), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Newhook: 1+ assists | 0.273 | 0.145 | 28/99 | -0.022 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.295 | 0.175 | 34/99 | -0.060 | STANDARD |
| Nick Suzuki: 1+ assists | 0.480 | 0.590 | 60/42 | +0.083 | STANDARD |
| Nick Suzuki: 2+ points | 0.279 | 0.375 | 39/64 | +0.065 | STANDARD |
| Phillip Danault: 1+ assists | 0.197 | 0.105 | 20/99 | -0.014 | STANDARD |
| Josh Anderson: 1+ assists | 0.214 | 0.130 | 25/99 | -0.049 | STANDARD |

**COL @ NJD** · priced 182/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 29.27, exp saves 25.27 (sd 6.74), pull risk 0.061
- COL net: Scott Wedgewood (CONFIRMED) exp shots 28.54, exp saves 24.76 (sd 6.74), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.155 | 0.325 | 35/70 | +0.130 | STANDARD |
| Cale Makar: 1+ assists | 0.399 | 0.555 | 56/45 | +0.134 | STANDARD |
| Luke Evangelista: 1+ points | 0.318 | 0.465 | 48/55 | +0.115 | STANDARD |
| Scott Wedgewood: 28+ saves | 0.330 | 0.475 | 50/55 | +0.103 |  |
| Cale Makar: 1+ points | 0.496 | 0.640 | 65/37 | +0.118 | STANDARD |
| Jack Hughes: 1+ assists | 0.389 | 0.530 | 54/48 | +0.114 | STANDARD |

**ANA @ NYI** · priced 156/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.2, exp saves 24.63 (sd 6.66), pull risk 0.053
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.37, exp saves 23.37 (sd 6.6), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lukas Dostal: 27+ saves | 0.310 | 0.450 | 47/57 | +0.103 |  |
| Ilya Sorokin: 23+ saves | 0.624 | 0.515 | 54/51 | +0.066 |  |
| A.J. Greer: 1+ goals | 0.212 | 0.110 | 12/90 | +0.085 | STANDARD |
| Alex Killorn: 1+ points | 0.446 | 0.355 | 38/67 | +0.049 | STANDARD |
| Alex Killorn: 1+ assists | 0.308 | 0.230 | 26/80 | +0.034 | STANDARD |
| Frank Vatrano: 1+ assists | 0.173 | 0.115 | 22/99 | -0.059 | STANDARD |

**LAK @ WSH** · priced 172/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.19, exp saves 24.65 (sd 6.48), pull risk 0.046
- LAK net: Darcy Kuemper (PROBABLE) exp shots 26.88, exp saves 22.97 (sd 6.41), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.139 | 0.375 | 40/65 | +0.195 | STANDARD |
| Mats Zuccarello: 1+ points | 0.305 | 0.490 | 52/54 | +0.138 | STANDARD |
| Artemi Panarin: 1+ assists | 0.336 | 0.470 | 48/54 | +0.107 | STANDARD |
| Darcy Kuemper: 27+ saves | 0.282 | 0.410 | 42/60 | +0.101 |  |
| Artemi Panarin: 2+ points | 0.162 | 0.270 | 29/75 | +0.075 | STANDARD |
| Artemi Panarin: 1+ points | 0.513 | 0.620 | 63/39 | +0.080 | STANDARD |

**TOR @ CBJ** · priced 146/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (CONFIRMED) exp shots 25.9, exp saves 22.95 (sd 6.05), pull risk 0.037
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.4, exp saves 26.78 (sd 7.15), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.339 | 0.455 | 46/55 | +0.094 | STANDARD |
| Kirill Marchenko: 1+ points | 0.454 | 0.550 | 56/46 | +0.069 | STANDARD |
| Auston Matthews: 1+ points | 0.554 | 0.650 | 66/36 | +0.070 | STANDARD |
| Jet Greaves: 25+ saves | 0.385 | 0.475 | 50/55 | +0.048 |  |
| Auston Matthews: 2+ points | 0.200 | 0.290 | 31/73 | +0.056 | STANDARD |
| Darren Raddysh: 1+ assists | 0.325 | 0.415 | 43/60 | +0.058 | STANDARD |

**WPG @ STL** · priced 168/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROBABLE) exp shots 26.09, exp saves 22.9 (sd 6.22), pull risk 0.045
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.62, exp saves 22.69 (sd 6.4), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Philip Broberg: 1+ points | 0.460 | 0.365 | 38/65 | +0.064 | STANDARD |
| Philip Broberg: 1+ assists | 0.402 | 0.320 | 33/69 | +0.057 | STANDARD |
| Mason McTavish: 1+ assists | 0.269 | 0.345 | 36/67 | +0.045 | STANDARD |
| Pavel Buchnevich: 1+ assists | 0.253 | 0.325 | 35/70 | +0.032 | STANDARD |
| Alex Iafallo: 1+ assists | 0.244 | 0.175 | 20/85 | +0.033 | STANDARD |
| Jimmy Snuggerud: 1+ assists | 0.392 | 0.325 | 34/69 | +0.036 | STANDARD |

**BOS @ DAL** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.49, exp saves 21.27 (sd 6.01), pull risk 0.058
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.85, exp saves 24.08 (sd 6.58), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.231 | 0.335 | 35/68 | +0.074 | STANDARD |
| Fraser Minten: 1+ assists | 0.327 | 0.240 | 27/79 | +0.043 | STANDARD |
| Miro Heiskanen: 1+ points | 0.480 | 0.555 | 57/46 | +0.043 | STANDARD |
| Fraser Minten: 1+ points | 0.474 | 0.400 | 41/61 | +0.047 | STANDARD |
| Tyler Seguin: 1+ assists | 0.212 | 0.285 | 30/73 | +0.044 | STANDARD |
| Thomas Harley: 1+ assists | 0.387 | 0.315 | 33/70 | +0.041 | STANDARD |

**MIN @ EDM** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.88, exp saves 24.28 (sd 6.69), pull risk 0.064
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 24.81 (sd 7.09), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kasperi Kapanen: 1+ assists | 0.312 | 0.185 | 22/85 | +0.080 | STANDARD |
| Connor McDavid: 1+ assists | 0.587 | 0.700 | 72/32 | +0.078 | STANDARD |
| Connor McDavid: 2+ assists | 0.219 | 0.330 | 34/68 | +0.086 | STANDARD |
| Leon Draisaitl: 2+ points | 0.332 | 0.435 | 45/58 | +0.071 | STANDARD |
| Connor McDavid: 2+ points | 0.425 | 0.525 | 54/49 | +0.068 | STANDARD |
| Kasperi Kapanen: 1+ points | 0.420 | 0.320 | 33/69 | +0.074 | STANDARD |

**DET @ SEA** · priced 149/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 29.42, exp saves 25.69 (sd 6.74), pull risk 0.05
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.75, exp saves 22.84 (sd 6.46), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Moritz Seider: 1+ points | 0.454 | 0.585 | 60/43 | +0.099 | STANDARD |
| Moritz Seider: 2+ points | 0.130 | 0.250 | 27/77 | +0.088 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.354 | 0.235 | 27/80 | +0.070 | STANDARD |
| Moritz Seider: 1+ assists | 0.396 | 0.500 | 52/52 | +0.066 | STANDARD |
| Kaapo Kakko: 1+ points | 0.490 | 0.390 | 41/63 | +0.063 | STANDARD |
| Berkly Catton: 1+ goals | 0.209 | 0.125 | 18/93 | +0.018 | STANDARD |

**CAR @ VAN** · priced 153/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 32.33, exp saves 27.7 (sd 7.44), pull risk 0.074
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.8, exp saves 19.88 (sd 5.73), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.219 | 0.335 | 35/68 | +0.085 | STANDARD |
| Sebastian Aho: 1+ assists | 0.396 | 0.495 | 50/51 | +0.076 | STANDARD |
| Nikolaj Ehlers: 1+ points | 0.504 | 0.600 | 62/42 | +0.059 | STANDARD |
| Filip Chytil: 1+ goals | 0.245 | 0.155 | 17/86 | +0.066 | STANDARD |
| Linus Karlsson: 1+ goals | 0.232 | 0.145 | 18/89 | +0.042 | STANDARD |
| Sean Walker: 1+ assists | 0.338 | 0.260 | 29/77 | +0.034 | STANDARD |

**TBL @ VGK** · priced 167/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.99, exp saves 23.65 (sd 6.38), pull risk 0.049
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.35, exp saves 22.53 (sd 6.4), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.270 | 0.405 | 42/61 | +0.104 | STANDARD |
| John Carlson: 1+ points | 0.335 | 0.460 | 48/56 | +0.088 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.443 | 0.565 | 57/44 | +0.100 | STANDARD |
| Nikita Kucherov: 2+ points | 0.251 | 0.370 | 38/64 | +0.093 | STANDARD |
| Zemgus Girgensons: 1+ points | 0.231 | 0.135 | 25/98 | -0.033 | STANDARD |
| Shea Theodore: 1+ points | 0.421 | 0.340 | 35/67 | +0.055 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
