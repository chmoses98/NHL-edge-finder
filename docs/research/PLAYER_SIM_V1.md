# PLAYER_SIM_V1: joint player-event simulation (2026-09-30)

**Authority: RESEARCH_ONLY. PLAYER_SIM_V1 and MARKET_ANCHORED_PLAYER_V1 are SHADOW arms.** They never gate a contract,
never change DATA_ONLY_V1 or DATA_ONLY_V2 (tested byte-for-byte), and carry no wagering authority.

Versions: `PLAYER_SIM_V1`, `player-sim-1.0`, `player-features-1.0`. Live parameters: `data/params/player-sim-1.0.json`
(fit on 2021-22 .. 2025-26). Evidence: this file, `docs/research/player_sim_v1/` (walk-forward outputs + `eval.json` +
`allocation_2023.json` + `market_benchmark.json`).

## 1. Why

On opening night (2026-09-29) 834 of the 1,089 contracts joined to the five games (77%) were player-driven (297 goals,
207 points, 155 assists, 165 first-goal, 10 saves) and every one of them was UNSUPPORTED. The manual handicap filled the
gap with hit rates and judgment. This arm replaces that with a chain of hockey events underneath every player number.

## 2. The event chain

```
V2 team state (xG ratings, special teams, goalie true talent)          -- unchanged DATA_ONLY_V2 lambdas
  -> nhl-sim-2.0 draw: WHEN each team scores (half-minute steps, score-state x game-time hazards, OT/SO)
       (the step each goal falls in is recorded; recording draws no random numbers, so V2 is bit-identical)
  -> strength state of each goal
       EN / EA: estimated P(state | time bucket, scoring team's own differential) from official situation codes
       PP / SH: this matchup's special-teams share of the team's goals (penalty minutes drawn/taken x PP/PK quality)
       OT: 3-on-3
  -> scorer    ~ deployment share of the team's time in that state (line, PP unit, PK, empty-net / extra-attacker duty)
                 x shrunk individual xG per 60 in that state (shot creation x shot quality, own xG model)
                 x shrunk finishing (goals / xG)
                 x shrunk on-ice goals-for ratio (does the team score more than expected when he is on the ice?)
                 x this draw's ice-time multiplier (game-to-game TOI noise; small early-exit probability)
  -> primary assist:   unassisted at the league rate for the state, else
                       ~ co-ice share with the scorer (recent shift charts / tonight's lines) x shrunk P(A1 | on ice)
  -> secondary assist: none at the league rate given an A1, else
                       ~ mean co-ice with scorer and A1 x shrunk P(A2 | on ice)   (heavier shrinkage than A1)
  -> goals, A1, A2, assists, points per player per draw  -> every ladder (1+, 2+, 3+ ...) from the same draws
  -> first goal: the earliest simulated goal of the draw (ties inside a half-minute step broken uniformly)
  -> each net: goals against = opponent goals not into an empty net (incl. OT);
               saves ~ NegBin(expected non-goal shots faced x game-script terms); goalie-pull hazard after the k-th goal
```

Invariants checked on every simulated game and property-tested: player goals equal the team's non-shootout goals in
every draw; A2 <= A1 <= goals; nobody holds two roles on one goal; opponents never assist; points = goals + assists;
ladders monotone; saves + goals against = shots faced; empty-net goals never count against a goalie; the shootout
creates no player statistic; fixed seed reproduces every number.

## 3. Data (all free, official unless noted)

| source | what | history | point-in-time use | limits |
|---|---|---|---|---|
| NHL api-web `gamecenter/{id}/boxscore` | official skater line (G, A, PTS, SOG, TOI, PPG, shifts) and goalie line (saves, SA, GA, starter, TOI) | 2021-22 .. now | settlement; history rows dated before the game | none found: 100% of 6,991 games parsed |
| NHL api-web `gamecenter/{id}/play-by-play` | every goal (scorer, A1, A2, situationCode, clock, goalie in net), every attempt (shooter, x/y, type) | same | per-game tables; strength timeline | penalty expiry between events is attributed to the PP until the next event (seconds) |
| NHL stats `shiftcharts?cayenneExp=gameId=` | every shift | same; 57 of 1,398 2024-25 games have none | TOI by strength, on-ice at each goal, co-ice pairs | games without shifts keep official lines but drop out of TOI/co-ice features |
| DailyFaceoff team line-combination pages | EV lines, D pairs, PP1/PP2, PK1/PK2, IR, `sourceName` (e.g. "Warmups (reporter)"), `updatedAt` | **none** (live only, archived from 2026-09-30 as `context/lines`) | tonight's deployment; never used in backtests | HTML `__NEXT_DATA__` shape may drift (parser returns None, arm falls back); jersey numbers may lag trades |
| ESPN injuries (existing kind) | Out / IR | live | removes players from the projected lineup | name matching only |
| Kalshi historical API | settled KXNHLGOAL / PTS / AST / SAVE / FIRSTGOAL markets + hourly candles (2025-26) | 2025-26 | market benchmark only | candle midpoints, not executable depth; ~1% of fetches rate-limited |
| MoneyPuck shots (existing) | shot-level xG | 2021-26 | cross-check of our xG only | historical only |

