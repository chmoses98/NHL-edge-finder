# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-07T21:26:40Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 10 · markets on board: 3969 · contracts joined: 2289 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2039, 'OK': 145, 'NO_EDGE': 105}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 333, 'game_early_goal': 10, 'first_goal': 360, 'game_winner': 20, 'player_goals': 618, 'game_overtime': 10, 'player_points': 451, 'goalie_saves': 17, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ SEA | 2026-11-07T22:00:00Z | T-30m | 0.530 | 0.469 | 0.171 | 6.51 | 3.36 | 3.15 | 229 (25/204) | PROJECTED/CONFIRMED |
| MTL @ TOR | 2026-11-08T00:00:00Z | T-90m | 0.458 | 0.542 | 0.172 | 6.73 | 3.23 | 3.50 | 221 (25/196) | CONFIRMED/CONFIRMED |
| UTA @ OTT | 2026-11-08T00:00:00Z | T-90m | 0.450 | 0.550 | 0.169 | 6.71 | 3.19 | 3.52 | 234 (25/209) | CONFIRMED/PROJECTED |
| NJD @ NYI | 2026-11-08T00:00:00Z | T-90m | 0.495 | 0.504 | 0.178 | 5.80 | 2.88 | 2.92 | 226 (25/201) | PROBABLE/CONFIRMED |
| CHI @ CAR | 2026-11-08T01:00:00Z | T-3h | 0.733 | 0.267 | 0.158 | 6.02 | 3.77 | 2.25 | 234 (25/209) | PROBABLE/PROBABLE |
| SJS @ DAL | 2026-11-08T01:00:00Z | T-3h | 0.683 | 0.317 | 0.168 | 5.91 | 3.53 | 2.38 | 233 (25/208) | CONFIRMED/PROJECTED |
| TBL @ MIN | 2026-11-08T01:00:00Z | T-3h | 0.444 | 0.556 | 0.172 | 6.33 | 2.97 | 3.36 | 228 (25/203) | CONFIRMED/CONFIRMED |
| DET @ COL | 2026-11-08T02:00:00Z | T-3h | 0.630 | 0.370 | 0.174 | 6.23 | 3.53 | 2.69 | 238 (25/213) | CONFIRMED/PROJECTED |
| PIT @ LAK | 2026-11-08T02:00:00Z | T-3h | 0.571 | 0.429 | 0.171 | 6.64 | 3.55 | 3.09 | 221 (25/196) | PROBABLE/CONFIRMED |
| VAN @ EDM | 2026-11-08T03:00:00Z | T-3h | 0.734 | 0.266 | 0.139 | 7.19 | 4.43 | 2.76 | 225 (25/200) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV07CHICAR-CAR3 | game_spread | 0.357 | 0.470 | 0.447 | 48 | 54 | no | +0.086 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR5 | team_total | 0.328 | 0.425 | 0.405 | 43 | 58 | no | +0.075 | OK |
| KXNHLGAME-26NOV07NYRSEA-NYR | game_winner | 0.469 | 0.565 | 0.546 | 57 | 44 | no | +0.073 | OK |
| KXNHLGAME-26NOV07NYRSEA-SEA | game_winner | 0.530 | 0.435 | 0.454 | 44 | 57 | yes | +0.073 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CAR2 | game_spread | 0.512 | 0.605 | 0.587 | 61 | 40 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR4 | team_total | 0.535 | 0.630 | 0.612 | 64 | 38 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ4 | team_total | 0.347 | 0.440 | 0.421 | 45 | 57 | no | +0.066 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR2 | game_spread | 0.260 | 0.345 | 0.327 | 35 | 66 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4 | team_total | 0.482 | 0.565 | 0.549 | 57 | 44 | no | +0.060 | OK |
| KXNHLGAME-26NOV07NJNYI-NJ | game_winner | 0.504 | 0.585 | 0.569 | 59 | 42 | no | +0.058 | OK |
| KXNHLGAME-26NOV07NJNYI-NYI | game_winner | 0.495 | 0.415 | 0.431 | 42 | 59 | yes | +0.058 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ3 | game_spread | 0.162 | 0.240 | 0.223 | 25 | 77 | no | +0.056 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-SEA2 | game_spread | 0.318 | 0.245 | 0.259 | 25 | 76 | yes | +0.055 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL3 | game_spread | 0.299 | 0.380 | 0.363 | 39 | 63 | no | +0.055 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ2 | game_spread | 0.280 | 0.355 | 0.339 | 36 | 65 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL5 | team_total | 0.282 | 0.355 | 0.340 | 36 | 65 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ2 | team_total | 0.779 | 0.850 | 0.838 | 86 | 16 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-SEA3 | team_total | 0.657 | 0.585 | 0.600 | 59 | 42 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-SEA4 | team_total | 0.445 | 0.375 | 0.389 | 38 | 63 | yes | +0.049 | OK |
| KXNHLGAME-26NOV07CHICAR-CAR | game_winner | 0.733 | 0.800 | 0.788 | 81 | 21 | no | +0.046 | OK |
| KXNHLGAME-26NOV07CHICAR-CHI | game_winner | 0.267 | 0.205 | 0.217 | 21 | 80 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ3 | team_total | 0.568 | 0.640 | 0.626 | 65 | 37 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR3 | team_total | 0.743 | 0.815 | 0.802 | 83 | 20 | no | +0.045 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR3 | game_spread | 0.155 | 0.215 | 0.202 | 22 | 79 | no | +0.044 | OK |
| KXNHLTOTAL-26NOV07SJDAL-6 | game_total | 0.510 | 0.575 | 0.562 | 58 | 43 | no | +0.043 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NYI2 | game_spread | 0.275 | 0.215 | 0.226 | 22 | 79 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ5 | team_total | 0.176 | 0.240 | 0.226 | 25 | 77 | no | +0.042 | OK |
| KXNHLTOTAL-26NOV07NJNYI-5 | game_total | 0.717 | 0.775 | 0.764 | 78 | 23 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR6 | team_total | 0.169 | 0.230 | 0.217 | 24 | 78 | no | +0.039 | OK |
| KXNHLTOTAL-26NOV07CHICAR-6 | game_total | 0.538 | 0.600 | 0.588 | 61 | 41 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL2 | game_spread | 0.449 | 0.505 | 0.494 | 51 | 50 | no | +0.033 | OK |
| KXNHLGAME-26NOV07PITLA-LA | game_winner | 0.571 | 0.515 | 0.526 | 52 | 49 | yes | +0.033 | OK |
| KXNHLGAME-26NOV07SJDAL-DAL | game_winner | 0.683 | 0.735 | 0.725 | 74 | 27 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-SEA5 | team_total | 0.254 | 0.185 | 0.198 | 21 | 84 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.519 | 0.465 | 0.476 | 47 | 54 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL3 | game_spread | 0.263 | 0.315 | 0.304 | 32 | 69 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV07PITLA-8 | game_total | 0.325 | 0.275 | 0.285 | 28 | 73 | yes | +0.031 | OK |
| KXNHLTOTAL-26NOV07SJDAL-4 | game_total | 0.832 | 0.875 | 0.867 | 88 | 13 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV07SJDAL-5 | game_total | 0.738 | 0.790 | 0.780 | 80 | 22 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT2 | game_spread | 0.236 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV07NJNYI-7 | game_total | 0.383 | 0.435 | 0.424 | 44 | 57 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA6 | team_total | 0.146 | 0.105 | 0.112 | 11 | 90 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR2 | team_total | 0.896 | 0.940 | 0.933 | 95 | 7 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA3 | team_total | 0.695 | 0.640 | 0.651 | 65 | 37 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA4 | team_total | 0.486 | 0.430 | 0.441 | 44 | 58 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV07CHICAR-7 | game_total | 0.414 | 0.465 | 0.455 | 47 | 54 | no | +0.029 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-SEA3 | game_spread | 0.197 | 0.155 | 0.163 | 16 | 85 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-SEA6 | team_total | 0.123 | 0.075 | 0.083 | 9 | 94 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL3 | team_total | 0.701 | 0.750 | 0.741 | 76 | 26 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-NYR4 | team_total | 0.397 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL2 | team_total | 0.869 | 0.910 | 0.903 | 92 | 10 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA5 | team_total | 0.288 | 0.235 | 0.245 | 25 | 78 | yes | +0.025 | OK |
| KXNHLTOTAL-26NOV07PITLA-9 | game_total | 0.235 | 0.195 | 0.202 | 20 | 81 | yes | +0.023 | OK |
| KXNHLGAME-26NOV07PITLA-PIT | game_winner | 0.429 | 0.475 | 0.466 | 48 | 53 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV07PITLA-LA2 | game_spread | 0.358 | 0.310 | 0.319 | 32 | 70 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV07CHICAR-8 | game_total | 0.233 | 0.280 | 0.270 | 29 | 73 | no | +0.023 | OK |
| KXNHLGAME-26NOV07SJDAL-SJ | game_winner | 0.317 | 0.275 | 0.283 | 28 | 73 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN4 | team_total | 0.306 | 0.260 | 0.269 | 27 | 75 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-SEA2 | team_total | 0.843 | 0.800 | 0.809 | 81 | 21 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL2 | team_total | 0.862 | 0.900 | 0.893 | 91 | 11 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV07CHICAR-4 | game_total | 0.841 | 0.880 | 0.873 | 89 | 13 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 | team_total | 0.484 | 0.535 | 0.525 | 55 | 48 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV07DETCOL-5 | game_total | 0.770 | 0.805 | 0.798 | 81 | 20 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.405 | 0.365 | 0.373 | 37 | 64 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV07UTAOTT-8 | game_total | 0.333 | 0.295 | 0.302 | 30 | 71 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV07CHICAR-5 | game_total | 0.751 | 0.795 | 0.787 | 81 | 22 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV07SJDAL-8 | game_total | 0.220 | 0.255 | 0.248 | 26 | 75 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CHI2 | game_spread | 0.113 | 0.085 | 0.090 | 9 | 92 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV07SJDAL-7 | game_total | 0.396 | 0.435 | 0.427 | 44 | 57 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV07NJNYI-6 | game_total | 0.496 | 0.535 | 0.527 | 54 | 47 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV07UTAOTT-10 | game_total | 0.122 | 0.095 | 0.100 | 10 | 91 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV07TBMIN-5 | game_total | 0.783 | 0.820 | 0.813 | 83 | 19 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM3 | game_spread | 0.398 | 0.435 | 0.427 | 44 | 57 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN5 | team_total | 0.153 | 0.120 | 0.126 | 13 | 89 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-NYR2 | team_total | 0.816 | 0.850 | 0.844 | 86 | 16 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV07NJNYI-4 | game_total | 0.816 | 0.850 | 0.844 | 86 | 16 | no | +0.015 | OK |
| KXNHLGAME-26NOV07DETCOL-DET | game_winner | 0.370 | 0.335 | 0.342 | 34 | 67 | yes | +0.015 | OK |
| KXNHLGAME-26NOV07DETCOL-COL | game_winner | 0.630 | 0.665 | 0.658 | 67 | 34 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL3 | team_total | 0.692 | 0.735 | 0.727 | 75 | 28 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM2 | game_spread | 0.539 | 0.575 | 0.568 | 58 | 43 | no | +0.014 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ SEA | 0.530 | 0.552 | 0.171 | 0.220 | 6.51 | 6.42 | 1.005/1.015 | KXNHLTOTAL-26NOV07NYRSEA-8 -0.023 |
| MTL @ TOR | 0.458 | 0.532 | 0.172 | 0.210 | 6.73 | 6.78 | 0.988/0.983 | KXNHLGAME-26NOV07MTLTOR-TOR +0.074 |
| UTA @ OTT | 0.450 | 0.521 | 0.169 | 0.213 | 6.71 | 6.58 | 1.071/0.993 | KXNHLGAME-26NOV07UTAOTT-UTA -0.070 |
| NJD @ NYI | 0.495 | 0.516 | 0.178 | 0.216 | 5.80 | 6.19 | 0.952/0.983 | KXNHLTOTAL-26NOV07NJNYI-7 +0.069 |
| CHI @ CAR | 0.733 | 0.685 | 0.158 | 0.193 | 6.02 | 6.53 | 1.000/0.995 | KXNHLTEAMTOTAL-26NOV07CHICAR-CHI3 +0.104 |
| SJS @ DAL | 0.683 | 0.628 | 0.168 | 0.214 | 5.91 | 6.21 | 0.994/1.027 | KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3 +0.081 |
| TBL @ MIN | 0.444 | 0.486 | 0.172 | 0.214 | 6.33 | 6.43 | 1.033/0.985 | KXNHLTEAMTOTAL-26NOV07TBMIN-MIN4 +0.048 |
| DET @ COL | 0.630 | 0.661 | 0.174 | 0.202 | 6.23 | 6.48 | 0.979/1.015 | KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 +0.054 |
| PIT @ LAK | 0.571 | 0.546 | 0.171 | 0.218 | 6.64 | 6.35 | 0.994/1.012 | KXNHLTOTAL-26NOV07PITLA-8 -0.051 |
| VAN @ EDM | 0.734 | 0.670 | 0.139 | 0.190 | 7.19 | 6.99 | 0.994/1.030 | KXNHLSPREAD-26NOV07VANEDM-EDM2 -0.076 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 38 recommended · full analysis in card.md / packet.json `thesis_card`

