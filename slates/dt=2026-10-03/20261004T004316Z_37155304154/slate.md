# NHL slate 2026-10-03 — RESEARCH_ONLY

generated 2026-10-04T00:43:16Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 13 · simulated (not started): 3 · markets on board: 3752 · contracts joined: 492 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 417, 'OK': 43, 'NO_EDGE': 32}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 70, 'game_early_goal': 3, 'first_goal': 100, 'game_winner': 6, 'player_goals': 99, 'game_overtime': 3, 'player_points': 66, 'goalie_saves': 4, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| STL @ COL | 2026-10-04T01:00:00Z | T-10m | 0.676 | 0.324 | 0.151 | 6.79 | 4.00 | 2.80 | 169 (25/144) | PROBABLE/CONFIRMED |
| CGY @ VAN | 2026-10-04T02:00:00Z | T-60m | 0.468 | 0.532 | 0.174 | 6.29 | 3.04 | 3.25 | 160 (25/135) | PROBABLE/CONFIRMED |
| LAK @ SJS | 2026-10-04T02:00:00Z | T-60m | 0.490 | 0.510 | 0.174 | 6.11 | 3.02 | 3.09 | 163 (25/138) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL4 | team_total | 0.316 | 0.240 | 0.254 | 25 | 77 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT03STLCOL-8 | game_total | 0.346 | 0.275 | 0.289 | 28 | 73 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL3 | team_total | 0.528 | 0.455 | 0.470 | 46 | 55 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL5 | team_total | 0.162 | 0.105 | 0.115 | 11 | 90 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT03STLCOL-7 | game_total | 0.539 | 0.475 | 0.488 | 48 | 53 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT03STLCOL-9 | game_total | 0.252 | 0.195 | 0.206 | 20 | 81 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL2 | team_total | 0.755 | 0.695 | 0.708 | 71 | 32 | yes | +0.031 | OK |
| KXNHLGAME-26OCT03STLCOL-COL | game_winner | 0.676 | 0.725 | 0.716 | 73 | 28 | no | +0.029 | OK |
| KXNHLGAME-26OCT03STLCOL-STL | game_winner | 0.324 | 0.275 | 0.284 | 28 | 73 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT03STLCOL-6 | game_total | 0.654 | 0.605 | 0.615 | 61 | 40 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL6 | team_total | 0.069 | 0.035 | 0.040 | 4 | 97 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL3 | game_spread | 0.327 | 0.375 | 0.365 | 38 | 63 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL2 | game_spread | 0.468 | 0.515 | 0.506 | 52 | 49 | no | +0.025 | OK |
| KXNHLGAME-26OCT03CGYVAN-VAN | game_winner | 0.468 | 0.515 | 0.506 | 52 | 49 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT03LASJ-7 | game_total | 0.429 | 0.475 | 0.466 | 48 | 53 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT03STLCOL-5 | game_total | 0.833 | 0.795 | 0.803 | 80 | 21 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT03STLCOL-STL2 | game_spread | 0.159 | 0.125 | 0.131 | 13 | 88 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT03LASJ-6 | game_total | 0.543 | 0.585 | 0.577 | 59 | 42 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-VAN3 | game_spread | 0.150 | 0.185 | 0.178 | 19 | 82 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT03STLCOL-10 | game_total | 0.136 | 0.095 | 0.102 | 11 | 92 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ4 | team_total | 0.364 | 0.410 | 0.401 | 42 | 60 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT03LASJ-5 | game_total | 0.761 | 0.800 | 0.793 | 81 | 21 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY3 | team_total | 0.631 | 0.595 | 0.602 | 60 | 41 | yes | +0.015 | OK |
| KXNHLGAME-26OCT03CGYVAN-CGY | game_winner | 0.532 | 0.495 | 0.502 | 50 | 51 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT03STLCOL-4 | game_total | 0.901 | 0.875 | 0.881 | 88 | 13 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY4 | team_total | 0.418 | 0.380 | 0.388 | 39 | 63 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT03LASJ-8 | game_total | 0.246 | 0.275 | 0.269 | 28 | 73 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT03STLCOL-STL3 | game_spread | 0.085 | 0.065 | 0.069 | 7 | 94 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT03LASJ-SJ3 | game_spread | 0.161 | 0.185 | 0.180 | 19 | 82 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-CGY2 | game_spread | 0.313 | 0.285 | 0.290 | 29 | 72 | yes | +0.008 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-VAN2 | game_spread | 0.258 | 0.290 | 0.283 | 30 | 72 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ3 | team_total | 0.585 | 0.615 | 0.609 | 62 | 39 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT03LASJ-3 | game_total | 0.961 | 0.975 | 0.973 | 98 | 3 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY6 | team_total | 0.113 | 0.090 | 0.094 | 10 | 92 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ5 | team_total | 0.193 | 0.220 | 0.214 | 23 | 79 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT03STLCOL-3 | game_total | 0.977 | 0.965 | 0.968 | 97 | 4 | yes | +0.005 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-CGY3 | game_spread | 0.195 | 0.175 | 0.179 | 18 | 83 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT03LASJ-4 | game_total | 0.848 | 0.870 | 0.866 | 88 | 14 | no | +0.004 | OK |
| KXNHLGAME-26OCT03LASJ-LA | game_winner | 0.510 | 0.485 | 0.490 | 49 | 52 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-COL6 | team_total | 0.213 | 0.190 | 0.194 | 20 | 82 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY5 | team_total | 0.234 | 0.205 | 0.211 | 22 | 81 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ2 | team_total | 0.798 | 0.825 | 0.820 | 84 | 19 | no | +0.001 | OK |
| KXNHLSPREAD-26OCT03LASJ-SJ2 | game_spread | 0.275 | 0.295 | 0.291 | 30 | 71 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN2 | team_total | 0.800 | 0.825 | 0.820 | 84 | 19 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT03STLCOL-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY2 | team_total | 0.829 | 0.810 | 0.814 | 82 | 20 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ6 | team_total | 0.086 | 0.100 | 0.097 | 11 | 91 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN4 | team_total | 0.375 | 0.400 | 0.395 | 41 | 61 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT03LASJ-9 | game_total | 0.172 | 0.190 | 0.186 | 20 | 82 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT03LASJ-10 | game_total | 0.080 | 0.085 | 0.084 | 9 | 92 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT03LASJ-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-3 | game_total | 0.966 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-9 | game_total | 0.195 | 0.180 | 0.183 | 19 | 83 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-10 | game_total | 0.090 | 0.085 | 0.086 | 9 | 92 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN3 | team_total | 0.590 | 0.615 | 0.610 | 63 | 40 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26OCT03LASJ-SJ | game_winner | 0.490 | 0.505 | 0.502 | 51 | 50 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN6 | team_total | 0.084 | 0.090 | 0.089 | 10 | 92 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03STLCOL-COL3 | team_total | 0.767 | 0.775 | 0.773 | 78 | 23 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-8 | game_total | 0.274 | 0.265 | 0.267 | 27 | 74 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN5 | team_total | 0.199 | 0.210 | 0.208 | 22 | 80 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT03LASJ-LA2 | game_spread | 0.294 | 0.285 | 0.287 | 29 | 72 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03STLCOL-COL2 | team_total | 0.906 | 0.910 | 0.909 | 92 | 10 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT03LASJ-LA3 | game_spread | 0.177 | 0.175 | 0.175 | 18 | 83 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-7 | game_total | 0.463 | 0.455 | 0.457 | 46 | 55 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-5 | game_total | 0.782 | 0.785 | 0.784 | 79 | 22 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-LA6 | team_total | 0.092 | 0.090 | 0.090 | 10 | 92 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-4 | game_total | 0.863 | 0.860 | 0.861 | 87 | 15 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03STLCOL-COL5 | team_total | 0.380 | 0.370 | 0.372 | 38 | 64 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-LA2 | team_total | 0.805 | 0.815 | 0.813 | 83 | 20 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03STLCOL-COL4 | team_total | 0.580 | 0.585 | 0.584 | 59 | 42 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-LA3 | team_total | 0.600 | 0.610 | 0.608 | 62 | 40 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-LA5 | team_total | 0.207 | 0.215 | 0.213 | 23 | 80 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-6 | game_total | 0.574 | 0.575 | 0.575 | 58 | 43 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-LA4 | team_total | 0.386 | 0.395 | 0.393 | 41 | 62 |  | -0.022 | NO_EDGE |
| KXNHL1P-26OCT03STLCOL-COL | period_winner |  | 0.440 |  | 45 | 57 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT03STLCOL-STL | period_winner |  | 0.210 |  | 22 | 80 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT03STLCOL-TIE | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT03STLCOL-COL2 | period_spread |  | 0.170 |  | 19 | 85 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT03STLCOL-STL2 | period_spread |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| STL @ COL | 0.676 | 0.632 | 0.151 | 0.209 | 6.79 | 6.45 | 0.977/1.032 | KXNHLTEAMTOTAL-26OCT03STLCOL-COL5 -0.072 |
| CGY @ VAN | 0.468 | 0.555 | 0.174 | 0.218 | 6.29 | 6.33 | 1.030/0.978 | KXNHLGAME-26OCT03CGYVAN-CGY -0.086 |
| LAK @ SJS | 0.490 | 0.522 | 0.174 | 0.222 | 6.11 | 6.12 | 1.039/0.988 | KXNHLSPREAD-26OCT03LASJ-LA2 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Colorado wins NO @ 28c · p 0.3701 (adj 0.3273) · $8.97 · thesis STL:WINS
- Jimmy Snuggerud: 1+ goals YES @ 24c · p 0.2872 (adj 0.2742) · $4.81 · thesis STL:OFFENSE_4PLUS
- Colorado wins by over 2.5 goals NO @ 63c · p 0.7135 (adj 0.6693) · $7.42 · thesis GAME:TIGHT
- Connor McMichael: 1+ assists NO @ 78c · p 0.8463 (adj 0.8107) · $20.0 · thesis STL:SUPPRESSED
- Zayne Parekh: 1+ goals NO @ 84c · p 0.8998 (adj 0.8836) · $18.08 · thesis CGY:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 25c · p 0.3095 (adj 0.2934) · $8.61 · thesis VAN:OFFENSE_4PLUS
- Paul Cotter: 1+ goals NO @ 83c · p 0.8723 (adj 0.8605) · $18.08 · thesis VAN:SUPPRESSED
- Linus Karlsson: 1+ goals YES @ 22c · p 0.2631 (adj 0.2511) · $5.24 · thesis VAN:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 58c · p 0.8177 (adj 0.6599) · $19.68 · thesis LAK:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 13c · p 0.1968 (adj 0.1789) · $10.63 · thesis SJS:OFFENSE_4PLUS
- Mason Marchment: 1+ assists NO @ 67c · p 0.8085 (adj 0.7152) · $19.68 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**STL @ COL** · priced 116/118 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROBABLE) exp shots 24.45, exp saves 21.49 (sd 5.94), pull risk 0.045
- STL net: Jordan Binnington (CONFIRMED) exp shots 31.38, exp saves 26.45 (sd 7.3), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.343 | 0.530 | 55/49 | +0.150 | STANDARD |
| Cale Makar: 2+ points | 0.185 | 0.360 | 38/66 | +0.140 | STANDARD |
| Cale Makar: 1+ assists | 0.447 | 0.610 | 62/40 | +0.136 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.509 | 0.650 | 66/36 | +0.115 | STANDARD |
| Cale Makar: 1+ points | 0.548 | 0.685 | 73/36 | +0.076 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.159 | 0.295 | 32/73 | +0.098 | STANDARD |

