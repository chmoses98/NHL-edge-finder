# NHL slate 2026-10-17 — RESEARCH_ONLY

generated 2026-10-17T22:25:52Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 10 · markets on board: 4521 · contracts joined: 2229 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 1979, 'OK': 189, 'NO_EDGE': 61}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 310, 'game_early_goal': 10, 'first_goal': 368, 'game_winner': 20, 'player_goals': 626, 'game_overtime': 10, 'player_points': 397, 'goalie_saves': 18, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYI @ TOR | 2026-10-17T23:00:00Z | T-30m | 0.470 | 0.530 | 0.173 | 6.33 | 3.07 | 3.26 | 234 (25/209) | CONFIRMED/PROBABLE |
| BUF @ MTL | 2026-10-17T23:00:00Z | T-30m | 0.517 | 0.483 | 0.178 | 6.19 | 3.15 | 3.04 | 217 (25/192) | CONFIRMED/PROBABLE |
| SJS @ DET | 2026-10-17T23:00:00Z | T-30m | 0.549 | 0.451 | 0.176 | 5.95 | 3.13 | 2.81 | 229 (25/204) | CONFIRMED/CONFIRMED |
| OTT @ PHI | 2026-10-17T23:00:00Z | T-30m | 0.488 | 0.512 | 0.188 | 5.58 | 2.76 | 2.82 | 237 (25/212) | CONFIRMED/CONFIRMED |
| NYR @ CBJ | 2026-10-17T23:00:00Z | T-30m | 0.531 | 0.469 | 0.177 | 5.82 | 3.00 | 2.82 | 217 (25/192) | PROBABLE/CONFIRMED |
| DAL @ CHI | 2026-10-17T23:00:00Z | T-30m | 0.464 | 0.536 | 0.188 | 5.60 | 2.70 | 2.90 | 226 (25/201) | CONFIRMED/CONFIRMED |
| STL @ NSH | 2026-10-18T00:00:00Z | T-90m | 0.538 | 0.462 | 0.170 | 6.88 | 3.56 | 3.32 | 215 (25/190) | PROBABLE/CONFIRMED |
| BOS @ LAK | 2026-10-18T01:00:00Z | T-90m | 0.511 | 0.489 | 0.187 | 5.60 | 2.83 | 2.77 | 218 (25/193) | PROBABLE/PROJECTED |
| EDM @ UTA | 2026-10-18T02:00:00Z | T-3h | 0.560 | 0.440 | 0.169 | 6.72 | 3.56 | 3.16 | 221 (25/196) | PROBABLE/CONFIRMED |
| PIT @ VGK | 2026-10-18T02:00:00Z | T-3h | 0.600 | 0.400 | 0.156 | 6.86 | 3.78 | 3.09 | 215 (25/190) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL4 | team_total | 0.341 | 0.505 | 0.471 | 51 | 50 | no | +0.141 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL3 | team_total | 0.561 | 0.710 | 0.682 | 72 | 30 | no | +0.125 | OK |
| KXNHLGAME-26OCT17DALCHI-CHI | game_winner | 0.464 | 0.335 | 0.359 | 34 | 67 | yes | +0.108 | OK |
| KXNHLGAME-26OCT17DALCHI-DAL | game_winner | 0.536 | 0.665 | 0.641 | 67 | 34 | no | +0.108 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL2 | game_spread | 0.297 | 0.425 | 0.398 | 43 | 58 | no | +0.106 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL3 | game_spread | 0.172 | 0.300 | 0.271 | 31 | 71 | no | +0.104 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL5 | team_total | 0.172 | 0.295 | 0.267 | 31 | 72 | no | +0.094 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL2 | team_total | 0.779 | 0.885 | 0.868 | 89 | 12 | no | +0.093 | OK |
| KXNHLTOTAL-26OCT17STLNSH-7 | game_total | 0.557 | 0.445 | 0.467 | 45 | 56 | yes | +0.089 | OK |
| KXNHLTOTAL-26OCT17STLNSH-8 | game_total | 0.355 | 0.255 | 0.273 | 26 | 75 | yes | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH5 | team_total | 0.292 | 0.195 | 0.212 | 20 | 81 | yes | +0.081 | OK |
| KXNHLTOTAL-26OCT17STLNSH-6 | game_total | 0.666 | 0.565 | 0.586 | 57 | 44 | yes | +0.079 | OK |
| KXNHLTOTAL-26OCT17STLNSH-9 | game_total | 0.264 | 0.175 | 0.191 | 18 | 83 | yes | +0.073 | OK |
| KXNHLTOTAL-26OCT17DALCHI-7 | game_total | 0.350 | 0.445 | 0.425 | 45 | 56 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH4 | team_total | 0.483 | 0.390 | 0.408 | 40 | 62 | yes | +0.066 | OK |
| KXNHLSPREAD-26OCT17DALCHI-CHI2 | game_spread | 0.246 | 0.165 | 0.179 | 17 | 84 | yes | +0.066 | OK |
| KXNHLTOTAL-26OCT17DALCHI-5 | game_total | 0.693 | 0.775 | 0.760 | 78 | 23 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH3 | team_total | 0.691 | 0.600 | 0.619 | 61 | 41 | yes | +0.064 | OK |
| KXNHLTOTAL-26OCT17DALCHI-6 | game_total | 0.460 | 0.545 | 0.528 | 55 | 46 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT17SJDET-DET4 | team_total | 0.390 | 0.475 | 0.458 | 48 | 53 | no | +0.063 | OK |
| KXNHLGAME-26OCT17NYITOR-NYI | game_winner | 0.530 | 0.445 | 0.462 | 45 | 56 | yes | +0.062 | OK |
| KXNHLGAME-26OCT17OTTPHI-OTT | game_winner | 0.512 | 0.595 | 0.579 | 60 | 41 | no | +0.061 | OK |
| KXNHLGAME-26OCT17OTTPHI-PHI | game_winner | 0.488 | 0.405 | 0.421 | 41 | 60 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4 | team_total | 0.325 | 0.405 | 0.388 | 41 | 60 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT17DALCHI-4 | game_total | 0.793 | 0.865 | 0.853 | 87 | 14 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT17BOSLA-5 | game_total | 0.690 | 0.765 | 0.751 | 77 | 24 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA4 | team_total | 0.326 | 0.410 | 0.393 | 42 | 60 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA3 | team_total | 0.547 | 0.630 | 0.614 | 64 | 38 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH6 | team_total | 0.150 | 0.080 | 0.091 | 9 | 93 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-5 | game_total | 0.725 | 0.795 | 0.782 | 80 | 21 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-7 | game_total | 0.389 | 0.465 | 0.450 | 47 | 54 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-4 | game_total | 0.819 | 0.885 | 0.874 | 89 | 12 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT17SJDET-7 | game_total | 0.410 | 0.485 | 0.470 | 49 | 52 | no | +0.053 | OK |
| KXNHLGAME-26OCT17NYITOR-TOR | game_winner | 0.470 | 0.545 | 0.530 | 55 | 46 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-6 | game_total | 0.501 | 0.575 | 0.560 | 58 | 43 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT17BOSLA-6 | game_total | 0.461 | 0.535 | 0.520 | 54 | 47 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR2 | game_spread | 0.263 | 0.335 | 0.320 | 34 | 67 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL6 | team_total | 0.071 | 0.135 | 0.119 | 14 | 87 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT17SJDET-5 | game_total | 0.738 | 0.805 | 0.793 | 81 | 20 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT3 | team_total | 0.543 | 0.620 | 0.605 | 63 | 39 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT17NYITOR-NYI2 | game_spread | 0.313 | 0.245 | 0.258 | 25 | 76 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT17DALCHI-8 | game_total | 0.178 | 0.245 | 0.230 | 25 | 76 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT3 | game_spread | 0.160 | 0.225 | 0.211 | 23 | 78 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT2 | game_spread | 0.278 | 0.345 | 0.331 | 35 | 66 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR3 | game_spread | 0.152 | 0.215 | 0.201 | 22 | 79 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH2 | team_total | 0.866 | 0.805 | 0.819 | 81 | 20 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT17BUFMTL-MTL4 | team_total | 0.397 | 0.465 | 0.451 | 47 | 54 | no | +0.045 | OK |
| KXNHLGAME-26OCT17PITVGK-PIT | game_winner | 0.400 | 0.335 | 0.348 | 34 | 67 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT17SJDET-DET3 | team_total | 0.611 | 0.675 | 0.663 | 68 | 33 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT17PITVGK-VGK3 | game_spread | 0.262 | 0.325 | 0.312 | 33 | 68 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT17SJDET-4 | game_total | 0.829 | 0.885 | 0.875 | 89 | 12 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT17SJDET-6 | game_total | 0.520 | 0.585 | 0.572 | 59 | 42 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT17STLNSH-5 | game_total | 0.844 | 0.785 | 0.798 | 79 | 22 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT17BOSLA-7 | game_total | 0.351 | 0.415 | 0.402 | 42 | 59 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT2 | team_total | 0.767 | 0.830 | 0.819 | 84 | 18 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17STLNSH-10 | game_total | 0.138 | 0.080 | 0.089 | 9 | 93 | yes | +0.042 | OK |
| KXNHLTOTAL-26OCT17BOSLA-4 | game_total | 0.790 | 0.845 | 0.835 | 85 | 16 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-PHI2 | game_spread | 0.262 | 0.205 | 0.216 | 21 | 80 | yes | +0.040 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-8 | game_total | 0.207 | 0.265 | 0.253 | 27 | 74 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA5 | team_total | 0.159 | 0.225 | 0.210 | 24 | 79 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT17NYRCBJ-CBJ4 | team_total | 0.364 | 0.425 | 0.413 | 43 | 58 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA2 | team_total | 0.772 | 0.830 | 0.819 | 84 | 18 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT17BOSLA-8 | game_total | 0.180 | 0.235 | 0.223 | 24 | 77 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT17BUFMTL-6 | game_total | 0.556 | 0.615 | 0.603 | 62 | 39 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT17NYITOR-NYI4 | team_total | 0.423 | 0.365 | 0.376 | 37 | 64 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT17BOSLA-LA3 | game_spread | 0.162 | 0.215 | 0.203 | 22 | 79 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT4 | team_total | 0.382 | 0.320 | 0.332 | 33 | 69 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT17NYITOR-NYI5 | team_total | 0.236 | 0.180 | 0.190 | 19 | 83 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT17BUFMTL-MTL2 | team_total | 0.816 | 0.865 | 0.856 | 87 | 14 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT17NYITOR-TOR4 | team_total | 0.378 | 0.435 | 0.423 | 44 | 57 | no | +0.035 | OK |
| KXNHLGAME-26OCT17PITVGK-VGK | game_winner | 0.600 | 0.655 | 0.644 | 66 | 35 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT17BUFMTL-MTL5 | team_total | 0.213 | 0.270 | 0.258 | 28 | 74 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT17BOSLA-LA2 | game_spread | 0.281 | 0.335 | 0.324 | 34 | 67 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT17DALCHI-9 | game_total | 0.118 | 0.165 | 0.154 | 17 | 84 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT17NYITOR-NYI3 | team_total | 0.639 | 0.585 | 0.596 | 59 | 42 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT17SJDET-DET3 | game_spread | 0.196 | 0.245 | 0.235 | 25 | 76 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT17DALCHI-CHI3 | game_spread | 0.136 | 0.095 | 0.102 | 10 | 91 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT17BUFMTL-MTL3 | game_spread | 0.178 | 0.230 | 0.219 | 24 | 78 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT17NYRCBJ-CBJ3 | team_total | 0.584 | 0.635 | 0.625 | 64 | 37 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT17BUFMTL-4 | game_total | 0.854 | 0.895 | 0.888 | 90 | 11 | no | +0.029 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYI @ TOR | 0.470 | 0.507 | 0.173 | 0.218 | 6.33 | 6.31 | 0.988/0.952 | KXNHLSPREAD-26OCT17NYITOR-NYI2 -0.038 |
| BUF @ MTL | 0.517 | 0.519 | 0.178 | 0.222 | 6.19 | 6.44 | 0.983/1.000 | KXNHLTOTAL-26OCT17BUFMTL-7 +0.051 |
| SJS @ DET | 0.549 | 0.519 | 0.176 | 0.219 | 5.95 | 6.21 | 0.994/1.021 | KXNHLTEAMTOTAL-26OCT17SJDET-SJ3 +0.057 |
| OTT @ PHI | 0.488 | 0.476 | 0.188 | 0.231 | 5.58 | 5.69 | 0.994/0.968 | KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT3 +0.025 |
| NYR @ CBJ | 0.531 | 0.559 | 0.177 | 0.219 | 5.82 | 6.06 | 0.955/0.988 | KXNHLTEAMTOTAL-26OCT17NYRCBJ-CBJ3 +0.051 |
| DAL @ CHI | 0.464 | 0.467 | 0.188 | 0.221 | 5.60 | 6.16 | 0.988/0.994 | KXNHLTOTAL-26OCT17DALCHI-7 +0.098 |
| STL @ NSH | 0.538 | 0.506 | 0.170 | 0.222 | 6.88 | 6.48 | 1.002/1.032 | KXNHLTOTAL-26OCT17STLNSH-6 -0.062 |
| BOS @ LAK | 0.511 | 0.540 | 0.187 | 0.222 | 5.60 | 6.05 | 0.988/0.968 | KXNHLTOTAL-26OCT17BOSLA-7 +0.078 |
| EDM @ UTA | 0.560 | 0.528 | 0.169 | 0.214 | 6.72 | 6.89 | 0.991/1.023 | KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM4 +0.047 |
| PIT @ VGK | 0.600 | 0.630 | 0.156 | 0.204 | 6.86 | 6.49 | 1.004/1.021 | KXNHLTOTAL-26OCT17PITVGK-6 -0.061 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 37 recommended · full analysis in card.md / packet.json `thesis_card`

