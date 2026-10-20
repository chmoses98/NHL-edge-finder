# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-20T18:38:22Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4433 · contracts joined: 2536 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2261, 'OK': 189, 'NO_EDGE': 86}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 379, 'game_early_goal': 11, 'first_goal': 398, 'game_winner': 22, 'player_goals': 691, 'game_overtime': 11, 'player_points': 488, 'goalie_saves': 19, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 2026-10-20T23:00:00Z | T-3h | 0.605 | 0.395 | 0.177 | 6.17 | 3.42 | 2.75 | 256 (25/231) | CONFIRMED/PROBABLE |
| COL @ NJD | 2026-10-20T23:00:00Z | T-3h | 0.456 | 0.544 | 0.180 | 5.79 | 2.77 | 3.02 | 238 (25/213) | CONFIRMED/CONFIRMED |
| ANA @ NYI | 2026-10-20T23:00:00Z | T-3h | 0.616 | 0.384 | 0.172 | 5.98 | 3.35 | 2.63 | 227 (25/202) | CONFIRMED/CONFIRMED |
| LAK @ WSH | 2026-10-20T23:00:00Z | T-3h | 0.656 | 0.344 | 0.171 | 5.82 | 3.39 | 2.43 | 232 (25/207) | CONFIRMED/PROBABLE |
| TOR @ CBJ | 2026-10-20T23:00:00Z | T-3h | 0.648 | 0.352 | 0.160 | 6.19 | 3.58 | 2.62 | 231 (25/206) | CONFIRMED/CONFIRMED |
| WPG @ STL | 2026-10-21T00:00:00Z | T-3h | 0.603 | 0.397 | 0.174 | 5.87 | 3.25 | 2.62 | 224 (25/199) | CONFIRMED/CONFIRMED |
| BOS @ DAL | 2026-10-21T00:00:00Z | T-3h | 0.503 | 0.497 | 0.191 | 5.54 | 2.78 | 2.76 | 221 (25/196) | CONFIRMED/CONFIRMED |
| MIN @ EDM | 2026-10-21T01:00:00Z | T-6h | 0.568 | 0.432 | 0.171 | 6.42 | 3.42 | 3.00 | 243 (25/218) | PROJECTED/PROJECTED |
| DET @ SEA | 2026-10-21T01:40:00Z | T-6h | 0.585 | 0.415 | 0.176 | 5.98 | 3.26 | 2.72 | 210 (25/185) | CONFIRMED/CONFIRMED |
| CAR @ VAN | 2026-10-21T02:00:00Z | T-6h | 0.337 | 0.663 | 0.158 | 6.49 | 2.70 | 3.79 | 215 (25/190) | PROBABLE/PROBABLE |
| TBL @ VGK | 2026-10-21T02:30:00Z | T-6h | 0.539 | 0.461 | 0.181 | 5.92 | 3.08 | 2.84 | 239 (25/214) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET4 | team_total | 0.301 | 0.430 | 0.403 | 44 | 58 | no | +0.102 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET3 | team_total | 0.514 | 0.635 | 0.612 | 64 | 37 | no | +0.100 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL4 | team_total | 0.312 | 0.430 | 0.405 | 44 | 58 | no | +0.091 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL3 | team_total | 0.537 | 0.650 | 0.628 | 66 | 36 | no | +0.087 | OK |
| KXNHLTOTAL-26OCT20COLNJ-7 | game_total | 0.378 | 0.485 | 0.463 | 49 | 52 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ4 | team_total | 0.310 | 0.415 | 0.393 | 42 | 59 | no | +0.083 | OK |
| KXNHLTOTAL-26OCT20COLNJ-6 | game_total | 0.493 | 0.595 | 0.575 | 60 | 41 | no | +0.081 | OK |
| KXNHLGAME-26OCT20BOSDAL-BOS | game_winner | 0.497 | 0.395 | 0.415 | 40 | 61 | yes | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 | team_total | 0.526 | 0.625 | 0.606 | 63 | 38 | no | +0.078 | OK |
| KXNHLGAME-26OCT20DETSEA-SEA | game_winner | 0.585 | 0.485 | 0.505 | 49 | 52 | yes | +0.077 | OK |
| KXNHLGAME-26OCT20DETSEA-DET | game_winner | 0.415 | 0.515 | 0.495 | 52 | 49 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3 | team_total | 0.487 | 0.585 | 0.566 | 59 | 42 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4 | team_total | 0.457 | 0.555 | 0.536 | 56 | 45 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL3 | game_spread | 0.152 | 0.250 | 0.228 | 26 | 76 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET2 | game_spread | 0.211 | 0.305 | 0.284 | 31 | 70 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET2 | team_total | 0.748 | 0.835 | 0.820 | 84 | 17 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL2 | team_total | 0.760 | 0.850 | 0.835 | 86 | 16 | no | +0.071 | OK |
| KXNHLTOTAL-26OCT20COLNJ-5 | game_total | 0.718 | 0.810 | 0.794 | 82 | 20 | no | +0.070 | OK |
| KXNHLGAME-26OCT20BOSDAL-DAL | game_winner | 0.503 | 0.595 | 0.577 | 60 | 41 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL2 | game_spread | 0.275 | 0.365 | 0.346 | 37 | 64 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5 | team_total | 0.266 | 0.360 | 0.340 | 37 | 65 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT20SJMTL-7 | game_total | 0.444 | 0.535 | 0.517 | 54 | 47 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL5 | team_total | 0.150 | 0.240 | 0.220 | 25 | 77 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4 | team_total | 0.278 | 0.365 | 0.347 | 37 | 64 | no | +0.065 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET3 | game_spread | 0.116 | 0.195 | 0.176 | 20 | 81 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET5 | team_total | 0.145 | 0.230 | 0.210 | 24 | 78 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3 | team_total | 0.674 | 0.760 | 0.744 | 77 | 25 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT20SJMTL-6 | game_total | 0.553 | 0.635 | 0.619 | 64 | 37 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA3 | team_total | 0.443 | 0.525 | 0.508 | 53 | 48 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL3 | game_spread | 0.245 | 0.325 | 0.308 | 33 | 68 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT20COLNJ-4 | game_total | 0.814 | 0.885 | 0.873 | 89 | 12 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-5 | game_total | 0.680 | 0.755 | 0.741 | 76 | 25 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ5 | team_total | 0.151 | 0.230 | 0.212 | 24 | 78 | no | +0.056 | OK |
| KXNHLGAME-26OCT20CARVAN-CAR | game_winner | 0.663 | 0.735 | 0.721 | 74 | 27 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT20COLNJ-8 | game_total | 0.203 | 0.275 | 0.259 | 28 | 73 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR3 | game_spread | 0.310 | 0.385 | 0.370 | 39 | 62 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR2 | team_total | 0.726 | 0.800 | 0.786 | 81 | 21 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT20DETSEA-7 | game_total | 0.410 | 0.490 | 0.474 | 50 | 52 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA2 | game_spread | 0.356 | 0.285 | 0.299 | 29 | 72 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT20SJMTL-5 | game_total | 0.769 | 0.840 | 0.827 | 85 | 17 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ2 | game_spread | 0.244 | 0.315 | 0.300 | 32 | 69 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA2 | team_total | 0.686 | 0.755 | 0.742 | 76 | 25 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT20DETSEA-6 | game_total | 0.523 | 0.595 | 0.581 | 60 | 41 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ2 | team_total | 0.760 | 0.830 | 0.817 | 84 | 18 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB4 | team_total | 0.324 | 0.395 | 0.380 | 40 | 61 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB3 | team_total | 0.547 | 0.615 | 0.602 | 62 | 39 | no | +0.047 | OK |
| KXNHLGAME-26OCT20COLNJ-NJ | game_winner | 0.456 | 0.525 | 0.511 | 53 | 48 | no | +0.046 | OK |
| KXNHLGAME-26OCT20COLNJ-COL | game_winner | 0.544 | 0.475 | 0.489 | 48 | 53 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB2 | team_total | 0.764 | 0.825 | 0.814 | 83 | 18 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT20LAWSH-WSH2 | game_spread | 0.421 | 0.355 | 0.368 | 36 | 65 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ3 | game_spread | 0.135 | 0.195 | 0.181 | 20 | 81 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT20DETSEA-5 | game_total | 0.745 | 0.810 | 0.798 | 82 | 20 | no | +0.044 | OK |
| KXNHLGAME-26OCT20CARVAN-VAN | game_winner | 0.337 | 0.275 | 0.287 | 28 | 73 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT20TBVGK-5 | game_total | 0.736 | 0.795 | 0.784 | 80 | 21 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL2 | team_total | 0.851 | 0.905 | 0.896 | 91 | 10 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL2 | game_spread | 0.381 | 0.445 | 0.432 | 45 | 56 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL6 | team_total | 0.128 | 0.185 | 0.172 | 19 | 82 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20SJMTL-4 | game_total | 0.852 | 0.905 | 0.896 | 91 | 10 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20TBVGK-6 | game_total | 0.512 | 0.575 | 0.562 | 58 | 43 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20TBVGK-7 | game_total | 0.402 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20SJMTL-8 | game_total | 0.254 | 0.320 | 0.306 | 33 | 69 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR2 | game_spread | 0.452 | 0.515 | 0.502 | 52 | 49 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-WPG2 | game_spread | 0.197 | 0.255 | 0.242 | 26 | 75 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT20LAWSH-LA2 | game_spread | 0.159 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLGAME-26OCT20LAWSH-WSH | game_winner | 0.656 | 0.595 | 0.608 | 60 | 41 | yes | +0.040 | OK |
| KXNHLGAME-26OCT20LAWSH-LA | game_winner | 0.344 | 0.405 | 0.392 | 41 | 60 | no | +0.040 | OK |
| KXNHLGAME-26OCT20SJMTL-SJ | game_winner | 0.395 | 0.335 | 0.347 | 34 | 67 | yes | +0.039 | OK |
| KXNHLGAME-26OCT20SJMTL-MTL | game_winner | 0.605 | 0.665 | 0.653 | 67 | 34 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA4 | team_total | 0.237 | 0.300 | 0.287 | 31 | 71 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-BOS2 | game_spread | 0.270 | 0.215 | 0.225 | 22 | 79 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-7 | game_total | 0.336 | 0.395 | 0.383 | 40 | 61 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR2 | game_spread | 0.171 | 0.225 | 0.213 | 23 | 78 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT20TORCBJ-7 | game_total | 0.447 | 0.505 | 0.493 | 51 | 50 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-4 | game_total | 0.786 | 0.835 | 0.826 | 84 | 17 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB5 | team_total | 0.165 | 0.220 | 0.208 | 23 | 79 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-6 | game_total | 0.449 | 0.505 | 0.494 | 51 | 50 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2 | team_total | 0.738 | 0.685 | 0.696 | 69 | 32 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT20LAWSH-LA3 | game_spread | 0.080 | 0.130 | 0.118 | 14 | 88 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-CBJ2 | game_spread | 0.429 | 0.375 | 0.386 | 38 | 63 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR3 | game_spread | 0.090 | 0.135 | 0.125 | 14 | 87 | no | +0.032 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 0.605 | 0.610 | 0.177 | 0.206 | 6.17 | 6.25 | 0.943/1.024 | KXNHLTOTAL-26OCT20SJMTL-7 +0.016 |
| COL @ NJD | 0.456 | 0.483 | 0.180 | 0.219 | 5.79 | 6.15 | 0.984/0.971 | KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 +0.066 |
| ANA @ NYI | 0.616 | 0.578 | 0.172 | 0.215 | 5.98 | 6.36 | 0.947/1.016 | KXNHLTOTAL-26OCT20ANANYI-7 +0.074 |
| LAK @ WSH | 0.656 | 0.577 | 0.171 | 0.217 | 5.82 | 5.90 | 0.938/0.994 | KXNHLGAME-26OCT20LAWSH-LA +0.079 |
| TOR @ CBJ | 0.648 | 0.620 | 0.160 | 0.217 | 6.19 | 5.99 | 0.946/0.956 | KXNHLTEAMTOTAL-26OCT20TORCBJ-CBJ5 -0.049 |
| WPG @ STL | 0.603 | 0.597 | 0.174 | 0.214 | 5.87 | 6.23 | 0.977/1.003 | KXNHLTOTAL-26OCT20WPGSTL-7 +0.065 |
| BOS @ DAL | 0.503 | 0.527 | 0.191 | 0.220 | 5.54 | 6.21 | 0.994/0.956 | KXNHLTOTAL-26OCT20BOSDAL-7 +0.121 |
| MIN @ EDM | 0.568 | 0.595 | 0.171 | 0.206 | 6.42 | 6.68 | 0.994/0.995 | KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4 +0.054 |
| DET @ SEA | 0.585 | 0.572 | 0.176 | 0.217 | 5.98 | 6.26 | 1.023/1.024 | KXNHLTOTAL-26OCT20DETSEA-7 +0.055 |
| CAR @ VAN | 0.337 | 0.437 | 0.158 | 0.208 | 6.49 | 6.51 | 1.030/1.000 | KXNHLSPREAD-26OCT20CARVAN-CAR2 -0.113 |
| TBL @ VGK | 0.539 | 0.583 | 0.181 | 0.217 | 5.92 | 6.09 | 1.003/0.952 | KXNHLTEAMTOTAL-26OCT20TBVGK-VGK3 +0.055 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 40 recommended · full analysis in card.md / packet.json `thesis_card`

