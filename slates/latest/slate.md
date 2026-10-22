# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T23:17:58Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 7 · markets on board: 4912 · contracts joined: 1689 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 1514, 'OK': 136, 'NO_EDGE': 39}
families: {'period_winner': 63, 'period_spread': 42, 'period_total': 63, 'player_assists': 269, 'game_early_goal': 7, 'first_goal': 256, 'game_winner': 14, 'player_goals': 440, 'game_overtime': 7, 'player_points': 357, 'goalie_saves': 10, 'game_spread': 28, 'team_total': 70, 'game_total': 63}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NYI | 2026-10-22T23:30:00Z | T-10m | 0.579 | 0.421 | 0.181 | 5.82 | 3.15 | 2.67 | 208 (25/183) | CONFIRMED/CONFIRMED |
| VGK @ STL | 2026-10-23T00:00:00Z | T-30m | 0.570 | 0.430 | 0.171 | 6.34 | 3.39 | 2.95 | 266 (25/241) | CONFIRMED/PROBABLE |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-30m | 0.593 | 0.407 | 0.187 | 5.47 | 3.01 | 2.45 | 258 (25/233) | CONFIRMED/CONFIRMED |
| MIN @ CGY | 2026-10-23T01:00:00Z | T-90m | 0.463 | 0.537 | 0.188 | 5.73 | 2.75 | 2.98 | 235 (25/210) | CONFIRMED/CONFIRMED |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-90m | 0.532 | 0.468 | 0.176 | 6.55 | 3.37 | 3.17 | 236 (25/211) | CONFIRMED/PROBABLE |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-90m | 0.491 | 0.509 | 0.174 | 6.27 | 3.10 | 3.17 | 232 (25/207) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-90m | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 254 (25/229) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.358 | 0.505 | 0.475 | 51 | 50 | no | +0.124 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.578 | 0.715 | 0.690 | 72 | 29 | no | +0.117 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.179 | 0.305 | 0.276 | 31 | 70 | no | +0.106 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.537 | 0.655 | 0.632 | 66 | 35 | no | +0.097 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.463 | 0.345 | 0.368 | 35 | 66 | yes | +0.097 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.396 | 0.520 | 0.495 | 53 | 49 | no | +0.096 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.308 | 0.425 | 0.400 | 43 | 58 | no | +0.095 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.491 | 0.375 | 0.398 | 38 | 63 | yes | +0.095 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.509 | 0.625 | 0.602 | 63 | 38 | no | +0.095 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.182 | 0.300 | 0.273 | 31 | 71 | no | +0.094 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.430 | 0.545 | 0.522 | 55 | 46 | no | +0.093 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.570 | 0.455 | 0.478 | 46 | 55 | yes | +0.093 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.292 | 0.395 | 0.373 | 40 | 61 | no | +0.081 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.178 | 0.275 | 0.253 | 28 | 73 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA3 | team_total | 0.619 | 0.715 | 0.697 | 72 | 29 | no | +0.077 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.349 | 0.255 | 0.272 | 26 | 75 | yes | +0.075 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.231 | 0.325 | 0.305 | 33 | 68 | no | +0.074 | OK |
| KXNHLGAME-26OCT22LANYI-LA | game_winner | 0.421 | 0.515 | 0.496 | 52 | 49 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.666 | 0.575 | 0.594 | 58 | 43 | yes | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA5 | team_total | 0.217 | 0.310 | 0.290 | 32 | 70 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.795 | 0.875 | 0.862 | 88 | 13 | no | +0.067 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.367 | 0.455 | 0.437 | 46 | 55 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.452 | 0.365 | 0.382 | 37 | 64 | yes | +0.065 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.133 | 0.215 | 0.196 | 22 | 79 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.480 | 0.565 | 0.548 | 57 | 44 | no | +0.062 | OK |
| KXNHLGAME-26OCT22LANYI-NYI | game_winner | 0.579 | 0.495 | 0.512 | 50 | 51 | yes | +0.061 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.259 | 0.180 | 0.194 | 19 | 83 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.278 | 0.205 | 0.218 | 21 | 80 | yes | +0.056 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.671 | 0.745 | 0.731 | 75 | 26 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.367 | 0.445 | 0.429 | 45 | 56 | no | +0.056 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.468 | 0.545 | 0.530 | 55 | 46 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.245 | 0.175 | 0.188 | 18 | 83 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.222 | 0.155 | 0.167 | 16 | 85 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.592 | 0.665 | 0.651 | 67 | 34 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-NYI3 | team_total | 0.619 | 0.545 | 0.560 | 55 | 46 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA2 | game_spread | 0.214 | 0.285 | 0.270 | 29 | 72 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT22LANYI-NYI2 | game_spread | 0.344 | 0.270 | 0.284 | 28 | 74 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.504 | 0.575 | 0.561 | 58 | 43 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.567 | 0.635 | 0.622 | 64 | 37 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN6 | team_total | 0.076 | 0.135 | 0.121 | 14 | 87 | no | +0.046 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.532 | 0.465 | 0.478 | 47 | 54 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.115 | 0.175 | 0.161 | 18 | 83 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT22MINCGY-5 | game_total | 0.713 | 0.775 | 0.763 | 78 | 23 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.156 | 0.215 | 0.202 | 22 | 79 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA2 | team_total | 0.821 | 0.875 | 0.865 | 88 | 13 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA6 | team_total | 0.100 | 0.155 | 0.142 | 16 | 85 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR4 | team_total | 0.402 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-NYI4 | team_total | 0.397 | 0.335 | 0.347 | 34 | 67 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.188 | 0.255 | 0.240 | 27 | 76 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR3 | team_total | 0.616 | 0.675 | 0.664 | 68 | 33 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.803 | 0.855 | 0.846 | 86 | 15 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK2 | team_total | 0.783 | 0.840 | 0.830 | 85 | 17 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA3 | game_spread | 0.164 | 0.115 | 0.124 | 12 | 89 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.328 | 0.385 | 0.373 | 39 | 62 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA2 | team_total | 0.745 | 0.795 | 0.786 | 80 | 21 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.262 | 0.315 | 0.304 | 32 | 69 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT22MINCGY-4 | game_total | 0.808 | 0.855 | 0.846 | 86 | 15 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.610 | 0.598 | 62 | 40 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.777 | 0.825 | 0.816 | 83 | 18 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT22MINCGY-8 | game_total | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22UTASEA-5 | game_total | 0.778 | 0.825 | 0.816 | 83 | 18 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.293 | 0.350 | 0.338 | 36 | 66 | no | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.407 | 0.355 | 0.365 | 36 | 65 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM2 | game_spread | 0.314 | 0.265 | 0.274 | 27 | 74 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.385 | 0.374 | 39 | 62 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3 | team_total | 0.607 | 0.555 | 0.566 | 56 | 45 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK4 | team_total | 0.354 | 0.405 | 0.395 | 41 | 60 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.354 | 0.405 | 0.395 | 41 | 60 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-NYI2 | team_total | 0.820 | 0.775 | 0.785 | 78 | 23 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL6 | team_total | 0.076 | 0.115 | 0.106 | 12 | 89 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.436 | 0.485 | 0.475 | 49 | 52 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK5 | team_total | 0.182 | 0.225 | 0.216 | 23 | 78 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL2 | team_total | 0.847 | 0.800 | 0.810 | 81 | 21 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR5 | team_total | 0.221 | 0.270 | 0.260 | 28 | 74 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-8 | game_total | 0.163 | 0.205 | 0.196 | 21 | 80 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA5 | team_total | 0.136 | 0.175 | 0.167 | 18 | 83 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT22UTASEA-4 | game_total | 0.860 | 0.895 | 0.889 | 90 | 11 | no | +0.023 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NYI | 0.579 | 0.535 | 0.181 | 0.223 | 5.82 | 5.95 | 0.978/0.995 | KXNHLTEAMTOTAL-26OCT22LANYI-LA3 +0.055 |
| VGK @ STL | 0.570 | 0.504 | 0.171 | 0.219 | 6.34 | 6.28 | 0.977/1.004 | KXNHLSPREAD-26OCT22VGKSTL-STL2 -0.066 |
| WPG @ DAL | 0.593 | 0.580 | 0.187 | 0.216 | 5.47 | 6.01 | 0.994/1.003 | KXNHLTOTAL-26OCT22WPGDAL-7 +0.092 |
| MIN @ CGY | 0.463 | 0.452 | 0.188 | 0.219 | 5.73 | 6.07 | 0.978/0.991 | KXNHLTOTAL-26OCT22MINCGY-7 +0.067 |
| CAR @ EDM | 0.532 | 0.565 | 0.176 | 0.210 | 6.55 | 6.74 | 0.994/0.987 | KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 +0.046 |
| UTA @ SEA | 0.491 | 0.498 | 0.174 | 0.215 | 6.27 | 6.52 | 1.015/0.992 | KXNHLTOTAL-26OCT22UTASEA-7 +0.043 |
| DET @ VAN | 0.450 | 0.531 | 0.176 | 0.215 | 6.37 | 6.28 | 1.021/1.003 | KXNHLGAME-26OCT22DETVAN-DET -0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 27 recommended · full analysis in card.md / packet.json `thesis_card`

