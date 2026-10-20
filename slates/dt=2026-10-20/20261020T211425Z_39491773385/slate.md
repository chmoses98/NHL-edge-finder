# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-20T21:14:25Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4572 · contracts joined: 2675 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2400, 'OK': 183, 'NO_EDGE': 92}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 437, 'game_early_goal': 11, 'first_goal': 398, 'game_winner': 22, 'player_goals': 692, 'game_overtime': 11, 'player_points': 565, 'goalie_saves': 22, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 2026-10-20T23:00:00Z | T-90m | 0.606 | 0.394 | 0.169 | 6.16 | 3.41 | 2.75 | 256 (25/231) | CONFIRMED/CONFIRMED |
| COL @ NJD | 2026-10-20T23:00:00Z | T-90m | 0.456 | 0.544 | 0.180 | 5.79 | 2.77 | 3.02 | 241 (25/216) | CONFIRMED/CONFIRMED |
| ANA @ NYI | 2026-10-20T23:00:00Z | T-90m | 0.616 | 0.384 | 0.172 | 5.98 | 3.35 | 2.63 | 233 (25/208) | CONFIRMED/CONFIRMED |
| LAK @ WSH | 2026-10-20T23:00:00Z | T-90m | 0.656 | 0.344 | 0.171 | 5.82 | 3.39 | 2.43 | 251 (25/226) | CONFIRMED/PROBABLE |
| TOR @ CBJ | 2026-10-20T23:00:00Z | T-90m | 0.648 | 0.352 | 0.160 | 6.19 | 3.58 | 2.62 | 238 (25/213) | CONFIRMED/CONFIRMED |
| WPG @ STL | 2026-10-21T00:00:00Z | T-90m | 0.603 | 0.397 | 0.174 | 5.87 | 3.25 | 2.62 | 260 (25/235) | CONFIRMED/CONFIRMED |
| BOS @ DAL | 2026-10-21T00:00:00Z | T-90m | 0.503 | 0.497 | 0.191 | 5.54 | 2.78 | 2.76 | 221 (25/196) | CONFIRMED/CONFIRMED |
| MIN @ EDM | 2026-10-21T01:00:00Z | T-3h | 0.561 | 0.439 | 0.174 | 6.39 | 3.39 | 3.00 | 245 (25/220) | PROBABLE/PROBABLE |
| DET @ SEA | 2026-10-21T01:40:00Z | T-3h | 0.585 | 0.415 | 0.176 | 5.98 | 3.26 | 2.72 | 236 (25/211) | CONFIRMED/CONFIRMED |
| CAR @ VAN | 2026-10-21T02:00:00Z | T-3h | 0.337 | 0.663 | 0.157 | 6.47 | 2.69 | 3.78 | 244 (25/219) | PROBABLE/CONFIRMED |
| TBL @ VGK | 2026-10-21T02:30:00Z | T-3h | 0.539 | 0.461 | 0.181 | 5.92 | 3.08 | 2.84 | 250 (25/225) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET4 | team_total | 0.301 | 0.425 | 0.399 | 43 | 58 | no | +0.102 | OK |
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
| KXNHLSPREAD-26OCT20BOSDAL-DAL3 | game_spread | 0.152 | 0.245 | 0.224 | 25 | 76 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4 | team_total | 0.459 | 0.560 | 0.540 | 57 | 45 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5 | team_total | 0.263 | 0.360 | 0.339 | 37 | 65 | no | +0.071 | OK |
| KXNHLTOTAL-26OCT20COLNJ-5 | game_total | 0.718 | 0.810 | 0.794 | 82 | 20 | no | +0.070 | OK |
| KXNHLGAME-26OCT20BOSDAL-DAL | game_winner | 0.503 | 0.595 | 0.577 | 60 | 41 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL2 | game_spread | 0.275 | 0.365 | 0.346 | 37 | 64 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3 | team_total | 0.669 | 0.760 | 0.743 | 77 | 25 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL5 | team_total | 0.150 | 0.240 | 0.220 | 25 | 77 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4 | team_total | 0.278 | 0.365 | 0.347 | 37 | 64 | no | +0.065 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET3 | game_spread | 0.116 | 0.195 | 0.176 | 20 | 81 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET5 | team_total | 0.145 | 0.235 | 0.214 | 25 | 78 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT20COLNJ-8 | game_total | 0.203 | 0.285 | 0.267 | 29 | 72 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT20DETSEA-7 | game_total | 0.410 | 0.495 | 0.478 | 50 | 51 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET2 | team_total | 0.748 | 0.830 | 0.816 | 84 | 18 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL2 | team_total | 0.760 | 0.840 | 0.826 | 85 | 17 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA3 | team_total | 0.443 | 0.525 | 0.508 | 53 | 48 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT20SJMTL-7 | game_total | 0.444 | 0.525 | 0.509 | 53 | 48 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT20COLNJ-4 | game_total | 0.814 | 0.885 | 0.873 | 89 | 12 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL3 | game_spread | 0.246 | 0.325 | 0.308 | 33 | 68 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-5 | game_total | 0.680 | 0.755 | 0.741 | 76 | 25 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR3 | game_spread | 0.307 | 0.385 | 0.369 | 39 | 62 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT20SJMTL-6 | game_total | 0.557 | 0.640 | 0.624 | 65 | 37 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ5 | team_total | 0.151 | 0.230 | 0.212 | 24 | 78 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT20DETSEA-5 | game_total | 0.745 | 0.815 | 0.802 | 82 | 19 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ3 | game_spread | 0.135 | 0.205 | 0.189 | 21 | 80 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT20SJMTL-5 | game_total | 0.767 | 0.840 | 0.827 | 85 | 17 | no | +0.053 | OK |
| KXNHLGAME-26OCT20CARVAN-CAR | game_winner | 0.663 | 0.735 | 0.721 | 74 | 27 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR2 | team_total | 0.726 | 0.800 | 0.786 | 81 | 21 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA2 | game_spread | 0.356 | 0.285 | 0.299 | 29 | 72 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ2 | game_spread | 0.244 | 0.315 | 0.300 | 32 | 69 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA2 | team_total | 0.686 | 0.755 | 0.742 | 76 | 25 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT20DETSEA-6 | game_total | 0.523 | 0.595 | 0.581 | 60 | 41 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ2 | team_total | 0.760 | 0.830 | 0.817 | 84 | 18 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB4 | team_total | 0.324 | 0.400 | 0.384 | 41 | 61 | no | +0.049 | OK |
| KXNHLGAME-26OCT20COLNJ-COL | game_winner | 0.544 | 0.475 | 0.489 | 48 | 53 | yes | +0.046 | OK |
| KXNHLGAME-26OCT20COLNJ-NJ | game_winner | 0.456 | 0.525 | 0.511 | 53 | 48 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT20SJMTL-4 | game_total | 0.850 | 0.905 | 0.896 | 91 | 10 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT20TBVGK-5 | game_total | 0.736 | 0.795 | 0.784 | 80 | 21 | no | +0.043 | OK |
| KXNHLGAME-26OCT20CARVAN-VAN | game_winner | 0.337 | 0.270 | 0.283 | 28 | 74 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR2 | game_spread | 0.450 | 0.515 | 0.502 | 52 | 49 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT20COLNJ-9 | game_total | 0.138 | 0.200 | 0.186 | 21 | 81 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT20SJMTL-8 | game_total | 0.254 | 0.315 | 0.302 | 32 | 69 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL2 | game_spread | 0.382 | 0.445 | 0.432 | 45 | 56 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL6 | team_total | 0.129 | 0.195 | 0.180 | 21 | 82 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-WPG2 | game_spread | 0.197 | 0.255 | 0.242 | 26 | 75 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT20LAWSH-LA2 | game_spread | 0.159 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLGAME-26OCT20LAWSH-LA | game_winner | 0.344 | 0.405 | 0.392 | 41 | 60 | no | +0.040 | OK |
| KXNHLGAME-26OCT20LAWSH-WSH | game_winner | 0.656 | 0.595 | 0.608 | 60 | 41 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA4 | team_total | 0.237 | 0.300 | 0.287 | 31 | 71 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT20TORCBJ-5 | game_total | 0.771 | 0.825 | 0.815 | 83 | 18 | no | +0.038 | OK |
| KXNHLGAME-26OCT20SJMTL-MTL | game_winner | 0.606 | 0.665 | 0.654 | 67 | 34 | no | +0.038 | OK |
| KXNHLGAME-26OCT20SJMTL-SJ | game_winner | 0.394 | 0.335 | 0.346 | 34 | 67 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-BOS2 | game_spread | 0.270 | 0.215 | 0.225 | 22 | 79 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-7 | game_total | 0.336 | 0.395 | 0.383 | 40 | 61 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR2 | game_spread | 0.171 | 0.225 | 0.213 | 23 | 78 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB3 | team_total | 0.547 | 0.610 | 0.598 | 62 | 40 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT20TORCBJ-7 | game_total | 0.447 | 0.505 | 0.493 | 51 | 50 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-8 | game_total | 0.173 | 0.225 | 0.214 | 23 | 78 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB2 | team_total | 0.764 | 0.825 | 0.814 | 84 | 19 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-4 | game_total | 0.786 | 0.840 | 0.830 | 85 | 17 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT20LAWSH-WSH2 | game_spread | 0.421 | 0.365 | 0.376 | 37 | 64 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-6 | game_total | 0.449 | 0.505 | 0.494 | 51 | 50 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL2 | team_total | 0.850 | 0.900 | 0.891 | 91 | 11 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT20LAWSH-LA3 | game_spread | 0.080 | 0.125 | 0.114 | 13 | 88 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-CBJ2 | game_spread | 0.429 | 0.375 | 0.386 | 38 | 63 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR3 | game_spread | 0.090 | 0.135 | 0.125 | 14 | 87 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT20TBVGK-TB3 | game_spread | 0.138 | 0.185 | 0.175 | 19 | 82 | no | +0.032 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 0.606 | 0.605 | 0.169 | 0.214 | 6.16 | 6.24 | 0.943/1.021 | KXNHLTOTAL-26OCT20SJMTL-5 +0.017 |
| COL @ NJD | 0.456 | 0.483 | 0.180 | 0.219 | 5.79 | 6.15 | 0.984/0.971 | KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 +0.066 |
| ANA @ NYI | 0.616 | 0.578 | 0.172 | 0.215 | 5.98 | 6.36 | 0.947/1.016 | KXNHLTOTAL-26OCT20ANANYI-7 +0.074 |
| LAK @ WSH | 0.656 | 0.577 | 0.171 | 0.217 | 5.82 | 5.90 | 0.938/0.994 | KXNHLGAME-26OCT20LAWSH-LA +0.079 |
| TOR @ CBJ | 0.648 | 0.620 | 0.160 | 0.217 | 6.19 | 5.99 | 0.946/0.956 | KXNHLTEAMTOTAL-26OCT20TORCBJ-CBJ5 -0.049 |
| WPG @ STL | 0.603 | 0.597 | 0.174 | 0.214 | 5.87 | 6.23 | 0.977/1.003 | KXNHLTOTAL-26OCT20WPGSTL-7 +0.065 |
| BOS @ DAL | 0.503 | 0.527 | 0.191 | 0.220 | 5.54 | 6.21 | 0.994/0.956 | KXNHLTOTAL-26OCT20BOSDAL-7 +0.121 |
| MIN @ EDM | 0.561 | 0.594 | 0.174 | 0.207 | 6.39 | 6.68 | 0.994/0.993 | KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4 +0.058 |
| DET @ SEA | 0.585 | 0.572 | 0.176 | 0.217 | 5.98 | 6.26 | 1.023/1.024 | KXNHLTOTAL-26OCT20DETSEA-7 +0.055 |
| CAR @ VAN | 0.337 | 0.443 | 0.157 | 0.212 | 6.47 | 6.52 | 1.030/1.003 | KXNHLSPREAD-26OCT20CARVAN-CAR2 -0.115 |
| TBL @ VGK | 0.539 | 0.583 | 0.181 | 0.217 | 5.92 | 6.09 | 1.003/0.952 | KXNHLTEAMTOTAL-26OCT20TBVGK-VGK3 +0.055 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 42 recommended · full analysis in card.md / packet.json `thesis_card`

