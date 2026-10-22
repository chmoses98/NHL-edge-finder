# Sealed prospective research ledger — design, threat model and security review

> RESEARCH ONLY · shadow. Implements Option A of `LEDGER_ISOLATION_REVIEW.md`. **Nothing here is activated**: `publish=true` is refused until the owner has generated keys, reviewed this document and set a repository variable (below); no schedule is enabled; the NHL betting engine remains PASS-only and no stake, cap, model or recommendation is touched.

## 1. What is protected, and what is not

The prospective tier (games starting after 2026-10-21T17:13:05Z) exists to evaluate a frozen protocol (looks at 150 / 300 / 450 independent games, Lan–DeMets spending, ≤ 3 primary hypotheses) **without being tuned against**. A ledger row holds the frozen pregame forecasts, the final score and everything *derived* from the comparison (win-probability surprise, randomised PIT, Brier/RPS inputs, attribution class).

* **Encryption hides the evaluation record from everyone who does not hold the owner's private key, including the public, collaborators, every workflow and every development tool.** It also makes the record *committed* (commit–reveal): the ciphertext and its hash are public and timestamped before anyone reads the result.
* **It does not hide public facts.** Final scores and the archived pregame slates are public; a determined person can recompute any row from the public archive. What the sealing removes is the *convenient, accidental and unrecorded* path to the performance numbers (no file, log, artifact, PR, branch or tool output contains them), and it gives the preregistered process an audit trail. The protocol, not secrecy of scores, is what prevents tuning; the sealing prevents the shortcut and proves what was frozen when.
* **Encryption alone does not prevent malicious replacement or forgery** (§5). It provides confidentiality. Integrity comes from the hash chain, the checkpoints and the owner's reproduction check, each with the limits stated in §6.

## 2. Architecture

```
GitHub Actions (public repo, NOT trusted)                      Owner's MacBook (trusted, offline key)
─────────────────────────────────────────                      ───────────────────────────────────────
archive (public) ─► build_rows (in memory)                     identity.txt  (age PRIVATE key, never uploaded)
                    │                                          witness_private.pem (Ed25519, passphrase-protected)
                    ▼
   pad to 4 KiB ─► age encrypt to PUBLIC recipients ──► sealed/NNNNNN.age        ┐ branch
                    │                                                             │ model-research-sealed-ledger
                    └► manifest.jsonl  (hash chain; no outcomes) ───────────────┤ (+ tags sealed-ledger-head-N,
                       checkpoints/runner_*.json (optional signed head)           ┘   job summary with head hash)
                                                                    git clone ledger ─► owner verify ─► owner witness (signed head, local log)
                                                                    at ≥150 games:  owner look (decrypts locally, runs the frozen scorecard)
```

* **Cryptography (no custom primitives).** `age` v1 via `pyrage` (Rust `rage`): X25519 key agreement, HKDF, ChaCha20-Poly1305 streaming AEAD — authenticated hybrid encryption. Anyone can verify the format and decrypt independently of this repository with the reference tool: `age -d -i identity.txt sealed/000003.age`. Checkpoints use Ed25519 from `cryptography` (OpenSSL). Hashes are SHA-256.
* **Multiple recipients.** `recipients.txt` should list a primary and a backup public key; either one decrypts. The recipients file hash is committed in the genesis entry; any later change is refused.
* **Fixed-size plaintext.** Every record is serialised and space-padded to exactly 4,096 bytes before encryption (real records are ≈ 0.9 KB; a larger record **fails closed** rather than leak its size). `age` adds a small random-length header, so ciphertext lengths vary by ≈ 100 bytes independently of content; `verify` enforces a size band.
* **Opaque names.** Files are `sealed/<manifest seq>.age`. No game id, date, count or result is in a filename.
* **Manifest** (`manifest.jsonl`, canonical JSON, one entry per line, each carrying `prev_hash` and `entry_hash = SHA-256(domain ‖ canonical(entry))`):
  * `GENESIS`: random `ledger_id`, SHA-256 of `recipients.txt`, recipient count, pad size, **SHA-256 of the frozen protocol rules** (freeze instant, looks 150/300/450, spending 0.0007/0.0164/0.05, ≤ 3 primary hypotheses, unit = game), run id, code SHA.
  * `RECORD`: `game_id`, `game_date_et` (both public schedule facts), `version`, `supersedes`, `reason`, `ct_sha256`, `ct_bytes`, **two pregame data-quality fields only** (`slate_age_min`, `sb_present`), seal time, run id, code SHA.
  * `DAY`: for a date whose scheduled games are all final, the public list of scheduled game ids, those sealed, and those lacking a pregame forecast — a public commitment so a later omission is visible.
  * Nothing outcome-derived (no result, error, ROI, PIT, class, Brier component) appears in any entry, filename, log line, summary, artifact, commit message or PR.
