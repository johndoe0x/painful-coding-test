"""
PB0130 — 첫 타입 변경 위치

Chapter: Variables
Topic: Dynamic Typing
Seed: 13 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
직전 값과 실제 타입이 처음 달라지는 값의 인덱스를 반환하고, 없으면 -1을 반환하세요.

연습 초점
---------
동적 타입 전환의 위치 탐색

구현할 함수
-----------
def first_type_change_index(values: list[object]) -> int:

예시 및 필수 테스트
-------------------
- first_type_change_index([1, 2, 'x']) == 2
- first_type_change_index([]) == -1
- first_type_change_index([True, 0]) == 1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0130 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_type_change_index(values: list[object]) -> int:
    raise NotImplementedError("TODO: PB0130")


def self_test() -> None:
    assert first_type_change_index([1, 2, 'x']) == 2
    assert first_type_change_index([]) == -1
    assert first_type_change_index([True, 0]) == 1
