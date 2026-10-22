# Commit map: PR #53 branch before and after the rebuild

On 2026-10-21 the branch `claude/nhl-model-improvement-f6kn0k` was rebuilt on the exact tip of PR #52 (`1040fbb`) so that its diff excludes `main`'s PR #51 (`research/projection_foundation/**`). The 21 research commits were replayed unchanged (cherry-pick, no conflicts, subjects identical). The tree of the new tip differs from the old tip only by PR #51's five files.

* Backup of the pre-rebuild branch: remote branch `backup/pr53-pre-rebuild-6d5c366` (tip `6d5c366f`). Delete it once the rebuilt PR is accepted.
* `experiment_registry.jsonl` is byte-identical before and after (25 entries, hash chain verified). Its `code_commit` fields hold **pre-rebuild SHAs**; use the map below to find the corresponding rebuilt commit (or the backup branch for the original object).

| pre-rebuild | rebuilt | subject |
|---|---|---|
| `2f8a591c` | `10ba26fb` | Model research: archive reconstruction modules, scoring, append-only hash-chained registry, preregistration of |
| `20baa265` | `68efe2b6` | Model research: M-DIST-1, M-CAL-1, M-CAL-2 results (V1 totals not too narrow; recalibration and strength-noise |
| `f736d29e` | `325e03ad` | Registry v1.1: stricter PROMISING rule (separately versioned, v1.0 untouched), power disclosure, side-by-side  |
| `62bef9cd` | `d1d6a5dc` | Model research: script calibration study (M-SCRIPT-1) |
| `86340795` | `ccbaeeb9` | Model research: M-MKT-1 (no incremental information beyond the Kalshi T-60 mid; protocol deviation noted and r |
| `6c8cb791` | `75d03c61` | Model research: M-LIVE-1 single look, M-INFO-1 goalie-confirmation event study (rev 2 after in-play contaminat |
| `2df8b31b` | `7e949391` | PR52 review fixes: expression engine (double-counted model weight made BET impossible; input/unit/crossed-book |
| `bcd25a3b` | `a1d357d4` | PR52 data-review fixes: coverage usable-quote ordering (D1), quiet-market age rule option (D2), discriminating |
| `38c2118a` | `30545381` | D2 sensitivity: corrected quiet-market age rule moves no frozen hypothesis ROI by more than 0.61 points and fl |
| `30a91a8f` | `7b13769a` | Model research: player usage study (M-PLAYER-1), Oct 20 model view, D2 sensitivity |
| `38232a60` | `79ed15b5` | Model research: player usage study (M-PLAYER-1), Oct 20 model view |
| `1a27cce1` | `5f5ebd62` | Daily research feedback loop: idempotent ledger, blinded prospective scorecard with one-time looks, manual-dis |
| `5a63e69a` | `b26d227a` | Model research: generated results tables, PR52 independent review report |
| `8eea69e9` | `c9a7c837` | Reports: actual wager audit + Oct 20 case study, prediction-error audit |
| `ead59945` | `9d89a5ac` | Reports: challenger comparison, prospective protocol; preregister M-SHADOW-1 |
| `402c4327` | `a0cdb871` | Reports: market families and expression, matchup and script study |
| `d5c743ce` | `b3651611` | Report: information-event assessment |
| `a5095def` | `66863051` | Report: data quality and lineage |
| `f6ad77b0` | `b5bf5acd` | Model research: reproducible table builder, lint |
| `4e64dec3` | `6971b81e` | Reports: executive report, README, progress ledger |
| `6d5c366f` | `1a05fb2a` | Exec report: registry count |
