"""
PB0207 — 문자열 길이 범위

Chapter: Math
Topic: Boolean AND
Seed: 21 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: bool_and

문제
----
text 길이가 minimum 이상 maximum 이하이면 True를 반환하세요.

연습 초점
---------
길이에 대한 양쪽 경계

구현할 함수
-----------
def has_length_between(text: str, minimum: int, maximum: int) -> bool:

필수 구현 방식
--------------
- 논리 연산자 and를 사용한다.

예시 및 필수 테스트
-------------------
- has_length_between('abc', 2, 4) is True and has_length_between('ab', 2, 4) is True and has_length_between('abcd', 2, 4) is True
- has_length_between('', 0, 0) is True
- has_length_between('abcde', 1, 4) is False and has_length_between('a', 2, 4) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0207 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def has_length_between(text: str, minimum: int, maximum: int) -> bool:
    raise NotImplementedError("TODO: PB0207")


def self_test() -> None:
    assert has_length_between('abc', 2, 4) is True and has_length_between('ab', 2, 4) is True and has_length_between('abcd', 2, 4) is True
    assert has_length_between('', 0, 0) is True
    assert has_length_between('abcde', 1, 4) is False and has_length_between('a', 2, 4) is False
