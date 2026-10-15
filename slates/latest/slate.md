# NHL slate 2026-10-15 — RESEARCH_ONLY

generated 2026-10-15T23:22:21Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 6 · markets on board: 4960 · contracts joined: 1459 (unjoined to any game: 1871)
gates: {'UNSUPPORTED': 1309, 'OK': 88, 'NO_EDGE': 62}
families: {'period_winner': 54, 'period_spread': 36, 'period_total': 54, 'player_assists': 224, 'game_early_goal': 6, 'first_goal': 227, 'game_winner': 12, 'player_goals': 383, 'game_overtime': 6, 'player_points': 306, 'goalie_saves': 13, 'game_spread': 24, 'team_total': 60, 'game_total': 54}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ DET | 2026-10-15T23:30:00Z | T-<10m | 0.601 | 0.399 | 0.180 | 5.81 | 3.22 | 2.59 | 232 (25/207) | CONFIRMED/CONFIRMED |
| WPG @ CHI | 2026-10-16T00:00:00Z | T-30m | 0.493 | 0.507 | 0.180 | 5.82 | 2.89 | 2.93 | 255 (25/230) | CONFIRMED/PROBABLE |
| SJS @ NSH | 2026-10-16T00:00:00Z | T-30m | 0.532 | 0.468 | 0.175 | 6.40 | 3.30 | 3.10 | 249 (25/224) | PROBABLE/CONFIRMED |
| STL @ MIN | 2026-10-16T00:00:00Z | T-30m | 0.540 | 0.460 | 0.181 | 5.99 | 3.12 | 2.87 | 242 (25/217) | CONFIRMED/PROJECTED |
| UTA @ EDM | 2026-10-16T01:00:00Z | T-90m | 0.557 | 0.443 | 0.166 | 6.64 | 3.51 | 3.13 | 242 (25/217) | CONFIRMED/CONFIRMED |
| CGY @ VGK | 2026-10-16T02:00:00Z | T-90m | 0.665 | 0.335 | 0.158 | 6.30 | 3.70 | 2.61 | 239 (25/214) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT15WPGCHI-7 | game_total | 0.383 | 0.455 | 0.440 | 46 | 55 | no | +0.049 | OK |
| KXNHLGAME-26OCT15UTAEDM-EDM | game_winner | 0.557 | 0.485 | 0.499 | 49 | 52 | yes | +0.049 | OK |
| KXNHLGAME-26OCT15UTAEDM-UTA | game_winner | 0.443 | 0.515 | 0.501 | 52 | 49 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-5 | game_total | 0.719 | 0.790 | 0.777 | 80 | 22 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-6 | game_total | 0.494 | 0.565 | 0.551 | 57 | 44 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG4 | team_total | 0.346 | 0.425 | 0.409 | 44 | 59 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-4 | game_total | 0.818 | 0.875 | 0.865 | 88 | 13 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT15UTAEDM-EDM2 | game_spread | 0.345 | 0.285 | 0.297 | 29 | 72 | yes | +0.041 | OK |
| KXNHLGAME-26OCT15CGYVGK-CGY | game_winner | 0.335 | 0.275 | 0.286 | 28 | 73 | yes | +0.041 | OK |
| KXNHLGAME-26OCT15CGYVGK-VGK | game_winner | 0.665 | 0.725 | 0.714 | 73 | 28 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI3 | team_total | 0.482 | 0.545 | 0.532 | 55 | 46 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT15UTAEDM-UTA2 | game_spread | 0.248 | 0.305 | 0.293 | 31 | 70 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG5 | team_total | 0.173 | 0.230 | 0.218 | 24 | 78 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG3 | team_total | 0.569 | 0.630 | 0.618 | 64 | 38 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT15UTAEDM-UTA3 | game_spread | 0.145 | 0.195 | 0.184 | 20 | 81 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG2 | team_total | 0.789 | 0.840 | 0.831 | 85 | 17 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK3 | game_spread | 0.304 | 0.355 | 0.345 | 36 | 65 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-8 | game_total | 0.208 | 0.255 | 0.245 | 26 | 75 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-9 | game_total | 0.141 | 0.185 | 0.175 | 19 | 82 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT15PHIDET-PHI3 | game_spread | 0.103 | 0.145 | 0.136 | 15 | 86 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT15PHIDET-5 | game_total | 0.720 | 0.765 | 0.756 | 77 | 24 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI2 | team_total | 0.722 | 0.765 | 0.757 | 77 | 24 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT15WPGCHI-WPG3 | game_spread | 0.165 | 0.205 | 0.196 | 21 | 80 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY4 | team_total | 0.277 | 0.235 | 0.243 | 24 | 77 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-CGY2 | game_spread | 0.161 | 0.125 | 0.132 | 13 | 88 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT15PHIDET-4 | game_total | 0.819 | 0.855 | 0.848 | 86 | 15 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI4 | team_total | 0.273 | 0.320 | 0.310 | 33 | 69 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-UTA2 | team_total | 0.809 | 0.845 | 0.838 | 85 | 16 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT15STLMIN-MIN4 | team_total | 0.392 | 0.435 | 0.426 | 44 | 57 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM5 | team_total | 0.283 | 0.245 | 0.252 | 25 | 76 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM3 | team_total | 0.685 | 0.645 | 0.653 | 65 | 36 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT15STLMIN-MIN3 | game_spread | 0.189 | 0.225 | 0.218 | 23 | 78 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-UTA3 | team_total | 0.605 | 0.645 | 0.637 | 65 | 36 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT15PHIDET-6 | game_total | 0.494 | 0.535 | 0.527 | 54 | 47 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT15STLMIN-4 | game_total | 0.834 | 0.865 | 0.859 | 87 | 14 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK2 | game_spread | 0.446 | 0.485 | 0.477 | 49 | 52 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT15PHIDET-DET2 | game_spread | 0.372 | 0.335 | 0.342 | 34 | 67 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 | team_total | 0.317 | 0.360 | 0.351 | 37 | 65 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM6 | team_total | 0.143 | 0.110 | 0.116 | 12 | 90 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK2 | team_total | 0.879 | 0.910 | 0.904 | 92 | 10 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT15SJNSH-NSH3 | game_spread | 0.193 | 0.225 | 0.218 | 23 | 78 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY5 | team_total | 0.131 | 0.105 | 0.110 | 11 | 90 | yes | +0.015 | OK |
| KXNHLGAME-26OCT15PHIDET-PHI | game_winner | 0.399 | 0.435 | 0.428 | 44 | 57 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT15PHIDET-7 | game_total | 0.380 | 0.420 | 0.412 | 43 | 59 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY3 | team_total | 0.480 | 0.445 | 0.452 | 45 | 56 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK3 | team_total | 0.725 | 0.755 | 0.749 | 76 | 25 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG6 | team_total | 0.073 | 0.100 | 0.094 | 11 | 91 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT15PHIDET-PHI2 | game_spread | 0.197 | 0.230 | 0.223 | 24 | 78 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4 | team_total | 0.521 | 0.565 | 0.556 | 58 | 45 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY6 | team_total | 0.054 | 0.035 | 0.038 | 4 | 97 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT15STLMIN-5 | game_total | 0.747 | 0.775 | 0.770 | 78 | 23 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-CGY3 | game_spread | 0.085 | 0.065 | 0.069 | 7 | 94 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT15STLMIN-MIN2 | game_spread | 0.314 | 0.345 | 0.339 | 35 | 66 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT15WPGCHI-WPG2 | game_spread | 0.285 | 0.315 | 0.309 | 32 | 69 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM4 | team_total | 0.477 | 0.445 | 0.451 | 45 | 56 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-UTA5 | team_total | 0.217 | 0.250 | 0.243 | 26 | 76 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY2 | team_total | 0.724 | 0.690 | 0.697 | 70 | 32 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT15UTAEDM-UTA4 | team_total | 0.394 | 0.425 | 0.419 | 43 | 58 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT15STLMIN-2 | game_total | 0.981 | 0.980 | 0.980 |  | 1 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT15PHIDET-3 | game_total | 0.949 | 0.965 | 0.962 | 97 | 4 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT15SJNSH-SJ5 | team_total | 0.208 | 0.185 | 0.190 | 19 | 82 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI5 | team_total | 0.124 | 0.145 | 0.141 | 15 | 86 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT15SJNSH-SJ6 | team_total | 0.092 | 0.075 | 0.078 | 8 | 93 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-CHI4 | team_total | 0.337 | 0.365 | 0.359 | 37 | 64 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-3 | game_total | 0.951 | 0.965 | 0.963 | 97 | 4 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT15SJNSH-8 | game_total | 0.290 | 0.265 | 0.270 | 27 | 74 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK6 | team_total | 0.164 | 0.190 | 0.184 | 20 | 82 | no | +0.006 | OK |
| KXNHLGAME-26OCT15WPGCHI-CHI | game_winner | 0.493 | 0.465 | 0.471 | 47 | 54 | yes | +0.005 | OK |
| KXNHLGAME-26OCT15WPGCHI-WPG | game_winner | 0.507 | 0.535 | 0.529 | 54 | 47 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT15STLMIN-6 | game_total | 0.527 | 0.555 | 0.549 | 56 | 45 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT15UTAEDM-5 | game_total | 0.815 | 0.835 | 0.831 | 84 | 17 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-CHI2 | team_total | 0.773 | 0.795 | 0.791 | 80 | 21 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT15STLMIN-MIN2 | team_total | 0.815 | 0.840 | 0.835 | 85 | 17 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-10 | game_total | 0.061 | 0.080 | 0.076 | 9 | 93 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT15STLMIN-MIN3 | team_total | 0.609 | 0.640 | 0.634 | 65 | 37 | no | +0.005 | OK |
| KXNHLGAME-26OCT15PHIDET-DET | game_winner | 0.601 | 0.575 | 0.580 | 58 | 43 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT15CGYVGK-3 | game_total | 0.965 | 0.975 | 0.973 | 98 | 3 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT15STLMIN-3 | game_total | 0.955 | 0.965 | 0.963 | 97 | 4 | no | +0.003 | OK |
| KXNHLGAME-26OCT15STLMIN-MIN | game_winner | 0.540 | 0.565 | 0.560 | 57 | 44 | no | +0.002 | OK |
| KXNHLGAME-26OCT15STLMIN-STL | game_winner | 0.460 | 0.435 | 0.440 | 44 | 57 | yes | +0.002 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ DET | 0.601 | 0.515 | 0.180 | 0.226 | 5.81 | 5.82 | 1.024/0.990 | KXNHLSPREAD-26OCT15PHIDET-DET2 -0.088 |
| WPG @ CHI | 0.493 | 0.491 | 0.180 | 0.218 | 5.82 | 6.17 | 0.988/0.996 | KXNHLTOTAL-26OCT15WPGCHI-7 +0.063 |
| SJS @ NSH | 0.532 | 0.527 | 0.175 | 0.218 | 6.40 | 6.51 | 1.002/1.021 | KXNHLTOTAL-26OCT15SJNSH-7 +0.021 |
| STL @ MIN | 0.540 | 0.555 | 0.181 | 0.220 | 5.99 | 6.39 | 0.991/0.993 | KXNHLTOTAL-26OCT15STLMIN-7 +0.074 |
| UTA @ EDM | 0.557 | 0.583 | 0.166 | 0.205 | 6.64 | 6.76 | 0.994/0.989 | KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM4 +0.035 |
| CGY @ VGK | 0.665 | 0.660 | 0.158 | 0.207 | 6.30 | 6.19 | 1.003/1.006 | KXNHLTOTAL-26OCT15CGYVGK-6 -0.029 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 23 recommended · full analysis in card.md / packet.json `thesis_card`

