# NHL slate 2026-10-18 — RESEARCH_ONLY

generated 2026-10-18T23:05:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 1 · markets on board: 2432 · contracts joined: 239 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 214, 'OK': 24, 'NO_EDGE': 1}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 37, 'game_early_goal': 1, 'first_goal': 36, 'game_winner': 2, 'player_goals': 60, 'game_overtime': 1, 'player_points': 53, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ CGY | 2026-10-19T00:00:00Z | T-30m | 0.452 | 0.548 | 0.184 | 5.84 | 2.78 | 3.07 | 239 (25/214) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4 | team_total | 0.377 | 0.525 | 0.495 | 53 | 48 | no | +0.125 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR3 | team_total | 0.602 | 0.730 | 0.706 | 74 | 28 | no | +0.104 | OK |
| KXNHLSPREAD-26OCT18CARCGY-CAR3 | game_spread | 0.193 | 0.315 | 0.287 | 32 | 69 | no | +0.102 | OK |
| KXNHLGAME-26OCT18CARCGY-CAR | game_winner | 0.548 | 0.665 | 0.643 | 67 | 34 | no | +0.097 | OK |
| KXNHLGAME-26OCT18CARCGY-CGY | game_winner | 0.452 | 0.335 | 0.357 | 34 | 67 | yes | +0.097 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5 | team_total | 0.200 | 0.320 | 0.293 | 33 | 69 | no | +0.095 | OK |
| KXNHLSPREAD-26OCT18CARCGY-CAR2 | game_spread | 0.320 | 0.435 | 0.411 | 44 | 57 | no | +0.093 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR2 | team_total | 0.805 | 0.890 | 0.876 | 90 | 12 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT18CARCGY-6 | game_total | 0.501 | 0.585 | 0.568 | 59 | 42 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT18CARCGY-CGY2 | game_spread | 0.241 | 0.165 | 0.179 | 17 | 84 | yes | +0.061 | OK |
| KXNHLTOTAL-26OCT18CARCGY-7 | game_total | 0.389 | 0.465 | 0.449 | 47 | 54 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT18CARCGY-5 | game_total | 0.725 | 0.800 | 0.786 | 81 | 21 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT18CARCGY-4 | game_total | 0.819 | 0.875 | 0.865 | 88 | 13 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR6 | team_total | 0.089 | 0.150 | 0.136 | 16 | 86 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3 | team_total | 0.530 | 0.475 | 0.486 | 48 | 53 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT18CARCGY-CGY3 | game_spread | 0.137 | 0.095 | 0.102 | 10 | 91 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT18CARCGY-8 | game_total | 0.210 | 0.255 | 0.246 | 26 | 75 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY4 | team_total | 0.312 | 0.275 | 0.282 | 28 | 73 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT18CARCGY-9 | game_total | 0.144 | 0.180 | 0.172 | 19 | 83 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT18CARCGY-3 | game_total | 0.952 | 0.975 | 0.972 | 98 | 3 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY2 | team_total | 0.759 | 0.725 | 0.732 | 73 | 28 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY5 | team_total | 0.152 | 0.125 | 0.130 | 13 | 88 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT18CARCGY-10 | game_total | 0.063 | 0.085 | 0.080 | 9 | 92 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY6 | team_total | 0.063 | 0.045 | 0.048 | 5 | 96 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT18CARCGY-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHL1P-26OCT18CARCGY-CAR | period_winner |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT18CARCGY-CGY | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT18CARCGY-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT18CARCGY-CAR2 | period_spread |  | 0.150 |  | 16 | 86 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT18CARCGY-CGY2 | period_spread |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT18CARCGY-1 | period_total |  | 0.820 |  | 83 | 19 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT18CARCGY-2 | period_total |  | 0.565 |  | 57 | 44 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT18CARCGY-3 | period_total |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT18CARCGY-CAR | period_winner |  | 0.440 |  | 45 | 57 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT18CARCGY-CGY | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT18CARCGY-TIE | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT18CARCGY-CAR2 | period_spread |  | 0.180 |  | 20 | 84 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT18CARCGY-CGY2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT18CARCGY-1 | period_total |  | 0.885 |  | 90 | 13 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT18CARCGY-2 | period_total |  | 0.600 |  | 61 | 41 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT18CARCGY-3 | period_total |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT18CARCGY-CAR | period_winner |  | 0.460 |  | 47 | 55 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT18CARCGY-CGY | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT18CARCGY-TIE | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT18CARCGY-CAR2 | period_spread |  | 0.230 |  | 25 | 79 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT18CARCGY-CGY2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT18CARCGY-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT18CARCGY-2 | period_total |  | 0.660 |  | 67 | 35 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT18CARCGY-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARASVECHNIKOV37-1 | player_assists |  | 0.415 |  | 42 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARASVECHNIKOV37-2 | player_assists |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARBNADEAU29-1 | player_assists |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARJBLAKE53-1 | player_assists |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARJBLAKE53-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARJCHATFIELD5-1 | player_assists |  |  |  | 25 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARJMARTINOOK48-1 | player_assists |  | 0.220 |  | 24 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARJSLAVIN74-1 | player_assists |  |  |  | 25 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARKMILLER19-1 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARKMILLER19-2 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARLSTANKOVEN22-1 | player_assists |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARMJANKOWSKI77-1 | player_assists |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARNEHLERS27-1 | player_assists |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARNEHLERS27-2 | player_assists |  | 0.100 |  | 11 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARSAHO20-1 | player_assists |  | 0.530 |  | 54 | 48 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARSAHO20-2 | player_assists |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARSGOSTISBEHERE4-1 | player_assists |  | 0.425 |  | 43 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARSGOSTISBEHERE4-2 | player_assists |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARSWALKER26-1 | player_assists |  | 0.170 |  | 31 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARSWALKER26-2 | player_assists |  |  |  | 6 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARWCARRIER28-1 | player_assists |  | 0.170 |  | 30 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CARWCARRIER28-2 | player_assists |  | 0.060 |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CGYASUNIEV61-1 | player_assists |  | 0.210 |  | 24 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CGYJFARABEE86-1 | player_assists |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CGYJFARABEE86-2 | player_assists |  |  |  | 6 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CGYKBAHL7-1 | player_assists |  |  |  | 15 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CGYMBACKLUND11-1 | player_assists |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CGYMCORONATO27-1 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CGYMCORONATO27-2 | player_assists |  |  |  | 6 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CGYMFROST16-1 | player_assists |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CARCGY-CGYMFROST16-2 | player_assists |  |  |  | 5 |  |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ CGY | 0.452 | 0.451 | 0.184 | 0.220 | 5.84 | 6.16 | 0.978/0.984 | KXNHLTOTAL-26OCT18CARCGY-7 +0.058 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Sebastian Aho: 1+ assists NO @ 48c · p 0.6443 (adj 0.531) · $13.46 · thesis CAR:SUPPRESSED
- Sebastian Aho: 1+ goals NO @ 66c · p 0.7193 (adj 0.7032) · $16.54 · thesis CAR:SUPPRESSED
- Calgary over 2.5 goals scored YES @ 48c · p 0.5687 (adj 0.5218) · $11.11 · thesis CGY:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 69c · p 0.7921 (adj 0.7225) · $2.31 · thesis CGY:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CAR @ CGY** · priced 184/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 31.92, exp saves 27.3 (sd 7.29), pull risk 0.068
- CAR net: Brandon Bussi (CONFIRMED) exp shots 24.78, exp saves 21.62 (sd 6.03), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.180 | 0.360 | 37/65 | +0.154 | STANDARD |
| Sebastian Aho: 1+ assists | 0.356 | 0.530 | 54/48 | +0.147 | STANDARD |
| Sean Walker: 1+ assists | 0.324 | 0.170 | 31/97 | -0.001 | STANDARD |
| Sebastian Aho: 1+ points | 0.532 | 0.670 | 69/35 | +0.102 | STANDARD |
| Bradly Nadeau: 1+ assists | 0.127 | 0.255 | 27/76 | +0.100 | STANDARD |
| Kevin Bahl: 1+ points | 0.279 | 0.155 | 18/87 | +0.088 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
