# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T14:16:14Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +28.21 | +9.90 | +24.53 | 0.664 | -44.38 | -62.65 | 81.74 |
| B thesis-diversified (joint) ← optimiser card | 131.89 | +22.26 | +12.95 | +13.19 | 0.609 | -49.64 | -60.91 | 111.98 |
| C best expression per thesis | 79.97 | +20.80 | +10.74 | +11.56 | 0.601 | -46.97 | -54.76 | 92.33 |
| R FUNDED research stakes | 28.00 | +4.25 | +2.44 | +2.60 | 0.606 | -11.03 | -14.67 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  414 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_ANA_win | p_overtime | goals | shots NYR/ANA | NYR/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.56 | 0.44 | 0.00 | 5.98 | 26.7/27.1 | 23.9/22.8 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.109 | 0.48 | 0.52 | 0.00 | 6.04 | 21.2/32.3 | 28.6/17.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.54 | 0.46 | 0.47 | 5.98 | 26.7/27.5 | 24.3/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.57 | 0.43 | 0.00 | 9.42 | 28.3/29.0 | 23.3/21.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.50 | 0.50 | 0.48 | 5.95 | 21.4/32.6 | 29.0/18.2 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.079 | 0.51 | 0.49 | 0.00 | 9.27 | 23.1/34.6 | 28.2/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 14 | 0.229 | 0.204 | +0.081 | +0.056 | $14.35 | FUNDED_RESEARCH | $4 | ANA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 9 | 0.122 | 0.111 | +0.026 | +0.015 | $3.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 10 | 0.131 | 0.122 | +0.025 | +0.015 | $3.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Taylor Raddysh: 1+ goals YES | 9 | 0.117 | 0.108 | +0.021 | +0.012 | $3.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes; why: higher confidence-adjusted growth (52.05 vs 4.25 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (52.05 vs 6.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (52.05 vs 5.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.036); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: ANA offense suppressed (<= 2 goals)
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (3.51 vs 0.00 bp); despite a smaller raw edge (+0.021 vs +0.024/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3865): highest fidelity KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3515): highest fidelity KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.4327): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4, phi -0.244)
- KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4, phi -0.155)
- KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4, phi -0.15)
- KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3515, phi -0.153)

portfolios: A EV +9.32 (adj +4.80) on $38.90, P(profit) 0.446, adj growth 41.5 bp · B EV +10.40 (adj +6.97) on $25.13, P(profit) 0.4806, adj growth 59.4 bp · C EV +8.49 (adj +5.59) on $24.38, P(profit) 0.229, adj growth 47.5 bp · R EV +2.17 (adj +1.50) on $4.00, P(profit) 0.229, adj growth 50.2 bp

