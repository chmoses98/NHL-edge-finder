# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T15:51:11Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4555 · contracts joined: 2656 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2356, 'NO_EDGE': 121, 'OK': 179}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 371, 'game_early_goal': 12, 'first_goal': 431, 'game_winner': 24, 'player_goals': 750, 'game_overtime': 12, 'player_points': 489, 'goalie_saves': 3, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 2026-10-22T23:00:00Z | T-6h | 0.586 | 0.414 | 0.167 | 6.46 | 3.50 | 2.96 | 220 (25/195) | PROBABLE/PROJECTED |
| NYR @ TOR | 2026-10-22T23:00:00Z | T-6h | 0.456 | 0.544 | 0.174 | 6.46 | 3.09 | 3.37 | 228 (25/203) | CONFIRMED/PROJECTED |
| SJS @ OTT | 2026-10-22T23:00:00Z | T-6h | 0.558 | 0.442 | 0.172 | 6.45 | 3.42 | 3.04 | 226 (25/201) | PROJECTED/PROJECTED |
| ANA @ NJD | 2026-10-22T23:00:00Z | T-6h | 0.584 | 0.416 | 0.172 | 6.32 | 3.42 | 2.90 | 228 (25/203) | PROJECTED/PROJECTED |
| FLA @ PIT | 2026-10-22T23:00:00Z | T-6h | 0.545 | 0.455 | 0.169 | 6.61 | 3.44 | 3.16 | 251 (25/226) | PROJECTED/PROJECTED |
| LAK @ NYI | 2026-10-22T23:30:00Z | T-6h | 0.551 | 0.449 | 0.184 | 5.61 | 2.94 | 2.67 | 206 (25/181) | CONFIRMED/PROJECTED |
| VGK @ STL | 2026-10-23T00:00:00Z | T-6h | 0.550 | 0.450 | 0.174 | 6.36 | 3.34 | 3.02 | 225 (25/200) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-6h | 0.592 | 0.408 | 0.180 | 5.55 | 3.05 | 2.50 | 205 (25/180) | PROJECTED/PROJECTED |
| MIN @ CGY | 2026-10-23T01:00:00Z | T-6h | 0.457 | 0.543 | 0.186 | 5.85 | 2.79 | 3.06 | 220 (25/195) | PROJECTED/PROJECTED |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-6h | 0.529 | 0.471 | 0.170 | 6.54 | 3.37 | 3.17 | 218 (25/193) | PROJECTED/PROJECTED |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-6h | 0.456 | 0.544 | 0.170 | 6.51 | 3.11 | 3.40 | 225 (25/200) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-6h | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 204 (25/179) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.377 | 0.490 | 0.467 | 50 | 52 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.310 | 0.415 | 0.393 | 42 | 59 | no | +0.083 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.457 | 0.355 | 0.375 | 36 | 65 | yes | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.595 | 0.700 | 0.680 | 71 | 31 | no | +0.080 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.186 | 0.290 | 0.267 | 30 | 72 | no | +0.080 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.550 | 0.455 | 0.474 | 46 | 55 | yes | +0.073 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.450 | 0.545 | 0.526 | 55 | 46 | no | +0.073 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.543 | 0.635 | 0.617 | 64 | 37 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.228 | 0.315 | 0.296 | 32 | 69 | no | +0.067 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.214 | 0.295 | 0.277 | 30 | 71 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.462 | 0.545 | 0.528 | 55 | 46 | no | +0.061 | OK |
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.584 | 0.665 | 0.649 | 67 | 34 | no | +0.061 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.416 | 0.335 | 0.351 | 34 | 67 | yes | +0.061 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.245 | 0.325 | 0.308 | 33 | 68 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.196 | 0.280 | 0.262 | 29 | 73 | no | +0.060 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.544 | 0.625 | 0.609 | 63 | 38 | no | +0.059 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.456 | 0.375 | 0.391 | 38 | 63 | yes | +0.059 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.332 | 0.255 | 0.269 | 26 | 75 | yes | +0.058 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.682 | 0.755 | 0.741 | 76 | 25 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ2 | game_spread | 0.361 | 0.435 | 0.420 | 44 | 57 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.252 | 0.180 | 0.193 | 19 | 83 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.241 | 0.170 | 0.183 | 18 | 84 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.207 | 0.275 | 0.260 | 28 | 73 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5 | team_total | 0.266 | 0.340 | 0.324 | 35 | 67 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.655 | 0.580 | 0.596 | 59 | 43 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.286 | 0.355 | 0.341 | 36 | 65 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.377 | 0.450 | 0.435 | 46 | 56 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.144 | 0.205 | 0.191 | 21 | 80 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.329 | 0.395 | 0.381 | 40 | 61 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.807 | 0.870 | 0.859 | 88 | 14 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.389 | 0.455 | 0.442 | 46 | 55 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.509 | 0.575 | 0.562 | 58 | 43 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3 | team_total | 0.674 | 0.740 | 0.728 | 75 | 27 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.602 | 0.670 | 0.657 | 68 | 34 | no | +0.042 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.529 | 0.465 | 0.478 | 47 | 54 | yes | +0.042 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.471 | 0.535 | 0.522 | 54 | 47 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.437 | 0.365 | 0.379 | 38 | 65 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.804 | 0.860 | 0.850 | 87 | 15 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.193 | 0.260 | 0.245 | 28 | 76 | no | +0.035 | OK |
| KXNHLGAME-26OCT22LANYI-NYI | game_winner | 0.551 | 0.495 | 0.506 | 50 | 51 | yes | +0.034 | OK |
| KXNHLGAME-26OCT22LANYI-LA | game_winner | 0.449 | 0.505 | 0.494 | 51 | 50 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ6 | team_total | 0.127 | 0.180 | 0.168 | 19 | 83 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA2 | team_total | 0.745 | 0.795 | 0.786 | 80 | 21 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.128 | 0.175 | 0.165 | 18 | 83 | no | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.408 | 0.355 | 0.365 | 36 | 65 | yes | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.592 | 0.645 | 0.635 | 65 | 36 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.789 | 0.835 | 0.826 | 84 | 17 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22ANANJ-7 | game_total | 0.471 | 0.525 | 0.514 | 53 | 48 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.264 | 0.315 | 0.304 | 32 | 69 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.158 | 0.205 | 0.195 | 21 | 80 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT22LANYI-5 | game_total | 0.696 | 0.745 | 0.736 | 75 | 26 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.502 | 0.560 | 0.548 | 57 | 45 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.452 | 0.505 | 0.494 | 51 | 50 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.252 | 0.205 | 0.214 | 21 | 80 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.385 | 0.374 | 39 | 62 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL2 | team_total | 0.841 | 0.790 | 0.801 | 80 | 22 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ2 | team_total | 0.854 | 0.900 | 0.892 | 91 | 11 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA5 | team_total | 0.132 | 0.180 | 0.169 | 19 | 83 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3 | team_total | 0.606 | 0.550 | 0.561 | 56 | 46 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.208 | 0.160 | 0.169 | 17 | 85 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.355 | 0.405 | 0.395 | 41 | 60 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT22MINCGY-5 | game_total | 0.732 | 0.775 | 0.767 | 78 | 23 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN6 | team_total | 0.087 | 0.130 | 0.120 | 14 | 88 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT22LANYI-7 | game_total | 0.348 | 0.395 | 0.386 | 40 | 61 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.260 | 0.250 | 27 | 75 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR4 | team_total | 0.398 | 0.450 | 0.440 | 46 | 56 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT22ANANJ-5 | game_total | 0.785 | 0.825 | 0.818 | 83 | 18 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.339 | 0.385 | 0.376 | 39 | 62 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL6 | team_total | 0.119 | 0.080 | 0.087 | 9 | 93 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4 | team_total | 0.389 | 0.340 | 0.350 | 35 | 67 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.450 | 0.495 | 0.486 | 50 | 51 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK4 | team_total | 0.370 | 0.415 | 0.406 | 42 | 59 | no | +0.023 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.595 | 0.586 | 60 | 41 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-8 | game_total | 0.295 | 0.250 | 0.259 | 26 | 76 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM2 | game_spread | 0.316 | 0.275 | 0.283 | 28 | 73 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET4 | team_total | 0.441 | 0.490 | 0.480 | 50 | 52 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.583 | 0.625 | 0.617 | 63 | 38 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT22ANANJ-6 | game_total | 0.583 | 0.625 | 0.617 | 63 | 38 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL6 | team_total | 0.083 | 0.115 | 0.108 | 12 | 89 | no | +0.021 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 0.586 | 0.575 | 0.167 | 0.211 | 6.46 | 6.58 | 0.993/1.000 | KXNHLTOTAL-26OCT22NSHBOS-7 +0.026 |
| NYR @ TOR | 0.456 | 0.506 | 0.174 | 0.219 | 6.46 | 6.35 | 0.988/0.992 | KXNHLSPREAD-26OCT22NYRTOR-NYR2 -0.051 |
| SJS @ OTT | 0.558 | 0.567 | 0.172 | 0.214 | 6.45 | 6.29 | 1.041/1.034 | KXNHLTOTAL-26OCT22SJOTT-6 -0.027 |
| ANA @ NJD | 0.584 | 0.534 | 0.172 | 0.215 | 6.32 | 6.40 | 0.992/1.024 | KXNHLGAME-26OCT22ANANJ-NJ -0.049 |
| FLA @ PIT | 0.545 | 0.594 | 0.169 | 0.212 | 6.61 | 6.53 | 1.021/1.001 | KXNHLGAME-26OCT22FLAPIT-FLA -0.049 |
| LAK @ NYI | 0.551 | 0.531 | 0.184 | 0.224 | 5.61 | 5.94 | 0.978/0.989 | KXNHLTOTAL-26OCT22LANYI-7 +0.063 |
| VGK @ STL | 0.550 | 0.494 | 0.174 | 0.222 | 6.36 | 6.33 | 0.993/1.004 | KXNHLSPREAD-26OCT22VGKSTL-STL2 -0.056 |
| WPG @ DAL | 0.592 | 0.575 | 0.180 | 0.214 | 5.55 | 5.95 | 0.986/0.988 | KXNHLTOTAL-26OCT22WPGDAL-7 +0.072 |
| MIN @ CGY | 0.457 | 0.449 | 0.186 | 0.221 | 5.85 | 6.11 | 0.986/0.995 | KXNHLTOTAL-26OCT22MINCGY-7 +0.052 |
| CAR @ EDM | 0.529 | 0.567 | 0.170 | 0.215 | 6.54 | 6.74 | 0.994/0.989 | KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 +0.052 |
| UTA @ SEA | 0.456 | 0.499 | 0.170 | 0.215 | 6.51 | 6.50 | 1.005/0.992 | KXNHLGAME-26OCT22UTASEA-UTA -0.044 |
| DET @ VAN | 0.450 | 0.532 | 0.176 | 0.218 | 6.37 | 6.28 | 1.021/1.003 | KXNHLSPREAD-26OCT22DETVAN-DET2 -0.083 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 39 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3063 (adj 0.2922) · $2.44 · thesis NSH:OFFENSE_4PLUS
- Adam Wilsby: 1+ goals YES @ 6c · p 0.079 (adj 0.0742) · $1.03 · thesis NSH:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 15c · p 0.1938 (adj 0.1741) · $1.62 · thesis BOS:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 61c · p 0.659 (adj 0.6455) · $5.11 · thesis BOS:SUPPRESSED
- Gabe Perreault: 1+ assists YES @ 25c · p 0.3164 (adj 0.2732) · $1.23 · thesis NYR:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 56c · p 0.716 (adj 0.6081) · $7.92 · thesis OTT:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 14c · p 0.183 (adj 0.1698) · $2.42 · thesis OTT:OFFENSE_4PLUS
- Ridly Greig: 1+ goals YES @ 17c · p 0.1996 (adj 0.191) · $1.45 · thesis OTT:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 68c · p 0.7777 (adj 0.7077) · $4.87 · thesis SJS:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 13c · p 0.2102 (adj 0.1864) · $4.77 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 10c · p 0.1316 (adj 0.1225) · $1.57 · thesis ANA:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 72c · p 0.7709 (adj 0.7569) · $7.92 · thesis NJD:SUPPRESSED
- New Jersey wins by over 2.5 goals NO @ 69c · p 0.7914 (adj 0.7222) · $2.34 · thesis ANA:WINS
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.6986 (adj 0.6802) · $6.0 · thesis FLA:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 14c · p 0.192 (adj 0.1715) · $2.31 · thesis PIT:WINS_BY_2PLUS
- Sam Reinhart: 1+ goals NO @ 67c · p 0.7294 (adj 0.7133) · $5.87 · thesis FLA:SUPPRESSED
- Andrei Kuzmenko: 1+ goals YES @ 15c · p 0.1929 (adj 0.1772) · $1.9 · thesis PIT:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 64c · p 0.8273 (adj 0.6893) · $7.92 · thesis LAK:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 73c · p 0.7702 (adj 0.7589) · $5.55 · thesis VGK:SUPPRESSED
- Mark Stone: 1+ assists NO @ 55c · p 0.6244 (adj 0.5797) · $2.46 · thesis VGK:SUPPRESSED
- Gabriel Vilardi: 1+ goals YES @ 21c · p 0.2645 (adj 0.2496) · $3.26 · thesis WPG:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 71c · p 0.7756 (adj 0.7403) · $3.87 · thesis GAME:TIGHT
- Mikko Rantanen: 1+ goals NO @ 67c · p 0.7171 (adj 0.7016) · $4.81 · thesis DAL:SUPPRESSED
- Kirill Kaprizov: 1+ goals NO @ 53c · p 0.6127 (adj 0.5883) · $7.92 · thesis MIN:SUPPRESSED
- Minnesota wins by over 1.5 goals NO @ 59c · p 0.6804 (adj 0.6327) · $3.44 · thesis CGY:WINS
- Jonathan Castagna: 1+ goals YES @ 10c · p 0.1348 (adj 0.1186) · $1.1 · thesis CGY:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 17c · p 0.2061 (adj 0.1946) · $1.5 · thesis CGY:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1194 (adj 0.1046) · $1.8 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 14c · p 0.1832 (adj 0.1686) · $2.19 · thesis EDM:OFFENSE_4PLUS
- Filip Hallander: 1+ goals YES @ 9c · p 0.1276 (adj 0.1119) · $1.53 · thesis EDM:OFFENSE_4PLUS
- Zach Hyman: 1+ goals YES @ 31c · p 0.3615 (adj 0.3461) · $3.07 · thesis EDM:OFFENSE_4PLUS
- Shane Wright: 1+ goals YES @ 14c · p 0.2009 (adj 0.1844) · $3.57 · thesis SEA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 11c · p 0.1484 (adj 0.1363) · $2.27 · thesis UTA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 64c · p 0.7021 (adj 0.6841) · $7.15 · thesis UTA:SUPPRESSED
- Utah wins by over 1.5 goals NO @ 61c · p 0.7049 (adj 0.6549) · $6.6 · thesis SEA:WINS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2699 (adj 0.2474) · $5.34 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 11c · p 0.1771 (adj 0.1541) · $3.57 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 12c · p 0.1648 (adj 0.1511) · $2.41 · thesis VAN:OFFENSE_4PLUS
- Moritz Seider: 1+ goals NO @ 85c · p 0.8956 (adj 0.8804) · $7.92 · thesis DET:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ BOS** · priced 164/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Michael DiPietro (PROBABLE) exp shots 27.6, exp saves 23.97 (sd 6.6), pull risk 0.061
- NSH net: Juuse Saros (PROJECTED) exp shots 28.42, exp saves 24.26 (sd 6.75), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Michael DiPietro: 23+ saves | 0.592 | 0.375 | 53/78 | +0.044 |  |
| Charlie McAvoy: 1+ assists | 0.381 | 0.520 | 53/49 | +0.112 | STANDARD |
| Charlie McAvoy: 1+ points | 0.471 | 0.580 | 60/44 | +0.072 | STANDARD |
| Pavel Zacha: 1+ assists | 0.346 | 0.445 | 45/56 | +0.077 | STANDARD |
| David Pastrnak: 1+ assists | 0.491 | 0.580 | 59/43 | +0.061 | STANDARD |
| Ryan O'Reilly: 2+ points | 0.235 | 0.150 | 22/92 | +0.003 | STANDARD |

