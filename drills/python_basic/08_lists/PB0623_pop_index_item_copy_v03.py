"""
PB0623 — 지정 위치 원소 꺼내기

Chapter: Lists
Topic: List Pop
Seed: 63 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: pop_call

문제
----
index가 유효하면 복사본에서 해당 원소를 pop해 남은 리스트와 제거값을 반환하고, 유효하지 않으면 복사본과 None을 반환한다.

연습 초점
---------
양수·음수 인덱스의 유효 범위를 확인한 뒤 pop(index)를 호출한다.

구현할 함수
-----------
def pop_at_index(values: list[int], index: int) -> tuple[list[int], int | None]:

필수 구현 방식
--------------
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- ((items := [10, 20, 30]), pop_at_index(items, 1) == ([10, 30], 20) and items == [10, 20, 30])[-1] is True
- pop_at_index([1, 2], -1) == ([1], 2)
- pop_at_index([1, 2], 5) == ([1, 2], None)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0623 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def pop_at_index(values: list[int], index: int) -> tuple[list[int], int | None]:
    raise NotImplementedError("TODO: PB0623")


def self_test() -> None:
    assert ((items := [10, 20, 30]), pop_at_index(items, 1) == ([10, 30], 20) and items == [10, 20, 30])[-1] is True
    assert pop_at_index([1, 2], -1) == ([1], 2)
    assert pop_at_index([1, 2], 5) == ([1, 2], None)
