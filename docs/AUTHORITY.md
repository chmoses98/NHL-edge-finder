# Authority

**ALL NHL MODEL FAMILIES ARE RESEARCH_ONLY. NO BETTING AUTHORITY EXISTS. NO BETS ARE PLACED.**

## Ladder

`RESEARCH_ONLY` -> `SHADOW` -> `LIMITED` -> `TRUSTED` (`schemas/prediction.Authority`). Every prediction row is
written with `authority = RESEARCH_ONLY` by `workflows/simulate`. `evaluation/authority.eligibility` reports what the
prospective evidence would support (SHADOW at n >= 100 settled pregame predictions; LIMITED at n >= 300 with Brier
skill vs the market > 0, mean CLV > 0 and ECE < 0.05; TRUSTED at n >= 1000 with a bootstrap-CI lower bound > 0).
Eligibility is informational. It never changes what is written.

## Rules

1. Backtests never count toward authority. Only rows with `pregame == True` from live capture count.
2. The market is the benchmark. If `MARKET_BASELINE` beats `DATA_ONLY_V1`, that is the finding and it is reported.
3. `MARKET_ANCHORED_V1` uses the market as a prior and is never independent evidence.
4. Promotion is a separate explicit owner decision recorded in this file, with the evidence report linked.
5. Positive fee-adjusted edge rows in `slate.md` are research observations, not recommendations.

## Router isolation (must never change by accident)

`kalshi-bet-router` has no `Sport.NHL`, no destination profile, and lists hockey as out of scope. This repository
ships no importer scripts (`import_routed_wagers.py` etc.), no wager ledger branch, no `kalshi-router/*` branches,
and no `{sport}.json` payload handling. Adding any of those is an authority change and requires the owner's decision.

## What would have to change to grant authority

- An `Authority` value other than `RESEARCH_ONLY` written in `workflows/simulate.py` (currently hard-coded).
- A documented decision here citing `eval/report.json` with sample sizes and dates.
- Router-side changes owned by the router repository, never by this one.
