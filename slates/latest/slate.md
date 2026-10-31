# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-10-31T23:25:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 2 · markets on board: 2808 · contracts joined: 464 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 414, 'OK': 41, 'NO_EDGE': 9}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 69, 'game_early_goal': 2, 'first_goal': 72, 'game_winner': 4, 'player_goals': 126, 'game_overtime': 2, 'player_points': 92, 'goalie_saves': 3, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ DAL | 2026-11-01T00:00:00Z | T-30m | 0.584 | 0.416 | 0.180 | 5.48 | 2.98 | 2.50 | 234 (25/209) | CONFIRMED/CONFIRMED |
| CGY @ COL | 2026-11-01T02:00:00Z | T-90m | 0.681 | 0.319 | 0.164 | 6.21 | 3.68 | 2.53 | 230 (25/205) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.308 | 0.465 | 0.432 | 47 | 54 | no | +0.134 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.454 | 0.605 | 0.575 | 61 | 40 | no | +0.129 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.515 | 0.660 | 0.632 | 67 | 35 | no | +0.119 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.312 | 0.440 | 0.413 | 45 | 57 | no | +0.101 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.319 | 0.215 | 0.234 | 22 | 79 | yes | +0.086 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.681 | 0.785 | 0.766 | 79 | 22 | no | +0.086 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.160 | 0.255 | 0.233 | 26 | 75 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.729 | 0.825 | 0.808 | 84 | 19 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL4 | team_total | 0.360 | 0.435 | 0.420 | 44 | 57 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL3 | game_spread | 0.205 | 0.275 | 0.260 | 28 | 73 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-5 | game_total | 0.677 | 0.745 | 0.732 | 75 | 26 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-6 | game_total | 0.564 | 0.635 | 0.621 | 64 | 37 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.260 | 0.195 | 0.207 | 20 | 81 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL3 | team_total | 0.585 | 0.660 | 0.645 | 67 | 35 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.465 | 0.395 | 0.409 | 40 | 61 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.149 | 0.095 | 0.104 | 10 | 91 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.703 | 0.645 | 0.657 | 65 | 36 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL5 | team_total | 0.181 | 0.240 | 0.227 | 25 | 77 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-7 | game_total | 0.329 | 0.385 | 0.373 | 39 | 62 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL2 | team_total | 0.798 | 0.845 | 0.836 | 85 | 16 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-DAL2 | game_spread | 0.342 | 0.395 | 0.384 | 40 | 61 | no | +0.032 | OK |
| KXNHLGAME-26OCT31CBJDAL-CBJ | game_winner | 0.416 | 0.365 | 0.375 | 37 | 64 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL2 | team_total | 0.886 | 0.935 | 0.927 | 95 | 8 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-4 | game_total | 0.781 | 0.825 | 0.817 | 83 | 18 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-7 | game_total | 0.446 | 0.495 | 0.485 | 50 | 51 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-8 | game_total | 0.259 | 0.305 | 0.295 | 31 | 70 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-5 | game_total | 0.773 | 0.825 | 0.815 | 84 | 19 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-8 | game_total | 0.163 | 0.205 | 0.196 | 21 | 80 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-6 | game_total | 0.438 | 0.485 | 0.476 | 49 | 52 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-4 | game_total | 0.859 | 0.900 | 0.893 | 91 | 11 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5 | team_total | 0.120 | 0.080 | 0.087 | 9 | 93 | yes | +0.024 | OK |
| KXNHLGAME-26OCT31CBJDAL-DAL | game_winner | 0.584 | 0.625 | 0.617 | 63 | 38 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-9 | game_total | 0.103 | 0.135 | 0.128 | 14 | 87 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY3 | game_spread | 0.076 | 0.050 | 0.054 | 6 | 96 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-DAL6 | team_total | 0.074 | 0.100 | 0.094 | 11 | 91 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-3 | game_total | 0.938 | 0.955 | 0.952 | 96 | 5 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-10 | game_total | 0.085 | 0.105 | 0.101 | 11 | 90 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-9 | game_total | 0.182 | 0.210 | 0.204 | 22 | 80 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT31CBJDAL-CBJ2 | game_spread | 0.206 | 0.185 | 0.189 | 19 | 82 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-10 | game_total | 0.041 | 0.055 | 0.052 | 6 | 95 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY6 | team_total | 0.045 | 0.025 | 0.028 | 4 | 99 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT31CBJDAL-2 | game_total | 0.971 | 0.980 | 0.978 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT31CGYCOL-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT31CGYCOL-3 | game_total | 0.964 | 0.975 | 0.973 | 99 | 4 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT31CBJDAL-CBJ3 | game_spread | 0.110 | 0.105 | 0.106 | 11 | 90 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ4 | team_total | 0.248 | 0.255 | 0.254 | 26 | 75 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ6 | team_total | 0.040 | 0.040 | 0.040 | 5 | 97 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ5 | team_total | 0.110 | 0.110 | 0.110 | 12 | 90 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3 | team_total | 0.463 | 0.465 | 0.465 | 47 | 54 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ2 | team_total | 0.709 | 0.710 | 0.710 | 72 | 30 |  | -0.024 | NO_EDGE |
| KXNHL1P-26OCT31CBJDAL-CBJ | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT31CBJDAL-DAL | period_winner |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT31CBJDAL-TIE | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT31CBJDAL-CBJ2 | period_spread |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT31CBJDAL-DAL2 | period_spread |  | 0.110 |  | 13 | 91 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT31CBJDAL-1 | period_total |  | 0.805 |  | 82 | 21 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT31CBJDAL-2 | period_total |  | 0.505 |  | 51 | 50 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT31CBJDAL-3 | period_total |  | 0.225 |  | 23 | 78 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT31CBJDAL-CBJ | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT31CBJDAL-DAL | period_winner |  | 0.405 |  | 42 | 61 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT31CBJDAL-TIE | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT31CBJDAL-CBJ2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT31CBJDAL-DAL2 | period_spread |  | 0.140 |  | 15 | 87 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT31CBJDAL-1 | period_total |  | 0.860 |  | 87 | 15 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT31CBJDAL-2 | period_total |  | 0.570 |  | 58 | 44 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT31CBJDAL-3 | period_total |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT31CBJDAL-CBJ | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT31CBJDAL-DAL | period_winner |  | 0.435 |  | 45 | 58 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT31CBJDAL-TIE | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT31CBJDAL-CBJ2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT31CBJDAL-DAL2 | period_spread |  | 0.190 |  | 21 | 83 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT31CBJDAL-1 | period_total |  | 0.885 |  | 89 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT31CBJDAL-2 | period_total |  | 0.625 |  | 63 | 38 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT31CBJDAL-3 | period_total |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CBJDAL-CBJAFANTILLI19-1 | player_assists |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CBJDAL-CBJAFANTILLI19-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CBJDAL-CBJCCOYLE3-1 | player_assists |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CBJDAL-CBJCCOYLE3-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CBJDAL-CBJCGARLAND83-1 | player_assists |  | 0.190 |  | 20 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CBJDAL-CBJCSILLINGER4-1 | player_assists |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ DAL | 0.584 | 0.534 | 0.180 | 0.224 | 5.48 | 5.92 | 0.995/0.947 | KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3 +0.089 |
| CGY @ COL | 0.681 | 0.694 | 0.164 | 0.189 | 6.21 | 6.54 | 0.979/0.992 | KXNHLTOTAL-26OCT31CGYCOL-7 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Damon Severson: 1+ goals YES @ 6c · p 0.1066 (adj 0.0937) · $6.88 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1869 (adj 0.1714) · $8.87 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 19c · p 0.2535 (adj 0.2364) · $10.75 · thesis CBJ:OFFENSE_4PLUS
- Valeri Nichushkin: 1+ assists NO @ 71c · p 0.7868 (adj 0.7459) · $20.0 · thesis CBJ:SUPPRESSED
- Cale Makar: 1+ goals NO @ 73c · p 0.803 (adj 0.7835) · $20.0 · thesis COL:SUPPRESSED
- Calgary over 3.5 goals scored YES @ 20c · p 0.2829 (adj 0.2389) · $6.85 · thesis CGY:OFFENSE_4PLUS
- Colorado wins by over 1.5 goals NO @ 40c · p 0.5235 (adj 0.44) · $2.78 · thesis GAME:TIGHT
- Gavin Brindley: 1+ goals NO @ 87c · p 0.8997 (adj 0.891) · $20.0 · thesis DIFFUSE

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CBJ @ DAL** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.99, exp saves 21.79 (sd 6.04), pull risk 0.05
- CBJ net: Jet Greaves (CONFIRMED) exp shots 26.69, exp saves 23.11 (sd 6.39), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Sillinger: 1+ points | 0.354 | 0.255 | 27/76 | +0.070 | STANDARD |
| Mikko Rantanen: 2+ points | 0.218 | 0.315 | 33/70 | +0.067 | STANDARD |
| Miro Heiskanen: 1+ points | 0.447 | 0.535 | 54/47 | +0.066 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.436 | 0.520 | 53/49 | +0.056 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.213 | 0.295 | 30/71 | +0.062 | STANDARD |
| Jason Robertson: 2+ points | 0.245 | 0.325 | 34/69 | +0.050 | STANDARD |

**CGY @ COL** · priced 178/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.33, exp saves 23.3 (sd 6.25), pull risk 0.043
- CGY net: Arsenii Sergeev (CONFIRMED) exp shots 33.08, exp saves 27.7 (sd 7.76), pull risk 0.103

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 2+ points | 0.209 | 0.345 | 36/67 | +0.106 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.399 | 0.525 | 53/48 | +0.104 | STANDARD |
| Cale Makar: 1+ assists | 0.474 | 0.595 | 60/41 | +0.099 | STANDARD |
| Cale Makar: 1+ points | 0.579 | 0.690 | 70/32 | +0.086 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.536 | 0.640 | 65/37 | +0.077 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.156 | 0.255 | 27/76 | +0.071 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
