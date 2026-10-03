# NHL slate 2026-10-03 — RESEARCH_ONLY

generated 2026-10-03T23:55:12Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 13 · simulated (not started): 5 · markets on board: 3872 · contracts joined: 828 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 703, 'OK': 69, 'NO_EDGE': 56}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 108, 'game_early_goal': 5, 'first_goal': 170, 'game_winner': 10, 'player_goals': 169, 'game_overtime': 5, 'player_points': 120, 'goalie_saves': 6, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| DAL @ NSH | 2026-10-04T00:00:00Z | T-<10m | 0.490 | 0.510 | 0.181 | 5.96 | 2.95 | 3.01 | 165 (25/140) | PROBABLE/CONFIRMED |
| BOS @ MIN | 2026-10-04T00:00:00Z | T-<10m | 0.637 | 0.363 | 0.168 | 6.31 | 3.59 | 2.72 | 171 (25/146) | CONFIRMED/CONFIRMED |
| STL @ COL | 2026-10-04T01:00:00Z | T-60m | 0.665 | 0.335 | 0.153 | 6.73 | 3.93 | 2.80 | 169 (25/144) | PROBABLE/PROBABLE |
| CGY @ VAN | 2026-10-04T02:00:00Z | T-90m | 0.468 | 0.532 | 0.174 | 6.29 | 3.04 | 3.25 | 160 (25/135) | PROBABLE/CONFIRMED |
| LAK @ SJS | 2026-10-04T02:00:00Z | T-90m | 0.490 | 0.510 | 0.174 | 6.11 | 3.02 | 3.09 | 163 (25/138) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL4 | team_total | 0.318 | 0.240 | 0.255 | 25 | 77 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL3 | team_total | 0.525 | 0.455 | 0.469 | 46 | 55 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT03STLCOL-8 | game_total | 0.341 | 0.275 | 0.288 | 28 | 73 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL5 | team_total | 0.162 | 0.105 | 0.115 | 11 | 90 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL4 | team_total | 0.369 | 0.435 | 0.422 | 44 | 57 | no | +0.043 | OK |
| KXNHLGAME-26OCT03DALNSH-NSH | game_winner | 0.490 | 0.425 | 0.438 | 43 | 58 | yes | +0.043 | OK |
| KXNHLGAME-26OCT03STLCOL-COL | game_winner | 0.665 | 0.725 | 0.713 | 73 | 28 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL3 | team_total | 0.586 | 0.645 | 0.634 | 65 | 36 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT03STLCOL-9 | game_total | 0.247 | 0.195 | 0.205 | 20 | 81 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT03STLCOL-6 | game_total | 0.643 | 0.585 | 0.597 | 59 | 42 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT03STLCOL-7 | game_total | 0.533 | 0.475 | 0.487 | 48 | 53 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL2 | game_spread | 0.458 | 0.515 | 0.503 | 52 | 49 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL3 | game_spread | 0.320 | 0.375 | 0.364 | 38 | 63 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL2 | team_total | 0.757 | 0.700 | 0.712 | 71 | 31 | yes | +0.033 | OK |
| KXNHLGAME-26OCT03DALNSH-DAL | game_winner | 0.510 | 0.565 | 0.554 | 57 | 44 | no | +0.033 | OK |
| KXNHLGAME-26OCT03STLCOL-STL | game_winner | 0.335 | 0.285 | 0.295 | 29 | 72 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL3 | game_spread | 0.168 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL2 | game_spread | 0.285 | 0.335 | 0.325 | 34 | 67 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT03STLCOL-STL2 | game_spread | 0.167 | 0.125 | 0.133 | 13 | 88 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL5 | team_total | 0.189 | 0.240 | 0.229 | 25 | 77 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT03LASJ-5 | game_total | 0.761 | 0.805 | 0.797 | 81 | 20 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT03DALNSH-5 | game_total | 0.741 | 0.785 | 0.777 | 79 | 22 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL6 | team_total | 0.069 | 0.035 | 0.040 | 4 | 97 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL2 | team_total | 0.795 | 0.845 | 0.836 | 86 | 17 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT03STLCOL-10 | game_total | 0.131 | 0.090 | 0.097 | 10 | 92 | yes | +0.024 | OK |
| KXNHLGAME-26OCT03CGYVAN-VAN | game_winner | 0.468 | 0.515 | 0.506 | 52 | 49 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT03DALNSH-4 | game_total | 0.829 | 0.865 | 0.858 | 87 | 14 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT03LASJ-6 | game_total | 0.543 | 0.585 | 0.577 | 59 | 42 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-VAN3 | game_spread | 0.150 | 0.185 | 0.178 | 19 | 82 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ4 | team_total | 0.364 | 0.410 | 0.401 | 42 | 60 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT03LASJ-SJ3 | game_spread | 0.161 | 0.195 | 0.188 | 20 | 81 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-VAN2 | game_spread | 0.258 | 0.295 | 0.287 | 30 | 71 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT03DALNSH-NSH2 | game_spread | 0.269 | 0.235 | 0.242 | 24 | 77 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT03LASJ-4 | game_total | 0.848 | 0.875 | 0.870 | 88 | 13 | no | +0.014 | OK |
| KXNHLGAME-26OCT03CGYVAN-CGY | game_winner | 0.532 | 0.495 | 0.502 | 50 | 51 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT03LASJ-7 | game_total | 0.429 | 0.465 | 0.458 | 47 | 54 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL6 | team_total | 0.081 | 0.105 | 0.100 | 11 | 90 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT03STLCOL-5 | game_total | 0.824 | 0.795 | 0.801 | 80 | 21 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY4 | team_total | 0.418 | 0.380 | 0.388 | 39 | 63 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT03DALNSH-7 | game_total | 0.412 | 0.445 | 0.438 | 45 | 56 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-CGY2 | game_spread | 0.313 | 0.285 | 0.290 | 29 | 72 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ3 | team_total | 0.585 | 0.615 | 0.609 | 62 | 39 | no | +0.008 | OK |
| KXNHLGAME-26OCT03BOSMIN-BOS | game_winner | 0.363 | 0.335 | 0.340 | 34 | 67 | yes | +0.007 | OK |
| KXNHLGAME-26OCT03BOSMIN-MIN | game_winner | 0.637 | 0.665 | 0.660 | 67 | 34 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT03LASJ-3 | game_total | 0.961 | 0.975 | 0.973 | 98 | 3 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY6 | team_total | 0.113 | 0.090 | 0.094 | 10 | 92 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT03STLCOL-4 | game_total | 0.893 | 0.875 | 0.879 | 88 | 13 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ5 | team_total | 0.193 | 0.220 | 0.214 | 23 | 79 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT03DALNSH-9 | game_total | 0.155 | 0.175 | 0.171 | 18 | 83 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT03STLCOL-STL3 | game_spread | 0.090 | 0.070 | 0.074 | 8 | 94 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY3 | team_total | 0.631 | 0.600 | 0.606 | 61 | 41 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-COL6 | team_total | 0.205 | 0.185 | 0.189 | 19 | 82 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT03DALNSH-6 | game_total | 0.528 | 0.555 | 0.550 | 56 | 45 | no | +0.004 | OK |
| KXNHLSPREAD-26OCT03BOSMIN-MIN3 | game_spread | 0.271 | 0.295 | 0.290 | 30 | 71 | no | +0.004 | OK |
| KXNHLSPREAD-26OCT03BOSMIN-MIN2 | game_spread | 0.409 | 0.435 | 0.430 | 44 | 57 | no | +0.004 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-CGY3 | game_spread | 0.195 | 0.175 | 0.179 | 18 | 83 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT03STLCOL-3 | game_total | 0.975 | 0.965 | 0.967 | 97 | 4 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT03BOSMIN-3 | game_total | 0.965 | 0.975 | 0.973 | 98 | 3 | no | +0.003 | OK |
| KXNHLGAME-26OCT03LASJ-LA | game_winner | 0.510 | 0.485 | 0.490 | 49 | 52 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-BOS3 | team_total | 0.520 | 0.495 | 0.500 | 50 | 51 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT03DALNSH-8 | game_total | 0.225 | 0.250 | 0.245 | 26 | 76 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY5 | team_total | 0.234 | 0.210 | 0.215 | 22 | 80 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT03DALNSH-3 | game_total | 0.956 | 0.965 | 0.963 | 97 | 4 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT03LASJ-8 | game_total | 0.246 | 0.265 | 0.261 | 27 | 74 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ2 | team_total | 0.798 | 0.825 | 0.820 | 84 | 19 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT03CGYVAN-8 | game_total | 0.274 | 0.255 | 0.259 | 26 | 75 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT03STLCOL-2 | game_total | 0.991 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLSPREAD-26OCT03LASJ-SJ2 | game_spread | 0.275 | 0.295 | 0.291 | 30 | 71 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT03BOSMIN-10 | game_total | 0.096 | 0.085 | 0.087 | 9 | 92 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN2 | team_total | 0.800 | 0.825 | 0.820 | 84 | 19 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-BOS5 | team_total | 0.148 | 0.135 | 0.138 | 14 | 87 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT03DALNSH-10 | game_total | 0.067 | 0.080 | 0.077 | 9 | 93 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-CGY2 | team_total | 0.829 | 0.810 | 0.814 | 82 | 20 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03LASJ-SJ6 | team_total | 0.086 | 0.095 | 0.093 | 10 | 91 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT03LASJ-9 | game_total | 0.172 | 0.190 | 0.186 | 20 | 82 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT03CGYVAN-5 | game_total | 0.782 | 0.795 | 0.793 | 80 | 21 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT03BOSMIN-5 | game_total | 0.782 | 0.795 | 0.793 | 80 | 21 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT03DALNSH-NSH3 | game_spread | 0.155 | 0.145 | 0.147 | 15 | 86 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03STLCOL-COL2 | team_total | 0.898 | 0.905 | 0.904 | 91 | 10 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-BOS6 | team_total | 0.059 | 0.050 | 0.052 | 6 | 96 |  | -0.005 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| DAL @ NSH | 0.490 | 0.527 | 0.181 | 0.222 | 5.96 | 6.07 | 1.002/0.968 | KXNHLTEAMTOTAL-26OCT03DALNSH-NSH4 +0.043 |
| BOS @ MIN | 0.637 | 0.624 | 0.168 | 0.205 | 6.31 | 6.44 | 0.991/0.999 | KXNHLTOTAL-26OCT03BOSMIN-7 +0.024 |
| STL @ COL | 0.665 | 0.634 | 0.153 | 0.200 | 6.73 | 6.42 | 0.977/1.024 | KXNHLTEAMTOTAL-26OCT03STLCOL-COL5 -0.062 |
| CGY @ VAN | 0.468 | 0.555 | 0.174 | 0.218 | 6.29 | 6.33 | 1.030/0.978 | KXNHLGAME-26OCT03CGYVAN-CGY -0.086 |
| LAK @ SJS | 0.490 | 0.522 | 0.174 | 0.222 | 6.11 | 6.12 | 1.039/0.988 | KXNHLSPREAD-26OCT03LASJ-LA2 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 19 recommended · full analysis in card.md / packet.json `thesis_card`

