"""
PB0660 — tuple 쌍들을 하나로 펼치기

Chapter: Lists
Topic: Tuples
Seed: 66 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
pairs의 각 두 원소를 순서대로 이어 하나의 tuple로 반환한다.

연습 초점
---------
중첩된 고정 길이 tuple을 읽어 가변 길이 tuple 결과를 구축한다.

구현할 함수
-----------
def flatten_tuple_pairs(pairs: list[tuple[int, int]]) -> tuple[int, ...]:

예시 및 필수 테스트
-------------------
- flatten_tuple_pairs([(1, 2), (3, 4)]) == (1, 2, 3, 4)
- flatten_tuple_pairs([(5, 6)]) == (5, 6)
- flatten_tuple_pairs([]) == ()

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0660 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def flatten_tuple_pairs(pairs: list[tuple[int, int]]) -> tuple[int, ...]:
    raise NotImplementedError("TODO: PB0660")


def self_test() -> None:
    assert flatten_tuple_pairs([(1, 2), (3, 4)]) == (1, 2, 3, 4)
    assert flatten_tuple_pairs([(5, 6)]) == (5, 6)
    assert flatten_tuple_pairs([]) == ()
