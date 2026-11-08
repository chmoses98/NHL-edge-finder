# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-08T00:02:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 6 · markets on board: 3935 · contracts joined: 1376 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 1226, 'OK': 91, 'NO_EDGE': 59}
families: {'period_winner': 54, 'period_spread': 36, 'period_total': 54, 'player_assists': 199, 'game_early_goal': 6, 'first_goal': 215, 'game_winner': 12, 'player_goals': 375, 'game_overtime': 6, 'player_points': 271, 'goalie_saves': 10, 'game_spread': 24, 'team_total': 60, 'game_total': 54}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ CAR | 2026-11-08T01:00:00Z | T-30m | 0.733 | 0.267 | 0.158 | 6.02 | 3.77 | 2.25 | 234 (25/209) | PROBABLE/PROBABLE |
| SJS @ DAL | 2026-11-08T01:00:00Z | T-30m | 0.684 | 0.316 | 0.166 | 5.90 | 3.51 | 2.38 | 233 (25/208) | CONFIRMED/CONFIRMED |
| TBL @ MIN | 2026-11-08T01:00:00Z | T-30m | 0.444 | 0.556 | 0.172 | 6.33 | 2.97 | 3.36 | 225 (25/200) | CONFIRMED/CONFIRMED |
| DET @ COL | 2026-11-08T02:00:00Z | T-90m | 0.630 | 0.370 | 0.174 | 6.23 | 3.53 | 2.69 | 238 (25/213) | CONFIRMED/PROJECTED |
| PIT @ LAK | 2026-11-08T02:00:00Z | T-90m | 0.571 | 0.429 | 0.171 | 6.64 | 3.55 | 3.09 | 221 (25/196) | PROBABLE/CONFIRMED |
| VAN @ EDM | 2026-11-08T03:00:00Z | T-90m | 0.734 | 0.266 | 0.139 | 7.19 | 4.43 | 2.76 | 225 (25/200) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV07CHICAR-CAR3 | game_spread | 0.357 | 0.470 | 0.447 | 48 | 54 | no | +0.086 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR5 | team_total | 0.328 | 0.425 | 0.405 | 43 | 58 | no | +0.075 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CAR2 | game_spread | 0.512 | 0.605 | 0.587 | 61 | 40 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4 | team_total | 0.482 | 0.575 | 0.557 | 58 | 43 | no | +0.071 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL3 | game_spread | 0.295 | 0.385 | 0.366 | 39 | 62 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR4 | team_total | 0.535 | 0.635 | 0.616 | 65 | 38 | no | +0.068 | OK |
| KXNHLGAME-26NOV07CHICAR-CHI | game_winner | 0.267 | 0.195 | 0.208 | 20 | 81 | yes | +0.056 | OK |
| KXNHLGAME-26NOV07CHICAR-CAR | game_winner | 0.733 | 0.805 | 0.792 | 81 | 20 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL5 | team_total | 0.278 | 0.355 | 0.339 | 36 | 65 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL3 | team_total | 0.694 | 0.765 | 0.752 | 78 | 25 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR6 | team_total | 0.169 | 0.230 | 0.217 | 24 | 78 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA3 | team_total | 0.695 | 0.635 | 0.647 | 64 | 37 | yes | +0.039 | OK |
| KXNHLTOTAL-26NOV07SJDAL-6 | game_total | 0.515 | 0.575 | 0.563 | 58 | 43 | no | +0.037 | OK |
| KXNHLTOTAL-26NOV07CHICAR-6 | game_total | 0.538 | 0.595 | 0.584 | 60 | 41 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA5 | team_total | 0.288 | 0.230 | 0.241 | 24 | 78 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR3 | team_total | 0.743 | 0.805 | 0.794 | 82 | 21 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV07SJDAL-4 | game_total | 0.828 | 0.875 | 0.867 | 88 | 13 | no | +0.034 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL2 | game_spread | 0.449 | 0.505 | 0.494 | 51 | 50 | no | +0.033 | OK |
| KXNHLGAME-26NOV07PITLA-PIT | game_winner | 0.429 | 0.485 | 0.474 | 49 | 52 | no | +0.033 | OK |
| KXNHLGAME-26NOV07PITLA-LA | game_winner | 0.571 | 0.515 | 0.526 | 52 | 49 | yes | +0.033 | OK |
| KXNHLTOTAL-26NOV07SJDAL-5 | game_total | 0.736 | 0.790 | 0.780 | 80 | 22 | no | +0.032 | OK |
| KXNHLGAME-26NOV07SJDAL-DAL | game_winner | 0.684 | 0.735 | 0.725 | 74 | 27 | no | +0.032 | OK |
| KXNHLGAME-26NOV07SJDAL-SJ | game_winner | 0.316 | 0.265 | 0.275 | 27 | 74 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.519 | 0.465 | 0.476 | 47 | 54 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL3 | game_spread | 0.263 | 0.315 | 0.304 | 32 | 69 | no | +0.032 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT2 | game_spread | 0.236 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA6 | team_total | 0.146 | 0.105 | 0.112 | 11 | 90 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 | team_total | 0.484 | 0.535 | 0.525 | 54 | 47 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA4 | team_total | 0.486 | 0.430 | 0.441 | 44 | 58 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV07CHICAR-7 | game_total | 0.414 | 0.470 | 0.459 | 48 | 54 | no | +0.029 | OK |
| KXNHLTOTAL-26NOV07CHICAR-5 | game_total | 0.751 | 0.800 | 0.791 | 81 | 21 | no | +0.028 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM3 | game_spread | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLGAME-26NOV07VANEDM-VAN | game_winner | 0.266 | 0.225 | 0.233 | 23 | 78 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV07PITLA-9 | game_total | 0.235 | 0.195 | 0.202 | 20 | 81 | yes | +0.023 | OK |
| KXNHLSPREAD-26NOV07PITLA-LA2 | game_spread | 0.358 | 0.310 | 0.319 | 32 | 70 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV07TBMIN-6 | game_total | 0.581 | 0.625 | 0.616 | 63 | 38 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV07CHICAR-8 | game_total | 0.233 | 0.275 | 0.266 | 28 | 73 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN4 | team_total | 0.306 | 0.260 | 0.269 | 27 | 75 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV07TBMIN-7 | game_total | 0.470 | 0.520 | 0.510 | 53 | 49 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV07SJDAL-8 | game_total | 0.214 | 0.255 | 0.246 | 26 | 75 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL2 | team_total | 0.862 | 0.900 | 0.893 | 91 | 11 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV07CHICAR-4 | game_total | 0.841 | 0.880 | 0.873 | 89 | 13 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV07PITLA-8 | game_total | 0.325 | 0.280 | 0.289 | 29 | 73 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV07DETCOL-5 | game_total | 0.770 | 0.810 | 0.802 | 82 | 20 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.405 | 0.365 | 0.373 | 37 | 64 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR2 | team_total | 0.896 | 0.935 | 0.928 | 95 | 8 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV07SJDAL-7 | game_total | 0.395 | 0.435 | 0.427 | 44 | 57 | no | +0.018 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CHI2 | game_spread | 0.113 | 0.085 | 0.090 | 9 | 92 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV07SJDAL-9 | game_total | 0.144 | 0.180 | 0.172 | 19 | 83 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV07TBMIN-5 | game_total | 0.783 | 0.820 | 0.813 | 83 | 19 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV07SJDAL-3 | game_total | 0.953 | 0.975 | 0.972 | 98 | 3 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN5 | team_total | 0.153 | 0.120 | 0.126 | 13 | 89 | yes | +0.015 | OK |
| KXNHLGAME-26NOV07DETCOL-DET | game_winner | 0.370 | 0.335 | 0.342 | 34 | 67 | yes | +0.015 | OK |
| KXNHLGAME-26NOV07DETCOL-COL | game_winner | 0.630 | 0.665 | 0.658 | 67 | 34 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL3 | team_total | 0.692 | 0.735 | 0.727 | 75 | 28 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL2 | team_total | 0.869 | 0.900 | 0.894 | 91 | 11 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM2 | game_spread | 0.539 | 0.575 | 0.568 | 58 | 43 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV07PITLA-10 | game_total | 0.120 | 0.095 | 0.100 | 10 | 91 | yes | +0.014 | OK |
| KXNHLGAME-26NOV07VANEDM-EDM | game_winner | 0.734 | 0.765 | 0.759 | 77 | 24 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV07VANEDM-10 | game_total | 0.172 | 0.145 | 0.150 | 15 | 86 | yes | +0.013 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT3 | game_spread | 0.138 | 0.165 | 0.159 | 17 | 84 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV07PITLA-6 | game_total | 0.629 | 0.595 | 0.602 | 60 | 41 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN6 | team_total | 0.065 | 0.040 | 0.044 | 5 | 97 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CHI2 | team_total | 0.648 | 0.615 | 0.622 | 62 | 39 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV07CHICAR-9 | game_total | 0.159 | 0.185 | 0.180 | 19 | 82 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV07PITLA-7 | game_total | 0.518 | 0.485 | 0.492 | 49 | 52 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL5 | team_total | 0.285 | 0.325 | 0.317 | 34 | 69 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL2 | game_spread | 0.403 | 0.435 | 0.429 | 44 | 57 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA2 | team_total | 0.869 | 0.835 | 0.842 | 85 | 18 | yes | +0.010 | OK |
| KXNHLSPREAD-26NOV07PITLA-LA3 | game_spread | 0.231 | 0.205 | 0.210 | 21 | 80 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV07DETCOL-7 | game_total | 0.454 | 0.485 | 0.479 | 49 | 52 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV07DETCOL-4 | game_total | 0.854 | 0.880 | 0.875 | 89 | 13 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV07TBMIN-MIN4 | team_total | 0.356 | 0.385 | 0.379 | 39 | 62 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL6 | team_total | 0.133 | 0.165 | 0.158 | 18 | 85 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV07VANEDM-9 | game_total | 0.302 | 0.275 | 0.280 | 28 | 73 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV07DETCOL-6 | game_total | 0.566 | 0.600 | 0.593 | 61 | 41 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV07TBMIN-4 | game_total | 0.867 | 0.885 | 0.882 | 89 | 12 | no | +0.006 | OK |
| KXNHLTOTAL-26NOV07PITLA-4 | game_total | 0.892 | 0.875 | 0.879 | 88 | 13 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV07VANEDM-7 | game_total | 0.601 | 0.575 | 0.580 | 58 | 43 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV07VANEDM-2 | game_total | 0.994 | 0.985 | 0.988 | 99 | 2 | yes | +0.004 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ CAR | 0.733 | 0.685 | 0.158 | 0.193 | 6.02 | 6.53 | 1.000/0.995 | KXNHLTEAMTOTAL-26NOV07CHICAR-CHI3 +0.104 |
| SJS @ DAL | 0.684 | 0.623 | 0.166 | 0.212 | 5.90 | 6.19 | 0.994/1.021 | KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3 +0.082 |
| TBL @ MIN | 0.444 | 0.486 | 0.172 | 0.214 | 6.33 | 6.43 | 1.033/0.985 | KXNHLTEAMTOTAL-26NOV07TBMIN-MIN4 +0.048 |
| DET @ COL | 0.630 | 0.661 | 0.174 | 0.202 | 6.23 | 6.48 | 0.979/1.015 | KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 +0.054 |
| PIT @ LAK | 0.571 | 0.546 | 0.171 | 0.218 | 6.64 | 6.35 | 0.994/1.012 | KXNHLTOTAL-26NOV07PITLA-8 -0.051 |
| VAN @ EDM | 0.734 | 0.670 | 0.139 | 0.190 | 7.19 | 6.99 | 0.994/1.030 | KXNHLSPREAD-26NOV07VANEDM-EDM2 -0.076 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 24 recommended · full analysis in card.md / packet.json `thesis_card`

