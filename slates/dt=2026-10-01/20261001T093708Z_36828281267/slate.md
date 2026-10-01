# NHL slate 2026-10-01 — RESEARCH_ONLY

generated 2026-10-01T09:37:08Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 8 · simulated (not started): 8 · markets on board: 2424 · contracts joined: 408 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 208, 'OK': 115, 'NO_EDGE': 85}
families: {'period_winner': 72, 'period_spread': 48, 'period_total': 72, 'game_early_goal': 8, 'game_winner': 16, 'game_overtime': 8, 'game_spread': 32, 'team_total': 80, 'game_total': 72}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 2026-10-01T23:00:00Z | T-12h | 0.537 | 0.463 | 0.180 | 5.69 | 2.97 | 2.72 | 51 (25/26) | PROJECTED/PROJECTED |
| TBL @ NYR | 2026-10-01T23:00:00Z | T-12h | 0.502 | 0.498 | 0.190 | 5.72 | 2.87 | 2.85 | 51 (25/26) | PROJECTED/PROJECTED |
| BUF @ CBJ | 2026-10-01T23:00:00Z | T-12h | 0.515 | 0.485 | 0.177 | 5.95 | 3.02 | 2.93 | 51 (25/26) | PROJECTED/PROBABLE |
| MIN @ NSH | 2026-10-02T00:00:00Z | T-12h | 0.472 | 0.528 | 0.169 | 6.51 | 3.16 | 3.36 | 51 (25/26) | PROJECTED/PROJECTED |
| SEA @ CGY | 2026-10-02T01:00:00Z | T-12h | 0.522 | 0.478 | 0.177 | 6.10 | 3.12 | 2.98 | 51 (25/26) | CONFIRMED/PROJECTED |
| CHI @ UTA | 2026-10-02T01:30:00Z | T-12h | 0.626 | 0.374 | 0.168 | 6.13 | 3.47 | 2.67 | 51 (25/26) | PROJECTED/PROJECTED |
| EDM @ VAN | 2026-10-02T02:00:00Z | T-12h | 0.423 | 0.577 | 0.168 | 6.65 | 3.08 | 3.58 | 51 (25/26) | PROJECTED/PROJECTED |
| FLA @ SJS | 2026-10-02T02:00:00Z | T-12h | 0.526 | 0.474 | 0.173 | 6.52 | 3.35 | 3.17 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT01FLASJ-FLA | game_winner | 0.474 | 0.575 | 0.555 | 58 | 43 | no | +0.079 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3 | game_spread | 0.233 | 0.330 | 0.309 | 34 | 68 | no | +0.072 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM2 | game_spread | 0.362 | 0.455 | 0.436 | 46 | 55 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA2 | game_spread | 0.263 | 0.355 | 0.336 | 36 | 65 | no | +0.071 | OK |
| KXNHLGAME-26OCT01FLASJ-SJ | game_winner | 0.526 | 0.435 | 0.453 | 44 | 57 | yes | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT01PHINJ-NJ4 | team_total | 0.354 | 0.445 | 0.426 | 45 | 56 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA3 | game_spread | 0.159 | 0.245 | 0.226 | 25 | 76 | no | +0.068 | OK |
| KXNHLGAME-26OCT01EDMVAN-EDM | game_winner | 0.577 | 0.665 | 0.648 | 67 | 34 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB4 | team_total | 0.332 | 0.425 | 0.406 | 44 | 59 | no | +0.062 | OK |
| KXNHLGAME-26OCT01EDMVAN-VAN | game_winner | 0.423 | 0.345 | 0.360 | 35 | 66 | yes | +0.057 | OK |
| KXNHLGAME-26OCT01TBNYR-TB | game_winner | 0.498 | 0.575 | 0.560 | 58 | 43 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB3 | team_total | 0.553 | 0.635 | 0.619 | 65 | 38 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ2 | game_spread | 0.313 | 0.240 | 0.254 | 25 | 77 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT01PHINJ-NJ2 | game_spread | 0.308 | 0.375 | 0.361 | 38 | 63 | no | +0.046 | OK |
| KXNHLGAME-26OCT01PHINJ-NJ | game_winner | 0.537 | 0.605 | 0.592 | 61 | 40 | no | +0.046 | OK |
| KXNHLGAME-26OCT01PHINJ-PHI | game_winner | 0.463 | 0.395 | 0.408 | 40 | 61 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT01PHINJ-6 | game_total | 0.477 | 0.545 | 0.531 | 55 | 46 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3 | team_total | 0.652 | 0.575 | 0.591 | 59 | 44 | yes | +0.045 | OK |
| KXNHLGAME-26OCT01TBNYR-NYR | game_winner | 0.502 | 0.435 | 0.448 | 44 | 57 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT01TBNYR-4 | game_total | 0.807 | 0.865 | 0.855 | 87 | 14 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT01TBNYR-6 | game_total | 0.478 | 0.550 | 0.536 | 56 | 46 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT01TBNYR-7 | game_total | 0.369 | 0.435 | 0.422 | 44 | 57 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB2 | game_spread | 0.271 | 0.335 | 0.322 | 34 | 67 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ4 | team_total | 0.439 | 0.365 | 0.379 | 38 | 65 | yes | +0.043 | OK |
| KXNHLSPREAD-26OCT01PHINJ-NJ3 | game_spread | 0.185 | 0.250 | 0.236 | 26 | 76 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT01PHINJ-NJ3 | team_total | 0.575 | 0.645 | 0.631 | 66 | 37 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT01PHINJ-7 | game_total | 0.364 | 0.425 | 0.413 | 43 | 58 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT01TBNYR-5 | game_total | 0.709 | 0.770 | 0.759 | 78 | 24 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT01PHINJ-NJ5 | team_total | 0.182 | 0.240 | 0.227 | 25 | 77 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB3 | game_spread | 0.153 | 0.205 | 0.194 | 21 | 80 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB5 | team_total | 0.163 | 0.225 | 0.211 | 24 | 79 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ5 | team_total | 0.255 | 0.195 | 0.206 | 21 | 82 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT01PHINJ-5 | game_total | 0.704 | 0.755 | 0.745 | 76 | 25 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT01TBNYR-8 | game_total | 0.195 | 0.250 | 0.238 | 26 | 76 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH5 | team_total | 0.223 | 0.170 | 0.180 | 18 | 84 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT01PHINJ-4 | game_total | 0.799 | 0.850 | 0.841 | 86 | 16 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT01MINNSH-8 | game_total | 0.304 | 0.250 | 0.260 | 26 | 76 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 | team_total | 0.402 | 0.460 | 0.448 | 47 | 55 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 | team_total | 0.493 | 0.555 | 0.543 | 57 | 46 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN2 | game_spread | 0.230 | 0.180 | 0.189 | 19 | 83 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN3 | team_total | 0.597 | 0.535 | 0.547 | 55 | 48 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB2 | team_total | 0.771 | 0.825 | 0.815 | 84 | 19 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN3 | game_spread | 0.134 | 0.090 | 0.098 | 10 | 92 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-5 | game_total | 0.740 | 0.785 | 0.777 | 79 | 22 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB6 | team_total | 0.066 | 0.110 | 0.100 | 12 | 90 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM5 | team_total | 0.297 | 0.350 | 0.339 | 36 | 66 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ3 | game_spread | 0.196 | 0.155 | 0.163 | 16 | 85 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-7 | game_total | 0.406 | 0.460 | 0.449 | 47 | 55 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA3 | game_spread | 0.259 | 0.305 | 0.295 | 31 | 70 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH4 | team_total | 0.402 | 0.345 | 0.356 | 36 | 67 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN4 | team_total | 0.380 | 0.325 | 0.336 | 34 | 69 | yes | +0.025 | OK |
| KXNHLGAME-26OCT01MINNSH-MIN | game_winner | 0.528 | 0.575 | 0.566 | 58 | 43 | no | +0.024 | OK |
| KXNHLGAME-26OCT01MINNSH-NSH | game_winner | 0.472 | 0.425 | 0.434 | 43 | 58 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN5 | team_total | 0.204 | 0.155 | 0.164 | 17 | 86 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT01MINNSH-6 | game_total | 0.609 | 0.565 | 0.574 | 57 | 44 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT01MINNSH-9 | game_total | 0.221 | 0.180 | 0.188 | 19 | 83 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT01MINNSH-7 | game_total | 0.498 | 0.450 | 0.459 | 46 | 56 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT01TBNYR-NYR2 | game_spread | 0.273 | 0.235 | 0.242 | 24 | 77 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF4 | team_total | 0.344 | 0.395 | 0.384 | 41 | 62 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN6 | team_total | 0.094 | 0.060 | 0.066 | 7 | 95 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT01TBNYR-9 | game_total | 0.132 | 0.170 | 0.162 | 18 | 84 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ2 | team_total | 0.840 | 0.795 | 0.805 | 81 | 22 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF3 | team_total | 0.565 | 0.610 | 0.601 | 62 | 40 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA3 | team_total | 0.616 | 0.670 | 0.660 | 69 | 35 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA5 | team_total | 0.219 | 0.265 | 0.255 | 28 | 75 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT01PHINJ-8 | game_total | 0.190 | 0.230 | 0.222 | 24 | 78 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH3 | team_total | 0.614 | 0.565 | 0.575 | 58 | 45 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ6 | team_total | 0.122 | 0.080 | 0.087 | 10 | 94 | yes | +0.016 | OK |
| KXNHLSPREAD-26OCT01MINNSH-NSH2 | game_spread | 0.268 | 0.235 | 0.241 | 24 | 77 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT01MINNSH-10 | game_total | 0.111 | 0.075 | 0.081 | 9 | 94 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-6 | game_total | 0.518 | 0.565 | 0.556 | 58 | 45 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF5 | team_total | 0.175 | 0.210 | 0.203 | 22 | 80 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01PHINJ-NJ6 | team_total | 0.081 | 0.110 | 0.103 | 12 | 90 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-8 | game_total | 0.224 | 0.260 | 0.253 | 27 | 75 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA2 | game_spread | 0.400 | 0.435 | 0.428 | 44 | 57 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT01PHINJ-9 | game_total | 0.129 | 0.160 | 0.153 | 17 | 85 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF2 | team_total | 0.787 | 0.820 | 0.814 | 83 | 19 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN2 | team_total | 0.804 | 0.770 | 0.777 | 78 | 24 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT01PHINJ-3 | game_total | 0.945 | 0.965 | 0.962 | 97 | 4 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM6 | team_total | 0.148 | 0.185 | 0.177 | 20 | 83 | no | +0.012 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ NJD | 0.537 | 0.532 | 0.180 | 0.222 | 5.69 | 5.86 | 0.987/0.993 | KXNHLTOTAL-26OCT01PHINJ-5 +0.032 |
| TBL @ NYR | 0.502 | 0.518 | 0.190 | 0.221 | 5.72 | 6.02 | 0.958/0.957 | KXNHLTOTAL-26OCT01TBNYR-7 +0.050 |
| BUF @ CBJ | 0.515 | 0.550 | 0.177 | 0.218 | 5.95 | 6.17 | 0.964/1.000 | KXNHLTEAMTOTAL-26OCT01BUFCBJ-CBJ3 +0.052 |
| MIN @ NSH | 0.472 | 0.485 | 0.169 | 0.221 | 6.51 | 6.52 | 1.000/1.003 | KXNHLSPREAD-26OCT01MINNSH-MIN2 -0.022 |
| SEA @ CGY | 0.522 | 0.512 | 0.177 | 0.219 | 6.10 | 6.11 | 1.005/1.005 | KXNHLSPREAD-26OCT01SEACGY-CGY2 -0.018 |
| CHI @ UTA | 0.626 | 0.653 | 0.168 | 0.207 | 6.13 | 6.50 | 0.992/1.003 | KXNHLTOTAL-26OCT01CHIUTA-7 +0.068 |
| EDM @ VAN | 0.423 | 0.448 | 0.168 | 0.214 | 6.65 | 6.51 | 1.021/0.994 | KXNHLTOTAL-26OCT01EDMVAN-6 -0.034 |
| FLA @ SJS | 0.526 | 0.553 | 0.173 | 0.214 | 6.52 | 6.42 | 1.034/0.998 | KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 -0.029 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- New Jersey over 3.5 goals scored NO @ 56c · p 0.6388 (adj 0.5969) · $6.49 · thesis NJD:SUPPRESSED
- New Jersey wins by over 1.5 goals NO @ 63c · p 0.7051 (adj 0.665) · $6.45 · thesis PHI:WINS
- New Jersey wins NO @ 40c · p 0.4771 (adj 0.4361) · $3.24 · thesis PHI:WINS
- Tampa Bay wins NO @ 43c · p 0.518 (adj 0.4715) · $10.89 · thesis NYR:WINS
- Vancouver wins YES @ 35c · p 0.4448 (adj 0.3949) · $9.46 · thesis VAN:WINS
- Edmonton over 4.5 goals scored NO @ 66c · p 0.7325 (adj 0.6913) · $3.63 · thesis VAN:WINS
- Florida wins by over 2.5 goals NO @ 76c · p 0.8515 (adj 0.8033) · $20.0 · thesis SJS:WINS
- San Jose wins by over 1.5 goals YES @ 25c · p 0.3318 (adj 0.2859) · $4.81 · thesis SJS:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ NJD** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.74, exp saves 21.68 (sd 5.97), pull risk 0.046
- PHI net: Dan Vladar (PROJECTED) exp shots 28.45, exp saves 24.58 (sd 6.61), pull risk 0.056