- Ben Meyers: 1+ goals YES @ 10c · p 0.1539 (adj 0.1379) · $3.64 · thesis SEA:OFFENSE_4PLUS
- Jani Nyman: 1+ goals YES @ 11c · p 0.1568 (adj 0.1426) · $3.09 · thesis SEA:OFFENSE_4PLUS
- Kaapo Kakko: 1+ goals YES @ 15c · p 0.2019 (adj 0.1877) · $3.76 · thesis SEA:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 65c · p 0.7134 (adj 0.6963) · $9.48 · thesis NYR:SUPPRESSED
- Brandon Duhaime: 1+ goals YES @ 7c · p 0.1064 (adj 0.0948) · $2.28 · thesis TOR:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1691 (adj 0.1518) · $2.95 · thesis TOR:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 47c · p 0.6201 (adj 0.5193) · $5.68 · thesis MTL:SUPPRESSED
- Nick Suzuki: 2+ assists NO @ 84c · p 0.9171 (adj 0.871) · $8.55 · thesis MTL:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 17c · p 0.2123 (adj 0.1992) · $2.64 · thesis UTA:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 16c · p 0.2013 (adj 0.1872) · $2.39 · thesis OTT:OFFENSE_4PLUS
- Dylan Cozens: 1+ goals YES @ 25c · p 0.2979 (adj 0.2834) · $3.17 · thesis OTT:OFFENSE_4PLUS
- Fabian Zetterlund: 1+ goals YES @ 20c · p 0.2399 (adj 0.2274) · $2.32 · thesis OTT:OFFENSE_4PLUS
- New York I wins by over 1.5 goals YES @ 22c · p 0.2981 (adj 0.2566) · $2.42 · thesis NYI:WINS_BY_2PLUS
- New Jersey wins by over 1.5 goals NO @ 65c · p 0.739 (adj 0.692) · $8.22 · thesis NYI:WINS
- Cody Glass: 1+ goals YES @ 11c · p 0.1403 (adj 0.1302) · $2.12 · thesis NJD:OFFENSE_4PLUS
- Dillon Boucher: 1+ goals YES @ 5c · p 0.0895 (adj 0.0771) · $2.45 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 62c · p 0.7034 (adj 0.6813) · $9.48 · thesis CAR:SUPPRESSED
- Oliver Moore: 1+ goals YES @ 11c · p 0.1534 (adj 0.1413) · $3.05 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 19c · p 0.243 (adj 0.2273) · $3.74 · thesis CHI:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 63c · p 0.6875 (adj 0.6719) · $8.75 · thesis DAL:SUPPRESSED
- Jacob Trouba: 1+ goals YES @ 5c · p 0.0736 (adj 0.0652) · $1.22 · thesis SJS:OFFENSE_4PLUS
- San Jose over 3.5 goals scored YES @ 23c · p 0.2946 (adj 0.2573) · $2.25 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 74c · p 0.8138 (adj 0.7644) · $7.97 · thesis SJS:SUPPRESSED
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1383 (adj 0.125) · $3.43 · thesis MIN:OFFENSE_4PLUS
- Bobby Brink: 1+ goals YES @ 14c · p 0.1867 (adj 0.1738) · $3.32 · thesis MIN:OFFENSE_4PLUS
- Michael McCarron: 1+ goals YES @ 12c · p 0.1553 (adj 0.1452) · $2.45 · thesis MIN:OFFENSE_4PLUS
- Quinn Hughes: 1+ assists NO @ 37c · p 0.444 (adj 0.4045) · $4.32 · thesis MIN:SUPPRESSED
- Carter Mazur: 1+ goals YES @ 6c · p 0.0851 (adj 0.0763) · $1.39 · thesis DET:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ assists YES @ 28c · p 0.3437 (adj 0.3094) · $2.39 · thesis COL:OFFENSE_4PLUS
- Sam Malinski: 1+ assists YES @ 25c · p 0.318 (adj 0.2765) · $1.81 · thesis COL:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0751 (adj 0.0688) · $1.74 · thesis LAK:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1258 (adj 0.1119) · $1.92 · thesis PIT:WINS_BY_2PLUS
- Andre Lee: 1+ goals YES @ 10c · p 0.1253 (adj 0.1165) · $1.22 · thesis LAK:OFFENSE_4PLUS
- Erik Karlsson: 1+ goals NO @ 84c · p 0.8696 (adj 0.8609) · $9.2 · thesis PIT:SUPPRESSED
- Brendan Gallagher: 1+ goals YES @ 9c · p 0.1436 (adj 0.1277) · $3.58 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 15c · p 0.2205 (adj 0.1966) · $4.63 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 16c · p 0.2125 (adj 0.1981) · $3.71 · thesis VAN:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 11c · p 0.1464 (adj 0.1361) · $2.31 · thesis EDM:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYR @ SEA** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.17, exp saves 23.66 (sd 6.46), pull risk 0.059
- NYR net: Joonas Korpisalo (CONFIRMED) exp shots 27.28, exp saves 23.31 (sd 6.59), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joonas Korpisalo: 25+ saves | 0.426 | 0.595 | 79/60 | -0.043 |  |
| Freddy Gaudreau: 1+ points | 0.423 | 0.320 | 35/71 | +0.057 | STANDARD |
| Freddy Gaudreau: 1+ assists | 0.296 | 0.200 | 22/82 | +0.064 | STANDARD |
| Pavel Dorofeyev: 1+ goals | 0.287 | 0.355 | 36/65 | +0.047 | STANDARD |
| Brandon Montour: 1+ assists | 0.393 | 0.325 | 34/69 | +0.037 | STANDARD |
| Joey Daccord: 25+ saves | 0.439 | 0.505 | 52/51 | +0.033 |  |

