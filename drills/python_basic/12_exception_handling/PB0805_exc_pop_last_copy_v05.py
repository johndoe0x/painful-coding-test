"""
PB0805 — 빈 리스트 안전 pop

Chapter: Exception Handling
Topic: Error Catching
Seed: 81 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: try

문제
----
원본을 복사한 뒤 pop한 결과 리스트와 제거값을 반환한다. 비어 있어 IndexError면 ([], None)을 반환한다.

연습 초점
---------
복사본 mutation과 IndexError 처리

구현할 함수
-----------
def exc_pop_last_copy(values: list[int]) -> tuple[list[int], int | None]:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- ((items := [1, 2]), exc_pop_last_copy(items) == ([1], 2) and items == [1, 2])[-1] is True
- exc_pop_last_copy([]) == ([], None)
- exc_pop_last_copy([-1]) == ([], -1)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0805 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_pop_last_copy(values: list[int]) -> tuple[list[int], int | None]:
    raise NotImplementedError("TODO: PB0805")


def self_test() -> None:
    assert ((items := [1, 2]), exc_pop_last_copy(items) == ([1], 2) and items == [1, 2])[-1] is True
    assert exc_pop_last_copy([]) == ([], None)
    assert exc_pop_last_copy([-1]) == ([], -1)
