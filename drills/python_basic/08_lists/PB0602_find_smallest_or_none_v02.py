"""
PB0602 — 최솟값 또는 None

Chapter: Lists
Topic: List Functions
Seed: 61 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
values가 비어 있으면 None을, 아니면 min 결과를 반환한다.

연습 초점
---------
min을 호출하기 전에 빈 리스트를 처리한다.

구현할 함수
-----------
def smallest_or_none(values: list[int]) -> int | None:

예시 및 필수 테스트
-------------------
- smallest_or_none([4, 1, 7]) == 1
- smallest_or_none([-2, -5]) == -5
- smallest_or_none([]) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0602 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def smallest_or_none(values: list[int]) -> int | None:
    raise NotImplementedError("TODO: PB0602")


def self_test() -> None:
    assert smallest_or_none([4, 1, 7]) == 1
    assert smallest_or_none([-2, -5]) == -5
    assert smallest_or_none([]) is None