**MTL @ TOR** · priced 167/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 29.0, exp saves 25.08 (sd 6.94), pull risk 0.07
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.71, exp saves 24.68 (sd 6.91), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.380 | 0.535 | 54/47 | +0.133 | STANDARD |
| Nick Suzuki: 1+ points | 0.576 | 0.670 | 69/35 | +0.058 | STANDARD |
| Nick Suzuki: 2+ assists | 0.083 | 0.175 | 19/84 | +0.068 | STANDARD |
| Nick Suzuki: 2+ points | 0.220 | 0.310 | 33/71 | +0.055 | STANDARD |
| Easton Cowan: 1+ points | 0.519 | 0.430 | 45/59 | +0.052 | STANDARD |
| Morgan Rielly: 1+ points | 0.414 | 0.330 | 34/68 | +0.059 | STANDARD |

**UTA @ OTT** · priced 174/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (CONFIRMED) exp shots 26.39, exp saves 22.89 (sd 6.44), pull risk 0.067
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.47, exp saves 23.56 (sd 6.6), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lawson Crouse: 1+ points | 0.404 | 0.170 | 33/99 | +0.059 | STANDARD |
| Jack McBain: 1+ points | 0.306 | 0.150 | 29/99 | +0.001 | STANDARD |
| Lawson Crouse: 1+ assists | 0.249 | 0.115 | 20/97 | +0.038 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.474 | 0.380 | 40/64 | +0.057 | STANDARD |
| Fabian Zetterlund: 1+ assists | 0.307 | 0.215 | 24/81 | +0.055 | STANDARD |
| Mikhail Sergachev: 1+ assists | 0.438 | 0.525 | 53/48 | +0.064 | STANDARD |

