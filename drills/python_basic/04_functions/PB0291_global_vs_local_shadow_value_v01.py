"""
PB0291 — 전역 기준값과 지역 증가값

Chapter: Functions
Topic: Global vs Local Scope
Seed: 30 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: global_read, no_global

문제
----
제공된 모듈 전역 상수 GLOBAL_SHADOW_BASE를 읽고, 매개변수 value를 지역에서 1 증가시켜 (전역 기준값, 지역 증가값)을 반환한다. 전역 상수는 수정하지 않는다.

연습 초점
---------
읽기 전용 전역 상수와 지역 매개변수 재할당의 차이

구현할 함수
-----------
def shadow_value(value: int) -> tuple[int, int]:

필수 구현 방식
--------------
- 문제 파일에 제공된 모듈 전역 상수를 함수에서 읽어 사용한다.
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- shadow_value(5) == (100, 6)
- shadow_value(0) == (100, 1)
- shadow_value(-2) == (100, -1)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0291 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


GLOBAL_SHADOW_BASE = 100


def shadow_value(value: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0291")


def self_test() -> None:
    assert shadow_value(5) == (100, 6)
    assert shadow_value(0) == (100, 1)
    assert shadow_value(-2) == (100, -1)
