# Sealed ledger — unattended operation (architecture, permissions, exceptions, one-time setup)

> RESEARCH ONLY · shadow · **nothing here is activated**: the schedule is commented out, `research/sealed_ledger/recipients.txt` holds no key, no ledger repository, deploy key or variable exists. The NHL betting engine stays PASS-only; no stake, cap, model weight or recommendation can be changed by anything described here. This document supersedes the publication path (environment `sealed-ledger`, branch `model-research-sealed-ledger`) of `SEALED_LEDGER_DESIGN.md`; the cryptography, manifest, checkpoints, audit and threat model there still apply.

## 1. Goal

After a one-time setup the ledger collects every day **with no approval prompt and no routine action by the owner**. The owner is contacted only for a genuine exception or a research decision: (1) initialisation, (2) a key change, (3) a protocol change, (4) decryption/evaluation (the 150/300/450-game looks), (5) any activation of real betting. Those five stay behind explicit gates.

## 2. Architecture

```
 CODE REPOSITORY (public)                                     LEDGER REPOSITORY (public, ciphertext only)          OWNER'S MAC
 ────────────────────────                                     ───────────────────────────────────────────          ───────────
 sealed_ledger_daily.yml  (unattended, cron, NO inputs)       manifest.jsonl  (hash chain, no outcomes)            age PRIVATE keys   (never leave the Mac)
   reconcile job  contents: read ─ reads archive, ledger ──►    sealed/NNNNNN.age (ciphertext)                       witness key + log  (never leave the Mac)
   publish job    contents: read ─ env sealed-ledger-publish    checkpoints/ (optional)                              weekly launchd check (optional, local)
     └─ DEPLOY KEY (write to the LEDGER repo ONLY) ──────────►  tags sealed-ledger-head-N                            decryption, the looks (owner.py)
 sealed_ledger_admin.yml  (init / hand correction / hand       Actions DISABLED · no workflow · no secret · rulesets: no force-push, no delete
   exclusion; publish job waits for the OWNER'S APPROVAL)
```

* **Encryption is unchanged**: `age` (X25519 + ChaCha20-Poly1305) to the owner's PUBLIC keys; the private keys exist only on the owner's Mac. Nothing in either workflow can decrypt.
* **The ledger lives in its own repository** (`SEALED_LEDGER_REPO`). It holds no code, no workflow, no secret and has GitHub Actions disabled, so a credential that can write it can do *nothing else* on GitHub.
* **The routine workflow has no write permission on the code repository at all** (`contents: read` in every job; the only other grant is `issues: write` in the alert job). It cannot push a branch, edit a file, change a model weight, a recommendation, a stake or a cap. A test pins this.

## 3. Credentials and who can use them

