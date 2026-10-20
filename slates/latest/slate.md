# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-20T22:02:28Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4578 · contracts joined: 2681 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2406, 'OK': 181, 'NO_EDGE': 94}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 438, 'game_early_goal': 11, 'first_goal': 400, 'game_winner': 22, 'player_goals': 694, 'game_overtime': 11, 'player_points': 566, 'goalie_saves': 22, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 2026-10-20T23:00:00Z | T-30m | 0.606 | 0.394 | 0.169 | 6.16 | 3.41 | 2.75 | 262 (25/237) | CONFIRMED/CONFIRMED |
| COL @ NJD | 2026-10-20T23:00:00Z | T-30m | 0.456 | 0.544 | 0.180 | 5.79 | 2.77 | 3.02 | 241 (25/216) | CONFIRMED/CONFIRMED |
| ANA @ NYI | 2026-10-20T23:00:00Z | T-30m | 0.616 | 0.384 | 0.172 | 5.98 | 3.35 | 2.63 | 233 (25/208) | CONFIRMED/CONFIRMED |
| LAK @ WSH | 2026-10-20T23:00:00Z | T-30m | 0.656 | 0.344 | 0.171 | 5.82 | 3.39 | 2.43 | 251 (25/226) | CONFIRMED/PROBABLE |
| TOR @ CBJ | 2026-10-20T23:00:00Z | T-30m | 0.648 | 0.352 | 0.160 | 6.19 | 3.58 | 2.62 | 238 (25/213) | CONFIRMED/CONFIRMED |
| WPG @ STL | 2026-10-21T00:00:00Z | T-90m | 0.603 | 0.397 | 0.174 | 5.87 | 3.25 | 2.62 | 260 (25/235) | CONFIRMED/CONFIRMED |
| BOS @ DAL | 2026-10-21T00:00:00Z | T-90m | 0.503 | 0.497 | 0.191 | 5.54 | 2.78 | 2.76 | 221 (25/196) | CONFIRMED/CONFIRMED |
| MIN @ EDM | 2026-10-21T01:00:00Z | T-90m | 0.561 | 0.439 | 0.174 | 6.39 | 3.39 | 3.00 | 245 (25/220) | PROBABLE/PROBABLE |
| DET @ SEA | 2026-10-21T01:40:00Z | T-3h | 0.585 | 0.415 | 0.176 | 5.98 | 3.26 | 2.72 | 236 (25/211) | CONFIRMED/CONFIRMED |
| CAR @ VAN | 2026-10-21T02:00:00Z | T-3h | 0.337 | 0.663 | 0.157 | 6.47 | 2.69 | 3.78 | 244 (25/219) | PROBABLE/CONFIRMED |
| TBL @ VGK | 2026-10-21T02:30:00Z | T-3h | 0.539 | 0.461 | 0.181 | 5.92 | 3.08 | 2.84 | 250 (25/225) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4 | team_total | 0.459 | 0.600 | 0.572 | 61 | 41 | no | +0.114 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET4 | team_total | 0.301 | 0.425 | 0.399 | 43 | 58 | no | +0.102 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET3 | team_total | 0.514 | 0.640 | 0.616 | 65 | 37 | no | +0.100 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL4 | team_total | 0.312 | 0.425 | 0.401 | 43 | 58 | no | +0.091 | OK |
| KXNHLGAME-26OCT20DETSEA-DET | game_winner | 0.415 | 0.525 | 0.503 | 53 | 48 | no | +0.087 | OK |
| KXNHLGAME-26OCT20DETSEA-SEA | game_winner | 0.585 | 0.475 | 0.497 | 48 | 53 | yes | +0.087 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL3 | team_total | 0.537 | 0.650 | 0.628 | 66 | 36 | no | +0.087 | OK |
| KXNHLTOTAL-26OCT20COLNJ-7 | game_total | 0.378 | 0.485 | 0.463 | 49 | 52 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET2 | game_spread | 0.211 | 0.315 | 0.292 | 32 | 69 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ4 | team_total | 0.310 | 0.415 | 0.393 | 42 | 59 | no | +0.083 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5 | team_total | 0.263 | 0.365 | 0.343 | 37 | 64 | no | +0.081 | OK |
| KXNHLTOTAL-26OCT20COLNJ-5 | game_total | 0.718 | 0.815 | 0.798 | 82 | 19 | no | +0.081 | OK |
| KXNHLTOTAL-26OCT20COLNJ-6 | game_total | 0.493 | 0.600 | 0.579 | 61 | 41 | no | +0.081 | OK |
| KXNHLGAME-26OCT20BOSDAL-BOS | game_winner | 0.497 | 0.395 | 0.415 | 40 | 61 | yes | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 | team_total | 0.526 | 0.625 | 0.606 | 63 | 38 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3 | team_total | 0.487 | 0.585 | 0.566 | 59 | 42 | no | +0.076 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL3 | game_spread | 0.152 | 0.245 | 0.224 | 25 | 76 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET2 | team_total | 0.748 | 0.835 | 0.820 | 84 | 17 | no | +0.072 | OK |
| KXNHLGAME-26OCT20BOSDAL-DAL | game_winner | 0.503 | 0.595 | 0.577 | 60 | 41 | no | +0.070 | OK |
| KXNHLTOTAL-26OCT20SJMTL-7 | game_total | 0.444 | 0.535 | 0.517 | 54 | 47 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL2 | game_spread | 0.275 | 0.365 | 0.346 | 37 | 64 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3 | team_total | 0.669 | 0.760 | 0.743 | 77 | 25 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL5 | team_total | 0.150 | 0.240 | 0.220 | 25 | 77 | no | +0.067 | OK |
| KXNHLTOTAL-26OCT20SJMTL-6 | game_total | 0.557 | 0.645 | 0.628 | 65 | 36 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4 | team_total | 0.278 | 0.365 | 0.347 | 37 | 64 | no | +0.065 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET3 | game_spread | 0.116 | 0.195 | 0.176 | 20 | 81 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET5 | team_total | 0.145 | 0.235 | 0.214 | 25 | 78 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT20COLNJ-8 | game_total | 0.203 | 0.285 | 0.267 | 29 | 72 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT20DETSEA-7 | game_total | 0.410 | 0.495 | 0.478 | 50 | 51 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL2 | team_total | 0.760 | 0.845 | 0.830 | 86 | 17 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT20COLNJ-4 | game_total | 0.814 | 0.885 | 0.873 | 89 | 12 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL3 | game_spread | 0.246 | 0.325 | 0.308 | 33 | 68 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-5 | game_total | 0.680 | 0.755 | 0.741 | 76 | 25 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR3 | game_spread | 0.307 | 0.385 | 0.369 | 39 | 62 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ5 | team_total | 0.151 | 0.230 | 0.212 | 24 | 78 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT20DETSEA-5 | game_total | 0.745 | 0.815 | 0.802 | 82 | 19 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ3 | game_spread | 0.135 | 0.205 | 0.189 | 21 | 80 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT20SJMTL-5 | game_total | 0.767 | 0.840 | 0.827 | 85 | 17 | no | +0.053 | OK |
| KXNHLGAME-26OCT20CARVAN-CAR | game_winner | 0.663 | 0.735 | 0.721 | 74 | 27 | no | +0.053 | OK |
| KXNHLGAME-26OCT20CARVAN-VAN | game_winner | 0.337 | 0.265 | 0.279 | 27 | 74 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA2 | game_spread | 0.356 | 0.285 | 0.299 | 29 | 72 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT20SJMTL-8 | game_total | 0.254 | 0.325 | 0.310 | 33 | 68 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ2 | game_spread | 0.244 | 0.315 | 0.300 | 32 | 69 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA2 | team_total | 0.686 | 0.755 | 0.742 | 76 | 25 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT20DETSEA-6 | game_total | 0.523 | 0.600 | 0.585 | 61 | 41 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ2 | team_total | 0.760 | 0.830 | 0.817 | 84 | 18 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA3 | team_total | 0.443 | 0.520 | 0.504 | 53 | 49 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB4 | team_total | 0.324 | 0.395 | 0.380 | 40 | 61 | no | +0.049 | OK |
| KXNHLGAME-26OCT20COLNJ-COL | game_winner | 0.544 | 0.475 | 0.489 | 48 | 53 | yes | +0.046 | OK |
| KXNHLGAME-26OCT20COLNJ-NJ | game_winner | 0.456 | 0.525 | 0.511 | 53 | 48 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-4 | game_total | 0.786 | 0.845 | 0.834 | 85 | 16 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT20SJMTL-4 | game_total | 0.850 | 0.905 | 0.896 | 91 | 10 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT20TBVGK-5 | game_total | 0.736 | 0.795 | 0.784 | 80 | 21 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR2 | team_total | 0.726 | 0.790 | 0.778 | 80 | 22 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR2 | game_spread | 0.450 | 0.520 | 0.506 | 53 | 49 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT20COLNJ-9 | game_total | 0.138 | 0.200 | 0.186 | 21 | 81 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL2 | game_spread | 0.382 | 0.445 | 0.432 | 45 | 56 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL6 | team_total | 0.129 | 0.190 | 0.176 | 20 | 82 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-WPG2 | game_spread | 0.197 | 0.255 | 0.242 | 26 | 75 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT20DETSEA-4 | game_total | 0.833 | 0.885 | 0.876 | 89 | 12 | no | +0.040 | OK |
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
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB2 | team_total | 0.764 | 0.825 | 0.814 | 84 | 19 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT20LAWSH-WSH2 | game_spread | 0.421 | 0.365 | 0.376 | 37 | 64 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT20TBVGK-4 | game_total | 0.828 | 0.875 | 0.867 | 88 | 13 | no | +0.034 | OK |
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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 40 recommended · full analysis in card.md / packet.json `thesis_card`

