# NHL slate 2026-11-13 — RESEARCH_ONLY

generated 2026-11-14T01:53:47Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2610 · contracts joined: 446 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 396, 'OK': 24, 'NO_EDGE': 26}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 60, 'game_early_goal': 2, 'first_goal': 72, 'game_winner': 4, 'player_goals': 125, 'game_overtime': 2, 'player_points': 83, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ VAN | 2026-11-14T02:00:00Z | T-<10m | 0.419 | 0.581 | 0.172 | 6.53 | 3.01 | 3.52 | 220 (25/195) | PROJECTED/PROJECTED |
| NSH @ VGK | 2026-11-14T03:00:00Z | T-60m | 0.597 | 0.403 | 0.169 | 6.39 | 3.51 | 2.88 | 226 (25/201) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV13NYRVAN-NYR3 | game_spread | 0.233 | 0.315 | 0.297 | 32 | 69 | no | +0.062 | OK |
| KXNHLSPREAD-26NOV13NYRVAN-NYR2 | game_spread | 0.364 | 0.445 | 0.428 | 45 | 56 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26NOV13NYRVAN-VAN4 | team_total | 0.368 | 0.295 | 0.309 | 30 | 71 | yes | +0.054 | OK |
| KXNHLGAME-26NOV13NYRVAN-NYR | game_winner | 0.581 | 0.655 | 0.641 | 66 | 35 | no | +0.053 | OK |
| KXNHLGAME-26NOV13NYRVAN-VAN | game_winner | 0.419 | 0.345 | 0.359 | 35 | 66 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV13NYRVAN-VAN3 | team_total | 0.578 | 0.505 | 0.520 | 51 | 50 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV13NYRVAN-VAN5 | team_total | 0.195 | 0.130 | 0.141 | 14 | 88 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4 | team_total | 0.483 | 0.545 | 0.533 | 55 | 46 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV13NYRVAN-VAN2 | game_spread | 0.228 | 0.175 | 0.185 | 18 | 83 | yes | +0.037 | OK |
| KXNHLSPREAD-26NOV13NYRVAN-VAN3 | game_spread | 0.131 | 0.085 | 0.093 | 9 | 92 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR2 | team_total | 0.860 | 0.910 | 0.902 | 92 | 10 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV13NYRVAN-VAN2 | team_total | 0.790 | 0.745 | 0.755 | 75 | 26 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV13NSHVGK-10 | game_total | 0.100 | 0.065 | 0.071 | 7 | 94 | yes | +0.025 | OK |
| KXNHLTOTAL-26NOV13NSHVGK-9 | game_total | 0.204 | 0.165 | 0.172 | 17 | 84 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR3 | team_total | 0.693 | 0.735 | 0.727 | 74 | 27 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV13NYRVAN-VAN6 | team_total | 0.087 | 0.055 | 0.060 | 6 | 95 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV13NSHVGK-8 | game_total | 0.285 | 0.245 | 0.253 | 25 | 76 | yes | +0.022 | OK |
| KXNHLTOTAL-26NOV13NYRVAN-10 | game_total | 0.111 | 0.085 | 0.090 | 9 | 92 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV13NYRVAN-8 | game_total | 0.309 | 0.275 | 0.282 | 28 | 73 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR5 | team_total | 0.284 | 0.315 | 0.309 | 32 | 69 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-VGK6 | team_total | 0.138 | 0.110 | 0.115 | 12 | 90 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV13NSHVGK-7 | game_total | 0.477 | 0.445 | 0.451 | 45 | 56 | yes | +0.009 | OK |
| KXNHLTOTAL-26NOV13NSHVGK-6 | game_total | 0.593 | 0.565 | 0.571 | 57 | 44 | yes | +0.006 | OK |
| KXNHLTOTAL-26NOV13NYRVAN-9 | game_total | 0.222 | 0.200 | 0.204 | 21 | 81 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-VGK5 | team_total | 0.283 | 0.260 | 0.265 | 27 | 75 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-NSH5 | team_total | 0.168 | 0.145 | 0.149 | 16 | 87 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-NSH6 | team_total | 0.073 | 0.065 | 0.067 | 7 | 94 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV13NYRVAN-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV13NSHVGK-3 | game_total | 0.970 | 0.975 | 0.974 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV13NYRVAN-3 | game_total | 0.971 | 0.975 | 0.974 | 98 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV13NSHVGK-4 | game_total | 0.874 | 0.865 | 0.867 | 87 | 14 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV13NSHVGK-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-NSH3 | team_total | 0.553 | 0.530 | 0.535 | 54 | 48 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV13NSHVGK-NSH3 | game_spread | 0.117 | 0.125 | 0.123 | 13 | 88 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV13NYRVAN-7 | game_total | 0.503 | 0.485 | 0.489 | 49 | 52 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV13NYRVAN-5 | game_total | 0.804 | 0.815 | 0.813 | 82 | 19 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV13NSHVGK-5 | game_total | 0.795 | 0.785 | 0.787 | 79 | 22 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-VGK3 | team_total | 0.688 | 0.670 | 0.674 | 68 | 34 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV13NYRVAN-4 | game_total | 0.880 | 0.885 | 0.884 | 89 | 12 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26NOV13NSHVGK-VGK3 | game_spread | 0.244 | 0.255 | 0.253 | 26 | 75 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-VGK4 | team_total | 0.480 | 0.465 | 0.468 | 47 | 54 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-NSH2 | team_total | 0.774 | 0.760 | 0.763 | 77 | 25 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-VGK2 | team_total | 0.860 | 0.870 | 0.868 | 88 | 14 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-NSH4 | team_total | 0.337 | 0.320 | 0.323 | 33 | 69 |  | -0.009 | NO_EDGE |
| KXNHLGAME-26NOV13NSHVGK-VGK | game_winner | 0.597 | 0.585 | 0.587 | 59 | 42 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26NOV13NSHVGK-NSH2 | game_spread | 0.209 | 0.215 | 0.214 | 22 | 79 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR6 | team_total | 0.142 | 0.150 | 0.148 | 16 | 86 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV13NYRVAN-6 | game_total | 0.614 | 0.605 | 0.607 | 61 | 40 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV13NSHVGK-VGK2 | game_spread | 0.378 | 0.375 | 0.376 | 38 | 63 |  | -0.018 | NO_EDGE |
| KXNHLGAME-26NOV13NSHVGK-NSH | game_winner | 0.403 | 0.405 | 0.405 | 41 | 60 |  | -0.020 | NO_EDGE |
| KXNHL1P-26NOV13NYRVAN-NYR | period_winner |  | 0.415 |  | 42 | 59 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV13NYRVAN-TIE | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV13NYRVAN-VAN | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV13NYRVAN-NYR2 | period_spread |  | 0.155 |  | 16 | 85 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV13NYRVAN-VAN2 | period_spread |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV13NYRVAN-1 | period_total |  | 0.850 |  | 86 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV13NYRVAN-2 | period_total |  | 0.580 |  | 59 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV13NYRVAN-3 | period_total |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV13NYRVAN-NYR | period_winner |  | 0.435 |  | 44 | 57 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV13NYRVAN-TIE | period_winner |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV13NYRVAN-VAN | period_winner |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV13NYRVAN-NYR2 | period_spread |  | 0.170 |  | 18 | 84 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV13NYRVAN-VAN2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV13NYRVAN-1 | period_total |  | 0.900 |  | 92 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV13NYRVAN-2 | period_total |  | 0.625 |  | 63 | 38 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV13NYRVAN-3 | period_total |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV13NYRVAN-NYR | period_winner |  | 0.470 |  | 48 | 54 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV13NYRVAN-TIE | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV13NYRVAN-VAN | period_winner |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV13NYRVAN-NYR2 | period_spread |  | 0.220 |  | 24 | 80 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV13NYRVAN-VAN2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV13NYRVAN-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV13NYRVAN-2 | period_total |  | 0.675 |  | 69 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV13NYRVAN-3 | period_total |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NYRVAN-NYRAFOX23-1 | player_assists |  | 0.625 |  | 63 | 38 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NYRVAN-NYRAFOX23-2 | player_assists |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NYRVAN-NYRAFOX23-3 | player_assists |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NYRVAN-NYRALAFRENIERE13-1 | player_assists |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NYRVAN-NYRALAFRENIERE13-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NYRVAN-NYRGPERREAULT94-1 | player_assists |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ VAN | 0.419 | 0.495 | 0.172 | 0.218 | 6.53 | 6.30 | 1.026/0.992 | KXNHLTEAMTOTAL-26NOV13NYRVAN-NYR4 -0.085 |
| NSH @ VGK | 0.597 | 0.617 | 0.169 | 0.206 | 6.39 | 6.35 | 1.003/1.000 | KXNHLSPREAD-26NOV13NSHVGK-VGK3 +0.024 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Linus Karlsson: 1+ goals YES @ 16c · p 0.239 (adj 0.218) · $12.51 · thesis VAN:OFFENSE_4PLUS
- New York R wins by over 1.5 goals NO @ 56c · p 0.722 (adj 0.6134) · $16.78 · thesis VAN:WINS
- Gabe Perreault: 1+ goals NO @ 71c · p 0.7641 (adj 0.7493) · $19.11 · thesis NYR:SUPPRESSED
- Braeden Bowman: 1+ goals YES @ 13c · p 0.1735 (adj 0.1614) · $6.26 · thesis VGK:OFFENSE_4PLUS
- Brett Howden: 1+ goals YES @ 18c · p 0.2237 (adj 0.2115) · $6.21 · thesis VGK:OFFENSE_4PLUS
- Ivan Barbashev: 1+ goals YES @ 21c · p 0.2554 (adj 0.2428) · $6.69 · thesis VGK:OFFENSE_4PLUS
- Victor Olofsson: 1+ goals NO @ 74c · p 0.7803 (adj 0.769) · $16.01 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYR @ VAN** · priced 159/169 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- VAN net: Leevi Merilainen (PROJECTED) exp shots 27.19, exp saves 23.59 (sd 6.55), pull risk 0.065
- NYR net: Joonas Korpisalo (PROJECTED) exp shots 25.7, exp saves 22.2 (sd 6.13), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pavel Dorofeyev: 1+ points | 0.455 | 0.590 | 60/42 | +0.108 | STANDARD |
| Pavel Dorofeyev: 1+ goals | 0.272 | 0.385 | 39/62 | +0.091 | STANDARD |
| Adam Fox: 1+ assists | 0.516 | 0.625 | 63/38 | +0.088 | STANDARD |
| Adam Fox: 2+ points | 0.215 | 0.320 | 34/70 | +0.070 | STANDARD |
| J.T. Miller: 1+ assists | 0.351 | 0.450 | 46/56 | +0.072 | STANDARD |
| Adam Fox: 1+ points | 0.578 | 0.675 | 68/33 | +0.076 | STANDARD |

**NSH @ VGK** · priced 174/175 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- VGK net: Carter Hart (PROJECTED) exp shots 25.55, exp saves 22.46 (sd 6.11), pull risk 0.048
- NSH net: Juuse Saros (PROJECTED) exp shots 29.76, exp saves 25.38 (sd 7.02), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivan Barbashev: 1+ points | 0.539 | 0.440 | 45/57 | +0.072 | STANDARD |
| Ivan Barbashev: 1+ assists | 0.386 | 0.290 | 30/72 | +0.071 | STANDARD |
| Jack Eichel: 2+ points | 0.262 | 0.355 | 36/65 | +0.072 | STANDARD |
| Jack Eichel: 1+ assists | 0.474 | 0.560 | 57/45 | +0.058 | STANDARD |
| Victor Olofsson: 1+ assists | 0.232 | 0.315 | 32/69 | +0.063 | STANDARD |
| Jack Eichel: 1+ points | 0.636 | 0.715 | 72/29 | +0.059 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
