# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T01:28:55Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +34.71 | +8.47 | +35.75 | 0.714 | -50.73 | -66.36 | 65.31 |
| B thesis-diversified (joint) ← optimiser card | 129.30 | +25.70 | +15.52 | +12.70 | 0.571 | -54.72 | -69.37 | 133.16 |
| C best expression per thesis | 109.46 | +26.66 | +11.52 | +17.74 | 0.632 | -40.01 | -50.38 | 99.55 |
| R FUNDED research stakes | 20.00 | +2.15 | +0.89 | +2.66 | 0.667 | -6.00 | -12.81 | 0.00 |

## DET @ SEA  ·  10000 joint draws  ·  450 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.478 / away 0.522

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_DET_win | p_overtime | goals | shots SEA/DET | SEA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.02 | 27.8/28.1 | 25.1/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.48 | 5.92 | 27.9/28.3 | 25.0/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.64 | 0.36 | 0.00 | 9.26 | 29.6/29.9 | 24.5/22.6 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 6.04 | 22.4/33.7 | 30.3/18.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.50 | 0.50 | 0.47 | 5.87 | 22.2/33.6 | 30.3/19.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.56 | 0.44 | 0.00 | 3.45 | 26.8/27.1 | 25.3/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Winterton: 1+ goals YES | 12 | 0.169 | 0.154 | +0.042 | +0.027 | $6.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 11 | 0.153 | 0.141 | +0.036 | +0.024 | $6.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Dylan Larkin: 1+ goals NO | 68 | 0.741 | 0.725 | +0.046 | +0.030 | $20.00 | FUNDED_RESEARCH | $5 | DET:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ goals YES | 17 | 0.213 | 0.200 | +0.033 | +0.020 | $5.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: higher confidence-adjusted growth (13.98 vs 11.45 bp); despite a smaller raw edge (+0.042 vs +0.113/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT20DETSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.027); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: higher confidence-adjusted growth (12.40 vs 11.45 bp); despite a smaller raw edge (+0.037 vs +0.113/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT20DETSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **Dylan Larkin: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20DETSEA-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (9.09 vs 6.02 bp); despite a smaller raw edge (+0.046 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT20DETSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: DET offense succeeds (4+ goals)
- **Kaapo Kakko: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: Player prop expression KXNHLGOAL-26OCT20DETSEA-SEAKKAKKO84-1|yes selected over player prop KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.31 vs 0.44 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [DIRECT], best adjusted EV KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes — Player prop expression KXNHLGOAL-26OCT20DETSEA-SEAKKAKKO84-1|yes selected over player prop KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.31 vs 0.44 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis DET:SUPPRESSED (p 0.4539): highest fidelity KXNHLTEAMTOTAL-26OCT20DETSEA-DET4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.58): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT20DETSEA-SEAKKAKKO84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.182)
- KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.164)
- KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3287, phi -0.226)
- KXNHLGOAL-26OCT20DETSEA-SEAKKAKKO84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.21)
- override: Player prop expression KXNHLGOAL-26OCT20DETSEA-SEAKKAKKO84-1|yes selected over player prop KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.31 vs 0.44 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +12.75 (adj +3.53) on $50.00, P(profit) 0.5286, adj growth 27.4 bp · B EV +6.55 (adj +4.22) on $38.60, P(profit) 0.404, adj growth 36.7 bp · C EV +6.77 (adj +2.37) on $33.48, P(profit) 0.4842, adj growth 20.9 bp · R EV +0.33 (adj +0.21) on $5.00, P(profit) 0.7414, adj growth 7.7 bp

