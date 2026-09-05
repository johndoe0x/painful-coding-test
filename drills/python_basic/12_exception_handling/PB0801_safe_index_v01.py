"""
PB0801 — 안전한 리스트 인덱스

Chapter: Exception Handling
Topic: Error Catching
Seed: 81 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: try

문제
----
values[index]를 반환하고 IndexError면 None을 반환한다.

연습 초점
---------
IndexError를 최소 범위에서 처리

구현할 함수
-----------
def safe_index(values: list[object], index: int) -> object | None:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- safe_index([1], 2) is None
- safe_index([1], 0) == 1
- safe_index([], 0) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0801 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def safe_index(values: list[object], index: int) -> object | None:
    raise NotImplementedError("TODO: PB0801")


def self_test() -> None:
    assert safe_index([1], 2) is None
    assert safe_index([1], 0) == 1
    assert safe_index([], 0) is None
