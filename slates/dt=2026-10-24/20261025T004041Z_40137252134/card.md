# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T00:40:41Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 142.43 | +28.01 | +8.97 | +24.92 | 0.618 | -58.71 | -77.76 | 65.44 |
| B thesis-diversified (joint) ← optimiser card | 122.80 | +13.51 | +6.93 | +4.34 | 0.620 | -33.78 | -43.58 | 61.91 |
| C best expression per thesis | 35.10 | +7.66 | +3.68 | +2.55 | 0.522 | -35.10 | -35.10 | 31.90 |
| R FUNDED research stakes | 15.00 | +1.34 | +0.81 | +0.49 | 0.738 | -5.33 | -9.18 | 0.00 |

## TBL @ UTA  ·  10000 joint draws  ·  446 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.569 / away 0.431

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TBL_win | p_overtime | goals | shots UTA/TBL | UTA/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.02 | 26.7/26.8 | 23.9/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.49 | 5.93 | 27.0/27.1 | 23.9/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.63 | 0.37 | 0.00 | 9.31 | 28.6/28.5 | 23.1/21.8 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.070 | 0.70 | 0.30 | 0.00 | 5.99 | 31.6/21.1 | 18.6/27.1 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.070 | 0.55 | 0.45 | 0.00 | 5.99 | 21.5/31.3 | 27.7/17.8 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.56 | 0.44 | 0.48 | 5.98 | 31.5/21.4 | 18.2/28.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack McBain: 1+ goals YES | 11 | 0.155 | 0.142 | +0.038 | +0.026 | $6.78 | FUNDED_RESEARCH | $2 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Anthony Cirelli: 1+ goals YES | 18 | 0.228 | 0.215 | +0.038 | +0.024 | $7.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 67 | 0.781 | 0.703 | +0.096 | +0.017 | $17.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (13.64 vs 0.62 bp); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.029); failure: UTA offense suppressed (<= 2 goals)
- **Anthony Cirelli: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-TBIMIKHEYEV95-1|yes; why: higher confidence-adjusted growth (8.37 vs 0.84 bp); alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: TBL offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TBUTA-UTALCOOLEY92-1|no; why: higher confidence-adjusted growth (2.93 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.3393): highest fidelity KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.463): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis UTA:SUPPRESSED (p 0.3261): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3261, phi -0.175)
- KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.438, phi -0.236)
- KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.463, phi -0.192)

portfolios: A EV +8.62 (adj +4.36) on $42.43, P(profit) 0.3491, adj growth 34.4 bp · B EV +6.04 (adj +2.84) on $31.18, P(profit) 0.3491, adj growth 24.6 bp · C EV +1.42 (adj +0.92) on $7.17, P(profit) 0.228, adj growth 8.0 bp · R EV +0.65 (adj +0.44) on $2.00, P(profit) 0.155, adj growth 14.6 bp

## DET @ CGY  ·  10000 joint draws  ·  450 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.460 / away 0.540

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_DET_win | p_overtime | goals | shots CGY/DET | CGY/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.53 | 0.47 | 0.00 | 5.98 | 28.1/28.4 | 25.0/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.45 | 5.87 | 28.6/28.7 | 25.6/25.3 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.087 | 0.46 | 0.54 | 0.00 | 5.95 | 22.8/34.1 | 30.3/19.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.46 | 0.54 | 0.47 | 5.87 | 22.7/34.2 | 30.7/19.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.50 | 0.50 | 0.00 | 9.22 | 30.2/30.6 | 24.5/23.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.54 | 0.46 | 0.00 | 3.49 | 27.4/27.7 | 25.8/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Moritz Seider: 1+ goals NO | 85 | 0.906 | 0.890 | +0.047 | +0.032 | $19.17 | FUNDED_RESEARCH | $5 | DET:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Ben Jones: 1+ goals NO | 85 | 0.902 | 0.887 | +0.043 | +0.029 | $19.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 18 | 0.230 | 0.216 | +0.039 | +0.026 | $7.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 11 | 0.149 | 0.136 | +0.032 | +0.019 | $4.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Moritz Seider: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24DETCGY-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (18.36 vs 3.37 bp); despite a smaller raw edge (+0.047 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24DETCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: DET offense succeeds (4+ goals)
- **Ben Jones: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT24DETCGY-CGYBJONES39-1|no; why: higher confidence-adjusted growth (14.99 vs 0.14 bp); despite a smaller raw edge (+0.043 vs +0.105/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24DETCGY-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: CGY offense succeeds (4+ goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes; why: higher confidence-adjusted growth (9.20 vs 7.37 bp); relationships: KXNHLGOAL-26OCT24DETCGY-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24DETCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: CGY offense suppressed (<= 2 goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes has the higher standalone adjusted growth (9.20 vs 7.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24DETCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4323): highest fidelity KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT24DETCGY-DETVARVIDSSON33-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:SUPPRESSED (p 0.4213): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24DETCGY-DETMSEIDER53-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3499, phi -0.155)
- KXNHLGOAL-26OCT24DETCGY-CGYBJONES39-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.3555, phi -0.143)
- KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.197)
- KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.186)