- Cole Caufield: 1+ goals NO @ 55c · p 0.6064 (adj 0.5911) · $4.96 · thesis MTL:SUPPRESSED
- Macklin Celebrini: 1+ assists NO @ 52c · p 0.6049 (adj 0.5599) · $4.47 · thesis SJS:SUPPRESSED
- Alex Nedeljkovic: 28+ saves NO @ 55c · p 0.7578 (adj 0.587) · $5.09 · thesis SJS:NET_LOW_VOLUME
- Mason Marchment: 1+ goals YES @ 19c · p 0.2243 (adj 0.2145) · $1.71 · thesis SJS:OFFENSE_4PLUS
- Fedor Svechkov: 1+ goals YES @ 8c · p 0.1156 (adj 0.1055) · $1.71 · thesis COL:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 11c · p 0.15 (adj 0.1387) · $1.95 · thesis NJD:OFFENSE_4PLUS
- Parker Kelly: 1+ goals YES @ 9c · p 0.1252 (adj 0.1152) · $1.68 · thesis COL:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 64c · p 0.7039 (adj 0.6867) · $6.94 · thesis NJD:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 13c · p 0.2121 (adj 0.1903) · $4.66 · thesis ANA:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 15c · p 0.1964 (adj 0.1823) · $2.2 · thesis NYI:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.129 (adj 0.1205) · $1.35 · thesis ANA:OFFENSE_4PLUS
- Jackson LaCombe: 1+ goals YES @ 11c · p 0.1365 (adj 0.1286) · $1.03 · thesis ANA:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2403 (adj 0.224) · $2.84 · thesis WSH:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 4c · p 0.0605 (adj 0.0541) · $1.02 · thesis LAK:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 53c · p 0.6642 (adj 0.5737) · $5.89 · thesis LAK:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 23c · p 0.2927 (adj 0.2745) · $3.49 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 18c · p 0.2327 (adj 0.217) · $2.68 · thesis CBJ:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 80c · p 0.8448 (adj 0.8323) · $6.94 · thesis TOR:SUPPRESSED
- Matthew Knies: 1+ goals NO @ 68c · p 0.7206 (adj 0.7092) · $4.21 · thesis CBJ:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 22c · p 0.2981 (adj 0.2761) · $4.45 · thesis STL:OFFENSE_4PLUS
- Philip Broberg: 1+ assists YES @ 33c · p 0.4115 (adj 0.3682) · $1.75 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 30c · p 0.3373 (adj 0.3267) · $1.13 · thesis STL:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7354 (adj 0.7203) · $6.94 · thesis DAL:SUPPRESSED
- Boston over 2.5 goals scored YES @ 51c · p 0.5983 (adj 0.5516) · $4.64 · thesis BOS:OFFENSE_4PLUS
- Charlie McAvoy: 1+ assists NO @ 59c · p 0.6544 (adj 0.6172) · $4.42 · thesis BOS:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 13c · p 0.1898 (adj 0.1724) · $3.03 · thesis EDM:OFFENSE_4PLUS
- Zach Hyman: 1+ goals YES @ 31c · p 0.3749 (adj 0.3574) · $4.45 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 32c · p 0.4097 (adj 0.3623) · $4.78 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ assists YES @ 33c · p 0.4141 (adj 0.3696) · $2.93 · thesis EDM:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 11c · p 0.1534 (adj 0.1413) · $2.05 · thesis SEA:OFFENSE_4PLUS
- Adam Larsson: 1+ assists YES @ 19c · p 0.3134 (adj 0.2299) · $2.12 · thesis SEA:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 68c · p 0.7414 (adj 0.7248) · $6.94 · thesis DET:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 13c · p 0.1691 (adj 0.1581) · $1.74 · thesis SEA:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 16c · p 0.2489 (adj 0.2254) · $5.01 · thesis VAN:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 62c · p 0.7693 (adj 0.669) · $5.17 · thesis VAN:WINS
- Sebastian Aho: 1+ goals NO @ 62c · p 0.6853 (adj 0.6677) · $6.33 · thesis CAR:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 4c · p 0.0802 (adj 0.0689) · $1.87 · thesis VGK:OFFENSE_4PLUS
- Brett Howden: 1+ goals YES @ 19c · p 0.2331 (adj 0.2211) · $2.02 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 72c · p 0.7669 (adj 0.7539) · $6.64 · thesis VGK:SUPPRESSED
- Nikita Kucherov: 1+ goals NO @ 65c · p 0.6958 (adj 0.6818) · $3.96 · thesis TBL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ MTL** · priced 199/211 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 27.0, exp saves 23.56 (sd 6.5), pull risk 0.051
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.29, exp saves 23.25 (sd 6.52), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Nedeljkovic: 28+ saves | 0.242 | 0.470 | 49/55 | +0.190 |  |
| Sam Dickinson: 1+ assists | 0.225 | 0.085 | 16/99 | +0.055 | STANDARD |
| Collin Graf: 1+ assists | 0.210 | 0.090 | 17/99 | +0.030 | STANDARD |
| Nick Suzuki: 1+ assists | 0.479 | 0.590 | 60/42 | +0.084 | STANDARD |
| Sam Dickinson: 1+ points | 0.273 | 0.175 | 19/84 | +0.072 | STANDARD |
| Ivar Stenberg: 1+ points | 0.332 | 0.430 | 44/58 | +0.071 | PRIOR_HEAVY |

