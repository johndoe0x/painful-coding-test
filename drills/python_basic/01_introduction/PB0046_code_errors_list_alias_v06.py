"""
PB0046 — 리스트 별칭 오류 고치기

Chapter: Introduction
Topic: Code Errors
Seed: 05 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
starter는 new_values = values로 같은 리스트를 가리켜 원본까지 변경합니다. 원본은 보존하고 value를 추가한 별도 복사본을 만들어 (원본 내용의 복사본, 새 리스트)로 반환하세요.

연습 초점
---------
대입으로 생기는 별칭과 얕은 복사의 차이

구현할 함수
-----------
def append_without_alias(values: list[int], value: int) -> tuple[list[int], list[int]]:

예시 및 필수 테스트
-------------------
- append_without_alias([1, 2], 3) == ([1, 2], [1, 2, 3])
- append_without_alias([], 1) == ([], [1])
- append_without_alias([0], 0) == ([0], [0, 0])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0046 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def append_without_alias(values: list[int], value: int) -> tuple[list[int], list[int]]:
    new_values = values
    new_values.append(value)
    return values, new_values


def self_test() -> None:
    assert append_without_alias([1, 2], 3) == ([1, 2], [1, 2, 3])
    assert append_without_alias([], 1) == ([], [1])
    assert append_without_alias([0], 0) == ([0], [0, 0])
