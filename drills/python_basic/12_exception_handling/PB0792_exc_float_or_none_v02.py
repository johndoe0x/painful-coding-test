"""
PB0792 — 실수 변환 실패 None

Chapter: Exception Handling
Topic: Try Except
Seed: 80 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: try

문제
----
float 변환에 성공하면 값, ValueError면 None을 반환한다.

연습 초점
---------
성공 경로와 예외 경로 반환 분리

구현할 함수
-----------
def exc_float_or_none(text: str) -> float | None:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_float_or_none('3.5') == 3.5
- exc_float_or_none('bad') is None
- exc_float_or_none(' 0 ') == 0.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0792 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_float_or_none(text: str) -> float | None:
    raise NotImplementedError("TODO: PB0792")


def self_test() -> None:
    assert exc_float_or_none('3.5') == 3.5
    assert exc_float_or_none('bad') is None
    assert exc_float_or_none(' 0 ') == 0.0
