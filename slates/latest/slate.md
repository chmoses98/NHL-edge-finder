# NHL slate 2026-10-10 — RESEARCH_ONLY

generated 2026-10-11T00:03:13Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 2 · markets on board: 4044 · contracts joined: 494 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 444, 'NO_EDGE': 41, 'OK': 9}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 92, 'game_early_goal': 2, 'first_goal': 71, 'game_winner': 4, 'player_goals': 132, 'game_overtime': 2, 'player_points': 95, 'goalie_saves': 2, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ CGY | 2026-10-11T02:00:00Z | T-90m | 0.477 | 0.523 | 0.179 | 6.32 | 3.09 | 3.23 | 237 (25/212) | CONFIRMED/PROJECTED |
| LAK @ VGK | 2026-10-11T02:00:00Z | T-90m | 0.621 | 0.379 | 0.171 | 6.09 | 3.44 | 2.65 | 257 (25/232) | PROJECTED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT10ANACGY-5 | game_total | 0.787 | 0.815 | 0.810 | 82 | 19 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT10LAVGK-LA2 | team_total | 0.735 | 0.770 | 0.763 | 78 | 24 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT10LAVGK-LA4 | team_total | 0.284 | 0.320 | 0.313 | 33 | 69 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT10LAVGK-LA3 | game_spread | 0.096 | 0.115 | 0.111 | 12 | 89 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT10ANACGY-4 | game_total | 0.866 | 0.885 | 0.881 | 89 | 12 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT10LAVGK-LA2 | game_spread | 0.183 | 0.205 | 0.201 | 21 | 80 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT10ANACGY-ANA3 | game_spread | 0.183 | 0.205 | 0.201 | 21 | 80 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT10ANACGY-CGY3 | game_spread | 0.156 | 0.175 | 0.171 | 18 | 83 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT10LAVGK-5 | game_total | 0.757 | 0.780 | 0.776 | 79 | 23 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT10LAVGK-LA5 | team_total | 0.134 | 0.150 | 0.147 | 16 | 86 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-4 | game_total | 0.843 | 0.860 | 0.857 | 87 | 15 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-3 | game_total | 0.960 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT10ANACGY-7 | game_total | 0.466 | 0.485 | 0.481 | 49 | 52 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT10ANACGY-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT10LAVGK-VGK2 | game_spread | 0.392 | 0.375 | 0.378 | 38 | 63 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-LA6 | team_total | 0.052 | 0.060 | 0.058 | 7 | 95 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-CGY6 | team_total | 0.089 | 0.095 | 0.094 | 10 | 91 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT10ANACGY-3 | game_total | 0.967 | 0.965 | 0.965 | 97 | 4 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT10LAVGK-VGK | game_winner | 0.621 | 0.605 | 0.608 | 61 | 40 |  | -0.006 | NO_EDGE |
| KXNHLGAME-26OCT10LAVGK-LA | game_winner | 0.379 | 0.395 | 0.392 | 40 | 61 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-6 | game_total | 0.549 | 0.565 | 0.562 | 57 | 44 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT10ANACGY-9 | game_total | 0.195 | 0.205 | 0.203 | 21 | 80 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-ANA2 | team_total | 0.827 | 0.840 | 0.838 | 85 | 17 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT10ANACGY-ANA2 | game_spread | 0.303 | 0.315 | 0.313 | 32 | 69 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-CGY5 | team_total | 0.206 | 0.215 | 0.213 | 22 | 79 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT10ANACGY-6 | game_total | 0.581 | 0.595 | 0.592 | 60 | 41 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-LA3 | team_total | 0.501 | 0.515 | 0.512 | 52 | 49 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-CGY3 | team_total | 0.601 | 0.615 | 0.612 | 62 | 39 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-8 | game_total | 0.245 | 0.255 | 0.253 | 26 | 75 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-ANA3 | team_total | 0.632 | 0.650 | 0.646 | 66 | 36 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-VGK6 | team_total | 0.130 | 0.120 | 0.122 | 13 | 89 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT10ANACGY-10 | game_total | 0.093 | 0.100 | 0.098 | 11 | 91 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-ANA5 | team_total | 0.226 | 0.240 | 0.237 | 25 | 77 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-CGY2 | team_total | 0.808 | 0.820 | 0.818 | 83 | 19 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-ANA6 | team_total | 0.103 | 0.105 | 0.105 | 11 | 90 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT10ANACGY-CGY2 | game_spread | 0.266 | 0.275 | 0.273 | 28 | 73 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-7 | game_total | 0.434 | 0.445 | 0.443 | 45 | 56 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-10 | game_total | 0.076 | 0.080 | 0.079 | 9 | 93 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-CGY4 | team_total | 0.386 | 0.395 | 0.393 | 40 | 61 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-ANA4 | team_total | 0.417 | 0.425 | 0.423 | 43 | 58 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT10LAVGK-VGK3 | game_spread | 0.252 | 0.255 | 0.254 | 26 | 75 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26OCT10ANACGY-ANA | game_winner | 0.523 | 0.515 | 0.517 | 52 | 49 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-9 | game_total | 0.167 | 0.170 | 0.169 | 18 | 84 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT10ANACGY-8 | game_total | 0.273 | 0.275 | 0.275 | 28 | 73 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-VGK4 | team_total | 0.461 | 0.465 | 0.464 | 47 | 54 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-VGK5 | team_total | 0.265 | 0.260 | 0.261 | 27 | 75 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-VGK3 | team_total | 0.676 | 0.675 | 0.675 | 68 | 33 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26OCT10ANACGY-CGY | game_winner | 0.477 | 0.475 | 0.475 | 48 | 53 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-VGK2 | team_total | 0.857 | 0.855 | 0.855 | 87 | 16 |  | -0.021 | NO_EDGE |
| KXNHL1P-26OCT10ANACGY-TIE | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT10ANACGY-CGY | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT10ANACGY-ANA | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT10ANACGY-CGY2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT10ANACGY-ANA2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT10ANACGY-3 | period_total |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT10ANACGY-2 | period_total |  | 0.550 |  | 56 | 46 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT10ANACGY-1 | period_total |  | 0.845 |  | 85 | 16 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT10ANACGY-TIE | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT10ANACGY-CGY | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT10ANACGY-ANA | period_winner |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT10ANACGY-CGY2 | period_spread |  | 0.110 |  | 13 | 91 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT10ANACGY-ANA2 | period_spread |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT10ANACGY-3 | period_total |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT10ANACGY-2 | period_total |  | 0.630 |  | 64 | 38 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT10ANACGY-1 | period_total |  | 0.900 |  | 92 | 12 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT10ANACGY-TIE | period_winner |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT10ANACGY-CGY | period_winner |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT10ANACGY-ANA | period_winner |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT10ANACGY-CGY2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT10ANACGY-ANA2 | period_spread |  | 0.160 |  | 18 | 86 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT10ANACGY-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT10ANACGY-2 | period_total |  | 0.665 |  | 67 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT10ANACGY-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT10ANACGY-CGYZWHITECLOUD28-1 | player_assists |  | 0.140 |  | 16 | 88 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT10ANACGY-CGYYSHARANGOVICH17-1 | player_assists |  | 0.220 |  | 24 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT10ANACGY-CGYYKUZNETSOV37-1 | player_assists |  | 0.140 |  | 18 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT10ANACGY-ANATHINDS55-1 | player_assists |  | 0.080 |  | 14 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT10ANACGY-ANATLUNEAU67-1 | player_assists |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT10ANACGY-ANATMITCHELL34-1 | player_assists |  | 0.085 |  | 15 | 98 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ CGY | 0.477 | 0.496 | 0.179 | 0.219 | 6.32 | 6.53 | 1.005/1.035 | KXNHLTOTAL-26OCT10ANACGY-7 +0.044 |
| LAK @ VGK | 0.621 | 0.597 | 0.171 | 0.226 | 6.09 | 5.96 | 1.003/0.993 | KXNHLSPREAD-26OCT10LAVGK-VGK2 -0.034 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Aydar Suniev: 1+ goals YES @ 13c · p 0.1953 (adj 0.1715) · $8.54 · thesis CGY:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 16c · p 0.2241 (adj 0.2056) · $10.06 · thesis ANA:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 10c · p 0.1312 (adj 0.1209) · $3.71 · thesis ANA:OFFENSE_4PLUS
- Martin Pospisil: 1+ goals YES @ 10c · p 0.1285 (adj 0.1201) · $3.83 · thesis CGY:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0806 (adj 0.0717) · $4.11 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 69c · p 0.7523 (adj 0.7355) · $20.0 · thesis VGK:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 49c · p 0.6473 (adj 0.5386) · $16.83 · thesis LAK:SUPPRESSED
- Trevor Moore: 1+ assists YES @ 23c · p 0.3076 (adj 0.2613) · $5.86 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ CGY** · priced 182/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 30.92, exp saves 26.73 (sd 7.25), pull risk 0.067
- ANA net: Ville Husso (PROJECTED) exp shots 26.97, exp saves 23.27 (sd 6.52), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Whitecloud: 1+ assists | 0.268 | 0.140 | 16/88 | +0.099 | STANDARD |
| Adam Klapka: 1+ assists | 0.247 | 0.120 | 20/96 | +0.036 | STANDARD |
| Noah Warren: 1+ assists | 0.202 | 0.085 | 15/98 | +0.043 | PRIOR_HEAVY |
| Yegor Sharangovich: 1+ assists | 0.330 | 0.220 | 24/80 | +0.077 | STANDARD |
| Leo Carlsson: 1+ assists | 0.389 | 0.495 | 50/51 | +0.083 | STANDARD |
| Dustin Wolf: 26+ saves | 0.568 | 0.470 | 50/56 | +0.051 |  |

**LAK @ VGK** · priced 202/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.29, exp saves 23.03 (sd 6.3), pull risk 0.046
- LAK net: Darcy Kuemper (PROBABLE) exp shots 28.34, exp saves 24.25 (sd 6.62), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.353 | 0.520 | 53/49 | +0.140 | STANDARD |
| Joel Edmundson: 1+ assists | 0.220 | 0.080 | 14/98 | +0.072 | STANDARD |
| Joel Edmundson: 1+ points | 0.270 | 0.130 | 16/90 | +0.100 | STANDARD |
| Mitch Marner: 1+ assists | 0.411 | 0.545 | 55/46 | +0.112 | STANDARD |
| Mikey Anderson: 1+ assists | 0.218 | 0.085 | 15/98 | +0.059 | STANDARD |
| Artemi Panarin: 2+ points | 0.177 | 0.305 | 32/71 | +0.098 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