**NYR @ TOR** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 27.8, exp saves 24.1 (sd 6.59), pull risk 0.064
- NYR net: Dylan Garand (PROJECTED) exp shots 26.92, exp saves 23.14 (sd 6.54), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gabe Perreault: 1+ assists | 0.316 | 0.230 | 25/79 | +0.053 | STANDARD |
| Gavin McKenna: 1+ points | 0.385 | 0.465 | 47/54 | +0.058 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.468 | 0.545 | 57/48 | +0.035 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.241 | 0.315 | 33/70 | +0.045 | STANDARD |
| Auston Matthews: 2+ points | 0.262 | 0.195 | 32/93 | -0.073 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.336 | 0.400 | 42/62 | +0.028 | STANDARD |

**SJS @ OTT** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 24.89, exp saves 21.66 (sd 6.14), pull risk 0.057
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.6, exp saves 24.36 (sd 6.71), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.284 | 0.450 | 46/56 | +0.139 | STANDARD |
| Jake Sanderson: 1+ points | 0.376 | 0.530 | 54/48 | +0.126 | STANDARD |
| Ivar Stenberg: 1+ points | 0.357 | 0.470 | 48/54 | +0.086 | STANDARD |
| Tim Stutzle: 1+ assists | 0.417 | 0.530 | 55/49 | +0.075 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.222 | 0.330 | 34/68 | +0.082 | STANDARD |
| Ridly Greig: 1+ points | 0.418 | 0.320 | 34/70 | +0.062 | STANDARD |

