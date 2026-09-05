"""
PB0349 — 배송 방법 선택

Chapter: Conditional Statements
Topic: If-Else Statements
Seed: 35 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: if_else

문제
----
특급 배송이면 'air', 아니면 'ground'를 반환한다.

연습 초점
---------
도메인 선택을 두 분기로 표현

구현할 함수
-----------
def shipping_method_choice(is_express: bool) -> str:

필수 구현 방식
--------------
- else 경로가 있는 if문을 사용한다.

예시 및 필수 테스트
-------------------
- shipping_method_choice(True) == 'air'
- shipping_method_choice(False) == 'ground'
- shipping_method_choice(not True) == 'ground'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0349 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def shipping_method_choice(is_express: bool) -> str:
    raise NotImplementedError("TODO: PB0349")


def self_test() -> None:
    assert shipping_method_choice(True) == 'air'
    assert shipping_method_choice(False) == 'ground'
    assert shipping_method_choice(not True) == 'ground'