## COL @ PHI  ·  10000 joint draws  ·  376 bet sides mapped, 26 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_COL_win | p_overtime | goals | shots PHI/COL | PHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.139 | 0.39 | 0.61 | 0.00 | 5.97 | 21.2/33.6 | 29.2/18.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.44 | 0.56 | 0.46 | 5.9 | 21.3/33.4 | 29.9/18.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.100 | 0.44 | 0.56 | 0.00 | 5.96 | 27.0/27.6 | 23.8/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.49 | 0.51 | 0.48 | 5.87 | 27.3/27.9 | 24.7/24.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.078 | 0.33 | 0.67 | 0.00 | 9.17 | 22.9/35.5 | 28.1/18.1 | even strength |
| COL shot control · low event (<=4) · tight (1-goal/OT) | 0.076 | 0.47 | 0.53 | 0.48 | 2.81 | 20.0/31.9 | 30.3/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 1+ goals NO | 54 | 0.624 | 0.602 | +0.067 | +0.045 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Colorado wins by over 1.5 goals NO | 54 | 0.677 | 0.585 | +0.119 | +0.027 | $4.27 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 67 | 0.792 | 0.710 | +0.107 | +0.024 | $8.58 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 5.5 goals scored NO | 85 | 0.905 | 0.875 | +0.046 | +0.016 | $14.35 | FUNDED_RESEARCH | $4 | PHI:WINS | DIRECT (1.00) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT19COLPHI-PHI2|yes; why: higher confidence-adjusted growth (17.67 vs 8.87 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.987 vs 0.558); relationships: KXNHLSPREAD-26OCT19COLPHI-COL2|no: REINFORCING (phi 0.25); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.211); KXNHLTEAMTOTAL-26OCT19COLPHI-COL6|no: REINFORCING (phi 0.201); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT19COLPHI-COL3|no; why: higher confidence-adjusted growth (6.57 vs 5.91 bp); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: REINFORCING (phi 0.25); KXNHLSPREAD-26OCT19COLPHI-COL3|no: DUPLICATIVE (phi 0.741); KXNHLTEAMTOTAL-26OCT19COLPHI-COL6|no: DUPLICATIVE (phi 0.376); failure: COL wins by 2+
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT19COLPHI-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT19COLPHI-COL2|no has the higher standalone adjusted growth (6.57 vs 5.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.741); they share one thesis budget; relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: REINFORCING (phi 0.211); KXNHLSPREAD-26OCT19COLPHI-COL2|no: DUPLICATIVE (phi 0.741); KXNHLTEAMTOTAL-26OCT19COLPHI-COL6|no: REINFORCING (phi 0.432); failure: COL wins by 2+
- **Colorado over 5.5 goals scored NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes; why: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes has the higher standalone adjusted growth (37.43 vs 4.69 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.055); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: REINFORCING (phi 0.201); KXNHLSPREAD-26OCT19COLPHI-COL2|no: DUPLICATIVE (phi 0.376); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.432); failure: high-event game (8+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:SCORES_FIRST (p 0.4661): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3131): highest fidelity KXNHLTEAMTOTAL-26OCT19COLPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2319): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no (same contract)
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3906, phi -0.302)
- KXNHLSPREAD-26OCT19COLPHI-COL2|no: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.2 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3233, phi -1.0)
- KXNHLSPREAD-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.7 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3233, phi -0.741)
- KXNHLTEAMTOTAL-26OCT19COLPHI-COL6|no: FUNDED_RESEARCH; family MIXED; loses 0% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2214, phi -0.505)

portfolios: A EV +10.32 (adj +1.33) on $38.90, P(profit) 0.6459, adj growth 10.8 bp · B EV +5.42 (adj +2.38) on $47.20, P(profit) 0.6012, adj growth 21.1 bp · C EV +9.00 (adj +3.46) on $29.19, P(profit) 0.6517, adj growth 30.1 bp · R EV +1.28 (adj +0.58) on $12.00, P(profit) 0.6012, adj growth 20.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT19COLPHI-COL|no == KXNHLGAME-26OCT19COLPHI-PHI|yes

## SJS @ TOR  ·  10000 joint draws  ·  438 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_SJS_win | p_overtime | goals | shots TOR/SJS | TOR/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.135 | 0.53 | 0.47 | 0.00 | 6.01 | 28.1/28.4 | 25.0/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.48 | 5.95 | 28.1/28.3 | 25.1/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.58 | 0.42 | 0.00 | 9.38 | 29.6/29.9 | 24.0/23.2 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.084 | 0.53 | 0.47 | 0.00 | 6.0 | 22.6/33.6 | 29.9/19.2 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.51 | 0.49 | 0.46 | 5.87 | 22.5/33.9 | 30.4/19.3 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.059 | 0.47 | 0.53 | 0.00 | 9.1 | 23.6/35.1 | 28.6/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ goals NO | 78 | 0.829 | 0.816 | +0.037 | +0.024 | $20.00 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 19 | 0.234 | 0.222 | +0.033 | +0.021 | $6.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Full Game: Over 6.5 goals scored NO | 45 | 0.520 | 0.483 | +0.053 | +0.015 | $5.70 | FUNDED_RESEARCH | $2 | SJS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Full Game: Over 5.5 goals scored NO | 35 | 0.415 | 0.380 | +0.049 | +0.014 | $2.26 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-5|no; why: higher confidence-adjusted growth (7.54 vs 2.37 bp); despite a smaller raw edge (+0.037 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.001 vs 0.401); relationships: KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLTOTAL-26OCT19SJTOR-7|no: MOSTLY_INDEPENDENT (phi 0.133); KXNHLTOTAL-26OCT19SJTOR-6|no: MOSTLY_INDEPENDENT (phi 0.126); failure: SJS offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (5.78 vs 0.84 bp); despite a smaller raw edge (+0.033 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLTOTAL-26OCT19SJTOR-7|no: INTENTIONAL_DIVERSIFIER (phi -0.172); KXNHLTOTAL-26OCT19SJTOR-6|no: INTENTIONAL_DIVERSIFIER (phi -0.162); failure: SJS offense suppressed (<= 2 goals)
- **Full Game: Over 6.5 goals scored NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-5|no; why: KXNHLTOTAL-26OCT19SJTOR-5|no has the higher standalone adjusted growth (2.37 vs 2.06 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.476); relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.133); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.172); KXNHLTOTAL-26OCT19SJTOR-6|no: DUPLICATIVE (phi 0.808); failure: high-event game (8+ goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-5|no; why: Broad expression KXNHLTOTAL-26OCT19SJTOR-6|no selected over broad KXNHLTOTAL-26OCT19SJTOR-5|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.126); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.162); KXNHLTOTAL-26OCT19SJTOR-7|no: DUPLICATIVE (phi 0.808); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3779): highest fidelity KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.4108): highest fidelity KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT19SJTOR-7|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2183): highest fidelity KXNHLTOTAL-26OCT19SJTOR-7|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT19SJTOR-7|no (same contract)
- KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3779, phi -0.172)
- KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4108, phi -0.231)
- KXNHLTOTAL-26OCT19SJTOR-7|no: FUNDED_RESEARCH; family MIXED; loses 17% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2788, phi -0.648)
- KXNHLTOTAL-26OCT19SJTOR-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2788, phi -0.523)
- override: Broad expression KXNHLTOTAL-26OCT19SJTOR-6|no selected over broad KXNHLTOTAL-26OCT19SJTOR-5|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.88 (adj +1.01) on $38.90, P(profit) 0.4793, adj growth 6.9 bp · B EV +3.01 (adj +1.58) on $34.80, P(profit) 0.586, adj growth 14.0 bp · C EV +2.06 (adj +1.00) on $10.75, P(profit) 0.4087, adj growth 8.7 bp · R EV +0.60 (adj +0.25) on $8.00, P(profit) 0.4565, adj growth 8.6 bp

