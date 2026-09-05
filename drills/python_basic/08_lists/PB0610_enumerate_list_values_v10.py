"""
PB0610 — 인덱스와 원소 묶기

Chapter: Lists
Topic: List Functions
Seed: 61 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
enumerate의 start 값을 적용해 각 문자열을 번호와 묶은 리스트로 반환한다.

연습 초점
---------
enumerate 객체를 구체적인 tuple 리스트로 변환한다.

구현할 함수
-----------
def enumerate_values(values: list[str], start: int = 0) -> list[tuple[int, str]]:

예시 및 필수 테스트
-------------------
- enumerate_values(['a', 'b']) == [(0, 'a'), (1, 'b')]
- enumerate_values(['x', 'y'], 1) == [(1, 'x'), (2, 'y')]
- enumerate_values([], 5) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0610 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def enumerate_values(values: list[str], start: int = 0) -> list[tuple[int, str]]:
    raise NotImplementedError("TODO: PB0610")


def self_test() -> None:
    assert enumerate_values(['a', 'b']) == [(0, 'a'), (1, 'b')]
    assert enumerate_values(['x', 'y'], 1) == [(1, 'x'), (2, 'y')]
    assert enumerate_values([], 5) == []
