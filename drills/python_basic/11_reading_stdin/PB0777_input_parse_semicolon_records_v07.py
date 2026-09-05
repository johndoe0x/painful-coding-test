"""
PB0777 — 세미콜론 key:value 레코드

Chapter: Reading Stdin
Topic: Parse Input
Seed: 78 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
'key:value' 항목들을 세미콜론으로 나눠 int value 딕셔너리로 반환한다. 빈 text는 빈 딕셔너리다.

연습 초점
---------
두 단계 구분자 파싱과 dict 구축

구현할 함수
-----------
def input_parse_semicolon_records(text: str) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- input_parse_semicolon_records('a:1;b:2') == {'a': 1, 'b': 2}
- input_parse_semicolon_records('') == {}
- input_parse_semicolon_records('x:-1') == {'x': -1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0777 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_semicolon_records(text: str) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0777")


def self_test() -> None:
    assert input_parse_semicolon_records('a:1;b:2') == {'a': 1, 'b': 2}
    assert input_parse_semicolon_records('') == {}
    assert input_parse_semicolon_records('x:-1') == {'x': -1}
