# Thesis-card postmortem — RESEARCH_ONLY

evaluated 2026-10-02T02:35:51Z · games 3 · rows (all runs) 416

## Final card (chosen bets, last pregame run)

```
{
 "n": 23,
 "won": 12,
 "expression_results": {
  "THESIS_WRONG_EXPRESSION_LOST": 9,
  "THESIS_RIGHT_EXPRESSION_WON": 8,
  "THESIS_RIGHT_EXPRESSION_LOST": 2,
  "THESIS_WRONG_EXPRESSION_WON": 4
 },
 "thesis_hit_rate": 0.435,
 "mean_clv": -0.0061,
 "n_clv": 23,
 "brier_model": 0.0987,
 "brier_adjusted": 0.1029,
 "brier_kalshi_mid": 0.1077,
 "realized_profit": -11.25,
 "stake": 113.16
}
```

## Final shortlist (all shortlisted, last pregame run)

```
{
 "n": 78,
 "won": 52,
 "expression_results": {
  "THESIS_WRONG_EXPRESSION_LOST": 20,
  "THESIS_WRONG_EXPRESSION_WON": 17,
  "THESIS_RIGHT_EXPRESSION_WON": 35,
  "THESIS_RIGHT_EXPRESSION_LOST": 6
 },
 "thesis_hit_rate": 0.526,
 "mean_clv": -0.0067,
 "n_clv": 78,
 "brier_model": 0.1631,
 "brier_adjusted": 0.1724,
 "brier_kalshi_mid": 0.182,
 "realized_profit": -11.25,
 "stake": 113.16
}
```

## game 2026020009: realised script NJD shot control · normal event (5-7) · tight (1-goal/OT)

portfolio: {"n_bets": 8, "stake": 26.23, "realized_profit": -26.23, "expected_profit": 2.47, "realized_vs_simulated": "<= p5", "largest_thesis_share": 0.417, "n_theses": 3, "theses_with_multiple_losses": ["NJD:OFFENSE_4PLUS", "PHI:OFFENSE_4PLUS"], "multiple_losses_on_one_thesis": [{"thesis": "NJD:OFFENSE_4PLUS", "thesis_happened": false, "n_lost": 4, "loss": 10.93, "reading": "thesis was wrong and several bets shared it: concentration cost"}, {"thesis": "PHI:OFFENSE_4PLUS", "thesis_happened": false, "n_lost": 3, "loss": 6.71, "reading": "thesis was wrong and several bets shared it: concentration cost"}]}

