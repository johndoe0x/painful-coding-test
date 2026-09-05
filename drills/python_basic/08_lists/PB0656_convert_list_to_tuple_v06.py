"""
PB0656 — 리스트를 tuple로 변환하기

Chapter: Lists
Topic: Tuples
Seed: 66 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
values와 같은 순서의 원소를 가진 새 tuple을 반환한다.

연습 초점
---------
변경 가능한 list를 불변 tuple로 변환한다.

구현할 함수
-----------
def list_as_tuple(values: list[str]) -> tuple[str, ...]:

예시 및 필수 테스트
-------------------
- list_as_tuple(['a', 'b']) == ('a', 'b')
- list_as_tuple(['x']) == ('x',)
- list_as_tuple([]) == ()

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0656 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def list_as_tuple(values: list[str]) -> tuple[str, ...]:
    raise NotImplementedError("TODO: PB0656")


def self_test() -> None:
    assert list_as_tuple(['a', 'b']) == ('a', 'b')
    assert list_as_tuple(['x']) == ('x',)
    assert list_as_tuple([]) == ()
