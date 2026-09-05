from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("사용법: python3 -B -m python_basic PB0001 [--strict|--verify-receipt]")
        raise SystemExit(2)

    runner = Path(__file__).resolve().parent.parent / "run_problem.py"
    completed = subprocess.run(
        [sys.executable, "-B", str(runner), *sys.argv[1:]],
        check=False,
    )
    raise SystemExit(completed.returncode)


if __name__ == "__main__":
    main()
