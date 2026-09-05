"""
PB0670 — 고유값 개수 보고서

Chapter: Sets
Topic: Intro to Sets
Seed: 67 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
unique에는 고유값 set, count에는 그 개수를 담아 반환한다.

연습 초점
---------
set 값과 cardinality를 딕셔너리로 구성

구현할 함수
-----------
def set_cardinality_report(values: list[str]) -> dict[str, object]:

예시 및 필수 테스트
-------------------
- set_cardinality_report(['a', 'b', 'a']) == {'unique': {'a', 'b'}, 'count': 2}
- set_cardinality_report([]) == {'unique': set(), 'count': 0}
- set_cardinality_report(['x']) == {'unique': {'x'}, 'count': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0670 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_cardinality_report(values: list[str]) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0670")


def self_test() -> None:
    assert set_cardinality_report(['a', 'b', 'a']) == {'unique': {'a', 'b'}, 'count': 2}
    assert set_cardinality_report([]) == {'unique': set(), 'count': 0}
    assert set_cardinality_report(['x']) == {'unique': {'x'}, 'count': 1}
