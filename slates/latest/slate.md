# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-20T19:32:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4471 · contracts joined: 2574 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2299, 'OK': 190, 'NO_EDGE': 85}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 393, 'game_early_goal': 11, 'first_goal': 398, 'game_winner': 22, 'player_goals': 691, 'game_overtime': 11, 'player_points': 510, 'goalie_saves': 21, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 2026-10-20T23:00:00Z | T-3h | 0.605 | 0.395 | 0.177 | 6.17 | 3.42 | 2.75 | 256 (25/231) | CONFIRMED/PROBABLE |
| COL @ NJD | 2026-10-20T23:00:00Z | T-3h | 0.456 | 0.544 | 0.180 | 5.79 | 2.77 | 3.02 | 241 (25/216) | CONFIRMED/CONFIRMED |
| ANA @ NYI | 2026-10-20T23:00:00Z | T-3h | 0.616 | 0.384 | 0.172 | 5.98 | 3.35 | 2.63 | 227 (25/202) | CONFIRMED/CONFIRMED |
| LAK @ WSH | 2026-10-20T23:00:00Z | T-3h | 0.656 | 0.344 | 0.171 | 5.82 | 3.39 | 2.43 | 239 (25/214) | CONFIRMED/PROBABLE |
| TOR @ CBJ | 2026-10-20T23:00:00Z | T-3h | 0.648 | 0.352 | 0.160 | 6.19 | 3.58 | 2.62 | 231 (25/206) | CONFIRMED/CONFIRMED |
| WPG @ STL | 2026-10-21T00:00:00Z | T-3h | 0.603 | 0.397 | 0.174 | 5.87 | 3.25 | 2.62 | 224 (25/199) | CONFIRMED/CONFIRMED |
| BOS @ DAL | 2026-10-21T00:00:00Z | T-3h | 0.503 | 0.497 | 0.191 | 5.54 | 2.78 | 2.76 | 221 (25/196) | CONFIRMED/CONFIRMED |
| MIN @ EDM | 2026-10-21T01:00:00Z | T-3h | 0.568 | 0.432 | 0.171 | 6.42 | 3.42 | 3.00 | 245 (25/220) | PROJECTED/PROJECTED |
| DET @ SEA | 2026-10-21T01:40:00Z | T-6h | 0.585 | 0.415 | 0.176 | 5.98 | 3.26 | 2.72 | 236 (25/211) | CONFIRMED/CONFIRMED |
| CAR @ VAN | 2026-10-21T02:00:00Z | T-6h | 0.337 | 0.663 | 0.158 | 6.49 | 2.70 | 3.79 | 215 (25/190) | PROBABLE/PROBABLE |
| TBL @ VGK | 2026-10-21T02:30:00Z | T-6h | 0.539 | 0.461 | 0.181 | 5.92 | 3.08 | 2.84 | 239 (25/214) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET4 | team_total | 0.301 | 0.430 | 0.403 | 44 | 58 | no | +0.102 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET3 | team_total | 0.514 | 0.640 | 0.616 | 65 | 37 | no | +0.100 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL4 | team_total | 0.312 | 0.425 | 0.401 | 43 | 58 | no | +0.091 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL3 | team_total | 0.537 | 0.650 | 0.628 | 66 | 36 | no | +0.087 | OK |
| KXNHLTOTAL-26OCT20COLNJ-7 | game_total | 0.378 | 0.485 | 0.463 | 49 | 52 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ4 | team_total | 0.310 | 0.415 | 0.393 | 42 | 59 | no | +0.083 | OK |
| KXNHLTOTAL-26OCT20COLNJ-6 | game_total | 0.493 | 0.595 | 0.575 | 60 | 41 | no | +0.081 | OK |
| KXNHLGAME-26OCT20BOSDAL-BOS | game_winner | 0.497 | 0.395 | 0.415 | 40 | 61 | yes | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 | team_total | 0.526 | 0.625 | 0.606 | 63 | 38 | no | +0.078 | OK |
| KXNHLGAME-26OCT20DETSEA-DET | game_winner | 0.415 | 0.515 | 0.495 | 52 | 49 | no | +0.077 | OK |
| KXNHLGAME-26OCT20DETSEA-SEA | game_winner | 0.585 | 0.485 | 0.505 | 49 | 52 | yes | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3 | team_total | 0.487 | 0.585 | 0.566 | 59 | 42 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4 | team_total | 0.457 | 0.555 | 0.536 | 56 | 45 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL3 | game_spread | 0.152 | 0.245 | 0.224 | 25 | 76 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET2 | game_spread | 0.211 | 0.305 | 0.284 | 31 | 70 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET2 | team_total | 0.748 | 0.835 | 0.820 | 84 | 17 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL2 | team_total | 0.760 | 0.850 | 0.835 | 86 | 16 | no | +0.071 | OK |
| KXNHLTOTAL-26OCT20COLNJ-5 | game_total | 0.718 | 0.810 | 0.794 | 82 | 20 | no | +0.070 | OK |
| KXNHLGAME-26OCT20BOSDAL-DAL | game_winner | 0.503 | 0.595 | 0.577 | 60 | 41 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL2 | game_spread | 0.275 | 0.365 | 0.346 | 37 | 64 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5 | team_total | 0.266 | 0.365 | 0.344 | 38 | 65 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT20SJMTL-7 | game_total | 0.444 | 0.535 | 0.517 | 54 | 47 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL5 | team_total | 0.150 | 0.240 | 0.220 | 25 | 77 | no | +0.067 | OK |
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
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ5 | team_total | 0.151 | 0.230 | 0.212 | 24 | 78 | no | +0.056 | OK |
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
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB3 | team_total | 0.547 | 0.620 | 0.606 | 63 | 39 | no | +0.047 | OK |
| KXNHLGAME-26OCT20COLNJ-COL | game_winner | 0.544 | 0.475 | 0.489 | 48 | 53 | yes | +0.046 | OK |
| KXNHLGAME-26OCT20COLNJ-NJ | game_winner | 0.456 | 0.525 | 0.511 | 53 | 48 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB2 | team_total | 0.764 | 0.830 | 0.818 | 84 | 18 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT20LAWSH-WSH2 | game_spread | 0.421 | 0.355 | 0.368 | 36 | 65 | yes | +0.045 | OK |
| KXNHLGAME-26OCT20CARVAN-VAN | game_winner | 0.337 | 0.270 | 0.283 | 28 | 74 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT20TBVGK-5 | game_total | 0.736 | 0.795 | 0.784 | 80 | 21 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL2 | team_total | 0.851 | 0.905 | 0.896 | 91 | 10 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL2 | game_spread | 0.381 | 0.445 | 0.432 | 45 | 56 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL6 | team_total | 0.128 | 0.185 | 0.172 | 19 | 82 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20SJMTL-4 | game_total | 0.852 | 0.905 | 0.896 | 91 | 10 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20TBVGK-6 | game_total | 0.512 | 0.575 | 0.562 | 58 | 43 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20TBVGK-7 | game_total | 0.402 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20SJMTL-8 | game_total | 0.254 | 0.320 | 0.306 | 33 | 69 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR2 | game_spread | 0.452 | 0.520 | 0.506 | 53 | 49 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-WPG2 | game_spread | 0.197 | 0.255 | 0.242 | 26 | 75 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT20LAWSH-LA2 | game_spread | 0.159 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLGAME-26OCT20LAWSH-LA | game_winner | 0.344 | 0.405 | 0.392 | 41 | 60 | no | +0.040 | OK |
| KXNHLGAME-26OCT20LAWSH-WSH | game_winner | 0.656 | 0.595 | 0.608 | 60 | 41 | yes | +0.040 | OK |
| KXNHLGAME-26OCT20SJMTL-MTL | game_winner | 0.605 | 0.665 | 0.653 | 67 | 34 | no | +0.039 | OK |
| KXNHLGAME-26OCT20SJMTL-SJ | game_winner | 0.395 | 0.335 | 0.347 | 34 | 67 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA4 | team_total | 0.237 | 0.300 | 0.287 | 31 | 71 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR5 | team_total | 0.131 | 0.190 | 0.177 | 20 | 82 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-BOS2 | game_spread | 0.270 | 0.215 | 0.225 | 22 | 79 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-7 | game_total | 0.336 | 0.395 | 0.383 | 40 | 61 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR2 | game_spread | 0.171 | 0.225 | 0.213 | 23 | 78 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT20DETSEA-8 | game_total | 0.229 | 0.285 | 0.273 | 29 | 72 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT20TORCBJ-7 | game_total | 0.447 | 0.505 | 0.493 | 51 | 50 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-4 | game_total | 0.786 | 0.840 | 0.830 | 85 | 17 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT20TBVGK-4 | game_total | 0.828 | 0.880 | 0.871 | 89 | 13 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB5 | team_total | 0.165 | 0.220 | 0.208 | 23 | 79 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-6 | game_total | 0.449 | 0.505 | 0.494 | 51 | 50 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT20LAWSH-LA3 | game_spread | 0.080 | 0.130 | 0.118 | 14 | 88 | no | +0.033 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 41 recommended · full analysis in card.md / packet.json `thesis_card`

