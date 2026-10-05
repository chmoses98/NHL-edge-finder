# NHL slate 2026-10-05 — RESEARCH_ONLY

generated 2026-10-05T18:34:13Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2834 · contracts joined: 736 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 636, 'OK': 51, 'NO_EDGE': 49}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 105, 'game_early_goal': 4, 'first_goal': 142, 'game_winner': 8, 'player_goals': 142, 'game_overtime': 4, 'player_points': 137, 'goalie_saves': 6, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ TBL | 2026-10-05T23:00:00Z | T-3h | 0.613 | 0.387 | 0.182 | 5.51 | 3.10 | 2.42 | 183 (25/158) | PROBABLE/CONFIRMED |
| OTT @ BOS | 2026-10-05T23:30:00Z | T-3h | 0.591 | 0.409 | 0.175 | 6.10 | 3.34 | 2.76 | 189 (25/164) | CONFIRMED/CONFIRMED |
| WPG @ PIT | 2026-10-05T23:30:00Z | T-3h | 0.620 | 0.381 | 0.166 | 6.52 | 3.64 | 2.87 | 179 (25/154) | CONFIRMED/CONFIRMED |
| SJS @ DAL | 2026-10-06T00:00:00Z | T-3h | 0.595 | 0.405 | 0.173 | 6.37 | 3.49 | 2.87 | 185 (25/160) | CONFIRMED/CONFIRMED |

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
| KXNHLTOTAL-26OCT05PHITB-5 | game_total | 0.674 | 0.760 | 0.744 | 77 | 25 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-OTT2 | game_spread | 0.213 | 0.295 | 0.277 | 30 | 71 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB3 | team_total | 0.613 | 0.695 | 0.679 | 70 | 31 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS5 | team_total | 0.250 | 0.175 | 0.188 | 18 | 83 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB5 | team_total | 0.198 | 0.275 | 0.258 | 28 | 73 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT05PHITB-7 | game_total | 0.338 | 0.415 | 0.399 | 42 | 59 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT05PHITB-4 | game_total | 0.777 | 0.845 | 0.833 | 85 | 16 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-OTT3 | game_spread | 0.117 | 0.185 | 0.169 | 19 | 82 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT05PHITB-TB2 | game_spread | 0.371 | 0.435 | 0.422 | 44 | 57 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS2 | team_total | 0.843 | 0.785 | 0.798 | 79 | 22 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-BOS3 | game_spread | 0.232 | 0.175 | 0.185 | 18 | 83 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB2 | team_total | 0.814 | 0.870 | 0.860 | 88 | 14 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT05PHITB-8 | game_total | 0.171 | 0.225 | 0.213 | 23 | 78 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT2 | team_total | 0.754 | 0.805 | 0.795 | 81 | 20 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT4 | team_total | 0.310 | 0.370 | 0.358 | 38 | 64 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT3 | team_total | 0.530 | 0.590 | 0.578 | 60 | 42 | no | +0.033 | OK |
| KXNHLGAME-26OCT05PHITB-PHI | game_winner | 0.387 | 0.335 | 0.345 | 34 | 67 | yes | +0.031 | OK |
| KXNHLGAME-26OCT05PHITB-TB | game_winner | 0.613 | 0.665 | 0.655 | 67 | 34 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT05PHITB-9 | game_total | 0.111 | 0.155 | 0.145 | 16 | 85 | no | +0.030 | OK |
| KXNHLGAME-26OCT05SJDAL-DAL | game_winner | 0.595 | 0.645 | 0.635 | 65 | 36 | no | +0.029 | OK |
| KXNHLGAME-26OCT05SJDAL-SJ | game_winner | 0.405 | 0.355 | 0.365 | 36 | 65 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB6 | team_total | 0.087 | 0.125 | 0.116 | 13 | 88 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS6 | team_total | 0.120 | 0.075 | 0.083 | 9 | 94 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT05SJDAL-DAL3 | game_spread | 0.241 | 0.285 | 0.276 | 29 | 72 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT05PHITB-3 | game_total | 0.938 | 0.965 | 0.961 | 97 | 4 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT5 | team_total | 0.151 | 0.190 | 0.182 | 20 | 82 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT05PHITB-PHI2 | game_spread | 0.180 | 0.155 | 0.160 | 16 | 85 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4 | team_total | 0.472 | 0.505 | 0.498 | 51 | 50 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT05SJDAL-SJ2 | game_spread | 0.211 | 0.185 | 0.190 | 19 | 82 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT05SJDAL-DAL2 | game_spread | 0.374 | 0.410 | 0.403 | 42 | 60 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL5 | team_total | 0.277 | 0.305 | 0.299 | 31 | 70 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT05PHITB-2 | game_total | 0.970 | 0.985 | 0.983 | 99 | 2 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL3 | team_total | 0.688 | 0.715 | 0.710 | 72 | 29 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-6 | game_total | 0.545 | 0.515 | 0.521 | 52 | 49 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ6 | team_total | 0.071 | 0.055 | 0.058 | 6 | 95 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-7 | game_total | 0.433 | 0.405 | 0.410 | 41 | 60 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT6 | team_total | 0.060 | 0.080 | 0.076 | 9 | 93 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-10 | game_total | 0.077 | 0.065 | 0.067 | 7 | 94 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ4 | team_total | 0.337 | 0.310 | 0.315 | 32 | 70 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL2 | team_total | 0.861 | 0.880 | 0.876 | 89 | 13 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-9 | game_total | 0.171 | 0.150 | 0.154 | 16 | 86 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ5 | team_total | 0.170 | 0.155 | 0.158 | 16 | 85 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT05WPGPIT-10 | game_total | 0.107 | 0.095 | 0.097 | 10 | 91 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT05PHITB-10 | game_total | 0.047 | 0.055 | 0.053 | 6 | 95 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-2 | game_total | 0.989 | 0.980 | 0.982 | 99 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-5 | game_total | 0.790 | 0.805 | 0.802 | 81 | 20 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-8 | game_total | 0.303 | 0.285 | 0.288 | 29 | 72 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-3 | game_total | 0.959 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-3 | game_total | 0.969 | 0.965 | 0.966 | 97 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-3 | game_total | 0.973 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-9 | game_total | 0.215 | 0.205 | 0.207 | 21 | 80 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI4 | team_total | 0.234 | 0.245 | 0.243 | 25 | 76 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-8 | game_total | 0.246 | 0.235 | 0.237 | 24 | 77 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL6 | team_total | 0.139 | 0.145 | 0.144 | 15 | 86 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-4 | game_total | 0.869 | 0.875 | 0.874 | 88 | 13 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI6 | team_total | 0.035 | 0.035 | 0.035 | 4 | 97 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-10 | game_total | 0.099 | 0.095 | 0.096 | 10 | 91 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT3 | team_total | 0.717 | 0.705 | 0.707 | 71 | 30 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ2 | team_total | 0.775 | 0.760 | 0.763 | 77 | 25 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ3 | team_total | 0.549 | 0.535 | 0.538 | 54 | 47 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-9 | game_total | 0.203 | 0.195 | 0.197 | 20 | 81 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-WPG3 | game_spread | 0.111 | 0.115 | 0.114 | 12 | 89 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI5 | team_total | 0.102 | 0.105 | 0.104 | 11 | 90 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-4 | game_total | 0.850 | 0.840 | 0.842 | 85 | 17 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-5 | game_total | 0.808 | 0.815 | 0.814 | 82 | 19 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-4 | game_total | 0.883 | 0.885 | 0.885 | 89 | 12 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT05SJDAL-SJ3 | game_spread | 0.117 | 0.115 | 0.115 | 12 | 89 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-PIT3 | game_spread | 0.267 | 0.275 | 0.273 | 28 | 73 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-WPG5 | team_total | 0.169 | 0.165 | 0.166 | 17 | 84 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT2 | team_total | 0.875 | 0.870 | 0.871 | 88 | 14 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT6 | team_total | 0.157 | 0.150 | 0.151 | 16 | 86 |  | -0.013 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ TBL | 0.613 | 0.578 | 0.182 | 0.228 | 5.51 | 5.80 | 0.951/0.994 | KXNHLTEAMTOTAL-26OCT05PHITB-PHI3 +0.067 |
| OTT @ BOS | 0.591 | 0.502 | 0.175 | 0.225 | 6.10 | 6.01 | 0.955/0.968 | KXNHLSPREAD-26OCT05OTTBOS-BOS2 -0.091 |
| WPG @ PIT | 0.620 | 0.628 | 0.166 | 0.206 | 6.52 | 6.47 | 1.012/0.997 | KXNHLSPREAD-26OCT05WPGPIT-PIT3 +0.018 |
| SJS @ DAL | 0.595 | 0.553 | 0.173 | 0.220 | 6.37 | 6.26 | 0.993/1.039 | KXNHLSPREAD-26OCT05SJDAL-DAL2 -0.054 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Sean Couturier: 1+ goals YES @ 10c · p 0.1577 (adj 0.1408) · $7.63 · thesis PHI:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 52c · p 0.722 (adj 0.5842) · $18.82 · thesis TBL:SUPPRESSED
- Tampa Bay wins by over 2.5 goals NO @ 69c · p 0.7826 (adj 0.7338) · $14.73 · thesis GAME:TIGHT
- Nikita Kucherov: 1+ assists NO @ 35c · p 0.4753 (adj 0.3906) · $5.88 · thesis TBL:SUPPRESSED
- Marat Khusnutdinov: 1+ goals YES @ 9c · p 0.1514 (adj 0.1348) · $8.89 · thesis BOS:OFFENSE_4PLUS
- Hayden Hodgson: 1+ goals YES @ 6c · p 0.1003 (adj 0.0877) · $5.06 · thesis OTT:OFFENSE_4PLUS
- Nick Cousins: 1+ goals YES @ 7c · p 0.1098 (adj 0.0986) · $5.47 · thesis OTT:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1901 (adj 0.1763) · $7.26 · thesis BOS:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 14c · p 0.1977 (adj 0.182) · $8.55 · thesis PIT:OFFENSE_4PLUS
- Morgan Barron: 1+ goals YES @ 10c · p 0.133 (adj 0.1235) · $4.27 · thesis WPG:OFFENSE_4PLUS
- Ben Kindel: 1+ goals NO @ 77c · p 0.8032 (adj 0.7936) · $12.86 · thesis PIT:SUPPRESSED
- Egor Chinakhov: 1+ assists YES @ 32c · p 0.3823 (adj 0.3461) · $3.54 · thesis PIT:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 67c · p 0.7288 (adj 0.7128) · $16.61 · thesis DAL:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 69c · p 0.8122 (adj 0.7263) · $16.61 · thesis SJS:SUPPRESSED
- Jason Robertson: 1+ goals NO @ 58c · p 0.6313 (adj 0.6172) · $10.18 · thesis DAL:SUPPRESSED
- Igor Chernyshov: 1+ goals YES @ 18c · p 0.215 (adj 0.205) · $3.64 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ TBL** · priced 122/132 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 23.71, exp saves 20.81 (sd 5.7), pull risk 0.041
- PHI net: Dan Vladar (CONFIRMED) exp shots 28.33, exp saves 24.37 (sd 6.7), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andrei Vasilevskiy: 21+ saves | 0.505 | 0.290 | 53/95 | -0.042 |  |
| John Carlson: 1+ assists | 0.278 | 0.490 | 50/52 | +0.185 | STANDARD |
| John Carlson: 1+ points | 0.364 | 0.560 | 57/45 | +0.169 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.525 | 0.655 | 66/35 | +0.109 | STANDARD |
| John Carlson: 2+ points | 0.078 | 0.205 | 21/80 | +0.111 | STANDARD |
| John Carlson: 2+ assists | 0.045 | 0.150 | 16/86 | +0.087 | STANDARD |

