# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-09T01:08:12Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +7.79 | +1.78 | +13.67 | 0.620 | -22.05 | -33.62 | 14.94 |
| B thesis-diversified (joint) ← optimiser card | 29.29 | +5.93 | +3.87 | -2.18 | 0.234 | -29.29 | -29.29 | 33.11 |
| C best expression per thesis | 35.78 | +7.11 | +2.76 | +9.11 | 0.560 | -21.84 | -35.78 | 23.73 |
| R FUNDED research stakes | 5.00 | +0.29 | +0.18 | +2.51 | 0.704 | -5.00 | -5.00 | 0.00 |

## TOR @ VGK  ·  10000 joint draws  ·  448 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.601 / away 0.400

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TOR_win | p_overtime | goals | shots VGK/TOR | VGK/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.153 | 0.76 | 0.24 | 0.00 | 5.99 | 34.0/21.4 | 19.1/29.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.59 | 0.41 | 0.48 | 5.92 | 34.3/21.7 | 18.7/30.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.68 | 0.32 | 0.00 | 6.04 | 28.4/27.7 | 25.0/24.0 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.105 | 0.77 | 0.23 | 0.00 | 9.28 | 36.0/23.0 | 18.9/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.47 | 0.49 | 5.96 | 28.4/27.7 | 24.5/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.73 | 0.27 | 0.00 | 9.35 | 30.1/29.2 | 24.6/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Parker Wotherspoon: 1+ goals YES | 3 | 0.054 | 0.046 | +0.022 | +0.015 | $3.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.088 | 0.080 | +0.024 | +0.016 | $3.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 8 | 0.112 | 0.103 | +0.027 | +0.017 | $4.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 65 | 0.704 | 0.690 | +0.038 | +0.024 | $18.05 | FUNDED_RESEARCH | $5 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Parker Wotherspoon: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: VGK offense suppressed (<= 2 goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (8.88 vs 3.56 bp); despite a smaller raw edge (+0.024 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKPWOTHERSPOON29-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: VGK offense suppressed (<= 2 goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (8.37 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT08TORVGK-VGKPWOTHERSPOON29-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: TOR offense suppressed (<= 2 goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no; why: Player prop expression KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.84 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT08TORVGK-VGKPWOTHERSPOON29-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: TOR offense succeeds (4+ goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:SUPPRESSED (p 0.5076): highest fidelity KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no — Player prop expression KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.84 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VGK:OFFENSE_4PLUS (p 0.5093): highest fidelity KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.2885): highest fidelity KXNHLAST-26OCT08TORVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08TORVGK-VGKMMARNER93-1|no (same contract)
- KXNHLGOAL-26OCT08TORVGK-VGKPWOTHERSPOON29-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2885, phi -0.086)
- KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2885, phi -0.115)
- KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.5076, phi -0.177)
- KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2861, phi -0.277)
- override: Player prop expression KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.84 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.79 (adj +1.78) on $50.00, P(profit) 0.6195, adj growth 14.9 bp · B EV +5.93 (adj +3.87) on $29.29, P(profit) 0.2344, adj growth 33.1 bp · C EV +7.11 (adj +2.76) on $35.78, P(profit) 0.5602, adj growth 23.7 bp · R EV +0.29 (adj +0.18) on $5.00, P(profit) 0.7044, adj growth 6.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
