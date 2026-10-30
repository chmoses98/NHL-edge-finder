# NHL slate 2026-10-29 — RESEARCH_ONLY

generated 2026-10-30T00:15:28Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 3 · markets on board: 4500 · contracts joined: 684 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 609, 'CANNOT_TRUST_INPUTS': 75}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 97, 'game_early_goal': 3, 'first_goal': 109, 'game_winner': 6, 'player_goals': 190, 'game_overtime': 3, 'player_points': 129, 'goalie_saves': 6, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ ANA | 2026-10-30T02:00:00Z | T-90m | 0.499 | 0.501 | 0.169 | 6.44 | 3.21 | 3.22 | 237 (25/212) | PROJECTED/PROBABLE |
| OTT @ LAK | 2026-10-30T02:00:00Z | T-90m | 0.517 | 0.483 | 0.178 | 6.13 | 3.12 | 3.01 | 227 (25/202) | CONFIRMED/CONFIRMED |
| VAN @ SJS | 2026-10-30T02:00:00Z | T-90m | 0.591 | 0.409 | 0.160 | 7.13 | 3.87 | 3.25 | 220 (25/195) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF4 | team_total | 0.413 | 0.495 | 0.478 | 50 | 51 |  | +0.060 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF3 | team_total | 0.628 | 0.710 | 0.694 | 72 | 30 |  | +0.058 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29BUFANA-BUF2 | game_spread | 0.289 | 0.365 | 0.349 | 37 | 64 |  | +0.055 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29BUFANA-ANA | game_winner | 0.499 | 0.425 | 0.440 | 43 | 58 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29BUFANA-BUF | game_winner | 0.501 | 0.575 | 0.560 | 58 | 43 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29BUFANA-BUF3 | game_spread | 0.176 | 0.245 | 0.230 | 25 | 76 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF5 | team_total | 0.231 | 0.300 | 0.285 | 31 | 71 |  | +0.045 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-8 | game_total | 0.398 | 0.335 | 0.347 | 34 | 67 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-7 | game_total | 0.483 | 0.545 | 0.533 | 55 | 46 |  | +0.040 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-10 | game_total | 0.163 | 0.115 | 0.123 | 12 | 89 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29OTTLA-OTT3 | game_spread | 0.157 | 0.205 | 0.195 | 21 | 80 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29OTTLA-LA | game_winner | 0.517 | 0.465 | 0.475 | 47 | 54 |  | +0.029 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29OTTLA-OTT | game_winner | 0.483 | 0.535 | 0.525 | 54 | 47 |  | +0.029 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29BUFANA-ANA2 | game_spread | 0.290 | 0.240 | 0.250 | 25 | 77 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-6 | game_total | 0.597 | 0.645 | 0.636 | 65 | 36 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-7 | game_total | 0.594 | 0.545 | 0.555 | 55 | 46 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-9 | game_total | 0.298 | 0.250 | 0.259 | 26 | 76 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF2 | team_total | 0.827 | 0.870 | 0.862 | 88 | 14 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-6 | game_total | 0.700 | 0.655 | 0.664 | 66 | 35 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29OTTLA-OTT2 | game_spread | 0.266 | 0.305 | 0.297 | 31 | 70 |  | +0.019 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN5 | team_total | 0.239 | 0.205 | 0.211 | 21 | 80 |  | +0.017 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6 | team_total | 0.106 | 0.145 | 0.136 | 16 | 87 |  | +0.016 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29OTTLA-LA2 | game_spread | 0.299 | 0.265 | 0.272 | 27 | 74 |  | +0.015 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA3 | team_total | 0.611 | 0.575 | 0.582 | 58 | 43 |  | +0.014 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA2 | team_total | 0.815 | 0.785 | 0.791 | 79 | 22 |  | +0.013 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-8 | game_total | 0.291 | 0.325 | 0.318 | 33 | 68 |  | +0.013 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN3 | team_total | 0.629 | 0.595 | 0.602 | 60 | 41 |  | +0.013 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN4 | team_total | 0.419 | 0.385 | 0.392 | 39 | 62 |  | +0.012 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN6 | team_total | 0.115 | 0.085 | 0.090 | 10 | 93 |  | +0.009 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-5 | game_total | 0.802 | 0.830 | 0.825 | 84 | 18 |  | +0.008 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA5 | team_total | 0.208 | 0.180 | 0.185 | 19 | 83 |  | +0.008 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT3 | team_total | 0.587 | 0.615 | 0.609 | 62 | 39 |  | +0.007 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-4 | game_total | 0.877 | 0.900 | 0.896 | 91 | 11 |  | +0.006 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT2 | team_total | 0.794 | 0.820 | 0.815 | 83 | 19 |  | +0.006 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29VANSJ-SJ3 | game_spread | 0.261 | 0.285 | 0.280 | 29 | 72 |  | +0.005 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29BUFANA-ANA3 | game_spread | 0.174 | 0.155 | 0.159 | 16 | 85 |  | +0.005 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA4 | team_total | 0.390 | 0.360 | 0.366 | 37 | 65 |  | +0.004 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29OTTLA-9 | game_total | 0.173 | 0.155 | 0.159 | 16 | 85 |  | +0.004 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 |  | +0.002 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN2 | team_total | 0.822 | 0.805 | 0.809 | 81 | 20 |  | +0.001 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29OTTLA-7 | game_total | 0.437 | 0.415 | 0.419 | 42 | 59 |  | +0.000 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-10 | game_total | 0.103 | 0.120 | 0.116 | 13 | 89 |  | +0.000 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA3 | team_total | 0.626 | 0.600 | 0.605 | 61 | 41 |  | -0.001 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29OTTLA-8 | game_total | 0.252 | 0.230 | 0.234 | 24 | 78 |  | -0.001 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-9 | game_total | 0.210 | 0.230 | 0.226 | 24 | 78 |  | -0.002 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA6 | team_total | 0.093 | 0.075 | 0.078 | 9 | 94 |  | -0.003 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-3 | game_total | 0.971 | 0.980 | 0.979 | 99 | 3 |  | -0.003 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29OTTLA-LA3 | game_spread | 0.176 | 0.165 | 0.167 | 17 | 84 |  | -0.004 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29VANSJ-VAN3 | game_spread | 0.133 | 0.125 | 0.127 | 13 | 88 |  | -0.005 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT4 | team_total | 0.368 | 0.390 | 0.386 | 40 | 62 |  | -0.005 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4 | team_total | 0.411 | 0.390 | 0.394 | 40 | 62 |  | -0.005 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29OTTLA-3 | game_total | 0.963 | 0.970 | 0.969 | 98 | 4 |  | -0.005 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29OTTLA-10 | game_total | 0.080 | 0.070 | 0.072 | 8 | 94 |  | -0.006 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-5 | game_total | 0.863 | 0.850 | 0.853 | 86 | 16 |  | -0.006 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29OTTLA-6 | game_total | 0.552 | 0.535 | 0.538 | 54 | 47 |  | -0.006 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-4 | game_total | 0.919 | 0.910 | 0.912 | 92 | 10 |  | -0.006 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29OTTLA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ6 | team_total | 0.194 | 0.175 | 0.179 | 19 | 84 |  | -0.007 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29VANSJ-VAN2 | game_spread | 0.224 | 0.215 | 0.217 | 22 | 79 |  | -0.008 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29VANSJ-VAN | game_winner | 0.409 | 0.395 | 0.398 | 40 | 61 |  | -0.008 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29VANSJ-SJ | game_winner | 0.591 | 0.605 | 0.602 | 61 | 40 |  | -0.008 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-3 | game_total | 0.982 | 0.980 | 0.980 | 99 | 3 |  | -0.009 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ5 | team_total | 0.357 | 0.345 | 0.347 | 35 | 66 |  | -0.009 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ2 | team_total | 0.896 | 0.895 | 0.895 | 90 | 11 |  | -0.010 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT6 | team_total | 0.086 | 0.090 | 0.089 | 10 | 92 |  | -0.011 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29VANSJ-SJ2 | game_spread | 0.386 | 0.395 | 0.393 | 40 | 61 |  | -0.012 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA5 | team_total | 0.228 | 0.215 | 0.218 | 23 | 80 |  | -0.014 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT5 | team_total | 0.194 | 0.205 | 0.203 | 22 | 81 |  | -0.015 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA2 | team_total | 0.826 | 0.830 | 0.829 | 84 | 18 |  | -0.016 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ3 | team_total | 0.747 | 0.735 | 0.737 | 75 | 28 |  | -0.016 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29OTTLA-5 | game_total | 0.764 | 0.765 | 0.765 | 77 | 24 |  | -0.017 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29OTTLA-4 | game_total | 0.849 | 0.850 | 0.850 | 86 | 16 |  | -0.019 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA6 | team_total | 0.105 | 0.100 | 0.101 | 12 | 92 |  | -0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ4 | team_total | 0.555 | 0.550 | 0.551 | 56 | 46 |  | -0.022 | CANNOT_TRUST_INPUTS |
| KXNHL1P-26OCT29BUFANA-ANA | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT29BUFANA-BUF | period_winner |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT29BUFANA-TIE | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT29BUFANA-ANA2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT29BUFANA-BUF2 | period_spread |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ ANA | 0.499 | 0.562 | 0.169 | 0.211 | 6.44 | 6.67 | 1.036/1.000 | KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4 +0.073 |
| OTT @ LAK | 0.517 | 0.529 | 0.178 | 0.224 | 6.13 | 6.01 | 0.996/1.040 | KXNHLTOTAL-26OCT29OTTLA-6 -0.027 |
| VAN @ SJS | 0.591 | 0.558 | 0.160 | 0.212 | 7.13 | 6.61 | 1.040/1.034 | KXNHLTOTAL-26OCT29VANSJ-8 -0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status NO_BETS · gate PASS · 0 recommended · full analysis in card.md / packet.json `thesis_card`


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ ANA** · priced 176/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 27.32, exp saves 23.86 (sd 6.5), pull risk 0.06
- BUF net: Colten Ellis (PROBABLE) exp shots 28.64, exp saves 24.47 (sd 6.89), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Warren: 1+ assists | 0.260 | 0.115 | 21/98 | +0.039 | STANDARD |
| Lukas Dostal: 27+ saves | 0.334 | 0.455 | 47/56 | +0.088 |  |
| A.J. Greer: 1+ goals | 0.262 | 0.145 | 15/86 | +0.103 | STANDARD |
| Alex Killorn: 1+ points | 0.454 | 0.350 | 37/67 | +0.068 | STANDARD |
| Tage Thompson: 1+ points | 0.546 | 0.630 | 64/38 | +0.058 | STANDARD |
| Jackson LaCombe: 2+ assists | 0.207 | 0.125 | 16/91 | +0.038 | STANDARD |

