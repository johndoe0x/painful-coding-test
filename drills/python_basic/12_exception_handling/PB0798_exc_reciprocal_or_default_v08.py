"""
PB0798 — 역수 계산 기본값

Chapter: Exception Handling
Topic: Try Except
Seed: 80 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: try

문제
----
text를 float로 바꿔 역수를 계산한다. 변환 실패 또는 0 나눗셈이면 default를 반환한다.

연습 초점
---------
ValueError와 ZeroDivisionError 동시 처리

구현할 함수
-----------
def exc_reciprocal_or_default(text: str, default: float) -> float:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_reciprocal_or_default('4', -1.0) == 0.25
- exc_reciprocal_or_default('0', -1.0) == -1.0
- exc_reciprocal_or_default('x', 2.0) == 2.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0798 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_reciprocal_or_default(text: str, default: float) -> float:
    raise NotImplementedError("TODO: PB0798")


def self_test() -> None:
    assert exc_reciprocal_or_default('4', -1.0) == 0.25
    assert exc_reciprocal_or_default('0', -1.0) == -1.0
    assert exc_reciprocal_or_default('x', 2.0) == 2.0
