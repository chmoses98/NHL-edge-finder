# NHL slate 2026-11-01 — RESEARCH_ONLY

generated 2026-11-01T23:41:20Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 1 · markets on board: 2356 · contracts joined: 217 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 192, 'OK': 19, 'NO_EDGE': 6}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 30, 'game_early_goal': 1, 'first_goal': 32, 'game_winner': 2, 'player_goals': 59, 'game_overtime': 1, 'player_points': 43, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ ANA | 2026-11-02T01:00:00Z | T-60m | 0.562 | 0.438 | 0.167 | 6.83 | 3.62 | 3.22 | 217 (25/192) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV01OTTANA-ANA | game_winner | 0.562 | 0.465 | 0.484 | 47 | 54 | yes | +0.075 | OK |
| KXNHLGAME-26NOV01OTTANA-OTT | game_winner | 0.438 | 0.525 | 0.507 | 53 | 48 | no | +0.065 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA2 | game_spread | 0.347 | 0.275 | 0.289 | 28 | 73 | yes | +0.053 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT3 | game_spread | 0.148 | 0.215 | 0.200 | 22 | 79 | no | +0.051 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT2 | game_spread | 0.249 | 0.315 | 0.301 | 32 | 69 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4 | team_total | 0.500 | 0.435 | 0.448 | 44 | 57 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA5 | team_total | 0.305 | 0.245 | 0.256 | 25 | 76 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 | team_total | 0.411 | 0.475 | 0.462 | 48 | 53 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT3 | team_total | 0.624 | 0.680 | 0.669 | 69 | 33 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA6 | team_total | 0.157 | 0.110 | 0.118 | 12 | 90 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2 | team_total | 0.823 | 0.875 | 0.866 | 89 | 14 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA3 | team_total | 0.704 | 0.650 | 0.661 | 66 | 36 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA3 | game_spread | 0.227 | 0.185 | 0.193 | 19 | 82 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5 | team_total | 0.230 | 0.275 | 0.266 | 28 | 73 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV01OTTANA-4 | game_total | 0.905 | 0.925 | 0.921 | 93 | 8 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT6 | team_total | 0.111 | 0.125 | 0.122 | 13 | 88 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA2 | team_total | 0.870 | 0.850 | 0.854 | 86 | 16 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV01OTTANA-5 | game_total | 0.841 | 0.855 | 0.852 | 86 | 15 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV01OTTANA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV01OTTANA-8 | game_total | 0.354 | 0.335 | 0.339 | 34 | 67 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-10 | game_total | 0.135 | 0.125 | 0.127 | 13 | 88 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-9 | game_total | 0.260 | 0.245 | 0.248 | 25 | 76 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-3 | game_total | 0.980 | 0.980 | 0.980 | 99 | 3 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-6 | game_total | 0.655 | 0.665 | 0.663 | 67 | 34 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-7 | game_total | 0.548 | 0.555 | 0.554 | 56 | 45 |  | -0.016 | NO_EDGE |
| KXNHL1P-26NOV01OTTANA-ANA | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV01OTTANA-OTT | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV01OTTANA-TIE | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV01OTTANA-ANA2 | period_spread |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV01OTTANA-OTT2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV01OTTANA-1 | period_total |  | 0.860 |  | 87 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV01OTTANA-2 | period_total |  | 0.605 |  | 61 | 40 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV01OTTANA-3 | period_total |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV01OTTANA-ANA | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV01OTTANA-OTT | period_winner |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV01OTTANA-TIE | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV01OTTANA-ANA2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV01OTTANA-OTT2 | period_spread |  | 0.140 |  | 15 | 87 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV01OTTANA-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV01OTTANA-2 | period_total |  | 0.655 |  | 67 | 36 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV01OTTANA-3 | period_total |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV01OTTANA-ANA | period_winner |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV01OTTANA-OTT | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV01OTTANA-TIE | period_winner |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV01OTTANA-ANA2 | period_spread |  | 0.140 |  | 15 | 87 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV01OTTANA-OTT2 | period_spread |  | 0.160 |  | 17 | 85 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV01OTTANA-1 | period_total |  | 0.920 |  | 94 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV01OTTANA-2 | period_total |  | 0.705 |  | 71 | 30 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV01OTTANA-3 | period_total |  | 0.445 |  | 46 | 57 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANAAKILLORN17-1 | player_assists |  | 0.235 |  | 24 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANABSENNECKE45-1 | player_assists |  | 0.410 |  | 42 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANABSENNECKE45-2 | player_assists |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANACGAUTHIER61-1 | player_assists |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANACGAUTHIER61-2 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANAJCAULFIELD28-1 | player_assists |  | 0.230 |  | 24 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANAJLACOMBE2-1 | player_assists |  | 0.495 |  | 50 | 51 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANAJLACOMBE2-2 | player_assists |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANALCARLSSON91-1 | player_assists |  | 0.465 |  | 47 | 54 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANALCARLSSON91-2 | player_assists |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANAMGRANLUND64-1 | player_assists |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANAMGRANLUND64-2 | player_assists |  | 0.075 |  | 11 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANATLUNEAU67-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANATLUNEAU67-2 | player_assists |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTCGIROUX28-1 | player_assists |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTCGIROUX28-2 | player_assists |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTDBATHERSON19-1 | player_assists |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTDBATHERSON19-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTDCOZENS24-1 | player_assists |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTDCOZENS24-2 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTFZETTERLUND20-1 | player_assists |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTJSANDERSON85-1 | player_assists |  | 0.460 |  | 47 | 55 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTJSANDERSON85-2 | player_assists |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTSHALLIDAY34-1 | player_assists |  | 0.205 |  | 21 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTSPINTO12-1 | player_assists |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTSPINTO12-2 | player_assists |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTTCHABOT72-1 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTTCHABOT72-2 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTTSTUTZLE18-1 | player_assists |  | 0.505 |  | 51 | 50 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTTSTUTZLE18-2 | player_assists |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHLF10G-26NOV01OTTANA-Y | game_early_goal |  | 0.610 |  | 62 | 40 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ ANA | 0.562 | 0.586 | 0.167 | 0.213 | 6.83 | 6.57 | 0.968/1.034 | KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 -0.047 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 3 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 16c · p 0.2467 (adj 0.2238) · $14.4 · thesis ANA:OFFENSE_4PLUS
- Ottawa wins by over 2.5 goals NO @ 79c · p 0.8805 (adj 0.8327) · $20.0 · thesis ANA:WINS
- Ottawa over 3.5 goals scored NO @ 53c · p 0.6403 (adj 0.5654) · $5.2 · thesis OTT:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**OTT @ ANA** · priced 164/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 27.11, exp saves 23.63 (sd 6.52), pull risk 0.056
- OTT net: Jonas Johansson (PROJECTED) exp shots 27.68, exp saves 23.48 (sd 6.69), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ points | 0.445 | 0.545 | 55/46 | +0.078 | STANDARD |
| Jake Sanderson: 1+ assists | 0.361 | 0.460 | 47/55 | +0.072 | STANDARD |
| A.J. Greer: 1+ goals | 0.247 | 0.155 | 16/85 | +0.077 | STANDARD |
| Thomas Chabot: 1+ assists | 0.246 | 0.335 | 34/67 | +0.069 | STANDARD |
| Tim Stutzle: 2+ points | 0.236 | 0.325 | 33/68 | +0.069 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.580 | 0.495 | 50/51 | +0.062 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
