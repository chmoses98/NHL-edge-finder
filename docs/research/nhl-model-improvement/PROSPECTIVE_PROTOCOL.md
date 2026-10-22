# Prospective shadow protocol (proposal; needs approval before it binds anyone)

> RESEARCH ONLY. The prospective tier is every regular-season game that **starts after 2026-10-21T17:13:05Z** (the prior audit's registry freeze). No code in `nhl_edge.model_research` other than `daily.py` can read such a game; `daily.py` blinds all aggregate model-vs-market performance until a predeclared look.

## What is recorded (every game, automatically, publish=false until approved)

`daily.py ingest` appends one row per *final* game to an append-only, idempotent ledger (`shadow_game_ledger.jsonl`): the forecast frozen at T-60 (last production slate run ≤ cut; run id, age), V1 and V2 probabilities, the frozen challenger C1 probability (parameters from `data/cal_experiments.json`, never refitted), sportsbook consensus, the outcome, predictive-distribution PITs, the Brier/RPS contributions, the attribution class (A–F with evidence), and goalie flags. Kalshi mids join at the look from the market-audit pipeline (which now blinds prospective ROI as well).

## Looks and error spending

* Looks at **150, 300, 450** independent games (information fractions 1/3, 2/3, 1).
* Proposed spending: Lan–DeMets O'Brien–Fleming-type, one-sided total α = 0.05 per *pre-registered primary hypothesis*: cumulative 0.0007 / 0.0164 / 0.0500 (nominal one-sided z ≈ 3.39 / 2.40 / 1.96, approximate). The prior text "alpha spent 0.005/0.015/0.05" summed to 0.07 and was never implemented; this replaces it for any look taken under *this* protocol.
* **Multiplicity:** at most **three** primary hypotheses may be registered before a look (Holm across them); everything else is reported as exploratory. A betting hypothesis additionally needs the v1.1 VALIDATED conditions (positive lower-90% ROI, positive ROI at +1c slippage, BH/Holm-adjusted p within the spending boundary, executability from captured depth).
* Primary forecast comparison (registered as `M-SHADOW-1`): paired game-bootstrap Brier difference of **V1, V2, C1-frozen versus the sportsbook consensus and the Kalshi T-60 mid** on the home-win probability, plus RPS for total goals. One-sided "model better than market" is expected to fail; the useful outputs are (i) calibration drift, (ii) how far models trail, (iii) whether the margin/OT corrections hold out of sample.
* A look is written **once** (`LOOK_150.json` etc., never overwritten; enforced and tested). Between looks the scorecard prints only the game count and PREGAME data-quality measures (sportsbook coverage, slate age). No outcome-derived number (hit rate, Brier, extreme-miss share, attribution classes, goalie-mismatch share) appears before a look; the workflow's `Verify blinding` step fails the run if a LOOK file or an extra field appears early. The default artifact contains only the blinded scorecard and an outcome-free ingest summary; the ledger (which holds outcomes) is never published in the clear: every record is encrypted on the runner with `age` to the owner's public key(s) and only ciphertext plus a hash-chained, outcome-free manifest is committed (`SEALED_LEDGER_DESIGN.md`); the owner decrypts locally at the look. `publish=true` stays refused until the owner has generated keys and activated it (`SEALED_LEDGER_KEY_SETUP.md`). The rules in this protocol are unchanged and their hash is committed in every ledger's genesis entry.

## Power, honestly

At 150 games the standard error of a per-game Brier difference is about 0.004–0.005; a gap of 0.01 is the smallest the first look can resolve. A betting edge of +3% ROI needs hundreds to thousands of independent games depending on price. Expect the first look to be inconclusive unless the effect is large. That is a result, not a failure.

## What is out of scope

No wager, stake, cap, model or recommendation changes at any look without explicit approval. Retraining happens on a controlled schedule on the *development* tier only; a challenger that is changed after a look is a new id and restarts its own prospective clock.
