"""
PB0069 — 상품 변수 선언

Chapter: Variables
Topic: Variable Declaration
Seed: 07 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: assignment

문제
----
세 입력과 계산한 total을 각각 변수로 선언해 같은 이름의 키를 가진 딕셔너리로 반환하세요.

연습 초점
---------
여러 입력과 계산 변수 선언

구현할 함수
-----------
def declare_item(name: str, unit_price: float, quantity: int) -> dict[str, object]:

필수 구현 방식
--------------
- 함수 본문에서 지역 변수 할당을 사용한다.

예시 및 필수 테스트
-------------------
- declare_item('pen', 2.5, 4) == {'name': 'pen', 'unit_price': 2.5, 'quantity': 4, 'total': 10.0}
- declare_item('', 0, 0) == {'name': '', 'unit_price': 0, 'quantity': 0, 'total': 0}
- declare_item('x', 3, 1) == {'name': 'x', 'unit_price': 3, 'quantity': 1, 'total': 3}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0069 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def declare_item(name: str, unit_price: float, quantity: int) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0069")


def self_test() -> None:
    assert declare_item('pen', 2.5, 4) == {'name': 'pen', 'unit_price': 2.5, 'quantity': 4, 'total': 10.0}
    assert declare_item('', 0, 0) == {'name': '', 'unit_price': 0, 'quantity': 0, 'total': 0}
    assert declare_item('x', 3, 1) == {'name': 'x', 'unit_price': 3, 'quantity': 1, 'total': 3}