**NJD @ NYI** · priced 172/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 28.65, exp saves 24.91 (sd 6.74), pull risk 0.057
- NJD net: Jake Allen (CONFIRMED) exp shots 26.66, exp saves 23.05 (sd 6.42), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.381 | 0.510 | 52/50 | +0.102 | STANDARD |
| Jack Hughes: 2+ points | 0.214 | 0.320 | 33/69 | +0.081 | STANDARD |
| Emil Heineman: 1+ assists | 0.300 | 0.195 | 20/81 | +0.089 | STANDARD |
| Luke Evangelista: 1+ assists | 0.228 | 0.330 | 34/68 | +0.077 | STANDARD |
| Jack Hughes: 1+ points | 0.580 | 0.680 | 70/34 | +0.064 | STANDARD |
| Nico Hischier: 1+ assists | 0.285 | 0.375 | 39/64 | +0.059 | STANDARD |

**CHI @ CAR** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 21.81, exp saves 19.44 (sd 5.57), pull risk 0.045
- CHI net: Spencer Knight (PROBABLE) exp shots 33.1, exp saves 27.69 (sd 7.63), pull risk 0.097

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.204 | 0.335 | 35/68 | +0.100 | STANDARD |
| Sebastian Aho: 1+ assists | 0.380 | 0.505 | 51/50 | +0.103 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.465 | 0.355 | 36/65 | +0.089 | STANDARD |
| Sebastian Aho: 1+ points | 0.561 | 0.660 | 69/37 | +0.052 | STANDARD |
| Sebastian Aho: 1+ goals | 0.297 | 0.385 | 39/62 | +0.067 | STANDARD |
| Nikolaj Ehlers: 1+ assists | 0.392 | 0.480 | 49/53 | +0.060 | STANDARD |

