# NHL slate 2026-10-29 — RESEARCH_ONLY

generated 2026-10-30T01:08:55Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 3 · markets on board: 4374 · contracts joined: 684 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 609, 'OK': 43, 'NO_EDGE': 32}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 97, 'game_early_goal': 3, 'first_goal': 109, 'game_winner': 6, 'player_goals': 190, 'game_overtime': 3, 'player_points': 129, 'goalie_saves': 6, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ ANA | 2026-10-30T02:00:00Z | T-30m | 0.503 | 0.497 | 0.173 | 6.43 | 3.22 | 3.21 | 237 (25/212) | PROJECTED/PROBABLE |
| OTT @ LAK | 2026-10-30T02:00:00Z | T-30m | 0.517 | 0.483 | 0.178 | 6.13 | 3.12 | 3.01 | 227 (25/202) | CONFIRMED/CONFIRMED |
| VAN @ SJS | 2026-10-30T02:00:00Z | T-30m | 0.591 | 0.409 | 0.160 | 7.13 | 3.87 | 3.25 | 220 (25/195) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF4 | team_total | 0.411 | 0.495 | 0.478 | 50 | 51 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF3 | team_total | 0.626 | 0.710 | 0.694 | 72 | 30 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF2 | game_spread | 0.287 | 0.365 | 0.349 | 37 | 64 | no | +0.057 | OK |
| KXNHLGAME-26OCT29BUFANA-ANA | game_winner | 0.503 | 0.425 | 0.440 | 43 | 58 | yes | +0.056 | OK |
| KXNHLGAME-26OCT29BUFANA-BUF | game_winner | 0.497 | 0.575 | 0.560 | 58 | 43 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF3 | game_spread | 0.175 | 0.245 | 0.230 | 25 | 76 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF5 | team_total | 0.225 | 0.300 | 0.284 | 31 | 71 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT29BUFANA-7 | game_total | 0.484 | 0.545 | 0.533 | 55 | 46 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT29VANSJ-10 | game_total | 0.163 | 0.115 | 0.123 | 12 | 89 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF2 | team_total | 0.827 | 0.875 | 0.866 | 88 | 13 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT29BUFANA-6 | game_total | 0.599 | 0.655 | 0.644 | 66 | 35 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT29VANSJ-8 | game_total | 0.398 | 0.345 | 0.355 | 35 | 66 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT3 | game_spread | 0.157 | 0.205 | 0.195 | 21 | 80 | no | +0.032 | OK |
| KXNHLGAME-26OCT29OTTLA-LA | game_winner | 0.517 | 0.465 | 0.475 | 47 | 54 | yes | +0.029 | OK |
| KXNHLGAME-26OCT29OTTLA-OTT | game_winner | 0.483 | 0.535 | 0.525 | 54 | 47 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT29BUFANA-ANA2 | game_spread | 0.290 | 0.240 | 0.249 | 25 | 77 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT29VANSJ-7 | game_total | 0.594 | 0.545 | 0.555 | 55 | 46 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT29VANSJ-9 | game_total | 0.298 | 0.250 | 0.259 | 26 | 76 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT29VANSJ-6 | game_total | 0.700 | 0.655 | 0.664 | 66 | 35 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT29BUFANA-5 | game_total | 0.800 | 0.835 | 0.828 | 84 | 17 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT29BUFANA-4 | game_total | 0.874 | 0.910 | 0.904 | 92 | 10 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN6 | team_total | 0.115 | 0.080 | 0.086 | 9 | 93 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT2 | game_spread | 0.266 | 0.305 | 0.297 | 31 | 70 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN5 | team_total | 0.239 | 0.205 | 0.211 | 21 | 80 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6 | team_total | 0.106 | 0.145 | 0.136 | 16 | 87 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT29OTTLA-LA2 | game_spread | 0.299 | 0.265 | 0.272 | 27 | 74 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA3 | team_total | 0.611 | 0.575 | 0.582 | 58 | 43 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA2 | team_total | 0.815 | 0.785 | 0.791 | 79 | 22 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT29BUFANA-8 | game_total | 0.291 | 0.325 | 0.318 | 33 | 68 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN3 | team_total | 0.629 | 0.595 | 0.602 | 60 | 41 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT29BUFANA-9 | game_total | 0.211 | 0.235 | 0.230 | 24 | 77 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT3 | team_total | 0.587 | 0.620 | 0.613 | 63 | 39 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT2 | team_total | 0.794 | 0.820 | 0.815 | 83 | 19 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT29VANSJ-SJ3 | game_spread | 0.261 | 0.285 | 0.280 | 29 | 72 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT29BUFANA-ANA3 | game_spread | 0.174 | 0.155 | 0.159 | 16 | 85 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT29OTTLA-6 | game_total | 0.552 | 0.525 | 0.530 | 53 | 48 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA4 | team_total | 0.390 | 0.360 | 0.366 | 37 | 65 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ6 | team_total | 0.194 | 0.170 | 0.175 | 18 | 84 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT29OTTLA-9 | game_total | 0.173 | 0.155 | 0.159 | 16 | 85 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN4 | team_total | 0.419 | 0.390 | 0.396 | 40 | 62 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT29VANSJ-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT29BUFANA-10 | game_total | 0.102 | 0.120 | 0.116 | 13 | 89 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT29OTTLA-7 | game_total | 0.437 | 0.415 | 0.419 | 42 | 59 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA6 | team_total | 0.106 | 0.090 | 0.093 | 10 | 92 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT29BUFANA-3 | game_total | 0.969 | 0.980 | 0.978 | 99 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT29OTTLA-8 | game_total | 0.252 | 0.230 | 0.234 | 24 | 78 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA3 | team_total | 0.625 | 0.605 | 0.609 | 61 | 40 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT29BUFANA-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA5 | team_total | 0.208 | 0.185 | 0.190 | 20 | 83 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA6 | team_total | 0.093 | 0.075 | 0.078 | 9 | 94 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT29OTTLA-LA3 | game_spread | 0.176 | 0.165 | 0.167 | 17 | 84 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4 | team_total | 0.413 | 0.390 | 0.395 | 40 | 62 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT29VANSJ-VAN3 | game_spread | 0.133 | 0.125 | 0.127 | 13 | 88 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT4 | team_total | 0.368 | 0.390 | 0.386 | 40 | 62 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT29OTTLA-3 | game_total | 0.963 | 0.970 | 0.969 | 98 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT5 | team_total | 0.194 | 0.210 | 0.207 | 22 | 80 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT29OTTLA-10 | game_total | 0.080 | 0.070 | 0.072 | 8 | 94 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT29VANSJ-5 | game_total | 0.863 | 0.855 | 0.857 | 86 | 15 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT29VANSJ-4 | game_total | 0.919 | 0.910 | 0.912 | 92 | 10 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT29OTTLA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT29VANSJ-VAN2 | game_spread | 0.224 | 0.215 | 0.217 | 22 | 79 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT29OTTLA-4 | game_total | 0.849 | 0.855 | 0.854 | 86 | 15 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN2 | team_total | 0.822 | 0.810 | 0.812 | 82 | 20 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT29VANSJ-VAN | game_winner | 0.409 | 0.395 | 0.398 | 40 | 61 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT29VANSJ-SJ | game_winner | 0.591 | 0.605 | 0.602 | 61 | 40 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT29VANSJ-3 | game_total | 0.982 | 0.980 | 0.980 | 99 | 3 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ5 | team_total | 0.357 | 0.345 | 0.347 | 35 | 66 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29OTTLA-OTT6 | team_total | 0.086 | 0.085 | 0.085 | 9 | 92 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ2 | team_total | 0.896 | 0.895 | 0.895 | 90 | 11 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA5 | team_total | 0.230 | 0.215 | 0.218 | 23 | 80 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT29VANSJ-SJ2 | game_spread | 0.386 | 0.395 | 0.393 | 40 | 61 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29BUFANA-ANA2 | team_total | 0.825 | 0.830 | 0.829 | 84 | 18 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ3 | team_total | 0.747 | 0.740 | 0.741 | 75 | 27 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT29OTTLA-5 | game_total | 0.764 | 0.765 | 0.765 | 77 | 24 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT29VANSJ-SJ4 | team_total | 0.555 | 0.550 | 0.551 | 56 | 46 |  | -0.022 | NO_EDGE |
| KXNHL1P-26OCT29BUFANA-ANA | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT29BUFANA-BUF | period_winner |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT29BUFANA-TIE | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT29BUFANA-ANA2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT29BUFANA-BUF2 | period_spread |  | 0.125 |  | 13 | 88 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ ANA | 0.503 | 0.567 | 0.173 | 0.216 | 6.43 | 6.64 | 1.025/1.000 | KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4 +0.074 |
| OTT @ LAK | 0.517 | 0.529 | 0.178 | 0.224 | 6.13 | 6.01 | 0.996/1.040 | KXNHLTOTAL-26OCT29OTTLA-6 -0.027 |
| VAN @ SJS | 0.591 | 0.558 | 0.160 | 0.212 | 7.13 | 6.61 | 1.040/1.034 | KXNHLTOTAL-26OCT29VANSJ-8 -0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Tim Washe: 1+ goals YES @ 10c · p 0.155 (adj 0.1375) · $7.52 · thesis ANA:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 62c · p 0.6982 (adj 0.6762) · $20.0 · thesis BUF:SUPPRESSED
- Alex Killorn: 1+ goals YES @ 17c · p 0.2225 (adj 0.2069) · $7.7 · thesis ANA:OFFENSE_4PLUS
- Beckett Sennecke: 1+ goals YES @ 30c · p 0.3479 (adj 0.3347) · $7.12 · thesis ANA:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0754 (adj 0.0678) · $3.4 · thesis LAK:OFFENSE_4PLUS
- Thomas Chabot: 1+ assists NO @ 70c · p 0.7903 (adj 0.7427) · $18.96 · thesis OTT:SUPPRESSED
- Drake Batherson: 1+ goals NO @ 69c · p 0.7331 (adj 0.7211) · $11.04 · thesis OTT:SUPPRESSED
- Erik Gustafsson: 1+ assists NO @ 64c · p 0.7084 (adj 0.6717) · $12.46 · thesis LAK:SUPPRESSED
- Ivar Stenberg: 1+ goals NO @ 72c · p 0.807 (adj 0.784) · $20.0 · thesis SJS:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 18c · p 0.2182 (adj 0.2074) · $5.37 · thesis VAN:OFFENSE_4PLUS
- Filip Chytil: 1+ assists NO @ 72c · p 0.7941 (adj 0.752) · $20.0 · thesis VAN:SUPPRESSED
- Filip Chytil: 1+ goals YES @ 20c · p 0.2326 (adj 0.2232) · $3.73 · thesis VAN:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ ANA** · priced 174/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.32, exp saves 23.88 (sd 6.56), pull risk 0.062
- BUF net: Colten Ellis (PROBABLE) exp shots 28.64, exp saves 24.43 (sd 6.9), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.263 | 0.140 | 15/87 | +0.104 | STANDARD |
| Lukas Dostal: 27+ saves | 0.341 | 0.455 | 49/58 | +0.062 |  |
| Tage Thompson: 1+ points | 0.525 | 0.635 | 64/37 | +0.089 | STANDARD |
| Tage Thompson: 2+ points | 0.172 | 0.275 | 29/74 | +0.075 | STANDARD |
| Noah Warren: 1+ assists | 0.255 | 0.160 | 21/89 | +0.033 | STANDARD |
| Jackson LaCombe: 2+ points | 0.264 | 0.170 | 20/86 | +0.053 | STANDARD |

