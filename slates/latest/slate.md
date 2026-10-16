# NHL slate 2026-10-15 — RESEARCH_ONLY

generated 2026-10-16T01:51:33Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 1 · markets on board: 4557 · contracts joined: 239 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 214, 'OK': 17, 'NO_EDGE': 8}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 36, 'game_early_goal': 1, 'first_goal': 37, 'game_winner': 2, 'player_goals': 64, 'game_overtime': 1, 'player_points': 49, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CGY @ VGK | 2026-10-16T02:00:00Z | T-<10m | 0.665 | 0.335 | 0.158 | 6.30 | 3.70 | 2.61 | 239 (25/214) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT15CGYVGK-CGY | game_winner | 0.335 | 0.275 | 0.286 | 28 | 73 | yes | +0.041 | OK |
| KXNHLGAME-26OCT15CGYVGK-VGK | game_winner | 0.665 | 0.725 | 0.714 | 73 | 28 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK3 | game_spread | 0.304 | 0.365 | 0.352 | 37 | 64 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK2 | game_spread | 0.446 | 0.495 | 0.485 | 50 | 51 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY5 | team_total | 0.131 | 0.095 | 0.101 | 10 | 91 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY4 | team_total | 0.277 | 0.235 | 0.243 | 24 | 77 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-CGY2 | game_spread | 0.161 | 0.125 | 0.132 | 13 | 88 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4 | team_total | 0.521 | 0.570 | 0.560 | 58 | 44 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 | team_total | 0.317 | 0.360 | 0.351 | 37 | 65 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK2 | team_total | 0.879 | 0.905 | 0.900 | 91 | 10 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY3 | team_total | 0.480 | 0.440 | 0.448 | 45 | 57 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK3 | team_total | 0.725 | 0.755 | 0.749 | 76 | 25 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY6 | team_total | 0.054 | 0.035 | 0.038 | 4 | 97 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-CGY3 | game_spread | 0.085 | 0.065 | 0.069 | 7 | 94 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY2 | team_total | 0.724 | 0.690 | 0.697 | 70 | 32 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK6 | team_total | 0.164 | 0.185 | 0.181 | 19 | 82 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT15CGYVGK-3 | game_total | 0.965 | 0.975 | 0.973 | 98 | 3 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT15CGYVGK-4 | game_total | 0.865 | 0.875 | 0.873 | 88 | 13 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-5 | game_total | 0.784 | 0.800 | 0.797 | 81 | 21 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-7 | game_total | 0.463 | 0.475 | 0.473 | 48 | 53 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-10 | game_total | 0.094 | 0.090 | 0.091 | 10 | 92 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-8 | game_total | 0.273 | 0.275 | 0.275 | 28 | 73 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-6 | game_total | 0.582 | 0.585 | 0.584 | 59 | 42 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-9 | game_total | 0.192 | 0.190 | 0.190 | 20 | 82 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT15CGYVGK-CGY | period_winner |  | 0.225 |  | 24 | 79 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT15CGYVGK-TIE | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT15CGYVGK-VGK | period_winner |  | 0.455 |  | 47 | 56 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT15CGYVGK-CGY2 | period_spread |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT15CGYVGK-VGK2 | period_spread |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT15CGYVGK-1 | period_total |  | 0.835 |  | 84 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT15CGYVGK-2 | period_total |  | 0.605 |  | 64 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT15CGYVGK-3 | period_total |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT15CGYVGK-CGY | period_winner |  | 0.225 |  | 24 | 79 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT15CGYVGK-TIE | period_winner |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT15CGYVGK-VGK | period_winner |  | 0.470 |  | 49 | 55 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT15CGYVGK-CGY2 | period_spread |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT15CGYVGK-VGK2 | period_spread |  | 0.220 |  | 24 | 80 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT15CGYVGK-1 | period_total |  | 0.900 |  | 92 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT15CGYVGK-2 | period_total |  | 0.620 |  | 63 | 39 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT15CGYVGK-3 | period_total |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT15CGYVGK-CGY | period_winner |  | 0.220 |  | 23 | 79 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT15CGYVGK-TIE | period_winner |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT15CGYVGK-VGK | period_winner |  | 0.515 |  | 53 | 50 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT15CGYVGK-CGY2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT15CGYVGK-VGK2 | period_spread |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT15CGYVGK-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT15CGYVGK-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT15CGYVGK-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-CGYASUNIEV61-1 | player_assists |  | 0.190 |  | 21 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-CGYJFARABEE86-1 | player_assists |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-CGYKBAHL7-1 | player_assists |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-CGYMBACKLUND11-1 | player_assists |  | 0.210 |  | 23 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-CGYMCORONATO27-1 | player_assists |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-CGYMCORONATO27-2 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-CGYMFROST16-1 | player_assists |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-CGYMGRIDIN92-1 | player_assists |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-CGYRSTROME22-1 | player_assists |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-CGYSNEMEC71-1 | player_assists |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-CGYYSHARANGOVICH17-1 | player_assists |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-CGYZPAREKH19-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKBHOWDEN21-1 | player_assists |  | 0.220 |  | 23 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKBMCNABB3-1 | player_assists |  | 0.225 |  | 24 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKIBARBASHEV49-1 | player_assists |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKIBARBASHEV49-2 | player_assists |  | 0.080 |  | 10 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKJEICHEL9-1 | player_assists |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKJEICHEL9-2 | player_assists |  | 0.225 |  | 24 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKJEICHEL9-3 | player_assists |  | 0.050 |  | 7 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKMMARNER93-1 | player_assists |  | 0.555 |  | 56 | 45 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKMMARNER93-2 | player_assists |  | 0.190 |  | 21 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKMMARNER93-3 | player_assists |  |  |  | 5 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKMSTONE61-1 | player_assists |  | 0.490 |  | 50 | 52 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKMSTONE61-2 | player_assists |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKNHANIFIN15-1 | player_assists |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKNHANIFIN15-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKRANDERSSON4-1 | player_assists |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKRANDERSSON4-2 | player_assists |  |  |  | 5 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKSTHEODORE27-1 | player_assists |  | 0.410 |  | 42 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKSTHEODORE27-2 | player_assists |  | 0.090 |  | 11 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1 | player_assists |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CGY @ VGK | 0.665 | 0.660 | 0.158 | 0.207 | 6.30 | 6.19 | 1.003/1.006 | KXNHLTOTAL-26OCT15CGYVGK-6 -0.029 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 3 recommended · full analysis in card.md / packet.json `thesis_card`

