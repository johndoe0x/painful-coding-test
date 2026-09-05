"""
PB0739 — 중복 value의 뒤쪽 item 제거

Chapter: Dictionaries
Topic: Dict Remove
Seed: 74 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
같은 value가 여러 번 나오면 첫 item만 남긴다.

연습 초점
---------
seen value set과 순서 보존

구현할 함수
-----------
def dict_remove_duplicate_values(mapping: dict[str, int]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- dict_remove_duplicate_values({'a': 1, 'b': 2, 'c': 1}) == {'a': 1, 'b': 2}
- dict_remove_duplicate_values({}) == {}
- dict_remove_duplicate_values({'x': 0}) == {'x': 0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0739 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_remove_duplicate_values(mapping: dict[str, int]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0739")


def self_test() -> None:
    assert dict_remove_duplicate_values({'a': 1, 'b': 2, 'c': 1}) == {'a': 1, 'b': 2}
    assert dict_remove_duplicate_values({}) == {}
    assert dict_remove_duplicate_values({'x': 0}) == {'x': 0}