- Mason Marchment: 1+ goals YES @ 18c · p 0.2261 (adj 0.2133) · $2.13 · thesis SJS:OFFENSE_4PLUS
- Cole Caufield: 1+ goals NO @ 55c · p 0.6064 (adj 0.5911) · $3.54 · thesis MTL:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 72c · p 0.7974 (adj 0.7537) · $6.25 · thesis SJS:SUPPRESSED
- Montreal over 4.5 goals scored NO @ 65c · p 0.7315 (adj 0.6858) · $3.88 · thesis MTL:SUPPRESSED
- Cody Glass: 1+ goals YES @ 11c · p 0.15 (adj 0.1387) · $1.65 · thesis NJD:OFFENSE_4PLUS
- Cale Makar: 1+ assists NO @ 45c · p 0.6011 (adj 0.4996) · $4.44 · thesis COL:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 64c · p 0.7039 (adj 0.6867) · $5.78 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ assists NO @ 47c · p 0.611 (adj 0.5129) · $3.7 · thesis NJD:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 13c · p 0.2121 (adj 0.1903) · $4.29 · thesis ANA:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 15c · p 0.1964 (adj 0.1823) · $1.99 · thesis NYI:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.129 (adj 0.1205) · $1.28 · thesis ANA:OFFENSE_4PLUS
- Ilya Sorokin: 23+ saves YES @ 50c · p 0.6237 (adj 0.54) · $4.16 · thesis NYI:NET_HIGH_VOLUME
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2403 (adj 0.2215) · $3.68 · thesis WSH:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 54c · p 0.6642 (adj 0.577) · $3.66 · thesis LAK:SUPPRESSED
- Darcy Kuemper: 27+ saves NO @ 59c · p 0.7176 (adj 0.6181) · $2.09 · thesis LAK:NET_LOW_VOLUME
- Charlie Coyle: 1+ goals YES @ 22c · p 0.2927 (adj 0.2733) · $4.37 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 18c · p 0.2327 (adj 0.217) · $2.76 · thesis CBJ:OFFENSE_4PLUS
- Full Game: Over 6.5 goals scored NO @ 50c · p 0.5801 (adj 0.5375) · $5.03 · thesis GAME:LOW_EVENT
- Matthew Knies: 1+ goals NO @ 68c · p 0.7206 (adj 0.7092) · $2.45 · thesis CBJ:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 22c · p 0.2981 (adj 0.2761) · $3.81 · thesis STL:OFFENSE_4PLUS
- Jake Neighbours: 1+ assists YES @ 24c · p 0.3222 (adj 0.2786) · $2.16 · thesis STL:OFFENSE_4PLUS
- Philip Broberg: 1+ assists YES @ 33c · p 0.4115 (adj 0.3682) · $1.85 · thesis STL:OFFENSE_4PLUS
- Dalibor Dvorsky: 1+ goals NO @ 82c · p 0.8493 (adj 0.8407) · $6.32 · thesis STL:SUPPRESSED
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7354 (adj 0.7203) · $6.32 · thesis DAL:SUPPRESSED
- Boston over 2.5 goals scored YES @ 51c · p 0.5983 (adj 0.5516) · $4.23 · thesis BOS:OFFENSE_4PLUS
- Charlie McAvoy: 1+ assists NO @ 59c · p 0.6544 (adj 0.6172) · $4.03 · thesis BOS:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 13c · p 0.1898 (adj 0.1724) · $2.89 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 32c · p 0.4097 (adj 0.3623) · $4.11 · thesis EDM:SUPPRESSED
- Zach Hyman: 1+ goals YES @ 32c · p 0.3749 (adj 0.3587) · $3.3 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ assists YES @ 30c · p 0.3802 (adj 0.3376) · $2.26 · thesis EDM:OFFENSE_4PLUS
- Freddy Gaudreau: 1+ goals YES @ 8c · p 0.1422 (adj 0.1179) · $2.23 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 11c · p 0.1534 (adj 0.1413) · $1.95 · thesis SEA:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 68c · p 0.7414 (adj 0.7248) · $6.32 · thesis DET:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 13c · p 0.1691 (adj 0.1581) · $1.69 · thesis SEA:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 16c · p 0.2489 (adj 0.2254) · $4.53 · thesis VAN:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 49c · p 0.6566 (adj 0.5451) · $1.92 · thesis VAN:WINS
- Carolina wins by over 2.5 goals NO @ 62c · p 0.7693 (adj 0.669) · $3.37 · thesis VAN:WINS
- Sebastian Aho: 1+ goals NO @ 62c · p 0.6853 (adj 0.6677) · $5.66 · thesis CAR:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 4c · p 0.0802 (adj 0.0689) · $1.71 · thesis VGK:OFFENSE_4PLUS
- Brett Howden: 1+ goals YES @ 19c · p 0.2331 (adj 0.2211) · $1.84 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 72c · p 0.7669 (adj 0.7539) · $6.05 · thesis VGK:SUPPRESSED
- Nikita Kucherov: 1+ goals NO @ 65c · p 0.6958 (adj 0.6818) · $3.61 · thesis TBL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ MTL** · priced 195/205 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 27.0, exp saves 23.56 (sd 6.5), pull risk 0.051
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.29, exp saves 23.25 (sd 6.52), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Nedeljkovic: 28+ saves | 0.242 | 0.475 | 52/57 | +0.171 |  |
| Sam Dickinson: 1+ assists | 0.212 | 0.075 | 14/99 | +0.063 | STANDARD |
| Nick Suzuki: 1+ assists | 0.479 | 0.590 | 60/42 | +0.084 | STANDARD |
| Michael Kesselring: 1+ points | 0.243 | 0.145 | 19/90 | +0.042 | STANDARD |
| Nick Suzuki: 2+ assists | 0.141 | 0.235 | 26/79 | +0.057 | STANDARD |
| Nick Suzuki: 2+ points | 0.282 | 0.375 | 38/63 | +0.071 | STANDARD |

