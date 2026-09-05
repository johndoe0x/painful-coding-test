"""
PB0077 — 활성 사용자 수

Chapter: Variables
Topic: Variable Naming
Seed: 08 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
활성 여부 목록에서 True의 개수를 반환하세요.

연습 초점
---------
복수형과 불리언 의미가 드러나는 이름

구현할 함수
-----------
def count_active_users(user_activity_flags: list[bool]) -> int:

예시 및 필수 테스트
-------------------
- count_active_users([True, False, True]) == 2
- count_active_users([]) == 0
- count_active_users([False]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0077 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_active_users(user_activity_flags: list[bool]) -> int:
    raise NotImplementedError("TODO: PB0077")


def self_test() -> None:
    assert count_active_users([True, False, True]) == 2
    assert count_active_users([]) == 0
    assert count_active_users([False]) == 0
