"""
PB0541 — 문자열 전체 뒤집기

Chapter: Strings
Topic: Reversing a String
Seed: 55 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: reverse_slice

문제
----
text의 글자 순서를 완전히 뒤집은 새 문자열을 반환한다.

연습 초점
---------
음수 step 슬라이스로 처음부터 끝까지 역방향 선택한다.

구현할 함수
-----------
def reverse_text(text: str) -> str:

필수 구현 방식
--------------
- step이 -1인 역방향 슬라이스를 사용한다.

예시 및 필수 테스트
-------------------
- reverse_text('abc') == 'cba'
- reverse_text('A') == 'A'
- reverse_text('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0541 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_text(text: str) -> str:
    raise NotImplementedError("TODO: PB0541")


def self_test() -> None:
    assert reverse_text('abc') == 'cba'
    assert reverse_text('A') == 'A'
    assert reverse_text('') == ''
