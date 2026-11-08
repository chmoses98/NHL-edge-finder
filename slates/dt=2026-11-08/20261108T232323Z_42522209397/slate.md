# NHL slate 2026-11-08 — RESEARCH_ONLY

generated 2026-11-08T23:23:23Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 3 · markets on board: 2578 · contracts joined: 683 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 608, 'OK': 54, 'NO_EDGE': 21}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 95, 'game_early_goal': 3, 'first_goal': 111, 'game_winner': 6, 'player_goals': 195, 'game_overtime': 3, 'player_points': 125, 'goalie_saves': 4, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ TOR | 2026-11-09T00:00:00Z | T-30m | 0.452 | 0.548 | 0.175 | 6.55 | 3.11 | 3.44 | 222 (25/197) | CONFIRMED/CONFIRMED |
| PHI @ CGY | 2026-11-09T00:00:00Z | T-30m | 0.566 | 0.434 | 0.190 | 5.42 | 2.91 | 2.50 | 231 (25/206) | CONFIRMED/CONFIRMED |
| PIT @ ANA | 2026-11-09T01:00:00Z | T-90m | 0.615 | 0.385 | 0.153 | 7.29 | 4.04 | 3.24 | 230 (25/205) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI4 | team_total | 0.251 | 0.380 | 0.352 | 39 | 63 | no | +0.103 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 | team_total | 0.462 | 0.585 | 0.561 | 59 | 42 | no | +0.101 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA2 | game_spread | 0.418 | 0.315 | 0.335 | 32 | 69 | yes | +0.083 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI2 | team_total | 0.709 | 0.805 | 0.788 | 81 | 20 | no | +0.080 | OK |
| KXNHLTOTAL-26NOV08PHICGY-5 | game_total | 0.662 | 0.755 | 0.738 | 76 | 25 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA6 | team_total | 0.222 | 0.135 | 0.150 | 14 | 87 | yes | +0.074 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI2 | game_spread | 0.213 | 0.305 | 0.285 | 31 | 70 | no | +0.073 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI3 | game_spread | 0.110 | 0.195 | 0.175 | 20 | 81 | no | +0.069 | OK |
| KXNHLTOTAL-26NOV08PHICGY-6 | game_total | 0.423 | 0.515 | 0.497 | 52 | 49 | no | +0.069 | OK |
| KXNHLGAME-26NOV08PHICGY-CGY | game_winner | 0.566 | 0.475 | 0.493 | 48 | 53 | yes | +0.069 | OK |
| KXNHLGAME-26NOV08PHICGY-PHI | game_winner | 0.434 | 0.525 | 0.507 | 53 | 48 | no | +0.069 | OK |
| KXNHLGAME-26NOV08PITANA-ANA | game_winner | 0.615 | 0.525 | 0.543 | 53 | 48 | yes | +0.068 | OK |
| KXNHLGAME-26NOV08PITANA-PIT | game_winner | 0.385 | 0.475 | 0.457 | 48 | 53 | no | +0.068 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT2 | game_spread | 0.210 | 0.295 | 0.277 | 30 | 71 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA5 | team_total | 0.394 | 0.315 | 0.330 | 32 | 69 | yes | +0.059 | OK |
| KXNHLTOTAL-26NOV08PHICGY-7 | game_total | 0.316 | 0.395 | 0.379 | 40 | 61 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI5 | team_total | 0.113 | 0.190 | 0.172 | 20 | 82 | no | +0.057 | OK |
| KXNHLTOTAL-26NOV08PHICGY-4 | game_total | 0.767 | 0.840 | 0.827 | 85 | 17 | no | +0.053 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA3 | game_spread | 0.284 | 0.210 | 0.224 | 22 | 80 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA4 | team_total | 0.589 | 0.515 | 0.530 | 52 | 49 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3 | team_total | 0.605 | 0.535 | 0.549 | 54 | 47 | yes | +0.047 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT3 | game_spread | 0.125 | 0.185 | 0.172 | 19 | 82 | no | +0.044 | OK |
| KXNHLSPREAD-26NOV08PHICGY-CGY2 | game_spread | 0.325 | 0.265 | 0.276 | 27 | 74 | yes | +0.041 | OK |
| KXNHLTOTAL-26NOV08PHICGY-8 | game_total | 0.158 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLTOTAL-26NOV08PITANA-8 | game_total | 0.417 | 0.365 | 0.375 | 37 | 64 | yes | +0.031 | OK |
| KXNHLTOTAL-26NOV08NJTOR-8 | game_total | 0.310 | 0.265 | 0.274 | 27 | 74 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV08PHICGY-9 | game_total | 0.105 | 0.150 | 0.140 | 16 | 86 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA3 | team_total | 0.769 | 0.715 | 0.726 | 73 | 30 | yes | +0.026 | OK |
| KXNHLTOTAL-26NOV08PITANA-9 | game_total | 0.319 | 0.275 | 0.284 | 28 | 73 | yes | +0.025 | OK |
| KXNHLGAME-26NOV08NJTOR-TOR | game_winner | 0.452 | 0.405 | 0.414 | 41 | 60 | yes | +0.025 | OK |
| KXNHLGAME-26NOV08NJTOR-NJ | game_winner | 0.548 | 0.595 | 0.586 | 60 | 41 | no | +0.025 | OK |
| KXNHLTOTAL-26NOV08NJTOR-9 | game_total | 0.224 | 0.185 | 0.192 | 19 | 82 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV08PITANA-10 | game_total | 0.182 | 0.140 | 0.148 | 15 | 87 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR4 | team_total | 0.388 | 0.345 | 0.353 | 35 | 66 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI6 | team_total | 0.044 | 0.075 | 0.067 | 8 | 93 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT3 | team_total | 0.623 | 0.665 | 0.657 | 67 | 34 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV08NJTOR-7 | game_total | 0.508 | 0.465 | 0.474 | 47 | 54 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR5 | team_total | 0.210 | 0.175 | 0.182 | 18 | 83 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA2 | team_total | 0.905 | 0.875 | 0.882 | 88 | 13 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR2 | team_total | 0.809 | 0.775 | 0.782 | 78 | 23 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT2 | team_total | 0.825 | 0.860 | 0.854 | 87 | 15 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT4 | team_total | 0.417 | 0.460 | 0.451 | 47 | 55 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV08NJTOR-NJ3 | game_spread | 0.213 | 0.245 | 0.238 | 25 | 76 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV08NJTOR-TOR2 | game_spread | 0.246 | 0.215 | 0.221 | 22 | 79 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV08PHICGY-10 | game_total | 0.042 | 0.065 | 0.060 | 7 | 94 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV08PHICGY-3 | game_total | 0.934 | 0.960 | 0.956 | 97 | 5 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV08NJTOR-6 | game_total | 0.617 | 0.585 | 0.592 | 59 | 42 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV08PITANA-6 | game_total | 0.723 | 0.695 | 0.701 | 70 | 31 | yes | +0.009 | OK |
| KXNHLTOTAL-26NOV08PITANA-7 | game_total | 0.615 | 0.585 | 0.591 | 59 | 42 | yes | +0.008 | OK |
| KXNHLSPREAD-26NOV08NJTOR-NJ2 | game_spread | 0.337 | 0.365 | 0.359 | 37 | 64 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR6 | team_total | 0.092 | 0.070 | 0.074 | 8 | 94 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV08NJTOR-10 | game_total | 0.111 | 0.090 | 0.094 | 10 | 92 | yes | +0.004 | OK |
| KXNHLSPREAD-26NOV08PHICGY-CGY3 | game_spread | 0.194 | 0.170 | 0.175 | 18 | 84 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV08PITANA-2 | game_total | 0.994 | 0.985 | 0.988 | 99 | 2 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT5 | team_total | 0.238 | 0.260 | 0.255 | 27 | 75 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV08PHICGY-2 | game_total | 0.970 | 0.980 | 0.978 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV08PITANA-5 | game_total | 0.875 | 0.865 | 0.867 | 87 | 14 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV08NJTOR-2 | game_total | 0.987 | 0.980 | 0.982 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08NJTOR-NJ6 | team_total | 0.134 | 0.110 | 0.114 | 13 | 91 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV08NJTOR-TOR3 | game_spread | 0.144 | 0.135 | 0.137 | 14 | 87 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV08PITANA-3 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV08NJTOR-4 | game_total | 0.882 | 0.875 | 0.876 | 88 | 13 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV08PITANA-4 | game_total | 0.928 | 0.925 | 0.926 | 93 | 8 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV08NJTOR-3 | game_total | 0.971 | 0.970 | 0.970 | 98 | 4 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08NJTOR-NJ2 | team_total | 0.852 | 0.860 | 0.858 | 87 | 15 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08PHICGY-CGY3 | team_total | 0.564 | 0.575 | 0.573 | 58 | 43 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT6 | team_total | 0.114 | 0.120 | 0.119 | 13 | 89 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV08NJTOR-5 | game_total | 0.809 | 0.805 | 0.806 | 81 | 20 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08PHICGY-CGY2 | team_total | 0.790 | 0.785 | 0.786 | 79 | 22 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08PHICGY-CGY6 | team_total | 0.071 | 0.075 | 0.074 | 9 | 94 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08PHICGY-CGY4 | team_total | 0.339 | 0.350 | 0.348 | 36 | 66 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08NJTOR-NJ5 | team_total | 0.268 | 0.265 | 0.266 | 27 | 74 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08NJTOR-NJ4 | team_total | 0.460 | 0.470 | 0.468 | 48 | 54 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08PHICGY-CGY5 | team_total | 0.168 | 0.170 | 0.170 | 18 | 84 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08NJTOR-NJ3 | team_total | 0.669 | 0.670 | 0.670 | 68 | 34 |  | -0.025 | NO_EDGE |
| KXNHL1P-26NOV08NJTOR-NJ | period_winner |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV08NJTOR-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV08NJTOR-TOR | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV08NJTOR-NJ2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV08NJTOR-TOR2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ TOR | 0.452 | 0.495 | 0.175 | 0.220 | 6.55 | 6.30 | 0.956/0.949 | KXNHLTEAMTOTAL-26NOV08NJTOR-NJ5 -0.053 |
| PHI @ CGY | 0.566 | 0.511 | 0.190 | 0.219 | 5.42 | 5.97 | 0.978/0.994 | KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 +0.114 |
| PIT @ ANA | 0.615 | 0.641 | 0.153 | 0.194 | 7.29 | 7.18 | 0.986/1.042 | KXNHLTEAMTOTAL-26NOV08PITANA-PIT4 -0.030 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Teddy Blueger: 1+ goals YES @ 9c · p 0.1491 (adj 0.1318) · $8.57 · thesis TOR:OFFENSE_4PLUS
- Easton Cowan: 1+ goals YES @ 17c · p 0.2149 (adj 0.2024) · $6.45 · thesis TOR:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 59c · p 0.6469 (adj 0.6314) · $14.93 · thesis NJD:SUPPRESSED
- Cody Glass: 1+ goals YES @ 12c · p 0.1509 (adj 0.1419) · $4.11 · thesis NJD:OFFENSE_4PLUS
- Travis Konecny: 1+ assists NO @ 65c · p 0.7362 (adj 0.6906) · $14.88 · thesis PHI:SUPPRESSED
- Porter Martone: 1+ goals NO @ 77c · p 0.8132 (adj 0.7999) · $15.12 · thesis PHI:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 9c · p 0.1138 (adj 0.1066) · $2.72 · thesis CGY:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 11c · p 0.1563 (adj 0.1435) · $6.79 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 19c · p 0.2442 (adj 0.2281) · $8.0 · thesis ANA:OFFENSE_4PLUS
- Kaedan Korczak: 1+ goals YES @ 3c · p 0.0516 (adj 0.0437) · $2.38 · thesis DIFFUSE
- Beckett Sennecke: 1+ goals YES @ 34c · p 0.4006 (adj 0.3842) · $10.95 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ TOR** · priced 168/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 32.87, exp saves 28.44 (sd 7.46), pull risk 0.06
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.54, exp saves 22.93 (sd 6.4), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Tavares: 1+ assists | 0.242 | 0.360 | 38/66 | +0.082 | STANDARD |
| Jack Hughes: 2+ points | 0.253 | 0.360 | 38/66 | +0.071 | STANDARD |
| Luke Evangelista: 1+ assists | 0.255 | 0.360 | 37/65 | +0.079 | STANDARD |
| Jack Hughes: 1+ assists | 0.418 | 0.520 | 53/49 | +0.074 | STANDARD |
| Evan Rodrigues: 1+ assists | 0.152 | 0.245 | 25/76 | +0.075 | STANDARD |
| John Tavares: 1+ points | 0.457 | 0.545 | 55/46 | +0.066 | STANDARD |

