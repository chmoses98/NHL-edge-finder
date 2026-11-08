# NHL slate 2026-11-08 — RESEARCH_ONLY

generated 2026-11-08T16:46:25Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 6 · markets on board: 2932 · contracts joined: 1333 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 1183, 'OK': 109, 'NO_EDGE': 41}
families: {'period_winner': 54, 'period_spread': 36, 'period_total': 54, 'player_assists': 181, 'game_early_goal': 6, 'first_goal': 218, 'game_winner': 12, 'player_goals': 377, 'game_overtime': 6, 'player_points': 244, 'goalie_saves': 7, 'game_spread': 24, 'team_total': 60, 'game_total': 54}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ BOS | 2026-11-08T18:00:00Z | T-60m | 0.660 | 0.340 | 0.160 | 6.53 | 3.80 | 2.74 | 220 (25/195) | PROJECTED/CONFIRMED |
| VGK @ BUF | 2026-11-08T20:30:00Z | T-3h | 0.558 | 0.442 | 0.172 | 6.45 | 3.41 | 3.03 | 232 (25/207) | PROJECTED/PROJECTED |
| TBL @ WPG | 2026-11-08T23:00:00Z | T-6h | 0.442 | 0.558 | 0.182 | 5.96 | 2.80 | 3.16 | 202 (25/177) | PROBABLE/PROJECTED |
| NJD @ TOR | 2026-11-09T00:00:00Z | T-6h | 0.457 | 0.543 | 0.171 | 6.54 | 3.12 | 3.43 | 226 (25/201) | PROBABLE/PROJECTED |
| PHI @ CGY | 2026-11-09T00:00:00Z | T-6h | 0.577 | 0.423 | 0.187 | 5.43 | 2.93 | 2.50 | 227 (25/202) | CONFIRMED/PROBABLE |
| PIT @ ANA | 2026-11-09T01:00:00Z | T-6h | 0.611 | 0.389 | 0.153 | 7.18 | 3.96 | 3.22 | 226 (25/201) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 | team_total | 0.460 | 0.590 | 0.564 | 60 | 42 | no | +0.103 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI4 | team_total | 0.251 | 0.380 | 0.352 | 39 | 63 | no | +0.102 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI2 | team_total | 0.706 | 0.805 | 0.787 | 81 | 20 | no | +0.083 | OK |
| KXNHLGAME-26NOV08PHICGY-CGY | game_winner | 0.577 | 0.475 | 0.495 | 48 | 53 | yes | +0.079 | OK |
| KXNHLGAME-26NOV08PHICGY-PHI | game_winner | 0.423 | 0.525 | 0.505 | 53 | 48 | no | +0.079 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI2 | game_spread | 0.209 | 0.305 | 0.284 | 31 | 70 | no | +0.076 | OK |
| KXNHLGAME-26NOV08PITANA-ANA | game_winner | 0.611 | 0.515 | 0.534 | 52 | 49 | yes | +0.073 | OK |
| KXNHLTEAMTOTAL-26NOV08FLABOS-BOS3 | team_total | 0.738 | 0.645 | 0.665 | 65 | 36 | yes | +0.072 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA2 | game_spread | 0.407 | 0.315 | 0.332 | 32 | 69 | yes | +0.071 | OK |
| KXNHLTOTAL-26NOV08PHICGY-5 | game_total | 0.666 | 0.755 | 0.738 | 76 | 25 | no | +0.071 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI3 | game_spread | 0.111 | 0.195 | 0.175 | 20 | 81 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26NOV08FLABOS-BOS5 | team_total | 0.340 | 0.255 | 0.271 | 26 | 75 | yes | +0.066 | OK |
| KXNHLTOTAL-26NOV08PHICGY-6 | game_total | 0.427 | 0.515 | 0.497 | 52 | 49 | no | +0.066 | OK |
| KXNHLSPREAD-26NOV08FLABOS-BOS2 | game_spread | 0.442 | 0.355 | 0.372 | 36 | 65 | yes | +0.065 | OK |
| KXNHLTOTAL-26NOV08PHICGY-7 | game_total | 0.319 | 0.405 | 0.387 | 41 | 60 | no | +0.065 | OK |
| KXNHLGAME-26NOV08FLABOS-BOS | game_winner | 0.660 | 0.575 | 0.593 | 58 | 43 | yes | +0.063 | OK |
| KXNHLGAME-26NOV08FLABOS-FLA | game_winner | 0.340 | 0.425 | 0.407 | 43 | 58 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26NOV08FLABOS-BOS4 | team_total | 0.539 | 0.450 | 0.468 | 46 | 56 | yes | +0.062 | OK |
| KXNHLSPREAD-26NOV08FLABOS-BOS3 | game_spread | 0.303 | 0.225 | 0.239 | 23 | 78 | yes | +0.061 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT2 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA4 | team_total | 0.572 | 0.490 | 0.507 | 50 | 52 | yes | +0.055 | OK |
| KXNHLTOTAL-26NOV08TBWPG-6 | game_total | 0.519 | 0.595 | 0.580 | 60 | 41 | no | +0.054 | OK |
| KXNHLGAME-26NOV08PITANA-PIT | game_winner | 0.389 | 0.465 | 0.450 | 47 | 54 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV08FLABOS-BOS6 | team_total | 0.180 | 0.095 | 0.109 | 12 | 93 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA5 | team_total | 0.377 | 0.295 | 0.311 | 31 | 72 | yes | +0.052 | OK |
| KXNHLSPREAD-26NOV08FLABOS-FLA2 | game_spread | 0.166 | 0.235 | 0.220 | 24 | 77 | no | +0.051 | OK |
| KXNHLTOTAL-26NOV08PHICGY-4 | game_total | 0.770 | 0.840 | 0.828 | 85 | 17 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA6 | team_total | 0.209 | 0.140 | 0.152 | 15 | 87 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26NOV08FLABOS-BOS2 | team_total | 0.889 | 0.825 | 0.840 | 83 | 18 | yes | +0.049 | OK |
| KXNHLTOTAL-26NOV08PHICGY-8 | game_total | 0.159 | 0.225 | 0.210 | 23 | 78 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI5 | team_total | 0.113 | 0.190 | 0.172 | 21 | 83 | no | +0.047 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT3 | game_spread | 0.125 | 0.185 | 0.171 | 19 | 82 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA3 | team_total | 0.759 | 0.695 | 0.709 | 70 | 31 | yes | +0.045 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA3 | game_spread | 0.277 | 0.215 | 0.226 | 22 | 79 | yes | +0.044 | OK |
| KXNHLTOTAL-26NOV08TBWPG-7 | game_total | 0.409 | 0.475 | 0.462 | 48 | 53 | no | +0.043 | OK |
| KXNHLSPREAD-26NOV08PHICGY-CGY2 | game_spread | 0.327 | 0.265 | 0.277 | 27 | 74 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV08FLABOS-FLA4 | team_total | 0.301 | 0.365 | 0.352 | 37 | 64 | no | +0.043 | OK |
| KXNHLSPREAD-26NOV08FLABOS-FLA3 | game_spread | 0.089 | 0.150 | 0.136 | 16 | 86 | no | +0.042 | OK |
| KXNHLGAME-26NOV08VGKBUF-BUF | game_winner | 0.558 | 0.495 | 0.508 | 50 | 51 | yes | +0.041 | OK |
| KXNHLGAME-26NOV08VGKBUF-VGK | game_winner | 0.442 | 0.505 | 0.492 | 51 | 50 | no | +0.041 | OK |
| KXNHLTOTAL-26NOV08TBWPG-5 | game_total | 0.739 | 0.795 | 0.785 | 80 | 21 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV08VGKBUF-VGK2 | game_spread | 0.237 | 0.295 | 0.283 | 30 | 71 | no | +0.038 | OK |
| KXNHLSPREAD-26NOV08VGKBUF-BUF2 | game_spread | 0.340 | 0.285 | 0.296 | 29 | 72 | yes | +0.035 | OK |
| KXNHLTOTAL-26NOV08PHICGY-9 | game_total | 0.106 | 0.155 | 0.144 | 16 | 85 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV08TBWPG-4 | game_total | 0.829 | 0.875 | 0.867 | 88 | 13 | no | +0.033 | OK |
| KXNHLSPREAD-26NOV08VGKBUF-VGK3 | game_spread | 0.138 | 0.190 | 0.179 | 20 | 82 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF4 | team_total | 0.457 | 0.405 | 0.415 | 41 | 60 | yes | +0.030 | OK |
| KXNHLGAME-26NOV08NJTOR-NJ | game_winner | 0.543 | 0.595 | 0.585 | 60 | 41 | no | +0.030 | OK |
| KXNHLGAME-26NOV08NJTOR-TOR | game_winner | 0.457 | 0.405 | 0.415 | 41 | 60 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV08FLABOS-FLA3 | team_total | 0.513 | 0.565 | 0.555 | 57 | 44 | no | +0.029 | OK |
| KXNHLTOTAL-26NOV08FLABOS-8 | game_total | 0.311 | 0.260 | 0.270 | 27 | 75 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV08TBWPG-8 | game_total | 0.230 | 0.275 | 0.266 | 28 | 73 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB4 | team_total | 0.398 | 0.450 | 0.439 | 46 | 56 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-VGK4 | team_total | 0.368 | 0.420 | 0.409 | 43 | 59 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF6 | team_total | 0.131 | 0.090 | 0.097 | 10 | 92 | yes | +0.025 | OK |
| KXNHLTOTAL-26NOV08FLABOS-7 | game_total | 0.502 | 0.455 | 0.464 | 46 | 55 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI6 | team_total | 0.041 | 0.075 | 0.067 | 8 | 93 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV08NJTOR-9 | game_total | 0.225 | 0.185 | 0.192 | 19 | 82 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT3 | team_total | 0.621 | 0.670 | 0.660 | 68 | 34 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB5 | team_total | 0.214 | 0.260 | 0.250 | 27 | 75 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB3 | team_total | 0.622 | 0.670 | 0.661 | 68 | 34 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR5 | team_total | 0.212 | 0.170 | 0.178 | 18 | 84 | yes | +0.022 | OK |
| KXNHLTOTAL-26NOV08FLABOS-9 | game_total | 0.223 | 0.185 | 0.192 | 19 | 82 | yes | +0.022 | OK |
| KXNHLTOTAL-26NOV08TBWPG-9 | game_total | 0.158 | 0.195 | 0.187 | 20 | 81 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-BUF5 | team_total | 0.263 | 0.220 | 0.228 | 23 | 79 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV08PITANA-8 | game_total | 0.406 | 0.365 | 0.373 | 37 | 64 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB2 | team_total | 0.822 | 0.860 | 0.853 | 87 | 15 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3 | team_total | 0.606 | 0.560 | 0.569 | 57 | 45 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG3 | team_total | 0.534 | 0.575 | 0.567 | 58 | 43 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT2 | team_total | 0.823 | 0.860 | 0.853 | 87 | 15 | no | +0.018 | OK |
| KXNHLSPREAD-26NOV08TBWPG-TB3 | game_spread | 0.201 | 0.235 | 0.228 | 24 | 77 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV08FLABOS-6 | game_total | 0.613 | 0.575 | 0.583 | 58 | 43 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-VGK5 | team_total | 0.192 | 0.230 | 0.222 | 24 | 78 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG4 | team_total | 0.319 | 0.360 | 0.352 | 37 | 65 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV08NJTOR-7 | game_total | 0.503 | 0.465 | 0.473 | 47 | 54 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV08VGKBUF-VGK3 | team_total | 0.589 | 0.630 | 0.622 | 64 | 38 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR4 | team_total | 0.391 | 0.350 | 0.358 | 36 | 66 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV08TBWPG-10 | game_total | 0.070 | 0.100 | 0.093 | 11 | 91 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV08NJTOR-8 | game_total | 0.308 | 0.270 | 0.277 | 28 | 74 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV08VGKBUF-BUF3 | game_spread | 0.215 | 0.185 | 0.191 | 19 | 82 | yes | +0.014 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ BOS | 0.660 | 0.627 | 0.160 | 0.208 | 6.53 | 6.66 | 0.968/1.015 | KXNHLTEAMTOTAL-26NOV08FLABOS-FLA3 +0.047 |
| VGK @ BUF | 0.558 | 0.495 | 0.172 | 0.215 | 6.45 | 6.35 | 0.998/1.004 | KXNHLGAME-26NOV08VGKBUF-BUF -0.064 |
| TBL @ WPG | 0.442 | 0.483 | 0.182 | 0.224 | 5.96 | 6.16 | 1.002/0.958 | KXNHLTEAMTOTAL-26NOV08TBWPG-WPG3 +0.060 |
| NJD @ TOR | 0.457 | 0.502 | 0.171 | 0.219 | 6.54 | 6.34 | 0.960/0.959 | KXNHLSPREAD-26NOV08NJTOR-NJ2 -0.049 |
| PHI @ CGY | 0.577 | 0.503 | 0.187 | 0.226 | 5.43 | 5.97 | 0.978/0.994 | KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 +0.122 |
| PIT @ ANA | 0.611 | 0.618 | 0.153 | 0.198 | 7.18 | 7.27 | 1.030/1.033 | KXNHLTOTAL-26NOV08PITANA-7 +0.020 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 21 recommended · full analysis in card.md / packet.json `thesis_card`

