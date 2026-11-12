# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-12T02:50:36Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +15.74 | +5.05 | +13.01 | 0.629 | -40.94 | -59.07 | 40.22 |
| B thesis-diversified (joint) ← optimiser card | 86.44 | +14.02 | +7.76 | +3.03 | 0.595 | -40.61 | -47.65 | 67.11 |
| C best expression per thesis | 78.79 | +11.25 | +4.91 | +8.88 | 0.618 | -33.00 | -46.91 | 43.12 |
| R FUNDED research stakes | 11.00 | +1.12 | +0.61 | -0.61 | 0.408 | -7.12 | -7.12 | 0.00 |

## NSH @ ANA  ·  10000 joint draws  ·  474 bet sides mapped, 26 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.565 / away 0.435

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_NSH_win | p_overtime | goals | shots ANA/NSH | ANA/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.73 | 0.27 | 0.00 | 6.07 | 28.5/28.1 | 25.5/23.9 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.117 | 0.75 | 0.25 | 0.00 | 6.01 | 33.8/22.1 | 19.8/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.116 | 0.72 | 0.28 | 0.00 | 9.48 | 30.0/29.5 | 24.7/22.2 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.108 | 0.80 | 0.20 | 0.00 | 9.45 | 35.5/23.5 | 19.4/26.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.55 | 0.45 | 0.46 | 6.04 | 28.4/27.9 | 24.7/25.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.57 | 0.43 | 0.47 | 5.94 | 34.2/22.5 | 19.3/30.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Wilsby: 1+ goals YES | 4 | 0.076 | 0.065 | +0.034 | +0.022 | $4.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 33 | 0.408 | 0.387 | +0.062 | +0.042 | $15.65 | FUNDED_RESEARCH | $4 | ANA:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 11 | 0.155 | 0.143 | +0.038 | +0.026 | $6.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 62 | 0.692 | 0.673 | +0.056 | +0.037 | $20.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV11NSHANA-NSHAWILSBY2-1|yes; why: higher confidence-adjusted growth (24.42 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV11NSHANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: NSH offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11NSHANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (16.77 vs 10.80 bp); relationships: KXNHLGOAL-26NOV11NSHANA-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV11NSHANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes has the higher standalone adjusted growth (16.77 vs 13.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV11NSHANA-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: ANA offense suppressed (<= 2 goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11NSHANA-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (12.70 vs 6.26 bp); despite a smaller raw edge (+0.056 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV11NSHANA-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV11NSHANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12.
- thesis ANA:OFFENSE_4PLUS (p 0.5684): highest fidelity KXNHLSPREAD-26NOV11NSHANA-NSH3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:SUPPRESSED (p 0.4536): highest fidelity KXNHLTEAMTOTAL-26NOV11NSHANA-NSH4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.4517): highest fidelity KXNHLSPREAD-26NOV11NSHANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV11NSHANA-ANA3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV11NSHANA-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4536, phi -0.152)
- KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2403, phi -0.249)
- KXNHLGOAL-26NOV11NSHANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2403, phi -0.143)
- KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3214, phi -0.246)

portfolios: A EV +8.16 (adj +2.82) on $50.00, P(profit) 0.5542, adj growth 22.1 bp · B EV +10.46 (adj +6.93) on $47.07, P(profit) 0.4432, adj growth 59.8 bp · C EV +5.31 (adj +3.25) on $38.30, P(profit) 0.5336, adj growth 28.6 bp · R EV +0.72 (adj +0.48) on $4.00, P(profit) 0.408, adj growth 16.8 bp

## PIT @ SJS  ·  10000 joint draws  ·  464 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.429 / away 0.571

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_PIT_win | p_overtime | goals | shots SJS/PIT | SJS/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.49 | 0.51 | 0.00 | 6.03 | 27.4/27.6 | 23.8/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.48 | 0.52 | 0.47 | 5.95 | 27.7/28.0 | 24.6/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.49 | 0.51 | 0.00 | 9.37 | 29.2/29.3 | 22.9/23.0 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.077 | 0.39 | 0.61 | 0.00 | 6.06 | 22.0/32.5 | 28.2/19.1 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.47 | 0.53 | 0.46 | 5.91 | 22.3/33.1 | 29.6/19.1 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.057 | 0.43 | 0.57 | 0.00 | 9.23 | 23.3/34.7 | 27.9/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alexander Wennberg: 1+ assists NO | 66 | 0.771 | 0.692 | +0.095 | +0.017 | $16.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Pittsburgh over 3.5 goals scored NO | 50 | 0.569 | 0.532 | +0.051 | +0.015 | $3.25 | FUNDED_RESEARCH | $1 | PIT:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ben Kindel: 1+ goals NO | 76 | 0.794 | 0.785 | +0.022 | +0.012 | $11.13 | FUNDED_RESEARCH | $3 | PIT:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Pittsburgh wins by over 1.5 goals NO | 64 | 0.703 | 0.669 | +0.047 | +0.013 | $8.52 | FUNDED_RESEARCH | $3 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Alexander Wennberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV11PITSJ-7|no; why: higher confidence-adjusted growth (2.75 vs 0.93 bp); wins across more scripts (relative breadth 1.007 vs 0.739); relationships: KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV11PITSJ-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: SJS offense succeeds (4+ goals)
- **Pittsburgh over 3.5 goals scored NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no; why: Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV11PITSJ-PITBKINDEL81-1|no: REINFORCING (phi 0.182); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: REINFORCING (phi 0.531); failure: PIT offense succeeds (4+ goals)
- **Ben Kindel: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no; why: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no has the higher standalone adjusted growth (4.84 vs 1.76 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.052); relationships: KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: REINFORCING (phi 0.182); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: MOSTLY_INDEPENDENT (phi 0.113); failure: PIT offense succeeds (4+ goals)
- **Pittsburgh wins by over 1.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no; why: Broad expression KXNHLSPREAD-26NOV11PITSJ-PIT2|no selected over player prop KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.94 vs 0.44 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no: INTENTIONAL_DIVERSIFIER (phi -0.131); KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: REINFORCING (phi 0.531); KXNHLGOAL-26NOV11PITSJ-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi 0.113); failure: PIT wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4037): highest fidelity KXNHLSPREAD-26NOV11PITSJ-PIT2|no [DIRECT], best adjusted EV KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes — Broad expression KXNHLSPREAD-26NOV11PITSJ-PIT2|no selected over player prop KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.94 vs 0.44 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis PIT:SUPPRESSED (p 0.3636): highest fidelity KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no — Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis SJS:SUPPRESSED (p 0.3833): highest fidelity KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no (same contract)
- KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4037, phi -0.221)
- KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4203, phi -0.978)
- KXNHLGOAL-26NOV11PITSJ-PITBKINDEL81-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4203, phi -0.181)
- KXNHLSPREAD-26NOV11PITSJ-PIT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.2971, phi -1.0)
- override: Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26NOV11PITSJ-PIT2|no selected over player prop KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.94 vs 0.44 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +7.58 (adj +2.23) on $50.00, P(profit) 0.5315, adj growth 18.1 bp · B EV +3.56 (adj +0.83) on $39.37, P(profit) 0.5193, adj growth 7.3 bp · C EV +5.94 (adj +1.66) on $40.49, P(profit) 0.6348, adj growth 14.5 bp · R EV +0.40 (adj +0.13) on $7.00, P(profit) 0.5794, adj growth 4.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
