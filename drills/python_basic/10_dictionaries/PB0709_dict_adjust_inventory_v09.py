"""
PB0709 — 재고 변화 적용

Chapter: Dictionaries
Topic: Dict Operations
Seed: 71 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 changes 값을 기존 재고에 더한다. 없는 상품은 0에서 시작하며 원본은 바꾸지 않는다.

연습 초점
---------
두 딕셔너리 조회와 누적 갱신

구현할 함수
-----------
def dict_adjust_inventory(stock: dict[str, int], changes: dict[str, int]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- ((items := {'pen': 3}), (changes := {'pen': -1, 'book': 2}), dict_adjust_inventory(items, changes) == {'pen': 2, 'book': 2} and items == {'pen': 3} and changes == {'pen': -1, 'book': 2})[-1] is True
- dict_adjust_inventory({}, {}) == {}
- dict_adjust_inventory({'x': 0}, {'x': 0}) == {'x': 0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0709 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_adjust_inventory(stock: dict[str, int], changes: dict[str, int]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0709")


def self_test() -> None:
    assert ((items := {'pen': 3}), (changes := {'pen': -1, 'book': 2}), dict_adjust_inventory(items, changes) == {'pen': 2, 'book': 2} and items == {'pen': 3} and changes == {'pen': -1, 'book': 2})[-1] is True
    assert dict_adjust_inventory({}, {}) == {}
    assert dict_adjust_inventory({'x': 0}, {'x': 0}) == {'x': 0}
