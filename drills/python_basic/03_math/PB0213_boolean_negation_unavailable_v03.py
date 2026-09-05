"""
PB0213 — 꺼진 플래그 위치

Chapter: Math
Topic: Boolean Negation
Seed: 22 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: bool_not

문제
----
flags에서 False인 원소의 0부터 시작하는 인덱스를 원래 순서로 반환하세요. not으로 각 플래그의 부정을 검사하세요.

연습 초점
---------
not 조건으로 값 대신 위치를 선택하기

구현할 함수
-----------
def inactive_indices(flags: list[bool]) -> list[int]:

필수 구현 방식
--------------
- 논리 연산자 not을 사용한다.

예시 및 필수 테스트
-------------------
- inactive_indices([True, False, True, False]) == [1, 3]
- inactive_indices([]) == []
- inactive_indices([False, False]) == [0, 1] and inactive_indices([True]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0213 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def inactive_indices(flags: list[bool]) -> list[int]:
    raise NotImplementedError("TODO: PB0213")


def self_test() -> None:
    assert inactive_indices([True, False, True, False]) == [1, 3]
    assert inactive_indices([]) == []
    assert inactive_indices([False, False]) == [0, 1] and inactive_indices([True]) == []
