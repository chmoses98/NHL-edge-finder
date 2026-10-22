# Sealed ledger — owner setup checklist (macOS, unattended operation)

> **You never paste a private key anywhere — not into chat, an issue, a PR, a repository variable, or a synced note.** The one secret that does go into GitHub is the **ledger deploy key** (below): it can write *only* the ledger repository (which holds nothing but ciphertext), it is not an age key, and it cannot decrypt anything. Architecture and permissions analysis: `SEALED_LEDGER_UNATTENDED.md`. Key custody and recovery: `SEALED_LEDGER_KEY_SETUP.md`.
>
> **[YOU]** = only you can do it. **[CLAUDE]** = the assistant can do it on request, with no secret involved. After step H nothing in this list is routine.

## A. Prepare the Mac  **[YOU]**

- [ ] FileVault is on (System Settings → Privacy & Security → FileVault).
- [ ] `brew install age python@3.12 git`
- [ ] ```bash
      mkdir -m 700 ~/sift-ledger && cd ~/sift-ledger
      git clone https://github.com/chmoses98/NHL-edge-finder.git repo      # check out a commit you have reviewed
      python3.12 -m venv venv && ./venv/bin/pip install -r repo/requirements/research-runtime.in
      alias owner='PYTHONPATH=$HOME/sift-ledger/repo/src $HOME/sift-ledger/venv/bin/python -m nhl_edge.sealed_ledger.owner'
      ```
      (The `*.lock` files pin Linux wheels for the runner and will not install on macOS.)

## B. Keys  **[YOU]**

- [ ] `owner keygen --identity ~/sift-ledger/primary-identity.txt` → copy the printed **public** key (`age1…`).
- [ ] `owner keygen --identity ~/sift-ledger/backup-identity.txt` → copy that public key too.
- [ ] `owner witness-keygen --dir ~/sift-ledger/witness` (passphrase ≥ 8 characters), then store the same passphrase in your login Keychain for the optional weekly job: `security add-generic-password -a "$USER" -s sift-witness -w`.
- [ ] `chmod 600 ~/sift-ledger/*identity.txt`

## C. Independent backups and recovery drill  **[YOU]** — before anything is published

- [ ] `cd ~/sift-ledger && age -p -o primary-identity.txt.age primary-identity.txt && age -p -o backup-identity.txt.age backup-identity.txt` (a long passphrase each).
- [ ] `primary-identity.txt.age` → offline USB A; `backup-identity.txt.age` → a *different* medium/location B; copy `~/sift-ledger/witness/` to A. Write down where each copy is.
- [ ] Restore test: decrypt each `.age` backup to a scratch file (`age -d -o /tmp/p.txt …`), run `owner check-key` (after D) on it, delete the scratch file.
- [ ] No unencrypted identity in iCloud/Dropbox, email or the repository checkout.

## D. Give the repository your PUBLIC keys  **[YOU, or CLAUDE with your two `age1…` strings]**

- [ ] Add the two `age1…` lines to `research/sealed_ledger/recipients.txt` (keep the comments) via a PR; merge it. `git pull` your checkout.
- [ ] `owner check-key --identity ~/sift-ledger/primary-identity.txt --recipients ~/sift-ledger/repo/research/sealed_ledger/recipients.txt` and for the backup: both must print `"identity_matches_recipient": true, "canary_roundtrip": true`, no warning.

## E. The ledger repository and its deploy key  **[YOU]** (GitHub web UI)

- [ ] **New repository** `<you>/nhl-sealed-ledger` — **public**, **empty** (do NOT add a README, licence or .gitignore). Settings → Actions → General → **Disable actions**.
- [ ] Ledger repo → Settings → Rules → Rulesets: (1) branch `main`: *Restrict deletions* + *Block force pushes*; (2) tags `sealed-ledger-head-*`: *Restrict deletions* + *Restrict updates*.
- [ ] On the Mac: `ssh-keygen -t ed25519 -N "" -C "sealed-ledger-publisher" -f /tmp/ledger_deploy_key` → ledger repo → Settings → Deploy keys → Add → paste `/tmp/ledger_deploy_key.pub`, **tick "Allow write access"**. Keep the *private* file `/tmp/ledger_deploy_key` only until step F, then `rm -P /tmp/ledger_deploy_key*`.

