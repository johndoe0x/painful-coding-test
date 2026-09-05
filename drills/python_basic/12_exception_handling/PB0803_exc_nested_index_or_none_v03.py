"""
PB0803 — 중첩 리스트 안전 조회

Chapter: Exception Handling
Topic: Error Catching
Seed: 81 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: try

문제
----
matrix[row][column]을 반환하고 어느 단계에서든 IndexError가 나면 None을 반환한다.

연습 초점
---------
한 표현식의 여러 IndexError 지점 처리

구현할 함수
-----------
def exc_nested_index_or_none(matrix: list[list[int]], row: int, column: int) -> int | None:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_nested_index_or_none([[1, 2], [3]], 0, 1) == 2
- exc_nested_index_or_none([[1]], 2, 0) is None
- exc_nested_index_or_none([[1]], 0, 2) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0803 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_nested_index_or_none(matrix: list[list[int]], row: int, column: int) -> int | None:
    raise NotImplementedError("TODO: PB0803")


def self_test() -> None:
    assert exc_nested_index_or_none([[1, 2], [3]], 0, 1) == 2
    assert exc_nested_index_or_none([[1]], 2, 0) is None
    assert exc_nested_index_or_none([[1]], 0, 2) is None
