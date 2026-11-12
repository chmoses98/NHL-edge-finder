# NHL slate 2026-11-11 — RESEARCH_ONLY

generated 2026-11-12T00:12:12Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 5 · markets on board: 3399 · contracts joined: 1175 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 1050, 'OK': 46, 'NO_EDGE': 79}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 175, 'game_early_goal': 5, 'first_goal': 180, 'game_winner': 10, 'player_goals': 310, 'game_overtime': 5, 'player_points': 243, 'goalie_saves': 12, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ CGY | 2026-11-12T00:30:00Z | T-10m | 0.551 | 0.449 | 0.182 | 5.85 | 3.07 | 2.77 | 236 (25/211) | CONFIRMED/PROBABLE |
| PHI @ EDM | 2026-11-12T02:00:00Z | T-90m | 0.627 | 0.373 | 0.169 | 6.27 | 3.54 | 2.73 | 224 (25/199) | CONFIRMED/PROBABLE |
| UTA @ VGK | 2026-11-12T02:30:00Z | T-90m | 0.555 | 0.445 | 0.170 | 6.46 | 3.41 | 3.05 | 240 (25/215) | CONFIRMED/PROBABLE |
| NSH @ ANA | 2026-11-12T03:00:00Z | T-90m | 0.580 | 0.420 | 0.169 | 6.72 | 3.63 | 3.09 | 240 (25/215) | CONFIRMED/PROJECTED |
| PIT @ SJS | 2026-11-12T03:00:00Z | T-90m | 0.469 | 0.531 | 0.168 | 6.83 | 3.30 | 3.53 | 235 (25/210) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV11NYRCGY-NYR | game_winner | 0.449 | 0.575 | 0.550 | 58 | 43 | no | +0.104 | OK |
| KXNHLGAME-26NOV11NYRCGY-CGY | game_winner | 0.551 | 0.435 | 0.458 | 44 | 57 | yes | +0.094 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-NYR4 | team_total | 0.311 | 0.425 | 0.401 | 43 | 58 | no | +0.092 | OK |
| KXNHLSPREAD-26NOV11NYRCGY-NYR2 | game_spread | 0.235 | 0.345 | 0.321 | 35 | 66 | no | +0.090 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-NYR3 | team_total | 0.529 | 0.635 | 0.614 | 64 | 37 | no | +0.085 | OK |
| KXNHLSPREAD-26NOV11NYRCGY-NYR3 | game_spread | 0.129 | 0.225 | 0.203 | 23 | 78 | no | +0.079 | OK |
| KXNHLSPREAD-26NOV11NYRCGY-CGY2 | game_spread | 0.319 | 0.225 | 0.242 | 23 | 78 | yes | +0.077 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-NYR5 | team_total | 0.153 | 0.235 | 0.216 | 24 | 77 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-NYR2 | team_total | 0.758 | 0.835 | 0.821 | 85 | 18 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY3 | team_total | 0.608 | 0.535 | 0.550 | 54 | 47 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY4 | team_total | 0.379 | 0.315 | 0.327 | 32 | 69 | yes | +0.044 | OK |
| KXNHLSPREAD-26NOV11NYRCGY-CGY3 | game_spread | 0.191 | 0.135 | 0.145 | 14 | 87 | yes | +0.043 | OK |
| KXNHLGAME-26NOV11PITSJ-SJ | game_winner | 0.469 | 0.415 | 0.426 | 42 | 59 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV11PITSJ-PIT3 | game_spread | 0.203 | 0.245 | 0.236 | 25 | 76 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-NYR6 | team_total | 0.061 | 0.095 | 0.087 | 10 | 91 | no | +0.023 | OK |
| KXNHLGAME-26NOV11PITSJ-PIT | game_winner | 0.531 | 0.575 | 0.566 | 58 | 43 | no | +0.022 | OK |
| KXNHLSPREAD-26NOV11PITSJ-PIT2 | game_spread | 0.324 | 0.365 | 0.357 | 37 | 64 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV11NYRCGY-5 | game_total | 0.728 | 0.765 | 0.758 | 77 | 24 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY2 | team_total | 0.810 | 0.770 | 0.778 | 78 | 24 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY5 | team_total | 0.197 | 0.150 | 0.159 | 17 | 87 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV11PHIEDM-EDM4 | team_total | 0.487 | 0.530 | 0.522 | 54 | 48 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV11NSHANA-5 | game_total | 0.828 | 0.855 | 0.850 | 86 | 15 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV11NYRCGY-6 | game_total | 0.500 | 0.535 | 0.528 | 54 | 47 | no | +0.013 | OK |
| KXNHLSPREAD-26NOV11PHIEDM-EDM3 | game_spread | 0.264 | 0.295 | 0.289 | 30 | 71 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY6 | team_total | 0.086 | 0.060 | 0.065 | 7 | 95 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV11NYRCGY-4 | game_total | 0.820 | 0.850 | 0.844 | 86 | 16 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ6 | team_total | 0.117 | 0.095 | 0.099 | 10 | 91 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV11NYRCGY-7 | game_total | 0.393 | 0.425 | 0.419 | 43 | 58 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV11NSHANA-4 | game_total | 0.895 | 0.915 | 0.911 | 92 | 9 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV11UTAVGK-10 | game_total | 0.104 | 0.085 | 0.089 | 9 | 92 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA4 | team_total | 0.504 | 0.535 | 0.529 | 54 | 47 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV11NYRCGY-3 | game_total | 0.950 | 0.965 | 0.962 | 97 | 4 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV11PITSJ-5 | game_total | 0.835 | 0.855 | 0.851 | 86 | 15 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ3 | team_total | 0.643 | 0.615 | 0.621 | 62 | 39 | yes | +0.006 | OK |
| KXNHLTOTAL-26NOV11PITSJ-4 | game_total | 0.898 | 0.915 | 0.912 | 92 | 9 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ4 | team_total | 0.433 | 0.405 | 0.411 | 41 | 60 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV11PHIEDM-EDM2 | team_total | 0.866 | 0.895 | 0.890 | 91 | 12 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV11PHIEDM-PHI6 | team_total | 0.059 | 0.045 | 0.048 | 5 | 96 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ5 | team_total | 0.247 | 0.225 | 0.229 | 23 | 78 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV11UTAVGK-8 | game_total | 0.298 | 0.275 | 0.280 | 28 | 73 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4 | team_total | 0.479 | 0.505 | 0.500 | 51 | 50 | no | +0.004 | OK |
| KXNHLGAME-26NOV11NSHANA-ANA | game_winner | 0.580 | 0.555 | 0.560 | 56 | 45 | yes | +0.003 | OK |
| KXNHLSPREAD-26NOV11UTAVGK-UTA2 | game_spread | 0.244 | 0.265 | 0.261 | 27 | 74 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA6 | team_total | 0.161 | 0.140 | 0.144 | 15 | 87 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV11PHIEDM-4 | game_total | 0.861 | 0.875 | 0.872 | 88 | 13 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV11PITSJ-10 | game_total | 0.138 | 0.125 | 0.128 | 13 | 88 | yes | +0.000 | OK |
| KXNHLSPREAD-26NOV11PITSJ-SJ2 | game_spread | 0.263 | 0.240 | 0.244 | 25 | 77 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-9 | game_total | 0.262 | 0.245 | 0.248 | 25 | 76 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT5 | team_total | 0.286 | 0.310 | 0.305 | 32 | 70 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT2 | team_total | 0.863 | 0.880 | 0.877 | 89 | 13 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV11PHIEDM-5 | game_total | 0.780 | 0.795 | 0.792 | 80 | 21 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV11NYRCGY-2 | game_total | 0.980 | 0.990 | 0.989 |  | 2 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26NOV11NSHANA-NSH3 | game_spread | 0.134 | 0.145 | 0.143 | 15 | 86 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26NOV11UTAVGK-UTA3 | game_spread | 0.144 | 0.155 | 0.153 | 16 | 85 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT3 | team_total | 0.688 | 0.710 | 0.706 | 72 | 30 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV11UTAVGK-3 | game_total | 0.971 | 0.980 | 0.978 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26NOV11UTAVGK-UTA | game_winner | 0.445 | 0.465 | 0.461 | 47 | 54 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26NOV11UTAVGK-VGK | game_winner | 0.555 | 0.535 | 0.539 | 54 | 47 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-7 | game_total | 0.536 | 0.555 | 0.551 | 56 | 45 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV11NYRCGY-9 | game_total | 0.144 | 0.155 | 0.153 | 16 | 85 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PHIEDM-EDM3 | team_total | 0.699 | 0.720 | 0.716 | 73 | 29 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26NOV11UTAVGK-VGK2 | game_spread | 0.341 | 0.325 | 0.328 | 33 | 68 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV11UTAVGK-4 | game_total | 0.877 | 0.885 | 0.883 | 89 | 12 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH3 | team_total | 0.598 | 0.620 | 0.616 | 63 | 39 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-3 | game_total | 0.976 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH2 | team_total | 0.805 | 0.825 | 0.821 | 84 | 19 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV11PHIEDM-10 | game_total | 0.090 | 0.080 | 0.082 | 9 | 93 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV11UTAVGK-9 | game_total | 0.216 | 0.200 | 0.203 | 21 | 81 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26NOV11PHIEDM-PHI3 | game_spread | 0.100 | 0.095 | 0.096 | 10 | 91 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH4 | team_total | 0.381 | 0.395 | 0.392 | 40 | 61 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV11PHIEDM-2 | game_total | 0.986 | 0.990 | 0.989 |  | 2 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PHIEDM-EDM6 | team_total | 0.140 | 0.130 | 0.132 | 14 | 88 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PHIEDM-EDM5 | team_total | 0.284 | 0.300 | 0.297 | 31 | 71 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-3 | game_total | 0.976 | 0.980 | 0.979 | 99 | 3 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-UTA2 | team_total | 0.797 | 0.810 | 0.808 | 82 | 20 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26NOV11NSHANA-NSH2 | game_spread | 0.226 | 0.235 | 0.233 | 24 | 77 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-VGK3 | team_total | 0.667 | 0.655 | 0.657 | 66 | 35 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PHIEDM-PHI3 | team_total | 0.518 | 0.505 | 0.508 | 51 | 50 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV11PHIEDM-3 | game_total | 0.967 | 0.975 | 0.973 | 99 | 4 |  | -0.009 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ CGY | 0.551 | 0.519 | 0.182 | 0.221 | 5.85 | 6.15 | 0.978/1.004 | KXNHLTEAMTOTAL-26NOV11NYRCGY-NYR3 +0.058 |
| PHI @ EDM | 0.627 | 0.618 | 0.169 | 0.210 | 6.27 | 6.48 | 1.022/0.994 | KXNHLTOTAL-26NOV11PHIEDM-7 +0.036 |
| UTA @ VGK | 0.555 | 0.569 | 0.170 | 0.217 | 6.46 | 6.42 | 1.003/0.999 | KXNHLSPREAD-26NOV11UTAVGK-UTA2 -0.019 |
| NSH @ ANA | 0.580 | 0.664 | 0.169 | 0.191 | 6.72 | 6.83 | 0.968/0.994 | KXNHLSPREAD-26NOV11NSHANA-ANA3 +0.091 |
| PIT @ SJS | 0.469 | 0.492 | 0.168 | 0.217 | 6.83 | 6.49 | 1.039/1.012 | KXNHLTOTAL-26NOV11PITSJ-8 -0.054 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 20 recommended · full analysis in card.md / packet.json `thesis_card`

