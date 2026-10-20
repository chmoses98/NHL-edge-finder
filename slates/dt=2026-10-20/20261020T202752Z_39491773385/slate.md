# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-20T20:27:52Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4565 · contracts joined: 2668 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2393, 'OK': 187, 'NO_EDGE': 88}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 434, 'game_early_goal': 11, 'first_goal': 398, 'game_winner': 22, 'player_goals': 692, 'game_overtime': 11, 'player_points': 561, 'goalie_saves': 22, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 2026-10-20T23:00:00Z | T-90m | 0.605 | 0.395 | 0.177 | 6.17 | 3.42 | 2.75 | 256 (25/231) | CONFIRMED/PROBABLE |
| COL @ NJD | 2026-10-20T23:00:00Z | T-90m | 0.456 | 0.544 | 0.180 | 5.79 | 2.77 | 3.02 | 241 (25/216) | CONFIRMED/CONFIRMED |
| ANA @ NYI | 2026-10-20T23:00:00Z | T-90m | 0.616 | 0.384 | 0.172 | 5.98 | 3.35 | 2.63 | 233 (25/208) | CONFIRMED/CONFIRMED |
| LAK @ WSH | 2026-10-20T23:00:00Z | T-90m | 0.656 | 0.344 | 0.171 | 5.82 | 3.39 | 2.43 | 251 (25/226) | CONFIRMED/PROBABLE |
| TOR @ CBJ | 2026-10-20T23:00:00Z | T-90m | 0.648 | 0.352 | 0.160 | 6.19 | 3.58 | 2.62 | 238 (25/213) | CONFIRMED/CONFIRMED |
| WPG @ STL | 2026-10-21T00:00:00Z | T-3h | 0.603 | 0.397 | 0.174 | 5.87 | 3.25 | 2.62 | 260 (25/235) | CONFIRMED/CONFIRMED |
| BOS @ DAL | 2026-10-21T00:00:00Z | T-3h | 0.503 | 0.497 | 0.191 | 5.54 | 2.78 | 2.76 | 221 (25/196) | CONFIRMED/CONFIRMED |
| MIN @ EDM | 2026-10-21T01:00:00Z | T-3h | 0.561 | 0.439 | 0.174 | 6.39 | 3.39 | 3.00 | 245 (25/220) | PROBABLE/PROBABLE |
| DET @ SEA | 2026-10-21T01:40:00Z | T-3h | 0.585 | 0.415 | 0.176 | 5.98 | 3.26 | 2.72 | 236 (25/211) | CONFIRMED/CONFIRMED |
| CAR @ VAN | 2026-10-21T02:00:00Z | T-3h | 0.337 | 0.663 | 0.158 | 6.49 | 2.70 | 3.79 | 244 (25/219) | PROBABLE/PROBABLE |
| TBL @ VGK | 2026-10-21T02:30:00Z | T-6h | 0.539 | 0.461 | 0.181 | 5.92 | 3.08 | 2.84 | 243 (25/218) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET4 | team_total | 0.301 | 0.430 | 0.403 | 44 | 58 | no | +0.102 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET3 | team_total | 0.514 | 0.640 | 0.616 | 65 | 37 | no | +0.100 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL4 | team_total | 0.312 | 0.425 | 0.401 | 43 | 58 | no | +0.091 | OK |
| KXNHLGAME-26OCT20DETSEA-DET | game_winner | 0.415 | 0.525 | 0.503 | 53 | 48 | no | +0.087 | OK |
| KXNHLGAME-26OCT20DETSEA-SEA | game_winner | 0.585 | 0.475 | 0.497 | 48 | 53 | yes | +0.087 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL3 | team_total | 0.537 | 0.650 | 0.628 | 66 | 36 | no | +0.087 | OK |
| KXNHLTOTAL-26OCT20COLNJ-7 | game_total | 0.378 | 0.485 | 0.463 | 49 | 52 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET2 | game_spread | 0.211 | 0.315 | 0.292 | 32 | 69 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ4 | team_total | 0.310 | 0.415 | 0.393 | 42 | 59 | no | +0.083 | OK |
| KXNHLTOTAL-26OCT20COLNJ-6 | game_total | 0.493 | 0.595 | 0.575 | 60 | 41 | no | +0.081 | OK |
| KXNHLGAME-26OCT20BOSDAL-BOS | game_winner | 0.497 | 0.395 | 0.415 | 40 | 61 | yes | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 | team_total | 0.526 | 0.625 | 0.606 | 63 | 38 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3 | team_total | 0.487 | 0.585 | 0.566 | 59 | 42 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4 | team_total | 0.457 | 0.560 | 0.540 | 57 | 45 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL3 | game_spread | 0.152 | 0.245 | 0.224 | 25 | 76 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET2 | team_total | 0.748 | 0.835 | 0.820 | 84 | 17 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL2 | team_total | 0.760 | 0.850 | 0.835 | 86 | 16 | no | +0.071 | OK |
| KXNHLTOTAL-26OCT20COLNJ-5 | game_total | 0.718 | 0.810 | 0.794 | 82 | 20 | no | +0.070 | OK |
| KXNHLGAME-26OCT20BOSDAL-DAL | game_winner | 0.503 | 0.595 | 0.577 | 60 | 41 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL2 | game_spread | 0.275 | 0.365 | 0.346 | 37 | 64 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5 | team_total | 0.266 | 0.360 | 0.340 | 37 | 65 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT20SJMTL-7 | game_total | 0.444 | 0.535 | 0.517 | 54 | 47 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL5 | team_total | 0.150 | 0.240 | 0.220 | 25 | 77 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ5 | team_total | 0.151 | 0.235 | 0.216 | 24 | 77 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4 | team_total | 0.278 | 0.365 | 0.347 | 37 | 64 | no | +0.065 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET3 | game_spread | 0.116 | 0.195 | 0.176 | 20 | 81 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET5 | team_total | 0.145 | 0.235 | 0.214 | 25 | 78 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3 | team_total | 0.674 | 0.760 | 0.744 | 77 | 25 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT20DETSEA-7 | game_total | 0.410 | 0.495 | 0.478 | 50 | 51 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ2 | team_total | 0.760 | 0.835 | 0.822 | 84 | 17 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT20SJMTL-6 | game_total | 0.553 | 0.635 | 0.619 | 64 | 37 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA3 | team_total | 0.443 | 0.525 | 0.508 | 53 | 48 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL3 | game_spread | 0.245 | 0.325 | 0.308 | 33 | 68 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT20COLNJ-4 | game_total | 0.814 | 0.885 | 0.873 | 89 | 12 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-5 | game_total | 0.680 | 0.755 | 0.741 | 76 | 25 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT20DETSEA-5 | game_total | 0.745 | 0.815 | 0.802 | 82 | 19 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ3 | game_spread | 0.135 | 0.205 | 0.189 | 21 | 80 | no | +0.054 | OK |
| KXNHLGAME-26OCT20CARVAN-CAR | game_winner | 0.663 | 0.735 | 0.721 | 74 | 27 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT20COLNJ-8 | game_total | 0.203 | 0.275 | 0.259 | 28 | 73 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR3 | game_spread | 0.310 | 0.385 | 0.370 | 39 | 62 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR2 | team_total | 0.726 | 0.800 | 0.786 | 81 | 21 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA2 | game_spread | 0.356 | 0.285 | 0.299 | 29 | 72 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT20SJMTL-5 | game_total | 0.769 | 0.840 | 0.827 | 85 | 17 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ2 | game_spread | 0.244 | 0.315 | 0.300 | 32 | 69 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA2 | team_total | 0.686 | 0.755 | 0.742 | 76 | 25 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT20DETSEA-6 | game_total | 0.523 | 0.595 | 0.581 | 60 | 41 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB4 | team_total | 0.324 | 0.400 | 0.384 | 41 | 61 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB3 | team_total | 0.547 | 0.615 | 0.602 | 62 | 39 | no | +0.047 | OK |
| KXNHLGAME-26OCT20COLNJ-COL | game_winner | 0.544 | 0.475 | 0.489 | 48 | 53 | yes | +0.046 | OK |
| KXNHLGAME-26OCT20COLNJ-NJ | game_winner | 0.456 | 0.525 | 0.511 | 53 | 48 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB2 | team_total | 0.764 | 0.830 | 0.818 | 84 | 18 | no | +0.046 | OK |
| KXNHLGAME-26OCT20CARVAN-VAN | game_winner | 0.337 | 0.275 | 0.287 | 28 | 73 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT20TBVGK-5 | game_total | 0.736 | 0.795 | 0.784 | 80 | 21 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL2 | team_total | 0.851 | 0.905 | 0.896 | 91 | 10 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL2 | game_spread | 0.381 | 0.445 | 0.432 | 45 | 56 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL6 | team_total | 0.128 | 0.190 | 0.176 | 20 | 82 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20SJMTL-4 | game_total | 0.852 | 0.905 | 0.896 | 91 | 10 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20TBVGK-6 | game_total | 0.512 | 0.575 | 0.562 | 58 | 43 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20SJMTL-8 | game_total | 0.254 | 0.320 | 0.306 | 33 | 69 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR2 | game_spread | 0.452 | 0.515 | 0.502 | 52 | 49 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-WPG2 | game_spread | 0.197 | 0.255 | 0.242 | 26 | 75 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT20DETSEA-4 | game_total | 0.833 | 0.885 | 0.876 | 89 | 12 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT20LAWSH-LA2 | game_spread | 0.159 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLGAME-26OCT20LAWSH-LA | game_winner | 0.344 | 0.405 | 0.392 | 41 | 60 | no | +0.040 | OK |
| KXNHLGAME-26OCT20LAWSH-WSH | game_winner | 0.656 | 0.595 | 0.608 | 60 | 41 | yes | +0.040 | OK |
| KXNHLGAME-26OCT20SJMTL-MTL | game_winner | 0.605 | 0.665 | 0.653 | 67 | 34 | no | +0.039 | OK |
| KXNHLGAME-26OCT20SJMTL-SJ | game_winner | 0.395 | 0.335 | 0.347 | 34 | 67 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA4 | team_total | 0.237 | 0.300 | 0.287 | 31 | 71 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT20TORCBJ-5 | game_total | 0.771 | 0.825 | 0.815 | 83 | 18 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR5 | team_total | 0.131 | 0.185 | 0.173 | 19 | 82 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-BOS2 | game_spread | 0.270 | 0.215 | 0.225 | 22 | 79 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-7 | game_total | 0.336 | 0.395 | 0.383 | 40 | 61 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR2 | game_spread | 0.171 | 0.225 | 0.213 | 23 | 78 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT20DETSEA-8 | game_total | 0.229 | 0.285 | 0.273 | 29 | 72 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-4 | game_total | 0.786 | 0.840 | 0.830 | 85 | 17 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT20LAWSH-WSH2 | game_spread | 0.421 | 0.365 | 0.376 | 37 | 64 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-6 | game_total | 0.449 | 0.505 | 0.494 | 51 | 50 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT20LAWSH-LA3 | game_spread | 0.080 | 0.125 | 0.114 | 13 | 88 | no | +0.033 | OK |
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
| MIN @ EDM | 0.561 | 0.594 | 0.174 | 0.207 | 6.39 | 6.68 | 0.994/0.993 | KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4 +0.058 |
| DET @ SEA | 0.585 | 0.572 | 0.176 | 0.217 | 5.98 | 6.26 | 1.023/1.024 | KXNHLTOTAL-26OCT20DETSEA-7 +0.055 |
| CAR @ VAN | 0.337 | 0.437 | 0.158 | 0.208 | 6.49 | 6.51 | 1.030/1.000 | KXNHLSPREAD-26OCT20CARVAN-CAR2 -0.113 |
| TBL @ VGK | 0.539 | 0.583 | 0.181 | 0.217 | 5.92 | 6.09 | 1.003/0.952 | KXNHLTEAMTOTAL-26OCT20TBVGK-VGK3 +0.055 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 42 recommended · full analysis in card.md / packet.json `thesis_card`