**COL @ NJD** · priced 184/190 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 29.27, exp saves 25.27 (sd 6.74), pull risk 0.061
- COL net: Scott Wedgewood (CONFIRMED) exp shots 28.54, exp saves 24.76 (sd 6.74), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.155 | 0.325 | 34/69 | +0.140 | STANDARD |
| Scott Wedgewood: 28+ saves | 0.330 | 0.485 | 50/53 | +0.123 |  |
| Cale Makar: 1+ assists | 0.399 | 0.550 | 56/46 | +0.124 | STANDARD |
| Jack Hughes: 1+ assists | 0.389 | 0.540 | 55/47 | +0.124 | STANDARD |
| Luke Evangelista: 1+ points | 0.318 | 0.460 | 47/55 | +0.115 | STANDARD |
| Jack Hughes: 2+ points | 0.205 | 0.335 | 35/68 | +0.100 | STANDARD |

**ANA @ NYI** · priced 179/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.2, exp saves 24.63 (sd 6.66), pull risk 0.053
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.37, exp saves 23.37 (sd 6.6), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ondrej Palat: 1+ assists | 0.237 | 0.105 | 20/99 | +0.026 | STANDARD |
| Ilya Sorokin: 23+ saves | 0.624 | 0.510 | 52/50 | +0.086 |  |
| Tim Washe: 1+ points | 0.322 | 0.220 | 23/79 | +0.080 | STANDARD |
| Lukas Dostal: 27+ saves | 0.310 | 0.410 | 43/61 | +0.064 |  |
| Tim Washe: 1+ assists | 0.222 | 0.125 | 16/91 | +0.053 | STANDARD |
| Alex Killorn: 1+ points | 0.446 | 0.350 | 36/66 | +0.069 | STANDARD |

