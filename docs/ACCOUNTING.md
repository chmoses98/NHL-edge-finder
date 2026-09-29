# NHL wager accounting (routed from kalshi-bet-router)

**Accounting only.** This records bets the owner already placed manually on Kalshi. It never decides, sizes,
recommends or places a bet. All NHL model families (DATA_ONLY_V1, DATA_ONLY_V2, MARKET_ANCHORED_V1) remain
RESEARCH_ONLY, and nothing here reads or writes them.

## How a wager gets here
1. The owner places an NHL bet on Kalshi by hand.
2. kalshi-bet-router, which has READ-ONLY exchange access, sees the fills on its next scheduled run. It classifies
   the market as NHL from Kalshi's own metadata (competition "Pro Hockey"), rebuilds the order from its fills and
   sends one `to_nhl_import_row` row.
3. The router opens a delivery pull request into this repository's `accounting-data` branch, running this
   repository's importer (`scripts/accounting/import_routed_wagers.py`, code taken from `main`) and its validator
   (`scripts/accounting/validate_routed_ledger.py`). It merges only when the gate passes.
4. After Kalshi settles the market, the router's settlement job delivers the settlement the same way
   (`scripts/accounting/import_routed_settlements.py`, `router-settlement-economics.v2`).

**The router is the exchange-evidence authority.** Price, contracts, stake and fees come from the observed Kalshi
fills, and `fees_are_estimated` is always false. Nothing is reconstructed or estimated here.

## Where it lives
| what | where |
|---|---|
| ledger branch | `accounting-data`: an orphan branch holding only a README and the two files below; no model data |
| wagers | `data/accounting/wagers.jsonl` (`nhl_accounted_wager.v1`), one line per order |
| settlements | `data/accounting/settlements.jsonl` (`nhl_wager_settlement.v1`), one line per settled wager |
| code | `main`: `src/nhl_edge/accounting/ledger.py`, `scripts/accounting/*.py` |

There is no season partition, because an NHL season spans two calendar years and filing must never guess one.

## Guarantees (tested in `tests/test_accounting.py`)
- **Identity is minted here and is deterministic.**
  - `wager_id` = `nhlw-` + sha256(`source_bet_key`)[:24].
  - `settlement_id` = `nhls-` + sha256(`source_bet_key`)[:24].
  - No wall clock and no economics feed into either.
- **Same row twice** gives `DUPLICATE_NOOP` and zero bytes change.
- **Same key with different economics** gives `CONFLICT` (field names reported, never values). Nothing is rewritten, and the importer exits 1 so the router's gate fails.
- **A settlement with no wager on the ledger** is refused as `ORPHAN`.
- **A second, different settlement** for a settled wager is a `CONFLICT`.
- **Rows that are refused:** model or recommendation provenance fields; unknown fields; estimated fees; a venue other than kalshi; non-positive contracts or stake; a price outside (0, 1); malformed timestamps.
- **The validator** checks that every line decodes, both schemas, unique keys, that every settlement has its wager with the same ticker and side, and (with `--against <ref>`) that no existing line was removed or rewritten.
- **Public Actions logs** carry counts and reasons only: never a ticker, stake, price, contract count, P&L or source key.
