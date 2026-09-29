# DATA_ONLY_V2 research upgrade (2026-09-29)

**Authority: RESEARCH_ONLY. DATA_ONLY_V2 is a SHADOW arm.** It never gates a contract, never replaces DATA_ONLY_V1 and
carries no wagering authority. DATA_ONLY_V1 / `nhl-sim-1.1` / `nhl-features-1.0` are frozen as the control: their
code paths, constants and archived predictions are unchanged. A test proves V1's prediction rows are identical with
the shadow on or off.

New versions: `DATA_ONLY_V2`, `nhl-sim-2.0`, `nhl-features-2.0`. Live parameters: `data/params/nhl-sim-2.0.json`,
`data/params/nhl-features-2.0.json`. Evidence: `WALK_FORWARD_V2.md` (+ JSON / per-game CSV) and `MARKET_BENCHMARK.md`.

## Data added

| data | source | where | notes |
|---|---|---|---|
| shot-level MoneyPuck rows 2021-22 .. 2025-26 (613k rows, 5 seasons, 8.7 MB) | `peter-tanner.com/moneypuck/downloads/shots_{yr}.zip` via `research-data.yml` | `data/history/moneypuck/shots_*.parquet`, `data/history/SHOTS_MANIFEST.json` | slim columns only; game clock, score, manpower, empty-net flags, goalie id, xG |
| historical Kalshi NHL markets + candles | Kalshi historical + live hosts via `research-data.yml` | `data/history/kalshi/` | see MARKET_BENCHMARK.md |
| live situation rows (5on5/5on4/4on5/all) | the context refresh's existing MoneyPuck download | archive kind `context/team_games_st` (new, deduplicated by content hash) | `context/team_games` unchanged |

## 1. OT / regulation-tie calibration (nhl-sim-2.0)

**Why V1 under-predicts ties.** V1 draws regulation as independent Poissons with a fixed rate, plus a 3-minute pull
window with prior multipliers. Play-by-play shows scoring is strongly state dependent (table below; 2021-22 .. 2025-26
regular season, 39,431 regulation goals, 6,559 games): tied teams slow down through the third period, the second period
runs hot (long change), trailing teams press and the pull turns the last minutes into an empty-net shooting gallery for
the leader. The tied-state slowdown is the dominant tie mechanism; the empty-net effect *reduces* ties (a two-goal lead
is harder to erase), so both must be modelled together.

**Estimated multiplier on a team's scoring rate** (live table, fitted on 2021-2025; columns = the team's own score
differential before the goal, rows = regulation time bucket; 1.00 = the team's game rate):

| bucket | -3 | -2 | -1 | 0 | +1 | +2 | +3 |
|---|---:|---:|---:|---:|---:|---:|---:|
| P1 (0-20) | 0.95 | 0.92 | 0.94 | 0.87 | 0.87 | 0.83 | 0.95 |
| P2 (20-40) | 1.04 | 1.10 | 1.10 | 1.04 | 1.04 | 0.95 | 0.95 |
| P3 40-50 | 1.00 | 1.02 | 0.97 | 0.87 | 0.89 | 0.89 | 0.84 |
| P3 50-55 | 0.97 | 1.05 | 0.98 | 0.87 | 0.79 | 0.80 | 0.94 |
| P3 55-57 | 1.12 | 1.10 | 0.94 | 0.78 | 0.75 | 1.59 | 1.20 |
| P3 57-58 | 0.95 | 1.50 | 1.09 | 0.77 | 1.14 | 3.22 | 1.15 |
| P3 58-59 | 0.93 | 1.54 | 1.32 | 0.71 | 3.56 | 4.12 | 1.05 |
| P3 59-60 | 0.82 | 1.52 | 2.32 | 0.75 | 5.96 | 4.95 | 0.80 |

