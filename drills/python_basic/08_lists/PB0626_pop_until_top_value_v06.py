"""
PB0626 — 맨 위가 목표값일 때까지 꺼내기

Chapter: Lists
Topic: List Pop
Seed: 63 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: pop_call

문제
----
복사본의 마지막 값이 target이거나 리스트가 빌 때까지 pop하고, 제거값을 pop된 순서로 함께 반환한다.

연습 초점
---------
스택의 top을 반복 검사하며 조건이 충족될 때 루프를 멈춘다.

구현할 함수
-----------
def pop_until_top(values: list[int], target: int) -> tuple[list[int], list[int]]:

필수 구현 방식
--------------
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3, 4]), pop_until_top(items, 2) == ([1, 2], [4, 3]) and items == [1, 2, 3, 4])[-1] is True
- pop_until_top([1, 2], 9) == ([], [2, 1])
- pop_until_top([], 1) == ([], [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0626 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def pop_until_top(values: list[int], target: int) -> tuple[list[int], list[int]]:
    raise NotImplementedError("TODO: PB0626")


def self_test() -> None:
    assert ((items := [1, 2, 3, 4]), pop_until_top(items, 2) == ([1, 2], [4, 3]) and items == [1, 2, 3, 4])[-1] is True
    assert pop_until_top([1, 2], 9) == ([], [2, 1])
    assert pop_until_top([], 1) == ([], [])