**LAK @ WSH** · priced 190/200 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.19, exp saves 24.65 (sd 6.48), pull risk 0.046
- LAK net: Darcy Kuemper (PROBABLE) exp shots 26.88, exp saves 22.97 (sd 6.41), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Desharnais: 1+ points | 0.220 | 0.055 | 10/99 | +0.113 | STANDARD |
| Artemi Panarin: 1+ assists | 0.336 | 0.475 | 48/53 | +0.117 | STANDARD |
| Vincent Desharnais: 1+ assists | 0.194 | 0.070 | 13/99 | +0.056 | STANDARD |
| Anthony Beauvillier: 1+ assists | 0.199 | 0.085 | 16/99 | +0.030 | STANDARD |
| Darcy Kuemper: 27+ saves | 0.282 | 0.395 | 40/61 | +0.091 |  |
| Artemi Panarin: 1+ points | 0.513 | 0.625 | 63/38 | +0.091 | STANDARD |

**TOR @ CBJ** · priced 171/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (CONFIRMED) exp shots 25.9, exp saves 22.95 (sd 6.05), pull risk 0.037
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.4, exp saves 26.78 (sd 7.15), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.345 | 0.455 | 46/55 | +0.088 | STANDARD |
| Jet Greaves: 25+ saves | 0.385 | 0.490 | 51/53 | +0.068 |  |
| Kirill Marchenko: 1+ points | 0.458 | 0.555 | 57/46 | +0.065 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.277 | 0.365 | 37/64 | +0.067 | STANDARD |
| Adam Fantilli: 1+ assists | 0.369 | 0.455 | 46/55 | +0.063 | STANDARD |
| Auston Matthews: 1+ points | 0.559 | 0.645 | 65/36 | +0.064 | STANDARD |

