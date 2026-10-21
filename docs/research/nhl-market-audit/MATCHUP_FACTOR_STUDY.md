# Matchup-factor study (Phase D)

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

**Question.** Do timestamp-safe, opponent-adjusted hockey factors add information beyond the Kalshi price?

**Method (`market_audit/matchup_study.py`, declared in git before any result was computed).** Independent challenger features from games dated strictly before the game: ridge opponent-adjusted
5v5 xG-rate differential and expected total (refit daily, 45-day half-life, MoneyPuck team-games), finishing, power-play/penalty-kill edge, rest, back-to-backs, timezone hours crossed.
Test: `y ~ offset(logit(mid at T-60m)) + beta * x`, FIT on the chronologically first 60% of games, SCORED once on the last 40% (never refit). Starting-goalie identity is deliberately excluded: the archive
cannot say when the starter became known, so any goalie feature risks leaking.

| block | features | fit games | hold-out games | in-sample z | block Wald p | hold-out change in log loss vs market | 95% CI (games) |
|---|---|---|---|---|---|---|---|
| W1_oa_xg | oa_xg_diff | 780 | 519 | oa_xg_diff:0.33 | 0.745 | -0.00110 | [-0.00409, 0.00189] |
| W2_rest_travel | rest_diff, b2b_home, b2b_away, tz_away | 780 | 519 | rest_diff:-2.02, b2b_home:-1.01, b2b_away:2.41, tz_away:-0.38 | 0.130 | 0.00695 | [-0.00088, 0.01489] |
| W3_finishing_specialteams | fin_diff, pp_edge | 780 | 519 | fin_diff:-1.02, pp_edge:-1.30 | 0.299 | 0.00148 | [-0.00421, 0.00696] |
| W4_all | oa_xg_diff, rest_diff, b2b_home, b2b_away, tz_away, fin_diff, pp_edge | 780 | 519 | oa_xg_diff:-0.02, rest_diff:-1.97, b2b_home:-0.89, b2b_away:2.40, tz_away:-0.37, fin_diff:-1.02, pp_edge:-1.23 | 0.231 | 0.00852 | [-0.00116, 0.01831] |
| T1_oa_exp_total | oa_exp_total | 673 | 525 | oa_exp_total:-0.15 | 0.877 | -0.00015 | [-0.00143, 0.00116] |
| T2_b2b_travel | b2b_home, b2b_away, tz_away | 673 | 525 | b2b_home:-1.43, b2b_away:-1.17, tz_away:-0.73 | 0.200 | 0.00073 | [-0.00331, 0.00476] |
| T3_all | oa_exp_total, b2b_home, b2b_away, tz_away | 673 | 525 | oa_exp_total:-0.13, b2b_home:-1.44, b2b_away:-1.15, tz_away:-0.72 | 0.319 | 0.00079 | [-0.00314, 0.00476] |

Negative change in log loss = the feature block improved on the market alone. **No block helps out of sample; every confidence interval includes zero**, and the rest/travel block, which shows an
in-sample coefficient near |z|=2, makes the hold-out slightly worse (the signature of overfitting a 780-game fit window). The market already prices opponent-adjusted shot quality, rest and travel to within this test's
resolution. This is consistent with the model audit: the production model is built from the same inputs and adds nothing either.

Limits: one season of market prices; features are public and standard; a stronger or non-public input (confirmed lineups, injuries timed against the repricing instant, goalie confirmation timing) is **untestable**
here because the archive does not timestamp when that information reached the market.
