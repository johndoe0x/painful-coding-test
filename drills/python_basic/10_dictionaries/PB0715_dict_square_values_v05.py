"""
PB0715 — 모든 value 제곱

Chapter: Dictionaries
Topic: Dict Looping
Seed: 72 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: for, dict_items_call

문제
----
같은 key를 유지하며 각 value를 제곱한 새 딕셔너리를 반환한다.

연습 초점
---------
dict comprehension의 key-value 변환

구현할 함수
-----------
def dict_square_values(mapping: dict[str, int]) -> dict[str, int]:

필수 구현 방식
--------------
- for문을 사용한다.
- dict.items()를 사용한다.

예시 및 필수 테스트
-------------------
- dict_square_values({'a': 2, 'b': -3}) == {'a': 4, 'b': 9}
- dict_square_values({}) == {}
- dict_square_values({'z': 0}) == {'z': 0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0715 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_square_values(mapping: dict[str, int]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0715")


def self_test() -> None:
    assert dict_square_values({'a': 2, 'b': -3}) == {'a': 4, 'b': 9}
    assert dict_square_values({}) == {}
    assert dict_square_values({'z': 0}) == {'z': 0}
