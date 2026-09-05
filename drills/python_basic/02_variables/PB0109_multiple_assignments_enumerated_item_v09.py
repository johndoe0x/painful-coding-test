"""
PB0109 — 번호와 값 언패킹

Chapter: Variables
Topic: Multiple Assignments
Seed: 11 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: multiple_assignment

문제
----
enumerate가 주는 index와 value를 다중 할당해 '<index>:<value>' 리스트를 반환하세요.

연습 초점
---------
반복 중 tuple 언패킹

구현할 함수
-----------
def enumerate_items(values: list[str], start: int) -> list[str]:

필수 구현 방식
--------------
- tuple/list 다중 할당 또는 swap 형태를 사용한다.

예시 및 필수 테스트
-------------------
- enumerate_items(['a', 'b'], 1) == ['1:a', '2:b']
- enumerate_items([], 5) == []
- enumerate_items([''], 0) == ['0:']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0109 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def enumerate_items(values: list[str], start: int) -> list[str]:
    raise NotImplementedError("TODO: PB0109")


def self_test() -> None:
    assert enumerate_items(['a', 'b'], 1) == ['1:a', '2:b']
    assert enumerate_items([], 5) == []
    assert enumerate_items([''], 0) == ['0:']
