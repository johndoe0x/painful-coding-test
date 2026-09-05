"""
PB0714 — 접두사 key의 값 합계

Chapter: Dictionaries
Topic: Dict Looping
Seed: 72 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: for, dict_items_call

문제
----
prefix로 시작하는 key들의 value 합계를 반환한다.

연습 초점
---------
key 조건 검사와 value 누적

구현할 함수
-----------
def dict_sum_for_prefix(mapping: dict[str, int], prefix: str) -> int:

필수 구현 방식
--------------
- for문을 사용한다.
- dict.items()를 사용한다.

예시 및 필수 테스트
-------------------
- dict_sum_for_prefix({'app': 2, 'api': 3, 'web': 4}, 'ap') == 5
- dict_sum_for_prefix({}, 'a') == 0
- dict_sum_for_prefix({'a': 1, 'b': 2}, '') == 3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0714 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_sum_for_prefix(mapping: dict[str, int], prefix: str) -> int:
    raise NotImplementedError("TODO: PB0714")


def self_test() -> None:
    assert dict_sum_for_prefix({'app': 2, 'api': 3, 'web': 4}, 'ap') == 5
    assert dict_sum_for_prefix({}, 'a') == 0
    assert dict_sum_for_prefix({'a': 1, 'b': 2}, '') == 3
