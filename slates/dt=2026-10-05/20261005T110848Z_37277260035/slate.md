# NHL slate 2026-10-05 — RESEARCH_ONLY

generated 2026-10-05T11:08:48Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2424 · contracts joined: 334 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 234, 'NO_EDGE': 62, 'OK': 38}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 25, 'game_early_goal': 4, 'first_goal': 36, 'game_winner': 8, 'player_goals': 36, 'game_overtime': 4, 'player_points': 33, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ TBL | 2026-10-05T23:00:00Z | T-6h | 0.638 | 0.362 | 0.174 | 5.75 | 3.29 | 2.46 | 181 (25/156) | PROJECTED/PROJECTED |
| OTT @ BOS | 2026-10-05T23:30:00Z | T-12h | 0.564 | 0.436 | 0.175 | 6.16 | 3.29 | 2.88 | 51 (25/26) | PROJECTED/PROJECTED |
| WPG @ PIT | 2026-10-05T23:30:00Z | T-12h | 0.628 | 0.372 | 0.165 | 6.47 | 3.65 | 2.83 | 51 (25/26) | PROJECTED/CONFIRMED |
| SJS @ DAL | 2026-10-06T00:00:00Z | T-12h | 0.580 | 0.420 | 0.176 | 6.31 | 3.41 | 2.90 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT05OTTBOS-BOS | game_winner | 0.564 | 0.465 | 0.485 | 47 | 54 | yes | +0.077 | OK |
| KXNHLGAME-26OCT05OTTBOS-OTT | game_winner | 0.436 | 0.525 | 0.507 | 53 | 48 | no | +0.067 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-BOS2 | game_spread | 0.343 | 0.275 | 0.288 | 28 | 73 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-OTT2 | game_spread | 0.233 | 0.295 | 0.282 | 30 | 71 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT05PHITB-5 | game_total | 0.709 | 0.765 | 0.754 | 77 | 24 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-OTT3 | game_spread | 0.131 | 0.185 | 0.173 | 19 | 82 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT05PHITB-6 | game_total | 0.486 | 0.545 | 0.533 | 55 | 46 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS4 | team_total | 0.432 | 0.365 | 0.378 | 38 | 65 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS3 | team_total | 0.642 | 0.575 | 0.589 | 59 | 44 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS5 | team_total | 0.241 | 0.185 | 0.195 | 20 | 83 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT05OTTBOS-BOS3 | game_spread | 0.216 | 0.175 | 0.183 | 18 | 83 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT05PHITB-TB3 | game_spread | 0.253 | 0.295 | 0.286 | 30 | 71 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT05PHITB-7 | game_total | 0.370 | 0.415 | 0.406 | 42 | 59 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB4 | team_total | 0.431 | 0.485 | 0.474 | 50 | 53 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT05PHITB-8 | game_total | 0.197 | 0.235 | 0.227 | 24 | 77 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT4 | team_total | 0.335 | 0.385 | 0.375 | 40 | 63 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS6 | team_total | 0.114 | 0.080 | 0.086 | 9 | 93 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT05PHITB-4 | game_total | 0.813 | 0.845 | 0.839 | 85 | 16 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT3 | team_total | 0.556 | 0.605 | 0.595 | 62 | 41 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT05PHITB-9 | game_total | 0.134 | 0.165 | 0.158 | 17 | 84 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT05SJDAL-DAL3 | game_spread | 0.232 | 0.265 | 0.258 | 27 | 74 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT2 | team_total | 0.775 | 0.810 | 0.803 | 82 | 20 | no | +0.014 | OK |
| KXNHLGAME-26OCT05SJDAL-DAL | game_winner | 0.580 | 0.615 | 0.608 | 62 | 39 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB5 | team_total | 0.234 | 0.275 | 0.266 | 29 | 74 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT5 | team_total | 0.167 | 0.205 | 0.197 | 22 | 81 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB2 | team_total | 0.839 | 0.865 | 0.860 | 87 | 14 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-BOS2 | team_total | 0.833 | 0.795 | 0.803 | 81 | 22 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB3 | team_total | 0.656 | 0.690 | 0.683 | 70 | 32 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT05PHITB-3 | game_total | 0.949 | 0.965 | 0.962 | 97 | 4 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-TB6 | team_total | 0.105 | 0.130 | 0.125 | 14 | 88 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4 | team_total | 0.457 | 0.490 | 0.483 | 50 | 52 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT05SJDAL-5 | game_total | 0.783 | 0.805 | 0.801 | 81 | 20 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT05SJDAL-DAL2 | game_spread | 0.359 | 0.385 | 0.380 | 39 | 62 | no | +0.005 | OK |
| KXNHLGAME-26OCT05SJDAL-SJ | game_winner | 0.420 | 0.395 | 0.400 | 40 | 61 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL2 | team_total | 0.849 | 0.865 | 0.862 | 87 | 14 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI2 | team_total | 0.693 | 0.720 | 0.715 | 73 | 29 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL5 | team_total | 0.264 | 0.290 | 0.285 | 30 | 72 | no | +0.002 | OK |
| KXNHLSPREAD-26OCT05PHITB-TB2 | game_spread | 0.401 | 0.425 | 0.420 | 43 | 58 | no | +0.002 | OK |
| KXNHLSPREAD-26OCT05SJDAL-SJ2 | game_spread | 0.221 | 0.205 | 0.208 | 21 | 80 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-10 | game_total | 0.106 | 0.095 | 0.097 | 10 | 91 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT05PHITB-10 | game_total | 0.057 | 0.070 | 0.067 | 8 | 94 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-8 | game_total | 0.252 | 0.235 | 0.238 | 24 | 77 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-WPG2 | game_spread | 0.190 | 0.205 | 0.202 | 21 | 80 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-6 | game_total | 0.556 | 0.535 | 0.539 | 54 | 47 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-WPG3 | game_spread | 0.105 | 0.115 | 0.113 | 12 | 89 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-3 | game_total | 0.970 | 0.965 | 0.966 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-9 | game_total | 0.178 | 0.160 | 0.164 | 17 | 85 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-4 | game_total | 0.864 | 0.875 | 0.873 | 88 | 13 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-2 | game_total | 0.988 | 0.980 | 0.982 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-7 | game_total | 0.466 | 0.485 | 0.481 | 49 | 52 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26OCT05PHITB-TB | game_winner | 0.638 | 0.655 | 0.652 | 66 | 35 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT6 | team_total | 0.155 | 0.145 | 0.147 | 15 | 86 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT05PHITB-PHI3 | game_spread | 0.088 | 0.095 | 0.094 | 10 | 91 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-10 | game_total | 0.081 | 0.070 | 0.072 | 8 | 94 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-7 | game_total | 0.442 | 0.420 | 0.424 | 43 | 59 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05OTTBOS-OTT6 | team_total | 0.071 | 0.080 | 0.078 | 9 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-3 | game_total | 0.963 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-2 | game_total | 0.985 | 0.975 | 0.977 | 99 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-3 | game_total | 0.966 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL3 | team_total | 0.671 | 0.695 | 0.690 | 71 | 32 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT3 | team_total | 0.717 | 0.695 | 0.700 | 71 | 32 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI4 | team_total | 0.244 | 0.265 | 0.261 | 28 | 75 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT05PHITB-PHI2 | game_spread | 0.172 | 0.165 | 0.166 | 17 | 84 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT05OTTBOS-4 | game_total | 0.851 | 0.845 | 0.846 | 85 | 16 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-DAL6 | team_total | 0.130 | 0.140 | 0.138 | 15 | 87 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI3 | team_total | 0.451 | 0.475 | 0.470 | 49 | 54 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT05WPGPIT-PIT | game_winner | 0.628 | 0.615 | 0.618 | 62 | 39 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-WPG2 | team_total | 0.767 | 0.780 | 0.777 | 79 | 23 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT05SJDAL-10 | game_total | 0.094 | 0.095 | 0.095 | 10 | 91 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05PHITB-PHI6 | team_total | 0.038 | 0.045 | 0.043 | 6 | 97 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-PIT4 | team_total | 0.508 | 0.495 | 0.498 | 50 | 51 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT05WPGPIT-PIT2 | game_spread | 0.407 | 0.395 | 0.397 | 40 | 61 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT05SJDAL-SJ3 | game_spread | 0.123 | 0.125 | 0.125 | 13 | 88 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ3 | team_total | 0.557 | 0.540 | 0.543 | 55 | 47 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-9 | game_total | 0.211 | 0.205 | 0.206 | 21 | 80 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05SJDAL-SJ6 | team_total | 0.073 | 0.070 | 0.071 | 8 | 94 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-WPG6 | team_total | 0.069 | 0.070 | 0.070 | 8 | 94 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT05WPGPIT-5 | game_total | 0.802 | 0.810 | 0.808 | 82 | 20 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT05WPGPIT-WPG5 | team_total | 0.164 | 0.165 | 0.165 | 17 | 84 |  | -0.013 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ TBL | 0.638 | 0.573 | 0.174 | 0.216 | 5.75 | 5.80 | 0.957/0.991 | KXNHLGAME-26OCT05PHITB-PHI +0.064 |
| OTT @ BOS | 0.564 | 0.513 | 0.175 | 0.222 | 6.16 | 6.11 | 0.968/0.998 | KXNHLSPREAD-26OCT05OTTBOS-BOS2 -0.056 |
| WPG @ PIT | 0.628 | 0.625 | 0.165 | 0.204 | 6.47 | 6.48 | 1.021/0.997 | KXNHLSPREAD-26OCT05WPGPIT-PIT3 +0.014 |
| SJS @ DAL | 0.580 | 0.554 | 0.176 | 0.213 | 6.31 | 6.21 | 0.986/1.034 | KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4 -0.031 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 2 recommended · full analysis in card.md / packet.json `thesis_card`

