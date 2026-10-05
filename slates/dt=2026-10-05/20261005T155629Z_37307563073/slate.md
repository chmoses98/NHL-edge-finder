# NHL slate 2026-10-05 — RESEARCH_ONLY

generated 2026-10-05T15:56:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2828 · contracts joined: 730 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 630, 'OK': 46, 'NO_EDGE': 54}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 105, 'game_early_goal': 4, 'first_goal': 142, 'game_winner': 8, 'player_goals': 142, 'game_overtime': 4, 'player_points': 137, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ TBL | 2026-10-05T23:00:00Z | T-6h | 0.638 | 0.362 | 0.174 | 5.75 | 3.29 | 2.46 | 181 (25/156) | PROJECTED/PROJECTED |
| OTT @ BOS | 2026-10-05T23:30:00Z | T-6h | 0.585 | 0.415 | 0.174 | 6.05 | 3.29 | 2.76 | 188 (25/163) | CONFIRMED/PROJECTED |
| WPG @ PIT | 2026-10-05T23:30:00Z | T-6h | 0.623 | 0.377 | 0.168 | 6.49 | 3.65 | 2.85 | 177 (25/152) | PROBABLE/CONFIRMED |
| SJS @ DAL | 2026-10-06T00:00:00Z | T-6h | 0.580 | 0.420 | 0.176 | 6.31 | 3.41 | 2.90 | 184 (25/159) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT05OTTBOS-BOS | game_winner | 0.585 | 0.465 | 0.489 | 47 | 54 | yes | +0.098 | OK |
| KXNHLGAME-26OCT05OTTBOS-OTT | game_winner | 0.415 | 0.525 | 0.503 | 53 | 48 | no | +0.088 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-BOS2 | game_spread | 0.356 | 0.265 | 0.282 | 27 | 74 | yes | +0.073 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-OTT2 | game_spread | 0.214 | 0.295 | 0.277 | 30 | 71 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT3 | team_total | 0.525 | 0.610 | 0.593 | 62 | 40 | no | +0.058 | OK |
| KXNHLGAME-26OCT05SJDAL-SJ | game_winner | 0.420 | 0.345 | 0.360 | 35 | 66 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT4 | team_total | 0.310 | 0.390 | 0.373 | 40 | 62 | no | +0.054 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-OTT3 | game_spread | 0.120 | 0.185 | 0.170 | 19 | 82 | no | +0.049 | OK |
| KXNHLGAME-26OCT05SJDAL-DAL | game_winner | 0.580 | 0.645 | 0.632 | 65 | 36 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT05PHITB-TB3 | game_spread | 0.253 | 0.315 | 0.302 | 32 | 69 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT2 | team_total | 0.759 | 0.815 | 0.805 | 82 | 19 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS3 | team_total | 0.643 | 0.585 | 0.597 | 59 | 42 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4 | team_total | 0.457 | 0.515 | 0.503 | 52 | 49 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-BOS3 | game_spread | 0.226 | 0.175 | 0.184 | 18 | 83 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT05SJDAL-DAL2 | game_spread | 0.359 | 0.415 | 0.404 | 42 | 59 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS4 | team_total | 0.429 | 0.365 | 0.378 | 38 | 65 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB4 | team_total | 0.431 | 0.490 | 0.478 | 50 | 52 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT5 | team_total | 0.149 | 0.200 | 0.189 | 21 | 81 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS5 | team_total | 0.241 | 0.190 | 0.200 | 20 | 82 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT05PHITB-5 | game_total | 0.709 | 0.760 | 0.750 | 77 | 25 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT05PHITB-6 | game_total | 0.486 | 0.535 | 0.525 | 54 | 47 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL3 | team_total | 0.671 | 0.715 | 0.707 | 72 | 29 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT05SJDAL-DAL3 | game_spread | 0.232 | 0.275 | 0.266 | 28 | 73 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT05PHITB-7 | game_total | 0.370 | 0.415 | 0.406 | 42 | 59 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB5 | team_total | 0.234 | 0.275 | 0.266 | 28 | 73 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT05PHITB-TB2 | game_spread | 0.401 | 0.445 | 0.436 | 45 | 56 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL5 | team_total | 0.264 | 0.305 | 0.296 | 31 | 70 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT05SJDAL-SJ2 | game_spread | 0.221 | 0.185 | 0.192 | 19 | 82 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ4 | team_total | 0.345 | 0.305 | 0.313 | 31 | 70 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS6 | team_total | 0.116 | 0.075 | 0.082 | 9 | 94 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB3 | team_total | 0.656 | 0.700 | 0.691 | 71 | 31 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT05PHITB-4 | game_total | 0.813 | 0.845 | 0.839 | 85 | 16 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL2 | team_total | 0.849 | 0.880 | 0.874 | 89 | 13 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS2 | team_total | 0.833 | 0.800 | 0.807 | 81 | 21 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB2 | team_total | 0.839 | 0.875 | 0.868 | 89 | 14 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT05PHITB-8 | game_total | 0.197 | 0.225 | 0.219 | 23 | 78 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT05PHITB-3 | game_total | 0.949 | 0.965 | 0.962 | 97 | 4 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB6 | team_total | 0.105 | 0.130 | 0.125 | 14 | 88 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT05PHITB-9 | game_total | 0.134 | 0.155 | 0.151 | 16 | 85 | no | +0.007 | OK |
| KXNHLGAME-26OCT05PHITB-TB | game_winner | 0.638 | 0.665 | 0.660 | 67 | 34 | no | +0.007 | OK |
| KXNHLGAME-26OCT05PHITB-PHI | game_winner | 0.362 | 0.335 | 0.340 | 34 | 67 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT6 | team_total | 0.059 | 0.080 | 0.075 | 9 | 93 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT05SJDAL-5 | game_total | 0.783 | 0.805 | 0.801 | 81 | 20 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ5 | team_total | 0.175 | 0.155 | 0.159 | 16 | 85 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL6 | team_total | 0.130 | 0.145 | 0.142 | 15 | 86 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT05WPGPIT-10 | game_total | 0.107 | 0.095 | 0.097 | 10 | 91 | yes | +0.001 | OK |
| KXNHLSPREAD-26OCT05WPGPIT-WPG3 | game_spread | 0.103 | 0.115 | 0.113 | 12 | 89 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ3 | team_total | 0.557 | 0.535 | 0.539 | 54 | 47 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-3 | game_total | 0.958 | 0.965 | 0.964 | 97 | 4 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT05PHITB-10 | game_total | 0.057 | 0.070 | 0.067 | 8 | 94 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-4 | game_total | 0.864 | 0.875 | 0.873 | 88 | 13 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT6 | team_total | 0.156 | 0.145 | 0.147 | 15 | 86 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-3 | game_total | 0.969 | 0.965 | 0.966 | 97 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT5 | team_total | 0.312 | 0.295 | 0.298 | 30 | 71 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-6 | game_total | 0.577 | 0.600 | 0.595 | 61 | 41 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-4 | game_total | 0.877 | 0.885 | 0.883 | 89 | 12 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT05PHITB-PHI3 | game_spread | 0.088 | 0.095 | 0.094 | 10 | 91 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT05SJDAL-SJ3 | game_spread | 0.123 | 0.115 | 0.117 | 12 | 89 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-5 | game_total | 0.805 | 0.815 | 0.813 | 82 | 19 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-3 | game_total | 0.966 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-9 | game_total | 0.215 | 0.205 | 0.207 | 21 | 80 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-2 | game_total | 0.986 | 0.990 | 0.989 |  | 2 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT05PHITB-PHI2 | game_spread | 0.172 | 0.165 | 0.166 | 17 | 84 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ2 | team_total | 0.775 | 0.760 | 0.763 | 77 | 25 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-5 | game_total | 0.755 | 0.765 | 0.763 | 77 | 24 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI2 | team_total | 0.693 | 0.705 | 0.703 | 71 | 30 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-PIT3 | game_spread | 0.265 | 0.275 | 0.273 | 28 | 73 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT3 | team_total | 0.715 | 0.705 | 0.707 | 71 | 30 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT05PHITB-2 | game_total | 0.977 | 0.980 | 0.980 | 99 | 3 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-4 | game_total | 0.840 | 0.845 | 0.844 | 85 | 16 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-10 | game_total | 0.094 | 0.095 | 0.095 | 10 | 91 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI6 | team_total | 0.038 | 0.040 | 0.040 | 5 | 97 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-10 | game_total | 0.075 | 0.070 | 0.071 | 8 | 94 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-8 | game_total | 0.276 | 0.285 | 0.283 | 29 | 72 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT2 | team_total | 0.877 | 0.875 | 0.875 | 88 | 13 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-8 | game_total | 0.304 | 0.295 | 0.297 | 30 | 71 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ6 | team_total | 0.073 | 0.065 | 0.066 | 8 | 95 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-WPG2 | team_total | 0.770 | 0.780 | 0.778 | 79 | 23 |  | -0.012 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ TBL | 0.638 | 0.573 | 0.174 | 0.216 | 5.75 | 5.80 | 0.957/0.991 | KXNHLGAME-26OCT05PHITB-PHI +0.064 |
| OTT @ BOS | 0.585 | 0.516 | 0.174 | 0.222 | 6.05 | 6.07 | 0.955/0.998 | KXNHLGAME-26OCT05OTTBOS-OTT +0.069 |
| WPG @ PIT | 0.623 | 0.628 | 0.168 | 0.205 | 6.49 | 6.47 | 1.016/0.997 | KXNHLSPREAD-26OCT05WPGPIT-PIT3 +0.017 |
| SJS @ DAL | 0.580 | 0.554 | 0.176 | 0.213 | 6.31 | 6.21 | 0.986/1.034 | KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4 -0.031 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- John Carlson: 1+ assists NO @ 52c · p 0.7242 (adj 0.585) · $14.33 · thesis TBL:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 11c · p 0.1563 (adj 0.1422) · $4.35 · thesis PHI:OFFENSE_4PLUS
- Porter Martone: 1+ goals NO @ 79c · p 0.8377 (adj 0.8245) · $14.33 · thesis PHI:SUPPRESSED
- Tampa Bay over 4.5 goals scored NO @ 73c · p 0.7955 (adj 0.7602) · $7.98 · thesis TBL:SUPPRESSED
- William Eklund: 1+ assists NO @ 67c · p 0.8362 (adj 0.7249) · $16.4 · thesis OTT:SUPPRESSED
- Marat Khusnutdinov: 1+ goals YES @ 11c · p 0.1533 (adj 0.14) · $5.04 · thesis BOS:OFFENSE_4PLUS
- JJ Peterka: 1+ assists NO @ 69c · p 0.7821 (adj 0.7336) · $16.4 · thesis BOS:SUPPRESSED
- Nick Cousins: 1+ goals YES @ 9c · p 0.1148 (adj 0.1061) · $2.28 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 14c · p 0.1873 (adj 0.1742) · $5.73 · thesis PIT:OFFENSE_4PLUS
- Isak Rosen: 1+ goals NO @ 87c · p 0.8964 (adj 0.8885) · $16.4 · thesis WPG:SUPPRESSED
- Blake Lizotte: 1+ goals YES @ 12c · p 0.1469 (adj 0.1377) · $2.22 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 33c · p 0.3675 (adj 0.3569) · $3.54 · thesis PIT:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 14c · p 0.1898 (adj 0.1761) · $5.46 · thesis SJS:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 67c · p 0.726 (adj 0.7107) · $14.83 · thesis DAL:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 69c · p 0.8172 (adj 0.728) · $14.9 · thesis SJS:SUPPRESSED
- Jason Robertson: 1+ goals NO @ 59c · p 0.6319 (adj 0.6189) · $5.81 · thesis DAL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ TBL** · priced 122/130 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 23.71, exp saves 20.84 (sd 5.75), pull risk 0.04
- PHI net: Joseph Woll (PROJECTED) exp shots 28.33, exp saves 24.32 (sd 6.61), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.276 | 0.490 | 50/52 | +0.187 | STANDARD |
| John Carlson: 1+ points | 0.360 | 0.560 | 57/45 | +0.173 | STANDARD |
| John Carlson: 2+ points | 0.075 | 0.210 | 22/80 | +0.114 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.515 | 0.635 | 64/37 | +0.098 | STANDARD |
| John Carlson: 2+ assists | 0.041 | 0.155 | 17/86 | +0.091 | STANDARD |
| Nikita Kucherov: 2+ points | 0.338 | 0.450 | 46/56 | +0.085 | STANDARD |

