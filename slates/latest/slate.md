# NHL slate 2026-10-10 — RESEARCH_ONLY

generated 2026-10-10T23:12:09Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 3 · markets on board: 4354 · contracts joined: 702 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 627, 'OK': 30, 'NO_EDGE': 45}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 115, 'game_early_goal': 3, 'first_goal': 107, 'game_winner': 6, 'player_goals': 194, 'game_overtime': 3, 'player_points': 129, 'goalie_saves': 4, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ NYI | 2026-10-10T23:30:00Z | T-10m | 0.494 | 0.506 | 0.191 | 5.46 | 2.70 | 2.75 | 208 (25/183) | CONFIRMED/CONFIRMED |
| ANA @ CGY | 2026-10-11T02:00:00Z | T-90m | 0.477 | 0.523 | 0.179 | 6.32 | 3.09 | 3.23 | 237 (25/212) | CONFIRMED/PROJECTED |
| LAK @ VGK | 2026-10-11T02:00:00Z | T-90m | 0.621 | 0.379 | 0.171 | 6.09 | 3.44 | 2.65 | 257 (25/232) | PROJECTED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB4 | team_total | 0.307 | 0.445 | 0.416 | 45 | 56 | no | +0.116 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB3 | team_total | 0.530 | 0.655 | 0.631 | 66 | 35 | no | +0.104 | OK |
| KXNHLGAME-26OCT10TBNYI-NYI | game_winner | 0.494 | 0.375 | 0.398 | 38 | 63 | yes | +0.097 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB2 | game_spread | 0.274 | 0.385 | 0.361 | 39 | 62 | no | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB2 | team_total | 0.753 | 0.855 | 0.838 | 86 | 15 | no | +0.088 | OK |
| KXNHLGAME-26OCT10TBNYI-TB | game_winner | 0.506 | 0.615 | 0.594 | 62 | 39 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB3 | game_spread | 0.155 | 0.255 | 0.232 | 26 | 75 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB5 | team_total | 0.147 | 0.240 | 0.219 | 25 | 77 | no | +0.071 | OK |
| KXNHLTOTAL-26OCT10TBNYI-5 | game_total | 0.672 | 0.745 | 0.731 | 75 | 26 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT10TBNYI-6 | game_total | 0.432 | 0.505 | 0.490 | 51 | 50 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI2 | game_spread | 0.259 | 0.195 | 0.207 | 20 | 81 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT10TBNYI-7 | game_total | 0.328 | 0.395 | 0.381 | 40 | 61 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT10TBNYI-4 | game_total | 0.775 | 0.835 | 0.824 | 84 | 17 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB6 | team_total | 0.056 | 0.105 | 0.093 | 11 | 90 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT10TBNYI-8 | game_total | 0.165 | 0.215 | 0.204 | 22 | 79 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT10TBNYI-9 | game_total | 0.106 | 0.145 | 0.136 | 15 | 86 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT10TBNYI-3 | game_total | 0.933 | 0.965 | 0.960 | 97 | 4 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI3 | game_spread | 0.145 | 0.115 | 0.121 | 12 | 89 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT10TBNYI-10 | game_total | 0.041 | 0.065 | 0.059 | 7 | 94 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT10ANACGY-5 | game_total | 0.787 | 0.815 | 0.810 | 82 | 19 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT10LAVGK-LA2 | team_total | 0.735 | 0.770 | 0.763 | 78 | 24 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT10LAVGK-LA4 | team_total | 0.284 | 0.315 | 0.309 | 32 | 69 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT10LAVGK-LA3 | game_spread | 0.096 | 0.115 | 0.111 | 12 | 89 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT10ANACGY-7 | game_total | 0.466 | 0.495 | 0.489 | 50 | 51 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT10ANACGY-4 | game_total | 0.866 | 0.885 | 0.881 | 89 | 12 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT10LAVGK-LA2 | game_spread | 0.183 | 0.205 | 0.201 | 21 | 80 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT10ANACGY-ANA3 | game_spread | 0.183 | 0.205 | 0.201 | 21 | 80 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT10ANACGY-CGY3 | game_spread | 0.156 | 0.175 | 0.171 | 18 | 83 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT10LAVGK-5 | game_total | 0.757 | 0.780 | 0.776 | 79 | 23 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-NYI5 | team_total | 0.138 | 0.125 | 0.128 | 13 | 88 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT10TBNYI-2 | game_total | 0.968 | 0.975 | 0.974 | 98 | 3 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10TBNYI-NYI6 | team_total | 0.052 | 0.045 | 0.046 | 5 | 96 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10TBNYI-NYI3 | team_total | 0.516 | 0.495 | 0.499 | 50 | 51 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-LA5 | team_total | 0.134 | 0.150 | 0.147 | 16 | 86 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-4 | game_total | 0.843 | 0.860 | 0.857 | 87 | 15 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-3 | game_total | 0.960 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10TBNYI-NYI2 | team_total | 0.751 | 0.730 | 0.734 | 74 | 28 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT10ANACGY-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT10LAVGK-VGK2 | game_spread | 0.392 | 0.375 | 0.378 | 38 | 63 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-LA6 | team_total | 0.052 | 0.060 | 0.058 | 7 | 95 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT10ANACGY-3 | game_total | 0.967 | 0.965 | 0.965 | 97 | 4 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT10LAVGK-LA | game_winner | 0.379 | 0.395 | 0.392 | 40 | 61 |  | -0.006 | NO_EDGE |
| KXNHLGAME-26OCT10LAVGK-VGK | game_winner | 0.621 | 0.605 | 0.608 | 61 | 40 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-6 | game_total | 0.549 | 0.565 | 0.562 | 57 | 44 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT10ANACGY-9 | game_total | 0.195 | 0.205 | 0.203 | 21 | 80 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10TBNYI-NYI4 | team_total | 0.298 | 0.280 | 0.283 | 29 | 73 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT10ANACGY-8 | game_total | 0.273 | 0.285 | 0.283 | 29 | 72 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-ANA2 | team_total | 0.827 | 0.840 | 0.838 | 85 | 17 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT10ANACGY-6 | game_total | 0.581 | 0.595 | 0.592 | 60 | 41 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-LA3 | team_total | 0.501 | 0.515 | 0.512 | 52 | 49 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-CGY3 | team_total | 0.601 | 0.615 | 0.612 | 62 | 39 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-8 | game_total | 0.245 | 0.255 | 0.253 | 26 | 75 |  | -0.008 | NO_EDGE |
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
| KXNHLTEAMTOTAL-26OCT10ANACGY-CGY6 | team_total | 0.089 | 0.090 | 0.090 | 10 | 92 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26OCT10LAVGK-VGK3 | game_spread | 0.252 | 0.255 | 0.254 | 26 | 75 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26OCT10ANACGY-ANA | game_winner | 0.523 | 0.515 | 0.517 | 52 | 49 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT10LAVGK-9 | game_total | 0.167 | 0.170 | 0.169 | 18 | 84 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-CGY5 | team_total | 0.206 | 0.215 | 0.213 | 23 | 80 |  | -0.017 | NO_EDGE |
| KXNHLSPREAD-26OCT10ANACGY-ANA2 | game_spread | 0.303 | 0.310 | 0.309 | 32 | 70 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10ANACGY-ANA3 | team_total | 0.632 | 0.640 | 0.638 | 65 | 37 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-VGK4 | team_total | 0.461 | 0.465 | 0.464 | 47 | 54 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-VGK5 | team_total | 0.265 | 0.260 | 0.261 | 27 | 75 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-VGK3 | team_total | 0.676 | 0.675 | 0.675 | 68 | 33 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26OCT10ANACGY-CGY | game_winner | 0.477 | 0.475 | 0.475 | 48 | 53 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT10LAVGK-VGK2 | team_total | 0.857 | 0.855 | 0.855 | 87 | 16 |  | -0.021 | NO_EDGE |
| KXNHL1P-26OCT10TBNYI-NYI | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT10TBNYI-TB | period_winner |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT10TBNYI-TIE | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT10TBNYI-NYI2 | period_spread |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT10TBNYI-TB2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ NYI | 0.494 | 0.509 | 0.191 | 0.224 | 5.46 | 5.92 | 0.947/0.946 | KXNHLTOTAL-26OCT10TBNYI-6 +0.077 |
| ANA @ CGY | 0.477 | 0.496 | 0.179 | 0.219 | 6.32 | 6.53 | 1.005/1.035 | KXNHLTOTAL-26OCT10ANACGY-7 +0.044 |
| LAK @ VGK | 0.621 | 0.597 | 0.171 | 0.226 | 6.09 | 5.96 | 1.003/0.993 | KXNHLSPREAD-26OCT10LAVGK-VGK2 -0.034 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- John Carlson: 1+ assists NO @ 53c · p 0.7319 (adj 0.5974) · $20.0 · thesis TBL:SUPPRESSED
- Tampa Bay wins by over 2.5 goals NO @ 75c · p 0.8443 (adj 0.7947) · $20.0 · thesis NYI:WINS
- Jake Guentzel: 1+ goals NO @ 66c · p 0.7008 (adj 0.6894) · $5.11 · thesis TBL:SUPPRESSED
- Aydar Suniev: 1+ goals YES @ 13c · p 0.1953 (adj 0.1765) · $9.89 · thesis CGY:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 16c · p 0.2241 (adj 0.2068) · $10.41 · thesis ANA:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 9c · p 0.1312 (adj 0.1197) · $5.83 · thesis ANA:OFFENSE_4PLUS
- Cutter Gauthier: 1+ goals NO @ 59c · p 0.6342 (adj 0.6219) · $9.37 · thesis ANA:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0806 (adj 0.0717) · $4.12 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 69c · p 0.7523 (adj 0.7355) · $20.0 · thesis VGK:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 50c · p 0.6473 (adj 0.5483) · $17.03 · thesis LAK:SUPPRESSED
- Trevor Moore: 1+ assists YES @ 23c · p 0.3076 (adj 0.2613) · $5.86 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TBL @ NYI** · priced 153/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 27.33, exp saves 23.71 (sd 6.49), pull risk 0.052
- TBL net: Andrei Vasilevskiy (CONFIRMED) exp shots 26.5, exp saves 22.84 (sd 6.24), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.356 | 0.565 | 57/44 | +0.187 | STANDARD |
| John Carlson: 1+ assists | 0.268 | 0.475 | 48/53 | +0.184 | STANDARD |
| John Carlson: 2+ points | 0.072 | 0.210 | 22/80 | +0.117 | STANDARD |
| John Carlson: 2+ assists | 0.038 | 0.150 | 17/87 | +0.084 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.474 | 0.585 | 59/42 | +0.089 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.197 | 0.305 | 32/71 | +0.079 | STANDARD |

