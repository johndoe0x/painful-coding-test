"""
PB0760 — 단어 사이 공백 하나로

Chapter: Reading Stdin
Topic: Reading Input
Seed: 76 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
앞뒤 공백을 없애고 단어 사이의 연속 공백 문자를 공백 한 칸으로 바꾼다.

연습 초점
---------
split과 단일 공백 join 조합

구현할 함수
-----------
def line_normalize_spaces(line: str) -> str:

예시 및 필수 테스트
-------------------
- line_normalize_spaces('  a   b  ') == 'a b'
- line_normalize_spaces('') == ''
- line_normalize_spaces('single') == 'single'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0760 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def line_normalize_spaces(line: str) -> str:
    raise NotImplementedError("TODO: PB0760")


def self_test() -> None:
    assert line_normalize_spaces('  a   b  ') == 'a b'
    assert line_normalize_spaces('') == ''
    assert line_normalize_spaces('single') == 'single'
