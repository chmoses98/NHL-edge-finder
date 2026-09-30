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
| period_winner / period_total / period_spread | KXNHL1P... | PERIOD | V1: UNSUPPORTED (RESEARCH). V2 shadow: MODELLED_RESEARCH_ONLY, settled (nhl-period-settle-1.0, 2026-09-30) | nhl-sim-2.0 prices them from per-period draws; settled from official play-by-play period goals |
| first_goal | KXNHLFIRSTGOAL | EVENT | V1: UNSUPPORTED. PLAYER_SIM_V1 shadow: MODELLED_RESEARCH_ONLY, settled | first scorer from simulated event order; no-goal-before-shootout left UNSETTLEABLE (rules silent) |
| player_goals / player_points / player_assists | KXNHLGOAL, KXNHLPTS, KXNHLAST | FINAL_INCL_OT (official stat line) | V1: UNSUPPORTED. PLAYER_SIM_V1 shadow: MODELLED_RESEARCH_ONLY, settled | see "Player markets" below |
| goalie_saves | KXNHLSAVE (singular; KXNHLSAVES never seen live) | FINAL_INCL_OT (official saves) | V1: UNSUPPORTED. PLAYER_SIM_V1 shadow: MODELLED_RESEARCH_ONLY, settled | ladder of N+ thresholds per goalie |
| player_shots / player_h2h | (none listed live) | | UNSUPPORTED (no live series) | |
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


## Player markets (live rule text, 2026-09-29 production board; `docs/probe/samples/player_sources/`)

| series | ticker example | title / strike | YES means (rules_primary) |
|---|---|---|---|
| KXNHLGOAL | `KXNHLGOAL-26SEP29CHIVGK-CHIAMANGIAPANE26-2` | "Andrew Mangiapane: 2+ goals", `strike_type=greater`, `floor_strike=1.5` | "If <player> records 2+ goals in the <A> vs <B> NHL game originally scheduled for <date>" |
| KXNHLAST | `KXNHLAST-26SEP29CHIVGK-CHIBBYRAM24-1` | "Bowen Byram: 1+ assists", floor 0.5 | "... records 1+ assists ..." |
| KXNHLPTS | `KXNHLPTS-26SEP29CHIVGK-CHIBBYRAM24-1` | "Bowen Byram: 1+ points", floor 0.5 | "... records 1+ points ..." |
| KXNHLSAVE | `KXNHLSAVE-26SEP29CHIVGK-CHISKNIGHT30-26` | "Spencer Knight: 26+ saves", floor 25.5 | "... records 26+ saves ..." |
| KXNHLFIRSTGOAL | `KXNHLFIRSTGOAL-26SEP29CHIVGK-CHIALEVSHUNOV55` | "Artyom Levshunov: First Goalscorer", `strike_type=structured` | "If <player> scores the 1st goal in ..." |

`rules_secondary` (all five): "If a player is active but never enters the game, the market settles to the last fair
market price before game start. Once a player enters the game, the market settles based on the player's <stat>
recorded." Settlement source: NHL (nhl.com); series contract terms `HOCKEYENTITYSTAT.pdf`; fee_type `quadratic`, multiplier 1.

Mapping (`players/pricing.py`, `settlement/player.py`): the official boxscore line (overtime counts, the shootout never
does); a player absent from the boxscore or dressed with 00:00 TOI is UNSETTLEABLE (Kalshi's fair-price rule, never
guessed); PLAYER_SIM_V1 probabilities are conditional on the player playing (goalies: starting). Player identity: the
market suffix is `<Kalshi team code><first initial><LAST NAME, may be truncated><jersey>[-<N>]`; **Kalshi's jersey numbers
are stale for players who changed teams** (73 of 832 opening-night contracts: e.g. Brady Tkachuk `FLABTKACHUK7`, roster #8),
so resolution is team + jersey + name, falling back to team + first initial + full last name, and refusing ambiguity.
Opening-night inventory (2026-09-29, 5 games): 297 goals, 207 points, 155 assists, 165 first-goal, 10 saves contracts
(834 of 1,089 joined contracts = 77%).
