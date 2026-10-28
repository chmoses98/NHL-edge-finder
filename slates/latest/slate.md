# NHL slate 2026-10-27 — RESEARCH_ONLY

generated 2026-10-28T00:10:11Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 4 · markets on board: 4646 · contracts joined: 1002 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 902, 'NO_EDGE': 55, 'OK': 45}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 162, 'game_early_goal': 4, 'first_goal': 148, 'game_winner': 8, 'player_goals': 260, 'game_overtime': 4, 'player_points': 221, 'goalie_saves': 7, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ UTA | 2026-10-28T01:00:00Z | T-30m | 0.535 | 0.465 | 0.173 | 6.21 | 3.21 | 3.00 | 238 (25/213) | CONFIRMED/CONFIRMED |
| OTT @ VGK | 2026-10-28T02:00:00Z | T-90m | 0.572 | 0.428 | 0.163 | 6.68 | 3.57 | 3.11 | 242 (25/217) | CONFIRMED/CONFIRMED |
| VAN @ ANA | 2026-10-28T02:00:00Z | T-90m | 0.632 | 0.368 | 0.159 | 6.81 | 3.85 | 2.96 | 250 (25/225) | CONFIRMED/PROJECTED |
| BUF @ SJS | 2026-10-28T02:30:00Z | T-90m | 0.463 | 0.537 | 0.171 | 6.74 | 3.25 | 3.50 | 272 (25/247) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT27OTTVGK-7 | game_total | 0.524 | 0.475 | 0.485 | 48 | 53 | yes | +0.026 | OK |
| KXNHLGAME-26OCT27BUFSJ-SJ | game_winner | 0.463 | 0.415 | 0.425 | 42 | 59 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF3 | game_spread | 0.203 | 0.245 | 0.236 | 25 | 76 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-9 | game_total | 0.243 | 0.200 | 0.208 | 21 | 81 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF2 | game_spread | 0.322 | 0.365 | 0.356 | 37 | 64 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT5 | team_total | 0.212 | 0.175 | 0.182 | 18 | 83 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT27VANANA-ANA3 | game_spread | 0.285 | 0.325 | 0.317 | 33 | 68 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-6 | game_total | 0.635 | 0.595 | 0.603 | 60 | 41 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT27MINUTA-5 | game_total | 0.771 | 0.810 | 0.803 | 82 | 20 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT27MINUTA-6 | game_total | 0.556 | 0.600 | 0.591 | 61 | 41 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT3 | team_total | 0.603 | 0.560 | 0.569 | 57 | 45 | yes | +0.016 | OK |
| KXNHLGAME-26OCT27BUFSJ-BUF | game_winner | 0.537 | 0.575 | 0.567 | 58 | 43 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT27MINUTA-7 | game_total | 0.447 | 0.485 | 0.477 | 49 | 52 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-8 | game_total | 0.329 | 0.295 | 0.302 | 30 | 71 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF3 | team_total | 0.682 | 0.715 | 0.709 | 72 | 29 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT6 | team_total | 0.098 | 0.070 | 0.075 | 8 | 94 | yes | +0.013 | OK |
| KXNHLGAME-26OCT27VANANA-ANA | game_winner | 0.632 | 0.665 | 0.659 | 67 | 34 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT27MINUTA-MIN3 | game_spread | 0.149 | 0.175 | 0.170 | 18 | 83 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT27VANANA-VAN6 | team_total | 0.085 | 0.060 | 0.064 | 7 | 95 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4 | team_total | 0.472 | 0.510 | 0.502 | 52 | 50 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-SJ2 | game_spread | 0.262 | 0.235 | 0.240 | 24 | 77 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT27VANANA-10 | game_total | 0.135 | 0.115 | 0.119 | 12 | 89 | yes | +0.008 | OK |
| KXNHLSPREAD-26OCT27VANANA-ANA2 | game_spread | 0.425 | 0.455 | 0.449 | 46 | 55 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT27MINUTA-MIN2 | game_spread | 0.259 | 0.285 | 0.280 | 29 | 72 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-10 | game_total | 0.124 | 0.100 | 0.104 | 11 | 91 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ3 | team_total | 0.633 | 0.605 | 0.611 | 61 | 40 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT27VANANA-VAN5 | team_total | 0.186 | 0.155 | 0.161 | 17 | 86 | yes | +0.006 | OK |
| KXNHLSPREAD-26OCT27OTTVGK-VGK3 | game_spread | 0.231 | 0.255 | 0.250 | 26 | 75 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT27MINUTA-4 | game_total | 0.856 | 0.880 | 0.876 | 89 | 13 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT27MINUTA-UTA2 | team_total | 0.825 | 0.845 | 0.841 | 85 | 16 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT27VANANA-9 | game_total | 0.258 | 0.235 | 0.240 | 24 | 77 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ6 | team_total | 0.112 | 0.095 | 0.098 | 10 | 91 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT27VANANA-VAN4 | team_total | 0.350 | 0.320 | 0.326 | 33 | 69 | yes | +0.005 | OK |
| KXNHLSPREAD-26OCT27OTTVGK-OTT2 | game_spread | 0.236 | 0.215 | 0.219 | 22 | 79 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ4 | team_total | 0.420 | 0.395 | 0.400 | 40 | 61 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT27VANANA-ANA4 | team_total | 0.550 | 0.580 | 0.574 | 59 | 43 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT27VANANA-4 | game_total | 0.902 | 0.920 | 0.917 | 93 | 9 | no | +0.002 | OK |
| KXNHLGAME-26OCT27VANANA-VAN | game_winner | 0.368 | 0.345 | 0.349 | 35 | 66 | yes | +0.002 | OK |
| KXNHLSPREAD-26OCT27VANANA-VAN3 | game_spread | 0.108 | 0.095 | 0.097 | 10 | 91 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT27VANANA-VAN2 | team_total | 0.784 | 0.765 | 0.769 | 77 | 24 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT27VANANA-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLGAME-26OCT27OTTVGK-OTT | game_winner | 0.428 | 0.405 | 0.410 | 41 | 60 | yes | +0.001 | OK |
| KXNHLGAME-26OCT27OTTVGK-VGK | game_winner | 0.572 | 0.595 | 0.590 | 60 | 41 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT27MINUTA-MIN3 | team_total | 0.582 | 0.605 | 0.600 | 61 | 40 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT27BUFSJ-5 | game_total | 0.830 | 0.850 | 0.846 | 86 | 16 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT27BUFSJ-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT27OTTVGK-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27VANANA-ANA2 | team_total | 0.895 | 0.915 | 0.911 | 93 | 10 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT4 | team_total | 0.384 | 0.365 | 0.369 | 37 | 64 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT27MINUTA-MIN | game_winner | 0.465 | 0.485 | 0.481 | 49 | 52 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT27MINUTA-UTA | game_winner | 0.535 | 0.515 | 0.519 | 52 | 49 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-4 | game_total | 0.897 | 0.910 | 0.907 | 92 | 10 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT27MINUTA-9 | game_total | 0.182 | 0.195 | 0.192 | 20 | 81 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT27VANANA-VAN2 | game_spread | 0.187 | 0.170 | 0.173 | 18 | 84 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT27VANANA-3 | game_total | 0.978 | 0.975 | 0.976 | 98 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF5 | team_total | 0.279 | 0.305 | 0.300 | 32 | 71 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT27OTTVGK-VGK2 | game_spread | 0.358 | 0.375 | 0.372 | 38 | 63 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-3 | game_total | 0.977 | 0.975 | 0.975 | 98 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT27OTTVGK-5 | game_total | 0.824 | 0.835 | 0.833 | 84 | 17 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-7 | game_total | 0.537 | 0.555 | 0.551 | 56 | 45 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27MINUTA-MIN2 | team_total | 0.794 | 0.815 | 0.811 | 83 | 20 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT27VANANA-5 | game_total | 0.835 | 0.850 | 0.847 | 86 | 16 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27VANANA-VAN3 | team_total | 0.562 | 0.540 | 0.544 | 55 | 47 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT27MINUTA-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT27VANANA-8 | game_total | 0.350 | 0.330 | 0.334 | 34 | 68 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27VANANA-ANA5 | team_total | 0.350 | 0.365 | 0.362 | 37 | 64 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT27MINUTA-8 | game_total | 0.263 | 0.280 | 0.277 | 29 | 73 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT27MINUTA-3 | game_total | 0.965 | 0.970 | 0.969 | 98 | 4 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT27OTTVGK-3 | game_total | 0.974 | 0.970 | 0.971 | 98 | 4 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ5 | team_total | 0.234 | 0.220 | 0.223 | 23 | 79 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF6 | team_total | 0.140 | 0.155 | 0.152 | 17 | 86 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27MINUTA-UTA5 | team_total | 0.227 | 0.240 | 0.237 | 25 | 77 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT27OTTVGK-4 | game_total | 0.892 | 0.895 | 0.894 | 90 | 11 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27MINUTA-MIN4 | team_total | 0.363 | 0.380 | 0.377 | 39 | 63 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-10 | game_total | 0.129 | 0.120 | 0.122 | 13 | 89 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF2 | team_total | 0.861 | 0.870 | 0.868 | 88 | 14 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-VGK5 | team_total | 0.294 | 0.280 | 0.283 | 29 | 73 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT27MINUTA-UTA2 | game_spread | 0.314 | 0.305 | 0.307 | 31 | 70 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27MINUTA-MIN5 | team_total | 0.190 | 0.205 | 0.202 | 22 | 81 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT2 | team_total | 0.810 | 0.800 | 0.802 | 81 | 21 |  | -0.011 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ UTA | 0.535 | 0.566 | 0.173 | 0.213 | 6.21 | 6.40 | 0.989/0.991 | KXNHLTEAMTOTAL-26OCT27MINUTA-UTA4 +0.049 |
| OTT @ VGK | 0.572 | 0.581 | 0.163 | 0.213 | 6.68 | 6.30 | 1.004/1.040 | KXNHLTOTAL-26OCT27OTTVGK-6 -0.062 |
| VAN @ ANA | 0.632 | 0.602 | 0.159 | 0.204 | 6.81 | 6.78 | 1.016/1.026 | KXNHLSPREAD-26OCT27VANANA-ANA2 -0.039 |
| BUF @ SJS | 0.463 | 0.524 | 0.171 | 0.214 | 6.74 | 6.52 | 1.039/0.999 | KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4 -0.069 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Kirill Kaprizov: 1+ goals NO @ 56c · p 0.6421 (adj 0.6203) · $18.02 · thesis MIN:SUPPRESSED
- Jack McBain: 1+ goals YES @ 11c · p 0.1562 (adj 0.1434) · $6.1 · thesis UTA:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 18c · p 0.235 (adj 0.22) · $7.82 · thesis UTA:OFFENSE_4PLUS
- Anders Lee: 1+ goals YES @ 20c · p 0.2453 (adj 0.2327) · $5.72 · thesis UTA:OFFENSE_4PLUS
- Mitch Marner: 1+ assists NO @ 46c · p 0.6081 (adj 0.5086) · $14.69 · thesis VGK:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0852 (adj 0.0776) · $3.07 · thesis VGK:OFFENSE_4PLUS
- Jonas Johansson: 28+ saves NO @ 61c · p 0.773 (adj 0.647) · $16.33 · thesis OTT:NET_LOW_VOLUME
- Michael Amadio: 1+ goals YES @ 13c · p 0.1607 (adj 0.1518) · $3.49 · thesis OTT:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 18c · p 0.2693 (adj 0.2445) · $13.75 · thesis ANA:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 18c · p 0.2344 (adj 0.2195) · $7.6 · thesis VAN:OFFENSE_4PLUS
- Arshdeep Bains: 1+ goals YES @ 8c · p 0.1147 (adj 0.101) · $3.52 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 17c · p 0.2116 (adj 0.2) · $5.22 · thesis VAN:OFFENSE_4PLUS
- Adam Gaudette: 1+ goals YES @ 13c · p 0.1747 (adj 0.1623) · $5.56 · thesis SJS:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 61c · p 0.6756 (adj 0.658) · $17.7 · thesis BUF:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 22c · p 0.2695 (adj 0.2559) · $6.41 · thesis SJS:OFFENSE_4PLUS
- Buffalo wins by over 2.5 goals NO @ 76c · p 0.834 (adj 0.7945) · $15.0 · thesis SJS:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MIN @ UTA** · priced 183/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (CONFIRMED) exp shots 27.66, exp saves 24.14 (sd 6.55), pull risk 0.053
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 28.67, exp saves 24.59 (sd 6.81), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.252 | 0.405 | 41/60 | +0.131 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.397 | 0.510 | 52/50 | +0.085 | STANDARD |
| Kailer Yamamoto: 1+ points | 0.434 | 0.330 | 35/69 | +0.068 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.609 | 0.705 | 72/31 | +0.066 | STANDARD |
| Quinn Hughes: 1+ assists | 0.512 | 0.605 | 61/40 | +0.071 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.358 | 0.445 | 45/56 | +0.065 | STANDARD |

