"""Same as `temporalguard ct3 probe`; kept so `python scripts/ct3_agent_probe.py ...` still works."""

import sys

from temporalguard.eval.ct3_probe import main

if __name__ == "__main__":
    sys.exit(main())
