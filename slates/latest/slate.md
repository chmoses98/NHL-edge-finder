# NHL slate 2026-11-02 — RESEARCH_ONLY

generated 2026-11-03T00:37:41Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 2 · markets on board: 2851 · contracts joined: 455 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 405, 'OK': 27, 'NO_EDGE': 23}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 70, 'game_early_goal': 2, 'first_goal': 69, 'game_winner': 4, 'player_goals': 118, 'game_overtime': 2, 'player_points': 92, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| COL @ CHI | 2026-11-03T01:00:00Z | T-10m | 0.373 | 0.627 | 0.172 | 6.09 | 2.65 | 3.44 | 220 (25/195) | CONFIRMED/CONFIRMED |
| CGY @ SJS | 2026-11-03T02:00:00Z | T-60m | 0.530 | 0.470 | 0.166 | 6.65 | 3.42 | 3.23 | 235 (25/210) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL4 | team_total | 0.462 | 0.565 | 0.545 | 57 | 44 | no | +0.081 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL5 | team_total | 0.266 | 0.340 | 0.324 | 35 | 67 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL3 | team_total | 0.681 | 0.750 | 0.737 | 76 | 26 | no | +0.045 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL3 | game_spread | 0.260 | 0.325 | 0.311 | 33 | 68 | no | +0.045 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-8 | game_total | 0.324 | 0.265 | 0.276 | 27 | 74 | yes | +0.041 | OK |
| KXNHLTOTAL-26NOV02COLCHI-4 | game_total | 0.844 | 0.885 | 0.878 | 89 | 12 | no | +0.029 | OK |
| KXNHLGAME-26NOV02COLCHI-CHI | game_winner | 0.373 | 0.325 | 0.334 | 33 | 68 | yes | +0.027 | OK |
| KXNHLGAME-26NOV02COLCHI-COL | game_winner | 0.627 | 0.675 | 0.666 | 68 | 33 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV02COLCHI-6 | game_total | 0.546 | 0.595 | 0.585 | 60 | 41 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-6 | game_total | 0.634 | 0.585 | 0.595 | 59 | 42 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-7 | game_total | 0.524 | 0.475 | 0.485 | 48 | 53 | yes | +0.027 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL2 | game_spread | 0.397 | 0.445 | 0.435 | 45 | 56 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-9 | game_total | 0.235 | 0.195 | 0.203 | 20 | 81 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-10 | game_total | 0.117 | 0.085 | 0.091 | 9 | 92 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ6 | team_total | 0.128 | 0.095 | 0.101 | 10 | 91 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV02COLCHI-5 | game_total | 0.762 | 0.800 | 0.793 | 81 | 21 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL6 | team_total | 0.127 | 0.165 | 0.157 | 18 | 85 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL2 | team_total | 0.858 | 0.895 | 0.888 | 91 | 12 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV02COLCHI-7 | game_total | 0.429 | 0.465 | 0.458 | 47 | 54 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 | team_total | 0.234 | 0.195 | 0.202 | 21 | 82 | yes | +0.012 | OK |
| KXNHLSPREAD-26NOV02COLCHI-CHI2 | game_spread | 0.185 | 0.165 | 0.169 | 17 | 84 | yes | +0.005 | OK |
| KXNHLTOTAL-26NOV02COLCHI-8 | game_total | 0.242 | 0.265 | 0.260 | 27 | 74 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY6 | team_total | 0.111 | 0.085 | 0.090 | 10 | 93 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ4 | team_total | 0.462 | 0.435 | 0.440 | 44 | 57 | yes | +0.005 | OK |
| KXNHLTOTAL-26NOV02COLCHI-9 | game_total | 0.165 | 0.185 | 0.181 | 19 | 82 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ5 | team_total | 0.265 | 0.240 | 0.245 | 25 | 77 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ3 | team_total | 0.667 | 0.640 | 0.645 | 65 | 37 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-2 | game_total | 0.990 | 0.980 | 0.982 | 99 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-3 | game_total | 0.960 | 0.970 | 0.968 | 98 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI2 | team_total | 0.731 | 0.715 | 0.718 | 72 | 29 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-SJ3 | game_spread | 0.203 | 0.215 | 0.213 | 22 | 79 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY4 | team_total | 0.411 | 0.390 | 0.394 | 40 | 62 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-4 | game_total | 0.891 | 0.885 | 0.886 | 89 | 12 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-3 | game_total | 0.975 | 0.970 | 0.971 | 98 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI4 | team_total | 0.288 | 0.275 | 0.277 | 28 | 73 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26NOV02COLCHI-CHI3 | game_spread | 0.099 | 0.095 | 0.096 | 10 | 91 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI6 | team_total | 0.055 | 0.045 | 0.047 | 6 | 97 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-5 | game_total | 0.820 | 0.810 | 0.812 | 82 | 20 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY3 | team_total | 0.626 | 0.605 | 0.609 | 62 | 41 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ2 | team_total | 0.848 | 0.840 | 0.842 | 85 | 17 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5 | team_total | 0.137 | 0.125 | 0.127 | 14 | 89 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-CGY2 | game_spread | 0.271 | 0.265 | 0.266 | 27 | 74 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI3 | team_total | 0.495 | 0.505 | 0.503 | 51 | 50 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-10 | game_total | 0.079 | 0.080 | 0.080 | 9 | 93 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-SJ2 | game_spread | 0.322 | 0.315 | 0.316 | 32 | 69 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY2 | team_total | 0.825 | 0.820 | 0.821 | 83 | 19 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-CGY3 | game_spread | 0.165 | 0.165 | 0.165 | 17 | 84 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26NOV02CGYSJ-SJ | game_winner | 0.530 | 0.525 | 0.526 | 53 | 48 |  | -0.018 | NO_EDGE |
| KXNHLGAME-26NOV02CGYSJ-CGY | game_winner | 0.470 | 0.475 | 0.474 | 48 | 53 |  | -0.018 | NO_EDGE |
| KXNHL1P-26NOV02COLCHI-CHI | period_winner |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV02COLCHI-COL | period_winner |  | 0.425 |  | 43 | 58 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV02COLCHI-TIE | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV02COLCHI-CHI2 | period_spread |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV02COLCHI-COL2 | period_spread |  | 0.175 |  | 18 | 83 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV02COLCHI-1 | period_total |  | 0.840 |  | 85 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV02COLCHI-2 | period_total |  | 0.565 |  | 57 | 44 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV02COLCHI-3 | period_total |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV02COLCHI-CHI | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV02COLCHI-COL | period_winner |  | 0.445 |  | 46 | 57 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV02COLCHI-TIE | period_winner |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV02COLCHI-CHI2 | period_spread |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV02COLCHI-COL2 | period_spread |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV02COLCHI-1 | period_total |  | 0.900 |  | 92 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV02COLCHI-2 | period_total |  | 0.615 |  | 63 | 40 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV02COLCHI-3 | period_total |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV02COLCHI-CHI | period_winner |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV02COLCHI-COL | period_winner |  | 0.485 |  | 50 | 53 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV02COLCHI-TIE | period_winner |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV02COLCHI-CHI2 | period_spread |  | 0.080 |  | 10 | 94 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV02COLCHI-COL2 | period_spread |  | 0.250 |  | 27 | 77 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV02COLCHI-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV02COLCHI-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV02COLCHI-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02COLCHI-CHIAFRONDELL16-1 | player_assists |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1 | player_assists |  | 0.470 |  | 48 | 54 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02COLCHI-CHICBEDARD98-2 | player_assists |  | 0.125 |  | 16 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02COLCHI-CHIFNAZAR91-1 | player_assists |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02COLCHI-CHIPKANE88-1 | player_assists |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02COLCHI-CHIPKANE88-2 | player_assists |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| COL @ CHI | 0.373 | 0.360 | 0.172 | 0.206 | 6.09 | 6.49 | 0.989/0.980 | KXNHLTOTAL-26NOV02COLCHI-7 +0.071 |
| CGY @ SJS | 0.530 | 0.559 | 0.166 | 0.212 | 6.65 | 6.46 | 1.040/1.007 | KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 -0.040 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.2647 (adj 0.2498) · $9.66 · thesis CHI:OFFENSE_4PLUS
- Cole Smith: 1+ goals YES @ 7c · p 0.0951 (adj 0.0876) · $3.33 · thesis CHI:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 78c · p 0.8229 (adj 0.8084) · $20.0 · thesis COL:SUPPRESSED
- Connor Bedard: 1+ assists NO @ 54c · p 0.6226 (adj 0.5763) · $14.93 · thesis CHI:SUPPRESSED
- Ivar Stenberg: 1+ goals NO @ 76c · p 0.8203 (adj 0.804) · $20.0 · thesis SJS:SUPPRESSED
- Michael Misa: 1+ goals YES @ 18c · p 0.2175 (adj 0.2069) · $4.95 · thesis SJS:OFFENSE_4PLUS
- Michael Misa: 1+ assists YES @ 26c · p 0.3199 (adj 0.2874) · $4.51 · thesis SJS:OFFENSE_4PLUS
- Mason Marchment: 1+ goals YES @ 25c · p 0.2843 (adj 0.2732) · $2.62 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**COL @ CHI** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 31.92, exp saves 26.8 (sd 7.53), pull risk 0.092
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 24.7, exp saves 21.74 (sd 6.05), pull risk 0.048

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.297 | 0.400 | 41/61 | +0.076 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.366 | 0.460 | 47/55 | +0.066 | STANDARD |
| Connor Bedard: 1+ assists | 0.377 | 0.470 | 48/54 | +0.065 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.509 | 0.600 | 61/41 | +0.064 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.157 | 0.225 | 25/80 | +0.032 | STANDARD |
| Patrick Kane: 1+ points | 0.449 | 0.515 | 52/49 | +0.044 | STANDARD |

**CGY @ SJS** · priced 183/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.38, exp saves 24.66 (sd 6.72), pull risk 0.057
- CGY net: Dustin Wolf (CONFIRMED) exp shots 28.99, exp saves 24.78 (sd 6.97), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ assists | 0.243 | 0.100 | 18/98 | +0.052 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.435 | 0.570 | 58/44 | +0.108 | STANDARD |
| Macklin Celebrini: 2+ points | 0.303 | 0.420 | 43/59 | +0.090 | STANDARD |
| Sam Dickinson: 1+ points | 0.296 | 0.185 | 21/84 | +0.074 | STANDARD |
| Macklin Celebrini: 3+ points | 0.100 | 0.195 | 20/81 | +0.079 | STANDARD |
| Ivar Stenberg: 1+ points | 0.409 | 0.500 | 51/51 | +0.063 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
