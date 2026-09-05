"""
PB0293 — 전역 보너스와 지역 보너스

Chapter: Functions
Topic: Global vs Local Scope
Seed: 30 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: global_read, no_global

문제
----
score에 GLOBAL_SCORE_BONUS와 local_bonus를 각각 더해 (전역 보너스 점수, 지역 보너스 점수)를 반환한다.

연습 초점
---------
공통 전역 설정과 호출별 지역 설정 비교

구현할 함수
-----------
def score_with_global_and_local_bonus(score: int, local_bonus: int) -> tuple[int, int]:

필수 구현 방식
--------------
- 문제 파일에 제공된 모듈 전역 상수를 함수에서 읽어 사용한다.
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- score_with_global_and_local_bonus(80, 5) == (90, 85)
- score_with_global_and_local_bonus(0, 0) == (10, 0)
- score_with_global_and_local_bonus(-5, 2) == (5, -3)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0293 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


GLOBAL_SCORE_BONUS = 10


def score_with_global_and_local_bonus(score: int, local_bonus: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0293")


def self_test() -> None:
    assert score_with_global_and_local_bonus(80, 5) == (90, 85)
    assert score_with_global_and_local_bonus(0, 0) == (10, 0)
    assert score_with_global_and_local_bonus(-5, 2) == (5, -3)