| credential | where it lives | what it can do | who/what can use it |
|---|---|---|---|
| age **private** keys (primary, backup) | owner's Mac, offline backups | decrypt the ledger | owner only (`owner.py`, refuses CI) |
| witness signing key + log | owner's Mac (passphrase in Keychain for the optional weekly job) | sign checkpoints | owner only |
| **ledger deploy key** (SSH, write) | GitHub *environment* secrets `SEALED_LEDGER_DEPLOY_KEY` in `sealed-ledger-publish` (routine) and `sealed-ledger-admin` (approval-gated) | write the **ledger repository only** (fast-forward pushes enforced by the publisher and by the ledger repo's ruleset) | the publish job of a workflow run from `main` (environment branch policy) |
| `GITHUB_TOKEN` of the code repo | automatic | **read only** in every sealed job | — |
| everything else (PAT, App, other secrets) | does not exist | — | — |

## 4. Separation of duties

| operation | who/what triggers | gate | enforced by |
|---|---|---|---|
| routine daily collection, missed-day catch-up, retries | schedule / parameter-free dispatch | none (unattended) | environment `sealed-ledger-publish`: deployment branches = `main` only, **no reviewers**; `contents: read`; deploy key scope |
| source-revision correction, postponed/boundary exclusion | the same routine pass, mechanically, by rules hashed into every ledger | none, **prespecified** (§5) | `PROTOCOL_RULES` hash in the genesis entry; tests |
| **initialisation** (`init`) | `sealed_ledger_admin.yml` | **owner approval** (environment `sealed-ledger-admin`, required reviewer) | GitHub; script refuses if a genesis hash is already registered |
| hand correction / hand exclusion (exceptions) | `sealed_ledger_admin.yml` | **owner approval** | same |
| **key change** (`recipients.txt`) | code change on `main` | owner merges it; invalidates `SEALED_LEDGER_ACTIVATION_SHA` → routine publishing stops until the owner re-registers (approval) | hash comparison in the publish script |
| **protocol change** (looks, spending, operational rules, frozen C1 parameters) | code change on `main` | owner merges it; changes the protocol hash → every `verify` fails (`genesis protocol_rules_sha256 differs`), and the reconcile blocks on a changed C1 file | `core.verify_store`, `reconcile` (C1 hash), tests pin the literal |
| **decryption / looks** | owner on their Mac | the private key | `owner.py` (refuses CI, refuses before 150 closed-day games, once per look) |
| **real betting** | not part of this system | not enabled anywhere; routine runs cannot touch production | no write permission, no production module is ever run (test) |

## 5. What the unattended pass does (`runner reconcile`, one idempotent pass)

1. **Missed days.** Every date from 2026-10-21 through yesterday (ET) that has scheduled games and no `DAY` entry is processed in ascending order (≤ 14 per run; the next run continues). A skipped run, a retry or a re-run converge to the same ledger; re-processing a sealed game is a byte-for-byte no-op.
2. **Source revisions.** A sealed game whose final score was revised in the archive becomes the next *versioned correction* (`SOURCE_SCORE_REVISED`), re-derived from the newer archive snapshot; earlier versions and ciphertexts stay; ≤ 3 versions per game, ≤ 10 corrections per run (more is an exception).
3. **Postponed / cancelled games.** A scheduled game that is still listed on its date and not final **14 days** after its start is excluded from its day (`POSTPONED_OR_CANCELLED`); a game whose start moved across the freeze instant is excluded (`START_TIME_BOUNDARY`). Both rules read only the schedule — never a result — so they cannot be used to shape the sample; they are fixed in `PROTOCOL_RULES` before any prospective evaluation and committed in the ledger's genesis. A game that is merely late makes its day **WAIT**: normal, no alert. A game that is later rescheduled to a new date is picked up there (if it was not yet excluded) or stays excluded (if it was).
4. **Model integrity.** The V1 distribution is regenerated bit-exactly from the archived seeds; any difference (`MODEL_DRIFT`) or a change of the frozen C1 parameters (`C1_PARAMS_CHANGED`) blocks the run instead of sealing forecasts from a different model. Every entry also records the run id and code SHA.
5. **Integrity audit** of everything now closed (schedule drift, extra ids, unsealed finals, orphan results, revisions not covered) → any problem is an exception.
6. The new store must extend the previous one (append-only) and pass `verify_store`; only then is it published (fast-forward push; a rejected push is never forced — the next run starts from the remote head).

**Statuses and what the owner sees**

| status | meaning | alert? |
|---|---|---|
| `OK` / `IDLE` | ledger up to date / nothing to do | no |
| `PARTIAL` | more than 14 days were missing; the next run continues | no |
| `WAITING` | a game has not finished yet (normal) | no |
| `BLOCKED: <codes>` | an exception, safely sealed days kept, nothing sealed past the problem | **one deduplicated issue** (`sealed ledger: BLOCKED: DRIFT` …) with the run URL and codes only |
| workflow failure (network, push rejected, install, audit…) | a run failed; the next run retries from scratch | one deduplicated issue |

Block codes: `MODEL_DRIFT`, `C1_PARAMS_CHANGED`, `DRIFT`, `EXTRA`, `UNSEALED`, `OPEN_DAY`, `ORPHAN_RESULT`, `NO_PREGAME_FORECAST`, `CORRECTION_LIMIT`, `TOO_MANY_CORRECTIONS`, `CANNOT_REDERIVE`, `CORRECTION_REFUSED`, `SEAL_REFUSED`, `EARLIER_DAY_NOT_CLEAN`. Each means the data or the code is not what the frozen protocol assumes; the decision is the owner's (usually: investigate, then an approved `sealed_ledger_admin` action or a reviewed code change).

## 6. What GitHub's native permissions can and cannot enforce (requirement 5)

| mechanism | can restrict | cannot restrict | verdict |
|---|---|---|---|
| `GITHUB_TOKEN` `permissions:` | the *kind* of access (contents, issues, …) | **which branch/path**: `contents: write` is write to every branch of the repository; the workflow file itself declares the permission, so anyone who can run a modified workflow gets it | rejected as the publisher credential; used only as **read-only** |
| branch/tag **rulesets** (can list `github-actions`, apps, deploy keys as bypass actors) | which refs may be force-pushed/deleted/updated, by role | *which workflow* acts (all runs share one bot identity); cannot allow a credential on "just this branch" without denying everything else by pattern, and a new branch carrying a `push`-triggered workflow with `contents: write` is an escalation path | used on the **ledger** repo to block force-push/deletion; not relied on to confine a credential |
| **fine-grained PAT** | one repository, contents write | a branch; expires (≤ 1 year → recurring owner chore); tied to the owner's account | rejected (scope not narrower than a deploy key, plus expiry) |
| **deploy key** (SSH) | write access to **exactly one repository** | a branch inside it | **chosen**, on a repository that has nothing else in it |
| GitHub **App** installation token | selected repositories | a branch; needs hosting/creation | same scope as a deploy key with more moving parts |
| **environments** | which refs may use the environment, its secrets and variables (deployment branch policy); optional required reviewers; secrets per environment | what a job does once released; the secret's blast radius | **chosen** for *who may use the key* (main only; reviewers only for admin) |

So the destination restriction **is** natively enforceable, but not with a branch-scoped credential: it is enforced by **repository scoping** — the only thing the automated publisher can write is a repository that contains nothing but ciphertext and a manifest, with Actions disabled. The residual limitation: inside that repository the key can write any ref, and no GitHub feature can narrow it further; the defence there is rulesets (no force-push, no deletion), the publisher's own fast-forward/extension/genesis checks, and the owner's offline anchors.

## 7. Residual risks (honest list)

* **The deploy key is a standing credential in GitHub secrets.** A compromised publish job (a malicious release of a pinned action you update to, a malicious PyPI file that passes a lock you regenerate, a merged change to `scripts/sealed_ledger_publish.sh` or the workflow) could read it and push forged or junk records, or (if rulesets are not set) rewrite the ledger repository. It could not read the private key, touch the code repository, models, stakes or caps. Detection: hash chain, `owner reproduce`, witness log, genesis registration; recovery: rotate the deploy key (owner action), restore from your local copies.
* **Routine publishing has no approval step by design.** What stands in for it: the environment's branch policy (only code merged to `main` can use the key), the activation hash (key/protocol changes stop it), `contents: read`, the minimal hash-locked install, the pinned actions, and the owner's review of every change to those files.
* **Anyone who can merge to `main`** (the owner; a collaborator if you add one; an admin) controls what the routine job does. Recommended: a ruleset on `main` requiring pull requests, CODEOWNERS for `.github/workflows/**`, `requirements/**`, `scripts/sealed_ledger_publish.sh`, `src/nhl_edge/sealed_ledger/**` and `research/sealed_ledger/recipients.txt`; no other collaborators; two-factor authentication.
* **Scheduled workflows stop** if GitHub disables them after 60 days without repository activity, or skip a cron tick. The next run catches up any missed day. If it never runs, nothing alerts from GitHub; the owner's optional weekly check reports `the ledger has not closed a day for N days`.
* **Forged-but-validly-encrypted records** by someone with the deploy key are caught only by DAY accounting (never counted unless a DAY lists them) and `owner reproduce` at the look.
* **Automatic exclusion and correction rules are mechanical but are rules**: a game played > 14 days late is lost; a revised score replaces the earlier one for evaluation (both stay visible). Both are fixed before any evaluation and visible in the manifest.
* Everything in `SEALED_LEDGER_DESIGN.md` §5–§6 (admin risk, tag limits, first-checkpoint limits) still holds.

## 8. One-time setup (the owner) and what happens afterwards

**You do once (about 45 minutes; the checklist has the exact clicks and commands — `SEALED_LEDGER_OWNER_CHECKLIST.md`)**

1. On your Mac: generate the age primary + backup identities and the witness key; back them up offline; test a restore. *(private keys never leave the Mac)*
2. Create the **ledger repository** (public, empty — no README/licence/gitignore), **disable Actions** in it, add rulesets (no force-push, no deletion on `main` and on tags `sealed-ledger-head-*`).
3. Generate a **deploy key** (`ssh-keygen -t ed25519`), add its **public** half to the ledger repository as a deploy key **with write access**; keep the private half only to paste into the two environment secrets below, then delete the local copy.
4. In the code repository: create environments **`sealed-ledger-publish`** (deployment branches = `main` only; **no required reviewers**) and **`sealed-ledger-admin`** (deployment branches = `main`; **you as required reviewer**); add the secret `SEALED_LEDGER_DEPLOY_KEY` to both; add the repository variable `SEALED_LEDGER_REPO`; add the environment variables `SEALED_LEDGER_REPO` (same value) and `SEALED_LEDGER_ACTIVATION_SHA` (= SHA-256 of the committed `recipients.txt`) to both environments.
5. Send the two public `age1…` keys (or commit them yourself); merge.
6. Approve the one-time **init** (`sealed_ledger_admin`, action `init`), run `owner first-checkpoint`, compare the genesis hash in three places, write it down offline, and register it as the environment variable `SEALED_LEDGER_GENESIS_HASH` in both environments.
7. Run the schedule's `dry_run=true` once to see it end to end; then approve enabling the cron (a one-line change reviewed and merged by you).
8. Optional, recommended: install the macOS launchd job that runs `owner weekly-check` (verify + witness + stale-ledger notification) so even the weekly witnessing is automatic.

**Automatically afterwards**

* every morning (08:17 ET): catch up all missing days, seal new games (encrypted), close complete days, apply source revisions as versioned corrections, exclude games that never finish, verify, publish to the ledger repository, upload an outcome-free report;
* retries and missed-day recovery on the next run; one deduplicated issue only for a genuine exception;
* (optional) your Mac verifies and witnesses weekly and notifies you only if something is wrong or the ledger stopped growing.

**Still yours (the only things that should ever need you)**: the first-checkpoint at setup; an exception issue; a key or protocol change (a PR you review); the looks at 150/300/450 closed-day games (decrypt locally, `owner look`); any decision about betting (nothing is enabled).
