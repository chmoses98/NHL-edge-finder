# NHL slate 2026-11-08 — RESEARCH_ONLY

generated 2026-11-09T00:12:54Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 1 · markets on board: 2458 · contracts joined: 230 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 205, 'OK': 20, 'NO_EDGE': 5}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 32, 'game_early_goal': 1, 'first_goal': 37, 'game_winner': 2, 'player_goals': 68, 'game_overtime': 1, 'player_points': 41, 'goalie_saves': 1, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ ANA | 2026-11-09T01:00:00Z | T-30m | 0.615 | 0.385 | 0.153 | 7.29 | 4.04 | 3.24 | 230 (25/205) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV08PITANA-ANA2 | game_spread | 0.418 | 0.315 | 0.335 | 32 | 69 | yes | +0.083 | OK |
| KXNHLGAME-26NOV08PITANA-ANA | game_winner | 0.615 | 0.525 | 0.543 | 53 | 48 | yes | +0.068 | OK |
| KXNHLGAME-26NOV08PITANA-PIT | game_winner | 0.385 | 0.475 | 0.457 | 48 | 53 | no | +0.068 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT2 | game_spread | 0.210 | 0.295 | 0.277 | 30 | 71 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA5 | team_total | 0.394 | 0.315 | 0.330 | 32 | 69 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA6 | team_total | 0.222 | 0.145 | 0.158 | 16 | 87 | yes | +0.053 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA3 | game_spread | 0.284 | 0.210 | 0.224 | 22 | 80 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA4 | team_total | 0.589 | 0.515 | 0.530 | 52 | 49 | yes | +0.051 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT3 | game_spread | 0.125 | 0.185 | 0.172 | 19 | 82 | no | +0.044 | OK |
| KXNHLTOTAL-26NOV08PITANA-8 | game_total | 0.417 | 0.365 | 0.375 | 37 | 64 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA3 | team_total | 0.769 | 0.715 | 0.726 | 73 | 30 | yes | +0.026 | OK |
| KXNHLTOTAL-26NOV08PITANA-9 | game_total | 0.319 | 0.275 | 0.284 | 28 | 73 | yes | +0.025 | OK |
| KXNHLTOTAL-26NOV08PITANA-10 | game_total | 0.182 | 0.140 | 0.148 | 15 | 87 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT3 | team_total | 0.623 | 0.665 | 0.657 | 67 | 34 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT2 | team_total | 0.825 | 0.860 | 0.854 | 87 | 15 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT4 | team_total | 0.417 | 0.455 | 0.447 | 46 | 55 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA2 | team_total | 0.905 | 0.880 | 0.886 | 89 | 13 | yes | +0.009 | OK |
| KXNHLTOTAL-26NOV08PITANA-6 | game_total | 0.723 | 0.695 | 0.701 | 70 | 31 | yes | +0.009 | OK |
| KXNHLTOTAL-26NOV08PITANA-7 | game_total | 0.615 | 0.585 | 0.591 | 59 | 42 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV08PITANA-2 | game_total | 0.994 | 0.985 | 0.988 | 99 | 2 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT5 | team_total | 0.238 | 0.260 | 0.255 | 27 | 75 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV08PITANA-5 | game_total | 0.875 | 0.865 | 0.867 | 87 | 14 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV08PITANA-3 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV08PITANA-4 | game_total | 0.928 | 0.925 | 0.926 | 93 | 8 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT6 | team_total | 0.114 | 0.120 | 0.119 | 13 | 89 |  | -0.011 | NO_EDGE |
| KXNHL1P-26NOV08PITANA-ANA | period_winner |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV08PITANA-PIT | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV08PITANA-TIE | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV08PITANA-ANA2 | period_spread |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV08PITANA-PIT2 | period_spread |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV08PITANA-1 | period_total |  | 0.870 |  | 88 | 14 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV08PITANA-2 | period_total |  | 0.625 |  | 63 | 38 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV08PITANA-3 | period_total |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV08PITANA-ANA | period_winner |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV08PITANA-PIT | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV08PITANA-TIE | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV08PITANA-ANA2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV08PITANA-PIT2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV08PITANA-1 | period_total |  | 0.925 |  | 95 | 10 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV08PITANA-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV08PITANA-3 | period_total |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV08PITANA-ANA | period_winner |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV08PITANA-PIT | period_winner |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV08PITANA-TIE | period_winner |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV08PITANA-ANA2 | period_spread |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV08PITANA-PIT2 | period_spread |  | 0.155 |  | 17 | 86 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV08PITANA-1 | period_total |  | 0.935 |  | 96 | 9 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV08PITANA-2 | period_total |  | 0.735 |  | 76 | 29 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV08PITANA-3 | period_total |  | 0.460 |  | 47 | 55 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAAKILLORN17-1 | player_assists |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAAKILLORN17-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANABSENNECKE45-1 | player_assists |  | 0.470 |  | 48 | 54 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANABSENNECKE45-2 | player_assists |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANACGAUTHIER61-1 | player_assists |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANACGAUTHIER61-2 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAJCAULFIELD28-1 | player_assists |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAJLACOMBE2-1 | player_assists |  | 0.550 |  | 56 | 46 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAJLACOMBE2-2 | player_assists |  | 0.190 |  | 20 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAJLACOMBE2-3 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANALCARLSSON91-1 | player_assists |  | 0.520 |  | 53 | 49 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANALCARLSSON91-2 | player_assists |  | 0.170 |  | 18 | 84 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAMGRANLUND64-1 | player_assists |  | 0.475 |  | 49 | 54 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAMGRANLUND64-2 | player_assists |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANATLUNEAU67-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANATLUNEAU67-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITBKINDEL81-1 | player_assists |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITBKINDEL81-2 | player_assists |  | 0.065 |  | 7 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITECHINAKHOV59-1 | player_assists |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITEKARLSSON65-1 | player_assists |  | 0.500 |  | 51 | 51 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITEKARLSSON65-2 | player_assists |  | 0.160 |  | 18 | 86 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITEKARLSSON65-3 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITEMALKIN71-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITEMALKIN71-2 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITKLETANG58-1 | player_assists |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITKLETANG58-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITRRAKELL67-1 | player_assists |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITRRAKELL67-2 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITSCROSBY87-1 | player_assists |  | 0.455 |  | 47 | 56 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITSCROSBY87-2 | player_assists |  | 0.120 |  | 14 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITTNOVAK18-1 | player_assists |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ ANA | 0.615 | 0.641 | 0.153 | 0.194 | 7.29 | 7.18 | 0.986/1.042 | KXNHLTEAMTOTAL-26NOV08PITANA-PIT4 -0.030 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Jeff Malott: 1+ goals YES @ 11c · p 0.1563 (adj 0.1435) · $6.83 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 19c · p 0.2442 (adj 0.2281) · $8.04 · thesis ANA:OFFENSE_4PLUS
- Beckett Sennecke: 1+ goals YES @ 35c · p 0.4006 (adj 0.3867) · $8.29 · thesis ANA:OFFENSE_4PLUS
- Sam Colangelo: 1+ goals YES @ 14c · p 0.1729 (adj 0.1634) · $4.25 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ ANA** · priced 175/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (PROJECTED) exp shots 26.45, exp saves 23.06 (sd 6.45), pull risk 0.063
- PIT net: Arturs Silovs (CONFIRMED) exp shots 28.23, exp saves 23.71 (sd 6.93), pull risk 0.106

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Erik Karlsson: 1+ points | 0.510 | 0.595 | 61/42 | +0.053 | STANDARD |
| Sidney Crosby: 1+ assists | 0.371 | 0.455 | 47/56 | +0.052 | STANDARD |
| Ben Kindel: 1+ points | 0.419 | 0.500 | 51/51 | +0.053 | STANDARD |
| Alex Killorn: 1+ points | 0.484 | 0.405 | 41/60 | +0.057 | STANDARD |
| Erik Karlsson: 1+ assists | 0.430 | 0.500 | 51/51 | +0.042 | STANDARD |
| Alex Killorn: 1+ goals | 0.244 | 0.180 | 19/83 | +0.043 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
