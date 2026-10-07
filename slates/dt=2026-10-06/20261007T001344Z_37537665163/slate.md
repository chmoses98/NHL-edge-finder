# NHL slate 2026-10-06 — RESEARCH_ONLY

generated 2026-10-07T00:13:44Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 9 · simulated (not started): 2 · markets on board: 3547 · contracts joined: 408 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 358, 'OK': 38, 'NO_EDGE': 12}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 51, 'game_early_goal': 2, 'first_goal': 70, 'game_winner': 4, 'player_goals': 123, 'game_overtime': 2, 'player_points': 60, 'goalie_saves': 2, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ SEA | 2026-10-07T01:40:00Z | T-60m | 0.503 | 0.497 | 0.174 | 6.38 | 3.21 | 3.17 | 198 (25/173) | PROBABLE/PROJECTED |
| FLA @ LAK | 2026-10-07T02:00:00Z | T-90m | 0.557 | 0.443 | 0.172 | 6.25 | 3.31 | 2.94 | 210 (25/185) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT06VGKSEA-SEA | game_winner | 0.503 | 0.375 | 0.400 | 38 | 63 | yes | +0.107 | OK |
| KXNHLGAME-26OCT06VGKSEA-VGK | game_winner | 0.497 | 0.615 | 0.592 | 62 | 39 | no | +0.097 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK2 | game_spread | 0.286 | 0.385 | 0.364 | 39 | 62 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA3 | team_total | 0.624 | 0.525 | 0.545 | 53 | 48 | yes | +0.077 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK3 | game_spread | 0.172 | 0.265 | 0.244 | 27 | 74 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA2 | game_spread | 0.291 | 0.205 | 0.221 | 21 | 80 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA4 | team_total | 0.412 | 0.315 | 0.334 | 33 | 70 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA5 | team_total | 0.229 | 0.150 | 0.164 | 16 | 86 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA3 | team_total | 0.651 | 0.570 | 0.587 | 58 | 44 | yes | +0.054 | OK |
| KXNHLGAME-26OCT06FLALA-FLA | game_winner | 0.443 | 0.515 | 0.501 | 52 | 49 | no | +0.049 | OK |
| KXNHLGAME-26OCT06FLALA-LA | game_winner | 0.557 | 0.485 | 0.499 | 49 | 52 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA4 | team_total | 0.434 | 0.360 | 0.374 | 37 | 65 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA3 | game_spread | 0.134 | 0.195 | 0.181 | 20 | 81 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA3 | game_spread | 0.181 | 0.125 | 0.135 | 13 | 88 | yes | +0.043 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA2 | game_spread | 0.337 | 0.275 | 0.287 | 28 | 73 | yes | +0.043 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA2 | game_spread | 0.240 | 0.300 | 0.287 | 31 | 71 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA6 | team_total | 0.106 | 0.060 | 0.067 | 7 | 95 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA3 | game_spread | 0.211 | 0.165 | 0.173 | 17 | 84 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA2 | team_total | 0.823 | 0.770 | 0.781 | 78 | 24 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK3 | team_total | 0.620 | 0.665 | 0.656 | 67 | 34 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK2 | team_total | 0.820 | 0.860 | 0.853 | 87 | 15 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA4 | team_total | 0.352 | 0.395 | 0.386 | 40 | 61 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT06VGKSEA-8 | game_total | 0.284 | 0.245 | 0.253 | 25 | 76 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK5 | team_total | 0.218 | 0.255 | 0.247 | 26 | 75 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA5 | team_total | 0.241 | 0.195 | 0.204 | 21 | 82 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA6 | team_total | 0.115 | 0.075 | 0.082 | 9 | 94 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK4 | team_total | 0.404 | 0.445 | 0.437 | 45 | 56 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA2 | team_total | 0.840 | 0.795 | 0.805 | 81 | 22 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA3 | team_total | 0.567 | 0.605 | 0.597 | 61 | 40 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT06FLALA-9 | game_total | 0.185 | 0.155 | 0.161 | 16 | 85 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT06FLALA-10 | game_total | 0.089 | 0.065 | 0.069 | 7 | 94 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT06VGKSEA-9 | game_total | 0.203 | 0.175 | 0.180 | 18 | 83 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT06FLALA-8 | game_total | 0.263 | 0.235 | 0.240 | 24 | 77 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT06VGKSEA-7 | game_total | 0.476 | 0.445 | 0.451 | 45 | 56 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA2 | team_total | 0.783 | 0.820 | 0.813 | 84 | 20 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT06FLALA-6 | game_total | 0.573 | 0.545 | 0.551 | 55 | 46 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK6 | team_total | 0.101 | 0.120 | 0.116 | 13 | 89 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT06VGKSEA-10 | game_total | 0.098 | 0.080 | 0.083 | 9 | 93 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT06VGKSEA-6 | game_total | 0.587 | 0.565 | 0.569 | 57 | 44 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT06FLALA-7 | game_total | 0.456 | 0.435 | 0.439 | 44 | 57 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA6 | team_total | 0.077 | 0.090 | 0.087 | 10 | 92 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA5 | team_total | 0.181 | 0.205 | 0.200 | 22 | 81 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT06VGKSEA-3 | game_total | 0.969 | 0.965 | 0.966 | 97 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT06VGKSEA-2 | game_total | 0.987 | 0.980 | 0.982 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT06FLALA-2 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT06VGKSEA-5 | game_total | 0.796 | 0.785 | 0.787 | 79 | 22 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT06FLALA-3 | game_total | 0.966 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT06FLALA-4 | game_total | 0.861 | 0.850 | 0.852 | 86 | 16 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT06VGKSEA-4 | game_total | 0.871 | 0.875 | 0.874 | 88 | 13 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT06FLALA-5 | game_total | 0.779 | 0.775 | 0.776 | 78 | 23 |  | -0.013 | NO_EDGE |
| KXNHL1P-26OCT06VGKSEA-SEA | period_winner |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT06VGKSEA-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT06VGKSEA-VGK | period_winner |  | 0.380 |  | 40 | 64 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT06VGKSEA-SEA2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT06VGKSEA-VGK2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT06VGKSEA-1 | period_total |  | 0.845 |  | 86 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT06VGKSEA-2 | period_total |  | 0.545 |  | 55 | 46 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT06VGKSEA-3 | period_total |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT06VGKSEA-SEA | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT06VGKSEA-TIE | period_winner |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT06VGKSEA-VGK | period_winner |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT06VGKSEA-SEA2 | period_spread |  | 0.085 |  | 9 | 92 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT06VGKSEA-VGK2 | period_spread |  | 0.150 |  | 17 | 87 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT06VGKSEA-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT06VGKSEA-2 | period_total |  | 0.605 |  | 62 | 41 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT06VGKSEA-3 | period_total |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT06VGKSEA-SEA | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT06VGKSEA-TIE | period_winner |  | 0.265 |  | 29 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT06VGKSEA-VGK | period_winner |  | 0.415 |  | 43 | 60 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT06VGKSEA-SEA2 | period_spread |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT06VGKSEA-VGK2 | period_spread |  | 0.190 |  | 21 | 83 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT06VGKSEA-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT06VGKSEA-2 | period_total |  | 0.650 |  | 67 | 37 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT06VGKSEA-3 | period_total |  | 0.370 |  | 39 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06VGKSEA-SEABMONTOUR62-1 | player_assists |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06VGKSEA-SEABMONTOUR62-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06VGKSEA-SEACSTEPHENSON9-1 | player_assists |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06VGKSEA-SEACSTEPHENSON9-2 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06VGKSEA-SEAJEBERLE7-1 | player_assists |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06VGKSEA-SEAJEBERLE7-2 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ SEA | 0.503 | 0.485 | 0.174 | 0.223 | 6.38 | 6.10 | 1.001/1.003 | KXNHLTOTAL-26OCT06VGKSEA-6 -0.045 |
| FLA @ LAK | 0.557 | 0.580 | 0.172 | 0.220 | 6.25 | 5.96 | 0.995/1.014 | KXNHLTOTAL-26OCT06FLALA-6 -0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Winterton: 1+ goals YES @ 10c · p 0.1407 (adj 0.1293) · $5.73 · thesis SEA:OFFENSE_4PLUS
- Freddy Gaudreau: 1+ goals YES @ 8c · p 0.1144 (adj 0.1046) · $4.7 · thesis SEA:OFFENSE_4PLUS
- Jack Eichel: 1+ goals NO @ 67c · p 0.7222 (adj 0.7079) · $18.02 · thesis VGK:SUPPRESSED
- Shane Wright: 1+ goals YES @ 15c · p 0.1964 (adj 0.176) · $4.45 · thesis SEA:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 68c · p 0.7706 (adj 0.7467) · $17.39 · thesis FLA:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 64c · p 0.7886 (adj 0.6855) · $17.39 · thesis LAK:SUPPRESSED
- Alex Laferriere: 1+ goals YES @ 23c · p 0.2745 (adj 0.2621) · $6.0 · thesis LAK:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 49c · p 0.6102 (adj 0.5288) · $9.23 · thesis LAK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VGK @ SEA** · priced 143/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROBABLE) exp shots 28.49, exp saves 24.64 (sd 6.77), pull risk 0.058
- VGK net: Adin Hill (PROJECTED) exp shots 25.65, exp saves 22.19 (sd 6.17), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joey Daccord: 25+ saves | 0.503 | 0.295 | 53/94 | -0.045 |  |
| Jack Eichel: 2+ points | 0.206 | 0.355 | 37/66 | +0.118 | STANDARD |
| Jack Eichel: 1+ assists | 0.407 | 0.535 | 55/48 | +0.096 | STANDARD |
| Mitch Marner: 1+ assists | 0.385 | 0.500 | 52/52 | +0.078 | STANDARD |
| Mitch Marner: 1+ points | 0.530 | 0.640 | 65/37 | +0.084 | STANDARD |
| Jack Eichel: 1+ points | 0.570 | 0.665 | 69/36 | +0.054 | STANDARD |

**FLA @ LAK** · priced 159/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 26.39, exp saves 23.09 (sd 6.23), pull risk 0.049
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.81, exp saves 23.61 (sd 6.55), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.211 | 0.370 | 38/64 | +0.132 | STANDARD |
| Brady Tkachuk: 1+ points | 0.422 | 0.565 | 59/46 | +0.100 | STANDARD |
| Sam Reinhart: 1+ points | 0.460 | 0.590 | 61/43 | +0.093 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.232 | 0.360 | 38/66 | +0.093 | STANDARD |
| Alex Laferriere: 1+ assists | 0.387 | 0.260 | 27/75 | +0.103 | STANDARD |
| Alex Laferriere: 1+ points | 0.555 | 0.430 | 45/59 | +0.088 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
