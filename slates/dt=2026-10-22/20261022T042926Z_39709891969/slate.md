# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T04:29:26Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 2511 · contracts joined: 612 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 312, 'OK': 177, 'NO_EDGE': 123}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'game_early_goal': 12, 'game_winner': 24, 'game_overtime': 12, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 2026-10-22T23:00:00Z | T-12h | 0.618 | 0.382 | 0.169 | 6.24 | 3.50 | 2.74 | 51 (25/26) | PROJECTED/PROJECTED |
| NYR @ TOR | 2026-10-22T23:00:00Z | T-12h | 0.456 | 0.544 | 0.173 | 6.44 | 3.09 | 3.36 | 51 (25/26) | PROJECTED/PROJECTED |
| SJS @ OTT | 2026-10-22T23:00:00Z | T-12h | 0.607 | 0.393 | 0.168 | 6.26 | 3.47 | 2.79 | 51 (25/26) | PROJECTED/PROJECTED |
| ANA @ NJD | 2026-10-22T23:00:00Z | T-12h | 0.595 | 0.405 | 0.175 | 6.26 | 3.43 | 2.83 | 51 (25/26) | PROJECTED/PROJECTED |
| FLA @ PIT | 2026-10-22T23:00:00Z | T-12h | 0.514 | 0.486 | 0.164 | 6.81 | 3.46 | 3.36 | 51 (25/26) | PROJECTED/PROJECTED |
| LAK @ NYI | 2026-10-22T23:30:00Z | T-12h | 0.586 | 0.414 | 0.182 | 5.68 | 3.11 | 2.57 | 51 (25/26) | PROJECTED/PROJECTED |
| VGK @ STL | 2026-10-23T00:00:00Z | T-12h | 0.533 | 0.467 | 0.174 | 6.25 | 3.23 | 3.02 | 51 (25/26) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-12h | 0.596 | 0.404 | 0.183 | 5.55 | 3.06 | 2.49 | 51 (25/26) | PROJECTED/PROJECTED |
| MIN @ CGY | 2026-10-23T01:00:00Z | T-12h | 0.457 | 0.543 | 0.186 | 5.85 | 2.79 | 3.06 | 51 (25/26) | PROJECTED/PROJECTED |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-12h | 0.533 | 0.467 | 0.170 | 6.55 | 3.37 | 3.17 | 51 (25/26) | PROJECTED/PROJECTED |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-12h | 0.488 | 0.512 | 0.178 | 6.29 | 3.11 | 3.18 | 51 (25/26) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-12h | 0.450 | 0.550 | 0.174 | 6.37 | 3.02 | 3.35 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.375 | 0.485 | 0.463 | 49 | 52 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.311 | 0.415 | 0.393 | 42 | 59 | no | +0.082 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.457 | 0.355 | 0.375 | 36 | 65 | yes | +0.081 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.187 | 0.285 | 0.263 | 29 | 72 | no | +0.079 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.488 | 0.395 | 0.413 | 40 | 61 | yes | +0.071 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.512 | 0.605 | 0.587 | 61 | 40 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.293 | 0.385 | 0.366 | 39 | 62 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.596 | 0.690 | 0.672 | 70 | 32 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.399 | 0.495 | 0.476 | 51 | 52 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.174 | 0.255 | 0.237 | 26 | 75 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.380 | 0.470 | 0.452 | 48 | 54 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.214 | 0.295 | 0.278 | 30 | 71 | no | +0.061 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.543 | 0.625 | 0.609 | 63 | 38 | no | +0.060 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.533 | 0.455 | 0.470 | 46 | 55 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.600 | 0.685 | 0.669 | 70 | 33 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA3 | team_total | 0.622 | 0.700 | 0.685 | 71 | 31 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.194 | 0.270 | 0.253 | 28 | 74 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.481 | 0.555 | 0.540 | 56 | 45 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.686 | 0.755 | 0.742 | 76 | 25 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.197 | 0.270 | 0.254 | 28 | 74 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.239 | 0.175 | 0.187 | 18 | 83 | yes | +0.049 | OK |
| KXNHLGAME-26OCT22LANYI-LA | game_winner | 0.414 | 0.485 | 0.471 | 49 | 52 | no | +0.049 | OK |
| KXNHLGAME-26OCT22LANYI-NYI | game_winner | 0.586 | 0.515 | 0.529 | 52 | 49 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.279 | 0.210 | 0.223 | 22 | 80 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.806 | 0.865 | 0.855 | 87 | 14 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.105 | 0.165 | 0.151 | 17 | 84 | no | +0.046 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.467 | 0.535 | 0.522 | 54 | 47 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA2 | game_spread | 0.203 | 0.265 | 0.252 | 27 | 74 | no | +0.044 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.615 | 0.602 | 62 | 39 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.809 | 0.865 | 0.855 | 87 | 14 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.340 | 0.405 | 0.392 | 41 | 60 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.316 | 0.255 | 0.267 | 26 | 75 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.351 | 0.420 | 0.406 | 43 | 59 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT22SJOTT-SJ4 | team_total | 0.313 | 0.380 | 0.366 | 39 | 63 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.236 | 0.295 | 0.283 | 30 | 71 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.453 | 0.515 | 0.503 | 52 | 49 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.150 | 0.205 | 0.193 | 21 | 80 | no | +0.039 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.596 | 0.655 | 0.644 | 66 | 35 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.209 | 0.265 | 0.253 | 27 | 74 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.258 | 0.315 | 0.303 | 32 | 69 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.268 | 0.330 | 0.317 | 34 | 68 | no | +0.037 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.467 | 0.525 | 0.513 | 53 | 48 | no | +0.036 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.533 | 0.475 | 0.487 | 48 | 53 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT22LANYI-NYI2 | game_spread | 0.351 | 0.290 | 0.302 | 30 | 72 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA5 | team_total | 0.221 | 0.285 | 0.271 | 30 | 73 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.787 | 0.840 | 0.830 | 85 | 17 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT22SJOTT-SJ3 | team_total | 0.530 | 0.595 | 0.582 | 61 | 42 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA2 | team_total | 0.820 | 0.870 | 0.861 | 88 | 14 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22SJOTT-SJ2 | team_total | 0.758 | 0.815 | 0.805 | 83 | 20 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22SJOTT-SJ3 | game_spread | 0.111 | 0.155 | 0.145 | 16 | 85 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.417 | 0.365 | 0.375 | 37 | 64 | yes | +0.030 | OK |
| KXNHLGAME-26OCT22SJOTT-OTT | game_winner | 0.607 | 0.555 | 0.566 | 56 | 45 | yes | +0.030 | OK |
| KXNHLGAME-26OCT22SJOTT-SJ | game_winner | 0.393 | 0.445 | 0.434 | 45 | 56 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.335 | 0.385 | 0.375 | 39 | 62 | no | +0.029 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.405 | 0.355 | 0.365 | 36 | 65 | yes | +0.029 | OK |
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.595 | 0.645 | 0.635 | 65 | 36 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5 | team_total | 0.266 | 0.320 | 0.309 | 33 | 69 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.464 | 0.520 | 0.509 | 53 | 49 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3 | team_total | 0.678 | 0.730 | 0.720 | 74 | 28 | no | +0.028 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.404 | 0.355 | 0.365 | 36 | 65 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT22SJOTT-SJ2 | game_spread | 0.199 | 0.250 | 0.239 | 26 | 76 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT22SJOTT-OTT2 | game_spread | 0.382 | 0.330 | 0.340 | 34 | 68 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-8 | game_total | 0.172 | 0.220 | 0.210 | 23 | 79 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT22DETVAN-VAN2 | game_spread | 0.247 | 0.205 | 0.213 | 21 | 80 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ2 | game_spread | 0.368 | 0.420 | 0.409 | 43 | 59 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA2 | team_total | 0.724 | 0.775 | 0.765 | 79 | 24 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22SJOTT-SJ5 | team_total | 0.156 | 0.205 | 0.194 | 22 | 81 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET3 | team_total | 0.652 | 0.700 | 0.691 | 71 | 31 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4 | team_total | 0.317 | 0.270 | 0.279 | 28 | 74 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA6 | team_total | 0.097 | 0.065 | 0.070 | 7 | 94 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.158 | 0.200 | 0.191 | 21 | 81 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM2 | game_spread | 0.315 | 0.275 | 0.283 | 28 | 73 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL6 | team_total | 0.106 | 0.075 | 0.080 | 8 | 93 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL6 | team_total | 0.082 | 0.120 | 0.111 | 13 | 89 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.265 | 0.310 | 0.301 | 32 | 70 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR3 | game_spread | 0.149 | 0.185 | 0.177 | 19 | 82 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA5 | team_total | 0.121 | 0.155 | 0.148 | 16 | 85 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT22MINCGY-5 | game_total | 0.728 | 0.765 | 0.758 | 77 | 24 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-9 | game_total | 0.113 | 0.150 | 0.142 | 16 | 86 | no | +0.019 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 0.618 | 0.591 | 0.169 | 0.209 | 6.24 | 6.53 | 0.968/1.000 | KXNHLTEAMTOTAL-26OCT22NSHBOS-NSH3 +0.058 |
| NYR @ TOR | 0.456 | 0.520 | 0.173 | 0.219 | 6.44 | 6.30 | 0.965/0.992 | KXNHLGAME-26OCT22NYRTOR-NYR -0.064 |
| SJS @ OTT | 0.607 | 0.601 | 0.168 | 0.213 | 6.26 | 6.20 | 0.998/1.034 | KXNHLTOTAL-26OCT22SJOTT-6 -0.019 |
| ANA @ NJD | 0.595 | 0.542 | 0.175 | 0.214 | 6.26 | 6.39 | 0.987/1.024 | KXNHLTEAMTOTAL-26OCT22ANANJ-ANA4 +0.058 |
| FLA @ PIT | 0.514 | 0.556 | 0.164 | 0.211 | 6.81 | 6.61 | 1.033/0.998 | KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA4 -0.048 |
| LAK @ NYI | 0.586 | 0.542 | 0.182 | 0.224 | 5.68 | 5.91 | 0.956/0.993 | KXNHLTEAMTOTAL-26OCT22LANYI-LA3 +0.063 |
| VGK @ STL | 0.533 | 0.492 | 0.174 | 0.224 | 6.25 | 6.33 | 0.993/1.003 | KXNHLSPREAD-26OCT22VGKSTL-STL2 -0.044 |
| WPG @ DAL | 0.596 | 0.577 | 0.183 | 0.220 | 5.55 | 5.96 | 0.986/0.988 | KXNHLTOTAL-26OCT22WPGDAL-7 +0.072 |
| MIN @ CGY | 0.457 | 0.450 | 0.186 | 0.219 | 5.85 | 6.12 | 0.986/0.995 | KXNHLTOTAL-26OCT22MINCGY-7 +0.046 |
| CAR @ EDM | 0.533 | 0.567 | 0.170 | 0.205 | 6.55 | 6.76 | 0.994/0.989 | KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 +0.050 |
| UTA @ SEA | 0.488 | 0.497 | 0.178 | 0.223 | 6.29 | 6.53 | 1.015/0.992 | KXNHLTOTAL-26OCT22UTASEA-7 +0.051 |
| DET @ VAN | 0.450 | 0.532 | 0.174 | 0.221 | 6.37 | 6.28 | 1.021/1.003 | KXNHLSPREAD-26OCT22DETVAN-DET2 -0.085 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 17 recommended · full analysis in card.md / packet.json `thesis_card`

