# NHL slate 2026-11-06 — RESEARCH_ONLY

generated 2026-11-07T00:48:31Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 2 · markets on board: 2805 · contracts joined: 456 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 406, 'NO_EDGE': 31, 'OK': 19}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 66, 'game_early_goal': 2, 'first_goal': 73, 'game_winner': 4, 'player_goals': 122, 'game_overtime': 2, 'player_points': 89, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MIN | 2026-11-07T01:00:00Z | T-10m | 0.718 | 0.282 | 0.146 | 6.43 | 3.95 | 2.47 | 222 (25/197) | CONFIRMED/CONFIRMED |
| ANA @ CGY | 2026-11-07T01:00:00Z | T-10m | 0.488 | 0.512 | 0.169 | 6.64 | 3.29 | 3.35 | 234 (25/209) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV06ANACGY-ANA | game_winner | 0.512 | 0.425 | 0.442 | 43 | 58 | yes | +0.064 | OK |
| KXNHLGAME-26NOV06ANACGY-CGY | game_winner | 0.488 | 0.575 | 0.558 | 58 | 43 | no | +0.064 | OK |
| KXNHLSPREAD-26NOV06ANACGY-CGY3 | game_spread | 0.176 | 0.235 | 0.222 | 24 | 77 | no | +0.042 | OK |
| KXNHLSPREAD-26NOV06ANACGY-CGY2 | game_spread | 0.286 | 0.345 | 0.333 | 35 | 66 | no | +0.038 | OK |
| KXNHLSPREAD-26NOV06ANACGY-ANA2 | game_spread | 0.299 | 0.245 | 0.255 | 25 | 76 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4 | team_total | 0.573 | 0.625 | 0.615 | 63 | 38 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY5 | team_total | 0.238 | 0.285 | 0.275 | 29 | 72 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5 | team_total | 0.256 | 0.215 | 0.223 | 22 | 79 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA3 | team_total | 0.655 | 0.615 | 0.623 | 62 | 39 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY4 | team_total | 0.425 | 0.465 | 0.457 | 47 | 54 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY2 | team_total | 0.836 | 0.870 | 0.864 | 88 | 14 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA6 | team_total | 0.122 | 0.085 | 0.091 | 10 | 93 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY3 | team_total | 0.640 | 0.685 | 0.676 | 70 | 33 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4 | team_total | 0.441 | 0.405 | 0.412 | 41 | 60 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV06ANACGY-ANA3 | game_spread | 0.183 | 0.155 | 0.160 | 16 | 85 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV06SJMIN-4 | game_total | 0.877 | 0.895 | 0.892 | 90 | 11 | no | +0.006 | OK |
| KXNHLTOTAL-26NOV06ANACGY-8 | game_total | 0.327 | 0.305 | 0.309 | 31 | 70 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV06ANACGY-10 | game_total | 0.118 | 0.105 | 0.108 | 11 | 90 | yes | +0.002 | OK |
| KXNHLSPREAD-26NOV06SJMIN-SJ3 | game_spread | 0.065 | 0.075 | 0.073 | 8 | 93 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ2 | team_total | 0.696 | 0.715 | 0.711 | 72 | 29 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA2 | team_total | 0.838 | 0.820 | 0.824 | 83 | 19 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-2 | game_total | 0.989 | 0.980 | 0.982 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-5 | game_total | 0.801 | 0.815 | 0.812 | 82 | 19 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ4 | team_total | 0.248 | 0.265 | 0.262 | 27 | 74 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-3 | game_total | 0.970 | 0.975 | 0.974 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN5 | team_total | 0.366 | 0.390 | 0.385 | 40 | 62 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ6 | team_total | 0.041 | 0.045 | 0.044 | 5 | 96 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-9 | game_total | 0.238 | 0.225 | 0.228 | 23 | 78 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-3 | game_total | 0.973 | 0.980 | 0.979 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26NOV06SJMIN-SJ2 | game_spread | 0.128 | 0.135 | 0.133 | 14 | 87 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY6 | team_total | 0.119 | 0.130 | 0.128 | 14 | 88 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-4 | game_total | 0.889 | 0.895 | 0.894 | 90 | 11 |  | -0.006 | NO_EDGE |
| KXNHLGAME-26NOV06SJMIN-SJ | game_winner | 0.282 | 0.295 | 0.292 | 30 | 71 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-7 | game_total | 0.520 | 0.535 | 0.532 | 54 | 47 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-5 | game_total | 0.817 | 0.830 | 0.827 | 84 | 18 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26NOV06SJMIN-MIN3 | game_spread | 0.361 | 0.375 | 0.372 | 38 | 63 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN3 | team_total | 0.765 | 0.780 | 0.777 | 79 | 23 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-6 | game_total | 0.601 | 0.620 | 0.616 | 63 | 39 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-7 | game_total | 0.481 | 0.495 | 0.492 | 50 | 51 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN6 | team_total | 0.200 | 0.205 | 0.204 | 21 | 80 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN2 | team_total | 0.906 | 0.910 | 0.909 | 92 | 10 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-8 | game_total | 0.292 | 0.285 | 0.286 | 29 | 72 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV06SJMIN-MIN2 | game_spread | 0.507 | 0.515 | 0.513 | 52 | 49 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ5 | team_total | 0.112 | 0.110 | 0.110 | 12 | 90 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-10 | game_total | 0.100 | 0.100 | 0.100 | 11 | 91 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26NOV06SJMIN-MIN | game_winner | 0.718 | 0.715 | 0.716 | 72 | 29 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-9 | game_total | 0.205 | 0.205 | 0.205 | 21 | 80 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-6 | game_total | 0.626 | 0.625 | 0.625 | 63 | 38 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ3 | team_total | 0.453 | 0.455 | 0.455 | 46 | 55 |  | -0.021 | NO_EDGE |
| KXNHL1P-26NOV06SJMIN-MIN | period_winner |  | 0.455 |  | 46 | 55 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV06SJMIN-SJ | period_winner |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV06SJMIN-TIE | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV06SJMIN-MIN2 | period_spread |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV06SJMIN-SJ2 | period_spread |  | 0.055 |  | 6 | 95 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV06SJMIN-1 | period_total |  | 0.860 |  | 87 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV06SJMIN-2 | period_total |  | 0.580 |  | 59 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV06SJMIN-3 | period_total |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV06SJMIN-MIN | period_winner |  | 0.475 |  | 48 | 53 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV06SJMIN-SJ | period_winner |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV06SJMIN-TIE | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV06SJMIN-MIN2 | period_spread |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV06SJMIN-SJ2 | period_spread |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV06SJMIN-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV06SJMIN-2 | period_total |  | 0.625 |  | 64 | 39 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV06SJMIN-3 | period_total |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV06SJMIN-MIN | period_winner |  | 0.515 |  | 52 | 49 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV06SJMIN-SJ | period_winner |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV06SJMIN-TIE | period_winner |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV06SJMIN-MIN2 | period_spread |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV06SJMIN-SJ2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV06SJMIN-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV06SJMIN-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV06SJMIN-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV06SJMIN-MINBBRINK10-1 | player_assists |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV06SJMIN-MINBBRINK10-2 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV06SJMIN-MINBCOLEMAN20-1 | player_assists |  | 0.235 |  | 24 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV06SJMIN-MINJBRODIN25-1 | player_assists |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV06SJMIN-MINJBRODIN25-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV06SJMIN-MINJERIKSSONEK14-1 | player_assists |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MIN | 0.718 | 0.616 | 0.146 | 0.213 | 6.43 | 6.39 | 0.991/1.040 | KXNHLSPREAD-26NOV06SJMIN-MIN2 -0.115 |
| ANA @ CGY | 0.488 | 0.468 | 0.169 | 0.211 | 6.64 | 6.77 | 1.006/1.016 | KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4 +0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Yakov Trenin: 1+ goals YES @ 11c · p 0.1626 (adj 0.1482) · $8.62 · thesis MIN:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 45c · p 0.5365 (adj 0.5136) · $16.92 · thesis MIN:SUPPRESSED
- Minnesota over 3.5 goals scored NO @ 38c · p 0.5088 (adj 0.4218) · $11.5 · thesis MIN:SUPPRESSED
- Blake Coleman: 1+ goals YES @ 23c · p 0.2775 (adj 0.2644) · $8.8 · thesis MIN:OFFENSE_4PLUS
- Sam Colangelo: 1+ goals YES @ 12c · p 0.1702 (adj 0.1564) · $7.58 · thesis ANA:OFFENSE_4PLUS
- Pavel Mintyukov: 1+ goals YES @ 6c · p 0.0957 (adj 0.0843) · $4.65 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1313 (adj 0.1197) · $5.93 · thesis ANA:OFFENSE_4PLUS
- Nico Myatovic: 1+ goals YES @ 10c · p 0.1376 (adj 0.127) · $5.15 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ MIN** · priced 161/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 26.53, exp saves 23.25 (sd 6.35), pull risk 0.048
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 30.36, exp saves 25.69 (sd 7.2), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.322 | 0.480 | 49/53 | +0.130 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.414 | 0.555 | 56/45 | +0.118 | STANDARD |
| Matt Boldy: 1+ assists | 0.407 | 0.535 | 54/47 | +0.105 | STANDARD |
| Quinn Hughes: 2+ points | 0.315 | 0.435 | 44/57 | +0.098 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.210 | 0.320 | 33/69 | +0.085 | STANDARD |
| Ivar Stenberg: 1+ points | 0.340 | 0.450 | 46/56 | +0.083 | STANDARD |

**ANA @ CGY** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 29.8, exp saves 25.55 (sd 7.09), pull risk 0.077
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.38, exp saves 23.69 (sd 6.61), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dustin Wolf: 25+ saves | 0.561 | 0.465 | 47/54 | +0.074 |  |
| Alex Killorn: 1+ points | 0.441 | 0.365 | 38/65 | +0.045 | STANDARD |
| Alex Killorn: 1+ assists | 0.296 | 0.225 | 23/78 | +0.053 | STANDARD |
| Leo Carlsson: 1+ assists | 0.409 | 0.470 | 48/54 | +0.033 | STANDARD |
| Sam Colangelo: 1+ goals | 0.170 | 0.115 | 12/89 | +0.043 | STANDARD |
| Lukas Dostal: 25+ saves | 0.447 | 0.500 | 51/51 | +0.026 |  |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
