# NHL Kalshi bet router — production wager capture + settlement (handoff, 2026-09-29)

## A. Verdict
**NHL ROUTER READY BUT HELD FOR FIRST OBSERVED DELIVERY.**
- Every piece is merged and live on production.
- Production runs are clean, and adding NHL changed no other sport's routing.
- One owner-side credential scope blocks the final hop: the router's token cannot open pull requests on this repository (section K).
- Auto-merge for NHL stays `False` until the first real NHL delivery is observed.
- `NHL_DESTINATION_READY=true` on fixtures: the full import/settle/validate path passes end-to-end against the real importers.

## B. SHAs
| | |
|---|---|
| kalshi-bet-router start | `4e9532a` |
| kalshi-bet-router main after PR #103 | `1dc65f3` (the code production runs; the docs follow-up is listed in C) |
| NHL-edge-finder start | `d0db2c5` |
| NHL-edge-finder main after PR #6 | `9efa2de` |
| `accounting-data` head | `4a0e769` (orphan branch; README plus two empty ledgers) |

## C. PRs
- NHL-edge-finder **#6**: the accounting package, the importers and the validator, with 52 tests.
- kalshi-bet-router **#103**, which adds:
  - `Sport.NHL`
  - the competitions and classification changes
  - 20 registry series
  - `to_nhl_import_row`
  - the NHL `DestinationProfile`
  - the probe additions
  - 37 NHL tests
- A docs follow-up in each repo (production verification plus this handoff).

## D. Classification
| Kalshi evidence | Verdict |
|---|---|
| competition "Pro Hockey" (the live taxonomy files it under Hockey) | **NHL** |
| "NHL", "National Hockey League" | **NHL** |
| "College Hockey (M/W)", "NCAA Hockey" | OTHER |
| KHL, SHL, AHL, PWHL, Finland Liiga, Germany DEL, Czech Extraliga, Switzerland National League, IIHF, World Juniors, Field Hockey | OTHER |
| an unknown competition under Hockey | UNRESOLVED (`competition_unknown`), fail closed |
| "Pro Baseball" filed under Hockey (seen 2026-09-15) | **MLB**, unchanged (NHL is a closed-vocabulary league, so it is no rival) |
| the word "hockey" in series tags or title alone | never NHL evidence |
| Tennis | unchanged and unrouted |

**Series recognised (exact match, all verified):**
- Game lines: KXNHLGAME, KXNHLSPREAD, KXNHLTOTAL, KXNHLTEAMTOTAL, KXNHLOT, KXNHLOVERTIME.
- Periods: KXNHL1P, KXNHL2P, KXNHL3P, KXNHL1PTOTAL, KXNHL2PTOTAL, KXNHL3PTOTAL, KXNHL1PSPREAD, KXNHL2PSPREAD, KXNHL3PSPREAD.
- Players: KXNHLFIRSTGOAL, KXNHLGOAL, KXNHLPTS, KXNHLAST, KXNHLSAVES.

**Live check (series probe run 36624797846):**
- All 20 registry series were confirmed, and the taxonomy had 0 collisions.
- A public opening-night sample of 6 markets (moneyline, spread, total, team total, overtime, 1st period) classified `{'NHL': 6}` through `L1_event_competition` = "Pro Hockey", giving `NHL_LIVE_SAMPLE_ALL_NHL=true`.

## E. Destination
- **Repository:** `chmoses98/NHL-edge-finder`. The ledger branch is `accounting-data`, an **orphan** branch.
  - The repository's `main` carries shadow model snapshots and research data, which must never sit in the accounting ledger. CFB uses the same pattern.
- **Code:** comes from `main`.
- **Merge paths:** exactly `data/accounting/wagers.jsonl` and `data/accounting/settlements.jsonl`.
- **Row format:** no season partition. IDs are minted from `source_bet_key` (`nhlw-`/`nhls-`), and settlements use `router-settlement-economics.v2`.
- **Profile settings:** `requires_season=false` and `ledger_branch_runs_ci=false`. The destination's own validator supplies the verdict, and `auto_merge=false`.

