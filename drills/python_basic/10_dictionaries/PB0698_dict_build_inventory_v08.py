"""
PB0698 — 상품 재고 만들기

Chapter: Dictionaries
Topic: Intro to Dictionaries
Seed: 70 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
같은 인덱스의 name과 quantity를 연결한다. 두 리스트의 길이는 같다고 가정한다.

연습 초점
---------
zip을 이용한 딕셔너리 생성

구현할 함수
-----------
def dict_build_inventory(names: list[str], quantities: list[int]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- dict_build_inventory(['pen', 'book'], [3, 2]) == {'pen': 3, 'book': 2}
- dict_build_inventory([], []) == {}
- dict_build_inventory(['x'], [0]) == {'x': 0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0698 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_build_inventory(names: list[str], quantities: list[int]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0698")


def self_test() -> None:
    assert dict_build_inventory(['pen', 'book'], [3, 2]) == {'pen': 3, 'book': 2}
    assert dict_build_inventory([], []) == {}
    assert dict_build_inventory(['x'], [0]) == {'x': 0}
