"""
PB0729 — 10점 단위 점수 구간

Chapter: Dictionaries
Topic: Dict Practice
Seed: 73 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 점수를 10으로 내림한 구간 시작값에 묶어 개수를 센다. 예: 87은 80 구간이다.

연습 초점
---------
계산된 key로 빈도 누적

구현할 함수
-----------
def dict_score_histogram(scores: list[int]) -> dict[int, int]:

예시 및 필수 테스트
-------------------
- dict_score_histogram([87, 82, 91]) == {80: 2, 90: 1}
- dict_score_histogram([]) == {}
- dict_score_histogram([0, 9, 10]) == {0: 2, 10: 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0729 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_score_histogram(scores: list[int]) -> dict[int, int]:
    raise NotImplementedError("TODO: PB0729")


def self_test() -> None:
    assert dict_score_histogram([87, 82, 91]) == {80: 2, 90: 1}
    assert dict_score_histogram([]) == {}
    assert dict_score_histogram([0, 9, 10]) == {0: 2, 10: 1}
