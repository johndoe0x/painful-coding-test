"""
PB0793 — 문자열 정수 나눗셈

Chapter: Exception Handling
Topic: Try Except
Seed: 80 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: try

문제
----
두 문자열을 int로 바꿔 나눈다. ValueError 또는 ZeroDivisionError가 나면 None을 반환한다.

연습 초점
---------
하나의 try에서 여러 실패 가능성 처리

구현할 함수
-----------
def exc_divide_text_or_none(left: str, right: str) -> float | None:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_divide_text_or_none('6', '2') == 3.0
- exc_divide_text_or_none('x', '2') is None
- exc_divide_text_or_none('1', '0') is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0793 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_divide_text_or_none(left: str, right: str) -> float | None:
    raise NotImplementedError("TODO: PB0793")


def self_test() -> None:
    assert exc_divide_text_or_none('6', '2') == 3.0
    assert exc_divide_text_or_none('x', '2') is None
    assert exc_divide_text_or_none('1', '0') is None
