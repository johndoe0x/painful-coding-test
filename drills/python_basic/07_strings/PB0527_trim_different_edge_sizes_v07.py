"""
PB0527 — 앞뒤에서 서로 다르게 잘라내기

Chapter: Strings
Topic: String Slicing Part 1
Seed: 53 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
앞 left_count글자와 뒤 right_count글자를 제거하며 두 값은 0 이상이고 합이 text 길이 이하라고 가정한다.

연습 초점
---------
0인 오른쪽 제거량을 포함해 동적인 슬라이스 끝 경계를 처리한다.

구현할 함수
-----------
def trim_text(text: str, left_count: int, right_count: int) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- trim_text('abcdefgh', 2, 3) == 'cde'
- trim_text('python', 0, 2) == 'pyth'
- trim_text('abc', 1, 0) == 'bc'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0527 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def trim_text(text: str, left_count: int, right_count: int) -> str:
    raise NotImplementedError("TODO: PB0527")


def self_test() -> None:
    assert trim_text('abcdefgh', 2, 3) == 'cde'
    assert trim_text('python', 0, 2) == 'pyth'
    assert trim_text('abc', 1, 0) == 'bc'