**COL @ NJD** · priced 184/190 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 29.27, exp saves 25.27 (sd 6.74), pull risk 0.061
- COL net: Scott Wedgewood (CONFIRMED) exp shots 28.54, exp saves 24.76 (sd 6.74), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.155 | 0.325 | 34/69 | +0.140 | STANDARD |
| Cale Makar: 1+ assists | 0.399 | 0.555 | 56/45 | +0.134 | STANDARD |
| Scott Wedgewood: 28+ saves | 0.330 | 0.485 | 50/53 | +0.123 |  |
| Jack Hughes: 1+ assists | 0.389 | 0.540 | 55/47 | +0.124 | STANDARD |
| Luke Evangelista: 1+ points | 0.318 | 0.460 | 47/55 | +0.115 | STANDARD |
| Cale Makar: 1+ points | 0.496 | 0.635 | 64/37 | +0.118 | STANDARD |

**ANA @ NYI** · priced 179/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.2, exp saves 24.63 (sd 6.66), pull risk 0.053
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.37, exp saves 23.37 (sd 6.6), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lukas Dostal: 27+ saves | 0.310 | 0.445 | 45/56 | +0.113 |  |
| Ilya Sorokin: 23+ saves | 0.624 | 0.495 | 50/51 | +0.106 |  |
| Tim Washe: 1+ points | 0.322 | 0.220 | 23/79 | +0.080 | STANDARD |
| Tim Washe: 1+ assists | 0.222 | 0.125 | 16/91 | +0.053 | STANDARD |
| Alex Killorn: 1+ points | 0.446 | 0.350 | 36/66 | +0.069 | STANDARD |
| Judd Caulfield: 1+ points | 0.300 | 0.205 | 26/85 | +0.027 | PRIOR_HEAVY |

