"""
PB0561 — 영수증 한 줄 만들기

Chapter: Strings
Topic: Strings Formatting
Seed: 57 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: f_string

문제
----
총액 quantity * price를 소수점 둘째 자리까지 표시해 '<item> x<quantity> = <total>' 형식으로 반환한다.

연습 초점
---------
f-string 안에서 계산값과 소수점 형식 지정자를 사용한다.

구현할 함수
-----------
def format_receipt(item: str, quantity: int, price: float) -> str:

필수 구현 방식
--------------
- f-string을 사용한다.

예시 및 필수 테스트
-------------------
- format_receipt('pen', 2, 1.5) == 'pen x2 = 3.00'
- format_receipt('book', 1, 12.0) == 'book x1 = 12.00'
- format_receipt('free', 3, 0.0) == 'free x3 = 0.00'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0561 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_receipt(item: str, quantity: int, price: float) -> str:
    raise NotImplementedError("TODO: PB0561")


def self_test() -> None:
    assert format_receipt('pen', 2, 1.5) == 'pen x2 = 3.00'
    assert format_receipt('book', 1, 12.0) == 'book x1 = 12.00'
    assert format_receipt('free', 3, 0.0) == 'free x3 = 0.00'
