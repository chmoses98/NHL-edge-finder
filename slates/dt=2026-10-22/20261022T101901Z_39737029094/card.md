# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-22T10:19:01Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +20.30 | +5.89 | +20.35 | 0.662 | -40.14 | -55.50 | 47.70 |
| B thesis-diversified (joint) ← optimiser card | 125.58 | +16.07 | +5.26 | +16.36 | 0.683 | -29.17 | -42.11 | 46.48 |
| C best expression per thesis | 100.26 | +12.99 | +4.57 | +14.15 | 0.636 | -30.32 | -40.72 | 40.39 |
| R FUNDED research stakes | 37.00 | +4.33 | +1.37 | +4.61 | 0.677 | -8.75 | -12.51 | 0.00 |

## NSH @ BOS  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_NSH_win | p_overtime | goals | shots BOS/NSH | BOS/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.61 | 0.39 | 0.00 | 6.06 | 28.2/28.1 | 25.0/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.50 | 6.03 | 28.4/28.2 | 24.8/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.62 | 0.38 | 0.00 | 9.36 | 29.6/29.3 | 23.9/22.8 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.081 | 0.68 | 0.32 | 0.00 | 6.07 | 33.1/22.3 | 19.7/28.3 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.56 | 0.44 | 0.47 | 5.9 | 33.2/22.4 | 19.1/29.7 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.062 | 0.69 | 0.31 | 0.00 | 9.33 | 34.3/23.5 | 18.8/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 7.5 goals scored YES | 24 | 0.297 | 0.266 | +0.044 | +0.013 | $2.13 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Full Game: Over 5.5 goals scored YES | 55 | 0.614 | 0.580 | +0.047 | +0.012 | $3.95 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Full Game: Over 7.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-9|yes; why: higher confidence-adjusted growth (1.99 vs 1.70 bp); relationships: KXNHLTOTAL-26OCT22NSHBOS-6|yes: DUPLICATIVE (phi 0.515); failure: NSH offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-8|yes; why: second expression of the same thesis: KXNHLTOTAL-26OCT22NSHBOS-8|yes has the higher standalone adjusted growth (1.99 vs 1.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.515); they share one thesis budget; relationships: KXNHLTOTAL-26OCT22NSHBOS-8|yes: DUPLICATIVE (phi 0.515); failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:HIGH_EVENT (p 0.2968): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-8|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-8|yes (same contract)
- KXNHLTOTAL-26OCT22NSHBOS-8|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NSH:SUPPRESSED (p 0.4293, phi -0.415)
- KXNHLTOTAL-26OCT22NSHBOS-6|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.204, phi -0.639)

portfolios: A EV +2.67 (adj +0.71) on $22.73, P(profit) 0.508, adj growth 4.3 bp · B EV +0.70 (adj +0.20) on $6.08, P(profit) 0.6141, adj growth 1.8 bp · C EV +0.71 (adj +0.21) on $4.08, P(profit) 0.2968, adj growth 1.9 bp · R EV +0.26 (adj +0.07) on $2.00, P(profit) 0.2968, adj growth 2.5 bp

