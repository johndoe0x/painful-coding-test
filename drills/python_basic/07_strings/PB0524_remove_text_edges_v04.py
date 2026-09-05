"""
PB0524 — 양 끝 글자 제거하기

Chapter: Strings
Topic: String Slicing Part 1
Seed: 53 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
첫 글자와 마지막 글자를 제외한 가운데 부분을 반환하며 길이가 2 이하면 ''를 반환한다.

연습 초점
---------
고정된 시작·끝 경계의 슬라이싱을 연습한다.

구현할 함수
-----------
def remove_text_edges(text: str) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- remove_text_edges('python') == 'ytho'
- remove_text_edges('ab') == ''
- remove_text_edges('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0524 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def remove_text_edges(text: str) -> str:
    raise NotImplementedError("TODO: PB0524")


def self_test() -> None:
    assert remove_text_edges('python') == 'ytho'
    assert remove_text_edges('ab') == ''
    assert remove_text_edges('') == ''
