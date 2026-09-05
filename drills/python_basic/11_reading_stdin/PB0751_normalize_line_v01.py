"""
PB0751 — 입력 한 줄 정리

Chapter: Reading Stdin
Topic: Reading Input
Seed: 76 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
line 앞뒤의 모든 공백 문자를 제거해 반환한다.

연습 초점
---------
str.strip으로 입력 경계 정리

구현할 함수
-----------
def normalize_line(line: str) -> str:

예시 및 필수 테스트
-------------------
- normalize_line('  hello  ') == 'hello'
- normalize_line('') == ''
- normalize_line('  a b ') == 'a b'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0751 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def normalize_line(line: str) -> str:
    raise NotImplementedError("TODO: PB0751")


def self_test() -> None:
    assert normalize_line('  hello  ') == 'hello'
    assert normalize_line('') == ''
    assert normalize_line('  a b ') == 'a b'