- Mason Marchment: 1+ goals YES @ 18c · p 0.2285 (adj 0.2151) · $2.34 · thesis SJS:OFFENSE_4PLUS
- Cole Caufield: 2+ goals NO @ 87c · p 0.9097 (adj 0.8973) · $6.3 · thesis MTL:SUPPRESSED
- Cole Caufield: 1+ goals NO @ 55c · p 0.6055 (adj 0.5904) · $3.22 · thesis MTL:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 74c · p 0.7935 (adj 0.7642) · $3.99 · thesis SJS:SUPPRESSED
- Cale Makar: 1+ assists NO @ 45c · p 0.6011 (adj 0.4996) · $4.36 · thesis COL:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 64c · p 0.7039 (adj 0.6867) · $5.59 · thesis NJD:SUPPRESSED
- Cody Glass: 1+ goals YES @ 11c · p 0.15 (adj 0.1375) · $1.52 · thesis NJD:OFFENSE_4PLUS
- Jack Hughes: 1+ assists NO @ 47c · p 0.611 (adj 0.5161) · $3.94 · thesis NJD:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 13c · p 0.2121 (adj 0.1903) · $4.26 · thesis ANA:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 15c · p 0.1964 (adj 0.1835) · $2.14 · thesis NYI:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.129 (adj 0.1205) · $1.24 · thesis ANA:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2403 (adj 0.2215) · $3.72 · thesis WSH:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 54c · p 0.6642 (adj 0.577) · $3.75 · thesis LAK:SUPPRESSED
- Ryan Leonard: 1+ assists YES @ 31c · p 0.3762 (adj 0.3381) · $1.3 · thesis WSH:OFFENSE_4PLUS
- Jordan Kyrou: 1+ assists NO @ 67c · p 0.7271 (adj 0.6961) · $3.42 · thesis WSH:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 23c · p 0.2927 (adj 0.2758) · $2.98 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 18c · p 0.2327 (adj 0.217) · $2.2 · thesis CBJ:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 80c · p 0.8448 (adj 0.8323) · $5.26 · thesis TOR:SUPPRESSED
- Jack Roslovic: 1+ goals NO @ 77c · p 0.8089 (adj 0.7979) · $4.27 · thesis TOR:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 23c · p 0.2981 (adj 0.2773) · $2.96 · thesis STL:OFFENSE_4PLUS
- Jake Neighbours: 1+ assists YES @ 24c · p 0.3222 (adj 0.2786) · $2.27 · thesis STL:OFFENSE_4PLUS
- Philip Broberg: 1+ assists YES @ 33c · p 0.4115 (adj 0.3682) · $2.02 · thesis STL:OFFENSE_4PLUS
- Dalibor Dvorsky: 1+ goals NO @ 82c · p 0.8493 (adj 0.8407) · $6.35 · thesis STL:SUPPRESSED
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7354 (adj 0.7203) · $6.35 · thesis DAL:SUPPRESSED
- Boston over 2.5 goals scored YES @ 51c · p 0.5983 (adj 0.5516) · $4.24 · thesis BOS:OFFENSE_4PLUS
- Charlie McAvoy: 1+ assists NO @ 59c · p 0.6544 (adj 0.6172) · $4.05 · thesis BOS:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 13c · p 0.1898 (adj 0.1724) · $2.74 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 32c · p 0.4097 (adj 0.3623) · $4.48 · thesis EDM:SUPPRESSED
- Zach Hyman: 1+ goals YES @ 32c · p 0.3749 (adj 0.3587) · $3.07 · thesis EDM:OFFENSE_4PLUS
- Edmonton over 2.5 goals scored YES @ 65c · p 0.7184 (adj 0.6817) · $3.71 · thesis EDM:OFFENSE_4PLUS
- Adam Larsson: 1+ assists YES @ 18c · p 0.3134 (adj 0.2234) · $2.16 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 11c · p 0.1534 (adj 0.1413) · $1.86 · thesis SEA:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 68c · p 0.7414 (adj 0.7248) · $6.35 · thesis DET:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 13c · p 0.1691 (adj 0.1581) · $1.57 · thesis SEA:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 18c · p 0.2497 (adj 0.231) · $3.44 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 17c · p 0.2316 (adj 0.215) · $2.92 · thesis VAN:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 62c · p 0.778 (adj 0.6721) · $6.35 · thesis VAN:WINS
- Sean Walker: 1+ assists YES @ 28c · p 0.3509 (adj 0.3105) · $2.1 · thesis CAR:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 4c · p 0.0802 (adj 0.0689) · $1.71 · thesis VGK:OFFENSE_4PLUS
- Brett Howden: 1+ goals YES @ 19c · p 0.2331 (adj 0.2211) · $1.84 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 72c · p 0.7669 (adj 0.7539) · $6.08 · thesis VGK:SUPPRESSED
- Nikita Kucherov: 1+ goals NO @ 65c · p 0.6958 (adj 0.6831) · $3.91 · thesis TBL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ MTL** · priced 195/205 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 27.0, exp saves 23.53 (sd 6.48), pull risk 0.053
- SJS net: Alex Nedeljkovic (PROBABLE) exp shots 27.29, exp saves 23.18 (sd 6.64), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Nedeljkovic: 28+ saves | 0.244 | 0.460 | 51/59 | +0.149 |  |
| Sam Dickinson: 1+ assists | 0.208 | 0.075 | 14/99 | +0.060 | STANDARD |
| Nick Suzuki: 1+ assists | 0.480 | 0.595 | 60/41 | +0.093 | STANDARD |
| Nick Suzuki: 2+ points | 0.279 | 0.380 | 39/63 | +0.074 | STANDARD |
| Michael Kesselring: 1+ points | 0.245 | 0.145 | 18/89 | +0.054 | STANDARD |
| Phillip Danault: 1+ assists | 0.197 | 0.100 | 19/99 | -0.003 | STANDARD |

