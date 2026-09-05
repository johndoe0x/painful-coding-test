"""
PB0275 — 선택적 절반값

Chapter: Functions
Topic: Type Hints
Seed: 28 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
value가 None이면 None, 아니면 절반인 float를 반환한다.

연습 초점
---------
유니온 타입으로 선택적 값 표현

구현할 함수
-----------
def optional_half_typed(value: int | None) -> float | None:

예시 및 필수 테스트
-------------------
- optional_half_typed(5) == 2.5
- optional_half_typed(None) is None
- optional_half_typed(-4) == -2.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0275 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def optional_half_typed(value: int | None) -> float | None:
    raise NotImplementedError("TODO: PB0275")


def self_test() -> None:
    assert optional_half_typed(5) == 2.5
    assert optional_half_typed(None) is None
    assert optional_half_typed(-4) == -2.0
