# NHL slate 2026-10-27 — RESEARCH_ONLY

generated 2026-10-27T17:34:09Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4559 · contracts joined: 2608 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2333, 'OK': 150, 'NO_EDGE': 125}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 393, 'game_early_goal': 11, 'first_goal': 403, 'game_winner': 22, 'player_goals': 702, 'game_overtime': 11, 'player_points': 539, 'goalie_saves': 10, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ PHI | 2026-10-27T23:00:00Z | T-3h | 0.574 | 0.426 | 0.189 | 5.72 | 3.09 | 2.63 | 239 (25/214) | CONFIRMED/CONFIRMED |
| BOS @ CAR | 2026-10-28T00:00:00Z | T-6h | 0.569 | 0.431 | 0.181 | 6.07 | 3.26 | 2.82 | 239 (25/214) | PROBABLE/CONFIRMED |
| LAK @ CHI | 2026-10-28T00:00:00Z | T-6h | 0.508 | 0.491 | 0.192 | 5.56 | 2.80 | 2.76 | 220 (25/195) | CONFIRMED/PROJECTED |
| MTL @ STL | 2026-10-28T00:00:00Z | T-6h | 0.465 | 0.535 | 0.172 | 6.57 | 3.17 | 3.39 | 233 (25/208) | CONFIRMED/CONFIRMED |
| NYI @ NSH | 2026-10-28T00:00:00Z | T-6h | 0.527 | 0.473 | 0.175 | 6.17 | 3.16 | 3.01 | 231 (25/206) | PROBABLE/PROBABLE |
| NJD @ DAL | 2026-10-28T00:00:00Z | T-6h | 0.561 | 0.439 | 0.187 | 5.58 | 2.97 | 2.61 | 263 (25/238) | CONFIRMED/CONFIRMED |
| FLA @ WPG | 2026-10-28T00:00:00Z | T-6h | 0.525 | 0.475 | 0.184 | 5.99 | 3.08 | 2.92 | 228 (25/203) | CONFIRMED/CONFIRMED |
| MIN @ UTA | 2026-10-28T01:00:00Z | T-6h | 0.532 | 0.468 | 0.173 | 6.20 | 3.21 | 3.00 | 236 (25/211) | PROBABLE/CONFIRMED |
| OTT @ VGK | 2026-10-28T02:00:00Z | T-6h | 0.596 | 0.405 | 0.168 | 6.66 | 3.65 | 3.01 | 231 (25/206) | PROJECTED/PROJECTED |
| VAN @ ANA | 2026-10-28T02:00:00Z | T-6h | 0.638 | 0.362 | 0.159 | 6.80 | 3.85 | 2.95 | 243 (25/218) | PROJECTED/PROJECTED |
| BUF @ SJS | 2026-10-28T02:30:00Z | T-6h | 0.473 | 0.527 | 0.168 | 6.68 | 3.25 | 3.43 | 245 (25/220) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT27LACHI-6 | game_total | 0.450 | 0.555 | 0.534 | 56 | 45 | no | +0.083 | OK |
| KXNHLTOTAL-26OCT27LACHI-7 | game_total | 0.345 | 0.450 | 0.428 | 46 | 56 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ3 | team_total | 0.496 | 0.595 | 0.576 | 60 | 41 | no | +0.077 | OK |
| KXNHLGAME-26OCT27CBJPHI-CBJ | game_winner | 0.426 | 0.525 | 0.505 | 53 | 48 | no | +0.077 | OK |
| KXNHLGAME-26OCT27CBJPHI-PHI | game_winner | 0.574 | 0.475 | 0.495 | 48 | 53 | yes | +0.077 | OK |
| KXNHLSPREAD-26OCT27CBJPHI-CBJ2 | game_spread | 0.213 | 0.305 | 0.285 | 31 | 70 | no | +0.072 | OK |
| KXNHLTOTAL-26OCT27LACHI-5 | game_total | 0.686 | 0.775 | 0.759 | 78 | 23 | no | +0.072 | OK |
| KXNHLSPREAD-26OCT27CBJPHI-CBJ3 | game_spread | 0.116 | 0.195 | 0.176 | 20 | 81 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ4 | team_total | 0.281 | 0.370 | 0.351 | 38 | 64 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ2 | team_total | 0.731 | 0.805 | 0.792 | 81 | 20 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA4 | team_total | 0.309 | 0.390 | 0.373 | 40 | 62 | no | +0.054 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-FLA3 | game_spread | 0.144 | 0.215 | 0.199 | 22 | 79 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA4 | team_total | 0.339 | 0.420 | 0.403 | 43 | 59 | no | +0.054 | OK |
| KXNHLSPREAD-26OCT27CBJPHI-PHI2 | game_spread | 0.337 | 0.265 | 0.279 | 27 | 74 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT27LACHI-4 | game_total | 0.789 | 0.855 | 0.843 | 86 | 15 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-CAR3 | game_spread | 0.214 | 0.285 | 0.270 | 29 | 72 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ4 | team_total | 0.273 | 0.350 | 0.334 | 36 | 66 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR4 | team_total | 0.422 | 0.505 | 0.488 | 52 | 51 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA3 | team_total | 0.564 | 0.640 | 0.625 | 65 | 37 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-CAR2 | game_spread | 0.344 | 0.415 | 0.400 | 42 | 59 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA3 | team_total | 0.536 | 0.610 | 0.595 | 62 | 40 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR3 | team_total | 0.638 | 0.710 | 0.696 | 72 | 30 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ3 | team_total | 0.497 | 0.565 | 0.551 | 57 | 44 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA5 | team_total | 0.143 | 0.210 | 0.195 | 22 | 80 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT27LACHI-8 | game_total | 0.173 | 0.240 | 0.225 | 25 | 77 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT27NJDAL-5 | game_total | 0.693 | 0.755 | 0.743 | 76 | 25 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ5 | team_total | 0.128 | 0.190 | 0.176 | 20 | 82 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA2 | team_total | 0.758 | 0.820 | 0.809 | 83 | 19 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT27NJDAL-NJ3 | game_spread | 0.120 | 0.175 | 0.163 | 18 | 83 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-FLA2 | game_spread | 0.256 | 0.315 | 0.303 | 32 | 69 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA2 | team_total | 0.782 | 0.840 | 0.829 | 85 | 17 | no | +0.039 | OK |
| KXNHLGAME-26OCT27FLAWPG-FLA | game_winner | 0.475 | 0.535 | 0.523 | 54 | 47 | no | +0.038 | OK |
| KXNHLGAME-26OCT27FLAWPG-WPG | game_winner | 0.525 | 0.465 | 0.477 | 47 | 54 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI4 | team_total | 0.316 | 0.375 | 0.363 | 38 | 63 | no | +0.038 | OK |
| KXNHLGAME-26OCT27MTLSTL-STL | game_winner | 0.465 | 0.525 | 0.513 | 53 | 48 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ2 | team_total | 0.731 | 0.790 | 0.779 | 80 | 22 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL4 | team_total | 0.453 | 0.395 | 0.406 | 40 | 61 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI3 | team_total | 0.537 | 0.595 | 0.584 | 60 | 41 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT27LACHI-9 | game_total | 0.115 | 0.170 | 0.158 | 18 | 84 | no | +0.035 | OK |
| KXNHLGAME-26OCT27BOSCAR-BOS | game_winner | 0.431 | 0.375 | 0.386 | 38 | 63 | yes | +0.035 | OK |
| KXNHLGAME-26OCT27BOSCAR-CAR | game_winner | 0.569 | 0.625 | 0.614 | 63 | 38 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA5 | team_total | 0.174 | 0.230 | 0.218 | 24 | 78 | no | +0.034 | OK |
| KXNHLGAME-26OCT27NJDAL-DAL | game_winner | 0.561 | 0.505 | 0.516 | 51 | 50 | yes | +0.034 | OK |
| KXNHLGAME-26OCT27NJDAL-NJ | game_winner | 0.439 | 0.495 | 0.484 | 50 | 51 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT27NJDAL-NJ2 | game_spread | 0.223 | 0.275 | 0.264 | 28 | 73 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR5 | team_total | 0.233 | 0.295 | 0.282 | 31 | 72 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF3 | game_spread | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT27LACHI-LA3 | game_spread | 0.147 | 0.195 | 0.185 | 20 | 81 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR2 | team_total | 0.833 | 0.880 | 0.872 | 89 | 13 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-10 | game_total | 0.114 | 0.075 | 0.082 | 8 | 93 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-8 | game_total | 0.312 | 0.265 | 0.274 | 27 | 74 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT27CBJPHI-PHI3 | game_spread | 0.208 | 0.165 | 0.173 | 17 | 84 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT27NJDAL-6 | game_total | 0.454 | 0.505 | 0.495 | 51 | 50 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL5 | team_total | 0.260 | 0.210 | 0.219 | 22 | 80 | yes | +0.028 | OK |
| KXNHLGAME-26OCT27MTLSTL-MTL | game_winner | 0.535 | 0.485 | 0.495 | 49 | 52 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-5 | game_total | 0.711 | 0.755 | 0.747 | 76 | 25 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL3 | team_total | 0.662 | 0.610 | 0.621 | 62 | 40 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-VGK4 | team_total | 0.513 | 0.465 | 0.474 | 47 | 54 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ5 | team_total | 0.126 | 0.175 | 0.164 | 19 | 84 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT27BOSCAR-7 | game_total | 0.428 | 0.475 | 0.465 | 48 | 53 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT27MTLSTL-STL3 | game_spread | 0.155 | 0.195 | 0.186 | 20 | 81 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT27NJDAL-4 | game_total | 0.796 | 0.840 | 0.832 | 85 | 17 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-BOS2 | game_spread | 0.225 | 0.185 | 0.192 | 19 | 82 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-4 | game_total | 0.807 | 0.845 | 0.838 | 85 | 16 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-5 | game_total | 0.744 | 0.785 | 0.777 | 79 | 22 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-PHI5 | team_total | 0.203 | 0.165 | 0.172 | 17 | 84 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-6 | game_total | 0.619 | 0.575 | 0.584 | 58 | 43 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT27BOSCAR-6 | game_total | 0.541 | 0.585 | 0.576 | 59 | 42 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT27BOSCAR-5 | game_total | 0.757 | 0.795 | 0.788 | 80 | 21 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF2 | game_spread | 0.313 | 0.355 | 0.346 | 36 | 65 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL6 | team_total | 0.127 | 0.085 | 0.092 | 10 | 93 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT27NJDAL-7 | game_total | 0.344 | 0.385 | 0.377 | 39 | 62 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI2 | team_total | 0.769 | 0.805 | 0.798 | 81 | 20 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA6 | team_total | 0.056 | 0.090 | 0.082 | 10 | 92 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4 | team_total | 0.454 | 0.505 | 0.495 | 52 | 51 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-PHI3 | team_total | 0.605 | 0.565 | 0.573 | 57 | 44 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT27MTLSTL-STL2 | game_spread | 0.258 | 0.295 | 0.287 | 30 | 71 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-4 | game_total | 0.834 | 0.865 | 0.859 | 87 | 14 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI5 | team_total | 0.153 | 0.195 | 0.186 | 21 | 82 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-6 | game_total | 0.526 | 0.565 | 0.557 | 57 | 44 | no | +0.017 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ PHI | 0.574 | 0.543 | 0.189 | 0.222 | 5.72 | 5.85 | 0.994/1.008 | KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ3 +0.043 |
| BOS @ CAR | 0.569 | 0.563 | 0.181 | 0.214 | 6.07 | 6.66 | 1.000/0.956 | KXNHLTOTAL-26OCT27BOSCAR-7 +0.101 |
| LAK @ CHI | 0.508 | 0.475 | 0.192 | 0.219 | 5.56 | 5.98 | 0.988/0.989 | KXNHLTEAMTOTAL-26OCT27LACHI-LA4 +0.071 |
| MTL @ STL | 0.465 | 0.567 | 0.172 | 0.213 | 6.57 | 6.54 | 1.032/0.983 | KXNHLGAME-26OCT27MTLSTL-MTL -0.103 |
| NYI @ NSH | 0.527 | 0.529 | 0.175 | 0.218 | 6.17 | 6.36 | 1.002/0.973 | KXNHLTOTAL-26OCT27NYINSH-7 +0.041 |
| NJD @ DAL | 0.561 | 0.553 | 0.187 | 0.229 | 5.58 | 5.89 | 0.968/0.949 | KXNHLTOTAL-26OCT27NJDAL-7 +0.059 |
| FLA @ WPG | 0.525 | 0.530 | 0.184 | 0.224 | 5.99 | 6.11 | 0.997/0.991 | KXNHLTOTAL-26OCT27FLAWPG-5 +0.022 |
| MIN @ UTA | 0.532 | 0.566 | 0.173 | 0.212 | 6.20 | 6.40 | 0.991/0.991 | KXNHLTEAMTOTAL-26OCT27MINUTA-UTA4 +0.051 |
| OTT @ VGK | 0.596 | 0.586 | 0.168 | 0.213 | 6.66 | 6.34 | 1.004/1.051 | KXNHLTOTAL-26OCT27OTTVGK-8 -0.054 |
| VAN @ ANA | 0.638 | 0.599 | 0.159 | 0.205 | 6.80 | 6.80 | 1.024/1.026 | KXNHLSPREAD-26OCT27VANANA-ANA2 -0.043 |
| BUF @ SJS | 0.473 | 0.529 | 0.168 | 0.221 | 6.68 | 6.50 | 1.034/0.998 | KXNHLGAME-26OCT27BUFSJ-BUF -0.057 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 42 recommended · full analysis in card.md / packet.json `thesis_card`