- Dillon Boucher: 1+ goals YES @ 5c · p 0.0895 (adj 0.0771) · $3.54 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 62c · p 0.7034 (adj 0.6801) · $13.67 · thesis CAR:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 19c · p 0.243 (adj 0.2273) · $5.38 · thesis CHI:OFFENSE_4PLUS
- Oliver Moore: 1+ goals YES @ 12c · p 0.1534 (adj 0.1426) · $2.85 · thesis CHI:OFFENSE_4PLUS
- Dallas wins by over 1.5 goals NO @ 50c · p 0.5943 (adj 0.5447) · $8.12 · thesis GAME:TIGHT
- San Jose over 3.5 goals scored YES @ 22c · p 0.2922 (adj 0.2536) · $4.09 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 72c · p 0.7965 (adj 0.7557) · $11.7 · thesis SJS:SUPPRESSED
- Macklin Celebrini: 1+ assists NO @ 53c · p 0.6113 (adj 0.5656) · $8.81 · thesis SJS:SUPPRESSED
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1359 (adj 0.1232) · $4.62 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 15c · p 0.1898 (adj 0.1786) · $3.65 · thesis MIN:OFFENSE_4PLUS
- Charle-Edouard D'Astous: 1+ goals NO @ 90c · p 0.9279 (adj 0.9197) · $13.67 · thesis TBL:SUPPRESSED
- Kirill Kaprizov: 1+ goals NO @ 57c · p 0.6235 (adj 0.6089) · $8.67 · thesis MIN:SUPPRESSED
- Carter Mazur: 1+ goals YES @ 6c · p 0.0851 (adj 0.0751) · $1.85 · thesis DET:OFFENSE_4PLUS
- Lucas Raymond: 1+ assists NO @ 60c · p 0.6819 (adj 0.636) · $9.46 · thesis DET:SUPPRESSED
- Sheldon Dries: 1+ goals YES @ 8c · p 0.1065 (adj 0.0961) · $1.89 · thesis DET:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ assists YES @ 28c · p 0.3437 (adj 0.3094) · $3.61 · thesis COL:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0751 (adj 0.0676) · $2.35 · thesis LAK:OFFENSE_4PLUS
- Ben Kindel: 1+ assists NO @ 70c · p 0.7767 (adj 0.7359) · $13.67 · thesis PIT:SUPPRESSED
- Blake Lizotte: 1+ goals YES @ 10c · p 0.1258 (adj 0.1181) · $2.24 · thesis PIT:WINS_BY_2PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1566 (adj 0.1487) · $2.25 · thesis PIT:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3483 (adj 0.3262) · $9.82 · thesis EDM:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2205 (adj 0.2041) · $6.53 · thesis VAN:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 10c · p 0.1436 (adj 0.1302) · $4.11 · thesis VAN:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 11c · p 0.1464 (adj 0.1361) · $3.45 · thesis EDM:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ CAR** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 21.81, exp saves 19.44 (sd 5.57), pull risk 0.045
- CHI net: Spencer Knight (PROBABLE) exp shots 33.1, exp saves 27.69 (sd 7.63), pull risk 0.097

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.204 | 0.330 | 35/69 | +0.091 | STANDARD |
| Sebastian Aho: 1+ assists | 0.380 | 0.500 | 51/51 | +0.093 | STANDARD |
| Nikolaj Ehlers: 1+ points | 0.540 | 0.640 | 65/37 | +0.074 | STANDARD |
| Nikolaj Ehlers: 1+ assists | 0.392 | 0.490 | 50/52 | +0.070 | STANDARD |
| Sebastian Aho: 1+ points | 0.561 | 0.655 | 68/37 | +0.052 | STANDARD |
| Sebastian Aho: 1+ goals | 0.297 | 0.390 | 40/62 | +0.067 | STANDARD |

