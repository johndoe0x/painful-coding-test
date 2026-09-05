"""
PB0736 — 접두사 key 제거

Chapter: Dictionaries
Topic: Dict Remove
Seed: 74 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
prefix로 시작하는 key를 모두 제거한다.

연습 초점
---------
startswith 조건과 딕셔너리 필터

구현할 함수
-----------
def dict_drop_prefix_keys(mapping: dict[str, int], prefix: str) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- dict_drop_prefix_keys({'tmp_a': 1, 'keep': 2}, 'tmp_') == {'keep': 2}
- dict_drop_prefix_keys({}, 'x') == {}
- dict_drop_prefix_keys({'a': 1}, '') == {}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0736 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_drop_prefix_keys(mapping: dict[str, int], prefix: str) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0736")


def self_test() -> None:
    assert dict_drop_prefix_keys({'tmp_a': 1, 'keep': 2}, 'tmp_') == {'keep': 2}
    assert dict_drop_prefix_keys({}, 'x') == {}
    assert dict_drop_prefix_keys({'a': 1}, '') == {}