Consistency on 6,991 games (2021-22 .. 2025-26 + 3 opening-night games): **0** games where primary + secondary assists
differ from the official assists, and 0 where play-by-play goals differ from official goals (per player and per team,
shootout excluded).

## 4. Layers and what the data said

### 4.1 Shot quality (own xG)
Logistic regression on distance, angle, shot type, rebound (<= 3 s), behind-net, strength. Fit on 2021-22 .. 2022-23
(242k unblocked attempts), held-out 2023-24: log loss 0.2204 vs 0.2448 for a constant rate; total xG 8,158 vs 8,105
goals; player-season ixG correlates 0.994 with MoneyPuck's xG.

### 4.2 Player state and ice time
Deployment = the player's share of his team's seconds in each strength state (EV, PP, SH, own-net-empty EA, opponent-
net-empty EN, OT), exponentially weighted with a 6-game half-life (roles change) and shrunk with 0.5 pseudo-games toward
the position mean (validation chose 0.5 over 1.5). Talent rates use a 60-game half-life with prior seasons discounted
x0.75. Tonight's DailyFaceoff slots (f1..f4, d1..d3, pp1/pp2, pk1/pk2) are blended in with 3 pseudo-games (confirmed from
warmups / morning skate) or 1.5 (projected). Expected TOI by state = share x the matchup's expected team minutes; the
per-draw TOI multiplier is lognormal with sd 0.16 (estimated: log TOI around the 10-game mean) plus a 0.35% early-exit
probability (estimated: games under 35% of usual TOI), so the same star plays 17 or 23 minutes in different draws.

### 4.3 Scorer (shot creation x quality x finishing x line)
Scorer weight in state s = share_s x shrunk ixG/60_s (prior 300 EV / 60 PP / 60 SH minutes at the position rate) x shrunk
finishing (goals / xG with a 40-xG prior; finishing persistence is weak: removing it costs 0.005 nats per goal) x
shrunk on-ice goals-for ratio (the team's goals while he is on the ice vs what the team scored per minute in the same
games, 12-goal prior; exponent chosen on validation: 1.0 beat 0 and 0.5). EN goals use empty-net ice share x empty-net
scoring rate; EA goals use extra-attacker share x EA xG rate; OT uses 3-on-3 share x EV rate.

### 4.4 Assists (primary and secondary modelled separately)
Given the scorer: unassisted at the league rate for the state (EV 6.4%, PP 1.2%, SH 20%, EN 19%); otherwise the
primary assist goes to a teammate with weight = the share of the SCORER's state time spent with that teammate (recent
shift co-ice, most recent games heaviest; players new to the team get the share-proportional prior, not zero) x the
teammate's P(A1 | on ice for a teammate's goal) shrunk with 25 opportunities toward the position rate (F EV 0.317, D EV
0.139). Secondary: none at the league rate given an A1 (EV 21%, PP 4.7%); otherwise mean co-ice with scorer and A1 x
P(A2 | on ice) shrunk harder (45 opportunities).

### 4.5 Points
Points are never modelled on their own: each draw's goals + A1 + A2 per player, so goal / assist / point ladders and the
team score are one joint distribution.

### 4.6 Goalie saves
Full-game saves ~ NegBin(mu, alpha = 0.017) with log mu = log(expected non-goal shots faced) + 0.014 x regulation margin
of the goalie's team (a team protecting a lead faces more shots) - 0.001 x goals against + 0.016 x OT, the slope on the
expected-shots term fixed at 1 (a free slope fit 1.37 and extrapolated the league-wide drop in shots from 31.6 to 27.7
per team-game badly). Expected shots faced = point-in-time league level x opponent shots-for rate x own shots-against
rate (25-game half-life, 15-game prior) x venue. The starter is replaced after his k-th goal against before 50:00 with
the estimated hazard (k=3: 3%, 4: 9%, 5: 16%, 6: 24%) and keeps the saves of the time he played. Empty-net goals never
count against him; OT goals do; the shootout does not exist for saves.

### 4.7 Correlation
One draw drives everything, so same-game dependence is structural: if the team scores 6, its first line's point
probabilities in that draw are high; a busy night for a goalie is also a night of more goals against; PP goals credit
the PP unit together. Each packet game block carries the Pearson correlation matrix of the YES indicators of up to 40
priced contracts plus team goals and the moneyline, for exposure research (no staking).

