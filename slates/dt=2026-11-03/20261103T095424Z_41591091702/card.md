# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-03T09:54:24Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +22.87 | +5.22 | +20.33 | 0.625 | -64.34 | -81.21 | 30.44 |
| B thesis-diversified (joint) ← optimiser card | 65.16 | +9.18 | +2.83 | +8.15 | 0.626 | -23.47 | -31.68 | 24.68 |
| C best expression per thesis | 24.67 | +8.12 | +3.09 | -6.24 | 0.428 | -24.67 | -24.67 | 26.75 |
| R FUNDED research stakes | 21.00 | +3.24 | +1.02 | +2.24 | 0.585 | -9.09 | -11.19 | 0.00 |

## UTA @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_UTA_win | p_overtime | goals | shots TOR/UTA | TOR/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.51 | 0.49 | 0.00 | 6.09 | 28.4/28.8 | 25.2/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.51 | 0.49 | 0.00 | 9.45 | 30.3/30.9 | 24.9/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.48 | 5.98 | 28.6/29.0 | 25.5/25.2 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.094 | 0.46 | 0.54 | 0.00 | 6.02 | 22.6/34.5 | 30.6/19.3 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.092 | 0.43 | 0.57 | 0.00 | 9.42 | 24.3/36.3 | 29.1/18.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.47 | 0.53 | 0.48 | 5.98 | 22.9/34.8 | 31.3/19.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_WPG_win | p_overtime | goals | shots MTL/WPG | MTL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.63 | 0.37 | 0.00 | 6.05 | 27.1/27.0 | 24.0/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.50 | 5.95 | 27.3/27.4 | 24.1/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.65 | 0.35 | 0.00 | 9.22 | 28.5/28.4 | 23.4/21.7 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 6.04 | 31.6/21.4 | 18.8/27.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.067 | 0.56 | 0.44 | 0.00 | 6.01 | 21.4/31.7 | 28.2/17.8 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.46 | 5.92 | 32.1/21.9 | 18.8/28.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_DET_win | p_overtime | goals | shots TBL/DET | TBL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.66 | 0.34 | 0.00 | 6.01 | 27.3/27.1 | 24.3/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.55 | 0.45 | 0.46 | 5.97 | 27.3/27.0 | 23.9/23.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.101 | 0.76 | 0.24 | 0.00 | 6.0 | 32.6/21.5 | 19.3/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.66 | 0.34 | 0.00 | 9.32 | 29.1/28.8 | 23.7/22.1 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.56 | 0.44 | 0.49 | 5.9 | 32.3/21.7 | 18.6/28.9 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.064 | 0.72 | 0.28 | 0.00 | 9.32 | 34.1/22.9 | 18.6/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 53 | 0.606 | 0.565 | +0.058 | +0.018 | $6.16 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 66 | 0.729 | 0.692 | +0.053 | +0.016 | $6.96 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV03DETTB-TB3|no; why: higher confidence-adjusted growth (2.82 vs 2.58 bp); relationships: KXNHLSPREAD-26NOV03DETTB-TB3|no: DUPLICATIVE (phi 0.756); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV03DETTB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV03DETTB-TB2|no has the higher standalone adjusted growth (2.82 vs 2.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.756); they share one thesis budget; relationships: KXNHLSPREAD-26NOV03DETTB-TB2|no: DUPLICATIVE (phi 0.756); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.415): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03DETTB-TB2|no (same contract)
- KXNHLSPREAD-26NOV03DETTB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3944, phi -1.0)
- KXNHLSPREAD-26NOV03DETTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3944, phi -0.756)

portfolios: A EV +2.91 (adj +0.89) on $31.58, P(profit) 0.6056, adj growth 6.2 bp · B EV +1.20 (adj +0.37) on $13.12, P(profit) 0.6056, adj growth 3.2 bp · C EV +1.07 (adj +0.33) on $10.09, P(profit) 0.6056, adj growth 2.9 bp · R EV +0.37 (adj +0.11) on $4.00, P(profit) 0.6056, adj growth 3.8 bp

