"""Build a fresh, persistent public-release checkout without learner data."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
DESTINATION = ROOT / "public-release"

# Intentionally explicit: a new personal .py file must never become public
# merely because its basename happens to match a discovery glob.
PUBLIC_SOURCE_FILES = (
    "run_problem.py", "bank_inventory.py", "review_bank.py", "export_public.py",
    "python_basic/__init__.py", "python_basic/__main__.py",
    "python_basic/generate_bank.py", "python_basic/regenerate_problems.py",
    "python_basic/source_checks.py", "python_basic/validate_bank.py",
    "python_basic/catalog/__init__.py", "python_basic/catalog/model.py",
    "python_basic/catalog/intro_variables_math.py",
    "python_basic/catalog/functions_conditionals_loops.py",
    "python_basic/catalog/strings_lists.py",
    "python_basic/catalog/collections_io_exceptions.py",
    "python_basic/catalog/validate_catalog.py",
    "python_coding/__init__.py", "python_coding/__main__.py",
    "python_coding/generate_bank.py", "python_coding/quality_catalog.py",
    "python_coding/quality_regenerate.py", "python_coding/regenerate_variants.py",
    "python_coding/validate_bank.py", "python_coding/fluency_catalog.py",
    "tests/test_basic_quality.py", "tests/test_coding_quality.py",
    "tests/test_fluency_catalog.py", "tests/test_bank_review.py",
)
PUBLIC_DOCUMENTS = (
    "STUDY_PATH.md", "python_basic/README.md", "python_basic/INDEX.md",
    "python_coding/README.md", "python_coding/INDEX.md",
    "python_coding/REGENERATION_REPORT.md",
    "python_basic/catalog/generated_manifest.json", "python_coding/generated_manifest.json",
    "docs/reviews/2026-09-05-problem-bank-review.md",
    "docs/reviews/2026-09-05-python-coding-purpose-correction.md",
    "docs/reviews/2026-09-05-problem-bank.json",
)

README = """# Python Coding Drills

Python 문법과 코딩테스트용 Python 도구를 자동화하는 한국어 문제은행입니다.

- Python Basic: 820개 문법·기초 자료구조 드릴
- Python Coding: 800개 사용법 변형·반복 드릴
- 목적을 벗어났던 48개를 정렬 key, 복사/alias, deque, Counter,
  heapq, bisect 등의 150~300초 Python 사용법 문제로 교정했습니다.
- 알고리즘 패턴 학습과 C 레벨 인증은 후속 NeetCode 250의 역할입니다.
- 각 문제 파일은 스타터 코드와 공개 테스트를 제공합니다.

먼저 [학습 경로](STUDY_PATH.md)를 읽으세요.
[목적 교정 보고서](docs/reviews/2026-09-05-python-coding-purpose-correction.md)와
[1,620개 전체 검사 결과](docs/reviews/2026-09-05-problem-bank.json)도 제공합니다.
문제 수는 서로 다른 알고리즘 수나 면접 준비 완료의 증거가 아닙니다.

## 시작하기

Python 3.11 이상을 사용합니다. 별도 패키지 설치는 필요 없습니다.

```bash
git clone https://github.com/johndoe0x/painful-coding-test.git
cd painful-coding-test/drills
# python_basic/INDEX.md 또는 STUDY_PATH.md에서 문제를 선택해 구현합니다.
python3 -B -m python_basic PB0001 --strict
python3 -B -m python_coding CI0022 --strict
```

미구현 스타터는 FAIL을 출력하는 것이 정상입니다. 작성한 구현이 공개 예시와
구현 방식 검사를 통과하면 로컬 proofs/에 영수증을 기록합니다. 이 영수증은
공개 테스트 실행 기록이며 비공개 채점, 독립 풀이, 장기 기억을 인증하지 않습니다.
리뷰용 참조 구현은 tests/에 있으므로 블라인드 연습 중에는 열지 마세요.

## 검증

