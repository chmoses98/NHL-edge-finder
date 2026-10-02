# HANDOFF: NHL thesis-card repair pass (2026-10-02)

Scope: infrastructure / reporting defects found on the first prospective slates, plus contract-selection, research
governance and research staking on top of the existing optimiser. **No model weight, player probability, simulation
parameter, family label, confidence haircut or calibration was changed.** Everything stays RESEARCH_ONLY; nothing places
or routes a wager. Method detail: `docs/research/THESIS_ENGINE.md` section 16.

## Root causes (verified against production code and the data-archive at 2026-10-02 ~12:45Z)

1. **Final card mixed generations.** `thesis_postmortem.build_report` found each game's latest (run_id, decided_at)
   but then kept every row with that run_id. A worker run id spans ~5h and ~5 simulate generations. For 2026-10-01's
   first three games it reported 23 chosen bets (cap 12), P/L −$11.25 on $113.16; the snapshot-unique card is 11 bets,
   +$4.14 on $53.71 (`docs/research/repair_pass/report_thesis_reconstructed_2026-10-02T1300Z.md`).
2. **Settle job crashed whenever it ingested two games in one run.** `player_events/<table>` was appended per game with
   the same timestamp + run id → `ImmutabilityError` (worker log, run 36955011158: 02:20Z and 04:20Z). Only the 02:35Z
   run, with a single new game, succeeded — which is why exactly three games were settled.
3. **Conductor lost yesterday's games.** It decided "settle?" from the newest schedule snapshot only; that snapshot is
   fetched for the current ET date, so from 04:20Z the 2026-10-01 games were invisible and settle was never due again
   (STATUS_settle stayed at 02:35Z; MIN@NSH even had events ingested but no result).
4. **"Stale" STATUS_evaluate.json** was the legacy `eval/STATUS_evaluate.json` (written while the job's root was wrong,
   until 2026-09-30); the root breadcrumb was current. Readers looked at the wrong file.

## What changed

- Snapshot identity: `snapshot_id` = hash(run_id, decided_at_utc) on every new `thesis_games` / `thesis_decisions` row;
  legacy rows reconstruct the identical id. FINAL_CARD_UNIQUE = the one latest complete pregame snapshot per game,
  chosen from `thesis_games`; mismatches / duplicates → `AMBIGUOUS_FINAL_SNAPSHOT`, excluded from P/L. Invariant
  `final_card_n <= sum(game caps)` reported per slate. ALL_PROSPECTIVE_DECISIONS kept separately (no P/L).
- Completeness per slate (`games_scheduled / final / settled / player_events_ingested / thesis_evaluated / missing`,
  `final_card_complete`, `postmortem_complete`) and the label `COMPLETE — n/n` or `PARTIAL — k/n games evaluated`.
- Settle: per-game ledger parts, contained player ingestion, a settle backlog in STATUS_settle (`backlog`,
  `games_pending`, `games_terminal`). Conductor: 4-day schedule union; settle due every 45 min while any game 3-72h
  past start is not COMPLETE; evaluate due after settle and whenever older than settle. Evaluate writes its breadcrumb
  LAST, at the root and mirrored to `eval/`, with per-step status and slate completeness.
- Expression fidelity (STRUCTURAL / DIRECT / FRAGILE / NONE; capture, lift, relation, scope), expression preference
  within one price tick (reliability, then fidelity), research governance (FUNDED_RESEARCH / SHADOW_ONLY / REJECTED;
  player-prop tier; MARKET_DISAGREEMENT_REVIEW gate with honest corroboration; opponent-adjustment labels), whole-dollar
  research stakes ($250 bankroll, $5 max, round up, never past a cap), per-game review block, enriched postmortem
  (THESIS / EXPRESSION / PRICE / MODEL / PORTFOLIO / GOVERNANCE), `research.rules_replay`.
- Versions: `nhl-thesis-1.1`, `nhl-card-1.1`. Preregistered model leads: `docs/research/PREREGISTERED_HYPOTHESES.md`.

## Diagnostic replays (NOT evidence that the new rules are better)

At each game's final production decision instant, pregame data only, link-copied archive. The old code reproduced the
production-logged card exactly for all 8 games of 2026-10-01 (same bets, max |Δp| 0.0000), which also verifies replay
determinism and point-in-time behaviour.

| slate | card | bets | stake | player props | settled | realized P/L (settled only) |
|---|---|---:|---:|---:|---:|---:|
| 2026-10-01 | OLD nominal card | 30 | $253.01 | 26 | 11 | +$4.15 |
| 2026-10-01 | NEW optimiser card (nominal) | 30 | $254.10 | 25 | 11 | +$2.37 |
| 2026-10-01 | NEW FUNDED research | 11 | $36 | 6 | 4 | +$2.36 |
| 2026-09-30 | OLD nominal card | 12 | $142.47 | 10 | 12 | −$33.35 |
| 2026-09-30 | NEW FUNDED research | 5 | $18 | 3 | 5 | −$11.00 |

2026-10-01: 19 card bets shadow-only, 1 removed by the expression-fidelity rule (BUF@CBJ: Thompson 1+ assist NO →
BUF −2.5 NO, adjusted EV within 0.3 pts, capture 1.00 vs 0.83; on this night the BUF@CBJ nominal card made +$0.57 instead of +$2.38 — one outcome, not evidence either way),
4 by the market-disagreement gate (McDavid 1+ / 2+ assist NO, Carlson assist NO, Trocheck assist NO). Five Oct 1 games
were unsettled in the archive at replay time (the settlement bug). 2026-09-30 (no production thesis card existed; old
code replayed at 23:20Z / 01:50Z): 2 removed by the gate (Sorokin saves NO, Zuccarello assist NO), 0 substitutions.
Full tables: `docs/research/repair_pass/replay_2026-10-01/replay.md`, `.../replay_2026-09-30/replay.md`.

## Still needs prospective evidence

Everything about whether fidelity preference, the gate or the player-prop tier improve results (H2, H3), the assists /
points compression (H1), saves score effects (H4), and settlement completeness in production (H5). Two slates prove nothing.
