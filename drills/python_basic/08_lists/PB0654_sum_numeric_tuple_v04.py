"""
PB0654 — 숫자 tuple 합계

Chapter: Lists
Topic: Tuples
Seed: 66 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
길이에 제한이 없는 정수 tuple의 모든 원소 합을 반환한다.

연습 초점
---------
가변 길이 tuple 타입 힌트와 iterable로서의 tuple을 익힌다.

구현할 함수
-----------
def tuple_total(values: tuple[int, ...]) -> int:

예시 및 필수 테스트
-------------------
- tuple_total((1, 2, 3)) == 6
- tuple_total((-2, 2)) == 0
- tuple_total(()) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0654 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def tuple_total(values: tuple[int, ...]) -> int:
    raise NotImplementedError("TODO: PB0654")


def self_test() -> None:
    assert tuple_total((1, 2, 3)) == 6
    assert tuple_total((-2, 2)) == 0
    assert tuple_total(()) == 0
