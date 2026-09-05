"""
PB0661 — 정수 중복 제거

Chapter: Sets
Topic: Intro to Sets
Seed: 67 / 82
Variant: 01 / 10
Time cap: 60 seconds
Source checks:

문제
----
values의 모든 정수를 set으로 변환해 반환한다.

연습 초점
---------
set 생성과 중복 제거

구현할 함수
-----------
def unique_values(values: list[int]) -> set[int]:

예시 및 필수 테스트
-------------------
- unique_values([1, 1, 2]) == {1, 2}
- unique_values([]) == set()
- unique_values([-1, -1, 0]) == {-1, 0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0661 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def unique_values(values: list[int]) -> set[int]:
    raise NotImplementedError("TODO: PB0661")


def self_test() -> None:
    assert unique_values([1, 1, 2]) == {1, 2}
    assert unique_values([]) == set()
    assert unique_values([-1, -1, 0]) == {-1, 0}