- Adam Pelech: 1+ goals YES @ 4c · p 0.0601 (adj 0.0551) · $1.13 · thesis NYI:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 10c · p 0.1309 (adj 0.1219) · $1.6 · thesis NYI:OFFENSE_4PLUS
- Gavin McKenna: 1+ assists NO @ 71c · p 0.7684 (adj 0.7367) · $4.89 · thesis TOR:SUPPRESSED
- Ilya Sorokin: 26+ saves NO @ 54c · p 0.6922 (adj 0.5706) · $3.42 · thesis NYI:NET_LOW_VOLUME
- Owen Power: 1+ goals NO @ 87c · p 0.9039 (adj 0.8942) · $7.85 · thesis BUF:SUPPRESSED
- Ryan McLeod: 1+ goals YES @ 15c · p 0.183 (adj 0.1723) · $1.4 · thesis BUF:OFFENSE_4PLUS
- Zach Benson: 1+ assists YES @ 33c · p 0.398 (adj 0.3615) · $2.26 · thesis BUF:OFFENSE_4PLUS
- Zach Benson: 1+ goals YES @ 24c · p 0.2763 (adj 0.266) · $1.69 · thesis BUF:OFFENSE_4PLUS
- Nate Danielson: 1+ goals NO @ 84c · p 0.884 (adj 0.8718) · $7.39 · thesis DET:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 69c · p 0.8093 (adj 0.7285) · $7.11 · thesis SJS:SUPPRESSED
- Luca Cagnoni: 1+ assists NO @ 69c · p 0.7613 (adj 0.7207) · $4.66 · thesis SJS:SUPPRESSED
- Drake Batherson: 1+ goals NO @ 68c · p 0.7391 (adj 0.7231) · $6.64 · thesis OTT:SUPPRESSED
- Porter Martone: 1+ goals NO @ 78c · p 0.8224 (adj 0.8105) · $7.08 · thesis PHI:SUPPRESSED
- Dylan Cozens: 1+ goals NO @ 72c · p 0.7631 (adj 0.7511) · $5.14 · thesis OTT:SUPPRESSED
- Danton Heinen: 1+ goals YES @ 11c · p 0.1362 (adj 0.1271) · $1.09 · thesis CBJ:OFFENSE_4PLUS
- Will Cuylle: 1+ goals NO @ 78c · p 0.8126 (adj 0.8032) · $5.54 · thesis NYR:SUPPRESSED
- Pavel Dorofeyev: 1+ goals NO @ 69c · p 0.7277 (adj 0.7158) · $3.74 · thesis NYR:SUPPRESSED
- Anton Frondell: 1+ goals YES @ 19c · p 0.2475 (adj 0.2306) · $3.36 · thesis CHI:OFFENSE_4PLUS
- Frank Nazar: 1+ goals YES @ 19c · p 0.2415 (adj 0.2274) · $3.04 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 24c · p 0.295 (adj 0.28) · $3.42 · thesis CHI:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 11c · p 0.1484 (adj 0.1351) · $1.77 · thesis CHI:OFFENSE_4PLUS
- Adam Wilsby: 1+ goals YES @ 5c · p 0.0706 (adj 0.0654) · $1.16 · thesis NSH:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 24c · p 0.2836 (adj 0.2715) · $2.37 · thesis STL:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 27c · p 0.3128 (adj 0.3009) · $2.31 · thesis NSH:OFFENSE_4PLUS
- Dalibor Dvorsky: 1+ goals NO @ 82c · p 0.8494 (adj 0.8408) · $6.49 · thesis STL:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 48c · p 0.6051 (adj 0.5205) · $3.45 · thesis LAK:SUPPRESSED
- Charlie McAvoy: 1+ assists NO @ 59c · p 0.6746 (adj 0.6273) · $6.06 · thesis BOS:SUPPRESSED
- Artemi Panarin: 2+ assists NO @ 84c · p 0.9078 (adj 0.8639) · $7.85 · thesis LAK:SUPPRESSED
- Elias Lindholm: 1+ goals YES @ 20c · p 0.2332 (adj 0.2224) · $1.72 · thesis BOS:OFFENSE_4PLUS
- Nate Schmidt: 1+ goals YES @ 4c · p 0.0666 (adj 0.0587) · $1.4 · thesis UTA:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 71c · p 0.7978 (adj 0.7514) · $7.85 · thesis EDM:SUPPRESSED
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1098 (adj 0.1011) · $1.71 · thesis EDM:OFFENSE_4PLUS
- Zach Hyman: 1+ goals YES @ 31c · p 0.358 (adj 0.3448) · $3.54 · thesis EDM:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 68c · p 0.7344 (adj 0.7196) · $7.85 · thesis VGK:SUPPRESSED
- Evgeni Malkin: 1+ assists NO @ 63c · p 0.7155 (adj 0.6703) · $7.31 · thesis PIT:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0836 (adj 0.0752) · $1.07 · thesis VGK:WINS_BY_2PLUS
- Bryan Rust: 1+ goals YES @ 24c · p 0.286 (adj 0.272) · $2.64 · thesis PIT:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYI @ TOR** · priced 180/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.61, exp saves 26.56 (sd 7.07), pull risk 0.06
- NYI net: Ilya Sorokin (PROBABLE) exp shots 26.0, exp saves 22.41 (sd 6.3), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ilya Sorokin: 26+ saves | 0.308 | 0.470 | 48/54 | +0.135 |  |
| Gavin McKenna: 1+ points | 0.373 | 0.465 | 47/54 | +0.069 | PRIOR_HEAVY |
| Adam Pelech: 1+ points | 0.290 | 0.215 | 23/80 | +0.048 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.329 | 0.400 | 41/61 | +0.044 | STANDARD |
| Adam Pelech: 1+ assists | 0.245 | 0.180 | 20/84 | +0.034 | STANDARD |
| Gavin McKenna: 1+ assists | 0.232 | 0.295 | 30/71 | +0.044 | PRIOR_HEAVY |

