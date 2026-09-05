"""
PB0318 — 점수 승자 비교

Chapter: Conditional Statements
Topic: Comparison Operators
Seed: 32 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
home이 높으면 'home', away가 높으면 'away', 같으면 'draw'를 반환한다.

연습 초점
---------
비교 결과를 도메인 라벨로 변환

구현할 함수
-----------
def score_relation(home: int, away: int) -> str:

예시 및 필수 테스트
-------------------
- score_relation(3, 1) == 'home'
- score_relation(0, 2) == 'away'
- score_relation(4, 4) == 'draw'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0318 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def score_relation(home: int, away: int) -> str:
    raise NotImplementedError("TODO: PB0318")


def self_test() -> None:
    assert score_relation(3, 1) == 'home'
    assert score_relation(0, 2) == 'away'
    assert score_relation(4, 4) == 'draw'