## F. Tests
| Repo | Result | NHL-specific tests |
|---|---|---|
| kalshi-bet-router | 1657 passed, 1 skipped (baseline 1619 + 1) | 37 |
| NHL-edge-finder | 381 passed | 52 |

- CI was green on both Python versions for router PR #103 and green on NHL PR #6.
- The router's hockey-out-of-scope tests were rewritten to use sports that really are out of scope (Basketball, Golf). None were deleted.

## G. Idempotency
- **Tested** by the router's end-to-end test against this repository's real importers, together with `tests/test_accounting.py` here:
  - Re-importing an identical wager gives DUPLICATE_NOOP and changes zero bytes.
  - An identical settlement re-import behaves the same way.
  - The same key with different economics gives CONFLICT and exits 1.
  - An orphan settlement is refused.
  - The validator passes.
  - Only the two ledger paths change.
  - Reconciliation by identity accounts for every row.
- **Checked in production on every run:** the workflow imports twice and requires the git tree to be unchanged after the second import. Run 36627519837 reported "a second identical import changed nothing" for every destination.

## H. Privacy
- The importer, the settlement importer and the validator print only counts and failure reasons. They never print a ticker, stake, price, contract count, P&L or `source_bet_key`, and a test enforces this.
- The router's probes print counts and public catalogue names only.
- No routed row carries model provenance, and the destination refuses such fields.

## I. Production
| Run | Result |
|---|---|
| Credential probe 36624794314 | NHL-edge-finder: read ✔ push ✔ **open PR ✘ (403)**; the other four destinations ✔ |
| Series probe 36624797846 | as described in D |
| Delivery dry run 36624801843 | success; `ROUTER_COVERAGE sport=NHL eligible=0`; CFB 75, MLB 81, NFL 56, all DUPLICATE_NOOP; 0 destinations failed |
| **Scheduled production delivery 36627519837** (`DRY_RUN=false`) | success; identical counts; UNACCOUNTED 0 everywhere; no `::error::` |
| Production settlement 36624693205 | success; NHL registered with v2 economics; 131 settled (CFB 75, NFL 56 DUPLICATE_NOOP) |
| Pre-merge baseline 36623489485 | the same eligible 212 and blocked 14, so the change moved nothing |

- **No NHL wager has been placed yet.** No NHL row has been delivered and **no real NHL settlement has been observed**. The settlement path is TESTED only.
- The runs report `HEALTH: blocked`, which predates this work and is not NHL: 5 soccer orders and 9 NFL combo markets with no competition.

## J. Authority
NHL WAGER ROUTING IS ACCOUNTING ONLY. ALL NHL MODELS REMAIN RESEARCH_ONLY. NO AUTOMATIC BETTING AUTHORITY WAS CREATED. NO BETS WERE PLACED BY THIS WORK.

Kalshi access remains read-only.
- No order placement, cancel, amend, staking hook or model-to-execution link was added.
- DATA_ONLY_V1, DATA_ONLY_V2, nhl-sim-1.1, nhl-sim-2.0, the model weights, staking, recommendations and bet selection are untouched.

## K. Owner action
**One action: grant the router's `DOWNSTREAM_REPO_TOKEN` "Pull requests: Read and write" on `chmoses98/NHL-edge-finder`.**
- For a fine-grained token: in GitHub → Settings → Developer settings → Fine-grained tokens, add `NHL-edge-finder` to the token's repository access. Keep Contents and Pull requests at Read and write, which is what the other destinations already have.
- Then re-run `downstream-credential-probe.yml`. The probe should report "RESULT: usable for delivery" for NHL.

**If an NHL bet is placed before the fix:**
- The router pushes it to `kalshi-router/NHL`, flags an NHL-only error, and retries on every run.
- Nothing is lost.
- It is recorded on the first run after the fix.
- While auto-merge is off, the owner merges that delivery PR, or it is left for the auto-merge flip once one delivery has been observed.
