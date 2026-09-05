"""
PB0300 — 전역 세율과 지역 세율

Chapter: Functions
Topic: Global vs Local Scope
Seed: 30 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: global_read, no_global

문제
----
GLOBAL_TAX_RATE와 지역 매개변수 rate를 각각 적용하고 round(total * (1 + rate), 2)로 센트 단위 반올림해 (전역 세금 결과, 지역 세금 결과)를 반환한다.

연습 초점
---------
전역 기본 세율과 호출별 지역 세율의 명시적 반올림 비교

구현할 함수
-----------
def shadow_total_tax(total: float, rate: float) -> tuple[float, float]:

필수 구현 방식
--------------
- 문제 파일에 제공된 모듈 전역 상수를 함수에서 읽어 사용한다.
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- shadow_total_tax(100.0, 0.2) == (110.0, 120.0)
- shadow_total_tax(19.99, 0.075) == (21.99, 21.49)
- shadow_total_tax(50.0, 0.0) == (55.0, 50.0)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0300 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


GLOBAL_TAX_RATE = 0.1


def shadow_total_tax(total: float, rate: float) -> tuple[float, float]:
    raise NotImplementedError("TODO: PB0300")


def self_test() -> None:
    assert shadow_total_tax(100.0, 0.2) == (110.0, 120.0)
    assert shadow_total_tax(19.99, 0.075) == (21.99, 21.49)
    assert shadow_total_tax(50.0, 0.0) == (55.0, 50.0)
