# NHL slate 2026-10-17 — RESEARCH_ONLY

generated 2026-10-17T20:01:11Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 11 · markets on board: 4657 · contracts joined: 2426 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2151, 'OK': 206, 'NO_EDGE': 69}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 328, 'game_early_goal': 11, 'first_goal': 406, 'game_winner': 22, 'player_goals': 691, 'game_overtime': 11, 'player_points': 421, 'goalie_saves': 19, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ FLA | 2026-10-17T22:00:00Z | T-90m | 0.517 | 0.483 | 0.175 | 6.58 | 3.35 | 3.23 | 215 (25/190) | CONFIRMED/PROJECTED |
| NYI @ TOR | 2026-10-17T23:00:00Z | T-90m | 0.470 | 0.530 | 0.173 | 6.33 | 3.07 | 3.26 | 234 (25/209) | CONFIRMED/PROBABLE |
| BUF @ MTL | 2026-10-17T23:00:00Z | T-90m | 0.517 | 0.483 | 0.178 | 6.19 | 3.15 | 3.04 | 217 (25/192) | CONFIRMED/PROBABLE |
| SJS @ DET | 2026-10-17T23:00:00Z | T-90m | 0.550 | 0.450 | 0.179 | 5.95 | 3.14 | 2.81 | 229 (25/204) | CONFIRMED/CONFIRMED |
| OTT @ PHI | 2026-10-17T23:00:00Z | T-90m | 0.489 | 0.511 | 0.183 | 5.58 | 2.76 | 2.82 | 237 (25/212) | CONFIRMED/CONFIRMED |
| NYR @ CBJ | 2026-10-17T23:00:00Z | T-90m | 0.531 | 0.469 | 0.177 | 5.82 | 3.00 | 2.82 | 217 (25/192) | PROBABLE/CONFIRMED |
| DAL @ CHI | 2026-10-17T23:00:00Z | T-90m | 0.464 | 0.536 | 0.188 | 5.60 | 2.70 | 2.90 | 206 (25/181) | CONFIRMED/CONFIRMED |
| STL @ NSH | 2026-10-18T00:00:00Z | T-3h | 0.538 | 0.462 | 0.170 | 6.88 | 3.56 | 3.32 | 217 (25/192) | PROBABLE/CONFIRMED |
| BOS @ LAK | 2026-10-18T01:00:00Z | T-3h | 0.511 | 0.489 | 0.187 | 5.60 | 2.83 | 2.77 | 218 (25/193) | PROBABLE/PROJECTED |
| EDM @ UTA | 2026-10-18T02:00:00Z | T-3h | 0.560 | 0.440 | 0.169 | 6.72 | 3.56 | 3.16 | 221 (25/196) | PROBABLE/CONFIRMED |
| PIT @ VGK | 2026-10-18T02:00:00Z | T-3h | 0.600 | 0.400 | 0.156 | 6.86 | 3.78 | 3.09 | 215 (25/190) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL4 | team_total | 0.341 | 0.495 | 0.463 | 50 | 51 | no | +0.131 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL3 | team_total | 0.561 | 0.710 | 0.682 | 72 | 30 | no | +0.125 | OK |
| KXNHLGAME-26OCT17DALCHI-CHI | game_winner | 0.464 | 0.335 | 0.359 | 34 | 67 | yes | +0.108 | OK |
| KXNHLGAME-26OCT17DALCHI-DAL | game_winner | 0.536 | 0.665 | 0.641 | 67 | 34 | no | +0.108 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL2 | game_spread | 0.297 | 0.425 | 0.398 | 43 | 58 | no | +0.106 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL3 | game_spread | 0.172 | 0.295 | 0.267 | 30 | 71 | no | +0.104 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4 | team_total | 0.416 | 0.290 | 0.314 | 30 | 72 | yes | +0.102 | OK |
| KXNHLGAME-26OCT17SEAFLA-FLA | game_winner | 0.517 | 0.635 | 0.612 | 64 | 37 | no | +0.096 | OK |
| KXNHLGAME-26OCT17SEAFLA-SEA | game_winner | 0.483 | 0.365 | 0.388 | 37 | 64 | yes | +0.096 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL5 | team_total | 0.172 | 0.295 | 0.267 | 31 | 72 | no | +0.094 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA3 | team_total | 0.629 | 0.510 | 0.534 | 52 | 50 | yes | +0.092 | OK |
| KXNHLTOTAL-26OCT17STLNSH-8 | game_total | 0.355 | 0.245 | 0.265 | 25 | 76 | yes | +0.092 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL2 | team_total | 0.779 | 0.880 | 0.864 | 89 | 13 | no | +0.083 | OK |
| KXNHLTOTAL-26OCT17STLNSH-7 | game_total | 0.557 | 0.455 | 0.475 | 46 | 55 | yes | +0.079 | OK |
| KXNHLTOTAL-26OCT17STLNSH-6 | game_total | 0.666 | 0.565 | 0.586 | 57 | 44 | yes | +0.079 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH4 | team_total | 0.483 | 0.385 | 0.404 | 39 | 62 | yes | +0.076 | OK |
| KXNHLTOTAL-26OCT17DALCHI-5 | game_total | 0.693 | 0.785 | 0.768 | 79 | 22 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-SEA2 | game_spread | 0.276 | 0.185 | 0.201 | 19 | 82 | yes | +0.075 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA2 | game_spread | 0.309 | 0.405 | 0.385 | 41 | 60 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA5 | team_total | 0.233 | 0.140 | 0.156 | 15 | 87 | yes | +0.074 | OK |
| KXNHLTOTAL-26OCT17STLNSH-9 | game_total | 0.264 | 0.175 | 0.191 | 18 | 83 | yes | +0.073 | OK |
| KXNHLTOTAL-26OCT17DALCHI-6 | game_total | 0.460 | 0.555 | 0.536 | 56 | 45 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA3 | game_spread | 0.194 | 0.285 | 0.265 | 29 | 72 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH5 | team_total | 0.292 | 0.200 | 0.217 | 21 | 81 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4 | team_total | 0.322 | 0.420 | 0.400 | 43 | 59 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT17DALCHI-CHI2 | game_spread | 0.246 | 0.165 | 0.179 | 17 | 84 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH3 | team_total | 0.691 | 0.600 | 0.619 | 61 | 41 | yes | +0.064 | OK |
| KXNHLTOTAL-26OCT17DALCHI-7 | game_total | 0.350 | 0.435 | 0.417 | 44 | 57 | no | +0.063 | OK |
| KXNHLGAME-26OCT17OTTPHI-PHI | game_winner | 0.489 | 0.405 | 0.422 | 41 | 60 | yes | +0.062 | OK |
| KXNHLGAME-26OCT17OTTPHI-OTT | game_winner | 0.511 | 0.595 | 0.578 | 60 | 41 | no | +0.062 | OK |
| KXNHLGAME-26OCT17NYITOR-NYI | game_winner | 0.530 | 0.445 | 0.462 | 45 | 56 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT3 | team_total | 0.545 | 0.625 | 0.609 | 63 | 38 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT17DALCHI-4 | game_total | 0.793 | 0.865 | 0.853 | 87 | 14 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT17SJDET-DET4 | team_total | 0.395 | 0.475 | 0.459 | 48 | 53 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT17BOSLA-5 | game_total | 0.690 | 0.765 | 0.751 | 77 | 24 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA4 | team_total | 0.326 | 0.410 | 0.393 | 42 | 60 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA3 | team_total | 0.547 | 0.630 | 0.614 | 64 | 38 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH6 | team_total | 0.150 | 0.080 | 0.091 | 9 | 93 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-5 | game_total | 0.725 | 0.795 | 0.782 | 80 | 21 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-7 | game_total | 0.389 | 0.465 | 0.450 | 47 | 54 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-4 | game_total | 0.819 | 0.885 | 0.874 | 89 | 12 | no | +0.053 | OK |
| KXNHLGAME-26OCT17NYITOR-TOR | game_winner | 0.470 | 0.545 | 0.530 | 55 | 46 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-6 | game_total | 0.501 | 0.575 | 0.560 | 58 | 43 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL6 | team_total | 0.071 | 0.135 | 0.119 | 14 | 87 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA2 | team_total | 0.823 | 0.755 | 0.770 | 76 | 25 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT17NYITOR-NYI2 | game_spread | 0.313 | 0.245 | 0.258 | 25 | 76 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT17DALCHI-8 | game_total | 0.178 | 0.245 | 0.230 | 25 | 76 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT3 | game_spread | 0.159 | 0.225 | 0.210 | 23 | 78 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT17SJDET-5 | game_total | 0.741 | 0.805 | 0.793 | 81 | 20 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR3 | game_spread | 0.152 | 0.215 | 0.201 | 22 | 79 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT4 | team_total | 0.382 | 0.315 | 0.328 | 32 | 69 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT2 | game_spread | 0.278 | 0.345 | 0.331 | 35 | 66 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH2 | team_total | 0.866 | 0.805 | 0.819 | 81 | 20 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA6 | team_total | 0.109 | 0.055 | 0.063 | 6 | 95 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT17SEAFLA-7 | game_total | 0.512 | 0.445 | 0.458 | 45 | 56 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT17SJDET-DET3 | team_total | 0.609 | 0.675 | 0.662 | 68 | 33 | no | +0.045 | OK |
| KXNHLGAME-26OCT17PITVGK-PIT | game_winner | 0.400 | 0.335 | 0.348 | 34 | 67 | yes | +0.044 | OK |
| KXNHLTOTAL-26OCT17SJDET-7 | game_total | 0.409 | 0.475 | 0.462 | 48 | 53 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT17PITVGK-VGK3 | game_spread | 0.262 | 0.325 | 0.312 | 33 | 68 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT2 | team_total | 0.766 | 0.830 | 0.819 | 84 | 18 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT17STLNSH-5 | game_total | 0.844 | 0.785 | 0.798 | 79 | 22 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT17DALCHI-9 | game_total | 0.118 | 0.175 | 0.162 | 18 | 83 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT17BOSLA-7 | game_total | 0.351 | 0.420 | 0.406 | 43 | 59 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17SJDET-6 | game_total | 0.521 | 0.585 | 0.572 | 59 | 42 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17STLNSH-10 | game_total | 0.138 | 0.080 | 0.089 | 9 | 93 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR2 | game_spread | 0.263 | 0.330 | 0.316 | 34 | 68 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17BOSLA-6 | game_total | 0.461 | 0.530 | 0.516 | 54 | 48 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17SEAFLA-8 | game_total | 0.315 | 0.255 | 0.266 | 26 | 75 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-SEA3 | game_spread | 0.168 | 0.115 | 0.124 | 12 | 89 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT17SJDET-4 | game_total | 0.832 | 0.885 | 0.876 | 89 | 12 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT17BOSLA-4 | game_total | 0.790 | 0.845 | 0.835 | 85 | 16 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-8 | game_total | 0.207 | 0.265 | 0.253 | 27 | 74 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT5 | team_total | 0.209 | 0.155 | 0.165 | 16 | 85 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA5 | team_total | 0.159 | 0.225 | 0.210 | 24 | 79 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT17NYRCBJ-CBJ4 | team_total | 0.364 | 0.430 | 0.417 | 44 | 58 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT17BUFMTL-7 | game_total | 0.444 | 0.505 | 0.493 | 51 | 50 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA2 | team_total | 0.772 | 0.830 | 0.819 | 84 | 18 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT17BOSLA-8 | game_total | 0.180 | 0.235 | 0.223 | 24 | 77 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT17NYITOR-NYI4 | team_total | 0.423 | 0.365 | 0.376 | 37 | 64 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT17BOSLA-LA3 | game_spread | 0.162 | 0.215 | 0.203 | 22 | 79 | no | +0.037 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ FLA | 0.517 | 0.516 | 0.175 | 0.218 | 6.58 | 6.31 | 1.015/1.005 | KXNHLTOTAL-26OCT17SEAFLA-6 -0.044 |
| NYI @ TOR | 0.470 | 0.507 | 0.173 | 0.218 | 6.33 | 6.31 | 0.988/0.952 | KXNHLSPREAD-26OCT17NYITOR-NYI2 -0.038 |
| BUF @ MTL | 0.517 | 0.519 | 0.178 | 0.222 | 6.19 | 6.44 | 0.983/1.000 | KXNHLTOTAL-26OCT17BUFMTL-7 +0.051 |
| SJS @ DET | 0.550 | 0.519 | 0.179 | 0.219 | 5.95 | 6.21 | 0.994/1.021 | KXNHLTEAMTOTAL-26OCT17SJDET-SJ3 +0.055 |
| OTT @ PHI | 0.489 | 0.476 | 0.183 | 0.231 | 5.58 | 5.69 | 0.994/0.968 | KXNHLTOTAL-26OCT17OTTPHI-5 +0.024 |
| NYR @ CBJ | 0.531 | 0.559 | 0.177 | 0.219 | 5.82 | 6.06 | 0.955/0.988 | KXNHLTEAMTOTAL-26OCT17NYRCBJ-CBJ3 +0.051 |
| DAL @ CHI | 0.464 | 0.467 | 0.188 | 0.221 | 5.60 | 6.16 | 0.988/0.994 | KXNHLTOTAL-26OCT17DALCHI-7 +0.098 |
| STL @ NSH | 0.538 | 0.506 | 0.170 | 0.222 | 6.88 | 6.48 | 1.002/1.032 | KXNHLTOTAL-26OCT17STLNSH-6 -0.062 |
| BOS @ LAK | 0.511 | 0.540 | 0.187 | 0.222 | 5.60 | 6.05 | 0.988/0.968 | KXNHLTOTAL-26OCT17BOSLA-7 +0.078 |
| EDM @ UTA | 0.560 | 0.528 | 0.169 | 0.214 | 6.72 | 6.89 | 0.991/1.023 | KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM4 +0.047 |
| PIT @ VGK | 0.600 | 0.630 | 0.156 | 0.204 | 6.86 | 6.49 | 1.004/1.021 | KXNHLTOTAL-26OCT17PITVGK-6 -0.061 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 40 recommended · full analysis in card.md / packet.json `thesis_card`

