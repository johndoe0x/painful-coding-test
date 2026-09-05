"""
PB0262 — 첫 음수 조기 반환

Chapter: Functions
Topic: Return Statement
Seed: 27 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
앞에서부터 찾아 첫 음수를 즉시 반환하고, 없으면 None을 반환한다.

연습 초점
---------
조건 충족 시 조기 return

구현할 함수
-----------
def first_negative_or_none(numbers: list[int]) -> int | None:

예시 및 필수 테스트
-------------------
- first_negative_or_none([3, -2, -5]) == -2
- first_negative_or_none([0, 4]) is None
- first_negative_or_none([-1]) == -1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0262 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_negative_or_none(numbers: list[int]) -> int | None:
    raise NotImplementedError("TODO: PB0262")


def self_test() -> None:
    assert first_negative_or_none([3, -2, -5]) == -2
    assert first_negative_or_none([0, 4]) is None
    assert first_negative_or_none([-1]) == -1
