"""
PB0819 — 나눗셈 결과 메시지

Chapter: Exception Handling
Topic: Multiple Except Blocks
Seed: 82 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: try, multiple_except

문제
----
두 문자열을 float로 바꿔 나눈 결과를 str로 반환한다. ValueError면 'not-a-number', ZeroDivisionError면 'cannot-divide-by-zero'다.

연습 초점
---------
성공값 문자열화와 타입별 오류 메시지

구현할 함수
-----------
def exc_parse_division_message(numerator: str, denominator: str) -> str:

필수 구현 방식
--------------
- try-except를 사용한다.
- 함수 안에 둘 이상의 except 블록을 사용한다.

예시 및 필수 테스트
-------------------
- exc_parse_division_message('5', '2') == '2.5'
- exc_parse_division_message('x', '2') == 'not-a-number'
- exc_parse_division_message('1', '0') == 'cannot-divide-by-zero'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0819 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_parse_division_message(numerator: str, denominator: str) -> str:
    raise NotImplementedError("TODO: PB0819")


def self_test() -> None:
    assert exc_parse_division_message('5', '2') == '2.5'
    assert exc_parse_division_message('x', '2') == 'not-a-number'
    assert exc_parse_division_message('1', '0') == 'cannot-divide-by-zero'
