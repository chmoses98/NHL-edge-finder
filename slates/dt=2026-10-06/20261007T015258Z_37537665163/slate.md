# NHL slate 2026-10-06 — RESEARCH_ONLY

generated 2026-10-07T01:52:58Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 9 · simulated (not started): 1 · markets on board: 3706 · contracts joined: 210 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 185, 'OK': 20, 'NO_EDGE': 5}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 28, 'game_early_goal': 1, 'first_goal': 34, 'game_winner': 2, 'player_goals': 62, 'game_overtime': 1, 'player_points': 34, 'goalie_saves': 1, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ LAK | 2026-10-07T02:00:00Z | T-<10m | 0.557 | 0.443 | 0.172 | 6.25 | 3.31 | 2.94 | 210 (25/185) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT06FLALA-LA3 | team_total | 0.651 | 0.570 | 0.587 | 58 | 44 | yes | +0.054 | OK |
| KXNHLGAME-26OCT06FLALA-FLA | game_winner | 0.443 | 0.515 | 0.501 | 52 | 49 | no | +0.049 | OK |
| KXNHLGAME-26OCT06FLALA-LA | game_winner | 0.557 | 0.485 | 0.499 | 49 | 52 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA2 | game_spread | 0.337 | 0.275 | 0.287 | 28 | 73 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA4 | team_total | 0.434 | 0.365 | 0.378 | 38 | 65 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA2 | game_spread | 0.240 | 0.295 | 0.283 | 30 | 71 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA3 | game_spread | 0.134 | 0.185 | 0.174 | 19 | 82 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA3 | game_spread | 0.211 | 0.175 | 0.182 | 18 | 83 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA5 | team_total | 0.241 | 0.195 | 0.204 | 21 | 82 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA6 | team_total | 0.115 | 0.075 | 0.082 | 9 | 94 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA2 | team_total | 0.840 | 0.795 | 0.805 | 81 | 22 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA2 | team_total | 0.783 | 0.820 | 0.813 | 83 | 19 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT06FLALA-10 | game_total | 0.089 | 0.065 | 0.069 | 7 | 94 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT06FLALA-2 | game_total | 0.985 | 0.965 | 0.971 | 97 | 4 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA4 | team_total | 0.352 | 0.390 | 0.382 | 40 | 62 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT06FLALA-8 | game_total | 0.263 | 0.235 | 0.240 | 24 | 77 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA3 | team_total | 0.567 | 0.600 | 0.593 | 61 | 41 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT06FLALA-6 | game_total | 0.573 | 0.545 | 0.551 | 55 | 46 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT06FLALA-9 | game_total | 0.185 | 0.165 | 0.169 | 17 | 84 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT06FLALA-3 | game_total | 0.966 | 0.955 | 0.957 | 96 | 5 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT06FLALA-7 | game_total | 0.456 | 0.435 | 0.439 | 44 | 57 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA6 | team_total | 0.077 | 0.090 | 0.087 | 10 | 92 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA5 | team_total | 0.181 | 0.205 | 0.200 | 22 | 81 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT06FLALA-4 | game_total | 0.861 | 0.850 | 0.852 | 86 | 16 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT06FLALA-5 | game_total | 0.779 | 0.775 | 0.776 | 78 | 23 |  | -0.013 | NO_EDGE |
| KXNHL1P-26OCT06FLALA-FLA | period_winner |  | 0.330 |  | 35 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT06FLALA-LA | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT06FLALA-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT06FLALA-FLA2 | period_spread |  | 0.100 |  | 11 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT06FLALA-LA2 | period_spread |  | 0.085 |  | 9 | 92 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT06FLALA-1 | period_total |  | 0.815 |  | 82 | 19 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT06FLALA-2 | period_total |  | 0.520 |  | 53 | 49 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT06FLALA-3 | period_total |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT06FLALA-FLA | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT06FLALA-LA | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT06FLALA-TIE | period_winner |  | 0.305 |  | 33 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT06FLALA-FLA2 | period_spread |  | 0.130 |  | 15 | 89 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT06FLALA-LA2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT06FLALA-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT06FLALA-2 | period_total |  | 0.585 |  | 60 | 43 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT06FLALA-3 | period_total |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT06FLALA-FLA | period_winner |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT06FLALA-LA | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT06FLALA-TIE | period_winner |  | 0.250 |  | 27 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT06FLALA-FLA2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT06FLALA-LA2 | period_spread |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT06FLALA-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT06FLALA-2 | period_total |  | 0.650 |  | 67 | 37 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT06FLALA-3 | period_total |  | 0.370 |  | 39 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLABMARCHAND63-1 | player_assists |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLABMARCHAND63-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLABTKACHUK8-1 | player_assists |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLABTKACHUK8-2 | player_assists |  | 0.050 |  | 9 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLACVERHAEGHE23-1 | player_assists |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLACVERHAEGHE23-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLAMTKACHUK19-1 | player_assists |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLAMTKACHUK19-2 | player_assists |  | 0.075 |  | 12 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLASBENNETT9-1 | player_assists |  | 0.340 |  | 36 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLASBENNETT9-2 | player_assists |  | 0.045 |  | 8 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLASJONES3-1 | player_assists |  | 0.370 |  | 39 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLASJONES3-2 | player_assists |  | 0.060 |  | 11 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLASREINHART13-1 | player_assists |  | 0.390 |  | 41 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-FLASREINHART13-2 | player_assists |  | 0.070 |  | 12 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LAAKEMPE9-1 | player_assists |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LAAKEMPE9-2 | player_assists |  | 0.055 |  | 9 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1 | player_assists |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LAAPANARIN10-1 | player_assists |  | 0.515 |  | 52 | 49 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LAAPANARIN10-2 | player_assists |  | 0.160 |  | 17 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LAAPANARIN10-3 | player_assists |  |  |  | 5 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LABCLARKE92-1 | player_assists |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LABCLARKE92-2 | player_assists |  | 0.050 |  | 9 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LADDOUGHTY8-1 | player_assists |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LADDOUGHTY8-2 | player_assists |  |  |  | 6 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1 | player_assists |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-2 | player_assists |  | 0.055 |  | 9 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LAQBYFIELD55-1 | player_assists |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT06FLALA-LAQBYFIELD55-2 | player_assists |  | 0.050 |  | 9 | 99 |  |  | UNSUPPORTED |
| KXNHLF10G-26OCT06FLALA-Y | game_early_goal |  | 0.570 |  | 58 | 44 |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26OCT06FLALA-FLAALUNDELL15 | first_goal |  | 0.030 |  | 4 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26OCT06FLALA-FLABIMAMA14 | first_goal |  |  |  | 2 |  |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ LAK | 0.557 | 0.580 | 0.172 | 0.220 | 6.25 | 5.96 | 0.995/1.014 | KXNHLTOTAL-26OCT06FLALA-6 -0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Sam Reinhart: 1+ goals NO @ 68c · p 0.7703 (adj 0.7465) · $18.7 · thesis FLA:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 64c · p 0.7859 (adj 0.6846) · $18.7 · thesis LAK:SUPPRESSED
- Alex Laferriere: 1+ goals YES @ 23c · p 0.2813 (adj 0.2672) · $7.98 · thesis LAK:OFFENSE_4PLUS
- Trevor Moore: 1+ goals YES @ 19c · p 0.2301 (adj 0.2176) · $4.62 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ LAK** · priced 159/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 26.39, exp saves 23.09 (sd 6.23), pull risk 0.049
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.81, exp saves 23.61 (sd 6.55), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.214 | 0.370 | 38/64 | +0.130 | STANDARD |
| Brady Tkachuk: 1+ points | 0.410 | 0.550 | 56/46 | +0.113 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.235 | 0.370 | 38/64 | +0.109 | STANDARD |
| Sam Reinhart: 1+ points | 0.456 | 0.585 | 60/43 | +0.097 | STANDARD |
| Artemi Panarin: 1+ assists | 0.389 | 0.515 | 52/49 | +0.103 | STANDARD |
| Alex Laferriere: 1+ points | 0.552 | 0.430 | 44/58 | +0.095 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
