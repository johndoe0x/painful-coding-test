"""
PB0053 — 운동 에너지 공식 주석

Chapter: Introduction
Topic: Comments
Seed: 06 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: comment

문제
----
mass와 speed가 0 이상일 때 0.5 * mass * speed**2를 반환하고, 0.5와 속도 제곱의 의미를 주석으로 설명하세요.

연습 초점
---------
공식의 근거를 남기는 주석

구현할 함수
-----------
def kinetic_energy(mass: float, speed: float) -> float:

필수 구현 방식
--------------
- 함수 본문에 계산 이유를 설명하는 주석을 한 줄 이상 작성한다.

예시 및 필수 테스트
-------------------
- kinetic_energy(2, 3) == 9.0
- kinetic_energy(0, 10) == 0.0
- kinetic_energy(4, 0) == 0.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0053 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def kinetic_energy(mass: float, speed: float) -> float:
    raise NotImplementedError("TODO: PB0053")


def self_test() -> None:
    assert kinetic_energy(2, 3) == 9.0
    assert kinetic_energy(0, 10) == 0.0
    assert kinetic_energy(4, 0) == 0.0
