#!/usr/bin/env python
"""Publish the Edge Finder research explorer (contract 1.1.0) into ``<out>/explorer``, after the app export.

    python scripts/research_export.py --data-root data/archive --out data/archive/app/latest [--now ...] [--history-root data/history]

Thin wrapper over :mod:`nhl_edge.research_export` (same as ``nhl research-export``). Exit 1 when the publication
failed; the previous explorer tree is then untouched.
"""

from __future__ import annotations

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for p in (os.path.join(REPO_ROOT, "src"), os.path.join(REPO_ROOT, "contract")):
    if p not in sys.path:
        sys.path.insert(0, p)

from nhl_edge.research_export import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
