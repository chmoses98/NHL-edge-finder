# NHL slate 2026-11-11 — RESEARCH_ONLY

generated 2026-11-12T02:25:33Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 3 · markets on board: 3489 · contracts joined: 706 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 631, 'NO_EDGE': 48, 'OK': 27}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 104, 'game_early_goal': 3, 'first_goal': 107, 'game_winner': 6, 'player_goals': 187, 'game_overtime': 3, 'player_points': 149, 'goalie_saves': 6, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ VGK | 2026-11-12T02:30:00Z | T-<10m | 0.558 | 0.442 | 0.172 | 6.47 | 3.42 | 3.05 | 231 (25/206) | CONFIRMED/CONFIRMED |
| NSH @ ANA | 2026-11-12T03:00:00Z | T-30m | 0.580 | 0.420 | 0.169 | 6.72 | 3.63 | 3.09 | 240 (25/215) | CONFIRMED/PROJECTED |
| PIT @ SJS | 2026-11-12T03:00:00Z | T-30m | 0.469 | 0.531 | 0.168 | 6.83 | 3.30 | 3.53 | 235 (25/210) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV11PITSJ-SJ | game_winner | 0.469 | 0.415 | 0.426 | 42 | 59 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV11PITSJ-PIT3 | game_spread | 0.203 | 0.245 | 0.236 | 25 | 76 | no | +0.024 | OK |
| KXNHLGAME-26NOV11PITSJ-PIT | game_winner | 0.531 | 0.575 | 0.566 | 58 | 43 | no | +0.022 | OK |
| KXNHLSPREAD-26NOV11PITSJ-PIT2 | game_spread | 0.324 | 0.365 | 0.357 | 37 | 64 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ4 | team_total | 0.433 | 0.395 | 0.403 | 40 | 61 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH2 | team_total | 0.805 | 0.840 | 0.833 | 85 | 17 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV11NSHANA-5 | game_total | 0.828 | 0.855 | 0.850 | 86 | 15 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH4 | team_total | 0.381 | 0.415 | 0.408 | 42 | 59 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV11UTAVGK-10 | game_total | 0.107 | 0.085 | 0.089 | 9 | 92 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ6 | team_total | 0.117 | 0.095 | 0.099 | 10 | 91 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV11NSHANA-4 | game_total | 0.895 | 0.915 | 0.911 | 92 | 9 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA4 | team_total | 0.504 | 0.535 | 0.529 | 54 | 47 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT3 | team_total | 0.688 | 0.715 | 0.710 | 72 | 29 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV11UTAVGK-7 | game_total | 0.495 | 0.465 | 0.471 | 47 | 54 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV11NSHANA-7 | game_total | 0.536 | 0.565 | 0.559 | 57 | 44 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV11PITSJ-5 | game_total | 0.835 | 0.855 | 0.851 | 86 | 15 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ3 | team_total | 0.643 | 0.615 | 0.621 | 62 | 39 | yes | +0.006 | OK |
| KXNHLTOTAL-26NOV11PITSJ-4 | game_total | 0.898 | 0.915 | 0.912 | 92 | 9 | no | +0.006 | OK |
| KXNHLTOTAL-26NOV11UTAVGK-9 | game_total | 0.216 | 0.190 | 0.195 | 20 | 82 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ5 | team_total | 0.247 | 0.225 | 0.229 | 23 | 78 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4 | team_total | 0.479 | 0.505 | 0.500 | 51 | 50 | no | +0.004 | OK |
| KXNHLGAME-26NOV11NSHANA-ANA | game_winner | 0.580 | 0.555 | 0.560 | 56 | 45 | yes | +0.003 | OK |
| KXNHLTOTAL-26NOV11UTAVGK-8 | game_total | 0.297 | 0.275 | 0.279 | 28 | 73 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-VGK6 | team_total | 0.130 | 0.115 | 0.118 | 12 | 89 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA6 | team_total | 0.161 | 0.140 | 0.144 | 15 | 87 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV11PITSJ-10 | game_total | 0.138 | 0.125 | 0.128 | 13 | 88 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-UTA5 | team_total | 0.201 | 0.185 | 0.188 | 19 | 82 | yes | +0.000 | OK |
| KXNHLSPREAD-26NOV11UTAVGK-UTA3 | game_spread | 0.141 | 0.155 | 0.152 | 16 | 85 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26NOV11PITSJ-SJ2 | game_spread | 0.263 | 0.245 | 0.248 | 25 | 76 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA2 | team_total | 0.873 | 0.890 | 0.887 | 90 | 12 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-9 | game_total | 0.262 | 0.245 | 0.248 | 25 | 76 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT5 | team_total | 0.286 | 0.310 | 0.305 | 32 | 70 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT2 | team_total | 0.863 | 0.880 | 0.877 | 89 | 13 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV11UTAVGK-3 | game_total | 0.971 | 0.965 | 0.966 | 97 | 4 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26NOV11NSHANA-NSH3 | game_spread | 0.134 | 0.145 | 0.143 | 15 | 86 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV11UTAVGK-4 | game_total | 0.875 | 0.885 | 0.883 | 89 | 12 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH3 | team_total | 0.598 | 0.620 | 0.616 | 63 | 39 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-UTA6 | team_total | 0.090 | 0.080 | 0.082 | 9 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-VGK3 | team_total | 0.670 | 0.655 | 0.658 | 66 | 35 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-7 | game_total | 0.549 | 0.565 | 0.562 | 57 | 44 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-VGK5 | team_total | 0.267 | 0.250 | 0.253 | 26 | 76 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-3 | game_total | 0.976 | 0.980 | 0.979 | 99 | 3 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-3 | game_total | 0.976 | 0.980 | 0.979 | 99 | 3 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26NOV11NSHANA-NSH2 | game_spread | 0.226 | 0.240 | 0.237 | 25 | 77 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV11UTAVGK-2 | game_total | 0.988 | 0.990 | 0.990 |  | 2 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-UTA2 | team_total | 0.798 | 0.805 | 0.804 | 81 | 20 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-8 | game_total | 0.333 | 0.345 | 0.343 | 35 | 66 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-VGK4 | team_total | 0.458 | 0.445 | 0.448 | 45 | 56 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA5 | team_total | 0.305 | 0.320 | 0.317 | 33 | 69 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH5 | team_total | 0.209 | 0.220 | 0.218 | 23 | 79 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26NOV11PITSJ-SJ3 | game_spread | 0.159 | 0.155 | 0.156 | 16 | 85 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA3 | team_total | 0.707 | 0.720 | 0.717 | 73 | 29 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-2 | game_total | 0.990 | 0.990 | 0.990 |  | 2 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-10 | game_total | 0.126 | 0.120 | 0.121 | 13 | 89 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-6 | game_total | 0.646 | 0.655 | 0.653 | 66 | 35 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH6 | team_total | 0.096 | 0.100 | 0.099 | 11 | 91 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-6 | game_total | 0.656 | 0.665 | 0.663 | 67 | 34 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT6 | team_total | 0.146 | 0.145 | 0.145 | 15 | 86 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV11UTAVGK-5 | game_total | 0.802 | 0.805 | 0.804 | 81 | 20 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-8 | game_total | 0.353 | 0.345 | 0.347 | 35 | 66 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV11UTAVGK-UTA2 | game_spread | 0.240 | 0.245 | 0.244 | 25 | 76 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV11NSHANA-ANA3 | game_spread | 0.241 | 0.245 | 0.244 | 25 | 76 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV11UTAVGK-VGK3 | game_spread | 0.218 | 0.215 | 0.216 | 22 | 79 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26NOV11UTAVGK-6 | game_total | 0.603 | 0.595 | 0.597 | 60 | 41 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ2 | team_total | 0.833 | 0.830 | 0.831 | 84 | 18 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26NOV11NSHANA-NSH | game_winner | 0.420 | 0.425 | 0.424 | 43 | 58 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-9 | game_total | 0.245 | 0.245 | 0.245 | 25 | 76 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-VGK2 | team_total | 0.850 | 0.850 | 0.850 | 86 | 16 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-UTA3 | team_total | 0.588 | 0.585 | 0.586 | 59 | 42 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-UTA4 | team_total | 0.377 | 0.375 | 0.375 | 38 | 63 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26NOV11UTAVGK-VGK | game_winner | 0.558 | 0.555 | 0.556 | 56 | 45 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26NOV11UTAVGK-UTA | game_winner | 0.442 | 0.445 | 0.444 | 45 | 56 |  | -0.020 | NO_EDGE |
| KXNHLSPREAD-26NOV11NSHANA-ANA2 | game_spread | 0.366 | 0.365 | 0.365 | 37 | 64 |  | -0.020 | NO_EDGE |
| KXNHLSPREAD-26NOV11UTAVGK-VGK2 | game_spread | 0.337 | 0.340 | 0.339 | 35 | 67 |  | -0.023 | NO_EDGE |
| KXNHL1P-26NOV11UTAVGK-VGK | period_winner |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV11UTAVGK-UTA | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV11UTAVGK-TIE | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV11UTAVGK-VGK2 | period_spread |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV11UTAVGK-UTA2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ VGK | 0.558 | 0.566 | 0.172 | 0.216 | 6.47 | 6.42 | 1.003/1.001 | KXNHLSPREAD-26NOV11UTAVGK-UTA2 -0.016 |
| NSH @ ANA | 0.580 | 0.664 | 0.169 | 0.191 | 6.72 | 6.83 | 0.968/0.994 | KXNHLSPREAD-26NOV11NSHANA-ANA3 +0.091 |
| PIT @ SJS | 0.469 | 0.492 | 0.168 | 0.217 | 6.83 | 6.49 | 1.039/1.012 | KXNHLTOTAL-26NOV11PITSJ-8 -0.054 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Brayden McNabb: 1+ goals YES @ 4c · p 0.085 (adj 0.0725) · $6.0 · thesis VGK:OFFENSE_4PLUS
- Ivan Barbashev: 1+ goals YES @ 16c · p 0.2213 (adj 0.2047) · $9.76 · thesis VGK:OFFENSE_4PLUS
- Braeden Bowman: 1+ goals YES @ 12c · p 0.1662 (adj 0.1534) · $6.96 · thesis VGK:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 17c · p 0.2208 (adj 0.2056) · $7.22 · thesis UTA:OFFENSE_4PLUS
- Beckett Sennecke: 1+ goals YES @ 33c · p 0.4129 (adj 0.3909) · $15.47 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 11c · p 0.1567 (adj 0.1438) · $6.46 · thesis ANA:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 18c · p 0.2351 (adj 0.2201) · $8.07 · thesis ANA:OFFENSE_4PLUS
- Steven Stamkos: 1+ goals NO @ 62c · p 0.6891 (adj 0.6693) · $19.42 · thesis NSH:SUPPRESSED
- Erik Karlsson: 1+ goals NO @ 82c · p 0.8553 (adj 0.8452) · $20.0 · thesis PIT:SUPPRESSED
- Pittsburgh over 3.5 goals scored NO @ 50c · p 0.569 (adj 0.532) · $3.12 · thesis PIT:SUPPRESSED
- Pittsburgh wins by over 1.5 goals NO @ 64c · p 0.7029 (adj 0.6689) · $7.33 · thesis SJS:WINS
- Alexander Wennberg: 1+ assists NO @ 67c · p 0.7708 (adj 0.6955) · $10.48 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ VGK** · priced 175/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.76, exp saves 23.29 (sd 6.44), pull risk 0.057
- UTA net: Sebastian Cossa (CONFIRMED) exp shots 27.42, exp saves 23.42 (sd 6.51), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brayden McNabb: 1+ assists | 0.305 | 0.180 | 19/83 | +0.104 | STANDARD |
| Brayden McNabb: 1+ points | 0.365 | 0.250 | 27/77 | +0.081 | STANDARD |
| Mitch Marner: 1+ assists | 0.448 | 0.545 | 56/47 | +0.064 | STANDARD |
| Lawson Crouse: 1+ points | 0.431 | 0.340 | 36/68 | +0.055 | STANDARD |
| Ivan Barbashev: 1+ points | 0.510 | 0.420 | 43/59 | +0.063 | STANDARD |
| Jack Eichel: 1+ assists | 0.471 | 0.560 | 57/45 | +0.062 | STANDARD |

