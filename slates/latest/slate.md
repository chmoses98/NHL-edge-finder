# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T23:42:57Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 6 · markets on board: 4781 · contracts joined: 1481 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 1331, 'OK': 118, 'NO_EDGE': 32}
families: {'period_winner': 54, 'period_spread': 36, 'period_total': 54, 'player_assists': 241, 'game_early_goal': 6, 'first_goal': 222, 'game_winner': 12, 'player_goals': 384, 'game_overtime': 6, 'player_points': 320, 'goalie_saves': 8, 'game_spread': 24, 'team_total': 60, 'game_total': 54}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ STL | 2026-10-23T00:00:00Z | T-10m | 0.574 | 0.426 | 0.172 | 6.39 | 3.44 | 2.95 | 266 (25/241) | CONFIRMED/CONFIRMED |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-10m | 0.593 | 0.407 | 0.187 | 5.47 | 3.01 | 2.45 | 258 (25/233) | CONFIRMED/CONFIRMED |
| MIN @ CGY | 2026-10-23T01:00:00Z | T-60m | 0.463 | 0.537 | 0.188 | 5.73 | 2.75 | 2.98 | 235 (25/210) | CONFIRMED/CONFIRMED |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-60m | 0.532 | 0.468 | 0.176 | 6.55 | 3.37 | 3.17 | 236 (25/211) | CONFIRMED/PROBABLE |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-90m | 0.491 | 0.509 | 0.174 | 6.27 | 3.10 | 3.17 | 232 (25/207) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-90m | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 254 (25/229) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.358 | 0.510 | 0.479 | 52 | 50 | no | +0.124 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.578 | 0.715 | 0.690 | 72 | 29 | no | +0.117 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.179 | 0.305 | 0.276 | 31 | 70 | no | +0.106 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.537 | 0.655 | 0.632 | 66 | 35 | no | +0.097 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.463 | 0.345 | 0.368 | 35 | 66 | yes | +0.097 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.396 | 0.520 | 0.495 | 53 | 49 | no | +0.096 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.308 | 0.425 | 0.400 | 43 | 58 | no | +0.095 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.491 | 0.375 | 0.398 | 38 | 63 | yes | +0.095 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.509 | 0.625 | 0.602 | 63 | 38 | no | +0.095 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.574 | 0.465 | 0.487 | 47 | 54 | yes | +0.086 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.182 | 0.295 | 0.269 | 31 | 72 | no | +0.084 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.356 | 0.255 | 0.274 | 26 | 75 | yes | +0.083 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.292 | 0.395 | 0.373 | 40 | 61 | no | +0.081 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.178 | 0.275 | 0.253 | 28 | 73 | no | +0.078 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.227 | 0.325 | 0.304 | 33 | 68 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA3 | team_total | 0.619 | 0.720 | 0.701 | 73 | 29 | no | +0.077 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.426 | 0.525 | 0.505 | 53 | 48 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.462 | 0.365 | 0.384 | 37 | 64 | yes | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA5 | team_total | 0.217 | 0.310 | 0.290 | 32 | 70 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.672 | 0.585 | 0.603 | 59 | 42 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.265 | 0.185 | 0.199 | 19 | 82 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.480 | 0.565 | 0.548 | 57 | 44 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.228 | 0.155 | 0.168 | 16 | 85 | yes | +0.059 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.795 | 0.870 | 0.857 | 88 | 14 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.278 | 0.205 | 0.218 | 21 | 80 | yes | +0.056 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.671 | 0.745 | 0.731 | 75 | 26 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.367 | 0.445 | 0.429 | 45 | 56 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.367 | 0.445 | 0.429 | 45 | 56 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.133 | 0.205 | 0.189 | 21 | 80 | no | +0.056 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.468 | 0.545 | 0.530 | 55 | 46 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.245 | 0.175 | 0.188 | 18 | 83 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.592 | 0.670 | 0.655 | 68 | 34 | no | +0.053 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.532 | 0.465 | 0.478 | 47 | 54 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT22MINCGY-5 | game_total | 0.713 | 0.775 | 0.763 | 78 | 23 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.262 | 0.325 | 0.312 | 33 | 68 | no | +0.043 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.615 | 0.602 | 62 | 39 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.156 | 0.215 | 0.202 | 22 | 79 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA2 | team_total | 0.821 | 0.880 | 0.870 | 89 | 13 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR4 | team_total | 0.402 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.188 | 0.255 | 0.240 | 27 | 76 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR3 | team_total | 0.616 | 0.675 | 0.664 | 68 | 33 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.803 | 0.860 | 0.850 | 87 | 15 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.566 | 0.625 | 0.613 | 63 | 38 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA3 | game_spread | 0.164 | 0.115 | 0.124 | 12 | 89 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN6 | team_total | 0.076 | 0.135 | 0.121 | 15 | 88 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.328 | 0.385 | 0.373 | 39 | 62 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.270 | 0.258 | 28 | 74 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT22MINCGY-4 | game_total | 0.808 | 0.860 | 0.851 | 87 | 15 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.777 | 0.830 | 0.820 | 84 | 18 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT22MINCGY-8 | game_total | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL2 | team_total | 0.853 | 0.800 | 0.812 | 81 | 21 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT22UTASEA-5 | game_total | 0.778 | 0.825 | 0.816 | 83 | 18 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA6 | team_total | 0.100 | 0.155 | 0.142 | 17 | 86 | no | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.407 | 0.355 | 0.365 | 36 | 65 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM2 | game_spread | 0.314 | 0.265 | 0.274 | 27 | 74 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.385 | 0.374 | 39 | 62 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3 | team_total | 0.607 | 0.555 | 0.566 | 56 | 45 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.354 | 0.405 | 0.395 | 41 | 60 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.436 | 0.485 | 0.475 | 49 | 52 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK2 | team_total | 0.783 | 0.830 | 0.821 | 84 | 18 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR5 | team_total | 0.221 | 0.270 | 0.260 | 28 | 74 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL6 | team_total | 0.131 | 0.085 | 0.093 | 10 | 93 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT22UTASEA-4 | game_total | 0.860 | 0.895 | 0.889 | 90 | 11 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT22UTASEA-6 | game_total | 0.571 | 0.615 | 0.606 | 62 | 39 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4 | team_total | 0.388 | 0.340 | 0.349 | 35 | 67 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT22VGKSTL-8 | game_total | 0.285 | 0.245 | 0.253 | 25 | 76 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT22VGKSTL-9 | game_total | 0.202 | 0.165 | 0.172 | 17 | 84 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT22UTASEA-7 | game_total | 0.461 | 0.505 | 0.496 | 51 | 50 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET4 | team_total | 0.441 | 0.490 | 0.480 | 50 | 52 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT22MINCGY-9 | game_total | 0.129 | 0.165 | 0.157 | 17 | 84 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET3 | team_total | 0.654 | 0.700 | 0.691 | 71 | 31 | no | +0.021 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.593 | 0.635 | 0.627 | 64 | 37 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY3 | game_spread | 0.137 | 0.100 | 0.107 | 11 | 91 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL6 | team_total | 0.076 | 0.115 | 0.106 | 13 | 90 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA2 | team_total | 0.809 | 0.775 | 0.782 | 78 | 23 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT22VGKSTL-6 | game_total | 0.594 | 0.555 | 0.563 | 56 | 45 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA5 | team_total | 0.207 | 0.170 | 0.177 | 18 | 84 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN3 | team_total | 0.583 | 0.545 | 0.553 | 55 | 46 | yes | +0.016 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ STL | 0.574 | 0.506 | 0.172 | 0.218 | 6.39 | 6.28 | 0.977/1.004 | KXNHLSPREAD-26OCT22VGKSTL-STL2 -0.071 |
| WPG @ DAL | 0.593 | 0.580 | 0.187 | 0.216 | 5.47 | 6.01 | 0.994/1.003 | KXNHLTOTAL-26OCT22WPGDAL-7 +0.092 |
| MIN @ CGY | 0.463 | 0.452 | 0.188 | 0.219 | 5.73 | 6.07 | 0.978/0.991 | KXNHLTOTAL-26OCT22MINCGY-7 +0.067 |
| CAR @ EDM | 0.532 | 0.565 | 0.176 | 0.210 | 6.55 | 6.74 | 0.994/0.987 | KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 +0.046 |
| UTA @ SEA | 0.491 | 0.498 | 0.174 | 0.215 | 6.27 | 6.52 | 1.015/0.992 | KXNHLTOTAL-26OCT22UTASEA-7 +0.043 |
| DET @ VAN | 0.450 | 0.531 | 0.176 | 0.215 | 6.37 | 6.28 | 1.021/1.003 | KXNHLGAME-26OCT22DETVAN-DET -0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 24 recommended · full analysis in card.md / packet.json `thesis_card`

