# Rules replay 2026-09-30 — DIAGNOSTIC ONLY (RESEARCH_ONLY)

_DIAGNOSTIC ONLY. Replayed at each game's final production decision instant on pregame data; no hindsight substitution. Realized P/L covers settled contracts only. This is NOT evidence that the new rules are better: it verifies that the architecture behaves as intended._

| card | bets | stake | player props | largest thesis share | mean abs phi | settled | settled stake | realized P/L | ROI (settled) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| OLD (nominal optimiser card) | 12 | 142.47 | 10 | 0.140 | 0.070 | 12 | 142.47 | -33.35 | -0.23 |
| NEW optimiser card (nominal) | 12 | 142.47 | 10 | 0.140 | 0.070 | 12 | 142.47 | -33.35 | -0.23 |
| NEW FUNDED research ($) | 5 | 18.00 | 3 | 0.278 | 0.178 | 5 | 18.00 | -11.00 | -0.61 |

shadow-only (on the optimiser card, not funded): 7 · removed by the expression-fidelity rule: 0 · removed by the market-disagreement gate: 2

## 2026020006 · cutoff 2026-09-30T23:20:00Z


| card | bet | p model | p adj | mid | EV adj | fidelity (capture) | nominal $ | research | result | P/L (OLD nominal / NEW research) |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|
| OLD | KXNHLGOAL-26SEP30PITPHI-PHIPMARTONE94-1|no | 0.776 | 0.755 | 0.695 | +0.04 | DIRECT (0.884) | 20.000 | - | WON | +7.98 |
| OLD | KXNHLGOAL-26SEP30PITPHI-PITCDEWAR19-1|yes | 0.157 | 0.144 | 0.105 | +0.03 | FRAGILE (0.257) | 7.060 | - | LOST | -7.06 |
| OLD | KXNHLGOAL-26SEP30PITPHI-PHISCOUTURIER14-1|yes | 0.179 | 0.166 | 0.125 | +0.03 | FRAGILE (0.274) | 7.670 | - | LOST | -7.67 |
| OLD | KXNHLGOAL-26SEP30PITPHI-PITRRAKELL67-1|yes | 0.327 | 0.311 | 0.265 | +0.03 | FRAGILE (0.495) | 9.510 | - | LOST | -9.51 |
| NEW | KXNHLGOAL-26SEP30PITPHI-PHIPMARTONE94-1|no | 0.776 | 0.755 | 0.695 | +0.04 | DIRECT (0.884) | 20.000 | FUNDED_RESEARCH $5 | WON | +2.00 |
| NEW | KXNHLGOAL-26SEP30PITPHI-PITCDEWAR19-1|yes | 0.157 | 0.144 | 0.105 | +0.03 | FRAGILE (0.257) | 7.060 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |
| NEW | KXNHLGOAL-26SEP30PITPHI-PHISCOUTURIER14-1|yes | 0.179 | 0.166 | 0.125 | +0.03 | FRAGILE (0.274) | 7.670 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |
| NEW | KXNHLGOAL-26SEP30PITPHI-PITRRAKELL67-1|yes | 0.327 | 0.311 | 0.265 | +0.03 | FRAGILE (0.495) | 9.510 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |

## 2026020007 · cutoff 2026-10-01T01:50:00Z


| card | bet | p model | p adj | mid | EV adj | fidelity (capture) | nominal $ | research | result | P/L (OLD nominal / NEW research) |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|
| OLD | KXNHLGOAL-26SEP30LACOL-COLNMACKINNON29-1|no | 0.644 | 0.622 | 0.555 | +0.04 | DIRECT (0.828) | 19.920 | - | LOST | -19.92 |
| OLD | KXNHLAST-26SEP30LACOL-LAMZUCCARELLO36-1|no | 0.792 | 0.709 | 0.665 | +0.02 | DIRECT (0.879) | 19.920 | - | WON | +9.14 |
| OLD | KXNHLGOAL-26SEP30LACOL-LAALAFERRIERE14-1|yes | 0.251 | 0.239 | 0.205 | +0.02 | FRAGILE (0.413) | 5.390 | - | LOST | -5.39 |
| OLD | KXNHLGAME-26SEP30LACOL-COL|no | 0.419 | 0.386 | 0.345 | +0.02 | STRUCTURAL (1.000) | 4.760 | - | LOST | -4.76 |
| NEW | KXNHLGOAL-26SEP30LACOL-COLNMACKINNON29-1|no | 0.644 | 0.622 | 0.555 | +0.04 | DIRECT (0.828) | 19.920 | FUNDED_RESEARCH $5 | LOST | -5.00 |
| NEW | KXNHLAST-26SEP30LACOL-LAMZUCCARELLO36-1|no | 0.792 | 0.709 | 0.665 | +0.02 | DIRECT (0.879) | 19.920 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED $0 | WON | +0.00 |
| NEW | KXNHLGOAL-26SEP30LACOL-LAALAFERRIERE14-1|yes | 0.251 | 0.239 | 0.205 | +0.02 | FRAGILE (0.413) | 5.390 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP $0 | LOST | +0.00 |
| NEW | KXNHLGAME-26SEP30LACOL-COL|no | 0.419 | 0.386 | 0.345 | +0.02 | STRUCTURAL (1.000) | 4.760 | FUNDED_RESEARCH $2 | LOST | -2.00 |

## 2026020008 · cutoff 2026-09-30T23:20:00Z


| card | bet | p model | p adj | mid | EV adj | fidelity (capture) | nominal $ | research | result | P/L (OLD nominal / NEW research) |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|
| OLD | KXNHLGOAL-26SEP30NYITOR-TORTBLUEGER73-1|yes | 0.130 | 0.119 | 0.085 | +0.02 | FRAGILE (0.212) | 6.270 | - | LOST | -6.27 |
| OLD | KXNHLAST-26SEP30NYITOR-TORAMATTHEWS34-1|no | 0.694 | 0.645 | 0.595 | +0.03 | DIRECT (0.826) | 17.260 | - | WON | +10.72 |
| OLD | KXNHLGAME-26SEP30NYITOR-TOR|no | 0.520 | 0.481 | 0.435 | +0.02 | STRUCTURAL (1.000) | 12.480 | - | LOST | -12.48 |
| OLD | KXNHLSAVE-26SEP30NYITOR-NYIISOROKIN30-25|no | 0.626 | 0.528 | 0.475 | +0.02 | DIRECT (0.994) | 12.230 | - | WON | +11.87 |
| NEW | KXNHLGOAL-26SEP30NYITOR-TORTBLUEGER73-1|yes | 0.130 | 0.119 | 0.085 | +0.02 | FRAGILE (0.212) | 6.270 | FUNDED_RESEARCH $2 | LOST | -2.00 |
| NEW | KXNHLAST-26SEP30NYITOR-TORAMATTHEWS34-1|no | 0.694 | 0.645 | 0.595 | +0.03 | DIRECT (0.826) | 17.260 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED $0 | WON | +0.00 |
| NEW | KXNHLGAME-26SEP30NYITOR-TOR|no | 0.520 | 0.481 | 0.435 | +0.02 | STRUCTURAL (1.000) | 12.480 | FUNDED_RESEARCH $4 | LOST | -4.00 |
| NEW | KXNHLSAVE-26SEP30NYITOR-NYIISOROKIN30-25|no | 0.626 | 0.528 | 0.475 | +0.02 | DIRECT (0.994) | 12.230 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED $0 | WON | +0.00 |
