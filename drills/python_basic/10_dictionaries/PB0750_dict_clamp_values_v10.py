"""
PB0750 — value 범위 제한

Chapter: Dictionaries
Topic: Dict Values
Seed: 75 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 value를 low 이상 high 이하로 제한한 새 딕셔너리를 반환한다. low<=high라고 가정한다.

연습 초점
---------
min과 max를 조합한 value 변환

구현할 함수
-----------
def dict_clamp_values(mapping: dict[str, int], low: int, high: int) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- dict_clamp_values({'a': -1, 'b': 5, 'c': 20}, 0, 10) == {'a': 0, 'b': 5, 'c': 10}
- dict_clamp_values({}, 0, 1) == {}
- dict_clamp_values({'x': 3}, 3, 3) == {'x': 3}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0750 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_clamp_values(mapping: dict[str, int], low: int, high: int) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0750")


def self_test() -> None:
    assert dict_clamp_values({'a': -1, 'b': 5, 'c': 20}, 0, 10) == {'a': 0, 'b': 5, 'c': 10}
    assert dict_clamp_values({}, 0, 1) == {}
    assert dict_clamp_values({'x': 3}, 3, 3) == {'x': 3}
