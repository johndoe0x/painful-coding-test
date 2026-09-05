"""
PB0248 — 두 문자열 연결

Chapter: Functions
Topic: Parameters
Seed: 25 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
left와 right 사이에 separator를 넣어 반환한다.

연습 초점
---------
세 매개변수의 위치와 역할

구현할 함수
-----------
def join_text_pair(left: str, right: str, separator: str) -> str:

예시 및 필수 테스트
-------------------
- join_text_pair('a', 'b', '-') == 'a-b'
- join_text_pair('', 'b', ':') == ':b'
- join_text_pair('a', '', '') == 'a'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0248 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def join_text_pair(left: str, right: str, separator: str) -> str:
    raise NotImplementedError("TODO: PB0248")


def self_test() -> None:
    assert join_text_pair('a', 'b', '-') == 'a-b'
    assert join_text_pair('', 'b', ':') == ':b'
    assert join_text_pair('a', '', '') == 'a'