**SJS @ DAL** · priced 179/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.49, exp saves 21.6 (sd 5.9), pull risk 0.045
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.67, exp saves 23.5 (sd 6.65), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.284 | 0.385 | 40/63 | +0.070 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.186 | 0.285 | 31/74 | +0.060 | STANDARD |
| Collin Graf: 1+ points | 0.361 | 0.265 | 32/79 | +0.025 | STANDARD |
| Ivar Stenberg: 1+ points | 0.312 | 0.405 | 42/61 | +0.061 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.489 | 0.575 | 60/45 | +0.044 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.393 | 0.475 | 49/54 | +0.050 | STANDARD |

**TBL @ MIN** · priced 165/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.08, exp saves 24.13 (sd 6.68), pull risk 0.068
- TBL net: Dennis Hildeby (CONFIRMED) exp shots 27.46, exp saves 23.81 (sd 6.5), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.491 | 0.635 | 64/37 | +0.122 | STANDARD |
| Matt Boldy: 1+ assists | 0.373 | 0.485 | 49/52 | +0.090 | STANDARD |
| Nikita Kucherov: 2+ points | 0.295 | 0.405 | 42/61 | +0.078 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.385 | 0.490 | 50/52 | +0.077 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.145 | 0.245 | 26/77 | +0.073 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.278 | 0.375 | 38/63 | +0.076 | STANDARD |