- Ben Meyers: 1+ goals YES @ 10c · p 0.1478 (adj 0.1346) · $2.51 · thesis SEA:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 63c · p 0.7086 (adj 0.6877) · $5.74 · thesis FLA:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 11c · p 0.1554 (adj 0.1403) · $2.08 · thesis SEA:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.6937 (adj 0.6765) · $5.62 · thesis FLA:SUPPRESSED
- Jean-Gabriel Pageau: 1+ goals YES @ 14c · p 0.1664 (adj 0.1585) · $1.11 · thesis NYI:OFFENSE_4PLUS
- Gavin McKenna: 1+ assists NO @ 71c · p 0.7684 (adj 0.7367) · $4.69 · thesis TOR:SUPPRESSED
- Ilya Sorokin: 26+ saves NO @ 53c · p 0.6922 (adj 0.5593) · $3.04 · thesis NYI:NET_LOW_VOLUME
- Owen Power: 1+ goals NO @ 86c · p 0.9039 (adj 0.8917) · $7.57 · thesis BUF:SUPPRESSED
- Ryan McLeod: 1+ goals YES @ 15c · p 0.183 (adj 0.1723) · $1.44 · thesis BUF:OFFENSE_4PLUS
- Chris Kreider: 1+ goals NO @ 73c · p 0.7669 (adj 0.7564) · $4.83 · thesis MTL:SUPPRESSED
- Zach Benson: 1+ goals YES @ 24c · p 0.2763 (adj 0.2647) · $1.48 · thesis BUF:OFFENSE_4PLUS
- Nate Danielson: 1+ goals NO @ 83c · p 0.884 (adj 0.8692) · $5.98 · thesis DET:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 70c · p 0.8093 (adj 0.7318) · $5.01 · thesis SJS:SUPPRESSED
- Macklin Celebrini: 2+ assists NO @ 83c · p 0.901 (adj 0.853) · $5.98 · thesis SJS:SUPPRESSED
- Detroit over 3.5 goals scored NO @ 53c · p 0.599 (adj 0.562) · $1.97 · thesis DET:SUPPRESSED
- Tim Stutzle: 1+ assists NO @ 49c · p 0.626 (adj 0.5311) · $4.36 · thesis OTT:SUPPRESSED
- Porter Martone: 1+ goals NO @ 78c · p 0.8224 (adj 0.8105) · $7.57 · thesis PHI:SUPPRESSED
- Dylan Cozens: 1+ goals NO @ 72c · p 0.7631 (adj 0.7511) · $5.32 · thesis OTT:SUPPRESSED
- J.T. Miller: 1+ assists NO @ 58c · p 0.6558 (adj 0.6154) · $3.56 · thesis NYR:SUPPRESSED
- Will Cuylle: 1+ goals NO @ 78c · p 0.8126 (adj 0.8032) · $4.62 · thesis NYR:SUPPRESSED
- Pavel Dorofeyev: 1+ goals NO @ 69c · p 0.7277 (adj 0.7158) · $2.16 · thesis NYR:SUPPRESSED
- Anton Frondell: 1+ goals YES @ 19c · p 0.2475 (adj 0.2306) · $3.24 · thesis CHI:OFFENSE_4PLUS
- Frank Nazar: 1+ goals YES @ 19c · p 0.2415 (adj 0.2274) · $2.93 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 24c · p 0.295 (adj 0.28) · $3.3 · thesis CHI:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 11c · p 0.1484 (adj 0.1351) · $1.71 · thesis CHI:OFFENSE_4PLUS
- Adam Wilsby: 1+ goals YES @ 4c · p 0.0706 (adj 0.063) · $1.7 · thesis NSH:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 24c · p 0.2836 (adj 0.2715) · $2.11 · thesis STL:OFFENSE_4PLUS
- Jake Neighbours: 1+ assists YES @ 24c · p 0.3083 (adj 0.2666) · $1.38 · thesis STL:OFFENSE_4PLUS
- Charlie McAvoy: 1+ assists NO @ 59c · p 0.6746 (adj 0.6298) · $6.76 · thesis BOS:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 48c · p 0.6051 (adj 0.5205) · $4.43 · thesis LAK:SUPPRESSED
- Hampus Lindholm: 1+ assists YES @ 25c · p 0.3209 (adj 0.2804) · $2.06 · thesis BOS:OFFENSE_4PLUS
- Elias Lindholm: 1+ goals YES @ 20c · p 0.2332 (adj 0.2224) · $1.6 · thesis BOS:OFFENSE_4PLUS
- Nate Schmidt: 1+ goals YES @ 4c · p 0.0666 (adj 0.0587) · $1.34 · thesis UTA:OFFENSE_4PLUS
- Zach Hyman: 2+ goals YES @ 5c · p 0.0736 (adj 0.0677) · $1.06 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 71c · p 0.7978 (adj 0.7514) · $7.57 · thesis EDM:SUPPRESSED
- Zach Hyman: 1+ goals YES @ 30c · p 0.358 (adj 0.3422) · $3.2 · thesis EDM:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 67c · p 0.7344 (adj 0.7171) · $7.57 · thesis VGK:SUPPRESSED
- Evgeni Malkin: 1+ assists NO @ 63c · p 0.7155 (adj 0.6703) · $7.06 · thesis PIT:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0836 (adj 0.0752) · $1.03 · thesis VGK:WINS_BY_2PLUS
- Bryan Rust: 1+ goals YES @ 24c · p 0.286 (adj 0.272) · $2.55 · thesis PIT:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ FLA** · priced 160/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 25.35, exp saves 22.01 (sd 6.12), pull risk 0.056
- SEA net: Joey Daccord (PROJECTED) exp shots 29.28, exp saves 25.19 (sd 6.88), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brady Tkachuk: 1+ assists | 0.293 | 0.405 | 42/61 | +0.080 | STANDARD |
| Kaapo Kakko: 1+ points | 0.470 | 0.360 | 37/65 | +0.084 | STANDARD |
| Sam Reinhart: 1+ assists | 0.311 | 0.420 | 43/59 | +0.082 | STANDARD |
| Brady Tkachuk: 1+ points | 0.512 | 0.620 | 63/39 | +0.081 | STANDARD |
| Sam Reinhart: 2+ points | 0.158 | 0.265 | 28/75 | +0.079 | STANDARD |
| Sam Reinhart: 1+ points | 0.513 | 0.620 | 63/39 | +0.080 | STANDARD |

