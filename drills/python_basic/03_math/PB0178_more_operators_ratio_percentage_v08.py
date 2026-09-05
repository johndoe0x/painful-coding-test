"""
PB0178 — 비율을 백분율로

Chapter: Math
Topic: More Operators
Seed: 18 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
whole이 0이 아닐 때 part / whole * 100을 반환하세요.

연습 초점
---------
실수 나눗셈과 배율 변환

구현할 함수
-----------
def ratio_percentage(part: float, whole: float) -> float:

예시 및 필수 테스트
-------------------
- ratio_percentage(1, 4) == 25.0
- ratio_percentage(0, 5) == 0.0
- ratio_percentage(5, 5) == 100.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0178 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def ratio_percentage(part: float, whole: float) -> float:
    raise NotImplementedError("TODO: PB0178")


def self_test() -> None:
    assert ratio_percentage(1, 4) == 25.0
    assert ratio_percentage(0, 5) == 0.0
    assert ratio_percentage(5, 5) == 100.0
