"""
PB0629 — 뒤에서 하나씩 교대로 분배하기

Chapter: Lists
Topic: List Pop
Seed: 63 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: pop_call

문제
----
복사본이 빌 때까지 pop하면서 첫 제거값은 left, 다음은 right에 번갈아 append해 두 리스트를 반환한다.

연습 초점
---------
스택 제거 순서와 차례 상태를 함께 관리한다.

구현할 함수
-----------
def deal_from_stack(values: list[int]) -> tuple[list[int], list[int]]:

필수 구현 방식
--------------
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3, 4]), deal_from_stack(items) == ([4, 2], [3, 1]) and items == [1, 2, 3, 4])[-1] is True
- deal_from_stack([1, 2, 3]) == ([3, 1], [2])
- deal_from_stack([]) == ([], [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0629 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def deal_from_stack(values: list[int]) -> tuple[list[int], list[int]]:
    raise NotImplementedError("TODO: PB0629")


def self_test() -> None:
    assert ((items := [1, 2, 3, 4]), deal_from_stack(items) == ([4, 2], [3, 1]) and items == [1, 2, 3, 4])[-1] is True
    assert deal_from_stack([1, 2, 3]) == ([3, 1], [2])
    assert deal_from_stack([]) == ([], [])