- Brayden Schenn: 2+ goals YES @ 2c · p 0.0381 (adj 0.0361) · $1.99 · thesis NYI:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 4c · p 0.0603 (adj 0.0552) · $1.72 · thesis LAK:OFFENSE_4PLUS
- Scott Laughton: 1+ goals YES @ 12c · p 0.1497 (adj 0.1398) · $1.96 · thesis LAK:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 22c · p 0.2698 (adj 0.2549) · $4.21 · thesis STL:OFFENSE_4PLUS
- Trevor Connelly: 1+ goals NO @ 78c · p 0.8186 (adj 0.8077) · $10.39 · thesis VGK:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 73c · p 0.7692 (adj 0.7581) · $7.54 · thesis VGK:SUPPRESSED
- Jimmy Snuggerud: 1+ goals YES @ 28c · p 0.3162 (adj 0.3059) · $2.35 · thesis STL:OFFENSE_4PLUS
- Miro Heiskanen: 1+ goals NO @ 86c · p 0.8976 (adj 0.8857) · $11.95 · thesis DAL:SUPPRESSED
- Gabriel Vilardi: 1+ goals YES @ 22c · p 0.2655 (adj 0.2529) · $3.89 · thesis WPG:OFFENSE_4PLUS
- Alex Iafallo: 1+ goals YES @ 13c · p 0.1639 (adj 0.1542) · $2.66 · thesis WPG:OFFENSE_4PLUS
- Wyatt Johnston: 1+ goals NO @ 63c · p 0.6673 (adj 0.6567) · $4.67 · thesis DAL:SUPPRESSED
- Aydar Suniev: 1+ goals YES @ 17c · p 0.2214 (adj 0.2061) · $4.47 · thesis CGY:OFFENSE_4PLUS
- Kirill Kaprizov: 2+ goals NO @ 87c · p 0.9142 (adj 0.8994) · $9.88 · thesis MIN:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 10c · p 0.1405 (adj 0.1254) · $2.82 · thesis CGY:OFFENSE_4PLUS
- Matt Boldy: 1+ goals NO @ 59c · p 0.6503 (adj 0.634) · $8.05 · thesis MIN:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 12c · p 0.1854 (adj 0.1678) · $6.18 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 7c · p 0.111 (adj 0.0995) · $3.58 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 24c · p 0.2899 (adj 0.2762) · $5.29 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 36c · p 0.4248 (adj 0.3899) · $5.81 · thesis EDM:SUPPRESSED
- Shane Wright: 1+ goals YES @ 15c · p 0.2053 (adj 0.1902) · $5.05 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1362 (adj 0.1259) · $2.91 · thesis SEA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 64c · p 0.6997 (adj 0.6835) · $11.95 · thesis UTA:SUPPRESSED
- Mackie Samoskevich: 1+ goals YES @ 18c · p 0.2181 (adj 0.2073) · $3.08 · thesis SEA:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2701 (adj 0.2476) · $7.37 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2593 (adj 0.2407) · $6.38 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 11c · p 0.1648 (adj 0.1474) · $4.18 · thesis VAN:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 67c · p 0.7198 (adj 0.7048) · $8.89 · thesis DET:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**LAK @ NYI** · priced 154/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 26.76, exp saves 23.3 (sd 6.37), pull risk 0.05
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 27.67, exp saves 23.94 (sd 6.49), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Trevor Moore: 1+ assists | 0.276 | 0.150 | 20/90 | +0.065 | STANDARD |
| Artemi Panarin: 1+ assists | 0.385 | 0.450 | 46/56 | +0.038 | STANDARD |
| Trevor Moore: 1+ points | 0.419 | 0.360 | 37/65 | +0.033 | STANDARD |
| Jean-Gabriel Pageau: 1+ points | 0.375 | 0.320 | 33/69 | +0.030 | STANDARD |
| Brayden Schenn: 1+ points | 0.479 | 0.425 | 45/60 | +0.011 | STANDARD |
| Artemi Panarin: 2+ assists | 0.083 | 0.130 | 14/88 | +0.030 | STANDARD |

