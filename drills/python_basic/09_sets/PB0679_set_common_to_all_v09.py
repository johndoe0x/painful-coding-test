"""
PB0679 — 모든 그룹의 공통값

Chapter: Sets
Topic: Set Operations
Seed: 68 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
groups가 비면 빈 set, 아니면 모든 set에 공통인 값을 반환한다.

연습 초점
---------
연속 intersection과 첫 원소 초기화

구현할 함수
-----------
def set_common_to_all(groups: list[set[str]]) -> set[str]:

예시 및 필수 테스트
-------------------
- set_common_to_all([{'a', 'b'}, {'b', 'c'}, {'b'}]) == {'b'}
- set_common_to_all([]) == set()
- set_common_to_all([{'x', 'y'}]) == {'x', 'y'}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0679 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_common_to_all(groups: list[set[str]]) -> set[str]:
    raise NotImplementedError("TODO: PB0679")


def self_test() -> None:
    assert set_common_to_all([{'a', 'b'}, {'b', 'c'}, {'b'}]) == {'b'}
    assert set_common_to_all([]) == set()
    assert set_common_to_all([{'x', 'y'}]) == {'x', 'y'}
