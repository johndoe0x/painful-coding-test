"""
PB0056 — 가중치 설명

Chapter: Introduction
Topic: Comments
Seed: 06 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: comment

문제
----
exam_weight를 시험 비중으로 사용해 최종 점수를 계산하고 가중치 합이 1이 되는 이유를 주석으로 작성하세요.

연습 초점
---------
숫자의 의미를 드러내는 주석

구현할 함수
-----------
def weighted_course_score(exam: float, project: float, exam_weight: float) -> float:

필수 구현 방식
--------------
- 함수 본문에 계산 이유를 설명하는 주석을 한 줄 이상 작성한다.

예시 및 필수 테스트
-------------------
- weighted_course_score(80, 100, 0.75) == 85.0
- weighted_course_score(0, 100, 0) == 100.0
- weighted_course_score(100, 0, 1) == 100.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0056 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def weighted_course_score(exam: float, project: float, exam_weight: float) -> float:
    raise NotImplementedError("TODO: PB0056")


def self_test() -> None:
    assert weighted_course_score(80, 100, 0.75) == 85.0
    assert weighted_course_score(0, 100, 0) == 100.0
    assert weighted_course_score(100, 0, 1) == 100.0
