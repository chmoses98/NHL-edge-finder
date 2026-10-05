# NHL slate 2026-10-05 — RESEARCH_ONLY

generated 2026-10-05T16:56:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2834 · contracts joined: 736 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 636, 'OK': 54, 'NO_EDGE': 46}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 105, 'game_early_goal': 4, 'first_goal': 142, 'game_winner': 8, 'player_goals': 142, 'game_overtime': 4, 'player_points': 137, 'goalie_saves': 6, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ TBL | 2026-10-05T23:00:00Z | T-6h | 0.613 | 0.387 | 0.182 | 5.51 | 3.10 | 2.42 | 183 (25/158) | PROBABLE/CONFIRMED |
| OTT @ BOS | 2026-10-05T23:30:00Z | T-6h | 0.591 | 0.409 | 0.175 | 6.10 | 3.34 | 2.76 | 189 (25/164) | CONFIRMED/CONFIRMED |
| WPG @ PIT | 2026-10-05T23:30:00Z | T-6h | 0.620 | 0.381 | 0.166 | 6.52 | 3.64 | 2.87 | 179 (25/154) | CONFIRMED/CONFIRMED |
| SJS @ DAL | 2026-10-06T00:00:00Z | T-6h | 0.586 | 0.414 | 0.166 | 6.28 | 3.41 | 2.87 | 185 (25/160) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT05OTTBOS-BOS | game_winner | 0.591 | 0.465 | 0.490 | 47 | 54 | yes | +0.104 | OK |
| KXNHLGAME-26OCT05OTTBOS-OTT | game_winner | 0.409 | 0.525 | 0.502 | 53 | 48 | no | +0.094 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-BOS2 | game_spread | 0.366 | 0.265 | 0.284 | 27 | 74 | yes | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB4 | team_total | 0.385 | 0.485 | 0.465 | 49 | 52 | no | +0.078 | OK |
| KXNHLTOTAL-26OCT05PHITB-6 | game_total | 0.443 | 0.535 | 0.517 | 54 | 47 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS3 | team_total | 0.655 | 0.565 | 0.583 | 57 | 44 | yes | +0.067 | OK |
| KXNHLSPREAD-26OCT05PHITB-TB3 | game_spread | 0.228 | 0.315 | 0.296 | 32 | 69 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS4 | team_total | 0.441 | 0.355 | 0.372 | 36 | 65 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT05PHITB-5 | game_total | 0.674 | 0.755 | 0.740 | 76 | 25 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-OTT2 | game_spread | 0.213 | 0.295 | 0.277 | 30 | 71 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB3 | team_total | 0.613 | 0.700 | 0.683 | 71 | 31 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS5 | team_total | 0.250 | 0.175 | 0.188 | 18 | 83 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB5 | team_total | 0.198 | 0.275 | 0.258 | 28 | 73 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT05PHITB-7 | game_total | 0.338 | 0.415 | 0.399 | 42 | 59 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT4 | team_total | 0.310 | 0.385 | 0.369 | 39 | 62 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT05PHITB-4 | game_total | 0.777 | 0.845 | 0.833 | 85 | 16 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-OTT3 | game_spread | 0.117 | 0.185 | 0.169 | 19 | 82 | no | +0.052 | OK |
| KXNHLGAME-26OCT05SJDAL-SJ | game_winner | 0.414 | 0.345 | 0.358 | 35 | 66 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT3 | team_total | 0.530 | 0.595 | 0.582 | 60 | 41 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT05PHITB-TB2 | game_spread | 0.371 | 0.435 | 0.422 | 44 | 57 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-BOS3 | game_spread | 0.232 | 0.175 | 0.185 | 18 | 83 | yes | +0.041 | OK |
| KXNHLGAME-26OCT05SJDAL-DAL | game_winner | 0.586 | 0.645 | 0.633 | 65 | 36 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB2 | team_total | 0.814 | 0.875 | 0.864 | 89 | 14 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT05PHITB-8 | game_total | 0.171 | 0.225 | 0.213 | 23 | 78 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT2 | team_total | 0.754 | 0.805 | 0.795 | 81 | 20 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS2 | team_total | 0.843 | 0.790 | 0.802 | 80 | 22 | yes | +0.032 | OK |
| KXNHLGAME-26OCT05PHITB-TB | game_winner | 0.613 | 0.665 | 0.655 | 67 | 34 | no | +0.031 | OK |
| KXNHLGAME-26OCT05PHITB-PHI | game_winner | 0.387 | 0.335 | 0.345 | 34 | 67 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT05SJDAL-DAL2 | game_spread | 0.363 | 0.415 | 0.404 | 42 | 59 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT05PHITB-9 | game_total | 0.111 | 0.155 | 0.145 | 16 | 85 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT5 | team_total | 0.151 | 0.195 | 0.186 | 20 | 81 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4 | team_total | 0.456 | 0.505 | 0.495 | 51 | 50 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL3 | team_total | 0.670 | 0.715 | 0.706 | 72 | 29 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB6 | team_total | 0.087 | 0.125 | 0.116 | 13 | 88 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS6 | team_total | 0.120 | 0.075 | 0.083 | 9 | 94 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT05SJDAL-DAL3 | game_spread | 0.232 | 0.275 | 0.266 | 28 | 73 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL5 | team_total | 0.263 | 0.305 | 0.296 | 31 | 70 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT05SJDAL-SJ2 | game_spread | 0.220 | 0.185 | 0.192 | 19 | 82 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT05PHITB-3 | game_total | 0.938 | 0.965 | 0.961 | 97 | 4 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL2 | team_total | 0.850 | 0.880 | 0.874 | 89 | 13 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT05PHITB-PHI2 | game_spread | 0.180 | 0.155 | 0.160 | 16 | 85 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ4 | team_total | 0.335 | 0.305 | 0.311 | 31 | 70 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT05PHITB-10 | game_total | 0.047 | 0.065 | 0.061 | 7 | 94 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT05SJDAL-5 | game_total | 0.780 | 0.805 | 0.800 | 81 | 20 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-7 | game_total | 0.433 | 0.405 | 0.410 | 41 | 60 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ6 | team_total | 0.069 | 0.055 | 0.058 | 6 | 95 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT6 | team_total | 0.060 | 0.075 | 0.072 | 8 | 93 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT05SJDAL-7 | game_total | 0.457 | 0.485 | 0.479 | 49 | 52 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL6 | team_total | 0.128 | 0.145 | 0.141 | 15 | 86 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-10 | game_total | 0.077 | 0.065 | 0.067 | 7 | 94 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT05SJDAL-4 | game_total | 0.861 | 0.875 | 0.872 | 88 | 13 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-9 | game_total | 0.171 | 0.155 | 0.158 | 16 | 85 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT05SJDAL-6 | game_total | 0.572 | 0.595 | 0.590 | 60 | 41 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT05WPGPIT-10 | game_total | 0.107 | 0.095 | 0.097 | 10 | 91 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ5 | team_total | 0.169 | 0.150 | 0.154 | 16 | 86 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-3 | game_total | 0.959 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-6 | game_total | 0.545 | 0.525 | 0.529 | 53 | 48 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05PHITB-2 | game_total | 0.970 | 0.980 | 0.978 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI2 | team_total | 0.689 | 0.705 | 0.702 | 71 | 30 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT5 | team_total | 0.310 | 0.295 | 0.298 | 30 | 71 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT05SJDAL-SJ3 | game_spread | 0.122 | 0.115 | 0.116 | 12 | 89 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-3 | game_total | 0.966 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-9 | game_total | 0.215 | 0.205 | 0.207 | 21 | 80 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI4 | team_total | 0.234 | 0.245 | 0.243 | 25 | 76 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-8 | game_total | 0.246 | 0.235 | 0.237 | 24 | 77 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-10 | game_total | 0.091 | 0.095 | 0.094 | 10 | 91 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI6 | team_total | 0.035 | 0.035 | 0.035 | 4 | 97 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT3 | team_total | 0.717 | 0.705 | 0.707 | 71 | 30 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ3 | team_total | 0.550 | 0.535 | 0.538 | 54 | 47 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT05PHITB-PHI3 | game_spread | 0.092 | 0.095 | 0.094 | 10 | 91 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-2 | game_total | 0.987 | 0.990 | 0.989 |  | 2 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-3 | game_total | 0.973 | 0.970 | 0.971 | 98 | 4 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-WPG3 | game_spread | 0.111 | 0.115 | 0.114 | 12 | 89 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI5 | team_total | 0.102 | 0.105 | 0.104 | 11 | 90 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-4 | game_total | 0.850 | 0.845 | 0.846 | 85 | 16 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-5 | game_total | 0.808 | 0.815 | 0.814 | 82 | 19 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ2 | team_total | 0.772 | 0.760 | 0.763 | 77 | 25 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-4 | game_total | 0.883 | 0.885 | 0.885 | 89 | 12 |  | -0.011 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ TBL | 0.613 | 0.578 | 0.182 | 0.228 | 5.51 | 5.80 | 0.951/0.994 | KXNHLTEAMTOTAL-26OCT05PHITB-PHI3 +0.067 |
| OTT @ BOS | 0.591 | 0.502 | 0.175 | 0.225 | 6.10 | 6.01 | 0.955/0.968 | KXNHLSPREAD-26OCT05OTTBOS-BOS2 -0.091 |
| WPG @ PIT | 0.620 | 0.628 | 0.166 | 0.206 | 6.52 | 6.47 | 1.012/0.997 | KXNHLSPREAD-26OCT05WPGPIT-PIT3 +0.018 |
| SJS @ DAL | 0.586 | 0.549 | 0.166 | 0.214 | 6.28 | 6.24 | 0.993/1.034 | KXNHLSPREAD-26OCT05SJDAL-DAL2 -0.040 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 15 recommended · full analysis in card.md / packet.json `thesis_card`

