# NHL slate 2026-11-08 — RESEARCH_ONLY

generated 2026-11-08T20:04:32Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 5 · markets on board: 2911 · contracts joined: 1128 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 1003, 'OK': 91, 'NO_EDGE': 34}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 158, 'game_early_goal': 5, 'first_goal': 183, 'game_winner': 10, 'player_goals': 316, 'game_overtime': 5, 'player_points': 209, 'goalie_saves': 7, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BUF | 2026-11-08T20:30:00Z | T-10m | 0.577 | 0.423 | 0.172 | 6.55 | 3.51 | 3.04 | 232 (25/207) | CONFIRMED/CONFIRMED |
| TBL @ WPG | 2026-11-08T23:00:00Z | T-90m | 0.442 | 0.558 | 0.182 | 5.96 | 2.80 | 3.16 | 208 (25/183) | PROBABLE/PROJECTED |
| NJD @ TOR | 2026-11-09T00:00:00Z | T-3h | 0.457 | 0.543 | 0.171 | 6.54 | 3.12 | 3.43 | 227 (25/202) | PROBABLE/PROJECTED |
| PHI @ CGY | 2026-11-09T00:00:00Z | T-3h | 0.577 | 0.423 | 0.187 | 5.43 | 2.93 | 2.50 | 231 (25/206) | CONFIRMED/PROBABLE |
| PIT @ ANA | 2026-11-09T01:00:00Z | T-3h | 0.611 | 0.389 | 0.153 | 7.18 | 3.96 | 3.22 | 230 (25/205) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 | team_total | 0.460 | 0.590 | 0.564 | 60 | 42 | no | +0.103 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI4 | team_total | 0.251 | 0.380 | 0.352 | 39 | 63 | no | +0.102 | OK |
| KXNHLGAME-26NOV08PHICGY-CGY | game_winner | 0.577 | 0.475 | 0.495 | 48 | 53 | yes | +0.079 | OK |
| KXNHLGAME-26NOV08PHICGY-PHI | game_winner | 0.423 | 0.525 | 0.505 | 53 | 48 | no | +0.079 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI2 | game_spread | 0.209 | 0.305 | 0.284 | 31 | 70 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI2 | team_total | 0.706 | 0.800 | 0.783 | 81 | 21 | no | +0.073 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA2 | game_spread | 0.407 | 0.315 | 0.332 | 32 | 69 | yes | +0.071 | OK |
| KXNHLTOTAL-26NOV08PHICGY-5 | game_total | 0.666 | 0.755 | 0.738 | 76 | 25 | no | +0.071 | OK |
| KXNHLGAME-26NOV08VGKBUF-BUF | game_winner | 0.577 | 0.485 | 0.503 | 49 | 52 | yes | +0.069 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI3 | game_spread | 0.111 | 0.195 | 0.175 | 20 | 81 | no | +0.069 | OK |
| KXNHLTOTAL-26NOV08PHICGY-6 | game_total | 0.427 | 0.515 | 0.497 | 52 | 49 | no | +0.066 | OK |
| KXNHLTOTAL-26NOV08PHICGY-7 | game_total | 0.319 | 0.405 | 0.387 | 41 | 60 | no | +0.065 | OK |
| KXNHLGAME-26NOV08PITANA-ANA | game_winner | 0.611 | 0.525 | 0.542 | 53 | 48 | yes | +0.063 | OK |
| KXNHLGAME-26NOV08PITANA-PIT | game_winner | 0.389 | 0.475 | 0.458 | 48 | 53 | no | +0.063 | OK |
| KXNHLGAME-26NOV08VGKBUF-VGK | game_winner | 0.423 | 0.505 | 0.488 | 51 | 50 | no | +0.059 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT2 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI5 | team_total | 0.113 | 0.195 | 0.176 | 21 | 82 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA4 | team_total | 0.572 | 0.490 | 0.507 | 50 | 52 | yes | +0.055 | OK |
| KXNHLTOTAL-26NOV08TBWPG-6 | game_total | 0.519 | 0.595 | 0.580 | 60 | 41 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA5 | team_total | 0.377 | 0.295 | 0.311 | 31 | 72 | yes | +0.052 | OK |
| KXNHLSPREAD-26NOV08VGKBUF-BUF2 | game_spread | 0.356 | 0.285 | 0.299 | 29 | 72 | yes | +0.052 | OK |
| KXNHLTOTAL-26NOV08PHICGY-4 | game_total | 0.770 | 0.840 | 0.828 | 85 | 17 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA6 | team_total | 0.209 | 0.140 | 0.152 | 15 | 87 | yes | +0.050 | OK |
| KXNHLTOTAL-26NOV08PHICGY-8 | game_total | 0.159 | 0.225 | 0.210 | 23 | 78 | no | +0.049 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT3 | game_spread | 0.125 | 0.185 | 0.171 | 19 | 82 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA3 | team_total | 0.759 | 0.695 | 0.709 | 70 | 31 | yes | +0.045 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA3 | game_spread | 0.277 | 0.210 | 0.222 | 22 | 80 | yes | +0.044 | OK |
| KXNHLSPREAD-26NOV08VGKBUF-VGK2 | game_spread | 0.231 | 0.295 | 0.282 | 30 | 71 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF4 | team_total | 0.481 | 0.415 | 0.428 | 42 | 59 | yes | +0.044 | OK |
| KXNHLTOTAL-26NOV08TBWPG-7 | game_total | 0.409 | 0.475 | 0.462 | 48 | 53 | no | +0.043 | OK |
| KXNHLSPREAD-26NOV08PHICGY-CGY2 | game_spread | 0.327 | 0.265 | 0.277 | 27 | 74 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF3 | team_total | 0.688 | 0.625 | 0.638 | 63 | 38 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF5 | team_total | 0.283 | 0.225 | 0.236 | 23 | 78 | yes | +0.041 | OK |
| KXNHLTOTAL-26NOV08TBWPG-5 | game_total | 0.739 | 0.795 | 0.785 | 80 | 21 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV08VGKBUF-VGK3 | game_spread | 0.134 | 0.190 | 0.178 | 20 | 82 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB4 | team_total | 0.398 | 0.455 | 0.443 | 46 | 55 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV08TBWPG-4 | game_total | 0.829 | 0.875 | 0.867 | 88 | 13 | no | +0.033 | OK |
| KXNHLGAME-26NOV08NJTOR-NJ | game_winner | 0.543 | 0.595 | 0.585 | 60 | 41 | no | +0.030 | OK |
| KXNHLGAME-26NOV08NJTOR-TOR | game_winner | 0.457 | 0.405 | 0.415 | 41 | 60 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3 | team_total | 0.606 | 0.555 | 0.565 | 56 | 45 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV08VGKBUF-BUF3 | game_spread | 0.227 | 0.185 | 0.193 | 19 | 82 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV08TBWPG-8 | game_total | 0.230 | 0.275 | 0.266 | 28 | 73 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF6 | team_total | 0.143 | 0.095 | 0.103 | 11 | 92 | yes | +0.026 | OK |
| KXNHLTOTAL-26NOV08PHICGY-9 | game_total | 0.106 | 0.150 | 0.140 | 16 | 86 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI6 | team_total | 0.041 | 0.080 | 0.070 | 9 | 93 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV08NJTOR-9 | game_total | 0.225 | 0.185 | 0.192 | 19 | 82 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-VGK5 | team_total | 0.194 | 0.235 | 0.226 | 24 | 77 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT3 | team_total | 0.621 | 0.665 | 0.656 | 67 | 34 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-VGK4 | team_total | 0.370 | 0.415 | 0.406 | 42 | 59 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB5 | team_total | 0.214 | 0.260 | 0.250 | 27 | 75 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB3 | team_total | 0.622 | 0.665 | 0.657 | 67 | 34 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR5 | team_total | 0.212 | 0.175 | 0.182 | 18 | 83 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG2 | team_total | 0.757 | 0.795 | 0.788 | 80 | 21 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV08TBWPG-9 | game_total | 0.158 | 0.195 | 0.187 | 20 | 81 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV08PITANA-8 | game_total | 0.406 | 0.365 | 0.373 | 37 | 64 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB2 | team_total | 0.822 | 0.860 | 0.853 | 87 | 15 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF2 | team_total | 0.859 | 0.820 | 0.828 | 83 | 19 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG3 | team_total | 0.534 | 0.575 | 0.567 | 58 | 43 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT2 | team_total | 0.823 | 0.860 | 0.853 | 87 | 15 | no | +0.018 | OK |
| KXNHLSPREAD-26NOV08TBWPG-TB3 | game_spread | 0.201 | 0.240 | 0.232 | 25 | 77 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG4 | team_total | 0.319 | 0.360 | 0.352 | 37 | 65 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR4 | team_total | 0.391 | 0.350 | 0.358 | 36 | 66 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV08NJTOR-8 | game_total | 0.308 | 0.270 | 0.277 | 28 | 74 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV08PHICGY-3 | game_total | 0.933 | 0.960 | 0.956 | 97 | 5 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV08PITANA-10 | game_total | 0.172 | 0.140 | 0.146 | 15 | 87 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA2 | team_total | 0.900 | 0.870 | 0.877 | 88 | 14 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-VGK3 | team_total | 0.591 | 0.625 | 0.618 | 63 | 38 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV08PHICGY-10 | game_total | 0.043 | 0.065 | 0.060 | 7 | 94 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT4 | team_total | 0.411 | 0.450 | 0.442 | 46 | 56 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV08PITANA-9 | game_total | 0.305 | 0.275 | 0.281 | 28 | 73 | yes | +0.011 | OK |
| KXNHLSPREAD-26NOV08NJTOR-NJ3 | game_spread | 0.216 | 0.250 | 0.243 | 26 | 76 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-VGK2 | team_total | 0.801 | 0.835 | 0.829 | 85 | 18 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV08VGKBUF-2 | game_total | 0.990 | 0.975 | 0.979 | 98 | 3 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT5 | team_total | 0.228 | 0.260 | 0.253 | 27 | 75 | no | +0.008 | OK |
| KXNHLSPREAD-26NOV08NJTOR-TOR2 | game_spread | 0.249 | 0.220 | 0.226 | 23 | 79 | yes | +0.007 | OK |
| KXNHLGAME-26NOV08TBWPG-TB | game_winner | 0.558 | 0.585 | 0.580 | 59 | 42 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV08TBWPG-10 | game_total | 0.070 | 0.095 | 0.089 | 11 | 92 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV08NJTOR-7 | game_total | 0.503 | 0.475 | 0.481 | 48 | 53 | yes | +0.005 | OK |
| KXNHLTOTAL-26NOV08NJTOR-10 | game_total | 0.111 | 0.095 | 0.098 | 10 | 91 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV08PITANA-6 | game_total | 0.709 | 0.680 | 0.686 | 69 | 33 | yes | +0.004 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BUF | 0.577 | 0.498 | 0.172 | 0.216 | 6.55 | 6.36 | 1.000/1.004 | KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF4 -0.079 |
| TBL @ WPG | 0.442 | 0.483 | 0.182 | 0.224 | 5.96 | 6.16 | 1.002/0.958 | KXNHLTEAMTOTAL-26NOV08TBWPG-WPG3 +0.060 |
| NJD @ TOR | 0.457 | 0.502 | 0.171 | 0.219 | 6.54 | 6.34 | 0.960/0.959 | KXNHLSPREAD-26NOV08NJTOR-NJ2 -0.049 |
| PHI @ CGY | 0.577 | 0.503 | 0.187 | 0.226 | 5.43 | 5.97 | 0.978/0.994 | KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 +0.122 |
| PIT @ ANA | 0.611 | 0.618 | 0.153 | 0.198 | 7.18 | 7.27 | 1.030/1.033 | KXNHLTOTAL-26NOV08PITANA-7 +0.020 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 15 recommended · full analysis in card.md / packet.json `thesis_card`

