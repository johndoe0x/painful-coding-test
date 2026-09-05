"""
PB0302 — 기본 제곱 지수

Chapter: Functions
Topic: Default Arguments
Seed: 31 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
base의 exponent 거듭제곱을 반환하며 exponent 생략 시 2를 사용한다.

연습 초점
---------
숫자 기본 인자

구현할 함수
-----------
def power_with_default(base: int, exponent: int = 2) -> int:

예시 및 필수 테스트
-------------------
- power_with_default(5) == 25
- power_with_default(2, 3) == 8
- power_with_default(-3) == 9

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0302 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def power_with_default(base: int, exponent: int = 2) -> int:
    raise NotImplementedError("TODO: PB0302")


def self_test() -> None:
    assert power_with_default(5) == 25
    assert power_with_default(2, 3) == 8
    assert power_with_default(-3) == 9