**NYI @ TOR** · priced 180/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.61, exp saves 26.56 (sd 7.07), pull risk 0.06
- NYI net: Ilya Sorokin (PROBABLE) exp shots 26.0, exp saves 22.41 (sd 6.3), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ilya Sorokin: 26+ saves | 0.308 | 0.485 | 50/53 | +0.145 |  |
| Adam Pelech: 1+ points | 0.290 | 0.145 | 23/94 | +0.048 | STANDARD |
| Gavin McKenna: 1+ points | 0.373 | 0.445 | 45/56 | +0.050 | PRIOR_HEAVY |
| Kirill Marchenko: 1+ assists | 0.329 | 0.400 | 41/61 | +0.044 | STANDARD |
| Gavin McKenna: 1+ assists | 0.232 | 0.295 | 30/71 | +0.044 | PRIOR_HEAVY |
| Sergei Bobrovsky: 26+ saves | 0.558 | 0.495 | 50/51 | +0.040 |  |

**BUF @ MTL** · priced 158/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.31, exp saves 24.62 (sd 6.73), pull risk 0.061
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 26.14, exp saves 22.47 (sd 6.39), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.628 | 0.445 | 52/63 | +0.091 |  |
| Ukko-Pekka Luukkonen: 26+ saves | 0.308 | 0.475 | 49/54 | +0.134 |  |
| Nick Suzuki: 1+ assists | 0.461 | 0.570 | 58/44 | +0.082 | STANDARD |
| Zach Benson: 1+ points | 0.562 | 0.460 | 47/55 | +0.074 | STANDARD |
| Nick Suzuki: 2+ points | 0.266 | 0.350 | 36/66 | +0.058 | STANDARD |
| Chris Kreider: 1+ points | 0.411 | 0.485 | 50/53 | +0.042 | STANDARD |