- Aydar Suniev: 1+ goals YES @ 16c · p 0.2122 (adj 0.1966) · $6.2 · thesis CGY:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 8c · p 0.1089 (adj 0.1004) · $3.09 · thesis CGY:OFFENSE_4PLUS
- Jonathan Castagna: 1+ goals YES @ 9c · p 0.1191 (adj 0.1081) · $2.55 · thesis CGY:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 68c · p 0.7276 (adj 0.7132) · $12.23 · thesis NYR:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 10c · p 0.1497 (adj 0.136) · $5.92 · thesis PHI:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 16c · p 0.217 (adj 0.2015) · $7.17 · thesis PHI:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 27c · p 0.4108 (adj 0.316) · $8.33 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ assists YES @ 27c · p 0.3491 (adj 0.3071) · $6.99 · thesis EDM:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 4c · p 0.0836 (adj 0.0714) · $4.71 · thesis VGK:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 9c · p 0.1511 (adj 0.1346) · $7.48 · thesis UTA:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 16c · p 0.2198 (adj 0.2036) · $7.55 · thesis UTA:OFFENSE_4PLUS
- Ivan Barbashev: 1+ goals YES @ 17c · p 0.2233 (adj 0.2075) · $6.41 · thesis VGK:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.1598 (adj 0.1436) · $6.67 · thesis ANA:OFFENSE_4PLUS
- Beckett Sennecke: 1+ goals YES @ 33c · p 0.4129 (adj 0.3909) · $12.1 · thesis ANA:OFFENSE_4PLUS
- Jackson LaCombe: 1+ goals YES @ 12c · p 0.1706 (adj 0.1567) · $5.54 · thesis ANA:OFFENSE_4PLUS
- Steven Stamkos: 1+ goals NO @ 62c · p 0.6891 (adj 0.6706) · $15.53 · thesis NSH:SUPPRESSED
- Rutger McGroarty: 1+ goals NO @ 84c · p 0.8695 (adj 0.8596) · $13.52 · thesis PIT:SUPPRESSED
- Ben Kindel: 1+ goals NO @ 76c · p 0.7945 (adj 0.7846) · $10.3 · thesis PIT:SUPPRESSED
- Pittsburgh wins by over 1.5 goals NO @ 64c · p 0.7029 (adj 0.6689) · $5.07 · thesis SJS:WINS
- Tyler Toffoli: 1+ assists YES @ 24c · p 0.3038 (adj 0.2644) · $2.64 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYR @ CGY** · priced 184/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 27.6, exp saves 23.91 (sd 6.56), pull risk 0.057
- NYR net: Joonas Korpisalo (PROBABLE) exp shots 28.16, exp saves 24.37 (sd 6.66), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| J.T. Miller: 1+ assists | 0.351 | 0.435 | 44/57 | +0.062 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.298 | 0.215 | 22/79 | +0.066 | STANDARD |
| Zach Whitecloud: 1+ points | 0.291 | 0.210 | 24/82 | +0.038 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.356 | 0.285 | 30/73 | +0.042 | STANDARD |
| Adam Fox: 1+ assists | 0.511 | 0.575 | 58/43 | +0.041 | STANDARD |
| Aydar Suniev: 1+ goals | 0.212 | 0.150 | 16/86 | +0.043 | STANDARD |

