"""
PB0373 — 빈 리스트 대체

Chapter: Conditional Statements
Topic: Truthy and Falsy
Seed: 38 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: if

문제
----
values가 truthy면 복사본을, None이나 빈 리스트면 [0]을 반환한다.

연습 초점
---------
None과 빈 컬렉션의 falsy 특성

구현할 함수
-----------
def normalize_sequence_default(values: list[int] | None) -> list[int]:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- normalize_sequence_default([1, 2]) == [1, 2]
- normalize_sequence_default([]) == [0]
- normalize_sequence_default(None) == [0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0373 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def normalize_sequence_default(values: list[int] | None) -> list[int]:
    raise NotImplementedError("TODO: PB0373")


def self_test() -> None:
    assert normalize_sequence_default([1, 2]) == [1, 2]
    assert normalize_sequence_default([]) == [0]
    assert normalize_sequence_default(None) == [0]