- Damon Severson: 1+ goals YES @ 8c · p 0.1152 (adj 0.1026) · $1.7 · thesis CBJ:OFFENSE_4PLUS
- Noah Cates: 1+ goals YES @ 12c · p 0.1559 (adj 0.1444) · $1.9 · thesis PHI:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 15c · p 0.1855 (adj 0.1754) · $1.98 · thesis CBJ:OFFENSE_4PLUS
- Pavel Zacha: 1+ goals YES @ 21c · p 0.2769 (adj 0.2589) · $4.75 · thesis BOS:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 13c · p 0.1851 (adj 0.1651) · $3.0 · thesis BOS:OFFENSE_4PLUS
- Mark Kastelic: 1+ goals YES @ 7c · p 0.1058 (adj 0.0944) · $1.98 · thesis BOS:OFFENSE_4PLUS
- William Borgen: 1+ goals YES @ 4c · p 0.0624 (adj 0.0543) · $1.03 · thesis BOS:WINS_BY_2PLUS
- Roman Kantserov: 1+ goals NO @ 73c · p 0.7945 (adj 0.7771) · $7.12 · thesis CHI:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 55c · p 0.7003 (adj 0.5961) · $5.42 · thesis CHI:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0764 (adj 0.066) · $1.02 · thesis LAK:OFFENSE_4PLUS
- Erik Gustafsson: 1+ assists NO @ 61c · p 0.7334 (adj 0.6499) · $6.44 · thesis LAK:SUPPRESSED
- Pius Suter: 1+ goals YES @ 14c · p 0.1867 (adj 0.1688) · $2.22 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 30c · p 0.3566 (adj 0.3387) · $3.55 · thesis STL:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 26c · p 0.3059 (adj 0.2932) · $2.74 · thesis STL:OFFENSE_4PLUS
- Jonatan Berggren: 1+ goals YES @ 14c · p 0.173 (adj 0.161) · $1.48 · thesis STL:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 13c · p 0.1737 (adj 0.1615) · $2.6 · thesis NSH:WINS_BY_2PLUS
- Victor Eklund: 1+ assists NO @ 72c · p 0.7992 (adj 0.7546) · $8.36 · thesis NYI:SUPPRESSED
- Mavrik Bourque: 1+ goals YES @ 17c · p 0.2085 (adj 0.1976) · $2.08 · thesis NSH:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 12c · p 0.1541 (adj 0.1418) · $1.72 · thesis NYI:OFFENSE_4PLUS
- Connor Brown: 1+ goals YES @ 11c · p 0.1594 (adj 0.1458) · $3.24 · thesis NJD:OFFENSE_4PLUS
- Roope Hintz: 1+ goals YES @ 26c · p 0.3052 (adj 0.2927) · $2.68 · thesis DAL:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 68c · p 0.7228 (adj 0.7108) · $5.22 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ assists NO @ 56c · p 0.6311 (adj 0.5906) · $4.26 · thesis NJD:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 66c · p 0.7201 (adj 0.7026) · $5.13 · thesis FLA:SUPPRESSED
- Seth Jones: 1+ assists NO @ 55c · p 0.64 (adj 0.5925) · $3.27 · thesis FLA:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 68c · p 0.7302 (adj 0.7164) · $4.14 · thesis FLA:SUPPRESSED
- Cole Schwindt: 1+ goals YES @ 9c · p 0.1179 (adj 0.1072) · $1.25 · thesis FLA:OFFENSE_4PLUS
- Olli Maatta: 1+ goals YES @ 3c · p 0.0559 (adj 0.0469) · $1.32 · thesis MIN:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 57c · p 0.6373 (adj 0.6192) · $8.06 · thesis MIN:SUPPRESSED
- Anders Lee: 1+ goals YES @ 20c · p 0.2451 (adj 0.2326) · $2.66 · thesis UTA:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ assists NO @ 49c · p 0.6045 (adj 0.5268) · $4.48 · thesis MIN:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0878 (adj 0.0759) · $1.11 · thesis VGK:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 59c · p 0.712 (adj 0.6294) · $6.61 · thesis OTT:SUPPRESSED
- Ivan Barbashev: 1+ goals YES @ 21c · p 0.2479 (adj 0.2359) · $1.85 · thesis VGK:OFFENSE_4PLUS
- Jack Eichel: 1+ goals NO @ 66c · p 0.6991 (adj 0.6881) · $3.96 · thesis VGK:SUPPRESSED
- Max Sasson: 1+ goals YES @ 12c · p 0.1623 (adj 0.1492) · $2.39 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 17c · p 0.2134 (adj 0.2001) · $2.39 · thesis VAN:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2379 (adj 0.2172) · $2.01 · thesis VAN:OFFENSE_4PLUS
- Adam Gaudette: 1+ goals YES @ 13c · p 0.1775 (adj 0.1631) · $2.7 · thesis SJS:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 62c · p 0.6821 (adj 0.6653) · $7.99 · thesis BUF:SUPPRESSED
- Ivar Stenberg: 1+ goals NO @ 77c · p 0.8133 (adj 0.8012) · $8.13 · thesis SJS:SUPPRESSED
- Macklin Celebrini: 1+ assists NO @ 43c · p 0.5683 (adj 0.4608) · $2.08 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CBJ @ PHI** · priced 178/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.63, exp saves 24.07 (sd 6.4), pull risk 0.049
- CBJ net: Cam Talbot (CONFIRMED) exp shots 25.48, exp saves 22.01 (sd 6.26), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Werenski: 1+ assists | 0.445 | 0.560 | 57/45 | +0.088 | STANDARD |
| Zach Werenski: 2+ points | 0.196 | 0.310 | 32/70 | +0.089 | STANDARD |
| Zach Werenski: 1+ points | 0.550 | 0.655 | 66/35 | +0.084 | STANDARD |
| Valeri Nichushkin: 1+ points | 0.381 | 0.480 | 49/53 | +0.072 | STANDARD |
| Travis Sanheim: 1+ points | 0.396 | 0.315 | 34/71 | +0.040 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.229 | 0.310 | 32/70 | +0.056 | STANDARD |