portfolios: A EV +4.55 (adj +1.35) on $50.00, P(profit) 0.6738, adj growth 11.5 bp · B EV +4.72 (adj +3.03) on $50.00, P(profit) 0.3421, adj growth 27.7 bp · C EV +2.90 (adj +1.40) on $21.63, P(profit) 0.7812, adj growth 12.2 bp · R EV +0.27 (adj +0.18) on $5.00, P(profit) 0.9056, adj growth 7.1 bp

## MIN @ SEA  ·  10000 joint draws  ·  440 bet sides mapped, 29 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.389 / away 0.611

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_MIN_win | p_overtime | goals | shots SEA/MIN | SEA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.56 | 0.44 | 0.00 | 6.02 | 28.6/28.9 | 25.6/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.47 | 5.95 | 28.5/29.1 | 25.7/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.56 | 0.44 | 0.00 | 9.29 | 30.0/30.6 | 24.9/23.5 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.093 | 0.53 | 0.47 | 0.00 | 5.98 | 22.9/34.5 | 30.8/19.4 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.48 | 0.52 | 0.46 | 5.91 | 23.0/34.3 | 30.8/19.9 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.059 | 0.49 | 0.51 | 0.00 | 9.23 | 24.3/35.9 | 29.0/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Kaprizov: 2+ goals NO | 88 | 0.919 | 0.908 | +0.032 | +0.021 | $17.18 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Minnesota over 4.5 goals scored NO | 73 | 0.802 | 0.761 | +0.058 | +0.017 | $11.62 | FUNDED_RESEARCH | $3 | SEA:WINS | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Matt Boldy: 1+ goals NO | 60 | 0.648 | 0.635 | +0.032 | +0.018 | $8.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 52 | 0.630 | 0.555 | +0.093 | +0.018 | $4.71 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes has the higher standalone adjusted growth (14.63 vs 9.41 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.107); relationships: KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no: REINFORCING (phi 0.244); KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: DUPLICATIVE (phi 0.388); failure: MIN offense succeeds (4+ goals)
- **Minnesota over 4.5 goals scored NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no selected over player prop KXNHLAST-26OCT24MINSEA-MINKKAPRIZOV97-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.78 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: REINFORCING (phi 0.244); KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no: REINFORCING (phi 0.235); KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.249); failure: MIN offense succeeds (4+ goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: Player prop expression KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no selected over broad KXNHLSPREAD-26OCT24MINSEA-MIN2|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.74 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no: REINFORCING (phi 0.235); KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: MIN offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: Player prop expression KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT24MINSEA-MINMBOLDY12-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.80 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: DUPLICATIVE (phi 0.388); KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no: REINFORCING (phi 0.249); KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:WINS_BY_2PLUS (p 0.3116): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN2|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.4115): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4218): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN2|no — Player prop expression KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT24MINSEA-MINMBOLDY12-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.80 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3593, phi -0.248)
- KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3593, phi -0.664)
- KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3593, phi -0.288)
- KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3593, phi -0.288)
- override: Player prop expression KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no selected over broad KXNHLSPREAD-26OCT24MINSEA-MIN2|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.74 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT24MINSEA-MINMBOLDY12-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.80 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no selected over player prop KXNHLAST-26OCT24MINSEA-MINKKAPRIZOV97-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.78 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +14.84 (adj +3.26) on $50.00, P(profit) 0.5346, adj growth 19.5 bp · B EV +2.75 (adj +1.06) on $41.62, P(profit) 0.7094, adj growth 9.7 bp · C EV +3.34 (adj +1.36) on $6.30, P(profit) 0.1949, adj growth 11.7 bp · R EV +0.41 (adj +0.19) on $8.00, P(profit) 0.7635, adj growth 6.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT24MINSEA-SEA|yes == KXNHLGAME-26OCT24MINSEA-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
