# NHL slate 2026-11-06 — RESEARCH_ONLY

generated 2026-11-06T08:10:15Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2189 · contracts joined: 153 (unjoined to any game: 1280)
gates: {'UNSUPPORTED': 78, 'NO_EDGE': 56, 'OK': 19}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'game_early_goal': 3, 'game_winner': 6, 'game_overtime': 3, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ BUF | 2026-11-07T00:00:00Z | T-12h | 0.597 | 0.403 | 0.171 | 6.35 | 3.49 | 2.86 | 51 (25/26) | PROJECTED/PROJECTED |
| SJS @ MIN | 2026-11-07T01:00:00Z | T-12h | 0.701 | 0.299 | 0.151 | 6.43 | 3.89 | 2.54 | 51 (25/26) | PROJECTED/PROJECTED |
| ANA @ CGY | 2026-11-07T01:00:00Z | T-12h | 0.469 | 0.531 | 0.170 | 6.58 | 3.19 | 3.39 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV06ANACGY-CGY | game_winner | 0.469 | 0.535 | 0.522 | 54 | 47 | no | +0.043 | OK |
| KXNHLGAME-26NOV06ANACGY-ANA | game_winner | 0.531 | 0.465 | 0.478 | 47 | 54 | yes | +0.043 | OK |
| KXNHLSPREAD-26NOV06ANACGY-ANA2 | game_spread | 0.319 | 0.260 | 0.271 | 27 | 75 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA4 | team_total | 0.451 | 0.380 | 0.394 | 40 | 64 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5 | team_total | 0.265 | 0.205 | 0.216 | 22 | 81 | yes | +0.033 | OK |
| KXNHLSPREAD-26NOV06ANACGY-CGY2 | game_spread | 0.265 | 0.315 | 0.305 | 32 | 69 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV06ANACGY-CGY3 | game_spread | 0.159 | 0.205 | 0.195 | 21 | 80 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA3 | team_total | 0.662 | 0.605 | 0.617 | 62 | 41 | yes | +0.025 | OK |
| KXNHLTOTAL-26NOV06ANACGY-8 | game_total | 0.315 | 0.275 | 0.283 | 28 | 73 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA6 | team_total | 0.125 | 0.090 | 0.096 | 10 | 92 | yes | +0.019 | OK |
| KXNHLSPREAD-26NOV06ANACGY-ANA3 | game_spread | 0.199 | 0.165 | 0.171 | 17 | 84 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV06ANACGY-9 | game_total | 0.229 | 0.190 | 0.197 | 20 | 82 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN6 | team_total | 0.192 | 0.165 | 0.170 | 17 | 84 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY2 | team_total | 0.822 | 0.845 | 0.841 | 85 | 16 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV06SJMIN-8 | game_total | 0.298 | 0.270 | 0.276 | 28 | 74 | yes | +0.004 | OK |
| KXNHLSPREAD-26NOV06SJMIN-SJ3 | game_spread | 0.071 | 0.090 | 0.086 | 10 | 92 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV06ANACGY-ANA2 | team_total | 0.843 | 0.820 | 0.825 | 83 | 19 | yes | +0.004 | OK |
| KXNHLSPREAD-26NOV06CBJBUF-BUF3 | game_spread | 0.243 | 0.265 | 0.261 | 27 | 74 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV06ANACGY-7 | game_total | 0.510 | 0.485 | 0.490 | 49 | 52 | yes | +0.003 | OK |
| KXNHLTOTAL-26NOV06ANACGY-10 | game_total | 0.116 | 0.100 | 0.103 | 11 | 91 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-2 | game_total | 0.989 | 0.980 | 0.982 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-2 | game_total | 0.988 | 0.980 | 0.982 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26NOV06CBJBUF-BUF2 | game_spread | 0.376 | 0.395 | 0.391 | 40 | 61 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-5 | game_total | 0.798 | 0.785 | 0.788 | 79 | 22 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-7 | game_total | 0.484 | 0.465 | 0.469 | 47 | 54 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-9 | game_total | 0.207 | 0.190 | 0.193 | 20 | 82 |  | -0.004 | NO_EDGE |
| KXNHLGAME-26NOV06CBJBUF-BUF | game_winner | 0.597 | 0.615 | 0.611 | 62 | 39 |  | -0.004 | NO_EDGE |
| KXNHLGAME-26NOV06CBJBUF-CBJ | game_winner | 0.403 | 0.385 | 0.389 | 39 | 62 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV06CBJBUF-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-CBJ6 | team_total | 0.070 | 0.060 | 0.062 | 7 | 95 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY3 | team_total | 0.618 | 0.645 | 0.640 | 66 | 37 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN2 | team_total | 0.901 | 0.895 | 0.896 | 90 | 11 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF2 | team_total | 0.859 | 0.870 | 0.868 | 88 | 14 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ5 | team_total | 0.120 | 0.110 | 0.112 | 12 | 90 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-6 | game_total | 0.618 | 0.605 | 0.608 | 61 | 40 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-4 | game_total | 0.879 | 0.870 | 0.872 | 88 | 14 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV06CBJBUF-7 | game_total | 0.472 | 0.485 | 0.482 | 49 | 52 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ4 | team_total | 0.264 | 0.250 | 0.253 | 26 | 76 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY4 | team_total | 0.403 | 0.430 | 0.425 | 45 | 59 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN5 | team_total | 0.355 | 0.335 | 0.339 | 35 | 68 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV06CBJBUF-3 | game_total | 0.968 | 0.970 | 0.970 | 98 | 4 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV06CBJBUF-9 | game_total | 0.200 | 0.195 | 0.196 | 20 | 81 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26NOV06CBJBUF-CBJ3 | game_spread | 0.116 | 0.115 | 0.115 | 12 | 89 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-3 | game_total | 0.970 | 0.970 | 0.970 | 98 | 4 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF4 | team_total | 0.474 | 0.490 | 0.487 | 50 | 52 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26NOV06CBJBUF-CBJ2 | game_spread | 0.209 | 0.200 | 0.202 | 21 | 81 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF6 | team_total | 0.136 | 0.130 | 0.131 | 14 | 88 |  | -0.013 | NO_EDGE |
| KXNHLGAME-26NOV06SJMIN-SJ | game_winner | 0.299 | 0.305 | 0.304 | 31 | 70 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-5 | game_total | 0.807 | 0.805 | 0.805 | 81 | 20 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-4 | game_total | 0.883 | 0.880 | 0.881 | 89 | 13 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26NOV06CBJBUF-5 | game_total | 0.788 | 0.785 | 0.786 | 79 | 22 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF5 | team_total | 0.280 | 0.290 | 0.288 | 30 | 72 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-CBJ4 | team_total | 0.331 | 0.320 | 0.322 | 33 | 69 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-CBJ5 | team_total | 0.165 | 0.160 | 0.161 | 17 | 85 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26NOV06CBJBUF-4 | game_total | 0.866 | 0.870 | 0.869 | 88 | 14 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY5 | team_total | 0.223 | 0.240 | 0.237 | 26 | 78 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26NOV06ANACGY-3 | game_total | 0.973 | 0.975 | 0.975 | 99 | 4 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-6 | game_total | 0.602 | 0.595 | 0.596 | 60 | 41 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26NOV06SJMIN-10 | game_total | 0.101 | 0.095 | 0.096 | 11 | 92 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26NOV06SJMIN-MIN | game_winner | 0.701 | 0.705 | 0.704 | 71 | 30 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-CBJ3 | team_total | 0.551 | 0.540 | 0.542 | 55 | 47 |  | -0.017 | NO_EDGE |
| KXNHLSPREAD-26NOV06SJMIN-SJ2 | game_spread | 0.141 | 0.140 | 0.140 | 15 | 87 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ6 | team_total | 0.045 | 0.045 | 0.045 | 6 | 97 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26NOV06SJMIN-MIN3 | game_spread | 0.342 | 0.345 | 0.344 | 35 | 66 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-BUF3 | team_total | 0.683 | 0.695 | 0.693 | 71 | 32 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06ANACGY-CGY6 | team_total | 0.107 | 0.105 | 0.105 | 12 | 91 |  | -0.020 | NO_EDGE |
| KXNHLTOTAL-26NOV06CBJBUF-10 | game_total | 0.097 | 0.090 | 0.091 | 11 | 93 |  | -0.020 | NO_EDGE |
| KXNHLTOTAL-26NOV06CBJBUF-6 | game_total | 0.585 | 0.590 | 0.589 | 60 | 42 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06CBJBUF-CBJ2 | team_total | 0.770 | 0.775 | 0.774 | 79 | 24 |  | -0.023 | NO_EDGE |
| KXNHLTOTAL-26NOV06CBJBUF-8 | game_total | 0.281 | 0.280 | 0.280 | 29 | 73 |  | -0.023 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN3 | team_total | 0.757 | 0.755 | 0.756 | 77 | 26 |  | -0.025 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ3 | team_total | 0.472 | 0.460 | 0.462 | 48 | 56 |  | -0.025 | NO_EDGE |
| KXNHLSPREAD-26NOV06SJMIN-MIN2 | game_spread | 0.489 | 0.490 | 0.490 | 50 | 52 |  | -0.027 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-MIN4 | team_total | 0.560 | 0.550 | 0.552 | 57 | 47 |  | -0.027 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV06SJMIN-SJ2 | team_total | 0.710 | 0.710 | 0.710 | 73 | 31 |  | -0.034 | NO_EDGE |
| KXNHL1P-26NOV06CBJBUF-BUF | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV06CBJBUF-CBJ | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV06CBJBUF-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV06CBJBUF-BUF2 | period_spread |  | 0.145 |  | 17 | 88 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV06CBJBUF-CBJ2 | period_spread |  | 0.085 |  | 11 | 94 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ BUF | 0.597 | 0.528 | 0.171 | 0.215 | 6.35 | 6.32 | 0.998/0.990 | KXNHLGAME-26NOV06CBJBUF-CBJ +0.069 |
| SJS @ MIN | 0.701 | 0.613 | 0.151 | 0.212 | 6.43 | 6.38 | 0.995/1.034 | KXNHLSPREAD-26NOV06SJMIN-MIN2 -0.100 |
| ANA @ CGY | 0.469 | 0.444 | 0.170 | 0.208 | 6.58 | 6.76 | 0.998/1.016 | KXNHLTEAMTOTAL-26NOV06ANACGY-ANA3 +0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Buffalo wins by over 1.5 goals NO @ 61c · p 0.689 (adj 0.647) · $14.39 · thesis CBJ:WINS
- Minnesota wins by over 2.5 goals NO @ 66c · p 0.7393 (adj 0.6971) · $16.73 · thesis GAME:TIGHT
- San Jose over 3.5 goals scored YES @ 26c · p 0.3195 (adj 0.2848) · $1.3 · thesis SJS:OFFENSE_4PLUS
- Calgary wins by over 1.5 goals NO @ 69c · p 0.7527 (adj 0.7188) · $2.63 · thesis ANA:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CBJ @ BUF** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROJECTED) exp shots 26.94, exp saves 23.32 (sd 6.31), pull risk 0.058
- CBJ net: Cam Talbot (PROJECTED) exp shots 28.07, exp saves 24.05 (sd 6.75), pull risk 0.07

**SJS @ MIN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 26.54, exp saves 23.27 (sd 6.35), pull risk 0.048
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 30.36, exp saves 25.76 (sd 7.15), pull risk 0.084

**ANA @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.01, exp saves 25.62 (sd 7.07), pull risk 0.084
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.37, exp saves 23.8 (sd 6.59), pull risk 0.064

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