- Pavel Zacha: 1+ goals YES @ 29c · p 0.3367 (adj 0.3238) · $4.85 · thesis BOS:OFFENSE_4PLUS
- Sam Bennett: 1+ goals YES @ 25c · p 0.2949 (adj 0.2812) · $4.23 · thesis FLA:OFFENSE_4PLUS
- Sam Reinhart: 1+ assists NO @ 62c · p 0.6921 (adj 0.6511) · $7.85 · thesis FLA:SUPPRESSED
- Fraser Minten: 1+ goals YES @ 20c · p 0.2329 (adj 0.2234) · $2.62 · thesis BOS:OFFENSE_4PLUS
- Victor Olofsson: 1+ assists NO @ 75c · p 0.8364 (adj 0.7882) · $14.45 · thesis VGK:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 5c · p 0.072 (adj 0.0665) · $2.37 · thesis VGK:OFFENSE_4PLUS
- Mark Stone: 1+ assists NO @ 56c · p 0.6262 (adj 0.5906) · $5.9 · thesis VGK:SUPPRESSED
- Charle-Edouard D'Astous: 1+ goals NO @ 89c · p 0.9206 (adj 0.9117) · $14.45 · thesis TBL:SUPPRESSED
- Cole Perfetti: 1+ assists YES @ 32c · p 0.396 (adj 0.3555) · $4.75 · thesis WPG:OFFENSE_4PLUS
- Alex Iafallo: 1+ goals YES @ 13c · p 0.1587 (adj 0.1503) · $2.28 · thesis WPG:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 77c · p 0.8211 (adj 0.7931) · $5.89 · thesis WPG:WINS
- Teddy Blueger: 1+ goals YES @ 10c · p 0.1464 (adj 0.1323) · $4.74 · thesis TOR:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 61c · p 0.6684 (adj 0.6513) · $11.9 · thesis NJD:SUPPRESSED
- Easton Cowan: 1+ goals YES @ 18c · p 0.2221 (adj 0.2091) · $4.22 · thesis TOR:OFFENSE_4PLUS
- John Tavares: 1+ assists NO @ 64c · p 0.7545 (adj 0.6736) · $11.81 · thesis TOR:SUPPRESSED
- Travis Konecny: 1+ assists NO @ 65c · p 0.7386 (adj 0.6893) · $13.44 · thesis PHI:SUPPRESSED
- Porter Martone: 1+ goals NO @ 78c · p 0.813 (adj 0.8022) · $8.16 · thesis PHI:SUPPRESSED
- Anaheim wins by over 1.5 goals YES @ 32c · p 0.4122 (adj 0.3636) · $5.15 · thesis ANA:WINS_BY_2PLUS
- Pittsburgh wins by over 1.5 goals NO @ 71c · p 0.7969 (adj 0.751) · $14.45 · thesis ANA:WINS
- Beckett Sennecke: 1+ goals YES @ 36c · p 0.4063 (adj 0.3935) · $3.07 · thesis ANA:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1601 (adj 0.1501) · $3.42 · thesis PIT:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ BOS** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.87, exp saves 24.43 (sd 6.48), pull risk 0.053
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 26.05, exp saves 21.93 (sd 6.41), pull risk 0.096

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Bennett: 1+ points | 0.524 | 0.425 | 44/59 | +0.066 | STANDARD |
| Sam Reinhart: 1+ assists | 0.308 | 0.390 | 40/62 | +0.056 | STANDARD |
| Sam Reinhart: 1+ points | 0.504 | 0.575 | 59/44 | +0.039 | STANDARD |
| Fraser Minten: 1+ points | 0.450 | 0.380 | 39/63 | +0.043 | STANDARD |
| Fraser Minten: 1+ assists | 0.284 | 0.215 | 22/79 | +0.052 | STANDARD |
| Sam Bennett: 1+ goals | 0.295 | 0.240 | 25/77 | +0.032 | STANDARD |