- John Carlson: 1+ assists NO @ 52c · p 0.722 (adj 0.5875) · $18.09 · thesis TBL:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 11c · p 0.1562 (adj 0.1421) · $5.42 · thesis PHI:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 69c · p 0.7826 (adj 0.7338) · $15.83 · thesis GAME:TIGHT
- Christian Dvorak: 1+ goals YES @ 15c · p 0.1949 (adj 0.1812) · $5.12 · thesis PHI:OFFENSE_4PLUS
- Marat Khusnutdinov: 1+ goals YES @ 10c · p 0.1514 (adj 0.1373) · $6.82 · thesis BOS:OFFENSE_4PLUS
- William Eklund: 1+ assists NO @ 67c · p 0.834 (adj 0.7241) · $17.45 · thesis OTT:SUPPRESSED
- JJ Peterka: 1+ assists NO @ 69c · p 0.7847 (adj 0.7349) · $17.45 · thesis BOS:SUPPRESSED
- Nick Cousins: 1+ goals YES @ 8c · p 0.1113 (adj 0.101) · $3.49 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 14c · p 0.1977 (adj 0.182) · $8.21 · thesis PIT:OFFENSE_4PLUS
- Morgan Barron: 1+ goals YES @ 10c · p 0.133 (adj 0.1235) · $4.13 · thesis WPG:OFFENSE_4PLUS
- Egor Chinakhov: 1+ assists YES @ 32c · p 0.3823 (adj 0.3461) · $3.17 · thesis PIT:OFFENSE_4PLUS
- Jason Robertson: 1+ goals NO @ 56c · p 0.6299 (adj 0.6112) · $13.14 · thesis DAL:SUPPRESSED
- Mikko Rantanen: 1+ goals NO @ 67c · p 0.732 (adj 0.7152) · $13.99 · thesis DAL:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 69c · p 0.8183 (adj 0.7284) · $14.2 · thesis SJS:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 15c · p 0.1886 (adj 0.1777) · $3.48 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ TBL** · priced 124/132 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 23.71, exp saves 20.81 (sd 5.7), pull risk 0.041
- PHI net: Dan Vladar (CONFIRMED) exp shots 28.33, exp saves 24.37 (sd 6.7), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.278 | 0.485 | 49/52 | +0.185 | STANDARD |
| John Carlson: 1+ points | 0.364 | 0.560 | 57/45 | +0.169 | STANDARD |
| John Carlson: 2+ points | 0.078 | 0.210 | 22/80 | +0.111 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.525 | 0.640 | 65/37 | +0.089 | STANDARD |
| John Carlson: 2+ assists | 0.045 | 0.150 | 16/86 | +0.087 | STANDARD |
| Nikita Kucherov: 2+ points | 0.341 | 0.445 | 45/56 | +0.082 | STANDARD |