**COL @ NJD** · priced 184/190 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 29.27, exp saves 25.27 (sd 6.74), pull risk 0.061
- COL net: Scott Wedgewood (CONFIRMED) exp shots 28.54, exp saves 24.76 (sd 6.74), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.155 | 0.320 | 33/69 | +0.140 | STANDARD |
| Cale Makar: 1+ assists | 0.399 | 0.555 | 56/45 | +0.134 | STANDARD |
| Scott Wedgewood: 28+ saves | 0.330 | 0.485 | 50/53 | +0.123 |  |
| Jack Hughes: 1+ assists | 0.389 | 0.535 | 54/47 | +0.124 | STANDARD |
| Luke Evangelista: 1+ points | 0.318 | 0.460 | 47/55 | +0.115 | STANDARD |
| Cale Makar: 1+ points | 0.496 | 0.630 | 64/38 | +0.108 | STANDARD |

**ANA @ NYI** · priced 179/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.2, exp saves 24.63 (sd 6.66), pull risk 0.053
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.37, exp saves 23.37 (sd 6.6), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Washe: 1+ points | 0.322 | 0.130 | 24/98 | +0.070 | STANDARD |
| Judd Caulfield: 1+ points | 0.300 | 0.140 | 26/98 | +0.027 | PRIOR_HEAVY |
| Jeff Malott: 1+ points | 0.252 | 0.115 | 21/98 | +0.030 | STANDARD |
| Lukas Dostal: 27+ saves | 0.310 | 0.445 | 46/57 | +0.103 |  |
| Ondrej Palat: 1+ assists | 0.237 | 0.105 | 20/99 | +0.026 | STANDARD |
| Ilya Sorokin: 23+ saves | 0.624 | 0.495 | 51/52 | +0.096 |  |

