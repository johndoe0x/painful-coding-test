"""
PB0194 — 양끝 중 모음

Chapter: Math
Topic: Boolean OR
Seed: 20 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: bool_or

문제
----
text가 비면 False입니다. 첫 글자 또는 마지막 글자가 영문 모음이면 대소문자와 무관하게 True를 반환하세요.

연습 초점
---------
두 위치 조건의 OR

구현할 함수
-----------
def either_end_is_vowel(text: str) -> bool:

필수 구현 방식
--------------
- 논리 연산자 or를 사용한다.

예시 및 필수 테스트
-------------------
- either_end_is_vowel('Apple') is True and either_end_is_vowel('art') is True
- either_end_is_vowel('') is False
- either_end_is_vowel('sky') is False and either_end_is_vowel('trEE') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0194 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def either_end_is_vowel(text: str) -> bool:
    raise NotImplementedError("TODO: PB0194")


def self_test() -> None:
    assert either_end_is_vowel('Apple') is True and either_end_is_vowel('art') is True
    assert either_end_is_vowel('') is False
    assert either_end_is_vowel('sky') is False and either_end_is_vowel('trEE') is True
