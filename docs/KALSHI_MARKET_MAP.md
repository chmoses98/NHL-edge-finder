# Kalshi NHL market map

> Source of truth for what exists: `data/catalog/discovery_summary.json` (written by `nhl discover` on a runner) and
> the live discovery rows on `data-archive/catalog/`. Families live in `data/catalog/market_ontology.yaml`.

Observed live 2026-09-29 (docs/probe/samples): `KXNHLGAME` (winner; `custom_strike.hockey_team`, title "San Jose
wins"), `KXNHLSPREAD` (puck line; `strike_type=greater`, `floor_strike=2.5`, "Vancouver wins by over 2.5 goals"),
`KXNHLTOTAL` ("Full Game: Over 8.5 goals scored"). Series `fee_type=quadratic_with_maker_fees`, `fee_multiplier=1`.
Settled markets carry `status=finalized`, `result=yes|no`. Ticker convention `KXNHLGAME-26OCT05SJDAL-SJ`: event
suffix is `YYMMMDD` + AWAY + HOME with short tricodes (`SJ`, `TB`, `NJ`, `LA`), market suffix names the team
(digits appended for alternate lines). Rules text: "If X wins the A vs B NHL game originally scheduled for ...".
Postponement rule: remains open if played within 48h; otherwise resolves to a fair price (our settlement leaves
these UNSETTLEABLE and defers to Kalshi's result).

| family | series | settles on | status | notes |
|---|---|---|---|---|
| game_winner | KXNHLGAME | FINAL_INCL_OT_SO | SUPPORTED | verified on live markets; settlement tested |
| game_spread (puck line, alt lines) | KXNHLSPREAD | FINAL_INCL_OT_SO | SUPPORTED | OT/SO win is a 1-goal margin |
| game_total (alt totals) | KXNHLTOTAL | FINAL_INCL_OT_SO | SUPPORTED | shootout counts one goal |
| team_total | KXNHLTEAMTOTAL | FINAL_INCL_OT_SO | SUPPORTED (pricing + settlement) | series name unverified until discovery lists it |
| game_regulation_winner | KXNHLREG*, KXNHL3WAY | REGULATION | PARTIAL / NEEDS_RULE_REVIEW | priced and settled (tie = NO); tie handling to confirm from rules |
| game_win_margin | KXNHLWINMARGIN | FINAL_INCL_OT_SO | PARTIAL / NEEDS_RULE_REVIEW | bucket bounds to confirm |
| game_overtime, game_shootout, game_both_teams_score | KXNHLOT, KXNHLSO, KXNHLBTTS | FINAL_INCL_OT_SO | PARTIAL | priced from the sim; series names unverified |
| period_winner / period_total / period_spread | KXNHL1P... | PERIOD | V1: UNSUPPORTED (RESEARCH). V2 shadow: PARTIAL (rules verified, no settlement) | nhl-sim-2.0 prices them from per-period draws; period settlement not implemented (see below) |
| first_goal | KXNHLFIRST* | EVENT | UNSUPPORTED (RESEARCH) | |
| player_goals / points / assists / shots / goalie_saves / player_h2h | KXNHLGOALS... | FINAL_INCL_OT | UNSUPPORTED (RESEARCH) | player model is roadmap |
| parlay_combo | KXNHLPREPACK*, KXMVENHL* | | UNSUPPORTED (RESEARCH) | |
| season_champion | KXSTANLEYCUP, KXNHLCUP... | SEASON | UNSUPPORTED (RESEARCH) | |
| season_awards, non_hockey_or_office | KXHART... | | UNSUPPORTED (UNMODELABLE) | |

Any series not matched lands in `UNRESOLVED`, is kept in the capture with its raw payload, and raises a coverage
alarm in the conductor run. It is never dropped.

## Semantics cross-checks (`kalshi/contracts.build_contract`)

- Regulation wording in the title/rules switches `settles_on` to REGULATION and downgrades MODELABLE to BUILDABLE.
- The rules' "originally scheduled for" date must match the ticker date, else confidence is low and the contract
  is UNRESOLVED (never priced, never settled).
- The game join is by (date, set of two team ids), never by ticker order; the NHL schedule decides home/away.

## Prices and fees

Executable prices only: buying YES costs `yes_ask`, buying NO costs `no_ask`; midpoint is reported as `p_market`.
Fee: Kalshi quadratic schedule, taker `0.07 * P * (1 - P)` per contract (maker 0.0175), ceiling per order in cents,
per-series `fee_multiplier` honoured via `FeeSchedule.from_series`. This is an estimate; the router's accounting notes
verified the taker formula to the cent against exchange fills. `edge_*_after_fee` is EV per contract in dollars.


## Period family rule review (2026-09-29, live rule text from the production market board)

| series | YES means (rules_primary / rules_secondary) | simulator mapping (nhl-sim-2.0) |
|---|---|---|
| KXNHL1P / 2P / 3P `-TEAM` | "If X wins the Nth period"; "Only goals scored during the Nth period count"; 3rd period "(excluding overtime)" | team's period-N goals > opponent's |
| KXNHL1P / 2P / 3P `-TIE` | "If neither team wins the Nth period" | period-N goals equal |
| KXNHL1PSPREAD / 2P / 3P | "If X wins by more than 1.5 goals in the Nth period"; "3rd period markets do not include overtime" | team's period-N margin > 1.5 |
| KXNHL1PTOTAL / 2P / 3P | "If the teams collectively score more than x goals in the Nth Period" (titles say "points"; rules say goals) | period-N total > x |

All: postponed games that start within 48 h resolve on the official result; otherwise "fair price". Empty-net goals
count (nothing excludes them). Full-game KXNHLTOTAL and KXNHLTEAMTOTAL: regulation + OT goals, and a shootout win is
credited as one goal, which is exactly the simulator's final-score convention. KXNHLOT: "at least 1 overtime period is
played" (opening faceoff of OT taken) == regulation tie.

**Status: PARTIAL, not SUPPORTED.** Contract semantics are confirmed and the simulator maps them, but the settlement
engine does not yet read period line scores, so a period contract cannot be settled or evaluated by this repository.
Promotion requires period settlement (boxscore/landing `linescore.byPeriod`) plus tests. V1 is unchanged (no periods).