**SJS @ DAL** · priced 179/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.49, exp saves 21.62 (sd 5.94), pull risk 0.046
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.67, exp saves 23.51 (sd 6.64), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.280 | 0.395 | 40/61 | +0.093 | STANDARD |
| Collin Graf: 1+ points | 0.360 | 0.255 | 29/78 | +0.056 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.484 | 0.580 | 59/43 | +0.069 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.389 | 0.480 | 49/53 | +0.064 | STANDARD |
| Ivar Stenberg: 1+ points | 0.318 | 0.405 | 42/61 | +0.055 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.203 | 0.285 | 29/72 | +0.062 | STANDARD |

**TBL @ MIN** · priced 169/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.08, exp saves 24.13 (sd 6.68), pull risk 0.068
- TBL net: Dennis Hildeby (CONFIRMED) exp shots 27.46, exp saves 23.81 (sd 6.5), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.491 | 0.635 | 64/37 | +0.122 | STANDARD |
| Nikita Kucherov: 2+ points | 0.295 | 0.400 | 41/61 | +0.078 | STANDARD |
| Calvin Pickard: 25+ saves | 0.479 | 0.380 | 46/70 | +0.002 |  |
| Nikita Kucherov: 2+ assists | 0.145 | 0.235 | 26/79 | +0.054 | STANDARD |
| Quinn Hughes: 1+ assists | 0.545 | 0.635 | 64/37 | +0.068 | STANDARD |
| Quinn Hughes: 2+ points | 0.253 | 0.340 | 36/68 | +0.051 | STANDARD |

