# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-15T07:43:39Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +26.50 | +6.18 | +24.94 | 0.638 | -63.32 | -86.91 | 39.62 |
| B thesis-diversified (joint) ← optimiser card | 75.23 | +11.93 | +3.40 | +12.24 | 0.642 | -30.24 | -33.90 | 29.85 |
| C best expression per thesis | 68.23 | +10.00 | +2.90 | +9.18 | 0.618 | -25.87 | -33.86 | 25.47 |
| R FUNDED research stakes | 23.00 | +3.92 | +1.09 | +4.07 | 0.637 | -9.49 | -12.13 | 0.00 |

## BUF @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_BUF_win | p_overtime | goals | shots TOR/BUF | TOR/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.54 | 0.46 | 0.00 | 6.03 | 28.2/28.9 | 25.4/24.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.117 | 0.48 | 0.52 | 0.00 | 6.02 | 22.6/34.2 | 30.5/19.2 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.49 | 0.51 | 0.46 | 5.98 | 22.4/34.1 | 30.6/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.54 | 0.46 | 0.50 | 6.01 | 27.9/28.6 | 25.3/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.56 | 0.44 | 0.00 | 9.33 | 29.3/29.9 | 23.9/22.7 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.083 | 0.47 | 0.53 | 0.00 | 9.24 | 23.7/36.2 | 29.3/18.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYI_win | p_overtime | goals | shots OTT/NYI | OTT/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.62 | 0.38 | 0.00 | 6.01 | 26.8/26.8 | 23.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.54 | 0.46 | 0.48 | 5.93 | 27.0/26.7 | 23.6/23.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.087 | 0.65 | 0.35 | 0.00 | 5.96 | 32.0/21.4 | 18.7/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.61 | 0.39 | 0.00 | 9.27 | 28.3/28.2 | 22.6/21.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.56 | 0.44 | 0.46 | 5.88 | 32.0/21.2 | 18.1/28.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.61 | 0.39 | 0.00 | 3.53 | 25.4/25.5 | 23.9/23.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_SEA_win | p_overtime | goals | shots TBL/SEA | TBL/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.131 | 0.65 | 0.35 | 0.00 | 5.98 | 32.7/21.1 | 18.3/28.1 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.57 | 0.43 | 0.47 | 5.94 | 33.2/21.4 | 18.1/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.60 | 0.40 | 0.00 | 6.0 | 27.4/26.8 | 23.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.51 | 0.49 | 0.43 | 5.9 | 27.5/26.8 | 23.6/24.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.081 | 0.69 | 0.30 | 0.00 | 9.07 | 34.6/22.3 | 17.8/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.63 | 0.37 | 0.00 | 9.19 | 29.1/28.4 | 23.1/22.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Seattle wins by over 1.5 goals YES | 15 | 0.213 | 0.179 | +0.054 | +0.020 | $3.50 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 68 | 0.768 | 0.719 | +0.072 | +0.024 | $15.97 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 2.5 goals scored NO | 27 | 0.347 | 0.304 | +0.064 | +0.020 | $1.50 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: higher confidence-adjusted growth (6.52 vs 5.79 bp); despite a smaller raw edge (+0.054 vs +0.072/contract); relationships: KXNHLSPREAD-26OCT15SEATB-TB3|no: REINFORCING (phi 0.286); KXNHLTEAMTOTAL-26OCT15SEATB-TB3|no: REINFORCING (phi 0.47); failure: TBL wins (incl. OT/SO)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no; why: higher confidence-adjusted growth (5.79 vs 2.43 bp); wins across more scripts (relative breadth 1.009 vs 0.89); relationships: KXNHLSPREAD-26OCT15SEATB-SEA2|yes: REINFORCING (phi 0.286); KXNHLTEAMTOTAL-26OCT15SEATB-TB3|no: DUPLICATIVE (phi 0.401); failure: TBL wins by 2+
- **Tampa Bay over 2.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15SEATB-SEA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT15SEATB-SEA2|yes has the higher standalone adjusted growth (6.52 vs 4.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.470); they share one thesis budget; relationships: KXNHLSPREAD-26OCT15SEATB-SEA2|yes: REINFORCING (phi 0.47); KXNHLSPREAD-26OCT15SEATB-TB3|no: DUPLICATIVE (phi 0.401); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.13, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis SEA:WINS_BY_2PLUS (p 0.213): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no (same contract)
- thesis TBL:SUPPRESSED (p 0.3584): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no (same contract)
- thesis GAME:TIGHT (p 0.433): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no (same contract)
- KXNHLSPREAD-26OCT15SEATB-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS (p 0.5823, phi -0.614)
- KXNHLSPREAD-26OCT15SEATB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.354, phi -0.743)
- KXNHLTEAMTOTAL-26OCT15SEATB-TB3|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4235, phi -0.625)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT15SEATB-TB3|no kept

