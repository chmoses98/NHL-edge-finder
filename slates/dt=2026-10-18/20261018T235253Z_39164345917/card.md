# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T23:52:53Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +12.84 | +1.79 | +9.58 | 0.598 | -33.82 | -33.82 | 12.49 |
| B thesis-diversified (joint) ← optimiser card | 44.66 | +3.64 | +1.65 | +7.26 | 0.523 | -22.58 | -24.25 | 15.10 |
| C best expression per thesis | 42.94 | +7.40 | +2.11 | +17.81 | 0.614 | -21.71 | -29.61 | 18.89 |
| R FUNDED research stakes | 10.00 | +0.91 | +0.36 | +3.90 | 0.649 | -5.74 | -10.00 | 0.00 |

## CAR @ CGY  ·  10000 joint draws  ·  470 bet sides mapped, 29 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.343 / away 0.657

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_CAR_win | p_overtime | goals | shots CGY/CAR | CGY/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.140 | 0.39 | 0.61 | 0.00 | 5.96 | 21.9/34.6 | 30.2/19.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.47 | 0.53 | 0.48 | 5.84 | 21.9/34.4 | 31.1/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.47 | 0.53 | 0.00 | 6.05 | 27.6/28.6 | 24.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.49 | 0.51 | 0.46 | 5.92 | 27.6/28.6 | 25.1/24.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.088 | 0.36 | 0.64 | 0.00 | 9.21 | 23.3/36.0 | 28.5/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.44 | 0.56 | 0.00 | 9.19 | 29.1/30.2 | 23.6/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nikolaj Ehlers: 1+ goals NO | 72 | 0.785 | 0.768 | +0.051 | +0.034 | $16.21 | FUNDED_RESEARCH | $5 | CAR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 66 | 0.719 | 0.702 | +0.044 | +0.026 | $13.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Carolina over 4.5 goals scored NO | 69 | 0.772 | 0.724 | +0.068 | +0.019 | $6.65 | FUNDED_RESEARCH | $2 | CGY:WINS | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 69 | 0.792 | 0.723 | +0.087 | +0.018 | $8.01 | FUNDED_RESEARCH | $3 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no; why: higher confidence-adjusted growth (12.73 vs 6.92 bp); relationships: KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no: REINFORCING (phi 0.212); KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.165); failure: CAR offense succeeds (4+ goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no; why: Player prop expression KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.86 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no: REINFORCING (phi 0.198); KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.164); failure: CAR offense succeeds (4+ goals)
- **Carolina over 4.5 goals scored NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no; why: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no has the higher standalone adjusted growth (6.27 vs 3.73 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.241); relationships: KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no: REINFORCING (phi 0.212); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: REINFORCING (phi 0.198); KXNHLSPREAD-26OCT18CARCGY-CAR3|no: REINFORCING (phi 0.536); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no; why: KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no has the higher standalone adjusted growth (6.27 vs 3.24 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.198); relationships: KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no: REINFORCING (phi 0.165); KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: REINFORCING (phi 0.164); KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no: REINFORCING (phi 0.536); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CAR:SUPPRESSED (p 0.3809): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no — Player prop expression KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.86 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis CGY:WINS (p 0.454): highest fidelity KXNHLSPREAD-26OCT18CARCGY-CAR2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT18CARCGY-CAR2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no kept
- thesis CGY:OFFENSE_4PLUS (p 0.3323): highest fidelity KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3|yes (same contract)
- KXNHLGOAL-26OCT18CARCGY-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4107, phi -0.22)
- KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4107, phi -0.233)
- KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4107, phi -0.65)
- KXNHLSPREAD-26OCT18CARCGY-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.7 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3216, phi -0.744)
- override: Player prop expression KXNHLGOAL-26OCT18CARCGY-CARSAHO20-1|no selected over player prop KXNHLAST-26OCT18CARCGY-CARSAHO20-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.86 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT18CARCGY-CAR2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5|no kept

portfolios: A EV +12.84 (adj +1.79) on $50.00, P(profit) 0.5979, adj growth 12.5 bp · B EV +3.64 (adj +1.65) on $44.66, P(profit) 0.5233, adj growth 15.1 bp · C EV +7.40 (adj +2.11) on $42.94, P(profit) 0.6138, adj growth 18.9 bp · R EV +0.91 (adj +0.36) on $10.00, P(profit) 0.6494, adj growth 12.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT18CARCGY-CAR|no == KXNHLGAME-26OCT18CARCGY-CGY|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
