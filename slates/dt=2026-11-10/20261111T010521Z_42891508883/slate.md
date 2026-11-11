# NHL slate 2026-11-10 — RESEARCH_ONLY

generated 2026-11-11T01:05:21Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 7 · simulated (not started): 1 · markets on board: 3345 · contracts joined: 230 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 205, 'OK': 15, 'NO_EDGE': 10}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 37, 'game_early_goal': 1, 'first_goal': 33, 'game_winner': 2, 'player_goals': 58, 'game_overtime': 1, 'player_points': 50, 'goalie_saves': 1, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ LAK | 2026-11-11T03:00:00Z | T-90m | 0.571 | 0.429 | 0.179 | 5.99 | 3.22 | 2.77 | 230 (25/205) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH3 | team_total | 0.524 | 0.575 | 0.565 | 58 | 43 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH4 | team_total | 0.310 | 0.355 | 0.346 | 36 | 65 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV10NSHLA-5 | game_total | 0.744 | 0.785 | 0.777 | 79 | 22 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV10NSHLA-6 | game_total | 0.522 | 0.565 | 0.557 | 57 | 44 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH2 | team_total | 0.758 | 0.795 | 0.788 | 80 | 21 | no | +0.020 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH2 | game_spread | 0.217 | 0.255 | 0.247 | 26 | 75 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV10NSHLA-7 | game_total | 0.413 | 0.455 | 0.447 | 46 | 55 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV10NSHLA-4 | game_total | 0.833 | 0.865 | 0.859 | 87 | 14 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV10NSHLA-3 | game_total | 0.958 | 0.975 | 0.972 | 98 | 3 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH3 | game_spread | 0.122 | 0.145 | 0.140 | 15 | 86 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV10NSHLA-8 | game_total | 0.228 | 0.255 | 0.249 | 26 | 75 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH5 | team_total | 0.153 | 0.180 | 0.174 | 19 | 83 | no | +0.007 | OK |
| KXNHLGAME-26NOV10NSHLA-LA | game_winner | 0.571 | 0.545 | 0.550 | 55 | 46 | yes | +0.003 | OK |
| KXNHLGAME-26NOV10NSHLA-NSH | game_winner | 0.429 | 0.455 | 0.450 | 46 | 55 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV10NSHLA-9 | game_total | 0.158 | 0.175 | 0.172 | 18 | 83 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV10NSHLA-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26NOV10NSHLA-LA2 | game_spread | 0.342 | 0.325 | 0.328 | 33 | 68 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH6 | team_total | 0.062 | 0.070 | 0.068 | 8 | 94 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV10NSHLA-10 | game_total | 0.072 | 0.075 | 0.074 | 8 | 93 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA6 | team_total | 0.106 | 0.105 | 0.105 | 11 | 90 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26NOV10NSHLA-LA3 | game_spread | 0.212 | 0.215 | 0.214 | 22 | 79 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA2 | team_total | 0.826 | 0.835 | 0.833 | 85 | 18 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA3 | team_total | 0.630 | 0.625 | 0.626 | 63 | 38 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA5 | team_total | 0.225 | 0.225 | 0.225 | 23 | 78 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA4 | team_total | 0.414 | 0.415 | 0.415 | 42 | 59 |  | -0.021 | NO_EDGE |
| KXNHL1P-26NOV10NSHLA-LA | period_winner |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV10NSHLA-NSH | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV10NSHLA-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV10NSHLA-LA2 | period_spread |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV10NSHLA-NSH2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV10NSHLA-1 | period_total |  | 0.835 |  | 85 | 18 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV10NSHLA-2 | period_total |  | 0.555 |  | 56 | 45 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV10NSHLA-3 | period_total |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV10NSHLA-LA | period_winner |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV10NSHLA-NSH | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV10NSHLA-TIE | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV10NSHLA-LA2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV10NSHLA-NSH2 | period_spread |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV10NSHLA-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV10NSHLA-2 | period_total |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV10NSHLA-3 | period_total |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV10NSHLA-LA | period_winner |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV10NSHLA-NSH | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV10NSHLA-TIE | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV10NSHLA-LA2 | period_spread |  | 0.190 |  | 20 | 82 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV10NSHLA-NSH2 | period_spread |  | 0.145 |  | 17 | 88 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV10NSHLA-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV10NSHLA-2 | period_total |  | 0.655 |  | 67 | 36 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV10NSHLA-3 | period_total |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAKEMPE9-1 | player_assists |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAKEMPE9-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAALAFERRIERE14-1 | player_assists |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAALAFERRIERE14-2 | player_assists |  | 0.080 |  | 10 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAPANARIN10-1 | player_assists |  | 0.545 |  | 55 | 46 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAPANARIN10-2 | player_assists |  | 0.180 |  | 20 | 84 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAPANARIN10-3 | player_assists |  | 0.035 |  | 6 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAATURCOTTE15-1 | player_assists |  | 0.495 |  | 93 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LABCLARKE92-1 | player_assists |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LABCLARKE92-2 | player_assists |  | 0.105 |  | 11 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LACPERRY90-1 | player_assists |  | 0.210 |  | 23 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LADDOUGHTY8-1 | player_assists |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LADDOUGHTY8-2 | player_assists |  | 0.035 |  | 6 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAEGUSTAFSSON64-1 | player_assists |  | 0.355 |  | 38 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAEGUSTAFSSON64-2 | player_assists |  | 0.015 |  | 2 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAEHAULA56-1 | player_assists |  | 0.225 |  | 25 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAJEDMUNDSON6-1 | player_assists |  | 0.110 |  | 13 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAQBYFIELD55-1 | player_assists |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAQBYFIELD55-2 | player_assists |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LATMOORE12-1 | player_assists |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHAKERFOOT14-1 | player_assists |  | 0.240 |  | 26 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHAWILSBY2-1 | player_assists |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHBSKJEI76-1 | player_assists |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHBSKJEI76-2 | player_assists |  | 0.035 |  | 6 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHFFORSBERG9-1 | player_assists |  | 0.430 |  | 44 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHFFORSBERG9-2 | player_assists |  | 0.115 |  | 12 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1 | player_assists |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-2 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHNHOGLANDER21-1 | player_assists |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHRCOLTON79-1 | player_assists |  | 0.185 |  | 20 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHRJOSI59-1 | player_assists |  | 0.535 |  | 54 | 47 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ LAK | 0.571 | 0.581 | 0.179 | 0.216 | 5.99 | 6.18 | 0.987/1.000 | KXNHLTOTAL-26NOV10NSHLA-7 +0.037 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 3 recommended · full analysis in card.md / packet.json `thesis_card`