- Full Game: Over 6.5 goals scored YES @ 43c · p 0.508 (adj 0.4665) · $8.65 · thesis GAME:HIGH_EVENT
- New Jersey wins by over 2.5 goals NO @ 71c · p 0.7897 (adj 0.7473) · $20.0 · thesis ANA:WINS
- Anaheim wins by over 1.5 goals YES @ 19c · p 0.2485 (adj 0.2167) · $2.81 · thesis ANA:WINS_BY_2PLUS
- Dallas wins by over 2.5 goals NO @ 71c · p 0.7727 (adj 0.7389) · $11.59 · thesis GAME:TIGHT
- Winnipeg wins by over 1.5 goals YES @ 17c · p 0.2189 (adj 0.192) · $2.43 · thesis WPG:WINS_BY_2PLUS
- Minnesota wins by over 1.5 goals NO @ 59c · p 0.6801 (adj 0.6325) · $8.25 · thesis CGY:WINS
- Minnesota wins by over 2.5 goals NO @ 72c · p 0.7956 (adj 0.7553) · $10.35 · thesis CGY:WINS
- Calgary wins by over 1.5 goals YES @ 18c · p 0.2396 (adj 0.2073) · $2.09 · thesis CGY:WINS_BY_2PLUS
- Calgary over 4.5 goals scored YES @ 13c · p 0.1756 (adj 0.1503) · $1.07 · thesis CGY:OFFENSE_4PLUS
- Edmonton wins by over 1.5 goals YES @ 28c · p 0.3528 (adj 0.3139) · $6.03 · thesis EDM:WINS_BY_2PLUS
- Carolina wins by over 1.5 goals NO @ 70c · p 0.7601 (adj 0.725) · $3.34 · thesis EDM:WINS
- Utah wins by over 1.5 goals NO @ 62c · p 0.7024 (adj 0.6587) · $14.35 · thesis SEA:WINS
- Utah wins by over 2.5 goals NO @ 75c · p 0.8115 (adj 0.7782) · $2.54 · thesis SEA:WINS
- Vancouver wins by over 2.5 goals YES @ 13c · p 0.2007 (adj 0.1628) · $3.75 · thesis VAN:WINS_BY_2PLUS
- Detroit over 1.5 goals scored NO @ 13c · p 0.1972 (adj 0.1611) · $3.11 · thesis DET:SUPPRESSED
- Detroit wins by over 1.5 goals NO @ 62c · p 0.75 (adj 0.6623) · $6.33 · thesis VAN:WINS
- Detroit wins by over 2.5 goals NO @ 74c · p 0.8462 (adj 0.7739) · $12.26 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ BOS** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.6, exp saves 24.04 (sd 6.61), pull risk 0.059
- NSH net: Juuse Saros (PROJECTED) exp shots 28.42, exp saves 24.26 (sd 6.82), pull risk 0.076

