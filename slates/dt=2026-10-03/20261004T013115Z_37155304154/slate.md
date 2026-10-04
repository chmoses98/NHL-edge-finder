# NHL slate 2026-10-03 — RESEARCH_ONLY

generated 2026-10-04T01:31:15Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 13 · simulated (not started): 2 · markets on board: 3852 · contracts joined: 323 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 273, 'OK': 21, 'NO_EDGE': 29}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 42, 'game_early_goal': 2, 'first_goal': 69, 'game_winner': 4, 'player_goals': 68, 'game_overtime': 2, 'player_points': 39, 'goalie_saves': 3, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CGY @ VAN | 2026-10-04T02:00:00Z | T-10m | 0.468 | 0.532 | 0.174 | 6.29 | 3.04 | 3.25 | 160 (25/135) | PROBABLE/CONFIRMED |
| LAK @ SJS | 2026-10-04T02:00:00Z | T-10m | 0.490 | 0.510 | 0.174 | 6.11 | 3.02 | 3.09 | 163 (25/138) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT03LASJ-7 | game_total | 0.429 | 0.475 | 0.466 | 48 | 53 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT03LASJ-6 | game_total | 0.543 | 0.585 | 0.577 | 59 | 42 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-VAN3 | game_spread | 0.150 | 0.185 | 0.178 | 19 | 82 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ4 | team_total | 0.364 | 0.405 | 0.397 | 41 | 60 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-VAN2 | game_spread | 0.258 | 0.295 | 0.287 | 30 | 71 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT03LASJ-5 | game_total | 0.761 | 0.795 | 0.789 | 80 | 21 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY3 | team_total | 0.631 | 0.595 | 0.602 | 60 | 41 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT03LASJ-4 | game_total | 0.848 | 0.875 | 0.870 | 88 | 13 | no | +0.014 | OK |
| KXNHLGAME-26OCT03CGYVAN-VAN | game_winner | 0.468 | 0.505 | 0.498 | 51 | 50 | no | +0.014 | OK |
| KXNHLGAME-26OCT03CGYVAN-CGY | game_winner | 0.532 | 0.495 | 0.502 | 50 | 51 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY4 | team_total | 0.418 | 0.385 | 0.392 | 39 | 62 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT03LASJ-8 | game_total | 0.246 | 0.275 | 0.269 | 28 | 73 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT03LASJ-SJ3 | game_spread | 0.161 | 0.185 | 0.180 | 19 | 82 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-CGY2 | game_spread | 0.313 | 0.285 | 0.290 | 29 | 72 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ3 | team_total | 0.585 | 0.615 | 0.609 | 62 | 39 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT03LASJ-3 | game_total | 0.961 | 0.975 | 0.973 | 98 | 3 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ5 | team_total | 0.193 | 0.220 | 0.214 | 23 | 79 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-CGY3 | game_spread | 0.195 | 0.175 | 0.179 | 18 | 83 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY5 | team_total | 0.234 | 0.210 | 0.215 | 22 | 80 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ2 | team_total | 0.798 | 0.825 | 0.820 | 84 | 19 | no | +0.001 | OK |
| KXNHLSPREAD-26OCT03LASJ-SJ2 | game_spread | 0.275 | 0.295 | 0.291 | 30 | 71 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN2 | team_total | 0.800 | 0.825 | 0.820 | 84 | 19 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY2 | team_total | 0.829 | 0.810 | 0.814 | 82 | 20 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ6 | team_total | 0.086 | 0.105 | 0.101 | 12 | 91 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN4 | team_total | 0.375 | 0.400 | 0.395 | 41 | 61 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT03LASJ-9 | game_total | 0.172 | 0.190 | 0.186 | 20 | 82 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-5 | game_total | 0.782 | 0.795 | 0.793 | 80 | 21 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY6 | team_total | 0.113 | 0.095 | 0.098 | 11 | 92 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT03LASJ-10 | game_total | 0.080 | 0.085 | 0.084 | 9 | 92 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT03LASJ-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-3 | game_total | 0.966 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-9 | game_total | 0.195 | 0.180 | 0.183 | 19 | 83 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-10 | game_total | 0.090 | 0.085 | 0.086 | 9 | 92 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN3 | team_total | 0.590 | 0.615 | 0.610 | 63 | 40 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26OCT03LASJ-SJ | game_winner | 0.490 | 0.505 | 0.502 | 51 | 50 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26OCT03LASJ-LA | game_winner | 0.510 | 0.495 | 0.498 | 50 | 51 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN6 | team_total | 0.084 | 0.095 | 0.093 | 11 | 92 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-8 | game_total | 0.274 | 0.265 | 0.267 | 27 | 74 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN5 | team_total | 0.199 | 0.210 | 0.208 | 22 | 80 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT03LASJ-LA2 | game_spread | 0.294 | 0.285 | 0.287 | 29 | 72 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT03LASJ-LA3 | game_spread | 0.177 | 0.175 | 0.175 | 18 | 83 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-7 | game_total | 0.463 | 0.455 | 0.457 | 46 | 55 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-4 | game_total | 0.863 | 0.860 | 0.861 | 87 | 15 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-LA2 | team_total | 0.805 | 0.815 | 0.813 | 83 | 20 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-LA6 | team_total | 0.092 | 0.095 | 0.094 | 11 | 92 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-LA3 | team_total | 0.600 | 0.610 | 0.608 | 62 | 40 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-LA5 | team_total | 0.207 | 0.210 | 0.209 | 22 | 80 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-6 | game_total | 0.574 | 0.575 | 0.575 | 58 | 43 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-LA4 | team_total | 0.386 | 0.390 | 0.389 | 40 | 62 |  | -0.022 | NO_EDGE |
| KXNHL1P-26OCT03CGYVAN-CGY | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT03CGYVAN-TIE | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT03CGYVAN-VAN | period_winner |  | 0.330 |  | 35 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT03CGYVAN-CGY2 | period_spread |  | 0.100 |  | 13 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT03CGYVAN-VAN2 | period_spread |  | 0.110 |  | 13 | 91 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT03CGYVAN-1 | period_total |  | 0.815 |  | 82 | 19 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT03CGYVAN-2 | period_total |  | 0.550 |  | 56 | 46 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT03CGYVAN-3 | period_total |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT03CGYVAN-CGY | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT03CGYVAN-TIE | period_winner |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT03CGYVAN-VAN | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT03CGYVAN-CGY2 | period_spread |  | 0.110 |  | 14 | 92 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT03CGYVAN-VAN2 | period_spread |  | 0.120 |  | 15 | 91 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT03CGYVAN-1 | period_total |  | 0.890 |  | 92 | 14 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT03CGYVAN-2 | period_total |  | 0.605 |  | 63 | 42 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT03CGYVAN-3 | period_total |  | 0.340 |  | 36 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT03CGYVAN-CGY | period_winner |  | 0.360 |  | 38 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT03CGYVAN-TIE | period_winner |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT03CGYVAN-VAN | period_winner |  | 0.370 |  | 39 | 65 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT03CGYVAN-CGY2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT03CGYVAN-VAN2 | period_spread |  | 0.165 |  | 19 | 86 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT03CGYVAN-1 | period_total |  | 0.910 |  | 94 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT03CGYVAN-2 | period_total |  | 0.660 |  | 68 | 36 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT03CGYVAN-3 | period_total |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT03CGYVAN-CGYJFARABEE86-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT03CGYVAN-CGYJFARABEE86-2 | player_assists |  | 0.040 |  | 6 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT03CGYVAN-CGYMCORONATO27-1 | player_assists |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT03CGYVAN-CGYMCORONATO27-2 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT03CGYVAN-CGYMFROST16-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT03CGYVAN-CGYMFROST16-2 | player_assists |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CGY @ VAN | 0.468 | 0.555 | 0.174 | 0.218 | 6.29 | 6.33 | 1.030/0.978 | KXNHLGAME-26OCT03CGYVAN-CGY -0.086 |
| LAK @ SJS | 0.490 | 0.522 | 0.174 | 0.222 | 6.11 | 6.12 | 1.039/0.988 | KXNHLSPREAD-26OCT03LASJ-LA2 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Zayne Parekh: 1+ goals NO @ 84c · p 0.8998 (adj 0.8836) · $20.0 · thesis CGY:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 25c · p 0.3095 (adj 0.2934) · $10.05 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 22c · p 0.2631 (adj 0.2511) · $6.04 · thesis VAN:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 19c · p 0.2226 (adj 0.2132) · $3.95 · thesis VAN:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 58c · p 0.8177 (adj 0.6599) · $19.68 · thesis LAK:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 13c · p 0.1968 (adj 0.1789) · $10.63 · thesis SJS:OFFENSE_4PLUS
- Mason Marchment: 1+ assists NO @ 67c · p 0.8085 (adj 0.7152) · $19.68 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CGY @ VAN** · priced 106/109 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 28.38, exp saves 24.66 (sd 6.66), pull risk 0.058
- CGY net: Devin Cooley (CONFIRMED) exp shots 28.2, exp saves 24.23 (sd 6.63), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zayne Parekh: 1+ goals | 0.100 | 0.165 | 17/84 | +0.050 | STANDARD |
| Marco Rossi: 1+ goals | 0.309 | 0.245 | 25/76 | +0.046 | STANDARD |
| Zayne Parekh: 1+ points | 0.389 | 0.440 | 45/57 | +0.024 | STANDARD |
| Joel Farabee: 1+ points | 0.514 | 0.465 | 48/55 | +0.016 | STANDARD |
| Linus Karlsson: 1+ goals | 0.263 | 0.215 | 22/79 | +0.031 | STANDARD |
| Joel Farabee: 1+ assists | 0.349 | 0.305 | 31/70 | +0.025 | STANDARD |

**LAK @ SJS** · priced 105/112 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.98, exp saves 24.31 (sd 6.6), pull risk 0.054
- LAK net: Anton Forsberg (PROBABLE) exp shots 26.75, exp saves 23.29 (sd 6.35), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.182 | 0.425 | 43/58 | +0.221 | STANDARD |
| Mason Marchment: 1+ assists | 0.192 | 0.335 | 34/67 | +0.123 | STANDARD |
| Artemi Panarin: 1+ assists | 0.372 | 0.515 | 52/49 | +0.120 | STANDARD |
| Anton Forsberg: 26+ saves | 0.354 | 0.495 | 52/53 | +0.098 |  |
| Yaroslav Askarov: 28+ saves | 0.304 | 0.435 | 47/60 | +0.079 |  |
| Adrian Kempe: 1+ assists | 0.332 | 0.435 | 44/57 | +0.081 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
