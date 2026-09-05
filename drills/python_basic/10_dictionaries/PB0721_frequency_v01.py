"""
PB0721 — 문자열 빈도표

Chapter: Dictionaries
Topic: Dict Practice
Seed: 73 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 문자열이 등장한 횟수를 딕셔너리로 반환한다.

연습 초점
---------
get 기본값을 이용한 빈도 누적

구현할 함수
-----------
def frequency(values: list[str]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- frequency(['a', 'b', 'a']) == {'a': 2, 'b': 1}
- frequency([]) == {}
- frequency(['x']) == {'x': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0721 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def frequency(values: list[str]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0721")


def self_test() -> None:
    assert frequency(['a', 'b', 'a']) == {'a': 2, 'b': 1}
    assert frequency([]) == {}
    assert frequency(['x']) == {'x': 1}