**BOS @ CAR** · priced 181/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.29, exp saves 20.31 (sd 5.85), pull risk 0.064
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 32.38, exp saves 27.54 (sd 7.68), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sean Walker: 1+ points | 0.402 | 0.295 | 31/72 | +0.077 | STANDARD |
| Sean Walker: 1+ assists | 0.333 | 0.235 | 26/79 | +0.059 | STANDARD |
| Seth Jarvis: 1+ assists | 0.253 | 0.350 | 37/67 | +0.062 | STANDARD |
| K'Andre Miller: 1+ assists | 0.352 | 0.270 | 28/74 | +0.057 | STANDARD |
| Jeremy Swayman: 30+ saves | 0.394 | 0.475 | 51/56 | +0.029 |  |
| Casey Mittelstadt: 1+ goals | 0.185 | 0.105 | 13/92 | +0.047 | STANDARD |

**LAK @ CHI** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 28.78, exp saves 24.84 (sd 6.75), pull risk 0.059
- LAK net: Anton Forsberg (PROJECTED) exp shots 25.18, exp saves 21.9 (sd 6.11), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.300 | 0.460 | 47/55 | +0.133 | STANDARD |
| Erik Gustafsson: 1+ assists | 0.267 | 0.395 | 40/61 | +0.107 | STANDARD |
| Patrick Kane: 1+ points | 0.462 | 0.585 | 60/43 | +0.091 | STANDARD |
| Erik Gustafsson: 1+ points | 0.322 | 0.425 | 43/58 | +0.081 | STANDARD |
| Connor Bedard: 1+ assists | 0.374 | 0.475 | 49/54 | +0.069 | STANDARD |
| Connor Bedard: 1+ points | 0.551 | 0.640 | 65/37 | +0.063 | STANDARD |

