# NHL slate 2026-10-11 — RESEARCH_ONLY

generated 2026-10-11T21:58:07Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 2 · markets on board: 2701 · contracts joined: 454 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 404, 'NO_EDGE': 29, 'OK': 21}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 63, 'game_early_goal': 2, 'first_goal': 71, 'game_winner': 4, 'player_goals': 124, 'game_overtime': 2, 'player_points': 90, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VAN @ NYR | 2026-10-11T22:00:00Z | T-<10m | 0.698 | 0.302 | 0.152 | 6.43 | 3.87 | 2.56 | 211 (25/186) | CONFIRMED/PROBABLE |
| CAR @ PHI | 2026-10-11T23:00:00Z | T-60m | 0.378 | 0.622 | 0.178 | 5.82 | 2.54 | 3.27 | 243 (25/218) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT11CARPHI-CAR3 | game_spread | 0.243 | 0.295 | 0.284 | 30 | 71 | no | +0.033 | OK |
| KXNHLGAME-26OCT11CARPHI-CAR | game_winner | 0.622 | 0.665 | 0.657 | 67 | 34 | no | +0.022 | OK |
| KXNHLGAME-26OCT11CARPHI-PHI | game_winner | 0.378 | 0.335 | 0.343 | 34 | 67 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT11VANNYR-8 | game_total | 0.294 | 0.255 | 0.262 | 26 | 75 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT11CARPHI-CAR2 | game_spread | 0.384 | 0.425 | 0.417 | 43 | 58 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT11VANNYR-9 | game_total | 0.207 | 0.175 | 0.181 | 18 | 83 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT11VANNYR-7 | game_total | 0.483 | 0.445 | 0.453 | 45 | 56 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4 | team_total | 0.427 | 0.470 | 0.461 | 48 | 54 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR2 | team_total | 0.841 | 0.865 | 0.860 | 87 | 14 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT11CARPHI-5 | game_total | 0.726 | 0.755 | 0.749 | 76 | 25 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT11CARPHI-4 | game_total | 0.820 | 0.845 | 0.840 | 85 | 16 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT11CARPHI-6 | game_total | 0.493 | 0.525 | 0.519 | 53 | 48 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT11VANNYR-10 | game_total | 0.102 | 0.080 | 0.084 | 9 | 93 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR5 | team_total | 0.231 | 0.255 | 0.250 | 26 | 75 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3 | team_total | 0.473 | 0.445 | 0.451 | 45 | 56 | yes | +0.005 | OK |
| KXNHLSPREAD-26OCT11CARPHI-PHI2 | game_spread | 0.185 | 0.165 | 0.169 | 17 | 84 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT11VANNYR-6 | game_total | 0.601 | 0.575 | 0.580 | 58 | 43 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT11CARPHI-7 | game_total | 0.379 | 0.405 | 0.400 | 41 | 60 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR3 | team_total | 0.652 | 0.675 | 0.670 | 68 | 33 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2 | team_total | 0.716 | 0.695 | 0.699 | 70 | 31 | yes | +0.001 | OK |
| KXNHLSPREAD-26OCT11VANNYR-NYR3 | game_spread | 0.334 | 0.355 | 0.351 | 36 | 65 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT11CARPHI-8 | game_total | 0.209 | 0.225 | 0.222 | 23 | 78 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT11VANNYR-5 | game_total | 0.800 | 0.785 | 0.788 | 79 | 22 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT11VANNYR-NYR | game_winner | 0.698 | 0.715 | 0.712 | 72 | 29 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT11VANNYR-VAN | game_winner | 0.302 | 0.285 | 0.288 | 29 | 72 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR6 | team_total | 0.105 | 0.120 | 0.117 | 13 | 89 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT11VANNYR-3 | game_total | 0.969 | 0.965 | 0.966 | 97 | 4 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT11VANNYR-VAN3 | game_spread | 0.071 | 0.065 | 0.066 | 7 | 94 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT11VANNYR-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR6 | team_total | 0.187 | 0.170 | 0.173 | 18 | 84 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-10 | game_total | 0.060 | 0.065 | 0.064 | 7 | 94 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT11CARPHI-PHI3 | game_spread | 0.098 | 0.105 | 0.104 | 11 | 90 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-3 | game_total | 0.951 | 0.960 | 0.958 | 97 | 5 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6 | team_total | 0.049 | 0.040 | 0.042 | 5 | 97 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5 | team_total | 0.122 | 0.105 | 0.108 | 12 | 91 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR5 | team_total | 0.350 | 0.335 | 0.338 | 34 | 67 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR2 | team_total | 0.901 | 0.890 | 0.892 | 90 | 12 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI5 | team_total | 0.121 | 0.115 | 0.116 | 12 | 89 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI6 | team_total | 0.046 | 0.040 | 0.041 | 5 | 97 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN4 | team_total | 0.265 | 0.255 | 0.257 | 26 | 75 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR4 | team_total | 0.559 | 0.545 | 0.548 | 55 | 46 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT11VANNYR-4 | game_total | 0.877 | 0.870 | 0.872 | 88 | 14 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-9 | game_total | 0.142 | 0.150 | 0.148 | 16 | 86 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT11VANNYR-NYR2 | game_spread | 0.482 | 0.495 | 0.492 | 50 | 51 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI4 | team_total | 0.263 | 0.255 | 0.257 | 26 | 75 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT11VANNYR-VAN2 | game_spread | 0.138 | 0.135 | 0.136 | 14 | 87 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI2 | team_total | 0.713 | 0.705 | 0.707 | 71 | 30 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR3 | team_total | 0.754 | 0.755 | 0.755 | 76 | 25 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI3 | team_total | 0.469 | 0.460 | 0.462 | 47 | 55 |  | -0.018 | NO_EDGE |
| KXNHL1P-26OCT11VANNYR-NYR | period_winner |  | 0.450 |  | 46 | 56 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT11VANNYR-TIE | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT11VANNYR-VAN | period_winner |  | 0.230 |  | 24 | 78 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT11VANNYR-NYR2 | period_spread |  | 0.155 |  | 17 | 86 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT11VANNYR-VAN2 | period_spread |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT11VANNYR-1 | period_total |  | 0.850 |  | 87 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT11VANNYR-2 | period_total |  | 0.555 |  | 57 | 46 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT11VANNYR-3 | period_total |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT11VANNYR-NYR | period_winner |  | 0.470 |  | 48 | 54 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT11VANNYR-TIE | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT11VANNYR-VAN | period_winner |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT11VANNYR-NYR2 | period_spread |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT11VANNYR-VAN2 | period_spread |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT11VANNYR-1 | period_total |  | 0.895 |  | 92 | 13 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT11VANNYR-2 | period_total |  | 0.615 |  | 62 | 39 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT11VANNYR-3 | period_total |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT11VANNYR-NYR | period_winner |  | 0.510 |  | 52 | 50 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT11VANNYR-TIE | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT11VANNYR-VAN | period_winner |  | 0.230 |  | 24 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT11VANNYR-NYR2 | period_spread |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT11VANNYR-VAN2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT11VANNYR-1 | period_total |  | 0.900 |  | 92 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT11VANNYR-2 | period_total |  | 0.650 |  | 67 | 37 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT11VANNYR-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11VANNYR-NYRAFOX23-1 | player_assists |  | 0.570 |  | 58 | 44 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11VANNYR-NYRAFOX23-2 | player_assists |  | 0.210 |  | 22 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11VANNYR-NYRAFOX23-3 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11VANNYR-NYRALAFRENIERE13-1 | player_assists |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11VANNYR-NYRALAFRENIERE13-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT11VANNYR-NYRETOLVANEN17-1 | player_assists |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VAN @ NYR | 0.698 | 0.614 | 0.152 | 0.207 | 6.43 | 6.22 | 0.988/1.026 | KXNHLSPREAD-26OCT11VANNYR-NYR2 -0.094 |
| CAR @ PHI | 0.378 | 0.478 | 0.178 | 0.227 | 5.82 | 5.88 | 0.992/0.997 | KXNHLGAME-26OCT11CARPHI-CAR -0.100 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Drew O'Connor: 1+ goals YES @ 12c · p 0.182 (adj 0.1653) · $9.76 · thesis VAN:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 61c · p 0.6749 (adj 0.6574) · $20.0 · thesis NYR:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 19c · p 0.2393 (adj 0.2257) · $7.58 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 17c · p 0.2132 (adj 0.2011) · $5.9 · thesis VAN:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 67c · p 0.7507 (adj 0.7293) · $15.0 · thesis CAR:SUPPRESSED
- David Jiricek: 1+ goals NO @ 92c · p 0.953 (adj 0.9435) · $16.67 · thesis PHI:SUPPRESSED
- Nikolaj Ehlers: 1+ goals NO @ 75c · p 0.8066 (adj 0.7912) · $15.0 · thesis CAR:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VAN @ NYR** · priced 152/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 25.36, exp saves 22.27 (sd 6.14), pull risk 0.05
- VAN net: Kevin Lankinen (PROBABLE) exp shots 27.14, exp saves 23.19 (sd 6.53), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Garand: 21+ saves | 0.611 | 0.495 | 50/51 | +0.093 |  |
| Pavel Dorofeyev: 1+ points | 0.496 | 0.600 | 62/42 | +0.067 | STANDARD |
| Pavel Dorofeyev: 2+ points | 0.139 | 0.240 | 26/78 | +0.069 | STANDARD |
| Adam Fox: 1+ points | 0.551 | 0.650 | 67/37 | +0.063 | STANDARD |
| J.T. Miller: 1+ assists | 0.379 | 0.470 | 49/55 | +0.054 | STANDARD |
| Adam Fox: 1+ assists | 0.482 | 0.570 | 58/44 | +0.061 | STANDARD |

**CAR @ PHI** · priced 192/192 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 30.15, exp saves 26.02 (sd 6.92), pull risk 0.055
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.75, exp saves 19.77 (sd 5.63), pull risk 0.049

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ points | 0.470 | 0.640 | 65/37 | +0.144 | STANDARD |
| Sebastian Aho: 1+ assists | 0.297 | 0.465 | 47/54 | +0.146 | STANDARD |
| Joseph Woll: 29+ saves | 0.350 | 0.495 | 52/53 | +0.102 |  |
| Sebastian Aho: 2+ points | 0.141 | 0.280 | 29/73 | +0.115 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.474 | 0.575 | 59/44 | +0.069 | STANDARD |
| Nikolaj Ehlers: 1+ points | 0.446 | 0.540 | 55/47 | +0.067 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
