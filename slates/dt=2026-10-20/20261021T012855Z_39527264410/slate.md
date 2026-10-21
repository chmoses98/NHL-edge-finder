# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-21T01:28:55Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 3 · markets on board: 4546 · contracts joined: 732 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 657, 'OK': 54, 'NO_EDGE': 21}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 123, 'game_early_goal': 3, 'first_goal': 102, 'game_winner': 6, 'player_goals': 187, 'game_overtime': 3, 'player_points': 161, 'goalie_saves': 6, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| DET @ SEA | 2026-10-21T01:40:00Z | T-10m | 0.585 | 0.415 | 0.176 | 5.98 | 3.26 | 2.72 | 236 (25/211) | CONFIRMED/CONFIRMED |
| CAR @ VAN | 2026-10-21T02:00:00Z | T-30m | 0.337 | 0.663 | 0.157 | 6.47 | 2.69 | 3.78 | 244 (25/219) | PROBABLE/CONFIRMED |
| TBL @ VGK | 2026-10-21T02:30:00Z | T-60m | 0.539 | 0.461 | 0.181 | 5.92 | 3.08 | 2.84 | 252 (25/227) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET4 | team_total | 0.301 | 0.425 | 0.399 | 43 | 58 | no | +0.102 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET3 | team_total | 0.514 | 0.635 | 0.612 | 64 | 37 | no | +0.100 | OK |
| KXNHLGAME-26OCT20DETSEA-DET | game_winner | 0.415 | 0.525 | 0.503 | 53 | 48 | no | +0.087 | OK |
| KXNHLGAME-26OCT20DETSEA-SEA | game_winner | 0.585 | 0.475 | 0.497 | 48 | 53 | yes | +0.087 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET2 | game_spread | 0.211 | 0.315 | 0.292 | 32 | 69 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET2 | team_total | 0.748 | 0.845 | 0.828 | 85 | 16 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET5 | team_total | 0.145 | 0.240 | 0.218 | 25 | 77 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET3 | game_spread | 0.116 | 0.195 | 0.176 | 20 | 81 | no | +0.064 | OK |
| KXNHLTOTAL-26OCT20DETSEA-7 | game_total | 0.410 | 0.495 | 0.478 | 50 | 51 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR3 | game_spread | 0.307 | 0.385 | 0.369 | 39 | 62 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT20DETSEA-5 | game_total | 0.745 | 0.815 | 0.802 | 82 | 19 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA2 | game_spread | 0.356 | 0.285 | 0.299 | 29 | 72 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT20DETSEA-6 | game_total | 0.523 | 0.595 | 0.581 | 60 | 41 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT20TBVGK-5 | game_total | 0.736 | 0.795 | 0.784 | 80 | 21 | no | +0.043 | OK |
| KXNHLGAME-26OCT20CARVAN-CAR | game_winner | 0.663 | 0.725 | 0.713 | 73 | 28 | no | +0.042 | OK |
| KXNHLGAME-26OCT20CARVAN-VAN | game_winner | 0.337 | 0.275 | 0.287 | 28 | 73 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR2 | game_spread | 0.450 | 0.515 | 0.502 | 52 | 49 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT20DETSEA-4 | game_total | 0.833 | 0.885 | 0.876 | 89 | 12 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB4 | team_total | 0.324 | 0.390 | 0.376 | 40 | 62 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB3 | team_total | 0.547 | 0.605 | 0.593 | 61 | 40 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT20DETSEA-8 | game_total | 0.229 | 0.285 | 0.273 | 29 | 72 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN3 | team_total | 0.503 | 0.445 | 0.457 | 45 | 56 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB2 | team_total | 0.764 | 0.820 | 0.810 | 83 | 19 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT20TBVGK-4 | game_total | 0.828 | 0.875 | 0.867 | 88 | 13 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET6 | team_total | 0.059 | 0.105 | 0.094 | 11 | 90 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2 | team_total | 0.736 | 0.685 | 0.696 | 69 | 32 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT20TBVGK-6 | game_total | 0.512 | 0.565 | 0.554 | 57 | 44 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT20TBVGK-7 | game_total | 0.402 | 0.455 | 0.444 | 46 | 55 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN4 | team_total | 0.294 | 0.245 | 0.254 | 25 | 76 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT20TBVGK-TB2 | game_spread | 0.246 | 0.295 | 0.285 | 30 | 71 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT20TBVGK-8 | game_total | 0.220 | 0.265 | 0.256 | 27 | 74 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5 | team_total | 0.143 | 0.105 | 0.112 | 11 | 90 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR4 | team_total | 0.538 | 0.585 | 0.576 | 59 | 42 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB5 | team_total | 0.165 | 0.215 | 0.204 | 23 | 80 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA3 | game_spread | 0.224 | 0.180 | 0.188 | 19 | 83 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT20TBVGK-TB3 | game_spread | 0.138 | 0.180 | 0.171 | 19 | 83 | no | +0.022 | OK |
| KXNHLGAME-26OCT20TBVGK-TB | game_winner | 0.461 | 0.505 | 0.496 | 51 | 50 | no | +0.022 | OK |
| KXNHLGAME-26OCT20TBVGK-VGK | game_winner | 0.539 | 0.495 | 0.504 | 50 | 51 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT20DETSEA-9 | game_total | 0.158 | 0.200 | 0.191 | 21 | 81 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR5 | team_total | 0.334 | 0.375 | 0.367 | 38 | 63 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR3 | team_total | 0.740 | 0.775 | 0.768 | 78 | 23 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT20TBVGK-9 | game_total | 0.153 | 0.185 | 0.178 | 19 | 82 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT20CARVAN-VAN2 | game_spread | 0.164 | 0.135 | 0.140 | 14 | 87 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2 | team_total | 0.890 | 0.920 | 0.915 | 93 | 9 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT20DETSEA-10 | game_total | 0.070 | 0.100 | 0.093 | 11 | 91 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT20CARVAN-VAN3 | game_spread | 0.088 | 0.065 | 0.069 | 7 | 94 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6 | team_total | 0.176 | 0.205 | 0.199 | 21 | 80 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT20DETSEA-3 | game_total | 0.957 | 0.975 | 0.972 | 98 | 3 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB6 | team_total | 0.069 | 0.085 | 0.082 | 9 | 92 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN6 | team_total | 0.059 | 0.040 | 0.043 | 5 | 97 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-SEA3 | team_total | 0.638 | 0.615 | 0.620 | 62 | 39 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT20CARVAN-9 | game_total | 0.213 | 0.195 | 0.198 | 20 | 81 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT20TBVGK-3 | game_total | 0.956 | 0.965 | 0.963 | 97 | 4 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-SEA6 | team_total | 0.107 | 0.090 | 0.093 | 10 | 92 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT20TBVGK-2 | game_total | 0.979 | 0.985 | 0.984 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT20CARVAN-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT20CARVAN-5 | game_total | 0.802 | 0.815 | 0.812 | 82 | 19 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT20TBVGK-10 | game_total | 0.068 | 0.080 | 0.077 | 9 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT20DETSEA-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT20TBVGK-VGK2 | game_spread | 0.312 | 0.295 | 0.298 | 30 | 71 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT20CARVAN-3 | game_total | 0.973 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT20CARVAN-8 | game_total | 0.297 | 0.285 | 0.287 | 29 | 72 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT20CARVAN-7 | game_total | 0.488 | 0.475 | 0.478 | 48 | 53 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT20TBVGK-VGK2 | team_total | 0.809 | 0.815 | 0.814 | 82 | 19 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT20CARVAN-4 | game_total | 0.882 | 0.885 | 0.884 | 89 | 12 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT20TBVGK-VGK3 | game_spread | 0.191 | 0.185 | 0.186 | 19 | 82 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT20DETSEA-SEA5 | team_total | 0.232 | 0.225 | 0.226 | 23 | 78 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT20TBVGK-VGK5 | team_total | 0.199 | 0.215 | 0.212 | 23 | 80 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT20CARVAN-10 | game_total | 0.107 | 0.100 | 0.101 | 11 | 91 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT20TBVGK-VGK3 | team_total | 0.604 | 0.615 | 0.613 | 62 | 39 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT20CARVAN-6 | game_total | 0.604 | 0.595 | 0.597 | 60 | 41 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT20TBVGK-VGK6 | team_total | 0.089 | 0.090 | 0.090 | 10 | 92 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT20DETSEA-SEA2 | team_total | 0.833 | 0.830 | 0.831 | 84 | 18 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT20DETSEA-SEA4 | team_total | 0.419 | 0.415 | 0.416 | 42 | 59 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT20TBVGK-VGK4 | team_total | 0.385 | 0.385 | 0.385 | 39 | 62 |  | -0.021 | NO_EDGE |
| KXNHL1P-26OCT20DETSEA-DET | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT20DETSEA-SEA | period_winner |  | 0.330 |  | 35 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT20DETSEA-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT20DETSEA-DET2 | period_spread |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT20DETSEA-SEA2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| DET @ SEA | 0.585 | 0.572 | 0.176 | 0.217 | 5.98 | 6.26 | 1.023/1.024 | KXNHLTOTAL-26OCT20DETSEA-7 +0.055 |
| CAR @ VAN | 0.337 | 0.443 | 0.157 | 0.212 | 6.47 | 6.52 | 1.030/1.003 | KXNHLSPREAD-26OCT20CARVAN-CAR2 -0.115 |
| TBL @ VGK | 0.539 | 0.583 | 0.181 | 0.217 | 5.92 | 6.09 | 1.003/0.952 | KXNHLTEAMTOTAL-26OCT20TBVGK-VGK3 +0.055 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Winterton: 1+ goals YES @ 12c · p 0.1691 (adj 0.1543) · $6.88 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 11c · p 0.1534 (adj 0.1413) · $6.22 · thesis SEA:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 68c · p 0.7414 (adj 0.7248) · $20.0 · thesis DET:SUPPRESSED
- Kaapo Kakko: 1+ goals YES @ 17c · p 0.2133 (adj 0.2) · $5.5 · thesis SEA:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 16c · p 0.2489 (adj 0.2254) · $14.32 · thesis VAN:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 49c · p 0.6566 (adj 0.5451) · $6.06 · thesis VAN:WINS
- Carolina wins by over 2.5 goals NO @ 62c · p 0.7693 (adj 0.669) · $10.65 · thesis VAN:WINS
- Sebastian Aho: 1+ goals NO @ 62c · p 0.6853 (adj 0.6677) · $17.91 · thesis CAR:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 4c · p 0.0802 (adj 0.0689) · $5.4 · thesis VGK:OFFENSE_4PLUS
- Brett Howden: 1+ goals YES @ 19c · p 0.2331 (adj 0.2211) · $5.81 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 72c · p 0.7669 (adj 0.7539) · $19.13 · thesis VGK:SUPPRESSED
- Nikita Kucherov: 1+ goals NO @ 65c · p 0.6958 (adj 0.6818) · $11.41 · thesis TBL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**DET @ SEA** · priced 176/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (CONFIRMED) exp shots 29.42, exp saves 25.64 (sd 6.73), pull risk 0.054
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.75, exp saves 22.88 (sd 6.51), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Larsson: 1+ assists | 0.313 | 0.185 | 19/82 | +0.113 | STANDARD |
| Adam Larsson: 1+ points | 0.358 | 0.240 | 25/77 | +0.095 | STANDARD |
| Moritz Seider: 1+ points | 0.462 | 0.575 | 58/43 | +0.091 | STANDARD |
| Moritz Seider: 2+ points | 0.127 | 0.235 | 27/80 | +0.062 | STANDARD |
| Moritz Seider: 1+ assists | 0.401 | 0.505 | 51/50 | +0.081 | STANDARD |
| Kaapo Kakko: 1+ points | 0.491 | 0.395 | 40/61 | +0.074 | STANDARD |

