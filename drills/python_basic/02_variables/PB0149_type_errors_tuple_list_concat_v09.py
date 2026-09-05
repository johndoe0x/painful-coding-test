"""
PB0149 — tuple과 list 결합

Chapter: Variables
Topic: Type Errors
Seed: 15 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
right를 tuple로 변환해 left 뒤에 이어 붙인 tuple을 반환하세요.

연습 초점
---------
서로 다른 시퀀스 타입 통일

구현할 함수
-----------
def combine_as_tuple(left: tuple[int, ...], right: list[int]) -> tuple[int, ...]:

예시 및 필수 테스트
-------------------
- combine_as_tuple((1, 2), [3]) == (1, 2, 3)
- combine_as_tuple((), []) == ()
- combine_as_tuple((0,), []) == (0,)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0149 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def combine_as_tuple(left: tuple[int, ...], right: list[int]) -> tuple[int, ...]:
    raise NotImplementedError("TODO: PB0149")


def self_test() -> None:
    assert combine_as_tuple((1, 2), [3]) == (1, 2, 3)
    assert combine_as_tuple((), []) == ()
    assert combine_as_tuple((0,), []) == (0,)
