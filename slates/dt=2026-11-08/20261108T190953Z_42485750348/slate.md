# NHL slate 2026-11-08 — RESEARCH_ONLY

generated 2026-11-08T19:09:53Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 5 · markets on board: 2920 · contracts joined: 1128 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 1003, 'OK': 87, 'NO_EDGE': 38}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 158, 'game_early_goal': 5, 'first_goal': 183, 'game_winner': 10, 'player_goals': 316, 'game_overtime': 5, 'player_points': 209, 'goalie_saves': 7, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BUF | 2026-11-08T20:30:00Z | T-60m | 0.558 | 0.442 | 0.172 | 6.45 | 3.41 | 3.03 | 232 (25/207) | PROJECTED/PROJECTED |
| TBL @ WPG | 2026-11-08T23:00:00Z | T-3h | 0.442 | 0.558 | 0.182 | 5.96 | 2.80 | 3.16 | 208 (25/183) | PROBABLE/PROJECTED |
| NJD @ TOR | 2026-11-09T00:00:00Z | T-3h | 0.457 | 0.543 | 0.171 | 6.54 | 3.12 | 3.43 | 227 (25/202) | PROBABLE/PROJECTED |
| PHI @ CGY | 2026-11-09T00:00:00Z | T-3h | 0.577 | 0.423 | 0.187 | 5.43 | 2.93 | 2.50 | 231 (25/206) | CONFIRMED/PROBABLE |
| PIT @ ANA | 2026-11-09T01:00:00Z | T-3h | 0.611 | 0.389 | 0.153 | 7.18 | 3.96 | 3.22 | 230 (25/205) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 | team_total | 0.460 | 0.590 | 0.564 | 60 | 42 | no | +0.103 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI4 | team_total | 0.251 | 0.380 | 0.352 | 39 | 63 | no | +0.102 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI2 | team_total | 0.706 | 0.805 | 0.787 | 81 | 20 | no | +0.083 | OK |
| KXNHLGAME-26NOV08PHICGY-CGY | game_winner | 0.577 | 0.475 | 0.495 | 48 | 53 | yes | +0.079 | OK |
| KXNHLGAME-26NOV08PHICGY-PHI | game_winner | 0.423 | 0.525 | 0.505 | 53 | 48 | no | +0.079 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI2 | game_spread | 0.209 | 0.305 | 0.284 | 31 | 70 | no | +0.076 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA2 | game_spread | 0.407 | 0.315 | 0.332 | 32 | 69 | yes | +0.071 | OK |
| KXNHLTOTAL-26NOV08PHICGY-5 | game_total | 0.666 | 0.755 | 0.738 | 76 | 25 | no | +0.071 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI3 | game_spread | 0.111 | 0.195 | 0.175 | 20 | 81 | no | +0.069 | OK |
| KXNHLTOTAL-26NOV08PHICGY-6 | game_total | 0.427 | 0.515 | 0.497 | 52 | 49 | no | +0.066 | OK |
| KXNHLTOTAL-26NOV08PHICGY-7 | game_total | 0.319 | 0.405 | 0.387 | 41 | 60 | no | +0.065 | OK |
| KXNHLGAME-26NOV08PITANA-ANA | game_winner | 0.611 | 0.520 | 0.538 | 53 | 49 | yes | +0.063 | OK |
| KXNHLGAME-26NOV08PITANA-PIT | game_winner | 0.389 | 0.475 | 0.458 | 48 | 53 | no | +0.063 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT2 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI5 | team_total | 0.113 | 0.200 | 0.179 | 22 | 82 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA4 | team_total | 0.572 | 0.490 | 0.507 | 50 | 52 | yes | +0.055 | OK |
| KXNHLTOTAL-26NOV08TBWPG-6 | game_total | 0.519 | 0.595 | 0.580 | 60 | 41 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA5 | team_total | 0.377 | 0.295 | 0.311 | 31 | 72 | yes | +0.052 | OK |
| KXNHLTOTAL-26NOV08PHICGY-4 | game_total | 0.770 | 0.840 | 0.828 | 85 | 17 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA6 | team_total | 0.209 | 0.140 | 0.152 | 15 | 87 | yes | +0.050 | OK |
| KXNHLTOTAL-26NOV08PHICGY-8 | game_total | 0.159 | 0.225 | 0.210 | 23 | 78 | no | +0.049 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT3 | game_spread | 0.125 | 0.185 | 0.171 | 19 | 82 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA3 | team_total | 0.759 | 0.695 | 0.709 | 70 | 31 | yes | +0.045 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA3 | game_spread | 0.277 | 0.210 | 0.222 | 22 | 80 | yes | +0.044 | OK |
| KXNHLTOTAL-26NOV08TBWPG-7 | game_total | 0.409 | 0.475 | 0.462 | 48 | 53 | no | +0.043 | OK |
| KXNHLSPREAD-26NOV08PHICGY-CGY2 | game_spread | 0.327 | 0.265 | 0.277 | 27 | 74 | yes | +0.043 | OK |
| KXNHLGAME-26NOV08VGKBUF-BUF | game_winner | 0.558 | 0.495 | 0.508 | 50 | 51 | yes | +0.041 | OK |
| KXNHLGAME-26NOV08VGKBUF-VGK | game_winner | 0.442 | 0.505 | 0.492 | 51 | 50 | no | +0.041 | OK |
| KXNHLTOTAL-26NOV08TBWPG-5 | game_total | 0.739 | 0.795 | 0.785 | 80 | 21 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV08VGKBUF-VGK2 | game_spread | 0.237 | 0.295 | 0.283 | 30 | 71 | no | +0.038 | OK |
| KXNHLSPREAD-26NOV08VGKBUF-BUF2 | game_spread | 0.340 | 0.285 | 0.296 | 29 | 72 | yes | +0.035 | OK |
| KXNHLTOTAL-26NOV08PHICGY-9 | game_total | 0.106 | 0.155 | 0.144 | 16 | 85 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV08TBWPG-4 | game_total | 0.829 | 0.875 | 0.867 | 88 | 13 | no | +0.033 | OK |
| KXNHLSPREAD-26NOV08VGKBUF-VGK3 | game_spread | 0.138 | 0.190 | 0.179 | 20 | 82 | no | +0.032 | OK |
| KXNHLGAME-26NOV08NJTOR-NJ | game_winner | 0.543 | 0.595 | 0.585 | 60 | 41 | no | +0.030 | OK |
| KXNHLGAME-26NOV08NJTOR-TOR | game_winner | 0.457 | 0.405 | 0.415 | 41 | 60 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3 | team_total | 0.606 | 0.555 | 0.565 | 56 | 45 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV08TBWPG-8 | game_total | 0.230 | 0.275 | 0.266 | 28 | 73 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB4 | team_total | 0.398 | 0.450 | 0.439 | 46 | 56 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-VGK5 | team_total | 0.192 | 0.235 | 0.226 | 24 | 77 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-VGK4 | team_total | 0.368 | 0.415 | 0.405 | 42 | 59 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI6 | team_total | 0.041 | 0.080 | 0.070 | 9 | 93 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF3 | team_total | 0.670 | 0.625 | 0.634 | 63 | 38 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV08NJTOR-9 | game_total | 0.225 | 0.185 | 0.192 | 19 | 82 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT3 | team_total | 0.621 | 0.665 | 0.656 | 67 | 34 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB5 | team_total | 0.214 | 0.260 | 0.250 | 27 | 75 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB3 | team_total | 0.622 | 0.665 | 0.657 | 67 | 34 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR5 | team_total | 0.212 | 0.175 | 0.182 | 18 | 83 | yes | +0.022 | OK |
| KXNHLTOTAL-26NOV08TBWPG-9 | game_total | 0.158 | 0.195 | 0.187 | 20 | 81 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF5 | team_total | 0.263 | 0.225 | 0.232 | 23 | 78 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF4 | team_total | 0.457 | 0.415 | 0.423 | 42 | 59 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV08PITANA-8 | game_total | 0.406 | 0.365 | 0.373 | 37 | 64 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG3 | team_total | 0.534 | 0.575 | 0.567 | 58 | 43 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT2 | team_total | 0.823 | 0.860 | 0.853 | 87 | 15 | no | +0.018 | OK |
| KXNHLSPREAD-26NOV08NJTOR-TOR2 | game_spread | 0.249 | 0.215 | 0.222 | 22 | 79 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV08TBWPG-TB3 | game_spread | 0.201 | 0.240 | 0.232 | 25 | 77 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG4 | team_total | 0.319 | 0.360 | 0.352 | 37 | 65 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV08NJTOR-7 | game_total | 0.503 | 0.465 | 0.473 | 47 | 54 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-VGK3 | team_total | 0.589 | 0.625 | 0.618 | 63 | 38 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR4 | team_total | 0.391 | 0.350 | 0.358 | 36 | 66 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV08NJTOR-8 | game_total | 0.308 | 0.270 | 0.277 | 28 | 74 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV08VGKBUF-BUF3 | game_spread | 0.215 | 0.185 | 0.191 | 19 | 82 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF6 | team_total | 0.131 | 0.095 | 0.101 | 11 | 92 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV08PHICGY-3 | game_total | 0.933 | 0.960 | 0.956 | 97 | 5 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV08PITANA-10 | game_total | 0.172 | 0.140 | 0.146 | 15 | 87 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA2 | team_total | 0.900 | 0.870 | 0.877 | 88 | 14 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV08PHICGY-10 | game_total | 0.043 | 0.065 | 0.060 | 7 | 94 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV08PITANA-9 | game_total | 0.305 | 0.275 | 0.281 | 28 | 73 | yes | +0.011 | OK |
| KXNHLSPREAD-26NOV08NJTOR-NJ3 | game_spread | 0.216 | 0.250 | 0.243 | 26 | 76 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG2 | team_total | 0.757 | 0.790 | 0.784 | 80 | 22 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB2 | team_total | 0.822 | 0.855 | 0.849 | 87 | 16 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT5 | team_total | 0.228 | 0.260 | 0.253 | 27 | 75 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF2 | team_total | 0.847 | 0.825 | 0.830 | 83 | 18 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-VGK2 | team_total | 0.803 | 0.835 | 0.829 | 85 | 18 | no | +0.007 | OK |
| KXNHLGAME-26NOV08TBWPG-TB | game_winner | 0.558 | 0.585 | 0.580 | 59 | 42 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV08TBWPG-10 | game_total | 0.070 | 0.095 | 0.089 | 11 | 92 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV08NJTOR-10 | game_total | 0.111 | 0.085 | 0.090 | 10 | 93 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV08PITANA-6 | game_total | 0.709 | 0.685 | 0.690 | 69 | 32 | yes | +0.004 | OK |
| KXNHLSPREAD-26NOV08TBWPG-TB2 | game_spread | 0.330 | 0.355 | 0.350 | 36 | 65 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV08PITANA-2 | game_total | 0.993 | 0.985 | 0.987 | 99 | 2 | yes | +0.003 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BUF | 0.558 | 0.495 | 0.172 | 0.215 | 6.45 | 6.35 | 0.998/1.004 | KXNHLGAME-26NOV08VGKBUF-BUF -0.064 |
| TBL @ WPG | 0.442 | 0.483 | 0.182 | 0.224 | 5.96 | 6.16 | 1.002/0.958 | KXNHLTEAMTOTAL-26NOV08TBWPG-WPG3 +0.060 |
| NJD @ TOR | 0.457 | 0.502 | 0.171 | 0.219 | 6.54 | 6.34 | 0.960/0.959 | KXNHLSPREAD-26NOV08NJTOR-NJ2 -0.049 |
| PHI @ CGY | 0.577 | 0.503 | 0.187 | 0.226 | 5.43 | 5.97 | 0.978/0.994 | KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 +0.122 |
| PIT @ ANA | 0.611 | 0.618 | 0.153 | 0.198 | 7.18 | 7.27 | 1.030/1.033 | KXNHLTOTAL-26NOV08PITANA-7 +0.020 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 14 recommended · full analysis in card.md / packet.json `thesis_card`