- Mikko Rantanen: 1+ goals NO @ 69c · p 0.7519 (adj 0.7352) · $12.61 · thesis DAL:SUPPRESSED
- Dallas wins by over 2.5 goals NO @ 79c · p 0.8509 (adj 0.8179) · $9.99 · thesis NSH:WINS
- Mavrik Bourque: 1+ goals YES @ 18c · p 0.2161 (adj 0.2058) · $2.59 · thesis NSH:OFFENSE_4PLUS
- Jason Robertson: 1+ goals NO @ 62c · p 0.659 (adj 0.6468) · $3.73 · thesis DAL:SUPPRESSED
- Yakov Trenin: 1+ goals YES @ 11c · p 0.151 (adj 0.1395) · $3.73 · thesis MIN:OFFENSE_4PLUS
- Olli Maatta: 1+ goals YES @ 5c · p 0.0818 (adj 0.0688) · $2.2 · thesis MIN:OFFENSE_4PLUS
- JJ Peterka: 1+ assists NO @ 71c · p 0.8346 (adj 0.7471) · $12.61 · thesis BOS:SUPPRESSED
- Max Shabanov: 1+ assists NO @ 68c · p 0.7922 (adj 0.7128) · $11.76 · thesis MIN:SUPPRESSED
- Colorado wins NO @ 28c · p 0.3688 (adj 0.3266) · $5.68 · thesis STL:WINS
- Pius Suter: 1+ goals YES @ 11c · p 0.1483 (adj 0.1375) · $2.92 · thesis STL:OFFENSE_4PLUS
- Connor McMichael: 1+ assists NO @ 78c · p 0.85 (adj 0.8125) · $12.61 · thesis STL:SUPPRESSED
- Nathan MacKinnon: 1+ goals NO @ 55c · p 0.6063 (adj 0.591) · $6.5 · thesis COL:SUPPRESSED
- Zayne Parekh: 1+ goals NO @ 85c · p 0.8998 (adj 0.8849) · $11.4 · thesis CGY:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 25c · p 0.3095 (adj 0.2934) · $5.43 · thesis VAN:OFFENSE_4PLUS
- Paul Cotter: 1+ goals NO @ 83c · p 0.8723 (adj 0.8605) · $11.4 · thesis VAN:SUPPRESSED
- Linus Karlsson: 1+ goals YES @ 22c · p 0.2631 (adj 0.2511) · $3.3 · thesis VAN:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 58c · p 0.8177 (adj 0.6599) · $12.41 · thesis LAK:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 13c · p 0.1968 (adj 0.1789) · $6.71 · thesis SJS:OFFENSE_4PLUS
- Mason Marchment: 1+ assists NO @ 67c · p 0.8085 (adj 0.7152) · $12.41 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**DAL @ NSH** · priced 114/114 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 27.51, exp saves 23.93 (sd 6.48), pull risk 0.053
- DAL net: Casey DeSmith (CONFIRMED) exp shots 26.36, exp saves 22.78 (sd 6.36), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 1+ points | 0.532 | 0.655 | 66/35 | +0.102 | STANDARD |
| Mikko Rantanen: 2+ points | 0.175 | 0.295 | 30/71 | +0.101 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.377 | 0.495 | 50/51 | +0.095 | STANDARD |
| Roope Hintz: 1+ assists | 0.244 | 0.360 | 37/65 | +0.090 | STANDARD |
| Roope Hintz: 1+ points | 0.433 | 0.545 | 56/47 | +0.079 | STANDARD |
| Miro Heiskanen: 1+ points | 0.464 | 0.565 | 58/45 | +0.069 | STANDARD |

