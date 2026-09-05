"""
PB0601 — 리스트 기본 통계

Chapter: Lists
Topic: List Functions
Seed: 61 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
비어 있지 않은 values에 대해 len, min, max, sum 결과를 해당 이름의 키로 반환한다.

연습 초점
---------
여러 리스트 내장 함수를 하나의 명확한 결과 구조에 담는다.

구현할 함수
-----------
def list_stats(values: list[int]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- list_stats([2, 5]) == {'len': 2, 'min': 2, 'max': 5, 'sum': 7}
- list_stats([-3, 0, 4]) == {'len': 3, 'min': -3, 'max': 4, 'sum': 1}
- list_stats([7]) == {'len': 1, 'min': 7, 'max': 7, 'sum': 7}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0601 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def list_stats(values: list[int]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0601")


def self_test() -> None:
    assert list_stats([2, 5]) == {'len': 2, 'min': 2, 'max': 5, 'sum': 7}
    assert list_stats([-3, 0, 4]) == {'len': 3, 'min': -3, 'max': 4, 'sum': 1}
    assert list_stats([7]) == {'len': 1, 'min': 7, 'max': 7, 'sum': 7}
