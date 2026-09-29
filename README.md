# NHL-edge-finder — accounting-data (routed-wager ledger)

**ACCOUNTING ONLY.** This branch records NHL bets the owner placed **manually** on Kalshi, as observed (read-only) and
delivered by `chmoses98/kalshi-bet-router`, and what the exchange later paid on them. It holds nothing else: no model
predictions, research snapshots, slate packets or V1/V2 outputs. A row here says "the owner placed this bet", never
"a model recommended it". All NHL model families remain RESEARCH_ONLY.

| file | contents |
|---|---|
| `data/accounting/wagers.jsonl` | one line per order (`nhl_accounted_wager.v1`), append-only |
| `data/accounting/settlements.jsonl` | one line per settled wager (`nhl_wager_settlement.v1`, `router-settlement-economics.v2`), append-only |

The importers and validator live on `main` (`scripts/accounting/`, `docs/ACCOUNTING.md`). This orphan branch carries
no `.github/`, so pull requests into it get no CI; the router runs the destination's own validator and merges only when
its gate passes. Existing lines are never rewritten or removed.
