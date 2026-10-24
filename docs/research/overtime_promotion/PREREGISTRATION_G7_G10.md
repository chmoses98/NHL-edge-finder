# V2 overtime / regulation-tie projection — registration of the remaining gates G7–G10

RESEARCH_ONLY. Registered **before any live outcome of the G10 sample exists and before any G7–G9 measurement is run**. Nothing here activates, changes or promotes a model; a promotion needs an explicit human approval of a separate, reversible registry change (§6). The historical evidence (G1–G6b, J1: `v2-joint/`, `v2-joint-retuned/`, `PROMOTION_SCORECARD.md`) is frozen and is not re-opened or re-scored here.

## 1. Candidate and scope
* **Target:** "overtime / regulation tie" — the game-level fields `p_reg_tie`, `p_overtime`, `p_home_reg_win`, `p_away_reg_win`, `p_shootout` published in `slate.games[]` / the app export `model_game`.
* **Incumbent:** `DATA_ONLY_V1` (`nhl-sim-1.1`). **Candidate:** the live `DATA_ONLY_V2` arm (`nhl-sim-2.0` driven by the nhl-features-2.0 lambdas) as it runs in `nhl simulate`. Historical evidence covers `SIM2` (V2 simulator on V1 rates) and `SIM2_ST` (special-teams lambdas); on 2024–25 their overtime Brier is 0.1761 / 0.1759 vs V1 0.1786 (WALK_FORWARD_V2), so the lambda source moves the overtime target by ≈ 0.0002. The live gate G10 therefore tests the arm that would actually be published, not a proxy.
* **Out of scope and unchanged under any outcome:** win probability, margin, totals, contract prices (`predictions`, including the `game_overtime` contract), recommendations, stakes, caps, routing. A promotion changes which model's number is shown in the game-level overtime fields and nothing else.

## 2. G7 — runtime (≤ 300 s per slate, inputs available at the pregame cutoff)
1. **Production evidence:** `duration_s` of every capture-worker cycle that ran `simulate` (which includes the V2 shadow and all other shadow arms) since V2 shadow began, from `STATUS_worker.json` on `data-archive`; report median/p95/max and the share above 300 s. The whole cycle (simulate + app_export + research_export) must stay ≤ 300 s at the 95th percentile.
2. **Marginal cost:** a cold-process measurement of the V2 stage (`shadow_v2.run_shadow`) for a 16-game slate at the production `n_sims` (20,000), five repetitions; median ≤ 150 s (half the budget) and the V2 share of a full `run_simulate` reported.
3. **Inputs at the cutoff:** every V2 input must be derived from records with an observed-at time ≤ the run time (the existing `_read_latest(..., now)` discipline); checked by a test that a record observed after `now` cannot change the V2 output.
Pass = all three.

## 3. G8 — deterministic reproducibility
1. **Process determinism:** the same inputs and seed give byte-identical V2 game summaries across repeated calls and across fresh processes with `PYTHONHASHSEED` ∈ {0, 1, 12345}.
2. **Archive replay:** for every archived live V2 game block available (≥ 50 games; each carries `lam_home`, `lam_away`, `seed`, `n_sims`), re-running `simulate_game_v2` with the repository parameter file reproduces the archived `p_reg_tie` / `p_overtime` / `p_home_win` **exactly** (equality of the floats as archived).
3. **Deterministic training:** `fit_live_params` on the pinned history regenerates `data/params/nhl-sim-2.0.json` (every field except `fitted_at_utc`) exactly.
Pass = all three. A mismatch is reported with its cause, never waved through.

## 4. G9 — publication-contract compatibility
1. With the projection registry at its default (V1) the published slate/app-export documents are byte-identical to the pre-change code (golden test; the existing "V1 output identical with and without the V2 shadow" test continues to pass).
2. With the registry set to the candidate, every changed field keeps its name, type and range; the only additions are provenance fields (`overtime_model`); documents still validate against `edge_finder.app.v1`; `p_reg_tie == p_overtime`, `p_home_reg_win + p_away_reg_win + p_overtime == 1` (±1e-9) and the ladder checks hold.
3. **Fail-safe:** if the V2 arm fails, is absent or is not finite for a game, that game publishes V1's numbers with `overtime_model.fallback = true`; never a partial mixture of the two.
4. The registry refuses to select a non-default model unless it carries an explicit approval record (§6), so merging the code cannot promote anything.
Pass = all four.

## 5. G10 — live non-inferiority (preregistered)
* **Sample:** regular-season games whose scheduled start is **≥ 2026-10-26T00:00:00Z** (later than this document's merge), settled `final`, with a V1/V2 pair in the same archived slate snapshot generated **≥ 10 minutes before the start** (the latest such snapshot). Games before 2026-10-26 (the shadow ran since 2026-09-29) are reported descriptively once, after this document is merged, and **cannot count toward the decision**.
* **Metric and statistic:** per game Δᵢ = (p₂ᵢ − yᵢ)² − (p₁ᵢ − yᵢ)² with p = P(overtime), y = 1 if the game ended in OT or SO; Δ̄ = mean Δ; 95% **upper** bound by a date-cluster bootstrap (ET date clusters, 4,000 resamples, seed 20261024).
* **Size:** the paired per-game Δ has SD 0.0349 (18,777 historical games). To show Δ̄ upper < +0.0010 (the registered Brier non-inferiority margin of `promotion.NON_INFERIORITY`) with 90% power at the historical true Δ = −0.0022 needs n ≈ 1,019; **primary look n = 1,050 paired games** (about late March 2027 at the usual pace of ≈ 7 games per day). Stated plainly: a shorter live window cannot establish non-inferiority at this margin.
* **PASS at the primary look** requires all of: (a) Δ̄ upper95 < +0.0010; (b) Δ̄ < 0; (c) |mean p₂ − mean y| ≤ 0.03; (d) pair coverage ≥ 90% of eligible games and V2 fallback ≤ 5% of eligible games; (e) every pair satisfies the pregame-provenance rule above.
* **Interim looks (harm only) at n = 250, 500, 750:** G10 is declared FAILED, and the candidate withdrawn from consideration, if the **99%** interval lower bound of Δ̄ is > 0 (significantly worse). No interim look can pass the gate or shorten it.
* **Not decisive at 1,050** (Δ̄ < 0 but upper95 ≥ +0.0010): one pre-registered extension look at n = 1,600; no other. At the extension the same rule applies; if it fails to show non-inferiority the gate FAILS.
* **After a promotion** (if ever approved): the same statistic on a rolling 500 paired games; lower95 > 0 triggers the automatic demotion to V1 (a registry change back to the default), reported at once.
* The evaluator (`research/overtime_gates.py live`) reads only immutable archive records and is run on a schedule; its output is a report, never a switch.

## 6. The reversible registry change
`data/registry/projection-registry.json` (default `DATA_ONLY_V1` for the overtime target). A promotion is **one reviewed pull request** that changes that value and adds an approval record `{approved_by, approved_at_utc, evidence}`; the code ignores a non-default value without a complete approval record. Rollback = revert that commit or set the value back; no data migration. The change is prepared as a **draft** and is not merged or activated without the owner's explicit approval.

## 7. What would change this registration
Only a documented amendment written before the affected data exists, never after a G10 number has been seen.