**BUF @ MTL** · priced 158/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.31, exp saves 24.62 (sd 6.73), pull risk 0.061
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 26.14, exp saves 22.47 (sd 6.39), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ukko-Pekka Luukkonen: 26+ saves | 0.308 | 0.455 | 48/57 | +0.105 |  |
| Nick Suzuki: 1+ assists | 0.461 | 0.565 | 57/44 | +0.082 | STANDARD |
| Jacob Fowler: 23+ saves | 0.628 | 0.525 | 54/49 | +0.071 |  |
| Zach Benson: 1+ points | 0.562 | 0.470 | 48/54 | +0.064 | STANDARD |
| Nick Suzuki: 2+ points | 0.266 | 0.345 | 35/66 | +0.058 | STANDARD |
| Chris Kreider: 1+ points | 0.411 | 0.485 | 49/52 | +0.052 | STANDARD |

**SJS @ DET** · priced 171/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.93, exp saves 22.5 (sd 6.24), pull risk 0.057
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 29.07, exp saves 25.14 (sd 6.77), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.406 | 0.585 | 59/42 | +0.157 | STANDARD |
| Macklin Celebrini: 2+ points | 0.259 | 0.395 | 40/61 | +0.115 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.191 | 0.315 | 32/69 | +0.104 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ points | 0.319 | 0.440 | 45/57 | +0.094 | PRIOR_HEAVY |
| Macklin Celebrini: 2+ assists | 0.099 | 0.205 | 22/81 | +0.080 | STANDARD |
| Ivar Stenberg: 2+ points | 0.058 | 0.145 | 15/86 | +0.074 | PRIOR_HEAVY |