## NYR @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYR_win | p_overtime | goals | shots TOR/NYR | TOR/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.55 | 0.45 | 0.00 | 6.02 | 27.3/27.3 | 24.0/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.47 | 5.96 | 27.3/27.7 | 24.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.51 | 0.49 | 0.00 | 9.26 | 29.1/29.5 | 23.5/22.9 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.079 | 0.45 | 0.55 | 0.00 | 6.01 | 22.1/32.5 | 28.9/18.9 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.49 | 0.51 | 0.43 | 5.92 | 21.8/32.3 | 28.9/18.6 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.060 | 0.56 | 0.44 | 0.00 | 5.98 | 32.0/22.0 | 18.9/27.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_SJS_win | p_overtime | goals | shots OTT/SJS | OTT/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.62 | 0.38 | 0.00 | 5.98 | 27.1/26.7 | 23.8/23.1 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.112 | 0.66 | 0.34 | 0.00 | 5.97 | 32.0/20.8 | 18.1/27.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.47 | 5.93 | 27.1/26.6 | 23.4/23.8 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.56 | 0.44 | 0.48 | 5.89 | 32.4/21.2 | 18.1/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.59 | 0.41 | 0.00 | 9.33 | 28.5/28.0 | 22.4/21.7 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.071 | 0.71 | 0.29 | 0.00 | 9.31 | 33.9/22.5 | 18.1/25.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_ANA_win | p_overtime | goals | shots NJD/ANA | NJD/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.03 | 28.6/28.7 | 25.4/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.51 | 0.49 | 0.47 | 5.96 | 28.8/28.6 | 25.3/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.56 | 0.44 | 0.00 | 9.36 | 30.3/30.0 | 24.2/23.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.087 | 0.61 | 0.39 | 0.00 | 6.03 | 33.8/22.8 | 19.7/29.3 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.52 | 0.48 | 0.47 | 5.91 | 34.2/23.0 | 19.8/31.0 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.057 | 0.65 | 0.35 | 0.00 | 9.42 | 35.1/24.0 | 18.9/27.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 2.5 goals NO | 70 | 0.791 | 0.743 | +0.076 | +0.028 | $20.00 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey over 3.5 goals scored NO | 47 | 0.556 | 0.511 | +0.069 | +0.023 | $2.77 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey over 2.5 goals scored NO | 27 | 0.346 | 0.303 | +0.062 | +0.019 | $1.31 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 19 | 0.247 | 0.216 | +0.046 | +0.015 | $1.04 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4|no; why: higher confidence-adjusted growth (8.65 vs 4.74 bp); wins across more scripts (relative breadth 1.007 vs 0.871); relationships: KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4|no: DUPLICATIVE (phi 0.498); KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no: DUPLICATIVE (phi 0.374); KXNHLSPREAD-26OCT22ANANJ-ANA2|yes: REINFORCING (phi 0.295); failure: NJD wins by 2+
- **New Jersey over 3.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22ANANJ-NJ3|no has the higher standalone adjusted growth (8.65 vs 4.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.498); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22ANANJ-NJ3|no: DUPLICATIVE (phi 0.498); KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no: DUPLICATIVE (phi 0.649); KXNHLSPREAD-26OCT22ANANJ-ANA2|yes: REINFORCING (phi 0.405); failure: NJD offense succeeds (4+ goals)
- **New Jersey over 2.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22ANANJ-NJ3|no has the higher standalone adjusted growth (8.65 vs 3.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.374); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22ANANJ-NJ3|no: DUPLICATIVE (phi 0.374); KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4|no: DUPLICATIVE (phi 0.649); KXNHLSPREAD-26OCT22ANANJ-ANA2|yes: REINFORCING (phi 0.486); failure: NJD offense succeeds (4+ goals)
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22ANANJ-NJ3|no has the higher standalone adjusted growth (8.65 vs 3.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22ANANJ-NJ3|no: REINFORCING (phi 0.295); KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4|no: REINFORCING (phi 0.405); KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no: REINFORCING (phi 0.486); failure: NJD wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis ANA:WINS (p 0.4622): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- thesis NJD:SUPPRESSED (p 0.3568): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.2472): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- KXNHLSPREAD-26OCT22ANANJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3185, phi -0.752)
- KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4338, phi -0.98)
- KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4338, phi -0.637)
- KXNHLSPREAD-26OCT22ANANJ-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.5378, phi -0.618)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3|no kept

portfolios: A EV +3.14 (adj +1.02) on $22.73, P(profit) 0.5407, adj growth 8.6 bp · B EV +3.05 (adj +1.09) on $25.12, P(profit) 0.791, adj growth 9.8 bp · C EV +2.14 (adj +0.79) on $20.00, P(profit) 0.791, adj growth 7.3 bp · R EV +1.13 (adj +0.39) on $8.00, P(profit) 0.5636, adj growth 12.8 bp