## STL @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_STL_win | p_overtime | goals | shots NYR/STL | NYR/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.55 | 0.45 | 0.00 | 6.04 | 26.7/26.7 | 23.4/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.49 | 5.94 | 26.7/26.7 | 23.4/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.55 | 0.45 | 0.00 | 9.31 | 28.5/28.4 | 22.9/22.1 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.072 | 0.63 | 0.37 | 0.00 | 6.04 | 31.4/21.3 | 18.5/27.3 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.070 | 0.48 | 0.52 | 0.00 | 6.0 | 21.4/31.7 | 27.9/18.1 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.53 | 0.47 | 0.48 | 5.88 | 31.6/21.4 | 18.3/28.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 10 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_MIN_win | p_overtime | goals | shots PHI/MIN | PHI/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.54 | 0.46 | 0.00 | 5.99 | 27.0/27.3 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.48 | 5.87 | 27.1/27.4 | 24.2/23.8 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.091 | 0.50 | 0.50 | 0.00 | 5.94 | 21.5/32.8 | 29.1/18.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.50 | 0.50 | 0.47 | 5.85 | 21.7/32.8 | 29.3/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.55 | 0.45 | 0.00 | 9.21 | 28.8/29.1 | 23.2/22.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.56 | 0.44 | 0.00 | 3.48 | 25.8/26.2 | 24.4/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Philadelphia over 4.5 goals scored YES | 13 | 0.194 | 0.159 | +0.056 | +0.021 | $3.00 | FUNDED_RESEARCH | $1 | PHI:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Philadelphia over 3.5 goals scored YES | 29 | 0.380 | 0.332 | +0.075 | +0.028 | $4.58 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 75 | 0.847 | 0.781 | +0.084 | +0.018 | $15.94 | FUNDED_RESEARCH | $4 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Philadelphia over 4.5 goals scored YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (12.46 vs 8.36 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.466); relationships: KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes: DUPLICATIVE (phi 0.627); KXNHLSPREAD-26NOV03MINPHI-MIN3|no: REINFORCING (phi 0.199); failure: PHI offense suppressed (<= 2 goals)
- **Philadelphia over 3.5 goals scored YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (12.46 vs 8.01 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.532); relationships: KXNHLTEAMTOTAL-26NOV03MINPHI-PHI5|yes: DUPLICATIVE (phi 0.627); KXNHLSPREAD-26NOV03MINPHI-MIN3|no: REINFORCING (phi 0.297); failure: PHI offense suppressed (<= 2 goals)
- **Minnesota wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: Broad expression KXNHLSPREAD-26NOV03MINPHI-MIN3|no selected over broad KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.49 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLTEAMTOTAL-26NOV03MINPHI-PHI5|yes: REINFORCING (phi 0.199); KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes: REINFORCING (phi 0.297); failure: MIN wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:WINS_BY_2PLUS (p 0.2894): highest fidelity KXNHLSPREAD-26NOV03MINPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3682): highest fidelity KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4411): highest fidelity KXNHLSPREAD-26NOV03MINPHI-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — Broad expression KXNHLSPREAD-26NOV03MINPHI-MIN3|no selected over broad KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.49 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLTEAMTOTAL-26NOV03MINPHI-PHI5|yes: FUNDED_RESEARCH; family MIXED; loses 47% of the draws where the thesis happens; opposing: failure thesis PHI:SUPPRESSED (p 0.4034, phi -0.403)
- KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PHI:SUPPRESSED (p 0.4034, phi -0.643)
- KXNHLSPREAD-26NOV03MINPHI-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.2 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2523, phi -0.732)
- override: Broad expression KXNHLSPREAD-26NOV03MINPHI-MIN3|no selected over broad KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.49 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +8.77 (adj +1.39) on $39.47, P(profit) 0.6537, adj growth 9.0 bp · B EV +4.10 (adj +1.25) on $23.53, P(profit) 0.3749, adj growth 10.9 bp · C EV +3.16 (adj +1.25) on $8.54, P(profit) 0.2894, adj growth 10.9 bp · R EV +1.34 (adj +0.43) on $7.00, P(profit) 0.3749, adj growth 14.1 bp
equivalent contracts collapsed: KXNHLGAME-26NOV03MINPHI-MIN|no == KXNHLGAME-26NOV03MINPHI-PHI|yes

