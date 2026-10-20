# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-20T11:05:32Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 2913 · contracts joined: 1016 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 741, 'OK': 153, 'NO_EDGE': 122}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'game_early_goal': 11, 'game_winner': 22, 'game_overtime': 11, 'game_spread': 44, 'team_total': 110, 'game_total': 99, 'player_assists': 93, 'first_goal': 71, 'player_goals': 179, 'player_points': 112}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 2026-10-20T23:00:00Z | T-6h | 0.570 | 0.430 | 0.177 | 6.20 | 3.32 | 2.88 | 51 (25/26) | PROJECTED/PROBABLE |
| COL @ NJD | 2026-10-20T23:00:00Z | T-6h | 0.430 | 0.570 | 0.173 | 6.06 | 2.81 | 3.25 | 221 (25/196) | PROJECTED/PROJECTED |
| ANA @ NYI | 2026-10-20T23:00:00Z | T-6h | 0.560 | 0.440 | 0.177 | 6.11 | 3.24 | 2.86 | 199 (25/174) | PROJECTED/CONFIRMED |
| LAK @ WSH | 2026-10-20T23:00:00Z | T-6h | 0.599 | 0.401 | 0.184 | 5.70 | 3.15 | 2.55 | 188 (25/163) | PROJECTED/PROJECTED |
| TOR @ CBJ | 2026-10-20T23:00:00Z | T-6h | 0.615 | 0.385 | 0.165 | 6.27 | 3.50 | 2.77 | 51 (25/26) | PROJECTED/CONFIRMED |
| WPG @ STL | 2026-10-21T00:00:00Z | T-12h | 0.607 | 0.393 | 0.179 | 5.97 | 3.31 | 2.66 | 51 (25/26) | PROJECTED/PROJECTED |
| BOS @ DAL | 2026-10-21T00:00:00Z | T-12h | 0.512 | 0.488 | 0.187 | 5.70 | 2.89 | 2.81 | 51 (25/26) | PROJECTED/PROJECTED |
| MIN @ EDM | 2026-10-21T01:00:00Z | T-12h | 0.563 | 0.437 | 0.167 | 6.43 | 3.42 | 3.00 | 51 (25/26) | PROJECTED/PROJECTED |
| DET @ SEA | 2026-10-21T01:40:00Z | T-12h | 0.574 | 0.426 | 0.176 | 6.03 | 3.26 | 2.77 | 51 (25/26) | PROJECTED/CONFIRMED |
| CAR @ VAN | 2026-10-21T02:00:00Z | T-12h | 0.344 | 0.656 | 0.161 | 6.45 | 2.72 | 3.73 | 51 (25/26) | PROJECTED/PROJECTED |
| TBL @ VGK | 2026-10-21T02:30:00Z | T-12h | 0.528 | 0.472 | 0.180 | 6.10 | 3.13 | 2.97 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4 | team_total | 0.436 | 0.550 | 0.527 | 56 | 46 | no | +0.086 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5 | team_total | 0.243 | 0.350 | 0.327 | 36 | 66 | no | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL4 | team_total | 0.338 | 0.440 | 0.419 | 45 | 57 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3 | team_total | 0.652 | 0.750 | 0.732 | 76 | 26 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL3 | game_spread | 0.213 | 0.310 | 0.289 | 32 | 70 | no | +0.072 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL2 | game_spread | 0.342 | 0.435 | 0.416 | 44 | 57 | no | +0.071 | OK |
| KXNHLGAME-26OCT20BOSDAL-BOS | game_winner | 0.488 | 0.395 | 0.413 | 40 | 61 | yes | +0.071 | OK |
| KXNHLGAME-26OCT20BOSDAL-DAL | game_winner | 0.512 | 0.605 | 0.587 | 61 | 40 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL3 | game_spread | 0.168 | 0.255 | 0.236 | 26 | 75 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET3 | team_total | 0.525 | 0.625 | 0.606 | 64 | 39 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET4 | team_total | 0.316 | 0.410 | 0.390 | 42 | 60 | no | +0.068 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR2 | game_spread | 0.436 | 0.525 | 0.507 | 53 | 48 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL3 | team_total | 0.558 | 0.650 | 0.632 | 66 | 36 | no | +0.065 | OK |
| KXNHLGAME-26OCT20SJMTL-MTL | game_winner | 0.570 | 0.655 | 0.639 | 66 | 35 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 | team_total | 0.537 | 0.620 | 0.604 | 63 | 39 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL2 | game_spread | 0.288 | 0.365 | 0.349 | 37 | 64 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT20DETSEA-7 | game_total | 0.417 | 0.495 | 0.479 | 50 | 51 | no | +0.055 | OK |
| KXNHLGAME-26OCT20SJMTL-SJ | game_winner | 0.430 | 0.355 | 0.370 | 36 | 65 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT20SJMTL-7 | game_total | 0.449 | 0.525 | 0.510 | 53 | 48 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ4 | team_total | 0.321 | 0.400 | 0.384 | 41 | 61 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET2 | team_total | 0.758 | 0.825 | 0.813 | 83 | 18 | no | +0.052 | OK |
| KXNHLGAME-26OCT20CARVAN-CAR | game_winner | 0.656 | 0.725 | 0.712 | 73 | 28 | no | +0.050 | OK |
| KXNHLGAME-26OCT20CARVAN-VAN | game_winner | 0.344 | 0.275 | 0.288 | 28 | 73 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR3 | game_spread | 0.295 | 0.365 | 0.350 | 37 | 64 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET3 | game_spread | 0.121 | 0.185 | 0.170 | 19 | 82 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ2 | game_spread | 0.228 | 0.295 | 0.281 | 30 | 71 | no | +0.048 | OK |
| KXNHLGAME-26OCT20DETSEA-DET | game_winner | 0.426 | 0.495 | 0.481 | 50 | 51 | no | +0.047 | OK |
| KXNHLGAME-26OCT20DETSEA-SEA | game_winner | 0.574 | 0.505 | 0.519 | 51 | 50 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET2 | game_spread | 0.220 | 0.285 | 0.271 | 29 | 72 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR4 | team_total | 0.528 | 0.600 | 0.586 | 61 | 41 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL6 | team_total | 0.115 | 0.180 | 0.165 | 19 | 83 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET5 | team_total | 0.154 | 0.220 | 0.205 | 23 | 79 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT20SJMTL-6 | game_total | 0.560 | 0.630 | 0.616 | 64 | 38 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-BOS2 | game_spread | 0.265 | 0.205 | 0.216 | 21 | 80 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL2 | team_total | 0.840 | 0.895 | 0.886 | 90 | 11 | no | +0.043 | OK |
| KXNHLGAME-26OCT20COLNJ-COL | game_winner | 0.570 | 0.505 | 0.518 | 51 | 50 | yes | +0.043 | OK |
| KXNHLGAME-26OCT20COLNJ-NJ | game_winner | 0.430 | 0.495 | 0.482 | 50 | 51 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ3 | game_spread | 0.128 | 0.190 | 0.176 | 20 | 82 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT20LAWSH-5 | game_total | 0.706 | 0.765 | 0.754 | 77 | 24 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR5 | team_total | 0.323 | 0.395 | 0.380 | 41 | 62 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ5 | team_total | 0.158 | 0.225 | 0.210 | 24 | 79 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT20COLNJ-7 | game_total | 0.423 | 0.485 | 0.472 | 49 | 52 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL2 | team_total | 0.780 | 0.840 | 0.829 | 85 | 17 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL5 | team_total | 0.170 | 0.235 | 0.221 | 25 | 78 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT20DETSEA-6 | game_total | 0.536 | 0.600 | 0.587 | 61 | 41 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT20SJMTL-8 | game_total | 0.259 | 0.315 | 0.303 | 32 | 69 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT20SJMTL-5 | game_total | 0.774 | 0.830 | 0.820 | 84 | 18 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT20DETSEA-5 | game_total | 0.753 | 0.815 | 0.804 | 83 | 20 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ2 | team_total | 0.764 | 0.815 | 0.806 | 82 | 19 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT20SJMTL-SJ2 | game_spread | 0.225 | 0.175 | 0.184 | 18 | 83 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-5 | game_total | 0.704 | 0.755 | 0.745 | 76 | 25 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT20DETSEA-8 | game_total | 0.234 | 0.285 | 0.274 | 29 | 72 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5 | team_total | 0.148 | 0.105 | 0.113 | 11 | 90 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT20COLNJ-5 | game_total | 0.758 | 0.805 | 0.796 | 81 | 20 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3 | team_total | 0.523 | 0.575 | 0.565 | 58 | 43 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT20COLNJ-6 | game_total | 0.534 | 0.585 | 0.575 | 59 | 42 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2 | team_total | 0.743 | 0.695 | 0.705 | 70 | 31 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR2 | team_total | 0.751 | 0.800 | 0.791 | 81 | 21 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR3 | team_total | 0.730 | 0.785 | 0.775 | 80 | 23 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT20COLNJ-COL2 | game_spread | 0.341 | 0.295 | 0.304 | 30 | 71 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT20LAWSH-4 | game_total | 0.804 | 0.845 | 0.837 | 85 | 16 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT20LAWSH-7 | game_total | 0.367 | 0.420 | 0.409 | 43 | 59 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA2 | game_spread | 0.351 | 0.305 | 0.314 | 31 | 70 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT20LAWSH-6 | game_total | 0.476 | 0.525 | 0.515 | 53 | 48 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-WPG3 | game_spread | 0.105 | 0.145 | 0.136 | 15 | 86 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN4 | team_total | 0.300 | 0.250 | 0.259 | 26 | 76 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT20SJMTL-4 | game_total | 0.857 | 0.900 | 0.892 | 91 | 11 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT20SJMTL-9 | game_total | 0.183 | 0.230 | 0.220 | 24 | 78 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT20DETSEA-4 | game_total | 0.839 | 0.880 | 0.873 | 89 | 13 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT20LAWSH-9 | game_total | 0.127 | 0.165 | 0.157 | 17 | 84 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN3 | team_total | 0.511 | 0.460 | 0.470 | 47 | 55 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA2 | team_total | 0.714 | 0.755 | 0.747 | 76 | 25 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT20ANANYI-NYI3 | game_spread | 0.204 | 0.245 | 0.236 | 25 | 76 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT20CARVAN-VAN2 | game_spread | 0.171 | 0.130 | 0.137 | 14 | 88 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT20SJMTL-SJ3 | game_spread | 0.129 | 0.095 | 0.101 | 10 | 91 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET6 | team_total | 0.063 | 0.095 | 0.088 | 10 | 91 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT20TBVGK-7 | game_total | 0.431 | 0.475 | 0.466 | 48 | 53 | no | +0.021 | OK |
| KXNHLGAME-26OCT20WPGSTL-STL | game_winner | 0.607 | 0.565 | 0.573 | 57 | 44 | yes | +0.020 | OK |
| KXNHLGAME-26OCT20WPGSTL-WPG | game_winner | 0.393 | 0.435 | 0.427 | 44 | 57 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT20COLNJ-8 | game_total | 0.237 | 0.275 | 0.267 | 28 | 73 | no | +0.019 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 0.570 | 0.551 | 0.177 | 0.214 | 6.20 | 6.41 | 0.976/1.024 | KXNHLTEAMTOTAL-26OCT20SJMTL-SJ3 +0.037 |
| COL @ NJD | 0.430 | 0.450 | 0.173 | 0.215 | 6.06 | 6.22 | 0.992/0.973 | KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 +0.036 |
| ANA @ NYI | 0.560 | 0.538 | 0.177 | 0.216 | 6.11 | 6.41 | 0.956/1.016 | KXNHLTOTAL-26OCT20ANANYI-7 +0.055 |
| LAK @ WSH | 0.599 | 0.569 | 0.184 | 0.229 | 5.70 | 5.94 | 0.961/0.989 | KXNHLTEAMTOTAL-26OCT20LAWSH-LA3 +0.051 |
| TOR @ CBJ | 0.615 | 0.576 | 0.165 | 0.216 | 6.27 | 6.07 | 0.964/0.956 | KXNHLTEAMTOTAL-26OCT20TORCBJ-CBJ4 -0.049 |
| WPG @ STL | 0.607 | 0.583 | 0.179 | 0.213 | 5.97 | 6.21 | 0.993/0.988 | KXNHLTOTAL-26OCT20WPGSTL-7 +0.044 |
| BOS @ DAL | 0.512 | 0.531 | 0.187 | 0.219 | 5.70 | 6.22 | 0.986/0.968 | KXNHLTOTAL-26OCT20BOSDAL-7 +0.087 |
| MIN @ EDM | 0.563 | 0.595 | 0.167 | 0.212 | 6.43 | 6.67 | 0.994/0.995 | KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4 +0.051 |
| DET @ SEA | 0.574 | 0.578 | 0.176 | 0.211 | 6.03 | 6.23 | 1.015/1.024 | KXNHLTOTAL-26OCT20DETSEA-7 +0.039 |
| CAR @ VAN | 0.344 | 0.443 | 0.161 | 0.214 | 6.45 | 6.48 | 1.026/0.997 | KXNHLSPREAD-26OCT20CARVAN-CAR2 -0.099 |
| TBL @ VGK | 0.528 | 0.586 | 0.180 | 0.218 | 6.10 | 6.11 | 1.004/0.958 | KXNHLGAME-26OCT20TBVGK-TB -0.058 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 21 recommended · full analysis in card.md / packet.json `thesis_card`