## FLA @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_FLA_win | p_overtime | goals | shots PIT/FLA | PIT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 6.07 | 27.0/26.9 | 23.8/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.46 | 5.95 | 26.9/26.9 | 23.6/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.59 | 0.41 | 0.00 | 9.37 | 28.8/28.6 | 22.9/22.3 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.078 | 0.65 | 0.35 | 0.00 | 6.08 | 32.0/21.7 | 18.9/27.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.53 | 0.47 | 0.47 | 5.95 | 32.1/21.7 | 18.4/28.8 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.063 | 0.72 | 0.28 | 0.00 | 9.26 | 34.0/23.0 | 18.7/26.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 1.5 goals NO | 71 | 0.769 | 0.737 | +0.045 | +0.013 | $12.37 | FUNDED_RESEARCH | $4 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 1.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22FLAPIT-FLA3|no; why: higher confidence-adjusted growth (1.74 vs 0.36 bp); alternative not eligible: confidence-adjusted EV +0.0048 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:WINS (p 0.5624): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22FLAPIT-FLA2|no (same contract)
- KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.231, phi -1.0)

portfolios: A EV +0.56 (adj +0.16) on $9.09, P(profit) 0.769, adj growth 1.4 bp · B EV +0.76 (adj +0.21) on $12.37, P(profit) 0.769, adj growth 1.9 bp · C EV +0.76 (adj +0.21) on $12.37, P(profit) 0.769, adj growth 1.9 bp · R EV +0.25 (adj +0.07) on $4.00, P(profit) 0.769, adj growth 2.3 bp

## LAK @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_LAK_win | p_overtime | goals | shots NYI/LAK | NYI/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.44 | 0.00 | 5.96 | 27.4/27.2 | 23.9/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.49 | 0.51 | 0.47 | 5.87 | 27.4/27.4 | 24.1/24.0 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.080 | 0.65 | 0.35 | 0.00 | 5.98 | 32.2/21.5 | 18.7/27.8 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.54 | 0.46 | 0.48 | 5.82 | 32.3/21.9 | 18.9/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.57 | 0.43 | 0.00 | 9.04 | 28.8/28.7 | 23.2/22.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.51 | 0.49 | 0.47 | 2.8 | 25.7/25.6 | 24.1/24.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYI shot control · normal event (5-7) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_VGK_win | p_overtime | goals | shots STL/VGK | STL/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.52 | 0.48 | 0.00 | 6.08 | 26.7/26.8 | 23.2/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.48 | 0.52 | 0.45 | 5.89 | 26.6/26.9 | 23.6/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.50 | 0.50 | 0.00 | 9.29 | 28.2/28.4 | 22.5/22.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.087 | 0.42 | 0.58 | 0.00 | 5.99 | 21.0/31.4 | 27.3/18.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.46 | 0.54 | 0.46 | 5.87 | 21.3/32.0 | 28.5/18.3 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.060 | 0.38 | 0.62 | 0.00 | 9.3 | 22.5/33.5 | 26.3/17.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.62 | 0.38 | 0.00 | 6.01 | 25.9/25.8 | 22.6/21.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.47 | 5.87 | 26.1/25.8 | 22.5/22.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.099 | 0.68 | 0.32 | 0.00 | 5.96 | 30.8/20.4 | 17.8/26.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.58 | 0.42 | 0.51 | 5.86 | 31.1/20.5 | 17.4/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.61 | 0.39 | 0.00 | 9.18 | 27.6/27.2 | 21.9/20.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.55 | 0.46 | 0.00 | 3.45 | 24.8/24.5 | 22.7/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins by over 2.5 goals NO | 71 | 0.773 | 0.739 | +0.048 | +0.014 | $14.26 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL2|no; why: higher confidence-adjusted growth (2.29 vs 0.87 bp); wins across more scripts (relative breadth 1.006 vs 0.888); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4294): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3517, phi -0.736)