**BOS @ MIN** · priced 118/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.46, exp saves 24.15 (sd 6.44), pull risk 0.05
- BOS net: Michael DiPietro (CONFIRMED) exp shots 30.36, exp saves 25.66 (sd 7.14), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| JJ Peterka: 1+ assists | 0.165 | 0.300 | 31/71 | +0.110 | STANDARD |
| Max Shabanov: 1+ assists | 0.208 | 0.330 | 34/68 | +0.097 | STANDARD |
| JJ Peterka: 1+ points | 0.344 | 0.455 | 47/56 | +0.078 | STANDARD |
| Max Shabanov: 1+ points | 0.363 | 0.470 | 49/55 | +0.070 | STANDARD |
| Elias Lindholm: 1+ points | 0.466 | 0.375 | 40/65 | +0.049 | STANDARD |
| Jesper Wallstedt: 24+ saves | 0.534 | 0.445 | 49/60 | +0.027 |  |

**STL @ COL** · priced 118/118 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROBABLE) exp shots 24.45, exp saves 21.42 (sd 5.99), pull risk 0.051
- STL net: Jordan Binnington (PROBABLE) exp shots 31.38, exp saves 26.45 (sd 7.4), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mackenzie Blackwood: 21+ saves | 0.558 | 0.290 | 53/95 | +0.010 |  |
| Nathan MacKinnon: 2+ points | 0.343 | 0.535 | 54/47 | +0.170 | STANDARD |
| Cale Makar: 2+ points | 0.186 | 0.355 | 36/65 | +0.148 | STANDARD |
| Cale Makar: 1+ assists | 0.444 | 0.605 | 62/41 | +0.129 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.502 | 0.650 | 66/36 | +0.122 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.158 | 0.300 | 33/73 | +0.098 | STANDARD |

