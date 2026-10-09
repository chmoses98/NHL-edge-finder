# NHL slate 2026-10-08 — RESEARCH_ONLY

generated 2026-10-09T01:08:12Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 1 · markets on board: 4073 · contracts joined: 226 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 201, 'OK': 22, 'NO_EDGE': 3}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 33, 'game_early_goal': 1, 'first_goal': 34, 'game_winner': 2, 'player_goals': 61, 'game_overtime': 1, 'player_points': 46, 'goalie_saves': 1, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TOR @ VGK | 2026-10-09T02:00:00Z | T-30m | 0.653 | 0.347 | 0.153 | 7.06 | 4.05 | 3.01 | 226 (25/201) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT08TORVGK-8 | game_total | 0.386 | 0.295 | 0.312 | 30 | 71 | yes | +0.071 | OK |
| KXNHLTOTAL-26OCT08TORVGK-9 | game_total | 0.290 | 0.205 | 0.220 | 21 | 80 | yes | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK4 | team_total | 0.595 | 0.505 | 0.523 | 51 | 50 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK5 | team_total | 0.389 | 0.305 | 0.321 | 31 | 70 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK3 | team_total | 0.779 | 0.705 | 0.721 | 71 | 30 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT08TORVGK-10 | game_total | 0.157 | 0.095 | 0.105 | 10 | 91 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT08TORVGK-6 | game_total | 0.696 | 0.625 | 0.640 | 63 | 38 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK6 | team_total | 0.218 | 0.150 | 0.162 | 16 | 86 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT08TORVGK-7 | game_total | 0.587 | 0.525 | 0.537 | 53 | 48 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK2 | game_spread | 0.445 | 0.385 | 0.397 | 39 | 62 | yes | +0.038 | OK |
| KXNHLGAME-26OCT08TORVGK-TOR | game_winner | 0.347 | 0.395 | 0.385 | 40 | 61 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK3 | game_spread | 0.306 | 0.265 | 0.273 | 27 | 74 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK2 | team_total | 0.910 | 0.875 | 0.883 | 88 | 13 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT08TORVGK-4 | game_total | 0.918 | 0.885 | 0.892 | 89 | 12 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT08TORVGK-5 | game_total | 0.859 | 0.825 | 0.832 | 83 | 18 | yes | +0.019 | OK |
| KXNHLGAME-26OCT08TORVGK-VGK | game_winner | 0.653 | 0.615 | 0.623 | 62 | 39 | yes | +0.016 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR3 | game_spread | 0.100 | 0.125 | 0.120 | 13 | 88 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR2 | game_spread | 0.178 | 0.205 | 0.199 | 21 | 80 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR5 | team_total | 0.197 | 0.170 | 0.175 | 18 | 84 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT08TORVGK-2 | game_total | 0.994 | 0.980 | 0.984 | 99 | 3 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR6 | team_total | 0.088 | 0.075 | 0.077 | 8 | 93 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT08TORVGK-3 | game_total | 0.982 | 0.975 | 0.977 | 98 | 3 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR3 | team_total | 0.577 | 0.565 | 0.567 | 57 | 44 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR4 | team_total | 0.361 | 0.345 | 0.348 | 36 | 67 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR2 | team_total | 0.796 | 0.790 | 0.791 | 80 | 22 |  | -0.015 | NO_EDGE |
| KXNHL1P-26OCT08TORVGK-TIE | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT08TORVGK-TOR | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT08TORVGK-VGK | period_winner |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT08TORVGK-TOR2 | period_spread |  | 0.075 |  | 8 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT08TORVGK-VGK2 | period_spread |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT08TORVGK-1 | period_total |  | 0.845 |  | 85 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT08TORVGK-2 | period_total |  | 0.565 |  | 57 | 44 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT08TORVGK-3 | period_total |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT08TORVGK-TIE | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT08TORVGK-TOR | period_winner |  | 0.290 |  | 31 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT08TORVGK-VGK | period_winner |  | 0.405 |  | 42 | 61 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT08TORVGK-TOR2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT08TORVGK-VGK2 | period_spread |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT08TORVGK-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT08TORVGK-2 | period_total |  | 0.645 |  | 66 | 37 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT08TORVGK-3 | period_total |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT08TORVGK-TIE | period_winner |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT08TORVGK-TOR | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT08TORVGK-VGK | period_winner |  | 0.445 |  | 45 | 56 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT08TORVGK-TOR2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT08TORVGK-VGK2 | period_spread |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT08TORVGK-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT08TORVGK-2 | period_total |  | 0.680 |  | 70 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT08TORVGK-3 | period_total |  | 0.400 |  | 42 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORAMATTHEWS34-1 | player_assists |  | 0.400 |  | 42 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORAMATTHEWS34-2 | player_assists |  | 0.070 |  | 11 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1 | player_assists |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-2 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORECOWAN53-1 | player_assists |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1 | player_assists |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORJMCCABE22-1 | player_assists |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORJROSLOVIC96-1 | player_assists |  | 0.240 |  | 26 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORJTAVARES91-1 | player_assists |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORJTAVARES91-2 | player_assists |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORKMARCHENKO86-1 | player_assists |  | 0.370 |  | 39 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORKMARCHENKO86-2 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORMRIELLY44-1 | player_assists |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORWNYLANDER88-1 | player_assists |  | 0.415 |  | 42 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORWNYLANDER88-2 | player_assists |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKJEICHEL9-1 | player_assists |  | 0.575 |  | 58 | 43 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKJEICHEL9-2 | player_assists |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKJEICHEL9-3 | player_assists |  | 0.055 |  | 6 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKMMARNER93-1 | player_assists |  | 0.575 |  | 58 | 43 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKMMARNER93-2 | player_assists |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKMSTONE61-1 | player_assists |  | 0.480 |  | 49 | 53 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKMSTONE61-2 | player_assists |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKNHANIFIN15-1 | player_assists |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKRANDERSSON4-1 | player_assists |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKRANDERSSON4-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1 | player_assists |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-2 | player_assists |  | 0.065 |  | 9 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKTHERTL48-1 | player_assists |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TOR @ VGK | 0.653 | 0.658 | 0.153 | 0.201 | 7.06 | 6.35 | 1.003/0.983 | KXNHLTOTAL-26OCT08TORVGK-6 -0.115 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Parker Wotherspoon: 1+ goals YES @ 3c · p 0.0537 (adj 0.0465) · $3.11 · thesis DIFFUSE
- Brayden McNabb: 1+ goals YES @ 6c · p 0.088 (adj 0.0797) · $3.79 · thesis VGK:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 8c · p 0.1118 (adj 0.1026) · $4.34 · thesis TOR:OFFENSE_4PLUS
- Auston Matthews: 1+ goals NO @ 65c · p 0.7044 (adj 0.6895) · $18.05 · thesis TOR:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TOR @ VGK** · priced 175/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (CONFIRMED) exp shots 24.89, exp saves 21.96 (sd 6.01), pull risk 0.043
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 31.39, exp saves 26.49 (sd 7.38), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Marchenko: 1+ points | 0.421 | 0.555 | 57/46 | +0.101 | STANDARD |
| Mitch Marner: 1+ assists | 0.442 | 0.575 | 58/43 | +0.111 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.244 | 0.370 | 39/65 | +0.090 | STANDARD |
| Mitch Marner: 2+ points | 0.233 | 0.345 | 35/66 | +0.092 | STANDARD |
| Darren Raddysh: 1+ points | 0.365 | 0.475 | 48/53 | +0.088 | STANDARD |
| Jack Eichel: 2+ points | 0.274 | 0.380 | 39/63 | +0.079 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