- Mason Marchment: 1+ goals YES @ 18c · p 0.2285 (adj 0.2151) · $2.43 · thesis SJS:OFFENSE_4PLUS
- Cole Caufield: 1+ goals NO @ 54c · p 0.6055 (adj 0.5879) · $4.99 · thesis MTL:SUPPRESSED
- Montreal over 3.5 goals scored NO @ 45c · p 0.5321 (adj 0.4885) · $2.11 · thesis MTL:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 74c · p 0.7935 (adj 0.7642) · $4.18 · thesis SJS:SUPPRESSED
- Cale Makar: 1+ assists NO @ 45c · p 0.6011 (adj 0.4996) · $5.11 · thesis COL:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 64c · p 0.7039 (adj 0.6867) · $6.08 · thesis NJD:SUPPRESSED
- Nico Hischier: 1+ goals NO @ 71c · p 0.7486 (adj 0.7377) · $3.77 · thesis NJD:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 13c · p 0.2121 (adj 0.1903) · $4.41 · thesis ANA:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 15c · p 0.1964 (adj 0.1823) · $2.08 · thesis NYI:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.129 (adj 0.1205) · $1.28 · thesis ANA:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2403 (adj 0.2215) · $3.85 · thesis WSH:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 54c · p 0.6642 (adj 0.577) · $3.87 · thesis LAK:SUPPRESSED
- Ryan Leonard: 1+ assists YES @ 31c · p 0.3762 (adj 0.3381) · $1.35 · thesis WSH:OFFENSE_4PLUS
- Jordan Kyrou: 1+ assists NO @ 67c · p 0.7271 (adj 0.6961) · $3.53 · thesis WSH:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 23c · p 0.2927 (adj 0.2758) · $3.42 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 18c · p 0.2327 (adj 0.217) · $2.55 · thesis CBJ:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 80c · p 0.8448 (adj 0.8323) · $6.15 · thesis TOR:SUPPRESSED
- Full Game: Over 6.5 goals scored NO @ 50c · p 0.5801 (adj 0.5375) · $4.29 · thesis GAME:LOW_EVENT
- Robert Thomas: 1+ goals YES @ 24c · p 0.2981 (adj 0.2811) · $2.97 · thesis STL:OFFENSE_4PLUS
- Gabriel Vilardi: 1+ goals YES @ 23c · p 0.2677 (adj 0.257) · $1.6 · thesis WPG:OFFENSE_4PLUS
- Dalibor Dvorsky: 1+ goals NO @ 82c · p 0.8493 (adj 0.8407) · $5.21 · thesis STL:SUPPRESSED
- Boston over 4.5 goals scored YES @ 13c · p 0.1997 (adj 0.1623) · $1.5 · thesis BOS:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7354 (adj 0.7203) · $6.56 · thesis DAL:SUPPRESSED
- Boston over 2.5 goals scored YES @ 51c · p 0.5983 (adj 0.5516) · $1.92 · thesis BOS:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 13c · p 0.1915 (adj 0.1736) · $3.13 · thesis EDM:OFFENSE_4PLUS
- Quinn Hughes: 1+ assists NO @ 39c · p 0.4831 (adj 0.434) · $3.83 · thesis MIN:SUPPRESSED
- Connor McDavid: 3+ assists NO @ 89c · p 0.9423 (adj 0.9112) · $6.56 · thesis EDM:SUPPRESSED
- Zach Hyman: 1+ goals YES @ 32c · p 0.3697 (adj 0.3548) · $2.53 · thesis EDM:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 12c · p 0.1691 (adj 0.1556) · $2.26 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 11c · p 0.1534 (adj 0.1413) · $1.94 · thesis SEA:OFFENSE_4PLUS
- Moritz Seider: 1+ goals NO @ 85c · p 0.9008 (adj 0.8843) · $6.48 · thesis DET:SUPPRESSED
- Detroit wins by over 1.5 goals NO @ 70c · p 0.7853 (adj 0.7402) · $5.73 · thesis SEA:WINS
- Drew O'Connor: 1+ goals YES @ 12c · p 0.1781 (adj 0.1623) · $2.9 · thesis VAN:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 18c · p 0.2497 (adj 0.2298) · $3.6 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 10c · p 0.1446 (adj 0.1322) · $2.12 · thesis VAN:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 62c · p 0.6788 (adj 0.6616) · $5.41 · thesis CAR:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 4c · p 0.0802 (adj 0.0689) · $1.77 · thesis VGK:OFFENSE_4PLUS
- Nikita Kucherov: 1+ goals NO @ 63c · p 0.6958 (adj 0.6781) · $6.56 · thesis TBL:SUPPRESSED
- Brett Howden: 1+ goals YES @ 19c · p 0.2331 (adj 0.2198) · $1.75 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 72c · p 0.7669 (adj 0.7539) · $6.29 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ MTL** · priced 195/205 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 27.0, exp saves 23.53 (sd 6.48), pull risk 0.053
- SJS net: Alex Nedeljkovic (PROBABLE) exp shots 27.29, exp saves 23.18 (sd 6.64), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Nedeljkovic: 28+ saves | 0.244 | 0.460 | 51/59 | +0.149 |  |
| Sam Dickinson: 1+ assists | 0.208 | 0.075 | 14/99 | +0.060 | STANDARD |
| Michael Kesselring: 1+ points | 0.245 | 0.125 | 18/93 | +0.054 | STANDARD |
| Nick Suzuki: 1+ assists | 0.480 | 0.595 | 60/41 | +0.093 | STANDARD |
| Nick Suzuki: 2+ points | 0.279 | 0.385 | 40/63 | +0.074 | STANDARD |
| Sam Dickinson: 1+ points | 0.260 | 0.160 | 17/85 | +0.080 | STANDARD |

