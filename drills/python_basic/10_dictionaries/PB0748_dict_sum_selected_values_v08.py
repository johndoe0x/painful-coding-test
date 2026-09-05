"""
PB0748 — 선택 key의 value 합계

Chapter: Dictionaries
Topic: Dict Values
Seed: 75 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
keys 중 mapping에 존재하는 key의 value만 합한다. 같은 key가 keys에 반복되면 반복해서 더한다.

연습 초점
---------
membership와 선택 조회 누적

구현할 함수
-----------
def dict_sum_selected_values(mapping: dict[str, int], keys: list[str]) -> int:

예시 및 필수 테스트
-------------------
- dict_sum_selected_values({'a': 2, 'b': 3}, ['a', 'x']) == 2
- dict_sum_selected_values({}, ['a']) == 0
- dict_sum_selected_values({'a': 2}, ['a', 'a']) == 4

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0748 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_sum_selected_values(mapping: dict[str, int], keys: list[str]) -> int:
    raise NotImplementedError("TODO: PB0748")


def self_test() -> None:
    assert dict_sum_selected_values({'a': 2, 'b': 3}, ['a', 'x']) == 2
    assert dict_sum_selected_values({}, ['a']) == 0
    assert dict_sum_selected_values({'a': 2}, ['a', 'a']) == 4
