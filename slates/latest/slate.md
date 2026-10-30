# NHL slate 2026-10-29 — RESEARCH_ONLY

generated 2026-10-30T01:36:52Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 3 · markets on board: 4466 · contracts joined: 684 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 609, 'OK': 44, 'NO_EDGE': 31}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 97, 'game_early_goal': 3, 'first_goal': 109, 'game_winner': 6, 'player_goals': 190, 'game_overtime': 3, 'player_points': 129, 'goalie_saves': 6, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ ANA | 2026-10-30T02:00:00Z | T-10m | 0.493 | 0.507 | 0.169 | 6.43 | 3.19 | 3.24 | 237 (25/212) | CONFIRMED/CONFIRMED |
| OTT @ LAK | 2026-10-30T02:00:00Z | T-10m | 0.517 | 0.483 | 0.178 | 6.13 | 3.12 | 3.01 | 227 (25/202) | CONFIRMED/CONFIRMED |
| VAN @ SJS | 2026-10-30T02:00:00Z | T-10m | 0.591 | 0.409 | 0.160 | 7.13 | 3.87 | 3.25 | 220 (25/195) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF4 | team_total | 0.416 | 0.495 | 0.479 | 50 | 51 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF3 | team_total | 0.631 | 0.710 | 0.695 | 72 | 30 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF3 | game_spread | 0.180 | 0.245 | 0.231 | 25 | 76 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF2 | game_spread | 0.298 | 0.365 | 0.351 | 37 | 64 | no | +0.046 | OK |
| KXNHLGAME-26OCT29BUFANA-ANA | game_winner | 0.493 | 0.425 | 0.438 | 43 | 58 | yes | +0.046 | OK |
| KXNHLGAME-26OCT29BUFANA-BUF | game_winner | 0.507 | 0.575 | 0.562 | 58 | 43 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF5 | team_total | 0.232 | 0.300 | 0.285 | 31 | 71 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT29BUFANA-7 | game_total | 0.485 | 0.545 | 0.533 | 55 | 46 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF2 | team_total | 0.829 | 0.875 | 0.867 | 88 | 13 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT29VANSJ-8 | game_total | 0.398 | 0.345 | 0.355 | 35 | 66 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT3 | game_spread | 0.157 | 0.205 | 0.195 | 21 | 80 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT29BUFANA-5 | game_total | 0.800 | 0.845 | 0.837 | 85 | 16 | no | +0.031 | OK |
| KXNHLGAME-26OCT29OTTLA-LA | game_winner | 0.517 | 0.465 | 0.475 | 47 | 54 | yes | +0.029 | OK |
| KXNHLGAME-26OCT29OTTLA-OTT | game_winner | 0.483 | 0.535 | 0.525 | 54 | 47 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT29BUFANA-6 | game_total | 0.596 | 0.645 | 0.635 | 65 | 36 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT29VANSJ-7 | game_total | 0.594 | 0.545 | 0.555 | 55 | 46 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT29VANSJ-10 | game_total | 0.163 | 0.125 | 0.132 | 13 | 88 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT29VANSJ-9 | game_total | 0.298 | 0.250 | 0.259 | 26 | 76 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT29VANSJ-6 | game_total | 0.700 | 0.655 | 0.664 | 66 | 35 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT29BUFANA-ANA2 | game_spread | 0.286 | 0.240 | 0.249 | 25 | 77 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN6 | team_total | 0.115 | 0.080 | 0.086 | 9 | 93 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT2 | game_spread | 0.266 | 0.305 | 0.297 | 31 | 70 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN5 | team_total | 0.239 | 0.205 | 0.211 | 21 | 80 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT29BUFANA-4 | game_total | 0.877 | 0.910 | 0.904 | 92 | 10 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT29OTTLA-LA2 | game_spread | 0.299 | 0.265 | 0.272 | 27 | 74 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA3 | team_total | 0.611 | 0.570 | 0.578 | 58 | 44 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA2 | team_total | 0.815 | 0.785 | 0.791 | 79 | 22 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6 | team_total | 0.109 | 0.140 | 0.133 | 15 | 87 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT29BUFANA-8 | game_total | 0.295 | 0.325 | 0.319 | 33 | 68 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT29OTTLA-8 | game_total | 0.252 | 0.225 | 0.230 | 23 | 78 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA5 | team_total | 0.208 | 0.180 | 0.185 | 19 | 83 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA6 | team_total | 0.093 | 0.070 | 0.074 | 8 | 94 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT29BUFANA-9 | game_total | 0.211 | 0.235 | 0.230 | 24 | 77 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT2 | team_total | 0.794 | 0.820 | 0.815 | 83 | 19 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT29VANSJ-SJ3 | game_spread | 0.261 | 0.285 | 0.280 | 29 | 72 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT29BUFANA-10 | game_total | 0.098 | 0.120 | 0.115 | 13 | 89 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT29OTTLA-6 | game_total | 0.552 | 0.525 | 0.530 | 53 | 48 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA4 | team_total | 0.390 | 0.360 | 0.366 | 37 | 65 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ6 | team_total | 0.194 | 0.170 | 0.175 | 18 | 84 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT29OTTLA-9 | game_total | 0.173 | 0.155 | 0.159 | 16 | 85 | yes | +0.004 | OK |
| KXNHLSPREAD-26OCT29BUFANA-ANA3 | game_spread | 0.172 | 0.155 | 0.158 | 16 | 85 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN4 | team_total | 0.419 | 0.390 | 0.396 | 40 | 62 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT29VANSJ-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT29OTTLA-7 | game_total | 0.437 | 0.415 | 0.419 | 42 | 59 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA3 | team_total | 0.626 | 0.605 | 0.609 | 61 | 40 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT29BUFANA-3 | game_total | 0.970 | 0.980 | 0.978 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT29BUFANA-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA6 | team_total | 0.103 | 0.090 | 0.092 | 10 | 92 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT29OTTLA-LA3 | game_spread | 0.176 | 0.165 | 0.167 | 17 | 84 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT3 | team_total | 0.587 | 0.615 | 0.609 | 63 | 40 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT29VANSJ-VAN3 | game_spread | 0.133 | 0.125 | 0.127 | 13 | 88 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT4 | team_total | 0.368 | 0.390 | 0.386 | 40 | 62 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT29OTTLA-3 | game_total | 0.963 | 0.970 | 0.969 | 98 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT5 | team_total | 0.194 | 0.210 | 0.207 | 22 | 80 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT29OTTLA-10 | game_total | 0.080 | 0.070 | 0.072 | 8 | 94 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT29VANSJ-5 | game_total | 0.863 | 0.855 | 0.857 | 86 | 15 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT29VANSJ-4 | game_total | 0.919 | 0.910 | 0.912 | 92 | 10 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT29OTTLA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN3 | team_total | 0.629 | 0.610 | 0.614 | 62 | 40 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT29VANSJ-VAN2 | game_spread | 0.224 | 0.215 | 0.217 | 22 | 79 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN2 | team_total | 0.822 | 0.810 | 0.812 | 82 | 20 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT29VANSJ-VAN | game_winner | 0.409 | 0.395 | 0.398 | 40 | 61 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT29VANSJ-SJ | game_winner | 0.591 | 0.605 | 0.602 | 61 | 40 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT29VANSJ-3 | game_total | 0.982 | 0.980 | 0.980 | 99 | 3 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ5 | team_total | 0.357 | 0.345 | 0.347 | 35 | 66 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT6 | team_total | 0.086 | 0.085 | 0.085 | 9 | 92 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4 | team_total | 0.407 | 0.395 | 0.397 | 40 | 61 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ2 | team_total | 0.896 | 0.895 | 0.895 | 90 | 11 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA2 | team_total | 0.821 | 0.830 | 0.828 | 84 | 18 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT29VANSJ-SJ2 | game_spread | 0.386 | 0.395 | 0.393 | 40 | 61 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ3 | team_total | 0.747 | 0.740 | 0.741 | 75 | 27 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT29OTTLA-5 | game_total | 0.764 | 0.765 | 0.765 | 77 | 24 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26OCT29OTTLA-4 | game_total | 0.849 | 0.850 | 0.850 | 86 | 16 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA5 | team_total | 0.224 | 0.215 | 0.217 | 23 | 80 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ4 | team_total | 0.555 | 0.550 | 0.551 | 56 | 46 |  | -0.022 | NO_EDGE |
| KXNHL1P-26OCT29BUFANA-ANA | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT29BUFANA-BUF | period_winner |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT29BUFANA-TIE | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT29BUFANA-ANA2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT29BUFANA-BUF2 | period_spread |  | 0.145 |  | 15 | 86 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ ANA | 0.493 | 0.558 | 0.169 | 0.205 | 6.43 | 6.68 | 1.044/1.000 | KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4 +0.081 |
| OTT @ LAK | 0.517 | 0.529 | 0.178 | 0.224 | 6.13 | 6.01 | 0.996/1.040 | KXNHLTOTAL-26OCT29OTTLA-6 -0.027 |
| VAN @ SJS | 0.591 | 0.558 | 0.160 | 0.212 | 7.13 | 6.61 | 1.040/1.034 | KXNHLTOTAL-26OCT29VANSJ-8 -0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Tim Washe: 1+ goals YES @ 10c · p 0.166 (adj 0.1445) · $8.94 · thesis ANA:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 62c · p 0.6887 (adj 0.6703) · $20.0 · thesis BUF:SUPPRESSED
- Alex Killorn: 1+ goals YES @ 17c · p 0.222 (adj 0.2065) · $7.54 · thesis ANA:OFFENSE_4PLUS
- Beckett Sennecke: 1+ goals YES @ 30c · p 0.3505 (adj 0.3366) · $7.58 · thesis ANA:OFFENSE_4PLUS
- Thomas Chabot: 1+ assists NO @ 70c · p 0.7903 (adj 0.7427) · $18.95 · thesis OTT:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0754 (adj 0.0665) · $3.05 · thesis LAK:OFFENSE_4PLUS
- Drake Batherson: 1+ goals NO @ 69c · p 0.7331 (adj 0.7211) · $11.05 · thesis OTT:SUPPRESSED
- Erik Gustafsson: 1+ assists NO @ 64c · p 0.7084 (adj 0.6717) · $12.42 · thesis LAK:SUPPRESSED
- Ivar Stenberg: 1+ goals NO @ 72c · p 0.807 (adj 0.784) · $19.32 · thesis SJS:SUPPRESSED
- Tyler Toffoli: 1+ assists YES @ 27c · p 0.3424 (adj 0.3037) · $6.45 · thesis SJS:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 18c · p 0.2182 (adj 0.2074) · $5.06 · thesis VAN:OFFENSE_4PLUS
- Filip Chytil: 1+ assists NO @ 72c · p 0.7941 (adj 0.752) · $19.16 · thesis VAN:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ ANA** · priced 174/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (CONFIRMED) exp shots 27.32, exp saves 23.8 (sd 6.64), pull risk 0.065
- BUF net: Colten Ellis (CONFIRMED) exp shots 28.64, exp saves 24.46 (sd 6.84), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lukas Dostal: 27+ saves | 0.334 | 0.455 | 51/60 | +0.049 |  |
| A.J. Greer: 1+ goals | 0.258 | 0.140 | 15/87 | +0.099 | STANDARD |
| Tage Thompson: 1+ points | 0.541 | 0.635 | 64/37 | +0.073 | STANDARD |
| Alex Killorn: 1+ points | 0.453 | 0.365 | 37/64 | +0.066 | STANDARD |
| Tim Washe: 1+ goals | 0.166 | 0.080 | 10/94 | +0.060 | STANDARD |
| Rasmus Dahlin: 1+ points | 0.516 | 0.600 | 61/41 | +0.057 | STANDARD |