- Brayden McNabb: 1+ goals YES @ 5c · p 0.0706 (adj 0.0642) · $2.67 · thesis VGK:OFFENSE_4PLUS
- Marc Gatcomb: 1+ goals YES @ 7c · p 0.0941 (adj 0.0868) · $3.11 · thesis VGK:OFFENSE_4PLUS
- Beck Malenstyn: 1+ goals YES @ 7c · p 0.0935 (adj 0.0864) · $2.94 · thesis BUF:OFFENSE_4PLUS
- Mark Stone: 1+ assists NO @ 56c · p 0.6318 (adj 0.5934) · $10.28 · thesis VGK:SUPPRESSED
- Cole Perfetti: 1+ assists YES @ 32c · p 0.396 (adj 0.353) · $6.46 · thesis WPG:OFFENSE_4PLUS
- Nikita Kucherov: 1+ assists NO @ 39c · p 0.5372 (adj 0.4231) · $6.84 · thesis TBL:SUPPRESSED
- Easton Cowan: 1+ goals YES @ 17c · p 0.2221 (adj 0.2078) · $8.01 · thesis TOR:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 10c · p 0.1464 (adj 0.1285) · $5.36 · thesis TOR:OFFENSE_4PLUS
- Brandon Duhaime: 1+ goals YES @ 6c · p 0.0922 (adj 0.0817) · $4.02 · thesis TOR:OFFENSE_4PLUS
- Colton Sissons: 1+ goals YES @ 9c · p 0.1276 (adj 0.1157) · $4.9 · thesis TOR:OFFENSE_4PLUS
- Travis Konecny: 1+ assists NO @ 65c · p 0.7386 (adj 0.6893) · $19.11 · thesis PHI:SUPPRESSED
- Jeff Malott: 1+ goals YES @ 11c · p 0.1549 (adj 0.1424) · $6.64 · thesis ANA:OFFENSE_4PLUS
- Kaedan Korczak: 1+ goals YES @ 3c · p 0.0544 (adj 0.0458) · $2.77 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.1601 (adj 0.1463) · $4.92 · thesis PIT:OFFENSE_4PLUS
- Beckett Sennecke: 1+ goals YES @ 36c · p 0.4063 (adj 0.3935) · $6.82 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VGK @ BUF** · priced 180/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (CONFIRMED) exp shots 27.36, exp saves 23.65 (sd 6.57), pull risk 0.063
- VGK net: Adin Hill (CONFIRMED) exp shots 27.71, exp saves 23.88 (sd 6.55), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.408 | 0.535 | 55/48 | +0.095 | STANDARD |
| Victor Olofsson: 1+ points | 0.313 | 0.425 | 44/59 | +0.080 | STANDARD |
| Victor Olofsson: 1+ assists | 0.159 | 0.265 | 28/75 | +0.078 | STANDARD |
| Jack Eichel: 1+ assists | 0.443 | 0.540 | 55/47 | +0.070 | STANDARD |
| Mitch Marner: 1+ points | 0.540 | 0.630 | 64/38 | +0.064 | STANDARD |
| Jack Eichel: 2+ points | 0.242 | 0.325 | 34/69 | +0.053 | STANDARD |