| bet | chosen | stake | won | thesis | thesis hit | expression | model P(bet|thesis outcome) | model P(win|realised script) | CLV | P/L |
|---|---|---:|---|---|---|---|---:|---:|---:|---:|
| KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes | True | 4.28 | False | NJD:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.1197 | 0.162 | 0.015 | -4.28 |
| KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no | False | 0.0 | True | NJD:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.6895 | 0.7637 | -0.005 | None |
| KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes | True | 2.13 | False | PHI:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.0972 | 0.1424 | -0.005 | -2.13 |
| KXNHLAST-26OCT01PHINJ-NJLEVANGELISTA77-1|no | True | 8.59 | False | NJD:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_LOST | 0.7081 | 0.775 | -0.015 | -8.59 |
| KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes | True | 1.92 | False | NJD:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.1029 | 0.1465 | -0.005 | -1.92 |
| KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes | False | 0.0 | False | PHI:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.0831 | 0.1176 | -0.02 | None |
| KXNHLGOAL-26OCT01PHINJ-NJLHUGHES43-1|no | False | 0.0 | False | NJD:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_LOST | 0.8676 | 0.9143 | -0.005 | None |
| KXNHLGOAL-26OCT01PHINJ-PHICDVORAK22-1|yes | False | 0.0 | False | PHI:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.1343 | 0.2074 | 0.0 | None |
| KXNHLGOAL-26OCT01PHINJ-PHIPMARTONE94-1|no | False | 0.0 | True | PHI:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.8877 | 0.7946 | 0.005 | None |
| KXNHLGOAL-26OCT01PHINJ-NJLEVANGELISTA77-1|no | False | 0.0 | True | NJD:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.7543 | 0.8142 | -0.005 | None |
| KXNHLAST-26OCT01PHINJ-NJAMANTHA39-1|no | False | 0.0 | True | NJD:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.8071 | 0.871 | -0.02 | None |
| KXNHLGAME-26OCT01PHINJ-PHI|yes | False | 0.0 | False | PHI:WINS | False | THESIS_WRONG_EXPRESSION_LOST | 0.0 | 0.4386 | -0.005 | None |
| KXNHLTOTAL-26OCT01PHINJ-6|no | False | 0.0 | True | GAME:LOW_EVENT | False | THESIS_WRONG_EXPRESSION_WON | 0.3176 | 0.5583 | -0.005 | None |
| KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes | True | 2.33 | False | PHI:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.0831 | 0.1176 | -0.01 | -2.33 |
| KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes | True | 2.25 | False | PHI:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.0972 | 0.1424 | -0.005 | -2.25 |
| KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes | True | 2.81 | False | NJD:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.1197 | 0.162 | -0.005 | -2.81 |
| KXNHLGOAL-26OCT01PHINJ-NJSNOESEN11-1|yes | True | 1.92 | False | NJD:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.091 | 0.1228 | -0.005 | -1.92 |
| KXNHLAST-26OCT01PHINJ-NJAMANTHA39-1|no | False | 0.0 | True | NJD:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.8071 | 0.871 | -0.01 | None |
| KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes | False | 0.0 | False | NJD:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.1029 | 0.1465 | -0.005 | None |
| KXNHLAST-26OCT01PHINJ-NJLEVANGELISTA77-1|no | False | 0.0 | False | NJD:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_LOST | 0.7081 | 0.775 | -0.015 | None |
| KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no | False | 0.0 | True | NJD:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.6895 | 0.7637 | -0.015 | None |
| KXNHLGOAL-26OCT01PHINJ-NJLEVANGELISTA77-1|no | False | 0.0 | True | NJD:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.7543 | 0.8142 | -0.005 | None |
| KXNHLGAME-26OCT01PHINJ-NJ|no | False | 0.0 | False | PHI:WINS | False | THESIS_WRONG_EXPRESSION_LOST | 0.0 | 0.4386 | -0.005 | None |
| KXNHLTOTAL-26OCT01PHINJ-6|no | False | 0.0 | True | GAME:LOW_EVENT | False | THESIS_WRONG_EXPRESSION_WON | 0.3176 | 0.5583 | -0.005 | None |

## game 2026020010: realised script balanced shots · normal event (5-7) · decided (2+)

portfolio: {"n_bets": 7, "stake": 42.62, "realized_profit": 19.68, "expected_profit": 3.98, "realized_vs_simulated": "> p95", "largest_thesis_share": 0.517, "n_theses": 2, "theses_with_multiple_losses": [], "multiple_losses_on_one_thesis": []}

