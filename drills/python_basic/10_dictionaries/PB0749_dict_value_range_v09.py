"""
PB0749 — value 최솟값과 최댓값

Chapter: Dictionaries
Topic: Dict Values
Seed: 75 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
비어 있으면 None, 아니면 (최솟값, 최댓값)을 반환한다.

연습 초점
---------
values에 min과 max 적용

구현할 함수
-----------
def dict_value_range(mapping: dict[str, int]) -> tuple[int, int] | None:

예시 및 필수 테스트
-------------------
- dict_value_range({'a': 3, 'b': 1}) == (1, 3)
- dict_value_range({}) is None
- dict_value_range({'x': -2}) == (-2, -2)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0749 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_value_range(mapping: dict[str, int]) -> tuple[int, int] | None:
    raise NotImplementedError("TODO: PB0749")


def self_test() -> None:
    assert dict_value_range({'a': 3, 'b': 1}) == (1, 3)
    assert dict_value_range({}) is None
    assert dict_value_range({'x': -2}) == (-2, -2)
