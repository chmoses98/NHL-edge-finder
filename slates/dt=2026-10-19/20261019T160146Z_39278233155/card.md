# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T16:01:46Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +28.82 | +10.23 | +25.86 | 0.668 | -43.54 | -60.85 | 85.44 |
| B thesis-diversified (joint) ← optimiser card | 136.51 | +24.15 | +14.58 | +14.96 | 0.599 | -48.30 | -65.21 | 126.59 |
| C best expression per thesis | 96.90 | +21.32 | +11.18 | +8.23 | 0.609 | -39.63 | -56.60 | 96.20 |
| R FUNDED research stakes | 24.00 | +3.88 | +2.18 | +1.00 | 0.621 | -10.42 | -12.57 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  414 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_ANA_win | p_overtime | goals | shots NYR/ANA | NYR/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.57 | 0.43 | 0.00 | 6.05 | 26.8/27.0 | 23.7/22.9 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.109 | 0.49 | 0.51 | 0.00 | 6.04 | 21.3/32.4 | 28.7/17.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.43 | 5.95 | 26.9/27.5 | 24.3/23.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.51 | 0.49 | 0.49 | 5.91 | 21.4/32.7 | 29.4/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 9.38 | 28.4/28.9 | 23.3/21.8 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.077 | 0.49 | 0.51 | 0.00 | 9.22 | 22.8/34.1 | 27.4/17.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 14 | 0.228 | 0.205 | +0.080 | +0.056 | $14.56 | FUNDED_RESEARCH | $4 | ANA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 8 | 0.121 | 0.111 | +0.036 | +0.026 | $6.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 10 | 0.134 | 0.124 | +0.028 | +0.018 | $4.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Taylor Raddysh: 1+ goals YES | 9 | 0.119 | 0.108 | +0.024 | +0.013 | $3.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (53.11 vs 8.06 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (53.11 vs 17.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (53.11 vs 7.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.028); failure: ANA offense suppressed (<= 2 goals)
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes; why: higher confidence-adjusted growth (3.89 vs 1.30 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.893 vs 0.767); alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.028); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3817): highest fidelity KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3536): highest fidelity KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.4336): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4002, phi -0.236)
- KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4002, phi -0.152)
- KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4002, phi -0.169)
- KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3536, phi -0.154)

portfolios: A EV +9.84 (adj +5.15) on $38.41, P(profit) 0.4515, adj growth 45.1 bp · B EV +12.35 (adj +8.55) on $28.35, P(profit) 0.4823, adj growth 72.8 bp · C EV +9.03 (adj +5.94) on $29.82, P(profit) 0.2281, adj growth 50.6 bp · R EV +2.15 (adj +1.52) on $4.00, P(profit) 0.2281, adj growth 50.9 bp

## COL @ PHI  ·  10000 joint draws  ·  378 bet sides mapped, 32 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_COL_win | p_overtime | goals | shots PHI/COL | PHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.140 | 0.38 | 0.62 | 0.00 | 5.97 | 21.2/33.5 | 29.2/18.4 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.47 | 0.53 | 0.47 | 5.91 | 21.5/33.4 | 30.1/18.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.48 | 0.52 | 0.00 | 5.98 | 26.9/27.7 | 24.0/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.48 | 0.52 | 0.50 | 5.88 | 27.0/27.9 | 24.5/23.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.079 | 0.35 | 0.65 | 0.00 | 9.09 | 22.5/35.5 | 27.8/17.9 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.072 | 0.39 | 0.61 | 0.00 | 3.42 | 20.0/32.0 | 29.8/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cale Makar: 1+ goals NO | 77 | 0.837 | 0.818 | +0.054 | +0.035 | $15.45 | FUNDED_RESEARCH | $4 | COL:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 54 | 0.620 | 0.598 | +0.063 | +0.040 | $14.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 67 | 0.798 | 0.711 | +0.112 | +0.026 | $16.10 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (16.15 vs 14.35 bp); despite a smaller raw edge (+0.054 vs +0.063/contract); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT19COLPHI-COL3|no: MOSTLY_INDEPENDENT (phi 0.129); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT19COLPHI-PHI2|yes; why: higher confidence-adjusted growth (14.35 vs 9.96 bp); despite a smaller raw edge (+0.063 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.001 vs 0.549); relationships: KXNHLGOAL-26OCT19COLPHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.191); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes; why: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes has the higher standalone adjusted growth (38.70 vs 6.88 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.139); relationships: KXNHLGOAL-26OCT19COLPHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.129); KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: REINFORCING (phi 0.191); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.3165): highest fidelity KXNHLTEAMTOTAL-26OCT19COLPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT19COLPHI-PHINACCIARI52-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SCORES_FIRST (p 0.4723): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2348): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no (same contract)
- KXNHLGOAL-26OCT19COLPHI-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3886, phi -0.189)
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3886, phi -0.278)
- KXNHLSPREAD-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.3 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3222, phi -0.73)

