# NHL slate 2026-10-16 — RESEARCH_ONLY

generated 2026-10-16T17:55:59Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2812 · contracts joined: 439 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 389, 'NO_EDGE': 46, 'OK': 4}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 62, 'game_early_goal': 2, 'first_goal': 73, 'game_winner': 4, 'player_goals': 119, 'game_overtime': 2, 'player_points': 82, 'goalie_saves': 1, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 2026-10-17T01:00:00Z | T-6h | 0.640 | 0.359 | 0.161 | 6.68 | 3.81 | 2.87 | 224 (25/199) | CONFIRMED/PROJECTED |
| BOS @ ANA | 2026-10-17T02:00:00Z | T-6h | 0.487 | 0.513 | 0.177 | 6.31 | 3.12 | 3.19 | 215 (25/190) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT16BOSANA-BOS3 | game_spread | 0.180 | 0.205 | 0.200 | 21 | 80 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT16PITCOL-5 | game_total | 0.825 | 0.845 | 0.841 | 85 | 16 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT16BOSANA-5 | game_total | 0.787 | 0.805 | 0.801 | 81 | 20 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL4 | team_total | 0.542 | 0.565 | 0.560 | 57 | 44 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT16PITCOL-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-4 | game_total | 0.895 | 0.905 | 0.903 | 91 | 10 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT6 | team_total | 0.073 | 0.055 | 0.058 | 7 | 96 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-4 | game_total | 0.865 | 0.880 | 0.877 | 89 | 13 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-ANA3 | game_spread | 0.163 | 0.180 | 0.177 | 19 | 83 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-9 | game_total | 0.197 | 0.185 | 0.187 | 19 | 82 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT2 | game_spread | 0.186 | 0.175 | 0.177 | 18 | 83 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT3 | game_spread | 0.101 | 0.095 | 0.096 | 10 | 91 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL5 | team_total | 0.340 | 0.360 | 0.356 | 37 | 65 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-10 | game_total | 0.121 | 0.115 | 0.116 | 12 | 89 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-3 | game_total | 0.975 | 0.975 | 0.975 | 98 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-3 | game_total | 0.966 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-COL | game_winner | 0.640 | 0.655 | 0.652 | 66 | 35 |  | -0.006 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-PIT | game_winner | 0.359 | 0.345 | 0.348 | 35 | 66 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-COL3 | game_spread | 0.292 | 0.310 | 0.306 | 32 | 70 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS6 | team_total | 0.099 | 0.095 | 0.096 | 10 | 91 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT5 | team_total | 0.172 | 0.160 | 0.162 | 17 | 85 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-8 | game_total | 0.273 | 0.260 | 0.263 | 27 | 75 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL3 | team_total | 0.738 | 0.750 | 0.748 | 76 | 26 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS2 | team_total | 0.821 | 0.835 | 0.832 | 85 | 18 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6 | team_total | 0.094 | 0.090 | 0.091 | 10 | 92 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-6 | game_total | 0.636 | 0.645 | 0.643 | 65 | 36 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-COL2 | game_spread | 0.426 | 0.435 | 0.433 | 44 | 57 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-10 | game_total | 0.093 | 0.085 | 0.087 | 10 | 93 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS5 | team_total | 0.228 | 0.220 | 0.221 | 23 | 79 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT4 | team_total | 0.329 | 0.320 | 0.322 | 33 | 69 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-8 | game_total | 0.329 | 0.325 | 0.326 | 33 | 68 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-9 | game_total | 0.234 | 0.235 | 0.235 | 24 | 77 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 | team_total | 0.391 | 0.400 | 0.398 | 41 | 61 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-ANA2 | game_spread | 0.275 | 0.275 | 0.275 | 28 | 73 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-BOS2 | game_spread | 0.294 | 0.295 | 0.295 | 30 | 71 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL2 | team_total | 0.892 | 0.895 | 0.894 | 91 | 12 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-7 | game_total | 0.467 | 0.465 | 0.465 | 47 | 54 |  | -0.021 | NO_EDGE |
| KXNHLGAME-26OCT16BOSANA-ANA | game_winner | 0.487 | 0.485 | 0.485 | 49 | 52 |  | -0.021 | NO_EDGE |
| KXNHLGAME-26OCT16BOSANA-BOS | game_winner | 0.513 | 0.515 | 0.515 | 52 | 49 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS3 | team_total | 0.625 | 0.625 | 0.625 | 63 | 38 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5 | team_total | 0.210 | 0.210 | 0.210 | 22 | 80 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT2 | team_total | 0.770 | 0.770 | 0.770 | 78 | 24 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA2 | team_total | 0.811 | 0.815 | 0.814 | 83 | 20 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL6 | team_total | 0.183 | 0.185 | 0.185 | 20 | 83 |  | -0.023 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-7 | game_total | 0.526 | 0.530 | 0.529 | 54 | 48 |  | -0.024 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3 | team_total | 0.607 | 0.610 | 0.609 | 62 | 40 |  | -0.024 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT3 | team_total | 0.548 | 0.550 | 0.550 | 56 | 46 |  | -0.026 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS4 | team_total | 0.411 | 0.410 | 0.410 | 42 | 60 |  | -0.026 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-6 | game_total | 0.580 | 0.580 | 0.580 | 59 | 43 |  | -0.027 | NO_EDGE |
| KXNHL1P-26OCT16PITCOL-COL | period_winner |  | 0.410 |  | 43 | 61 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-PIT | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-TIE | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.160 |  | 18 | 86 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.855 |  | 86 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.600 |  | 61 | 41 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-COL | period_winner |  | 0.430 |  | 45 | 59 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-PIT | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-TIE | period_winner |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.205 |  | 23 | 82 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.655 |  | 67 | 36 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-COL | period_winner |  | 0.470 |  | 49 | 55 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-PIT | period_winner |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-TIE | period_winner |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.090 |  | 12 | 94 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.905 |  | 93 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.665 |  | 68 | 35 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.405 |  | 43 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1 | player_assists |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLBNELSON11-1 | player_assists |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLBNELSON11-2 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1 | player_assists |  | 0.655 |  | 66 | 35 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-2 | player_assists |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-3 | player_assists |  | 0.060 |  | 10 | 98 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 0.640 | 0.619 | 0.161 | 0.208 | 6.68 | 6.66 | 0.978/1.033 | KXNHLSPREAD-26OCT16PITCOL-COL2 -0.022 |
| BOS @ ANA | 0.487 | 0.530 | 0.177 | 0.213 | 6.31 | 6.70 | 1.024/0.968 | KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 +0.076 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Fedor Svechkov: 1+ goals YES @ 10c · p 0.1443 (adj 0.1307) · $6.38 · thesis COL:OFFENSE_4PLUS
- Cale Makar: 1+ assists NO @ 35c · p 0.5573 (adj 0.3981) · $12.17 · thesis COL:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 11c · p 0.1428 (adj 0.1321) · $4.2 · thesis PIT:OFFENSE_4PLUS
- Evgeni Malkin: 1+ assists NO @ 62c · p 0.6954 (adj 0.6552) · $14.21 · thesis PIT:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 11c · p 0.2556 (adj 0.1577) · $6.86 · thesis ANA:OFFENSE_4PLUS
- Beckett Sennecke: 1+ goals YES @ 32c · p 0.3948 (adj 0.3749) · $14.26 · thesis ANA:OFFENSE_4PLUS
- Charlie McAvoy: 1+ assists NO @ 58c · p 0.6737 (adj 0.6243) · $17.5 · thesis BOS:SUPPRESSED
- Leo Carlsson: 1+ goals YES @ 32c · p 0.3756 (adj 0.3604) · $8.88 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ COL** · priced 170/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.95, exp saves 22.75 (sd 6.22), pull risk 0.057
- PIT net: Arturs Silovs (PROJECTED) exp shots 30.66, exp saves 25.86 (sd 7.26), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.443 | 0.655 | 66/35 | +0.191 | STANDARD |
| Cale Makar: 2+ points | 0.190 | 0.370 | 38/64 | +0.154 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.362 | 0.495 | 51/52 | +0.100 | STANDARD |
| Cale Makar: 1+ points | 0.553 | 0.685 | 70/33 | +0.101 | STANDARD |
| Cale Makar: 2+ assists | 0.115 | 0.235 | 25/78 | +0.093 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.509 | 0.610 | 62/40 | +0.074 | STANDARD |

**BOS @ ANA** · priced 154/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 25.7, exp saves 22.27 (sd 6.25), pull risk 0.064
- BOS net: Jeremy Swayman (PROJECTED) exp shots 31.08, exp saves 26.51 (sd 7.28), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.256 | 0.105 | 11/90 | +0.139 | STANDARD |
| Alex Killorn: 1+ points | 0.556 | 0.425 | 44/59 | +0.099 | STANDARD |
| Alex Killorn: 1+ assists | 0.390 | 0.270 | 28/74 | +0.096 | STANDARD |
| Jackson LaCombe: 1+ points | 0.639 | 0.525 | 53/48 | +0.092 | STANDARD |
| Alex Killorn: 2+ points | 0.199 | 0.095 | 13/94 | +0.061 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.326 | 0.425 | 43/58 | +0.077 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