**OTT @ BOS** · priced 132/138 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 29.37, exp saves 25.61 (sd 6.88), pull risk 0.055
- OTT net: Linus Ullmark (CONFIRMED) exp shots 25.52, exp saves 22.1 (sd 6.17), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.166 | 0.335 | 34/67 | +0.149 | STANDARD |
| William Eklund: 1+ points | 0.353 | 0.490 | 50/52 | +0.109 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.236 | 0.355 | 37/66 | +0.088 | PRIOR_HEAVY |
| JJ Peterka: 1+ points | 0.393 | 0.505 | 51/50 | +0.089 | STANDARD |
| JJ Peterka: 1+ assists | 0.215 | 0.315 | 32/69 | +0.080 | STANDARD |
| Tim Stutzle: 1+ assists | 0.384 | 0.475 | 48/53 | +0.069 | STANDARD |

**WPG @ PIT** · priced 125/128 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (CONFIRMED) exp shots 25.59, exp saves 22.42 (sd 6.15), pull risk 0.052
- WPG net: Clay Stevenson (CONFIRMED) exp shots 28.46, exp saves 24.09 (sd 6.75), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sergei Murashov: 23+ saves | 0.486 | 0.290 | 53/95 | -0.061 |  |
| Mark Scheifele: 1+ assists | 0.427 | 0.515 | 52/49 | +0.065 | STANDARD |
| Sidney Crosby: 1+ assists | 0.439 | 0.525 | 53/48 | +0.063 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.382 | 0.310 | 32/70 | +0.047 | STANDARD |
| Josh Morrissey: 1+ assists | 0.374 | 0.440 | 45/57 | +0.039 | STANDARD |
| Sidney Crosby: 2+ points | 0.260 | 0.325 | 34/69 | +0.035 | STANDARD |

**SJS @ DAL** · priced 132/134 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.83, exp saves 21.65 (sd 6.08), pull risk 0.055
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.49, exp saves 23.67 (sd 6.53), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason Marchment: 1+ assists | 0.182 | 0.320 | 33/69 | +0.113 | STANDARD |
| Roope Hintz: 1+ assists | 0.268 | 0.405 | 41/60 | +0.115 | STANDARD |
| Mikko Rantanen: 2+ points | 0.210 | 0.330 | 34/68 | +0.094 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.417 | 0.525 | 53/48 | +0.086 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.158 | 0.255 | 27/76 | +0.069 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ points | 0.283 | 0.370 | 38/64 | +0.061 | PRIOR_HEAVY |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