portfolios: A EV +7.17 (adj +1.88) on $44.12, P(profit) 0.6586, adj growth 11.4 bp · B EV +3.19 (adj +1.09) on $20.97, P(profit) 0.7677, adj growth 9.5 bp · C EV +3.11 (adj +1.07) on $21.04, P(profit) 0.7677, adj growth 9.4 bp · R EV +0.98 (adj +0.33) on $6.00, P(profit) 0.3949, adj growth 11.2 bp

## VAN @ FLA  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_VAN_win | p_overtime | goals | shots FLA/VAN | FLA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.60 | 0.40 | 0.00 | 6.06 | 27.3/26.7 | 23.6/23.3 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.112 | 0.66 | 0.34 | 0.00 | 6.01 | 32.7/21.1 | 18.4/28.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.50 | 0.50 | 0.49 | 5.96 | 27.5/27.0 | 23.6/24.2 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.56 | 0.44 | 0.46 | 5.92 | 32.9/21.2 | 18.0/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.60 | 0.40 | 0.00 | 9.32 | 28.8/28.3 | 22.6/22.1 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.086 | 0.67 | 0.33 | 0.00 | 9.17 | 34.3/22.5 | 17.8/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 1.5 goals NO | 50 | 0.652 | 0.550 | +0.134 | +0.032 | $2.93 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 63 | 0.772 | 0.676 | +0.126 | +0.030 | $14.20 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 3.5 goals scored YES | 24 | 0.365 | 0.277 | +0.113 | +0.025 | $4.32 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida over 2.5 goals scored NO | 24 | 0.320 | 0.275 | +0.067 | +0.022 | $3.80 | FUNDED_RESEARCH | $1 | FLA:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Florida wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT15VANFLA-FLA3|no; why: higher confidence-adjusted growth (9.21 vs 8.71 bp); relationships: KXNHLSPREAD-26OCT15VANFLA-FLA3|no: DUPLICATIVE (phi 0.744); KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4|yes: REINFORCING (phi 0.421); KXNHLTEAMTOTAL-26OCT15VANFLA-FLA3|no: DUPLICATIVE (phi 0.459); failure: FLA wins by 2+
- **Florida wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT15VANFLA-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15VANFLA-FLA2|no has the higher standalone adjusted growth (9.21 vs 8.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.744); they share one thesis budget; relationships: KXNHLSPREAD-26OCT15VANFLA-FLA2|no: DUPLICATIVE (phi 0.744); KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4|yes: REINFORCING (phi 0.344); KXNHLTEAMTOTAL-26OCT15VANFLA-FLA3|no: DUPLICATIVE (phi 0.373); failure: FLA wins by 2+
- **Vancouver over 3.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15VANFLA-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15VANFLA-FLA2|no has the higher standalone adjusted growth (9.21 vs 6.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.421); they share one thesis budget; relationships: KXNHLSPREAD-26OCT15VANFLA-FLA2|no: REINFORCING (phi 0.421); KXNHLSPREAD-26OCT15VANFLA-FLA3|no: REINFORCING (phi 0.344); KXNHLTEAMTOTAL-26OCT15VANFLA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.03); failure: VAN offense suppressed (<= 2 goals)
- **Florida over 2.5 goals scored NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15VANFLA-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15VANFLA-FLA2|no has the higher standalone adjusted growth (9.21 vs 5.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.459); they share one thesis budget; relationships: KXNHLSPREAD-26OCT15VANFLA-FLA2|no: DUPLICATIVE (phi 0.459); KXNHLSPREAD-26OCT15VANFLA-FLA3|no: DUPLICATIVE (phi 0.373); KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4|yes: MOSTLY_INDEPENDENT (phi 0.03); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS (p 0.4271): highest fidelity KXNHLSPREAD-26OCT15VANFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15VANFLA-FLA2|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.356): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15VANFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2254): highest fidelity KXNHLSPREAD-26OCT15VANFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15VANFLA-FLA2|no (same contract)
- KXNHLSPREAD-26OCT15VANFLA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.7 pts; opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3481, phi -1.0)
- KXNHLSPREAD-26OCT15VANFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.7 pts; opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3481, phi -0.744)
- KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.5 pts; opposing: failure thesis VAN:SUPPRESSED (p 0.4281, phi -0.656)
- KXNHLTEAMTOTAL-26OCT15VANFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4581, phi -0.631)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT15VANFLA-FLA5|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT15VANFLA-FLA3|no kept

