"""
PB0324 — 고득점 보너스

Chapter: Conditional Statements
Topic: If Statements
Seed: 33 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: if

문제
----
score가 90 이상이면 5를 더하고 아니면 그대로 반환한다.

연습 초점
---------
경계에서 단일 if 실행

구현할 함수
-----------
def bonus_if_high_score(score: int) -> int:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- bonus_if_high_score(90) == 95
- bonus_if_high_score(89) == 89
- bonus_if_high_score(-1) == -1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0324 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def bonus_if_high_score(score: int) -> int:
    raise NotImplementedError("TODO: PB0324")


def self_test() -> None:
    assert bonus_if_high_score(90) == 95
    assert bonus_if_high_score(89) == 89
    assert bonus_if_high_score(-1) == -1