**COL @ NJD** · priced 181/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 29.27, exp saves 25.27 (sd 6.74), pull risk 0.061
- COL net: Scott Wedgewood (CONFIRMED) exp shots 28.54, exp saves 24.76 (sd 6.74), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.155 | 0.320 | 34/70 | +0.130 | STANDARD |
| Cale Makar: 1+ assists | 0.399 | 0.555 | 56/45 | +0.134 | STANDARD |
| Jack Hughes: 1+ assists | 0.389 | 0.535 | 55/48 | +0.114 | STANDARD |
| Luke Evangelista: 1+ points | 0.318 | 0.460 | 47/55 | +0.115 | STANDARD |
| Scott Wedgewood: 28+ saves | 0.330 | 0.470 | 48/54 | +0.113 |  |
| Jack Hughes: 2+ points | 0.205 | 0.340 | 36/68 | +0.100 | STANDARD |

**ANA @ NYI** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.2, exp saves 24.63 (sd 6.66), pull risk 0.053
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.37, exp saves 23.37 (sd 6.6), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ondrej Palat: 1+ assists | 0.237 | 0.105 | 20/99 | +0.026 | STANDARD |
| Lukas Dostal: 27+ saves | 0.310 | 0.435 | 45/58 | +0.093 |  |
| Ilya Sorokin: 23+ saves | 0.624 | 0.520 | 54/50 | +0.066 |  |
| Alex Killorn: 1+ points | 0.446 | 0.350 | 36/66 | +0.069 | STANDARD |
| A.J. Greer: 1+ goals | 0.212 | 0.125 | 13/88 | +0.074 | STANDARD |
| Alex Killorn: 1+ assists | 0.308 | 0.225 | 25/80 | +0.045 | STANDARD |