**OTT @ PHI** · priced 181/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.39, exp saves 23.79 (sd 6.48), pull risk 0.052
- OTT net: Linus Ullmark (CONFIRMED) exp shots 24.0, exp saves 21.01 (sd 5.93), pull risk 0.046

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ assists | 0.374 | 0.515 | 52/49 | +0.119 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.149 | 0.275 | 28/73 | +0.107 | STANDARD |
| Tim Stutzle: 2+ points | 0.195 | 0.315 | 33/70 | +0.090 | STANDARD |
| Michael Amadio: 1+ assists | 0.234 | 0.125 | 24/99 | -0.018 | STANDARD |
| Tim Stutzle: 1+ points | 0.555 | 0.655 | 66/35 | +0.079 | STANDARD |
| Andre Burakovsky: 1+ points | 0.261 | 0.355 | 36/65 | +0.073 | STANDARD |

**NYR @ CBJ** · priced 160/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROBABLE) exp shots 24.38, exp saves 21.36 (sd 5.9), pull risk 0.047
- NYR net: Dylan Garand (CONFIRMED) exp shots 28.58, exp saves 24.54 (sd 6.73), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pavel Dorofeyev: 1+ points | 0.425 | 0.515 | 52/49 | +0.067 | STANDARD |
| Adam Fox: 1+ assists | 0.417 | 0.505 | 51/50 | +0.065 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.209 | 0.290 | 30/72 | +0.057 | STANDARD |
| J.T. Miller: 1+ assists | 0.344 | 0.425 | 43/58 | +0.059 | STANDARD |
| Adam Fox: 1+ points | 0.478 | 0.550 | 56/46 | +0.045 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.245 | 0.305 | 32/71 | +0.031 | STANDARD |

