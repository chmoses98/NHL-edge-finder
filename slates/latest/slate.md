# NHL slate 2026-11-11 — RESEARCH_ONLY

generated 2026-11-11T23:45:46Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 6 · markets on board: 3395 · contracts joined: 1395 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 1245, 'OK': 68, 'NO_EDGE': 82}
families: {'period_winner': 54, 'period_spread': 36, 'period_total': 54, 'player_assists': 205, 'game_early_goal': 6, 'first_goal': 215, 'game_winner': 12, 'player_goals': 370, 'game_overtime': 6, 'player_points': 285, 'goalie_saves': 14, 'game_spread': 24, 'team_total': 60, 'game_total': 54}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ BUF | 2026-11-12T00:00:00Z | T-10m | 0.470 | 0.530 | 0.184 | 6.09 | 2.95 | 3.14 | 220 (25/195) | CONFIRMED/CONFIRMED |
| NYR @ CGY | 2026-11-12T00:30:00Z | T-30m | 0.551 | 0.449 | 0.182 | 5.85 | 3.07 | 2.77 | 236 (25/211) | CONFIRMED/PROBABLE |
| PHI @ EDM | 2026-11-12T02:00:00Z | T-90m | 0.627 | 0.373 | 0.169 | 6.27 | 3.54 | 2.73 | 224 (25/199) | CONFIRMED/PROBABLE |
| UTA @ VGK | 2026-11-12T02:30:00Z | T-90m | 0.555 | 0.445 | 0.170 | 6.46 | 3.41 | 3.05 | 240 (25/215) | CONFIRMED/PROBABLE |
| NSH @ ANA | 2026-11-12T03:00:00Z | T-3h | 0.580 | 0.420 | 0.169 | 6.72 | 3.63 | 3.09 | 240 (25/215) | CONFIRMED/PROJECTED |
| PIT @ SJS | 2026-11-12T03:00:00Z | T-3h | 0.469 | 0.531 | 0.168 | 6.83 | 3.30 | 3.53 | 235 (25/210) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV11NYRCGY-NYR | game_winner | 0.449 | 0.575 | 0.550 | 58 | 43 | no | +0.104 | OK |
| KXNHLGAME-26NOV11NYRCGY-CGY | game_winner | 0.551 | 0.435 | 0.458 | 44 | 57 | yes | +0.094 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-NYR4 | team_total | 0.311 | 0.430 | 0.405 | 44 | 58 | no | +0.092 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-NYR3 | team_total | 0.529 | 0.635 | 0.614 | 64 | 37 | no | +0.085 | OK |
| KXNHLSPREAD-26NOV11NYRCGY-NYR2 | game_spread | 0.235 | 0.340 | 0.317 | 35 | 67 | no | +0.080 | OK |
| KXNHLSPREAD-26NOV11NYRCGY-NYR3 | game_spread | 0.129 | 0.225 | 0.203 | 23 | 78 | no | +0.079 | OK |
| KXNHLSPREAD-26NOV11NYRCGY-CGY2 | game_spread | 0.319 | 0.225 | 0.242 | 23 | 78 | yes | +0.077 | OK |
| KXNHLTOTAL-26NOV11TBBUF-6 | game_total | 0.540 | 0.635 | 0.617 | 64 | 37 | no | +0.074 | OK |
| KXNHLTOTAL-26NOV11TBBUF-7 | game_total | 0.429 | 0.525 | 0.506 | 53 | 48 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-NYR5 | team_total | 0.153 | 0.230 | 0.213 | 24 | 78 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-NYR2 | team_total | 0.758 | 0.835 | 0.821 | 85 | 18 | no | +0.051 | OK |
| KXNHLTOTAL-26NOV11TBBUF-5 | game_total | 0.759 | 0.830 | 0.817 | 84 | 18 | no | +0.051 | OK |
| KXNHLTOTAL-26NOV11TBBUF-8 | game_total | 0.244 | 0.315 | 0.300 | 32 | 69 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY3 | team_total | 0.608 | 0.535 | 0.550 | 54 | 47 | yes | +0.051 | OK |
| KXNHLTOTAL-26NOV11TBBUF-4 | game_total | 0.845 | 0.905 | 0.895 | 91 | 10 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26NOV11TBBUF-TB4 | team_total | 0.397 | 0.470 | 0.455 | 48 | 54 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY4 | team_total | 0.379 | 0.315 | 0.327 | 32 | 69 | yes | +0.044 | OK |
| KXNHLSPREAD-26NOV11NYRCGY-CGY3 | game_spread | 0.191 | 0.135 | 0.145 | 14 | 87 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV11TBBUF-TB3 | team_total | 0.616 | 0.675 | 0.663 | 68 | 33 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV11TBBUF-TB2 | team_total | 0.817 | 0.875 | 0.865 | 89 | 14 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV11TBBUF-TB5 | team_total | 0.213 | 0.270 | 0.258 | 28 | 74 | no | +0.034 | OK |
| KXNHLTOTAL-26NOV11TBBUF-9 | game_total | 0.170 | 0.220 | 0.209 | 23 | 79 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV11TBBUF-BUF5 | team_total | 0.180 | 0.225 | 0.215 | 23 | 78 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY5 | team_total | 0.197 | 0.145 | 0.154 | 16 | 87 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV11PITSJ-PIT3 | game_spread | 0.203 | 0.245 | 0.236 | 25 | 76 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV11TBBUF-BUF4 | team_total | 0.350 | 0.395 | 0.386 | 40 | 61 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-NYR6 | team_total | 0.061 | 0.095 | 0.087 | 10 | 91 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY6 | team_total | 0.086 | 0.055 | 0.060 | 6 | 95 | yes | +0.022 | OK |
| KXNHLGAME-26NOV11PITSJ-SJ | game_winner | 0.469 | 0.425 | 0.434 | 43 | 58 | yes | +0.022 | OK |
| KXNHLGAME-26NOV11PITSJ-PIT | game_winner | 0.531 | 0.575 | 0.566 | 58 | 43 | no | +0.022 | OK |
| KXNHLSPREAD-26NOV11PITSJ-PIT2 | game_spread | 0.324 | 0.365 | 0.357 | 37 | 64 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV11NYRCGY-5 | game_total | 0.728 | 0.765 | 0.758 | 77 | 24 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV11TBBUF-TB6 | team_total | 0.094 | 0.125 | 0.118 | 13 | 88 | no | +0.018 | OK |
| KXNHLTOTAL-26NOV11TBBUF-10 | game_total | 0.076 | 0.105 | 0.098 | 11 | 90 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV11NYRCGY-CGY2 | team_total | 0.810 | 0.770 | 0.778 | 78 | 24 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV11PHIEDM-EDM2 | team_total | 0.866 | 0.900 | 0.894 | 91 | 11 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV11PHIEDM-EDM4 | team_total | 0.487 | 0.530 | 0.522 | 54 | 48 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV11NSHANA-5 | game_total | 0.828 | 0.855 | 0.850 | 86 | 15 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV11NYRCGY-6 | game_total | 0.500 | 0.535 | 0.528 | 54 | 47 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV11TBBUF-BUF2 | team_total | 0.786 | 0.815 | 0.810 | 82 | 19 | no | +0.013 | OK |
| KXNHLSPREAD-26NOV11TBBUF-TB3 | game_spread | 0.186 | 0.215 | 0.209 | 22 | 79 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV11PHIEDM-EDM3 | game_spread | 0.264 | 0.295 | 0.289 | 30 | 71 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV11TBBUF-BUF3 | team_total | 0.572 | 0.605 | 0.598 | 61 | 40 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV11NYRCGY-4 | game_total | 0.820 | 0.850 | 0.844 | 86 | 16 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ6 | team_total | 0.117 | 0.095 | 0.099 | 10 | 91 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV11NYRCGY-7 | game_total | 0.393 | 0.425 | 0.419 | 43 | 58 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT2 | team_total | 0.863 | 0.885 | 0.881 | 89 | 12 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV11NSHANA-4 | game_total | 0.895 | 0.915 | 0.911 | 92 | 9 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV11UTAVGK-10 | game_total | 0.104 | 0.085 | 0.089 | 9 | 92 | yes | +0.009 | OK |
| KXNHLTOTAL-26NOV11TBBUF-3 | game_total | 0.960 | 0.975 | 0.973 | 98 | 3 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV11NYRCGY-3 | game_total | 0.950 | 0.965 | 0.962 | 97 | 4 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV11PITSJ-5 | game_total | 0.835 | 0.855 | 0.851 | 86 | 15 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ3 | team_total | 0.643 | 0.615 | 0.621 | 62 | 39 | yes | +0.006 | OK |
| KXNHLTOTAL-26NOV11PITSJ-4 | game_total | 0.898 | 0.915 | 0.912 | 92 | 9 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-SJ4 | team_total | 0.433 | 0.405 | 0.411 | 41 | 60 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV11PHIEDM-PHI6 | team_total | 0.059 | 0.045 | 0.048 | 5 | 96 | yes | +0.006 | OK |
| KXNHLSPREAD-26NOV11TBBUF-TB2 | game_spread | 0.309 | 0.335 | 0.330 | 34 | 67 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-NSH2 | team_total | 0.805 | 0.830 | 0.825 | 84 | 18 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV11UTAVGK-8 | game_total | 0.298 | 0.275 | 0.280 | 28 | 73 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4 | team_total | 0.479 | 0.505 | 0.500 | 51 | 50 | no | +0.004 | OK |
| KXNHLGAME-26NOV11NSHANA-ANA | game_winner | 0.580 | 0.555 | 0.560 | 56 | 45 | yes | +0.003 | OK |
| KXNHLGAME-26NOV11TBBUF-BUF | game_winner | 0.470 | 0.445 | 0.450 | 45 | 56 | yes | +0.003 | OK |
| KXNHLGAME-26NOV11TBBUF-TB | game_winner | 0.530 | 0.555 | 0.550 | 56 | 45 | no | +0.003 | OK |
| KXNHLSPREAD-26NOV11UTAVGK-UTA2 | game_spread | 0.244 | 0.265 | 0.261 | 27 | 74 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA6 | team_total | 0.161 | 0.140 | 0.144 | 15 | 87 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV11PHIEDM-4 | game_total | 0.861 | 0.875 | 0.872 | 88 | 13 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV11UTAVGK-VGK6 | team_total | 0.128 | 0.110 | 0.113 | 12 | 90 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV11PITSJ-10 | game_total | 0.138 | 0.125 | 0.128 | 13 | 88 | yes | +0.000 | OK |
| KXNHLSPREAD-26NOV11PITSJ-SJ2 | game_spread | 0.263 | 0.245 | 0.248 | 25 | 76 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV11NSHANA-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV11PITSJ-9 | game_total | 0.262 | 0.245 | 0.248 | 25 | 76 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT5 | team_total | 0.286 | 0.310 | 0.305 | 32 | 70 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11NSHANA-ANA4 | team_total | 0.504 | 0.530 | 0.525 | 54 | 48 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV11PHIEDM-5 | game_total | 0.780 | 0.795 | 0.792 | 80 | 21 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV11NYRCGY-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26NOV11NSHANA-NSH3 | game_spread | 0.134 | 0.145 | 0.143 | 15 | 86 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV11NYRCGY-8 | game_total | 0.210 | 0.225 | 0.222 | 23 | 78 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26NOV11UTAVGK-UTA3 | game_spread | 0.144 | 0.155 | 0.153 | 16 | 85 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV11PITSJ-PIT3 | team_total | 0.688 | 0.710 | 0.706 | 72 | 30 |  | -0.003 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ BUF | 0.470 | 0.474 | 0.184 | 0.221 | 6.09 | 6.32 | 1.002/0.946 | KXNHLTOTAL-26NOV11TBBUF-7 +0.043 |
| NYR @ CGY | 0.551 | 0.519 | 0.182 | 0.221 | 5.85 | 6.15 | 0.978/1.004 | KXNHLTEAMTOTAL-26NOV11NYRCGY-NYR3 +0.058 |
| PHI @ EDM | 0.627 | 0.618 | 0.169 | 0.210 | 6.27 | 6.48 | 1.022/0.994 | KXNHLTOTAL-26NOV11PHIEDM-7 +0.036 |
| UTA @ VGK | 0.555 | 0.569 | 0.170 | 0.217 | 6.46 | 6.42 | 1.003/0.999 | KXNHLSPREAD-26NOV11UTAVGK-UTA2 -0.019 |
| NSH @ ANA | 0.580 | 0.664 | 0.169 | 0.191 | 6.72 | 6.83 | 0.968/0.994 | KXNHLSPREAD-26NOV11NSHANA-ANA3 +0.091 |
| PIT @ SJS | 0.469 | 0.492 | 0.168 | 0.217 | 6.83 | 6.49 | 1.039/1.012 | KXNHLTOTAL-26NOV11PITSJ-8 -0.054 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 24 recommended · full analysis in card.md / packet.json `thesis_card`

