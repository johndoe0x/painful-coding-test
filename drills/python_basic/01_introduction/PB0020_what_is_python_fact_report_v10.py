"""
PB0020 — Python 정보 보고서

Chapter: Introduction
Topic: What is Python?
Seed: 02 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
facts를 바꾸지 않고 {'language': 'Python', 'fact_count': 개수, 'facts': 복사본}을 반환하세요.

연습 초점
---------
리스트 복사와 요약 메타데이터

구현할 함수
-----------
def python_fact_report(facts: list[str]) -> dict[str, object]:

예시 및 필수 테스트
-------------------
- python_fact_report(['dynamic', 'interpreted']) == {'language': 'Python', 'fact_count': 2, 'facts': ['dynamic', 'interpreted']}
- python_fact_report([]) == {'language': 'Python', 'fact_count': 0, 'facts': []}
- python_fact_report(['']) == {'language': 'Python', 'fact_count': 1, 'facts': ['']}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0020 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def python_fact_report(facts: list[str]) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0020")


def self_test() -> None:
    assert python_fact_report(['dynamic', 'interpreted']) == {'language': 'Python', 'fact_count': 2, 'facts': ['dynamic', 'interpreted']}
    assert python_fact_report([]) == {'language': 'Python', 'fact_count': 0, 'facts': []}
    assert python_fact_report(['']) == {'language': 'Python', 'fact_count': 1, 'facts': ['']}
