"""
PB0457 — 중첩 for 행렬 펼치기

Chapter: Loops
Topic: Nested Loops
Seed: 46 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: nested_loop

문제
----
바깥 for로 행을, 안쪽 for로 원소를 순회해 한 리스트로 반환한다.

연습 초점
---------
중첩 컬렉션의 이중 순회

구현할 함수
-----------
def flatten_matrix_nested(matrix: list[list[int]]) -> list[int]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- flatten_matrix_nested([[1, 2], [], [3]]) == [1, 2, 3]
- flatten_matrix_nested([]) == []
- flatten_matrix_nested([[-1]]) == [-1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0457 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def flatten_matrix_nested(matrix: list[list[int]]) -> list[int]:
    raise NotImplementedError("TODO: PB0457")


def self_test() -> None:
    assert flatten_matrix_nested([[1, 2], [], [3]]) == [1, 2, 3]
    assert flatten_matrix_nested([]) == []
    assert flatten_matrix_nested([[-1]]) == [-1]