- Mason Marchment: 1+ goals YES @ 18c · p 0.2285 (adj 0.2151) · $2.42 · thesis SJS:OFFENSE_4PLUS
- Cole Caufield: 2+ goals NO @ 87c · p 0.9097 (adj 0.8973) · $6.52 · thesis MTL:SUPPRESSED
- Cole Caufield: 1+ goals NO @ 56c · p 0.6055 (adj 0.5929) · $1.98 · thesis MTL:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 74c · p 0.7935 (adj 0.7642) · $4.16 · thesis SJS:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 64c · p 0.7039 (adj 0.6867) · $6.52 · thesis NJD:SUPPRESSED
- Cale Makar: 1+ assists NO @ 46c · p 0.6011 (adj 0.5029) · $4.11 · thesis COL:SUPPRESSED
- Jack Hughes: 1+ assists NO @ 48c · p 0.611 (adj 0.5161) · $3.22 · thesis NJD:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 13c · p 0.2121 (adj 0.1903) · $4.38 · thesis ANA:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 15c · p 0.1964 (adj 0.1823) · $2.07 · thesis NYI:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.129 (adj 0.1205) · $1.27 · thesis ANA:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2403 (adj 0.2215) · $3.82 · thesis WSH:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 54c · p 0.6642 (adj 0.577) · $3.85 · thesis LAK:SUPPRESSED
- Ryan Leonard: 1+ assists YES @ 31c · p 0.3762 (adj 0.3381) · $1.34 · thesis WSH:OFFENSE_4PLUS
- Jordan Kyrou: 1+ assists NO @ 67c · p 0.7271 (adj 0.6961) · $3.51 · thesis WSH:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 23c · p 0.2927 (adj 0.2745) · $3.31 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 18c · p 0.2327 (adj 0.217) · $2.56 · thesis CBJ:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 80c · p 0.8448 (adj 0.8323) · $6.15 · thesis TOR:SUPPRESSED
- Full Game: Over 6.5 goals scored NO @ 50c · p 0.5801 (adj 0.5375) · $4.29 · thesis GAME:LOW_EVENT
- Robert Thomas: 1+ goals YES @ 24c · p 0.2981 (adj 0.2798) · $2.55 · thesis STL:OFFENSE_4PLUS
- Philip Broberg: 1+ assists YES @ 33c · p 0.4115 (adj 0.3682) · $2.18 · thesis STL:OFFENSE_4PLUS
- Dalibor Dvorsky: 1+ goals NO @ 82c · p 0.8493 (adj 0.8407) · $5.39 · thesis STL:SUPPRESSED
- Jimmy Snuggerud: 1+ goals YES @ 30c · p 0.3373 (adj 0.3267) · $1.07 · thesis STL:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7354 (adj 0.7203) · $6.52 · thesis DAL:SUPPRESSED
- Boston over 2.5 goals scored YES @ 51c · p 0.5983 (adj 0.5516) · $3.75 · thesis BOS:OFFENSE_4PLUS
- Thomas Harley: 1+ assists YES @ 32c · p 0.3849 (adj 0.3475) · $1.85 · thesis DAL:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 13c · p 0.1915 (adj 0.1736) · $3.13 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 32c · p 0.413 (adj 0.364) · $4.12 · thesis EDM:SUPPRESSED
- Yakov Trenin: 1+ goals YES @ 10c · p 0.1345 (adj 0.1234) · $1.36 · thesis MIN:OFFENSE_4PLUS
- Zach Hyman: 1+ goals YES @ 32c · p 0.3697 (adj 0.3548) · $3.12 · thesis EDM:OFFENSE_4PLUS
- Moritz Seider: 1+ goals NO @ 85c · p 0.9008 (adj 0.8869) · $6.52 · thesis DET:SUPPRESSED
- Adam Larsson: 1+ assists YES @ 18c · p 0.3134 (adj 0.2202) · $1.91 · thesis SEA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 13c · p 0.1691 (adj 0.1581) · $1.49 · thesis SEA:OFFENSE_4PLUS
- Detroit wins by over 1.5 goals NO @ 70c · p 0.7853 (adj 0.7402) · $6.02 · thesis SEA:WINS
- Filip Chytil: 1+ goals YES @ 17c · p 0.2497 (adj 0.2285) · $4.06 · thesis VAN:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 12c · p 0.1781 (adj 0.1623) · $2.69 · thesis VAN:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 49c · p 0.6611 (adj 0.5434) · $3.13 · thesis VAN:WINS
- Nikolaj Ehlers: 1+ goals NO @ 70c · p 0.7606 (adj 0.7442) · $6.42 · thesis CAR:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 4c · p 0.0802 (adj 0.0689) · $1.72 · thesis VGK:OFFENSE_4PLUS
- Tampa Bay wins by over 1.5 goals NO @ 71c · p 0.7877 (adj 0.7464) · $6.1 · thesis VGK:WINS
- Brett Howden: 1+ goals YES @ 19c · p 0.2331 (adj 0.2198) · $1.53 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 72c · p 0.7669 (adj 0.7539) · $6.52 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ MTL** · priced 195/205 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 27.0, exp saves 23.53 (sd 6.48), pull risk 0.053
- SJS net: Alex Nedeljkovic (PROBABLE) exp shots 27.29, exp saves 23.18 (sd 6.64), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Nedeljkovic: 28+ saves | 0.244 | 0.450 | 49/59 | +0.149 |  |
| Sam Dickinson: 1+ assists | 0.208 | 0.075 | 14/99 | +0.060 | STANDARD |
| Nick Suzuki: 1+ assists | 0.480 | 0.595 | 60/41 | +0.093 | STANDARD |
| Michael Kesselring: 1+ points | 0.245 | 0.130 | 18/92 | +0.054 | STANDARD |
| Sam Dickinson: 1+ points | 0.260 | 0.150 | 16/86 | +0.090 | STANDARD |
| Nick Suzuki: 2+ points | 0.279 | 0.380 | 39/63 | +0.074 | STANDARD |

