"""
PB0676 — Jaccard 유사도

Chapter: Sets
Topic: Set Operations
Seed: 68 / 82
Variant: 06 / 10
Time cap: 150 seconds
Source checks:

문제
----
합집합이 비면 1.0, 아니면 교집합 크기를 합집합 크기로 나눈 값을 반환한다.

연습 초점
---------
교집합·합집합 크기와 나눗셈

구현할 함수
-----------
def set_jaccard_score(left: set[str], right: set[str]) -> float:

예시 및 필수 테스트
-------------------
- set_jaccard_score({'a', 'b'}, {'b', 'c'}) == 1 / 3
- set_jaccard_score(set(), set()) == 1.0
- set_jaccard_score({'x'}, {'x'}) == 1.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0676 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_jaccard_score(left: set[str], right: set[str]) -> float:
    raise NotImplementedError("TODO: PB0676")


def self_test() -> None:
    assert set_jaccard_score({'a', 'b'}, {'b', 'c'}) == 1 / 3
    assert set_jaccard_score(set(), set()) == 1.0
    assert set_jaccard_score({'x'}, {'x'}) == 1.0