**LAK @ WSH** · priced 171/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.19, exp saves 24.65 (sd 6.48), pull risk 0.046
- LAK net: Darcy Kuemper (PROBABLE) exp shots 26.88, exp saves 22.97 (sd 6.41), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darcy Kuemper: 27+ saves | 0.282 | 0.430 | 44/58 | +0.121 |  |
| Artemi Panarin: 1+ assists | 0.336 | 0.470 | 48/54 | +0.107 | STANDARD |
| Joel Edmundson: 1+ assists | 0.194 | 0.080 | 15/99 | +0.035 | STANDARD |
| Joel Edmundson: 1+ points | 0.240 | 0.130 | 19/93 | +0.039 | STANDARD |
| Artemi Panarin: 2+ points | 0.162 | 0.265 | 28/75 | +0.075 | STANDARD |
| Artemi Panarin: 1+ points | 0.513 | 0.615 | 63/40 | +0.070 | STANDARD |

**TOR @ CBJ** · priced 164/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (CONFIRMED) exp shots 25.9, exp saves 22.95 (sd 6.05), pull risk 0.037
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.4, exp saves 26.78 (sd 7.15), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.345 | 0.455 | 46/55 | +0.088 | STANDARD |
| Jet Greaves: 25+ saves | 0.385 | 0.490 | 51/53 | +0.068 |  |
| Auston Matthews: 1+ points | 0.559 | 0.660 | 67/35 | +0.075 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.277 | 0.375 | 39/64 | +0.067 | STANDARD |
| Kirill Marchenko: 1+ points | 0.458 | 0.550 | 56/46 | +0.065 | STANDARD |
| Auston Matthews: 2+ points | 0.201 | 0.290 | 30/72 | +0.065 | STANDARD |