**LAK @ WSH** · priced 190/200 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.19, exp saves 24.65 (sd 6.48), pull risk 0.046
- LAK net: Darcy Kuemper (PROBABLE) exp shots 26.88, exp saves 22.97 (sd 6.41), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Desharnais: 1+ points | 0.220 | 0.060 | 11/99 | +0.103 | STANDARD |
| Artemi Panarin: 1+ assists | 0.336 | 0.470 | 48/54 | +0.107 | STANDARD |
| Darcy Kuemper: 27+ saves | 0.282 | 0.415 | 42/59 | +0.111 |  |
| Vincent Desharnais: 1+ assists | 0.194 | 0.065 | 12/99 | +0.066 | STANDARD |
| Anthony Beauvillier: 1+ assists | 0.199 | 0.085 | 16/99 | +0.030 | STANDARD |
| Artemi Panarin: 1+ points | 0.513 | 0.625 | 63/38 | +0.091 | STANDARD |

**TOR @ CBJ** · priced 171/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (CONFIRMED) exp shots 25.9, exp saves 22.95 (sd 6.05), pull risk 0.037
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.4, exp saves 26.78 (sd 7.15), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.345 | 0.455 | 46/55 | +0.088 | STANDARD |
| Kirill Marchenko: 1+ points | 0.458 | 0.560 | 57/45 | +0.075 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.277 | 0.370 | 38/64 | +0.067 | STANDARD |
| Auston Matthews: 2+ points | 0.201 | 0.290 | 30/72 | +0.065 | STANDARD |
| Auston Matthews: 1+ points | 0.559 | 0.645 | 65/36 | +0.064 | STANDARD |
| Jet Greaves: 25+ saves | 0.385 | 0.470 | 49/55 | +0.048 |  |