## CAR @ VAN  ·  10000 joint draws  ·  452 bet sides mapped, 34 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.282 / away 0.718

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CAR_win | p_overtime | goals | shots VAN/CAR | VAN/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.171 | 0.37 | 0.63 | 0.00 | 6.02 | 20.8/34.0 | 29.5/18.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.144 | 0.48 | 0.52 | 0.48 | 5.95 | 21.1/34.6 | 31.1/17.8 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.128 | 0.37 | 0.63 | 0.00 | 9.39 | 22.5/36.1 | 28.6/17.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.082 | 0.42 | 0.58 | 0.00 | 6.04 | 27.0/28.3 | 24.3/23.8 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.073 | 0.41 | 0.59 | 0.00 | 3.47 | 19.8/32.7 | 30.3/18.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.48 | 0.52 | 0.49 | 5.98 | 26.7/28.0 | 24.7/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Filip Chytil: 1+ goals YES | 16 | 0.249 | 0.225 | +0.080 | +0.056 | $14.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 49 | 0.657 | 0.545 | +0.149 | +0.038 | $6.06 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 62 | 0.769 | 0.669 | +0.133 | +0.033 | $10.65 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 62 | 0.685 | 0.668 | +0.049 | +0.031 | $17.91 | FUNDED_RESEARCH | $5 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT20CARVAN-VAN2|yes; why: higher confidence-adjusted growth (47.34 vs 25.62 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; relationships: KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.164); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VAN offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (47.34 vs 12.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.164); they share one thesis budget; relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: REINFORCING (phi 0.164); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: DUPLICATIVE (phi 0.757); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: REINFORCING (phi 0.187); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (47.34 vs 10.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.134); they share one thesis budget; relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.134); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: DUPLICATIVE (phi 0.757); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: REINFORCING (phi 0.162); failure: CAR wins by 2+
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20CARVAN-VAN3|yes; why: KXNHLSPREAD-26OCT20CARVAN-VAN3|yes has the higher standalone adjusted growth (25.58 vs 9.26 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.135); relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.187); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: REINFORCING (phi 0.162); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3652): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4391): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:SCORES_FIRST (p 0.4662): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4186, phi -0.236)
- KXNHLSPREAD-26OCT20CARVAN-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 17.2 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3434, phi -1.0)
- KXNHLSPREAD-26OCT20CARVAN-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.4 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3434, phi -0.757)
- KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.458, phi -0.245)

portfolios: A EV +15.75 (adj +3.61) on $50.00, P(profit) 0.5489, adj growth 26.1 bp · B EV +12.10 (adj +6.61) on $48.95, P(profit) 0.5943, adj growth 56.9 bp · C EV +14.18 (adj +7.28) on $25.98, P(profit) 0.368, adj growth 62.1 bp · R EV +1.60 (adj +0.55) on $10.00, P(profit) 0.5589, adj growth 19.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT20CARVAN-VAN|yes == KXNHLGAME-26OCT20CARVAN-CAR|no

## TBL @ VGK  ·  10000 joint draws  ·  490 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.502 / away 0.498

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TBL_win | p_overtime | goals | shots VGK/TBL | VGK/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.63 | 0.37 | 0.00 | 6.03 | 26.8/26.8 | 23.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.49 | 5.94 | 26.8/27.1 | 23.8/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.65 | 0.35 | 0.00 | 9.21 | 28.5/28.5 | 23.4/21.5 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.072 | 0.58 | 0.42 | 0.00 | 5.95 | 21.4/31.7 | 28.4/17.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.067 | 0.70 | 0.30 | 0.00 | 5.99 | 31.4/21.2 | 18.5/26.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.54 | 0.46 | 0.53 | 2.82 | 25.4/25.4 | 23.9/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 4 | 0.080 | 0.069 | +0.037 | +0.026 | $5.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Brett Howden: 1+ goals YES | 19 | 0.233 | 0.221 | +0.032 | +0.020 | $5.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 72 | 0.767 | 0.754 | +0.033 | +0.020 | $19.13 | FUNDED_RESEARCH | $5 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 65 | 0.696 | 0.682 | +0.030 | +0.016 | $11.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (34.44 vs 5.57 bp); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VGK offense suppressed (<= 2 goals)
- **Brett Howden: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: higher confidence-adjusted growth (5.57 vs 5.30 bp); despite a smaller raw edge (+0.032 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20TBVGK-4|no; why: higher confidence-adjusted growth (4.42 vs 0.17 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.007 vs 0.351); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no; why: Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis VGK:OFFENSE_4PLUS (p 0.4283): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis VGK:WINS (p 0.5848): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.4793): highest fidelity KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no — Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3602, phi -0.131)
- KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3602, phi -0.236)
- KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4283, phi -0.197)
- KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3048, phi -0.253)
- override: Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.21 (adj +1.33) on $50.00, P(profit) 0.7759, adj growth 11.9 bp · B EV +7.05 (adj +4.69) on $41.75, P(profit) 0.6546, adj growth 39.6 bp · C EV +5.70 (adj +1.87) on $50.00, P(profit) 0.6472, adj growth 16.5 bp · R EV +0.22 (adj +0.13) on $5.00, P(profit) 0.7669, adj growth 4.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
