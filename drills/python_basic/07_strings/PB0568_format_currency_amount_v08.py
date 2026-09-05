"""
PB0568 — 통화 금액 표시하기

Chapter: Strings
Topic: Strings Formatting
Seed: 57 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: f_string

문제
----
symbol 뒤에 amount를 천 단위 쉼표와 소수점 둘째 자리까지 표시한다.

연습 초점
---------
숫자 형식 지정자의 그룹 구분과 정밀도를 함께 사용한다.

구현할 함수
-----------
def format_currency(symbol: str, amount: float) -> str:

필수 구현 방식
--------------
- f-string을 사용한다.

예시 및 필수 테스트
-------------------
- format_currency('$', 1234.5) == '$1,234.50'
- format_currency('₩', 0) == '₩0.00'
- format_currency('€', -12.3) == '€-12.30'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0568 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_currency(symbol: str, amount: float) -> str:
    raise NotImplementedError("TODO: PB0568")


def self_test() -> None:
    assert format_currency('$', 1234.5) == '$1,234.50'
    assert format_currency('₩', 0) == '₩0.00'
    assert format_currency('€', -12.3) == '€-12.30'
