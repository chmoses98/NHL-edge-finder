# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-10T02:18:45Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 92.91 | +9.83 | +4.13 | +11.54 | 0.611 | -35.78 | -48.33 | 34.48 |
| B thesis-diversified (joint) ← optimiser card | 59.13 | +18.17 | +13.79 | -18.42 | 0.463 | -35.79 | -41.76 | 114.41 |
| C best expression per thesis | 78.00 | +9.88 | +5.70 | +9.34 | 0.559 | -33.68 | -38.05 | 50.49 |
| R FUNDED research stakes | 6.00 | +2.17 | +1.81 | +0.64 | 0.821 | -6.00 | -6.00 | 0.00 |

## PHI @ VAN  ·  10000 joint draws  ·  436 bet sides mapped, 26 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.436 / away 0.564

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_PHI_win | p_overtime | goals | shots VAN/PHI | VAN/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.55 | 0.45 | 0.00 | 6.02 | 26.0/26.4 | 22.9/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.45 | 5.97 | 26.3/26.6 | 23.3/22.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.54 | 0.46 | 0.00 | 9.31 | 27.6/27.9 | 22.2/21.3 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.086 | 0.51 | 0.49 | 0.00 | 5.96 | 20.5/31.1 | 27.5/17.2 | even strength |
| PHI shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.47 | 0.53 | 0.47 | 5.86 | 20.7/30.9 | 27.6/17.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.057 | 0.51 | 0.49 | 0.51 | 2.85 | 24.6/24.7 | 23.2/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brendan Gallagher: 1+ goals YES | 11 | 0.170 | 0.152 | +0.053 | +0.035 | $8.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 74 | 0.816 | 0.796 | +0.063 | +0.042 | $17.59 | FUNDED_RESEARCH | $5 | PHI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 17 | 0.226 | 0.211 | +0.046 | +0.031 | $8.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Matvei Michkov: 1+ goals NO | 70 | 0.745 | 0.732 | +0.030 | +0.018 | $12.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (25.91 vs 14.12 bp); relationships: KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV09PHIVAN-PHIMMICHKOV39-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: VAN offense suppressed (<= 2 goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV09PHIVAN-PHI2|no; why: higher confidence-adjusted growth (21.50 vs 5.89 bp); despite a smaller raw edge (+0.063 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV09PHIVAN-PHIMMICHKOV39-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: PHI offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes has the higher standalone adjusted growth (25.91 vs 14.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV09PHIVAN-PHIMMICHKOV39-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: VAN offense suppressed (<= 2 goals)
- **Matvei Michkov: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no; why: Player prop expression KXNHLGOAL-26NOV09PHIVAN-PHIMMICHKOV39-1|no selected over broad KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI4|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.86 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.4013): highest fidelity KXNHLSPREAD-26NOV09PHIVAN-PHI3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.3056): highest fidelity KXNHLSPREAD-26NOV09PHIVAN-PHI2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.426): highest fidelity KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no — Player prop expression KXNHLGOAL-26NOV09PHIVAN-PHIMMICHKOV39-1|no selected over broad KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI4|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.86 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3802, phi -0.206)
- KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3588, phi -0.217)
- KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3802, phi -0.209)
- KXNHLGOAL-26NOV09PHIVAN-PHIMMICHKOV39-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3588, phi -0.217)
- override: Player prop expression KXNHLGOAL-26NOV09PHIVAN-PHIMMICHKOV39-1|no selected over broad KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI4|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.86 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.37 (adj +1.92) on $50.00, P(profit) 0.6692, adj growth 16.6 bp · B EV +8.01 (adj +5.33) on $46.91, P(profit) 0.3495, adj growth 47.0 bp · C EV +6.50 (adj +3.89) on $50.00, P(profit) 0.5329, adj growth 34.9 bp · R EV +0.42 (adj +0.28) on $5.00, P(profit) 0.8162, adj growth 10.7 bp