**TBL @ NYR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (PROJECTED) exp shots 28.0, exp saves 24.19 (sd 6.57), pull risk 0.059
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 24.5, exp saves 21.2 (sd 5.95), pull risk 0.056

**BUF @ CBJ** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 27.66, exp saves 24.19 (sd 6.44), pull risk 0.052
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 28.58, exp saves 24.65 (sd 6.64), pull risk 0.064

**MIN @ NSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 29.81, exp saves 25.56 (sd 6.96), pull risk 0.073
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 25.33 (sd 6.84), pull risk 0.065

**SEA @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.7, exp saves 24.09 (sd 6.42), pull risk 0.052
- SEA net: Joey Daccord (PROJECTED) exp shots 28.94, exp saves 24.96 (sd 6.81), pull risk 0.058

**CHI @ UTA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 24.86, exp saves 21.82 (sd 6.03), pull risk 0.048
- CHI net: Spencer Knight (PROJECTED) exp shots 29.49, exp saves 24.88 (sd 6.97), pull risk 0.088

**EDM @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.37, exp saves 25.99 (sd 7.22), pull risk 0.079
- EDM net: Devon Levi (PROJECTED) exp shots 26.05, exp saves 22.63 (sd 6.3), pull risk 0.059

**FLA @ SJS** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.16, exp saves 23.72 (sd 6.42), pull risk 0.058
- FLA net: Akira Schmid (PROJECTED) exp shots 26.2, exp saves 22.38 (sd 6.43), pull risk 0.075

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
