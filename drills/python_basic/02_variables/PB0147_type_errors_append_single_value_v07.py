"""
PB0147 — 리스트에 단일 값 추가

Chapter: Variables
Topic: Type Errors
Seed: 15 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
list와 int를 직접 더하지 말고 원본을 보존한 채 value 하나를 끝에 추가하세요.

연습 초점
---------
컬렉션과 원소 타입 구분

구현할 함수
-----------
def append_single_value(values: list[int], value: int) -> list[int]:

예시 및 필수 테스트
-------------------
- append_single_value([1, 2], 3) == [1, 2, 3]
- append_single_value([], 0) == [0]
- append_single_value([1], 1) == [1, 1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0147 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def append_single_value(values: list[int], value: int) -> list[int]:
    raise NotImplementedError("TODO: PB0147")


def self_test() -> None:
    assert append_single_value([1, 2], 3) == [1, 2, 3]
    assert append_single_value([], 0) == [0]
    assert append_single_value([1], 1) == [1, 1]