**NSH @ ANA** · priced 188/189 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 26.26, exp saves 23.15 (sd 6.25), pull risk 0.047
- NSH net: Justus Annunen (PROJECTED) exp shots 30.23, exp saves 25.3 (sd 7.29), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Killorn: 1+ points | 0.497 | 0.390 | 40/62 | +0.080 | STANDARD |
| Ryan O'Reilly: 1+ assists | 0.381 | 0.480 | 49/53 | +0.072 | STANDARD |
| Mavrik Bourque: 1+ points | 0.372 | 0.470 | 48/54 | +0.071 | STANDARD |
| Beckett Sennecke: 1+ goals | 0.413 | 0.325 | 33/68 | +0.067 | STANDARD |
| Roman Josi: 1+ points | 0.512 | 0.600 | 61/41 | +0.061 | STANDARD |
| Filip Forsberg: 1+ assists | 0.383 | 0.470 | 49/55 | +0.050 | STANDARD |

**PIT @ SJS** · priced 183/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.19, exp saves 24.23 (sd 6.76), pull risk 0.07
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.94, exp saves 23.38 (sd 6.49), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alexander Wennberg: 1+ assists | 0.229 | 0.345 | 36/67 | +0.085 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.243 | 0.355 | 37/66 | +0.081 | STANDARD |
| Ivar Stenberg: 1+ points | 0.402 | 0.505 | 51/50 | +0.080 | STANDARD |
| Alexander Wennberg: 1+ points | 0.368 | 0.470 | 49/55 | +0.065 | STANDARD |
| Macklin Celebrini: 2+ points | 0.298 | 0.395 | 40/61 | +0.076 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.449 | 0.545 | 55/46 | +0.074 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
