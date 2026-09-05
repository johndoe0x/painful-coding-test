"""
PB0785 — bool token 목록

Chapter: Reading Stdin
Topic: Read Input Practice
Seed: 79 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
공백 token 각각을 대소문자 무시 true 여부로 bool 변환한다.

연습 초점
---------
token별 문자열 정규화와 bool 생성

구현할 함수
-----------
def input_parse_flags(line: str) -> list[bool]:

예시 및 필수 테스트
-------------------
- input_parse_flags('true false TRUE') == [True, False, True]
- input_parse_flags('') == []
- input_parse_flags('yes 1') == [False, False]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0785 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_flags(line: str) -> list[bool]:
    raise NotImplementedError("TODO: PB0785")


def self_test() -> None:
    assert input_parse_flags('true false TRUE') == [True, False, True]
    assert input_parse_flags('') == []
    assert input_parse_flags('yes 1') == [False, False]