**CAR @ VAN** · priced 177/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 32.33, exp saves 27.64 (sd 7.5), pull risk 0.08
- CAR net: Pyotr Kochetkov (CONFIRMED) exp shots 22.8, exp saves 19.94 (sd 5.73), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.222 | 0.340 | 35/67 | +0.093 | STANDARD |
| Bradly Nadeau: 1+ assists | 0.150 | 0.265 | 28/75 | +0.087 | STANDARD |
| Drew O'Connor: 1+ points | 0.343 | 0.235 | 24/77 | +0.090 | STANDARD |
| Sebastian Aho: 1+ points | 0.588 | 0.695 | 70/31 | +0.087 | STANDARD |
| Bradly Nadeau: 1+ points | 0.301 | 0.405 | 41/60 | +0.082 | STANDARD |
| Sebastian Aho: 1+ assists | 0.397 | 0.495 | 51/52 | +0.066 | STANDARD |

**TBL @ VGK** · priced 196/201 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.99, exp saves 23.6 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.35, exp saves 22.57 (sd 6.35), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andrei Vasilevskiy: 27+ saves | 0.256 | 0.420 | 43/59 | +0.137 |  |
| Carter Hart: 23+ saves | 0.564 | 0.420 | 69/85 | -0.141 |  |
| Nikita Kucherov: 2+ points | 0.243 | 0.380 | 39/63 | +0.111 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.437 | 0.555 | 56/45 | +0.096 | STANDARD |
| Erik Cernak: 1+ points | 0.230 | 0.120 | 18/94 | +0.040 | STANDARD |
| John Carlson: 1+ assists | 0.271 | 0.370 | 38/64 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