**ANA @ NJD** · priced 176/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROJECTED) exp shots 27.82, exp saves 24.19 (sd 6.63), pull risk 0.061
- ANA net: Lukas Dostal (PROJECTED) exp shots 29.59, exp saves 25.35 (sd 7.01), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.198 | 0.390 | 41/63 | +0.155 | STANDARD |
| Luke Evangelista: 1+ points | 0.377 | 0.530 | 55/49 | +0.116 | STANDARD |
| Jack Hughes: 1+ assists | 0.411 | 0.540 | 55/47 | +0.101 | STANDARD |
| Jack Hughes: 2+ points | 0.233 | 0.355 | 37/66 | +0.091 | STANDARD |
| Jesper Bratt: 1+ assists | 0.392 | 0.500 | 51/51 | +0.080 | STANDARD |
| Luke Hughes: 1+ points | 0.455 | 0.560 | 57/45 | +0.078 | STANDARD |

**FLA @ PIT** · priced 192/200 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (PROJECTED) exp shots 26.42, exp saves 23.08 (sd 6.34), pull risk 0.055
- FLA net: Cooper Black (PROJECTED) exp shots 27.3, exp saves 23.16 (sd 6.6), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Robertson: 1+ assists | 0.238 | 0.090 | 17/99 | +0.058 | STANDARD |
| Blake Lizotte: 1+ assists | 0.252 | 0.110 | 21/99 | +0.030 | STANDARD |
| Ville Koivunen: 1+ points | 0.338 | 0.470 | 48/54 | +0.104 | STANDARD |
| Rickard Rakell: 2+ points | 0.246 | 0.130 | 22/96 | +0.014 | STANDARD |
| Ville Koivunen: 1+ assists | 0.221 | 0.335 | 35/68 | +0.084 | STANDARD |
| Sam Reinhart: 1+ assists | 0.291 | 0.405 | 41/60 | +0.092 | STANDARD |