**SJS @ DET** · priced 171/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.93, exp saves 22.5 (sd 6.24), pull risk 0.057
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 29.07, exp saves 25.14 (sd 6.77), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.406 | 0.575 | 58/43 | +0.147 | STANDARD |
| Macklin Celebrini: 2+ points | 0.259 | 0.400 | 41/61 | +0.115 | STANDARD |
| Ivar Stenberg: 1+ points | 0.319 | 0.440 | 45/57 | +0.094 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ assists | 0.191 | 0.310 | 32/70 | +0.095 | PRIOR_HEAVY |
| Macklin Celebrini: 2+ assists | 0.099 | 0.195 | 22/83 | +0.061 | STANDARD |
| Ivar Stenberg: 2+ points | 0.058 | 0.145 | 15/86 | +0.074 | PRIOR_HEAVY |

**OTT @ PHI** · priced 181/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.39, exp saves 23.79 (sd 6.48), pull risk 0.052
- OTT net: Linus Ullmark (CONFIRMED) exp shots 24.0, exp saves 21.01 (sd 5.93), pull risk 0.046

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ assists | 0.374 | 0.520 | 53/49 | +0.119 | STANDARD |
| Nick Cousins: 1+ points | 0.266 | 0.130 | 25/99 | +0.003 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.149 | 0.275 | 28/73 | +0.107 | STANDARD |
| Michael Amadio: 1+ assists | 0.234 | 0.120 | 23/99 | -0.008 | STANDARD |
| Tim Stutzle: 2+ points | 0.195 | 0.305 | 33/72 | +0.071 | STANDARD |
| Tim Stutzle: 1+ points | 0.555 | 0.660 | 67/35 | +0.079 | STANDARD |