## PIT @ UTA  ·  10000 joint draws  ·  462 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_PIT_win | p_overtime | goals | shots UTA/PIT | UTA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.61 | 0.39 | 0.00 | 6.06 | 27.5/27.3 | 24.2/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.114 | 0.62 | 0.38 | 0.00 | 9.48 | 28.8/28.6 | 23.0/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.53 | 0.47 | 0.47 | 6.0 | 27.3/27.2 | 23.9/23.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.081 | 0.70 | 0.30 | 0.00 | 6.01 | 32.1/21.3 | 18.7/27.4 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.58 | 0.42 | 0.43 | 5.96 | 32.2/21.8 | 18.6/28.7 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.070 | 0.67 | 0.33 | 0.00 | 9.42 | 33.9/23.1 | 18.3/26.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack McBain: 1+ goals YES | 12 | 0.164 | 0.150 | +0.036 | +0.023 | $6.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.151 | 0.141 | +0.023 | +0.013 | $3.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 62 | 0.669 | 0.654 | +0.032 | +0.018 | $12.20 | FUNDED_RESEARCH | $4 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Andrei Kuzmenko: 1+ goals YES | 13 | 0.158 | 0.148 | +0.020 | +0.010 | $2.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (10.25 vs 0.57 bp); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT19PITUTA-PITAKUZMENKO62-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: UTA offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19PITUTA-PITRRAKELL67-2|yes; why: higher confidence-adjusted growth (3.32 vs 1.62 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.867 vs 0.765); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT19PITUTA-PITAKUZMENKO62-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PIT offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19PITUTA-UTACKELLER9-2|no; why: higher confidence-adjusted growth (2.89 vs 0.19 bp); despite a smaller raw edge (+0.032 vs +0.063/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT19PITUTA-PITAKUZMENKO62-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: UTA offense succeeds (4+ goals)
- **Andrei Kuzmenko: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes has the higher standalone adjusted growth (3.32 vs 1.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.3668): highest fidelity KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3006): highest fidelity KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.493): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3006, phi -0.168)
- KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4145, phi -0.196)
- KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.493, phi -0.229)
- KXNHLGOAL-26OCT19PITUTA-PITAKUZMENKO62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4145, phi -0.171)

portfolios: A EV +4.69 (adj +2.76) on $33.31, P(profit) 0.3654, adj growth 22.6 bp · B EV +3.43 (adj +2.02) on $24.76, P(profit) 0.3654, adj growth 17.5 bp · C EV +1.25 (adj +0.69) on $15.65, P(profit) 0.7178, adj growth 6.0 bp · R EV +0.20 (adj +0.11) on $4.00, P(profit) 0.6686, adj growth 3.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
