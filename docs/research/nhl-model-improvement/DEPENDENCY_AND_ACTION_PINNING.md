# Pinned actions and hash-locked dependencies (research workflows)

> RESEARCH ONLY. Scope: `.github/workflows/sealed_ledger_daily.yml`, `sealed_ledger_admin.yml` and `market_audit.yml` — the two workflows that read the archive and (for the sealed ledger) hold a write token. Production workflows (`ci.yml`, capture, conductor, …) still use floating action tags and the project's normal install; changing them is a separate decision because it touches production CI.

## What is pinned and why

| layer | how it is pinned | what it protects against |
|---|---|---|
| GitHub Actions (`checkout`, `setup-python`, `upload-artifact`, `download-artifact`) | full 40-hex commit SHA with a `# vX.Y.Z` comment | a moved or re-tagged action (the tag a workflow names is mutable; the commit is not) |
| Python packages | `requirements/*.lock`, compiled by `uv` with `--generate-hashes`; installed with `pip install --require-hashes --only-binary=:all: --no-deps -r …` | a swapped or tampered package on PyPI, a new transitive release, any build-time code execution from an sdist |
| the project itself | not pip-installed: `PYTHONPATH=$GITHUB_WORKSPACE/src` | pip's isolated build fetching unpinned `setuptools`/`wheel` |
| Python itself | `actions/setup-python` with `3.11` (locks are resolved for CPython 3.11, Linux x86_64) | wheel/ABI mismatch |

Current pins (verified on 2026-10-22 with `git ls-remote --tags https://github.com/actions/<name> 'refs/tags/<vN>*'` — each floating major tag and its highest `vN.x.y` tag resolved to the same SHA, lightweight tags, so the SHA is a commit — and `git fetch --depth=1 <repo> <SHA> && git cat-file -t FETCH_HEAD` returning `commit`; re-run those two commands to re-verify):

| action | version | commit |
|---|---|---|
| `actions/checkout` | v4.4.0 | `11d5960a326750d5838078e36cf38b85af677262` |
| `actions/setup-python` | v5.6.0 | `a26af69be951a213d495a4c3e4e4022e16d87065` |
| `actions/upload-artifact` | v4.6.2 | `ea165f8d65b6e75b540449e92b4886f43607fa02` |
| `actions/download-artifact` | v4.3.0 | `d3f86a106a0bac45b974a628896c90dbdf5c8093` |

Locks: `requirements/research-runtime.lock` (the settle job and `market_audit`: numpy, pandas, pyarrow, pydantic, httpx, pyyaml, scipy, statsmodels, pyrage, cryptography + transitive) and `requirements/sealed-publish.lock` (the publish job, which holds the write token: only pyrage, cryptography, cffi, pycparser). The publish job deliberately installs the smallest possible set.

`pip --require-hashes` accepts a package only if its downloaded file matches one of the listed hashes; a mismatch fails the job (verified: a wrong hash → exit 1 "THESE PACKAGES DO NOT MATCH THE HASHES"). `--no-deps` stops pip resolving anything not in the lock; `--only-binary=:all:` refuses source distributions. The locks were installed and the sealed-ledger self-test run under CPython 3.11 before being committed.

Tests (`tests/test_research_workflows.py`) fail if: any `uses:` in these workflows is not a 40-hex SHA with a version comment; any `pip install` lacks `--require-hashes --only-binary=:all: --no-deps -r requirements/*.lock`; a lock line has no hash or contains a URL/VCS/editable reference; the small lock disagrees with the big one on a shared package.

## Update procedure (do this on a schedule: monthly, and immediately for a security advisory)

**Python dependencies**

```bash
pip install uv                                   # once
scripts/relock_research_deps.sh                  # re-resolve everything to the newest allowed versions
scripts/relock_research_deps.sh --upgrade-package pyrage    # or just one package (e.g. for an advisory)
git diff requirements/                           # review: versions that moved, anything new in the transitive set
pytest tests/test_sealed_ledger.py tests/test_research_workflows.py && pytest -q -n auto
```

Open a PR. In review, read the changelog of every changed *direct* dependency, and treat a change to `pyrage` or `cryptography` as security-relevant (check their release notes/advisories). The CI run of the PR installs nothing from the lock (CI installs the project normally), so also run a `publish=false` dry run of `model_research_daily` from the branch: its install step exercises the lock on the real runner image. Merge only after the dry run is green.

**GitHub Actions**

```bash
# 1. find the new release you want (example: checkout v4.x)
git ls-remote --tags https://github.com/actions/checkout 'refs/tags/v4.*' | sort -k2 -V | tail -3
# 2. confirm the tag is a COMMIT (not an annotated tag object) and read what changed
mkdir /tmp/pin && cd /tmp/pin && git init -q && git fetch --depth=50 https://github.com/actions/checkout <SHA> && git cat-file -t FETCH_HEAD && git log --oneline -20 FETCH_HEAD
# 3. replace the SHA and the "# vX.Y.Z" comment in BOTH research workflows (one pin, one version, everywhere)
# 4. run the tests (they enforce the SHA + comment format) and a publish=false dry run
```

Prefer a release at least two weeks old unless it fixes a published vulnerability. Never replace a SHA with a tag. GitHub's Dependabot (`github-actions` ecosystem) can open these PRs automatically; enabling it is an optional owner decision (it adds PR noise but no write access to anything).

## What this does not cover

* A malicious *release* of a pinned action or package that you update to is not caught by pinning; the review step above is the control.
* PyPI could serve a yanked/compromised file only if its hash is in the lock — hashes come from the index at lock time, so lock on a clean machine and compare the diff, not just the tests.
* `pip` itself and the runner image's Python are not pinned (they come from `actions/setup-python` and the hosted runner). The lock files bound everything installed *by us*.
* Production workflows are unchanged (see the scope note).
