"""
PB0615 — 빈 문자열은 추가하지 않기

Chapter: Lists
Topic: List Append
Seed: 62 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: append_call

문제
----
values를 순회하며 빈 문자열이 아닌 원소만 새 리스트에 append한다.

연습 초점
---------
조건을 통과한 원소만 결과에 추가한다.

구현할 함수
-----------
def collect_nonempty_strings(values: list[str]) -> list[str]:

필수 구현 방식
--------------
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- collect_nonempty_strings(['a', '', 'b']) == ['a', 'b']
- collect_nonempty_strings(['', '']) == []
- collect_nonempty_strings([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0615 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def collect_nonempty_strings(values: list[str]) -> list[str]:
    raise NotImplementedError("TODO: PB0615")


def self_test() -> None:
    assert collect_nonempty_strings(['a', '', 'b']) == ['a', 'b']
    assert collect_nonempty_strings(['', '']) == []
    assert collect_nonempty_strings([]) == []
