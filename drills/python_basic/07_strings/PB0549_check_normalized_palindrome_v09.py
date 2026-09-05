"""
PB0549 — 공백과 대소문자를 무시한 회문

Chapter: Strings
Topic: Reversing a String
Seed: 55 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: reverse_slice

문제
----
공백 문자를 모두 제거하고 소문자로 바꾼 결과가 뒤집어도 같으면 True를 반환한다.

연습 초점
---------
비교 전에 정규화한 문자열 하나를 만들고 역순과 비교한다.

구현할 함수
-----------
def is_space_insensitive_palindrome(text: str) -> bool:

필수 구현 방식
--------------
- step이 -1인 역방향 슬라이스를 사용한다.

예시 및 필수 테스트
-------------------
- is_space_insensitive_palindrome('Never odd or even') is True
- is_space_insensitive_palindrome('Python') is False
- is_space_insensitive_palindrome('   ') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0549 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_space_insensitive_palindrome(text: str) -> bool:
    raise NotImplementedError("TODO: PB0549")


def self_test() -> None:
    assert is_space_insensitive_palindrome('Never odd or even') is True
    assert is_space_insensitive_palindrome('Python') is False
    assert is_space_insensitive_palindrome('   ') is True
