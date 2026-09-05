"""
PB0455 — 같은 값의 모든 쌍

Chapter: Loops
Topic: Nested Loops
Seed: 46 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: nested_loop

문제
----
left와 right의 모든 원소 조합을 중첩 for로 확인해 값이 같은 (left값, right값) 쌍을 반환한다.

연습 초점
---------
두 컬렉션의 데카르트 곱 탐색

구현할 함수
-----------
def equal_cartesian_pairs(left: list[int], right: list[int]) -> list[tuple[int, int]]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- equal_cartesian_pairs([1, 2], [2, 1]) == [(1, 1), (2, 2)]
- equal_cartesian_pairs([], [1]) == []
- equal_cartesian_pairs([1, 1], [1]) == [(1, 1), (1, 1)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0455 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def equal_cartesian_pairs(left: list[int], right: list[int]) -> list[tuple[int, int]]:
    raise NotImplementedError("TODO: PB0455")


def self_test() -> None:
    assert equal_cartesian_pairs([1, 2], [2, 1]) == [(1, 1), (2, 2)]
    assert equal_cartesian_pairs([], [1]) == []
    assert equal_cartesian_pairs([1, 1], [1]) == [(1, 1), (1, 1)]