## F. Environments, secret and variables in the code repository  **[YOU]** (Settings in `NHL-edge-finder`)

- [ ] **Variables → Repository variable** `SEALED_LEDGER_REPO` = `<you>/nhl-sealed-ledger`.
- [ ] **Environments → New** `sealed-ledger-publish`: Deployment branches = **Selected branches → `main`**; **no required reviewers**. Add secret `SEALED_LEDGER_DEPLOY_KEY` = the content of `/tmp/ledger_deploy_key` (the whole file). Add environment variables `SEALED_LEDGER_REPO` (same value) and `SEALED_LEDGER_ACTIVATION_SHA` = `shasum -a 256 ~/sift-ledger/repo/research/sealed_ledger/recipients.txt` (after `git pull`).
- [ ] **Environments → New** `sealed-ledger-admin`: Deployment branches = `main`; **Required reviewers = you**. Same secret and the same two variables.
- [ ] Delete the local private deploy-key file now (`rm -P /tmp/ledger_deploy_key*`).
- [ ] Recommended: Rules → Rulesets on `main` of the code repo: require pull requests (no force-push, no deletion); add `CODEOWNERS` entries for `.github/workflows/**`, `requirements/**`, `scripts/sealed_ledger_publish.sh`, `src/nhl_edge/sealed_ledger/**`, `research/sealed_ledger/recipients.txt`. Keep default **Workflow permissions** = *Read repository contents*. No other collaborators; two-factor authentication on.

## G. Create the ledger and take the first checkpoint  **[YOU approve; CLAUDE can dispatch]**

- [ ] Run workflow **`sealed_ledger_admin`** on `main`: `action = init`. **Approve** the `sealed-ledger-admin` deployment when GitHub asks. The ledger repository now holds `manifest.jsonl` (one GENESIS entry), `sealed/000000.age` (a **synthetic canary** encrypted to both your keys) and tag `sealed-ledger-head-0`. No game is sealed.
- [ ] `git clone https://github.com/<you>/nhl-sealed-ledger.git ~/sift-ledger/ledger`
- [ ] `owner first-checkpoint --store ~/sift-ledger/ledger --identity ~/sift-ledger/primary-identity.txt --identity ~/sift-ledger/backup-identity.txt --dir ~/sift-ledger/witness --recipients ~/sift-ledger/repo/research/sealed_ledger/recipients.txt` — verifies the structure and recipients, proves **each identity on its own opens the real published canary**, signs your first witness checkpoint, writes `~/sift-ledger/witness/state.json`, prints `genesis_hash`, `recipients_sha256`, `witness_log_head`.
- [ ] **Compare the genesis hash in three places — identical:** the `owner` output; the admin run summary on GitHub (the tag message of `sealed-ledger-head-0` in the ledger repo); and a stdlib-only recomputation with no project code:
      ```bash
      python3 - <<'PY'
      import hashlib, json
      e = json.loads(open('/Users/YOU/sift-ledger/ledger/manifest.jsonl').readline())
      body = {k: v for k, v in e.items() if k != 'entry_hash'}
      c = json.dumps(body, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False).encode()
      print(hashlib.sha256(b'sift-sealed-ledger/v1/entry\n' + c).hexdigest())
      PY
      ```
