"""
PB0694 — pair 목록을 딕셔너리로

Chapter: Dictionaries
Topic: Intro to Dictionaries
Seed: 70 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
pairs를 순서대로 딕셔너리에 넣는다. 같은 key가 다시 나오면 마지막 value를 사용한다.

연습 초점
---------
반복 할당과 key 갱신

구현할 함수
-----------
def dict_from_pairs(pairs: list[tuple[str, int]]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- dict_from_pairs([('a', 1), ('b', 2)]) == {'a': 1, 'b': 2}
- dict_from_pairs([]) == {}
- dict_from_pairs([('a', 1), ('a', 3)]) == {'a': 3}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0694 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_from_pairs(pairs: list[tuple[str, int]]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0694")


def self_test() -> None:
    assert dict_from_pairs([('a', 1), ('b', 2)]) == {'a': 1, 'b': 2}
    assert dict_from_pairs([]) == {}
    assert dict_from_pairs([('a', 1), ('a', 3)]) == {'a': 3}
