# Owner decision on G7 (2026-10-25)

**Decision (owner):** G7 for the V2 overtime candidate is **inference time per slate**, as defined by `promotion.MAX_INFERENCE_SECONDS_PER_SLATE`, threshold **300 seconds**. The direct 16-game measurement of ≈ 34 s passes.

What this changes and what it does not:

| item | status |
|---|---|
| G7 (inference time per slate, 300 s) | **passed** — ≈ 34 s for a 16-game slate (`GATES.md`, direct cold-process measurement; archived runs are not slower) |
| G8 reproducibility, G9 publication contract | remain **passed** |
| G10 live non-inferiority | remains **open**: frozen start 2026-10-26, 1,050 paired settled games, harm looks at 250/500/750 |
| overtime promotion | **not authorized**; `data/registry/projection-registry.json` stays at the V1 default with no approval record |

## The whole-cycle proxy is preserved, not rewritten
`PREREGISTRATION_G7_G10.md` (frozen) registered a coarser criterion 1: whole capture-worker cycles that ran `simulate`. Its registered result stands exactly as recorded in `GATES.md`: 655 cycles since 2026-09-29, median 127 s, **p95 1,081 s, max 1,539 s, 17 % of cycles above 300 s — fails the 300 s threshold**. It is now tracked as a separate **operational delivery metric** (end-to-end cycle time), for which no pass/fail claim against the 300 s inference threshold is made. In particular:

* end-to-end delivery does **not** pass the 300 s threshold, and nothing in this repository claims it does;
* the metric is driven mostly by jobs unrelated to V2 sharing the cycle (context capture, settlement, exports); it should be watched for delivery reliability (`docs/research/DELIVERY_MONITORING.md`), not used as a promotion gate.

No frozen file was edited; `PREREGISTRATION_G7_G10.md` and the registered numbers are unchanged.
