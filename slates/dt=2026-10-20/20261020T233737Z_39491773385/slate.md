# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-20T23:37:37Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 6 · markets on board: 4470 · contracts joined: 1458 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 1308, 'OK': 92, 'NO_EDGE': 58}
families: {'period_winner': 54, 'period_spread': 36, 'period_total': 54, 'player_assists': 239, 'game_early_goal': 6, 'first_goal': 214, 'game_winner': 12, 'player_goals': 379, 'game_overtime': 6, 'player_points': 308, 'goalie_saves': 12, 'game_spread': 24, 'team_total': 60, 'game_total': 54}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ STL | 2026-10-21T00:00:00Z | T-10m | 0.603 | 0.397 | 0.174 | 5.87 | 3.25 | 2.62 | 260 (25/235) | CONFIRMED/CONFIRMED |
| BOS @ DAL | 2026-10-21T00:00:00Z | T-10m | 0.503 | 0.497 | 0.191 | 5.54 | 2.78 | 2.76 | 221 (25/196) | CONFIRMED/CONFIRMED |
| MIN @ EDM | 2026-10-21T01:00:00Z | T-60m | 0.561 | 0.439 | 0.174 | 6.39 | 3.39 | 3.00 | 245 (25/220) | PROBABLE/PROBABLE |
| DET @ SEA | 2026-10-21T01:40:00Z | T-90m | 0.585 | 0.415 | 0.176 | 5.98 | 3.26 | 2.72 | 236 (25/211) | CONFIRMED/CONFIRMED |
| CAR @ VAN | 2026-10-21T02:00:00Z | T-90m | 0.337 | 0.663 | 0.157 | 6.47 | 2.69 | 3.78 | 244 (25/219) | PROBABLE/CONFIRMED |
| TBL @ VGK | 2026-10-21T02:30:00Z | T-90m | 0.539 | 0.461 | 0.181 | 5.92 | 3.08 | 2.84 | 252 (25/227) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET4 | team_total | 0.301 | 0.425 | 0.399 | 43 | 58 | no | +0.102 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET3 | team_total | 0.514 | 0.635 | 0.612 | 64 | 37 | no | +0.100 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL4 | team_total | 0.312 | 0.425 | 0.401 | 43 | 58 | no | +0.091 | OK |
| KXNHLGAME-26OCT20DETSEA-DET | game_winner | 0.415 | 0.525 | 0.503 | 53 | 48 | no | +0.087 | OK |
| KXNHLGAME-26OCT20DETSEA-SEA | game_winner | 0.585 | 0.475 | 0.497 | 48 | 53 | yes | +0.087 | OK |
| KXNHLGAME-26OCT20BOSDAL-BOS | game_winner | 0.497 | 0.395 | 0.415 | 40 | 61 | yes | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL3 | team_total | 0.537 | 0.640 | 0.620 | 65 | 37 | no | +0.077 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL3 | game_spread | 0.152 | 0.245 | 0.224 | 25 | 76 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET2 | game_spread | 0.211 | 0.310 | 0.288 | 32 | 70 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET5 | team_total | 0.145 | 0.240 | 0.218 | 25 | 77 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET2 | team_total | 0.748 | 0.835 | 0.820 | 84 | 17 | no | +0.072 | OK |
| KXNHLGAME-26OCT20BOSDAL-DAL | game_winner | 0.503 | 0.595 | 0.577 | 60 | 41 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL5 | team_total | 0.150 | 0.240 | 0.220 | 25 | 77 | no | +0.067 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET3 | game_spread | 0.116 | 0.195 | 0.176 | 20 | 81 | no | +0.064 | OK |
| KXNHLTOTAL-26OCT20DETSEA-7 | game_total | 0.410 | 0.495 | 0.478 | 50 | 51 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL2 | team_total | 0.760 | 0.845 | 0.830 | 86 | 17 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT20DETSEA-6 | game_total | 0.523 | 0.605 | 0.589 | 61 | 40 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL2 | game_spread | 0.275 | 0.355 | 0.338 | 36 | 65 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-5 | game_total | 0.680 | 0.755 | 0.741 | 76 | 25 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR3 | game_spread | 0.307 | 0.385 | 0.369 | 39 | 62 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT20DETSEA-5 | game_total | 0.745 | 0.815 | 0.802 | 82 | 19 | no | +0.055 | OK |
| KXNHLGAME-26OCT20CARVAN-CAR | game_winner | 0.663 | 0.735 | 0.721 | 74 | 27 | no | +0.053 | OK |
| KXNHLGAME-26OCT20CARVAN-VAN | game_winner | 0.337 | 0.265 | 0.279 | 27 | 74 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA2 | game_spread | 0.356 | 0.285 | 0.299 | 29 | 72 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB4 | team_total | 0.324 | 0.395 | 0.380 | 40 | 61 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-4 | game_total | 0.786 | 0.845 | 0.834 | 85 | 16 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT20TBVGK-5 | game_total | 0.736 | 0.795 | 0.784 | 80 | 21 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR2 | game_spread | 0.450 | 0.515 | 0.502 | 52 | 49 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-WPG2 | game_spread | 0.197 | 0.255 | 0.242 | 26 | 75 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT20DETSEA-4 | game_total | 0.833 | 0.885 | 0.876 | 89 | 12 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-BOS2 | game_spread | 0.270 | 0.215 | 0.225 | 22 | 79 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB3 | team_total | 0.547 | 0.605 | 0.593 | 61 | 40 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT20DETSEA-8 | game_total | 0.229 | 0.285 | 0.273 | 29 | 72 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN3 | team_total | 0.503 | 0.445 | 0.457 | 45 | 56 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB2 | team_total | 0.764 | 0.825 | 0.814 | 84 | 19 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT20TBVGK-4 | game_total | 0.828 | 0.875 | 0.867 | 88 | 13 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-6 | game_total | 0.449 | 0.505 | 0.494 | 51 | 50 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT20TBVGK-6 | game_total | 0.512 | 0.565 | 0.554 | 57 | 44 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT20TBVGK-7 | game_total | 0.402 | 0.455 | 0.444 | 46 | 55 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN4 | team_total | 0.294 | 0.245 | 0.254 | 25 | 76 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT20DETSEA-9 | game_total | 0.158 | 0.205 | 0.195 | 21 | 80 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT20WPGSTL-WPG3 | team_total | 0.493 | 0.545 | 0.535 | 55 | 46 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT20TBVGK-TB2 | game_spread | 0.246 | 0.295 | 0.285 | 30 | 71 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT20WPGSTL-WPG2 | team_total | 0.730 | 0.775 | 0.766 | 78 | 23 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-7 | game_total | 0.336 | 0.385 | 0.375 | 39 | 62 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT20WPGSTL-WPG4 | team_total | 0.278 | 0.330 | 0.319 | 34 | 68 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT20TBVGK-8 | game_total | 0.220 | 0.265 | 0.256 | 27 | 74 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT20CARVAN-VAN2 | game_spread | 0.164 | 0.125 | 0.132 | 13 | 88 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5 | team_total | 0.143 | 0.105 | 0.112 | 11 | 90 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-WPG3 | game_spread | 0.106 | 0.145 | 0.136 | 15 | 86 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-8 | game_total | 0.173 | 0.220 | 0.210 | 23 | 79 | no | +0.026 | OK |
| KXNHLGAME-26OCT20WPGSTL-STL | game_winner | 0.603 | 0.555 | 0.565 | 56 | 45 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET6 | team_total | 0.059 | 0.100 | 0.090 | 11 | 91 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL6 | team_total | 0.060 | 0.100 | 0.090 | 11 | 91 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB5 | team_total | 0.165 | 0.215 | 0.204 | 23 | 80 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA3 | game_spread | 0.224 | 0.185 | 0.192 | 19 | 82 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT20TBVGK-TB3 | game_spread | 0.138 | 0.180 | 0.171 | 19 | 83 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2 | team_total | 0.736 | 0.695 | 0.704 | 70 | 31 | yes | +0.022 | OK |
| KXNHLGAME-26OCT20TBVGK-TB | game_winner | 0.461 | 0.505 | 0.496 | 51 | 50 | no | +0.022 | OK |
| KXNHLGAME-26OCT20TBVGK-VGK | game_winner | 0.539 | 0.495 | 0.504 | 50 | 51 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-9 | game_total | 0.113 | 0.145 | 0.138 | 15 | 86 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR3 | team_total | 0.740 | 0.775 | 0.768 | 78 | 23 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-3 | game_total | 0.940 | 0.965 | 0.961 | 97 | 4 | no | +0.017 | OK |
| KXNHLGAME-26OCT20WPGSTL-WPG | game_winner | 0.397 | 0.435 | 0.427 | 44 | 57 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-STL2 | game_spread | 0.371 | 0.335 | 0.342 | 34 | 67 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR4 | team_total | 0.538 | 0.580 | 0.572 | 59 | 43 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2 | team_total | 0.890 | 0.920 | 0.915 | 93 | 9 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT20DETSEA-10 | game_total | 0.070 | 0.100 | 0.093 | 11 | 91 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT20CARVAN-VAN3 | game_spread | 0.088 | 0.065 | 0.069 | 7 | 94 | yes | +0.014 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-BOS3 | game_spread | 0.152 | 0.125 | 0.130 | 13 | 88 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT20WPGSTL-WPG5 | team_total | 0.127 | 0.160 | 0.153 | 17 | 85 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6 | team_total | 0.176 | 0.205 | 0.199 | 21 | 80 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT20WPGSTL-5 | game_total | 0.735 | 0.765 | 0.759 | 77 | 24 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5 | team_total | 0.149 | 0.125 | 0.130 | 13 | 88 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT20DETSEA-3 | game_total | 0.957 | 0.975 | 0.972 | 98 | 3 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR5 | team_total | 0.334 | 0.370 | 0.363 | 38 | 64 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT20WPGSTL-6 | game_total | 0.505 | 0.535 | 0.529 | 54 | 47 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT20TBVGK-9 | game_total | 0.153 | 0.180 | 0.174 | 19 | 83 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB6 | team_total | 0.069 | 0.090 | 0.085 | 10 | 92 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN6 | team_total | 0.059 | 0.040 | 0.043 | 5 | 97 | yes | +0.005 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ STL | 0.603 | 0.597 | 0.174 | 0.214 | 5.87 | 6.23 | 0.977/1.003 | KXNHLTOTAL-26OCT20WPGSTL-7 +0.065 |
| BOS @ DAL | 0.503 | 0.527 | 0.191 | 0.220 | 5.54 | 6.21 | 0.994/0.956 | KXNHLTOTAL-26OCT20BOSDAL-7 +0.121 |
| MIN @ EDM | 0.561 | 0.594 | 0.174 | 0.207 | 6.39 | 6.68 | 0.994/0.993 | KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4 +0.058 |
| DET @ SEA | 0.585 | 0.572 | 0.176 | 0.217 | 5.98 | 6.26 | 1.023/1.024 | KXNHLTOTAL-26OCT20DETSEA-7 +0.055 |
| CAR @ VAN | 0.337 | 0.443 | 0.157 | 0.212 | 6.47 | 6.52 | 1.030/1.003 | KXNHLSPREAD-26OCT20CARVAN-CAR2 -0.115 |
| TBL @ VGK | 0.539 | 0.583 | 0.181 | 0.217 | 5.92 | 6.09 | 1.003/0.952 | KXNHLTEAMTOTAL-26OCT20TBVGK-VGK3 +0.055 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 24 recommended · full analysis in card.md / packet.json `thesis_card`

