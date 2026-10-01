# Card construction as a portfolio of game theses: a portable abstraction

NHL implements this first because it already has a true joint simulation (`docs/research/THESIS_ENGINE.md`). The same
philosophy should later carry to MLB, NFL, NBA, CFB and soccer. **No other repository was edited in this work.** This
note is the interface those repos can copy.

```
GAME / EVENT DISTRIBUTION   per-draw outcome arrays from ONE joint model (or a scenario tree with weights)
  -> THESIS LAYER           deterministic script labels (partition) + named thesis events (binary, with categories)
  -> MARKET EXPRESSION      per contract side: per-draw settlement indicator, executable price, fee, mid
  -> JOINT OUTCOME MATRIX   pairwise P(A), P(B), P(A and B), conditionals, phi, script overlap, relationship labels
  -> PORTFOLIO              max E[log wealth] on the draws with confidence-adjusted returns, exposure caps,
                            cardinality cap; A/B/C comparison
  -> CARD COMPLETION GATE   18 required fields per bet (UNKNOWN must be explained); JOINT CARD CHECK for multi-bet events
  -> DECISION LOG + POSTMORTEM  thesis / expression / price / model / portfolio results kept separate
```

## The contracts between layers (NHL names in brackets)

| layer | input | output | sport-specific part |
|---|---|---|---|
| distribution | the sport's simulator | `features`: dict of per-draw arrays (`DrawFeatures`) + `from_actual(official result)` with the same fields | everything: which quantities exist (runs by inning, drives, possessions, xG) |
| scripts | features | integer label per draw (primary partition), named dimensions and overlays (`thesis.scripts`) | the taxonomy and its a-priori thresholds (frozen from completed seasons, never a slate) |
| thesis events | features | list of `ThesisEvent(key, label, category, team, mask)` (`thesis.events`) | the event list ("starter goes 6+ innings", "rushing game script", "both teams score") |
| expressions | contracts + the draw | `Bet(bet_id, side, y[draws], p, price, fee, mid, team, meta)`; fail closed when there is no outcome vector (`thesis.outcomes`) | contract-to-indicator mapping, reusing each repo's own pricer so semantics cannot drift |
| mapping | bets, labels, events | contributions (sum exactly to p), concentration, breadth, phi, primary / secondary / failure thesis (`thesis.mapping`) | none |
| joint | shortlisted bets | pair statistics + labels (`thesis.joint`) | none |
| reliability | evaluation artifacts + PIT-safe prospective ledger | per-family label (+ per-bet calibration-bucket flags) (`thesis.reliability`) | artifact paths and families |
| confidence | p, mid, label, benchmark | p_adj = mid + k (p − mid), large-gap cap (`thesis.expression`) | the k table can stay; its evidence differs |
| portfolio | bets, p_adj, theses, duplicates | stakes, metrics on the simulated P/L (`thesis.portfolio`) | caps; cross-event independence (true for different games) |
| gate | card entries, joint matrices | PASS / FAIL with reasons (`thesis.card`) | none |

Everything except the first two rows and the reliability artifact paths is sport-agnostic and could move to a shared
package unchanged. The NHL implementation takes no hockey-specific input below the features.

## Sports without a true joint simulation

- **Scenario trees.** Enumerate a small set of interpretable scenarios (e.g. NFL: "favourite controls early / trailing
  team passes"), give each a probability and, per scenario, a conditional probability for every contract. Draw
  scenario and outcomes (conditionally independent within a scenario) to produce synthetic draws, then run the same
  layers. The labels are the scenarios themselves.
- **Empirical copulas.** Estimate pairwise dependence between contract outcomes from history (same-game pairs) and
  sample correlated Bernoulli draws matching the marginals. This handles pairs but not higher-order structure.
- **Confidence.** Both approaches carry less information than a structural simulation. Their reliability labels should
  start no higher than EVIDENCE_MIXED, their joint-matrix labels should be shown as approximate, and their DUPLICATIVE
  threshold should be lowered (dependence is estimated, not structural).
- **What never changes.** Positive EV at the executable price is necessary for every bet. A hedge is never added for
  its own sake. Correlated bets share a budget. The market is the benchmark. Disagreement increases scrutiny. One slate
  is never evidence for tuning.
