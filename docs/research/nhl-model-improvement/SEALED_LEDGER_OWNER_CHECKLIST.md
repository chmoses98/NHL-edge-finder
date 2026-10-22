# Sealed ledger — owner setup checklist (macOS)

> **You never paste a private key anywhere — not into chat, an issue, a PR, a repository variable or secret, or a synced note. Nobody will ask you to.** The only values that leave your Mac are public keys (`age1…`), hashes, and the output of `owner` commands that print neither. Longer explanations: `SEALED_LEDGER_KEY_SETUP.md`; threat model: `SEALED_LEDGER_DESIGN.md`. Replace `~/sift-ledger` with another private folder if you like.
>
> Items marked **[YOU]** can only be done by you. Items marked **[CLAUDE]** can be done by the assistant on request, with no secret involved.

## A. Prepare the Mac  **[YOU]**

- [ ] FileVault is on (System Settings → Privacy & Security → FileVault).
- [ ] `brew install age python@3.12 git` (the `age` tool is the independent, reference way to open the ledger without any of our code).
- [ ] ```bash
      mkdir -m 700 ~/sift-ledger && cd ~/sift-ledger
      git clone https://github.com/chmoses98/NHL-edge-finder.git repo      # check out a commit you have reviewed
      python3.12 -m venv venv && ./venv/bin/pip install -r repo/requirements/research-runtime.in
      alias owner='PYTHONPATH=$HOME/sift-ledger/repo/src $HOME/sift-ledger/venv/bin/python -m nhl_edge.sealed_ledger.owner'
      ```
      (The hash-locked files in `requirements/*.lock` are for the Linux runner only — they pin Linux wheels and will not install on macOS — so your local venv uses the same *input* list, unpinned. `owner look` runs the frozen scoring code, which needs the numerical stack. Re-run the install and re-check `owner check-key` after any Python or package upgrade.)

## B. Keys  **[YOU]**

- [ ] `owner keygen --identity ~/sift-ledger/primary-identity.txt` → prints the primary **public** key (`age1…`). Copy it.
- [ ] `owner keygen --identity ~/sift-ledger/backup-identity.txt` → prints the backup **public** key. Copy it. (Two different keys, different custody.)
- [ ] `owner witness-keygen --dir ~/sift-ledger/witness` (choose a passphrase of ≥ 8 characters; store it in your password manager).
- [ ] `chmod 600 ~/sift-ledger/*identity.txt`

## C. Independent backups and recovery drill  **[YOU]** — before anything is published

- [ ] Encrypt a copy of each identity with its own long passphrase:
      `cd ~/sift-ledger && age -p -o primary-identity.txt.age primary-identity.txt && age -p -o backup-identity.txt.age backup-identity.txt`
- [ ] Put `primary-identity.txt.age` on an offline USB stick (A) and `backup-identity.txt.age` on a *different* physical medium / location (B). Optionally also print the identity file and keep the paper in a safe. Copy `~/sift-ledger/witness/` to the same media as A. Write down where each copy is.
- [ ] **Restore test, now:** copy the `.age` backups to a scratch folder on the Mac, run `age -d -o /tmp/p.txt primary-identity.txt.age` and the same for the backup; `owner check-key --identity /tmp/p.txt --recipients <repo>/research/sealed_ledger/recipients.txt` (after step D) ; then `rm /tmp/p.txt /tmp/b.txt`. A backup you never restored is not a backup.
- [ ] Never keep an *unencrypted* copy of either identity on a synced folder (iCloud Drive, Dropbox), in email, or in the repository checkout. (`*identity*.txt` is git-ignored as a guard, not a safeguard.)

## D. Give the repository your PUBLIC keys  **[YOU, or CLAUDE with your two `age1…` strings]**

- [ ] Add the two `age1…` lines to `research/sealed_ledger/recipients.txt` (keep the comment lines) via a PR. Merge it.
- [ ] `owner check-key --identity ~/sift-ledger/primary-identity.txt --recipients ~/sift-ledger/repo/research/sealed_ledger/recipients.txt` and the same for the backup: both must print `"identity_matches_recipient": true, "canary_roundtrip": true` and no warning.

## E. GitHub settings  **[YOU]** (Settings in the web UI)

- [ ] **Environments → New environment → `sealed-ledger`**: *Deployment branches and tags* → **Selected branches → `main` only**; **Required reviewers** → yourself. This environment — not the workflow file — is the security boundary for publishing.
- [ ] In that environment add **Environment variable** `SEALED_LEDGER_ACTIVATION_SHA` = output of `shasum -a 256 ~/sift-ledger/repo/research/sealed_ledger/recipients.txt` (run `git pull` in the checkout first so it is the merged file). *Environment* variable, not repository variable.
- [ ] **Rules → Rulesets**: (1) branch `model-research-sealed-ledger`: *Restrict deletions* and *Block force pushes*; (2) tags `sealed-ledger-head-*`: *Restrict deletions* and *Restrict updates*. (These do not stop an admin who edits the ruleset; they stop accidents and ordinary writers.)
- [ ] Keep the repository's default **Workflow permissions** at *Read repository contents*.

