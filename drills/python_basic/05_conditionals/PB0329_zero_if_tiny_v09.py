"""
PB0329 — 작은 절댓값을 0으로

Chapter: Conditional Statements
Topic: If Statements
Seed: 33 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: if

문제
----
value를 그대로 두되 절댓값이 0.01 미만이면 0.0을 반환한다.

연습 초점
---------
엄격한 경계 비교를 단일 if로 처리

구현할 함수
-----------
def zero_if_tiny(value: float) -> float:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- zero_if_tiny(0.001) == 0.0
- zero_if_tiny(0.01) == 0.01
- zero_if_tiny(-2.5) == -2.5

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0329 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def zero_if_tiny(value: float) -> float:
    raise NotImplementedError("TODO: PB0329")


def self_test() -> None:
    assert zero_if_tiny(0.001) == 0.0
    assert zero_if_tiny(0.01) == 0.01
    assert zero_if_tiny(-2.5) == -2.5