**PHI @ EDM** · priced 172/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 24.67, exp saves 21.71 (sd 6.11), pull risk 0.054
- PHI net: Dan Vladar (PROBABLE) exp shots 27.72, exp saves 23.38 (sd 6.77), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.589 | 0.735 | 74/27 | +0.127 | STANDARD |
| Connor McDavid: 2+ points | 0.434 | 0.570 | 58/44 | +0.109 | STANDARD |
| Connor McDavid: 2+ assists | 0.229 | 0.365 | 38/65 | +0.105 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.480 | 0.610 | 62/40 | +0.103 | STANDARD |
| Leon Draisaitl: 2+ points | 0.350 | 0.475 | 49/54 | +0.092 | STANDARD |
| Leon Draisaitl: 2+ assists | 0.141 | 0.240 | 26/78 | +0.067 | STANDARD |

**UTA @ VGK** · priced 184/189 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.76, exp saves 23.36 (sd 6.35), pull risk 0.054
- UTA net: Sebastian Cossa (PROBABLE) exp shots 27.42, exp saves 23.43 (sd 6.56), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brayden McNabb: 1+ points | 0.375 | 0.255 | 27/76 | +0.091 | STANDARD |
| Brayden McNabb: 1+ assists | 0.317 | 0.200 | 23/83 | +0.075 | STANDARD |
| Lawson Crouse: 1+ points | 0.437 | 0.330 | 35/69 | +0.071 | STANDARD |
| Mitch Marner: 1+ assists | 0.452 | 0.555 | 57/46 | +0.071 | STANDARD |
| Andrew Peeke: 1+ points | 0.272 | 0.175 | 23/88 | +0.030 | STANDARD |
| Ivan Barbashev: 1+ points | 0.514 | 0.420 | 43/59 | +0.067 | STANDARD |

