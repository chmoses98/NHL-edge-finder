# NHL market audit — progress ledger (resume here)

Branch `research/nhl-market-audit-20261021` (from `main` f6e477f). RESEARCH_ONLY. Nothing here touches production,
stakes, the archive, or a model. Update this file at every checkpoint.

## Environment to reproduce
```
python -m venv .venv && . .venv/bin/activate && pip install -e ".[dev]" scipy statsmodels
git fetch --depth=1 origin data-archive accounting-data
mkdir -p ../rdata/data-archive ../rdata/accounting-data
git archive origin/data-archive | tar -x -C ../rdata/data-archive      # 16,769 files, ~5 GB on disk
git archive origin/accounting-data | tar -x -C ../rdata/accounting-data
```
Archive snapshot used: data-archive `2db3b91` (manifest 14,214 rows, last tick 2026-10-21T15:51:18Z).

## Done (checkpoint 1)
- [x] Phase A integrity: manifest 14,214 entries, 0 missing / 0 duplicate / 0 hash mismatch; all 256 delta chains verify.
- [x] `market_audit/streams.py`: every tick (2,870) -> `quote_events` (2.16M), `book_events` (687K), `market_static` (35,992 tickers).
- [x] `market_audit/taxonomy.py`: 35,992 / 35,992 game-scoped tickers have a PROVEN spec (structured strike == rules wording).
- [x] `market_audit/outcomes.py`: independent resolver. vs production settlements: 31,478 co-decided, 0 disagreements.
- [x] `market_audit/history_validation.py`: vs Kalshi's own settlement on 2025-26 history: 15,892 / 15,892 agree (1,360 shootout games).
- [x] tests: `tests/test_market_audit_outcomes.py` (16 passing). Baseline suite before changes: 581 passed, 2 skipped.

## Remaining (in dependency order)
1. Phase A reports: coverage per game / family / horizon, quality audit, orderbook coverage, temporal checks, wagers join.
2. Phase C: efficiency (history candles 2025-26 tier; live-archive tier).
3. Phase E: V1/V2/market audit; Oct-20 case study (note: ledger shows 2 of the 4 named bets WON — see CASE STUDY).
4. Phase F/H: preregistered hypothesis registry, discovery/validation split, walk-forward.
5. Phase G/I/J: expression-engine spec + shadow prototype, risk framework, automation plan, handoff, draft PR.
