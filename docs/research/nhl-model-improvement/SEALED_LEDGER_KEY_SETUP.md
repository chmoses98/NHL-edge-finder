# Sealed ledger — key setup, recovery and activation (owner procedure, MacBook)

> You do all of this yourself, on your own machine. **Never paste a private key into chat, an issue, a PR, an Actions secret, a note synced to an AI tool, or any file inside a git checkout.** Nobody will ever ask you for it. The only things you ever share are the *public* keys (they start with `age1`) and the SHA-256 of `recipients.txt`.

## 0. What you will hold

| item | what it is | where it lives | share? |
|---|---|---|---|
| **primary identity** | age private key (`AGE-SECRET-KEY-…`) | `~/sift-ledger/primary-identity.txt` (+ offline backups) | **never** |
| **backup identity** | a second age private key, different custody | offline (see 3) | **never** |
| primary / backup **public** keys | `age1…` lines | committed in `research/sealed_ledger/recipients.txt` | yes |
| **witness key** | Ed25519, passphrase-protected | `~/sift-ledger/witness/witness_private.pem` | never |
| witness public key, witness log | `witness_public.pem`, `witness.jsonl` | same folder; back up | public key fine |

Losing **both** identities makes the ledger unreadable (§6). Losing the witness directory loses your anti-rollback anchor (not your data).

## 1. One-time machine preparation

1. Make sure FileVault is on (System Settings → Privacy & Security → FileVault).
2. Install tooling (Homebrew): `brew install age python@3.12 git`.
3. Create a private working folder and a Python environment:
   ```bash
   mkdir -m 700 ~/sift-ledger && cd ~/sift-ledger
   git clone https://github.com/chmoses98/NHL-edge-finder.git repo        # review the commit you will run; pin it
   python3 -m venv venv && ./venv/bin/pip install -e "repo[sealed]"
   ```
   Run the owner tool with `~/sift-ledger/venv/bin/python -m nhl_edge.sealed_ledger.owner …` (shortened to `owner …` below). It refuses to run under CI.

## 2. Generate the keys (offline is best; any trusted machine is acceptable)

```bash
owner keygen --identity ~/sift-ledger/primary-identity.txt       # prints ONLY the public key (age1…)
owner keygen --identity ~/sift-ledger/backup-identity.txt        # a second, independent key
owner witness-keygen --dir ~/sift-ledger/witness                 # asks for a passphrase twice; prints the witness PUBLIC key
chmod 700 ~/sift-ledger; chmod 600 ~/sift-ledger/*identity.txt
```

The tool refuses to overwrite an existing key and writes private files with mode 0600. (`age-keygen -o file` from `brew install age` produces the identical format if you prefer the reference tool.)

## 3. Back up — before anything is published

* **Primary identity**: keep the file on the FileVault-encrypted MacBook **and** one passphrase-encrypted offline copy: `age -p -o primary-identity.txt.age primary-identity.txt` (choose a long passphrase you will not forget), then copy the `.age` file to a USB stick kept in a safe place. `owner` reads `.age` identity files and prompts for the passphrase.
* **Backup identity**: *different custody from the primary* — e.g. an encrypted copy in a second physical location or your password manager's secure note. The point is that no single loss or theft removes both keys.
* **Witness directory**: copy `~/sift-ledger/witness/` to the same offline medium (it contains the passphrase-protected private key, the public key and the log).
* Write down *where* each copy is. A backup you cannot find is no backup.

Test a restore now, not later: copy the `.age` file to a scratch folder, `age -d -o /tmp/test-identity.txt primary-identity.txt.age`, run `owner check-key` (step 4) against it, then `rm /tmp/test-identity.txt`.

## 4. Put only the PUBLIC keys in the repository

Copy the two `age1…` strings (printed by `keygen`, also in the `# public key:` comment line of each identity file) into `research/sealed_ledger/recipients.txt`, one per line (keep the comment lines), and open a pull request — or send the two `age1…` strings to Claude to do it. **Do not** send anything that starts with `AGE-SECRET-KEY`; the loader and CI both refuse such a file.

Then prove your keys match the committed file (this encrypts a random canary to the file and decrypts it with your key):

```bash
owner check-key --identity ~/sift-ledger/primary-identity.txt --recipients ~/sift-ledger/repo/research/sealed_ledger/recipients.txt
owner check-key --identity ~/sift-ledger/backup-identity.txt  --recipients ~/sift-ledger/repo/research/sealed_ledger/recipients.txt
```