**VGK @ BUF** · priced 180/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 27.36, exp saves 23.64 (sd 6.57), pull risk 0.065
- VGK net: Adin Hill (PROJECTED) exp shots 27.71, exp saves 23.93 (sd 6.63), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Colten Ellis: 24+ saves | 0.504 | 0.325 | 49/84 | -0.003 |  |
| Victor Olofsson: 1+ points | 0.315 | 0.420 | 44/60 | +0.068 | STANDARD |
| Mitch Marner: 1+ assists | 0.408 | 0.510 | 52/50 | +0.075 | STANDARD |
| Victor Olofsson: 1+ assists | 0.164 | 0.260 | 27/75 | +0.073 | STANDARD |
| Jack Eichel: 1+ assists | 0.440 | 0.530 | 54/48 | +0.063 | STANDARD |
| Mitch Marner: 1+ points | 0.542 | 0.630 | 64/38 | +0.061 | STANDARD |

**TBL @ WPG** · priced 150/151 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROBABLE) exp shots 28.45, exp saves 24.6 (sd 6.75), pull risk 0.061
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.75, exp saves 22.33 (sd 6.15), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Stuart Skinner: 24+ saves | 0.561 | 0.350 | 54/84 | +0.003 |  |
| Nikita Kucherov: 1+ assists | 0.463 | 0.610 | 62/40 | +0.120 | STANDARD |
| Nikita Kucherov: 2+ points | 0.270 | 0.400 | 42/62 | +0.094 | STANDARD |
| Andrei Vasilevskiy: 23+ saves | 0.482 | 0.365 | 57/84 | -0.105 |  |
| Nikita Kucherov: 2+ assists | 0.126 | 0.235 | 26/79 | +0.072 | STANDARD |
| John Carlson: 1+ points | 0.377 | 0.465 | 47/54 | +0.066 | STANDARD |