- Nate Danielson: 1+ goals NO @ 82c · p 0.8871 (adj 0.8691) · $13.04 · thesis DET:SUPPRESSED
- Porter Martone: 1+ goals NO @ 78c · p 0.8258 (adj 0.8131) · $13.04 · thesis PHI:SUPPRESSED
- Denver Barkey: 1+ goals YES @ 14c · p 0.1733 (adj 0.1637) · $2.81 · thesis PHI:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 15c · p 0.1789 (adj 0.1704) · $2.16 · thesis PHI:OFFENSE_4PLUS
- Nino Niederreiter: 1+ assists NO @ 79c · p 0.8746 (adj 0.8298) · $12.27 · thesis WPG:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 26c · p 0.3135 (adj 0.2989) · $5.03 · thesis CHI:OFFENSE_4PLUS
- Roman Kantserov: 1+ goals NO @ 74c · p 0.7922 (adj 0.7767) · $12.27 · thesis CHI:SUPPRESSED
- Gabriel Vilardi: 1+ goals YES @ 26c · p 0.2978 (adj 0.2871) · $3.03 · thesis WPG:OFFENSE_4PLUS
- Mason Marchment: 1+ goals YES @ 20c · p 0.2524 (adj 0.2381) · $5.56 · thesis SJS:OFFENSE_4PLUS
- Macklin Celebrini: 1+ assists NO @ 42c · p 0.5685 (adj 0.4534) · $5.26 · thesis SJS:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 69c · p 0.7862 (adj 0.7172) · $7.82 · thesis SJS:SUPPRESSED
- Ryan Hartman: 1+ goals YES @ 18c · p 0.2323 (adj 0.218) · $5.67 · thesis MIN:OFFENSE_4PLUS
- Rieger Lorenz: 1+ goals YES @ 10c · p 0.1383 (adj 0.1275) · $3.67 · thesis MIN:OFFENSE_4PLUS
- Philip Broberg: 1+ goals YES @ 6c · p 0.088 (adj 0.0797) · $2.45 · thesis STL:OFFENSE_4PLUS
- Quinn Hughes: 1+ assists NO @ 35c · p 0.4215 (adj 0.3832) · $5.64 · thesis MIN:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 16c · p 0.216 (adj 0.1995) · $5.51 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 9c · p 0.1273 (adj 0.1155) · $3.34 · thesis EDM:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 65c · p 0.7034 (adj 0.6888) · $11.26 · thesis UTA:SUPPRESSED
- Leon Draisaitl: 1+ assists NO @ 41c · p 0.4892 (adj 0.4471) · $6.51 · thesis EDM:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 68c · p 0.74 (adj 0.7238) · $9.78 · thesis VGK:SUPPRESSED
- Trevor Connelly: 1+ assists NO @ 64c · p 0.7766 (adj 0.6846) · $9.78 · thesis VGK:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 6c · p 0.085 (adj 0.0775) · $2.12 · thesis VGK:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 16c · p 0.1901 (adj 0.1801) · $1.97 · thesis CGY:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ DET** · priced 170/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (CONFIRMED) exp shots 24.83, exp saves 21.59 (sd 5.96), pull risk 0.05
- PHI net: Joseph Woll (CONFIRMED) exp shots 29.07, exp saves 25.28 (sd 6.67), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ben Chiarot: 1+ assists | 0.239 | 0.100 | 18/98 | +0.049 | STANDARD |
| Nick Seeler: 1+ points | 0.228 | 0.095 | 18/99 | +0.038 | STANDARD |
| Nate Danielson: 1+ points | 0.229 | 0.350 | 36/66 | +0.096 | STANDARD |
| Travis Sanheim: 1+ points | 0.391 | 0.300 | 31/71 | +0.066 | STANDARD |
| Dylan Larkin: 1+ assists | 0.334 | 0.420 | 44/60 | +0.049 | STANDARD |
| Nate Danielson: 1+ assists | 0.131 | 0.210 | 23/81 | +0.049 | STANDARD |

