# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-23T00:36:52Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 4 · markets on board: 4684 · contracts joined: 963 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 863, 'OK': 81, 'NO_EDGE': 19}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 143, 'game_early_goal': 4, 'first_goal': 150, 'game_winner': 8, 'player_goals': 263, 'game_overtime': 4, 'player_points': 199, 'goalie_saves': 4, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ CGY | 2026-10-23T01:00:00Z | T-10m | 0.463 | 0.537 | 0.188 | 5.73 | 2.75 | 2.98 | 235 (25/210) | CONFIRMED/CONFIRMED |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-10m | 0.532 | 0.468 | 0.176 | 6.55 | 3.37 | 3.17 | 236 (25/211) | CONFIRMED/PROBABLE |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-60m | 0.491 | 0.509 | 0.174 | 6.27 | 3.10 | 3.17 | 238 (25/213) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-60m | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 254 (25/229) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.358 | 0.510 | 0.479 | 52 | 50 | no | +0.124 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.578 | 0.715 | 0.690 | 72 | 29 | no | +0.117 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.179 | 0.305 | 0.276 | 31 | 70 | no | +0.106 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.537 | 0.655 | 0.632 | 66 | 35 | no | +0.097 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.463 | 0.345 | 0.368 | 35 | 66 | yes | +0.097 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.396 | 0.520 | 0.495 | 53 | 49 | no | +0.096 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.308 | 0.425 | 0.400 | 43 | 58 | no | +0.095 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.491 | 0.375 | 0.398 | 38 | 63 | yes | +0.095 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.509 | 0.625 | 0.602 | 63 | 38 | no | +0.095 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.178 | 0.285 | 0.261 | 29 | 72 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.182 | 0.295 | 0.269 | 31 | 72 | no | +0.084 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.292 | 0.395 | 0.373 | 40 | 61 | no | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA3 | team_total | 0.619 | 0.720 | 0.701 | 73 | 29 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA5 | team_total | 0.217 | 0.310 | 0.290 | 32 | 70 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.795 | 0.880 | 0.866 | 89 | 13 | no | +0.067 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.367 | 0.455 | 0.437 | 46 | 55 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.480 | 0.565 | 0.548 | 57 | 44 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.278 | 0.205 | 0.218 | 21 | 80 | yes | +0.056 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.468 | 0.545 | 0.530 | 55 | 46 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.245 | 0.175 | 0.188 | 18 | 83 | yes | +0.054 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.532 | 0.465 | 0.478 | 47 | 54 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT22MINCGY-5 | game_total | 0.713 | 0.775 | 0.763 | 78 | 23 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.262 | 0.325 | 0.312 | 33 | 68 | no | +0.043 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.615 | 0.602 | 62 | 39 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.156 | 0.215 | 0.202 | 22 | 79 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT22MINCGY-8 | game_total | 0.195 | 0.255 | 0.242 | 26 | 75 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA2 | team_total | 0.821 | 0.880 | 0.870 | 89 | 13 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR4 | team_total | 0.402 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR3 | team_total | 0.616 | 0.675 | 0.664 | 68 | 33 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA3 | game_spread | 0.164 | 0.115 | 0.124 | 12 | 89 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN6 | team_total | 0.076 | 0.130 | 0.117 | 14 | 88 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR5 | team_total | 0.221 | 0.275 | 0.263 | 28 | 73 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.270 | 0.258 | 28 | 74 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT22MINCGY-4 | game_total | 0.808 | 0.860 | 0.851 | 87 | 15 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT22UTASEA-5 | game_total | 0.778 | 0.825 | 0.816 | 83 | 18 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA6 | team_total | 0.100 | 0.155 | 0.142 | 17 | 86 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET4 | team_total | 0.441 | 0.500 | 0.488 | 51 | 51 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR2 | team_total | 0.821 | 0.865 | 0.857 | 87 | 14 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM2 | game_spread | 0.314 | 0.265 | 0.274 | 27 | 74 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.385 | 0.374 | 39 | 62 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3 | team_total | 0.607 | 0.555 | 0.566 | 56 | 45 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT22UTASEA-4 | game_total | 0.860 | 0.895 | 0.889 | 90 | 11 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT22UTASEA-6 | game_total | 0.571 | 0.615 | 0.606 | 62 | 39 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4 | team_total | 0.388 | 0.340 | 0.349 | 35 | 67 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT22UTASEA-7 | game_total | 0.461 | 0.505 | 0.496 | 51 | 50 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT22MINCGY-9 | game_total | 0.129 | 0.165 | 0.157 | 17 | 84 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET3 | team_total | 0.654 | 0.700 | 0.691 | 71 | 31 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET5 | team_total | 0.255 | 0.300 | 0.291 | 31 | 71 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY3 | game_spread | 0.137 | 0.100 | 0.107 | 11 | 91 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET2 | team_total | 0.845 | 0.875 | 0.869 | 88 | 13 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA2 | team_total | 0.809 | 0.775 | 0.782 | 78 | 23 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA5 | team_total | 0.207 | 0.170 | 0.177 | 18 | 84 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN3 | team_total | 0.583 | 0.545 | 0.553 | 55 | 46 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY3 | team_total | 0.523 | 0.485 | 0.493 | 49 | 52 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-EDM3 | team_total | 0.661 | 0.620 | 0.628 | 63 | 39 | yes | +0.015 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM3 | game_spread | 0.194 | 0.165 | 0.171 | 17 | 84 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY2 | team_total | 0.758 | 0.725 | 0.732 | 73 | 28 | yes | +0.014 | OK |
| KXNHLSPREAD-26OCT22DETVAN-VAN2 | game_spread | 0.245 | 0.215 | 0.221 | 22 | 79 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT22MINCGY-2 | game_total | 0.978 | 0.990 | 0.988 |  | 1 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT22CAREDM-4 | game_total | 0.882 | 0.905 | 0.901 | 91 | 10 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT22MINCGY-10 | game_total | 0.054 | 0.080 | 0.074 | 9 | 93 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY5 | team_total | 0.149 | 0.125 | 0.129 | 13 | 88 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR6 | team_total | 0.102 | 0.130 | 0.124 | 14 | 88 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT22MINCGY-3 | game_total | 0.947 | 0.965 | 0.962 | 97 | 4 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 | team_total | 0.447 | 0.410 | 0.417 | 42 | 60 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN4 | team_total | 0.365 | 0.335 | 0.341 | 34 | 67 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT22CAREDM-5 | game_total | 0.811 | 0.835 | 0.830 | 84 | 17 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA6 | team_total | 0.094 | 0.070 | 0.074 | 8 | 94 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-EDM6 | team_total | 0.125 | 0.100 | 0.105 | 11 | 91 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT22UTASEA-9 | game_total | 0.190 | 0.215 | 0.210 | 22 | 79 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT22UTASEA-8 | game_total | 0.268 | 0.295 | 0.289 | 30 | 71 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT22DETVAN-VAN3 | game_spread | 0.142 | 0.125 | 0.128 | 13 | 88 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN5 | team_total | 0.194 | 0.170 | 0.175 | 18 | 84 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN6 | team_total | 0.089 | 0.070 | 0.073 | 8 | 94 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-EDM5 | team_total | 0.256 | 0.230 | 0.235 | 24 | 78 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4 | team_total | 0.307 | 0.280 | 0.285 | 29 | 73 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT22DETVAN-4 | game_total | 0.870 | 0.885 | 0.882 | 89 | 12 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT22UTASEA-3 | game_total | 0.966 | 0.975 | 0.973 | 98 | 3 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-VAN2 | team_total | 0.793 | 0.775 | 0.779 | 78 | 23 | yes | +0.001 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ CGY | 0.463 | 0.452 | 0.188 | 0.219 | 5.73 | 6.07 | 0.978/0.991 | KXNHLTOTAL-26OCT22MINCGY-7 +0.067 |
| CAR @ EDM | 0.532 | 0.565 | 0.176 | 0.210 | 6.55 | 6.74 | 0.994/0.987 | KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 +0.046 |
| UTA @ SEA | 0.491 | 0.498 | 0.174 | 0.215 | 6.27 | 6.52 | 1.015/0.992 | KXNHLTOTAL-26OCT22UTASEA-7 +0.043 |
| DET @ VAN | 0.450 | 0.531 | 0.176 | 0.215 | 6.37 | 6.28 | 1.021/1.003 | KXNHLGAME-26OCT22DETVAN-DET -0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Aydar Suniev: 1+ goals YES @ 16c · p 0.2214 (adj 0.2048) · $7.45 · thesis CGY:OFFENSE_4PLUS
- Kirill Kaprizov: 2+ goals NO @ 87c · p 0.9142 (adj 0.8994) · $15.45 · thesis MIN:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 10c · p 0.1405 (adj 0.1266) · $3.84 · thesis CGY:OFFENSE_4PLUS
- Ben Jones: 1+ assists NO @ 78c · p 0.859 (adj 0.812) · $15.45 · thesis CGY:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 12c · p 0.1854 (adj 0.1666) · $8.1 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 7c · p 0.111 (adj 0.0995) · $4.71 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 24c · p 0.2899 (adj 0.2762) · $5.82 · thesis EDM:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 79c · p 0.8562 (adj 0.8206) · $14.37 · thesis EDM:WINS
- Shane Wright: 1+ goals YES @ 14c · p 0.2053 (adj 0.1877) · $8.87 · thesis SEA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 64c · p 0.6997 (adj 0.6835) · $16.87 · thesis UTA:SUPPRESSED
- Kaapo Kakko: 1+ goals YES @ 15c · p 0.189 (adj 0.178) · $4.54 · thesis SEA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 12c · p 0.1484 (adj 0.1401) · $2.96 · thesis UTA:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2701 (adj 0.2463) · $10.08 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2593 (adj 0.2407) · $8.92 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 12c · p 0.1767 (adj 0.1588) · $6.3 · thesis VAN:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 66c · p 0.7198 (adj 0.7036) · $16.26 · thesis DET:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MIN @ CGY** · priced 170/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 30.26, exp saves 26.04 (sd 7.05), pull risk 0.065
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 28.91, exp saves 25.15 (sd 6.68), pull risk 0.052

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 1+ goals | 0.381 | 0.500 | 51/51 | +0.092 | STANDARD |
| Quinn Hughes: 1+ points | 0.597 | 0.715 | 72/29 | +0.098 | STANDARD |
| Quinn Hughes: 2+ points | 0.233 | 0.350 | 36/66 | +0.091 | STANDARD |
| Quinn Hughes: 1+ assists | 0.531 | 0.645 | 66/37 | +0.083 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.274 | 0.380 | 39/63 | +0.080 | STANDARD |
| Quinn Hughes: 2+ assists | 0.175 | 0.275 | 29/74 | +0.071 | STANDARD |

