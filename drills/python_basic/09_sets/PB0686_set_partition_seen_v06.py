"""
PB0686 — 기존값과 새 값 분리

Chapter: Sets
Topic: Set Practice
Seed: 69 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
incoming을 seen 여부에 따라 known과 new 리스트로 나누며 중복도 입력 그대로 유지한다.

연습 초점
---------
set membership를 이용한 두 리스트 분기

구현할 함수
-----------
def set_partition_seen(seen: set[str], incoming: list[str]) -> dict[str, list[str]]:

예시 및 필수 테스트
-------------------
- set_partition_seen({'a'}, ['a', 'b', 'a']) == {'known': ['a', 'a'], 'new': ['b']}
- set_partition_seen(set(), []) == {'known': [], 'new': []}
- set_partition_seen({'x'}, ['y']) == {'known': [], 'new': ['y']}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0686 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_partition_seen(seen: set[str], incoming: list[str]) -> dict[str, list[str]]:
    raise NotImplementedError("TODO: PB0686")


def self_test() -> None:
    assert set_partition_seen({'a'}, ['a', 'b', 'a']) == {'known': ['a', 'a'], 'new': ['b']}
    assert set_partition_seen(set(), []) == {'known': [], 'new': []}
    assert set_partition_seen({'x'}, ['y']) == {'known': [], 'new': ['y']}
