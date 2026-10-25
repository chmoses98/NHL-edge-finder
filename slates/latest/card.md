# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T00:14:38Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 137.43 | +24.55 | +7.03 | +18.73 | 0.612 | -57.18 | -68.93 | 50.75 |
| B thesis-diversified (joint) ← optimiser card | 106.95 | +13.19 | +5.85 | +8.10 | 0.552 | -29.64 | -46.34 | 51.82 |
| C best expression per thesis | 44.46 | +8.83 | +3.64 | -5.06 | 0.495 | -27.89 | -27.89 | 31.56 |
| R FUNDED research stakes | 19.00 | +1.82 | +0.76 | +2.85 | 0.711 | -7.54 | -9.16 | 0.00 |

## TBL @ UTA  ·  10000 joint draws  ·  446 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.569 / away 0.431

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TBL_win | p_overtime | goals | shots UTA/TBL | UTA/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.63 | 0.37 | 0.00 | 6.05 | 26.8/26.7 | 23.6/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.48 | 5.95 | 26.9/27.1 | 23.8/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.63 | 0.37 | 0.00 | 9.31 | 28.4/28.4 | 23.3/21.4 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 6.02 | 31.8/21.3 | 18.5/27.3 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.065 | 0.54 | 0.46 | 0.00 | 6.05 | 21.3/31.3 | 27.9/17.8 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.55 | 0.45 | 0.46 | 5.91 | 31.8/21.5 | 18.4/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anthony Cirelli: 1+ goals YES | 18 | 0.223 | 0.211 | +0.033 | +0.021 | $6.02 | FUNDED_RESEARCH | $2 | TBL:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.153 | 0.142 | +0.025 | +0.015 | $3.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 67 | 0.778 | 0.701 | +0.093 | +0.016 | $15.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Anthony Cirelli: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-TBIMIKHEYEV95-1|yes; why: higher confidence-adjusted growth (6.09 vs 0.97 bp); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: TBL offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24TBUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (4.21 vs 0.41 bp); alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.032); failure: UTA offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24TBUTA-UTALCOOLEY92-1|no; why: higher confidence-adjusted growth (2.57 vs 0.31 bp); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.032); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis TBL:OFFENSE_4PLUS (p 0.3395): highest fidelity KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3363): highest fidelity KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4504): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24TBUTA-TBACIRELLI71-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.4402, phi -0.224)
- KXNHLGOAL-26OCT24TBUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3363, phi -0.17)
- KXNHLAST-26OCT24TBUTA-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.8 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4504, phi -0.207)

portfolios: A EV +5.91 (adj +2.41) on $37.43, P(profit) 0.3397, adj growth 18.9 bp · B EV +3.91 (adj +1.47) on $25.35, P(profit) 0.3397, adj growth 12.8 bp · C EV +3.06 (adj +1.01) on $20.93, P(profit) 0.8264, adj growth 8.8 bp · R EV +0.35 (adj +0.22) on $2.00, P(profit) 0.2232, adj growth 7.2 bp

## DET @ CGY  ·  10000 joint draws  ·  450 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.457 / away 0.543

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
| Ben Jones: 1+ goals NO | 85 | 0.902 | 0.887 | +0.043 | +0.029 | $20.00 | FUNDED_RESEARCH | $5 | CGY:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 18 | 0.230 | 0.216 | +0.039 | +0.026 | $7.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 11 | 0.149 | 0.136 | +0.032 | +0.019 | $4.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brennan Othmann: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Ben Jones: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT24DETCGY-CGYBJONES39-1|no; why: higher confidence-adjusted growth (14.99 vs 0.95 bp); despite a smaller raw edge (+0.043 vs +0.115/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: CGY offense succeeds (4+ goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes; why: higher confidence-adjusted growth (9.20 vs 7.37 bp); relationships: KXNHLGOAL-26OCT24DETCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: CGY offense suppressed (<= 2 goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes has the higher standalone adjusted growth (9.20 vs 7.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: CGY offense suppressed (<= 2 goals)
- **Brennan Othmann: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes has the higher standalone adjusted growth (9.20 vs 4.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4323): highest fidelity KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no (same contract)
- thesis CGY:SUPPRESSED (p 0.4213): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT24DETCGY-CGYBJONES39-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.3555, phi -0.143)
- KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.197)
- KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.186)
- KXNHLGOAL-26OCT24DETCGY-CGYBOTHMANN78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.174)

