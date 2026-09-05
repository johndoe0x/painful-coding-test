"""
PB0257 — 수치 범위 포함

Chapter: Functions
Topic: Multiple Parameters
Seed: 26 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
value가 low 이상 high 이하인지 반환한다.

연습 초점
---------
세 매개변수의 경계 관계

구현할 함수
-----------
def inside_numeric_range(value: float, low: float, high: float) -> bool:

예시 및 필수 테스트
-------------------
- inside_numeric_range(5.0, 1.0, 9.0) is True
- inside_numeric_range(1.0, 1.0, 9.0) is True
- inside_numeric_range(-2.0, -1.0, 3.0) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0257 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def inside_numeric_range(value: float, low: float, high: float) -> bool:
    raise NotImplementedError("TODO: PB0257")


def self_test() -> None:
    assert inside_numeric_range(5.0, 1.0, 9.0) is True
    assert inside_numeric_range(1.0, 1.0, 9.0) is True
    assert inside_numeric_range(-2.0, -1.0, 3.0) is False