**NYR @ CBJ** · priced 160/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROBABLE) exp shots 24.38, exp saves 21.36 (sd 5.9), pull risk 0.047
- NYR net: Dylan Garand (CONFIRMED) exp shots 28.58, exp saves 24.54 (sd 6.73), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Fox: 1+ assists | 0.417 | 0.510 | 52/50 | +0.065 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.425 | 0.515 | 52/49 | +0.067 | STANDARD |
| J.T. Miller: 1+ assists | 0.344 | 0.425 | 43/58 | +0.059 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.209 | 0.285 | 29/72 | +0.057 | STANDARD |
| Adam Fox: 1+ points | 0.478 | 0.550 | 56/46 | +0.045 | STANDARD |
| Pavel Dorofeyev: 2+ points | 0.102 | 0.170 | 19/85 | +0.039 | STANDARD |

**DAL @ CHI** · priced 150/155 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 27.33, exp saves 23.58 (sd 6.43), pull risk 0.064
- DAL net: Jake Oettinger (CONFIRMED) exp shots 23.84, exp saves 20.66 (sd 5.88), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Spencer Knight: 26+ saves | 0.372 | 0.500 | 51/51 | +0.100 |  |
| Jason Robertson: 1+ assists | 0.394 | 0.495 | 51/52 | +0.068 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.533 | 0.440 | 45/57 | +0.066 | STANDARD |
| Connor Bedard: 1+ assists | 0.345 | 0.435 | 45/58 | +0.058 | STANDARD |
| Jason Robertson: 2+ points | 0.269 | 0.355 | 37/66 | +0.055 | STANDARD |
| Mikko Rantanen: 2+ points | 0.259 | 0.345 | 36/67 | +0.055 | STANDARD |

