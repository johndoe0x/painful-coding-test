"""
PB0308 — 기본 로그 레벨

Chapter: Functions
Topic: Default Arguments
Seed: 31 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
'[<level>] <message>' 형식으로 반환하며 level 생략 시 INFO를 사용한다.

연습 초점
---------
문자열 기본값을 가진 서식 함수

구현할 함수
-----------
def log_line_default_level(message: str, level: str = 'INFO') -> str:

예시 및 필수 테스트
-------------------
- log_line_default_level('ready') == '[INFO] ready'
- log_line_default_level('bad', 'ERROR') == '[ERROR] bad'
- log_line_default_level('') == '[INFO] '

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0308 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def log_line_default_level(message: str, level: str = 'INFO') -> str:
    raise NotImplementedError("TODO: PB0308")


def self_test() -> None:
    assert log_line_default_level('ready') == '[INFO] ready'
    assert log_line_default_level('bad', 'ERROR') == '[ERROR] bad'
    assert log_line_default_level('') == '[INFO] '