Estimator (`nhl_edge.research.state_hazards`): each game's regulation timeline is cut at every goal; each team accrues
exposure minutes and goals in (bucket, own differential) cells; `goals ~ Poisson(lam_i * m_c * exposure / 60)` with
`lam_i` an exogenous strength control (league rate x team season GF rate x opponent season GA rate x venue); closed-form
MLE per cell shrunk toward 1 with 25 pseudo-goals; normalised to exposure-weighted mean 1. **Rejected first attempt:** a
team-game fixed effect (conditional multinomial). Conditioning on a team's own total makes its goals mechanically precede
its leading exposure and produced a spurious x2-x3 "trailing teams score more" table (e.g. P1 trailing-by-3 x1.91,
leading-by-3 x0.19); a unit test now checks that a state-free Poisson process yields a flat table.

**Simulator** (`nhl_edge.sim.engine_v2`): 120 half-minute steps; each step draws both teams' goals with
`lam * scale * m[bucket, own diff]`; goals accumulate per period, so `P1 + P2 + P3 == regulation` on every draw
(hypothesis-tested). No separate pull window; empty-net goals live in the table. OT: `p(decided before SO)` estimated
from results (0.68 over 2021-2025; V1 used a 0.66 prior), OT/SO winner as V1. `scale` (1.008) makes a league-average
matchup's mean regulation goals equal its input lambda. Optional shared gamma environment: selected OFF on both
validation seasons (total-goals log-likelihood fell monotonically with dispersion 0 -> 0.05).

**Alternatives tested (walk-forward, identical games):** V1 independent Poisson + prior pull window (control); shared
gamma environment (bivariate over-dispersion, rejected on validation: worse total-goals likelihood and no tie gain);
state hazards (selected). A Dixon-Coles-style tie inflation was not adopted: it would repair P(OT) by fiat without
explaining periods, margins or empty-net goals, which the state model gets from the same mechanism.

| arm | predicted P(OT) | observed | OT Brier | OT log loss | OT ECE | ML Brier | ML log loss |
|---|---:|---:|---:|---:|---:|---:|---:|
| V1 (sim 1.1) | 0.174 | 0.2275 | 0.1786 | 0.5456 | 0.053 | 0.2419 | 0.6766 |
| SIM2 (V1 lambdas, sim 2.0) | 0.212 | 0.2275 | 0.1761 | 0.5374 | 0.015 | 0.2418 | 0.6763 |

Tradeoffs: moneyline unchanged, 3-way regulation-winner log loss improves (0.6712 -> 0.6698), total bias rises from
+0.04 to +0.08 (still small; exact-total likelihood -2.1813 -> -2.1822), P2 over-predicted by 0.09 goals and P3 ties
over-predicted (0.287 vs 0.261) in 2024-26: the table was trained on seasons whose period shape differs slightly.

## 2. Goalie true talent + workload (nhl-features-2.0)