- Yanni Gourde: 1+ goals NO @ 84c · p 0.8875 (adj 0.8744) · $13.61 · thesis TBL:SUPPRESSED
- Ryan McLeod: 1+ assists NO @ 72c · p 0.7978 (adj 0.7539) · $13.61 · thesis BUF:SUPPRESSED
- Tage Thompson: 1+ goals NO @ 63c · p 0.6707 (adj 0.6593) · $5.51 · thesis BUF:SUPPRESSED
- Full Game: Over 5.5 goals scored NO @ 37c · p 0.4286 (adj 0.3968) · $1.03 · thesis GAME:LOW_EVENT
- Aydar Suniev: 1+ goals YES @ 16c · p 0.2122 (adj 0.1979) · $5.47 · thesis CGY:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 8c · p 0.1089 (adj 0.1004) · $2.59 · thesis CGY:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 68c · p 0.7276 (adj 0.7132) · $10.2 · thesis NYR:SUPPRESSED
- Morgan Frost: 1+ goals YES @ 23c · p 0.268 (adj 0.2573) · $3.25 · thesis CGY:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 10c · p 0.1497 (adj 0.136) · $5.04 · thesis PHI:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 16c · p 0.217 (adj 0.2015) · $5.9 · thesis PHI:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 11c · p 0.1456 (adj 0.1355) · $3.39 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 28c · p 0.4108 (adj 0.3193) · $5.32 · thesis EDM:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 4c · p 0.0836 (adj 0.0714) · $3.97 · thesis VGK:OFFENSE_4PLUS
- Ivan Barbashev: 1+ goals YES @ 16c · p 0.2233 (adj 0.2062) · $6.99 · thesis VGK:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 10c · p 0.1511 (adj 0.1358) · $4.98 · thesis UTA:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 17c · p 0.2198 (adj 0.2049) · $4.74 · thesis UTA:OFFENSE_4PLUS
- Beckett Sennecke: 1+ goals YES @ 33c · p 0.4129 (adj 0.3909) · $9.79 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 18c · p 0.2437 (adj 0.2265) · $6.16 · thesis ANA:OFFENSE_4PLUS
- Jackson LaCombe: 1+ goals YES @ 12c · p 0.1706 (adj 0.1567) · $4.47 · thesis ANA:OFFENSE_4PLUS
- Steven Stamkos: 1+ goals NO @ 62c · p 0.6826 (adj 0.6657) · $12.43 · thesis NSH:SUPPRESSED
- Erik Karlsson: 1+ goals NO @ 82c · p 0.8553 (adj 0.8452) · $13.61 · thesis PIT:SUPPRESSED
- Pittsburgh over 3.5 goals scored NO @ 50c · p 0.569 (adj 0.532) · $2.94 · thesis PIT:SUPPRESSED
- Pittsburgh wins by over 1.5 goals NO @ 64c · p 0.7029 (adj 0.6689) · $2.74 · thesis SJS:WINS
- Tyler Toffoli: 1+ assists YES @ 24c · p 0.3038 (adj 0.2644) · $2.25 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TBL @ BUF** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (CONFIRMED) exp shots 27.97, exp saves 24.22 (sd 6.68), pull risk 0.061
- TBL net: Andrei Vasilevskiy (CONFIRMED) exp shots 26.9, exp saves 23.29 (sd 6.42), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.462 | 0.635 | 65/38 | +0.142 | STANDARD |
| Nikita Kucherov: 2+ points | 0.286 | 0.420 | 44/60 | +0.098 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.127 | 0.255 | 28/77 | +0.091 | STANDARD |
| Yanni Gourde: 1+ points | 0.251 | 0.360 | 39/67 | +0.064 | STANDARD |
| John Carlson: 1+ points | 0.386 | 0.495 | 50/51 | +0.086 | STANDARD |
| Nikita Kucherov: 3+ points | 0.089 | 0.180 | 19/83 | +0.071 | STANDARD |