**LAK @ NYI** · priced 152/155 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 26.76, exp saves 23.29 (sd 6.31), pull risk 0.049
- LAK net: Anton Forsberg (PROJECTED) exp shots 27.67, exp saves 23.97 (sd 6.55), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.173 | 0.385 | 41/64 | +0.171 | STANDARD |
| Mats Zuccarello: 1+ points | 0.344 | 0.505 | 52/51 | +0.128 | STANDARD |
| Trevor Moore: 1+ assists | 0.279 | 0.200 | 23/83 | +0.037 | STANDARD |
| Trevor Moore: 1+ points | 0.438 | 0.370 | 39/65 | +0.031 | STANDARD |
| Artemi Panarin: 1+ assists | 0.383 | 0.450 | 47/57 | +0.030 | STANDARD |
| Mats Zuccarello: 2+ points | 0.065 | 0.130 | 19/93 | +0.000 | STANDARD |

**VGK @ STL** · priced 171/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 27.55, exp saves 23.79 (sd 6.58), pull risk 0.063
- VGK net: Adin Hill (PROJECTED) exp shots 25.57, exp saves 22.09 (sd 6.21), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.436 | 0.555 | 57/46 | +0.086 | STANDARD |
| Mitch Marner: 1+ assists | 0.410 | 0.515 | 53/50 | +0.072 | STANDARD |
| Jack Eichel: 2+ points | 0.232 | 0.335 | 36/69 | +0.063 | STANDARD |
| Mitch Marner: 1+ points | 0.544 | 0.640 | 65/37 | +0.070 | STANDARD |
| Mark Stone: 1+ assists | 0.376 | 0.465 | 48/55 | +0.057 | STANDARD |
| Trevor Connelly: 1+ points | 0.367 | 0.450 | 46/56 | +0.056 | STANDARD |

