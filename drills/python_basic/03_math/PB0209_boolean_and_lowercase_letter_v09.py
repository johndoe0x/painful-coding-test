"""
PB0209 — 소문자 영문자

Chapter: Math
Topic: Boolean AND
Seed: 21 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: bool_and

문제
----
character 길이가 정확히 1이고 'a'부터 'z' 사이이면 True를 반환하세요.

연습 초점
---------
형태와 값 범위의 AND

구현할 함수
-----------
def is_lowercase_letter(character: str) -> bool:

필수 구현 방식
--------------
- 논리 연산자 and를 사용한다.

예시 및 필수 테스트
-------------------
- is_lowercase_letter('a') is True and is_lowercase_letter('z') is True
- is_lowercase_letter('') is False
- is_lowercase_letter('A') is False and is_lowercase_letter('ab') is False and is_lowercase_letter('é') is False and is_lowercase_letter('0') is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0209 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_lowercase_letter(character: str) -> bool:
    raise NotImplementedError("TODO: PB0209")


def self_test() -> None:
    assert is_lowercase_letter('a') is True and is_lowercase_letter('z') is True
    assert is_lowercase_letter('') is False
    assert is_lowercase_letter('A') is False and is_lowercase_letter('ab') is False and is_lowercase_letter('é') is False and is_lowercase_letter('0') is False