**OTT @ BOS** · priced 134/138 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 29.37, exp saves 25.61 (sd 6.88), pull risk 0.055
- OTT net: Linus Ullmark (CONFIRMED) exp shots 25.52, exp saves 22.1 (sd 6.17), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.159 | 0.340 | 35/67 | +0.156 | STANDARD |
| William Eklund: 1+ points | 0.341 | 0.485 | 50/53 | +0.111 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.247 | 0.370 | 38/64 | +0.097 | PRIOR_HEAVY |
| JJ Peterka: 1+ points | 0.393 | 0.505 | 51/50 | +0.089 | STANDARD |
| JJ Peterka: 1+ assists | 0.215 | 0.315 | 32/69 | +0.080 | STANDARD |
| Jeremy Swayman: 26+ saves | 0.502 | 0.410 | 48/66 | +0.004 |  |

**WPG @ PIT** · priced 125/128 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (CONFIRMED) exp shots 25.59, exp saves 22.42 (sd 6.15), pull risk 0.052
- WPG net: Clay Stevenson (CONFIRMED) exp shots 28.46, exp saves 24.09 (sd 6.75), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mark Scheifele: 1+ assists | 0.427 | 0.515 | 52/49 | +0.065 | STANDARD |
| Sidney Crosby: 1+ assists | 0.439 | 0.525 | 53/48 | +0.063 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.382 | 0.310 | 32/70 | +0.047 | STANDARD |
| Josh Morrissey: 1+ assists | 0.374 | 0.440 | 45/57 | +0.039 | STANDARD |
| Sidney Crosby: 2+ points | 0.260 | 0.325 | 34/69 | +0.035 | STANDARD |
| Connor Dewar: 1+ goals | 0.198 | 0.135 | 14/87 | +0.049 | STANDARD |

**SJS @ DAL** · priced 132/134 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.83, exp saves 21.63 (sd 6.07), pull risk 0.052
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.49, exp saves 23.67 (sd 6.46), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.274 | 0.410 | 42/60 | +0.109 | STANDARD |
| Mason Marchment: 1+ assists | 0.188 | 0.320 | 33/69 | +0.107 | STANDARD |
| Mikko Rantanen: 2+ points | 0.215 | 0.330 | 34/68 | +0.089 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.419 | 0.525 | 53/48 | +0.083 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.145 | 0.250 | 26/76 | +0.082 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ points | 0.267 | 0.370 | 38/64 | +0.077 | PRIOR_HEAVY |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