**OTT @ LAK** · priced 168/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 27.33, exp saves 23.88 (sd 6.44), pull risk 0.051
- OTT net: Jonas Johansson (CONFIRMED) exp shots 26.32, exp saves 22.76 (sd 6.28), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ points | 0.388 | 0.515 | 52/49 | +0.105 | STANDARD |
| Jake Sanderson: 1+ assists | 0.308 | 0.435 | 44/57 | +0.105 | STANDARD |
| Thomas Chabot: 1+ points | 0.285 | 0.385 | 39/62 | +0.078 | STANDARD |
| Thomas Chabot: 1+ assists | 0.210 | 0.305 | 31/70 | +0.076 | STANDARD |
| Tim Stutzle: 1+ points | 0.557 | 0.635 | 64/37 | +0.056 | STANDARD |
| Jake Sanderson: 2+ points | 0.086 | 0.160 | 19/87 | +0.036 | STANDARD |

**VAN @ SJS** · priced 161/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 25.57, exp saves 22.3 (sd 6.23), pull risk 0.06
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 29.42, exp saves 25.06 (sd 6.94), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.425 | 0.575 | 58/43 | +0.128 | STANDARD |
| Macklin Celebrini: 2+ points | 0.333 | 0.460 | 47/55 | +0.099 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.472 | 0.595 | 60/41 | +0.101 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.284 | 0.405 | 41/60 | +0.099 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.134 | 0.245 | 25/76 | +0.094 | STANDARD |
| Ivar Stenberg: 2+ points | 0.107 | 0.200 | 22/82 | +0.063 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
