"""
PB0216 — 플래그 목록 반전

Chapter: Math
Topic: Boolean Negation
Seed: 22 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: bool_not

문제
----
각 flag에 not을 적용한 새 리스트를 반환하세요.

연습 초점
---------
반복되는 논리 부정

구현할 함수
-----------
def invert_flags(flags: list[bool]) -> list[bool]:

필수 구현 방식
--------------
- 논리 연산자 not을 사용한다.

예시 및 필수 테스트
-------------------
- invert_flags([True, False]) == [False, True]
- invert_flags([]) == []
- invert_flags([False]) == [True]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0216 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def invert_flags(flags: list[bool]) -> list[bool]:
    raise NotImplementedError("TODO: PB0216")


def self_test() -> None:
    assert invert_flags([True, False]) == [False, True]
    assert invert_flags([]) == []
    assert invert_flags([False]) == [True]