- Mitch Marner: 1+ goals NO @ 67c · p 0.74 (adj 0.7212) · $15.9 · thesis VGK:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 6c · p 0.085 (adj 0.0788) · $3.63 · thesis VGK:OFFENSE_4PLUS
- Trevor Connelly: 1+ assists NO @ 65c · p 0.7766 (adj 0.6878) · $14.1 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CGY @ VGK** · priced 187/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.2, exp saves 23.24 (sd 6.25), pull risk 0.041
- CGY net: Dustin Wolf (CONFIRMED) exp shots 30.19, exp saves 25.42 (sd 7.17), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Trevor Connelly: 1+ assists | 0.223 | 0.360 | 37/65 | +0.111 | PRIOR_HEAVY |
| Jack Eichel: 1+ assists | 0.466 | 0.595 | 60/41 | +0.107 | STANDARD |
| Jack Eichel: 2+ points | 0.272 | 0.395 | 41/62 | +0.092 | STANDARD |
| Mitch Marner: 2+ points | 0.222 | 0.345 | 35/66 | +0.102 | STANDARD |
| Mitch Marner: 1+ assists | 0.435 | 0.555 | 56/45 | +0.098 | STANDARD |
| Trevor Connelly: 1+ points | 0.391 | 0.510 | 52/50 | +0.091 | PRIOR_HEAVY |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