## VGK @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_VGK_win | p_overtime | goals | shots PIT/VGK | PIT/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.48 | 0.52 | 0.00 | 6.04 | 27.4/27.3 | 23.7/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.48 | 5.99 | 27.4/27.3 | 24.1/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.45 | 0.55 | 0.00 | 9.39 | 28.8/28.8 | 22.7/22.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.073 | 0.56 | 0.44 | 0.00 | 6.02 | 31.7/21.4 | 18.4/27.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.068 | 0.45 | 0.55 | 0.00 | 6.03 | 21.7/32.2 | 28.2/18.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.47 | 5.94 | 32.5/22.0 | 18.7/29.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_DAL_win | p_overtime | goals | shots WSH/DAL | WSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.56 | 0.44 | 0.00 | 5.98 | 25.9/26.0 | 22.8/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.47 | 5.96 | 26.1/26.2 | 23.0/22.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.60 | 0.40 | 0.00 | 9.35 | 27.6/27.7 | 22.2/20.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.076 | 0.50 | 0.50 | 0.00 | 5.95 | 20.7/30.8 | 27.1/17.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.47 | 0.53 | 0.46 | 5.86 | 20.6/30.8 | 27.5/17.5 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.062 | 0.65 | 0.35 | 0.00 | 6.02 | 30.4/20.8 | 18.1/26.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_COL_win | p_overtime | goals | shots CBJ/COL | CBJ/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.46 | 0.54 | 0.00 | 6.01 | 28.0/28.4 | 24.6/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.48 | 0.52 | 0.45 | 5.94 | 28.1/28.5 | 25.3/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.47 | 0.53 | 0.00 | 9.34 | 29.5/29.9 | 23.8/23.4 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.091 | 0.38 | 0.62 | 0.00 | 6.0 | 22.2/33.9 | 29.8/19.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.43 | 0.57 | 0.46 | 5.87 | 22.6/34.1 | 30.5/19.6 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.059 | 0.39 | 0.61 | 0.00 | 9.22 | 23.5/35.2 | 28.2/18.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_EDM_win | p_overtime | goals | shots NJD/EDM | NJD/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.47 | 0.53 | 0.00 | 6.07 | 28.2/27.8 | 24.0/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.49 | 0.51 | 0.47 | 6.0 | 28.2/28.0 | 24.6/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.49 | 0.51 | 0.00 | 9.43 | 29.7/29.4 | 23.3/23.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.093 | 0.56 | 0.44 | 0.00 | 6.07 | 33.6/22.0 | 18.9/29.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.54 | 0.46 | 0.43 | 5.93 | 33.1/22.0 | 18.8/29.6 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.073 | 0.54 | 0.46 | 0.00 | 9.41 | 35.2/23.8 | 18.2/28.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Edmonton over 5.5 goals scored YES | 7 | 0.113 | 0.089 | +0.038 | +0.014 | $2.11 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | FRAGILE (0.33) | EVIDENCE_MIXED | D |
| New Jersey wins by over 1.5 goals NO | 64 | 0.717 | 0.676 | +0.061 | +0.020 | $11.44 | FUNDED_RESEARCH | $3 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Edmonton wins by over 1.5 goals YES | 23 | 0.292 | 0.259 | +0.050 | +0.016 | $1.36 | FUNDED_RESEARCH | $1 | EDM:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Full Game: Over 6.5 goals scored YES | 46 | 0.521 | 0.488 | +0.044 | +0.011 | $2.74 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Edmonton over 5.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes; why: higher confidence-adjusted growth (6.30 vs 2.58 bp); despite a smaller raw edge (+0.038 vs +0.052/contract); relationships: KXNHLSPREAD-26NOV03EDMNJ-NJ2|no: REINFORCING (phi 0.213); KXNHLSPREAD-26NOV03EDMNJ-EDM2|yes: REINFORCING (phi 0.407); KXNHLTOTAL-26NOV03EDMNJ-7|yes: DUPLICATIVE (phi 0.327); failure: NJD wins (incl. OT/SO)
- **New Jersey wins by over 1.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes has the higher standalone adjusted growth (6.30 vs 3.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.213); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes: REINFORCING (phi 0.213); KXNHLSPREAD-26NOV03EDMNJ-EDM2|yes: DUPLICATIVE (phi 0.404); KXNHLTOTAL-26NOV03EDMNJ-7|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NJD wins by 2+
- **Edmonton wins by over 1.5 goals YES** — thesis: EDM wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes has the higher standalone adjusted growth (6.30 vs 3.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.407); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes: REINFORCING (phi 0.407); KXNHLSPREAD-26NOV03EDMNJ-NJ2|no: DUPLICATIVE (phi 0.404); KXNHLTOTAL-26NOV03EDMNJ-7|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: NJD wins (incl. OT/SO)
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes has the higher standalone adjusted growth (6.30 vs 1.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.327); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes: DUPLICATIVE (phi 0.327); KXNHLSPREAD-26NOV03EDMNJ-NJ2|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26NOV03EDMNJ-EDM2|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:HIGH_EVENT (p 0.3061): highest fidelity KXNHLTOTAL-26NOV03EDMNJ-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes less than the minimum stake; KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes kept
- thesis EDM:WINS (p 0.5035): highest fidelity KXNHLSPREAD-26NOV03EDMNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03EDMNJ-NJ2|no (same contract)
- thesis EDM:WINS_BY_2PLUS (p 0.2921): highest fidelity KXNHLSPREAD-26NOV03EDMNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03EDMNJ-NJ2|no (same contract)
- KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes: FUNDED_RESEARCH; family MIXED; loses 67% of the draws where the thesis happens; opposing: failure thesis NJD:WINS (p 0.4965, phi -0.32)
- KXNHLSPREAD-26NOV03EDMNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2832, phi -1.0)
- KXNHLSPREAD-26NOV03EDMNJ-EDM2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.4965, phi -0.638)
- KXNHLTOTAL-26NOV03EDMNJ-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.2012, phi -0.524)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes less than the minimum stake; KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6|yes kept

