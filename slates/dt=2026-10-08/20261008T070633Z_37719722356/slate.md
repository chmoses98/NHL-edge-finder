# NHL slate 2026-10-08 — RESEARCH_ONLY

generated 2026-10-08T07:06:33Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 2532 · contracts joined: 510 (unjoined to any game: 1560)
gates: {'UNSUPPORTED': 260, 'OK': 132, 'NO_EDGE': 118}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'game_early_goal': 10, 'game_winner': 20, 'game_overtime': 10, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 2026-10-08T23:00:00Z | T-12h | 0.506 | 0.494 | 0.178 | 6.11 | 3.07 | 3.03 | 51 (25/26) | PROJECTED/PROJECTED |
| DAL @ BUF | 2026-10-08T23:00:00Z | T-12h | 0.561 | 0.439 | 0.178 | 6.12 | 3.24 | 2.88 | 51 (25/26) | PROJECTED/PROJECTED |
| NSH @ MTL | 2026-10-08T23:00:00Z | T-12h | 0.581 | 0.419 | 0.171 | 6.57 | 3.54 | 3.03 | 51 (25/26) | PROJECTED/PROJECTED |
| PHI @ OTT | 2026-10-08T23:00:00Z | T-12h | 0.565 | 0.435 | 0.174 | 6.13 | 3.26 | 2.87 | 51 (25/26) | PROJECTED/PROJECTED |
| MIN @ TBL | 2026-10-08T23:00:00Z | T-12h | 0.561 | 0.439 | 0.178 | 5.90 | 3.13 | 2.77 | 51 (25/26) | PROJECTED/PROJECTED |
| VAN @ CAR | 2026-10-08T23:00:00Z | T-12h | 0.667 | 0.333 | 0.160 | 6.62 | 3.87 | 2.75 | 51 (25/26) | PROJECTED/PROJECTED |
| CHI @ NYI | 2026-10-08T23:30:00Z | T-12h | 0.607 | 0.393 | 0.173 | 5.82 | 3.23 | 2.59 | 51 (25/26) | PROBABLE/PROJECTED |
| SJS @ STL | 2026-10-09T00:00:00Z | T-12h | 0.615 | 0.385 | 0.171 | 6.40 | 3.58 | 2.82 | 51 (25/26) | PROJECTED/PROJECTED |
| COL @ CGY | 2026-10-09T01:00:00Z | T-12h | 0.379 | 0.621 | 0.168 | 6.36 | 2.79 | 3.57 | 51 (25/26) | PROJECTED/PROJECTED |
| TOR @ VGK | 2026-10-09T02:00:00Z | T-12h | 0.679 | 0.321 | 0.153 | 6.72 | 3.96 | 2.76 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT08VANCAR-CAR3 | game_spread | 0.313 | 0.410 | 0.390 | 42 | 60 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR2 | game_spread | 0.448 | 0.535 | 0.518 | 54 | 47 | no | +0.064 | OK |
| KXNHLGAME-26OCT08VANCAR-CAR | game_winner | 0.667 | 0.745 | 0.730 | 75 | 26 | no | +0.060 | OK |
| KXNHLGAME-26OCT08VANCAR-VAN | game_winner | 0.333 | 0.250 | 0.266 | 26 | 76 | yes | +0.060 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK2 | game_spread | 0.465 | 0.385 | 0.401 | 39 | 62 | yes | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK3 | team_total | 0.769 | 0.690 | 0.707 | 70 | 32 | yes | +0.055 | OK |
| KXNHLGAME-26OCT08DALBUF-BUF | game_winner | 0.561 | 0.485 | 0.500 | 49 | 52 | yes | +0.053 | OK |
| KXNHLGAME-26OCT08DALBUF-DAL | game_winner | 0.439 | 0.515 | 0.500 | 52 | 49 | no | +0.053 | OK |
| KXNHLGAME-26OCT08TORVGK-VGK | game_winner | 0.679 | 0.605 | 0.620 | 61 | 40 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL3 | game_spread | 0.266 | 0.335 | 0.320 | 34 | 67 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL4 | team_total | 0.494 | 0.425 | 0.439 | 43 | 58 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT08TORVGK-8 | game_total | 0.339 | 0.275 | 0.287 | 28 | 73 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL2 | game_spread | 0.398 | 0.465 | 0.451 | 47 | 54 | no | +0.045 | OK |
| KXNHLGAME-26OCT08COLCGY-COL | game_winner | 0.621 | 0.685 | 0.673 | 69 | 32 | no | +0.043 | OK |
| KXNHLGAME-26OCT08COLCGY-CGY | game_winner | 0.379 | 0.315 | 0.327 | 32 | 69 | yes | +0.043 | OK |
| KXNHLGAME-26OCT08TORVGK-TOR | game_winner | 0.321 | 0.390 | 0.376 | 40 | 62 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4 | team_total | 0.305 | 0.235 | 0.248 | 25 | 78 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN3 | team_total | 0.519 | 0.440 | 0.456 | 46 | 58 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL2 | game_spread | 0.236 | 0.295 | 0.282 | 30 | 71 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT08SJSTL-6 | game_total | 0.597 | 0.535 | 0.548 | 54 | 47 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL4 | team_total | 0.334 | 0.405 | 0.390 | 42 | 61 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK3 | game_spread | 0.322 | 0.265 | 0.276 | 27 | 74 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL3 | game_spread | 0.132 | 0.185 | 0.173 | 19 | 82 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT08SJSTL-STL2 | game_spread | 0.393 | 0.335 | 0.346 | 34 | 67 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK4 | team_total | 0.574 | 0.485 | 0.503 | 52 | 55 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT08VANCAR-VAN2 | game_spread | 0.164 | 0.115 | 0.124 | 12 | 89 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT08SJSTL-7 | game_total | 0.482 | 0.420 | 0.432 | 43 | 59 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT08TORVGK-7 | game_total | 0.532 | 0.475 | 0.486 | 48 | 53 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL3 | team_total | 0.700 | 0.625 | 0.641 | 65 | 40 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT08SJSTL-8 | game_total | 0.287 | 0.225 | 0.237 | 24 | 79 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK6 | team_total | 0.203 | 0.140 | 0.151 | 16 | 88 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL5 | team_total | 0.296 | 0.230 | 0.242 | 25 | 79 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-8 | game_total | 0.314 | 0.260 | 0.270 | 27 | 75 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR3 | game_spread | 0.083 | 0.130 | 0.119 | 14 | 88 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2 | team_total | 0.752 | 0.695 | 0.707 | 71 | 32 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT08DALBUF-BUF2 | game_spread | 0.332 | 0.285 | 0.294 | 29 | 72 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL3 | team_total | 0.557 | 0.615 | 0.604 | 63 | 40 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK2 | team_total | 0.904 | 0.865 | 0.874 | 87 | 14 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT08TORVGK-6 | game_total | 0.643 | 0.590 | 0.601 | 60 | 42 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT08CHINYI-5 | game_total | 0.722 | 0.765 | 0.757 | 77 | 24 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT08NSHMTL-MTL3 | game_spread | 0.231 | 0.275 | 0.266 | 28 | 73 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY4 | team_total | 0.319 | 0.265 | 0.275 | 28 | 75 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT08VANCAR-VAN3 | game_spread | 0.088 | 0.055 | 0.061 | 6 | 95 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5 | team_total | 0.152 | 0.105 | 0.113 | 12 | 91 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT08TORVGK-9 | game_total | 0.244 | 0.200 | 0.208 | 21 | 81 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL5 | team_total | 0.167 | 0.215 | 0.205 | 23 | 80 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3 | team_total | 0.528 | 0.475 | 0.486 | 49 | 54 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL2 | team_total | 0.779 | 0.820 | 0.812 | 83 | 19 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL2 | team_total | 0.870 | 0.830 | 0.839 | 84 | 18 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT08CHINYI-NYI2 | game_spread | 0.373 | 0.415 | 0.406 | 42 | 59 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT08TORVGK-10 | game_total | 0.126 | 0.090 | 0.096 | 10 | 92 | yes | +0.020 | OK |
| KXNHLGAME-26OCT08UTABOS-UTA | game_winner | 0.494 | 0.535 | 0.527 | 54 | 47 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT08CHINYI-7 | game_total | 0.385 | 0.425 | 0.417 | 43 | 58 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-9 | game_total | 0.230 | 0.185 | 0.193 | 20 | 83 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY5 | team_total | 0.156 | 0.125 | 0.131 | 13 | 88 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT08UTABOS-UTA2 | game_spread | 0.277 | 0.315 | 0.307 | 32 | 69 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-CAR4 | team_total | 0.555 | 0.605 | 0.595 | 62 | 41 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT08CHINYI-NYI3 | game_spread | 0.229 | 0.265 | 0.257 | 27 | 74 | no | +0.018 | OK |
| KXNHLGAME-26OCT08SJSTL-SJ | game_winner | 0.385 | 0.425 | 0.417 | 43 | 58 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-7 | game_total | 0.505 | 0.465 | 0.473 | 47 | 54 | yes | +0.017 | OK |
| KXNHLSPREAD-26OCT08MINTB-TB3 | game_spread | 0.201 | 0.235 | 0.228 | 24 | 77 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH3 | team_total | 0.584 | 0.540 | 0.549 | 55 | 47 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK5 | team_total | 0.372 | 0.305 | 0.318 | 34 | 73 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-CAR3 | team_total | 0.752 | 0.785 | 0.779 | 79 | 22 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT08DALBUF-4 | game_total | 0.846 | 0.875 | 0.870 | 88 | 13 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT08UTABOS-UTA3 | game_spread | 0.163 | 0.195 | 0.188 | 20 | 81 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT08MINTB-4 | game_total | 0.826 | 0.860 | 0.854 | 87 | 15 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL3 | team_total | 0.701 | 0.740 | 0.733 | 75 | 27 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL4 | team_total | 0.488 | 0.535 | 0.526 | 55 | 48 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT08CHINYI-NYI4 | team_total | 0.418 | 0.465 | 0.456 | 48 | 55 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT08SJSTL-SJ3 | game_spread | 0.108 | 0.145 | 0.137 | 16 | 87 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT08CHINYI-NYI5 | team_total | 0.222 | 0.270 | 0.260 | 29 | 75 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT08CHINYI-NYI3 | team_total | 0.640 | 0.680 | 0.672 | 69 | 33 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT08SJSTL-10 | game_total | 0.099 | 0.070 | 0.075 | 8 | 94 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL5 | team_total | 0.291 | 0.335 | 0.326 | 35 | 68 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR2 | game_spread | 0.156 | 0.200 | 0.190 | 22 | 82 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY2 | team_total | 0.757 | 0.720 | 0.728 | 73 | 29 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT08MINTB-6 | game_total | 0.509 | 0.550 | 0.542 | 56 | 46 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT08SJSTL-9 | game_total | 0.204 | 0.160 | 0.168 | 18 | 86 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT08SJSTL-5 | game_total | 0.795 | 0.765 | 0.771 | 77 | 24 | yes | +0.013 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 0.506 | 0.495 | 0.178 | 0.217 | 6.11 | 6.46 | 0.968/0.992 | KXNHLTOTAL-26OCT08UTABOS-7 +0.060 |
| DAL @ BUF | 0.561 | 0.528 | 0.178 | 0.221 | 6.12 | 6.16 | 0.998/0.986 | KXNHLGAME-26OCT08DALBUF-BUF -0.032 |
| NSH @ MTL | 0.581 | 0.584 | 0.171 | 0.213 | 6.57 | 6.51 | 0.952/1.000 | KXNHLTOTAL-26OCT08NSHMTL-8 -0.018 |
| PHI @ OTT | 0.565 | 0.565 | 0.174 | 0.221 | 6.13 | 6.04 | 1.050/0.993 | KXNHLTOTAL-26OCT08PHIOTT-6 -0.020 |
| MIN @ TBL | 0.561 | 0.534 | 0.178 | 0.224 | 5.90 | 6.28 | 0.957/1.003 | KXNHLTEAMTOTAL-26OCT08MINTB-MIN4 +0.067 |
| VAN @ CAR | 0.667 | 0.611 | 0.160 | 0.207 | 6.62 | 6.53 | 0.989/1.020 | KXNHLGAME-26OCT08VANCAR-VAN +0.055 |
| CHI @ NYI | 0.607 | 0.616 | 0.173 | 0.212 | 5.82 | 6.22 | 0.951/1.003 | KXNHLTOTAL-26OCT08CHINYI-7 +0.071 |
| SJS @ STL | 0.615 | 0.569 | 0.171 | 0.215 | 6.40 | 6.42 | 0.993/1.034 | KXNHLSPREAD-26OCT08SJSTL-STL2 -0.049 |
| COL @ CGY | 0.379 | 0.398 | 0.168 | 0.211 | 6.36 | 6.37 | 0.997/0.976 | KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3 +0.020 |
| TOR @ VGK | 0.679 | 0.650 | 0.153 | 0.204 | 6.72 | 6.29 | 1.003/0.965 | KXNHLTOTAL-26OCT08TORVGK-6 -0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 6 recommended · full analysis in card.md / packet.json `thesis_card`

