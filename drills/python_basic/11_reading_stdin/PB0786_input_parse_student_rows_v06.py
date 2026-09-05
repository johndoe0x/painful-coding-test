"""
PB0786 — 학생별 마지막 점수

Chapter: Reading Stdin
Topic: Read Input Practice
Seed: 79 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 'name score' 줄을 파싱한다. 같은 name이 다시 나오면 마지막 score를 저장한다.

연습 초점
---------
여러 레코드 파싱과 key 갱신

구현할 함수
-----------
def input_parse_student_rows(lines: list[str]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- input_parse_student_rows(['Ada 90', 'Kim 80']) == {'Ada': 90, 'Kim': 80}
- input_parse_student_rows([]) == {}
- input_parse_student_rows(['A 1', 'A 2']) == {'A': 2}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0786 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_student_rows(lines: list[str]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0786")


def self_test() -> None:
    assert input_parse_student_rows(['Ada 90', 'Kim 80']) == {'Ada': 90, 'Kim': 80}
    assert input_parse_student_rows([]) == {}
    assert input_parse_student_rows(['A 1', 'A 2']) == {'A': 2}
