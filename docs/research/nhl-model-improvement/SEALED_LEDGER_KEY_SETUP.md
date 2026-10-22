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
   python3 -m venv venv && ./venv/bin/pip install -r repo/requirements/research-runtime.in     # (the *.lock files pin Linux wheels for the runner; they do not install on macOS)
   ```
   Run the owner tool with `~/sift-ledger/venv/bin/python -m nhl_edge.sealed_ledger.owner …` (shortened to `owner …` below). It refuses to run under CI.

## 2. Generate the keys (offline is best; any trusted machine is acceptable)

```bash
owner keygen --identity ~/sift-ledger/primary-identity.txt       # prints ONLY the public key (age1…)
owner keygen --identity ~/sift-ledger/backup-identity.txt        # a second, independent key
owner witness-keygen --dir ~/sift-ledger/witness                 # asks for a passphrase (>= 8 characters); prints the witness PUBLIC key
chmod 700 ~/sift-ledger; chmod 600 ~/sift-ledger/*identity.txt
```

The tool refuses to overwrite an existing key and writes private files with mode 0600. (`age-keygen -o file` from `brew install age` produces the identical format if you prefer the reference tool.)

## 3. Back up — before anything is published

* **Primary identity**: keep the file on the FileVault-encrypted MacBook **and** one passphrase-encrypted offline copy: `age -p -o primary-identity.txt.age primary-identity.txt` (choose a long passphrase you will not forget), then copy the `.age` file to a USB stick kept in a safe place. `owner` reads `.age` identity files and prompts for the passphrase.
* **Backup identity**: *different custody from the primary* — e.g. an encrypted copy in a second physical location or your password manager's secure note. The point is that no single loss or theft removes both keys.
* **Witness directory**: copy `~/sift-ledger/witness/` to the same offline medium (it contains the passphrase-protected private key, the public key and the log).
* Write down *where* each copy is. A backup you cannot find is no backup.

Recovery drill, concretely (do it twice: once right after generating the keys, once on the real ledger at the first checkpoint):

1. `owner check-key --identity <restored file> --recipients …` — the restored copy derives a public key that is in `recipients.txt` and round-trips a canary.
2. On the real published ledger: `owner drill --store ~/sift-ledger/ledger --identity <primary> --identity <backup> --recipients …` — **each identity on its own** opens the genesis canary (a synthetic record sealed to every recipient). `owner first-checkpoint` does this for you.
3. With no project code at all: `age -d -i <identity> ~/sift-ledger/ledger/sealed/000000.age` prints the synthetic canary.

A key that has not passed step 2 on the real ledger is not a recovery key.

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

The ordered, checkable version of this section is `SEALED_LEDGER_OWNER_CHECKLIST.md`. In outline: put your public keys in `recipients.txt` (§4); create the `sealed-ledger` **environment** (deployment branches = `main` only, you as required reviewer) and set its **environment** variable `SEALED_LEDGER_ACTIVATION_SHA` = `shasum -a 256 research/sealed_ledger/recipients.txt`; add branch/tag rulesets for `model-research-sealed-ledger` and `sealed-ledger-head-*`; run the one-time `init_ledger` publish (it seals no game); verify it yourself with `owner first-checkpoint` (verification, recovery drill with every key, signed first witness checkpoint), compare the genesis hash across three places, write it down offline and register it as the environment variable `SEALED_LEDGER_GENESIS_HASH`; only then approve the first real `publish=true` run (2026-10-21, then each later date in ascending order, one at a time).

## 6. Routine use

```bash
git clone --branch model-research-sealed-ledger --single-branch https://github.com/chmoses98/NHL-edge-finder.git ~/sift-ledger/ledger   # first time
cd ~/sift-ledger/ledger && cp -a . ../ledger_prev_$(date +%F) && git pull --ff-only                                                      # keep the previous copy
owner verify  --store ~/sift-ledger/ledger --dir ~/sift-ledger/witness --recipients ~/sift-ledger/repo/research/sealed_ledger/recipients.txt --previous ~/sift-ledger/ledger_prev_YYYY-MM-DD
owner witness --store ~/sift-ledger/ledger --dir ~/sift-ledger/witness --recipients ~/sift-ledger/repo/research/sealed_ledger/recipients.txt   # signs the verified head into YOUR log; do this weekly
```
`witness` prints `witness_log_head`. **Write that value down somewhere other than the witness folder** (paper, a note on another device) and pass it next time as `--expect-witness-head <value>` to `verify`: it is what exposes removal of the last lines of your own log.
```bash
```

`verify` must print `"ok": true`. Any `problem` mentioning TRUNCATED, ROLLED BACK, REPLACED or REWRITTEN means the public ledger no longer extends what you witnessed: **stop, do not witness, and keep the copies**. (The strongest evidence is your own earlier copy plus your signed log.)

### The look (once, at ≥ 150 games)

```bash
owner witness --store ~/sift-ledger/ledger --dir ~/sift-ledger/witness --recipients ~/sift-ledger/repo/research/sealed_ledger/recipients.txt
owner reproduce --store ~/sift-ledger/ledger --identity ~/sift-ledger/primary-identity.txt --archive <data-archive checkout> --repo ~/sift-ledger/repo   # forgery/omission check; prints no values
owner look --store ~/sift-ledger/ledger --identity ~/sift-ledger/primary-identity.txt --dir ~/sift-ledger/witness --recipients ~/sift-ledger/repo/research/sealed_ledger/recipients.txt --out ~/sift-ledger/looks
```

`look` refuses before 150 *closed-day* games (and decrypts nothing), refuses a ledger that fails verification, a recipients mismatch or the witness check, and takes the smallest look level not yet taken (150, then 300, then 450) on exactly the first *k* games, once each: a marker in the witness folder stops a repeat even with a different `--out`, so keep that folder. Record in the experiment registry that the look was taken. Reading records any other way (for example `age -d`) before the threshold breaks the blinding and must be registered as such in the registry.

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