| bet | chosen | stake | won | thesis | thesis hit | expression | model P(bet|thesis outcome) | model P(win|realised script) | CLV | P/L |
|---|---|---:|---|---|---|---|---:|---:|---:|---:|
| KXNHLAST-26OCT01TBNYR-TBJCARLSON74-2|no | True | 6.44 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9942 | 0.9735 | -0.005 | 0.82 |
| KXNHLGOAL-26OCT01TBNYR-NYRTKARTYE24-1|yes | False | 0.0 | False | NYR:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_LOST | 0.2024 | 0.1375 | -0.005 | None |
| KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no | True | 6.44 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.8639 | 0.7532 | -0.015 | 4.72 |
| KXNHLGOAL-26OCT01TBNYR-TBCDASTOUS51-1|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.969 | 0.9419 | 0.01 | None |
| KXNHLSPREAD-26OCT01TBNYR-TB2|no | True | 4.19 | True | NYR:WINS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.5585 | -0.005 | 2.01 |
| KXNHLGOAL-26OCT01TBNYR-TBRMCDONAGH27-1|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9798 | 0.9564 | 0.01 | None |
| KXNHLSPREAD-26OCT01TBNYR-TB3|no | True | 3.99 | True | NYR:WINS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.6883 | -0.015 | 1.05 |
| KXNHLGOAL-26OCT01TBNYR-TBVHEDMAN77-1|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9633 | 0.9325 | 0.015 | None |
| KXNHLSPREAD-26OCT01TBNYR-NYR2|yes | False | 0.0 | True | NYR:WINS_BY_2PLUS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.5585 | -0.005 | None |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB4|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.5585 | -0.01 | None |
| KXNHLGOAL-26OCT01TBNYR-TBPHOLMBERG29-1|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9494 | 0.8881 | 0.0 | None |
| KXNHLPTS-26OCT01TBNYR-TBJCARLSON74-1|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.8133 | 0.6729 | -0.025 | None |
| KXNHLTEAMTOTAL-26OCT01TBNYR-NYR3|yes | False | 0.0 | True | NYR:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.5585 | -0.01 | None |
| KXNHLSPREAD-26OCT01TBNYR-NYR3|yes | False | 0.0 | True | NYR:WINS_BY_2PLUS | True | THESIS_RIGHT_EXPRESSION_WON | 0.627 | 0.4184 | -0.005 | None |
| KXNHLAST-26OCT01TBNYR-NYRGPERREAULT94-1|yes | False | 0.0 | False | NYR:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_LOST | 0.475 | 0.3279 | -0.015 | None |
| KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no | False | 0.0 | False | NYR:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_LOST | 0.7761 | 0.8224 | -0.02 | None |
| KXNHLAST-26OCT01TBNYR-TBVHEDMAN77-1|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9107 | 0.8147 | -0.005 | None |
| KXNHLGAME-26OCT01TBNYR-NYR|yes | False | 0.0 | True | NYR:WINS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.5585 | -0.015 | None |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB3|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9748 | 0.5585 | -0.005 | None |
| KXNHLAST-26OCT01TBNYR-TBJCARLSON74-2|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9942 | 0.9735 | -0.005 | None |
| KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no | True | 9.14 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.8639 | 0.7532 | -0.005 | 6.97 |
| KXNHLGOAL-26OCT01TBNYR-NYRTKARTYE24-1|yes | False | 0.0 | False | NYR:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_LOST | 0.2024 | 0.1375 | -0.005 | None |
| KXNHLGOAL-26OCT01TBNYR-TBJHARKINS10-1|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9726 | 0.936 | -0.005 | None |
| KXNHLSPREAD-26OCT01TBNYR-TB3|no | True | 9.14 | True | NYR:WINS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.6883 | -0.005 | 2.54 |
| KXNHLSPREAD-26OCT01TBNYR-TB2|no | True | 3.28 | True | NYR:WINS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.5585 | -0.005 | 1.57 |
| KXNHLAST-26OCT01TBNYR-TBVHEDMAN77-1|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9107 | 0.8147 | -0.015 | None |
| KXNHLPTS-26OCT01TBNYR-TBJCARLSON74-1|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.8133 | 0.6729 | -0.015 | None |
| KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no | False | 0.0 | False | NYR:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_LOST | 0.7761 | 0.8224 | -0.01 | None |
| KXNHLGOAL-26OCT01TBNYR-TBJCARLSON74-1|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9449 | 0.8984 | -0.005 | None |
| KXNHLSPREAD-26OCT01TBNYR-NYR2|yes | False | 0.0 | True | NYR:WINS_BY_2PLUS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.5585 | -0.005 | None |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB4|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.5585 | -0.01 | None |
| KXNHLGAME-26OCT01TBNYR-NYR|yes | False | 0.0 | True | NYR:WINS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.5585 | -0.005 | None |
| KXNHLTEAMTOTAL-26OCT01TBNYR-NYR5|yes | False | 0.0 | True | NYR:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_WON | 0.5326 | 0.2664 | -0.005 | None |
| KXNHLSPREAD-26OCT01TBNYR-NYR3|yes | False | 0.0 | True | NYR:WINS_BY_2PLUS | True | THESIS_RIGHT_EXPRESSION_WON | 0.627 | 0.4184 | -0.005 | None |
| KXNHLAST-26OCT01TBNYR-NYRGPERREAULT94-1|yes | False | 0.0 | False | NYR:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_LOST | 0.475 | 0.3279 | -0.015 | None |
| KXNHLTEAMTOTAL-26OCT01TBNYR-TB3|no | False | 0.0 | True | TBL:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9748 | 0.5585 | -0.005 | None |
| KXNHLTEAMTOTAL-26OCT01TBNYR-NYR3|yes | False | 0.0 | True | NYR:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.5585 | -0.01 | None |

