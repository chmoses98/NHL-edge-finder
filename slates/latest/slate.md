# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T06:23:14Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 2511 · contracts joined: 612 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 312, 'OK': 167, 'NO_EDGE': 133}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'game_early_goal': 12, 'game_winner': 24, 'game_overtime': 12, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 2026-10-22T23:00:00Z | T-12h | 0.618 | 0.382 | 0.169 | 6.24 | 3.50 | 2.74 | 51 (25/26) | PROJECTED/PROJECTED |
| NYR @ TOR | 2026-10-22T23:00:00Z | T-12h | 0.462 | 0.538 | 0.176 | 6.43 | 3.09 | 3.34 | 51 (25/26) | PROJECTED/PROJECTED |
| SJS @ OTT | 2026-10-22T23:00:00Z | T-12h | 0.569 | 0.431 | 0.168 | 6.47 | 3.47 | 3.01 | 51 (25/26) | PROJECTED/PROJECTED |
| ANA @ NJD | 2026-10-22T23:00:00Z | T-12h | 0.581 | 0.419 | 0.173 | 6.33 | 3.43 | 2.90 | 51 (25/26) | PROJECTED/PROJECTED |
| FLA @ PIT | 2026-10-22T23:00:00Z | T-12h | 0.508 | 0.492 | 0.171 | 6.73 | 3.39 | 3.34 | 51 (25/26) | PROJECTED/PROJECTED |
| LAK @ NYI | 2026-10-22T23:30:00Z | T-12h | 0.563 | 0.437 | 0.191 | 5.52 | 2.95 | 2.57 | 51 (25/26) | PROJECTED/PROJECTED |
| VGK @ STL | 2026-10-23T00:00:00Z | T-12h | 0.551 | 0.449 | 0.174 | 6.37 | 3.35 | 3.02 | 51 (25/26) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-12h | 0.596 | 0.404 | 0.183 | 5.55 | 3.06 | 2.49 | 51 (25/26) | PROJECTED/PROJECTED |
| MIN @ CGY | 2026-10-23T01:00:00Z | T-12h | 0.457 | 0.543 | 0.186 | 5.85 | 2.79 | 3.06 | 51 (25/26) | PROJECTED/PROJECTED |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-12h | 0.533 | 0.467 | 0.170 | 6.55 | 3.37 | 3.17 | 51 (25/26) | PROJECTED/PROJECTED |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-12h | 0.457 | 0.543 | 0.172 | 6.51 | 3.10 | 3.40 | 51 (25/26) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-12h | 0.450 | 0.550 | 0.174 | 6.37 | 3.02 | 3.35 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.375 | 0.485 | 0.463 | 49 | 52 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.311 | 0.415 | 0.393 | 42 | 59 | no | +0.082 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.457 | 0.355 | 0.375 | 36 | 65 | yes | +0.081 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.187 | 0.290 | 0.267 | 30 | 72 | no | +0.079 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.551 | 0.455 | 0.474 | 46 | 55 | yes | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.596 | 0.690 | 0.672 | 70 | 32 | no | +0.069 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.449 | 0.535 | 0.518 | 54 | 47 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.380 | 0.470 | 0.452 | 48 | 54 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.214 | 0.295 | 0.278 | 30 | 71 | no | +0.061 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.543 | 0.625 | 0.609 | 63 | 38 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.333 | 0.255 | 0.270 | 26 | 75 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.443 | 0.365 | 0.380 | 37 | 64 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.600 | 0.685 | 0.669 | 70 | 33 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.194 | 0.270 | 0.253 | 28 | 74 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.244 | 0.315 | 0.300 | 32 | 69 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.686 | 0.755 | 0.742 | 76 | 25 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.197 | 0.270 | 0.254 | 28 | 74 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.239 | 0.175 | 0.187 | 18 | 83 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.485 | 0.555 | 0.541 | 56 | 45 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.230 | 0.295 | 0.281 | 30 | 71 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.806 | 0.865 | 0.855 | 87 | 14 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.144 | 0.205 | 0.191 | 21 | 80 | no | +0.045 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.615 | 0.602 | 62 | 39 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.809 | 0.865 | 0.855 | 87 | 14 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.340 | 0.405 | 0.392 | 41 | 60 | no | +0.043 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.419 | 0.355 | 0.367 | 36 | 65 | yes | +0.043 | OK |
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.581 | 0.645 | 0.633 | 65 | 36 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.351 | 0.420 | 0.406 | 43 | 59 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.251 | 0.190 | 0.201 | 20 | 82 | yes | +0.040 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.457 | 0.395 | 0.407 | 40 | 61 | yes | +0.040 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.543 | 0.605 | 0.593 | 61 | 40 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.453 | 0.515 | 0.503 | 52 | 49 | no | +0.040 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.596 | 0.655 | 0.644 | 66 | 35 | no | +0.038 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.404 | 0.345 | 0.356 | 35 | 66 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.655 | 0.585 | 0.599 | 60 | 43 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.267 | 0.330 | 0.317 | 34 | 68 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.209 | 0.265 | 0.253 | 27 | 74 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL6 | team_total | 0.122 | 0.075 | 0.083 | 8 | 93 | yes | +0.037 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.467 | 0.525 | 0.513 | 53 | 48 | no | +0.036 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.533 | 0.475 | 0.487 | 48 | 53 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.328 | 0.385 | 0.373 | 39 | 62 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.117 | 0.165 | 0.154 | 17 | 84 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.787 | 0.840 | 0.830 | 85 | 17 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ2 | game_spread | 0.361 | 0.415 | 0.404 | 42 | 59 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5 | team_total | 0.264 | 0.320 | 0.308 | 33 | 69 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT22LANYI-5 | game_total | 0.685 | 0.735 | 0.725 | 74 | 27 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.206 | 0.260 | 0.249 | 27 | 75 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.462 | 0.520 | 0.508 | 53 | 49 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA2 | game_spread | 0.216 | 0.265 | 0.255 | 27 | 74 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.209 | 0.165 | 0.173 | 17 | 84 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.335 | 0.385 | 0.375 | 39 | 62 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-8 | game_total | 0.172 | 0.215 | 0.206 | 22 | 79 | no | +0.026 | OK |
| KXNHLGAME-26OCT22LANYI-LA | game_winner | 0.437 | 0.485 | 0.475 | 49 | 52 | no | +0.026 | OK |
| KXNHLGAME-26OCT22LANYI-NYI | game_winner | 0.563 | 0.515 | 0.525 | 52 | 49 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT22DETVAN-VAN2 | game_spread | 0.247 | 0.205 | 0.213 | 21 | 80 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.499 | 0.545 | 0.536 | 55 | 46 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK4 | team_total | 0.370 | 0.420 | 0.410 | 43 | 59 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET3 | team_total | 0.652 | 0.700 | 0.691 | 71 | 31 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA2 | team_total | 0.725 | 0.775 | 0.766 | 79 | 24 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR3 | game_spread | 0.148 | 0.185 | 0.177 | 19 | 82 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.158 | 0.200 | 0.191 | 21 | 81 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA5 | team_total | 0.120 | 0.165 | 0.155 | 18 | 85 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.253 | 0.210 | 0.218 | 22 | 80 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3 | team_total | 0.675 | 0.725 | 0.715 | 74 | 29 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM2 | game_spread | 0.315 | 0.275 | 0.283 | 28 | 73 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL6 | team_total | 0.082 | 0.120 | 0.111 | 13 | 89 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.265 | 0.310 | 0.301 | 32 | 70 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.583 | 0.630 | 0.621 | 64 | 38 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL2 | team_total | 0.841 | 0.800 | 0.809 | 81 | 21 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT22SJOTT-10 | game_total | 0.105 | 0.075 | 0.080 | 8 | 93 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT22MINCGY-5 | game_total | 0.728 | 0.765 | 0.758 | 77 | 24 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA5 | team_total | 0.209 | 0.170 | 0.177 | 18 | 84 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-9 | game_total | 0.113 | 0.150 | 0.142 | 16 | 86 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET2 | team_total | 0.843 | 0.875 | 0.869 | 88 | 13 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA6 | team_total | 0.093 | 0.065 | 0.070 | 7 | 94 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET4 | team_total | 0.444 | 0.490 | 0.481 | 50 | 52 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT22ANANJ-ANA2 | game_spread | 0.219 | 0.185 | 0.191 | 19 | 82 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-3 | game_total | 0.939 | 0.965 | 0.961 | 97 | 4 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT22LANYI-6 | game_total | 0.445 | 0.490 | 0.481 | 50 | 52 | no | +0.018 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 0.618 | 0.591 | 0.169 | 0.209 | 6.24 | 6.53 | 0.968/1.000 | KXNHLTEAMTOTAL-26OCT22NSHBOS-NSH3 +0.058 |
| NYR @ TOR | 0.462 | 0.510 | 0.176 | 0.217 | 6.43 | 6.32 | 0.978/0.992 | KXNHLSPREAD-26OCT22NYRTOR-NYR2 -0.052 |
| SJS @ OTT | 0.569 | 0.585 | 0.168 | 0.212 | 6.47 | 6.29 | 1.041/1.034 | KXNHLTOTAL-26OCT22SJOTT-8 -0.036 |
| ANA @ NJD | 0.581 | 0.536 | 0.173 | 0.212 | 6.33 | 6.41 | 0.992/1.024 | KXNHLGAME-26OCT22ANANJ-ANA +0.045 |
| FLA @ PIT | 0.508 | 0.558 | 0.171 | 0.212 | 6.73 | 6.58 | 1.021/1.001 | KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA4 -0.051 |
| LAK @ NYI | 0.563 | 0.543 | 0.191 | 0.220 | 5.52 | 5.90 | 0.956/0.989 | KXNHLTOTAL-26OCT22LANYI-7 +0.066 |
| VGK @ STL | 0.551 | 0.493 | 0.174 | 0.219 | 6.37 | 6.33 | 0.993/1.004 | KXNHLGAME-26OCT22VGKSTL-STL -0.058 |
| WPG @ DAL | 0.596 | 0.577 | 0.183 | 0.220 | 5.55 | 5.96 | 0.986/0.988 | KXNHLTOTAL-26OCT22WPGDAL-7 +0.072 |
| MIN @ CGY | 0.457 | 0.450 | 0.186 | 0.219 | 5.85 | 6.12 | 0.986/0.995 | KXNHLTOTAL-26OCT22MINCGY-7 +0.046 |
| CAR @ EDM | 0.533 | 0.567 | 0.170 | 0.205 | 6.55 | 6.76 | 0.994/0.989 | KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 +0.050 |
| UTA @ SEA | 0.457 | 0.502 | 0.172 | 0.216 | 6.51 | 6.51 | 1.005/0.992 | KXNHLGAME-26OCT22UTASEA-SEA +0.045 |
| DET @ VAN | 0.450 | 0.532 | 0.174 | 0.221 | 6.37 | 6.28 | 1.021/1.003 | KXNHLSPREAD-26OCT22DETVAN-DET2 -0.085 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 17 recommended · full analysis in card.md / packet.json `thesis_card`