**MTL @ STL** · priced 176/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Jordan Binnington (CONFIRMED) exp shots 26.31, exp saves 22.93 (sd 6.47), pull risk 0.058
- MTL net: Jacob Fowler (CONFIRMED) exp shots 27.26, exp saves 23.12 (sd 6.58), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonatan Berggren: 1+ points | 0.440 | 0.320 | 35/71 | +0.074 | STANDARD |
| Jonatan Berggren: 1+ assists | 0.325 | 0.210 | 24/82 | +0.072 | STANDARD |
| Jordan Binnington: 25+ saves | 0.392 | 0.505 | 53/52 | +0.071 |  |
| Philip Broberg: 1+ assists | 0.438 | 0.335 | 35/68 | +0.072 | STANDARD |
| Philip Broberg: 1+ points | 0.504 | 0.405 | 42/61 | +0.067 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.264 | 0.175 | 20/85 | +0.053 | STANDARD |

**NYI @ NSH** · priced 172/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 28.8, exp saves 24.81 (sd 6.84), pull risk 0.063
- NYI net: Semyon Varlamov (PROBABLE) exp shots 27.04, exp saves 23.32 (sd 6.58), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Wilsby: 1+ assists | 0.303 | 0.195 | 22/83 | +0.071 | STANDARD |
| Adam Wilsby: 1+ points | 0.358 | 0.255 | 27/76 | +0.074 | STANDARD |
| Victor Eklund: 1+ assists | 0.201 | 0.290 | 30/72 | +0.065 | STANDARD |
| Matthew Wood: 1+ points | 0.393 | 0.310 | 33/71 | +0.047 | STANDARD |
| Steven Stamkos: 2+ points | 0.252 | 0.170 | 24/90 | -0.000 | STANDARD |
| Emil Heineman: 1+ assists | 0.270 | 0.195 | 22/83 | +0.038 | STANDARD |

