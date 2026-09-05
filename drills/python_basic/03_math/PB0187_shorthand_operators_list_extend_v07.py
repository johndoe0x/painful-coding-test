"""
PB0187 — +=로 리스트 확장

Chapter: Math
Topic: Shorthand Operators
Seed: 19 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: augassign

문제
----
start의 복사본에 각 chunk를 +=로 확장해 반환하세요.

연습 초점
---------
리스트 +=와 원본 보존

구현할 함수
-----------
def extend_in_chunks(start: list[int], chunks: list[list[int]]) -> list[int]:

필수 구현 방식
--------------
- +=, -=, *= 같은 복합 할당 연산자를 사용한다.

예시 및 필수 테스트
-------------------
- ((items := [1]), (chunks := [[2, 3], [4]]), extend_in_chunks(items, chunks) == [1, 2, 3, 4] and items == [1] and chunks == [[2, 3], [4]])[-1] is True
- extend_in_chunks([], []) == []
- extend_in_chunks([0], [[]]) == [0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0187 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def extend_in_chunks(start: list[int], chunks: list[list[int]]) -> list[int]:
    raise NotImplementedError("TODO: PB0187")


def self_test() -> None:
    assert ((items := [1]), (chunks := [[2, 3], [4]]), extend_in_chunks(items, chunks) == [1, 2, 3, 4] and items == [1] and chunks == [[2, 3], [4]])[-1] is True
    assert extend_in_chunks([], []) == []
    assert extend_in_chunks([0], [[]]) == [0]
