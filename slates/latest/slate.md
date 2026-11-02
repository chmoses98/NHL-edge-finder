# NHL slate 2026-11-01 — RESEARCH_ONLY

generated 2026-11-02T00:09:56Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 1 · markets on board: 2111 · contracts joined: 217 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 192, 'OK': 21, 'NO_EDGE': 4}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 30, 'game_early_goal': 1, 'first_goal': 32, 'game_winner': 2, 'player_goals': 59, 'game_overtime': 1, 'player_points': 43, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ ANA | 2026-11-02T01:00:00Z | T-30m | 0.573 | 0.427 | 0.163 | 6.92 | 3.70 | 3.22 | 217 (25/192) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV01OTTANA-ANA | game_winner | 0.573 | 0.465 | 0.487 | 47 | 54 | yes | +0.086 | OK |
| KXNHLGAME-26NOV01OTTANA-OTT | game_winner | 0.427 | 0.525 | 0.505 | 53 | 48 | no | +0.075 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA2 | game_spread | 0.362 | 0.275 | 0.291 | 28 | 73 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4 | team_total | 0.519 | 0.435 | 0.452 | 44 | 57 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA5 | team_total | 0.321 | 0.245 | 0.259 | 25 | 76 | yes | +0.057 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT2 | game_spread | 0.241 | 0.315 | 0.299 | 32 | 69 | no | +0.054 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT3 | game_spread | 0.144 | 0.215 | 0.199 | 22 | 79 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 | team_total | 0.410 | 0.475 | 0.462 | 48 | 53 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA6 | team_total | 0.169 | 0.110 | 0.120 | 12 | 90 | yes | +0.041 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA3 | game_spread | 0.240 | 0.185 | 0.195 | 19 | 82 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA3 | team_total | 0.713 | 0.650 | 0.663 | 66 | 36 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT3 | team_total | 0.622 | 0.680 | 0.669 | 69 | 33 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2 | team_total | 0.822 | 0.875 | 0.866 | 89 | 14 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5 | team_total | 0.232 | 0.275 | 0.266 | 28 | 73 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA2 | team_total | 0.880 | 0.850 | 0.856 | 86 | 16 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV01OTTANA-8 | game_total | 0.364 | 0.335 | 0.341 | 34 | 67 | yes | +0.009 | OK |
| KXNHLTOTAL-26NOV01OTTANA-9 | game_total | 0.271 | 0.245 | 0.250 | 25 | 76 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV01OTTANA-4 | game_total | 0.907 | 0.925 | 0.922 | 93 | 8 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV01OTTANA-10 | game_total | 0.142 | 0.125 | 0.128 | 13 | 88 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT6 | team_total | 0.110 | 0.125 | 0.122 | 13 | 88 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV01OTTANA-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV01OTTANA-5 | game_total | 0.849 | 0.855 | 0.854 | 86 | 15 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-3 | game_total | 0.981 | 0.980 | 0.980 | 99 | 3 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-6 | game_total | 0.673 | 0.665 | 0.667 | 67 | 34 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-7 | game_total | 0.562 | 0.555 | 0.556 | 56 | 45 |  | -0.015 | NO_EDGE |
| KXNHL1P-26NOV01OTTANA-ANA | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV01OTTANA-OTT | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV01OTTANA-TIE | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV01OTTANA-ANA2 | period_spread |  | 0.110 |  | 13 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV01OTTANA-OTT2 | period_spread |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV01OTTANA-1 | period_total |  | 0.860 |  | 87 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV01OTTANA-2 | period_total |  | 0.615 |  | 62 | 39 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV01OTTANA-3 | period_total |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV01OTTANA-ANA | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV01OTTANA-OTT | period_winner |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV01OTTANA-TIE | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV01OTTANA-ANA2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV01OTTANA-OTT2 | period_spread |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV01OTTANA-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV01OTTANA-2 | period_total |  | 0.665 |  | 67 | 34 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV01OTTANA-3 | period_total |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV01OTTANA-ANA | period_winner |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV01OTTANA-OTT | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV01OTTANA-TIE | period_winner |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV01OTTANA-ANA2 | period_spread |  | 0.140 |  | 15 | 87 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV01OTTANA-OTT2 | period_spread |  | 0.160 |  | 17 | 85 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV01OTTANA-1 | period_total |  | 0.925 |  | 94 | 9 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV01OTTANA-2 | period_total |  | 0.700 |  | 71 | 31 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV01OTTANA-3 | period_total |  | 0.445 |  | 46 | 57 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANAAKILLORN17-1 | player_assists |  | 0.235 |  | 24 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANABSENNECKE45-1 | player_assists |  | 0.410 |  | 42 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANABSENNECKE45-2 | player_assists |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANACGAUTHIER61-1 | player_assists |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANACGAUTHIER61-2 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANAJCAULFIELD28-1 | player_assists |  | 0.230 |  | 24 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANAJLACOMBE2-1 | player_assists |  | 0.495 |  | 50 | 51 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANAJLACOMBE2-2 | player_assists |  | 0.160 |  | 17 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANALCARLSSON91-1 | player_assists |  | 0.470 |  | 48 | 54 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANALCARLSSON91-2 | player_assists |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANAMGRANLUND64-1 | player_assists |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANAMGRANLUND64-2 | player_assists |  | 0.105 |  | 11 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANATLUNEAU67-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-ANATLUNEAU67-2 | player_assists |  | 0.040 |  | 5 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTCGIROUX28-1 | player_assists |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTCGIROUX28-2 | player_assists |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTDBATHERSON19-1 | player_assists |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTDBATHERSON19-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTDCOZENS24-1 | player_assists |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTDCOZENS24-2 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTFZETTERLUND20-1 | player_assists |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTJSANDERSON85-1 | player_assists |  | 0.465 |  | 47 | 54 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTJSANDERSON85-2 | player_assists |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTSHALLIDAY34-1 | player_assists |  | 0.205 |  | 21 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTSPINTO12-1 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTSPINTO12-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTTCHABOT72-1 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTTCHABOT72-2 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTTSTUTZLE18-1 | player_assists |  | 0.505 |  | 51 | 50 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01OTTANA-OTTTSTUTZLE18-2 | player_assists |  | 0.155 |  | 17 | 86 |  |  | UNSUPPORTED |
| KXNHLF10G-26NOV01OTTANA-Y | game_early_goal |  | 0.610 |  | 63 | 41 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ ANA | 0.573 | 0.594 | 0.163 | 0.209 | 6.92 | 6.59 | 0.968/1.040 | KXNHLTOTAL-26NOV01OTTANA-8 -0.053 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 16c · p 0.2524 (adj 0.2281) · $15.51 · thesis ANA:OFFENSE_4PLUS
- Ottawa wins by over 2.5 goals NO @ 79c · p 0.8825 (adj 0.8337) · $20.0 · thesis ANA:WINS
- Jeff Malott: 1+ goals YES @ 10c · p 0.1359 (adj 0.1257) · $4.85 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 18c · p 0.2217 (adj 0.21) · $5.42 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**OTT @ ANA** · priced 164/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 27.11, exp saves 23.63 (sd 6.46), pull risk 0.054
- OTT net: Jonas Johansson (CONFIRMED) exp shots 27.68, exp saves 23.49 (sd 6.77), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.360 | 0.465 | 47/54 | +0.083 | STANDARD |
| Jake Sanderson: 1+ points | 0.442 | 0.540 | 55/47 | +0.071 | STANDARD |
| A.J. Greer: 1+ goals | 0.252 | 0.155 | 16/85 | +0.083 | STANDARD |
| Tim Stutzle: 2+ points | 0.236 | 0.330 | 34/68 | +0.069 | STANDARD |
| Thomas Chabot: 1+ assists | 0.244 | 0.335 | 34/67 | +0.070 | STANDARD |
| Thomas Chabot: 1+ points | 0.324 | 0.410 | 42/60 | +0.060 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