**STL @ NSH** · priced 162/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 27.32, exp saves 23.59 (sd 6.57), pull risk 0.067
- STL net: Jordan Binnington (CONFIRMED) exp shots 27.33, exp saves 23.54 (sd 6.62), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Neighbours: 1+ assists | 0.308 | 0.225 | 24/79 | +0.056 | STANDARD |
| Mason McTavish: 1+ assists | 0.254 | 0.325 | 34/69 | +0.041 | STANDARD |
| Jake Neighbours: 1+ points | 0.456 | 0.385 | 40/63 | +0.039 | STANDARD |
| Robert Thomas: 1+ assists | 0.414 | 0.485 | 49/52 | +0.048 | STANDARD |
| Adam Jiricek: 1+ assists | 0.234 | 0.290 | 30/72 | +0.031 | PRIOR_HEAVY |
| Cam Fowler: 1+ assists | 0.328 | 0.275 | 29/74 | +0.024 | STANDARD |

**BOS @ LAK** · priced 159/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROBABLE) exp shots 25.88, exp saves 22.58 (sd 6.19), pull risk 0.052
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.68, exp saves 25.56 (sd 6.91), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.395 | 0.525 | 53/48 | +0.108 | STANDARD |
| Trevor Moore: 1+ assists | 0.334 | 0.225 | 26/81 | +0.060 | STANDARD |
| Artemi Panarin: 2+ points | 0.225 | 0.320 | 34/70 | +0.060 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.325 | 0.415 | 42/59 | +0.068 | STANDARD |
| Marat Khusnutdinov: 1+ points | 0.344 | 0.255 | 26/75 | +0.070 | STANDARD |
| Fraser Minten: 1+ points | 0.444 | 0.360 | 37/65 | +0.057 | STANDARD |