- Victor Olofsson: 1+ assists NO @ 75c · p 0.8364 (adj 0.7907) · $20.0 · thesis VGK:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 5c · p 0.072 (adj 0.0653) · $2.91 · thesis VGK:OFFENSE_4PLUS
- Zach Benson: 1+ goals YES @ 24c · p 0.2763 (adj 0.266) · $4.2 · thesis BUF:OFFENSE_4PLUS
- Mark Stone: 1+ assists NO @ 56c · p 0.6262 (adj 0.5906) · $8.07 · thesis VGK:SUPPRESSED
- Cole Perfetti: 1+ assists YES @ 32c · p 0.396 (adj 0.353) · $6.33 · thesis WPG:OFFENSE_4PLUS
- Easton Cowan: 1+ goals YES @ 17c · p 0.2221 (adj 0.2078) · $7.97 · thesis TOR:OFFENSE_4PLUS
- Colton Sissons: 1+ goals YES @ 9c · p 0.1276 (adj 0.1157) · $4.9 · thesis TOR:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 61c · p 0.6684 (adj 0.6525) · $15.96 · thesis NJD:SUPPRESSED
- Nico Hischier: 1+ goals NO @ 69c · p 0.7348 (adj 0.7224) · $14.04 · thesis NJD:SUPPRESSED
- Travis Konecny: 1+ assists NO @ 66c · p 0.7386 (adj 0.6893) · $11.52 · thesis PHI:SUPPRESSED
- Jeff Malott: 1+ goals YES @ 11c · p 0.1549 (adj 0.1424) · $6.24 · thesis ANA:OFFENSE_4PLUS
- Kaedan Korczak: 1+ goals YES @ 3c · p 0.0544 (adj 0.0458) · $2.96 · thesis PIT:OFFENSE_4PLUS
- Pittsburgh wins by over 1.5 goals NO @ 71c · p 0.7969 (adj 0.751) · $20.0 · thesis ANA:WINS
- Beckett Sennecke: 1+ goals YES @ 36c · p 0.4063 (adj 0.3935) · $5.42 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VGK @ BUF** · priced 180/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 27.36, exp saves 23.64 (sd 6.57), pull risk 0.065
- VGK net: Adin Hill (PROJECTED) exp shots 27.71, exp saves 23.93 (sd 6.63), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.408 | 0.530 | 55/49 | +0.085 | STANDARD |
| Victor Olofsson: 1+ points | 0.315 | 0.420 | 44/60 | +0.068 | STANDARD |
| Victor Olofsson: 1+ assists | 0.164 | 0.255 | 26/75 | +0.073 | STANDARD |
| Jack Eichel: 1+ assists | 0.440 | 0.530 | 55/49 | +0.053 | STANDARD |
| Mitch Marner: 1+ points | 0.542 | 0.625 | 64/39 | +0.051 | STANDARD |
| Jack Eichel: 2+ points | 0.233 | 0.315 | 32/69 | +0.062 | STANDARD |

