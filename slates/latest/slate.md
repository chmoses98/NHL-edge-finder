# NHL slate 2026-11-06 — RESEARCH_ONLY

generated 2026-11-06T23:58:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2835 · contracts joined: 696 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 621, 'NO_EDGE': 37, 'OK': 38}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 104, 'game_early_goal': 3, 'first_goal': 108, 'game_winner': 6, 'player_goals': 182, 'game_overtime': 3, 'player_points': 143, 'goalie_saves': 6, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ BUF | 2026-11-07T00:00:00Z | T-<10m | 0.594 | 0.406 | 0.176 | 5.91 | 3.25 | 2.66 | 237 (25/212) | CONFIRMED/CONFIRMED |
| SJS @ MIN | 2026-11-07T01:00:00Z | T-60m | 0.718 | 0.282 | 0.146 | 6.43 | 3.95 | 2.47 | 222 (25/197) | CONFIRMED/CONFIRMED |
| ANA @ CGY | 2026-11-07T01:00:00Z | T-60m | 0.489 | 0.511 | 0.168 | 6.62 | 3.28 | 3.35 | 237 (25/212) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV06ANACGY-ANA | game_winner | 0.511 | 0.425 | 0.442 | 43 | 58 | yes | +0.064 | OK |
| KXNHLGAME-26NOV06ANACGY-CGY | game_winner | 0.489 | 0.575 | 0.558 | 58 | 43 | no | +0.064 | OK |
| KXNHLTOTAL-26NOV06CBJBUF-7 | game_total | 0.399 | 0.475 | 0.460 | 48 | 53 | no | +0.054 | OK |
| KXNHLTOTAL-26NOV06CBJBUF-6 | game_total | 0.511 | 0.585 | 0.570 | 59 | 42 | no | +0.052 | OK |
| KXNHLSPREAD-26NOV06ANACGY-CGY2 | game_spread | 0.284 | 0.355 | 0.340 | 36 | 65 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4 | team_total | 0.416 | 0.485 | 0.471 | 49 | 52 | no | +0.047 | OK |
| KXNHLTOTAL-26NOV06CBJBUF-5 | game_total | 0.734 | 0.795 | 0.784 | 80 | 21 | no | +0.044 | OK |
| KXNHLSPREAD-26NOV06ANACGY-ANA2 | game_spread | 0.307 | 0.245 | 0.257 | 25 | 76 | yes | +0.044 | OK |
| KXNHLSPREAD-26NOV06ANACGY-CGY3 | game_spread | 0.174 | 0.235 | 0.222 | 24 | 77 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF5 | team_total | 0.228 | 0.285 | 0.273 | 29 | 72 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV06CBJBUF-4 | game_total | 0.824 | 0.875 | 0.866 | 88 | 13 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV06CBJBUF-8 | game_total | 0.219 | 0.275 | 0.263 | 28 | 73 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-CBJ3 | team_total | 0.500 | 0.545 | 0.536 | 55 | 46 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5 | team_total | 0.254 | 0.215 | 0.222 | 22 | 79 | yes | +0.022 | OK |
| KXNHLSPREAD-26NOV06CBJBUF-BUF3 | game_spread | 0.225 | 0.270 | 0.261 | 28 | 74 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4 | team_total | 0.573 | 0.615 | 0.607 | 62 | 39 | no | +0.021 | OK |
| KXNHLSPREAD-26NOV06ANACGY-ANA3 | game_spread | 0.189 | 0.155 | 0.161 | 16 | 85 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV06CBJBUF-9 | game_total | 0.150 | 0.185 | 0.178 | 19 | 82 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF2 | team_total | 0.833 | 0.870 | 0.863 | 88 | 14 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY2 | team_total | 0.833 | 0.870 | 0.863 | 88 | 14 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY5 | team_total | 0.239 | 0.280 | 0.271 | 29 | 73 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4 | team_total | 0.444 | 0.400 | 0.409 | 41 | 61 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA6 | team_total | 0.122 | 0.085 | 0.092 | 10 | 93 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA3 | team_total | 0.651 | 0.615 | 0.622 | 62 | 39 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF3 | team_total | 0.644 | 0.685 | 0.677 | 70 | 33 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY4 | team_total | 0.423 | 0.455 | 0.449 | 46 | 55 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-CBJ4 | team_total | 0.286 | 0.325 | 0.317 | 34 | 69 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY3 | team_total | 0.636 | 0.670 | 0.663 | 68 | 34 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF6 | team_total | 0.106 | 0.135 | 0.129 | 15 | 88 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV06CBJBUF-10 | game_total | 0.068 | 0.085 | 0.081 | 9 | 92 | no | +0.006 | OK |
| KXNHLTOTAL-26NOV06SJMIN-4 | game_total | 0.877 | 0.895 | 0.892 | 90 | 11 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-CBJ5 | team_total | 0.137 | 0.160 | 0.155 | 17 | 85 | no | +0.004 | OK |
| KXNHLSPREAD-26NOV06CBJBUF-CBJ3 | game_spread | 0.109 | 0.125 | 0.122 | 13 | 88 | no | +0.004 | OK |
| KXNHLSPREAD-26NOV06CBJBUF-BUF2 | game_spread | 0.361 | 0.385 | 0.380 | 39 | 62 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV06CBJBUF-3 | game_total | 0.955 | 0.970 | 0.967 | 98 | 4 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV06SJMIN-6 | game_total | 0.601 | 0.625 | 0.620 | 63 | 38 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-CBJ6 | team_total | 0.055 | 0.070 | 0.067 | 8 | 94 | no | +0.001 | OK |
| KXNHLSPREAD-26NOV06SJMIN-SJ3 | game_spread | 0.065 | 0.075 | 0.073 | 8 | 93 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV06ANACGY-9 | game_total | 0.232 | 0.215 | 0.218 | 22 | 79 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ2 | team_total | 0.696 | 0.715 | 0.711 | 72 | 29 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY6 | team_total | 0.113 | 0.130 | 0.126 | 14 | 88 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-10 | game_total | 0.116 | 0.100 | 0.103 | 11 | 91 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26NOV06CBJBUF-CBJ | game_winner | 0.406 | 0.385 | 0.389 | 39 | 62 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26NOV06CBJBUF-BUF | game_winner | 0.594 | 0.615 | 0.611 | 62 | 39 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-2 | game_total | 0.990 | 0.980 | 0.982 | 99 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA2 | team_total | 0.839 | 0.815 | 0.820 | 83 | 20 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-5 | game_total | 0.801 | 0.815 | 0.812 | 82 | 19 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ4 | team_total | 0.248 | 0.265 | 0.262 | 27 | 74 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN2 | team_total | 0.906 | 0.915 | 0.913 | 92 | 9 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN5 | team_total | 0.366 | 0.390 | 0.385 | 40 | 62 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-CBJ2 | team_total | 0.740 | 0.760 | 0.756 | 77 | 25 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-4 | game_total | 0.887 | 0.895 | 0.893 | 90 | 11 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV06SJMIN-SJ2 | game_spread | 0.128 | 0.135 | 0.133 | 14 | 87 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26NOV06SJMIN-SJ | game_winner | 0.282 | 0.295 | 0.292 | 30 | 71 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-8 | game_total | 0.318 | 0.305 | 0.308 | 31 | 70 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-5 | game_total | 0.817 | 0.825 | 0.823 | 83 | 18 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN3 | team_total | 0.765 | 0.775 | 0.773 | 78 | 23 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-3 | game_total | 0.974 | 0.970 | 0.971 | 98 | 4 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-7 | game_total | 0.481 | 0.495 | 0.492 | 50 | 51 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV06CBJBUF-2 | game_total | 0.981 | 0.975 | 0.976 | 99 | 4 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-3 | game_total | 0.970 | 0.970 | 0.970 | 98 | 4 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-8 | game_total | 0.292 | 0.285 | 0.286 | 29 | 72 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ6 | team_total | 0.041 | 0.045 | 0.044 | 6 | 97 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV06SJMIN-MIN2 | game_spread | 0.507 | 0.515 | 0.513 | 52 | 49 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26NOV06CBJBUF-CBJ2 | game_spread | 0.204 | 0.205 | 0.205 | 21 | 80 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26NOV06SJMIN-MIN | game_winner | 0.718 | 0.715 | 0.716 | 72 | 29 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-9 | game_total | 0.205 | 0.200 | 0.201 | 21 | 81 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-6 | game_total | 0.630 | 0.625 | 0.626 | 63 | 38 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-10 | game_total | 0.100 | 0.095 | 0.096 | 11 | 92 |  | -0.017 | NO_EDGE |
| KXNHLSPREAD-26NOV06SJMIN-MIN3 | game_spread | 0.361 | 0.370 | 0.368 | 38 | 64 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-7 | game_total | 0.521 | 0.530 | 0.528 | 54 | 48 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ5 | team_total | 0.112 | 0.115 | 0.114 | 13 | 90 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ3 | team_total | 0.453 | 0.455 | 0.455 | 46 | 55 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN6 | team_total | 0.200 | 0.200 | 0.200 | 21 | 81 |  | -0.021 | NO_EDGE |
| KXNHL1P-26NOV06CBJBUF-BUF | period_winner |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV06CBJBUF-CBJ | period_winner |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV06CBJBUF-TIE | period_winner |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV06CBJBUF-BUF2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV06CBJBUF-CBJ2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ BUF | 0.594 | 0.545 | 0.176 | 0.220 | 5.91 | 6.16 | 1.003/0.947 | KXNHLTEAMTOTAL-26NOV06CBJBUF-CBJ3 +0.073 |
| SJS @ MIN | 0.718 | 0.616 | 0.146 | 0.213 | 6.43 | 6.39 | 0.991/1.040 | KXNHLSPREAD-26NOV06SJMIN-MIN2 -0.115 |
| ANA @ CGY | 0.489 | 0.469 | 0.168 | 0.211 | 6.62 | 6.77 | 1.006/1.016 | KXNHLTEAMTOTAL-26NOV06ANACGY-ANA3 +0.034 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Mathieu Olivier: 1+ goals YES @ 15c · p 0.1939 (adj 0.1804) · $5.96 · thesis CBJ:WINS_BY_2PLUS
- Tage Thompson: 2+ goals NO @ 90c · p 0.9317 (adj 0.9225) · $20.0 · thesis BUF:SUPPRESSED
- Kent Johnson: 1+ goals NO @ 75c · p 0.7922 (adj 0.7804) · $18.67 · thesis CBJ:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 22c · p 0.2563 (adj 0.2447) · $3.78 · thesis CBJ:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 11c · p 0.1626 (adj 0.1482) · $7.91 · thesis MIN:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 47c · p 0.5365 (adj 0.5174) · $13.82 · thesis MIN:SUPPRESSED
- Olli Maatta: 1+ goals YES @ 5c · p 0.0774 (adj 0.0668) · $2.94 · thesis MIN:OFFENSE_4PLUS
- Blake Coleman: 1+ goals YES @ 23c · p 0.2775 (adj 0.2644) · $7.03 · thesis MIN:OFFENSE_4PLUS
- Sam Colangelo: 1+ goals YES @ 11c · p 0.163 (adj 0.1485) · $8.09 · thesis ANA:OFFENSE_4PLUS
- Pavel Mintyukov: 1+ goals YES @ 6c · p 0.0988 (adj 0.0878) · $5.52 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 11c · p 0.1488 (adj 0.1379) · $5.38 · thesis ANA:OFFENSE_4PLUS
- Nico Myatovic: 1+ goals YES @ 10c · p 0.1338 (adj 0.1241) · $4.61 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CBJ @ BUF** · priced 185/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (CONFIRMED) exp shots 26.98, exp saves 23.44 (sd 6.27), pull risk 0.054
- CBJ net: Jet Greaves (CONFIRMED) exp shots 28.09, exp saves 24.11 (sd 6.65), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Sillinger: 1+ points | 0.379 | 0.305 | 34/73 | +0.023 | STANDARD |
| Tage Thompson: 2+ points | 0.234 | 0.305 | 31/70 | +0.052 | STANDARD |
| Jet Greaves: 26+ saves | 0.406 | 0.475 | 48/53 | +0.046 |  |
| Tage Thompson: 1+ points | 0.602 | 0.670 | 68/34 | +0.043 | STANDARD |
| Rasmus Dahlin: 1+ points | 0.554 | 0.620 | 63/39 | +0.039 | STANDARD |
| Cole Sillinger: 1+ assists | 0.261 | 0.195 | 23/84 | +0.018 | STANDARD |

