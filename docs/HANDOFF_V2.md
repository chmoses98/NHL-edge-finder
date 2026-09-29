# HANDOFF: NHL Edge Finder pre-opening-night V2 research upgrade (2026-09-29)

## A. Executive verdict

**PARTIAL V2 READY** — DATA_ONLY_V2 is merged, running as a SHADOW arm and archived with honest timestamps. Its
clear gain is regulation-tie / OT calibration. Moneyline, totals, puck line and team totals are neutral against V1.
**The market remains better than both models**: on 1,312 2025-26 games Kalshi's pregame moneyline and totals beat V1 and V2 at every horizon, and neither model shows detectable information beyond the market price.

## B. SHAs

| ref | start | end |
|---|---|---|
| `main` | `b53b19a` (PR #2 merge) | __MAIN_END__ |
| `data-archive` | `0bd03bf` (capture 14:42Z) at session start | still advancing (worker commits every ~10 min; see D). Never written by this session; no row rewritten |

## C. PRs

| # | purpose | status | CI |
|---|---|---|---|
| 3 | DATA_ONLY_V2 shadow arm: sim 2.0, special teams, goalie true talent, shadow integration, Kalshi/shots ingestion code, period rule review, goalie-status evaluator | merged (`1976790`) | green (push + PR; `main` green) |
__PR4_ROW__

## D. Capture health

- Worker generation 1 (`36568142839`, SHA `a3b4390`) ran the whole session. Archive commits every ~10 min (e.g. 15:12,
  15:22, 15:32Z …). Generation 2 (`36568193942`) waits in the pending slot, **pinned to `a3b4390` (pre-V2)**. It takes
  over at ~17:27Z and dispatches generation 3 with `ref: main`, so the worker's own V2 rows start with generation 3
  (~22:27Z). The worker was never stopped, restarted or duplicated.
- __ARCHIVE_LATEST__

## E. Historical Kalshi benchmark

**Sources:** `data/history/kalshi/` (research-data run 36587430636; historical host, with the live host for gaps).

**Coverage**

| series | settled markets | joined to official NHL games | notes |
|---|---:|---:|---|
| KXNHLGAME | 3,076 | 2,950 | the 126 unjoined are 2025 preseason plus 2 non-schedule games: refused, not guessed |
| KXNHLTOTAL | 7,813 | 7,808 | |
| KXNHLSPREAD | 5,138 | 5,134 | |
| KXNHLOVERTIME | 49 | 49 | playoffs only |
| KXNHLFIRSTGOAL | 24,006 | — | recorded only |

- Kalshi NHL game markets begin in the **2025 playoffs**, so the regular-season benchmark covers **2025-26 only**: 1,312 games, 2025-10-07 .. 2026-04-16.
- No settled history exists for KXNHLTEAMTOTAL or any period series.

**Candles**
- 1.47M candles, hourly and 1-minute windows aligned to official start times.
- About 1% of fetches failed with HTTP 429 and were recorded as gaps.

**Quote definition**
- Candle-close best bid/ask midpoint at or before each horizon; median spread 1¢.
- NOT executable history (no depth).

**Moneyline (identical games and instants):**

| horizon | n | V1 Brier | V2 Brier | Kalshi Brier | V1 log loss | V2 log loss | Kalshi log loss |
|---|---:|---:|---:|---:|---:|---:|---:|
| T-24h (flag) | 1302 | 0.2458 | 0.2457 | 0.2450 | 0.6845 | 0.6843 | 0.6830 |
| T-12h | 1312 | 0.2459 | 0.2458 | 0.2444 | 0.6847 | 0.6845 | 0.6818 |
| T-6h | 1312 | 0.2459 | 0.2458 | 0.2445 | 0.6847 | 0.6845 | 0.6818 |
| T-3h | 1312 | 0.2459 | 0.2458 | 0.2443 | 0.6847 | 0.6845 | 0.6814 |
| T-90m | 1312 | 0.2459 | 0.2458 | 0.2443 | 0.6847 | 0.6845 | 0.6815 |
| T-60m | 1312 | 0.2459 | 0.2458 | 0.2442 | 0.6847 | 0.6845 | 0.6812 |
| T-30m | 1312 | 0.2459 | 0.2458 | 0.2443 | 0.6847 | 0.6845 | 0.6814 |
| T-10m | 1312 | 0.2459 | 0.2458 | 0.2443 | 0.6847 | 0.6845 | 0.6815 |

T-24h is flagged because the model's inputs run through the previous day, which the market had not fully seen.

**Totals, T-60m (Brier):**

| line | V1 | V2 | Kalshi |
|---|---:|---:|---:|
| O5.5 | 0.2444 | 0.2442 | 0.2419 |
| O6.5 | 0.2501 | 0.2496 | 0.2466 |

Kalshi's settled totals agree with the official final score (shootout = one goal) in 100% of 2,390 checks.

**Puck line (KXNHLSPREAD ±1.5, hourly candles; T-60m Brier):**

| side | V1 | V2 | Kalshi |
|---|---:|---:|---:|
| home −1.5 | 0.2050 | 0.2047 | 0.2035 |
| away −1.5 | 0.1939 | 0.1940 | 0.1926 |

- Kalshi is narrowly better from T-12h onward.
- At the flagged T-24h horizon the models score better (0.1953 vs 0.1999 away), consistent with their one-day information advantage there. It is not evidence of edge.
- T-30m / T-10m have too few hourly quotes to read.
- Settlement agreement: 100%.

**Answers**
- **Does DATA_ONLY_V1 beat Kalshi pregame moneyline? No**, at every horizon.
- **Does V2? No.** It is fractionally better than V1 but still behind the market.
- **Does either add information conditional on the market?** Not detectably. In the logistic combination `y ~ logit(market) + logit(model)` the model coefficient is 0.19–0.39 with SE ≈ 0.40–0.46 (z ≤ 0.9 from T-12h on).
- **Are large disagreements predictive?** The OLS slope of `outcome − market` on `model − market` is ≈ 0.3 (SE 0.23): mostly model error, with at most a weak signal indistinguishable from zero. Where V1/V2 exceed the market by more than 10 points (n ≈ 81–86), outcomes beat the market by +0.06–0.07 (SE 0.05); in the mirror bin, by −0.005 to −0.02. Not significant.
- **Market-anchored arm** (MARKET_ANCHORED_V1 0.8 logit blend; not independent): T-60m Brier 0.2440 vs market 0.2442. That is noise-level, and no conclusion is drawn from it.
- **Nothing was tuned on these results.** No ROI analysis was done.

## F. OT fix

| | predicted P(OT) | observed | OT Brier | OT log loss | OT ECE |
|---|---:|---:|---:|---:|---:|
| V1 (nhl-sim-1.1) | 0.1742 | 0.2275 | 0.1786 | 0.5456 | 0.053 |
| V2 (nhl-sim-2.0, special teams) | 0.2126 | 0.2275 | 0.1759 | 0.5368 | 0.015 |

Method selected: score-state x game-time scoring hazards estimated from 39k regulation goals (2021-26), with an
exogenous team-strength offset, simulated in half-minute steps (docs/research/V2_RESEARCH.md). The main mechanism is
tied teams slowing down through the third period (x0.71-0.87); leaders' empty-net surge (x3.6-6.0 in the final two
minutes) *reduces* ties.

