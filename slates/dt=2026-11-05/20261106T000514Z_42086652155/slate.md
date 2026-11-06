# NHL slate 2026-11-05 — RESEARCH_ONLY

generated 2026-11-06T00:05:14Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 2 · markets on board: 4255 · contracts joined: 459 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 409, 'NO_EDGE': 39, 'OK': 11}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 65, 'game_early_goal': 2, 'first_goal': 72, 'game_winner': 4, 'player_goals': 127, 'game_overtime': 2, 'player_points': 90, 'goalie_saves': 3, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ EDM | 2026-11-06T01:00:00Z | T-30m | 0.642 | 0.358 | 0.156 | 6.99 | 4.00 | 3.00 | 236 (25/211) | CONFIRMED/PROBABLE |
| NSH @ COL | 2026-11-06T02:30:00Z | T-90m | 0.654 | 0.346 | 0.161 | 6.59 | 3.80 | 2.79 | 223 (25/198) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26NOV05ANAEDM-5 | game_total | 0.853 | 0.885 | 0.879 | 89 | 12 | no | +0.019 | OK |
| KXNHLSPREAD-26NOV05ANAEDM-ANA3 | game_spread | 0.103 | 0.125 | 0.120 | 13 | 88 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV05ANAEDM-10 | game_total | 0.153 | 0.135 | 0.138 | 14 | 87 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV05NSHCOL-4 | game_total | 0.889 | 0.905 | 0.902 | 91 | 10 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV05ANAEDM-2 | game_total | 0.994 | 0.985 | 0.987 | 99 | 2 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA2 | team_total | 0.786 | 0.805 | 0.801 | 81 | 20 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV05NSHCOL-NSH6 | team_total | 0.067 | 0.055 | 0.057 | 6 | 95 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-EDM6 | team_total | 0.212 | 0.185 | 0.190 | 20 | 83 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV05ANAEDM-4 | game_total | 0.914 | 0.925 | 0.923 | 93 | 8 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV05NSHCOL-NSH5 | team_total | 0.160 | 0.145 | 0.148 | 15 | 86 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV05NSHCOL-COL2 | team_total | 0.893 | 0.910 | 0.907 | 92 | 10 | no | +0.000 | OK |
| KXNHLTOTAL-26NOV05NSHCOL-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV05NSHCOL-8 | game_total | 0.314 | 0.295 | 0.299 | 30 | 71 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26NOV05NSHCOL-COL3 | game_spread | 0.296 | 0.315 | 0.311 | 32 | 69 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV05NSHCOL-9 | game_total | 0.228 | 0.215 | 0.217 | 22 | 79 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-EDM2 | team_total | 0.909 | 0.920 | 0.918 | 93 | 9 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV05NSHCOL-10 | game_total | 0.112 | 0.100 | 0.102 | 11 | 91 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV05ANAEDM-6 | game_total | 0.680 | 0.695 | 0.692 | 70 | 31 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26NOV05ANAEDM-ANA2 | game_spread | 0.185 | 0.195 | 0.193 | 20 | 81 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA6 | team_total | 0.089 | 0.080 | 0.082 | 9 | 93 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV05ANAEDM-7 | game_total | 0.570 | 0.585 | 0.582 | 59 | 42 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV05ANAEDM-3 | game_total | 0.982 | 0.980 | 0.980 | 99 | 3 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3 | team_total | 0.572 | 0.590 | 0.586 | 60 | 42 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26NOV05NSHCOL-COL2 | game_spread | 0.432 | 0.445 | 0.442 | 45 | 56 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA4 | team_total | 0.363 | 0.380 | 0.377 | 39 | 63 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05NSHCOL-NSH3 | team_total | 0.528 | 0.510 | 0.514 | 52 | 50 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05NSHCOL-NSH4 | team_total | 0.315 | 0.300 | 0.303 | 31 | 71 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV05ANAEDM-8 | game_total | 0.377 | 0.365 | 0.367 | 37 | 64 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26NOV05ANAEDM-EDM2 | game_spread | 0.437 | 0.425 | 0.427 | 43 | 58 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26NOV05NSHCOL-NSH3 | game_spread | 0.095 | 0.100 | 0.099 | 11 | 91 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05NSHCOL-COL6 | team_total | 0.178 | 0.170 | 0.172 | 18 | 84 |  | -0.012 | NO_EDGE |
| KXNHLGAME-26NOV05NSHCOL-COL | game_winner | 0.654 | 0.645 | 0.647 | 65 | 36 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV05NSHCOL-6 | game_total | 0.624 | 0.615 | 0.617 | 62 | 39 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV05NSHCOL-3 | game_total | 0.976 | 0.975 | 0.975 | 99 | 4 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26NOV05NSHCOL-7 | game_total | 0.513 | 0.505 | 0.507 | 51 | 50 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05NSHCOL-NSH2 | team_total | 0.757 | 0.750 | 0.751 | 76 | 26 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26NOV05ANAEDM-EDM | game_winner | 0.642 | 0.645 | 0.644 | 65 | 36 |  | -0.018 | NO_EDGE |
| KXNHLGAME-26NOV05ANAEDM-ANA | game_winner | 0.358 | 0.355 | 0.356 | 36 | 65 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26NOV05ANAEDM-EDM3 | game_spread | 0.303 | 0.305 | 0.305 | 31 | 70 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26NOV05NSHCOL-5 | game_total | 0.818 | 0.820 | 0.820 | 83 | 19 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-EDM5 | team_total | 0.378 | 0.370 | 0.372 | 38 | 64 |  | -0.019 | NO_EDGE |
| KXNHLSPREAD-26NOV05NSHCOL-NSH2 | game_spread | 0.171 | 0.170 | 0.170 | 18 | 84 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05NSHCOL-COL4 | team_total | 0.542 | 0.555 | 0.552 | 57 | 46 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26NOV05NSHCOL-NSH | game_winner | 0.346 | 0.345 | 0.345 | 35 | 66 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05NSHCOL-COL3 | team_total | 0.743 | 0.740 | 0.741 | 75 | 27 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05NSHCOL-COL5 | team_total | 0.336 | 0.330 | 0.331 | 34 | 68 |  | -0.020 | NO_EDGE |
| KXNHLTOTAL-26NOV05ANAEDM-9 | game_total | 0.278 | 0.280 | 0.280 | 29 | 73 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-EDM4 | team_total | 0.575 | 0.580 | 0.579 | 59 | 43 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5 | team_total | 0.194 | 0.195 | 0.195 | 21 | 82 |  | -0.025 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-EDM3 | team_total | 0.766 | 0.765 | 0.765 | 78 | 25 |  | -0.026 | NO_EDGE |
| KXNHL1P-26NOV05ANAEDM-TIE | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV05ANAEDM-EDM | period_winner |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV05ANAEDM-ANA | period_winner |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV05ANAEDM-EDM2 | period_spread |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV05ANAEDM-ANA2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV05ANAEDM-3 | period_total |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV05ANAEDM-2 | period_total |  | 0.635 |  | 64 | 37 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV05ANAEDM-1 | period_total |  | 0.880 |  | 89 | 13 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV05ANAEDM-TIE | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV05ANAEDM-EDM | period_winner |  | 0.420 |  | 44 | 60 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV05ANAEDM-ANA | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV05ANAEDM-EDM2 | period_spread |  | 0.170 |  | 19 | 85 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV05ANAEDM-ANA2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV05ANAEDM-3 | period_total |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV05ANAEDM-2 | period_total |  | 0.675 |  | 69 | 34 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV05ANAEDM-1 | period_total |  | 0.925 |  | 94 | 9 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV05ANAEDM-TIE | period_winner |  | 0.230 |  | 24 | 78 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV05ANAEDM-EDM | period_winner |  | 0.445 |  | 45 | 56 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV05ANAEDM-ANA | period_winner |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV05ANAEDM-EDM2 | period_spread |  | 0.215 |  | 24 | 81 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV05ANAEDM-ANA2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV05ANAEDM-3 | period_total |  | 0.445 |  | 46 | 57 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV05ANAEDM-2 | period_total |  | 0.735 |  | 76 | 29 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV05ANAEDM-1 | period_total |  | 0.935 |  | 95 | 8 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV05ANAEDM-EDMCDACH34-1 | player_assists |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-2 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV05ANAEDM-EDMRSHEA6-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV05ANAEDM-EDMRSHEA6-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV05ANAEDM-EDMRNUGENTHOPKINS93-2 | player_assists |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ EDM | 0.642 | 0.572 | 0.156 | 0.200 | 6.99 | 7.11 | 0.999/0.976 | KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3 +0.073 |
| NSH @ COL | 0.654 | 0.655 | 0.161 | 0.199 | 6.59 | 6.65 | 0.979/1.000 | KXNHLSPREAD-26NOV05NSHCOL-COL3 +0.015 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Tim Washe: 1+ goals YES @ 11c · p 0.1514 (adj 0.1398) · $5.93 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1223 (adj 0.113) · $4.3 · thesis ANA:OFFENSE_4PLUS
- Sam Colangelo: 1+ goals YES @ 13c · p 0.1664 (adj 0.156) · $4.98 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 16c · p 0.1988 (adj 0.1866) · $4.96 · thesis ANA:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 72c · p 0.7959 (adj 0.7554) · $20.0 · thesis NSH:SUPPRESSED
- Adam Wilsby: 1+ goals YES @ 5c · p 0.0697 (adj 0.0635) · $2.52 · thesis NSH:OFFENSE_4PLUS
- Nils Hoglander: 1+ goals YES @ 11c · p 0.1357 (adj 0.128) · $3.13 · thesis NSH:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 13c · p 0.1561 (adj 0.1483) · $2.93 · thesis NSH:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ EDM** · priced 184/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Matt Tomkins (CONFIRMED) exp shots 27.9, exp saves 24.13 (sd 6.74), pull risk 0.075
- ANA net: Laurent Brossoit (PROBABLE) exp shots 27.83, exp saves 23.61 (sd 6.86), pull risk 0.095

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 2+ points | 0.379 | 0.525 | 53/48 | +0.123 | STANDARD |
| Connor McDavid: 2+ points | 0.446 | 0.590 | 60/42 | +0.117 | STANDARD |
| Connor McDavid: 1+ assists | 0.590 | 0.715 | 73/30 | +0.095 | STANDARD |
| Connor McDavid: 2+ assists | 0.221 | 0.345 | 36/67 | +0.093 | STANDARD |
| Leon Draisaitl: 3+ points | 0.138 | 0.255 | 26/75 | +0.099 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.500 | 0.615 | 62/39 | +0.094 | STANDARD |

**NSH @ COL** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.73, exp saves 22.64 (sd 6.23), pull risk 0.051
- NSH net: Juuse Saros (PROJECTED) exp shots 32.54, exp saves 27.26 (sd 7.57), pull risk 0.094

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.381 | 0.470 | 49/55 | +0.052 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.527 | 0.610 | 62/40 | +0.056 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.204 | 0.285 | 29/72 | +0.062 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.172 | 0.250 | 27/77 | +0.046 | STANDARD |
| Mavrik Bourque: 1+ points | 0.353 | 0.420 | 43/59 | +0.040 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.145 | 0.205 | 22/81 | +0.035 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
