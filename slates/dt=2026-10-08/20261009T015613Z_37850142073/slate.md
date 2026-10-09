# NHL slate 2026-10-08 — RESEARCH_ONLY

generated 2026-10-09T01:56:13Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 1 · markets on board: 3482 · contracts joined: 226 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 201, 'OK': 19, 'NO_EDGE': 6}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 33, 'game_early_goal': 1, 'first_goal': 34, 'game_winner': 2, 'player_goals': 61, 'game_overtime': 1, 'player_points': 46, 'goalie_saves': 1, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TOR @ VGK | 2026-10-09T02:00:00Z | T-<10m | 0.653 | 0.347 | 0.153 | 7.06 | 4.05 | 3.01 | 226 (25/201) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK5 | team_total | 0.389 | 0.305 | 0.321 | 31 | 70 | yes | +0.064 | OK |
| KXNHLTOTAL-26OCT08TORVGK-8 | game_total | 0.386 | 0.305 | 0.320 | 31 | 70 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK4 | team_total | 0.595 | 0.515 | 0.531 | 52 | 49 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT08TORVGK-10 | game_total | 0.157 | 0.095 | 0.105 | 10 | 91 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK6 | team_total | 0.218 | 0.155 | 0.166 | 16 | 85 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK3 | team_total | 0.779 | 0.715 | 0.729 | 72 | 29 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK2 | game_spread | 0.445 | 0.385 | 0.397 | 39 | 62 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT08TORVGK-9 | game_total | 0.290 | 0.230 | 0.241 | 24 | 78 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT08TORVGK-6 | game_total | 0.696 | 0.645 | 0.655 | 65 | 36 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT08TORVGK-7 | game_total | 0.587 | 0.535 | 0.545 | 54 | 47 | yes | +0.029 | OK |
| KXNHLGAME-26OCT08TORVGK-TOR | game_winner | 0.347 | 0.395 | 0.385 | 40 | 61 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK3 | game_spread | 0.306 | 0.265 | 0.273 | 27 | 74 | yes | +0.023 | OK |
| KXNHLGAME-26OCT08TORVGK-VGK | game_winner | 0.653 | 0.615 | 0.623 | 62 | 39 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK2 | team_total | 0.910 | 0.880 | 0.887 | 89 | 13 | yes | +0.013 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR3 | game_spread | 0.100 | 0.125 | 0.120 | 13 | 88 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR2 | game_spread | 0.178 | 0.205 | 0.199 | 21 | 80 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT08TORVGK-5 | game_total | 0.859 | 0.835 | 0.840 | 84 | 17 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT08TORVGK-4 | game_total | 0.918 | 0.905 | 0.908 | 91 | 10 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT08TORVGK-3 | game_total | 0.982 | 0.975 | 0.977 | 98 | 3 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR5 | team_total | 0.197 | 0.185 | 0.187 | 19 | 82 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR6 | team_total | 0.088 | 0.080 | 0.082 | 9 | 93 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR3 | team_total | 0.577 | 0.565 | 0.567 | 57 | 44 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR4 | team_total | 0.361 | 0.355 | 0.356 | 36 | 65 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR2 | team_total | 0.796 | 0.790 | 0.791 | 80 | 22 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT08TORVGK-2 | game_total | 0.994 | 0.990 | 0.991 |  | 3 |  | -0.026 | NO_EDGE |
| KXNHL1P-26OCT08TORVGK-TIE | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT08TORVGK-TOR | period_winner |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT08TORVGK-VGK | period_winner |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT08TORVGK-TOR2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT08TORVGK-VGK2 | period_spread |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT08TORVGK-1 | period_total |  | 0.850 |  | 86 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT08TORVGK-2 | period_total |  | 0.580 |  | 59 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT08TORVGK-3 | period_total |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT08TORVGK-TIE | period_winner |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT08TORVGK-TOR | period_winner |  | 0.290 |  | 31 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT08TORVGK-VGK | period_winner |  | 0.410 |  | 43 | 61 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT08TORVGK-TOR2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT08TORVGK-VGK2 | period_spread |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT08TORVGK-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT08TORVGK-2 | period_total |  | 0.650 |  | 66 | 36 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT08TORVGK-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT08TORVGK-TIE | period_winner |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT08TORVGK-TOR | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT08TORVGK-VGK | period_winner |  | 0.445 |  | 45 | 56 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT08TORVGK-TOR2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT08TORVGK-VGK2 | period_spread |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT08TORVGK-1 | period_total |  | 0.920 |  | 94 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT08TORVGK-2 | period_total |  | 0.680 |  | 70 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT08TORVGK-3 | period_total |  | 0.405 |  | 43 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORAMATTHEWS34-1 | player_assists |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORAMATTHEWS34-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1 | player_assists |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORECOWAN53-1 | player_assists |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1 | player_assists |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-2 | player_assists |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORJMCCABE22-1 | player_assists |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORJROSLOVIC96-1 | player_assists |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORJTAVARES91-1 | player_assists |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORJTAVARES91-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORKMARCHENKO86-1 | player_assists |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORKMARCHENKO86-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORMRIELLY44-1 | player_assists |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORWNYLANDER88-1 | player_assists |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-TORWNYLANDER88-2 | player_assists |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKJEICHEL9-1 | player_assists |  | 0.585 |  | 59 | 42 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKJEICHEL9-2 | player_assists |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKJEICHEL9-3 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKMMARNER93-1 | player_assists |  | 0.575 |  | 58 | 43 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKMMARNER93-2 | player_assists |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKMSTONE61-1 | player_assists |  | 0.490 |  | 50 | 52 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKMSTONE61-2 | player_assists |  | 0.150 |  | 16 | 86 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKNHANIFIN15-1 | player_assists |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKRANDERSSON4-1 | player_assists |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKRANDERSSON4-2 | player_assists |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1 | player_assists |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-2 | player_assists |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT08TORVGK-VGKTHERTL48-1 | player_assists |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TOR @ VGK | 0.653 | 0.658 | 0.153 | 0.201 | 7.06 | 6.35 | 1.003/0.983 | KXNHLTOTAL-26OCT08TORVGK-6 -0.115 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Teddy Blueger: 1+ goals YES @ 8c · p 0.1118 (adj 0.1026) · $4.61 · thesis TOR:OFFENSE_4PLUS
- Darren Raddysh: 1+ assists NO @ 63c · p 0.7212 (adj 0.6731) · $16.92 · thesis TOR:SUPPRESSED
- Auston Matthews: 1+ goals NO @ 65c · p 0.7044 (adj 0.6895) · $13.08 · thesis TOR:SUPPRESSED
- Ivan Barbashev: 1+ assists YES @ 31c · p 0.3828 (adj 0.3439) · $6.46 · thesis VGK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TOR @ VGK** · priced 175/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (CONFIRMED) exp shots 24.89, exp saves 21.96 (sd 6.01), pull risk 0.043
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 31.39, exp saves 26.49 (sd 7.38), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Marchenko: 1+ points | 0.421 | 0.555 | 57/46 | +0.101 | STANDARD |
| Mitch Marner: 1+ assists | 0.442 | 0.575 | 58/43 | +0.111 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.244 | 0.375 | 39/64 | +0.100 | STANDARD |
| Mitch Marner: 2+ points | 0.233 | 0.360 | 37/65 | +0.101 | STANDARD |
| Jack Eichel: 2+ points | 0.274 | 0.395 | 41/62 | +0.089 | STANDARD |
| Darren Raddysh: 1+ points | 0.365 | 0.475 | 48/53 | +0.088 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
