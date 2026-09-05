"""
PB0153 — 선택적 숫자

Chapter: Variables
Topic: Empty Variable
Seed: 16 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
value가 None이면 0, 아니면 원래 정수를 반환하세요.

연습 초점
---------
숫자 0을 빈 값으로 오해하지 않기

구현할 함수
-----------
def optional_number(value: int | None) -> int:

예시 및 필수 테스트
-------------------
- optional_number(None) == 0
- optional_number(0) == 0
- optional_number(-1) == -1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0153 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def optional_number(value: int | None) -> int:
    raise NotImplementedError("TODO: PB0153")


def self_test() -> None:
    assert optional_number(None) == 0
    assert optional_number(0) == 0
    assert optional_number(-1) == -1
