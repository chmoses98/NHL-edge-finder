# Implementation roadmap and decisions needed

> Ordered by value per unit of effort. Nothing below is activated; every item is gated.

## Done in this branch (draft PR)

* Independent taxonomy + resolver, validated three ways (production settlement, three-source reconciliation, Kalshi's own settlement on 15,892 history markets).
* Reproducible 20-step pipeline with lineage; coverage, quality, efficiency, model, matchup, replay, wager and case-study reports; frozen hypothesis registry; shadow expression engine (default PASS); scorecard + ledger; disabled workflow.
* 27 + 4 new tests (all passing); the existing suite is unchanged and passing.

## Next (in dependency order)

| # | item | why | needs |
|---|---|---|---|
| 1 | Review and merge this research PR (code + docs only; no production path imports it) | makes the audit reproducible by others | **decision: approve merge** |
| 2 | Enable the daily workflow, `publish=false` first | starts the prospective clock accumulating evidence | **decision: approve the schedule** |
| 3 | Capture changes 1-5 in AUTOMATION_AND_MONITORING_PLAN.md | unlock settlement audit on live data, depth beyond four families, maker-fill estimation | **decision: approve a change to production capture** |
| 4 | Registry v1.1: PROMISING must require a positive lower 90% bound; add period/overtime hypotheses with a depth-aware cost model | fixes the rule defect found in M14 | none (new ids only) |
| 5 | Re-simulate stored seeds to get full predictive distributions, then CRPS / tail diagnostics | the archive stores threshold probabilities only | compute |
| 6 | Timestamped goalie / lineup / injury news (when the market could have learned it) | the only plausible source of a real pregame edge is information timing; it is untestable today | new capture |
| 7 | First prospective look at 150 games (~Dec 2026 at the current slate size) | the only route to a VALIDATED claim | time |

## Decisions requiring user approval

1. Merge the research branch / enable the workflow (items 1-2).
2. Any change to production capture (item 3).
3. Whether to wire the shadow engine into the card as a display-only "PASS reason" panel (not recommended until a family is VALIDATED).
4. Any stake or cap change: none is proposed; the evidence bar is in RISK_MANAGEMENT_FRAMEWORK.md.