**CGY @ VAN** · priced 106/109 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 28.38, exp saves 24.66 (sd 6.66), pull risk 0.058
- CGY net: Devin Cooley (CONFIRMED) exp shots 28.2, exp saves 24.23 (sd 6.63), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Marco Rossi: 1+ goals | 0.309 | 0.245 | 25/76 | +0.046 | STANDARD |
| Zayne Parekh: 1+ goals | 0.100 | 0.160 | 17/85 | +0.041 | STANDARD |
| Zayne Parekh: 1+ points | 0.389 | 0.445 | 46/57 | +0.024 | STANDARD |
| Joel Farabee: 1+ assists | 0.349 | 0.295 | 31/72 | +0.025 | STANDARD |
| Marco Rossi: 1+ points | 0.576 | 0.525 | 54/49 | +0.019 | STANDARD |
| Linus Karlsson: 1+ goals | 0.263 | 0.215 | 22/79 | +0.031 | STANDARD |

**LAK @ SJS** · priced 105/112 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.98, exp saves 24.31 (sd 6.6), pull risk 0.054
- LAK net: Anton Forsberg (PROBABLE) exp shots 26.75, exp saves 23.29 (sd 6.35), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.182 | 0.425 | 43/58 | +0.221 | STANDARD |
| Mason Marchment: 1+ assists | 0.192 | 0.335 | 34/67 | +0.123 | STANDARD |
| Artemi Panarin: 1+ assists | 0.372 | 0.515 | 52/49 | +0.120 | STANDARD |
| Luca Cagnoni: 1+ points | 0.319 | 0.420 | 43/59 | +0.074 | PRIOR_HEAVY |
| Alex Laferriere: 1+ assists | 0.375 | 0.280 | 29/73 | +0.070 | STANDARD |
| Mats Zuccarello: 2+ assists | 0.017 | 0.110 | 12/90 | +0.077 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
