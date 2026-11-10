# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-10T01:00:06Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +9.35 | +4.47 | +15.12 | 0.545 | -35.57 | -43.72 | 38.91 |
| B thesis-diversified (joint) ← optimiser card | 93.81 | +14.63 | +9.27 | +9.44 | 0.541 | -41.70 | -42.26 | 80.83 |
| C best expression per thesis | 74.04 | +10.58 | +6.21 | +3.23 | 0.679 | -24.64 | -46.17 | 54.30 |
| R FUNDED research stakes | 10.00 | +0.60 | +0.39 | +3.11 | 0.656 | -3.53 | -3.53 | 0.00 |

## PHI @ VAN  ·  10000 joint draws  ·  424 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_PHI_win | p_overtime | goals | shots VAN/PHI | VAN/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.54 | 0.46 | 0.00 | 6.03 | 26.3/26.4 | 23.0/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.48 | 5.9 | 25.9/26.4 | 23.2/22.5 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.090 | 0.49 | 0.51 | 0.00 | 6.0 | 20.9/30.9 | 27.2/17.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.58 | 0.42 | 0.00 | 9.3 | 27.6/27.8 | 22.1/21.1 | even strength |
| PHI shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.48 | 0.52 | 0.46 | 5.82 | 20.7/31.4 | 28.1/17.6 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.056 | 0.62 | 0.38 | 0.00 | 5.97 | 30.4/21.0 | 18.1/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brendan Gallagher: 1+ goals YES | 11 | 0.174 | 0.157 | +0.057 | +0.040 | $9.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 74 | 0.815 | 0.795 | +0.062 | +0.042 | $20.00 | FUNDED_RESEARCH | $5 | PHI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 17 | 0.228 | 0.212 | +0.048 | +0.032 | $9.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Arshdeep Bains: 1+ goals YES | 9 | 0.126 | 0.116 | +0.030 | +0.020 | $4.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (32.25 vs 15.15 bp); relationships: KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV09PHIVAN-VANABAINS13-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: VAN offense suppressed (<= 2 goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV09PHIVAN-PHI3|no; why: higher confidence-adjusted growth (20.90 vs 5.39 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV09PHIVAN-VANABAINS13-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PHI offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes has the higher standalone adjusted growth (32.25 vs 15.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV09PHIVAN-VANABAINS13-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: VAN offense suppressed (<= 2 goals)
- **Arshdeep Bains: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes has the higher standalone adjusted growth (32.25 vs 9.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.023); they share one thesis budget; relationships: KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, PHI shot control · normal event (5-7) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3986): highest fidelity KXNHLSPREAD-26NOV09PHIVAN-PHI3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.424): highest fidelity KXNHLSPREAD-26NOV09PHIVAN-PHI3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5325): highest fidelity KXNHLSPREAD-26NOV09PHIVAN-PHI2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV09PHIVAN-PHI2|no (same contract)
- KXNHLGOAL-26NOV09PHIVAN-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3833, phi -0.204)
- KXNHLGOAL-26NOV09PHIVAN-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3597, phi -0.207)
- KXNHLGOAL-26NOV09PHIVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3833, phi -0.217)
- KXNHLGOAL-26NOV09PHIVAN-VANABAINS13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3833, phi -0.158)

portfolios: A EV +4.57 (adj +1.89) on $50.00, P(profit) 0.7621, adj growth 17.1 bp · B EV +10.38 (adj +7.09) on $43.81, P(profit) 0.4407, adj growth 61.6 bp · C EV +7.67 (adj +4.85) on $47.53, P(profit) 0.7422, adj growth 42.4 bp · R EV +0.41 (adj +0.28) on $5.00, P(profit) 0.8154, adj growth 10.6 bp

## NYI @ SJS  ·  10000 joint draws  ·  476 bet sides mapped, 5 +EV candidates, 4 on card

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
| Kiefer Sherwood: 1+ goals YES | 17 | 0.214 | 0.202 | +0.034 | +0.022 | $6.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 70 | 0.774 | 0.735 | +0.059 | +0.020 | $19.37 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Michael Misa: 1+ goals YES | 19 | 0.229 | 0.218 | +0.028 | +0.017 | $5.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Matthew Schaefer: 1+ goals NO | 76 | 0.802 | 0.790 | +0.029 | +0.018 | $19.33 | FUNDED_RESEARCH | $5 | NYI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes; why: higher confidence-adjusted growth (7.16 vs 4.05 bp); relationships: KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV09NYISJ-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (4.23 vs 0.48 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26NOV09NYISJ-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: SJS offense succeeds (4+ goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes has the higher standalone adjusted growth (7.16 vs 4.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26NOV09NYISJ-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: SJS offense suppressed (<= 2 goals)
- **Matthew Schaefer: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV09NYISJ-NYI2|no; why: higher confidence-adjusted growth (3.90 vs 0.53 bp); despite a smaller raw edge (+0.029 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:OFFENSE_4PLUS (p 0.3891): highest fidelity KXNHLGOAL-26NOV09NYISJ-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3924): highest fidelity KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no (same contract)
- thesis NYI:SUPPRESSED (p 0.3849): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3924, phi -0.216)
- KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3891, phi -0.216)
- KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3924, phi -0.225)
- KXNHLGOAL-26NOV09NYISJ-NYIMSCHAEFER48-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3974, phi -0.181)

portfolios: A EV +4.78 (adj +2.58) on $50.00, P(profit) 0.3779, adj growth 21.8 bp · B EV +4.25 (adj +2.18) on $50.00, P(profit) 0.7637, adj growth 19.2 bp · C EV +2.91 (adj +1.36) on $26.51, P(profit) 0.829, adj growth 11.9 bp · R EV +0.19 (adj +0.11) on $5.00, P(profit) 0.8022, adj growth 4.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