**WPG @ STL** · priced 204/209 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 26.09, exp saves 22.93 (sd 6.2), pull risk 0.048
- WPG net: Stuart Skinner (CONFIRMED) exp shots 26.62, exp saves 22.57 (sd 6.42), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Morgan Barron: 1+ points | 0.260 | 0.140 | 27/99 | -0.024 | STANDARD |
| Dylan Samberg: 1+ assists | 0.232 | 0.115 | 22/99 | +0.000 | STANDARD |
| Philip Broberg: 1+ points | 0.467 | 0.365 | 37/64 | +0.080 | STANDARD |
| Pius Suter: 1+ assists | 0.206 | 0.110 | 21/99 | -0.015 | STANDARD |
| Brad Lambert: 1+ points | 0.181 | 0.090 | 17/99 | +0.001 | STANDARD |
| Robert Thomas: 1+ goals | 0.298 | 0.210 | 22/80 | +0.066 | STANDARD |

**BOS @ DAL** · priced 162/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.49, exp saves 21.25 (sd 6.05), pull risk 0.059
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.85, exp saves 24.03 (sd 6.59), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.226 | 0.325 | 34/69 | +0.069 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.441 | 0.525 | 53/48 | +0.061 | STANDARD |
| Morgan Geekie: 2+ points | 0.179 | 0.095 | 16/97 | +0.009 | STANDARD |
| Mikko Rantanen: 1+ points | 0.591 | 0.670 | 69/35 | +0.043 | STANDARD |
| Thomas Harley: 1+ assists | 0.385 | 0.310 | 32/70 | +0.050 | STANDARD |
| Thomas Harley: 1+ points | 0.445 | 0.370 | 38/64 | +0.048 | STANDARD |