## F. Create the ledger and take the first checkpoint  **[YOU approve; CLAUDE can dispatch]**

The ledger is created by a one-time `init` that seals **no game**. You verify it independently *before* any real record exists.

- [ ] Run workflow `model_research_daily` on `main` with `publish=true`, `init_ledger=true` (any date). Approve the `sealed-ledger` deployment when GitHub asks. The run creates branch `model-research-sealed-ledger` with `manifest.jsonl` (one `GENESIS` entry) and `sealed/000000.age` (a **synthetic canary** encrypted to both your keys) and tag `sealed-ledger-head-0`.
- [ ] Clone it (this is the copy you verify):
      `git clone --branch model-research-sealed-ledger --single-branch https://github.com/chmoses98/NHL-edge-finder.git ~/sift-ledger/ledger`
- [ ] `owner first-checkpoint --store ~/sift-ledger/ledger --identity ~/sift-ledger/primary-identity.txt --identity ~/sift-ledger/backup-identity.txt --dir ~/sift-ledger/witness --recipients ~/sift-ledger/repo/research/sealed_ledger/recipients.txt`
      It verifies the structure and the recipients hash, proves **each identity on its own opens the real published canary**, signs a witness checkpoint of the initial head, and prints `genesis_hash`, `recipients_sha256` and `witness_log_head`. It refuses anything but a fresh genesis-only ledger.
- [ ] **Compare three sources of the genesis hash — they must be identical:** (1) the `owner` output; (2) the *Actions run summary* ("Sealed ledger head … entry_hash"); (3) the message of tag `sealed-ledger-head-0` on GitHub. Then recompute it with no project code at all:
      ```bash
      python3 - <<'PY'
      import hashlib, json
      e = json.loads(open("/Users/YOU/sift-ledger/ledger/manifest.jsonl").readline())
      body = {k: v for k, v in e.items() if k != "entry_hash"}
      c = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode()
      print(hashlib.sha256(b"sift-sealed-ledger/v1/entry\n" + c).hexdigest())
      PY
      ```
- [ ] Independent check with the reference tool (opens only the synthetic canary):
      `age -d -i ~/sift-ledger/primary-identity.txt ~/sift-ledger/ledger/sealed/000000.age | head -c 200` — you should read "SYNTHETIC CANARY …". Repeat with the backup identity. Then try the **restored** copies from step C.
- [ ] **Write down offline** (paper or a note on a different device, *not* in the witness folder): `genesis_hash`, `recipients_sha256`, `witness_log_head`.
- [ ] Register the anchor: environment `sealed-ledger` → variable `SEALED_LEDGER_GENESIS_HASH` = the genesis hash. From now on the publish job refuses any ledger whose genesis differs from this value, and refuses to publish at all until it is set.

## G. First real publication (separate approval)  **[YOU approve; CLAUDE dispatches and verifies]**

- [ ] You say "go": the assistant runs `publish=true` for the first post-freeze date (2026-10-21), then later dates **in ascending order, one at a time**. Each run waits for your approval in the environment, runs the completeness audit (a skipped or incomplete earlier day makes the run fail closed) and commits only ciphertext + manifest.
- [ ] After each publication (at least weekly): `cd ~/sift-ledger/ledger && cp -a . ../ledger_prev && git pull --ff-only && owner verify --store . --dir ~/sift-ledger/witness --recipients ~/sift-ledger/repo/research/sealed_ledger/recipients.txt --previous ../ledger_prev --expect-genesis <genesis_hash> --expect-witness-head <witness_log_head>` → must print `"ok": true`. Then `owner witness … --recipients …` and write down the new `witness_log_head`. Any `TRUNCATED`, `ROLLED BACK`, `REPLACED` or `REWRITTEN` message: stop, keep the copies, do not witness.
- [ ] The preregistered look (≥ 150 closed-day games): see `SEALED_LEDGER_KEY_SETUP.md` §6. Nothing in this checklist opens real results early.

## H. Only after A–G and your explicit approval: the daily schedule  **[CLAUDE prepares; YOU approve]**

- [ ] Review the (already written, commented-out) `schedule:` block and the failure-alert job; approve enabling it. Until then nothing runs by itself.

## What you do NOT need to do

- You do not set or manage any secret. There is no private-key secret, anywhere, ever. (An *optional* signing-key secret exists only if you later choose runner attestations.)
- You do not touch Python dependencies or action pins; see `DEPENDENCY_AND_ACTION_PINNING.md` for the periodic update procedure the assistant follows.
