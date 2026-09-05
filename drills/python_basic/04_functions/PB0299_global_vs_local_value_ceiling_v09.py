"""
PB0299 — 전역 상한과 지역 상한

Chapter: Functions
Topic: Global vs Local Scope
Seed: 30 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: global_read, no_global

문제
----
value를 GLOBAL_VALUE_CEILING과 local_ceiling으로 각각 상한 제한해 (전역 제한값, 지역 제한값)을 반환한다.

연습 초점
---------
전역 안전 상한과 호출별 지역 상한을 별도로 적용

구현할 함수
-----------
def clamp_with_global_and_local_ceiling(value: int, local_ceiling: int) -> tuple[int, int]:

필수 구현 방식
--------------
- 문제 파일에 제공된 모듈 전역 상수를 함수에서 읽어 사용한다.
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- clamp_with_global_and_local_ceiling(120, 80) == (100, 80)
- clamp_with_global_and_local_ceiling(50, 80) == (50, 50)
- clamp_with_global_and_local_ceiling(-5, 0) == (-5, -5)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0299 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


GLOBAL_VALUE_CEILING = 100


def clamp_with_global_and_local_ceiling(value: int, local_ceiling: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0299")


def self_test() -> None:
    assert clamp_with_global_and_local_ceiling(120, 80) == (100, 80)
    assert clamp_with_global_and_local_ceiling(50, 80) == (50, 50)
    assert clamp_with_global_and_local_ceiling(-5, 0) == (-5, -5)
