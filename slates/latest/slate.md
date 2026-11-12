# NHL slate 2026-11-11 — RESEARCH_ONLY

generated 2026-11-12T02:50:36Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 2 · markets on board: 3465 · contracts joined: 475 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 425, 'NO_EDGE': 29, 'OK': 21}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 69, 'game_early_goal': 2, 'first_goal': 72, 'game_winner': 4, 'player_goals': 128, 'game_overtime': 2, 'player_points': 100, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ ANA | 2026-11-12T03:00:00Z | T-<10m | 0.575 | 0.425 | 0.165 | 6.66 | 3.58 | 3.09 | 240 (25/215) | CONFIRMED/CONFIRMED |
| PIT @ SJS | 2026-11-12T03:00:00Z | T-<10m | 0.469 | 0.531 | 0.168 | 6.83 | 3.30 | 3.53 | 235 (25/210) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV11PITSJ-SJ | game_winner | 0.469 | 0.415 | 0.426 | 42 | 59 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV11PITSJ-PIT3 | game_spread | 0.203 | 0.245 | 0.236 | 25 | 76 | no | +0.024 | OK |
| KXNHLGAME-26NOV11PITSJ-PIT | game_winner | 0.531 | 0.575 | 0.566 | 58 | 43 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV11NSHANA-5 | game_total | 0.821 | 0.855 | 0.849 | 86 | 15 | no | +0.021 | OK |
| KXNHLSPREAD-26NOV11PITSJ-PIT2 | game_spread | 0.324 | 0.365 | 0.357 | 37 | 64 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA4 | team_total | 0.495 | 0.535 | 0.527 | 54 | 47 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV11NSHANA-7 | game_total | 0.526 | 0.565 | 0.557 | 57 | 44 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ4 | team_total | 0.433 | 0.395 | 0.403 | 40 | 61 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV11NSHANA-4 | game_total | 0.891 | 0.915 | 0.911 | 92 | 9 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH4 | team_total | 0.380 | 0.415 | 0.408 | 42 | 59 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ6 | team_total | 0.117 | 0.095 | 0.099 | 10 | 91 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV11NSHANA-6 | game_total | 0.635 | 0.665 | 0.659 | 67 | 34 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH3 | team_total | 0.595 | 0.630 | 0.623 | 64 | 38 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ3 | team_total | 0.643 | 0.615 | 0.621 | 62 | 39 | yes | +0.006 | OK |
| KXNHLTOTAL-26NOV11PITSJ-4 | game_total | 0.898 | 0.915 | 0.912 | 92 | 9 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA2 | team_total | 0.867 | 0.890 | 0.886 | 90 | 12 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH2 | team_total | 0.804 | 0.835 | 0.829 | 85 | 18 | no | +0.006 | OK |
| KXNHLTOTAL-26NOV11NSHANA-8 | game_total | 0.329 | 0.355 | 0.350 | 36 | 65 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ5 | team_total | 0.247 | 0.225 | 0.229 | 23 | 78 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4 | team_total | 0.479 | 0.505 | 0.500 | 51 | 50 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV11PITSJ-10 | game_total | 0.138 | 0.125 | 0.128 | 13 | 88 | yes | +0.000 | OK |
| KXNHLSPREAD-26NOV11PITSJ-SJ2 | game_spread | 0.263 | 0.240 | 0.244 | 25 | 77 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-9 | game_total | 0.262 | 0.245 | 0.248 | 25 | 76 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT5 | team_total | 0.286 | 0.310 | 0.305 | 32 | 70 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT2 | team_total | 0.863 | 0.880 | 0.877 | 89 | 13 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA5 | team_total | 0.297 | 0.320 | 0.315 | 33 | 69 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26NOV11NSHANA-ANA | game_winner | 0.575 | 0.555 | 0.559 | 56 | 45 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT3 | team_total | 0.688 | 0.710 | 0.706 | 72 | 30 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA3 | team_total | 0.699 | 0.720 | 0.716 | 73 | 29 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26NOV11NSHANA-NSH3 | game_spread | 0.135 | 0.145 | 0.143 | 15 | 86 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-5 | game_total | 0.835 | 0.850 | 0.847 | 86 | 16 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-3 | game_total | 0.974 | 0.980 | 0.979 | 99 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-7 | game_total | 0.549 | 0.565 | 0.562 | 57 | 44 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA6 | team_total | 0.152 | 0.140 | 0.142 | 15 | 87 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-3 | game_total | 0.976 | 0.980 | 0.979 | 99 | 3 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26NOV11NSHANA-ANA3 | game_spread | 0.236 | 0.245 | 0.243 | 25 | 76 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH5 | team_total | 0.207 | 0.220 | 0.217 | 23 | 79 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH6 | team_total | 0.095 | 0.100 | 0.099 | 11 | 91 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26NOV11PITSJ-SJ3 | game_spread | 0.159 | 0.155 | 0.156 | 16 | 85 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-2 | game_total | 0.990 | 0.990 | 0.990 |  | 2 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-6 | game_total | 0.656 | 0.665 | 0.663 | 67 | 34 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT6 | team_total | 0.146 | 0.145 | 0.145 | 15 | 86 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-8 | game_total | 0.353 | 0.345 | 0.347 | 35 | 66 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-9 | game_total | 0.241 | 0.245 | 0.244 | 25 | 76 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV11NSHANA-NSH2 | game_spread | 0.234 | 0.240 | 0.239 | 25 | 77 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-10 | game_total | 0.121 | 0.120 | 0.120 | 13 | 89 |  | -0.017 | NO_EDGE |
| KXNHLSPREAD-26NOV11NSHANA-ANA2 | game_spread | 0.363 | 0.365 | 0.365 | 37 | 64 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26NOV11NSHANA-NSH | game_winner | 0.425 | 0.425 | 0.425 | 43 | 58 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ2 | team_total | 0.833 | 0.835 | 0.835 | 85 | 18 |  | -0.024 | NO_EDGE |
| KXNHL1P-26NOV11NSHANA-ANA | period_winner |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV11NSHANA-NSH | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV11NSHANA-TIE | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV11NSHANA-ANA2 | period_spread |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV11NSHANA-NSH2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV11NSHANA-1 | period_total |  | 0.865 |  | 88 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV11NSHANA-2 | period_total |  | 0.605 |  | 61 | 40 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV11NSHANA-3 | period_total |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV11NSHANA-ANA | period_winner |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV11NSHANA-NSH | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV11NSHANA-TIE | period_winner |  | 0.290 |  | 31 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV11NSHANA-ANA2 | period_spread |  | 0.145 |  | 17 | 88 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV11NSHANA-NSH2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV11NSHANA-1 | period_total |  | 0.905 |  | 93 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV11NSHANA-2 | period_total |  | 0.650 |  | 66 | 36 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV11NSHANA-3 | period_total |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV11NSHANA-ANA | period_winner |  | 0.445 |  | 45 | 56 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV11NSHANA-NSH | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV11NSHANA-TIE | period_winner |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV11NSHANA-ANA2 | period_spread |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV11NSHANA-NSH2 | period_spread |  | 0.140 |  | 16 | 88 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV11NSHANA-1 | period_total |  | 0.910 |  | 95 | 13 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV11NSHANA-2 | period_total |  | 0.685 |  | 71 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV11NSHANA-3 | period_total |  | 0.430 |  | 44 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV11NSHANA-ANAAKILLORN17-1 | player_assists |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV11NSHANA-ANABSENNECKE45-1 | player_assists |  | 0.440 |  | 45 | 57 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV11NSHANA-ANABSENNECKE45-2 | player_assists |  | 0.105 |  | 11 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV11NSHANA-ANACGAUTHIER61-1 | player_assists |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV11NSHANA-ANACGAUTHIER61-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV11NSHANA-ANADHELLESON14-1 | player_assists |  | 0.235 |  | 24 | 77 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ ANA | 0.575 | 0.664 | 0.165 | 0.193 | 6.66 | 6.83 | 0.968/0.990 | KXNHLSPREAD-26NOV11NSHANA-ANA2 +0.091 |
| PIT @ SJS | 0.469 | 0.492 | 0.168 | 0.217 | 6.83 | 6.49 | 1.039/1.012 | KXNHLTOTAL-26NOV11PITSJ-8 -0.054 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Adam Wilsby: 1+ goals YES @ 4c · p 0.0762 (adj 0.0646) · $4.62 · thesis NSH:OFFENSE_4PLUS
- Beckett Sennecke: 1+ goals YES @ 33c · p 0.408 (adj 0.3872) · $15.65 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 11c · p 0.1554 (adj 0.1428) · $6.8 · thesis ANA:OFFENSE_4PLUS
- Steven Stamkos: 1+ goals NO @ 62c · p 0.6924 (adj 0.6731) · $20.0 · thesis NSH:SUPPRESSED
- Alexander Wennberg: 1+ assists NO @ 66c · p 0.7708 (adj 0.6923) · $16.47 · thesis SJS:SUPPRESSED
- Pittsburgh over 3.5 goals scored NO @ 50c · p 0.569 (adj 0.532) · $3.25 · thesis PIT:SUPPRESSED
- Ben Kindel: 1+ goals NO @ 76c · p 0.7945 (adj 0.7846) · $11.13 · thesis PIT:SUPPRESSED
- Pittsburgh wins by over 1.5 goals NO @ 64c · p 0.7029 (adj 0.6689) · $8.52 · thesis SJS:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ ANA** · priced 188/189 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 26.26, exp saves 23.11 (sd 6.29), pull risk 0.049
- NSH net: Justus Annunen (CONFIRMED) exp shots 30.23, exp saves 25.36 (sd 7.33), pull risk 0.102

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ points | 0.366 | 0.475 | 49/54 | +0.077 | STANDARD |
| Ryan O'Reilly: 1+ assists | 0.384 | 0.480 | 49/53 | +0.069 | STANDARD |
| Alex Killorn: 1+ points | 0.490 | 0.395 | 40/61 | +0.074 | STANDARD |
| Beckett Sennecke: 2+ points | 0.352 | 0.260 | 27/75 | +0.068 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.226 | 0.315 | 32/69 | +0.069 | STANDARD |
| Alex Killorn: 1+ assists | 0.332 | 0.245 | 25/76 | +0.069 | STANDARD |

**PIT @ SJS** · priced 183/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.19, exp saves 24.23 (sd 6.76), pull risk 0.07
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.94, exp saves 23.38 (sd 6.49), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alexander Wennberg: 1+ assists | 0.229 | 0.350 | 36/66 | +0.095 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.243 | 0.355 | 37/66 | +0.081 | STANDARD |
| Alexander Wennberg: 1+ points | 0.368 | 0.475 | 49/54 | +0.075 | STANDARD |
| Ivar Stenberg: 1+ points | 0.402 | 0.505 | 51/50 | +0.080 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.449 | 0.545 | 55/46 | +0.074 | STANDARD |
| Erik Karlsson: 1+ assists | 0.439 | 0.535 | 54/47 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
