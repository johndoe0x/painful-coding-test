"""
PB0770 — 이름·나이·점수 변환

Chapter: Reading Stdin
Topic: Type Conversion with Input
Seed: 77 / 82
Variant: 10 / 10
Time cap: 150 seconds
Source checks:

문제
----
쉼표로 구분된 name, age, score를 각각 str, int, float로 변환한다. 각 필드의 공백을 제거한다.

연습 초점
---------
세 필드 분리와 필드별 타입 캐스팅

구현할 함수
-----------
def input_parse_person_score(line: str) -> tuple[str, int, float]:

예시 및 필수 테스트
-------------------
- input_parse_person_score('Ada,36,98.5') == ('Ada', 36, 98.5)
- input_parse_person_score(' Kim , 0 , 0 ') == ('Kim', 0, 0.0)
- input_parse_person_score('A,-1,2.5') == ('A', -1, 2.5)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0770 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_person_score(line: str) -> tuple[str, int, float]:
    raise NotImplementedError("TODO: PB0770")


def self_test() -> None:
    assert input_parse_person_score('Ada,36,98.5') == ('Ada', 36, 98.5)
    assert input_parse_person_score(' Kim , 0 , 0 ') == ('Kim', 0, 0.0)
    assert input_parse_person_score('A,-1,2.5') == ('A', -1, 2.5)