**DAL @ CHI** · priced 165/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 27.33, exp saves 23.58 (sd 6.43), pull risk 0.064
- DAL net: Jake Oettinger (CONFIRMED) exp shots 23.84, exp saves 20.66 (sd 5.88), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Spencer Knight: 26+ saves | 0.372 | 0.495 | 50/51 | +0.100 |  |
| Jason Robertson: 1+ assists | 0.394 | 0.490 | 50/52 | +0.068 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.533 | 0.445 | 45/56 | +0.066 | STANDARD |
| Jason Robertson: 2+ points | 0.269 | 0.355 | 37/66 | +0.055 | STANDARD |
| Connor Bedard: 1+ assists | 0.345 | 0.430 | 44/58 | +0.058 | STANDARD |
| Mikko Rantanen: 2+ points | 0.259 | 0.340 | 35/67 | +0.055 | STANDARD |

**STL @ NSH** · priced 162/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 27.32, exp saves 23.59 (sd 6.57), pull risk 0.067
- STL net: Jordan Binnington (CONFIRMED) exp shots 27.33, exp saves 23.54 (sd 6.62), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Neighbours: 1+ assists | 0.308 | 0.220 | 24/80 | +0.056 | STANDARD |
| Robert Thomas: 1+ assists | 0.414 | 0.490 | 50/52 | +0.048 | STANDARD |
| Mason McTavish: 1+ assists | 0.254 | 0.325 | 34/69 | +0.041 | STANDARD |
| Jake Neighbours: 1+ points | 0.456 | 0.385 | 40/63 | +0.039 | STANDARD |
| Adam Jiricek: 1+ assists | 0.234 | 0.290 | 30/72 | +0.031 | PRIOR_HEAVY |
| Cam Fowler: 1+ assists | 0.328 | 0.275 | 30/75 | +0.013 | STANDARD |

