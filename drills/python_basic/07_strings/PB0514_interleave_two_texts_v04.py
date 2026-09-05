"""
PB0514 — 두 문자열 번갈아 붙이기

Chapter: Strings
Topic: String Concatenation
Seed: 52 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
양쪽 글자를 같은 인덱스 순서로 번갈아 붙이고, 더 긴 쪽의 남은 부분은 끝에 붙인다.

연습 초점
---------
인덱스별 문자열 결합과 서로 다른 길이의 나머지 처리를 연습한다.

구현할 함수
-----------
def interleave_text(left: str, right: str) -> str:

예시 및 필수 테스트
-------------------
- interleave_text('abc', '123') == 'a1b2c3'
- interleave_text('ab', '1234') == 'a1b234'
- interleave_text('', 'xy') == 'xy'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0514 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def interleave_text(left: str, right: str) -> str:
    raise NotImplementedError("TODO: PB0514")


def self_test() -> None:
    assert interleave_text('abc', '123') == 'a1b2c3'
    assert interleave_text('ab', '1234') == 'a1b234'
    assert interleave_text('', 'xy') == 'xy'
