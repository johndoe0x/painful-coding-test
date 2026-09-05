"""
PB0507 — 짝수 위치만 대문자로

Chapter: Strings
Topic: String Looping Shorthand
Seed: 51 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: comprehension

문제
----
짝수 인덱스 글자는 대문자, 홀수 인덱스 글자는 소문자로 바꿔 반환한다.

연습 초점
---------
enumerate와 조건 표현식을 한 번의 문자열 생성에 사용한다.

구현할 함수
-----------
def alternating_case(text: str) -> str:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- alternating_case('python') == 'PyThOn'
- alternating_case('ABC') == 'AbC'
- alternating_case('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0507 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def alternating_case(text: str) -> str:
    raise NotImplementedError("TODO: PB0507")


def self_test() -> None:
    assert alternating_case('python') == 'PyThOn'
    assert alternating_case('ABC') == 'AbC'
    assert alternating_case('') == ''
