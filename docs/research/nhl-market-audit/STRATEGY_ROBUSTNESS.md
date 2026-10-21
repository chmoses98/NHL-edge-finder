# Strategy robustness and executability

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

Fees: Kalshi's quadratic taker schedule `0.07 p (1-p)` (reproduces the router's recorded fee to the cent). Slippage: +1c / +2c on the ask. Timing: decisions at T-60, T-10 and T-0 minutes.
Each block: ROI before fees, then net of fees at three slippage levels. Only the five full-game one-sided strategies are shown (they exist in both tiers).

### HIST_ALL M1

| min to start | pre-fee ROI | net, no slippage | net, +1c | net, +2c |
|---|---|---|---|---|
| 60 | -4.1% | -7.2% | -8.9% | -10.6% |
| 0 | -5.3% | -8.3% | -10.0% | -11.6% |

### HIST_ALL M2

| min to start | pre-fee ROI | net, no slippage | net, +1c | net, +2c |
|---|---|---|---|---|
| 60 | +0.0% | -3.2% | -5.0% | -6.7% |
| 0 | -0.9% | -4.0% | -5.8% | -7.5% |

### HIST_ALL M3

| min to start | pre-fee ROI | net, no slippage | net, +1c | net, +2c |
|---|---|---|---|---|
| 60 | -2.9% | -3.7% | -4.7% | -5.7% |
| 0 | -3.6% | -4.4% | -5.4% | -6.4% |

### HIST_ALL M4

| min to start | pre-fee ROI | net, no slippage | net, +1c | net, +2c |
|---|---|---|---|---|
| 60 | -1.5% | -2.2% | -3.1% | -4.0% |
| 0 | -1.5% | -2.2% | -3.2% | -4.0% |

### HIST_ALL M5

| min to start | pre-fee ROI | net, no slippage | net, +1c | net, +2c |
|---|---|---|---|---|
| 60 | -1.8% | -3.0% | -4.1% | -5.2% |
| 0 | -2.8% | -3.9% | -5.0% | -6.0% |

### LIVE M1

| min to start | pre-fee ROI | net, no slippage | net, +1c | net, +2c |
|---|---|---|---|---|
| 60 | -2.2% | -5.4% | -7.2% | -9.0% |
| 10 | -2.5% | -5.7% | -7.5% | -9.2% |
| 0 | -2.2% | -5.4% | -7.2% | -8.9% |

### LIVE M2

| min to start | pre-fee ROI | net, no slippage | net, +1c | net, +2c |
|---|---|---|---|---|
| 60 | +0.1% | -3.1% | -4.9% | -6.6% |
| 10 | +0.5% | -2.8% | -4.6% | -6.3% |
| 0 | +0.1% | -3.2% | -5.0% | -6.7% |

### LIVE M3

| min to start | pre-fee ROI | net, no slippage | net, +1c | net, +2c |
|---|---|---|---|---|
| 60 | +0.2% | -0.6% | -1.6% | -2.7% |
| 10 | +0.4% | -0.4% | -1.5% | -2.5% |
| 0 | +0.2% | -0.6% | -1.6% | -2.6% |

### LIVE M4

| min to start | pre-fee ROI | net, no slippage | net, +1c | net, +2c |
|---|---|---|---|---|
| 60 | +1.3% | +0.6% | -0.2% | -1.0% |
| 10 | +1.0% | +0.4% | -0.4% | -1.2% |
| 0 | +0.7% | +0.1% | -0.8% | -1.5% |

### LIVE M5

| min to start | pre-fee ROI | net, no slippage | net, +1c | net, +2c |
|---|---|---|---|---|
| 60 | -1.9% | -3.1% | -4.2% | -5.3% |
| 10 | -1.9% | -3.1% | -4.2% | -5.3% |
| 0 | -1.9% | -3.1% | -4.2% | -5.3% |


## Liquidity: walking the archived order book (LIVE, four families with depth)

| strategy | games | ROI at the touch | 50 contracts: full fills | ROI walking the book | extra cost | 200 contracts: full fills | ROI walking the book | extra cost |
|---|---|---|---|---|---|---|---|---|
| M1 | 146 | -5.6% | 100.0% | -5.9% | 0.21c | 100.0% | -6.0% | 0.21c |
| M2 | 146 | -2.9% | 100.0% | -3.1% | 0.1c | 100.0% | -3.2% | 0.11c |
| M3 | 149 | -0.8% | 100.0% | -0.8% | 0.04c | 100.0% | -0.9% | 0.07c |
| M4 | 147 | +0.5% | 99.3% | +0.4% | 0.07c | 99.2% | +0.4% | 0.12c |
| M5 | 149 | -3.0% | 100.0% | -3.1% | 0.06c | 100.0% | -3.1% | 0.07c |
| M7 | 148 | -2.0% | 100.0% | -2.2% | 0.07c | 100.0% | -2.3% | 0.15c |
| M8 | 148 | -7.0% | 100.0% | -7.1% | 0.04c | 100.0% | -7.3% | 0.14c |

Orders of 50 and 200 contracts (about $25 and $100) fill fully in essentially every case and cost only ~0.04-0.2c more than the touch. **Liquidity is not the binding constraint at research stake sizes; the spread and the fee are.**
Depth for periods, overtime, first-10-minutes and props was never captured, so executability there is unobserved.

## Power: how many independent games to detect an edge

| strategy | edge 1% | edge 2% | edge 3% | edge 5% | edge 10% |
|---|---|---|---|---|---|
| M1 | 49,342 | 12,336 | 5,483 | 1,974 | 494 |
| M2 | 48,117 | 12,030 | 5,347 | 1,925 | 482 |
| M3 | 7,776 | 1,944 | 864 | 312 | 78 |
| M4 | 7,455 | 1,864 | 829 | 299 | 75 |
| M5 | 5,541 | 1,386 | 616 | 222 | 56 |

## Summary

Before any fee, most strategies are at or below zero; the best live case is about +1 point. After the fee, essentially all are negative, and one cent of slippage deletes the best case. Changing the decision time
between T-60 and T-0 changes almost nothing. Model-uncertainty sensitivity is built into the engine (uncertainty floor, V1/V2 disagreement widening); see EXPRESSION_ENGINE_SPEC.md.