**WPG @ STL** · priced 204/209 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 26.09, exp saves 22.93 (sd 6.2), pull risk 0.048
- WPG net: Stuart Skinner (CONFIRMED) exp shots 26.62, exp saves 22.57 (sd 6.42), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Morgan Barron: 1+ points | 0.260 | 0.140 | 27/99 | -0.024 | STANDARD |
| Dylan Samberg: 1+ assists | 0.232 | 0.115 | 22/99 | +0.000 | STANDARD |
| Cole Koepke: 1+ points | 0.208 | 0.100 | 19/99 | +0.008 | STANDARD |
| Philip Broberg: 1+ points | 0.467 | 0.360 | 37/65 | +0.080 | STANDARD |
| Dylan DeMelo: 1+ assists | 0.213 | 0.115 | 22/99 | -0.019 | STANDARD |
| Pius Suter: 1+ assists | 0.206 | 0.115 | 22/99 | -0.026 | STANDARD |

**BOS @ DAL** · priced 162/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.49, exp saves 21.25 (sd 6.05), pull risk 0.059
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.85, exp saves 24.03 (sd 6.59), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.226 | 0.325 | 34/69 | +0.069 | STANDARD |
| Mikko Rantanen: 1+ points | 0.591 | 0.680 | 69/33 | +0.063 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.441 | 0.520 | 53/49 | +0.051 | STANDARD |
| Thomas Harley: 1+ assists | 0.385 | 0.310 | 32/70 | +0.050 | STANDARD |
| Thomas Harley: 1+ points | 0.445 | 0.370 | 38/64 | +0.048 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.346 | 0.420 | 43/59 | +0.047 | STANDARD |