Rejected alternatives:
- Team-game fixed-effect hazard fit: produced a spurious, endogenous "trailing teams score more" effect.
- Shared gamma environment: worse total-goals likelihood on both validation seasons.
- Dixon-Coles-style tie inflation: repairs P(OT) by fiat, with nothing for periods or margins.
- Multiplying the tie probability: prohibited, and not needed.

Tradeoffs:
- Moneyline: unchanged.
- Total bias: +0.04 → +0.07.
- Period 2: over-predicted by 0.09 goals.
- Period 3 ties: over-predicted (0.288 vs 0.261).

## G. Goalie model

**Inputs**
- Per-appearance xG faced vs goals allowed, from MoneyPuck shot rows (empty-net and shootout excluded). The starter is the goalie who faced his team's first shot.

**Regression**
- Exponential decay over appearances (half-life 120).
- Shrinkage toward league average with K expected goals. K is chosen on the previous season by out-of-sample likelihood: 1500 (2024-25), 300 (2025-26 and live).
- V1 effectively used K = 60.
- Talent beyond xG is weakly identifiable.

**Workload / rest**
- Back-to-back starts: GA vs expected 0.98 (95 starts) and 1.03 (189 starts). Shrunk to ×0.99–1.02, i.e. no material effect.
- Rest days are recorded, not modelled.

**Starter uncertainty**
- V1's status ladder is kept (CONFIRMED 0.985 / PROBABLE 0.85 / PROJECTED 0.70 / UNKNOWN 0).
- Alternatives now come from the current roster, weighted by start share. The first live dry run caught V1's stale last-season-club alternatives, e.g. Bobrovsky listed as a Florida backup.

