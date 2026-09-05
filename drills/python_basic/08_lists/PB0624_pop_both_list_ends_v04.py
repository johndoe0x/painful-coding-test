"""
PB0624 — 양 끝 원소 꺼내기

Chapter: Lists
Topic: List Pop
Seed: 63 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: pop_call

문제
----
원소가 두 개 이상이면 복사본의 첫 값과 마지막 값을 제거해 (남은 리스트, (첫 값, 마지막 값))을 반환하고 아니면 (복사본, None)을 반환한다.

연습 초점
---------
두 번의 pop에서 인덱스 이동과 제거 순서를 고려한다.

구현할 함수
-----------
def pop_both_ends(values: list[int]) -> tuple[list[int], tuple[int, int] | None]:

필수 구현 방식
--------------
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3, 4]), pop_both_ends(items) == ([2, 3], (1, 4)) and items == [1, 2, 3, 4])[-1] is True
- pop_both_ends([1, 2]) == ([], (1, 2))
- pop_both_ends([1]) == ([1], None)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0624 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def pop_both_ends(values: list[int]) -> tuple[list[int], tuple[int, int] | None]:
    raise NotImplementedError("TODO: PB0624")


def self_test() -> None:
    assert ((items := [1, 2, 3, 4]), pop_both_ends(items) == ([2, 3], (1, 4)) and items == [1, 2, 3, 4])[-1] is True
    assert pop_both_ends([1, 2]) == ([], (1, 2))
    assert pop_both_ends([1]) == ([1], None)
