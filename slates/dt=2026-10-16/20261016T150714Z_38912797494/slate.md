# NHL slate 2026-10-16 — RESEARCH_ONLY

generated 2026-10-16T15:07:14Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2808 · contracts joined: 435 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 385, 'NO_EDGE': 44, 'OK': 6}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 61, 'game_early_goal': 2, 'first_goal': 73, 'game_winner': 4, 'player_goals': 119, 'game_overtime': 2, 'player_points': 80, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 2026-10-17T01:00:00Z | T-6h | 0.643 | 0.357 | 0.163 | 6.70 | 3.81 | 2.88 | 223 (25/198) | PROJECTED/PROJECTED |
| BOS @ ANA | 2026-10-17T02:00:00Z | T-6h | 0.487 | 0.513 | 0.177 | 6.31 | 3.12 | 3.19 | 212 (25/187) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT6 | team_total | 0.074 | 0.055 | 0.058 | 6 | 95 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT16BOSANA-BOS3 | game_spread | 0.180 | 0.205 | 0.200 | 21 | 80 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT16PITCOL-COL3 | game_spread | 0.288 | 0.315 | 0.309 | 32 | 69 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT5 | team_total | 0.172 | 0.155 | 0.158 | 16 | 85 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL2 | team_total | 0.891 | 0.905 | 0.902 | 91 | 10 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL4 | team_total | 0.542 | 0.565 | 0.561 | 57 | 44 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT16PITCOL-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-4 | game_total | 0.895 | 0.905 | 0.903 | 91 | 10 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-4 | game_total | 0.865 | 0.880 | 0.877 | 89 | 13 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-ANA3 | game_spread | 0.163 | 0.175 | 0.173 | 18 | 83 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT2 | game_spread | 0.187 | 0.175 | 0.177 | 18 | 83 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-10 | game_total | 0.123 | 0.115 | 0.117 | 12 | 89 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-5 | game_total | 0.825 | 0.835 | 0.833 | 84 | 17 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-3 | game_total | 0.966 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-3 | game_total | 0.974 | 0.975 | 0.975 | 98 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS6 | team_total | 0.099 | 0.095 | 0.096 | 10 | 91 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL5 | team_total | 0.341 | 0.360 | 0.356 | 37 | 65 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-5 | game_total | 0.787 | 0.795 | 0.793 | 80 | 21 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT2 | team_total | 0.774 | 0.765 | 0.767 | 77 | 24 |  | -0.009 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-COL | game_winner | 0.643 | 0.655 | 0.653 | 66 | 35 |  | -0.009 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-PIT | game_winner | 0.357 | 0.345 | 0.347 | 35 | 66 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-9 | game_total | 0.243 | 0.235 | 0.237 | 24 | 77 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT4 | team_total | 0.336 | 0.320 | 0.323 | 33 | 69 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-8 | game_total | 0.335 | 0.325 | 0.327 | 33 | 68 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-8 | game_total | 0.273 | 0.265 | 0.267 | 27 | 74 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6 | team_total | 0.094 | 0.090 | 0.091 | 10 | 92 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA2 | team_total | 0.811 | 0.820 | 0.818 | 83 | 19 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-COL2 | game_spread | 0.425 | 0.435 | 0.433 | 44 | 57 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-6 | game_total | 0.637 | 0.645 | 0.643 | 65 | 36 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-10 | game_total | 0.093 | 0.085 | 0.087 | 10 | 93 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT3 | game_spread | 0.103 | 0.100 | 0.101 | 11 | 91 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL6 | team_total | 0.184 | 0.185 | 0.185 | 19 | 82 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-9 | game_total | 0.197 | 0.195 | 0.195 | 20 | 81 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL3 | team_total | 0.741 | 0.750 | 0.748 | 76 | 26 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS5 | team_total | 0.228 | 0.220 | 0.221 | 23 | 79 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-6 | game_total | 0.580 | 0.575 | 0.576 | 58 | 43 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 | team_total | 0.391 | 0.400 | 0.398 | 41 | 61 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT3 | team_total | 0.550 | 0.540 | 0.542 | 55 | 47 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-ANA2 | game_spread | 0.275 | 0.275 | 0.275 | 28 | 73 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-BOS2 | game_spread | 0.294 | 0.295 | 0.295 | 30 | 71 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3 | team_total | 0.607 | 0.605 | 0.605 | 61 | 40 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-7 | game_total | 0.527 | 0.525 | 0.525 | 53 | 48 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-7 | game_total | 0.467 | 0.465 | 0.465 | 47 | 54 |  | -0.021 | NO_EDGE |
| KXNHLGAME-26OCT16BOSANA-ANA | game_winner | 0.487 | 0.485 | 0.485 | 49 | 52 |  | -0.021 | NO_EDGE |
| KXNHLGAME-26OCT16BOSANA-BOS | game_winner | 0.513 | 0.515 | 0.515 | 52 | 49 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS3 | team_total | 0.625 | 0.620 | 0.621 | 63 | 39 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5 | team_total | 0.210 | 0.210 | 0.210 | 22 | 80 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS2 | team_total | 0.821 | 0.830 | 0.828 | 85 | 19 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS4 | team_total | 0.411 | 0.410 | 0.410 | 42 | 60 |  | -0.026 | NO_EDGE |
| KXNHL1P-26OCT16PITCOL-COL | period_winner |  | 0.405 |  | 42 | 61 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-PIT | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-TIE | period_winner |  | 0.310 |  | 33 | 71 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.170 |  | 18 | 84 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.845 |  | 85 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.590 |  | 60 | 42 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-COL | period_winner |  | 0.435 |  | 45 | 58 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-PIT | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-TIE | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.655 |  | 67 | 36 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-COL | period_winner |  | 0.475 |  | 49 | 54 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-PIT | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-TIE | period_winner |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.090 |  | 11 | 93 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.920 |  | 94 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.685 |  | 71 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.430 |  | 44 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1 | player_assists |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLBNELSON11-1 | player_assists |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLBNELSON11-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1 | player_assists |  | 0.560 |  | 57 | 45 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-2 | player_assists |  | 0.210 |  | 23 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-3 | player_assists |  |  |  | 6 |  |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 0.643 | 0.624 | 0.163 | 0.212 | 6.70 | 6.65 | 0.976/1.033 | KXNHLSPREAD-26OCT16PITCOL-COL2 -0.025 |
| BOS @ ANA | 0.487 | 0.530 | 0.177 | 0.213 | 6.31 | 6.70 | 1.024/0.968 | KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 +0.076 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Nathan MacKinnon: 1+ goals NO @ 51c · p 0.5754 (adj 0.5565) · $15.06 · thesis COL:SUPPRESSED
- Fedor Svechkov: 1+ goals YES @ 10c · p 0.1331 (adj 0.1223) · $4.12 · thesis COL:OFFENSE_4PLUS
- Bryan Rust: 1+ goals YES @ 24c · p 0.2854 (adj 0.2728) · $6.38 · thesis PIT:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 26c · p 0.3066 (adj 0.2924) · $6.25 · thesis COL:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 11c · p 0.2556 (adj 0.1577) · $6.86 · thesis ANA:OFFENSE_4PLUS
- Beckett Sennecke: 1+ goals YES @ 32c · p 0.3948 (adj 0.3749) · $14.22 · thesis ANA:OFFENSE_4PLUS
- Leo Carlsson: 1+ goals YES @ 32c · p 0.3756 (adj 0.3604) · $8.93 · thesis ANA:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 62c · p 0.6652 (adj 0.6526) · $10.83 · thesis BOS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ COL** · priced 169/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 25.95, exp saves 22.79 (sd 6.26), pull risk 0.055
- PIT net: Arturs Silovs (PROJECTED) exp shots 30.66, exp saves 25.8 (sd 7.33), pull risk 0.095

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ points | 0.544 | 0.685 | 70/33 | +0.110 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.367 | 0.505 | 52/51 | +0.106 | STANDARD |
| Cale Makar: 2+ points | 0.198 | 0.320 | 34/70 | +0.087 | STANDARD |
| Cale Makar: 1+ assists | 0.439 | 0.560 | 57/45 | +0.093 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.141 | 0.250 | 26/76 | +0.087 | STANDARD |
| Artturi Lehkonen: 1+ points | 0.547 | 0.455 | 47/56 | +0.059 | STANDARD |

**BOS @ ANA** · priced 151/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 25.7, exp saves 22.27 (sd 6.25), pull risk 0.064
- BOS net: Jeremy Swayman (PROJECTED) exp shots 31.08, exp saves 26.51 (sd 7.28), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.256 | 0.105 | 11/90 | +0.139 | STANDARD |
| Alex Killorn: 1+ points | 0.556 | 0.425 | 44/59 | +0.099 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.326 | 0.455 | 47/56 | +0.096 | STANDARD |
| Alex Killorn: 1+ assists | 0.390 | 0.275 | 29/74 | +0.086 | STANDARD |
| Jackson LaCombe: 1+ points | 0.639 | 0.525 | 54/49 | +0.082 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.558 | 0.455 | 47/56 | +0.070 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
