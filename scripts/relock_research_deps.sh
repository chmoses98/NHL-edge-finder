#!/usr/bin/env bash
# Re-resolve the hash-locked requirements used by the research workflows (CPython 3.11, Linux x86_64 = the ubuntu-latest runner).
# Usage: scripts/relock_research_deps.sh            # re-resolve to the newest allowed versions
#        scripts/relock_research_deps.sh --upgrade-package pyrage   # only that package
# Needs `uv` (pip install uv). Review the diff of requirements/*.lock, run the full test suite, then open a PR. See
# docs/research/nhl-model-improvement/DEPENDENCY_AND_ACTION_PINNING.md.
set -euo pipefail
cd "$(dirname "$0")/.."
for n in research-runtime sealed-publish; do
  uv pip compile "requirements/$n.in" --python-version 3.11 --python-platform x86_64-manylinux_2_28 --generate-hashes --no-header --quiet "$@" -o "requirements/$n.lock"
done
echo "re-locked; now review 'git diff requirements/' and run the tests (pytest tests/test_sealed_ledger.py tests/test_research_workflows.py)"