- Robert Thomas: 1+ goals YES @ 22c · p 0.2728 (adj 0.2571) · $4.7 · thesis STL:OFFENSE_4PLUS
- Raphael Lavoie: 1+ goals YES @ 9c · p 0.1226 (adj 0.1082) · $1.91 · thesis VGK:OFFENSE_4PLUS
- William Karlsson: 1+ assists NO @ 73c · p 0.8061 (adj 0.7606) · $11.95 · thesis VGK:SUPPRESSED
- Ivan Barbashev: 1+ goals YES @ 21c · p 0.2441 (adj 0.2343) · $2.6 · thesis VGK:OFFENSE_4PLUS
- Dylan Samberg: 1+ goals YES @ 3c · p 0.0544 (adj 0.0483) · $2.21 · thesis WPG:OFFENSE_4PLUS
- Gabriel Vilardi: 1+ goals YES @ 22c · p 0.2655 (adj 0.2529) · $4.07 · thesis WPG:OFFENSE_4PLUS
- Alex Iafallo: 1+ goals YES @ 13c · p 0.1639 (adj 0.1542) · $2.79 · thesis WPG:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 66c · p 0.7111 (adj 0.6971) · $10.44 · thesis DAL:SUPPRESSED
- Aydar Suniev: 1+ goals YES @ 17c · p 0.2214 (adj 0.2061) · $4.36 · thesis CGY:OFFENSE_4PLUS
- Kirill Kaprizov: 2+ goals NO @ 87c · p 0.9142 (adj 0.8994) · $11.87 · thesis MIN:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 10c · p 0.1405 (adj 0.1254) · $2.77 · thesis CGY:OFFENSE_4PLUS
- Ben Jones: 1+ goals NO @ 87c · p 0.909 (adj 0.8968) · $11.87 · thesis CGY:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 12c · p 0.1854 (adj 0.1678) · $6.17 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 7c · p 0.111 (adj 0.0995) · $3.44 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 24c · p 0.2899 (adj 0.2762) · $4.26 · thesis EDM:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 79c · p 0.8562 (adj 0.8206) · $10.42 · thesis EDM:WINS
- Shane Wright: 1+ goals YES @ 15c · p 0.2053 (adj 0.1902) · $5.21 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1362 (adj 0.1259) · $3.01 · thesis SEA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 64c · p 0.6997 (adj 0.6835) · $12.35 · thesis UTA:SUPPRESSED
- Mackie Samoskevich: 1+ goals YES @ 18c · p 0.2181 (adj 0.2073) · $3.18 · thesis SEA:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2701 (adj 0.2476) · $7.62 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2593 (adj 0.2407) · $6.6 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 11c · p 0.1648 (adj 0.1474) · $4.3 · thesis VAN:OFFENSE_4PLUS
- Moritz Seider: 1+ goals NO @ 85c · p 0.8985 (adj 0.8851) · $11.91 · thesis DET:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VGK @ STL** · priced 202/215 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 27.55, exp saves 23.79 (sd 6.48), pull risk 0.061
- VGK net: Adin Hill (CONFIRMED) exp shots 25.57, exp saves 22.08 (sd 6.22), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rasmus Andersson: 1+ points | 0.402 | 0.225 | 36/91 | +0.026 | STANDARD |
| Pius Suter: 1+ points | 0.341 | 0.180 | 30/94 | +0.027 | STANDARD |
| Brayden McNabb: 1+ assists | 0.276 | 0.140 | 24/96 | +0.023 | STANDARD |
| Noah Hanifin: 1+ points | 0.308 | 0.175 | 29/94 | +0.004 | STANDARD |
| Jeremy Lauzon: 1+ assists | 0.199 | 0.075 | 14/99 | +0.051 | STANDARD |
| Justin Barron: 1+ points | 0.215 | 0.095 | 18/99 | +0.025 | STANDARD |