**VGK @ STL** · priced 210/215 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 27.55, exp saves 23.81 (sd 6.62), pull risk 0.059
- VGK net: Adin Hill (PROBABLE) exp shots 25.57, exp saves 22.1 (sd 6.17), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brayden McNabb: 1+ assists | 0.258 | 0.125 | 24/99 | +0.005 | STANDARD |
| Mitch Marner: 1+ assists | 0.401 | 0.530 | 54/48 | +0.101 | STANDARD |
| Pius Suter: 1+ points | 0.339 | 0.215 | 29/86 | +0.035 | STANDARD |
| Jeremy Lauzon: 1+ points | 0.224 | 0.100 | 19/99 | +0.023 | STANDARD |
| Justin Barron: 1+ points | 0.218 | 0.095 | 18/99 | +0.027 | STANDARD |
| Jack Eichel: 1+ assists | 0.428 | 0.550 | 57/47 | +0.084 | STANDARD |

**WPG @ DAL** · priced 206/207 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.62, exp saves 21.58 (sd 5.98), pull risk 0.047
- WPG net: Stuart Skinner (CONFIRMED) exp shots 26.81, exp saves 22.93 (sd 6.47), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nils Lundkvist: 1+ points | 0.283 | 0.105 | 20/99 | +0.072 | STANDARD |
| Nils Lundkvist: 1+ assists | 0.244 | 0.095 | 18/99 | +0.054 | STANDARD |
| Adam Lowry: 1+ points | 0.286 | 0.140 | 27/99 | +0.002 | STANDARD |
| Dylan Samberg: 1+ assists | 0.231 | 0.100 | 19/99 | +0.030 | STANDARD |
| Arttu Hyry: 1+ points | 0.285 | 0.155 | 28/97 | -0.009 | STANDARD |
| Jamie Benn: 1+ assists | 0.265 | 0.135 | 26/99 | -0.009 | STANDARD |

