"""
PB0625 — 마지막 원소 여러 개 꺼내기

Chapter: Lists
Topic: List Pop
Seed: 63 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: pop_call

문제
----
0 <= count <= len(values)라고 가정해 복사본에서 마지막 원소를 count번 pop하고, 제거값들은 실제 pop된 순서로 반환한다.

연습 초점
---------
반복되는 pop이 뒤에서 앞으로 값을 꺼내는 순서를 확인한다.

구현할 함수
-----------
def pop_last_n(values: list[int], count: int) -> tuple[list[int], list[int]]:

필수 구현 방식
--------------
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3, 4]), pop_last_n(items, 2) == ([1, 2], [4, 3]) and items == [1, 2, 3, 4])[-1] is True
- pop_last_n([5], 1) == ([], [5])
- pop_last_n([1, 2], 0) == ([1, 2], [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0625 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def pop_last_n(values: list[int], count: int) -> tuple[list[int], list[int]]:
    raise NotImplementedError("TODO: PB0625")


def self_test() -> None:
    assert ((items := [1, 2, 3, 4]), pop_last_n(items, 2) == ([1, 2], [4, 3]) and items == [1, 2, 3, 4])[-1] is True
    assert pop_last_n([5], 1) == ([], [5])
    assert pop_last_n([1, 2], 0) == ([1, 2], [])