**TBL @ WPG** · priced 156/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROBABLE) exp shots 28.45, exp saves 24.6 (sd 6.75), pull risk 0.061
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.75, exp saves 22.33 (sd 6.15), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.463 | 0.615 | 63/40 | +0.120 | STANDARD |
| Nikita Kucherov: 2+ points | 0.270 | 0.400 | 42/62 | +0.094 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.126 | 0.235 | 26/79 | +0.072 | STANDARD |
| John Carlson: 1+ points | 0.377 | 0.465 | 47/54 | +0.066 | STANDARD |
| Cole Perfetti: 1+ assists | 0.396 | 0.310 | 32/70 | +0.061 | STANDARD |
| Nikita Kucherov: 1+ points | 0.640 | 0.725 | 76/31 | +0.035 | STANDARD |

**NJD @ TOR** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROBABLE) exp shots 32.87, exp saves 28.37 (sd 7.47), pull risk 0.065
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 26.54, exp saves 23.0 (sd 6.29), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.396 | 0.520 | 54/50 | +0.086 | STANDARD |
| Jack Hughes: 2+ points | 0.229 | 0.350 | 36/66 | +0.095 | STANDARD |
| John Tavares: 1+ assists | 0.245 | 0.365 | 38/65 | +0.089 | STANDARD |
| Easton Cowan: 2+ points | 0.160 | 0.055 | 10/99 | +0.053 | STANDARD |
| Luke Evangelista: 1+ assists | 0.246 | 0.350 | 37/67 | +0.068 | STANDARD |
| Jesper Bratt: 1+ assists | 0.382 | 0.480 | 49/53 | +0.070 | STANDARD |

