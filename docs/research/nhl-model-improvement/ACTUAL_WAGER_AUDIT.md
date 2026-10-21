# Actual routed wagers (34) and the October 20 case study

> RESEARCH ONLY. Separate from every backtest. The accounting ledger and the exchange records were read, never modified. Row-level evidence: `data/wager_classification.csv` / `.json` (34 rows, built from the raw ledger by a read-only reviewer; independently re-resolved against the archive). Nothing was placed or simulated against a live API.

## 1. What the router records (and does not)

* The router **places nothing**. It reads fills (`GET /portfolio/fills`), groups them by order id and files one row per final order; the owner bets by hand. The client is read-only (`_get` hard-codes GET; `/portfolio/orders` is not on the allow-list) and the NHL importer refuses provenance-style fields and any unknown field. So "the ledger refuses model/provenance fields" is correct.
* Each NHL row has 13 fields + `wager_id` + `schema_version`: `source_bet_key` (one-way hash), `import_batch_id`, `entry_method` (constant `IMPORTED_RECEIPT`), `game_date`, `market_ticker`, `side`, `executed_at`, `contracts`, `execution_price`, `stake`, `fees_paid`, `fees_are_estimated`, `venue`.
* **Not recorded:** exchange order id and fill ids, order status, order-created time, last-fill time, ledger-ingest time, maker/taker flag, and — critically — **the buy/sell action**. `side` is the contract traded, not the exposure (`EXPOSURE_SIDE_DESTINATIONS` is empty; `REDUCTION_NOT_REPRESENTABLE` is defined but never returned), so a *sell* of YES is filed like a *buy* of YES. The app export's `side:"BUY"` is hard-coded and is not evidence.
* `executed_at` = the exchange `created_time` of the order's first fill, truncated to the second. No ledger-observed time exists.
* **Provenance:** none. A ticker/side/time join to `thesis_decisions` is a heuristic: only 10 of 34 wagers have any decision before the fill; 2 were ever FUNDED_RESEARCH; routed stakes ($1–3 on the six Oct 1 prop/spread wagers) do not equal card stakes ($3–8.55). I did not infer provenance; every wager is **model-driven / manual / unknown = UNKNOWN**.

## 2. Entry / exit classification

Rule (no row is provable from a field because there is no action): **ENTRY only if it is the first order on its ticker** (a contract cannot be sold before it is held; assumes the ledger holds every order on the ticker). Result: **31 ENTRY, 1 EXIT, 1 PARTIAL_CLOSE, 1 UNKNOWN.**

* EXIT `nhlw-be219cd805a24d23efa250b6` (EDMCMCDAVID97 YES 12.35 @ 0.99, 2026-10-02T03:07:30Z) offsets two NO orders summing to exactly 12.35 contracts — a hedge/close, or an independent new bet, is not excluded.
* PARTIAL_CLOSE `nhlw-063d93e0ffdfae0b05b331bb` (Suzuki NO 1.00 @ 0.64) after a 103.79-contract YES position.
* UNKNOWN `nhlw-eaa495b337e216f9ef552adf`: a same-side repeat 16 s after the first at the same 0.31 — add-on buy and sell-close cannot be told apart.
* The EDM and MTL hedged pairs are counted as independent bets in the audit's z-score; netting same-ticker positions leaves the SD at 218.9 (vs 219.06): immaterial.

## 3. Performance, verified from raw records

34 wagers, staked **$1,011.79**, fees **$31.19**, net **−$187.64** (17 won, 17 lost). Each stake equals contracts × price + fee and each net equals gross − stake. The market-implied expectation at the fills (Σ contracts × P(win at the last board tick ≥45 s before the fill) − stake) replicates exactly at **−$55.85** (SD 219.06, z = −0.60; next-tick −57.77, average −56.81). Fees alone are −$31.19, so ≈ −$24.7 is spread. **The realised shortfall is statistically indistinguishable from fair-price trading.** Caveats the original audit did not state: boards are up to 27 minutes old (median 5.6); the 11 post-drop fills are benchmarked against pre-drop boards; the SD treats wagers as independent although same-day Unders are correlated.

Descriptive splits (n = 34; **associations, not causes**; none is significant):

| split | wagers | staked | net | ROI on stake |
|---|---|---|---|---|
| game-scoped (winner, spread, total, team total) | 21 | $610.92 | −$9.15 | −1.5% |
| player props (points, goals, assists, saves) | 13 | $400.87 | **−$178.49** | **−44.5%** |
| — player goals | 4 | $79.00 | −$79.00 | −100% (0 of 4) |
| — player points | 5 | $275.63 | −$121.91 | −44.2% |
| game_winner | 7 | $287.97 | +$86.87 | +30.2% |
| game_total / team_total | 4 / 4 | $129.99 / $107.99 | −$45.16 / −$68.59 | −34.7% / −63.5% |
| stake tercile (small / mid / large) | 12 / 11 / 11 | $70.9 / $265.0 / $676.0 | +$2.1 / +$56.4 / **−$246.1** | +2.9% / +21.3% / −36.4% |
| price band ≤0.30 / 0.30–0.50 / 0.50–0.70 / >0.70 | 4 / 10 / 16 / 4 | $79 / $262 / $561 / $110 | −$79 / +$36 / −$77 / −$67 | −100% / +13.7% / −13.8% / −60.9% |
| pre-drop / post-drop fills | 23 / 11 | $673.94 / $337.86 | −$138.41 / −$49.24 | −20.5% / −14.6% |