portfolios: A EV +12.99 (adj +2.53) on $44.12, P(profit) 0.5359, adj growth 17.6 bp · B EV +6.46 (adj +1.60) on $25.25, P(profit) 0.6782, adj growth 14.1 bp · C EV +4.62 (adj +1.11) on $17.79, P(profit) 0.6519, adj growth 9.8 bp · R EV +2.19 (adj +0.53) on $8.00, P(profit) 0.6782, adj growth 17.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15VANFLA-VAN|yes == KXNHLGAME-26OCT15VANFLA-FLA|no

## NYR @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_NYR_win | p_overtime | goals | shots NJD/NYR | NJD/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.130 | 0.54 | 0.46 | 0.00 | 5.94 | 33.0/21.2 | 18.2/29.2 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.45 | 5.87 | 33.1/21.1 | 18.0/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.49 | 0.51 | 0.00 | 5.98 | 27.3/26.7 | 23.3/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.49 | 0.51 | 0.48 | 5.88 | 27.6/26.9 | 23.6/24.3 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.078 | 0.57 | 0.43 | 0.00 | 9.11 | 34.4/22.1 | 16.9/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.51 | 0.49 | 0.00 | 9.19 | 28.9/28.1 | 22.1/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 2.5 goals NO | 77 | 0.822 | 0.794 | +0.040 | +0.011 | $14.36 | FUNDED_RESEARCH | $4 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT15NYRNJ-NYR2|yes; why: higher confidence-adjusted growth (1.63 vs 0.44 bp); wins across more scripts (relative breadth 1.022 vs 0.539); alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NJD wins by 2+

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis NYR:WINS (p 0.4887): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15NYRNJ-NJ3|no (same contract)
- KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2907, phi -0.726)

portfolios: A EV +0.90 (adj +0.25) on $17.65, P(profit) 0.8223, adj growth 2.2 bp · B EV +0.73 (adj +0.21) on $14.36, P(profit) 0.8223, adj growth 1.8 bp · C EV +0.73 (adj +0.21) on $14.36, P(profit) 0.8223, adj growth 1.8 bp · R EV +0.20 (adj +0.06) on $4.00, P(profit) 0.8223, adj growth 2.0 bp