- [ ] Independent check with the reference tool (opens only the synthetic canary): `age -d -i ~/sift-ledger/primary-identity.txt ~/sift-ledger/ledger/sealed/000000.age | head -c 200` → "SYNTHETIC CANARY …". Repeat with the backup, then with the **restored** copies from C.
- [ ] **Write down offline** (paper, a note on another device): `genesis_hash`, `recipients_sha256`, `witness_log_head`.
- [ ] Register the anchor: environment variable `SEALED_LEDGER_GENESIS_HASH` = the genesis hash, in **both** environments. From now on the publisher refuses any ledger whose genesis differs, and refuses to publish until it is set.

## H. See it work, then enable the schedule  **[YOU approve; CLAUDE prepares]**

- [ ] Run **`sealed_ledger_daily`** with `dry_run = true`: it reconciles on a throw-away copy and reports what it *would* seal (no publication). Check the report artifact (counts and game ids only).
- [ ] Run it once with `dry_run = false`: it catches up every day since 2026-10-21 and publishes (no approval prompt: the `sealed-ledger-publish` environment has no reviewers). Check that the ledger repository received only `manifest.jsonl`, `sealed/*.age`, tags.
- [ ] Approve enabling the cron: a one-line PR (uncomment `schedule:`) reviewed and merged by you.
- [ ] Optional, recommended — your Mac checks the ledger weekly and notifies only on trouble: copy `repo/scripts/owner_weekly_check.sh` somewhere stable, set `SIFT_LEDGER_URL`, and load a launchd agent:
      ```xml
      <!-- ~/Library/LaunchAgents/com.sift.ledgercheck.plist -->
      <plist version="1.0"><dict>
        <key>Label</key><string>com.sift.ledgercheck</string>
        <key>ProgramArguments</key><array><string>/Users/YOU/sift-ledger/repo/scripts/owner_weekly_check.sh</string></array>
        <key>EnvironmentVariables</key><dict><key>SIFT_LEDGER_URL</key><string>https://github.com/YOU/nhl-sealed-ledger.git</string></dict>
        <key>StartCalendarInterval</key><dict><key>Weekday</key><integer>1</integer><key>Hour</key><integer>9</integer></dict>
      </dict></plist>
      ```
      `launchctl load ~/Library/LaunchAgents/com.sift.ledgercheck.plist`. It verifies against your registered genesis hash, your last copy and your witness log head, signs a new checkpoint, and shows a macOS notification if anything is wrong or no day was closed for 4 days. (A copy of the witness folder on your offline medium once a month is still wise.)

## After H: what you do, and when

- **Nothing routine.** Collection, catch-up, retries, corrections from source revisions and exclusions of games that never finish all happen on their own.
- **An exception issue** (`sealed ledger: BLOCKED: …` or `… failed`): read it; most need only "investigate"; ask the assistant. Only *you* approve anything in `sealed_ledger_admin`.
- **A key or protocol change**: a PR you review and merge, then re-register the activation hash (and, for a key change, start a new ledger: a new genesis).
- **The looks** at 150 / 300 / 450 closed-day games: `SEALED_LEDGER_KEY_SETUP.md` §6 (decrypt locally, `owner reproduce`, `owner look`). Nothing else ever decrypts.
- **Real betting** stays disabled; nothing here can enable it.

## If an exception needs a decision  **[YOU decide; CLAUDE explains and dispatches]**

- [ ] The failed run's log shows the block codes; the report artifact (`reconcile_summary.json`) lists ids and counts only.
- [ ] `ORPHAN_RESULT`, `DRIFT`, `EXTRA`, `UNSEALED`, `MODEL_DRIFT`, `C1_PARAMS_CHANGED`: stop and ask the assistant to investigate before approving anything.
- [ ] A game stuck for a reason the 14-day rule does not cover: `sealed_ledger_admin` → `exclude` (reason code) — public in the manifest; only unfinished games can be excluded.
- [ ] A revision the automatic path refused (`CORRECTION_LIMIT`): `sealed_ledger_admin` → `correct` (`GAME_ID@VERSION`, reason) — rare; ask first.
