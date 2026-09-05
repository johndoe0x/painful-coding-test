"""
PB0682 — 첫 중복값 찾기

Chapter: Sets
Topic: Set Practice
Seed: 69 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
왼쪽부터 보며 두 번째로 등장하는 순간의 값을 반환하고 중복이 없으면 None을 반환한다.

연습 초점
---------
seen membership와 조기 반환

구현할 함수
-----------
def set_first_duplicate(values: list[str]) -> str | None:

예시 및 필수 테스트
-------------------
- set_first_duplicate(['a', 'b', 'a', 'b']) == 'a'
- set_first_duplicate(['a', 'b']) is None
- set_first_duplicate([]) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0682 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_first_duplicate(values: list[str]) -> str | None:
    raise NotImplementedError("TODO: PB0682")


def self_test() -> None:
    assert set_first_duplicate(['a', 'b', 'a', 'b']) == 'a'
    assert set_first_duplicate(['a', 'b']) is None
    assert set_first_duplicate([]) is None