- Vancouver wins by over 2.5 goals YES @ 6c · p 0.1099 (adj 0.0824) · $1.12 · thesis VAN:WINS_BY_2PLUS
- Vancouver wins by over 1.5 goals YES @ 12c · p 0.1889 (adj 0.152) · $1.06 · thesis VAN:WINS_BY_2PLUS
- Carolina wins by over 1.5 goals NO @ 47c · p 0.6097 (adj 0.5156) · $1.02 · thesis GAME:TIGHT
- Carolina wins by over 2.5 goals NO @ 60c · p 0.733 (adj 0.6401) · $1.59 · thesis GAME:TIGHT
- Colorado wins by over 1.5 goals NO @ 54c · p 0.6244 (adj 0.5797) · $8.37 · thesis GAME:TIGHT
- Colorado wins by over 2.5 goals NO @ 67c · p 0.7449 (adj 0.7049) · $8.21 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ BOS** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.45, exp saves 24.61 (sd 6.74), pull risk 0.066
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.34, exp saves 22.58 (sd 6.37), pull risk 0.064

**DAL @ BUF** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROJECTED) exp shots 25.45, exp saves 22.1 (sd 6.16), pull risk 0.057
- DAL net: Jake Oettinger (PROJECTED) exp shots 27.04, exp saves 23.36 (sd 6.44), pull risk 0.06

