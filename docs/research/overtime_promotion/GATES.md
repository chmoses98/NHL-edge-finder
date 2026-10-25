# V2 overtime / regulation-tie projection — gate status (G7–G10), 2026-10-24

RESEARCH_ONLY. Procedures and thresholds are those registered in `PREREGISTRATION_G7_G10.md` (committed 2026-10-24T05:54Z, before any of these measurements). Historical evidence (G1–G6b, J1) is untouched. **Nothing is promoted or activated.**

| gate | status | evidence |
|---|---|---|
| G7 runtime | **PASS** (owner decision 2026-10-25: G7 is inference time per slate, scorecard definition, 300 s; measured ≈ 34 s for 16 games). The registered whole-cycle proxy is kept, unchanged, as a separate operational delivery metric and does **not** pass the 300 s threshold. | below, `OWNER_DECISION_G7.md` |
| G8 reproducibility | **PASS** (all three parts) | below |
| G9 publication contract | **PASS** (four parts, tested) | below |
| G10 live non-inferiority | **IN PROGRESS by design — cannot pass before ≈ late March 2027** | below |

## G7 — runtime
1. *Production evidence, as registered* (whole capture-worker cycles that ran `simulate`, 655 cycles since 2026-09-29, from the history of `STATUS_worker.json`): median 127 s, **p95 1,081 s, max 1,539 s, 17% above 300 s → fails as registered.** Why it is the wrong proxy: the same file shows what else shares those cycles. Cycles that run `simulate` plus only `app_export`/`simulate` (no `context`, `evaluate`, `settle`, `research_export`) have **median 108–119 s, p95 115–132 s, max 133 s** (n = 100); an empty cycle (capture only) takes 95 s. The long cycles are the ones that also run `settle`/`evaluate` (median 823–864 s) or `context`/`research_export` (p95 1,015–1,049 s). So V2 adds about 13 s to a cycle's 95 s baseline; the 300-s breaches are the slow jobs, not the simulator.
2. *Direct, cold-process measurement* (`run_simulate` on the 5-game fixture archive, 20,000 sims, 5 repetitions): shadow off 0.71 s median, shadow on **11.2 s** median (9.2–12.4 s). Everything that depends on the V2 arm (V2 features and sim, then the player shadow and thesis layers that consume it) therefore costs ≈ 10.5 s for 5 games ≈ 2.1 s/game ≈ **34 s for a 16-game slate**, against the registered 150 s limit for the V2 stage and the scorecard's 300 s per slate.
3. *Inputs at the cutoff:* the only input V2 reads beyond V1's, the special-teams snapshot, is cut at the run's instant; a snapshot observed later is invisible (`test_g7_inputs_a_late_team_games_st_snapshot_never_reaches_the_v2_run`). V1/V2 share the goalie/roster/schedule readers, which have their own point-in-time tests.

**Owner call (answered 2026-10-25, see `OWNER_DECISION_G7.md`):** `promotion.MAX_INFERENCE_SECONDS_PER_SLATE` defines G7 as *inference* time per slate (300 s); criterion 1 of my registration used a coarser proxy (whole cycle) that I should not have chosen. I report it as failed-as-registered rather than quietly redefining it; on the scorecard's own definition and on direct measurement G7 passes by a wide margin. If you agree the scorecard definition governs, I will record that as a dated amendment (written *after* this data, and flagged as such).

## G8 — deterministic reproducibility
1. Fresh processes with `PYTHONHASHSEED` 0, 1 and 12345 produce the same sha256 of the V2 game summary: `242dcdfe…b877c` ✓.
2. **Archive replay:** 400 live V2 game blocks (the most recent, 2026-09-30 → 2026-10-24) re-simulated from their archived lambdas, seeds and `n_sims` with the repository parameter file reproduce the archived `p_home_win`, `p_reg_tie`, `p_overtime` **exactly** (0 mismatches) ✓. (A tampered block is detected: unit test.)
3. **Deterministic training:** `fit_live_params` on the pinned history regenerates `data/params/nhl-sim-2.0.json` and `nhl-features-2.0.json` identically (every field except the fit timestamp) ✓.

## G9 — publication contract
`tests/test_overtime_g9.py` + `tests/test_projection_registry.py`, on the real pipeline and the real export:
* At the committed default (V1) the slate's published game documents are **identical** to a run with no V2 at all (and carry no new fields); the V1 `predictions` ledger and contract rows are unchanged.
* With an **approved** switch, the five fields (`p_reg_tie`, `p_overtime`, `p_home_reg_win`, `p_away_reg_win`, `p_shootout`) come from V2 **together**, the only addition is the `overtime_model` provenance block (which keeps the V1 numbers), nothing else in the game moves, `p_reg_tie == p_overtime`, the three regulation/overtime probabilities sum to 1 and P(OT) stays in range. Contract prices, recommendations, markets and the board are unchanged; the app export validates against `edge_finder.app.v1` and `model_game` only gains `overtime_model`.
* A V2 failure, a missing block or a non-finite/out-of-range V2 value publishes **V1's numbers for that game** with `fallback = true` — never a mixture.
* A switch without a complete approval record `{approved_by, approved_at_utc, evidence}` is **ignored** and says why; the committed registry is V1 with no approval (tested), so merging this code promotes nothing.

## G10 — live non-inferiority (registered, running)
Design (see the registration): paired Brier(OT), V2 − V1, from archived pre-drop slate snapshots, games starting from 2026-10-26; **primary look at 1,050 paired settled games** (n sized for 90% power at the historical effect of −0.0022 against the 0.0010 non-inferiority margin; SD of the paired per-game difference is 0.0349); harm looks at 250/500/750 (99% interval); one registered extension at 1,600. At ≈ 7 games a day that is **late March 2027**; a shorter window cannot establish non-inferiority at this margin, and none is proposed. Tooling: `python -m nhl_edge.research.overtime_gates live --archive <data-archive>`; it is tested on synthetic data (pairs, outcome corrections, harm stop, no interim pass, coverage/fallback checks).

## Consequence for the promotion recommendation
With G7–G9 satisfied, **the only open gate is G10, and it is open by construction until the registered sample exists.** The exact reversible change is written out in `RECOMMENDATION.md` (one value and one approval record in `data/registry/projection-registry.json`); no pull request that flips it is opened until G10 has passed, and it is never merged or activated without your explicit approval. The loader also refuses an approval record whose fields look like placeholders (`PENDING`, `TODO`, `TBD`).