**WPG @ DAL** · priced 153/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.62, exp saves 21.55 (sd 5.96), pull risk 0.046
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.81, exp saves 22.93 (sd 6.41), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Miro Heiskanen: 1+ points | 0.488 | 0.580 | 60/44 | +0.055 | STANDARD |
| Mikko Rantanen: 2+ points | 0.241 | 0.330 | 35/69 | +0.054 | STANDARD |
| Cole Perfetti: 1+ points | 0.527 | 0.445 | 47/58 | +0.040 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.452 | 0.530 | 54/48 | +0.050 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.345 | 0.420 | 44/60 | +0.038 | STANDARD |
| Cole Perfetti: 2+ points | 0.174 | 0.100 | 15/95 | +0.015 | STANDARD |

**MIN @ CGY** · priced 168/169 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 30.26, exp saves 26.04 (sd 7.01), pull risk 0.067
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.91, exp saves 25.13 (sd 6.71), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Quinn Hughes: 2+ points | 0.242 | 0.355 | 37/66 | +0.082 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.387 | 0.485 | 50/53 | +0.065 | STANDARD |
| Quinn Hughes: 1+ assists | 0.551 | 0.635 | 66/39 | +0.043 | STANDARD |
| Quinn Hughes: 1+ points | 0.613 | 0.695 | 71/32 | +0.051 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.284 | 0.360 | 38/66 | +0.040 | STANDARD |
| Max Shabanov: 1+ points | 0.375 | 0.450 | 48/58 | +0.028 | STANDARD |