**WPG @ STL** · priced 170/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 26.09, exp saves 22.93 (sd 6.2), pull risk 0.048
- WPG net: Stuart Skinner (CONFIRMED) exp shots 26.62, exp saves 22.57 (sd 6.42), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Philip Broberg: 1+ points | 0.467 | 0.365 | 38/65 | +0.070 | STANDARD |
| Jake Neighbours: 1+ assists | 0.322 | 0.235 | 26/79 | +0.049 | STANDARD |
| Philip Broberg: 1+ assists | 0.411 | 0.335 | 35/68 | +0.046 | STANDARD |
| Robert Thomas: 1+ goals | 0.298 | 0.230 | 24/78 | +0.045 | STANDARD |
| Pavel Buchnevich: 1+ assists | 0.257 | 0.325 | 34/69 | +0.038 | STANDARD |
| Alex Iafallo: 1+ assists | 0.252 | 0.185 | 21/84 | +0.030 | STANDARD |

**BOS @ DAL** · priced 162/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.49, exp saves 21.25 (sd 6.05), pull risk 0.059
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.85, exp saves 24.03 (sd 6.59), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.226 | 0.330 | 35/69 | +0.069 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.441 | 0.535 | 55/48 | +0.061 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.346 | 0.425 | 44/59 | +0.047 | STANDARD |
| Miro Heiskanen: 1+ points | 0.471 | 0.550 | 56/46 | +0.051 | STANDARD |
| Morgan Geekie: 2+ points | 0.179 | 0.100 | 16/96 | +0.009 | STANDARD |
| Thomas Harley: 1+ points | 0.445 | 0.370 | 39/65 | +0.038 | STANDARD |