- Montreal over 4.5 goals scored NO @ 66c · p 0.7456 (adj 0.6978) · $9.88 · thesis SJS:WINS
- Montreal over 2.5 goals scored NO @ 26c · p 0.3376 (adj 0.2938) · $2.39 · thesis MTL:SUPPRESSED
- Montreal wins by over 2.5 goals NO @ 70c · p 0.7784 (adj 0.7342) · $7.96 · thesis SJS:WINS
- San Jose wins by over 1.5 goals YES @ 18c · p 0.2394 (adj 0.2072) · $2.19 · thesis SJS:WINS_BY_2PLUS
- Anaheim over 2.5 goals scored YES @ 54c · p 0.6039 (adj 0.5695) · $6.96 · thesis ANA:OFFENSE_4PLUS
- Toronto wins 1st Period by over 1.5 goals YES @ 3c · p 0.0884 (adj 0.0439) · $1.46 · thesis TOR:WINS_BY_2PLUS
- Full Game: Over 4.5 goals scored NO @ 19c · p 0.2444 (adj 0.2147) · $1.94 · thesis GAME:LOW_EVENT
- Full Game: Over 3.5 goals scored NO @ 12c · p 0.161 (adj 0.138) · $1.09 · thesis GAME:LOW_EVENT
- Full Game: Over 5.5 goals scored NO @ 40c · p 0.4675 (adj 0.4313) · $3.75 · thesis GAME:LOW_EVENT
- Boston over 4.5 goals scored YES @ 13c · p 0.194 (adj 0.1595) · $4.54 · thesis BOS:OFFENSE_4PLUS
- Boston over 2.5 goals scored YES @ 51c · p 0.5901 (adj 0.5451) · $2.22 · thesis BOS:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 75c · p 0.8079 (adj 0.7764) · $8.82 · thesis BOS:WINS
- Detroit wins by over 2.5 goals NO @ 82c · p 0.8725 (adj 0.8438) · $14.89 · thesis SEA:WINS
- Detroit wins by over 1.5 goals NO @ 72c · p 0.7843 (adj 0.7496) · $8.02 · thesis SEA:WINS
- Vancouver wins 1st Period by over 1.5 goals YES @ 3c · p 0.1017 (adj 0.0518) · $1.16 · thesis VAN:SCORES_FIRST
- Vancouver wins by over 2.5 goals YES @ 7c · p 0.1397 (adj 0.1023) · $2.43 · thesis VAN:WINS_BY_2PLUS
- Vancouver over 4.5 goals scored YES @ 11c · p 0.1953 (adj 0.1502) · $3.31 · thesis VAN:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 48c · p 0.6626 (adj 0.5407) · $14.74 · thesis VAN:WINS
- Tampa Bay wins by over 2.5 goals NO @ 83c · p 0.8765 (adj 0.8507) · $14.15 · thesis VGK:WINS
- Tampa Bay wins by over 1.5 goals NO @ 73c · p 0.7868 (adj 0.7559) · $3.32 · thesis VGK:WINS
- Vegas wins by over 1.5 goals YES @ 30c · p 0.3549 (adj 0.3249) · $2.0 · thesis VGK:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ MTL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.0, exp saves 23.41 (sd 6.55), pull risk 0.06
- SJS net: Alex Nedeljkovic (PROBABLE) exp shots 27.29, exp saves 23.32 (sd 6.61), pull risk 0.076