* **Blinded scorecard** is computed by the runner from the manifest alone and has the same keys and meaning as the document `daily.scorecard` prints before the first look (a test asserts key-for-key equality; `mean_slate_age_min` is computed from values rounded to 3 decimals), restricted to games a DAY entry accounts for. At ≥ 150 games the runner reports `LOOK_k_DUE_OWNER_LOCAL`; it **cannot** compute a look (no key). The frozen scoring code in `daily.scorecard` is unchanged and runs only inside `owner look`.

## 3. Operations

* **Ingestion is idempotent and resumable.** `seal_rows` skips any `game_id` already sealed. Order of writes: ciphertext (atomic rename, fsync) → manifest line (fsync). A crash between the two leaves an *orphan* ciphertext, flagged as a warning and overwritten at the same sequence number by the next run. A torn manifest tail blocks appends until the explicit `repair_torn_tail` (drops only an incomplete last line; the workflow never passes it, so a torn tail fails the run and opens an issue). A ciphertext the manifest does not reference is a verification **problem** on any published store (it cannot be told from plaintext behind a fake header); only `SealedStore` resuming a crashed run on the runner's own working copy tolerates one, and a failed job never commits. Each run first verifies the whole existing store and refuses to append to one that fails. The publish job re-verifies and requires the new manifest to *extend* the current remote head.
* **Corrections are versioned, never overwrites.** A changed historical record is only ever added when explicitly requested (`correct_game_ids` as `GAME_ID@CURRENT_VERSION` + a reason code from a closed list) as version *n+1* superseding the previous entry. Naming the version being superseded makes a correction idempotent: a workflow re-run repeating the request is refused as stale instead of stacking versions; both ciphertexts and both entries stay. Corrections are public metadata (visible in the manifest) and are listed in the look's provenance file. (Because the runner cannot decrypt, it cannot *detect* that a source score changed; `owner reproduce` does that locally.)
* **Which games count.** Only games that a `DAY` entry accounts for (a date whose scheduled games are all final and all sealed or listed as lacking a pregame forecast) count toward the 150-game threshold, enter a look, or appear in the runner's scorecard. A record that no `DAY` commits to (an extra or forged id, an incomplete day) is carried in the ledger but never evaluated, and a game sealed *after* its day was closed is a verification error. A day is not closed when none of its games has a pregame forecast (the signature of an incomplete archive fetch; a `DAY` entry cannot be undone).
* **Bounds.** ≤ 60 games per run; ≤ 30-minute job timeout; one run at a time (`concurrency`; GitHub keeps at most one *pending* run, so dispatch dates one at a time and wait for each to finish, and the scheduled form runs once a day); artifacts ≤ 14 days (staging 1 day); the archive is fetched sparsely; one issue per failed date.
* **Audit trail.** Every manifest entry carries the run id and code SHA; each publish is a normal (never forced) commit; each head is also written to an annotated tag `sealed-ledger-head-<seq>` and to the job summary; failed runs open an issue (run URL only).
* **Minimal permissions.** Workflow default `contents: read`. `settle` is read-only and holds no secret. Only `publish` has `contents: write` (ledger branch + head tag); it runs only from `refs/heads/main`, inside the `sealed-ledger` environment (add required reviewers there for a second human gate), checks out with `persist-credentials: false`, installs and verifies **before** any token exists, and receives the write token in exactly one step (the push). Only `alert` has `issues: write`. The only secret that can ever be referenced is an optional Ed25519 *signing* key (`LEDGER_ATTEST_KEY_PEM`, publish job only; unrelated to the ledger keys). Tests pin all of this.

## 4. Who can do what

| actor | read ciphertext | decrypt | append valid-looking ciphertext | rewrite history undetected |
|---|---|---|---|---|
| public reader | yes | **no** | no (cannot push) | no |
| collaborator / any token with repo read | yes | **no** | no | no |
| development workflows, challenger / tuning code, CI on PRs, this assistant | yes (public) | **no — no key exists on GitHub or in any tool**; only `owner.py` can decrypt, imports of it are forbidden by test, it refuses to run in CI | no (no write permission outside `publish`) | no |
| someone who can push to the ledger branch (write access) | yes | no | **yes** (the public key is public) | only if they also control every anchor in §6 |
| whoever controls the workflow file on `main` / a malicious Action or dependency | sees plaintext rows in runner memory | n/a (has the plaintext at seal time) | yes | see §6 |
| repository admin / GitHub account compromise | yes | no | yes | can rewrite branch, tags, variables; **cannot** alter the owner's local witness log |
| owner (private key + witness key) | yes | yes | — | detects §6 cases |