**NJD @ DAL** · priced 200/212 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Casey DeSmith (CONFIRMED) exp shots 26.96, exp saves 23.52 (sd 6.41), pull risk 0.052
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.01, exp saves 22.56 (sd 6.28), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cody Glass: 1+ points | 0.279 | 0.120 | 22/98 | +0.047 | STANDARD |
| Nils Lundkvist: 1+ assists | 0.249 | 0.110 | 20/98 | +0.037 | STANDARD |
| Justin Hryckowian: 1+ assists | 0.256 | 0.125 | 23/98 | +0.014 | STANDARD |
| Arttu Hyry: 1+ points | 0.276 | 0.150 | 28/98 | -0.018 | STANDARD |
| Nils Lundkvist: 1+ points | 0.289 | 0.170 | 23/89 | +0.047 | STANDARD |
| Lian Bichsel: 1+ points | 0.213 | 0.095 | 17/98 | +0.034 | STANDARD |

**FLA @ WPG** · priced 170/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Clay Stevenson (CONFIRMED) exp shots 27.13, exp saves 23.59 (sd 6.44), pull risk 0.056
- FLA net: Akira Schmid (CONFIRMED) exp shots 26.32, exp saves 22.64 (sd 6.37), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ points | 0.485 | 0.600 | 61/41 | +0.088 | STANDARD |
| Seth Jones: 1+ points | 0.413 | 0.515 | 52/49 | +0.079 | STANDARD |
| Brady Tkachuk: 1+ points | 0.504 | 0.600 | 61/41 | +0.069 | STANDARD |
| Seth Jones: 1+ assists | 0.360 | 0.455 | 46/55 | +0.073 | STANDARD |
| Sam Reinhart: 1+ assists | 0.295 | 0.385 | 40/63 | +0.058 | STANDARD |
| Sam Reinhart: 2+ points | 0.146 | 0.235 | 26/79 | +0.052 | STANDARD |

