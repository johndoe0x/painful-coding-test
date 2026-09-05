"""
PB0569 — 재고 상태 한 줄

Chapter: Strings
Topic: Strings Formatting
Seed: 57 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: f_string

문제
----
stock이 0보다 크면 '<item>: <stock> left', 아니면 '<item>: out of stock'을 반환한다.

연습 초점
---------
조건으로 고른 값을 f-string의 일정한 접두사와 결합한다.

구현할 함수
-----------
def format_inventory(item: str, stock: int) -> str:

필수 구현 방식
--------------
- f-string을 사용한다.

예시 및 필수 테스트
-------------------
- format_inventory('pen', 3) == 'pen: 3 left'
- format_inventory('book', 0) == 'book: out of stock'
- format_inventory('', 1) == ': 1 left'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0569 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_inventory(item: str, stock: int) -> str:
    raise NotImplementedError("TODO: PB0569")


def self_test() -> None:
    assert format_inventory('pen', 3) == 'pen: 3 left'
    assert format_inventory('book', 0) == 'book: out of stock'
    assert format_inventory('', 1) == ': 1 left'