**NSH @ MTL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (PROJECTED) exp shots 28.02, exp saves 24.37 (sd 6.55), pull risk 0.053
- NSH net: Juuse Saros (PROJECTED) exp shots 27.64, exp saves 23.62 (sd 6.62), pull risk 0.076

**PHI @ OTT** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 23.58, exp saves 20.54 (sd 5.8), pull risk 0.05
- PHI net: Dan Vladar (PROJECTED) exp shots 28.92, exp saves 24.88 (sd 6.83), pull risk 0.069

**MIN @ TBL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.09, exp saves 22.67 (sd 6.27), pull risk 0.056
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.6, exp saves 25.51 (sd 6.89), pull risk 0.064

**VAN @ CAR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Brandon Bussi (PROJECTED) exp shots 22.48, exp saves 19.73 (sd 5.68), pull risk 0.054
- VAN net: Kevin Lankinen (PROJECTED) exp shots 32.08, exp saves 27.1 (sd 7.51), pull risk 0.087

**CHI @ NYI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 24.34, exp saves 21.38 (sd 5.95), pull risk 0.051
- CHI net: Spencer Knight (PROJECTED) exp shots 30.03, exp saves 25.56 (sd 7.09), pull risk 0.075

**SJS @ STL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 25.77, exp saves 22.31 (sd 6.17), pull risk 0.056
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.07, exp saves 23.07 (sd 6.56), pull risk 0.076

**COL @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 32.7, exp saves 27.64 (sd 7.61), pull risk 0.083
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.32, exp saves 23.11 (sd 6.23), pull risk 0.047

**TOR @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 24.89, exp saves 21.92 (sd 6.06), pull risk 0.045
- TOR net: Anthony Stolarz (PROJECTED) exp shots 31.39, exp saves 26.54 (sd 7.3), pull risk 0.084

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
