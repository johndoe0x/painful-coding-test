"""
PB0717 — 가장 긴 key

Chapter: Dictionaries
Topic: Dict Looping
Seed: 72 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: for, dict_items_call

문제
----
가장 긴 key를 반환한다. 길이가 같으면 먼저 나온 key, 비어 있으면 None을 반환한다.

연습 초점
---------
items 순회와 최댓값 상태 유지

구현할 함수
-----------
def dict_longest_key(mapping: dict[str, object]) -> str | None:

필수 구현 방식
--------------
- for문을 사용한다.
- dict.items()를 사용한다.

예시 및 필수 테스트
-------------------
- dict_longest_key({'a': 1, 'long': 2, 'mid': 3}) == 'long'
- dict_longest_key({}) is None
- dict_longest_key({'aa': 1, 'bb': 2}) == 'aa'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0717 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_longest_key(mapping: dict[str, object]) -> str | None:
    raise NotImplementedError("TODO: PB0717")


def self_test() -> None:
    assert dict_longest_key({'a': 1, 'long': 2, 'mid': 3}) == 'long'
    assert dict_longest_key({}) is None
    assert dict_longest_key({'aa': 1, 'bb': 2}) == 'aa'
