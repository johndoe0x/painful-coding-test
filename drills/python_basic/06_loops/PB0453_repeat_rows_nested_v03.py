"""
PB0453 — 값별 반복 행

Chapter: Loops
Topic: Nested Loops
Seed: 46 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: nested_loop

문제
----
바깥 for로 값을, 안쪽 for로 width번 반복해 각 값으로 채운 행을 반환한다.

연습 초점
---------
입력 원소별 내부 반복

구현할 함수
-----------
def repeat_rows_nested(values: list[int], width: int) -> list[list[int]]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- repeat_rows_nested([2, 3], 3) == [[2, 2, 2], [3, 3, 3]]
- repeat_rows_nested([], 2) == []
- repeat_rows_nested([1], 0) == [[]]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0453 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def repeat_rows_nested(values: list[int], width: int) -> list[list[int]]:
    raise NotImplementedError("TODO: PB0453")


def self_test() -> None:
    assert repeat_rows_nested([2, 3], 3) == [[2, 2, 2], [3, 3, 3]]
    assert repeat_rows_nested([], 2) == []
    assert repeat_rows_nested([1], 0) == [[]]