**COL @ NJD** · priced 184/190 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 29.27, exp saves 25.27 (sd 6.74), pull risk 0.061
- COL net: Scott Wedgewood (CONFIRMED) exp shots 28.54, exp saves 24.76 (sd 6.74), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.155 | 0.320 | 34/70 | +0.130 | STANDARD |
| Cale Makar: 1+ assists | 0.399 | 0.550 | 56/46 | +0.124 | STANDARD |
| Jack Hughes: 1+ assists | 0.389 | 0.535 | 55/48 | +0.114 | STANDARD |
| Luke Evangelista: 1+ points | 0.318 | 0.460 | 47/55 | +0.115 | STANDARD |
| Scott Wedgewood: 28+ saves | 0.330 | 0.470 | 49/55 | +0.103 |  |
| Cale Makar: 2+ points | 0.147 | 0.280 | 29/73 | +0.109 | STANDARD |

**ANA @ NYI** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.2, exp saves 24.63 (sd 6.66), pull risk 0.053
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.37, exp saves 23.37 (sd 6.6), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ondrej Palat: 1+ assists | 0.237 | 0.105 | 20/99 | +0.026 | STANDARD |
| Lukas Dostal: 27+ saves | 0.310 | 0.435 | 45/58 | +0.093 |  |
| Ilya Sorokin: 23+ saves | 0.624 | 0.510 | 53/51 | +0.076 |  |
| Alex Killorn: 1+ points | 0.446 | 0.350 | 36/66 | +0.069 | STANDARD |
| Alex Killorn: 1+ assists | 0.308 | 0.220 | 24/80 | +0.055 | STANDARD |
| A.J. Greer: 1+ goals | 0.212 | 0.125 | 13/88 | +0.074 | STANDARD |

