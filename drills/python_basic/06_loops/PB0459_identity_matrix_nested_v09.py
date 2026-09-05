"""
PB0459 — 단위 행렬

Chapter: Loops
Topic: Nested Loops
Seed: 46 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: nested_loop

문제
----
중첩 for로 행과 열 인덱스가 같으면 1, 다르면 0인 size×size 행렬을 반환한다.

연습 초점
---------
중첩 좌표의 동등 비교

구현할 함수
-----------
def identity_matrix_nested(size: int) -> list[list[int]]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- identity_matrix_nested(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
- identity_matrix_nested(0) == []
- identity_matrix_nested(1) == [[1]]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0459 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def identity_matrix_nested(size: int) -> list[list[int]]:
    raise NotImplementedError("TODO: PB0459")


def self_test() -> None:
    assert identity_matrix_nested(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert identity_matrix_nested(0) == []
    assert identity_matrix_nested(1) == [[1]]