**MIN @ CGY** · priced 170/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 30.26, exp saves 26.04 (sd 7.05), pull risk 0.065
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 28.91, exp saves 25.15 (sd 6.68), pull risk 0.052

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ben Jones: 1+ points | 0.217 | 0.340 | 35/67 | +0.097 | STANDARD |
| Quinn Hughes: 2+ points | 0.233 | 0.355 | 37/66 | +0.091 | STANDARD |
| Quinn Hughes: 1+ assists | 0.531 | 0.650 | 66/36 | +0.093 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.381 | 0.495 | 50/51 | +0.092 | STANDARD |
| Quinn Hughes: 1+ points | 0.597 | 0.710 | 72/30 | +0.088 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.274 | 0.385 | 40/63 | +0.080 | STANDARD |

**CAR @ EDM** · priced 172/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 29.98, exp saves 26.06 (sd 7.0), pull risk 0.064
- CAR net: Brandon Bussi (PROBABLE) exp shots 25.41, exp saves 21.63 (sd 6.33), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mattias Ekholm: 1+ assists | 0.350 | 0.205 | 25/84 | +0.087 | STANDARD |
| Sebastian Aho: 1+ assists | 0.381 | 0.510 | 52/50 | +0.101 | STANDARD |
| Mattias Ekholm: 1+ points | 0.422 | 0.295 | 31/72 | +0.097 | STANDARD |
| Brandon Bussi: 25+ saves | 0.320 | 0.445 | 45/56 | +0.103 |  |
| Sebastian Aho: 2+ points | 0.209 | 0.325 | 33/68 | +0.096 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.461 | 0.575 | 58/43 | +0.092 | STANDARD |

**UTA @ SEA** · priced 180/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 29.05, exp saves 25.09 (sd 6.72), pull risk 0.064
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.24), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anders Lee: 1+ points | 0.385 | 0.240 | 42/94 | -0.052 | STANDARD |
| Clayton Keller: 2+ points | 0.230 | 0.360 | 37/65 | +0.104 | STANDARD |
| Kailer Yamamoto: 1+ assists | 0.264 | 0.140 | 27/99 | -0.020 | STANDARD |
| Clayton Keller: 1+ assists | 0.447 | 0.565 | 57/44 | +0.096 | STANDARD |
| Clayton Keller: 1+ points | 0.593 | 0.705 | 71/30 | +0.093 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.211 | 0.315 | 33/70 | +0.075 | STANDARD |

**DET @ VAN** · priced 172/203 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Liam Ohgren: 1+ points | 0.411 | 0.170 | 33/99 | +0.066 | STANDARD |
| Max Sasson: 1+ points | 0.321 | 0.110 | 21/99 | +0.099 | STANDARD |
| Tom Willander: 1+ assists | 0.283 | 0.130 | 25/99 | +0.020 | STANDARD |
| Ben Chiarot: 1+ assists | 0.248 | 0.095 | 18/99 | +0.057 | STANDARD |
| Liam Ohgren: 1+ assists | 0.286 | 0.135 | 26/99 | +0.012 | STANDARD |
| Paul Cotter: 1+ assists | 0.260 | 0.115 | 22/99 | +0.028 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