**OTT @ LAK** · priced 168/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 27.33, exp saves 23.88 (sd 6.44), pull risk 0.051
- OTT net: Jonas Johansson (CONFIRMED) exp shots 26.32, exp saves 22.76 (sd 6.28), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ points | 0.388 | 0.515 | 52/49 | +0.105 | STANDARD |
| Jake Sanderson: 1+ assists | 0.308 | 0.435 | 44/57 | +0.105 | STANDARD |
| Thomas Chabot: 1+ assists | 0.210 | 0.305 | 31/70 | +0.076 | STANDARD |
| Thomas Chabot: 1+ points | 0.285 | 0.380 | 39/63 | +0.069 | STANDARD |
| Jake Sanderson: 2+ points | 0.086 | 0.175 | 19/84 | +0.065 | STANDARD |
| Tim Stutzle: 1+ points | 0.557 | 0.635 | 64/37 | +0.056 | STANDARD |

**VAN @ SJS** · priced 161/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 25.57, exp saves 22.3 (sd 6.23), pull risk 0.06
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 29.42, exp saves 25.06 (sd 6.94), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.425 | 0.575 | 58/43 | +0.128 | STANDARD |
| Macklin Celebrini: 2+ points | 0.333 | 0.470 | 48/54 | +0.109 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.472 | 0.595 | 60/41 | +0.101 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.284 | 0.400 | 41/61 | +0.089 | STANDARD |
| Ivar Stenberg: 2+ points | 0.107 | 0.220 | 23/79 | +0.092 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.134 | 0.245 | 25/76 | +0.094 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
