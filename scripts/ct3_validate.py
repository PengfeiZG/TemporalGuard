"""Same as `temporalguard ct3 validate`; kept so `python scripts/ct3_validate.py FILE` still works."""

import sys

from temporalguard.eval.ct3_data import DEFAULT_PATH
from temporalguard.eval.ct3_validate import validate_file

if __name__ == "__main__":
    report, problems = validate_file(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PATH)
    print(report)
    sys.exit(1 if problems else 0)