**DET @ COL** · priced 178/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.53, exp saves 23.51 (sd 6.29), pull risk 0.046
- DET net: Daniil Tarasov (PROJECTED) exp shots 30.11, exp saves 25.32 (sd 7.17), pull risk 0.095

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lucas Raymond: 1+ assists | 0.318 | 0.410 | 42/60 | +0.065 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.370 | 0.455 | 46/55 | +0.063 | STANDARD |
| Lucas Raymond: 1+ points | 0.486 | 0.570 | 59/45 | +0.047 | STANDARD |
| Sam Malinski: 1+ assists | 0.318 | 0.240 | 25/77 | +0.055 | STANDARD |
| Sam Malinski: 1+ points | 0.376 | 0.300 | 32/72 | +0.041 | STANDARD |
| Artturi Lehkonen: 1+ assists | 0.344 | 0.275 | 28/73 | +0.050 | STANDARD |

**PIT @ LAK** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROBABLE) exp shots 27.28, exp saves 23.67 (sd 6.45), pull risk 0.059
- PIT net: Sergei Murashov (CONFIRMED) exp shots 27.6, exp saves 23.6 (sd 6.62), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 2+ points | 0.238 | 0.355 | 37/66 | +0.086 | STANDARD |
| Artemi Panarin: 1+ assists | 0.418 | 0.525 | 53/48 | +0.085 | STANDARD |
| Ben Kindel: 1+ points | 0.364 | 0.460 | 47/55 | +0.068 | STANDARD |
| Erik Karlsson: 1+ points | 0.487 | 0.570 | 58/44 | +0.056 | STANDARD |
| Ben Kindel: 1+ assists | 0.223 | 0.305 | 31/70 | +0.062 | STANDARD |
| Erik Karlsson: 1+ assists | 0.408 | 0.485 | 49/52 | +0.055 | STANDARD |

**VAN @ EDM** · priced 165/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 24.17, exp saves 21.32 (sd 5.93), pull risk 0.052
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.14, exp saves 25.04 (sd 7.29), pull risk 0.111

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.264 | 0.430 | 45/59 | +0.129 | STANDARD |
| Connor McDavid: 2+ points | 0.513 | 0.635 | 66/39 | +0.080 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.416 | 0.295 | 31/72 | +0.091 | STANDARD |
| Leon Draisaitl: 2+ points | 0.433 | 0.545 | 56/47 | +0.080 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.343 | 0.455 | 47/56 | +0.080 | STANDARD |
| Connor McDavid: 1+ assists | 0.629 | 0.740 | 77/29 | +0.067 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