**OTT @ LAK** · priced 168/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 27.33, exp saves 23.88 (sd 6.44), pull risk 0.051
- OTT net: Jonas Johansson (CONFIRMED) exp shots 26.32, exp saves 22.76 (sd 6.28), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ points | 0.388 | 0.515 | 52/49 | +0.105 | STANDARD |
| Jake Sanderson: 1+ assists | 0.308 | 0.435 | 44/57 | +0.105 | STANDARD |
| Thomas Chabot: 1+ points | 0.285 | 0.385 | 39/62 | +0.078 | STANDARD |
| Thomas Chabot: 1+ assists | 0.210 | 0.305 | 31/70 | +0.076 | STANDARD |
| Jake Sanderson: 2+ points | 0.086 | 0.180 | 19/83 | +0.074 | STANDARD |
| Tim Stutzle: 1+ points | 0.557 | 0.635 | 64/37 | +0.056 | STANDARD |

**VAN @ SJS** · priced 161/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 25.57, exp saves 22.3 (sd 6.23), pull risk 0.06
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 29.42, exp saves 25.06 (sd 6.94), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.425 | 0.575 | 58/43 | +0.128 | STANDARD |
| Macklin Celebrini: 2+ points | 0.333 | 0.465 | 48/55 | +0.099 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.472 | 0.595 | 60/41 | +0.101 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.284 | 0.405 | 41/60 | +0.099 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.134 | 0.245 | 25/76 | +0.094 | STANDARD |
| Ivar Stenberg: 2+ points | 0.107 | 0.215 | 22/79 | +0.092 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
