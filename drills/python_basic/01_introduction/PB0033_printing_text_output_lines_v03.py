"""
PB0033 — 출력 줄 합치기

Chapter: Introduction
Topic: Printing Text
Seed: 04 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 원소가 한 줄이 되도록 줄바꿈 문자로 결합하세요. 빈 리스트는 빈 문자열입니다.

연습 초점
---------
여러 출력 줄과 개행 문자

구현할 함수
-----------
def join_output_lines(lines: list[str]) -> str:

예시 및 필수 테스트
-------------------
- join_output_lines(['a', 'b']) == 'a\\nb'
- join_output_lines([]) == ''
- join_output_lines(['']) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0033 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def join_output_lines(lines: list[str]) -> str:
    raise NotImplementedError("TODO: PB0033")


def self_test() -> None:
    assert join_output_lines(['a', 'b']) == 'a\nb'
    assert join_output_lines([]) == ''
    assert join_output_lines(['']) == ''