portfolios: A EV +3.81 (adj +1.36) on $50.00, P(profit) 0.6104, adj growth 12.3 bp · B EV +4.70 (adj +2.96) on $36.14, P(profit) 0.423, adj growth 26.2 bp · C EV +2.43 (adj +1.27) on $17.23, P(profit) 0.2296, adj growth 11.0 bp · R EV +0.25 (adj +0.17) on $5.00, P(profit) 0.9016, adj growth 6.4 bp

## MIN @ SEA  ·  10000 joint draws  ·  440 bet sides mapped, 28 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.390 / away 0.610

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
| Kirill Kaprizov: 2+ goals NO | 88 | 0.919 | 0.908 | +0.032 | +0.021 | $20.00 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 1.5 goals NO | 61 | 0.747 | 0.655 | +0.120 | +0.028 | $15.51 | FUNDED_RESEARCH | $4 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 74 | 0.844 | 0.773 | +0.091 | +0.020 | $2.95 | FUNDED_RESEARCH | $1 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota over 4.5 goals scored NO | 73 | 0.802 | 0.763 | +0.058 | +0.020 | $7.00 | FUNDED_RESEARCH | $2 | SEA:WINS | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes has the higher standalone adjusted growth (14.63 vs 9.41 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.107); relationships: KXNHLSPREAD-26OCT24MINSEA-MIN2|no: REINFORCING (phi 0.202); KXNHLSPREAD-26OCT24MINSEA-MIN3|no: REINFORCING (phi 0.177); KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no: REINFORCING (phi 0.244); failure: MIN offense succeeds (4+ goals)
- **Minnesota wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes has the higher standalone adjusted growth (14.63 vs 7.36 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.286); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: REINFORCING (phi 0.202); KXNHLSPREAD-26OCT24MINSEA-MIN3|no: DUPLICATIVE (phi 0.738); KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no: REINFORCING (phi 0.492); failure: MIN wins by 2+
- **Minnesota wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: Broad expression KXNHLSPREAD-26OCT24MINSEA-MIN3|no selected over player prop KXNHLAST-26OCT24MINSEA-MINMBOLDY12-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: REINFORCING (phi 0.177); KXNHLSPREAD-26OCT24MINSEA-MIN2|no: DUPLICATIVE (phi 0.738); KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no: REINFORCING (phi 0.51); failure: MIN wins by 2+
- **Minnesota over 4.5 goals scored NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes has the higher standalone adjusted growth (14.63 vs 4.48 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.230); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: REINFORCING (phi 0.244); KXNHLSPREAD-26OCT24MINSEA-MIN2|no: REINFORCING (phi 0.492); KXNHLSPREAD-26OCT24MINSEA-MIN3|no: REINFORCING (phi 0.51); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:WINS_BY_2PLUS (p 0.3116): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN2|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.4115): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4218): highest fidelity KXNHLSPREAD-26OCT24MINSEA-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT24MINSEA-MIN2|no — Broad expression KXNHLSPREAD-26OCT24MINSEA-MIN3|no selected over player prop KXNHLAST-26OCT24MINSEA-MINMBOLDY12-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3593, phi -0.248)
- KXNHLSPREAD-26OCT24MINSEA-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.2 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2531, phi -1.0)
- KXNHLSPREAD-26OCT24MINSEA-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.9 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2531, phi -0.738)
- KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3593, phi -0.664)
- override: Broad expression KXNHLSPREAD-26OCT24MINSEA-MIN3|no selected over player prop KXNHLAST-26OCT24MINSEA-MINMBOLDY12-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: override declined: the joint re-optimisation gives KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-1|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no kept

portfolios: A EV +14.84 (adj +3.26) on $50.00, P(profit) 0.5346, adj growth 19.5 bp · B EV +4.59 (adj +1.42) on $45.46, P(profit) 0.7103, adj growth 12.8 bp · C EV +3.34 (adj +1.36) on $6.30, P(profit) 0.1949, adj growth 11.7 bp · R EV +1.22 (adj +0.37) on $12.00, P(profit) 0.7103, adj growth 13.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT24MINSEA-SEA|yes == KXNHLGAME-26OCT24MINSEA-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