**OTT @ VGK** · priced 185/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (CONFIRMED) exp shots 26.26, exp saves 22.87 (sd 6.3), pull risk 0.054
- OTT net: Jonas Johansson (CONFIRMED) exp shots 26.79, exp saves 22.82 (sd 6.49), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonas Johansson: 28+ saves | 0.227 | 0.395 | 40/61 | +0.146 |  |
| Mitch Marner: 1+ assists | 0.392 | 0.545 | 55/46 | +0.131 | STANDARD |
| Jake Sanderson: 1+ points | 0.370 | 0.505 | 52/51 | +0.103 | STANDARD |
| Jake Sanderson: 1+ assists | 0.288 | 0.410 | 42/60 | +0.095 | STANDARD |
| Adin Hill: 21+ saves | 0.651 | 0.535 | 57/50 | +0.064 |  |
| Mitch Marner: 1+ points | 0.543 | 0.650 | 66/36 | +0.081 | STANDARD |

**VAN @ ANA** · priced 180/199 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 23.87, exp saves 20.92 (sd 5.92), pull risk 0.058
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.6, exp saves 26.72 (sd 7.46), pull risk 0.091

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tom Willander: 1+ assists | 0.278 | 0.130 | 24/98 | +0.025 | STANDARD |
| Arshdeep Bains: 1+ points | 0.260 | 0.120 | 22/98 | +0.027 | STANDARD |
| Tim Washe: 1+ points | 0.412 | 0.290 | 30/72 | +0.097 | STANDARD |
| A.J. Greer: 1+ points | 0.435 | 0.320 | 33/69 | +0.089 | STANDARD |
| Tim Washe: 1+ assists | 0.303 | 0.200 | 21/81 | +0.082 | STANDARD |
| A.J. Greer: 1+ goals | 0.269 | 0.170 | 18/84 | +0.079 | STANDARD |

**BUF @ SJS** · priced 218/221 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.51, exp saves 24.68 (sd 6.72), pull risk 0.063
- BUF net: Colten Ellis (PROBABLE) exp shots 27.09, exp saves 23.35 (sd 6.5), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ points | 0.298 | 0.090 | 17/99 | +0.118 | STANDARD |
| Ivar Stenberg: 1+ points | 0.407 | 0.570 | 58/44 | +0.135 | STANDARD |
| Sam Dickinson: 1+ assists | 0.246 | 0.085 | 15/98 | +0.087 | STANDARD |
| Zack Ostapchuk: 1+ points | 0.236 | 0.090 | 16/98 | +0.067 | STANDARD |
| Barclay Goodrow: 1+ points | 0.230 | 0.100 | 18/98 | +0.039 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.447 | 0.575 | 59/44 | +0.096 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