**WPG @ CHI** · priced 187/204 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 27.63, exp saves 23.95 (sd 6.63), pull risk 0.064
- WPG net: Stuart Skinner (PROBABLE) exp shots 25.12, exp saves 21.75 (sd 6.06), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Vlasic: 1+ assists | 0.266 | 0.095 | 17/98 | +0.086 | STANDARD |
| Connor Bedard: 1+ assists | 0.351 | 0.490 | 50/52 | +0.112 | STANDARD |
| Connor Bedard: 1+ points | 0.540 | 0.660 | 67/35 | +0.094 | STANDARD |
| Connor Bedard: 2+ points | 0.187 | 0.300 | 32/72 | +0.079 | STANDARD |
| Patrick Kane: 1+ assists | 0.324 | 0.420 | 43/59 | +0.069 | STANDARD |
| Alex Vlasic: 1+ points | 0.302 | 0.210 | 22/80 | +0.070 | STANDARD |

**SJS @ NSH** · priced 184/198 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 27.54, exp saves 23.87 (sd 6.58), pull risk 0.066
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.64, exp saves 23.73 (sd 6.59), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.431 | 0.585 | 59/42 | +0.131 | STANDARD |
| Ivar Stenberg: 1+ points | 0.347 | 0.455 | 46/55 | +0.086 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ assists | 0.214 | 0.320 | 33/69 | +0.081 | PRIOR_HEAVY |
| Macklin Celebrini: 2+ points | 0.294 | 0.400 | 41/61 | +0.079 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.116 | 0.220 | 24/80 | +0.073 | STANDARD |
| Macklin Celebrini: 1+ points | 0.649 | 0.745 | 75/26 | +0.077 | STANDARD |

