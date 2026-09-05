"""
PB0136 — 리스트를 tuple로

Chapter: Variables
Topic: Type Casting
Seed: 14 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
list 입력을 같은 순서의 tuple로 변환하세요.

연습 초점
---------
컬렉션 타입 캐스팅

구현할 함수
-----------
def cast_list_to_tuple(values: list[object]) -> tuple[object, ...]:

예시 및 필수 테스트
-------------------
- cast_list_to_tuple([1, 'a']) == (1, 'a')
- cast_list_to_tuple([]) == ()
- cast_list_to_tuple([None]) == (None,)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0136 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def cast_list_to_tuple(values: list[object]) -> tuple[object, ...]:
    raise NotImplementedError("TODO: PB0136")


def self_test() -> None:
    assert cast_list_to_tuple([1, 'a']) == (1, 'a')
    assert cast_list_to_tuple([]) == ()
    assert cast_list_to_tuple([None]) == (None,)
