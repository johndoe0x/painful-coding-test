"""
PB0049 — 합격 경계 비교 고치기

Chapter: Introduction
Topic: Code Errors
Seed: 05 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
starter는 >를 사용해 minimum과 같은 점수를 탈락시킵니다. score가 minimum 이상일 때 True를 반환하세요.

연습 초점
---------
초과와 이상의 경계 포함 차이

구현할 함수
-----------
def is_passing_score(score: int, minimum: int) -> bool:

예시 및 필수 테스트
-------------------
- is_passing_score(80, 80) is True
- is_passing_score(79, 80) is False
- is_passing_score(81, 80) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0049 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_passing_score(score: int, minimum: int) -> bool:
    return score > minimum


def self_test() -> None:
    assert is_passing_score(80, 80) is True
    assert is_passing_score(79, 80) is False
    assert is_passing_score(81, 80) is True
