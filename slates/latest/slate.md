# NHL slate 2026-10-11 — RESEARCH_ONLY

generated 2026-10-11T22:47:24Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 1 · markets on board: 2722 · contracts joined: 245 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 220, 'OK': 13, 'NO_EDGE': 12}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 38, 'game_early_goal': 1, 'first_goal': 36, 'game_winner': 2, 'player_goals': 63, 'game_overtime': 1, 'player_points': 55, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ PHI | 2026-10-11T23:00:00Z | T-10m | 0.378 | 0.622 | 0.178 | 5.82 | 2.54 | 3.27 | 245 (25/220) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT11CARPHI-CAR3 | game_spread | 0.243 | 0.295 | 0.284 | 30 | 71 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4 | team_total | 0.427 | 0.475 | 0.465 | 48 | 53 | no | +0.026 | OK |
| KXNHLGAME-26OCT11CARPHI-CAR | game_winner | 0.622 | 0.665 | 0.657 | 67 | 34 | no | +0.022 | OK |
| KXNHLGAME-26OCT11CARPHI-PHI | game_winner | 0.378 | 0.335 | 0.343 | 34 | 67 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT11CARPHI-CAR2 | game_spread | 0.384 | 0.425 | 0.417 | 43 | 58 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR2 | team_total | 0.841 | 0.870 | 0.865 | 88 | 14 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT11CARPHI-5 | game_total | 0.726 | 0.755 | 0.749 | 76 | 25 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT11CARPHI-4 | game_total | 0.820 | 0.845 | 0.840 | 85 | 16 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT11CARPHI-6 | game_total | 0.493 | 0.525 | 0.519 | 53 | 48 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR5 | team_total | 0.231 | 0.255 | 0.250 | 26 | 75 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT11CARPHI-PHI2 | game_spread | 0.185 | 0.165 | 0.169 | 17 | 84 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT11CARPHI-7 | game_total | 0.379 | 0.405 | 0.400 | 41 | 60 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR3 | team_total | 0.652 | 0.675 | 0.670 | 68 | 33 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT11CARPHI-8 | game_total | 0.209 | 0.225 | 0.222 | 23 | 78 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR6 | team_total | 0.105 | 0.120 | 0.117 | 13 | 89 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-10 | game_total | 0.060 | 0.065 | 0.064 | 7 | 94 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT11CARPHI-PHI3 | game_spread | 0.098 | 0.105 | 0.104 | 11 | 90 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-3 | game_total | 0.951 | 0.960 | 0.958 | 97 | 5 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI5 | team_total | 0.121 | 0.110 | 0.112 | 12 | 90 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI6 | team_total | 0.046 | 0.045 | 0.045 | 5 | 96 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-9 | game_total | 0.142 | 0.150 | 0.148 | 16 | 86 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI4 | team_total | 0.263 | 0.255 | 0.257 | 26 | 75 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI2 | team_total | 0.713 | 0.705 | 0.707 | 71 | 30 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI3 | team_total | 0.469 | 0.460 | 0.462 | 47 | 55 |  | -0.018 | NO_EDGE |
| KXNHL1P-26OCT11CARPHI-CAR | period_winner |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT11CARPHI-PHI | period_winner |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT11CARPHI-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT11CARPHI-CAR2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT11CARPHI-PHI2 | period_spread |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT11CARPHI-1 | period_total |  | 0.815 |  | 82 | 19 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT11CARPHI-2 | period_total |  | 0.515 |  | 52 | 49 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT11CARPHI-3 | period_total |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT11CARPHI-CAR | period_winner |  | 0.425 |  | 44 | 59 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT11CARPHI-PHI | period_winner |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT11CARPHI-TIE | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT11CARPHI-CAR2 | period_spread |  | 0.185 |  | 20 | 83 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT11CARPHI-PHI2 | period_spread |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT11CARPHI-1 | period_total |  | 0.865 |  | 88 | 15 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT11CARPHI-2 | period_total |  | 0.585 |  | 59 | 42 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT11CARPHI-3 | period_total |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT11CARPHI-CAR | period_winner |  | 0.460 |  | 48 | 56 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT11CARPHI-PHI | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT11CARPHI-TIE | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT11CARPHI-CAR2 | period_spread |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT11CARPHI-PHI2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT11CARPHI-1 | period_total |  | 0.890 |  | 90 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT11CARPHI-2 | period_total |  | 0.630 |  | 64 | 38 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT11CARPHI-3 | period_total |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARASVECHNIKOV37-1 | player_assists |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARASVECHNIKOV37-2 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CAREROBINSON50-1 | player_assists |  | 0.125 |  | 18 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARJBLAKE53-1 | player_assists |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARJBLAKE53-2 | player_assists |  | 0.065 |  | 7 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARJCHATFIELD5-1 | player_assists |  | 0.165 |  | 22 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARJKOTKANIEMI82-1 | player_assists |  | 0.145 |  | 20 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARJMARTINOOK48-1 | player_assists |  | 0.160 |  | 23 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARJSLAVIN74-1 | player_assists |  | 0.190 |  | 23 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARJSTAAL11-1 | player_assists |  | 0.220 |  | 23 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARKMILLER19-1 | player_assists |  | 0.280 |  | 31 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARKMILLER19-2 | player_assists |  | 0.040 |  | 6 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARLSTANKOVEN22-1 | player_assists |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARLSTANKOVEN22-2 | player_assists |  | 0.045 |  | 5 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARNEHLERS27-1 | player_assists |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARNEHLERS27-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARSAHO20-1 | player_assists |  | 0.465 |  | 47 | 54 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARSAHO20-2 | player_assists |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARSGOSTISBEHERE4-1 | player_assists |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARSGOSTISBEHERE4-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARSWALKER26-1 | player_assists |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARTHALL71-1 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARTHALL71-2 | player_assists |  | 0.055 |  | 6 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-CARWCARRIER28-1 | player_assists |  | 0.190 |  | 23 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-PHICDVORAK22-1 | player_assists |  | 0.230 |  | 24 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-PHIDBARKEY86-1 | player_assists |  | 0.180 |  | 21 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-PHIDJIRICEK55-1 | player_assists |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-PHIDJIRICEK55-2 | player_assists |  | 0.040 |  | 5 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-PHIJDRYSDALE9-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-PHIMMICHKOV39-1 | player_assists |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11CARPHI-PHIMMICHKOV39-2 | player_assists |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ PHI | 0.378 | 0.478 | 0.178 | 0.227 | 5.82 | 5.88 | 0.992/0.997 | KXNHLGAME-26OCT11CARPHI-CAR -0.100 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Sebastian Aho: 1+ goals NO @ 67c · p 0.7507 (adj 0.7293) · $15.0 · thesis CAR:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 13c · p 0.1852 (adj 0.1689) · $6.78 · thesis PHI:OFFENSE_4PLUS
- Nikolaj Ehlers: 1+ goals NO @ 75c · p 0.8066 (adj 0.7912) · $15.0 · thesis CAR:SUPPRESSED
- Joseph Woll: 29+ saves NO @ 50c · p 0.6495 (adj 0.5336) · $8.14 · thesis PHI:NET_LOW_VOLUME

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CAR @ PHI** · priced 192/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 30.15, exp saves 26.02 (sd 6.92), pull risk 0.055
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.75, exp saves 19.77 (sd 5.63), pull risk 0.049

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ points | 0.470 | 0.655 | 66/35 | +0.164 | STANDARD |
| Sebastian Aho: 1+ assists | 0.297 | 0.465 | 47/54 | +0.146 | STANDARD |
| Sebastian Aho: 2+ points | 0.141 | 0.300 | 32/72 | +0.125 | STANDARD |
| Joseph Woll: 29+ saves | 0.350 | 0.505 | 51/50 | +0.132 |  |
| Andrei Svechnikov: 1+ points | 0.474 | 0.580 | 59/43 | +0.079 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.282 | 0.380 | 39/63 | +0.072 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