portfolios: A EV +0.61 (adj +0.18) on $9.09, P(profit) 0.7727, adj growth 1.7 bp · B EV +0.95 (adj +0.28) on $14.26, P(profit) 0.7727, adj growth 2.5 bp · C EV +0.95 (adj +0.28) on $14.26, P(profit) 0.7727, adj growth 2.5 bp · R EV +0.27 (adj +0.08) on $4.00, P(profit) 0.7727, adj growth 2.8 bp

## MIN @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_MIN_win | p_overtime | goals | shots CGY/MIN | CGY/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.43 | 0.57 | 0.00 | 6.0 | 29.1/29.4 | 25.4/25.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.46 | 0.54 | 0.46 | 5.94 | 29.3/29.6 | 26.1/26.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.44 | 0.56 | 0.00 | 9.18 | 31.0/31.2 | 24.9/25.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.083 | 0.35 | 0.65 | 0.00 | 5.98 | 23.6/34.8 | 30.4/20.7 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.50 | 0.50 | 0.47 | 5.94 | 23.6/35.0 | 31.6/20.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.059 | 0.46 | 0.54 | 0.48 | 2.79 | 27.5/27.7 | 26.1/26.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Minnesota wins by over 1.5 goals NO | 59 | 0.680 | 0.632 | +0.073 | +0.026 | $4.37 | FUNDED_RESEARCH | $2 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 1.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4|yes; why: higher confidence-adjusted growth (6.03 vs 4.88 bp); wins across more scripts (relative breadth 0.901 vs 0.746); relationships: only recommended bet in this game; failure: MIN wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CGY:WINS (p 0.4531): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3343): highest fidelity KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.2396): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no (same contract)
- KXNHLSPREAD-26OCT22MINCGY-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3199, phi -1.0)

portfolios: A EV +3.19 (adj +1.08) on $22.73, P(profit) 0.7015, adj growth 9.1 bp · B EV +0.53 (adj +0.18) on $4.37, P(profit) 0.6801, adj growth 1.8 bp · C EV +2.07 (adj +0.73) on $17.19, P(profit) 0.6801, adj growth 6.4 bp · R EV +0.24 (adj +0.08) on $2.00, P(profit) 0.6801, adj growth 3.2 bp

## CAR @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CAR_win | p_overtime | goals | shots EDM/CAR | EDM/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.62 | 0.38 | 0.00 | 6.08 | 27.5/28.0 | 25.0/23.4 | even strength |
| CAR shot control · normal event (5-7) · decided (2+) | 0.109 | 0.54 | 0.46 | 0.00 | 6.07 | 21.8/33.2 | 29.7/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.63 | 0.37 | 0.00 | 9.53 | 28.8/29.5 | 24.1/21.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.54 | 0.46 | 0.44 | 5.94 | 27.2/28.0 | 24.7/23.8 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.48 | 0.52 | 0.49 | 5.98 | 21.8/33.4 | 29.8/18.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.093 | 0.55 | 0.45 | 0.00 | 9.42 | 23.5/35.2 | 28.6/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Edmonton wins by over 1.5 goals YES | 28 | 0.353 | 0.314 | +0.059 | +0.020 | $4.77 | FUNDED_RESEARCH | $2 | EDM:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 1.5 goals NO | 69 | 0.760 | 0.723 | +0.055 | +0.018 | $11.08 | FUNDED_RESEARCH | $3 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Edmonton wins by over 1.5 goals YES** — thesis: EDM wins by 2+; alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: higher confidence-adjusted growth (4.11 vs 3.26 bp); relationships: KXNHLSPREAD-26OCT22CAREDM-CAR2|no: DUPLICATIVE (phi 0.415); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 1.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22CAREDM-EDM2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT22CAREDM-EDM2|yes has the higher standalone adjusted growth (4.11 vs 3.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.415); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22CAREDM-EDM2|yes: DUPLICATIVE (phi 0.415); failure: CAR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CAR shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:WINS_BY_2PLUS (p 0.3528): highest fidelity KXNHLSPREAD-26OCT22CAREDM-EDM2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-EDM2|yes (same contract)
- thesis EDM:WINS (p 0.5621): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-EDM2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT22CAREDM-EDM2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.4379, phi -0.652)
- KXNHLSPREAD-26OCT22CAREDM-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2399, phi -1.0)

