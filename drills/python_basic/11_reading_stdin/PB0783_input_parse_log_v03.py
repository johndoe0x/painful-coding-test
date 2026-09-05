"""
PB0783 — 로그 레벨과 메시지

Chapter: Reading Stdin
Topic: Read Input Practice
Seed: 79 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
첫 '|'를 기준으로 level과 message를 나누고 양쪽 공백을 제거한다.

연습 초점
---------
최대 한 번 split하는 로그 파싱

구현할 함수
-----------
def input_parse_log(line: str) -> tuple[str, str]:

예시 및 필수 테스트
-------------------
- input_parse_log('INFO | started') == ('INFO', 'started')
- input_parse_log('ERROR|a|b') == ('ERROR', 'a|b')
- input_parse_log(' | ') == ('', '')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0783 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_log(line: str) -> tuple[str, str]:
    raise NotImplementedError("TODO: PB0783")


def self_test() -> None:
    assert input_parse_log('INFO | started') == ('INFO', 'started')
    assert input_parse_log('ERROR|a|b') == ('ERROR', 'a|b')
    assert input_parse_log(' | ') == ('', '')