**COL @ NJD** · priced 167/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROJECTED) exp shots 29.27, exp saves 25.18 (sd 6.81), pull risk 0.066
- COL net: Scott Wedgewood (PROJECTED) exp shots 28.54, exp saves 24.88 (sd 6.6), pull risk 0.054

**ANA @ NYI** · priced 145/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.2, exp saves 24.5 (sd 6.68), pull risk 0.063
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.37, exp saves 23.44 (sd 6.54), pull risk 0.074

**LAK @ WSH** · priced 126/137 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 28.19, exp saves 24.61 (sd 6.51), pull risk 0.047
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.88, exp saves 22.98 (sd 6.37), pull risk 0.066

**TOR @ CBJ** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 25.9, exp saves 22.82 (sd 6.19), pull risk 0.044
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.4, exp saves 26.85 (sd 7.2), pull risk 0.067

**WPG @ STL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 26.09, exp saves 22.87 (sd 6.26), pull risk 0.048
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.62, exp saves 22.63 (sd 6.36), pull risk 0.072

**BOS @ DAL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.49, exp saves 21.24 (sd 6.02), pull risk 0.057
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.85, exp saves 24.07 (sd 6.59), pull risk 0.063

**MIN @ EDM** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.88, exp saves 24.35 (sd 6.61), pull risk 0.058
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 24.77 (sd 7.06), pull risk 0.088

**DET @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 29.42, exp saves 25.7 (sd 6.8), pull risk 0.051
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.75, exp saves 22.9 (sd 6.47), pull risk 0.075

**CAR @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 32.33, exp saves 27.71 (sd 7.51), pull risk 0.076
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.8, exp saves 19.93 (sd 5.8), pull risk 0.058

**TBL @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 26.99, exp saves 23.62 (sd 6.42), pull risk 0.05
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.35, exp saves 22.59 (sd 6.42), pull risk 0.065

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
