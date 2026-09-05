"""
PB0658 — tuple의 최솟값과 최댓값

Chapter: Lists
Topic: Tuples
Seed: 66 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
values가 비어 있으면 None을, 아니면 (최솟값, 최댓값) tuple을 반환한다.

연습 초점
---------
입력 tuple을 읽어 요약 결과를 새로운 고정 길이 tuple로 만든다.

구현할 함수
-----------
def tuple_extremes(values: tuple[int, ...]) -> tuple[int, int] | None:

예시 및 필수 테스트
-------------------
- tuple_extremes((3, 1, 8)) == (1, 8)
- tuple_extremes((-2, -5)) == (-5, -2)
- tuple_extremes(()) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0658 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def tuple_extremes(values: tuple[int, ...]) -> tuple[int, int] | None:
    raise NotImplementedError("TODO: PB0658")


def self_test() -> None:
    assert tuple_extremes((3, 1, 8)) == (1, 8)
    assert tuple_extremes((-2, -5)) == (-5, -2)
    assert tuple_extremes(()) is None
