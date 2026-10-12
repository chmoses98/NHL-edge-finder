# NHL slate 2026-10-12 — RESEARCH_ONLY

generated 2026-10-12T23:28:25Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 1 · markets on board: 2947 · contracts joined: 226 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 201, 'OK': 15, 'NO_EDGE': 10}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 31, 'game_early_goal': 1, 'first_goal': 36, 'game_winner': 2, 'player_goals': 64, 'game_overtime': 1, 'player_points': 42, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ MIN | 2026-10-13T00:00:00Z | T-30m | 0.543 | 0.457 | 0.181 | 6.06 | 3.16 | 2.90 | 226 (25/201) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT12VGKMIN-MIN | game_winner | 0.543 | 0.495 | 0.505 | 50 | 51 | yes | +0.026 | OK |
| KXNHLGAME-26OCT12VGKMIN-VGK | game_winner | 0.457 | 0.505 | 0.495 | 51 | 50 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK4 | team_total | 0.342 | 0.385 | 0.376 | 39 | 62 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-VGK2 | game_spread | 0.246 | 0.285 | 0.277 | 29 | 72 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-VGK3 | game_spread | 0.145 | 0.175 | 0.169 | 18 | 83 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-MIN2 | game_spread | 0.319 | 0.285 | 0.292 | 29 | 72 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK3 | team_total | 0.562 | 0.600 | 0.592 | 61 | 41 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK2 | team_total | 0.778 | 0.805 | 0.800 | 81 | 20 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT12VGKMIN-4 | game_total | 0.843 | 0.865 | 0.861 | 87 | 14 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK5 | team_total | 0.173 | 0.200 | 0.194 | 21 | 81 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN4 | team_total | 0.403 | 0.375 | 0.381 | 38 | 63 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN3 | team_total | 0.621 | 0.595 | 0.600 | 60 | 41 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN5 | team_total | 0.215 | 0.195 | 0.199 | 20 | 81 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT12VGKMIN-5 | game_total | 0.755 | 0.775 | 0.771 | 78 | 23 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN6 | team_total | 0.098 | 0.085 | 0.087 | 9 | 92 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT12VGKMIN-3 | game_total | 0.960 | 0.970 | 0.968 | 98 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN2 | team_total | 0.817 | 0.805 | 0.807 | 81 | 20 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-6 | game_total | 0.538 | 0.555 | 0.552 | 56 | 45 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK6 | team_total | 0.072 | 0.080 | 0.078 | 9 | 93 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT12VGKMIN-MIN3 | game_spread | 0.194 | 0.185 | 0.187 | 19 | 82 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-10 | game_total | 0.074 | 0.070 | 0.071 | 8 | 94 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-9 | game_total | 0.168 | 0.165 | 0.166 | 17 | 84 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-7 | game_total | 0.426 | 0.435 | 0.433 | 44 | 57 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-8 | game_total | 0.237 | 0.240 | 0.239 | 25 | 77 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT12VGKMIN-MIN | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT12VGKMIN-TIE | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT12VGKMIN-VGK | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT12VGKMIN-MIN2 | period_spread |  | 0.095 |  | 10 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT12VGKMIN-VGK2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT12VGKMIN-1 | period_total |  | 0.820 |  | 83 | 19 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT12VGKMIN-2 | period_total |  | 0.525 |  | 53 | 48 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT12VGKMIN-3 | period_total |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT12VGKMIN-MIN | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT12VGKMIN-TIE | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT12VGKMIN-VGK | period_winner |  | 0.340 |  | 36 | 68 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT12VGKMIN-MIN2 | period_spread |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT12VGKMIN-VGK2 | period_spread |  | 0.115 |  | 12 | 89 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT12VGKMIN-1 | period_total |  | 0.880 |  | 89 | 13 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT12VGKMIN-2 | period_total |  | 0.590 |  | 60 | 42 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT12VGKMIN-3 | period_total |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT12VGKMIN-MIN | period_winner |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT12VGKMIN-TIE | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT12VGKMIN-VGK | period_winner |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT12VGKMIN-MIN2 | period_spread |  | 0.155 |  | 17 | 86 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT12VGKMIN-VGK2 | period_spread |  | 0.150 |  | 16 | 86 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT12VGKMIN-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT12VGKMIN-2 | period_total |  | 0.650 |  | 66 | 36 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT12VGKMIN-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINBCOLEMAN20-1 | player_assists |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINJERIKSSONEK14-1 | player_assists |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINJERIKSSONEK14-2 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINJSPURGEON46-1 | player_assists |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINKKAPRIZOV97-1 | player_assists |  | 0.465 |  | 47 | 54 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINKKAPRIZOV97-2 | player_assists |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINMBOLDY12-1 | player_assists |  | 0.445 |  | 45 | 56 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINMBOLDY12-2 | player_assists |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINMSHABANOV49-1 | player_assists |  | 0.265 |  | 30 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINQHUGHES43-1 | player_assists |  | 0.545 |  | 55 | 46 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINQHUGHES43-2 | player_assists |  | 0.185 |  | 20 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINQHUGHES43-3 | player_assists |  | 0.035 |  | 4 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-MINRHARTMAN38-1 | player_assists |  | 0.230 |  | 25 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKBHOWDEN21-1 | player_assists |  | 0.180 |  | 20 | 84 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKBMCNABB3-1 | player_assists |  | 0.130 |  | 24 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKIBARBASHEV49-1 | player_assists |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKIBARBASHEV49-2 | player_assists |  | 0.040 |  | 5 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKJEICHEL9-1 | player_assists |  | 0.535 |  | 54 | 47 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKJEICHEL9-2 | player_assists |  | 0.185 |  | 20 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKJEICHEL9-3 | player_assists |  | 0.035 |  | 4 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1 | player_assists |  | 0.475 |  | 48 | 53 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2 | player_assists |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKMSTONE61-1 | player_assists |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKMSTONE61-2 | player_assists |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKSTHEODORE27-1 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKSTHEODORE27-2 | player_assists |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKTCONNELLY24-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKTCONNELLY24-2 | player_assists |  | 0.040 |  | 5 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKTHERTL48-1 | player_assists |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKTHERTL48-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12VGKMIN-VGKWKARLSSON71-1 | player_assists |  | 0.250 |  | 27 | 77 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ MIN | 0.543 | 0.532 | 0.181 | 0.218 | 6.06 | 6.16 | 0.991/1.003 | KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK4 +0.022 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Rieger Lorenz: 1+ goals YES @ 9c · p 0.1342 (adj 0.1219) · $6.52 · thesis MIN:OFFENSE_4PLUS
- Trevor Connelly: 1+ assists NO @ 73c · p 0.8225 (adj 0.7737) · $20.0 · thesis VGK:SUPPRESSED
- Braeden Bowman: 1+ goals YES @ 12c · p 0.1596 (adj 0.1484) · $5.78 · thesis VGK:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0742 (adj 0.0669) · $3.24 · thesis VGK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VGK @ MIN** · priced 173/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 29.04, exp saves 25.33 (sd 6.81), pull risk 0.054
- VGK net: Carter Hart (PROJECTED) exp shots 27.87, exp saves 24.03 (sd 6.63), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.416 | 0.535 | 54/47 | +0.097 | STANDARD |
| Brayden McNabb: 1+ assists | 0.242 | 0.130 | 24/98 | -0.010 | STANDARD |
| Jack Eichel: 2+ points | 0.216 | 0.315 | 32/69 | +0.079 | STANDARD |
| Trevor Connelly: 1+ assists | 0.177 | 0.275 | 28/73 | +0.079 | PRIOR_HEAVY |
| Jack Eichel: 1+ points | 0.580 | 0.675 | 68/33 | +0.075 | STANDARD |
| Trevor Connelly: 1+ points | 0.325 | 0.415 | 42/59 | +0.068 | PRIOR_HEAVY |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
