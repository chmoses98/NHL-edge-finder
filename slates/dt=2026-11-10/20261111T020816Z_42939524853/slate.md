# NHL slate 2026-11-10 — RESEARCH_ONLY

generated 2026-11-11T02:08:16Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 7 · simulated (not started): 1 · markets on board: 3307 · contracts joined: 230 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 205, 'OK': 16, 'NO_EDGE': 9}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 37, 'game_early_goal': 1, 'first_goal': 33, 'game_winner': 2, 'player_goals': 58, 'game_overtime': 1, 'player_points': 50, 'goalie_saves': 1, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ LAK | 2026-11-11T03:00:00Z | T-30m | 0.571 | 0.429 | 0.179 | 5.99 | 3.22 | 2.77 | 230 (25/205) | CONFIRMED/PROJECTED |

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
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH5 | team_total | 0.153 | 0.185 | 0.178 | 19 | 82 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV10NSHLA-3 | game_total | 0.958 | 0.975 | 0.972 | 98 | 3 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH3 | game_spread | 0.122 | 0.145 | 0.140 | 15 | 86 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV10NSHLA-8 | game_total | 0.228 | 0.255 | 0.249 | 26 | 75 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH6 | team_total | 0.062 | 0.075 | 0.072 | 8 | 93 | no | +0.004 | OK |
| KXNHLGAME-26NOV10NSHLA-LA | game_winner | 0.571 | 0.545 | 0.550 | 55 | 46 | yes | +0.003 | OK |
| KXNHLGAME-26NOV10NSHLA-NSH | game_winner | 0.429 | 0.455 | 0.450 | 46 | 55 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV10NSHLA-9 | game_total | 0.158 | 0.175 | 0.172 | 18 | 83 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA6 | team_total | 0.106 | 0.095 | 0.097 | 10 | 91 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV10NSHLA-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26NOV10NSHLA-LA2 | game_spread | 0.342 | 0.325 | 0.328 | 33 | 68 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA2 | team_total | 0.826 | 0.840 | 0.837 | 85 | 17 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV10NSHLA-10 | game_total | 0.072 | 0.075 | 0.074 | 8 | 93 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26NOV10NSHLA-LA3 | game_spread | 0.212 | 0.215 | 0.214 | 22 | 79 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA3 | team_total | 0.630 | 0.625 | 0.626 | 63 | 38 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA5 | team_total | 0.225 | 0.225 | 0.225 | 23 | 78 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA4 | team_total | 0.414 | 0.415 | 0.415 | 42 | 59 |  | -0.021 | NO_EDGE |
| KXNHL1P-26NOV10NSHLA-LA | period_winner |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV10NSHLA-NSH | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV10NSHLA-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV10NSHLA-LA2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV10NSHLA-NSH2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV10NSHLA-1 | period_total |  | 0.835 |  | 85 | 18 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV10NSHLA-2 | period_total |  | 0.555 |  | 56 | 45 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV10NSHLA-3 | period_total |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV10NSHLA-LA | period_winner |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV10NSHLA-NSH | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV10NSHLA-TIE | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV10NSHLA-LA2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV10NSHLA-NSH2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV10NSHLA-1 | period_total |  | 0.900 |  | 91 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV10NSHLA-2 | period_total |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV10NSHLA-3 | period_total |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV10NSHLA-LA | period_winner |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV10NSHLA-NSH | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV10NSHLA-TIE | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV10NSHLA-LA2 | period_spread |  | 0.180 |  | 19 | 83 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV10NSHLA-NSH2 | period_spread |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV10NSHLA-1 | period_total |  | 0.915 |  | 94 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV10NSHLA-2 | period_total |  | 0.655 |  | 67 | 36 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV10NSHLA-3 | period_total |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAKEMPE9-1 | player_assists |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAKEMPE9-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAALAFERRIERE14-1 | player_assists |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAALAFERRIERE14-2 | player_assists |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAPANARIN10-1 | player_assists |  | 0.545 |  | 55 | 46 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAPANARIN10-2 | player_assists |  | 0.170 |  | 19 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAPANARIN10-3 | player_assists |  | 0.035 |  | 6 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAATURCOTTE15-1 | player_assists |  | 0.275 |  | 49 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LABCLARKE92-1 | player_assists |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LABCLARKE92-2 | player_assists |  | 0.100 |  | 11 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LACPERRY90-1 | player_assists |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LADDOUGHTY8-1 | player_assists |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LADDOUGHTY8-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAEGUSTAFSSON64-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAEGUSTAFSSON64-2 | player_assists |  | 0.025 |  | 3 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAEHAULA56-1 | player_assists |  | 0.220 |  | 24 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAJEDMUNDSON6-1 | player_assists |  | 0.170 |  | 19 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAQBYFIELD55-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAQBYFIELD55-2 | player_assists |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LATMOORE12-1 | player_assists |  | 0.240 |  | 26 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHAKERFOOT14-1 | player_assists |  | 0.240 |  | 26 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHAWILSBY2-1 | player_assists |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHBSKJEI76-1 | player_assists |  | 0.285 |  | 31 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHBSKJEI76-2 | player_assists |  | 0.050 |  | 7 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHFFORSBERG9-1 | player_assists |  | 0.435 |  | 44 | 57 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHFFORSBERG9-2 | player_assists |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1 | player_assists |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-2 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHNHOGLANDER21-1 | player_assists |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHRCOLTON79-1 | player_assists |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHRJOSI59-1 | player_assists |  | 0.545 |  | 55 | 46 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ LAK | 0.571 | 0.581 | 0.179 | 0.216 | 5.99 | 6.18 | 0.987/1.000 | KXNHLTOTAL-26NOV10NSHLA-7 +0.037 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 3 recommended · full analysis in card.md / packet.json `thesis_card`

- Artemi Panarin: 1+ goals NO @ 63c · p 0.687 (adj 0.6715) · $17.87 · thesis LAK:SUPPRESSED
- Steven Stamkos: 1+ goals NO @ 64c · p 0.6964 (adj 0.6811) · $15.85 · thesis NSH:SUPPRESSED
- Mavrik Bourque: 1+ assists NO @ 70c · p 0.7781 (adj 0.734) · $14.15 · thesis NSH:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ LAK** · priced 169/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (CONFIRMED) exp shots 26.6, exp saves 23.25 (sd 6.29), pull risk 0.051
- NSH net: Juuse Saros (PROJECTED) exp shots 29.67, exp saves 25.51 (sd 6.87), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.439 | 0.545 | 55/46 | +0.084 | STANDARD |
| Joel Edmundson: 1+ points | 0.305 | 0.200 | 21/81 | +0.083 | STANDARD |
| Roman Josi: 1+ assists | 0.442 | 0.545 | 55/46 | +0.080 | STANDARD |
| Artemi Panarin: 2+ points | 0.250 | 0.345 | 35/66 | +0.074 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.222 | 0.310 | 32/70 | +0.063 | STANDARD |
| Steven Stamkos: 1+ points | 0.532 | 0.615 | 62/39 | +0.061 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
