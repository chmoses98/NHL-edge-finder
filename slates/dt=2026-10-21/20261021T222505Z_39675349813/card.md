# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T22:25:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +15.76 | +4.09 | +17.75 | 0.637 | -37.69 | -46.06 | 34.07 |
| B thesis-diversified (joint) ← optimiser card | 86.73 | +10.73 | +5.69 | +4.90 | 0.665 | -28.50 | -54.30 | 50.92 |
| C best expression per thesis | 81.90 | +10.99 | +5.57 | +4.80 | 0.711 | -29.67 | -49.98 | 49.93 |
| R FUNDED research stakes | 15.00 | +1.58 | +0.87 | +1.02 | 0.688 | -7.26 | -8.89 | 0.00 |

## PHI @ BUF  ·  10000 joint draws  ·  528 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.645 / away 0.355

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_PHI_win | p_overtime | goals | shots BUF/PHI | BUF/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.123 | 0.65 | 0.35 | 0.00 | 5.98 | 32.5/20.8 | 18.1/28.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.54 | 0.46 | 0.48 | 5.87 | 32.2/21.0 | 17.8/28.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.60 | 0.40 | 0.00 | 6.02 | 26.9/26.6 | 23.5/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.48 | 5.88 | 27.0/26.7 | 23.5/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.60 | 0.40 | 0.00 | 9.24 | 28.5/28.0 | 22.6/21.7 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.067 | 0.64 | 0.36 | 0.00 | 9.21 | 34.0/22.4 | 17.6/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tage Thompson: 1+ goals NO | 61 | 0.682 | 0.663 | +0.055 | +0.036 | $20.00 | FUNDED_RESEARCH | $5 | BUF:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 1.5 goals NO | 58 | 0.669 | 0.622 | +0.072 | +0.025 | $6.62 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo over 3.5 goals scored NO | 50 | 0.588 | 0.542 | +0.071 | +0.024 | $3.39 | FUNDED_RESEARCH | $1 | BUF:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 71 | 0.785 | 0.745 | +0.061 | +0.021 | $6.99 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no; why: higher confidence-adjusted growth (12.24 vs 8.24 bp); despite a smaller raw edge (+0.055 vs +0.129/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: REINFORCING (phi 0.174); KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: REINFORCING (phi 0.241); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: REINFORCING (phi 0.155); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no; why: higher confidence-adjusted growth (5.61 vs 5.09 bp); relationships: KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.174); KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: REINFORCING (phi 0.553); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: DUPLICATIVE (phi 0.743); failure: BUF wins by 2+
- **Buffalo over 3.5 goals scored NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.80 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.241); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: REINFORCING (phi 0.553); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: REINFORCING (phi 0.515); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no has the higher standalone adjusted growth (5.61 vs 4.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.743); they share one thesis budget; relationships: KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.155); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: DUPLICATIVE (phi 0.743); KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: REINFORCING (phi 0.515); failure: BUF wins by 2+

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis BUF:SUPPRESSED (p 0.3786): highest fidelity KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no — Broad expression KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.80 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:TIGHT (p 0.448): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3051): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4027, phi -0.245)
- KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3313, phi -1.0)
- KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4027, phi -0.981)
- KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3313, phi -0.743)
- override: Broad expression KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.80 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.97 (adj +1.91) on $50.00, P(profit) 0.5959, adj growth 14.2 bp · B EV +3.61 (adj +1.78) on $37.00, P(profit) 0.5813, adj growth 15.8 bp · C EV +3.29 (adj +1.68) on $32.71, P(profit) 0.4941, adj growth 14.9 bp · R EV +0.99 (adj +0.47) on $10.00, P(profit) 0.5652, adj growth 16.6 bp

## FLA @ OTT  ·  10000 joint draws  ·  462 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_FLA_win | p_overtime | goals | shots OTT/FLA | OTT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.62 | 0.38 | 0.00 | 6.0 | 26.3/26.1 | 23.2/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.46 | 5.92 | 26.9/26.7 | 23.5/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.65 | 0.35 | 0.00 | 9.23 | 28.1/27.9 | 22.7/21.4 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.087 | 0.68 | 0.32 | 0.00 | 5.96 | 31.4/20.9 | 18.4/27.0 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.58 | 0.42 | 0.46 | 5.86 | 31.6/21.1 | 17.9/28.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.058 | 0.50 | 0.50 | 0.48 | 2.8 | 25.0/24.8 | 23.3/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 63 | 0.723 | 0.698 | +0.077 | +0.052 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 15 | 0.195 | 0.181 | +0.036 | +0.023 | $6.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 58 | 0.671 | 0.623 | +0.074 | +0.026 | $19.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Nick Cousins: 1+ goals YES | 9 | 0.117 | 0.109 | +0.021 | +0.013 | $3.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: higher confidence-adjusted growth (26.20 vs 3.81 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: FLA offense succeeds (4+ goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT6|yes; why: higher confidence-adjusted growth (8.27 vs 5.17 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.895 vs 0.299); relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: OTT offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT21FLAOTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (6.23 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.055); failure: OTT offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes has the higher standalone adjusted growth (8.27 vs 4.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.055); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4671): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.424): highest fidelity KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.3486): highest fidelity KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no (same contract)
- KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3092, phi -0.233)
- KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3486, phi -0.195)
- KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.424, phi -0.252)
- KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3486, phi -0.142)

portfolios: A EV +5.80 (adj +2.18) on $50.00, P(profit) 0.6608, adj growth 19.9 bp · B EV +7.12 (adj +3.91) on $49.73, P(profit) 0.6203, adj growth 35.1 bp · C EV +7.70 (adj +3.89) on $49.19, P(profit) 0.6231, adj growth 35.0 bp · R EV +0.59 (adj +0.40) on $5.00, P(profit) 0.7229, adj growth 15.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
