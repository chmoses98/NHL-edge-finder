# NHL slate 2026-10-05 — RESEARCH_ONLY

generated 2026-10-05T14:56:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2820 · contracts joined: 730 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 630, 'OK': 41, 'NO_EDGE': 59}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 105, 'game_early_goal': 4, 'first_goal': 142, 'game_winner': 8, 'player_goals': 142, 'game_overtime': 4, 'player_points': 137, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ TBL | 2026-10-05T23:00:00Z | T-6h | 0.638 | 0.362 | 0.174 | 5.75 | 3.29 | 2.46 | 181 (25/156) | PROJECTED/PROJECTED |
| OTT @ BOS | 2026-10-05T23:30:00Z | T-6h | 0.564 | 0.436 | 0.175 | 6.16 | 3.29 | 2.88 | 188 (25/163) | PROJECTED/PROJECTED |
| WPG @ PIT | 2026-10-05T23:30:00Z | T-6h | 0.628 | 0.372 | 0.165 | 6.47 | 3.65 | 2.83 | 177 (25/152) | PROJECTED/CONFIRMED |
| SJS @ DAL | 2026-10-06T00:00:00Z | T-6h | 0.580 | 0.420 | 0.176 | 6.31 | 3.41 | 2.90 | 184 (25/159) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT05OTTBOS-BOS | game_winner | 0.564 | 0.465 | 0.485 | 47 | 54 | yes | +0.077 | OK |
| KXNHLGAME-26OCT05OTTBOS-OTT | game_winner | 0.436 | 0.525 | 0.507 | 53 | 48 | no | +0.067 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-BOS2 | game_spread | 0.343 | 0.275 | 0.288 | 28 | 73 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS4 | team_total | 0.432 | 0.360 | 0.374 | 37 | 65 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-OTT2 | game_spread | 0.233 | 0.295 | 0.282 | 30 | 71 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB4 | team_total | 0.431 | 0.495 | 0.482 | 50 | 51 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS5 | team_total | 0.241 | 0.185 | 0.195 | 19 | 82 | yes | +0.040 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-OTT3 | game_spread | 0.131 | 0.185 | 0.173 | 19 | 82 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS3 | team_total | 0.642 | 0.580 | 0.593 | 59 | 43 | yes | +0.035 | OK |
| KXNHLGAME-26OCT05SJDAL-DAL | game_winner | 0.580 | 0.635 | 0.624 | 64 | 37 | no | +0.034 | OK |
| KXNHLGAME-26OCT05SJDAL-SJ | game_winner | 0.420 | 0.365 | 0.376 | 37 | 64 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT05PHITB-TB3 | game_spread | 0.253 | 0.305 | 0.294 | 31 | 70 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT4 | team_total | 0.335 | 0.385 | 0.375 | 39 | 62 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT05PHITB-5 | game_total | 0.709 | 0.760 | 0.750 | 77 | 25 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT05PHITB-6 | game_total | 0.486 | 0.535 | 0.525 | 54 | 47 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-BOS3 | game_spread | 0.216 | 0.175 | 0.183 | 18 | 83 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT2 | team_total | 0.775 | 0.815 | 0.807 | 82 | 19 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT05PHITB-7 | game_total | 0.370 | 0.415 | 0.406 | 42 | 59 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB2 | team_total | 0.839 | 0.875 | 0.868 | 88 | 13 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB5 | team_total | 0.234 | 0.280 | 0.270 | 29 | 73 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT05PHITB-TB2 | game_spread | 0.401 | 0.445 | 0.436 | 45 | 56 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB3 | team_total | 0.656 | 0.700 | 0.691 | 71 | 31 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS6 | team_total | 0.114 | 0.075 | 0.082 | 9 | 94 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT05PHITB-4 | game_total | 0.813 | 0.845 | 0.839 | 85 | 16 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT3 | team_total | 0.556 | 0.600 | 0.591 | 61 | 41 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4 | team_total | 0.457 | 0.495 | 0.487 | 50 | 51 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT05SJDAL-DAL3 | game_spread | 0.232 | 0.265 | 0.258 | 27 | 74 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL3 | team_total | 0.671 | 0.705 | 0.698 | 71 | 30 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL2 | team_total | 0.849 | 0.880 | 0.874 | 89 | 13 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT5 | team_total | 0.167 | 0.195 | 0.189 | 20 | 81 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS2 | team_total | 0.833 | 0.800 | 0.807 | 81 | 21 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT05PHITB-8 | game_total | 0.197 | 0.225 | 0.219 | 23 | 78 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT05PHITB-3 | game_total | 0.949 | 0.965 | 0.962 | 97 | 4 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB6 | team_total | 0.105 | 0.130 | 0.125 | 14 | 88 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT05PHITB-9 | game_total | 0.134 | 0.155 | 0.151 | 16 | 85 | no | +0.007 | OK |
| KXNHLGAME-26OCT05PHITB-TB | game_winner | 0.638 | 0.665 | 0.660 | 67 | 34 | no | +0.007 | OK |
| KXNHLGAME-26OCT05PHITB-PHI | game_winner | 0.362 | 0.335 | 0.340 | 34 | 67 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT05OTTBOS-10 | game_total | 0.081 | 0.065 | 0.068 | 7 | 94 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT05SJDAL-5 | game_total | 0.783 | 0.805 | 0.801 | 81 | 20 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT05SJDAL-DAL2 | game_spread | 0.359 | 0.385 | 0.380 | 39 | 62 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL5 | team_total | 0.264 | 0.285 | 0.281 | 29 | 72 | no | +0.002 | OK |
| KXNHLSPREAD-26OCT05SJDAL-SJ2 | game_spread | 0.221 | 0.205 | 0.208 | 21 | 80 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-10 | game_total | 0.106 | 0.095 | 0.097 | 10 | 91 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ3 | team_total | 0.557 | 0.535 | 0.539 | 54 | 47 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT05PHITB-10 | game_total | 0.057 | 0.070 | 0.067 | 8 | 94 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ4 | team_total | 0.345 | 0.325 | 0.329 | 33 | 68 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-8 | game_total | 0.252 | 0.235 | 0.238 | 24 | 77 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-6 | game_total | 0.556 | 0.535 | 0.539 | 54 | 47 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-WPG3 | game_spread | 0.105 | 0.115 | 0.113 | 12 | 89 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-3 | game_total | 0.970 | 0.965 | 0.966 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-9 | game_total | 0.178 | 0.160 | 0.164 | 17 | 85 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-4 | game_total | 0.864 | 0.875 | 0.873 | 88 | 13 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-6 | game_total | 0.577 | 0.595 | 0.591 | 60 | 41 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT05PHITB-PHI3 | game_spread | 0.088 | 0.095 | 0.094 | 10 | 91 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-7 | game_total | 0.442 | 0.425 | 0.428 | 43 | 58 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT6 | team_total | 0.071 | 0.080 | 0.078 | 9 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ5 | team_total | 0.175 | 0.160 | 0.163 | 17 | 85 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-3 | game_total | 0.963 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-3 | game_total | 0.966 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-4 | game_total | 0.879 | 0.885 | 0.884 | 89 | 12 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT3 | team_total | 0.717 | 0.700 | 0.704 | 71 | 31 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT05PHITB-PHI2 | game_spread | 0.172 | 0.165 | 0.166 | 17 | 84 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-4 | game_total | 0.851 | 0.845 | 0.846 | 85 | 16 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI2 | team_total | 0.693 | 0.705 | 0.703 | 71 | 30 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL6 | team_total | 0.130 | 0.140 | 0.138 | 15 | 87 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-WPG2 | team_total | 0.767 | 0.780 | 0.777 | 79 | 23 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT05PHITB-2 | game_total | 0.977 | 0.980 | 0.980 | 99 | 3 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-10 | game_total | 0.094 | 0.095 | 0.095 | 10 | 91 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI6 | team_total | 0.038 | 0.040 | 0.040 | 5 | 97 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-PIT2 | game_spread | 0.407 | 0.395 | 0.397 | 40 | 61 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-8 | game_total | 0.276 | 0.285 | 0.283 | 29 | 72 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT05SJDAL-SJ3 | game_spread | 0.123 | 0.125 | 0.125 | 13 | 88 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-PIT3 | game_spread | 0.267 | 0.275 | 0.273 | 28 | 73 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-WPG2 | game_spread | 0.190 | 0.195 | 0.194 | 20 | 81 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-9 | game_total | 0.211 | 0.205 | 0.206 | 21 | 80 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ6 | team_total | 0.073 | 0.065 | 0.066 | 8 | 95 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-WPG6 | team_total | 0.069 | 0.070 | 0.070 | 8 | 94 |  | -0.013 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ TBL | 0.638 | 0.573 | 0.174 | 0.216 | 5.75 | 5.80 | 0.957/0.991 | KXNHLGAME-26OCT05PHITB-PHI +0.064 |
| OTT @ BOS | 0.564 | 0.513 | 0.175 | 0.222 | 6.16 | 6.11 | 0.968/0.998 | KXNHLSPREAD-26OCT05OTTBOS-BOS2 -0.056 |
| WPG @ PIT | 0.628 | 0.625 | 0.165 | 0.204 | 6.47 | 6.48 | 1.021/0.997 | KXNHLSPREAD-26OCT05WPGPIT-PIT3 +0.014 |
| SJS @ DAL | 0.580 | 0.554 | 0.176 | 0.213 | 6.31 | 6.21 | 0.986/1.034 | KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4 -0.031 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 14 recommended · full analysis in card.md / packet.json `thesis_card`