**Prospective measurement**
- `python -m nhl_edge.research.goalie_status_eval --archive data/archive`: status accuracy against boxscore starters, PROJECTED→CONFIRMED transitions, and V1/V2 probability movement on confirmation.
- No data until tonight's games settle.

**Historical limitation**
- The historical test uses actual starters, so it is RETROSPECTIVE ORACLE analysis, not a pregame backtest.
- With oracle starters: the V1-style goalie factor slightly *hurts* (ML Brier 0.2420; goalie-sensitive quartile 0.2493). V2 true talent helps slightly (0.2415; 0.2470).

## H. Special teams

**Inputs**
- MoneyPuck situation rows: 5on5, 5on4 (own PP), 4on5 (own PK).
- Live: new archive kind `context/team_games_st`, falling back to the repository's historical rows.

**Method**
- EV + PP (A's PP rate × B's PK rate × A-draws-B-takes minutes) + SH (league rate) + other.
- Heavy shrinkage: a 180-minute prior on PP/PK rates.
- Normalised so a league-average matchup equals V1 (no double counting; tested).

**Held-out effect**
- ML Brier 0.2418 → 0.2417.
- Exact-total log-likelihood −2.1822 → −2.1806.
- O5.5 Brier 0.2470 → 0.2467.
- Special-teams-extreme quartile ML Brier 0.2420 → 0.2413.

Small but consistent, so it stays in the primary V2 arm.

## I. Empty net

**Sample (2021-26)**
- 6,559 games; 2,323 empty-net goals (0.35 per game).
- Empty-net goals by time remaining: 926 in the final minute, 779 at 1–2 min, 361 at 2–3 min.
- 982 extra-attacker goals.
- Pulls detected in 4,147 games; median 2.05 min remaining (10–90%: 5.6 to 0.7 min).

**Estimated behaviour (scoring-rate multipliers)**

| state | 57–58 min | 58–59 min | 59–60 min |
|---|---:|---:|---:|
| Leader by one | ×1.1 | ×3.6 | ×6.0 |
| Leader by two | ×3.2 | ×4.1 | ×5.0 |
| Trailer by one | — | ×1.3 | ×2.3 |

**New mechanism**
- These cells are part of the sim 2.0 hazard table.
- V1's ×4.0 / ×1.8 prior window is not used by V2 (V1 unchanged).

## J. Period model

**Period rates**
- Goals per game: P1 1.77, P2 2.09, P3 2.15.

**Simulation**
- Per-step goals accumulate by period, so P1 + P2 + P3 = regulation on every draw (hypothesis-tested). OT is separate.

**Held-out results**
- P1 tie: predicted 0.342 vs observed 0.344.

**Kalshi support**
- Live rule text for KXNHL1P/2P/3P (incl. TIE), `…PSPREAD` and `…PTOTAL` was reviewed and recorded in docs/KALSHI_MARKET_MAP.md. The simulator maps them exactly.
- They remain **PARTIAL (PARTIAL_RULES_VERIFIED_NO_SETTLEMENT)**, because the settlement engine does not read period line scores.
- **Supported families:** unchanged (game_winner, game_spread, game_total, team_total).
- **Unsupported:** period families (V2 shadow prices only), first goal, player props, futures.

## K. V1 vs V2 overall (identical 2,624 held-out games)

**Result: improves on OT / regulation markets; mixed-to-neutral elsewhere.**

| | V1 | V2 |
|---|---:|---:|
| ML Brier | 0.2419 | 0.2417 |
| ML log loss | 0.6766 | 0.6763 |
| ML ECE | 0.023 | 0.025 (slightly worse) |
| 3-way regulation-win log loss | 0.6712 | 0.6698 |
| Totals exact-likelihood | −2.1813 | −2.1806 |
| O5.5 Brier | 0.2467 | 0.2467 |
| Puck line | equal | equal |
| Team totals | equal | equal |

## L. Tonight's opening-night shadow (true timestamp 2026-09-29T15:40:38Z, read-only run 36591929873 on archive `eb5c565`)

RESEARCH ONLY. Not recommendations.

