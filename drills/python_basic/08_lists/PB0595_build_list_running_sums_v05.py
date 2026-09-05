"""
PB0595 — 리스트 누적 합 만들기

Chapter: Lists
Topic: List Looping
Seed: 60 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: for

문제
----
각 원소까지의 누적 합을 같은 길이의 리스트로 반환한다.

연습 초점
---------
누적 상태를 갱신한 직후 결과 리스트에 기록한다.

구현할 함수
-----------
def list_running_sums(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- list_running_sums([2, 3, 4]) == [2, 5, 9]
- list_running_sums([-1, 1, 5]) == [-1, 0, 5]
- list_running_sums([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0595 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def list_running_sums(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0595")


def self_test() -> None:
    assert list_running_sums([2, 3, 4]) == [2, 5, 9]
    assert list_running_sums([-1, 1, 5]) == [-1, 0, 5]
    assert list_running_sums([]) == []