**LAK @ WSH** · priced 178/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.19, exp saves 24.65 (sd 6.48), pull risk 0.046
- LAK net: Darcy Kuemper (PROBABLE) exp shots 26.88, exp saves 22.97 (sd 6.41), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darcy Kuemper: 27+ saves | 0.282 | 0.440 | 46/58 | +0.121 |  |
| Artemi Panarin: 1+ assists | 0.336 | 0.470 | 48/54 | +0.107 | STANDARD |
| Mikey Anderson: 1+ points | 0.224 | 0.090 | 17/99 | +0.044 | STANDARD |
| Joel Edmundson: 1+ assists | 0.194 | 0.080 | 15/99 | +0.035 | STANDARD |
| Mikey Anderson: 1+ assists | 0.195 | 0.085 | 16/99 | +0.026 | STANDARD |
| Joel Edmundson: 1+ points | 0.240 | 0.135 | 19/92 | +0.039 | STANDARD |

**TOR @ CBJ** · priced 164/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (CONFIRMED) exp shots 25.9, exp saves 22.95 (sd 6.05), pull risk 0.037
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.4, exp saves 26.78 (sd 7.15), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.345 | 0.455 | 46/55 | +0.088 | STANDARD |
| Kirill Marchenko: 1+ points | 0.458 | 0.555 | 56/45 | +0.075 | STANDARD |
| Auston Matthews: 1+ points | 0.559 | 0.655 | 67/36 | +0.064 | STANDARD |
| Jet Greaves: 25+ saves | 0.385 | 0.480 | 51/55 | +0.048 |  |
| Kirill Marchenko: 1+ assists | 0.277 | 0.370 | 38/64 | +0.067 | STANDARD |
| Gavin McKenna: 1+ points | 0.340 | 0.420 | 43/59 | +0.053 | STANDARD |

