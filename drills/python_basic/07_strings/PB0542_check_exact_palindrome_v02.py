"""
PB0542 — 그대로 읽어 같은지 확인하기

Chapter: Strings
Topic: Reversing a String
Seed: 55 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: reverse_slice

문제
----
대소문자와 공백을 그대로 유지한 text가 뒤집어도 같으면 True를 반환한다.

연습 초점
---------
원본과 전체 역순 슬라이스를 직접 비교한다.

구현할 함수
-----------
def is_exact_palindrome(text: str) -> bool:

필수 구현 방식
--------------
- step이 -1인 역방향 슬라이스를 사용한다.

예시 및 필수 테스트
-------------------
- is_exact_palindrome('level') is True
- is_exact_palindrome('Level') is False
- is_exact_palindrome('') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0542 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_exact_palindrome(text: str) -> bool:
    raise NotImplementedError("TODO: PB0542")


def self_test() -> None:
    assert is_exact_palindrome('level') is True
    assert is_exact_palindrome('Level') is False
    assert is_exact_palindrome('') is True
