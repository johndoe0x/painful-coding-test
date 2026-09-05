"""
PB0356 — 월별 분기

Chapter: Conditional Statements
Topic: Else-If Statements
Seed: 36 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: elif

문제
----
1~3은 Q1, 4~6은 Q2, 7~9는 Q3, 10~12는 Q4, 그 밖은 invalid를 반환한다.

연습 초점
---------
범위 조건 여러 개를 elif로 구분

구현할 함수
-----------
def month_quarter(month: int) -> str:

필수 구현 방식
--------------
- elif 경로를 사용한다.

예시 및 필수 테스트
-------------------
- month_quarter(1) == 'Q1'
- month_quarter(9) == 'Q3'
- month_quarter(13) == 'invalid'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0356 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def month_quarter(month: int) -> str:
    raise NotImplementedError("TODO: PB0356")


def self_test() -> None:
    assert month_quarter(1) == 'Q1'
    assert month_quarter(9) == 'Q3'
    assert month_quarter(13) == 'invalid'
