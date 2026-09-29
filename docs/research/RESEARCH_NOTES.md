# Research notes

> The market is the benchmark. Negative results are recorded here as plainly as positive ones.

## 2026-09-29 foundation build

- Prospective collection starts opening night with five games. First evaluation rows appear after settlement.
- Historical walk-forward for DATA_ONLY_V1 is produced by `history.yml` into `docs/research/WALK_FORWARD_V1.md`
  (MoneyPuck 2022+ game logs, NHL official results, goalie factor fixed at 1.0, no market data available for the
  same games). If that file is absent the run has not completed yet.
- No historical Kalshi NHL price series was ingested tonight, so no historical DATA_ONLY vs market comparison
  exists yet; the prospective archive is the only apples-to-apples comparison and it starts now.

## Policy

- Walk-forward only (train past, test future). No random splits.
- No tuning to make historical scores look better; constants in `features/ratings.py` and `sim/engine.py` change
  only with a version bump and a written reason.
- Small samples prove nothing; report n with every number.

## Roadmap (ranked by expected value per unit of work)

1. Historical Kalshi NHL settled markets + candles (the NBA `kalshi/history.py` pattern) to benchmark the market on
   past seasons.
2. Explicit special teams: penalty rates x PP/PK efficiency from MoneyPuck 5on4/4on5 situations.
3. Goalie true talent and workload (daily curve from goalie game logs; rest days; back-to-back starts).
4. Empty-net and score-effect calibration from play-by-play (landing scoring flags empty-net goals); Dixon-Coles
   style tie correction, measured against P(OT) calibration.
5. Injury and line-combination impact (ESPN injuries archived; DailyFaceoff lines page not yet ingested).
6. Period-level simulation for period markets; player shot/goal props.
