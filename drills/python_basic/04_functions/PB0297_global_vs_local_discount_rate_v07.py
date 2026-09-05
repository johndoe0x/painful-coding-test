"""
PB0297 — 전역 할인율과 지역 할인율

Chapter: Functions
Topic: Global vs Local Scope
Seed: 30 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: global_read, no_global

문제
----
GLOBAL_DISCOUNT_RATE와 local_rate를 각각 적용한 가격을 round(price * (1 - rate), 2)로 반올림해 tuple로 반환한다.

연습 초점
---------
전역 기본 할인 정책과 지역 할인 정책의 센트 단위 비교

구현할 함수
-----------
def discount_with_global_and_local_rate(price: float, local_rate: float) -> tuple[float, float]:

필수 구현 방식
--------------
- 문제 파일에 제공된 모듈 전역 상수를 함수에서 읽어 사용한다.
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- discount_with_global_and_local_rate(100.0, 0.2) == (90.0, 80.0)
- discount_with_global_and_local_rate(19.99, 0.25) == (17.99, 14.99)
- discount_with_global_and_local_rate(0.0, 0.5) == (0.0, 0.0)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0297 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


GLOBAL_DISCOUNT_RATE = 0.1


def discount_with_global_and_local_rate(price: float, local_rate: float) -> tuple[float, float]:
    raise NotImplementedError("TODO: PB0297")


def self_test() -> None:
    assert discount_with_global_and_local_rate(100.0, 0.2) == (90.0, 80.0)
    assert discount_with_global_and_local_rate(19.99, 0.25) == (17.99, 14.99)
    assert discount_with_global_and_local_rate(0.0, 0.5) == (0.0, 0.0)
