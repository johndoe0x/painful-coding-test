"""
PB0039 — 번호가 붙은 줄

Chapter: Introduction
Topic: Printing Text
Seed: 04 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 줄에 1부터 시작하는 번호와 '. '를 붙인 문자열 리스트를 반환하세요.

연습 초점
---------
순서 번호를 포함한 출력

구현할 함수
-----------
def number_lines(lines: list[str]) -> list[str]:

예시 및 필수 테스트
-------------------
- number_lines(['one', 'two']) == ['1. one', '2. two']
- number_lines([]) == []
- number_lines(['']) == ['1. ']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0039 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def number_lines(lines: list[str]) -> list[str]:
    raise NotImplementedError("TODO: PB0039")


def self_test() -> None:
    assert number_lines(['one', 'two']) == ['1. one', '2. two']
    assert number_lines([]) == []
    assert number_lines(['']) == ['1. ']
