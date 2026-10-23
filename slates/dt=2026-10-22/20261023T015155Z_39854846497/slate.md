# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-23T01:51:55Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 2 · markets on board: 4547 · contracts joined: 494 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 444, 'OK': 33, 'NO_EDGE': 17}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 77, 'game_early_goal': 2, 'first_goal': 72, 'game_winner': 4, 'player_goals': 132, 'game_overtime': 2, 'player_points': 109, 'goalie_saves': 2, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ SEA | 2026-10-23T02:00:00Z | T-<10m | 0.496 | 0.504 | 0.177 | 6.22 | 3.10 | 3.12 | 240 (25/215) | CONFIRMED/CONFIRMED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-<10m | 0.422 | 0.578 | 0.167 | 6.46 | 2.98 | 3.48 | 254 (25/229) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.391 | 0.525 | 0.498 | 53 | 48 | no | +0.112 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.496 | 0.365 | 0.390 | 37 | 64 | yes | +0.109 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.504 | 0.635 | 0.610 | 64 | 37 | no | +0.109 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.172 | 0.285 | 0.259 | 29 | 72 | no | +0.094 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.285 | 0.395 | 0.372 | 40 | 61 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA3 | team_total | 0.609 | 0.715 | 0.695 | 72 | 29 | no | +0.086 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA5 | team_total | 0.211 | 0.320 | 0.296 | 33 | 69 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA2 | team_total | 0.812 | 0.890 | 0.877 | 90 | 12 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.281 | 0.205 | 0.219 | 21 | 80 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA6 | team_total | 0.095 | 0.165 | 0.148 | 17 | 84 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA3 | game_spread | 0.168 | 0.115 | 0.124 | 12 | 89 | yes | +0.040 | OK |
| KXNHLTOTAL-26OCT22UTASEA-4 | game_total | 0.855 | 0.905 | 0.896 | 91 | 10 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT22UTASEA-5 | game_total | 0.774 | 0.825 | 0.816 | 83 | 18 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4 | team_total | 0.388 | 0.330 | 0.341 | 34 | 68 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3 | team_total | 0.606 | 0.550 | 0.561 | 56 | 46 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT22UTASEA-6 | game_total | 0.565 | 0.615 | 0.605 | 62 | 39 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT22UTASEA-7 | game_total | 0.455 | 0.505 | 0.495 | 51 | 50 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA2 | team_total | 0.811 | 0.775 | 0.783 | 78 | 23 | yes | +0.019 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.578 | 0.615 | 0.608 | 62 | 39 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT22UTASEA-8 | game_total | 0.260 | 0.300 | 0.292 | 31 | 71 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.233 | 0.265 | 0.258 | 27 | 74 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT22UTASEA-9 | game_total | 0.185 | 0.220 | 0.213 | 23 | 79 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA6 | team_total | 0.091 | 0.075 | 0.078 | 8 | 93 | yes | +0.006 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.422 | 0.395 | 0.400 | 40 | 61 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT22UTASEA-3 | game_total | 0.964 | 0.975 | 0.973 | 98 | 3 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA5 | team_total | 0.205 | 0.175 | 0.181 | 19 | 84 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN3 | team_total | 0.571 | 0.545 | 0.550 | 55 | 46 | yes | +0.004 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.362 | 0.385 | 0.380 | 39 | 62 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET2 | team_total | 0.861 | 0.875 | 0.872 | 88 | 13 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET4 | team_total | 0.471 | 0.500 | 0.494 | 51 | 51 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN6 | team_total | 0.086 | 0.075 | 0.077 | 8 | 93 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN5 | team_total | 0.191 | 0.170 | 0.174 | 18 | 84 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN4 | team_total | 0.356 | 0.335 | 0.339 | 34 | 67 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT22DETVAN-10 | game_total | 0.106 | 0.095 | 0.097 | 10 | 91 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET5 | team_total | 0.277 | 0.300 | 0.295 | 31 | 71 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-3 | game_total | 0.969 | 0.975 | 0.974 | 98 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT22UTASEA-10 | game_total | 0.088 | 0.100 | 0.097 | 11 | 91 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-4 | game_total | 0.877 | 0.885 | 0.883 | 89 | 12 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET3 | team_total | 0.680 | 0.695 | 0.692 | 70 | 31 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT22UTASEA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN2 | team_total | 0.786 | 0.775 | 0.777 | 78 | 23 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT22DETVAN-VAN2 | game_spread | 0.226 | 0.215 | 0.217 | 22 | 79 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT22DETVAN-VAN3 | game_spread | 0.131 | 0.125 | 0.126 | 13 | 88 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-8 | game_total | 0.296 | 0.285 | 0.287 | 29 | 72 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-9 | game_total | 0.212 | 0.205 | 0.206 | 21 | 80 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-2 | game_total | 0.988 | 0.990 | 0.990 |  | 2 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET6 | team_total | 0.136 | 0.140 | 0.139 | 15 | 87 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-5 | game_total | 0.804 | 0.805 | 0.805 | 81 | 20 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-7 | game_total | 0.489 | 0.495 | 0.494 | 50 | 51 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT22DETVAN-6 | game_total | 0.601 | 0.600 | 0.600 | 61 | 41 |  | -0.026 | NO_EDGE |
| KXNHL1P-26OCT22UTASEA-SEA | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT22UTASEA-TIE | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT22UTASEA-UTA | period_winner |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT22UTASEA-SEA2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT22UTASEA-UTA2 | period_spread |  | 0.155 |  | 16 | 85 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT22UTASEA-1 | period_total |  | 0.845 |  | 85 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT22UTASEA-2 | period_total |  | 0.605 |  | 61 | 40 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT22UTASEA-3 | period_total |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT22UTASEA-SEA | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT22UTASEA-TIE | period_winner |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT22UTASEA-UTA | period_winner |  | 0.415 |  | 43 | 60 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT22UTASEA-SEA2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT22UTASEA-UTA2 | period_spread |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT22UTASEA-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT22UTASEA-2 | period_total |  | 0.630 |  | 64 | 38 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT22UTASEA-3 | period_total |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT22UTASEA-SEA | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT22UTASEA-TIE | period_winner |  | 0.240 |  | 26 | 78 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT22UTASEA-UTA | period_winner |  | 0.455 |  | 47 | 56 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT22UTASEA-SEA2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT22UTASEA-UTA2 | period_spread |  | 0.210 |  | 23 | 81 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT22UTASEA-1 | period_total |  | 0.920 |  | 95 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT22UTASEA-2 | period_total |  | 0.680 |  | 69 | 33 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT22UTASEA-3 | period_total |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT22UTASEA-SEABMCMANN74-1 | player_assists |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT22UTASEA-SEABMONTOUR62-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT22UTASEA-SEABMONTOUR62-2 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT22UTASEA-SEACSTEPHENSON9-1 | player_assists |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT22UTASEA-SEACSTEPHENSON9-2 | player_assists |  | 0.070 |  | 10 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT22UTASEA-SEAJEBERLE7-1 | player_assists |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ SEA | 0.496 | 0.491 | 0.177 | 0.217 | 6.22 | 6.54 | 1.023/0.989 | KXNHLTOTAL-26OCT22UTASEA-7 +0.052 |
| DET @ VAN | 0.422 | 0.523 | 0.167 | 0.217 | 6.46 | 6.28 | 1.031/0.994 | KXNHLSPREAD-26OCT22DETVAN-DET2 -0.102 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Shane Wright: 1+ goals YES @ 15c · p 0.1999 (adj 0.1862) · $7.65 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1403 (adj 0.129) · $5.77 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 15c · p 0.1942 (adj 0.1819) · $6.53 · thesis SEA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 64c · p 0.7024 (adj 0.6855) · $20.0 · thesis UTA:SUPPRESSED
- Filip Chytil: 1+ goals YES @ 18c · p 0.2669 (adj 0.2439) · $12.64 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 10c · p 0.166 (adj 0.147) · $8.15 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2552 (adj 0.2376) · $9.21 · thesis VAN:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 66c · p 0.7185 (adj 0.7014) · $18.05 · thesis DET:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ SEA** · priced 188/189 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (CONFIRMED) exp shots 29.05, exp saves 25.08 (sd 6.81), pull risk 0.069
- UTA net: Karel Vejmelka (CONFIRMED) exp shots 25.82, exp saves 22.3 (sd 6.3), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Berkly Catton: 1+ points | 0.414 | 0.225 | 38/93 | +0.017 | STANDARD |
| Shane Wright: 1+ points | 0.367 | 0.205 | 33/92 | +0.022 | STANDARD |
| Philipp Grubauer: 28+ saves | 0.358 | 0.505 | 99/98 | -0.340 |  |
| Clayton Keller: 1+ points | 0.594 | 0.725 | 73/28 | +0.112 | STANDARD |
| Kailer Yamamoto: 1+ assists | 0.273 | 0.145 | 27/98 | -0.010 | STANDARD |
| Clayton Keller: 2+ points | 0.228 | 0.355 | 37/66 | +0.096 | STANDARD |

**DET @ VAN** · priced 172/203 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (CONFIRMED) exp shots 30.0, exp saves 26.01 (sd 6.97), pull risk 0.06
- DET net: John Gibson (CONFIRMED) exp shots 25.34, exp saves 21.76 (sd 6.19), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Linus Karlsson: 1+ points | 0.496 | 0.235 | 40/93 | +0.079 | STANDARD |
| Liam Ohgren: 1+ points | 0.396 | 0.180 | 33/97 | +0.050 | STANDARD |
| Max Sasson: 1+ points | 0.322 | 0.115 | 21/98 | +0.100 | STANDARD |
| Linus Karlsson: 1+ assists | 0.326 | 0.120 | 23/99 | +0.083 | STANDARD |
| Tom Willander: 1+ assists | 0.276 | 0.120 | 23/99 | +0.034 | STANDARD |
| Brendan Gallagher: 1+ points | 0.263 | 0.115 | 22/99 | +0.031 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