**WPG @ STL** · priced 170/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 26.09, exp saves 22.93 (sd 6.2), pull risk 0.048
- WPG net: Stuart Skinner (CONFIRMED) exp shots 26.62, exp saves 22.57 (sd 6.42), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Philip Broberg: 1+ points | 0.467 | 0.365 | 37/64 | +0.080 | STANDARD |
| Jake Neighbours: 1+ assists | 0.322 | 0.235 | 25/78 | +0.059 | STANDARD |
| Philip Broberg: 1+ assists | 0.411 | 0.325 | 33/68 | +0.066 | STANDARD |
| Robert Thomas: 1+ goals | 0.298 | 0.225 | 24/79 | +0.045 | STANDARD |
| Pavel Buchnevich: 1+ assists | 0.257 | 0.325 | 34/69 | +0.038 | STANDARD |
| Alex Iafallo: 1+ assists | 0.252 | 0.190 | 21/83 | +0.030 | STANDARD |

**BOS @ DAL** · priced 162/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.49, exp saves 21.25 (sd 6.05), pull risk 0.059
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.85, exp saves 24.03 (sd 6.59), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.226 | 0.325 | 34/69 | +0.069 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.441 | 0.525 | 53/48 | +0.061 | STANDARD |
| Morgan Geekie: 1+ points | 0.532 | 0.455 | 46/55 | +0.054 | STANDARD |
| Thomas Harley: 1+ assists | 0.385 | 0.310 | 32/70 | +0.050 | STANDARD |
| Thomas Harley: 1+ points | 0.445 | 0.370 | 38/64 | +0.048 | STANDARD |
| Miro Heiskanen: 1+ points | 0.471 | 0.545 | 55/46 | +0.051 | STANDARD |

