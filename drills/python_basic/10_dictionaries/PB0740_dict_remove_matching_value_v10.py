"""
PB0740 — 특정 value 모두 제거

Chapter: Dictionaries
Topic: Dict Remove
Seed: 74 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
value가 target과 같은 item을 모두 제거한다.

연습 초점
---------
value 기준 딕셔너리 필터

구현할 함수
-----------
def dict_remove_matching_value(mapping: dict[str, str], target: str) -> dict[str, str]:

예시 및 필수 테스트
-------------------
- dict_remove_matching_value({'a': 'x', 'b': 'y', 'c': 'x'}, 'x') == {'b': 'y'}
- dict_remove_matching_value({}, 'x') == {}
- dict_remove_matching_value({'a': ''}, '') == {}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0740 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_remove_matching_value(mapping: dict[str, str], target: str) -> dict[str, str]:
    raise NotImplementedError("TODO: PB0740")


def self_test() -> None:
    assert dict_remove_matching_value({'a': 'x', 'b': 'y', 'c': 'x'}, 'x') == {'b': 'y'}
    assert dict_remove_matching_value({}, 'x') == {}
    assert dict_remove_matching_value({'a': ''}, '') == {}