**BOS @ LAK** · priced 159/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROBABLE) exp shots 25.88, exp saves 22.58 (sd 6.19), pull risk 0.052
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.68, exp saves 25.56 (sd 6.91), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.395 | 0.525 | 53/48 | +0.108 | STANDARD |
| Drew Doughty: 1+ points | 0.339 | 0.215 | 38/95 | -0.057 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.325 | 0.420 | 43/59 | +0.068 | STANDARD |
| Marat Khusnutdinov: 1+ points | 0.344 | 0.250 | 26/76 | +0.070 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.321 | 0.230 | 25/79 | +0.058 | STANDARD |
| Trevor Moore: 1+ assists | 0.334 | 0.245 | 27/78 | +0.050 | STANDARD |

**EDM @ UTA** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 27.03, exp saves 23.36 (sd 6.59), pull risk 0.068
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.83, exp saves 23.77 (sd 6.81), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vasily Podkolzin: 1+ assists | 0.387 | 0.235 | 26/79 | +0.114 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.229 | 0.355 | 37/66 | +0.095 | STANDARD |
| Mattias Ekholm: 1+ points | 0.432 | 0.315 | 32/69 | +0.097 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.450 | 0.565 | 57/44 | +0.093 | STANDARD |
| Leon Draisaitl: 2+ points | 0.286 | 0.395 | 40/61 | +0.087 | STANDARD |
| Connor McDavid: 2+ points | 0.380 | 0.485 | 50/53 | +0.072 | STANDARD |

**PIT @ VGK** · priced 163/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (CONFIRMED) exp shots 26.53, exp saves 23.38 (sd 6.31), pull risk 0.049
- PIT net: Sergei Murashov (PROJECTED) exp shots 28.1, exp saves 23.73 (sd 6.77), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.277 | 0.430 | 44/58 | +0.126 | STANDARD |
| Jack Eichel: 1+ assists | 0.469 | 0.615 | 62/39 | +0.125 | STANDARD |
| Adin Hill: 22+ saves | 0.617 | 0.480 | 50/54 | +0.100 |  |
| Mitch Marner: 2+ points | 0.227 | 0.350 | 37/67 | +0.087 | STANDARD |
| Jack Eichel: 2+ assists | 0.139 | 0.245 | 26/77 | +0.079 | STANDARD |
| Mitch Marner: 1+ assists | 0.445 | 0.540 | 55/47 | +0.068 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