- Robert Thomas: 1+ goals YES @ 22c · p 0.2981 (adj 0.2773) · $8.08 · thesis STL:OFFENSE_4PLUS
- Haydn Fleury: 1+ goals NO @ 94c · p 0.9619 (adj 0.9552) · $12.17 · thesis DIFFUSE
- Philip Broberg: 1+ assists YES @ 33c · p 0.4115 (adj 0.3682) · $3.35 · thesis STL:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 15c · p 0.1792 (adj 0.1694) · $1.51 · thesis STL:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7354 (adj 0.7203) · $12.17 · thesis DAL:SUPPRESSED
- Boston over 2.5 goals scored YES @ 51c · p 0.5983 (adj 0.5516) · $6.73 · thesis BOS:OFFENSE_4PLUS
- Pavel Zacha: 1+ goals YES @ 23c · p 0.2703 (adj 0.259) · $2.34 · thesis BOS:OFFENSE_4PLUS
- Thomas Harley: 1+ assists YES @ 32c · p 0.3849 (adj 0.3475) · $3.4 · thesis DAL:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 13c · p 0.1898 (adj 0.1724) · $5.57 · thesis EDM:OFFENSE_4PLUS
- Kasperi Kapanen: 1+ assists YES @ 22c · p 0.311 (adj 0.263) · $5.07 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 32c · p 0.4097 (adj 0.3623) · $7.42 · thesis EDM:SUPPRESSED
- Zach Hyman: 1+ goals YES @ 33c · p 0.3749 (adj 0.3612) · $4.25 · thesis EDM:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 11c · p 0.1534 (adj 0.1413) · $3.79 · thesis SEA:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 68c · p 0.7414 (adj 0.7248) · $12.17 · thesis DET:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 13c · p 0.1691 (adj 0.1581) · $3.32 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 17c · p 0.2119 (adj 0.2002) · $3.51 · thesis SEA:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 16c · p 0.2489 (adj 0.2254) · $8.71 · thesis VAN:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 49c · p 0.6566 (adj 0.5451) · $3.69 · thesis VAN:WINS
- Carolina wins by over 2.5 goals NO @ 62c · p 0.7693 (adj 0.669) · $6.48 · thesis VAN:WINS
- Sebastian Aho: 1+ goals NO @ 62c · p 0.6853 (adj 0.6677) · $10.89 · thesis CAR:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 4c · p 0.0802 (adj 0.0689) · $3.29 · thesis VGK:OFFENSE_4PLUS
- Brett Howden: 1+ goals YES @ 19c · p 0.2331 (adj 0.2211) · $3.53 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 72c · p 0.7669 (adj 0.7539) · $11.64 · thesis VGK:SUPPRESSED
- Nikita Kucherov: 1+ goals NO @ 65c · p 0.6958 (adj 0.6818) · $6.94 · thesis TBL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ STL** · priced 204/209 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 26.09, exp saves 22.93 (sd 6.2), pull risk 0.048
- WPG net: Stuart Skinner (CONFIRMED) exp shots 26.62, exp saves 22.57 (sd 6.42), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Samberg: 1+ assists | 0.232 | 0.115 | 22/99 | +0.000 | STANDARD |
| Morgan Barron: 1+ points | 0.260 | 0.145 | 28/99 | -0.034 | STANDARD |
| Philip Broberg: 1+ points | 0.467 | 0.365 | 37/64 | +0.080 | STANDARD |
| Pius Suter: 1+ assists | 0.206 | 0.110 | 21/99 | -0.015 | STANDARD |
| Jonatan Berggren: 1+ assists | 0.324 | 0.230 | 27/81 | +0.040 | STANDARD |
| Cole Koepke: 1+ points | 0.208 | 0.115 | 22/99 | -0.024 | STANDARD |