## game 2026020011: realised script balanced shots · high event (8+) · decided (2+)

portfolio: {"n_bets": 8, "stake": 44.31, "realized_profit": -4.7, "expected_profit": 1.98, "realized_vs_simulated": "<= p50", "largest_thesis_share": 0.393, "n_theses": 4, "theses_with_multiple_losses": ["CBJ:OFFENSE_4PLUS"], "multiple_losses_on_one_thesis": [{"thesis": "CBJ:OFFENSE_4PLUS", "thesis_happened": true, "n_lost": 2, "loss": 8.77, "reading": "thesis happened but its expressions missed: expression risk, not a thesis error"}]}

| bet | chosen | stake | won | thesis | thesis hit | expression | model P(bet|thesis outcome) | model P(win|realised script) | CLV | P/L |
|---|---|---:|---|---|---|---|---:|---:|---:|---:|
| KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes | True | 4.12 | False | CBJ:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_LOST | 0.3918 | 0.3874 | -0.005 | -4.12 |
| KXNHLGOAL-26OCT01BUFCBJ-BUFNOSTLUND86-1|no | True | 8.22 | True | BUF:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.8124 | 0.8206 | 0.0 | 1.57 |
| KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no | False | 0.0 | True | CBJ:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.8146 | 0.7726 | -0.005 | None |
| KXNHLGAME-26OCT01BUFCBJ-BUF|no | True | 2.34 | True | CBJ:WINS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.5954 | -0.005 | 2.27 |
| KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | False | 0.0 | True | BUF:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.5576 | 0.5406 | -0.015 | None |
| KXNHLAST-26OCT01BUFCBJ-CBJVNICHUSHKIN43-1|no | True | 6.79 | False | CBJ:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_LOST | 0.7111 | 0.656 | -0.01 | -6.79 |
| KXNHLGOAL-26OCT01BUFCBJ-CBJKJOHNSON91-1|no | False | 0.0 | True | CBJ:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.7651 | 0.72 | -0.005 | None |
| KXNHLGOAL-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | False | 0.0 | True | BUF:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.5719 | 0.6023 | -0.005 | None |
| KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes | True | 4.65 | False | CBJ:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_LOST | 0.3918 | 0.3874 | -0.005 | -4.65 |
| KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no | True | 8.98 | True | CBJ:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.8146 | 0.7726 | -0.005 | 1.83 |
| KXNHLGAME-26OCT01BUFCBJ-BUF|no | False | 0.0 | True | CBJ:WINS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.5954 | -0.005 | None |
| KXNHLSPREAD-26OCT01BUFCBJ-BUF3|no | False | 0.0 | True | CBJ:WINS | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 0.7817 | -0.005 | None |
| KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | True | 4.78 | True | BUF:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.5576 | 0.5406 | -0.015 | 2.97 |
| KXNHLAST-26OCT01BUFCBJ-CBJVNICHUSHKIN43-1|no | False | 0.0 | False | CBJ:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_LOST | 0.7111 | 0.656 | -0.01 | None |
| KXNHLGOAL-26OCT01BUFCBJ-CBJKJOHNSON91-1|no | False | 0.0 | True | CBJ:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.7651 | 0.72 | -0.005 | None |
| KXNHLGOAL-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | True | 4.43 | True | BUF:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.5719 | 0.6023 | -0.005 | 2.22 |
| KXNHLTEAMTOTAL-26OCT01BUFCBJ-BUF3|no | False | 0.0 | False | BUF:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_LOST | -0.0 | 0.16 | -0.005 | None |

_Prospective thesis-card evidence. THESIS / EXPRESSION / PRICE / MODEL / PORTFOLIO results are kept separate on purpose: a right thesis expressed through a contract that lost is not a wrong prediction. A handful of games proves nothing; never tune to one slate._
