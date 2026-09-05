"""
PB0666 — 후보 값 추가

Chapter: Sets
Topic: Intro to Sets
Seed: 67 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
원본 values를 바꾸지 않고 candidate를 포함한 새 set을 반환한다.

연습 초점
---------
set 복사와 add

구현할 함수
-----------
def set_add_candidate(values: set[int], candidate: int) -> set[int]:

예시 및 필수 테스트
-------------------
- ((items := {1, 2}), set_add_candidate(items, 3) == {1, 2, 3} and items == {1, 2})[-1] is True
- set_add_candidate({1, 2}, 2) == {1, 2}
- set_add_candidate(set(), 0) == {0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0666 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_add_candidate(values: set[int], candidate: int) -> set[int]:
    raise NotImplementedError("TODO: PB0666")


def self_test() -> None:
    assert ((items := {1, 2}), set_add_candidate(items, 3) == {1, 2, 3} and items == {1, 2})[-1] is True
    assert set_add_candidate({1, 2}, 2) == {1, 2}
    assert set_add_candidate(set(), 0) == {0}
