"""
PB0295 — 전역 배율과 지역 배율

Chapter: Functions
Topic: Global vs Local Scope
Seed: 30 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: global_read, no_global

문제
----
value에 GLOBAL_SCALE_FACTOR와 local_factor를 각각 곱해 (전역 배율 결과, 지역 배율 결과)를 반환한다.

연습 초점
---------
모듈 설정 배율과 매개변수 배율을 같은 계산에 적용

구현할 함수
-----------
def scale_with_global_and_local_factor(value: float, local_factor: float) -> tuple[float, float]:

필수 구현 방식
--------------
- 문제 파일에 제공된 모듈 전역 상수를 함수에서 읽어 사용한다.
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- scale_with_global_and_local_factor(3.0, 4.0) == (6.0, 12.0)
- scale_with_global_and_local_factor(0.0, 0.5) == (0.0, 0.0)
- scale_with_global_and_local_factor(-2.0, -1.0) == (-4.0, 2.0)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0295 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


GLOBAL_SCALE_FACTOR = 2.0


def scale_with_global_and_local_factor(value: float, local_factor: float) -> tuple[float, float]:
    raise NotImplementedError("TODO: PB0295")


def self_test() -> None:
    assert scale_with_global_and_local_factor(3.0, 4.0) == (6.0, 12.0)
    assert scale_with_global_and_local_factor(0.0, 0.5) == (0.0, 0.0)
    assert scale_with_global_and_local_factor(-2.0, -1.0) == (-4.0, 2.0)