**NYR @ CGY** · priced 184/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 27.6, exp saves 23.93 (sd 6.58), pull risk 0.059
- NYR net: Joonas Korpisalo (PROBABLE) exp shots 28.17, exp saves 24.39 (sd 6.7), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vladislav Gavrikov: 1+ assists | 0.298 | 0.215 | 22/79 | +0.066 | STANDARD |
| J.T. Miller: 1+ assists | 0.351 | 0.430 | 44/58 | +0.052 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.356 | 0.285 | 30/73 | +0.042 | STANDARD |
| Adam Fox: 1+ points | 0.575 | 0.640 | 65/37 | +0.039 | STANDARD |
| Adam Fox: 1+ assists | 0.511 | 0.575 | 58/43 | +0.041 | STANDARD |
| Zach Whitecloud: 1+ points | 0.291 | 0.230 | 25/79 | +0.028 | STANDARD |

**PHI @ EDM** · priced 172/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 24.67, exp saves 21.72 (sd 6.11), pull risk 0.054
- PHI net: Dan Vladar (PROBABLE) exp shots 27.73, exp saves 23.42 (sd 6.72), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ points | 0.434 | 0.575 | 59/44 | +0.109 | STANDARD |
| Connor McDavid: 1+ assists | 0.589 | 0.730 | 74/28 | +0.117 | STANDARD |
| Connor McDavid: 2+ assists | 0.229 | 0.360 | 38/66 | +0.095 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.480 | 0.610 | 62/40 | +0.103 | STANDARD |
| Leon Draisaitl: 2+ points | 0.350 | 0.475 | 49/54 | +0.092 | STANDARD |
| Connor McDavid: 3+ points | 0.188 | 0.290 | 30/72 | +0.078 | STANDARD |

