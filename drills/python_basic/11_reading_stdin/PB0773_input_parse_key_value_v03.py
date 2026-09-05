"""
PB0773 — 첫 등호 기준 key-value

Chapter: Reading Stdin
Topic: Parse Input
Seed: 78 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
첫 번째 '='만 구분자로 사용하고 양쪽 공백을 제거해 (key, value)를 반환한다.

연습 초점
---------
split 최대 횟수와 tuple 구성

구현할 함수
-----------
def input_parse_key_value(line: str) -> tuple[str, str]:

예시 및 필수 테스트
-------------------
- input_parse_key_value('name = Ada') == ('name', 'Ada')
- input_parse_key_value('x=a=b') == ('x', 'a=b')
- input_parse_key_value(' = ') == ('', '')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0773 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_key_value(line: str) -> tuple[str, str]:
    raise NotImplementedError("TODO: PB0773")


def self_test() -> None:
    assert input_parse_key_value('name = Ada') == ('name', 'Ada')
    assert input_parse_key_value('x=a=b') == ('x', 'a=b')
    assert input_parse_key_value(' = ') == ('', '')