**SJS @ MIN** · priced 161/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 26.53, exp saves 23.25 (sd 6.35), pull risk 0.048
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 30.36, exp saves 25.69 (sd 7.2), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.322 | 0.495 | 50/51 | +0.150 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.414 | 0.560 | 57/45 | +0.118 | STANDARD |
| Matt Boldy: 1+ assists | 0.407 | 0.535 | 55/48 | +0.095 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.683 | 0.795 | 80/21 | +0.096 | STANDARD |
| Quinn Hughes: 2+ points | 0.315 | 0.425 | 43/58 | +0.088 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.210 | 0.320 | 33/69 | +0.085 | STANDARD |

**ANA @ CGY** · priced 185/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 29.8, exp saves 25.58 (sd 7.03), pull risk 0.075
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.38, exp saves 23.71 (sd 6.59), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Killorn: 1+ assists | 0.303 | 0.215 | 23/80 | +0.060 | STANDARD |
| Alex Killorn: 1+ points | 0.449 | 0.365 | 37/64 | +0.063 | STANDARD |
| Dustin Wolf: 25+ saves | 0.562 | 0.485 | 49/52 | +0.055 |  |
| Sam Colangelo: 1+ goals | 0.163 | 0.105 | 11/90 | +0.046 | STANDARD |
| Lukas Dostal: 25+ saves | 0.449 | 0.505 | 52/51 | +0.023 |  |
| Leo Carlsson: 1+ assists | 0.415 | 0.470 | 48/54 | +0.027 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
