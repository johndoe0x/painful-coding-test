"""
PB0360 — 성과 순위

Chapter: Conditional Statements
Topic: Else-If Statements
Seed: 36 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: elif

문제
----
1000 이상 platinum, 500 이상 gold, 100 이상 silver, 0 이상 bronze, 음수 invalid를 반환한다.

연습 초점
---------
하한을 내림차순으로 검사하는 elif

구현할 함수
-----------
def performance_rank(points: int) -> str:

필수 구현 방식
--------------
- elif 경로를 사용한다.

예시 및 필수 테스트
-------------------
- performance_rank(1000) == 'platinum'
- performance_rank(499) == 'silver'
- performance_rank(-1) == 'invalid'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0360 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def performance_rank(points: int) -> str:
    raise NotImplementedError("TODO: PB0360")


def self_test() -> None:
    assert performance_rank(1000) == 'platinum'
    assert performance_rank(499) == 'silver'
    assert performance_rank(-1) == 'invalid'
