# Prospective ledger isolation review (2026-10-22)

> RESEARCH ONLY. **Verdict: FAIL — a branch of this repository cannot protect the prospective holdout. `publish=true` is disabled (fail-closed) until an isolated store exists.** Checked through the GitHub API with the owner's token on 2026-10-22; nothing was published.

## What was checked and what was found

| question | finding | consequence |
|---|---|---|
| Who can read a ledger branch? | The repository `chmoses98/NHL-edge-finder` is **public** (`private: false`, `visibility: public`). Every branch, commit, file, Actions log and Actions artifact is readable by anyone on the internet (artifacts by any signed-in GitHub user). | A `model-research-ledger` branch holding outcome-bearing rows would publish the holdout to everyone, instantly. **Fatal on its own.** |
| Repository collaborators | Exactly one: the owner (`admin`). | Not the risk; the public setting is. |
| Branch protection | `protected: false` on **every** branch, including `main` and `data-archive`. | The ledger could be force-pushed, rewritten or deleted by any workflow with `contents: write` (several exist, e.g. the capture worker) or by the owner. History is not tamper-proof by platform rule. |
| Can development or tuning jobs read it? | Yes. Any workflow (including CI on any pull request) can `git fetch origin <branch>` with the default read token; public readers and this assistant's GitHub tools (`get_file_contents` with a `ref`) can read any branch. | Blinding cannot be enforced technically against development work if the data sits in the repository in readable form. |
| Is the ledger itself tamper-evident? | No. `shadow_game_ledger.jsonl` is plain JSONL with no hash chain (unlike `experiment_registry.jsonl`, which is chained and verified). Idempotence is by `game_id` only. | A silent edit of a past row would not be detected by the file itself. |
| Accidental exposure through CI? | Checked in the real run (39773684266): logs print only counts (`games_final`, `appended`, `reproduction_max_abs_diff`) and the blinded scorecard; the default artifact is 2 outcome-free files (689 bytes); the ledger-bearing artifact is created only when `publish=true`. Since the repo is public these artifacts/logs would be public too, so the staging artifact is renamed `...ledger-staging...` (it was misleadingly called `private`). | Nothing outcome-bearing has left the runner so far. |
| Do the dry-runs already leak anything? | The two public dry-run artifacts and logs contain: date, game counts, a 0.0 reproduction difference, sportsbook-coverage share and mean slate age. No outcome, forecast value or performance measure. | None. |

## Interim hardening (in this PR)

* `model_research_daily.yml`: a first step **fails the run if `publish == 'true'`** with a pointer to this document, so the outcome-bearing ledger cannot be pushed to a public branch by accident. `publish=false` (the default) is unaffected.
* Static test `test_daily_publish_is_refused_while_the_repository_is_public_and_the_ledger_is_not_isolated`.

## Why a separate branch is not a fix, and what would be

Branch ≠ access boundary on GitHub. The only things that make data unreadable to the repository's readers, to unrelated workflows and to the development process itself are (a) not storing it in readable form, or (b) storing it somewhere with a different access list.

### Option A — sealed (encrypted) commit–reveal ledger — **recommended**

* The daily job holds only a **public key** (committed in the repository, fingerprint pinned in code and in the registry). It can encrypt; it cannot decrypt.
* Each game's full ledger row (forecasts **and** outcomes, PIT, attribution class) is encrypted with that public key (`gpg --encrypt`, available on the runner) and committed as `sealed/<game_id>.gpg`. A plaintext **index** is hash-chained (`seq, game_id, date, sealed_sha256, prev_hash, entry_hash`) — no forecasts, no outcomes — so idempotence, row counts and tamper-evidence need no secret. The blinded scorecard is computed from the index alone.
* The **private key never enters GitHub** (not in Actions secrets, not in an environment). The owner generates it once and keeps it offline. At the 150-game look the owner decrypts locally and runs `daily look`, which verifies the chain and every `sealed_sha256` first.
* Result: the holdout is unreadable by the public, by collaborators, by every workflow, and by development tooling including this assistant, **until the owner chooses to open it**; commit timestamps prove the forecasts pre-date the games (commit–reveal). Force-pushing or rewriting is detectable by anyone holding a mirror and by the chain.
* Costs: the owner must generate a key pair once and supply the public key; the look is a deliberate manual act.

### Option B — separate **private** repository for the ledger

A private repository (`chmoses98/nhl-research-ledger`, creatable by the owner or via tooling) with a **fine-grained token limited to that repository**, stored as a secret of a protected Actions *environment* restricted to `main` with a required reviewer, used only by the publish job. Isolates readers; but the token is a standing credential that a compromised `main` workflow could exfiltrate, outcome-bearing data still exists in plaintext on GitHub, and the owner must create the repository and token (not possible for this assistant).

### Option C — make this repository private

Removes public access but leaves every collaborator/workflow/tooling reader (and this assistant) with read access to branches. Not an isolation mechanism for the holdout; also a much larger decision (it hides the whole research record and the `data-archive` the project uses).

### Not an option

Publishing to a branch, a release, an artifact or a gist of this public repository and calling it private; relying on obscurity of a branch name; relying on this assistant "not looking".

## What remains safe and enabled today

`publish=false` dry-runs (counts, integrity checks and blinding status only; verified), the append-only hash-chained experiment registry, the frozen protocol in `PROSPECTIVE_PROTOCOL.md` (150/300/450-game looks, Lan–DeMets spending, ≤ 3 primary hypotheses, `LOOK_*` written once and never before 150 eligible post-freeze games — enforced in code, tested and checked in CI by the `Verify blinding` step).

## Decision requested

Approve Option A (I will implement the sealed ledger, with tests using a throwaway key, as a separate PR; you generate the key pair and send me **only the public key**), or choose B. Until then the post-freeze games are not being recorded: the archive still holds the same inputs, and the T-60 forecasts are exactly reproducible from the archived slates, so nothing is lost by waiting; the ledger can be back-filled in order, each row marked with the date it was actually sealed.
