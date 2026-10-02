# Preregistered research hypotheses (NHL)

> Registered 2026-10-02, BEFORE the evidence that would test them exists. Each names the data, the metric, the minimum
> sample, and the decision rule in advance. Until a test is run and passes, nothing about the model changes: no
> coefficient, probability, threshold or calibration is touched because of one or two slates (2026-09-30, 2026-10-01).
> Results are reported here whether they confirm or refute the hypothesis.

## H1. Assists / points compression makes large NO-side disagreements on star playmakers model error

- **Background (frozen evidence):** held-out 2025-26 calibration of `assists 1+` and `points 1+` is S-shaped
  (`docs/research/thesis_engine/model_audit.json` D; z up to ±5.8). Stars are under-predicted, depth players
  over-predicted. A model NO on a star's assist at a large gap to the market (e.g. McDavid 1+ assist NO, model 0.476
  vs mid 0.305 on 2026-10-01) is exactly the direction of the known bias.
- **Test data:** prospective `evaluations_player` rows, last pregame observation per (game, ticker), families
  `player_assists` / `player_points`, |p_player − p_market| ≥ 0.10.
- **Metric:** paired Brier difference (model − Kalshi mid) on those rows, split by the side the model favours.
- **Minimum sample:** 300 unique wagers from ≥ 30 games.
- **Decision rule:** if the model's Brier is worse than the mid's with a one-sided 95% bootstrap interval (games
  resampled) excluding 0, the disagreement-gate warning for these families stays and a recalibration study (walk-forward,
  held-out season) is opened. If not, the family's KNOWN_CALIBRATION_CONCERNS entry is reviewed with that evidence.

## H2. Fragile expressions under-perform structural / direct ones at similar adjusted value

- **Claim:** FINAL_CARD_UNIQUE bets in `fidelity_class` FRAGILE realise a lower ROI relative to their entry adjusted EV
  than STRUCTURAL / DIRECT bets.
- **Test data:** `eval/report_thesis.json` FINAL_CARD_UNIQUE, EXPRESSION.by_fidelity_class, nominal-card stakes.
- **Metric:** realised P/L minus entry expected P/L (adjusted), per dollar staked, by class.
- **Minimum sample:** 200 final-card bets per compared class.
- **Decision rule:** a difference whose 90% bootstrap interval excludes 0 justifies reviewing the one-tick similarity
  band (`thesis.engine.SIMILAR_EDGE`). The band is NOT changed before that.

## H3. Large player-prop disagreements with the market are mostly model error (prospective replication)

- **Background:** in the historical T-10m player benchmark the 279 rows where the model sat 10+ points below the mid
  settled 3.0 points below the mid (`thesis.expression` docstring). This motivated `K_LARGE_GAP` and the new
  MARKET_DISAGREEMENT_REVIEW gate.
- **Test data:** prospective `evaluations_player`, last pregame observation per wager, |gap| ≥ 0.10.
- **Metric:** mean (outcome − mid) and mean (outcome − model) per gap direction.
- **Minimum sample:** 300 unique wagers.
- **Decision rule:** if the outcome sits closer to the model than to the mid with a 95% interval, the gate's corroboration
  requirement is reviewed; otherwise it stays.

## H4. Muted score effects on shot volume understate result-saves dependence

- **Background:** `docs/research/THESIS_ENGINE.md` 11B (history: tied +1.13 / −1 −1.24; simulation about a quarter of that).
- **Test:** a margin / trailing-state term in the saves layer, fit on 2021-24 and validated walk-forward on 2025-26
  (saves ladder Brier and the result × saves joint calibration). Prospective NHL results are NOT used to fit it.
- **Decision rule:** adopt only with a version bump if held-out Brier improves and nothing else degrades.

## H5. Settlement completeness

- **Claim:** after the 2026-10-02 repair every scheduled game reaches COMPLETE in `STATUS_settle.json` within 6 hours of
  its scheduled end, with no manual action.
- **Metric:** time from scheduled start + 3h to the first COMPLETE backlog state, per game, over the next 100 games.
- **Decision rule:** any game exceeding 6 hours is investigated as an infrastructure defect.
