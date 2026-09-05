"""
PB0545 — 거울 문자열 만들기

Chapter: Strings
Topic: Reversing a String
Seed: 55 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: reverse_slice

문제
----
text 뒤에 text의 역순을 붙여 좌우 대칭 문자열을 반환한다.

연습 초점
---------
원본 문자열과 역방향 슬라이스를 결합한다.

구현할 함수
-----------
def mirror_text(text: str) -> str:

필수 구현 방식
--------------
- step이 -1인 역방향 슬라이스를 사용한다.

예시 및 필수 테스트
-------------------
- mirror_text('abc') == 'abccba'
- mirror_text('x') == 'xx'
- mirror_text('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0545 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def mirror_text(text: str) -> str:
    raise NotImplementedError("TODO: PB0545")


def self_test() -> None:
    assert mirror_text('abc') == 'abccba'
    assert mirror_text('x') == 'xx'
    assert mirror_text('') == ''
