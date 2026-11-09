# NHL slate 2026-11-08 — RESEARCH_ONLY

generated 2026-11-09T00:39:06Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 1 · markets on board: 2469 · contracts joined: 230 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 205, 'OK': 21, 'NO_EDGE': 4}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 32, 'game_early_goal': 1, 'first_goal': 37, 'game_winner': 2, 'player_goals': 68, 'game_overtime': 1, 'player_points': 41, 'goalie_saves': 1, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ ANA | 2026-11-09T01:00:00Z | T-10m | 0.605 | 0.395 | 0.154 | 7.33 | 4.04 | 3.30 | 230 (25/205) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV08PITANA-ANA2 | game_spread | 0.404 | 0.315 | 0.332 | 32 | 69 | yes | +0.069 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA6 | team_total | 0.220 | 0.145 | 0.158 | 15 | 86 | yes | +0.061 | OK |
| KXNHLGAME-26NOV08PITANA-ANA | game_winner | 0.605 | 0.525 | 0.541 | 53 | 48 | yes | +0.058 | OK |
| KXNHLGAME-26NOV08PITANA-PIT | game_winner | 0.395 | 0.475 | 0.459 | 48 | 53 | no | +0.058 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT2 | game_spread | 0.218 | 0.295 | 0.278 | 30 | 71 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA5 | team_total | 0.391 | 0.315 | 0.330 | 32 | 69 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA4 | team_total | 0.590 | 0.515 | 0.530 | 52 | 49 | yes | +0.053 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA3 | game_spread | 0.275 | 0.215 | 0.226 | 22 | 79 | yes | +0.043 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT3 | game_spread | 0.129 | 0.185 | 0.172 | 19 | 82 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA3 | team_total | 0.769 | 0.710 | 0.722 | 72 | 30 | yes | +0.035 | OK |
| KXNHLTOTAL-26NOV08PITANA-8 | game_total | 0.434 | 0.385 | 0.395 | 39 | 62 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV08PITANA-9 | game_total | 0.329 | 0.285 | 0.294 | 29 | 72 | yes | +0.025 | OK |
| KXNHLTOTAL-26NOV08PITANA-10 | game_total | 0.186 | 0.150 | 0.157 | 16 | 86 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV08PITANA-6 | game_total | 0.728 | 0.695 | 0.702 | 70 | 31 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV08PITANA-7 | game_total | 0.626 | 0.590 | 0.597 | 60 | 42 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA2 | team_total | 0.906 | 0.880 | 0.886 | 89 | 13 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT2 | team_total | 0.832 | 0.860 | 0.855 | 87 | 15 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT4 | team_total | 0.426 | 0.455 | 0.449 | 46 | 55 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT3 | team_total | 0.640 | 0.665 | 0.660 | 67 | 34 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV08PITANA-2 | game_total | 0.994 | 0.985 | 0.988 | 99 | 2 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT5 | team_total | 0.245 | 0.265 | 0.261 | 27 | 74 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV08PITANA-4 | game_total | 0.930 | 0.925 | 0.926 | 93 | 8 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV08PITANA-3 | game_total | 0.984 | 0.980 | 0.981 | 99 | 3 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT6 | team_total | 0.121 | 0.125 | 0.124 | 13 | 88 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV08PITANA-5 | game_total | 0.879 | 0.870 | 0.872 | 88 | 14 |  | -0.009 | NO_EDGE |
| KXNHL1P-26NOV08PITANA-ANA | period_winner |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV08PITANA-PIT | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV08PITANA-TIE | period_winner |  | 0.310 |  | 33 | 71 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV08PITANA-ANA2 | period_spread |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV08PITANA-PIT2 | period_spread |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV08PITANA-1 | period_total |  | 0.870 |  | 88 | 14 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV08PITANA-2 | period_total |  | 0.625 |  | 63 | 38 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV08PITANA-3 | period_total |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV08PITANA-ANA | period_winner |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV08PITANA-PIT | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV08PITANA-TIE | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV08PITANA-ANA2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV08PITANA-PIT2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV08PITANA-1 | period_total |  | 0.920 |  | 94 | 10 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV08PITANA-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV08PITANA-3 | period_total |  | 0.410 |  | 42 | 60 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV08PITANA-ANA | period_winner |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV08PITANA-PIT | period_winner |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV08PITANA-TIE | period_winner |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV08PITANA-ANA2 | period_spread |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV08PITANA-PIT2 | period_spread |  | 0.155 |  | 17 | 86 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV08PITANA-1 | period_total |  | 0.935 |  | 95 | 8 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV08PITANA-2 | period_total |  | 0.730 |  | 75 | 29 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV08PITANA-3 | period_total |  | 0.460 |  | 47 | 55 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAAKILLORN17-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAAKILLORN17-2 | player_assists |  | 0.040 |  | 5 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANABSENNECKE45-1 | player_assists |  | 0.475 |  | 48 | 53 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANABSENNECKE45-2 | player_assists |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANACGAUTHIER61-1 | player_assists |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANACGAUTHIER61-2 | player_assists |  | 0.100 |  | 11 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAJCAULFIELD28-1 | player_assists |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAJLACOMBE2-1 | player_assists |  | 0.550 |  | 56 | 46 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAJLACOMBE2-2 | player_assists |  | 0.185 |  | 20 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAJLACOMBE2-3 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANALCARLSSON91-1 | player_assists |  | 0.520 |  | 53 | 49 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANALCARLSSON91-2 | player_assists |  | 0.150 |  | 17 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAMGRANLUND64-1 | player_assists |  | 0.480 |  | 49 | 53 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANAMGRANLUND64-2 | player_assists |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANATLUNEAU67-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-ANATLUNEAU67-2 | player_assists |  | 0.065 |  | 7 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITBKINDEL81-1 | player_assists |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITBKINDEL81-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITECHINAKHOV59-1 | player_assists |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITEKARLSSON65-1 | player_assists |  | 0.500 |  | 51 | 51 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITEKARLSSON65-2 | player_assists |  | 0.160 |  | 18 | 86 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITEKARLSSON65-3 | player_assists |  | 0.035 |  | 6 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITEMALKIN71-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITEMALKIN71-2 | player_assists |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITKLETANG58-1 | player_assists |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITKLETANG58-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITRRAKELL67-1 | player_assists |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITRRAKELL67-2 | player_assists |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITSCROSBY87-1 | player_assists |  | 0.455 |  | 47 | 56 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITSCROSBY87-2 | player_assists |  | 0.120 |  | 14 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV08PITANA-PITTNOVAK18-1 | player_assists |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ ANA | 0.605 | 0.644 | 0.154 | 0.192 | 7.33 | 7.12 | 0.968/1.042 | KXNHLTEAMTOTAL-26NOV08PITANA-PIT3 -0.050 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Jeff Malott: 1+ goals YES @ 11c · p 0.1575 (adj 0.1444) · $6.37 · thesis ANA:OFFENSE_4PLUS
- Anaheim wins by over 2.5 goals YES @ 22c · p 0.3129 (adj 0.264) · $6.69 · thesis ANA:WINS_BY_2PLUS
- Pittsburgh wins by over 2.5 goals NO @ 82c · p 0.886 (adj 0.8505) · $20.0 · thesis ANA:WINS
- Beckett Sennecke: 1+ goals YES @ 35c · p 0.3948 (adj 0.3823) · $3.81 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ ANA** · priced 172/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 26.45, exp saves 23.05 (sd 6.43), pull risk 0.064
- PIT net: Arturs Silovs (CONFIRMED) exp shots 28.23, exp saves 23.65 (sd 6.97), pull risk 0.107

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Erik Karlsson: 1+ points | 0.499 | 0.595 | 61/42 | +0.064 | STANDARD |
| Sidney Crosby: 1+ assists | 0.370 | 0.455 | 47/56 | +0.053 | STANDARD |
| Alex Killorn: 1+ points | 0.488 | 0.405 | 41/60 | +0.061 | STANDARD |
| Ben Kindel: 1+ points | 0.413 | 0.495 | 51/52 | +0.049 | STANDARD |
| Erik Karlsson: 2+ points | 0.153 | 0.230 | 24/78 | +0.055 | STANDARD |
| Erik Karlsson: 1+ assists | 0.427 | 0.500 | 51/51 | +0.046 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