Goalie game logs from the shot rows (xG faced on unblocked, non-empty-net attempts vs goals allowed; the starter = the
goalie facing his team's first shot against). Talent at date D uses appearances strictly before D, exponentially weighted
(half-life 120 appearances, so prior seasons carry in without a hard reset) and shrunk toward league average with a prior
of K expected goals, K chosen on the previous season by out-of-sample goalie-game Poisson likelihood: K = 1500 (for
2024-25), 300 (for 2025-26), 300 (live 2026-27). V1 effectively used K = 60 on one prior season. The gain over
"every goalie is average" is tiny: goalie talent beyond xG is weakly identifiable, and heavy shrinkage is the honest
answer. Back-to-back starts: GA / talent-adjusted expected = 0.98 (95 starts, 2022-23) and 1.03 (189 starts, through
2024-25), shrunk to x0.99 / x1.02 (live 1.018): no material fatigue effect found. Rest days are recorded, not modelled.

Starter uncertainty: V1's status ladder is kept (CONFIRMED 0.985, PROBABLE 0.85, PROJECTED 0.70, UNKNOWN 0) so PROJECTED
is never treated as CONFIRMED. The alternative-goalie distribution is improved: alternatives come from the observation,
else the **current roster** (`context/rosters`), weighted by each goalie's recent start share (V1: a plain average; the
first live dry run showed last season's club is wrong after trades). Prospective measurement of PROJECTED -> CONFIRMED
accuracy and of probability movement after confirmation is possible from the archive (every observation is append-only
with its timestamp) but has no data until tonight's games settle.

Historical evaluation is **retrospective oracle-style** (the actual starter; historical confirmation timing is not
available), never a pregame backtest:

| arm (oracle starters) | ML Brier | ML log loss | goalie-sensitive quartile Brier |
|---|---:|---:|---:|
| V1 lambdas + V1-style goalie factor | 0.2420 | 0.6767 | 0.2493 |
| V1 (goalie 1.0) | 0.2419 | 0.6766 | 0.2472 |
| SIM2_ST + V2 true talent | 0.2415 | 0.6758 | 0.2470 |

The V1-style factor (weakly shrunk last-season GA/xGA) makes forecasts slightly worse even with the right starter; V2's
heavily shrunk talent helps slightly.

## 3. Explicit special teams (nhl-features-2.0)

`nhl_edge.features.special_teams`: EV (5on5) offence/defence per 60, PP (own 5on4) xGF/60, PK (own 4on5) xGA/60, PP
minutes drawn and PK minutes taken per game, each exponentially weighted like V1 and shrunk toward league mean (PP/PK
rates with a 180-minute prior, about 40 games of power-play time). Expected goals = EV + PP (A's PP vs B's PK, minutes =
A draws x B takes) + SH (league rate) + other (4v4, 3v3, 5v3, empty net; V1 all-situation ratings), then V1's
finishing, goalie, home and rest multipliers. Minutes partition the game and the sum is normalised so a league-average
matchup reproduces V1's league rate exactly (tested: no double counting).

Held out: moneyline Brier 0.2418 -> 0.2417, total exact-likelihood -2.1822 -> -2.1806, O5.5 Brier 0.2470 -> 0.2467,
team-total Briers equal or slightly better; in the quarter of games where special teams move the lambda ratio most,
0.2420 -> 0.2413. A small but consistent improvement, so it stays in the primary V2 arm.

## 4. Empty net / score state

Sample 2021-26: 2,323 empty-net goals (0.35 per game): 926 in the final minute, 779 in 1-2 minutes remaining, 361 in
2-3, 161 in 3-4, 96 earlier. 982 extra-attacker goals by a team with its own net empty. Pulls detected in 4,147 games
(first shot with that team's net empty: median 2.05 minutes remaining, 10%-90% 5.6 .. 0.7). Estimated late multipliers
replace V1's priors: leader by one x3.6 (58-59) and x6.0 (59-60); trailer by one x1.3 and x2.3; tied teams x0.71-0.78
in the last five minutes. Score effects exist through the whole third period (tied x0.87, leading x0.79-0.89).

## 5. Period model

Regulation goals by period 2021-26: P1 1.77, P2 2.09, P3 2.15 per game (not thirds). `SimV2Result` exposes per-period
goals; `pricing/price_v2.py` prices `period_winner` (incl. the TIE market), `period_spread` and `period_total` from the
same draw. Held-out period scoring (2024-26): P1 tie Brier 0.2257 (p 0.342 vs 0.344 observed), P2 home-win Brier 0.2318,
P3 over-1.5 Brier 0.2278. **Support:** the period families stay `RESEARCH` in the ontology; V2 prices them in the shadow
block tagged `PARTIAL_RULES_VERIFIED_NO_SETTLEMENT`. Settlement code for period results does not exist yet, so they cannot be
SUPPORTED regardless of the rule text.

## Overall V1 vs V2 (identical 2,624 games)

**Improves on OT / regulation markets, neutral elsewhere.** Primary V2 arm = special teams + goalie true talent +
sim 2.0. The large, clean gain is regulation-tie calibration; moneyline, totals, puck line and team totals are within
noise of V1. No arm was tuned on the test seasons.

## Live integration

`nhl simulate` builds V1 exactly as before, then (same snapshot, no extra network) runs the V2 shadow, archives it to
`predictions_v2` and appends a V1 / V2 / market block to `slate.json`, `packet.json` (`v2_shadow`) and `slate.md`.
`NHL_EDGE_V2_SHADOW=0` disables it. The worker picks up new `main` code only when a new generation starts; V2 rows
start at the first timestamp V2 actually ran and are never backdated into earlier opening-night snapshots.