**MIN @ EDM** · priced 191/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROBABLE) exp shots 27.88, exp saves 24.36 (sd 6.6), pull risk 0.06
- MIN net: Jesper Wallstedt (PROBABLE) exp shots 29.26, exp saves 24.78 (sd 6.99), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonas Brodin: 1+ assists | 0.244 | 0.105 | 20/99 | +0.033 | STANDARD |
| Alex Formenton: 1+ points | 0.339 | 0.225 | 24/79 | +0.086 | STANDARD |
| Connor McDavid: 2+ assists | 0.221 | 0.335 | 35/68 | +0.083 | STANDARD |
| Mathieu Joseph: 1+ assists | 0.182 | 0.080 | 15/99 | +0.023 | STANDARD |
| Kasperi Kapanen: 1+ points | 0.423 | 0.325 | 33/68 | +0.078 | STANDARD |
| Mathieu Joseph: 1+ points | 0.262 | 0.165 | 21/88 | +0.041 | STANDARD |

**DET @ SEA** · priced 176/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (CONFIRMED) exp shots 29.42, exp saves 25.64 (sd 6.73), pull risk 0.054
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.75, exp saves 22.88 (sd 6.51), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Larsson: 1+ assists | 0.313 | 0.180 | 19/83 | +0.113 | STANDARD |
| Moritz Seider: 1+ points | 0.462 | 0.590 | 60/42 | +0.101 | STANDARD |
| Adam Larsson: 1+ points | 0.358 | 0.240 | 25/77 | +0.095 | STANDARD |
| Ben Chiarot: 1+ points | 0.288 | 0.180 | 21/85 | +0.066 | STANDARD |
| Moritz Seider: 1+ assists | 0.401 | 0.505 | 51/50 | +0.081 | STANDARD |
| Moritz Seider: 2+ points | 0.127 | 0.230 | 26/80 | +0.062 | STANDARD |

