# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-21T02:27:21Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 1 · markets on board: 3572 · contracts joined: 252 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 227, 'OK': 16, 'NO_EDGE': 9}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 44, 'game_early_goal': 1, 'first_goal': 37, 'game_winner': 2, 'player_goals': 63, 'game_overtime': 1, 'player_points': 55, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ VGK | 2026-10-21T02:30:00Z | T-<10m | 0.539 | 0.461 | 0.181 | 5.92 | 3.08 | 2.84 | 252 (25/227) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT20TBVGK-5 | game_total | 0.736 | 0.795 | 0.784 | 80 | 21 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB4 | team_total | 0.324 | 0.385 | 0.373 | 39 | 62 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB3 | team_total | 0.547 | 0.605 | 0.593 | 61 | 40 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB2 | team_total | 0.764 | 0.820 | 0.810 | 83 | 19 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT20TBVGK-4 | game_total | 0.828 | 0.875 | 0.867 | 88 | 13 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT20TBVGK-TB3 | game_spread | 0.138 | 0.185 | 0.175 | 19 | 82 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT20TBVGK-6 | game_total | 0.512 | 0.565 | 0.554 | 57 | 44 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT20TBVGK-7 | game_total | 0.402 | 0.455 | 0.444 | 46 | 55 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT20TBVGK-TB2 | game_spread | 0.246 | 0.295 | 0.285 | 30 | 71 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB5 | team_total | 0.165 | 0.205 | 0.196 | 21 | 80 | no | +0.024 | OK |
| KXNHLGAME-26OCT20TBVGK-TB | game_winner | 0.461 | 0.505 | 0.496 | 51 | 50 | no | +0.022 | OK |
| KXNHLGAME-26OCT20TBVGK-VGK | game_winner | 0.539 | 0.495 | 0.504 | 50 | 51 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT20TBVGK-8 | game_total | 0.220 | 0.260 | 0.252 | 27 | 75 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT20TBVGK-9 | game_total | 0.153 | 0.175 | 0.170 | 18 | 83 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB6 | team_total | 0.069 | 0.085 | 0.082 | 9 | 92 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT20TBVGK-3 | game_total | 0.956 | 0.965 | 0.963 | 97 | 4 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-VGK5 | team_total | 0.199 | 0.220 | 0.216 | 23 | 79 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT20TBVGK-2 | game_total | 0.979 | 0.990 | 0.988 |  | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT20TBVGK-10 | game_total | 0.068 | 0.080 | 0.077 | 9 | 93 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT20TBVGK-VGK2 | game_spread | 0.312 | 0.295 | 0.298 | 30 | 71 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT20TBVGK-VGK6 | team_total | 0.089 | 0.085 | 0.086 | 9 | 92 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT20TBVGK-VGK2 | team_total | 0.809 | 0.815 | 0.814 | 82 | 19 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT20TBVGK-VGK3 | game_spread | 0.191 | 0.185 | 0.186 | 19 | 82 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT20TBVGK-VGK3 | team_total | 0.604 | 0.615 | 0.613 | 62 | 39 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT20TBVGK-VGK4 | team_total | 0.385 | 0.385 | 0.385 | 39 | 62 |  | -0.021 | NO_EDGE |
| KXNHL1P-26OCT20TBVGK-TB | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT20TBVGK-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT20TBVGK-VGK | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT20TBVGK-TB2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT20TBVGK-VGK2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT20TBVGK-1 | period_total |  | 0.845 |  | 85 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT20TBVGK-2 | period_total |  | 0.565 |  | 57 | 44 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT20TBVGK-3 | period_total |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT20TBVGK-TB | period_winner |  | 0.350 |  | 40 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT20TBVGK-TIE | period_winner |  | 0.310 |  | 35 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT20TBVGK-VGK | period_winner |  | 0.345 |  | 39 | 70 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT20TBVGK-TB2 | period_spread |  | 0.125 |  | 13 | 88 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT20TBVGK-VGK2 | period_spread |  | 0.120 |  | 14 | 90 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT20TBVGK-1 | period_total |  | 0.895 |  | 92 | 13 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT20TBVGK-2 | period_total |  | 0.610 |  | 62 | 40 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT20TBVGK-3 | period_total |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT20TBVGK-TB | period_winner |  | 0.370 |  | 39 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT20TBVGK-TIE | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT20TBVGK-VGK | period_winner |  | 0.360 |  | 38 | 66 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT20TBVGK-TB2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT20TBVGK-VGK2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT20TBVGK-1 | period_total |  | 0.915 |  | 94 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT20TBVGK-2 | period_total |  | 0.665 |  | 67 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT20TBVGK-3 | period_total |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBACIRELLI71-1 | player_assists |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBACIRELLI71-2 | player_assists |  | 0.040 |  | 6 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBBHAGEL38-1 | player_assists |  | 0.435 |  | 45 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBBHAGEL38-2 | player_assists |  | 0.095 |  | 13 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBBPOINT21-1 | player_assists |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBBPOINT21-2 | player_assists |  | 0.060 |  | 10 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBECERNAK81-1 | player_assists |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBGGONCALVES93-1 | player_assists |  | 0.265 |  | 30 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBGGONCALVES93-2 | player_assists |  | 0.050 |  | 8 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBIMIKHEYEV95-1 | player_assists |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1 | player_assists |  | 0.365 |  | 39 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBJCARLSON74-2 | player_assists |  | 0.060 |  | 10 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBJGUENTZEL59-1 | player_assists |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBJGUENTZEL59-2 | player_assists |  | 0.070 |  | 11 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBJMOSER90-1 | player_assists |  | 0.140 |  | 27 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBNKUCHEROV86-1 | player_assists |  | 0.570 |  | 58 | 44 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBNKUCHEROV86-2 | player_assists |  | 0.210 |  | 22 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBNKUCHEROV86-3 | player_assists |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBPHOLMBERG29-1 | player_assists |  | 0.235 |  | 27 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBRMCDONAGH27-1 | player_assists |  | 0.110 |  | 21 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBVHEDMAN77-1 | player_assists |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-TBZGIRGENSONS28-1 | player_assists |  | 0.140 |  | 15 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-VGKBHOWDEN21-1 | player_assists |  | 0.200 |  | 21 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-VGKBMCNABB3-1 | player_assists |  | 0.150 |  | 25 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-VGKIBARBASHEV49-1 | player_assists |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-VGKIBARBASHEV49-2 | player_assists |  | 0.050 |  | 8 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-VGKJEICHEL9-1 | player_assists |  | 0.540 |  | 55 | 47 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-VGKJEICHEL9-2 | player_assists |  | 0.185 |  | 20 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-VGKJEICHEL9-3 | player_assists |  | 0.040 |  | 6 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-VGKMMARNER93-1 | player_assists |  | 0.485 |  | 49 | 52 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT20TBVGK-VGKMMARNER93-2 | player_assists |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ VGK | 0.539 | 0.583 | 0.181 | 0.217 | 5.92 | 6.09 | 1.003/0.952 | KXNHLTEAMTOTAL-26OCT20TBVGK-VGK3 +0.055 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Brayden McNabb: 1+ goals YES @ 5c · p 0.0802 (adj 0.0714) · $4.12 · thesis VGK:OFFENSE_4PLUS
- Brett Howden: 1+ goals YES @ 19c · p 0.2331 (adj 0.2186) · $5.23 · thesis VGK:OFFENSE_4PLUS
- Trevor Connelly: 1+ assists NO @ 71c · p 0.7806 (adj 0.7428) · $19.48 · thesis VGK:SUPPRESSED
- Nikita Kucherov: 1+ goals NO @ 65c · p 0.6958 (adj 0.6818) · $11.56 · thesis TBL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TBL @ VGK** · priced 196/201 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.99, exp saves 23.6 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.35, exp saves 22.57 (sd 6.35), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andrei Vasilevskiy: 27+ saves | 0.256 | 0.420 | 43/59 | +0.137 |  |
| Nikita Kucherov: 2+ points | 0.243 | 0.380 | 39/63 | +0.111 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.437 | 0.570 | 58/44 | +0.106 | STANDARD |
| Brayden McNabb: 1+ assists | 0.270 | 0.150 | 25/95 | +0.007 | STANDARD |
| Erik Cernak: 1+ points | 0.230 | 0.125 | 19/94 | +0.029 | STANDARD |
| Jack Eichel: 1+ assists | 0.444 | 0.540 | 55/47 | +0.069 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
