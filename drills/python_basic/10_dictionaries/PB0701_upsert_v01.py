"""
PB0701 — key 추가 또는 갱신

Chapter: Dictionaries
Topic: Dict Operations
Seed: 71 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
원본을 바꾸지 않고 key를 value로 추가하거나 갱신한 새 딕셔너리를 반환한다.

연습 초점
---------
dict 복사와 item 할당

구현할 함수
-----------
def upsert(mapping: dict[str, int], key: str, value: int) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- ((items := {'a': 1}), upsert(items, 'a', 2) == {'a': 2} and items == {'a': 1})[-1] is True
- upsert({}, 'x', 0) == {'x': 0}
- upsert({'a': 1}, 'b', 2) == {'a': 1, 'b': 2}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0701 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def upsert(mapping: dict[str, int], key: str, value: int) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0701")


def self_test() -> None:
    assert ((items := {'a': 1}), upsert(items, 'a', 2) == {'a': 2} and items == {'a': 1})[-1] is True
    assert upsert({}, 'x', 0) == {'x': 0}
    assert upsert({'a': 1}, 'b', 2) == {'a': 1, 'b': 2}
