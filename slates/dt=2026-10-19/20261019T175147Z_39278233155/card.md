# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T17:51:47Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.63 | +9.21 | +24.27 | 0.676 | -38.72 | -54.91 | 77.64 |
| B thesis-diversified (joint) ← optimiser card | 118.26 | +21.20 | +12.63 | +11.78 | 0.583 | -41.30 | -58.18 | 108.50 |
| C best expression per thesis | 100.32 | +19.19 | +9.60 | +8.92 | 0.600 | -37.22 | -40.63 | 83.25 |
| R FUNDED research stakes | 18.00 | +2.77 | +1.63 | -1.55 | 0.347 | -7.87 | -7.87 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  434 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.577 / away 0.423

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_ANA_win | p_overtime | goals | shots NYR/ANA | NYR/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.60 | 0.40 | 0.00 | 6.01 | 26.5/27.1 | 23.9/22.6 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.107 | 0.52 | 0.48 | 0.00 | 6.04 | 21.4/32.7 | 29.1/18.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.51 | 0.49 | 0.49 | 5.96 | 26.9/27.5 | 24.2/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.61 | 0.39 | 0.00 | 9.4 | 28.5/29.2 | 23.5/21.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.48 | 0.52 | 0.47 | 5.99 | 21.5/32.9 | 29.5/18.3 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.076 | 0.50 | 0.50 | 0.00 | 9.4 | 22.8/34.2 | 27.3/16.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 14 | 0.219 | 0.198 | +0.071 | +0.050 | $10.94 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| A.J. Greer: 2+ goals YES | 1 | 0.029 | 0.024 | +0.018 | +0.013 | $1.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.06) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ assists YES | 26 | 0.336 | 0.295 | +0.062 | +0.022 | $6.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Taylor Raddysh: 1+ goals YES | 9 | 0.120 | 0.110 | +0.025 | +0.014 | $3.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANABSENNECKE45-2|yes; why: higher confidence-adjusted growth (41.21 vs 4.82 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.895 vs 0.743); relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: DUPLICATIVE (phi 0.323); KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: ANA offense suppressed (<= 2 goals)
- **A.J. Greer: 2+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (41.21 vs 31.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.323); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: DUPLICATIVE (phi 0.323); KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: ANA offense suppressed (<= 2 goals)
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-NYRJMILLER8-1|yes; why: higher confidence-adjusted growth (5.19 vs 0.02 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.027); failure: NYR offense suppressed (<= 2 goals)
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes has the higher standalone adjusted growth (5.19 vs 5.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.027); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.027); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3814): highest fidelity KXNHLAST-26OCT19ANANYR-ANAAKILLORN17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.4531): highest fidelity KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.3376): highest fidelity KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.399, phi -0.237)
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 94% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.399, phi -0.121)
- KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3376, phi -0.254)
- KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3376, phi -0.143)

portfolios: A EV +10.43 (adj +5.03) on $40.63, P(profit) 0.5538, adj growth 42.7 bp · B EV +10.34 (adj +6.76) on $22.59, P(profit) 0.5395, adj growth 56.4 bp · C EV +8.59 (adj +5.10) on $31.92, P(profit) 0.4093, adj growth 43.6 bp · R EV +1.43 (adj +1.00) on $3.00, P(profit) 0.219, adj growth 34.6 bp

## COL @ PHI  ·  10000 joint draws  ·  436 bet sides mapped, 34 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.325 / away 0.675

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_COL_win | p_overtime | goals | shots PHI/COL | PHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.137 | 0.39 | 0.61 | 0.00 | 5.93 | 21.1/33.4 | 29.3/18.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.45 | 0.55 | 0.46 | 5.87 | 21.4/33.8 | 30.4/18.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.43 | 0.57 | 0.00 | 5.99 | 26.9/27.7 | 23.9/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.50 | 0.50 | 0.46 | 5.9 | 26.9/27.8 | 24.7/23.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.079 | 0.34 | 0.66 | 0.00 | 9.16 | 22.8/35.6 | 28.1/18.1 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.077 | 0.41 | 0.59 | 0.00 | 3.45 | 20.1/32.2 | 29.9/18.6 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 2+ goals NO | 86 | 0.915 | 0.899 | +0.047 | +0.030 | $16.95 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Trevor Zegras: 1+ goals YES | 23 | 0.296 | 0.279 | +0.054 | +0.036 | $8.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 55 | 0.622 | 0.603 | +0.055 | +0.035 | $12.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 67 | 0.796 | 0.711 | +0.110 | +0.025 | $11.75 | FUNDED_RESEARCH | $3 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 2+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT19COLPHI-PHI3|yes; why: Player prop expression KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no selected over player prop KXNHLAST-26OCT19COLPHI-COLCMAKAR8-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.99 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT19COLPHI-PHITZEGRAS46-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: DUPLICATIVE (phi 0.391); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.188); failure: COL offense succeeds (4+ goals)
- **Trevor Zegras: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes; why: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes has the higher standalone adjusted growth (42.22 vs 15.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.099); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.151); failure: PHI offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no; why: second expression of the same thesis: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no has the higher standalone adjusted growth (18.03 vs 11.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.391); they share one thesis budget; relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: DUPLICATIVE (phi 0.391); KXNHLGOAL-26OCT19COLPHI-PHITZEGRAS46-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.213); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes; why: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes has the higher standalone adjusted growth (42.22 vs 6.55 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: REINFORCING (phi 0.188); KXNHLGOAL-26OCT19COLPHI-PHITZEGRAS46-1|yes: REINFORCING (phi 0.151); KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: REINFORCING (phi 0.213); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:SCORES_FIRST (p 0.4698): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3134): highest fidelity KXNHLTEAMTOTAL-26OCT19COLPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT19COLPHI-PHITZEGRAS46-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2308): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.241)
- KXNHLGOAL-26OCT19COLPHI-PHITZEGRAS46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4676, phi -0.258)
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.31)
- KXNHLSPREAD-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.1 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3232, phi -0.733)
- override: Player prop expression KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no selected over player prop KXNHLAST-26OCT19COLPHI-COLCMAKAR8-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.99 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +10.94 (adj +1.38) on $40.63, P(profit) 0.72, adj growth 11.6 bp · B EV +5.93 (adj +3.09) on $50.00, P(profit) 0.6518, adj growth 28.0 bp · C EV +7.66 (adj +3.02) on $31.62, P(profit) 0.6501, adj growth 26.6 bp · R EV +0.75 (adj +0.29) on $8.00, P(profit) 0.7494, adj growth 10.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT19COLPHI-PHI|yes == KXNHLGAME-26OCT19COLPHI-COL|no