- John Carlson: 1+ assists NO @ 53c · p 0.7242 (adj 0.5882) · $20.0 · thesis TBL:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 11c · p 0.1563 (adj 0.1422) · $5.99 · thesis PHI:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 70c · p 0.7884 (adj 0.7417) · $17.25 · thesis GAME:TIGHT
- Christian Dvorak: 1+ goals YES @ 16c · p 0.1947 (adj 0.1835) · $3.61 · thesis PHI:OFFENSE_4PLUS
- Carter Yakemchuk: 1+ goals NO @ 88c · p 0.9322 (adj 0.9166) · $18.9 · thesis OTT:SUPPRESSED
- Marat Khusnutdinov: 1+ goals YES @ 11c · p 0.1436 (adj 0.1327) · $4.09 · thesis BOS:OFFENSE_4PLUS
- Tim Stutzle: 1+ assists NO @ 53c · p 0.6177 (adj 0.5689) · $11.1 · thesis OTT:SUPPRESSED
- Jordan Spence: 1+ assists YES @ 28c · p 0.3438 (adj 0.3069) · $4.55 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 14c · p 0.1867 (adj 0.1738) · $6.91 · thesis PIT:WINS_BY_2PLUS
- Filip Hallander: 1+ goals YES @ 14c · p 0.1827 (adj 0.1683) · $5.29 · thesis PIT:OFFENSE_4PLUS
- Alex Iafallo: 1+ goals YES @ 12c · p 0.1459 (adj 0.1382) · $2.98 · thesis WPG:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 14c · p 0.1898 (adj 0.1761) · $7.7 · thesis SJS:OFFENSE_4PLUS
- Jason Robertson: 1+ goals NO @ 56c · p 0.6319 (adj 0.6127) · $20.0 · thesis DAL:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 69c · p 0.8172 (adj 0.7248) · $20.0 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ TBL** · priced 122/130 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 23.71, exp saves 20.84 (sd 5.75), pull risk 0.04
- PHI net: Joseph Woll (PROJECTED) exp shots 28.33, exp saves 24.32 (sd 6.61), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.276 | 0.485 | 50/53 | +0.177 | STANDARD |
| John Carlson: 1+ points | 0.360 | 0.555 | 57/46 | +0.163 | STANDARD |
| John Carlson: 2+ points | 0.075 | 0.205 | 22/81 | +0.104 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.515 | 0.625 | 64/39 | +0.078 | STANDARD |
| John Carlson: 2+ assists | 0.041 | 0.145 | 16/87 | +0.081 | STANDARD |
| Nikita Kucherov: 2+ points | 0.338 | 0.435 | 45/58 | +0.065 | STANDARD |