**UTA @ VGK** · priced 184/189 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 26.76, exp saves 23.34 (sd 6.46), pull risk 0.057
- UTA net: Sebastian Cossa (PROBABLE) exp shots 27.43, exp saves 23.42 (sd 6.6), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brayden McNabb: 1+ points | 0.375 | 0.255 | 27/76 | +0.091 | STANDARD |
| Brayden McNabb: 1+ assists | 0.317 | 0.205 | 23/82 | +0.075 | STANDARD |
| Lawson Crouse: 1+ points | 0.437 | 0.330 | 35/69 | +0.071 | STANDARD |
| Mitch Marner: 1+ assists | 0.452 | 0.550 | 57/47 | +0.061 | STANDARD |
| Ivan Barbashev: 1+ points | 0.514 | 0.420 | 43/59 | +0.067 | STANDARD |
| Mitch Marner: 1+ points | 0.579 | 0.670 | 68/34 | +0.065 | STANDARD |

**NSH @ ANA** · priced 188/189 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 26.23, exp saves 23.12 (sd 6.29), pull risk 0.048
- NSH net: Justus Annunen (PROJECTED) exp shots 30.21, exp saves 25.26 (sd 7.41), pull risk 0.108

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Killorn: 1+ points | 0.497 | 0.390 | 40/62 | +0.080 | STANDARD |
| Mavrik Bourque: 1+ points | 0.372 | 0.470 | 48/54 | +0.070 | STANDARD |
| Beckett Sennecke: 2+ points | 0.349 | 0.255 | 26/75 | +0.076 | STANDARD |
| Alex Killorn: 1+ assists | 0.329 | 0.240 | 25/77 | +0.066 | STANDARD |
| Beckett Sennecke: 1+ goals | 0.413 | 0.325 | 33/68 | +0.067 | STANDARD |
| Ryan O'Reilly: 1+ assists | 0.394 | 0.480 | 49/53 | +0.059 | STANDARD |

**PIT @ SJS** · priced 183/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.2, exp saves 24.24 (sd 6.75), pull risk 0.07
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.95, exp saves 23.36 (sd 6.53), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alexander Wennberg: 1+ assists | 0.229 | 0.350 | 37/67 | +0.085 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.243 | 0.355 | 37/66 | +0.081 | STANDARD |
| Ivar Stenberg: 1+ points | 0.402 | 0.505 | 51/50 | +0.080 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.449 | 0.545 | 55/46 | +0.074 | STANDARD |
| Erik Karlsson: 1+ assists | 0.439 | 0.535 | 54/47 | +0.073 | STANDARD |
| Macklin Celebrini: 2+ points | 0.298 | 0.390 | 40/62 | +0.066 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