**BOS @ DAL** · priced 162/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.49, exp saves 21.25 (sd 6.05), pull risk 0.059
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.85, exp saves 24.03 (sd 6.59), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.226 | 0.325 | 34/69 | +0.069 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.441 | 0.525 | 54/49 | +0.051 | STANDARD |
| Thomas Harley: 1+ assists | 0.385 | 0.310 | 32/70 | +0.050 | STANDARD |
| Thomas Harley: 1+ points | 0.445 | 0.370 | 38/64 | +0.048 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.346 | 0.415 | 43/60 | +0.038 | STANDARD |
| Miro Heiskanen: 1+ points | 0.471 | 0.540 | 55/47 | +0.041 | STANDARD |

**MIN @ EDM** · priced 191/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROBABLE) exp shots 27.88, exp saves 24.36 (sd 6.6), pull risk 0.06
- MIN net: Jesper Wallstedt (PROBABLE) exp shots 29.26, exp saves 24.78 (sd 6.99), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.221 | 0.340 | 35/67 | +0.093 | STANDARD |
| Alex Formenton: 1+ points | 0.339 | 0.230 | 24/78 | +0.086 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.480 | 0.580 | 59/43 | +0.073 | STANDARD |
| Kasperi Kapanen: 1+ points | 0.423 | 0.325 | 33/68 | +0.078 | STANDARD |
| Mattias Ekholm: 1+ points | 0.452 | 0.355 | 36/65 | +0.076 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.311 | 0.215 | 22/79 | +0.079 | STANDARD |