portfolios: A EV +2.52 (adj +0.84) on $18.18, P(profit) 0.3528, adj growth 6.8 bp · B EV +1.82 (adj +0.60) on $15.85, P(profit) 0.3528, adj growth 5.2 bp · C EV +1.31 (adj +0.44) on $6.55, P(profit) 0.3528, adj growth 3.8 bp · R EV +0.63 (adj +0.21) on $5.00, P(profit) 0.3528, adj growth 6.9 bp

## UTA @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_UTA_win | p_overtime | goals | shots SEA/UTA | SEA/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.48 | 0.52 | 0.00 | 6.04 | 27.2/27.7 | 24.2/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.49 | 0.51 | 0.48 | 5.93 | 27.6/28.1 | 24.7/24.3 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.099 | 0.45 | 0.55 | 0.00 | 6.03 | 21.8/32.8 | 29.0/18.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.51 | 0.49 | 0.00 | 9.33 | 28.7/29.2 | 23.2/22.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.49 | 0.51 | 0.46 | 5.91 | 21.7/32.9 | 29.5/18.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.077 | 0.45 | 0.55 | 0.00 | 9.32 | 23.1/34.7 | 27.8/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Utah wins by over 1.5 goals NO | 62 | 0.712 | 0.663 | +0.075 | +0.027 | $13.04 | FUNDED_RESEARCH | $4 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Seattle wins by over 1.5 goals YES | 21 | 0.280 | 0.242 | +0.058 | +0.021 | $3.61 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Utah wins by over 2.5 goals NO | 74 | 0.811 | 0.773 | +0.058 | +0.020 | $5.23 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Utah wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22UTASEA-SEA2|yes; why: higher confidence-adjusted growth (6.90 vs 5.38 bp); wins across more scripts (relative breadth 0.96 vs 0.541); relationships: KXNHLSPREAD-26OCT22UTASEA-SEA2|yes: DUPLICATIVE (phi 0.396); KXNHLSPREAD-26OCT22UTASEA-UTA3|no: DUPLICATIVE (phi 0.758); failure: UTA wins by 2+
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT22UTASEA-UTA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22UTASEA-UTA2|no has the higher standalone adjusted growth (6.90 vs 5.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.396); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22UTASEA-UTA2|no: DUPLICATIVE (phi 0.396); KXNHLSPREAD-26OCT22UTASEA-UTA3|no: DUPLICATIVE (phi 0.3); failure: UTA wins (incl. OT/SO)
- **Utah wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22UTASEA-UTA2|no has the higher standalone adjusted growth (6.90 vs 4.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.758); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22UTASEA-UTA2|no: DUPLICATIVE (phi 0.758); KXNHLSPREAD-26OCT22UTASEA-SEA2|yes: DUPLICATIVE (phi 0.3); failure: UTA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:WINS (p 0.4959): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2796): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.4062): highest fidelity KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT22UTASEA-UTA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2881, phi -1.0)
- KXNHLSPREAD-26OCT22UTASEA-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS (p 0.5041, phi -0.628)
- KXNHLSPREAD-26OCT22UTASEA-UTA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2881, phi -0.758)

portfolios: A EV +3.40 (adj +1.21) on $22.73, P(profit) 0.2796, adj growth 10.1 bp · B EV +2.89 (adj +1.03) on $21.88, P(profit) 0.7119, adj growth 9.0 bp · C EV +2.36 (adj +0.84) on $19.88, P(profit) 0.7119, adj growth 7.4 bp · R EV +0.89 (adj +0.32) on $7.00, P(profit) 0.7119, adj growth 10.7 bp

