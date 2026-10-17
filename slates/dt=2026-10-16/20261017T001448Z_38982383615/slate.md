# NHL slate 2026-10-16 — RESEARCH_ONLY

generated 2026-10-17T00:14:48Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2867 · contracts joined: 458 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 408, 'NO_EDGE': 33, 'OK': 17}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 68, 'game_early_goal': 2, 'first_goal': 73, 'game_winner': 4, 'player_goals': 119, 'game_overtime': 2, 'player_points': 92, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 2026-10-17T01:00:00Z | T-30m | 0.654 | 0.346 | 0.161 | 6.74 | 3.88 | 2.87 | 228 (25/203) | CONFIRMED/CONFIRMED |
| BOS @ ANA | 2026-10-17T02:00:00Z | T-90m | 0.539 | 0.461 | 0.170 | 6.64 | 3.44 | 3.20 | 230 (25/205) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT16BOSANA-ANA2 | game_spread | 0.323 | 0.275 | 0.284 | 28 | 73 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5 | team_total | 0.271 | 0.225 | 0.234 | 23 | 78 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT16PITCOL-5 | game_total | 0.825 | 0.865 | 0.858 | 87 | 14 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6 | team_total | 0.131 | 0.095 | 0.101 | 10 | 91 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 | team_total | 0.461 | 0.415 | 0.424 | 42 | 59 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT16BOSANA-9 | game_total | 0.235 | 0.195 | 0.203 | 20 | 81 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT16BOSANA-8 | game_total | 0.327 | 0.280 | 0.289 | 29 | 73 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT16BOSANA-BOS3 | game_spread | 0.157 | 0.195 | 0.187 | 20 | 81 | no | +0.022 | OK |
| KXNHLGAME-26OCT16BOSANA-ANA | game_winner | 0.539 | 0.495 | 0.504 | 50 | 51 | yes | +0.021 | OK |
| KXNHLGAME-26OCT16BOSANA-BOS | game_winner | 0.461 | 0.505 | 0.496 | 51 | 50 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3 | team_total | 0.673 | 0.630 | 0.639 | 64 | 38 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA2 | team_total | 0.855 | 0.825 | 0.831 | 83 | 18 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT16BOSANA-10 | game_total | 0.117 | 0.095 | 0.099 | 10 | 91 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL4 | team_total | 0.555 | 0.585 | 0.579 | 59 | 42 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT16BOSANA-6 | game_total | 0.632 | 0.605 | 0.611 | 61 | 40 | yes | +0.006 | OK |
| KXNHLSPREAD-26OCT16BOSANA-BOS2 | game_spread | 0.261 | 0.285 | 0.280 | 29 | 72 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT16PITCOL-10 | game_total | 0.128 | 0.115 | 0.118 | 12 | 89 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS2 | team_total | 0.821 | 0.840 | 0.836 | 85 | 17 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT6 | team_total | 0.074 | 0.065 | 0.067 | 7 | 94 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-ANA3 | game_spread | 0.200 | 0.185 | 0.188 | 19 | 82 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-4 | game_total | 0.895 | 0.905 | 0.903 | 91 | 10 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-2 | game_total | 0.991 | 0.990 | 0.990 |  | 1 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL2 | team_total | 0.896 | 0.910 | 0.907 | 92 | 10 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS6 | team_total | 0.103 | 0.095 | 0.096 | 10 | 91 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-7 | game_total | 0.524 | 0.500 | 0.505 | 51 | 51 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT3 | game_spread | 0.098 | 0.105 | 0.104 | 11 | 90 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-3 | game_total | 0.975 | 0.975 | 0.975 | 98 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL6 | team_total | 0.194 | 0.185 | 0.187 | 19 | 82 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-COL3 | game_spread | 0.302 | 0.315 | 0.312 | 32 | 69 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-3 | game_total | 0.975 | 0.975 | 0.975 | 98 | 3 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT2 | game_spread | 0.177 | 0.185 | 0.183 | 19 | 82 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-4 | game_total | 0.889 | 0.885 | 0.886 | 89 | 12 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT5 | team_total | 0.170 | 0.165 | 0.166 | 17 | 84 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-5 | game_total | 0.820 | 0.825 | 0.824 | 83 | 18 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT2 | team_total | 0.768 | 0.775 | 0.774 | 78 | 23 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-9 | game_total | 0.251 | 0.240 | 0.242 | 25 | 77 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL5 | team_total | 0.356 | 0.365 | 0.363 | 37 | 64 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-6 | game_total | 0.647 | 0.655 | 0.653 | 66 | 35 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS5 | team_total | 0.229 | 0.225 | 0.226 | 23 | 78 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL3 | team_total | 0.751 | 0.760 | 0.758 | 77 | 25 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-8 | game_total | 0.341 | 0.335 | 0.336 | 34 | 67 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT3 | team_total | 0.547 | 0.560 | 0.557 | 57 | 45 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS4 | team_total | 0.410 | 0.405 | 0.406 | 41 | 60 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-7 | game_total | 0.540 | 0.545 | 0.544 | 55 | 46 |  | -0.017 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-COL2 | game_spread | 0.438 | 0.435 | 0.436 | 44 | 57 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-PIT | game_winner | 0.346 | 0.345 | 0.345 | 35 | 66 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-COL | game_winner | 0.654 | 0.655 | 0.655 | 66 | 35 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS3 | team_total | 0.624 | 0.630 | 0.629 | 64 | 38 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT4 | team_total | 0.331 | 0.330 | 0.330 | 34 | 68 |  | -0.025 | NO_EDGE |
| KXNHL1P-26OCT16PITCOL-COL | period_winner |  | 0.430 |  | 44 | 58 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-PIT | period_winner |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-TIE | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.870 |  | 89 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.620 |  | 63 | 39 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-COL | period_winner |  | 0.440 |  | 45 | 57 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-PIT | period_winner |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-TIE | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.090 |  | 11 | 93 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.920 |  | 94 | 10 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.655 |  | 66 | 35 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-COL | period_winner |  | 0.470 |  | 48 | 54 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-PIT | period_winner |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-TIE | period_winner |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.230 |  | 24 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.925 |  | 94 | 9 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.675 |  | 69 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1 | player_assists |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLBNELSON11-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLBNELSON11-2 | player_assists |  |  |  | 5 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1 | player_assists |  | 0.660 |  | 67 | 35 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-2 | player_assists |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-3 | player_assists |  | 0.080 |  | 11 | 95 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 0.654 | 0.626 | 0.161 | 0.203 | 6.74 | 6.68 | 0.978/1.042 | KXNHLSPREAD-26OCT16PITCOL-COL2 -0.031 |
| BOS @ ANA | 0.539 | 0.548 | 0.170 | 0.213 | 6.64 | 6.76 | 1.016/0.999 | KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 +0.023 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Fedor Svechkov: 1+ goals YES @ 10c · p 0.1409 (adj 0.1282) · $5.58 · thesis COL:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 11c · p 0.1434 (adj 0.1338) · $4.31 · thesis PIT:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 51c · p 0.568 (adj 0.5522) · $13.22 · thesis COL:SUPPRESSED
- Artturi Lehkonen: 1+ goals YES @ 26c · p 0.3068 (adj 0.2939) · $6.75 · thesis COL:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 14c · p 0.2351 (adj 0.17) · $4.67 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 10c · p 0.1332 (adj 0.1224) · $4.07 · thesis ANA:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 62c · p 0.676 (adj 0.6595) · $15.39 · thesis BOS:SUPPRESSED
- Casey Mittelstadt: 1+ goals YES @ 15c · p 0.1825 (adj 0.1731) · $3.97 · thesis BOS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ COL** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.95, exp saves 22.78 (sd 6.25), pull risk 0.053
- PIT net: Arturs Silovs (CONFIRMED) exp shots 30.66, exp saves 25.81 (sd 7.26), pull risk 0.095

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.445 | 0.660 | 67/35 | +0.190 | STANDARD |
| Cale Makar: 2+ points | 0.191 | 0.370 | 38/64 | +0.153 | STANDARD |
| Cale Makar: 1+ points | 0.553 | 0.705 | 71/30 | +0.132 | STANDARD |
| Cale Makar: 2+ assists | 0.115 | 0.265 | 28/75 | +0.122 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.366 | 0.510 | 52/50 | +0.116 | STANDARD |
| Cale Makar: 3+ points | 0.047 | 0.170 | 18/84 | +0.103 | STANDARD |

**BOS @ ANA** · priced 178/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 25.7, exp saves 22.26 (sd 6.19), pull risk 0.065
- BOS net: Michael DiPietro (CONFIRMED) exp shots 31.08, exp saves 26.46 (sd 7.29), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.327 | 0.450 | 46/56 | +0.095 | STANDARD |
| A.J. Greer: 1+ goals | 0.235 | 0.135 | 14/87 | +0.087 | STANDARD |
| Charlie McAvoy: 1+ points | 0.422 | 0.520 | 53/49 | +0.071 | STANDARD |
| Jackson LaCombe: 1+ points | 0.635 | 0.540 | 55/47 | +0.068 | STANDARD |
| Mark Kastelic: 1+ assists | 0.165 | 0.070 | 13/99 | +0.027 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.561 | 0.470 | 48/54 | +0.064 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