**MIN @ UTA** · priced 181/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 27.66, exp saves 24.12 (sd 6.62), pull risk 0.058
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 28.67, exp saves 24.6 (sd 6.85), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.247 | 0.390 | 41/63 | +0.107 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.396 | 0.515 | 52/49 | +0.097 | STANDARD |
| Kailer Yamamoto: 1+ points | 0.434 | 0.325 | 35/70 | +0.068 | STANDARD |
| Quinn Hughes: 1+ assists | 0.514 | 0.610 | 62/40 | +0.069 | STANDARD |
| Kailer Yamamoto: 1+ assists | 0.288 | 0.195 | 22/83 | +0.056 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.613 | 0.705 | 72/31 | +0.062 | STANDARD |

**OTT @ VGK** · priced 177/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 26.26, exp saves 22.89 (sd 6.32), pull risk 0.053
- OTT net: Samuel Ersson (PROJECTED) exp shots 26.79, exp saves 22.83 (sd 6.49), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.402 | 0.530 | 54/48 | +0.100 | STANDARD |
| Jake Sanderson: 1+ assists | 0.288 | 0.415 | 42/59 | +0.105 | STANDARD |
| Jake Sanderson: 1+ points | 0.369 | 0.495 | 51/52 | +0.093 | STANDARD |
| Shea Theodore: 1+ assists | 0.357 | 0.245 | 27/78 | +0.073 | STANDARD |
| Mitch Marner: 1+ points | 0.552 | 0.640 | 66/38 | +0.052 | STANDARD |
| Jack Eichel: 2+ points | 0.262 | 0.350 | 37/67 | +0.052 | STANDARD |