**CGY @ VAN** · priced 106/109 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 28.38, exp saves 24.66 (sd 6.66), pull risk 0.058
- CGY net: Devin Cooley (CONFIRMED) exp shots 28.2, exp saves 24.23 (sd 6.63), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zayne Parekh: 1+ goals | 0.100 | 0.165 | 17/84 | +0.050 | STANDARD |
| Marco Rossi: 1+ goals | 0.309 | 0.245 | 25/76 | +0.046 | STANDARD |
| Joel Farabee: 1+ points | 0.514 | 0.460 | 47/55 | +0.026 | STANDARD |
| Zayne Parekh: 1+ points | 0.389 | 0.440 | 45/57 | +0.024 | STANDARD |
| Linus Karlsson: 1+ goals | 0.263 | 0.215 | 22/79 | +0.031 | STANDARD |
| Paul Cotter: 1+ goals | 0.128 | 0.175 | 18/83 | +0.032 | STANDARD |

**LAK @ SJS** · priced 105/112 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.98, exp saves 24.31 (sd 6.6), pull risk 0.054
- LAK net: Anton Forsberg (PROBABLE) exp shots 26.75, exp saves 23.29 (sd 6.35), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.182 | 0.425 | 43/58 | +0.221 | STANDARD |
| Mason Marchment: 1+ assists | 0.192 | 0.335 | 34/67 | +0.123 | STANDARD |
| Artemi Panarin: 1+ assists | 0.372 | 0.515 | 52/49 | +0.120 | STANDARD |
| Adrian Kempe: 1+ assists | 0.332 | 0.435 | 44/57 | +0.081 | STANDARD |
| Mats Zuccarello: 2+ assists | 0.017 | 0.110 | 12/90 | +0.077 | STANDARD |
| Mason Marchment: 1+ points | 0.398 | 0.490 | 50/52 | +0.065 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