**PHI @ CGY** · priced 177/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 26.62, exp saves 23.17 (sd 6.4), pull risk 0.053
- PHI net: Dan Vladar (PROBABLE) exp shots 27.45, exp saves 23.82 (sd 6.48), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ assists | 0.261 | 0.360 | 38/66 | +0.063 | STANDARD |
| Travis Konecny: 1+ points | 0.428 | 0.500 | 51/51 | +0.044 | STANDARD |
| Porter Martone: 1+ points | 0.400 | 0.465 | 48/55 | +0.033 | STANDARD |
| Porter Martone: 1+ goals | 0.187 | 0.240 | 26/78 | +0.021 | STANDARD |
| Travis Konecny: 2+ points | 0.108 | 0.160 | 18/86 | +0.023 | STANDARD |
| Travis Sanheim: 1+ points | 0.380 | 0.335 | 34/67 | +0.025 | STANDARD |

**PIT @ ANA** · priced 178/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 26.45, exp saves 22.95 (sd 6.53), pull risk 0.071
- PIT net: Arturs Silovs (PROJECTED) exp shots 28.23, exp saves 23.69 (sd 6.97), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Erik Karlsson: 1+ assists | 0.430 | 0.505 | 52/51 | +0.042 | STANDARD |
| Erik Karlsson: 1+ points | 0.515 | 0.590 | 61/43 | +0.037 | STANDARD |
| Alex Killorn: 1+ points | 0.483 | 0.410 | 42/60 | +0.046 | STANDARD |
| Ben Kindel: 1+ points | 0.425 | 0.495 | 51/52 | +0.038 | STANDARD |
| Judd Caulfield: 1+ goals | 0.238 | 0.170 | 20/86 | +0.026 | STANDARD |
| Sidney Crosby: 1+ assists | 0.383 | 0.450 | 47/57 | +0.030 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