**CAR @ EDM** · priced 172/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 29.98, exp saves 26.06 (sd 7.0), pull risk 0.064
- CAR net: Brandon Bussi (PROBABLE) exp shots 25.41, exp saves 21.63 (sd 6.33), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Carrier: 1+ points | 0.395 | 0.205 | 32/91 | +0.059 | STANDARD |
| William Carrier: 1+ assists | 0.271 | 0.105 | 20/99 | +0.060 | STANDARD |
| Sebastian Aho: 1+ assists | 0.381 | 0.505 | 51/50 | +0.101 | STANDARD |
| Mattias Ekholm: 1+ points | 0.422 | 0.300 | 31/71 | +0.097 | STANDARD |
| Sebastian Aho: 2+ points | 0.209 | 0.325 | 33/68 | +0.096 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.350 | 0.235 | 26/79 | +0.077 | STANDARD |

**UTA @ SEA** · priced 186/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 29.05, exp saves 25.09 (sd 6.72), pull risk 0.064
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.24), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Shane Wright: 1+ points | 0.377 | 0.230 | 33/87 | +0.031 | STANDARD |
| Clayton Keller: 2+ points | 0.230 | 0.355 | 37/66 | +0.095 | STANDARD |
| Clayton Keller: 1+ points | 0.593 | 0.715 | 72/29 | +0.103 | STANDARD |
| Kailer Yamamoto: 1+ assists | 0.264 | 0.145 | 26/97 | -0.010 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.211 | 0.325 | 33/68 | +0.094 | STANDARD |
| Clayton Keller: 1+ assists | 0.447 | 0.555 | 57/46 | +0.076 | STANDARD |

**DET @ VAN** · priced 172/203 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Max Sasson: 1+ points | 0.321 | 0.110 | 21/99 | +0.099 | STANDARD |
| Tom Willander: 1+ assists | 0.283 | 0.130 | 25/99 | +0.020 | STANDARD |
| Ben Chiarot: 1+ assists | 0.248 | 0.095 | 18/99 | +0.057 | STANDARD |
| Liam Ohgren: 1+ points | 0.411 | 0.260 | 33/81 | +0.066 | STANDARD |
| Liam Ohgren: 1+ assists | 0.286 | 0.135 | 26/99 | +0.012 | STANDARD |
| Paul Cotter: 1+ assists | 0.260 | 0.115 | 22/99 | +0.028 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
