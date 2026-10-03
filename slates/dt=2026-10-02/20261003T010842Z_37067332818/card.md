# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T01:08:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +10.68 | +2.59 | +14.81 | 0.565 | -29.73 | -33.41 | 21.08 |
| B thesis-diversified (joint) ← optimiser card | 27.65 | +9.99 | +5.23 | +0.28 | 0.646 | -27.65 | -27.65 | 44.82 |
| C best expression per thesis | 49.06 | +8.79 | +3.11 | +1.06 | 0.736 | -25.33 | -25.33 | 27.07 |
| R FUNDED research stakes | 2.00 | +1.06 | +0.73 | -2.00 | 0.114 | -2.00 | -2.00 | 0.00 |

## ANA @ VGK  ·  10000 joint draws  ·  358 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.645 / away 0.355

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_ANA_win | p_overtime | goals | shots VGK/ANA | VGK/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.66 | 0.34 | 0.00 | 6.03 | 28.1/28.2 | 25.3/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.54 | 0.46 | 0.50 | 5.97 | 28.0/28.1 | 24.8/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.66 | 0.34 | 0.00 | 9.35 | 29.5/29.6 | 24.3/22.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.076 | 0.62 | 0.38 | 0.00 | 6.04 | 22.5/33.4 | 30.2/18.7 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.48 | 0.52 | 0.47 | 5.9 | 22.5/33.5 | 30.2/19.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.061 | 0.70 | 0.30 | 0.00 | 6.02 | 32.6/22.3 | 19.7/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 7 | 0.114 | 0.102 | +0.040 | +0.027 | $6.20 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 18 | 0.233 | 0.218 | +0.043 | +0.028 | $8.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ assists YES | 23 | 0.363 | 0.270 | +0.121 | +0.028 | $6.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Braeden Bowman: 1+ goals YES | 15 | 0.195 | 0.183 | +0.036 | +0.024 | $6.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (22.68 vs 11.06 bp); despite a smaller raw edge (+0.040 vs +0.043/contract); relationships: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (11.06 vs 9.14 bp); despite a smaller raw edge (+0.043 vs +0.121/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (11.06 vs 9.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: ANA offense suppressed (<= 2 goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-VGKRANDERSSON4-1|yes; why: higher confidence-adjusted growth (9.14 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3325): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4029): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.3145): highest fidelity KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT02ANAVGK-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.176)
- KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.241)
- KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 45% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.292)
- KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3145, phi -0.174)

portfolios: A EV +10.68 (adj +2.59) on $50.00, P(profit) 0.5649, adj growth 21.1 bp · B EV +9.99 (adj +5.23) on $27.65, P(profit) 0.6464, adj growth 44.8 bp · C EV +8.79 (adj +3.11) on $49.06, P(profit) 0.7364, adj growth 27.1 bp · R EV +1.06 (adj +0.73) on $2.00, P(profit) 0.1141, adj growth 23.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02ANAVGK-VGK|no == KXNHLGAME-26OCT02ANAVGK-ANA|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
