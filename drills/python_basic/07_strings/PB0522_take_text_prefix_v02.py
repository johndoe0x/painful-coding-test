"""
PB0522 — 앞에서 n글자 가져오기

Chapter: Strings
Topic: String Slicing Part 1
Seed: 53 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
size가 0 이상이라고 가정하고 text의 앞 size글자를 반환한다.

연습 초점
---------
시작을 생략한 슬라이스가 길이를 넘어가도 안전함을 익힌다.

구현할 함수
-----------
def take_prefix(text: str, size: int) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- take_prefix('python', 3) == 'pyt'
- take_prefix('hi', 5) == 'hi'
- take_prefix('abc', 0) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0522 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def take_prefix(text: str, size: int) -> str:
    raise NotImplementedError("TODO: PB0522")


def self_test() -> None:
    assert take_prefix('python', 3) == 'pyt'
    assert take_prefix('hi', 5) == 'hi'
    assert take_prefix('abc', 0) == ''