portfolios: A EV +10.45 (adj +1.48) on $38.41, P(profit) 0.582, adj growth 12.6 bp · B EV +5.35 (adj +2.35) on $46.10, P(profit) 0.5319, adj growth 21.7 bp · C EV +7.33 (adj +2.92) on $21.56, P(profit) 0.6464, adj growth 25.3 bp · R EV +1.10 (adj +0.37) on $9.00, P(profit) 0.6867, adj growth 13.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT19COLPHI-COL|no == KXNHLGAME-26OCT19COLPHI-PHI|yes

## SJS @ TOR  ·  10000 joint draws  ·  422 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_SJS_win | p_overtime | goals | shots TOR/SJS | TOR/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.53 | 0.47 | 0.00 | 6.06 | 28.2/28.5 | 25.1/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.46 | 5.95 | 28.0/28.3 | 25.0/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.57 | 0.43 | 0.00 | 9.4 | 29.4/29.8 | 24.1/22.9 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.086 | 0.51 | 0.49 | 0.00 | 6.03 | 22.2/33.8 | 30.2/18.8 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.48 | 0.52 | 0.47 | 5.89 | 22.7/33.5 | 30.1/19.5 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.059 | 0.48 | 0.52 | 0.00 | 9.28 | 23.9/35.5 | 28.5/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.144 | 0.136 | +0.028 | +0.019 | $5.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ goals NO | 78 | 0.825 | 0.812 | +0.033 | +0.020 | $20.00 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 20 | 0.239 | 0.228 | +0.028 | +0.017 | $5.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Full Game: Over 5.5 goals scored NO | 35 | 0.407 | 0.376 | +0.041 | +0.010 | $5.40 | FUNDED_RESEARCH | $2 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT19SJTOR-SJ3|no; why: higher confidence-adjusted growth (7.49 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTOTAL-26OCT19SJTOR-6|no: INTENTIONAL_DIVERSIFIER (phi -0.115); failure: TOR offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (5.58 vs 3.32 bp); despite a smaller raw edge (+0.033 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLTOTAL-26OCT19SJTOR-6|no: MOSTLY_INDEPENDENT (phi 0.126); failure: SJS offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19SJTOR-SJICHERNYSHOV92-1|yes; why: higher confidence-adjusted growth (3.68 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLTOTAL-26OCT19SJTOR-6|no: INTENTIONAL_DIVERSIFIER (phi -0.166); failure: SJS offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-5|no; why: Broad expression KXNHLTOTAL-26OCT19SJTOR-6|no selected over broad KXNHLTOTAL-26OCT19SJTOR-5|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.115); KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.126); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.166); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3864): highest fidelity KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.4007): highest fidelity KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no (same contract)
- thesis GAME:LOW_EVENT (p 0.2165): highest fidelity KXNHLTOTAL-26OCT19SJTOR-6|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT19SJTOR-5|no — Broad expression KXNHLTOTAL-26OCT19SJTOR-6|no selected over broad KXNHLTOTAL-26OCT19SJTOR-5|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3655, phi -0.179)
- KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3864, phi -0.183)
- KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4007, phi -0.238)
- KXNHLTOTAL-26OCT19SJTOR-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2852, phi -0.523)
- override: Broad expression KXNHLTOTAL-26OCT19SJTOR-6|no selected over broad KXNHLTOTAL-26OCT19SJTOR-5|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.33 (adj +1.24) on $38.41, P(profit) 0.4011, adj growth 8.4 bp · B EV +3.44 (adj +1.98) on $36.42, P(profit) 0.5919, adj growth 17.3 bp · C EV +2.68 (adj +1.02) on $23.82, P(profit) 0.3922, adj growth 9.0 bp · R EV +0.43 (adj +0.18) on $7.00, P(profit) 0.3591, adj growth 6.2 bp

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
| Lawson Crouse: 1+ goals YES | 20 | 0.246 | 0.231 | +0.035 | +0.020 | $5.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.151 | 0.142 | +0.023 | +0.014 | $3.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 13 | 0.164 | 0.152 | +0.026 | +0.014 | $3.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 62 | 0.669 | 0.654 | +0.032 | +0.018 | $12.01 | FUNDED_RESEARCH | $4 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT19PITUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (5.02 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: UTA offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19PITUTA-PITRRAKELL67-2|yes; why: higher confidence-adjusted growth (3.98 vs 1.62 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.867 vs 0.765); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: PIT offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (5.02 vs 3.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: UTA offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19PITUTA-UTACKELLER9-2|no; why: higher confidence-adjusted growth (2.89 vs 0.19 bp); despite a smaller raw edge (+0.032 vs +0.063/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.493): highest fidelity KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.3668): highest fidelity KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3006): highest fidelity KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no (same contract)
- KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3006, phi -0.212)
- KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4145, phi -0.196)
- KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3006, phi -0.168)
- KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.493, phi -0.229)

portfolios: A EV +4.20 (adj +2.36) on $34.76, P(profit) 0.4678, adj growth 19.3 bp · B EV +3.01 (adj +1.70) on $25.64, P(profit) 0.4678, adj growth 14.8 bp · C EV +2.27 (adj +1.30) on $21.70, P(profit) 0.3594, adj growth 11.4 bp · R EV +0.20 (adj +0.11) on $4.00, P(profit) 0.6686, adj growth 3.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