**WPG @ DAL** · priced 206/207 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.62, exp saves 21.58 (sd 5.98), pull risk 0.047
- WPG net: Stuart Skinner (CONFIRMED) exp shots 26.81, exp saves 22.93 (sd 6.47), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nils Lundkvist: 1+ points | 0.283 | 0.105 | 20/99 | +0.072 | STANDARD |
| Nils Lundkvist: 1+ assists | 0.244 | 0.085 | 16/99 | +0.075 | STANDARD |
| Adam Lowry: 1+ points | 0.286 | 0.140 | 27/99 | +0.002 | STANDARD |
| Dylan Samberg: 1+ assists | 0.231 | 0.100 | 19/99 | +0.030 | STANDARD |
| Jamie Benn: 1+ assists | 0.265 | 0.135 | 26/99 | -0.009 | STANDARD |
| Arttu Hyry: 1+ points | 0.285 | 0.160 | 27/95 | +0.001 | STANDARD |

**MIN @ CGY** · priced 170/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 30.26, exp saves 26.04 (sd 7.05), pull risk 0.065
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 28.91, exp saves 25.15 (sd 6.68), pull risk 0.052

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ben Jones: 1+ points | 0.217 | 0.345 | 35/66 | +0.107 | STANDARD |
| Quinn Hughes: 2+ points | 0.233 | 0.355 | 37/66 | +0.091 | STANDARD |
| Quinn Hughes: 1+ assists | 0.531 | 0.650 | 66/36 | +0.093 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.381 | 0.495 | 50/51 | +0.092 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.274 | 0.385 | 40/63 | +0.080 | STANDARD |
| Quinn Hughes: 1+ points | 0.597 | 0.700 | 72/32 | +0.068 | STANDARD |

