"""
PB0067 — 측정값과 단위

Chapter: Variables
Topic: Variable Declaration
Seed: 07 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: assignment

문제
----
measurement_value와 measurement_unit라는 의미의 변수를 선언해 tuple로 반환하세요.

연습 초점
---------
값과 메타데이터를 별도 변수로 표현

구현할 함수
-----------
def declare_measurement(value: float, unit: str) -> tuple[float, str]:

필수 구현 방식
--------------
- 함수 본문에서 지역 변수 할당을 사용한다.

예시 및 필수 테스트
-------------------
- declare_measurement(12.5, 'cm') == (12.5, 'cm')
- declare_measurement(0, '') == (0, '')
- declare_measurement(-1, 'C') == (-1, 'C')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0067 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def declare_measurement(value: float, unit: str) -> tuple[float, str]:
    raise NotImplementedError("TODO: PB0067")


def self_test() -> None:
    assert declare_measurement(12.5, 'cm') == (12.5, 'cm')
    assert declare_measurement(0, '') == (0, '')
    assert declare_measurement(-1, 'C') == (-1, 'C')
