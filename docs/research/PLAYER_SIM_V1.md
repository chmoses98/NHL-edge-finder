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
