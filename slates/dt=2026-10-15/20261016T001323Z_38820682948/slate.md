# NHL slate 2026-10-15 — RESEARCH_ONLY

generated 2026-10-16T00:13:23Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 2 · markets on board: 4821 · contracts joined: 481 (unjoined to any game: 1871)
gates: {'UNSUPPORTED': 431, 'OK': 32, 'NO_EDGE': 18}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 72, 'game_early_goal': 2, 'first_goal': 74, 'game_winner': 4, 'player_goals': 129, 'game_overtime': 2, 'player_points': 98, 'goalie_saves': 6, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ EDM | 2026-10-16T01:00:00Z | T-30m | 0.557 | 0.443 | 0.166 | 6.64 | 3.51 | 3.13 | 242 (25/217) | CONFIRMED/CONFIRMED |
| CGY @ VGK | 2026-10-16T02:00:00Z | T-90m | 0.665 | 0.335 | 0.158 | 6.30 | 3.70 | 2.61 | 239 (25/214) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT15UTAEDM-UTA | game_winner | 0.443 | 0.515 | 0.501 | 52 | 49 | no | +0.049 | OK |
| KXNHLGAME-26OCT15UTAEDM-EDM | game_winner | 0.557 | 0.485 | 0.499 | 49 | 52 | yes | +0.049 | OK |
| KXNHLGAME-26OCT15CGYVGK-CGY | game_winner | 0.335 | 0.275 | 0.286 | 28 | 73 | yes | +0.041 | OK |
| KXNHLGAME-26OCT15CGYVGK-VGK | game_winner | 0.665 | 0.725 | 0.714 | 73 | 28 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT15UTAEDM-UTA2 | game_spread | 0.248 | 0.305 | 0.293 | 31 | 70 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT15UTAEDM-UTA3 | game_spread | 0.145 | 0.195 | 0.184 | 20 | 81 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT15UTAEDM-EDM2 | game_spread | 0.345 | 0.295 | 0.305 | 30 | 71 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK3 | game_spread | 0.304 | 0.355 | 0.345 | 36 | 65 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY4 | team_total | 0.277 | 0.235 | 0.243 | 24 | 77 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-CGY2 | game_spread | 0.161 | 0.125 | 0.132 | 13 | 88 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-UTA2 | team_total | 0.809 | 0.845 | 0.838 | 85 | 16 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM5 | team_total | 0.283 | 0.245 | 0.252 | 25 | 76 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM3 | team_total | 0.685 | 0.645 | 0.653 | 65 | 36 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-UTA4 | team_total | 0.394 | 0.435 | 0.427 | 44 | 57 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-UTA3 | team_total | 0.605 | 0.645 | 0.637 | 65 | 36 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK2 | game_spread | 0.446 | 0.485 | 0.477 | 49 | 52 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 | team_total | 0.317 | 0.360 | 0.351 | 37 | 65 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM6 | team_total | 0.143 | 0.110 | 0.116 | 12 | 90 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK2 | team_total | 0.879 | 0.910 | 0.904 | 92 | 10 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY5 | team_total | 0.131 | 0.105 | 0.110 | 11 | 90 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY3 | team_total | 0.480 | 0.445 | 0.452 | 45 | 56 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK3 | team_total | 0.725 | 0.755 | 0.749 | 76 | 25 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4 | team_total | 0.521 | 0.565 | 0.556 | 58 | 45 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY6 | team_total | 0.054 | 0.035 | 0.038 | 4 | 97 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-CGY3 | game_spread | 0.085 | 0.065 | 0.069 | 7 | 94 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM4 | team_total | 0.477 | 0.445 | 0.451 | 45 | 56 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-UTA5 | team_total | 0.217 | 0.250 | 0.243 | 26 | 76 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY2 | team_total | 0.724 | 0.690 | 0.697 | 70 | 32 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK6 | team_total | 0.164 | 0.190 | 0.184 | 20 | 82 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT15UTAEDM-5 | game_total | 0.815 | 0.835 | 0.831 | 84 | 17 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT15CGYVGK-3 | game_total | 0.965 | 0.975 | 0.973 | 98 | 3 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-UTA6 | team_total | 0.101 | 0.115 | 0.112 | 12 | 89 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT15UTAEDM-2 | game_total | 0.990 | 0.990 | 0.990 |  | 1 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT15UTAEDM-EDM3 | game_spread | 0.219 | 0.205 | 0.208 | 21 | 80 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-4 | game_total | 0.865 | 0.875 | 0.873 | 88 | 13 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT15UTAEDM-3 | game_total | 0.972 | 0.975 | 0.975 | 98 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT15UTAEDM-10 | game_total | 0.123 | 0.115 | 0.116 | 12 | 89 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT15UTAEDM-4 | game_total | 0.889 | 0.900 | 0.898 | 91 | 11 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-5 | game_total | 0.784 | 0.800 | 0.797 | 81 | 21 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM2 | team_total | 0.859 | 0.845 | 0.848 | 86 | 17 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT15UTAEDM-8 | game_total | 0.325 | 0.315 | 0.317 | 32 | 69 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-8 | game_total | 0.273 | 0.265 | 0.267 | 27 | 74 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-10 | game_total | 0.094 | 0.090 | 0.091 | 10 | 92 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-9 | game_total | 0.192 | 0.195 | 0.194 | 20 | 81 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT15UTAEDM-9 | game_total | 0.238 | 0.235 | 0.236 | 24 | 77 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT15UTAEDM-6 | game_total | 0.629 | 0.635 | 0.634 | 64 | 37 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT15UTAEDM-7 | game_total | 0.520 | 0.525 | 0.524 | 53 | 48 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-6 | game_total | 0.582 | 0.585 | 0.584 | 59 | 42 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT15CGYVGK-7 | game_total | 0.463 | 0.465 | 0.465 | 47 | 54 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT15UTAEDM-UTA | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT15UTAEDM-TIE | period_winner |  | 0.310 |  | 33 | 71 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT15UTAEDM-EDM | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT15UTAEDM-UTA2 | period_spread |  | 0.100 |  | 11 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT15UTAEDM-EDM2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT15UTAEDM-3 | period_total |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT15UTAEDM-2 | period_total |  | 0.585 |  | 59 | 42 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT15UTAEDM-1 | period_total |  | 0.855 |  | 86 | 15 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT15UTAEDM-UTA | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT15UTAEDM-TIE | period_winner |  | 0.290 |  | 31 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT15UTAEDM-EDM | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT15UTAEDM-UTA2 | period_spread |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT15UTAEDM-EDM2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT15UTAEDM-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT15UTAEDM-2 | period_total |  | 0.640 |  | 65 | 37 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT15UTAEDM-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT15UTAEDM-UTA | period_winner |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT15UTAEDM-TIE | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT15UTAEDM-EDM | period_winner |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT15UTAEDM-UTA2 | period_spread |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT15UTAEDM-EDM2 | period_spread |  | 0.155 |  | 17 | 86 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT15UTAEDM-3 | period_total |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT15UTAEDM-2 | period_total |  | 0.695 |  | 71 | 32 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT15UTAEDM-1 | period_total |  | 0.925 |  | 94 | 9 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15UTAEDM-EDMRSHEA6-2 | player_assists |  | 0.045 |  | 5 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15UTAEDM-EDMRSHEA6-1 | player_assists |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15UTAEDM-UTAKYAMAMOTO56-1 | player_assists |  | 0.175 |  | 18 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15UTAEDM-UTABHAYTON27-1 | player_assists |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-2 | player_assists |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1 | player_assists |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ EDM | 0.557 | 0.583 | 0.166 | 0.205 | 6.64 | 6.76 | 0.994/0.989 | KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM4 +0.035 |
| CGY @ VGK | 0.665 | 0.660 | 0.158 | 0.207 | 6.30 | 6.19 | 1.003/1.006 | KXNHLTOTAL-26OCT15CGYVGK-6 -0.029 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1273 (adj 0.113) · $7.03 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 16c · p 0.216 (adj 0.1995) · $8.78 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 32c · p 0.4399 (adj 0.3587) · $10.76 · thesis EDM:SUPPRESSED
- Connor McDavid: 1+ goals YES @ 43c · p 0.4705 (adj 0.4579) · $4.75 · thesis EDM:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 68c · p 0.74 (adj 0.7238) · $15.0 · thesis VGK:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 6c · p 0.085 (adj 0.0788) · $3.61 · thesis VGK:OFFENSE_4PLUS
- Trevor Connelly: 1+ assists NO @ 65c · p 0.7766 (adj 0.6911) · $15.0 · thesis VGK:SUPPRESSED
- Aydar Suniev: 1+ goals YES @ 16c · p 0.1901 (adj 0.1801) · $3.01 · thesis CGY:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ EDM** · priced 187/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 27.2, exp saves 23.67 (sd 6.43), pull risk 0.06
- UTA net: Karel Vejmelka (CONFIRMED) exp shots 27.99, exp saves 23.78 (sd 6.74), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mattias Ekholm: 1+ points | 0.474 | 0.330 | 34/68 | +0.118 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.193 | 0.330 | 34/68 | +0.112 | STANDARD |
| Connor McDavid: 1+ assists | 0.560 | 0.685 | 69/32 | +0.105 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.459 | 0.335 | 34/67 | +0.104 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.396 | 0.275 | 28/73 | +0.102 | STANDARD |
| Connor McDavid: 2+ assists | 0.197 | 0.310 | 32/70 | +0.088 | STANDARD |

**CGY @ VGK** · priced 187/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.2, exp saves 23.24 (sd 6.25), pull risk 0.041
- CGY net: Dustin Wolf (CONFIRMED) exp shots 30.19, exp saves 25.42 (sd 7.17), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.466 | 0.605 | 61/40 | +0.117 | STANDARD |
| Trevor Connelly: 1+ assists | 0.223 | 0.355 | 36/65 | +0.111 | PRIOR_HEAVY |
| Kevin Bahl: 1+ assists | 0.216 | 0.085 | 15/98 | +0.057 | STANDARD |
| Jack Eichel: 2+ points | 0.272 | 0.395 | 41/62 | +0.092 | STANDARD |
| Mitch Marner: 1+ assists | 0.435 | 0.555 | 56/45 | +0.098 | STANDARD |
| Trevor Connelly: 1+ points | 0.391 | 0.510 | 52/50 | +0.091 | PRIOR_HEAVY |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
