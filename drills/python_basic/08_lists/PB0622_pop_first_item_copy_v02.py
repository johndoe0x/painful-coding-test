"""
PB0622 — 복사본의 첫 원소 꺼내기

Chapter: Lists
Topic: List Pop
Seed: 63 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: pop_call

문제
----
values는 변경하지 않고 복사본의 첫 원소를 pop해 (남은 리스트, 제거값)으로 반환하며 빈 리스트는 ([], None)이다.

연습 초점
---------
pop(0)의 결과와 복사본 상태를 함께 반환한다.

구현할 함수
-----------
def pop_first(values: list[int]) -> tuple[list[int], int | None]:

필수 구현 방식
--------------
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3]), pop_first(items) == ([2, 3], 1) and items == [1, 2, 3])[-1] is True
- pop_first([8]) == ([], 8)
- pop_first([]) == ([], None)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0622 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def pop_first(values: list[int]) -> tuple[list[int], int | None]:
    raise NotImplementedError("TODO: PB0622")


def self_test() -> None:
    assert ((items := [1, 2, 3]), pop_first(items) == ([2, 3], 1) and items == [1, 2, 3])[-1] is True
    assert pop_first([8]) == ([], 8)
    assert pop_first([]) == ([], None)