## DET @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_DET_win | p_overtime | goals | shots VAN/DET | VAN/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.112 | 0.50 | 0.50 | 0.00 | 5.98 | 21.7/33.4 | 29.7/18.3 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.50 | 5.92 | 22.0/33.8 | 30.4/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.58 | 0.42 | 0.00 | 5.99 | 27.2/27.9 | 24.8/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.50 | 0.50 | 0.48 | 5.91 | 27.2/27.9 | 24.7/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.58 | 0.42 | 0.00 | 9.32 | 28.7/29.4 | 24.0/22.1 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.076 | 0.48 | 0.52 | 0.00 | 9.3 | 23.4/35.4 | 28.7/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 22 | 0.306 | 0.261 | +0.074 | +0.029 | $4.55 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit over 1.5 goals scored NO | 13 | 0.197 | 0.161 | +0.059 | +0.023 | $3.27 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | DET:SUPPRESSED | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Detroit wins by over 1.5 goals NO | 62 | 0.750 | 0.662 | +0.114 | +0.026 | $5.57 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit wins by over 2.5 goals NO | 74 | 0.846 | 0.774 | +0.093 | +0.021 | $12.26 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: Broad expression KXNHLSPREAD-26OCT22DETVAN-VAN2|yes selected over broad KXNHLSPREAD-26OCT22DETVAN-VAN3|yes because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.66 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no: REINFORCING (phi 0.449); KXNHLSPREAD-26OCT22DETVAN-DET2|no: DUPLICATIVE (phi 0.384); KXNHLSPREAD-26OCT22DETVAN-DET3|no: REINFORCING (phi 0.283); failure: DET wins (incl. OT/SO)
- **Detroit over 1.5 goals scored NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes has the higher standalone adjusted growth (11.24 vs 9.73 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.413); relationships: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: REINFORCING (phi 0.449); KXNHLSPREAD-26OCT22DETVAN-DET2|no: REINFORCING (phi 0.286); KXNHLSPREAD-26OCT22DETVAN-DET3|no: REINFORCING (phi 0.211); failure: DET wins (incl. OT/SO)
- **Detroit wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes has the higher standalone adjusted growth (11.24 vs 6.30 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.289); relationships: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: DUPLICATIVE (phi 0.384); KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no: REINFORCING (phi 0.286); KXNHLSPREAD-26OCT22DETVAN-DET3|no: DUPLICATIVE (phi 0.738); failure: DET wins by 2+
- **Detroit wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes has the higher standalone adjusted growth (11.24 vs 4.96 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.214); relationships: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: REINFORCING (phi 0.283); KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no: REINFORCING (phi 0.211); KXNHLSPREAD-26OCT22DETVAN-DET2|no: DUPLICATIVE (phi 0.738); failure: DET wins by 2+

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.11, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.3064): highest fidelity KXNHLSPREAD-26OCT22DETVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4122): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5315): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS (p 0.4685, phi -0.624)
- KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; loses 52% of the draws where the thesis happens; opposing: failure thesis DET:WINS (p 0.4685, phi -0.426)
- KXNHLSPREAD-26OCT22DETVAN-DET2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.5 pts; opposing: failure thesis DET:WINS_BY_2PLUS (p 0.25, phi -1.0)
- KXNHLSPREAD-26OCT22DETVAN-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.1 pts; opposing: failure thesis DET:WINS_BY_2PLUS (p 0.25, phi -0.738)
- override: Broad expression KXNHLSPREAD-26OCT22DETVAN-VAN2|yes selected over broad KXNHLSPREAD-26OCT22DETVAN-VAN3|yes because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.66 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.20 (adj +0.69) on $22.73, P(profit) 0.648, adj growth 5.7 bp · B EV +5.37 (adj +1.67) on $25.65, P(profit) 0.3608, adj growth 14.6 bp · C EV +2.70 (adj +1.07) on $5.93, P(profit) 0.2007, adj growth 9.3 bp · R EV +0.67 (adj +0.15) on $5.00, P(profit) 0.8462, adj growth 5.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22DETVAN-VAN|yes == KXNHLGAME-26OCT22DETVAN-DET|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
