"""
PB0619 — 누적 합을 append하기

Chapter: Lists
Topic: List Append
Seed: 62 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: append_call

문제
----
values를 순회하며 현재까지의 합계를 계산해 매 단계 결과 리스트 끝에 추가한다.

연습 초점
---------
상태 갱신 순서와 append 시점을 정확히 맞춘다.

구현할 함수
-----------
def append_running_totals(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- append_running_totals([1, 2, 3]) == [1, 3, 6]
- append_running_totals([5, -2]) == [5, 3]
- append_running_totals([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0619 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def append_running_totals(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0619")


def self_test() -> None:
    assert append_running_totals([1, 2, 3]) == [1, 3, 6]
    assert append_running_totals([5, -2]) == [5, 3]
    assert append_running_totals([]) == []
