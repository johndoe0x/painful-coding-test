"""
PB0336 — 저장공간 초과 비용

Chapter: Conditional Statements
Topic: If Statement Scope
Seed: 34 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: if

문제
----
지역 cost를 0으로 정하고 10GB를 초과하면 if 안에서 초과 GB마다 2를 곱해 반환한다.

연습 초점
---------
조건문 안 계산 결과를 밖에서 반환

구현할 함수
-----------
def storage_cost_over_quota(gigabytes: int) -> int:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- storage_cost_over_quota(12) == 4
- storage_cost_over_quota(10) == 0
- storage_cost_over_quota(0) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0336 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def storage_cost_over_quota(gigabytes: int) -> int:
    raise NotImplementedError("TODO: PB0336")


def self_test() -> None:
    assert storage_cost_over_quota(12) == 4
    assert storage_cost_over_quota(10) == 0
    assert storage_cost_over_quota(0) == 0
