# NHL slate 2026-10-05 — RESEARCH_ONLY

generated 2026-10-05T23:28:36Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 3 · markets on board: 2838 · contracts joined: 553 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 478, 'OK': 35, 'NO_EDGE': 40}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 80, 'game_early_goal': 3, 'first_goal': 106, 'game_winner': 6, 'player_goals': 106, 'game_overtime': 3, 'player_points': 104, 'goalie_saves': 4, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BOS | 2026-10-05T23:30:00Z | T-<10m | 0.591 | 0.409 | 0.175 | 6.10 | 3.34 | 2.76 | 189 (25/164) | CONFIRMED/CONFIRMED |
| WPG @ PIT | 2026-10-05T23:30:00Z | T-<10m | 0.620 | 0.381 | 0.166 | 6.52 | 3.64 | 2.87 | 179 (25/154) | CONFIRMED/CONFIRMED |
| SJS @ DAL | 2026-10-06T00:00:00Z | T-30m | 0.595 | 0.405 | 0.173 | 6.37 | 3.49 | 2.87 | 185 (25/160) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT05OTTBOS-BOS | game_winner | 0.591 | 0.475 | 0.498 | 48 | 53 | yes | +0.094 | OK |
| KXNHLGAME-26OCT05OTTBOS-OTT | game_winner | 0.409 | 0.525 | 0.502 | 53 | 48 | no | +0.094 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-BOS2 | game_spread | 0.366 | 0.265 | 0.284 | 27 | 74 | yes | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS3 | team_total | 0.655 | 0.565 | 0.583 | 57 | 44 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS4 | team_total | 0.441 | 0.355 | 0.372 | 36 | 65 | yes | +0.065 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-OTT2 | game_spread | 0.213 | 0.295 | 0.277 | 30 | 71 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-OTT3 | game_spread | 0.117 | 0.185 | 0.169 | 19 | 82 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS5 | team_total | 0.250 | 0.180 | 0.193 | 19 | 83 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-BOS3 | game_spread | 0.232 | 0.175 | 0.185 | 18 | 83 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS6 | team_total | 0.120 | 0.070 | 0.078 | 8 | 94 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT4 | team_total | 0.310 | 0.365 | 0.354 | 37 | 64 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT3 | team_total | 0.530 | 0.585 | 0.574 | 59 | 42 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS2 | team_total | 0.843 | 0.790 | 0.802 | 80 | 22 | yes | +0.032 | OK |
| KXNHLGAME-26OCT05SJDAL-SJ | game_winner | 0.405 | 0.355 | 0.365 | 36 | 65 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT05SJDAL-DAL3 | game_spread | 0.241 | 0.285 | 0.276 | 29 | 72 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT2 | team_total | 0.754 | 0.795 | 0.787 | 80 | 21 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4 | team_total | 0.472 | 0.515 | 0.506 | 52 | 49 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT05SJDAL-DAL2 | game_spread | 0.374 | 0.415 | 0.407 | 42 | 59 | no | +0.019 | OK |
| KXNHLGAME-26OCT05SJDAL-DAL | game_winner | 0.595 | 0.635 | 0.627 | 64 | 37 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT5 | team_total | 0.151 | 0.185 | 0.178 | 19 | 82 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-7 | game_total | 0.433 | 0.395 | 0.402 | 40 | 61 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL5 | team_total | 0.277 | 0.305 | 0.299 | 31 | 70 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL3 | team_total | 0.688 | 0.715 | 0.710 | 72 | 29 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-6 | game_total | 0.545 | 0.515 | 0.521 | 52 | 49 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ6 | team_total | 0.071 | 0.055 | 0.058 | 6 | 95 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT6 | team_total | 0.060 | 0.075 | 0.072 | 8 | 93 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-8 | game_total | 0.246 | 0.220 | 0.225 | 23 | 79 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-10 | game_total | 0.077 | 0.065 | 0.067 | 7 | 94 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ4 | team_total | 0.337 | 0.315 | 0.319 | 32 | 69 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL2 | team_total | 0.861 | 0.880 | 0.876 | 89 | 13 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-9 | game_total | 0.171 | 0.150 | 0.154 | 16 | 86 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT05WPGPIT-5 | game_total | 0.808 | 0.825 | 0.822 | 83 | 18 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ5 | team_total | 0.170 | 0.150 | 0.154 | 16 | 86 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT05WPGPIT-10 | game_total | 0.107 | 0.095 | 0.097 | 10 | 91 | yes | +0.000 | OK |
| KXNHLSPREAD-26OCT05SJDAL-SJ2 | game_spread | 0.211 | 0.195 | 0.198 | 20 | 81 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT05WPGPIT-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-5 | game_total | 0.790 | 0.810 | 0.806 | 82 | 20 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-8 | game_total | 0.303 | 0.285 | 0.288 | 29 | 72 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-3 | game_total | 0.959 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT6 | team_total | 0.157 | 0.145 | 0.147 | 15 | 86 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-3 | game_total | 0.969 | 0.965 | 0.966 | 97 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-2 | game_total | 0.987 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-3 | game_total | 0.973 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-9 | game_total | 0.215 | 0.205 | 0.207 | 21 | 80 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL6 | team_total | 0.139 | 0.150 | 0.148 | 16 | 86 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-4 | game_total | 0.869 | 0.875 | 0.874 | 88 | 13 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-10 | game_total | 0.099 | 0.095 | 0.096 | 10 | 91 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT3 | team_total | 0.717 | 0.705 | 0.707 | 71 | 30 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ2 | team_total | 0.775 | 0.760 | 0.763 | 77 | 25 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ3 | team_total | 0.549 | 0.535 | 0.538 | 54 | 47 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-9 | game_total | 0.203 | 0.195 | 0.197 | 20 | 81 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-WPG3 | game_spread | 0.111 | 0.115 | 0.114 | 12 | 89 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-4 | game_total | 0.850 | 0.845 | 0.846 | 85 | 16 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-8 | game_total | 0.285 | 0.275 | 0.277 | 28 | 73 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-7 | game_total | 0.473 | 0.485 | 0.483 | 49 | 52 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-4 | game_total | 0.883 | 0.885 | 0.885 | 89 | 12 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT05SJDAL-SJ3 | game_spread | 0.117 | 0.115 | 0.115 | 12 | 89 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-PIT3 | game_spread | 0.267 | 0.275 | 0.273 | 28 | 73 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT2 | team_total | 0.875 | 0.870 | 0.871 | 88 | 14 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-6 | game_total | 0.586 | 0.595 | 0.593 | 60 | 41 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-5 | game_total | 0.760 | 0.755 | 0.756 | 76 | 25 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-WPG2 | game_spread | 0.197 | 0.195 | 0.195 | 20 | 81 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-WPG6 | team_total | 0.071 | 0.070 | 0.070 | 8 | 94 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT5 | team_total | 0.310 | 0.300 | 0.302 | 31 | 71 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-7 | game_total | 0.502 | 0.495 | 0.496 | 50 | 51 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26OCT05WPGPIT-WPG | game_winner | 0.381 | 0.375 | 0.376 | 38 | 63 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26OCT05WPGPIT-PIT | game_winner | 0.620 | 0.625 | 0.624 | 63 | 38 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-PIT2 | game_spread | 0.401 | 0.395 | 0.396 | 40 | 61 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-WPG2 | team_total | 0.775 | 0.780 | 0.779 | 79 | 23 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-WPG5 | team_total | 0.169 | 0.170 | 0.170 | 18 | 84 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-WPG3 | team_total | 0.547 | 0.545 | 0.546 | 55 | 46 |  | -0.020 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-6 | game_total | 0.614 | 0.615 | 0.615 | 62 | 39 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT4 | team_total | 0.506 | 0.505 | 0.505 | 51 | 50 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-WPG4 | team_total | 0.334 | 0.335 | 0.335 | 35 | 68 |  | -0.029 | NO_EDGE |
| KXNHL1P-26OCT05OTTBOS-BOS | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT05OTTBOS-OTT | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT05OTTBOS-TIE | period_winner |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT05OTTBOS-BOS2 | period_spread |  | 0.080 |  | 10 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT05OTTBOS-OTT2 | period_spread |  | 0.095 |  | 12 | 93 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BOS | 0.591 | 0.502 | 0.175 | 0.225 | 6.10 | 6.01 | 0.955/0.968 | KXNHLSPREAD-26OCT05OTTBOS-BOS2 -0.091 |
| WPG @ PIT | 0.620 | 0.628 | 0.166 | 0.206 | 6.52 | 6.47 | 1.012/0.997 | KXNHLSPREAD-26OCT05WPGPIT-PIT3 +0.018 |
| SJS @ DAL | 0.595 | 0.553 | 0.173 | 0.220 | 6.37 | 6.26 | 0.993/1.039 | KXNHLSPREAD-26OCT05SJDAL-DAL2 -0.054 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Nick Cousins: 1+ goals YES @ 7c · p 0.1138 (adj 0.0966) · $5.03 · thesis OTT:OFFENSE_4PLUS
- William Eklund: 1+ assists NO @ 67c · p 0.8413 (adj 0.7235) · $20.0 · thesis OTT:SUPPRESSED
- Hayden Hodgson: 1+ goals YES @ 6c · p 0.0924 (adj 0.0818) · $4.3 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 13c · p 0.1627 (adj 0.157) · $5.35 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 14c · p 0.1977 (adj 0.182) · $9.1 · thesis PIT:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 27c · p 0.3099 (adj 0.2987) · $5.13 · thesis WPG:OFFENSE_4PLUS
- Ben Kindel: 1+ goals NO @ 77c · p 0.8032 (adj 0.7924) · $12.14 · thesis PIT:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 13c · p 0.1874 (adj 0.1718) · $8.77 · thesis SJS:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 67c · p 0.7288 (adj 0.7128) · $16.65 · thesis DAL:SUPPRESSED
- Jason Robertson: 1+ goals NO @ 57c · p 0.6313 (adj 0.6147) · $13.35 · thesis DAL:SUPPRESSED
- Igor Chernyshov: 1+ goals YES @ 17c · p 0.2123 (adj 0.2005) · $5.77 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**OTT @ BOS** · priced 134/138 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 29.37, exp saves 25.61 (sd 6.88), pull risk 0.055
- OTT net: Linus Ullmark (CONFIRMED) exp shots 25.52, exp saves 22.1 (sd 6.17), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.159 | 0.340 | 35/67 | +0.156 | STANDARD |
| Jeremy Swayman: 26+ saves | 0.501 | 0.340 | 48/80 | +0.003 |  |
| William Eklund: 1+ points | 0.339 | 0.490 | 50/52 | +0.124 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.234 | 0.365 | 38/65 | +0.100 | PRIOR_HEAVY |
| JJ Peterka: 1+ points | 0.379 | 0.505 | 51/50 | +0.103 | STANDARD |
| JJ Peterka: 1+ assists | 0.204 | 0.315 | 32/69 | +0.091 | STANDARD |

