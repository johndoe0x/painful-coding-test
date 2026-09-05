"""
PB0735 — 기준 미만 value 제거

Chapter: Dictionaries
Topic: Dict Remove
Seed: 74 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
value가 minimum 미만인 item을 제거한 새 딕셔너리를 반환한다.

연습 초점
---------
value 비교를 이용한 제거 필터

구현할 함수
-----------
def dict_remove_below(mapping: dict[str, int], minimum: int) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- dict_remove_below({'a': 1, 'b': 3}, 2) == {'b': 3}
- dict_remove_below({}, 0) == {}
- dict_remove_below({'a': 2}, 2) == {'a': 2}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0735 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_remove_below(mapping: dict[str, int], minimum: int) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0735")


def self_test() -> None:
    assert dict_remove_below({'a': 1, 'b': 3}, 2) == {'b': 3}
    assert dict_remove_below({}, 0) == {}
    assert dict_remove_below({'a': 2}, 2) == {'a': 2}
