"""
PB0286 — 지역 리스트 뒤집기

Chapter: Functions
Topic: Scope
Seed: 29 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: no_global

문제
----
원본과 지역 복사본을 뒤집은 결과를 (원본, 뒤집힌 복사본)으로 반환한다.

연습 초점
---------
가변 입력과 지역 복사본의 범위 분리

구현할 함수
-----------
def reverse_copy_local(values: list[int]) -> tuple[list[int], list[int]]:

필수 구현 방식
--------------
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- reverse_copy_local([1, 2, 3]) == ([1, 2, 3], [3, 2, 1])
- reverse_copy_local([]) == ([], [])
- reverse_copy_local([-1, 0]) == ([-1, 0], [0, -1])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0286 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_copy_local(values: list[int]) -> tuple[list[int], list[int]]:
    raise NotImplementedError("TODO: PB0286")


def self_test() -> None:
    assert reverse_copy_local([1, 2, 3]) == ([1, 2, 3], [3, 2, 1])
    assert reverse_copy_local([]) == ([], [])
    assert reverse_copy_local([-1, 0]) == ([-1, 0], [0, -1])