**CAR @ VAN** · priced 177/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 32.33, exp saves 27.64 (sd 7.5), pull risk 0.08
- CAR net: Pyotr Kochetkov (CONFIRMED) exp shots 22.8, exp saves 19.94 (sd 5.73), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Eric Robinson: 1+ assists | 0.216 | 0.095 | 18/99 | +0.026 | STANDARD |
| Bradly Nadeau: 1+ assists | 0.150 | 0.265 | 29/76 | +0.077 | STANDARD |
| Sebastian Aho: 2+ points | 0.222 | 0.335 | 34/67 | +0.093 | STANDARD |
| Drew O'Connor: 1+ points | 0.343 | 0.230 | 24/78 | +0.090 | STANDARD |
| Drew O'Connor: 1+ assists | 0.205 | 0.095 | 18/99 | +0.014 | STANDARD |
| Liam Ohgren: 1+ points | 0.402 | 0.295 | 31/72 | +0.077 | STANDARD |

**TBL @ VGK** · priced 194/199 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.99, exp saves 23.6 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.35, exp saves 22.57 (sd 6.35), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andrei Vasilevskiy: 27+ saves | 0.256 | 0.415 | 43/60 | +0.127 |  |
| Nikita Kucherov: 1+ assists | 0.437 | 0.570 | 58/44 | +0.106 | STANDARD |
| Nikita Kucherov: 2+ points | 0.243 | 0.370 | 38/64 | +0.101 | STANDARD |
| Erik Cernak: 1+ assists | 0.192 | 0.080 | 15/99 | +0.033 | STANDARD |
| Erik Cernak: 1+ points | 0.230 | 0.120 | 18/94 | +0.040 | STANDARD |
| John Carlson: 1+ assists | 0.271 | 0.370 | 38/64 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