**OTT @ BOS** · priced 135/137 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.37, exp saves 25.51 (sd 6.9), pull risk 0.059
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.52, exp saves 21.99 (sd 6.15), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.170 | 0.330 | 35/69 | +0.125 | STANDARD |
| William Eklund: 1+ points | 0.354 | 0.485 | 50/53 | +0.098 | STANDARD |
| JJ Peterka: 1+ points | 0.381 | 0.505 | 52/51 | +0.091 | STANDARD |
| JJ Peterka: 1+ assists | 0.200 | 0.315 | 33/70 | +0.086 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.242 | 0.345 | 35/66 | +0.083 | PRIOR_HEAVY |
| Tim Stutzle: 1+ assists | 0.382 | 0.480 | 49/53 | +0.070 | STANDARD |

**WPG @ PIT** · priced 126/126 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (PROJECTED) exp shots 25.59, exp saves 22.46 (sd 6.16), pull risk 0.049
- WPG net: Clay Stevenson (CONFIRMED) exp shots 28.46, exp saves 24.1 (sd 6.81), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Thomas Novak: 1+ goals | 0.222 | 0.130 | 24/98 | -0.031 | STANDARD |
| Mark Scheifele: 1+ assists | 0.430 | 0.520 | 53/49 | +0.062 | STANDARD |
| Sidney Crosby: 1+ assists | 0.439 | 0.520 | 53/49 | +0.054 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.385 | 0.305 | 32/71 | +0.050 | STANDARD |
| Sidney Crosby: 2+ points | 0.253 | 0.320 | 33/69 | +0.042 | STANDARD |
| Josh Morrissey: 1+ assists | 0.383 | 0.445 | 46/57 | +0.030 | STANDARD |

**SJS @ DAL** · priced 133/133 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.83, exp saves 21.65 (sd 6.02), pull risk 0.053
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.49, exp saves 23.66 (sd 6.53), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason Marchment: 1+ assists | 0.183 | 0.325 | 34/69 | +0.112 | STANDARD |
| Roope Hintz: 1+ assists | 0.274 | 0.400 | 41/61 | +0.100 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.150 | 0.270 | 28/74 | +0.097 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ points | 0.273 | 0.380 | 39/63 | +0.080 | PRIOR_HEAVY |
| Mikko Rantanen: 1+ assists | 0.421 | 0.510 | 52/50 | +0.061 | STANDARD |
| Roope Hintz: 1+ points | 0.477 | 0.565 | 58/45 | +0.056 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