## 5. Walk-forward evidence (REALISTIC_PIT; test seasons 2024-25 and 2025-26)

Protocol: every league-level parameter refit on seasons strictly before the test season; player / team features from
games strictly before each game date; team lambdas = DATA_ONLY_V2's own point-in-time walk-forward lambdas for the same
2,624 games; 4,000 draws per game; deployment from recent shift charts only (no lines archive exists historically);
dressed skaters = the actual dressed lineup (the target is P(event | plays)). Hyper-parameters were chosen on the
2023-24 validation season (allocation test, `player_sim_v1/allocation_2023.json`), except the goal co-presence switch
(see 5.3). Baselines: `SEASON_RATE` (Poisson, recent per-game rate), `ROLE_RATE` (Poisson, shrunk per-60 rate x recent
ice time). 47,225 (2024-25) and 47,231 (2025-26) skater-games; 2,624 goalie starts per season.

### 5.1 Goals (validated)

| season | target | PLAYER_SIM_V1 Brier / log loss / ECE | SEASON_RATE | ROLE_RATE | base rate / mean pred |
|---|---|---|---|---|---|
| 2024-25 | 1+ goal | **0.11805** / **0.3867** / 0.0040 | 0.11931 / 0.3919 / 0.0014 | 0.11922 / 0.3917 / 0.0024 | 0.149 / 0.151 |
| 2024-25 | 2+ goals | **0.01561** / **0.0740** / 0.0013 | 0.01568 / 0.0751 | 0.01567 / 0.0750 | 0.016 / 0.018 |
| 2025-26 | 1+ goal | **0.11988** / **0.3919** / 0.0019 | 0.12103 / 0.3969 / 0.0029 | 0.12087 / 0.3963 / 0.0021 | 0.152 / 0.153 |
| 2025-26 | 2+ goals | **0.01663** / **0.0778** / 0.0004 | 0.01667 / 0.0788 | 0.01666 / 0.0787 | 0.017 / 0.018 |

Goals beat both baselines on Brier and log loss in both seasons with small calibration error.

### 5.2 Goalie saves (validated)

| season | mean pred / actual saves | MAE (model / Poisson-shots) | pooled ladder 14+..40+ Brier: model / Poisson-shots | ECE: model / Poisson-shots |
|---|---|---|---|---|
| 2024-25 | 25.10 / 24.68 | 5.30 / 5.40 | **0.1722** / 0.1774 | **0.017** / 0.062 |
| 2025-26 | 24.08 / 24.16 | 5.35 / 5.38 | **0.1712** / 0.1744 | **0.009** / 0.052 |

By threshold (Brier; model / NB without game script / Poisson-shots): 2024-25 20+ 0.1627 / 0.1649 / 0.1727; 24+ 0.2371 /
0.2392 / 0.2470; 28+ 0.2127 / 0.2141 / 0.2157; 32+ 0.1289 / 0.1291 / 0.1289. 2025-26 20+ 0.1771 / 0.1782 / 0.1875; 24+
0.2358 / 0.2357 / 0.2414; 28+ 0.2031 / 0.2015 / 0.2011; 32+ 0.1204 / 0.1195 / 0.1200. The simulated game script helps at
the common thresholds (<= 24) and is neutral-to-slightly-worse at high thresholds (a mild under-dispersion at the top).
The first version (free slope on expected shots, all-seasons league level) was biased ~1.2 saves low; section 4.6.

### 5.3 Assists and points

(see the table below; the goal co-presence decision is documented here)

### 5.4 First goal
First-goal scorer: calibrated (ECE < 0.0001 in both seasons; mean 0.0278 vs 0.0278 observed), Brier skill vs a constant
+1.2%. Team to score first: no skill (Brier skill +0.0001 / +0.0002) — the event ordering is right on average, but it
adds nothing beyond "the better team is slightly likelier".

### 5.5 Ice time
Expected total TOI MAE 1.88 / 1.94 min vs 1.86 / 1.89 for a plain recent-mean: the TOI projection is not better than a
simple mean (the allocation uses shares, which is what matters for scoring). EV MAE 1.81 / 1.85 min, PP MAE 0.76 / 0.79.

### 5.6 Projection quality
PRIOR_HEAVY rows (1,000 / 1,113): predicted 1+ point 0.251 / 0.249 vs 0.210 / 0.226 observed; DEGRADED_ROLE (311 /
255): 0.297 vs 0.232 / 0.231; STANDARD: 0.357 / 0.360 vs 0.346 / 0.351. The flags mark exactly the rows to trust less.
