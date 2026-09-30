# NHL slate 2026-09-29 — RESEARCH_ONLY

generated 2026-09-30T02:16:35Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 1 · markets on board: 2792 · contracts joined: 195 (unjoined to any game: 1484)
gates: {'UNSUPPORTED': 170, 'OK': 18, 'NO_EDGE': 7}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 23, 'game_early_goal': 1, 'first_goal': 32, 'game_winner': 2, 'player_goals': 56, 'game_overtime': 1, 'player_points': 31, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ VGK | 2026-09-30T02:30:00Z | T-10m | 0.612 | 0.388 | 0.171 | 6.04 | 3.37 | 2.66 | 195 (25/170) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26SEP29CHIVGK-CHI | game_winner | 0.388 | 0.295 | 0.313 | 30 | 71 | yes | +0.074 | OK |
| KXNHLGAME-26SEP29CHIVGK-VGK | game_winner | 0.612 | 0.705 | 0.687 | 71 | 30 | no | +0.074 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK2 | game_spread | 0.386 | 0.475 | 0.457 | 48 | 53 | no | +0.067 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK3 | game_spread | 0.248 | 0.335 | 0.316 | 34 | 67 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK4 | team_total | 0.448 | 0.535 | 0.518 | 54 | 47 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK3 | team_total | 0.664 | 0.730 | 0.718 | 74 | 28 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK5 | team_total | 0.255 | 0.320 | 0.306 | 33 | 69 | no | +0.040 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI2 | game_spread | 0.193 | 0.145 | 0.154 | 15 | 86 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI4 | team_total | 0.288 | 0.240 | 0.249 | 25 | 77 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK2 | team_total | 0.849 | 0.885 | 0.878 | 89 | 12 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI3 | team_total | 0.499 | 0.455 | 0.464 | 46 | 55 | yes | +0.022 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-5 | game_total | 0.749 | 0.785 | 0.778 | 79 | 22 | no | +0.019 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI3 | game_spread | 0.103 | 0.075 | 0.080 | 8 | 93 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI6 | team_total | 0.056 | 0.035 | 0.038 | 4 | 97 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI5 | team_total | 0.139 | 0.110 | 0.115 | 12 | 90 | yes | +0.011 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-4 | game_total | 0.841 | 0.865 | 0.860 | 87 | 14 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI2 | team_total | 0.735 | 0.700 | 0.707 | 71 | 31 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK6 | team_total | 0.121 | 0.160 | 0.151 | 18 | 86 | no | +0.011 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-8 | game_total | 0.239 | 0.255 | 0.252 | 26 | 75 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-6 | game_total | 0.536 | 0.555 | 0.551 | 56 | 45 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-3 | game_total | 0.957 | 0.955 | 0.955 | 96 | 5 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-10 | game_total | 0.074 | 0.070 | 0.071 | 8 | 94 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-9 | game_total | 0.162 | 0.170 | 0.168 | 18 | 84 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-7 | game_total | 0.425 | 0.435 | 0.433 | 44 | 57 |  | -0.012 | NO_EDGE |
| KXNHL1P-26SEP29CHIVGK-CHI | period_winner |  | 0.235 |  | 24 | 77 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP29CHIVGK-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP29CHIVGK-VGK | period_winner |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP29CHIVGK-CHI2 | period_spread |  | 0.065 |  | 10 | 97 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP29CHIVGK-VGK2 | period_spread |  | 0.160 |  | 18 | 86 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26SEP29CHIVGK-1 | period_total |  | 0.825 |  | 83 | 18 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26SEP29CHIVGK-2 | period_total |  | 0.540 |  | 55 | 47 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26SEP29CHIVGK-3 | period_total |  | 0.240 |  | 26 | 78 |  |  | UNSUPPORTED |
| KXNHL2P-26SEP29CHIVGK-CHI | period_winner |  | 0.230 |  | 24 | 78 |  |  | UNSUPPORTED |
| KXNHL2P-26SEP29CHIVGK-TIE | period_winner |  | 0.285 |  | 31 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26SEP29CHIVGK-VGK | period_winner |  | 0.455 |  | 47 | 56 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26SEP29CHIVGK-CHI2 | period_spread |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26SEP29CHIVGK-VGK2 | period_spread |  | 0.195 |  | 22 | 83 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26SEP29CHIVGK-1 | period_total |  | 0.880 |  | 91 | 15 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26SEP29CHIVGK-2 | period_total |  | 0.610 |  | 64 | 42 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26SEP29CHIVGK-3 | period_total |  | 0.330 |  | 35 | 69 |  |  | UNSUPPORTED |
| KXNHL3P-26SEP29CHIVGK-CHI | period_winner |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHL3P-26SEP29CHIVGK-TIE | period_winner |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26SEP29CHIVGK-VGK | period_winner |  | 0.475 |  | 49 | 54 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26SEP29CHIVGK-CHI2 | period_spread |  | 0.085 |  | 12 | 95 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26SEP29CHIVGK-VGK2 | period_spread |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26SEP29CHIVGK-1 | period_total |  | 0.900 |  | 93 | 13 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26SEP29CHIVGK-2 | period_total |  | 0.645 |  | 68 | 39 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26SEP29CHIVGK-3 | period_total |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-CHIBBYRAM24-1 | player_assists |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-CHIBBYRAM24-2 | player_assists |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-CHIFNAZAR91-1 | player_assists |  | 0.220 |  | 24 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-CHIPKANE88-1 | player_assists |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-CHIPKANE88-2 | player_assists |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-CHITBERTUZZI59-1 | player_assists |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKBHOWDEN21-1 | player_assists |  | 0.180 |  | 20 | 84 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKIBARBASHEV49-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKIBARBASHEV49-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKJEICHEL9-1 | player_assists |  | 0.495 |  | 51 | 52 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKJEICHEL9-2 | player_assists |  | 0.160 |  | 17 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKMMARNER93-1 | player_assists |  | 0.475 |  | 48 | 53 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKMMARNER93-2 | player_assists |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKMSTONE61-1 | player_assists |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKMSTONE61-2 | player_assists |  | 0.095 |  | 10 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKRANDERSSON4-1 | player_assists |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKRANDERSSON4-2 | player_assists |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKSTHEODORE27-1 | player_assists |  | 0.435 |  | 45 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKSTHEODORE27-2 | player_assists |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKTHERTL48-1 | player_assists |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKTHERTL48-2 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKVOLOFSSON95-1 | player_assists |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29CHIVGK-VGKWKARLSSON71-1 | player_assists |  | 0.250 |  | 27 | 77 |  |  | UNSUPPORTED |
| KXNHLF10G-26SEP29CHIVGK-Y | game_early_goal |  | 0.585 |  | 59 | 42 |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26SEP29CHIVGK-CHIALEVSHUNOV55 | first_goal |  | 0.010 |  | 2 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26SEP29CHIVGK-CHIAMANGIAPANE26 | first_goal |  | 0.030 |  | 3 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26SEP29CHIVGK-CHIAVLASIC72 | first_goal |  | 0.010 |  | 2 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26SEP29CHIVGK-CHIBBYRAM24 | first_goal |  | 0.030 |  | 3 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26SEP29CHIVGK-CHICSMITH22 | first_goal |  | 0.010 |  | 2 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26SEP29CHIVGK-CHIFNAZAR91 | first_goal |  | 0.040 |  | 4 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26SEP29CHIVGK-CHIICOLE28 | first_goal |  | 0.010 |  | 1 |  |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ VGK | 0.612 | 0.662 | 0.171 | 0.206 | 6.04 | 6.20 | 1.003/0.987 | KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK4 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
