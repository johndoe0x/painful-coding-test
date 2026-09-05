"""
PB0258 — 시각 차이 초 계산

Chapter: Functions
Topic: Multiple Parameters
Seed: 26 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
같은 날의 두 시각을 초로 바꿔 두 번째에서 첫 번째를 뺀다.

연습 초점
---------
여섯 매개변수를 단계적으로 조합

구현할 함수
-----------
def elapsed_seconds(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int) -> int:

예시 및 필수 테스트
-------------------
- elapsed_seconds(1, 0, 0, 1, 1, 5) == 65
- elapsed_seconds(0, 0, 0, 0, 0, 0) == 0
- elapsed_seconds(2, 30, 0, 3, 0, 0) == 1800

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0258 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def elapsed_seconds(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int) -> int:
    raise NotImplementedError("TODO: PB0258")


def self_test() -> None:
    assert elapsed_seconds(1, 0, 0, 1, 1, 5) == 65
    assert elapsed_seconds(0, 0, 0, 0, 0, 0) == 0
    assert elapsed_seconds(2, 30, 0, 3, 0, 0) == 1800
