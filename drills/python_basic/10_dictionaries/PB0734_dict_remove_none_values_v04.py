"""
PB0734 — None value 제거

Chapter: Dictionaries
Topic: Dict Remove
Seed: 74 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
value가 None인 item만 제거한다. 0, False, 빈 문자열은 유지한다.

연습 초점
---------
None identity 검사와 필터링

구현할 함수
-----------
def dict_remove_none_values(mapping: dict[str, object | None]) -> dict[str, object]:

예시 및 필수 테스트
-------------------
- dict_remove_none_values({'a': 1, 'b': None}) == {'a': 1}
- dict_remove_none_values({}) == {}
- dict_remove_none_values({'zero': 0, 'false': False, 'empty': ''}) == {'zero': 0, 'false': False, 'empty': ''}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0734 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_remove_none_values(mapping: dict[str, object | None]) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0734")


def self_test() -> None:
    assert dict_remove_none_values({'a': 1, 'b': None}) == {'a': 1}
    assert dict_remove_none_values({}) == {}
    assert dict_remove_none_values({'zero': 0, 'false': False, 'empty': ''}) == {'zero': 0, 'false': False, 'empty': ''}
