# NHL slate 2026-10-08 — RESEARCH_ONLY

generated 2026-10-09T00:16:54Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 2 · markets on board: 3873 · contracts joined: 437 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 387, 'OK': 43, 'NO_EDGE': 7}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 63, 'game_early_goal': 2, 'first_goal': 68, 'game_winner': 4, 'player_goals': 120, 'game_overtime': 2, 'player_points': 81, 'goalie_saves': 3, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| COL @ CGY | 2026-10-09T01:00:00Z | T-30m | 0.435 | 0.565 | 0.183 | 5.61 | 2.61 | 3.00 | 211 (25/186) | CONFIRMED/PROBABLE |
| TOR @ VGK | 2026-10-09T02:00:00Z | T-90m | 0.653 | 0.347 | 0.153 | 7.06 | 4.05 | 3.01 | 226 (25/201) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL4 | team_total | 0.362 | 0.545 | 0.508 | 55 | 46 | no | +0.160 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL3 | team_total | 0.586 | 0.745 | 0.716 | 75 | 26 | no | +0.141 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL5 | team_total | 0.184 | 0.330 | 0.297 | 34 | 68 | no | +0.120 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL3 | game_spread | 0.195 | 0.335 | 0.303 | 34 | 67 | no | +0.119 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL2 | game_spread | 0.326 | 0.465 | 0.436 | 47 | 54 | no | +0.116 | OK |
| KXNHLGAME-26OCT08COLCGY-CGY | game_winner | 0.435 | 0.305 | 0.329 | 31 | 70 | yes | +0.110 | OK |
| KXNHLGAME-26OCT08COLCGY-COL | game_winner | 0.565 | 0.695 | 0.671 | 70 | 31 | no | +0.110 | OK |
| KXNHLTOTAL-26OCT08COLCGY-6 | game_total | 0.461 | 0.585 | 0.560 | 59 | 42 | no | +0.102 | OK |
| KXNHLTOTAL-26OCT08COLCGY-5 | game_total | 0.695 | 0.805 | 0.786 | 81 | 20 | no | +0.094 | OK |
| KXNHLTOTAL-26OCT08COLCGY-7 | game_total | 0.349 | 0.465 | 0.441 | 47 | 54 | no | +0.094 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL2 | team_total | 0.800 | 0.890 | 0.875 | 90 | 12 | no | +0.073 | OK |
| KXNHLTOTAL-26OCT08TORVGK-8 | game_total | 0.386 | 0.295 | 0.312 | 30 | 71 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL6 | team_total | 0.080 | 0.165 | 0.144 | 17 | 84 | no | +0.070 | OK |
| KXNHLTOTAL-26OCT08COLCGY-8 | game_total | 0.178 | 0.265 | 0.246 | 27 | 74 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT08TORVGK-9 | game_total | 0.290 | 0.205 | 0.220 | 21 | 80 | yes | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK4 | team_total | 0.595 | 0.505 | 0.523 | 51 | 50 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT08COLCGY-4 | game_total | 0.795 | 0.875 | 0.862 | 88 | 13 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK5 | team_total | 0.389 | 0.305 | 0.321 | 31 | 70 | yes | +0.064 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY2 | game_spread | 0.222 | 0.145 | 0.158 | 15 | 86 | yes | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK3 | team_total | 0.779 | 0.705 | 0.721 | 71 | 30 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT08TORVGK-10 | game_total | 0.157 | 0.095 | 0.105 | 10 | 91 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT08COLCGY-9 | game_total | 0.120 | 0.185 | 0.170 | 19 | 82 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT08TORVGK-7 | game_total | 0.587 | 0.515 | 0.530 | 52 | 49 | yes | +0.049 | OK |
| KXNHLTOTAL-26OCT08TORVGK-6 | game_total | 0.696 | 0.625 | 0.640 | 63 | 38 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK6 | team_total | 0.218 | 0.150 | 0.162 | 16 | 86 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK2 | game_spread | 0.445 | 0.385 | 0.397 | 39 | 62 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY3 | game_spread | 0.119 | 0.075 | 0.082 | 8 | 93 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK2 | team_total | 0.910 | 0.865 | 0.875 | 87 | 14 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT08COLCGY-3 | game_total | 0.941 | 0.975 | 0.970 | 98 | 3 | no | +0.027 | OK |
| KXNHLGAME-26OCT08TORVGK-TOR | game_winner | 0.347 | 0.395 | 0.385 | 40 | 61 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK3 | game_spread | 0.306 | 0.265 | 0.273 | 27 | 74 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT08TORVGK-4 | game_total | 0.918 | 0.885 | 0.892 | 89 | 12 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT08TORVGK-5 | game_total | 0.859 | 0.825 | 0.832 | 83 | 18 | yes | +0.019 | OK |
| KXNHLGAME-26OCT08TORVGK-VGK | game_winner | 0.653 | 0.615 | 0.623 | 62 | 39 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT08COLCGY-10 | game_total | 0.051 | 0.080 | 0.073 | 9 | 93 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR3 | game_spread | 0.100 | 0.125 | 0.120 | 13 | 88 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR2 | game_spread | 0.178 | 0.205 | 0.199 | 21 | 80 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR5 | team_total | 0.197 | 0.175 | 0.179 | 18 | 83 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT08COLCGY-2 | game_total | 0.973 | 0.985 | 0.983 | 99 | 2 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY4 | team_total | 0.277 | 0.255 | 0.259 | 26 | 75 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3 | team_total | 0.491 | 0.460 | 0.466 | 47 | 55 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR6 | team_total | 0.088 | 0.075 | 0.077 | 8 | 93 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT08TORVGK-3 | game_total | 0.982 | 0.975 | 0.977 | 98 | 3 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT08TORVGK-2 | game_total | 0.994 | 0.990 | 0.991 |  | 1 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY2 | team_total | 0.728 | 0.710 | 0.714 | 72 | 30 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY6 | team_total | 0.046 | 0.040 | 0.041 | 5 | 97 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR3 | team_total | 0.577 | 0.565 | 0.567 | 57 | 44 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY5 | team_total | 0.125 | 0.120 | 0.121 | 13 | 89 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR4 | team_total | 0.361 | 0.350 | 0.352 | 36 | 66 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR2 | team_total | 0.796 | 0.790 | 0.791 | 80 | 22 |  | -0.015 | NO_EDGE |
| KXNHL1P-26OCT08COLCGY-CGY | period_winner |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT08COLCGY-COL | period_winner |  | 0.435 |  | 44 | 57 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT08COLCGY-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT08COLCGY-CGY2 | period_spread |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT08COLCGY-COL2 | period_spread |  | 0.155 |  | 17 | 86 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT08COLCGY-1 | period_total |  | 0.835 |  | 84 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT08COLCGY-2 | period_total |  | 0.565 |  | 57 | 44 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT08COLCGY-3 | period_total |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT08COLCGY-CGY | period_winner |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT08COLCGY-COL | period_winner |  | 0.440 |  | 45 | 57 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT08COLCGY-TIE | period_winner |  | 0.290 |  | 31 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT08COLCGY-CGY2 | period_spread |  | 0.065 |  | 7 | 94 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT08COLCGY-COL2 | period_spread |  | 0.200 |  | 21 | 81 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT08COLCGY-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT08COLCGY-2 | period_total |  | 0.630 |  | 64 | 38 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT08COLCGY-3 | period_total |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT08COLCGY-CGY | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT08COLCGY-COL | period_winner |  | 0.490 |  | 50 | 52 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT08COLCGY-TIE | period_winner |  | 0.250 |  | 27 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT08COLCGY-CGY2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT08COLCGY-COL2 | period_spread |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT08COLCGY-1 | period_total |  | 0.890 |  | 90 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT08COLCGY-2 | period_total |  | 0.660 |  | 68 | 36 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT08COLCGY-3 | period_total |  | 0.380 |  | 40 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08COLCGY-CGYJFARABEE86-1 | player_assists |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08COLCGY-CGYMBACKLUND11-1 | player_assists |  | 0.225 |  | 24 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08COLCGY-CGYMCORONATO27-1 | player_assists |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08COLCGY-CGYMCORONATO27-2 | player_assists |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08COLCGY-CGYMFROST16-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08COLCGY-CGYMFROST16-2 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| COL @ CGY | 0.435 | 0.433 | 0.183 | 0.218 | 5.61 | 6.25 | 0.978/0.972 | KXNHLTOTAL-26OCT08COLCGY-7 +0.111 |
| TOR @ VGK | 0.653 | 0.658 | 0.153 | 0.201 | 7.06 | 6.35 | 1.003/0.983 | KXNHLTOTAL-26OCT08TORVGK-6 -0.115 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Nathan MacKinnon: 1+ goals NO @ 56c · p 0.644 (adj 0.6218) · $16.62 · thesis COL:SUPPRESSED
- Nathan MacKinnon: 2+ points NO @ 47c · p 0.7214 (adj 0.5291) · $13.38 · thesis COL:SUPPRESSED
- Colorado wins by over 1.5 goals NO @ 54c · p 0.6624 (adj 0.5796) · $5.6 · thesis GAME:TIGHT
- Auston Matthews: 1+ goals NO @ 65c · p 0.7044 (adj 0.6895) · $15.7 · thesis TOR:SUPPRESSED
- Auston Matthews: 1+ assists NO @ 60c · p 0.685 (adj 0.64) · $14.3 · thesis TOR:SUPPRESSED
- Ivan Barbashev: 1+ assists YES @ 31c · p 0.3828 (adj 0.3439) · $5.96 · thesis VGK:OFFENSE_4PLUS
- Shea Theodore: 1+ assists YES @ 35c · p 0.4305 (adj 0.3852) · $6.78 · thesis VGK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**COL @ CGY** · priced 160/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 32.7, exp saves 27.85 (sd 7.5), pull risk 0.072
- COL net: Scott Wedgewood (PROBABLE) exp shots 26.32, exp saves 22.94 (sd 6.27), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.279 | 0.535 | 54/47 | +0.234 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.451 | 0.665 | 67/34 | +0.193 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.119 | 0.325 | 34/69 | +0.176 | STANDARD |
| Cale Makar: 1+ assists | 0.409 | 0.605 | 62/41 | +0.164 | STANDARD |
| Nathan MacKinnon: 1+ points | 0.644 | 0.825 | 84/19 | +0.155 | STANDARD |
| Cale Makar: 2+ points | 0.149 | 0.330 | 34/68 | +0.155 | STANDARD |

**TOR @ VGK** · priced 175/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (CONFIRMED) exp shots 24.89, exp saves 21.96 (sd 6.01), pull risk 0.043
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 31.39, exp saves 26.49 (sd 7.38), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Marchenko: 1+ points | 0.421 | 0.555 | 57/46 | +0.101 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.244 | 0.375 | 39/64 | +0.100 | STANDARD |
| Mitch Marner: 1+ assists | 0.442 | 0.570 | 58/44 | +0.101 | STANDARD |
| Mitch Marner: 2+ points | 0.233 | 0.345 | 35/66 | +0.092 | STANDARD |
| Darren Raddysh: 1+ points | 0.365 | 0.475 | 48/53 | +0.088 | STANDARD |
| Darren Raddysh: 1+ assists | 0.279 | 0.385 | 39/62 | +0.085 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
