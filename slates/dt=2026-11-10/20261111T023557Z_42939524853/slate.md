# NHL slate 2026-11-10 — RESEARCH_ONLY

generated 2026-11-11T02:35:57Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 7 · simulated (not started): 1 · markets on board: 3548 · contracts joined: 230 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 205, 'OK': 15, 'NO_EDGE': 10}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 37, 'game_early_goal': 1, 'first_goal': 33, 'game_winner': 2, 'player_goals': 58, 'game_overtime': 1, 'player_points': 50, 'goalie_saves': 1, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ LAK | 2026-11-11T03:00:00Z | T-10m | 0.576 | 0.424 | 0.177 | 6.00 | 3.24 | 2.77 | 230 (25/205) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH4 | team_total | 0.312 | 0.370 | 0.358 | 38 | 64 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH3 | team_total | 0.523 | 0.575 | 0.565 | 58 | 43 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV10NSHLA-4 | game_total | 0.835 | 0.875 | 0.868 | 88 | 13 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH2 | team_total | 0.757 | 0.795 | 0.788 | 80 | 21 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV10NSHLA-5 | game_total | 0.748 | 0.790 | 0.782 | 80 | 22 | no | +0.020 | OK |
| KXNHLGAME-26NOV10NSHLA-NSH | game_winner | 0.424 | 0.465 | 0.457 | 47 | 54 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV10NSHLA-7 | game_total | 0.415 | 0.455 | 0.447 | 46 | 55 | no | +0.018 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH2 | game_spread | 0.219 | 0.255 | 0.248 | 26 | 75 | no | +0.018 | OK |
| KXNHLTOTAL-26NOV10NSHLA-6 | game_total | 0.526 | 0.565 | 0.557 | 57 | 44 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH5 | team_total | 0.154 | 0.185 | 0.179 | 19 | 82 | no | +0.015 | OK |
| KXNHLGAME-26NOV10NSHLA-LA | game_winner | 0.576 | 0.545 | 0.551 | 55 | 46 | yes | +0.009 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH3 | game_spread | 0.123 | 0.145 | 0.140 | 15 | 86 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV10NSHLA-3 | game_total | 0.960 | 0.975 | 0.972 | 98 | 3 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH6 | team_total | 0.061 | 0.080 | 0.076 | 9 | 93 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV10NSHLA-9 | game_total | 0.160 | 0.175 | 0.172 | 18 | 83 | no | +0.000 | OK |
| KXNHLSPREAD-26NOV10NSHLA-LA2 | game_spread | 0.342 | 0.325 | 0.328 | 33 | 68 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV10NSHLA-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV10NSHLA-8 | game_total | 0.233 | 0.250 | 0.247 | 26 | 76 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV10NSHLA-10 | game_total | 0.073 | 0.075 | 0.075 | 8 | 93 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA2 | team_total | 0.831 | 0.825 | 0.826 | 83 | 18 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA6 | team_total | 0.107 | 0.100 | 0.101 | 11 | 91 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA3 | team_total | 0.635 | 0.625 | 0.627 | 63 | 38 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA5 | team_total | 0.227 | 0.225 | 0.225 | 23 | 78 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26NOV10NSHLA-LA3 | game_spread | 0.215 | 0.215 | 0.215 | 22 | 79 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA4 | team_total | 0.415 | 0.415 | 0.415 | 42 | 59 |  | -0.022 | NO_EDGE |
| KXNHL1P-26NOV10NSHLA-LA | period_winner |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV10NSHLA-NSH | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV10NSHLA-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV10NSHLA-LA2 | period_spread |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV10NSHLA-NSH2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV10NSHLA-1 | period_total |  | 0.840 |  | 85 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV10NSHLA-2 | period_total |  | 0.555 |  | 56 | 45 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV10NSHLA-3 | period_total |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV10NSHLA-LA | period_winner |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV10NSHLA-NSH | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV10NSHLA-TIE | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV10NSHLA-LA2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV10NSHLA-NSH2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV10NSHLA-1 | period_total |  | 0.900 |  | 91 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV10NSHLA-2 | period_total |  | 0.600 |  | 61 | 41 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV10NSHLA-3 | period_total |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV10NSHLA-LA | period_winner |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV10NSHLA-NSH | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV10NSHLA-TIE | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV10NSHLA-LA2 | period_spread |  | 0.175 |  | 20 | 85 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV10NSHLA-NSH2 | period_spread |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV10NSHLA-1 | period_total |  | 0.895 |  | 94 | 15 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV10NSHLA-2 | period_total |  | 0.650 |  | 66 | 36 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV10NSHLA-3 | period_total |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAKEMPE9-1 | player_assists |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAKEMPE9-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAALAFERRIERE14-1 | player_assists |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAALAFERRIERE14-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAPANARIN10-1 | player_assists |  | 0.545 |  | 55 | 46 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAPANARIN10-2 | player_assists |  | 0.170 |  | 19 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAAPANARIN10-3 | player_assists |  | 0.035 |  | 6 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAATURCOTTE15-1 | player_assists |  | 0.165 |  | 27 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LABCLARKE92-1 | player_assists |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LABCLARKE92-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LACPERRY90-1 | player_assists |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LADDOUGHTY8-1 | player_assists |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LADDOUGHTY8-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAEGUSTAFSSON64-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAEGUSTAFSSON64-2 | player_assists |  | 0.025 |  | 3 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAEHAULA56-1 | player_assists |  | 0.220 |  | 24 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAJEDMUNDSON6-1 | player_assists |  | 0.160 |  | 18 | 86 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAQBYFIELD55-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LAQBYFIELD55-2 | player_assists |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-LATMOORE12-1 | player_assists |  | 0.240 |  | 26 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHAKERFOOT14-1 | player_assists |  | 0.240 |  | 26 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHAWILSBY2-1 | player_assists |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHBSKJEI76-1 | player_assists |  | 0.285 |  | 31 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHBSKJEI76-2 | player_assists |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHFFORSBERG9-1 | player_assists |  | 0.435 |  | 44 | 57 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHFFORSBERG9-2 | player_assists |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1 | player_assists |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHNHOGLANDER21-1 | player_assists |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHRCOLTON79-1 | player_assists |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV10NSHLA-NSHRJOSI59-1 | player_assists |  | 0.535 |  | 54 | 47 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ LAK | 0.576 | 0.586 | 0.177 | 0.218 | 6.00 | 6.19 | 0.987/1.004 | KXNHLTOTAL-26NOV10NSHLA-7 +0.040 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Adam Wilsby: 1+ goals YES @ 4c · p 0.0682 (adj 0.0599) · $3.78 · thesis NSH:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0791 (adj 0.0681) · $3.28 · thesis LAK:OFFENSE_4PLUS
- Artemi Panarin: 1+ goals NO @ 63c · p 0.6867 (adj 0.6713) · $17.8 · thesis LAK:SUPPRESSED
- Steven Stamkos: 1+ goals NO @ 64c · p 0.6957 (adj 0.6805) · $18.1 · thesis NSH:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ LAK** · priced 169/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (CONFIRMED) exp shots 26.6, exp saves 23.3 (sd 6.26), pull risk 0.048
- NSH net: Juuse Saros (CONFIRMED) exp shots 29.67, exp saves 25.52 (sd 6.94), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ points | 0.308 | 0.200 | 21/81 | +0.086 | STANDARD |
| Artemi Panarin: 1+ assists | 0.441 | 0.545 | 55/46 | +0.082 | STANDARD |
| Artemi Panarin: 2+ points | 0.252 | 0.345 | 35/66 | +0.073 | STANDARD |
| Roman Josi: 1+ points | 0.522 | 0.615 | 63/40 | +0.062 | STANDARD |
| Roman Josi: 1+ assists | 0.443 | 0.535 | 54/47 | +0.070 | STANDARD |
| Joel Edmundson: 1+ assists | 0.248 | 0.160 | 18/86 | +0.058 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