**NSH @ ANA** · priced 188/189 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 26.26, exp saves 23.15 (sd 6.25), pull risk 0.047
- NSH net: Justus Annunen (PROJECTED) exp shots 30.23, exp saves 25.3 (sd 7.29), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Killorn: 1+ points | 0.497 | 0.390 | 40/62 | +0.080 | STANDARD |
| Mavrik Bourque: 1+ points | 0.372 | 0.475 | 49/54 | +0.071 | STANDARD |
| Ryan O'Reilly: 1+ assists | 0.381 | 0.480 | 49/53 | +0.072 | STANDARD |
| Beckett Sennecke: 2+ points | 0.349 | 0.255 | 26/75 | +0.076 | STANDARD |
| Alex Killorn: 1+ assists | 0.329 | 0.240 | 25/77 | +0.066 | STANDARD |
| Beckett Sennecke: 1+ goals | 0.413 | 0.325 | 33/68 | +0.067 | STANDARD |

**PIT @ SJS** · priced 183/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.19, exp saves 24.23 (sd 6.76), pull risk 0.07
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.94, exp saves 23.38 (sd 6.49), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alexander Wennberg: 1+ assists | 0.229 | 0.350 | 37/67 | +0.085 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.243 | 0.355 | 37/66 | +0.081 | STANDARD |
| Ivar Stenberg: 1+ points | 0.402 | 0.505 | 51/50 | +0.080 | STANDARD |
| Alexander Wennberg: 1+ points | 0.368 | 0.470 | 49/55 | +0.065 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.449 | 0.550 | 56/46 | +0.074 | STANDARD |
| Erik Karlsson: 1+ assists | 0.439 | 0.535 | 54/47 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