**CAR @ EDM** · priced 172/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 29.98, exp saves 26.06 (sd 7.0), pull risk 0.064
- CAR net: Brandon Bussi (PROBABLE) exp shots 25.41, exp saves 21.63 (sd 6.33), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jordan Martinook: 1+ points | 0.343 | 0.215 | 30/87 | +0.028 | STANDARD |
| Mattias Ekholm: 1+ points | 0.422 | 0.295 | 31/72 | +0.097 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.350 | 0.225 | 25/80 | +0.087 | STANDARD |
| Brandon Bussi: 25+ saves | 0.320 | 0.445 | 45/56 | +0.103 |  |
| Sebastian Aho: 1+ assists | 0.381 | 0.505 | 51/50 | +0.101 | STANDARD |
| Sebastian Aho: 2+ points | 0.209 | 0.325 | 33/68 | +0.096 | STANDARD |

**UTA @ SEA** · priced 180/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 29.05, exp saves 25.09 (sd 6.72), pull risk 0.064
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.24), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anders Lee: 1+ points | 0.385 | 0.240 | 42/94 | -0.052 | STANDARD |
| Clayton Keller: 2+ points | 0.230 | 0.360 | 37/65 | +0.104 | STANDARD |
| Clayton Keller: 1+ points | 0.593 | 0.715 | 72/29 | +0.103 | STANDARD |
| Kailer Yamamoto: 1+ assists | 0.264 | 0.150 | 26/96 | -0.010 | STANDARD |
| Clayton Keller: 1+ assists | 0.447 | 0.555 | 57/46 | +0.076 | STANDARD |
| Logan Cooley: 1+ assists | 0.330 | 0.435 | 45/58 | +0.073 | STANDARD |

**DET @ VAN** · priced 172/203 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Liam Ohgren: 1+ points | 0.411 | 0.170 | 33/99 | +0.066 | STANDARD |
| Max Sasson: 1+ points | 0.321 | 0.110 | 21/99 | +0.099 | STANDARD |
| Ben Chiarot: 1+ assists | 0.248 | 0.095 | 18/99 | +0.057 | STANDARD |
| Liam Ohgren: 1+ assists | 0.286 | 0.135 | 26/99 | +0.012 | STANDARD |
| Paul Cotter: 1+ assists | 0.260 | 0.115 | 22/99 | +0.028 | STANDARD |
| Brendan Gallagher: 1+ points | 0.257 | 0.115 | 22/99 | +0.025 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
