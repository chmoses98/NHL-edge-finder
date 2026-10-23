# NHL slate 2026-10-23 — RESEARCH_ONLY

generated 2026-10-23T17:50:48Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2770 · contracts joined: 454 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 404, 'OK': 36, 'NO_EDGE': 14}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 66, 'game_early_goal': 2, 'first_goal': 75, 'game_winner': 4, 'player_goals': 126, 'game_overtime': 2, 'player_points': 82, 'goalie_saves': 3, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ CHI | 2026-10-24T00:00:00Z | T-6h | 0.470 | 0.530 | 0.182 | 5.92 | 2.87 | 3.05 | 221 (25/196) | PROBABLE/CONFIRMED |
| TBL @ COL | 2026-10-24T01:00:00Z | T-6h | 0.542 | 0.458 | 0.177 | 6.05 | 3.15 | 2.89 | 233 (25/208) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL4 | team_total | 0.377 | 0.485 | 0.463 | 49 | 52 | no | +0.086 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL3 | team_total | 0.592 | 0.685 | 0.667 | 70 | 33 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-MTL3 | game_spread | 0.179 | 0.255 | 0.238 | 26 | 75 | no | +0.058 | OK |
| KXNHLGAME-26OCT23MTLCHI-MTL | game_winner | 0.530 | 0.605 | 0.590 | 61 | 40 | no | +0.054 | OK |
| KXNHLGAME-26OCT23MTLCHI-CHI | game_winner | 0.470 | 0.395 | 0.410 | 40 | 61 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-MTL2 | game_spread | 0.301 | 0.375 | 0.360 | 38 | 63 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-5 | game_total | 0.737 | 0.805 | 0.792 | 81 | 20 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-7 | game_total | 0.402 | 0.475 | 0.460 | 48 | 53 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-6 | game_total | 0.515 | 0.590 | 0.575 | 60 | 42 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT23TBCOL-7 | game_total | 0.425 | 0.495 | 0.481 | 50 | 51 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT23TBCOL-4 | game_total | 0.837 | 0.895 | 0.885 | 90 | 11 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL2 | team_total | 0.801 | 0.855 | 0.845 | 86 | 15 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT23TBCOL-6 | game_total | 0.534 | 0.595 | 0.583 | 60 | 41 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL5 | team_total | 0.199 | 0.270 | 0.255 | 29 | 75 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-8 | game_total | 0.221 | 0.275 | 0.264 | 28 | 73 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT23TBCOL-5 | game_total | 0.754 | 0.805 | 0.796 | 81 | 20 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-4 | game_total | 0.828 | 0.880 | 0.871 | 89 | 13 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB3 | team_total | 0.556 | 0.610 | 0.599 | 62 | 40 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB4 | team_total | 0.338 | 0.395 | 0.383 | 41 | 62 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-CHI2 | game_spread | 0.254 | 0.215 | 0.222 | 22 | 79 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-9 | game_total | 0.152 | 0.190 | 0.182 | 20 | 82 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT23TBCOL-8 | game_total | 0.239 | 0.280 | 0.271 | 29 | 73 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB5 | team_total | 0.174 | 0.210 | 0.202 | 22 | 80 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-3 | game_total | 0.955 | 0.980 | 0.976 | 99 | 3 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL4 | team_total | 0.400 | 0.435 | 0.428 | 44 | 57 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT23TBCOL-3 | game_total | 0.958 | 0.980 | 0.977 | 99 | 3 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT23TBCOL-TB3 | game_spread | 0.142 | 0.165 | 0.160 | 17 | 84 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL3 | team_total | 0.616 | 0.650 | 0.643 | 66 | 36 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL6 | team_total | 0.085 | 0.115 | 0.108 | 13 | 90 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB2 | team_total | 0.781 | 0.815 | 0.808 | 83 | 20 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT23TBCOL-9 | game_total | 0.165 | 0.190 | 0.185 | 20 | 82 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL2 | team_total | 0.818 | 0.840 | 0.836 | 85 | 17 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-10 | game_total | 0.064 | 0.080 | 0.076 | 9 | 93 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT23TBCOL-10 | game_total | 0.074 | 0.090 | 0.086 | 10 | 92 | no | +0.001 | OK |
| KXNHLSPREAD-26OCT23TBCOL-TB2 | game_spread | 0.245 | 0.265 | 0.261 | 27 | 74 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL5 | team_total | 0.217 | 0.245 | 0.239 | 26 | 77 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT23MTLCHI-CHI3 | game_spread | 0.146 | 0.135 | 0.137 | 14 | 87 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT23TBCOL-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB6 | team_total | 0.071 | 0.085 | 0.082 | 10 | 93 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT23TBCOL-COL3 | game_spread | 0.195 | 0.210 | 0.207 | 22 | 80 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI4 | team_total | 0.332 | 0.350 | 0.346 | 36 | 66 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI3 | team_total | 0.552 | 0.570 | 0.566 | 58 | 44 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI2 | team_total | 0.778 | 0.785 | 0.784 | 79 | 22 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL6 | team_total | 0.099 | 0.110 | 0.108 | 13 | 91 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26OCT23TBCOL-COL | game_winner | 0.542 | 0.535 | 0.536 | 54 | 47 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26OCT23TBCOL-TB | game_winner | 0.458 | 0.465 | 0.464 | 47 | 54 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI6 | team_total | 0.067 | 0.065 | 0.065 | 8 | 95 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26OCT23TBCOL-COL2 | game_spread | 0.317 | 0.315 | 0.315 | 32 | 69 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI5 | team_total | 0.164 | 0.165 | 0.165 | 18 | 85 |  | -0.023 | NO_EDGE |
| KXNHL1P-26OCT23MTLCHI-CHI | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT23MTLCHI-MTL | period_winner |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT23MTLCHI-TIE | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT23MTLCHI-CHI2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT23MTLCHI-MTL2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23MTLCHI-1 | period_total |  | 0.835 |  | 85 | 18 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23MTLCHI-2 | period_total |  | 0.565 |  | 57 | 44 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23MTLCHI-3 | period_total |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23MTLCHI-CHI | period_winner |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23MTLCHI-MTL | period_winner |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23MTLCHI-TIE | period_winner |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT23MTLCHI-CHI2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT23MTLCHI-MTL2 | period_spread |  | 0.150 |  | 16 | 86 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23MTLCHI-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23MTLCHI-2 | period_total |  | 0.605 |  | 62 | 41 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23MTLCHI-3 | period_total |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23MTLCHI-CHI | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23MTLCHI-MTL | period_winner |  | 0.430 |  | 45 | 59 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23MTLCHI-TIE | period_winner |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT23MTLCHI-CHI2 | period_spread |  | 0.110 |  | 13 | 91 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT23MTLCHI-MTL2 | period_spread |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23MTLCHI-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23MTLCHI-2 | period_total |  | 0.665 |  | 68 | 35 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23MTLCHI-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIAFRONDELL16-1 | player_assists |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIAFRONDELL16-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1 | player_assists |  | 0.460 |  | 48 | 56 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-2 | player_assists |  | 0.105 |  | 15 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIFNAZAR91-1 | player_assists |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIFNAZAR91-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ CHI | 0.470 | 0.490 | 0.182 | 0.217 | 5.92 | 6.31 | 0.995/0.983 | KXNHLTOTAL-26OCT23MTLCHI-7 +0.072 |
| TBL @ COL | 0.542 | 0.579 | 0.177 | 0.220 | 6.05 | 6.28 | 0.978/0.957 | KXNHLTEAMTOTAL-26OCT23TBCOL-COL3 +0.057 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Anton Frondell: 1+ goals YES @ 20c · p 0.2498 (adj 0.2361) · $7.38 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 26c · p 0.3094 (adj 0.2933) · $6.71 · thesis CHI:OFFENSE_4PLUS
- Montreal wins by over 1.5 goals NO @ 63c · p 0.7014 (adj 0.6632) · $9.54 · thesis CHI:WINS
- Patrick Kane: 1+ assists NO @ 59c · p 0.691 (adj 0.6189) · $12.84 · thesis CHI:SUPPRESSED
- Ilya Mikheyev: 1+ goals YES @ 15c · p 0.1819 (adj 0.1727) · $3.9 · thesis TBL:OFFENSE_4PLUS
- Parker Kelly: 1+ goals YES @ 11c · p 0.1361 (adj 0.1283) · $3.07 · thesis COL:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 27c · p 0.3058 (adj 0.2956) · $3.92 · thesis COL:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MTL @ CHI** · priced 165/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 27.77, exp saves 23.96 (sd 6.57), pull risk 0.068
- MTL net: Jacob Fowler (CONFIRMED) exp shots 25.85, exp saves 22.35 (sd 6.24), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 22+ saves | 0.549 | 0.350 | 56/86 | -0.028 |  |
| Josh Anderson: 1+ points | 0.403 | 0.220 | 37/93 | +0.016 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.296 | 0.120 | 23/99 | +0.053 | STANDARD |
| Alex Newhook: 1+ assists | 0.297 | 0.140 | 26/98 | +0.023 | STANDARD |
| Oliver Kapanen: 1+ points | 0.375 | 0.510 | 52/50 | +0.107 | STANDARD |
| Josh Anderson: 1+ assists | 0.242 | 0.115 | 22/99 | +0.010 | STANDARD |

**TBL @ COL** · priced 165/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.7, exp saves 23.27 (sd 6.32), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 29.24, exp saves 25.12 (sd 6.79), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mackenzie Blackwood: 25+ saves | 0.416 | 0.290 | 57/99 | -0.171 |  |
| Nathan MacKinnon: 2+ points | 0.341 | 0.460 | 48/56 | +0.082 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.463 | 0.580 | 59/43 | +0.089 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.491 | 0.585 | 60/43 | +0.062 | STANDARD |
| Cale Makar: 2+ points | 0.192 | 0.280 | 30/74 | +0.055 | STANDARD |
| Cale Makar: 1+ points | 0.549 | 0.635 | 64/37 | +0.065 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
