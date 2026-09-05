"""
PB0780 — 간단한 query 문자열

Chapter: Reading Stdin
Topic: Parse Input
Seed: 78 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
&로 항목을 나누고 각 항목의 첫 '='로 key와 value를 분리한다. 빈 text는 빈 딕셔너리다.

연습 초점
---------
중첩 구분자와 split 최대 횟수

구현할 함수
-----------
def input_parse_query(text: str) -> dict[str, str]:

예시 및 필수 테스트
-------------------
- input_parse_query('a=1&b=two') == {'a': '1', 'b': 'two'}
- input_parse_query('') == {}
- input_parse_query('q=a=b') == {'q': 'a=b'}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0780 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_query(text: str) -> dict[str, str]:
    raise NotImplementedError("TODO: PB0780")


def self_test() -> None:
    assert input_parse_query('a=1&b=two') == {'a': '1', 'b': 'two'}
    assert input_parse_query('') == {}
    assert input_parse_query('q=a=b') == {'q': 'a=b'}