**MIN @ EDM** · priced 189/192 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.88, exp saves 24.28 (sd 6.69), pull risk 0.064
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 24.81 (sd 7.09), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonas Brodin: 1+ assists | 0.244 | 0.105 | 20/99 | +0.033 | STANDARD |
| Connor McDavid: 2+ assists | 0.219 | 0.335 | 35/68 | +0.086 | STANDARD |
| Alex Formenton: 1+ points | 0.334 | 0.225 | 24/79 | +0.081 | STANDARD |
| Mathieu Joseph: 1+ points | 0.258 | 0.150 | 21/91 | +0.037 | STANDARD |
| Zach Bogosian: 1+ points | 0.223 | 0.115 | 18/95 | +0.033 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.233 | 0.125 | 20/95 | +0.022 | STANDARD |

**DET @ SEA** · priced 150/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (CONFIRMED) exp shots 29.42, exp saves 25.64 (sd 6.73), pull risk 0.054
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.75, exp saves 22.88 (sd 6.51), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Moritz Seider: 1+ points | 0.462 | 0.590 | 60/42 | +0.101 | STANDARD |
| Moritz Seider: 2+ points | 0.127 | 0.240 | 27/79 | +0.071 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.352 | 0.245 | 27/78 | +0.069 | STANDARD |
| Moritz Seider: 1+ assists | 0.401 | 0.505 | 52/51 | +0.071 | STANDARD |
| Kaapo Kakko: 1+ points | 0.491 | 0.390 | 41/63 | +0.064 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.255 | 0.345 | 37/68 | +0.050 | STANDARD |