**MIN @ EDM** · priced 191/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROBABLE) exp shots 27.88, exp saves 24.36 (sd 6.6), pull risk 0.06
- MIN net: Jesper Wallstedt (PROBABLE) exp shots 29.26, exp saves 24.78 (sd 6.99), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonas Brodin: 1+ assists | 0.244 | 0.110 | 21/99 | +0.023 | STANDARD |
| Alex Formenton: 1+ points | 0.339 | 0.225 | 24/79 | +0.086 | STANDARD |
| Connor McDavid: 2+ assists | 0.221 | 0.335 | 35/68 | +0.083 | STANDARD |
| Mathieu Joseph: 1+ points | 0.262 | 0.150 | 21/91 | +0.041 | STANDARD |
| Mathieu Joseph: 1+ assists | 0.182 | 0.080 | 15/99 | +0.023 | STANDARD |
| Kasperi Kapanen: 1+ points | 0.423 | 0.325 | 33/68 | +0.078 | STANDARD |

**DET @ SEA** · priced 176/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (CONFIRMED) exp shots 29.42, exp saves 25.64 (sd 6.73), pull risk 0.054
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.75, exp saves 22.88 (sd 6.51), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Larsson: 1+ assists | 0.313 | 0.185 | 19/82 | +0.113 | STANDARD |
| Moritz Seider: 1+ points | 0.462 | 0.590 | 60/42 | +0.101 | STANDARD |
| Adam Larsson: 1+ points | 0.358 | 0.240 | 25/77 | +0.095 | STANDARD |
| Ben Chiarot: 1+ points | 0.288 | 0.180 | 21/85 | +0.066 | STANDARD |
| Moritz Seider: 1+ assists | 0.401 | 0.505 | 51/50 | +0.081 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.352 | 0.255 | 27/76 | +0.069 | STANDARD |

**CAR @ VAN** · priced 177/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 32.33, exp saves 27.64 (sd 7.5), pull risk 0.08
- CAR net: Pyotr Kochetkov (CONFIRMED) exp shots 22.8, exp saves 19.94 (sd 5.73), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zeev Buium: 1+ assists | 0.274 | 0.115 | 20/97 | +0.063 | STANDARD |
| Eric Robinson: 1+ assists | 0.216 | 0.095 | 18/99 | +0.026 | STANDARD |
| Paul Cotter: 1+ assists | 0.254 | 0.135 | 22/95 | +0.022 | STANDARD |
| Sebastian Aho: 2+ points | 0.222 | 0.340 | 35/67 | +0.093 | STANDARD |
| Bradly Nadeau: 1+ assists | 0.150 | 0.265 | 29/76 | +0.077 | STANDARD |
| Drew O'Connor: 1+ points | 0.343 | 0.235 | 24/77 | +0.090 | STANDARD |

**TBL @ VGK** · priced 194/199 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.99, exp saves 23.6 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.35, exp saves 22.57 (sd 6.35), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andrei Vasilevskiy: 27+ saves | 0.256 | 0.420 | 44/60 | +0.127 |  |
| Nikita Kucherov: 1+ assists | 0.437 | 0.570 | 58/44 | +0.106 | STANDARD |
| Nikita Kucherov: 2+ points | 0.243 | 0.370 | 38/64 | +0.101 | STANDARD |
| Erik Cernak: 1+ assists | 0.192 | 0.075 | 14/99 | +0.043 | STANDARD |
| Erik Cernak: 1+ points | 0.230 | 0.120 | 18/94 | +0.040 | STANDARD |
| John Carlson: 1+ assists | 0.271 | 0.370 | 38/64 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
