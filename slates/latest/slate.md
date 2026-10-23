# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-23T01:30:05Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 2 · markets on board: 4913 · contracts joined: 492 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 442, 'OK': 40, 'NO_EDGE': 10}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 77, 'game_early_goal': 2, 'first_goal': 72, 'game_winner': 4, 'player_goals': 132, 'game_overtime': 2, 'player_points': 109, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ SEA | 2026-10-23T02:00:00Z | T-10m | 0.491 | 0.509 | 0.174 | 6.27 | 3.10 | 3.17 | 238 (25/213) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-10m | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 254 (25/229) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.396 | 0.525 | 0.499 | 53 | 48 | no | +0.106 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.491 | 0.365 | 0.389 | 37 | 64 | yes | +0.105 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.509 | 0.625 | 0.602 | 63 | 38 | no | +0.095 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.178 | 0.285 | 0.261 | 29 | 72 | no | +0.088 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.292 | 0.395 | 0.373 | 40 | 61 | no | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA3 | team_total | 0.619 | 0.720 | 0.701 | 73 | 29 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA5 | team_total | 0.217 | 0.310 | 0.290 | 32 | 70 | no | +0.068 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.278 | 0.205 | 0.218 | 21 | 80 | yes | +0.056 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.615 | 0.602 | 62 | 39 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA2 | team_total | 0.821 | 0.880 | 0.870 | 89 | 13 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA3 | game_spread | 0.164 | 0.115 | 0.124 | 12 | 89 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.270 | 0.258 | 28 | 74 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT22UTASEA-4 | game_total | 0.860 | 0.905 | 0.897 | 91 | 10 | no | +0.034 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT22UTASEA-5 | game_total | 0.778 | 0.825 | 0.816 | 83 | 18 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA6 | team_total | 0.100 | 0.150 | 0.139 | 16 | 86 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET4 | team_total | 0.441 | 0.500 | 0.488 | 51 | 51 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.385 | 0.374 | 39 | 62 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3 | team_total | 0.607 | 0.550 | 0.562 | 56 | 46 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-VAN2 | game_spread | 0.245 | 0.205 | 0.213 | 21 | 80 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT22UTASEA-6 | game_total | 0.571 | 0.615 | 0.606 | 62 | 39 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4 | team_total | 0.388 | 0.340 | 0.349 | 35 | 67 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT22UTASEA-7 | game_total | 0.461 | 0.505 | 0.496 | 51 | 50 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET3 | team_total | 0.654 | 0.700 | 0.691 | 71 | 31 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET5 | team_total | 0.255 | 0.300 | 0.291 | 31 | 71 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET2 | team_total | 0.845 | 0.875 | 0.869 | 88 | 13 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA2 | team_total | 0.809 | 0.775 | 0.782 | 78 | 23 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA5 | team_total | 0.207 | 0.170 | 0.177 | 18 | 84 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN3 | team_total | 0.583 | 0.545 | 0.553 | 55 | 46 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN4 | team_total | 0.365 | 0.335 | 0.341 | 34 | 67 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA6 | team_total | 0.094 | 0.070 | 0.074 | 8 | 94 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT22UTASEA-9 | game_total | 0.190 | 0.215 | 0.210 | 22 | 79 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT22UTASEA-8 | game_total | 0.268 | 0.300 | 0.293 | 31 | 71 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT22DETVAN-VAN3 | game_spread | 0.142 | 0.125 | 0.128 | 13 | 88 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN5 | team_total | 0.194 | 0.170 | 0.175 | 18 | 84 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN6 | team_total | 0.089 | 0.070 | 0.073 | 8 | 94 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT22DETVAN-4 | game_total | 0.870 | 0.885 | 0.882 | 89 | 12 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT22UTASEA-3 | game_total | 0.966 | 0.975 | 0.973 | 98 | 3 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN2 | team_total | 0.793 | 0.775 | 0.779 | 78 | 23 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET6 | team_total | 0.121 | 0.135 | 0.132 | 14 | 87 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT22DETVAN-5 | game_total | 0.789 | 0.805 | 0.802 | 81 | 20 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-3 | game_total | 0.969 | 0.975 | 0.974 | 98 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-7 | game_total | 0.475 | 0.495 | 0.491 | 50 | 51 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT22UTASEA-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT22UTASEA-10 | game_total | 0.091 | 0.100 | 0.098 | 11 | 91 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-10 | game_total | 0.096 | 0.095 | 0.095 | 10 | 91 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-6 | game_total | 0.584 | 0.600 | 0.597 | 61 | 41 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-9 | game_total | 0.205 | 0.205 | 0.205 | 21 | 80 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-8 | game_total | 0.284 | 0.285 | 0.285 | 29 | 72 |  | -0.018 | NO_EDGE |
| KXNHL1P-26OCT22UTASEA-SEA | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT22UTASEA-TIE | period_winner |  | 0.310 |  | 33 | 71 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT22UTASEA-UTA | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT22UTASEA-SEA2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT22UTASEA-UTA2 | period_spread |  | 0.155 |  | 16 | 85 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT22UTASEA-1 | period_total |  | 0.855 |  | 86 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT22UTASEA-2 | period_total |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT22UTASEA-3 | period_total |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT22UTASEA-SEA | period_winner |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT22UTASEA-TIE | period_winner |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT22UTASEA-UTA | period_winner |  | 0.415 |  | 43 | 60 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT22UTASEA-SEA2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT22UTASEA-UTA2 | period_spread |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT22UTASEA-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT22UTASEA-2 | period_total |  | 0.630 |  | 64 | 38 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT22UTASEA-3 | period_total |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT22UTASEA-SEA | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT22UTASEA-TIE | period_winner |  | 0.240 |  | 26 | 78 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT22UTASEA-UTA | period_winner |  | 0.445 |  | 46 | 57 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT22UTASEA-SEA2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT22UTASEA-UTA2 | period_spread |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT22UTASEA-1 | period_total |  | 0.925 |  | 95 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT22UTASEA-2 | period_total |  | 0.680 |  | 69 | 33 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT22UTASEA-3 | period_total |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT22UTASEA-SEABMCMANN74-1 | player_assists |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT22UTASEA-SEABMONTOUR62-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT22UTASEA-SEABMONTOUR62-2 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT22UTASEA-SEACSTEPHENSON9-1 | player_assists |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT22UTASEA-SEACSTEPHENSON9-2 | player_assists |  | 0.065 |  | 10 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT22UTASEA-SEAJEBERLE7-1 | player_assists |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ SEA | 0.491 | 0.498 | 0.174 | 0.215 | 6.27 | 6.52 | 1.015/0.992 | KXNHLTOTAL-26OCT22UTASEA-7 +0.043 |
| DET @ VAN | 0.450 | 0.531 | 0.176 | 0.215 | 6.37 | 6.28 | 1.021/1.003 | KXNHLGAME-26OCT22DETVAN-DET -0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Shane Wright: 1+ goals YES @ 15c · p 0.2053 (adj 0.189) · $8.07 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1362 (adj 0.1259) · $4.91 · thesis SEA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 64c · p 0.6997 (adj 0.6835) · $20.0 · thesis UTA:SUPPRESSED
- Kaapo Kakko: 1+ goals YES @ 15c · p 0.189 (adj 0.178) · $5.45 · thesis SEA:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 18c · p 0.2701 (adj 0.2463) · $13.97 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 10c · p 0.1648 (adj 0.1474) · $8.82 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 12c · p 0.1767 (adj 0.1588) · $7.2 · thesis VAN:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 66c · p 0.7198 (adj 0.7036) · $19.06 · thesis DET:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ SEA** · priced 186/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 29.05, exp saves 25.09 (sd 6.72), pull risk 0.064
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.24), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Clayton Keller: 2+ points | 0.230 | 0.360 | 37/65 | +0.104 | STANDARD |
| Kailer Yamamoto: 1+ assists | 0.264 | 0.140 | 26/98 | -0.010 | STANDARD |
| Clayton Keller: 1+ points | 0.593 | 0.715 | 72/29 | +0.103 | STANDARD |
| Vincent Trocheck: 1+ points | 0.358 | 0.470 | 48/54 | +0.085 | STANDARD |
| Clayton Keller: 1+ assists | 0.447 | 0.555 | 57/46 | +0.076 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.211 | 0.310 | 33/71 | +0.065 | STANDARD |

**DET @ VAN** · priced 172/203 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Max Sasson: 1+ points | 0.321 | 0.110 | 21/99 | +0.099 | STANDARD |
| Tom Willander: 1+ assists | 0.283 | 0.120 | 23/99 | +0.041 | STANDARD |
| Ben Chiarot: 1+ assists | 0.248 | 0.090 | 17/99 | +0.068 | STANDARD |
| Liam Ohgren: 1+ assists | 0.286 | 0.135 | 26/99 | +0.012 | STANDARD |
| Liam Ohgren: 1+ points | 0.411 | 0.265 | 33/80 | +0.066 | STANDARD |
| Paul Cotter: 1+ assists | 0.260 | 0.115 | 22/99 | +0.028 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
