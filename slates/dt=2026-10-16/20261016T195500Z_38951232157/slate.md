# NHL slate 2026-10-16 — RESEARCH_ONLY

generated 2026-10-16T19:55:00Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2818 · contracts joined: 445 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 395, 'NO_EDGE': 32, 'OK': 18}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 63, 'game_early_goal': 2, 'first_goal': 73, 'game_winner': 4, 'player_goals': 119, 'game_overtime': 2, 'player_points': 84, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 2026-10-17T01:00:00Z | T-3h | 0.654 | 0.346 | 0.161 | 6.74 | 3.88 | 2.87 | 228 (25/203) | CONFIRMED/CONFIRMED |
| BOS @ ANA | 2026-10-17T02:00:00Z | T-6h | 0.539 | 0.461 | 0.170 | 6.64 | 3.44 | 3.20 | 217 (25/192) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT16BOSANA-8 | game_total | 0.327 | 0.275 | 0.285 | 28 | 73 | yes | +0.033 | OK |
| KXNHLGAME-26OCT16BOSANA-ANA | game_winner | 0.539 | 0.485 | 0.496 | 49 | 52 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT16BOSANA-ANA2 | game_spread | 0.323 | 0.275 | 0.284 | 28 | 73 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6 | team_total | 0.131 | 0.095 | 0.101 | 10 | 91 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT16BOSANA-BOS3 | game_spread | 0.157 | 0.195 | 0.187 | 20 | 81 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5 | team_total | 0.271 | 0.230 | 0.238 | 24 | 78 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3 | team_total | 0.673 | 0.630 | 0.639 | 64 | 38 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA2 | team_total | 0.855 | 0.825 | 0.831 | 83 | 18 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 | team_total | 0.461 | 0.420 | 0.428 | 43 | 59 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT16BOSANA-9 | game_total | 0.235 | 0.200 | 0.207 | 21 | 81 | yes | +0.013 | OK |
| KXNHLGAME-26OCT16BOSANA-BOS | game_winner | 0.461 | 0.495 | 0.488 | 50 | 51 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT16BOSANA-10 | game_total | 0.117 | 0.090 | 0.095 | 10 | 92 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT16BOSANA-7 | game_total | 0.524 | 0.495 | 0.501 | 50 | 51 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT16PITCOL-5 | game_total | 0.825 | 0.845 | 0.841 | 85 | 16 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT16BOSANA-BOS2 | game_spread | 0.261 | 0.285 | 0.280 | 29 | 72 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT16BOSANA-3 | game_total | 0.975 | 0.965 | 0.967 | 97 | 4 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT16PITCOL-10 | game_total | 0.128 | 0.115 | 0.118 | 12 | 89 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT16PITCOL-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS2 | team_total | 0.821 | 0.840 | 0.836 | 85 | 17 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT6 | team_total | 0.074 | 0.065 | 0.067 | 7 | 94 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-ANA3 | game_spread | 0.200 | 0.185 | 0.188 | 19 | 82 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-4 | game_total | 0.895 | 0.910 | 0.907 | 92 | 10 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL2 | team_total | 0.896 | 0.905 | 0.903 | 91 | 10 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS6 | team_total | 0.103 | 0.095 | 0.096 | 10 | 91 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-6 | game_total | 0.632 | 0.610 | 0.615 | 62 | 40 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-3 | game_total | 0.975 | 0.975 | 0.975 | 98 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL6 | team_total | 0.194 | 0.180 | 0.183 | 19 | 83 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-COL3 | game_spread | 0.302 | 0.315 | 0.312 | 32 | 69 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-4 | game_total | 0.889 | 0.885 | 0.886 | 89 | 12 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT5 | team_total | 0.170 | 0.160 | 0.162 | 17 | 85 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL4 | team_total | 0.555 | 0.565 | 0.563 | 57 | 44 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-9 | game_total | 0.251 | 0.240 | 0.242 | 25 | 77 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT2 | game_spread | 0.177 | 0.175 | 0.175 | 18 | 83 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT3 | game_spread | 0.098 | 0.100 | 0.100 | 11 | 91 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL3 | team_total | 0.751 | 0.755 | 0.754 | 76 | 25 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-8 | game_total | 0.341 | 0.330 | 0.332 | 34 | 68 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT3 | team_total | 0.547 | 0.555 | 0.553 | 56 | 45 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS4 | team_total | 0.410 | 0.415 | 0.414 | 42 | 59 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-7 | game_total | 0.540 | 0.535 | 0.536 | 54 | 47 |  | -0.017 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-COL2 | game_spread | 0.438 | 0.435 | 0.436 | 44 | 57 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-5 | game_total | 0.820 | 0.820 | 0.820 | 83 | 19 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-PIT | game_winner | 0.346 | 0.345 | 0.345 | 35 | 66 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-COL | game_winner | 0.654 | 0.655 | 0.655 | 66 | 35 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS3 | team_total | 0.624 | 0.630 | 0.629 | 64 | 38 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT2 | team_total | 0.768 | 0.770 | 0.770 | 78 | 24 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-6 | game_total | 0.647 | 0.650 | 0.649 | 66 | 36 |  | -0.023 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS5 | team_total | 0.229 | 0.225 | 0.226 | 24 | 79 |  | -0.024 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT4 | team_total | 0.331 | 0.330 | 0.330 | 34 | 68 |  | -0.025 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL5 | team_total | 0.356 | 0.360 | 0.359 | 38 | 66 |  | -0.032 | NO_EDGE |
| KXNHL1P-26OCT16PITCOL-COL | period_winner |  | 0.410 |  | 42 | 60 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-PIT | period_winner |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-TIE | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.170 |  | 18 | 84 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.050 |  | 8 | 98 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.855 |  | 86 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-COL | period_winner |  | 0.435 |  | 45 | 58 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-PIT | period_winner |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-TIE | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.900 |  | 91 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.660 |  | 67 | 35 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-COL | period_winner |  | 0.465 |  | 48 | 55 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-PIT | period_winner |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-TIE | period_winner |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.220 |  | 24 | 80 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.060 |  | 9 | 97 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.925 |  | 95 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.425 |  | 43 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1 | player_assists |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLBNELSON11-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLBNELSON11-2 | player_assists |  | 0.050 |  | 7 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1 | player_assists |  | 0.665 |  | 67 | 34 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-2 | player_assists |  | 0.235 |  | 26 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-3 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 0.654 | 0.626 | 0.161 | 0.203 | 6.74 | 6.68 | 0.978/1.042 | KXNHLSPREAD-26OCT16PITCOL-COL2 -0.031 |
| BOS @ ANA | 0.539 | 0.548 | 0.170 | 0.213 | 6.64 | 6.76 | 1.016/0.999 | KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 +0.023 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Cale Makar: 1+ assists NO @ 34c · p 0.5555 (adj 0.3901) · $12.86 · thesis COL:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 11c · p 0.1434 (adj 0.1326) · $4.12 · thesis PIT:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 26c · p 0.3068 (adj 0.2939) · $7.55 · thesis COL:OFFENSE_4PLUS
- Evgeni Malkin: 1+ assists NO @ 62c · p 0.6936 (adj 0.6543) · $13.19 · thesis PIT:SUPPRESSED
- Nikita Klepov: 1+ assists NO @ 77c · p 0.8516 (adj 0.8083) · $20.0 · thesis ANA:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 14c · p 0.2351 (adj 0.17) · $4.96 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.1342 (adj 0.1232) · $4.44 · thesis ANA:OFFENSE_4PLUS
- Beckett Sennecke: First Goalscorer YES @ 5c · p 0.0692 (adj 0.0646) · $2.88 · thesis ANA:SCORES_FIRST

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ COL** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.95, exp saves 22.78 (sd 6.25), pull risk 0.053
- PIT net: Arturs Silovs (CONFIRMED) exp shots 30.66, exp saves 25.81 (sd 7.26), pull risk 0.095

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.445 | 0.665 | 67/34 | +0.200 | STANDARD |
| Cale Makar: 2+ points | 0.191 | 0.380 | 39/63 | +0.162 | STANDARD |
| Cale Makar: 1+ points | 0.553 | 0.685 | 69/32 | +0.111 | STANDARD |
| Thomas Novak: 1+ assists | 0.263 | 0.135 | 23/96 | +0.020 | STANDARD |
| Cale Makar: 2+ assists | 0.115 | 0.235 | 26/79 | +0.083 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.366 | 0.480 | 49/53 | +0.086 | STANDARD |

**BOS @ ANA** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 25.7, exp saves 22.26 (sd 6.19), pull risk 0.065
- BOS net: Michael DiPietro (CONFIRMED) exp shots 31.08, exp saves 26.46 (sd 7.29), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.327 | 0.435 | 44/57 | +0.086 | STANDARD |
| Jackson LaCombe: 1+ points | 0.635 | 0.530 | 54/48 | +0.078 | STANDARD |
| A.J. Greer: 1+ goals | 0.235 | 0.135 | 14/87 | +0.087 | STANDARD |
| Charlie McAvoy: 1+ points | 0.422 | 0.520 | 53/49 | +0.071 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.561 | 0.470 | 48/54 | +0.064 | STANDARD |
| Nikita Klepov: 1+ assists | 0.148 | 0.235 | 24/77 | +0.069 | PRIOR_HEAVY |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