**TBL @ WPG** · priced 156/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROBABLE) exp shots 28.45, exp saves 24.6 (sd 6.75), pull risk 0.061
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.75, exp saves 22.33 (sd 6.15), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.463 | 0.615 | 62/39 | +0.131 | STANDARD |
| Nikita Kucherov: 2+ points | 0.270 | 0.395 | 41/62 | +0.094 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.126 | 0.225 | 25/80 | +0.062 | STANDARD |
| John Carlson: 1+ points | 0.377 | 0.465 | 47/54 | +0.066 | STANDARD |
| Cole Perfetti: 1+ assists | 0.396 | 0.310 | 32/70 | +0.061 | STANDARD |
| Nikita Kucherov: 1+ points | 0.640 | 0.725 | 76/31 | +0.035 | STANDARD |

**NJD @ TOR** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROBABLE) exp shots 32.87, exp saves 28.37 (sd 7.47), pull risk 0.065
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 26.54, exp saves 23.0 (sd 6.29), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.229 | 0.355 | 36/65 | +0.105 | STANDARD |
| John Tavares: 1+ assists | 0.245 | 0.365 | 38/65 | +0.089 | STANDARD |
| Jack Hughes: 1+ assists | 0.396 | 0.510 | 52/50 | +0.086 | STANDARD |
| Luke Evangelista: 1+ assists | 0.246 | 0.355 | 37/66 | +0.078 | STANDARD |
| Jesper Bratt: 1+ assists | 0.382 | 0.480 | 49/53 | +0.070 | STANDARD |
| Easton Cowan: 1+ points | 0.499 | 0.405 | 41/60 | +0.072 | STANDARD |