**NYR @ TOR** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- TOR net: Anthony Stolarz (PROJECTED) exp shots 27.8, exp saves 24.16 (sd 6.6), pull risk 0.062
- NYR net: Dylan Garand (PROJECTED) exp shots 26.92, exp saves 23.18 (sd 6.53), pull risk 0.065

**SJS @ OTT** · priced 0/0 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- OTT net: Linus Ullmark (PROJECTED) exp shots 24.89, exp saves 21.82 (sd 6.09), pull risk 0.048
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.6, exp saves 24.28 (sd 6.7), pull risk 0.072

**ANA @ NJD** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NJD net: Jake Allen (PROJECTED) exp shots 27.82, exp saves 24.19 (sd 6.58), pull risk 0.058
- ANA net: Lukas Dostal (PROJECTED) exp shots 29.59, exp saves 25.34 (sd 7.03), pull risk 0.072

**FLA @ PIT** · priced 0/0 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 26.42, exp saves 22.91 (sd 6.36), pull risk 0.064
- FLA net: Akira Schmid (PROJECTED) exp shots 27.3, exp saves 23.24 (sd 6.59), pull risk 0.078

**LAK @ NYI** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NYI net: Ilya Sorokin (PROJECTED) exp shots 26.76, exp saves 23.29 (sd 6.34), pull risk 0.049
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.67, exp saves 23.91 (sd 6.43), pull risk 0.06