**LAK @ WSH** · priced 190/200 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.19, exp saves 24.65 (sd 6.48), pull risk 0.046
- LAK net: Darcy Kuemper (PROBABLE) exp shots 26.88, exp saves 22.97 (sd 6.41), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Desharnais: 1+ points | 0.220 | 0.070 | 13/99 | +0.082 | STANDARD |
| Artemi Panarin: 1+ assists | 0.336 | 0.470 | 48/54 | +0.107 | STANDARD |
| Darcy Kuemper: 27+ saves | 0.282 | 0.415 | 42/59 | +0.111 |  |
| Vincent Desharnais: 1+ assists | 0.194 | 0.065 | 12/99 | +0.066 | STANDARD |
| Anthony Beauvillier: 1+ assists | 0.199 | 0.080 | 15/99 | +0.040 | STANDARD |
| Mikey Anderson: 1+ assists | 0.195 | 0.085 | 16/99 | +0.026 | STANDARD |

**TOR @ CBJ** · priced 171/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (CONFIRMED) exp shots 25.9, exp saves 22.95 (sd 6.05), pull risk 0.037
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.4, exp saves 26.78 (sd 7.15), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.345 | 0.455 | 46/55 | +0.088 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.277 | 0.370 | 38/64 | +0.067 | STANDARD |
| Kirill Marchenko: 1+ points | 0.458 | 0.550 | 56/46 | +0.065 | STANDARD |
| Auston Matthews: 1+ points | 0.559 | 0.650 | 66/36 | +0.064 | STANDARD |
| Jet Greaves: 25+ saves | 0.385 | 0.475 | 49/54 | +0.058 |  |
| Gavin McKenna: 1+ points | 0.340 | 0.425 | 44/59 | +0.053 | STANDARD |

