"""
PB0235 — 직육면체 부피

Chapter: Functions
Topic: Function Declaration
Seed: 24 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
세 변의 길이를 곱해 직육면체 부피를 반환한다.

연습 초점
---------
세 매개변수를 갖는 함수 선언

구현할 함수
-----------
def box_volume(width: float, height: float, depth: float) -> float:

예시 및 필수 테스트
-------------------
- box_volume(2.0, 3.0, 4.0) == 24.0
- box_volume(0.0, 3.0, 4.0) == 0.0
- box_volume(1.5, 2.0, 2.0) == 6.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0235 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def box_volume(width: float, height: float, depth: float) -> float:
    raise NotImplementedError("TODO: PB0235")


def self_test() -> None:
    assert box_volume(2.0, 3.0, 4.0) == 24.0
    assert box_volume(0.0, 3.0, 4.0) == 0.0
    assert box_volume(1.5, 2.0, 2.0) == 6.0
