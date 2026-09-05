"""
PB0655 — tuple을 리스트로 변환하기

Chapter: Lists
Topic: Tuples
Seed: 66 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
values와 같은 순서의 원소를 가진 새 리스트를 반환한다.

연습 초점
---------
불변 tuple에서 변경 가능한 list로 컨테이너 타입을 변환한다.

구현할 함수
-----------
def tuple_as_list(values: tuple[int, ...]) -> list[int]:

예시 및 필수 테스트
-------------------
- tuple_as_list((1, 2, 3)) == [1, 2, 3]
- tuple_as_list((7,)) == [7]
- tuple_as_list(()) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0655 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def tuple_as_list(values: tuple[int, ...]) -> list[int]:
    raise NotImplementedError("TODO: PB0655")


def self_test() -> None:
    assert tuple_as_list((1, 2, 3)) == [1, 2, 3]
    assert tuple_as_list((7,)) == [7]
    assert tuple_as_list(()) == []