```bash
python3 -B -m python_basic.catalog.validate_catalog
python3 -B python_basic/validate_bank.py --strict-user-code
python3 -B python_coding/validate_bank.py --strict-user-code
python3 -B review_bank.py
python3 -B -m unittest discover -s tests -v
```

개인 풀이·proofs·백업·편집기 설정은 공개 문제은행 폴더에 포함하지 않았습니다.
저장소에는 이전 대시보드 소스·학습 계획·Git 이력이 함께 보존됩니다.
문제은행은 NeetCode 학습을 보조하기 위해 작성한 연습 자료이며,
NeetCode의 공식 배포물이나 공식 채점기가 아닙니다.
"""

GITIGNORE = """.tmp/
proofs/
**/_preserved_answers/
**/__pycache__/
*.py[cod]
.venv/
.env
.env.*
.DS_Store
"""

WORKFLOW = """name: Validate problem bank
on: [push, pull_request]
permissions:
  contents: read
jobs:
  validate:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.11', '3.12', '3.13']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -B -m python_basic.catalog.validate_catalog
      - run: python -B python_basic/validate_bank.py --strict-user-code
      - run: python -B python_coding/validate_bank.py --strict-user-code
      - run: python -B review_bank.py
      - run: python -B -m unittest discover -s tests -v
"""


def starter_builds(bank: str, module: str) -> list[dict]:
    # Each historical generator uses local imports; separate interpreters prevent
    # python_basic.generate_bank and python_coding.generate_bank from colliding.
    source = (
        f"from {module} import build_catalog; import json; "
        "print(json.dumps([{'id': b.problem_id, 'path': b.relative_path.as_posix(), "
        "'source': b.starter_source, 'sha256': b.starter_sha256} for b in build_catalog()]))"
    )
    result = subprocess.run([sys.executable, "-B", "-c", source], cwd=ROOT / bank,
                            check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def export() -> None:
    if DESTINATION.exists():
        raise SystemExit(f"Refusing to overwrite release directory: {DESTINATION}")
    builds = {
        "python_basic": starter_builds("python_basic", "regenerate_problems"),
        "python_coding": starter_builds("python_coding", "quality_regenerate"),
    }
    paths = [ROOT / name for name in (*PUBLIC_SOURCE_FILES, *PUBLIC_DOCUMENTS)]
    for path in paths:
        if not path.is_file() or path.is_symlink():
            raise SystemExit(f"Missing or symlinked publication input: {path}")
    DESTINATION.mkdir(parents=True)
    for path in paths:
        destination = DESTINATION / path.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, destination)
    for bank, problems in builds.items():
        manifest_path = (DESTINATION / bank / ("catalog/generated_manifest.json" if bank == "python_basic"
                                              else "generated_manifest.json"))
        manifest = json.loads(manifest_path.read_text())
        for problem in problems:
            if manifest["problems"][problem["id"]]["starter_sha256"] != problem["sha256"]:
                raise SystemExit(f"Stale generated manifest: {problem['id']}")
            destination = DESTINATION / bank / problem["path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(problem["source"], encoding="utf-8")
            if sha256(destination.read_bytes()).hexdigest() != problem["sha256"]:
                raise SystemExit(f"Starter bytes mismatch: {problem['id']}")
    (DESTINATION / "README.md").write_text(README, encoding="utf-8")
    (DESTINATION / ".gitignore").write_text(GITIGNORE, encoding="utf-8")
    workflow = DESTINATION / ".github/workflows/validate.yml"
    workflow.parent.mkdir(parents=True)
    workflow.write_text(WORKFLOW, encoding="utf-8")
    # Rebuild the per-problem report for the public copy, where no personal drafts exist.
    subprocess.run([sys.executable, "-B", "review_bank.py", "--write"],
                   cwd=DESTINATION, check=True, stdout=subprocess.DEVNULL)
    print(f"release={DESTINATION}")
    print(f"starter_problems={sum(len(group) for group in builds.values())}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    export()