## NYI @ SJS  ·  10000 joint draws  ·  476 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.440 / away 0.560

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_NYI_win | p_overtime | goals | shots SJS/NYI | SJS/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.51 | 0.49 | 0.00 | 6.05 | 27.6/28.0 | 24.4/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.48 | 0.52 | 0.48 | 5.99 | 27.5/27.7 | 24.3/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.50 | 0.50 | 0.00 | 9.34 | 29.2/29.3 | 23.3/22.9 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.069 | 0.41 | 0.59 | 0.00 | 5.99 | 22.0/32.9 | 29.0/19.0 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.47 | 0.53 | 0.47 | 5.86 | 22.1/32.6 | 29.2/18.9 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.063 | 0.56 | 0.44 | 0.00 | 5.99 | 32.4/22.1 | 19.0/28.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Michael Misa: 2+ goals YES | 1 | 0.029 | 0.027 | +0.019 | +0.016 | $3.42 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | FRAGILE (0.06) | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: First Goalscorer YES | 2 | 0.036 | 0.033 | +0.015 | +0.012 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:SCORES_FIRST | FRAGILE (0.07) | EVIDENCE_MIXED | D |
| Sam Dickinson: 1+ goals YES | 5 | 0.073 | 0.067 | +0.020 | +0.014 | $3.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Mason Marchment: First Goalscorer YES | 3 | 0.044 | 0.042 | +0.012 | +0.010 | $2.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:SCORES_FIRST | FRAGILE (0.09) | EVIDENCE_MIXED | D |
- **Michael Misa: 2+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes; why: higher confidence-adjusted growth (47.30 vs 4.05 bp); despite a smaller raw edge (+0.019 vs +0.028/contract); relationships: KXNHLFIRSTGOAL-26NOV09NYISJ-SJKSHERWOOD44|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV09NYISJ-SJSDICKINSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLFIRSTGOAL-26NOV09NYISJ-SJMMARCHMENT27|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: SJS offense suppressed (<= 2 goals)
- **Kiefer Sherwood: First Goalscorer YES** — thesis: SJS scores first; alternative: KXNHLFIRSTGOAL-26NOV09NYISJ-SJMMARCHMENT27|yes; why: higher confidence-adjusted growth (13.88 vs 6.83 bp); relationships: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-2|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV09NYISJ-SJSDICKINSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLFIRSTGOAL-26NOV09NYISJ-SJMMARCHMENT27|yes: MOSTLY_INDEPENDENT (phi -0.042); failure: NYI scores first
- **Sam Dickinson: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes; why: higher confidence-adjusted growth (8.08 vs 4.05 bp); despite a smaller raw edge (+0.020 vs +0.028/contract); relationships: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-2|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLFIRSTGOAL-26NOV09NYISJ-SJKSHERWOOD44|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLFIRSTGOAL-26NOV09NYISJ-SJMMARCHMENT27|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: First Goalscorer YES** — thesis: SJS scores first; alternative: KXNHLFIRSTGOAL-26NOV09NYISJ-SJTTOFFOLI73|yes; why: higher confidence-adjusted growth (6.83 vs 3.29 bp); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-2|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLFIRSTGOAL-26NOV09NYISJ-SJKSHERWOOD44|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26NOV09NYISJ-SJSDICKINSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: NYI scores first

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:SCORES_FIRST (p 0.4959): highest fidelity KXNHLFIRSTGOAL-26NOV09NYISJ-SJMMARCHMENT27|yes [FRAGILE], best adjusted EV KXNHLFIRSTGOAL-26NOV09NYISJ-SJMMARCHMENT27|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3924): highest fidelity KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3891): highest fidelity KXNHLGOAL-26NOV09NYISJ-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV09NYISJ-SJMMISA77-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 94% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3924, phi -0.119)
- KXNHLFIRSTGOAL-26NOV09NYISJ-SJKSHERWOOD44|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family MIXED; loses 93% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SCORES_FIRST (p 0.5034, phi -0.196)
- KXNHLGOAL-26NOV09NYISJ-SJSDICKINSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3924, phi -0.117)
- KXNHLFIRSTGOAL-26NOV09NYISJ-SJMMARCHMENT27|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family MIXED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SCORES_FIRST (p 0.5034, phi -0.216)

portfolios: A EV +4.46 (adj +2.21) on $42.91, P(profit) 0.4752, adj growth 17.9 bp · B EV +10.17 (adj +8.46) on $12.22, P(profit) 0.1757, adj growth 67.4 bp · C EV +3.38 (adj +1.81) on $28.00, P(profit) 0.2101, adj growth 15.6 bp · R EV +1.75 (adj +1.53) on $1.00, P(profit) 0.0294, adj growth 44.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