**WPG @ STL** · priced 204/209 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 26.09, exp saves 22.93 (sd 6.2), pull risk 0.048
- WPG net: Stuart Skinner (CONFIRMED) exp shots 26.62, exp saves 22.57 (sd 6.42), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pius Suter: 1+ points | 0.346 | 0.215 | 30/87 | +0.032 | STANDARD |
| Morgan Barron: 1+ points | 0.260 | 0.140 | 27/99 | -0.024 | STANDARD |
| Dylan Samberg: 1+ assists | 0.232 | 0.115 | 22/99 | +0.000 | STANDARD |
| Cole Koepke: 1+ points | 0.208 | 0.105 | 20/99 | -0.003 | STANDARD |
| Philip Broberg: 1+ points | 0.467 | 0.365 | 37/64 | +0.080 | STANDARD |
| Mario Ferraro: 1+ points | 0.196 | 0.100 | 19/99 | -0.005 | STANDARD |

**BOS @ DAL** · priced 162/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.49, exp saves 21.25 (sd 6.05), pull risk 0.059
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.85, exp saves 24.03 (sd 6.59), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.226 | 0.325 | 34/69 | +0.069 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.441 | 0.525 | 53/48 | +0.061 | STANDARD |
| Thomas Harley: 1+ assists | 0.385 | 0.310 | 32/70 | +0.050 | STANDARD |
| Thomas Harley: 1+ points | 0.445 | 0.370 | 38/64 | +0.048 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.346 | 0.420 | 43/59 | +0.047 | STANDARD |
| Miro Heiskanen: 1+ points | 0.471 | 0.545 | 55/46 | +0.051 | STANDARD |

