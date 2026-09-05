"""
PB0263 — 안전한 나눗셈 반환

Chapter: Functions
Topic: Return Statement
Seed: 27 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
분모가 0이면 None을 조기 반환하고 아니면 나눗셈 결과를 반환한다.

연습 초점
---------
가드 절과 최종 return

구현할 함수
-----------
def divide_or_none(numerator: float, denominator: float) -> float | None:

예시 및 필수 테스트
-------------------
- divide_or_none(8.0, 2.0) == 4.0
- divide_or_none(3.0, 0.0) is None
- divide_or_none(-9.0, 3.0) == -3.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0263 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def divide_or_none(numerator: float, denominator: float) -> float | None:
    raise NotImplementedError("TODO: PB0263")


def self_test() -> None:
    assert divide_or_none(8.0, 2.0) == 4.0
    assert divide_or_none(3.0, 0.0) is None
    assert divide_or_none(-9.0, 3.0) == -3.0
