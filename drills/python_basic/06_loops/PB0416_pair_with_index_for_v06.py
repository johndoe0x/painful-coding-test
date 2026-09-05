"""
PB0416 — for 인덱스 쌍

Chapter: Loops
Topic: For Loops
Seed: 42 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: for

문제
----
for와 enumerate로 각 값을 0부터의 인덱스와 묶어 반환한다.

연습 초점
---------
for에서 enumerate 활용

구현할 함수
-----------
def pair_with_index_for(values: list[str]) -> list[tuple[int, str]]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- pair_with_index_for(['a', 'b']) == [(0, 'a'), (1, 'b')]
- pair_with_index_for([]) == []
- pair_with_index_for(['']) == [(0, '')]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0416 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def pair_with_index_for(values: list[str]) -> list[tuple[int, str]]:
    raise NotImplementedError("TODO: PB0416")


def self_test() -> None:
    assert pair_with_index_for(['a', 'b']) == [(0, 'a'), (1, 'b')]
    assert pair_with_index_for([]) == []
    assert pair_with_index_for(['']) == [(0, '')]