**DET @ COL** · priced 178/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.53, exp saves 23.51 (sd 6.29), pull risk 0.046
- DET net: Daniil Tarasov (PROJECTED) exp shots 30.11, exp saves 25.32 (sd 7.17), pull risk 0.095

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lucas Raymond: 1+ points | 0.486 | 0.570 | 60/46 | +0.037 | STANDARD |
| Sam Malinski: 1+ assists | 0.318 | 0.235 | 25/78 | +0.055 | STANDARD |
| Lucas Raymond: 1+ assists | 0.318 | 0.400 | 42/62 | +0.045 | STANDARD |
| Sam Malinski: 1+ points | 0.376 | 0.300 | 32/72 | +0.041 | STANDARD |
| Artturi Lehkonen: 1+ assists | 0.344 | 0.275 | 28/73 | +0.050 | STANDARD |
| Lucas Raymond: 2+ points | 0.145 | 0.210 | 24/82 | +0.024 | STANDARD |

**PIT @ LAK** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROBABLE) exp shots 27.28, exp saves 23.67 (sd 6.45), pull risk 0.059
- PIT net: Sergei Murashov (CONFIRMED) exp shots 27.6, exp saves 23.6 (sd 6.62), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.418 | 0.530 | 54/48 | +0.085 | STANDARD |
| Artemi Panarin: 2+ points | 0.238 | 0.340 | 35/67 | +0.077 | STANDARD |
| Ben Kindel: 1+ points | 0.364 | 0.460 | 47/55 | +0.068 | STANDARD |
| Ben Kindel: 1+ assists | 0.223 | 0.305 | 32/71 | +0.052 | STANDARD |
| Trevor Moore: 1+ points | 0.428 | 0.350 | 37/67 | +0.042 | STANDARD |
| Erik Karlsson: 1+ points | 0.487 | 0.565 | 58/45 | +0.046 | STANDARD |

**VAN @ EDM** · priced 165/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 24.17, exp saves 21.32 (sd 5.93), pull risk 0.052
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.14, exp saves 25.04 (sd 7.29), pull risk 0.111

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.264 | 0.405 | 42/61 | +0.109 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.617 | 0.485 | 50/53 | +0.100 | STANDARD |
| Connor McDavid: 1+ assists | 0.629 | 0.750 | 77/27 | +0.088 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.416 | 0.295 | 31/72 | +0.091 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.343 | 0.460 | 47/55 | +0.090 | STANDARD |
| Leon Draisaitl: 2+ points | 0.433 | 0.545 | 56/47 | +0.080 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
