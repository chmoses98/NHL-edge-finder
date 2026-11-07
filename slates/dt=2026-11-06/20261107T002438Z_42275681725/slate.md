# NHL slate 2026-11-06 — RESEARCH_ONLY

generated 2026-11-07T00:24:38Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 2 · markets on board: 2843 · contracts joined: 459 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 409, 'NO_EDGE': 33, 'OK': 17}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 67, 'game_early_goal': 2, 'first_goal': 73, 'game_winner': 4, 'player_goals': 122, 'game_overtime': 2, 'player_points': 91, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MIN | 2026-11-07T01:00:00Z | T-30m | 0.718 | 0.282 | 0.146 | 6.43 | 3.95 | 2.47 | 222 (25/197) | CONFIRMED/CONFIRMED |
| ANA @ CGY | 2026-11-07T01:00:00Z | T-30m | 0.489 | 0.511 | 0.168 | 6.62 | 3.28 | 3.35 | 237 (25/212) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV06ANACGY-ANA | game_winner | 0.511 | 0.425 | 0.442 | 43 | 58 | yes | +0.064 | OK |
| KXNHLGAME-26NOV06ANACGY-CGY | game_winner | 0.489 | 0.575 | 0.558 | 58 | 43 | no | +0.064 | OK |
| KXNHLSPREAD-26NOV06ANACGY-CGY2 | game_spread | 0.284 | 0.355 | 0.340 | 36 | 65 | no | +0.050 | OK |
| KXNHLSPREAD-26NOV06ANACGY-ANA2 | game_spread | 0.307 | 0.245 | 0.257 | 25 | 76 | yes | +0.044 | OK |
| KXNHLSPREAD-26NOV06ANACGY-CGY3 | game_spread | 0.174 | 0.235 | 0.222 | 24 | 77 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5 | team_total | 0.254 | 0.215 | 0.222 | 22 | 79 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4 | team_total | 0.573 | 0.615 | 0.607 | 62 | 39 | no | +0.021 | OK |
| KXNHLSPREAD-26NOV06ANACGY-ANA3 | game_spread | 0.189 | 0.155 | 0.161 | 16 | 85 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY3 | team_total | 0.636 | 0.685 | 0.676 | 70 | 33 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY5 | team_total | 0.239 | 0.280 | 0.271 | 29 | 73 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4 | team_total | 0.444 | 0.405 | 0.413 | 41 | 60 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA6 | team_total | 0.122 | 0.085 | 0.092 | 10 | 93 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA3 | team_total | 0.651 | 0.615 | 0.622 | 62 | 39 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY4 | team_total | 0.423 | 0.455 | 0.449 | 46 | 55 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY2 | team_total | 0.833 | 0.865 | 0.859 | 88 | 15 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV06SJMIN-4 | game_total | 0.877 | 0.895 | 0.892 | 90 | 11 | no | +0.006 | OK |
| KXNHLSPREAD-26NOV06SJMIN-SJ3 | game_spread | 0.065 | 0.075 | 0.073 | 8 | 93 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV06ANACGY-9 | game_total | 0.232 | 0.215 | 0.218 | 22 | 79 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ2 | team_total | 0.696 | 0.715 | 0.711 | 72 | 29 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY6 | team_total | 0.113 | 0.135 | 0.130 | 15 | 88 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-10 | game_total | 0.116 | 0.100 | 0.103 | 11 | 91 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-2 | game_total | 0.990 | 0.980 | 0.982 | 99 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA2 | team_total | 0.839 | 0.815 | 0.820 | 83 | 20 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-5 | game_total | 0.801 | 0.815 | 0.812 | 82 | 19 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ4 | team_total | 0.248 | 0.265 | 0.262 | 27 | 74 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN5 | team_total | 0.366 | 0.390 | 0.385 | 40 | 62 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-4 | game_total | 0.887 | 0.895 | 0.893 | 90 | 11 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV06SJMIN-SJ2 | game_spread | 0.128 | 0.135 | 0.133 | 14 | 87 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26NOV06SJMIN-SJ | game_winner | 0.282 | 0.295 | 0.292 | 30 | 71 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-8 | game_total | 0.318 | 0.305 | 0.308 | 31 | 70 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-5 | game_total | 0.817 | 0.825 | 0.823 | 83 | 18 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26NOV06SJMIN-MIN3 | game_spread | 0.361 | 0.375 | 0.372 | 38 | 63 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN3 | team_total | 0.765 | 0.780 | 0.777 | 79 | 23 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-3 | game_total | 0.974 | 0.970 | 0.971 | 98 | 4 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-6 | game_total | 0.601 | 0.615 | 0.612 | 62 | 39 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-7 | game_total | 0.481 | 0.495 | 0.492 | 50 | 51 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN6 | team_total | 0.200 | 0.205 | 0.204 | 21 | 80 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-3 | game_total | 0.970 | 0.970 | 0.970 | 98 | 4 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN2 | team_total | 0.906 | 0.910 | 0.909 | 92 | 10 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-8 | game_total | 0.292 | 0.285 | 0.286 | 29 | 72 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ6 | team_total | 0.041 | 0.045 | 0.044 | 6 | 97 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV06SJMIN-MIN2 | game_spread | 0.507 | 0.515 | 0.513 | 52 | 49 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26NOV06SJMIN-MIN | game_winner | 0.718 | 0.715 | 0.716 | 72 | 29 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-9 | game_total | 0.205 | 0.200 | 0.201 | 21 | 81 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-6 | game_total | 0.630 | 0.625 | 0.626 | 63 | 38 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-10 | game_total | 0.100 | 0.095 | 0.096 | 11 | 92 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-7 | game_total | 0.521 | 0.525 | 0.524 | 53 | 48 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ5 | team_total | 0.112 | 0.115 | 0.114 | 13 | 90 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ3 | team_total | 0.453 | 0.455 | 0.455 | 46 | 55 |  | -0.021 | NO_EDGE |
| KXNHL1P-26NOV06SJMIN-MIN | period_winner |  | 0.445 |  | 45 | 56 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV06SJMIN-SJ | period_winner |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV06SJMIN-TIE | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV06SJMIN-MIN2 | period_spread |  | 0.170 |  | 18 | 84 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV06SJMIN-SJ2 | period_spread |  | 0.055 |  | 6 | 95 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV06SJMIN-1 | period_total |  | 0.860 |  | 87 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV06SJMIN-2 | period_total |  | 0.585 |  | 59 | 42 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV06SJMIN-3 | period_total |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV06SJMIN-MIN | period_winner |  | 0.475 |  | 48 | 53 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV06SJMIN-SJ | period_winner |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV06SJMIN-TIE | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV06SJMIN-MIN2 | period_spread |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV06SJMIN-SJ2 | period_spread |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV06SJMIN-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV06SJMIN-2 | period_total |  | 0.635 |  | 64 | 37 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV06SJMIN-3 | period_total |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV06SJMIN-MIN | period_winner |  | 0.515 |  | 52 | 49 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV06SJMIN-SJ | period_winner |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV06SJMIN-TIE | period_winner |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV06SJMIN-MIN2 | period_spread |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV06SJMIN-SJ2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV06SJMIN-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV06SJMIN-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV06SJMIN-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV06SJMIN-MINBBRINK10-1 | player_assists |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV06SJMIN-MINBBRINK10-2 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV06SJMIN-MINBCOLEMAN20-1 | player_assists |  | 0.230 |  | 24 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV06SJMIN-MINJBRODIN25-1 | player_assists |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV06SJMIN-MINJBRODIN25-2 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV06SJMIN-MINJERIKSSONEK14-1 | player_assists |  | 0.425 |  | 44 | 59 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MIN | 0.718 | 0.616 | 0.146 | 0.213 | 6.43 | 6.39 | 0.991/1.040 | KXNHLSPREAD-26NOV06SJMIN-MIN2 -0.115 |
| ANA @ CGY | 0.489 | 0.469 | 0.168 | 0.211 | 6.62 | 6.77 | 1.006/1.016 | KXNHLTEAMTOTAL-26NOV06ANACGY-ANA3 +0.034 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Yakov Trenin: 1+ goals YES @ 11c · p 0.1626 (adj 0.1482) · $8.73 · thesis MIN:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 47c · p 0.5365 (adj 0.5186) · $10.21 · thesis MIN:SUPPRESSED
- Blake Coleman: 1+ goals YES @ 23c · p 0.2775 (adj 0.2644) · $8.93 · thesis MIN:OFFENSE_4PLUS
- Minnesota over 3.5 goals scored NO @ 39c · p 0.5088 (adj 0.4283) · $12.21 · thesis MIN:SUPPRESSED
- Sam Colangelo: 1+ goals YES @ 11c · p 0.163 (adj 0.1485) · $8.09 · thesis ANA:OFFENSE_4PLUS
- Pavel Mintyukov: 1+ goals YES @ 6c · p 0.0988 (adj 0.0878) · $5.52 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 11c · p 0.1488 (adj 0.1379) · $5.38 · thesis ANA:OFFENSE_4PLUS
- Nico Myatovic: 1+ goals YES @ 10c · p 0.1338 (adj 0.1241) · $4.61 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ MIN** · priced 161/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 26.53, exp saves 23.25 (sd 6.35), pull risk 0.048
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 30.36, exp saves 25.69 (sd 7.2), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.322 | 0.495 | 50/51 | +0.150 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.414 | 0.555 | 56/45 | +0.118 | STANDARD |
| Matt Boldy: 1+ assists | 0.407 | 0.535 | 54/47 | +0.105 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.210 | 0.325 | 33/68 | +0.095 | STANDARD |
| Quinn Hughes: 2+ points | 0.315 | 0.425 | 43/58 | +0.088 | STANDARD |
| Ivar Stenberg: 1+ points | 0.340 | 0.445 | 46/57 | +0.073 | STANDARD |

**ANA @ CGY** · priced 185/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 29.8, exp saves 25.58 (sd 7.03), pull risk 0.075
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.38, exp saves 23.71 (sd 6.59), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dustin Wolf: 25+ saves | 0.562 | 0.475 | 48/53 | +0.065 |  |
| Alex Killorn: 1+ assists | 0.303 | 0.220 | 23/79 | +0.060 | STANDARD |
| Alex Killorn: 1+ points | 0.449 | 0.375 | 39/64 | +0.043 | STANDARD |
| Sam Colangelo: 1+ goals | 0.163 | 0.105 | 11/90 | +0.046 | STANDARD |
| Leo Carlsson: 1+ assists | 0.415 | 0.470 | 48/54 | +0.027 | STANDARD |
| Lukas Dostal: 25+ saves | 0.449 | 0.500 | 51/51 | +0.023 |  |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