portfolios: A EV +6.37 (adj +1.81) on $39.47, P(profit) 0.3625, adj growth 9.8 bp · B EV +2.66 (adj +0.90) on $17.65, P(profit) 0.5155, adj growth 7.8 bp · C EV +1.53 (adj +0.57) on $2.99, P(profit) 0.1126, adj growth 4.9 bp · R EV +1.08 (adj +0.37) on $6.00, P(profit) 0.5155, adj growth 11.5 bp

## CAR @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_CAR_win | p_overtime | goals | shots NSH/CAR | NSH/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.143 | 0.38 | 0.62 | 0.00 | 6.02 | 21.6/34.5 | 30.1/18.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.47 | 0.53 | 0.46 | 6.0 | 21.9/34.8 | 31.2/18.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.113 | 0.38 | 0.62 | 0.00 | 9.35 | 23.0/35.8 | 28.1/17.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.45 | 0.55 | 0.00 | 6.03 | 27.3/28.3 | 24.5/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.45 | 0.55 | 0.00 | 9.38 | 29.1/30.1 | 23.3/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.50 | 0.50 | 0.47 | 5.97 | 27.6/28.6 | 25.3/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 59 | 0.665 | 0.623 | +0.058 | +0.015 | $8.28 | FUNDED_RESEARCH | $3 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nashville over 3.5 goals scored YES | 32 | 0.391 | 0.348 | +0.056 | +0.013 | $2.58 | FUNDED_RESEARCH | $1 | NSH:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes has the higher standalone adjusted growth (11.37 vs 2.21 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.220); relationships: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes: REINFORCING (phi 0.432); failure: CAR wins by 2+
- **Nashville over 3.5 goals scored YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes selected over broad KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.71 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV03CARNSH-CAR2|no: REINFORCING (phi 0.432); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.11.
- thesis GAME:HIGH_EVENT (p 0.3104): highest fidelity KXNHLTEAMTOTAL-26NOV03CARNSH-NSH3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes — Broad expression KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes selected over broad KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.71 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NSH:WINS_BY_2PLUS (p 0.2441): highest fidelity KXNHLSPREAD-26NOV03CARNSH-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS (p 0.45): highest fidelity KXNHLSPREAD-26NOV03CARNSH-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV03CARNSH-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3351, phi -1.0)
- KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NSH:SUPPRESSED (p 0.4046, phi -0.66)
- override: Broad expression KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes selected over broad KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.71 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.82 (adj +1.13) on $39.47, P(profit) 0.5492, adj growth 5.4 bp · B EV +1.22 (adj +0.31) on $10.86, P(profit) 0.6649, adj growth 2.7 bp · C EV +2.36 (adj +0.94) on $3.05, P(profit) 0.0946, adj growth 8.1 bp · R EV +0.45 (adj +0.11) on $4.00, P(profit) 0.6649, adj growth 3.7 bp

## ANA @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_ANA_win | p_overtime | goals | shots VAN/ANA | VAN/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.129 | 0.39 | 0.61 | 0.00 | 6.11 | 21.7/33.6 | 29.1/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.45 | 0.55 | 0.00 | 6.05 | 27.3/28.0 | 24.2/23.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.46 | 0.54 | 0.45 | 6.02 | 22.0/34.0 | 30.4/18.8 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.102 | 0.35 | 0.65 | 0.00 | 9.49 | 23.0/35.6 | 27.8/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.45 | 0.55 | 0.00 | 9.51 | 29.0/29.9 | 23.1/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.48 | 0.52 | 0.45 | 6.05 | 27.4/28.1 | 24.6/24.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
