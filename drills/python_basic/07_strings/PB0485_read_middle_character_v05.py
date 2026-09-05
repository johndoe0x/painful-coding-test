"""
PB0485 — 가운데 글자 찾기

Chapter: Strings
Topic: String Indexing
Seed: 49 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
길이가 홀수인 문자열은 가운데 글자를 반환하고, 빈 문자열이나 짝수 길이는 None을 반환한다.

연습 초점
---------
len과 정수 나눗셈으로 가운데 인덱스를 계산한다.

구현할 함수
-----------
def middle_character(text: str) -> str | None:

예시 및 필수 테스트
-------------------
- middle_character('abcde') == 'c'
- middle_character('abcd') is None
- middle_character('') is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0485 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def middle_character(text: str) -> str | None:
    raise NotImplementedError("TODO: PB0485")


def self_test() -> None:
    assert middle_character('abcde') == 'c'
    assert middle_character('abcd') is None
    assert middle_character('') is None
