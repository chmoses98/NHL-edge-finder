# DailyFaceoff data rights: decision, inventory of published material, remediation proposal (2026-10-26)

Owner decisions of 2026-10-26: (1) pursue explicit written permission (draft: `DFO_PERMISSION_REQUEST.md`); do **not** claim permission until received; (2) stop new publication of raw DailyFaceoff page bodies, raw JSON and HTML samples in public repositories; preserve the smallest useful derived features only where rights permit; inventory previously published material and propose remediation **without history rewrites or alteration of frozen experiments**.

## Status
| item | status |
|---|---|
| Permission | **Not requested yet / not received.** No terms of use were found (`SOURCE_AUDIT_2026-10-25.md`). Nothing in this repository claims permission. |
| New raw publication | **Stopped** (PR #98): `context/dailyfaceoff_raw` is no longer written and the archive refuses that kind; probe scripts save no HTML / embedded-page copies. The capture worker picks the change up at its next handover (within ~5 h of the merge); partitions written before then are listed below. |
| Derived features | Still published (see "what is derived" below) pending the answer; a minimization specification is ready. |
| Browser impersonation | Removed everywhere (PR #95). |

## Inventory of previously published material (public repository `chmoses98/NHL-edge-finder`)
| where | what | size | period | kind |
|---|---|---|---|---|
| `data-archive` branch, `context/dailyfaceoff_raw/` | verbatim goalie-page rows (the `data` array of the page's embedded JSON, sportsbook fields stripped) as written by each `context` run | 522 files, 3.4 MiB | 2026-09-29 → 2026-10-26 | **raw** |
| `main`, `docs/probe/samples/dailyfaceoff_goalies.html`, `dailyfaceoff_goalies_date.html` | full page HTML | 223 KB | committed 2026-10-22 and earlier (probe) | **raw** |
| `main`, `docs/probe/samples/player_sources/dfo_lines_{boston-bruins,edmonton-oilers,vegas-golden-knights}.html` and `.next_data.json` | full team line-combination pages and their embedded JSON | 733 KB + 263 KB | 2026-10-22 | **raw** |
| `main`, `docs/probe/samples/rotowire_goalies.html`, `player_sources/rotowire_nhl_lineups.html` | Rotowire pages (same class of risk; a different site) | — | 2026-10-22 and earlier | **raw** |
| `data-archive` branch, `context/lines/` | per-player rows: team, category, unit, slot, jersey, name, injury status, game-time-decision flag, DFO player id, `lines_updated_at_utc`, `lines_source` (includes the reporter's name), our observation time, resolved NHL player id | 504 files, 5.3 MiB | 2026-09-30 → 2026-10-26 | derived (small facts) |
| `data-archive` branch, `context/goalie_observations/` | per-team goalie status rows (name, status, DFO label in `note`, `dfo_goalie_id`, source time) | 583 files, 0.6 MiB | 2026-09-29 → 2026-10-26 | derived |
| `player-minutes-data` branch, `records/` | each candidate's DFO line rows (as `inputs.lines`) | part of 833 records | 2026-10-24 → | derived (copied) |
| `projection-data` / app contract | forecast rows carry participation and starter status derived from the above | — | — | derived |

The frozen experiments (`workload-shadow-data`, `player-minutes-data`, their activation fingerprints and manifests) contain only derived rows; none of them is touched by any proposal below.

## Remediation proposals (all non-destructive; the owner decides, none is applied)
1. **Stop (done).** Raw bodies are no longer produced anywhere.
2. **Stop shipping copies in the working tree.** `git rm` the eleven sample files above from `main` (this removes them from the current tree only; history is unchanged). Check first that no test or parser fixture reads them — none does (verified by search). Counter-argument: they are probe evidence; the structure they show is described in `docs/probe/probe_results.md`.
3. **Make the raw archive partitions unreachable without rewriting history.** Options, least to most intrusive: (a) leave as is, documented here; (b) a follow-up commit on `data-archive` deleting `context/dailyfaceoff_raw/` (history still holds it); (c) make the repository's data branches private. A history rewrite (BFG / force-push) is **not** proposed: it would break the archive's manifest hashes and the frozen experiments' provenance.
4. **Minimize derived rows (staged, after the answer).** The smallest set the models use: team, player id, category, unit, slot, status flags, `updatedAt`, observation time and a *source class* (Warmups / Practice / Projected / Last Game / other) instead of the free-text label that includes a reporter's name; drop jersey, display name and DFO ids after resolution. This changes the archived `context/lines` schema (consumers read `player_id`, `unit`, `slot`, `lines_source` substring tests), so it needs a compatibility pass and is not applied now.
5. **If permission is refused:** switch off the DailyFaceoff line and goalie feeds; production falls back to shift-derived deployment (`RECENT_SHIFTS`) and NHL-published goalie information (impact: no power-play-unit, scratch or early starter information; details in `DAILYFACEOFF_COMPLIANCE.md`).
