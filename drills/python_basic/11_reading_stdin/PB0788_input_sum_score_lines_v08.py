"""
PB0788 — 점수 줄 합계

Chapter: Reading Stdin
Topic: Read Input Practice
Seed: 79 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 'name score' 줄에서 score만 int로 변환해 모두 합한다.

연습 초점
---------
필요한 필드만 unpacking하고 누적

구현할 함수
-----------
def input_sum_score_lines(lines: list[str]) -> int:

예시 및 필수 테스트
-------------------
- input_sum_score_lines(['Ada 10', 'Kim 20']) == 30
- input_sum_score_lines([]) == 0
- input_sum_score_lines(['A -1', 'B 1']) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0788 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_sum_score_lines(lines: list[str]) -> int:
    raise NotImplementedError("TODO: PB0788")


def self_test() -> None:
    assert input_sum_score_lines(['Ada 10', 'Kim 20']) == 30
    assert input_sum_score_lines([]) == 0
    assert input_sum_score_lines(['A -1', 'B 1']) == 0