**MIN @ EDM** · priced 191/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROBABLE) exp shots 27.88, exp saves 24.36 (sd 6.6), pull risk 0.06
- MIN net: Jesper Wallstedt (PROBABLE) exp shots 29.26, exp saves 24.78 (sd 6.99), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonas Brodin: 1+ assists | 0.244 | 0.105 | 20/99 | +0.033 | STANDARD |
| Alex Formenton: 1+ points | 0.339 | 0.225 | 24/79 | +0.086 | STANDARD |
| Connor McDavid: 2+ assists | 0.221 | 0.335 | 35/68 | +0.083 | STANDARD |
| Mathieu Joseph: 1+ points | 0.262 | 0.160 | 21/89 | +0.041 | STANDARD |
| Mathieu Joseph: 1+ assists | 0.182 | 0.080 | 15/99 | +0.023 | STANDARD |
| Kasperi Kapanen: 1+ points | 0.423 | 0.325 | 33/68 | +0.078 | STANDARD |

**DET @ SEA** · priced 176/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (CONFIRMED) exp shots 29.42, exp saves 25.64 (sd 6.73), pull risk 0.054
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.75, exp saves 22.88 (sd 6.51), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Larsson: 1+ assists | 0.313 | 0.175 | 18/83 | +0.123 | STANDARD |
| Adam Larsson: 1+ points | 0.358 | 0.240 | 25/77 | +0.095 | STANDARD |
| Moritz Seider: 1+ points | 0.462 | 0.575 | 58/43 | +0.091 | STANDARD |
| Ben Chiarot: 1+ points | 0.288 | 0.175 | 21/86 | +0.066 | STANDARD |
| Moritz Seider: 2+ points | 0.127 | 0.235 | 26/79 | +0.071 | STANDARD |
| Moritz Seider: 1+ assists | 0.401 | 0.500 | 51/51 | +0.071 | STANDARD |

**CAR @ VAN** · priced 177/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 32.33, exp saves 27.65 (sd 7.44), pull risk 0.077
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 22.8, exp saves 19.96 (sd 5.7), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Eric Robinson: 1+ points | 0.356 | 0.195 | 29/90 | +0.052 | STANDARD |
| Drew O'Connor: 1+ points | 0.337 | 0.195 | 25/86 | +0.074 | STANDARD |
| Bradly Nadeau: 1+ assists | 0.143 | 0.260 | 28/76 | +0.084 | STANDARD |
| Eric Robinson: 1+ assists | 0.211 | 0.095 | 18/99 | +0.021 | STANDARD |
| Sebastian Aho: 2+ points | 0.225 | 0.340 | 35/67 | +0.089 | STANDARD |
| Sebastian Aho: 1+ assists | 0.396 | 0.500 | 51/51 | +0.076 | STANDARD |

**TBL @ VGK** · priced 187/192 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.99, exp saves 23.6 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.35, exp saves 22.57 (sd 6.35), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brayden McNabb: 1+ points | 0.327 | 0.155 | 29/98 | +0.023 | STANDARD |
| Andrei Vasilevskiy: 27+ saves | 0.256 | 0.415 | 44/61 | +0.118 |  |
| Nikita Kucherov: 1+ assists | 0.437 | 0.570 | 58/44 | +0.106 | STANDARD |
| Brayden McNabb: 1+ assists | 0.270 | 0.140 | 27/99 | -0.013 | STANDARD |
| Nikita Kucherov: 2+ points | 0.243 | 0.370 | 38/64 | +0.101 | STANDARD |
| John Carlson: 1+ assists | 0.271 | 0.370 | 38/64 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