**OTT @ BOS** · priced 131/137 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 29.37, exp saves 25.58 (sd 6.8), pull risk 0.057
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.52, exp saves 22.01 (sd 6.19), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.164 | 0.335 | 34/67 | +0.151 | STANDARD |
| William Eklund: 1+ points | 0.349 | 0.490 | 50/52 | +0.114 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.239 | 0.345 | 35/66 | +0.085 | PRIOR_HEAVY |
| JJ Peterka: 1+ points | 0.396 | 0.500 | 51/51 | +0.076 | STANDARD |
| JJ Peterka: 1+ assists | 0.218 | 0.315 | 32/69 | +0.077 | STANDARD |
| Tim Stutzle: 1+ assists | 0.386 | 0.480 | 49/53 | +0.066 | STANDARD |

**WPG @ PIT** · priced 124/126 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (PROBABLE) exp shots 25.59, exp saves 22.42 (sd 6.11), pull risk 0.051
- WPG net: Clay Stevenson (CONFIRMED) exp shots 28.46, exp saves 24.04 (sd 6.85), pull risk 0.09

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Egor Chinakhov: 2+ points | 0.184 | 0.095 | 17/98 | +0.004 | STANDARD |
| Mark Scheifele: 1+ assists | 0.429 | 0.515 | 52/49 | +0.064 | STANDARD |
| Sidney Crosby: 1+ assists | 0.443 | 0.525 | 53/48 | +0.060 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.391 | 0.315 | 33/70 | +0.045 | STANDARD |
| Thomas Novak: 1+ goals | 0.224 | 0.150 | 22/92 | -0.008 | STANDARD |
| Rickard Rakell: 1+ points | 0.631 | 0.570 | 58/44 | +0.034 | STANDARD |

**SJS @ DAL** · priced 133/133 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.83, exp saves 21.65 (sd 6.02), pull risk 0.053
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.49, exp saves 23.66 (sd 6.53), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason Marchment: 1+ assists | 0.183 | 0.320 | 33/69 | +0.112 | STANDARD |
| Roope Hintz: 1+ assists | 0.274 | 0.405 | 41/60 | +0.110 | STANDARD |
| Mikko Rantanen: 2+ points | 0.214 | 0.330 | 34/68 | +0.090 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.150 | 0.265 | 28/75 | +0.087 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ points | 0.273 | 0.370 | 38/64 | +0.071 | PRIOR_HEAVY |
| Mikko Rantanen: 1+ assists | 0.421 | 0.515 | 52/49 | +0.071 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