**MIN @ EDM** · priced 191/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.88, exp saves 24.28 (sd 6.69), pull risk 0.064
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 24.81 (sd 7.09), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonas Brodin: 1+ assists | 0.244 | 0.105 | 20/99 | +0.033 | STANDARD |
| Mathieu Joseph: 1+ points | 0.258 | 0.125 | 19/94 | +0.058 | STANDARD |
| Zach Bogosian: 1+ points | 0.223 | 0.110 | 17/95 | +0.043 | STANDARD |
| Alex Formenton: 1+ points | 0.334 | 0.225 | 24/79 | +0.081 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.312 | 0.205 | 22/81 | +0.080 | STANDARD |
| Owen Michaels: 1+ points | 0.247 | 0.140 | 21/93 | +0.025 | PRIOR_HEAVY |

**DET @ SEA** · priced 176/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (CONFIRMED) exp shots 29.42, exp saves 25.64 (sd 6.73), pull risk 0.054
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.75, exp saves 22.88 (sd 6.51), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Larsson: 1+ assists | 0.313 | 0.170 | 18/84 | +0.123 | STANDARD |
| Ben Chiarot: 1+ points | 0.288 | 0.150 | 21/91 | +0.066 | STANDARD |
| Moritz Seider: 1+ points | 0.462 | 0.590 | 60/42 | +0.101 | STANDARD |
| Moritz Seider: 2+ points | 0.127 | 0.250 | 27/77 | +0.091 | STANDARD |
| Adam Larsson: 1+ points | 0.358 | 0.240 | 25/77 | +0.095 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.352 | 0.245 | 27/78 | +0.069 | STANDARD |

**CAR @ VAN** · priced 156/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 32.33, exp saves 27.65 (sd 7.44), pull risk 0.077
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 22.8, exp saves 19.96 (sd 5.7), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.222 | 0.340 | 35/67 | +0.093 | STANDARD |
| Sebastian Aho: 1+ assists | 0.391 | 0.500 | 51/51 | +0.082 | STANDARD |
| Nikolaj Ehlers: 1+ points | 0.509 | 0.610 | 62/40 | +0.074 | STANDARD |
| Bradly Nadeau: 1+ assists | 0.155 | 0.255 | 29/78 | +0.053 | STANDARD |
| Sean Walker: 1+ assists | 0.351 | 0.260 | 29/77 | +0.046 | STANDARD |
| Linus Karlsson: 1+ goals | 0.232 | 0.145 | 18/89 | +0.041 | STANDARD |

**TBL @ VGK** · priced 183/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.99, exp saves 23.6 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.35, exp saves 22.57 (sd 6.35), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andrei Vasilevskiy: 27+ saves | 0.256 | 0.415 | 44/61 | +0.118 |  |
| Nikita Kucherov: 1+ assists | 0.437 | 0.565 | 57/44 | +0.106 | STANDARD |
| Nikita Kucherov: 2+ points | 0.243 | 0.370 | 38/64 | +0.101 | STANDARD |
| John Carlson: 1+ assists | 0.271 | 0.380 | 39/63 | +0.083 | STANDARD |
| John Carlson: 1+ points | 0.341 | 0.445 | 46/57 | +0.072 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.115 | 0.205 | 21/80 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
