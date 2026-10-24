# Promotion recommendation — V2 overtime / regulation-tie projection (DRAFT, not actionable yet)

RESEARCH_ONLY. **Status 2026-10-24: do not promote.** G1–G6b and J1 pass (historical, frozen); G7, G8, G9 pass (`GATES.md`); **G10 (registered live non-inferiority) is open until ≈ late March 2027** and is the only thing between the candidate and a promotion decision. This page records what I would recommend *if G10 passes*, so the decision is quick and reversible; it recommends nothing today.

## What would change
Only the game-level overtime fields of the published slate / app export (`p_reg_tie`, `p_overtime`, `p_home_reg_win`, `p_away_reg_win`, `p_shootout`) would come from `DATA_ONLY_V2` instead of `DATA_ONLY_V1`; V1's values stay beside them in an additive `overtime_model` block. **Not changed:** win probability, margin, totals, every contract price (including the overtime contract), recommendations, stakes, caps, routing, the app contract version. The overtime contract's model price stays V1 until you decide otherwise (changing a price is outside this promotion).

## Evidence in one paragraph (all in merged documents)
Brier(OT) −0.0025 [−0.0033, −0.0017] vs V1 on the untouched 2010–2016 seasons (7/7 favourable, both bootstraps), −0.0022 pooled 2023–25, −0.0023 on all 18,777 games 2010–2025; V1 predicts 18.7% overtime games (CLEAN2) against 23.7% observed, V2 22.6%; ECE 0.0112 vs 0.0498; regulation 3-class Brier −0.0044; no regression on the other targets (J1); additive with the retuned rates (J2) but the gain is the simulator's. Runtime ≈ 34 s per 16-game slate; archived live predictions replay bit-for-bit (400/400); training regenerates the parameter file exactly; contract tests pass at default and with the switch.

## The change itself (to be made only after G10 passes and with your explicit approval)
`data/registry/projection-registry.json`, target `overtime`:
```json
"published_model": "DATA_ONLY_V2",
"approval": {"approved_by": "<your name>", "approved_at_utc": "<UTC timestamp>", "evidence": "<link to the passing G10 report and this page>"}
```
Reversal: set `published_model` back to `DATA_ONLY_V1` (or revert the commit). No data migration; the loader falls back to V1 automatically if the approval record is incomplete or the V2 arm fails for a game. After a promotion the registered rolling-500 check (`overtime_gates live`) runs against the same archived pairs and a significantly-worse reading triggers the demotion above.

## Residual caveats to weigh
* The promotion makes the published overtime number inconsistent in provenance with the win-probability and totals numbers, which stay V1 (as the scorecard permits: one model per target).
* The live arm is `DATA_ONLY_V2` (special-teams lambdas and goalie true talent), not the exact historical `SIM2` arm; on 2024–25 they differ by ≈ 0.0002 Brier(OT), and G10 tests the live arm itself.
* A new-regime risk exists (the 2025 overtime rate was 24.8% vs 20.7% in 2023–24); the harm looks at 250/500/750 games are there to catch a drift early.