- Full Game: Over 6.5 goals scored YES @ 43c · p 0.508 (adj 0.4665) · $8.65 · thesis GAME:HIGH_EVENT
- New Jersey wins by over 1.5 goals NO @ 59c · p 0.6815 (adj 0.6332) · $7.63 · thesis ANA:WINS
- New Jersey wins by over 2.5 goals NO @ 71c · p 0.791 (adj 0.748) · $13.96 · thesis ANA:WINS
- Anaheim wins by over 1.5 goals YES @ 19c · p 0.2472 (adj 0.2161) · $2.01 · thesis ANA:WINS_BY_2PLUS
- Dallas wins by over 2.5 goals NO @ 71c · p 0.7727 (adj 0.7389) · $14.26 · thesis GAME:TIGHT
- Minnesota wins by over 1.5 goals NO @ 59c · p 0.6801 (adj 0.6325) · $11.22 · thesis CGY:WINS
- Calgary wins by over 1.5 goals YES @ 18c · p 0.2396 (adj 0.2073) · $2.08 · thesis CGY:WINS_BY_2PLUS
- Minnesota wins by over 2.5 goals NO @ 72c · p 0.7956 (adj 0.7528) · $4.88 · thesis CGY:WINS
- Calgary over 4.5 goals scored YES @ 13c · p 0.1756 (adj 0.1503) · $1.09 · thesis CGY:OFFENSE_4PLUS
- Edmonton over 5.5 goals scored YES @ 10c · p 0.1475 (adj 0.1212) · $2.5 · thesis GAME:HIGH_EVENT
- Edmonton wins by over 1.5 goals YES @ 28c · p 0.3528 (adj 0.3139) · $4.08 · thesis EDM:WINS_BY_2PLUS
- Carolina wins by over 1.5 goals NO @ 70c · p 0.7601 (adj 0.725) · $2.63 · thesis EDM:WINS
- Utah wins by over 1.5 goals NO @ 62c · p 0.7119 (adj 0.6634) · $18.76 · thesis SEA:WINS
- Seattle over 4.5 goals scored YES @ 18c · p 0.2339 (adj 0.2019) · $1.14 · thesis SEA:OFFENSE_4PLUS
- Detroit wins by over 1.5 goals NO @ 62c · p 0.75 (adj 0.6623) · $10.82 · thesis VAN:WINS
- Detroit wins by over 2.5 goals NO @ 74c · p 0.8462 (adj 0.7739) · $12.26 · thesis VAN:WINS
- Vancouver wins by over 1.5 goals YES @ 21c · p 0.3064 (adj 0.2405) · $2.76 · thesis VAN:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ BOS** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.6, exp saves 24.04 (sd 6.61), pull risk 0.059
- NSH net: Juuse Saros (PROJECTED) exp shots 28.42, exp saves 24.26 (sd 6.82), pull risk 0.076

