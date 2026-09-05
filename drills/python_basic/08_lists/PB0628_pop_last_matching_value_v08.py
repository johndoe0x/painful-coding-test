"""
PB0628 — 마지막으로 등장한 목표값 꺼내기

Chapter: Lists
Topic: List Pop
Seed: 63 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: pop_call

문제
----
target의 마지막 등장 위치를 복사본에서 pop해 반환하고, 없으면 복사본과 None을 반환한다.

연습 초점
---------
뒤쪽부터 위치를 찾은 뒤 pop(index)로 한 원소만 제거한다.

구현할 함수
-----------
def pop_last_occurrence(values: list[int], target: int) -> tuple[list[int], int | None]:

필수 구현 방식
--------------
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 1, 3]), pop_last_occurrence(items, 1) == ([1, 2, 3], 1) and items == [1, 2, 1, 3])[-1] is True
- pop_last_occurrence([4, 5], 9) == ([4, 5], None)
- pop_last_occurrence([], 1) == ([], None)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0628 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def pop_last_occurrence(values: list[int], target: int) -> tuple[list[int], int | None]:
    raise NotImplementedError("TODO: PB0628")


def self_test() -> None:
    assert ((items := [1, 2, 1, 3]), pop_last_occurrence(items, 1) == ([1, 2, 3], 1) and items == [1, 2, 1, 3])[-1] is True
    assert pop_last_occurrence([4, 5], 9) == ([4, 5], None)
    assert pop_last_occurrence([], 1) == ([], None)
