"""
PB0745 — value 배율 적용

Chapter: Dictionaries
Topic: Dict Values
Seed: 75 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 value에 factor를 곱한 새 딕셔너리를 반환한다.

연습 초점
---------
values 변환 dict comprehension

구현할 함수
-----------
def dict_scale_values(mapping: dict[str, float], factor: float) -> dict[str, float]:

예시 및 필수 테스트
-------------------
- dict_scale_values({'a': 2.0, 'b': -1.0}, 0.5) == {'a': 1.0, 'b': -0.5}
- dict_scale_values({}, 2.0) == {}
- dict_scale_values({'x': 3.0}, 0.0) == {'x': 0.0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0745 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_scale_values(mapping: dict[str, float], factor: float) -> dict[str, float]:
    raise NotImplementedError("TODO: PB0745")


def self_test() -> None:
    assert dict_scale_values({'a': 2.0, 'b': -1.0}, 0.5) == {'a': 1.0, 'b': -0.5}
    assert dict_scale_values({}, 2.0) == {}
    assert dict_scale_values({'x': 3.0}, 0.0) == {'x': 0.0}