**PHI @ CGY** · priced 177/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 26.62, exp saves 23.21 (sd 6.38), pull risk 0.051
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.45, exp saves 23.82 (sd 6.48), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ assists | 0.264 | 0.355 | 36/65 | +0.070 | STANDARD |
| Travis Konecny: 1+ points | 0.428 | 0.500 | 51/51 | +0.044 | STANDARD |
| Porter Martone: 1+ points | 0.399 | 0.465 | 48/55 | +0.034 | STANDARD |
| Cam York: 1+ goals | 0.073 | 0.010 | 6/ | +0.009 | STANDARD |
| Porter Martone: 1+ goals | 0.187 | 0.240 | 25/77 | +0.031 | STANDARD |
| Travis Sanheim: 1+ points | 0.384 | 0.340 | 35/67 | +0.018 | STANDARD |

**PIT @ ANA** · priced 175/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (PROJECTED) exp shots 26.45, exp saves 23.06 (sd 6.45), pull risk 0.063
- PIT net: Arturs Silovs (CONFIRMED) exp shots 28.23, exp saves 23.71 (sd 6.93), pull risk 0.106

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Erik Karlsson: 1+ points | 0.510 | 0.595 | 61/42 | +0.053 | STANDARD |
| Sidney Crosby: 1+ assists | 0.371 | 0.455 | 47/56 | +0.052 | STANDARD |
| Alex Killorn: 1+ points | 0.484 | 0.410 | 42/60 | +0.047 | STANDARD |
| Ben Kindel: 1+ points | 0.419 | 0.490 | 51/53 | +0.033 | STANDARD |
| Erik Karlsson: 1+ assists | 0.430 | 0.500 | 51/51 | +0.042 | STANDARD |
| Jackson LaCombe: 2+ points | 0.291 | 0.225 | 24/79 | +0.039 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