**CAR @ EDM** · priced 156/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 29.98, exp saves 26.08 (sd 6.92), pull risk 0.06
- CAR net: Brandon Bussi (PROJECTED) exp shots 25.41, exp saves 21.63 (sd 6.28), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mattias Ekholm: 1+ points | 0.440 | 0.305 | 32/71 | +0.105 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.366 | 0.240 | 26/78 | +0.092 | STANDARD |
| Sebastian Aho: 1+ assists | 0.384 | 0.505 | 51/50 | +0.099 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.471 | 0.585 | 59/42 | +0.092 | STANDARD |
| Evan Bouchard: 2+ points | 0.309 | 0.210 | 30/88 | -0.006 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.411 | 0.320 | 34/70 | +0.055 | STANDARD |

**UTA @ SEA** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 29.05, exp saves 25.15 (sd 6.79), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.27), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Clayton Keller: 1+ points | 0.590 | 0.720 | 73/29 | +0.106 | STANDARD |
| Clayton Keller: 2+ points | 0.224 | 0.350 | 37/67 | +0.091 | STANDARD |
| Clayton Keller: 1+ assists | 0.443 | 0.560 | 58/46 | +0.080 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.209 | 0.320 | 34/70 | +0.077 | STANDARD |
| Vincent Trocheck: 1+ points | 0.354 | 0.465 | 48/55 | +0.078 | STANDARD |
| Matty Beniers: 1+ goals | 0.228 | 0.130 | 21/95 | +0.006 | STANDARD |

**DET @ VAN** · priced 130/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake DeBrusk: 1+ goals | 0.325 | 0.170 | 28/94 | +0.031 | STANDARD |
| Alex DeBrincat: 2+ points | 0.293 | 0.180 | 33/97 | -0.053 | STANDARD |
| Dylan Larkin: 1+ points | 0.531 | 0.635 | 66/39 | +0.063 | STANDARD |
| Linus Karlsson: 1+ goals | 0.259 | 0.160 | 20/88 | +0.048 | STANDARD |
| Dylan Larkin: 1+ assists | 0.348 | 0.445 | 46/57 | +0.065 | STANDARD |
| Drew O'Connor: 1+ goals | 0.210 | 0.115 | 16/93 | +0.041 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
