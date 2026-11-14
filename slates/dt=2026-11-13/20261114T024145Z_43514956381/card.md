# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-14T02:41:45Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +7.69 | +2.81 | -8.78 | 0.459 | -29.83 | -29.83 | 22.68 |
| B thesis-diversified (joint) ← optimiser card | 45.91 | +4.09 | +2.57 | +0.34 | 0.711 | -24.58 | -24.58 | 22.35 |
| C best expression per thesis | 39.67 | +2.45 | +1.49 | +6.83 | 0.650 | -18.23 | -18.23 | 13.02 |
| R FUNDED research stakes | 5.00 | +0.26 | +0.16 | +2.40 | 0.711 | -5.00 | -5.00 | 0.00 |

## NSH @ VGK  ·  10000 joint draws  ·  446 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.597 / away 0.403

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_NSH_win | p_overtime | goals | shots VGK/NSH | VGK/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.124 | 0.73 | 0.27 | 0.00 | 5.99 | 33.4/21.6 | 19.1/28.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.64 | 0.36 | 0.00 | 6.05 | 28.0/27.5 | 24.4/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.49 | 0.51 | 0.48 | 5.97 | 28.1/27.6 | 24.2/24.7 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.57 | 0.43 | 0.45 | 5.88 | 33.4/21.9 | 18.8/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.70 | 0.30 | 0.00 | 9.27 | 29.5/28.9 | 23.9/22.3 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.083 | 0.74 | 0.26 | 0.00 | 9.32 | 35.0/23.1 | 18.8/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Braeden Bowman: 1+ goals YES | 13 | 0.173 | 0.161 | +0.036 | +0.024 | $6.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ goals YES | 21 | 0.255 | 0.243 | +0.034 | +0.021 | $6.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 66 | 0.711 | 0.697 | +0.035 | +0.021 | $16.84 | FUNDED_RESEARCH | $5 | NSH:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Victor Olofsson: 1+ goals NO | 74 | 0.780 | 0.769 | +0.027 | +0.015 | $16.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (9.96 vs 5.65 bp); relationships: KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: VGK offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (5.65 vs 2.56 bp); despite a smaller raw edge (+0.034 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: VGK offense suppressed (<= 2 goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV13NSHVGK-NSHROREILLY90-1|no; why: higher confidence-adjusted growth (4.42 vs 0.22 bp); despite a smaller raw edge (+0.035 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0049 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: NSH offense succeeds (4+ goals)
- **Victor Olofsson: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV13NSHVGK-VGKMMARNER93-1|no; why: Player prop expression KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no selected over player prop KXNHLAST-26NOV13NSHVGK-VGKVOLOFSSON95-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.91 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: VGK offense succeeds (4+ goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VGK:OFFENSE_4PLUS (p 0.4795): highest fidelity KXNHLAST-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:SUPPRESSED (p 0.4678): highest fidelity KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no (same contract)
- thesis VGK:SUPPRESSED (p 0.3098): highest fidelity KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no (same contract)
- KXNHLGOAL-26NOV13NSHVGK-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3098, phi -0.169)
- KXNHLGOAL-26NOV13NSHVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3098, phi -0.196)
- KXNHLGOAL-26NOV13NSHVGK-NSHSSTAMKOS91-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3104, phi -0.255)
- KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4795, phi -0.2)
- override: Player prop expression KXNHLGOAL-26NOV13NSHVGK-VGKVOLOFSSON95-1|no selected over player prop KXNHLAST-26NOV13NSHVGK-VGKVOLOFSSON95-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.91 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.69 (adj +2.81) on $50.00, P(profit) 0.4591, adj growth 22.7 bp · B EV +4.09 (adj +2.57) on $45.91, P(profit) 0.7113, adj growth 22.4 bp · C EV +2.45 (adj +1.49) on $39.67, P(profit) 0.6498, adj growth 13.0 bp · R EV +0.26 (adj +0.16) on $5.00, P(profit) 0.7106, adj growth 5.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
