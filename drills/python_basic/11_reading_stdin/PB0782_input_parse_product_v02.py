"""
PB0782 — 상품·수량·가격 레코드

Chapter: Reading Stdin
Topic: Read Input Practice
Seed: 79 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
공백 구분 item, quantity, price를 각각 str, int, float로 변환해 딕셔너리로 반환한다.

연습 초점
---------
구조화된 한 줄을 typed record로 변환

구현할 함수
-----------
def input_parse_product(line: str) -> dict[str, object]:

예시 및 필수 테스트
-------------------
- input_parse_product('pen 2 1.5') == {'item': 'pen', 'quantity': 2, 'price': 1.5}
- input_parse_product('x 0 0') == {'item': 'x', 'quantity': 0, 'price': 0.0}
- input_parse_product('book 1 10.25') == {'item': 'book', 'quantity': 1, 'price': 10.25}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0782 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_product(line: str) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0782")


def self_test() -> None:
    assert input_parse_product('pen 2 1.5') == {'item': 'pen', 'quantity': 2, 'price': 1.5}
    assert input_parse_product('x 0 0') == {'item': 'x', 'quantity': 0, 'price': 0.0}
    assert input_parse_product('book 1 10.25') == {'item': 'book', 'quantity': 1, 'price': 10.25}