## SJS @ TOR  ·  10000 joint draws  ·  436 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_SJS_win | p_overtime | goals | shots TOR/SJS | TOR/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.54 | 0.46 | 0.00 | 6.06 | 27.8/28.2 | 24.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.48 | 5.96 | 28.3/28.4 | 25.1/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.55 | 0.45 | 0.00 | 9.33 | 29.7/29.8 | 23.9/23.3 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.090 | 0.47 | 0.53 | 0.00 | 5.97 | 22.5/33.5 | 29.7/19.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.47 | 0.53 | 0.45 | 5.91 | 22.5/33.8 | 30.4/19.3 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.061 | 0.45 | 0.55 | 0.00 | 9.19 | 24.1/35.6 | 28.7/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ goals NO | 78 | 0.818 | 0.807 | +0.026 | +0.015 | $18.54 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 11 | 0.144 | 0.128 | +0.027 | +0.011 | $2.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 20 | 0.233 | 0.223 | +0.022 | +0.012 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-5|no; why: higher confidence-adjusted growth (2.98 vs 1.40 bp); despite a smaller raw edge (+0.026 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.004 vs 0.391); alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: SJS offense succeeds (4+ goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT19SJTOR-TORCSISSONS15-1|yes; why: higher confidence-adjusted growth (2.64 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.058/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: TOR offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (1.95 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.034/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3899): highest fidelity KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3893): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis TOR:OFFENSE_4PLUS (p 0.4224): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3899, phi -0.192)
- KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3635, phi -0.168)
- KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3893, phi -0.231)

portfolios: A EV +2.56 (adj +1.23) on $28.11, P(profit) 0.307, adj growth 9.6 bp · B EV +1.64 (adj +0.84) on $25.11, P(profit) 0.2873, adj growth 7.3 bp · C EV +0.39 (adj +0.22) on $3.75, P(profit) 0.2329, adj growth 1.9 bp · R EV +0.16 (adj +0.09) on $5.00, P(profit) 0.8176, adj growth 3.3 bp

## PIT @ UTA  ·  10000 joint draws  ·  494 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.624 / away 0.376

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_PIT_win | p_overtime | goals | shots UTA/PIT | UTA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.63 | 0.37 | 0.00 | 6.06 | 27.4/27.2 | 24.3/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.47 | 5.96 | 27.3/27.3 | 24.1/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.64 | 0.36 | 0.00 | 9.4 | 28.8/28.6 | 23.2/21.8 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.083 | 0.65 | 0.35 | 0.00 | 6.06 | 32.1/21.3 | 18.5/27.6 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.56 | 0.44 | 0.50 | 5.96 | 31.9/21.5 | 18.4/28.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.070 | 0.69 | 0.31 | 0.00 | 9.31 | 34.0/23.1 | 18.4/26.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack McBain: 1+ goals YES | 13 | 0.167 | 0.155 | +0.029 | +0.018 | $4.72 | FUNDED_RESEARCH | $2 | UTA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 20 | 0.245 | 0.230 | +0.033 | +0.018 | $5.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 27 | 0.316 | 0.303 | +0.033 | +0.020 | $6.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.149 | 0.141 | +0.022 | +0.013 | $3.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (5.60 vs 4.46 bp); despite a smaller raw edge (+0.029 vs +0.033/contract); relationships: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: UTA offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19PITUTA-UTAJMARINO6-1|yes; why: higher confidence-adjusted growth (4.46 vs 0.04 bp); despite a smaller raw edge (+0.033 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0020 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: UTA offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (4.18 vs 3.54 bp); relationships: KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes has the higher standalone adjusted growth (4.18 vs 3.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis UTA:OFFENSE_4PLUS (p 0.4904): highest fidelity KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.3725): highest fidelity KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:SUPPRESSED (p 0.4003): highest fidelity KXNHLAST-26OCT19PITUTA-PITSCROSBY87-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT19PITUTA-PITSCROSBY87-2|no (same contract)
- KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.2959, phi -0.164)
- KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.2959, phi -0.212)
- KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4003, phi -0.256)
- KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4003, phi -0.189)

portfolios: A EV +3.70 (adj +1.57) on $40.63, P(profit) 0.4701, adj growth 13.7 bp · B EV +3.28 (adj +1.94) on $20.56, P(profit) 0.6329, adj growth 16.8 bp · C EV +2.56 (adj +1.26) on $33.03, P(profit) 0.4328, adj growth 11.2 bp · R EV +0.43 (adj +0.25) on $2.00, P(profit) 0.1673, adj growth 7.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
