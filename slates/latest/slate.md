# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T08:31:32Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 2511 · contracts joined: 612 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 312, 'OK': 110, 'NO_EDGE': 190}
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
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.311 | 0.420 | 0.397 | 43 | 59 | no | +0.082 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.187 | 0.295 | 0.271 | 31 | 72 | no | +0.079 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.551 | 0.455 | 0.474 | 46 | 55 | yes | +0.074 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.457 | 0.360 | 0.379 | 37 | 65 | yes | +0.071 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.449 | 0.535 | 0.518 | 54 | 47 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.214 | 0.295 | 0.278 | 30 | 71 | no | +0.061 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.543 | 0.625 | 0.609 | 63 | 38 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.443 | 0.355 | 0.372 | 37 | 66 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.380 | 0.465 | 0.448 | 48 | 55 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.244 | 0.320 | 0.304 | 33 | 69 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.686 | 0.755 | 0.742 | 76 | 25 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.197 | 0.280 | 0.262 | 30 | 74 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.333 | 0.260 | 0.274 | 27 | 75 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.239 | 0.175 | 0.187 | 18 | 83 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.596 | 0.685 | 0.668 | 71 | 34 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.230 | 0.300 | 0.285 | 31 | 71 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.144 | 0.220 | 0.203 | 24 | 80 | no | +0.045 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.615 | 0.602 | 62 | 39 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.351 | 0.420 | 0.406 | 43 | 59 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.453 | 0.515 | 0.503 | 52 | 49 | no | +0.040 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.596 | 0.655 | 0.644 | 66 | 35 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.655 | 0.580 | 0.595 | 60 | 44 | yes | +0.038 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.467 | 0.530 | 0.517 | 54 | 48 | no | +0.036 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.533 | 0.475 | 0.487 | 48 | 53 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.806 | 0.860 | 0.850 | 87 | 15 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.328 | 0.385 | 0.373 | 39 | 62 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.340 | 0.400 | 0.388 | 41 | 61 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.809 | 0.860 | 0.851 | 87 | 15 | no | +0.032 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.419 | 0.360 | 0.371 | 37 | 65 | yes | +0.032 | OK |
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.581 | 0.640 | 0.629 | 65 | 37 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ2 | game_spread | 0.361 | 0.420 | 0.408 | 43 | 59 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22LANYI-5 | game_total | 0.685 | 0.735 | 0.725 | 74 | 27 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.206 | 0.265 | 0.252 | 28 | 75 | no | +0.031 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.457 | 0.400 | 0.411 | 41 | 61 | yes | +0.030 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.543 | 0.605 | 0.593 | 62 | 41 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.335 | 0.390 | 0.379 | 40 | 62 | no | +0.029 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.404 | 0.350 | 0.361 | 36 | 66 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.209 | 0.265 | 0.253 | 28 | 75 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.485 | 0.545 | 0.533 | 56 | 47 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-8 | game_total | 0.172 | 0.225 | 0.214 | 24 | 79 | no | +0.026 | OK |
| KXNHLGAME-26OCT22LANYI-LA | game_winner | 0.437 | 0.485 | 0.475 | 49 | 52 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.117 | 0.170 | 0.158 | 19 | 85 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.787 | 0.835 | 0.826 | 85 | 18 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR3 | game_spread | 0.148 | 0.190 | 0.181 | 20 | 82 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.158 | 0.205 | 0.195 | 22 | 81 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.253 | 0.210 | 0.218 | 22 | 80 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.462 | 0.520 | 0.508 | 54 | 50 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.265 | 0.315 | 0.305 | 33 | 70 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-9 | game_total | 0.113 | 0.150 | 0.142 | 16 | 86 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.209 | 0.170 | 0.177 | 18 | 84 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET4 | team_total | 0.444 | 0.495 | 0.485 | 51 | 52 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT22ANANJ-ANA2 | game_spread | 0.219 | 0.185 | 0.191 | 19 | 82 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT22LANYI-6 | game_total | 0.445 | 0.490 | 0.481 | 50 | 52 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY3 | game_spread | 0.135 | 0.095 | 0.102 | 11 | 92 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT22LANYI-7 | game_total | 0.336 | 0.375 | 0.367 | 38 | 63 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT22LANYI-4 | game_total | 0.783 | 0.820 | 0.813 | 83 | 19 | no | +0.016 | OK |
| KXNHLGAME-26OCT22LANYI-NYI | game_winner | 0.563 | 0.520 | 0.529 | 53 | 49 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL6 | team_total | 0.122 | 0.085 | 0.091 | 10 | 93 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY3 | team_total | 0.533 | 0.480 | 0.491 | 50 | 54 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.389 | 0.425 | 0.418 | 43 | 58 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ6 | team_total | 0.127 | 0.165 | 0.157 | 18 | 85 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT22LANYI-9 | game_total | 0.109 | 0.135 | 0.129 | 14 | 87 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET3 | team_total | 0.652 | 0.695 | 0.687 | 71 | 32 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT22LANYI-8 | game_total | 0.167 | 0.210 | 0.201 | 23 | 81 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4 | team_total | 0.317 | 0.270 | 0.279 | 29 | 75 | yes | +0.012 | OK |
| KXNHLSPREAD-26OCT22FLAPIT-PIT3 | game_spread | 0.186 | 0.215 | 0.209 | 22 | 79 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET5 | team_total | 0.254 | 0.295 | 0.286 | 31 | 72 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT22LANYI-10 | game_total | 0.044 | 0.070 | 0.064 | 8 | 94 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA2 | team_total | 0.725 | 0.770 | 0.761 | 79 | 25 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA2 | game_spread | 0.216 | 0.255 | 0.247 | 27 | 76 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM2 | game_spread | 0.315 | 0.280 | 0.287 | 29 | 73 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY2 | team_total | 0.763 | 0.725 | 0.733 | 74 | 29 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT22NSHBOS-NSH3 | game_spread | 0.103 | 0.125 | 0.120 | 13 | 88 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-10 | game_total | 0.046 | 0.075 | 0.068 | 9 | 94 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-7 | game_total | 0.456 | 0.425 | 0.431 | 43 | 58 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT22MINCGY-5 | game_total | 0.728 | 0.760 | 0.754 | 77 | 25 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT22NSHBOS-BOS2 | game_spread | 0.395 | 0.360 | 0.367 | 37 | 65 | yes | +0.008 | OK |
| KXNHLSPREAD-26OCT22SJOTT-SJ3 | game_spread | 0.133 | 0.160 | 0.154 | 17 | 85 | no | +0.008 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Full Game: Over 6.5 goals scored YES @ 43c · p 0.508 (adj 0.4665) · $8.65 · thesis GAME:HIGH_EVENT
- New Jersey wins by over 2.5 goals NO @ 71c · p 0.791 (adj 0.7455) · $18.54 · thesis ANA:WINS
- Anaheim wins by over 1.5 goals YES @ 19c · p 0.2472 (adj 0.2161) · $2.78 · thesis ANA:WINS_BY_2PLUS
- Dallas wins by over 2.5 goals NO @ 71c · p 0.7727 (adj 0.7389) · $14.26 · thesis GAME:TIGHT
- Calgary wins by over 1.5 goals YES @ 18c · p 0.2396 (adj 0.2073) · $3.69 · thesis CGY:WINS_BY_2PLUS
- Minnesota wins by over 2.5 goals NO @ 72c · p 0.7956 (adj 0.7503) · $13.21 · thesis CGY:WINS
- Edmonton wins by over 1.5 goals YES @ 29c · p 0.3528 (adj 0.3164) · $4.06 · thesis EDM:WINS_BY_2PLUS
- Utah wins by over 1.5 goals NO @ 62c · p 0.7119 (adj 0.6634) · $19.01 · thesis SEA:WINS
- Detroit wins by over 1.5 goals NO @ 62c · p 0.75 (adj 0.659) · $14.09 · thesis VAN:WINS
- Detroit over 2.5 goals scored NO @ 32c · p 0.402 (adj 0.3535) · $2.35 · thesis DET:SUPPRESSED
- Vancouver wins by over 1.5 goals YES @ 23c · p 0.3064 (adj 0.2582) · $1.7 · thesis VAN:WINS_BY_2PLUS

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