**PHI @ CGY** · priced 177/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 26.62, exp saves 23.17 (sd 6.4), pull risk 0.053
- PHI net: Dan Vladar (PROBABLE) exp shots 27.45, exp saves 23.82 (sd 6.48), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ assists | 0.261 | 0.360 | 37/65 | +0.073 | STANDARD |
| Travis Konecny: 1+ points | 0.428 | 0.500 | 52/52 | +0.034 | STANDARD |
| Porter Martone: 1+ points | 0.400 | 0.465 | 48/55 | +0.033 | STANDARD |
| Porter Martone: 1+ goals | 0.187 | 0.240 | 26/78 | +0.021 | STANDARD |
| Martin Pospisil: 1+ goals | 0.137 | 0.085 | 11/94 | +0.020 | STANDARD |
| Travis Sanheim: 1+ points | 0.380 | 0.335 | 34/67 | +0.025 | STANDARD |

**PIT @ ANA** · priced 178/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 26.45, exp saves 22.95 (sd 6.53), pull risk 0.071
- PIT net: Arturs Silovs (PROJECTED) exp shots 28.23, exp saves 23.69 (sd 6.97), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Killorn: 1+ points | 0.483 | 0.410 | 43/61 | +0.036 | STANDARD |
| Sidney Crosby: 1+ assists | 0.383 | 0.455 | 47/56 | +0.040 | STANDARD |
| Ben Kindel: 1+ points | 0.425 | 0.495 | 51/52 | +0.038 | STANDARD |
| Erik Karlsson: 1+ assists | 0.430 | 0.500 | 51/51 | +0.042 | STANDARD |
| Erik Karlsson: 1+ points | 0.515 | 0.585 | 61/44 | +0.027 | STANDARD |
| Erik Karlsson: 2+ points | 0.167 | 0.230 | 25/79 | +0.031 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