**VGK @ STL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- STL net: Joel Hofer (PROJECTED) exp shots 27.55, exp saves 23.75 (sd 6.52), pull risk 0.065
- VGK net: Carter Hart (PROJECTED) exp shots 25.57, exp saves 22.06 (sd 6.24), pull risk 0.06

**WPG @ DAL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.62, exp saves 21.57 (sd 6.0), pull risk 0.045
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.81, exp saves 22.91 (sd 6.49), pull risk 0.066

**MIN @ CGY** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- CGY net: Devin Cooley (PROJECTED) exp shots 30.26, exp saves 26.03 (sd 7.03), pull risk 0.066
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.91, exp saves 25.12 (sd 6.74), pull risk 0.055

**CAR @ EDM** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- EDM net: Devon Levi (PROJECTED) exp shots 29.98, exp saves 26.02 (sd 6.87), pull risk 0.065
- CAR net: Brandon Bussi (PROJECTED) exp shots 25.41, exp saves 21.66 (sd 6.28), pull risk 0.082

**UTA @ SEA** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- SEA net: Philipp Grubauer (PROJECTED) exp shots 29.05, exp saves 25.06 (sd 6.94), pull risk 0.07
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.29 (sd 6.36), pull risk 0.069

**DET @ VAN** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.14 (sd 7.03), pull risk 0.054
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.68 (sd 6.21), pull risk 0.068

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