**VAN @ ANA** · priced 173/192 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 23.87, exp saves 20.89 (sd 5.94), pull risk 0.059
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.6, exp saves 26.65 (sd 7.58), pull risk 0.096

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tom Willander: 1+ points | 0.324 | 0.155 | 28/97 | +0.030 | STANDARD |
| Max Sasson: 1+ points | 0.308 | 0.145 | 27/98 | +0.024 | STANDARD |
| Tom Willander: 1+ assists | 0.281 | 0.130 | 24/98 | +0.029 | STANDARD |
| Tim Washe: 1+ points | 0.421 | 0.275 | 30/75 | +0.106 | STANDARD |
| Tyson Hinds: 1+ assists | 0.218 | 0.080 | 14/98 | +0.070 | STANDARD |
| Brendan Gallagher: 1+ points | 0.278 | 0.145 | 27/98 | -0.006 | STANDARD |

**BUF @ SJS** · priced 193/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.51, exp saves 24.66 (sd 6.74), pull risk 0.066
- BUF net: Colten Ellis (PROJECTED) exp shots 27.09, exp saves 23.32 (sd 6.57), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.432 | 0.575 | 58/43 | +0.121 | STANDARD |
| Ivar Stenberg: 1+ points | 0.414 | 0.555 | 56/45 | +0.118 | STANDARD |
| Rasmus Dahlin: 1+ assists | 0.410 | 0.525 | 54/49 | +0.083 | STANDARD |
| Rasmus Dahlin: 1+ points | 0.509 | 0.620 | 63/39 | +0.084 | STANDARD |
| Tage Thompson: 1+ assists | 0.330 | 0.440 | 45/57 | +0.083 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.276 | 0.385 | 40/63 | +0.078 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
