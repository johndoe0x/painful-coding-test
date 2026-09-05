"""
PB0107 — 첫 값과 나머지 분리

Chapter: Variables
Topic: Multiple Assignments
Seed: 11 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: multiple_assignment

문제
----
빈 리스트면 (None, []), 아니면 확장 언패킹으로 첫 값과 나머지를 분리하세요.

연습 초점
---------
별표를 사용한 시퀀스 언패킹

구현할 함수
-----------
def split_head_tail(values: list[int]) -> tuple[int | None, list[int]]:

필수 구현 방식
--------------
- tuple/list 다중 할당 또는 swap 형태를 사용한다.

예시 및 필수 테스트
-------------------
- split_head_tail([1, 2, 3]) == (1, [2, 3])
- split_head_tail([]) == (None, [])
- split_head_tail([7]) == (7, [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0107 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def split_head_tail(values: list[int]) -> tuple[int | None, list[int]]:
    raise NotImplementedError("TODO: PB0107")


def self_test() -> None:
    assert split_head_tail([1, 2, 3]) == (1, [2, 3])
    assert split_head_tail([]) == (None, [])
    assert split_head_tail([7]) == (7, [])
