"""
PB0466 — 점수 센티널 처리

Chapter: Loops
Topic: Control Flow
Seed: 47 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: break_or_continue

문제
----
-1을 만나면 break하고 0~100 밖의 값은 continue하며 그전 유효 점수만 반환한다.

연습 초점
---------
특별 종료값과 무효값 건너뛰기

구현할 함수
-----------
def valid_scores_until_sentinel(scores: list[int]) -> list[int]:

필수 구현 방식
--------------
- break 또는 continue를 사용한다.

예시 및 필수 테스트
-------------------
- valid_scores_until_sentinel([80, 120, 90, -1, 70]) == [80, 90]
- valid_scores_until_sentinel([]) == []
- valid_scores_until_sentinel([-1, 50]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0466 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def valid_scores_until_sentinel(scores: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0466")


def self_test() -> None:
    assert valid_scores_until_sentinel([80, 120, 90, -1, 70]) == [80, 90]
    assert valid_scores_until_sentinel([]) == []
    assert valid_scores_until_sentinel([-1, 50]) == []