## 5. Threat model

Assumed: the repository is public; Actions logs and artifacts are public; GitHub, the runner image, `age`/`pyrage`/`cryptography` and the owner's MacBook are not malicious; the owner's private key is never exposed. **Not assumed**: that collaborators, workflows, dependencies, branches or tags are trustworthy.

| # | threat | protected? | how / limit |
|---|---|---|---|
| T1 | public or collaborator reads the evaluation record | **yes** | age encryption; ciphertext public by design |
| T2 | development / tuning job or tool reads or uses prospective results | **yes (technical + process)** | no key on GitHub; `owner.py` is the only decrypting module and nothing may import it; models/challengers never import `sealed_ledger`; the runner refuses a look; `owner look` refuses before 150 games. Public facts can still be recomputed by a determined person (§1). |
| T3 | accidental exposure via CI logs, artifacts, PRs, default-branch files, filenames, sizes, counts | **yes** | runner prints/uploads only an outcome-free summary and the blinded scorecard; a blinding step and a **synthetic-outcome self-test with unmistakable sentinels** fail the run on any leak; fixed-size padding and opaque names; tests scan every written file and all console output |
| T4 | edit, reorder, delete or insert in the middle; swap, delete or modify a ciphertext; plant a plaintext file | **yes (anyone can check)** | hash chain, per-ciphertext SHA-256, size band, allowed-file list, version discipline, DAY accounting |
| T5 | truncate the tail / roll back to an earlier valid state / delete and recreate the branch / replace the whole ledger with a consistent new chain | **only against an anchor held elsewhere** | a valid chain proves nothing about what is *missing from the end* or *replaced wholesale*. Detected by: the owner's signed witness log (strongest, off-GitHub), the `--previous` extension check, annotated tags, job-summary heads, optional runner attestations. Not detected before the first witness, and not if every anchor is also rewritten (anchors on GitHub share GitHub's trust). |
| T6 | forged or fake records appended by someone with write access (anyone can encrypt to a public key): flipped corrections, extra ids, records for real dates | **detectable, not preventable** | forged extras never count (only DAY-accounted games enter a look) and a record on an already-closed day fails verification; `owner reproduce` re-derives every date from a trusted archive and compares with the decrypted LATEST version of each game, flagging forged content, extra ids and omissions (field names only); DAY entries expose omissions; the optional runner signature narrows who could have written. A forged *correction with plausible content* is indistinguishable from a real one except by that comparison. **Encryption alone does not stop this.** |
| T7 | malicious or compromised workflow / dependency | **no** | it sees the plaintext at seal time and could leak or forge it. Mitigations: minimal permissions, activation gate bound to the recipients hash, no third-party secrets, code review of the workflow file, pin actions by SHA (recommended hardening), `reproduce` at the look |
| T8 | cherry-picking via corrections | detectable | every correction is public metadata with a reason code; the look's provenance lists them; protocol: no correction without an owner-visible reason |
| T9 | key loss | recoverable if a backup recipient exists | otherwise the records are unrecoverable; forecasts remain re-derivable from the archive but lose their commit–reveal value (owner decision, registry NOTE) |
| T10 | key compromise | **not** protected | treat the tier as unblinded from the exposure date; rotate by starting a new ledger; X25519 is not post-quantum (irrelevant for a one-season secret that is revealed at the look) |
| T11 | withholding runs | detectable | missing DAY entries; issue on failure |
| T12 | timing side channel (when a record is sealed) | accepted | reveals only that a game finished, which is public |

## 6. What the checkpoint mechanism can and cannot detect

A checkpoint is `(ledger_id, seq, head_hash, n_entries, signer, time)` plus an Ed25519 signature. Verification asks whether the current manifest still contains that head at that position.

| attack | chain alone | + owner witness log | + runner attestation | + tags / step summary |
|---|---|---|---|---|
| edit/reorder/delete in the middle | **yes** | yes | yes | yes |
| tail truncation | no | **yes** (once witnessed) | yes if signed after the truncated entries | partly (admin can delete tags) |
| rollback to an earlier valid state | no | **yes** | yes | partly |
| delete branch, recreate with fresh genesis (different `ledger_id`) | no | **yes** ("REPLACED") | yes | partly |
| rewrite a witnessed entry, keep length | yes if the chain was not rebuilt; no if it was | **yes** (entry hash differs) | yes | partly |
| append forged records after the last witness | no | no | no (if the signing key is compromised) | no |
| tampering before the first witness | no | no | no | no |
| deletion of the owner's own witness log | n/a | **partly**: removing a *middle* line or tampering is detected (hash chain + signatures); removing the *last* line(s) or the whole file is **not** detected by the log itself. `owner witness` prints `witness_log_head`; write it down somewhere other than that folder and pass it as `--expect-witness-head` to `verify` | | |