**WPG @ PIT** · priced 125/128 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (CONFIRMED) exp shots 25.59, exp saves 22.42 (sd 6.15), pull risk 0.052
- WPG net: Clay Stevenson (CONFIRMED) exp shots 28.46, exp saves 24.09 (sd 6.75), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sergei Murashov: 23+ saves | 0.486 | 0.350 | 50/80 | -0.031 |  |
| Rickard Rakell: 2+ points | 0.265 | 0.155 | 24/93 | +0.012 | STANDARD |
| Mark Scheifele: 1+ assists | 0.427 | 0.515 | 52/49 | +0.065 | STANDARD |
| Sidney Crosby: 1+ assists | 0.439 | 0.525 | 53/48 | +0.063 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.382 | 0.305 | 32/71 | +0.047 | STANDARD |
| Sidney Crosby: 2+ assists | 0.112 | 0.185 | 20/83 | +0.048 | STANDARD |

**SJS @ DAL** · priced 130/134 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.83, exp saves 21.63 (sd 6.07), pull risk 0.052
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.49, exp saves 23.67 (sd 6.46), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.274 | 0.425 | 43/58 | +0.129 | STANDARD |
| Mason Marchment: 1+ assists | 0.180 | 0.325 | 34/69 | +0.115 | STANDARD |
| Ivar Stenberg: 1+ points | 0.262 | 0.380 | 39/63 | +0.092 | PRIOR_HEAVY |
| Mikko Rantanen: 2+ points | 0.215 | 0.330 | 34/68 | +0.089 | STANDARD |
| Roope Hintz: 1+ points | 0.481 | 0.595 | 61/42 | +0.082 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.142 | 0.250 | 26/76 | +0.086 | PRIOR_HEAVY |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
