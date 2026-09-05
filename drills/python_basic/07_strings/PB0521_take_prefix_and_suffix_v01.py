"""
PB0521 — 앞뒤 조각 함께 자르기

Chapter: Strings
Topic: String Slicing Part 1
Seed: 53 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
text의 앞 size글자와 뒤 size글자를 tuple로 반환하며 size는 0 이상이다.

연습 초점
---------
양수 범위 슬라이스와 음수 시작 슬라이스를 나란히 사용한다.

구현할 함수
-----------
def prefix_suffix(text: str, size: int) -> tuple[str, str]:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- prefix_suffix('python', 2) == ('py', 'on')
- prefix_suffix('cat', 5) == ('cat', 'cat')
- prefix_suffix('abc', 0) == ('', '')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0521 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def prefix_suffix(text: str, size: int) -> tuple[str, str]:
    raise NotImplementedError("TODO: PB0521")


def self_test() -> None:
    assert prefix_suffix('python', 2) == ('py', 'on')
    assert prefix_suffix('cat', 5) == ('cat', 'cat')
    assert prefix_suffix('abc', 0) == ('', '')