Both must print `"identity_matches_recipient": true, "canary_roundtrip": true`, and no warning (a warning means only one recipient is configured).

## 5. Activation (separate, explicit approval — nothing below happens until you say so)

1. Review `SEALED_LEDGER_DESIGN.md` (threat model, §5–§7) and the PR.
2. Merge the PR that adds your public keys.
3. Compute the activation hash on the merged file and set it as a **repository variable** (not a secret): Settings → Secrets and variables → Actions → *Variables* → New repository variable `SEALED_LEDGER_ACTIVATION_SHA` = output of
   ```bash
   shasum -a 256 research/sealed_ledger/recipients.txt
   ```
   The workflow refuses to publish unless this equals the SHA-256 of the committed `recipients.txt`; changing a key later invalidates the activation until you reset it.
4. *(Recommended hardening)* Settings → Rules → Rulesets: a branch ruleset on `model-research-sealed-ledger` that blocks deletion and force-push, and a tag ruleset for `sealed-ledger-head-*` that blocks deletion and updates.
5. Approve **one controlled initialisation**: run `model_research_daily` with `publish=true` for the first post-freeze date (`2026-10-21`), then each later date in ascending order. Check the run: only `model-research-sealed-ledger` received commits; they hold only `manifest.jsonl`, `sealed/*.age`, `README.md`.
6. Witness it (below). Only then consider the schedule (uncomment `schedule:` after reviewing the configuration — another approval).

## 6. Routine use

```bash
git clone --branch model-research-sealed-ledger --single-branch https://github.com/chmoses98/NHL-edge-finder.git ~/sift-ledger/ledger   # first time
cd ~/sift-ledger/ledger && cp -a . ../ledger_prev_$(date +%F) && git pull --ff-only                                                      # keep the previous copy
owner verify  --store ~/sift-ledger/ledger --dir ~/sift-ledger/witness --recipients ~/sift-ledger/repo/research/sealed_ledger/recipients.txt --previous ~/sift-ledger/ledger_prev_YYYY-MM-DD
owner witness --store ~/sift-ledger/ledger --dir ~/sift-ledger/witness        # signs the verified head into YOUR log; do this weekly
```

`verify` must print `"ok": true`. Any `problem` mentioning TRUNCATED, ROLLED BACK, REPLACED or REWRITTEN means the public ledger no longer extends what you witnessed: **stop, do not witness, and keep the copies**. (The strongest evidence is your own earlier copy plus your signed log.)

### The look (once, at ≥ 150 games)

```bash
owner witness --store ~/sift-ledger/ledger --dir ~/sift-ledger/witness
owner reproduce --store ~/sift-ledger/ledger --identity ~/sift-ledger/primary-identity.txt --archive <data-archive checkout> --repo ~/sift-ledger/repo   # forgery/omission check; prints no values
owner look --store ~/sift-ledger/ledger --identity ~/sift-ledger/primary-identity.txt --dir ~/sift-ledger/witness --out ~/sift-ledger/looks
```

`look` refuses before 150 distinct games (and decrypts nothing), refuses a ledger that fails verification or the witness check, and writes `LOOK_150.json` once. Record in the experiment registry that the look was taken. Reading records any other way (for example `age -d`) before the threshold breaks the blinding and must be registered as such in the registry.

## 7. Recovery and incidents

| situation | do this |
|---|---|
| lost laptop / disk | restore the encrypted identity backup (`age -d -o identity.txt primary-identity.txt.age`), `owner check-key`, restore the witness folder, re-clone the repo at a reviewed commit |
| lost the primary but have the backup identity | use the backup identity for `owner look --identity …` (both are recipients of every record); generate a replacement for future ledgers |
| lost **both** identities | the records cannot be recovered. The pregame forecasts can be re-derived from the archive, but the commit–reveal value for that period is gone: record a NOTE in the experiment registry and start a new ledger with a new key |
| private key (or its backup) may have been exposed | treat the prospective tier as unblinded from that moment, record it in the registry, rotate: new keys, new ledger, new genesis; do not edit the old one |
| witness passphrase forgotten | generate a new witness key; keep the old log and note the discontinuity |
| `verify` fails | see §6; never witness a failing ledger |

## 8. What Claude (or any tool) can and cannot do

Claude can implement, test and review the sealing code, commit the public keys you give it, and run `publish=false` dry-runs. Claude cannot read the ledger, never receives a private key, and will not ask you for one. The activation variable, the key custody and the look are yours.
