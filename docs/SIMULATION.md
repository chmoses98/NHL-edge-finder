# Simulation (`nhl-sim-1.0`, `DATA_ONLY_V1`, `nhl-features-1.0`)

> RESEARCH_ONLY. This document says exactly what the simulator does, including what is crude.

## Inputs (`features/build.build_game_inputs`)

From snapshots at or before the cutoff: MoneyPuck team game log (situation `all`), NHL and MoneyPuck goalie season
rows, rosters, goalie observations, schedule.

## Team ratings (`features/ratings.py`)

- `off_xg60`, `def_xg60`: exponentially weighted xGF/60 and xGA/60 (half-life 20 games, previous season discounted
  x0.6, at most 120 games back), shrunk toward the league mean with a 20-game prior.
- `finish`: regressed GF/xGF ratio; `stop`: regressed GA/xGA (team level). Prior weight 60 xG (~20 games).
- League rates from the current season once it has 60+ team-games, else current + previous.

## Expected goals

```
lam_home = league_g60 * (off_home / L) * (def_away / L) * finish_home * goalie_factor_away * 1.045
lam_away = league_g60 * (off_away / L) * (def_home / L) * finish_away * goalie_factor_home / 1.045
```
Back-to-back (played yesterday): own offence x0.965, own goals against x1.025. Neutral site removes home ice.
Ratio clamp 2.5. Goalie factor = regressed GA/xGA from MoneyPuck (fallback NHL SV% with an 800-shot prior); 1.0 is
league average, lower is better.

## Goalies

Status ladder UNKNOWN < PROJECTED < PROBABLE < CONFIRMED with prior confidences 0 / 0.70 / 0.85 / 0.985 that the
named goalie starts. The factor fed to the sim is `w * named + (1 - w) * alternative` (alternative = listed backup
or league average). UNKNOWN uses the league average and is flagged in `input_reasons`.

## Game simulation (`sim/engine.simulate_game`)

1. Ordinary window: 57 minutes, independent Poisson with rates `lam * 57/60`. An optional shared Gamma environment
   multiplier (`env_dispersion`, default 0 = off) exists for over-dispersion research.
2. Late window: 3 minutes. If the margin is 1 or 2, the trailer is assumed to pull the goalie: leader rate x4.0,
   trailer rate x1.8; otherwise ordinary rates.
3. Regulation tie -> overtime. `p_ot_goal = 0.66` decides OT vs shootout. OT winner drawn from
   `0.5 + 0.55 * (ratio - 0.5)`, shootout winner from `0.5 + 0.25 * (ratio - 0.5)`, `ratio = lam_h / (lam_h + lam_a)`.
   The winner's final score is regulation + 1 (official NHL scoring).
4. 20,000 draws per game; seed = sha256(game_id, date, versions). Output arrays: regulation and final scores,
   overtime, shootout. Every contract is priced from these same arrays (`pricing/price.py`), so winner, regulation
   winner, puck lines, totals, team totals, margin buckets, OT/SO and BTTS are mutually coherent.
   `ladder_violations` checks sums and monotone ladders on every slate.

## Known crude assumptions and omissions (V1)

- Special teams are folded into all-situation xG rates; no explicit penalty rate x PP/PK efficiency.
- No score effects outside the late window; plain Poisson under-produces ties (~17% OT vs ~23% observed). A
  Dixon-Coles style tie correction is roadmap item 4.
- The late-window multipliers (4.0 / 1.8) are priors, not estimates; the landing feed flags empty-net goals and
  will calibrate them.
- Goalie quality uses season aggregates (previous + current), not a daily curve; walk-forward uses factor 1.0.
- No injury, line-combination or travel effects in V1 (injuries are archived and shown, not modelled).
- No period-level simulation; period markets are RESEARCH.
- Home ice and back-to-back adjustments are league-wide priors.
- Start-of-season ratings are last season's regressed values; the first weeks lean on the prior.