**EDM @ UTA** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 27.03, exp saves 23.36 (sd 6.59), pull risk 0.068
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.83, exp saves 23.77 (sd 6.81), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.229 | 0.355 | 37/66 | +0.095 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.450 | 0.570 | 58/44 | +0.093 | STANDARD |
| Leon Draisaitl: 2+ points | 0.286 | 0.400 | 42/62 | +0.077 | STANDARD |
| Mattias Ekholm: 1+ points | 0.432 | 0.325 | 34/69 | +0.076 | STANDARD |
| Connor McDavid: 2+ points | 0.380 | 0.475 | 49/54 | +0.062 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.363 | 0.270 | 28/74 | +0.069 | STANDARD |

**PIT @ VGK** · priced 163/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (CONFIRMED) exp shots 26.53, exp saves 23.38 (sd 6.31), pull risk 0.049
- PIT net: Sergei Murashov (PROJECTED) exp shots 28.1, exp saves 23.73 (sd 6.77), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.277 | 0.430 | 44/58 | +0.126 | STANDARD |
| Jack Eichel: 1+ assists | 0.469 | 0.620 | 63/39 | +0.125 | STANDARD |
| Adin Hill: 22+ saves | 0.617 | 0.480 | 50/54 | +0.100 |  |
| Mitch Marner: 2+ points | 0.227 | 0.350 | 37/67 | +0.087 | STANDARD |
| Jack Eichel: 2+ assists | 0.139 | 0.255 | 28/77 | +0.079 | STANDARD |
| Jack Eichel: 3+ points | 0.086 | 0.200 | 19/ | -0.114 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
