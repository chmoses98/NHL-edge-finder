# NHL slate 2026-10-23 — RESEARCH_ONLY

generated 2026-10-23T13:02:53Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2575 · contracts joined: 259 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 209, 'OK': 37, 'NO_EDGE': 13}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 27, 'game_early_goal': 2, 'first_goal': 37, 'game_winner': 4, 'player_goals': 62, 'game_overtime': 2, 'player_points': 31, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ CHI | 2026-10-24T00:00:00Z | T-6h | 0.481 | 0.519 | 0.184 | 6.00 | 2.94 | 3.06 | 208 (25/183) | PROJECTED/PROJECTED |
| TBL @ COL | 2026-10-24T01:00:00Z | T-6h | 0.538 | 0.462 | 0.176 | 6.07 | 3.16 | 2.92 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL4 | team_total | 0.380 | 0.465 | 0.448 | 47 | 54 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL3 | team_total | 0.595 | 0.680 | 0.664 | 69 | 33 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-MTL3 | game_spread | 0.179 | 0.245 | 0.231 | 25 | 76 | no | +0.048 | OK |
| KXNHLGAME-26OCT23MTLCHI-CHI | game_winner | 0.481 | 0.415 | 0.428 | 42 | 59 | yes | +0.044 | OK |
| KXNHLGAME-26OCT23MTLCHI-MTL | game_winner | 0.519 | 0.585 | 0.572 | 59 | 42 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT23TBCOL-7 | game_total | 0.425 | 0.490 | 0.477 | 50 | 52 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL5 | team_total | 0.200 | 0.265 | 0.251 | 28 | 75 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-6 | game_total | 0.528 | 0.585 | 0.574 | 59 | 42 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT23TBCOL-6 | game_total | 0.539 | 0.600 | 0.588 | 61 | 41 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-7 | game_total | 0.419 | 0.475 | 0.464 | 48 | 53 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-MTL2 | game_spread | 0.294 | 0.345 | 0.334 | 35 | 66 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-5 | game_total | 0.749 | 0.795 | 0.786 | 80 | 21 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT23TBCOL-5 | game_total | 0.761 | 0.805 | 0.797 | 81 | 20 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-4 | game_total | 0.836 | 0.875 | 0.868 | 88 | 13 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL2 | team_total | 0.804 | 0.845 | 0.837 | 85 | 16 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-8 | game_total | 0.231 | 0.275 | 0.266 | 28 | 73 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-9 | game_total | 0.158 | 0.200 | 0.191 | 21 | 81 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT23TBCOL-8 | game_total | 0.237 | 0.280 | 0.271 | 29 | 73 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL6 | team_total | 0.086 | 0.120 | 0.112 | 13 | 89 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT23TBCOL-9 | game_total | 0.165 | 0.195 | 0.189 | 20 | 81 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL4 | team_total | 0.400 | 0.440 | 0.432 | 45 | 57 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT23TBCOL-4 | game_total | 0.849 | 0.880 | 0.874 | 89 | 13 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB4 | team_total | 0.344 | 0.380 | 0.373 | 39 | 63 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB3 | team_total | 0.563 | 0.600 | 0.593 | 61 | 41 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-CHI2 | game_spread | 0.262 | 0.235 | 0.240 | 24 | 77 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT23TBCOL-10 | game_total | 0.075 | 0.095 | 0.091 | 10 | 91 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-3 | game_total | 0.959 | 0.980 | 0.977 | 99 | 3 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT23TBCOL-3 | game_total | 0.961 | 0.980 | 0.977 | 99 | 3 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-10 | game_total | 0.068 | 0.090 | 0.085 | 10 | 92 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB2 | team_total | 0.782 | 0.815 | 0.809 | 83 | 20 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL3 | team_total | 0.619 | 0.650 | 0.644 | 66 | 36 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB5 | team_total | 0.175 | 0.205 | 0.199 | 22 | 81 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL2 | team_total | 0.817 | 0.835 | 0.831 | 84 | 17 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT23TBCOL-COL3 | game_spread | 0.195 | 0.215 | 0.211 | 22 | 79 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT23TBCOL-TB3 | game_spread | 0.148 | 0.165 | 0.161 | 17 | 84 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB6 | team_total | 0.073 | 0.090 | 0.086 | 10 | 92 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL5 | team_total | 0.217 | 0.245 | 0.239 | 26 | 77 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT23TBCOL-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT23MTLCHI-CHI3 | game_spread | 0.154 | 0.145 | 0.147 | 15 | 86 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL6 | team_total | 0.099 | 0.115 | 0.112 | 13 | 90 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI6 | team_total | 0.074 | 0.070 | 0.071 | 8 | 94 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26OCT23TBCOL-TB | game_winner | 0.462 | 0.455 | 0.456 | 46 | 55 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI5 | team_total | 0.177 | 0.180 | 0.179 | 19 | 83 |  | -0.017 | NO_EDGE |
| KXNHLSPREAD-26OCT23TBCOL-TB2 | game_spread | 0.254 | 0.260 | 0.259 | 27 | 75 |  | -0.017 | NO_EDGE |
| KXNHLGAME-26OCT23TBCOL-COL | game_winner | 0.538 | 0.535 | 0.536 | 54 | 47 |  | -0.020 | NO_EDGE |
| KXNHLSPREAD-26OCT23TBCOL-COL2 | game_spread | 0.315 | 0.320 | 0.319 | 33 | 69 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI2 | team_total | 0.789 | 0.790 | 0.790 | 80 | 22 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI4 | team_total | 0.347 | 0.350 | 0.349 | 36 | 66 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI3 | team_total | 0.569 | 0.570 | 0.570 | 58 | 44 |  | -0.026 | NO_EDGE |
| KXNHL1P-26OCT23MTLCHI-CHI | period_winner |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT23MTLCHI-MTL | period_winner |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT23MTLCHI-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT23MTLCHI-CHI2 | period_spread |  | 0.060 |  | 10 | 98 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT23MTLCHI-MTL2 | period_spread |  | 0.110 |  | 13 | 91 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23MTLCHI-1 | period_total |  | 0.830 |  | 84 | 18 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23MTLCHI-2 | period_total |  | 0.555 |  | 56 | 45 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23MTLCHI-3 | period_total |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23MTLCHI-CHI | period_winner |  | 0.310 |  | 34 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23MTLCHI-MTL | period_winner |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23MTLCHI-TIE | period_winner |  | 0.290 |  | 32 | 74 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT23MTLCHI-CHI2 | period_spread |  | 0.115 |  | 15 | 92 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT23MTLCHI-MTL2 | period_spread |  | 0.120 |  | 15 | 91 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23MTLCHI-1 | period_total |  | 0.900 |  | 93 | 13 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23MTLCHI-2 | period_total |  | 0.605 |  | 62 | 41 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23MTLCHI-3 | period_total |  | 0.335 |  | 36 | 69 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23MTLCHI-CHI | period_winner |  | 0.335 |  | 37 | 70 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23MTLCHI-MTL | period_winner |  | 0.415 |  | 47 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23MTLCHI-TIE | period_winner |  | 0.270 |  | 30 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT23MTLCHI-CHI2 | period_spread |  | 0.105 |  | 14 | 93 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT23MTLCHI-MTL2 | period_spread |  | 0.165 |  | 20 | 87 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23MTLCHI-1 | period_total |  | 0.925 |  | 95 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23MTLCHI-2 | period_total |  | 0.670 |  | 69 | 35 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23MTLCHI-3 | period_total |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIAFRONDELL16-1 | player_assists |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIAFRONDELL16-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1 | player_assists |  | 0.460 |  | 48 | 56 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-2 | player_assists |  | 0.095 |  | 15 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIFNAZAR91-1 | player_assists |  | 0.270 |  | 31 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIFNAZAR91-2 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ CHI | 0.481 | 0.481 | 0.184 | 0.224 | 6.00 | 6.33 | 1.003/0.976 | KXNHLTOTAL-26OCT23MTLCHI-7 +0.056 |
| TBL @ COL | 0.538 | 0.579 | 0.176 | 0.216 | 6.07 | 6.27 | 0.976/0.957 | KXNHLTEAMTOTAL-26OCT23TBCOL-COL4 +0.053 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Greene: 1+ goals YES @ 11c · p 0.1539 (adj 0.1354) · $4.77 · thesis CHI:OFFENSE_4PLUS
- Oliver Kapanen: 1+ assists NO @ 67c · p 0.7722 (adj 0.6993) · $12.79 · thesis MTL:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 26c · p 0.2979 (adj 0.2859) · $4.88 · thesis CHI:OFFENSE_4PLUS
- Connor Bedard: 1+ assists NO @ 56c · p 0.6363 (adj 0.5881) · $9.43 · thesis CHI:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MTL @ CHI** · priced 154/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 27.77, exp saves 23.93 (sd 6.59), pull risk 0.067
- MTL net: Jacob Fowler (PROJECTED) exp shots 25.85, exp saves 22.38 (sd 6.23), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Oliver Kapanen: 1+ assists | 0.228 | 0.340 | 35/67 | +0.087 | STANDARD |
| Oliver Kapanen: 1+ points | 0.380 | 0.490 | 50/52 | +0.083 | STANDARD |
| Patrick Kane: 1+ assists | 0.311 | 0.420 | 43/59 | +0.082 | STANDARD |
| Patrick Kane: 1+ points | 0.476 | 0.575 | 58/43 | +0.077 | STANDARD |
| Connor Bedard: 1+ assists | 0.364 | 0.460 | 48/56 | +0.059 | STANDARD |
| Connor Bedard: 1+ points | 0.561 | 0.655 | 68/37 | +0.052 | STANDARD |

**TBL @ COL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.7, exp saves 23.26 (sd 6.31), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 29.24, exp saves 25.08 (sd 6.81), pull risk 0.069

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
