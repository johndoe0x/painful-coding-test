"""
PB0730 — 중복된 항목의 횟수

Chapter: Dictionaries
Topic: Dict Practice
Seed: 73 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 번 이상 등장한 값과 그 전체 등장 횟수만 반환한다.

연습 초점
---------
전체 빈도 계산 후 딕셔너리 필터링

구현할 함수
-----------
def dict_duplicate_counts(values: list[str]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- dict_duplicate_counts(['a', 'b', 'a', 'c', 'b', 'b']) == {'a': 2, 'b': 3}
- dict_duplicate_counts([]) == {}
- dict_duplicate_counts(['x']) == {}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0730 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_duplicate_counts(values: list[str]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0730")


def self_test() -> None:
    assert dict_duplicate_counts(['a', 'b', 'a', 'c', 'b', 'b']) == {'a': 2, 'b': 3}
    assert dict_duplicate_counts([]) == {}
    assert dict_duplicate_counts(['x']) == {}