- Tampa Bay wins by over 2.5 goals NO @ 71c · p 0.7884 (adj 0.7467) · $18.61 · thesis GAME:TIGHT
- Tampa Bay wins by over 1.5 goals NO @ 58c · p 0.6618 (adj 0.6184) · $3.86 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ TBL** · priced 122/130 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 23.71, exp saves 20.84 (sd 5.75), pull risk 0.04
- PHI net: Joseph Woll (PROJECTED) exp shots 28.33, exp saves 24.32 (sd 6.61), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 3+ points | 0.010 | 0.500 | 98/98 | +0.008 | STANDARD |
| Porter Martone: 2+ assists | 0.024 | 0.500 | 98/98 | -0.005 | STANDARD |
| Nikita Kucherov: 3+ assists | 0.037 | 0.500 | 98/98 | -0.018 | STANDARD |
| John Carlson: 2+ assists | 0.041 | 0.500 | 98/98 | -0.022 | STANDARD |
| Matvei Michkov: 2+ assists | 0.048 | 0.500 | 98/98 | -0.029 | STANDARD |
| Brayden Point: 3+ points | 0.055 | 0.500 | 98/98 | -0.036 | STANDARD |

**OTT @ BOS** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.37, exp saves 25.51 (sd 6.9), pull risk 0.059
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.52, exp saves 21.99 (sd 6.15), pull risk 0.062

**WPG @ PIT** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (PROJECTED) exp shots 25.59, exp saves 22.46 (sd 6.16), pull risk 0.049
- WPG net: Clay Stevenson (CONFIRMED) exp shots 28.46, exp saves 24.1 (sd 6.81), pull risk 0.084

**SJS @ DAL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.83, exp saves 21.65 (sd 6.02), pull risk 0.053
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.49, exp saves 23.66 (sd 6.53), pull risk 0.068

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