**CAR @ VAN** · priced 156/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 32.33, exp saves 27.65 (sd 7.44), pull risk 0.077
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 22.8, exp saves 19.96 (sd 5.7), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.222 | 0.335 | 35/68 | +0.083 | STANDARD |
| Sebastian Aho: 1+ assists | 0.391 | 0.495 | 51/52 | +0.072 | STANDARD |
| Bradly Nadeau: 1+ assists | 0.155 | 0.250 | 28/78 | +0.053 | STANDARD |
| Sean Walker: 1+ assists | 0.351 | 0.260 | 29/77 | +0.046 | STANDARD |
| Nikolaj Ehlers: 1+ points | 0.509 | 0.600 | 62/42 | +0.054 | STANDARD |
| Nikolaj Ehlers: 2+ points | 0.161 | 0.245 | 27/78 | +0.047 | STANDARD |

**TBL @ VGK** · priced 183/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.99, exp saves 23.6 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.35, exp saves 22.57 (sd 6.35), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.437 | 0.570 | 58/44 | +0.106 | STANDARD |
| John Carlson: 1+ assists | 0.271 | 0.400 | 42/62 | +0.093 | STANDARD |
| Nikita Kucherov: 2+ points | 0.243 | 0.370 | 38/64 | +0.101 | STANDARD |
| John Carlson: 1+ points | 0.341 | 0.455 | 46/55 | +0.092 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.115 | 0.205 | 21/80 | +0.073 | STANDARD |
| Jack Eichel: 1+ assists | 0.444 | 0.530 | 54/48 | +0.059 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
