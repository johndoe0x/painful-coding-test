"""
PB0746 — 모든 value 양수 검사

Chapter: Dictionaries
Topic: Dict Values
Seed: 75 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
모든 value가 0보다 크면 True를 반환한다. 빈 딕셔너리는 True다.

연습 초점
---------
values와 all

구현할 함수
-----------
def dict_all_values_positive(mapping: dict[str, int]) -> bool:

예시 및 필수 테스트
-------------------
- dict_all_values_positive({'a': 1, 'b': 2}) is True
- dict_all_values_positive({'a': 0}) is False
- dict_all_values_positive({}) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0746 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_all_values_positive(mapping: dict[str, int]) -> bool:
    raise NotImplementedError("TODO: PB0746")


def self_test() -> None:
    assert dict_all_values_positive({'a': 1, 'b': 2}) is True
    assert dict_all_values_positive({'a': 0}) is False
    assert dict_all_values_positive({}) is True