**NJD @ TOR** · priced 172/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROBABLE) exp shots 32.87, exp saves 28.37 (sd 7.47), pull risk 0.065
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 26.54, exp saves 23.0 (sd 6.29), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Tavares: 1+ assists | 0.245 | 0.370 | 38/64 | +0.098 | STANDARD |
| Jack Hughes: 2+ points | 0.229 | 0.350 | 36/66 | +0.095 | STANDARD |
| Jack Hughes: 1+ assists | 0.396 | 0.510 | 52/50 | +0.086 | STANDARD |
| Luke Evangelista: 1+ assists | 0.246 | 0.355 | 37/66 | +0.078 | STANDARD |
| Easton Cowan: 1+ points | 0.499 | 0.405 | 41/60 | +0.072 | STANDARD |
| Jesper Bratt: 1+ assists | 0.382 | 0.475 | 49/54 | +0.060 | STANDARD |

**PHI @ CGY** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 26.62, exp saves 23.17 (sd 6.4), pull risk 0.053
- PHI net: Dan Vladar (PROBABLE) exp shots 27.45, exp saves 23.82 (sd 6.48), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dan Vladar: 26+ saves | 0.391 | 0.270 | 51/97 | -0.137 |  |
| Travis Konecny: 1+ assists | 0.261 | 0.360 | 37/65 | +0.073 | STANDARD |
| Travis Konecny: 1+ points | 0.428 | 0.505 | 51/50 | +0.054 | STANDARD |
| Porter Martone: 1+ points | 0.400 | 0.460 | 47/55 | +0.033 | STANDARD |
| Travis Konecny: 2+ points | 0.108 | 0.160 | 18/86 | +0.023 | STANDARD |
| Porter Martone: 1+ goals | 0.187 | 0.230 | 24/78 | +0.021 | STANDARD |

**PIT @ ANA** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 26.45, exp saves 22.95 (sd 6.53), pull risk 0.071
- PIT net: Arturs Silovs (PROJECTED) exp shots 28.23, exp saves 23.69 (sd 6.97), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Arturs Silovs: 25+ saves | 0.461 | 0.275 | 52/97 | -0.076 |  |
| Erik Karlsson: 1+ assists | 0.430 | 0.510 | 52/50 | +0.052 | STANDARD |
| Alex Killorn: 1+ points | 0.483 | 0.410 | 42/60 | +0.046 | STANDARD |
| Erik Karlsson: 1+ points | 0.515 | 0.585 | 60/43 | +0.037 | STANDARD |
| Sidney Crosby: 1+ assists | 0.383 | 0.450 | 46/56 | +0.040 | STANDARD |
| Beckett Sennecke: 2+ points | 0.341 | 0.275 | 30/75 | +0.027 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
