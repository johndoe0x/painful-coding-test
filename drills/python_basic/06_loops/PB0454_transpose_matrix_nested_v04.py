"""
PB0454 — 행렬 전치

Chapter: Loops
Topic: Nested Loops
Seed: 46 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: nested_loop

문제
----
직사각형 matrix를 중첩 for로 전치하며 빈 matrix나 첫 행이 비면 빈 리스트를 반환한다.

연습 초점
---------
열 바깥·행 안쪽의 중첩 인덱스

구현할 함수
-----------
def transpose_matrix_nested(matrix: list[list[int]]) -> list[list[int]]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- transpose_matrix_nested([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
- transpose_matrix_nested([]) == []
- transpose_matrix_nested([[]]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0454 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def transpose_matrix_nested(matrix: list[list[int]]) -> list[list[int]]:
    raise NotImplementedError("TODO: PB0454")


def self_test() -> None:
    assert transpose_matrix_nested([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose_matrix_nested([]) == []
    assert transpose_matrix_nested([[]]) == []
