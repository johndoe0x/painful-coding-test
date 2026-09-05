# Python Coding Drills

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
