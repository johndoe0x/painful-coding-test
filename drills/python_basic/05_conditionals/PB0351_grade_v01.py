"""
PB0351 — 점수 등급

Chapter: Conditional Statements
Topic: Else-If Statements
Seed: 36 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: elif

문제
----
90/80/70/60 이상 경계로 A/B/C/D를, 그 아래는 F를 반환한다.

연습 초점
---------
내림차순 elif 경계 배치

구현할 함수
-----------
def grade(score: int) -> str:

필수 구현 방식
--------------
- elif 경로를 사용한다.

예시 및 필수 테스트
-------------------
- grade(95) == 'A'
- grade(80) == 'B'
- grade(59) == 'F'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0351 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def grade(score: int) -> str:
    raise NotImplementedError("TODO: PB0351")


def self_test() -> None:
    assert grade(95) == 'A'
    assert grade(80) == 'B'
    assert grade(59) == 'F'