| game | goalies (home / away) | V1 P(home) | V2 P(home) | market mid | V1 exp total | V2 exp total | market total (strike nearest 50%) | largest V1/V2 disagreement |
|---|---|---:|---:|---:|---:|---:|---|---|
| FLA @ CAR | PROJECTED Bussi / PROJECTED Markstrom | 0.651 | 0.611 | 0.545 | 6.52 | 6.49 | o6.5 @ 0.460 | KXNHLGAME-…-CAR −0.040 |
| MTL @ TOR | PROJECTED Bobrovsky / PROJECTED Dobes | 0.462 | 0.498 | 0.495 | 6.58 | 6.31 | o6.5 @ 0.490 | KXNHLTEAMTOTAL-…-MTL4 −0.054 |
| NYR @ BOS | CONFIRMED Swayman / PROJECTED Shesterkin | 0.545 | 0.526 | 0.495 | 5.83 | 6.16 | o5.5 @ 0.545 | KXNHLTOTAL-…-7 +0.058 |
| VAN @ EDM | CONFIRMED Jarry / PROJECTED Lankinen | 0.645 | 0.634 | 0.725 | 6.63 | 6.53 | o6.5 @ 0.515 | KXNHLTOTAL-…-8 −0.021 |
| CHI @ VGK | PROJECTED Hart / PROJECTED Knight | 0.626 | 0.672 | 0.705 | 6.04 | 6.25 | o5.5 @ 0.555 | KXNHLTEAMTOTAL-…-VGK4 +0.065 |

V2 P(OT) is 0.20–0.23 per game (V1 0.16–0.18). Files: `docs/shadow/20260929T154038Z_36591929873/` (slate, packet,
`predictions_v2` rows, provenance). __SECOND_SHADOW__

## M. Tests

**Tests**
- __TESTS__ passed; `ruff check src tests scripts` clean.
- 28 new tests covering:
  - sim 2.0 invariants (hypothesis): periods sum to regulation, OT/SO semantics, ladders.
  - Hazard estimator: flat on state-free data.
  - Empty-net and tie mechanisms.
  - Special teams: V1 equivalence, no double counting, shrinkage, cutoff.
  - Goalie point-in-time, rest/B2B, and the status-ladder mixture.
  - Kalshi pagination and merge, short-code / Utah joining, horizon cutoff (no future candle), missing quotes, cents/dollars payloads.
  - Period pricing coherence.
  - V1 identical with V2 on/off; V2 failure isolation.
  - Goalie-status evaluator.

**Test fix**
- One pre-existing test was made deterministic: the rerun-immutability test depended on the wall-clock second.

## N. Authority

**ALL NHL MODEL FAMILIES REMAIN RESEARCH_ONLY. NO BETTING AUTHORITY WAS CREATED. NO BETS WERE PLACED.**
DATA_ONLY_V2 is SHADOW: it never gates a contract. kalshi-bet-router was not modified.

## O. Remaining limitations

1. **Worker coverage.** The worker's own V2 rows start ~22:27Z (generation 3), so FLA@CAR has V2 only from the read-only shadow runs, not from the worker archive.
2. **Goalies.**
   - Historical goalie evaluation is oracle-style.
   - Live goalie workload uses history through 2025-26 only; current-season appearances are not yet ingested.
   - PROJECTED/CONFIRMED confidences are V1's priors until prospective data accumulates.
3. **sim 2.0 fit.**
   - The hazard table was trained on 2021-25. It over-predicts P2 goals and P3 ties slightly in 2024-26.
   - Total bias is +0.07.
   - The OT winner model is V1's strength-shrink prior (not re-estimated).
4. **Period markets.** Unsettleable here (no period settlement), so they stay PARTIAL.
5. **Out of scope today.** Injuries and line combinations remain unmodelled.
6. **Market benchmark.** One season only (Kalshi NHL game history starts in the 2025 playoffs); candle midpoints are not executable prices; spreads use hourly candles only; no settled team-total or period history exists; ~1% of candle fetches were rate-limited gaps; the walk-forward model uses information through the previous day, which flags the T-24h horizon.

## P. RUN NHL later today

**Use:** BOTH, with V1 as the reference and V2 as a labelled second opinion. Neither is a recommendation.
- The latest packet (`data-archive: slates/latest/packet.json`) has a `v2_shadow` block from generation 3 onward (~22:27Z).
- Before that, read `docs/shadow/<stamp>/packet.json` on the research branch.

**Prefer V2's numbers for:**
- OT / regulation-tie / 3-way contracts (clearly better calibrated).
- Period markets, as research context only (V1 has none; settlement is not built).

**Treat as equivalent:** moneyline, totals, puck lines and team totals. V2 did not beat V1 there.

**Human review:**
- Flag any V1/V2 disagreement ≥ 0.04 (`flagged_for_review`).
- Do not choose V2 because it is newer.

History says the Kalshi price is the better forecaster; treat any model-vs-market gap as more likely model error than edge. The market is the benchmark.