**STL @ MIN** · priced 181/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 26.75, exp saves 23.23 (sd 6.4), pull risk 0.059
- STL net: Joel Hofer (PROJECTED) exp shots 28.41, exp saves 24.34 (sd 6.78), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Bogosian: 1+ assists | 0.205 | 0.075 | 12/97 | +0.078 | STANDARD |
| Ryan Hartman: 1+ points | 0.479 | 0.355 | 37/66 | +0.092 | STANDARD |
| Philip Broberg: 1+ points | 0.428 | 0.325 | 34/69 | +0.072 | STANDARD |
| Zach Bogosian: 1+ points | 0.239 | 0.145 | 16/87 | +0.069 | STANDARD |
| Ryan Hartman: 1+ assists | 0.318 | 0.230 | 24/78 | +0.066 | STANDARD |
| Philip Broberg: 1+ assists | 0.372 | 0.285 | 30/73 | +0.057 | STANDARD |

**UTA @ EDM** · priced 187/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 27.2, exp saves 23.67 (sd 6.43), pull risk 0.06
- UTA net: Karel Vejmelka (CONFIRMED) exp shots 27.99, exp saves 23.78 (sd 6.74), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mattias Ekholm: 1+ points | 0.474 | 0.330 | 34/68 | +0.118 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.193 | 0.330 | 34/68 | +0.112 | STANDARD |
| Connor McDavid: 2+ assists | 0.197 | 0.320 | 33/69 | +0.098 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.396 | 0.275 | 28/73 | +0.102 | STANDARD |
| Connor McDavid: 1+ assists | 0.560 | 0.680 | 69/33 | +0.094 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.459 | 0.340 | 35/67 | +0.093 | STANDARD |

**CGY @ VGK** · priced 187/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.2, exp saves 23.24 (sd 6.25), pull risk 0.041
- CGY net: Dustin Wolf (CONFIRMED) exp shots 30.19, exp saves 25.42 (sd 7.17), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.466 | 0.610 | 62/40 | +0.117 | STANDARD |
| Trevor Connelly: 1+ assists | 0.223 | 0.365 | 37/64 | +0.120 | PRIOR_HEAVY |
| Mitch Marner: 1+ assists | 0.435 | 0.560 | 57/45 | +0.098 | STANDARD |
| Jack Eichel: 2+ points | 0.272 | 0.395 | 41/62 | +0.092 | STANDARD |
| Trevor Connelly: 1+ points | 0.391 | 0.510 | 52/50 | +0.091 | PRIOR_HEAVY |
| Mitch Marner: 2+ points | 0.222 | 0.340 | 35/67 | +0.092 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
