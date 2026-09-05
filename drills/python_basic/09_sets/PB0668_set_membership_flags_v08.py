"""
PB0668 — 허용값 포함 여부

Chapter: Sets
Topic: Intro to Sets
Seed: 67 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 candidate가 allowed에 들어 있는지를 입력 순서대로 반환한다.

연습 초점
---------
set membership와 리스트 순회

구현할 함수
-----------
def set_membership_flags(allowed: set[str], candidates: list[str]) -> list[bool]:

예시 및 필수 테스트
-------------------
- set_membership_flags({'read', 'write'}, ['read', 'delete']) == [True, False]
- set_membership_flags(set(), ['x']) == [False]
- set_membership_flags({'x'}, []) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0668 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_membership_flags(allowed: set[str], candidates: list[str]) -> list[bool]:
    raise NotImplementedError("TODO: PB0668")


def self_test() -> None:
    assert set_membership_flags({'read', 'write'}, ['read', 'delete']) == [True, False]
    assert set_membership_flags(set(), ['x']) == [False]
    assert set_membership_flags({'x'}, []) == []
