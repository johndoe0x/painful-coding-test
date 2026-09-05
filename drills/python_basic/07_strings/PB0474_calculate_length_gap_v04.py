"""
PB0474 — 문자열 길이 차이 구하기

Chapter: Strings
Topic: Length Function
Seed: 48 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 문자열 길이의 절댓값 차이를 반환한다.

연습 초점
---------
len 결과끼리 뺀 뒤 abs로 방향과 무관한 차이를 만든다.

구현할 함수
-----------
def text_length_gap(left: str, right: str) -> int:

예시 및 필수 테스트
-------------------
- text_length_gap('hello', 'hi') == 3
- text_length_gap('a', 'four') == 3
- text_length_gap('', '') == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0474 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def text_length_gap(left: str, right: str) -> int:
    raise NotImplementedError("TODO: PB0474")


def self_test() -> None:
    assert text_length_gap('hello', 'hi') == 3
    assert text_length_gap('a', 'four') == 3
    assert text_length_gap('', '') == 0