## PHI @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_PHI_win | p_overtime | goals | shots DET/PHI | DET/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.50 | 0.50 | 0.00 | 5.95 | 27.5/27.0 | 23.4/23.9 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.113 | 0.54 | 0.46 | 0.00 | 5.94 | 32.7/21.3 | 18.1/29.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.47 | 5.87 | 27.1/26.6 | 23.3/23.9 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.55 | 0.45 | 0.44 | 5.81 | 32.8/21.2 | 18.1/29.3 | even strength |
| DET shot control · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.50 | 0.50 | 0.47 | 2.76 | 31.4/19.9 | 18.5/29.9 | even strength |
| DET shot control · low event (<=4) · decided (2+) | 0.065 | 0.55 | 0.45 | 0.00 | 3.47 | 31.3/20.1 | 18.4/29.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.49 | 0.51 | 0.00 | 5.99 | 26.4/26.7 | 23.2/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.48 | 0.52 | 0.49 | 5.9 | 26.5/26.8 | 23.6/23.3 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.092 | 0.41 | 0.59 | 0.00 | 6.0 | 20.9/31.8 | 27.6/18.0 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.46 | 0.54 | 0.47 | 5.87 | 21.1/32.3 | 28.8/17.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.46 | 0.54 | 0.00 | 9.14 | 27.7/28.2 | 22.2/21.9 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.059 | 0.41 | 0.59 | 0.00 | 9.15 | 22.3/33.6 | 26.6/17.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_SJS_win | p_overtime | goals | shots NSH/SJS | NSH/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.05 | 27.6/27.7 | 24.5/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.46 | 5.92 | 27.7/27.7 | 24.5/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.56 | 0.44 | 0.00 | 9.37 | 29.1/29.0 | 23.0/22.3 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.073 | 0.57 | 0.43 | 0.00 | 5.98 | 32.5/22.0 | 19.0/28.7 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.067 | 0.50 | 0.50 | 0.00 | 5.97 | 22.1/32.6 | 29.1/18.8 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.54 | 0.46 | 0.48 | 5.97 | 32.9/22.4 | 19.3/29.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_STL_win | p_overtime | goals | shots MIN/STL | MIN/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.56 | 0.44 | 0.00 | 6.06 | 27.8/27.5 | 24.1/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.44 | 5.92 | 27.8/27.6 | 24.1/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.59 | 0.41 | 0.00 | 9.3 | 29.1/28.8 | 23.2/22.5 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.090 | 0.61 | 0.39 | 0.00 | 6.01 | 32.9/22.1 | 19.3/28.6 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.58 | 0.42 | 0.47 | 5.92 | 33.0/22.1 | 19.1/29.6 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.062 | 0.66 | 0.34 | 0.00 | 9.16 | 34.5/23.5 | 18.9/27.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_UTA_win | p_overtime | goals | shots EDM/UTA | EDM/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.65 | 0.35 | 0.00 | 6.06 | 27.4/27.3 | 24.4/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.121 | 0.62 | 0.38 | 0.00 | 9.55 | 29.5/29.3 | 23.6/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.50 | 0.50 | 0.45 | 5.99 | 27.6/27.7 | 24.5/24.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.080 | 0.70 | 0.30 | 0.00 | 6.02 | 32.7/22.0 | 19.4/28.2 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.065 | 0.68 | 0.32 | 0.00 | 9.38 | 34.2/23.2 | 18.6/26.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.55 | 0.45 | 0.47 | 5.99 | 33.0/22.3 | 19.1/29.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_CGY_win | p_overtime | goals | shots VGK/CGY | VGK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.73 | 0.27 | 0.00 | 6.05 | 28.5/27.8 | 25.3/23.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.116 | 0.79 | 0.21 | 0.00 | 6.01 | 33.6/22.0 | 19.8/28.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.55 | 0.45 | 0.44 | 5.83 | 28.4/27.8 | 24.6/25.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.57 | 0.43 | 0.47 | 5.89 | 33.9/21.9 | 18.9/30.4 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.079 | 0.81 | 0.19 | 0.00 | 9.33 | 35.5/23.6 | 19.6/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.75 | 0.25 | 0.00 | 9.34 | 29.7/29.1 | 24.4/21.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vegas wins by over 2.5 goals NO | 61 | 0.691 | 0.648 | +0.064 | +0.021 | $12.85 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 1.5 goals NO | 48 | 0.563 | 0.516 | +0.065 | +0.019 | $1.80 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vegas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no; why: higher confidence-adjusted growth (4.23 vs 3.12 bp); despite a smaller raw edge (+0.064 vs +0.065/contract); wins across more scripts (relative breadth 0.994 vs 0.816); relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: DUPLICATIVE (phi 0.759); failure: VGK wins by 2+
- **Vegas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no has the higher standalone adjusted growth (4.23 vs 3.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.759); they share one thesis budget; relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: DUPLICATIVE (phi 0.759); failure: VGK wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, VGK shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.4128): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK3|no (same contract)
- thesis VGK:SUPPRESSED (p 0.2982): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK3|no (same contract)
- KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4373, phi -0.759)
- KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4373, phi -1.0)

portfolios: A EV +5.44 (adj +1.52) on $44.12, P(profit) 0.6112, adj growth 8.5 bp · B EV +1.55 (adj +0.50) on $14.65, P(profit) 0.6908, adj growth 4.4 bp · C EV +1.54 (adj +0.51) on $15.04, P(profit) 0.6908, adj growth 4.5 bp · R EV +0.54 (adj +0.17) on $5.00, P(profit) 0.6908, adj growth 5.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