**ANA @ CGY** · priced 182/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 30.92, exp saves 26.73 (sd 7.25), pull risk 0.067
- ANA net: Ville Husso (PROJECTED) exp shots 26.97, exp saves 23.27 (sd 6.52), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Whitecloud: 1+ assists | 0.268 | 0.140 | 16/88 | +0.099 | STANDARD |
| Noah Warren: 1+ assists | 0.202 | 0.080 | 14/98 | +0.053 | PRIOR_HEAVY |
| Adam Klapka: 1+ assists | 0.247 | 0.130 | 20/94 | +0.036 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.330 | 0.220 | 24/80 | +0.077 | STANDARD |
| Leo Carlsson: 1+ assists | 0.389 | 0.495 | 50/51 | +0.083 | STANDARD |
| Dustin Wolf: 26+ saves | 0.568 | 0.470 | 50/56 | +0.051 |  |

**LAK @ VGK** · priced 202/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.29, exp saves 23.03 (sd 6.3), pull risk 0.046
- LAK net: Darcy Kuemper (PROBABLE) exp shots 28.34, exp saves 24.25 (sd 6.62), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.353 | 0.505 | 51/50 | +0.130 | STANDARD |
| Joel Edmundson: 1+ assists | 0.220 | 0.085 | 15/98 | +0.061 | STANDARD |
| Mikey Anderson: 1+ assists | 0.218 | 0.085 | 15/98 | +0.059 | STANDARD |
| Joel Edmundson: 1+ points | 0.270 | 0.140 | 18/90 | +0.079 | STANDARD |
| Mitch Marner: 1+ assists | 0.411 | 0.540 | 55/47 | +0.102 | STANDARD |
| Artemi Panarin: 2+ points | 0.177 | 0.305 | 32/71 | +0.098 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
