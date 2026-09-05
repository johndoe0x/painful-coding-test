"""
PB0058 — 배송비 기준 주석

Chapter: Introduction
Topic: Comments
Seed: 06 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: comment

문제
----
subtotal이 free_threshold 이상이면 배송비 없이, 아니면 fee를 더해 반환하고 경계 포함 이유를 주석으로 작성하세요.

연습 초점
---------
경계조건의 결정 이유 주석

구현할 함수
-----------
def total_with_shipping(subtotal: float, free_threshold: float, fee: float) -> float:

필수 구현 방식
--------------
- 함수 본문에 계산 이유를 설명하는 주석을 한 줄 이상 작성한다.

예시 및 필수 테스트
-------------------
- total_with_shipping(50, 50, 5) == 50
- total_with_shipping(49, 50, 5) == 54
- total_with_shipping(0, 0, 7) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0058 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def total_with_shipping(subtotal: float, free_threshold: float, fee: float) -> float:
    raise NotImplementedError("TODO: PB0058")


def self_test() -> None:
    assert total_with_shipping(50, 50, 5) == 50
    assert total_with_shipping(49, 50, 5) == 54
    assert total_with_shipping(0, 0, 7) == 0
