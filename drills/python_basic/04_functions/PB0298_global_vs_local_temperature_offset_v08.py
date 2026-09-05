"""
PB0298 — 전역 변환값과 지역 변환값

Chapter: Functions
Topic: Global vs Local Scope
Seed: 30 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: global_read, no_global

문제
----
value에 GLOBAL_TEMPERATURE_OFFSET과 local_offset을 각각 더한 결과를 tuple로 반환한다.

연습 초점
---------
모듈 전역 단위 변환 상수와 호출별 지역 보정값 비교

구현할 함수
-----------
def offset_with_global_and_local_value(value: int, local_offset: int) -> tuple[int, int]:

필수 구현 방식
--------------
- 문제 파일에 제공된 모듈 전역 상수를 함수에서 읽어 사용한다.
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- offset_with_global_and_local_value(0, 32) == (273, 32)
- offset_with_global_and_local_value(-273, 273) == (0, 0)
- offset_with_global_and_local_value(10, -10) == (283, 0)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0298 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


GLOBAL_TEMPERATURE_OFFSET = 273


def offset_with_global_and_local_value(value: int, local_offset: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0298")


def self_test() -> None:
    assert offset_with_global_and_local_value(0, 32) == (273, 32)
    assert offset_with_global_and_local_value(-273, 273) == (0, 0)
    assert offset_with_global_and_local_value(10, -10) == (283, 0)
