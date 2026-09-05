"""
PB0726 — 가장 자주 나온 값

Chapter: Dictionaries
Topic: Dict Practice
Seed: 73 / 82
Variant: 06 / 10
Time cap: 150 seconds
Source checks:

문제
----
가장 많이 등장한 값을 반환한다. 동률이면 먼저 등장한 값, 입력이 비면 None을 반환한다.

연습 초점
---------
빈도 딕셔너리와 안정적인 최댓값 선택

구현할 함수
-----------
def dict_most_frequent(values: list[str]) -> str | None:

예시 및 필수 테스트
-------------------
- dict_most_frequent(['a', 'b', 'a']) == 'a'
- dict_most_frequent([]) is None
- dict_most_frequent(['b', 'a']) == 'b'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0726 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_most_frequent(values: list[str]) -> str | None:
    raise NotImplementedError("TODO: PB0726")


def self_test() -> None:
    assert dict_most_frequent(['a', 'b', 'a']) == 'a'
    assert dict_most_frequent([]) is None
    assert dict_most_frequent(['b', 'a']) == 'b'
