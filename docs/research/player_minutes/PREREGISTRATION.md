# `player-minutes-1.0`: prospective ice-time and power-play-time test (RESEARCH_ONLY)

Registered before any `player-minutes-1.0` record exists. Separate from, and not a change to, the WORKLOAD_V1_LC shots test
(`docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md`), whose sample, looks, rule and branch (`workload-shadow-data`) are untouched. Nothing here is published,
priced or routed; promotion of any ice-time model is a separate decision that needs the owner's explicit approval.

## What is recorded

For every regular-season game that starts within 14 hours and has no record yet, at least 10 minutes before the drop, one write-once record per candidate skater
(the skaters who dressed in either team's recent games, exactly the LC candidate set) is written to the orphan branch `player-minutes-data`:

* `predictions`: `M0` = WORKLOAD_V1's expected ice time by game state (the frozen, unchanged `workload_v1` model, trained as for LC) as total, power-play, short-handed, even-strength and overtime minutes;
  `M1` = `M0` total times `exp(clip(0.23 · log((last3 + 1) / (M0 + 1)), −1, 1))` (`data/params/minutes-v1.json`; frozen; players with fewer than three known games keep `M0`). Power-play time has no adjusted variant: nothing was found to add (development result).
* `inputs`: everything observed before the drop that a later hypothesis might use: the player's last three dressed games' ice time; every `context/lines` row for him (confirmed/projected line, power-play and
  penalty-kill unit, scratch/injury flags, the source's own `updatedAt` and source name, our observation time); every matching `context/injuries` row; the incumbent PLAYER_SIM_V1's expected total and power-play
  minutes as captured at record time (where it published them); the snapshot instants. These are stored, never used by `M0`/`M1`.
* provenance: `predicted_at_utc`, `pregame` (>= 10 min before the drop), model and inputs fingerprints, code commit, activation fingerprint (a record from a different model fingerprint is refused and, if present, excluded).
* outcomes: after the game is final, a separate write-once `outcomes/` file with the official ice time by state and shots. A prediction record is never modified.

Missing records are never back-filled; a game that starts without a pregame record is listed in the collection coverage audit (the same audit as the LC test's). Lineup/role inputs have no history, so they exist only from the day they are archived.

## Hypotheses (confirmatory, three, each judged on its own)

Sample: records that count (pregame by their own clock, written per the append-only manifest before the drop, by the frozen model), paired with the official outcome (`toi_s > 0`, i.e. he dressed and played) and with the comparator below, ordered by (game start, game, player).
Loss: squared error in minutes. Interval: game-clustered bootstrap (4,000 draws, seed 20261024) of the ratio of summed losses; "relative change" = challenger / comparator − 1.

| id | question | comparator | passes when the 95% interval's upper bound is below |
|---|---|---|---|
| H1 | does WORKLOAD_V1 predict total ice time better than the production minutes? | PLAYER_SIM_V1 `toi_minutes`, last forecast archived before the drop (`projection-data`) | −2% |
| H2 | does it predict power-play time better? (rows with `shifts_ok` and an incumbent value captured at record time) | PLAYER_SIM_V1 expected power-play minutes captured in the record | −3% |
| H3 | does recent usage add to WORKLOAD_V1 total ice time? | `M0` | −0.5% |

H2's comparator exists only for players the production engine priced (it is taken from its `predictions_player` rows), so H2's pairs accumulate more slowly and H2 may stay INCONCLUSIVE for a long time; that is reported as it is.

Development expectations (2023–25, exposed seasons, so selection evidence only): H1 −4.5%, H2 −8.0%, H3 −1.1%.

## Looks and rule

Looks at 10,000 (descriptive only, no pass flag), 30,000 (**decision**) and 60,000 (**final**) paired player-games, taken as the first N pairs in the order above. All three hypotheses are computed on that same first-N sample
(H2 restricted to the rows that have a captured incumbent power-play value; if that restricted sample has fewer than 10,000 pairs at a look, H2 is INCONCLUSIVE at that look and is reported with its n; a sample under 200 pairs is reported as inconclusive).
A look is computed only once every recorded game that starts at or before its N-th pair has its official outcome (a recorded game more than 7 days old that never settled is ignored), so that the first N pairs are final;
it is then computed once, stored with a hash of its sample keys and its last key, and never rewritten. The scoreboard shows the cumulative numbers as descriptive only and states a verdict per hypothesis only from the looks:
a hypothesis that passes at the decision look is reported as supported prospectively; one that does not is carried to the final look unchanged; one that has not passed at the final look is reported as not supported.
Non-finite rows are dropped and counted. No threshold or sample is changed after data exist.
There is one decision look and one final look for each of three separately judged hypotheses; each statement is made per hypothesis at its stated interval, with the look it was made at.

A pass is evidence for a recommendation to the owner, never a promotion: M0/M1 are not wired to anything, and the production minutes, prices, stakes and routing are unchanged.

## Constraints

* No change to the LC test, the WORKLOAD_V1 frozen parameters, the production models or the sealed-ledger workflows (which stay dormant). No wager, stake or cap change.
* New hypotheses (for example confirmed lines, power-play units, expected ice time from a lineup source) need a new versioned schema and a new preregistration; the stored inputs are the data for them. Amendments only before the affected data exist.
