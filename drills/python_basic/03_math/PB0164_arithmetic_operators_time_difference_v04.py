"""
PB0164 — 경과 시간

Chapter: Math
Topic: Arithmetic Operators
Seed: 17 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
같은 날이고 end_minute가 더 크거나 같을 때 두 시각의 차이를 반환하세요.

연습 초점
---------
뺄셈으로 변화량 계산

구현할 함수
-----------
def elapsed_minutes(start_minute: int, end_minute: int) -> int:

예시 및 필수 테스트
-------------------
- elapsed_minutes(10, 25) == 15
- elapsed_minutes(0, 0) == 0
- elapsed_minutes(59, 60) == 1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0164 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def elapsed_minutes(start_minute: int, end_minute: int) -> int:
    raise NotImplementedError("TODO: PB0164")


def self_test() -> None:
    assert elapsed_minutes(10, 25) == 15
    assert elapsed_minutes(0, 0) == 0
    assert elapsed_minutes(59, 60) == 1