**Reading:** essentially the whole loss is the player-prop book (−$178.5 of −$187.6); game-scoped wagers were about break-even net of fees. The largest-stake tercile lost the most, but stake size is confounded with family and price and the sample is 11 wagers; with all 34 the realised loss is only 0.6 SD below the fair-price expectation, so no market family, stake or price band is established as the cause. Player goal-scorer contracts are excluded from actionable recommendations by the research brief; four such routed wagers lost all $79.

Post-drop fills: 11 of 34 were filled after the scheduled puck drop (stake $337.86, net −$49.24). The archive stores only hourly schedule snapshots, so *actual* puck drop is not archived; "post-drop" means after the scheduled time.

## 4. October 20 case study (explanatory; not a validation sample; nothing tuned to it)

The ledger shows **two wins and two losses, net −$27.29** (recomputed −$27.2882 from raw fills: stake $114.99, fees $3.79), not four losses.

### The late-fill / cash-out ambiguity — resolved

Three of the four fills carry `executed_at` 6–8 minutes **after** the scheduled drop. Evidence that these are genuine new entries, not cash-outs or ledger-sync artefacts:
1. `executed_at` is the exchange fill time in code. Import requires a closed market, so a sync stamp would read ≈01:20–02:51Z; these read 23:06–23:07Z.
2. The archive's volume counter on `KXNHLTEAMTOTAL-26OCT20LAWSH-LA3` rises 1,498.52 → 1,564.87 between the 23:03:02Z and 23:10:02Z ticks — a jump of exactly **66.35 = the order size**; no earlier jump of that size exists on the ticker. Volume rose by at least the order size around the fill for all 34 wagers.
3. Every fee equals `0.07·c·p·(1−p)` (ratio 0.9996–1.0048 across all 34): each order crossed the book on arrival (taker), so order-created time ≈ fill time. This is an inference from the fee schedule, not a stored field.
4. Prices track the live book (LAK NO ask 49c at 23:03 → 53c at 23:10; filled at 51c).
5. Each Oct 20 ticker has one ledger order, so no row offsets another.

Residual uncertainty: order-created time is not recorded and actual puck drop is not archived. The BOS/DAL wager was filled 52.7 minutes **before** the 00:00Z drop.

### The four wagers through the model (`data/oct20_case_model_view.json`)

| game | contract | fill vs scheduled drop | price | V1 P(side) | V2 P(side) | Kalshi P(side) at T-60 | V1 EV/contract at fill | result |
|---|---|---|---|---|---|---|---|---|
| TOR @ CBJ | Under 6.5 total | +6.1 min | 0.54 | 0.553 | 0.586 | 0.495 | −0.004 | **lost** (TOR 6–2) −$35.00 |
| LAK @ WSH | LAK team total Under 2.5 | +6.8 min | 0.51 | 0.557 | 0.487 | 0.480 | +0.030 | **lost** (LAK 5–2) −$35.00 |
| BOS @ DAL | Under 5.5 total | −52.7 min | 0.50 | 0.551 | 0.442 | 0.495 | +0.033 | won (DAL 3–2 OT) +$23.30 |
| ANA @ NYI | ANA team total Under 2.5 | +7.7 min | 0.49 | 0.503 | 0.433 | 0.470 | −0.005 | won (NYI 3–2) +$19.40 |

*Pregame thesis quality.* In all four the Kalshi price at T-60 already put the Under at 47–50% (mid ≈ 0.50–0.53 for the Over), and the route paid the **ask plus fee**, i.e. 2–4 cents above the market's own probability: market-implied EV at the fill (Kalshi T-60 probability − price − fee) was −6.2, −4.8, −2.3 and −3.8 cents per contract for the four wagers in table order. V1 saw a small positive EV in two (+3 cents) and ≈ 0 in the other two; **V2 disagreed with the Under in three of four** (BOS/DAL 0.44, ANA 0.43, LAK 0.49), and V1 and V2 disagree in sign on two. Where the two engines of the same lineage disagree, that is model uncertainty, not edge. Neither engine has shown value beyond the market (see `CHALLENGER_MODEL_COMPARISON.md`); under the corrected expression engine none of these would have been eligible (no VALIDATED family, model weight ≈ 0).
*Goalies.* All eight starters were as named at the cut (CONFIRMED except LAK's Kuemper, PROBABLE, who started): no goalie-information explanation exists. TOR@CBJ: CBJ were outshot 37–19 yet conceded 5 on 19 shots (14 saves; .737) — finishing/goaltending variance, not a goalie-assumption error.
*Scoring.* The two losses were single-team outbursts by the road side (TOR 6, LAK 5 against model rates of 2.57 and 2.35). Predictive-distribution positions: TOR@CBJ total PIT 0.77 / margin PIT 0.025 (classified F: unresolved, margin tail); LAK@WSH margin PIT 0.051 (E: normal variance). Across all 151 LIVE games 17.2% were "extreme" by this definition versus ≈ 19% expected under a calibrated model — four games do not tell us anything about model quality.
*Should they have been rejected?* Under the evidence the research program now has — no demonstrated forecast edge over the market, positive spread + fee cost on every taker fill, three of four placed *after* the game began (live-book, score-aware prices that a pregame model cannot evaluate) — **yes: a PASS is the evidence-consistent decision for all four**, regardless of how they settled. That is a process judgement; it is not derived from the two wins and two losses.

## 5. What is needed for a trustworthy wager audit going forward

1. Record the exchange `action` (buy/sell), order id, created/filled/ingested timestamps and maker/taker flag in the router's raw record (proposal; needs approval — it is a production-capture change).
2. A recommendation id (card hash + ticker + side) carried on each routed wager, or an explicit `MANUAL` marker, so model-driven vs manual is not inferred from time and ticker.
3. Archive actual puck-drop/first-faceoff time.
