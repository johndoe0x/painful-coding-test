"""
PB0345 — 합격과 불합격

Chapter: Conditional Statements
Topic: If-Else Statements
Seed: 35 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: if_else

문제
----
score가 60 이상이면 'pass', 아니면 'fail'을 반환한다.

연습 초점
---------
임계값 양쪽을 완전하게 처리

구현할 함수
-----------
def pass_or_fail(score: int) -> str:

필수 구현 방식
--------------
- else 경로가 있는 if문을 사용한다.

예시 및 필수 테스트
-------------------
- pass_or_fail(60) == 'pass'
- pass_or_fail(59) == 'fail'
- pass_or_fail(100) == 'pass'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0345 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def pass_or_fail(score: int) -> str:
    raise NotImplementedError("TODO: PB0345")


def self_test() -> None:
    assert pass_or_fail(60) == 'pass'
    assert pass_or_fail(59) == 'fail'
    assert pass_or_fail(100) == 'pass'
