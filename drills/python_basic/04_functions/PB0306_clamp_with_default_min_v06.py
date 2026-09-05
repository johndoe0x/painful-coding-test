"""
PB0306 — 기본 최솟값 제한

Chapter: Functions
Topic: Default Arguments
Seed: 31 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
value가 minimum보다 작으면 minimum, 아니면 value를 반환한다.

연습 초점
---------
경계값 기본 인자

구현할 함수
-----------
def clamp_with_default_min(value: int, minimum: int = 0) -> int:

예시 및 필수 테스트
-------------------
- clamp_with_default_min(-3) == 0
- clamp_with_default_min(5) == 5
- clamp_with_default_min(-3, -5) == -3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0306 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def clamp_with_default_min(value: int, minimum: int = 0) -> int:
    raise NotImplementedError("TODO: PB0306")


def self_test() -> None:
    assert clamp_with_default_min(-3) == 0
    assert clamp_with_default_min(5) == 5
    assert clamp_with_default_min(-3, -5) == -3