- Steven Stamkos: 2+ goals NO @ 92c · p 0.9489 (adj 0.9404) · $20.0 · thesis NSH:SUPPRESSED
- Artemi Panarin: 1+ goals NO @ 63c · p 0.687 (adj 0.6715) · $18.11 · thesis LAK:SUPPRESSED
- Steven Stamkos: 1+ goals NO @ 65c · p 0.6964 (adj 0.6823) · $9.9 · thesis NSH:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ LAK** · priced 169/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (CONFIRMED) exp shots 26.6, exp saves 23.25 (sd 6.29), pull risk 0.051
- NSH net: Juuse Saros (PROJECTED) exp shots 29.67, exp saves 25.51 (sd 6.87), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ assists | 0.247 | 0.110 | 13/91 | +0.109 | STANDARD |
| Artemi Panarin: 1+ assists | 0.439 | 0.545 | 55/46 | +0.084 | STANDARD |
| Joel Edmundson: 1+ points | 0.305 | 0.200 | 21/81 | +0.083 | STANDARD |
| Artemi Panarin: 2+ points | 0.250 | 0.350 | 36/66 | +0.074 | STANDARD |
| Roman Josi: 1+ assists | 0.442 | 0.535 | 54/47 | +0.070 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.222 | 0.305 | 32/71 | +0.054 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
