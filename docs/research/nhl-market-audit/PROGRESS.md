# NHL market audit - progress ledger (resume here)

Branch `research/nhl-market-audit-20261021` (from `main` f6e477f). RESEARCH_ONLY. Nothing here touches production, stakes, the archive, a model or a data contract. Update this file at every checkpoint.

## Reproduce

```
python -m venv .venv && . .venv/bin/activate && pip install -e ".[dev]" scipy statsmodels
git fetch --depth=1 origin data-archive accounting-data
mkdir -p ../rdata/data-archive ../rdata/accounting-data
git archive origin/data-archive    | tar -x -C ../rdata/data-archive      # ~16.8k files, ~5 GB on disk
git archive origin/accounting-data | tar -x -C ../rdata/accounting-data
python -m nhl_edge.market_audit.pipeline --archive ../rdata/data-archive --accounting ../rdata/accounting-data \
    --history data/history --repo . --work ../rdata/work --out docs/research/nhl-market-audit/data      # ~25 min cold, resumable
python -m nhl_edge.market_audit.render_reports --data docs/research/nhl-market-audit/data --out docs/research/nhl-market-audit
python -m nhl_edge.market_audit.scorecard --data docs/research/nhl-market-audit/data --ledger ../rdata/evidence_ledger.jsonl
```
Snapshot analysed: data-archive `2db3b91` (manifest 14,214 rows, last tick 2026-10-21T15:51:18Z); accounting-data `70c507a`.

## Frozen / one-shot items (do NOT redo or edit)

* Hypothesis registry `nhl-hypotheses-1.0` frozen at git `627b5fa7` (2026-10-21T17:13:05Z). Each test ran ONCE on the LIVE tier (2026-09-29..10-20). The LIVE tier is spent. A changed idea is a new id.
* Matchup-factor study design committed at `6164c712` before its results. Games that START after the freeze are PROSPECTIVE (looks at 150 / 300 / 450 games).
* Known defect in the frozen rule (reported, not redefined): single-tier PROMISING (M14, ROI +0.1%) is a false label. Registry v1.1 should require a positive lower-90% bound.

## Status

| phase | state |
|---|---|
| A inventory / coverage / quality / reconstruction | done (reports rendered from `data/*.json`; pipeline re-run cold end-to-end and reproduces every exploratory number) |
| B taxonomy + outcome engine | done; 0 disagreements vs production (31,478) and vs Kalshi history (15,892) |
| C market efficiency | done (HIST 1,312 games; LIVE 151 games) |
| D matchup factors | done; no block adds information beyond the market |
| E model audit, Oct-20 case study | done; ledger shows 2 wins + 2 losses on Oct 20 (not 4 losses) |
| F signal registry | done; 0 VALIDATED of 16 |
| G expression engine | shadow module + replay + tests; wiring NOT done (needs approval) |
| H replay / walk-forward / robustness / executability | done |
| I risk framework | document only |
| J automation | pipeline, scorecard, ledger, workflow (manual dispatch only) |

## Remaining / next exact action

1. Review the draft PR; decide on merge and on enabling the daily workflow (see IMPLEMENTATION_ROADMAP.md).
2. When prospective games reach 150, run the pipeline and read `hypothesis_results.json -> results.*.prospective` ONCE; do not look earlier.
3. Capture changes proposed in AUTOMATION_AND_MONITORING_PLAN.md need approval (production code is untouched).

## Known blockers

None. No credentials were required. The `gh` CLI is unavailable; GitHub operations go through the MCP tools.

## Verification record (this session)

* Full suite: 621 passed, 2 skipped (baseline before changes: 581 passed, 2 skipped). New: 37 tests in `tests/test_market_audit_*.py`. Ruff clean on all new files; 66 pre-existing ruff errors in untouched `research/` and `contract/` files are unchanged.
* Pipeline: cold run ~25 min; resumable; steps re-stamped only where inputs were unchanged (documented in git history).
* Reviewer-facing corrections made after proofreading the rendered text against the JSON: matched-control p-value label (it is P(control >= selected)), moneyline "no bias" -> "no statistically significant bias", model-worse verdicts qualified as uncorrected/overlapping, power statement split by price level, V1/V2 direction text computed from data.
* Exploration of `kalshi-bet-router` / `sift-sports-intelligence` by a subagent; the claims that matter (read-only client, no provenance field, cash-outs recorded as the contract traded) were re-checked directly in router source. Router docs contradict router code on NHL auto-merge (reported, not edited).