**DET @ SEA** · priced 176/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (CONFIRMED) exp shots 29.42, exp saves 25.64 (sd 6.73), pull risk 0.054
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.75, exp saves 22.88 (sd 6.51), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Larsson: 1+ assists | 0.313 | 0.185 | 19/82 | +0.113 | STANDARD |
| Moritz Seider: 1+ points | 0.462 | 0.590 | 60/42 | +0.101 | STANDARD |
| Adam Larsson: 1+ points | 0.358 | 0.240 | 25/77 | +0.095 | STANDARD |
| Moritz Seider: 1+ assists | 0.401 | 0.505 | 51/50 | +0.081 | STANDARD |
| Moritz Seider: 2+ points | 0.127 | 0.230 | 24/78 | +0.081 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.352 | 0.255 | 27/76 | +0.069 | STANDARD |

**CAR @ VAN** · priced 177/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 32.33, exp saves 27.64 (sd 7.5), pull risk 0.08
- CAR net: Pyotr Kochetkov (CONFIRMED) exp shots 22.8, exp saves 19.94 (sd 5.73), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.222 | 0.350 | 36/66 | +0.103 | STANDARD |
| Bradly Nadeau: 1+ assists | 0.150 | 0.265 | 28/75 | +0.087 | STANDARD |
| Drew O'Connor: 1+ assists | 0.205 | 0.095 | 16/97 | +0.035 | STANDARD |
| Drew O'Connor: 1+ points | 0.343 | 0.235 | 24/77 | +0.090 | STANDARD |
| Bradly Nadeau: 1+ points | 0.301 | 0.405 | 41/60 | +0.082 | STANDARD |
| Sebastian Aho: 1+ assists | 0.397 | 0.500 | 51/51 | +0.076 | STANDARD |

**TBL @ VGK** · priced 196/201 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.99, exp saves 23.6 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.35, exp saves 22.57 (sd 6.35), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 2+ points | 0.243 | 0.375 | 39/64 | +0.101 | STANDARD |
| Andrei Vasilevskiy: 27+ saves | 0.256 | 0.385 | 40/63 | +0.098 |  |
| Brett Howden: 1+ assists | 0.231 | 0.105 | 20/99 | +0.020 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.437 | 0.560 | 57/45 | +0.096 | STANDARD |
| Erik Cernak: 1+ assists | 0.192 | 0.075 | 14/99 | +0.043 | STANDARD |
| Erik Cernak: 1+ points | 0.230 | 0.115 | 18/95 | +0.040 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