Practical rule: the owner witnesses **at least weekly and always immediately before a look**, and keeps two copies of the witness directory.

## 7. Security review (this PR)

Verified by tests (`tests/test_sealed_ledger.py`, `tests/test_research_workflows.py`, `python -m nhl_edge.sealed_ledger.selftest`):

* encrypt/decrypt round trip with either recipient; stranger key fails; random ciphertexts for equal plaintexts; bit-flip and truncation fail AEAD authentication;
* fixed plaintext slot (small and 3× larger records land in the same ciphertext band; oversize refused); no sentinel/outcome field in any file or console output;
* chain edits/reorders/deletes/inserts, ciphertext modified/deleted/swapped/plaintext-in-place/stray files all rejected; contiguous sequence numbers; records sealed in the given order;
* duplicate ingestion is a byte-for-byte no-op; late games are added; duplicate ids in a batch refused; corrections are versioned, reason-coded, never overwrite, and a forged version number is rejected;
* DAY accounting; missing ciphertext detected;
* crash between ciphertext and manifest → orphan warning and clean resume; torn manifest tail blocks until repaired;
* checkpoint signatures, wrong key, altered checkpoint, witness-log chain; truncation, rollback and whole-ledger replacement detected only with an anchor (and shown to pass the chain check alone);
* recipients: secret key refused, empty refused, malformed refused, changed-after-genesis refused; the frozen-protocol hash is pinned literally and a store with other rules is rejected;
* owner tooling: keys written 0600 and never overwritten; `check-key`; `look` refuses before 150 games **without decrypting** (decrypt is monkeypatched to fail), requires a witness, is written once, refuses rolled-back and tampered ledgers; refuses to run under CI; `reproduce` flags forged and omitted rows without printing values;
* **real-path no-plaintext test**: the prospective runner (`ingest --seal`, `scorecard`, `verify`) run end-to-end on sentinel rows with plaintext writers (`append_rows`, `scorecard`) patched to raise, then every file and all stdout/stderr scanned; the plaintext `daily.ingest` refuses prospective dates;
* static isolation: AST checks that only `owner.py`/`selftest.py` call `decrypt`, nothing imports them, model/challenger modules never import `sealed_ledger`; a repo-wide scan finds no `AGE-SECRET-KEY-1…` or PEM private key; the workflow uses no secret except the optional signing key, contains no decryption path, and takes inputs only through env vars.

Findings during implementation (fixed): (a) `age` ciphertext lengths are not constant (random grease header) — replaced an exact-size check by a size band and documented that padding is applied to the plaintext; (b) the first draft sealed 32 KiB slots for ≈ 0.9 KB records — reduced to 4 KiB; (c) the Phase-3 plaintext design's artifact was misleadingly named "private" — gone.

An independent adversarial read (a separate agent given only the code and this document) then found, and this PR fixes: `owner reproduce` only checked version 1 of days with a DAY entry, so a forged v2 or extra ids were missed and counted toward the threshold (now: latest versions, all dates, extras and omissions, DAY-gated counting); "look once" held only per `--out` directory and a first look at ≥ 300 games skipped the 150-game look (now: marker in the witness directory, smallest untaken level on exactly the first *k* games); the self-test step ran through a pipe and could not fail the job; the file allow-list accepted any `.git*` name, orphan files, extra manifest fields and non-canonical lines (now exact `.git` only, orphans are problems, per-kind key whitelist, canonical lines, checkpoint schema); the witness-log text overclaimed (last-line removal); an empty witness passphrase silently stored the key unencrypted; repeated corrections stacked versions; `publish=true` could be dispatched from any ref and the signing secret reached the settle job; the write token was on disk while dependencies installed; `--previous` with a typo skipped the append-only check; the head tag was skipped on re-runs; duplicate recipients defeated the two-key warning; a torn genesis wedged the store; owner `witness`/`look` did not compare the genesis recipients hash.

Residual risks (accepted, to be revisited by the owner): T7 (workflow/dependency compromise), T6 (forgery by a writer is detectable only at the look), T5 before the first witness, third-party Actions pinned by tag rather than SHA, no lock file for Python dependencies, key custody.

## 8. Protocol preservation

The preregistered rules are unchanged: first look at 150 independent games, then 300 and 450, Lan–DeMets one-sided spending 0.0007 / 0.0164 / 0.0500, ≤ 3 primary hypotheses, unit = game. `PROTOCOL_RULES` and its SHA-256 (`527508ce…7376d`) are pinned by a test and committed in every ledger's genesis; `daily.scorecard` and `daily.LOOKS` are untouched. The sealed ledger changes *where* rows are stored, not how they are scored.