**NYR @ TOR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 27.8, exp saves 24.15 (sd 6.61), pull risk 0.062
- NYR net: Dylan Garand (PROJECTED) exp shots 26.92, exp saves 23.22 (sd 6.45), pull risk 0.062

**SJS @ OTT** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 24.89, exp saves 21.75 (sd 6.11), pull risk 0.055
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.6, exp saves 24.32 (sd 6.76), pull risk 0.074

**ANA @ NJD** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROJECTED) exp shots 27.82, exp saves 24.2 (sd 6.62), pull risk 0.06
- ANA net: Lukas Dostal (PROJECTED) exp shots 29.59, exp saves 25.38 (sd 6.99), pull risk 0.074

**FLA @ PIT** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (PROJECTED) exp shots 26.42, exp saves 23.0 (sd 6.33), pull risk 0.056
- FLA net: Cooper Black (PROJECTED) exp shots 27.3, exp saves 23.27 (sd 6.58), pull risk 0.079

**LAK @ NYI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 26.76, exp saves 23.28 (sd 6.36), pull risk 0.048
- LAK net: Anton Forsberg (PROJECTED) exp shots 27.67, exp saves 23.92 (sd 6.48), pull risk 0.06

**VGK @ STL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 27.55, exp saves 23.76 (sd 6.56), pull risk 0.064
- VGK net: Adin Hill (PROJECTED) exp shots 25.57, exp saves 22.06 (sd 6.14), pull risk 0.056

**WPG @ DAL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.62, exp saves 21.57 (sd 6.0), pull risk 0.045
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.81, exp saves 22.91 (sd 6.49), pull risk 0.066

**MIN @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 30.26, exp saves 26.03 (sd 7.03), pull risk 0.066
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.91, exp saves 25.12 (sd 6.74), pull risk 0.055

**CAR @ EDM** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 29.98, exp saves 26.02 (sd 6.87), pull risk 0.065
- CAR net: Brandon Bussi (PROJECTED) exp shots 25.41, exp saves 21.66 (sd 6.28), pull risk 0.082

**UTA @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 29.05, exp saves 25.1 (sd 6.78), pull risk 0.066
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.32), pull risk 0.065

**DET @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.14 (sd 7.02), pull risk 0.053
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.68 (sd 6.21), pull risk 0.068

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
