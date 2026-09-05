"""
PB0787 — CSV 사람 레코드

Chapter: Reading Stdin
Topic: Read Input Practice
Seed: 79 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
쉼표 구분 name, age, city의 공백을 제거하고 age만 int로 변환한다.

연습 초점
---------
필드 정리와 선택적 타입 변환

구현할 함수
-----------
def input_parse_person_csv(line: str) -> tuple[str, int, str]:

예시 및 필수 테스트
-------------------
- input_parse_person_csv('Ada,36,London') == ('Ada', 36, 'London')
- input_parse_person_csv(' Kim , 0 , Seoul ') == ('Kim', 0, 'Seoul')
- input_parse_person_csv('A,-1,') == ('A', -1, '')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0787 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_person_csv(line: str) -> tuple[str, int, str]:
    raise NotImplementedError("TODO: PB0787")


def self_test() -> None:
    assert input_parse_person_csv('Ada,36,London') == ('Ada', 36, 'London')
    assert input_parse_person_csv(' Kim , 0 , Seoul ') == ('Kim', 0, 'Seoul')
    assert input_parse_person_csv('A,-1,') == ('A', -1, '')
