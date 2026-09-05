"""
PB0197 — 극단 기온

Chapter: Math
Topic: Boolean OR
Seed: 20 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: bool_or

문제
----
value가 low 이하이거나 high 이상이면 True를 반환하세요.

연습 초점
---------
양쪽 경계 바깥 조건의 OR

구현할 함수
-----------
def is_extreme_temperature(value: float, low: float, high: float) -> bool:

필수 구현 방식
--------------
- 논리 연산자 or를 사용한다.

예시 및 필수 테스트
-------------------
- is_extreme_temperature(-10, -10, 35) is True and is_extreme_temperature(-11, -10, 35) is True
- is_extreme_temperature(20, -10, 35) is False
- is_extreme_temperature(35, -10, 35) is True and is_extreme_temperature(36, -10, 35) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0197 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_extreme_temperature(value: float, low: float, high: float) -> bool:
    raise NotImplementedError("TODO: PB0197")


def self_test() -> None:
    assert is_extreme_temperature(-10, -10, 35) is True and is_extreme_temperature(-11, -10, 35) is True
    assert is_extreme_temperature(20, -10, 35) is False
    assert is_extreme_temperature(35, -10, 35) is True and is_extreme_temperature(36, -10, 35) is True
