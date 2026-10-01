# NHL slate 2026-10-01 — RESEARCH_ONLY

generated 2026-10-01T08:37:06Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 8 · simulated (not started): 8 · markets on board: 2424 · contracts joined: 408 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 208, 'OK': 65, 'NO_EDGE': 135}
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
| KXNHLGAME-26OCT01FLASJ-SJ | game_winner | 0.526 | 0.435 | 0.453 | 44 | 57 | yes | +0.069 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3 | game_spread | 0.233 | 0.325 | 0.305 | 34 | 69 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM2 | game_spread | 0.362 | 0.450 | 0.432 | 46 | 56 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA2 | game_spread | 0.263 | 0.355 | 0.336 | 37 | 66 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ2 | game_spread | 0.313 | 0.235 | 0.249 | 25 | 78 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA3 | game_spread | 0.159 | 0.240 | 0.222 | 26 | 78 | no | +0.049 | OK |
| KXNHLGAME-26OCT01EDMVAN-EDM | game_winner | 0.577 | 0.655 | 0.640 | 67 | 36 | no | +0.047 | OK |
| KXNHLGAME-26OCT01EDMVAN-VAN | game_winner | 0.423 | 0.350 | 0.364 | 36 | 66 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT01PHINJ-NJ2 | game_spread | 0.308 | 0.380 | 0.365 | 39 | 63 | no | +0.046 | OK |
| KXNHLGAME-26OCT01PHINJ-PHI | game_winner | 0.463 | 0.390 | 0.404 | 40 | 62 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT01PHINJ-6 | game_total | 0.477 | 0.545 | 0.531 | 55 | 46 | no | +0.046 | OK |
| KXNHLGAME-26OCT01TBNYR-NYR | game_winner | 0.502 | 0.435 | 0.448 | 44 | 57 | yes | +0.045 | OK |
| KXNHLGAME-26OCT01TBNYR-TB | game_winner | 0.498 | 0.570 | 0.556 | 58 | 44 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT01TBNYR-4 | game_total | 0.807 | 0.875 | 0.863 | 89 | 14 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB2 | game_spread | 0.271 | 0.340 | 0.326 | 35 | 67 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT01PHINJ-NJ3 | game_spread | 0.185 | 0.255 | 0.240 | 27 | 76 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB4 | team_total | 0.332 | 0.435 | 0.414 | 48 | 61 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT01PHINJ-NJ4 | team_total | 0.354 | 0.435 | 0.418 | 46 | 59 | no | +0.039 | OK |
| KXNHLGAME-26OCT01PHINJ-NJ | game_winner | 0.537 | 0.600 | 0.588 | 61 | 41 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT01TBNYR-TB3 | game_spread | 0.153 | 0.205 | 0.194 | 21 | 80 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT01TBNYR-6 | game_total | 0.478 | 0.545 | 0.532 | 56 | 47 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT01TBNYR-7 | game_total | 0.369 | 0.435 | 0.422 | 45 | 58 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN2 | game_spread | 0.230 | 0.180 | 0.189 | 19 | 83 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT01PHINJ-7 | game_total | 0.364 | 0.420 | 0.409 | 43 | 59 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN3 | game_spread | 0.134 | 0.085 | 0.093 | 10 | 93 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT01TBNYR-5 | game_total | 0.709 | 0.770 | 0.759 | 79 | 25 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3 | team_total | 0.652 | 0.570 | 0.587 | 61 | 47 | yes | +0.025 | OK |
| KXNHLGAME-26OCT01MINNSH-MIN | game_winner | 0.528 | 0.575 | 0.566 | 58 | 43 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT01TBNYR-8 | game_total | 0.195 | 0.245 | 0.234 | 26 | 77 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT01PHINJ-5 | game_total | 0.704 | 0.750 | 0.741 | 76 | 26 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT01MINNSH-9 | game_total | 0.221 | 0.175 | 0.184 | 19 | 84 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT01MINNSH-8 | game_total | 0.304 | 0.255 | 0.264 | 27 | 76 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT01MINNSH-7 | game_total | 0.498 | 0.450 | 0.459 | 46 | 56 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT01TBNYR-NYR2 | game_spread | 0.273 | 0.225 | 0.234 | 24 | 79 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF4 | team_total | 0.344 | 0.405 | 0.392 | 43 | 62 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA3 | game_spread | 0.259 | 0.305 | 0.295 | 32 | 71 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ3 | game_spread | 0.196 | 0.150 | 0.158 | 17 | 87 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-7 | game_total | 0.406 | 0.450 | 0.441 | 46 | 56 | no | +0.016 | OK |
| KXNHLGAME-26OCT01MINNSH-NSH | game_winner | 0.472 | 0.430 | 0.438 | 44 | 58 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT01MINNSH-6 | game_total | 0.609 | 0.565 | 0.574 | 58 | 45 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB3 | team_total | 0.553 | 0.625 | 0.611 | 67 | 42 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT01TBNYR-9 | game_total | 0.132 | 0.170 | 0.162 | 19 | 85 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT01TBNYR-3 | game_total | 0.948 | 0.965 | 0.962 | 97 | 4 | no | +0.009 | OK |
| KXNHLGAME-26OCT01CHIUTA-CHI | game_winner | 0.374 | 0.345 | 0.351 | 35 | 66 | yes | +0.009 | OK |
| KXNHLGAME-26OCT01CHIUTA-UTA | game_winner | 0.626 | 0.660 | 0.653 | 67 | 35 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT01PHINJ-8 | game_total | 0.190 | 0.230 | 0.222 | 25 | 79 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-5 | game_total | 0.740 | 0.775 | 0.768 | 79 | 24 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT01BUFCBJ-BUF3 | game_spread | 0.153 | 0.175 | 0.170 | 18 | 83 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT01MINNSH-5 | game_total | 0.807 | 0.775 | 0.782 | 79 | 24 | yes | +0.005 | OK |
| KXNHLSPREAD-26OCT01MINNSH-NSH2 | game_spread | 0.268 | 0.235 | 0.241 | 25 | 78 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-6 | game_total | 0.518 | 0.560 | 0.552 | 58 | 46 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT01EDMVAN-4 | game_total | 0.890 | 0.925 | 0.919 | 95 | 10 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT01PHINJ-9 | game_total | 0.129 | 0.160 | 0.153 | 18 | 86 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA2 | game_spread | 0.400 | 0.435 | 0.428 | 45 | 58 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT01BUFCBJ-3 | game_total | 0.955 | 0.965 | 0.963 | 97 | 4 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT01TBNYR-10 | game_total | 0.054 | 0.080 | 0.074 | 10 | 94 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT01FLASJ-9 | game_total | 0.224 | 0.195 | 0.201 | 21 | 82 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ5 | team_total | 0.255 | 0.195 | 0.206 | 24 | 85 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT01TBNYR-2 | game_total | 0.977 | 0.985 | 0.984 | 99 | 2 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT01PHINJ-3 | game_total | 0.945 | 0.960 | 0.957 | 97 | 5 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT01EDMVAN-9 | game_total | 0.233 | 0.210 | 0.214 | 22 | 80 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT01FLASJ-3 | game_total | 0.973 | 0.950 | 0.956 | 97 | 7 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT01PHINJ-4 | game_total | 0.799 | 0.840 | 0.832 | 87 | 19 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT01FLASJ-8 | game_total | 0.304 | 0.275 | 0.281 | 29 | 74 | yes | +0.000 | OK |
| KXNHLSPREAD-26OCT01MINNSH-NSH3 | game_spread | 0.159 | 0.135 | 0.140 | 15 | 88 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN3 | team_total | 0.597 | 0.535 | 0.547 | 58 | 51 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT01MINNSH-3 | game_total | 0.971 | 0.965 | 0.966 | 97 | 4 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT01PHINJ-PHI2 | game_spread | 0.241 | 0.220 | 0.224 | 23 | 79 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-2 | game_total | 0.989 | 0.965 | 0.972 | 99 | 6 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT01BUFCBJ-CBJ | game_winner | 0.515 | 0.495 | 0.499 | 50 | 51 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT01TBNYR-NYR3 | game_spread | 0.157 | 0.135 | 0.139 | 15 | 88 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT01FLASJ-2 | game_total | 0.988 | 0.965 | 0.972 | 99 | 6 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT01SEACGY-SEA3 | game_spread | 0.153 | 0.165 | 0.163 | 17 | 84 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB5 | team_total | 0.163 | 0.215 | 0.204 | 26 | 83 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH3 | team_total | 0.614 | 0.560 | 0.571 | 60 | 48 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT01MINNSH-2 | game_total | 0.987 | 0.965 | 0.971 | 99 | 6 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT01MINNSH-MIN3 | game_spread | 0.202 | 0.215 | 0.212 | 22 | 79 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT01SEACGY-3 | game_total | 0.961 | 0.965 | 0.964 | 97 | 4 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT01CHIUTA-CHI2 | game_spread | 0.186 | 0.175 | 0.177 | 18 | 83 |  | -0.004 | NO_EDGE |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- New Jersey wins by over 1.5 goals NO @ 63c · p 0.7051 (adj 0.6625) · $8.06 · thesis PHI:WINS
- Philadelphia wins YES @ 40c · p 0.4771 (adj 0.4335) · $4.03 · thesis PHI:WINS
- New York R wins YES @ 44c · p 0.518 (adj 0.4765) · $8.79 · thesis NYR:WINS
- Vancouver wins YES @ 36c · p 0.4448 (adj 0.3974) · $8.19 · thesis VAN:WINS
- San Jose wins by over 1.5 goals YES @ 25c · p 0.3318 (adj 0.2834) · $4.27 · thesis SJS:WINS_BY_2PLUS
- Florida wins NO @ 43c · p 0.5463 (adj 0.4675) · $2.36 · thesis SJS:WINS
- Florida wins by over 2.5 goals NO @ 78c · p 0.8515 (adj 0.8057) · $12.6 · thesis SJS:WINS

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
