"""
PB0480 — 최소 길이까지 채우기

Chapter: Strings
Topic: Length Function
Seed: 48 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
text가 width보다 짧으면 한 글자인 fill을 오른쪽에 반복해 붙이고, 이미 충분히 길면 그대로 반환한다.

연습 초점
---------
현재 길이와 목표 길이의 차이만큼 문자열을 반복한다.

구현할 함수
-----------
def pad_to_width(text: str, width: int, fill: str) -> str:

예시 및 필수 테스트
-------------------
- pad_to_width('cat', 5, '.') == 'cat..'
- pad_to_width('python', 3, '-') == 'python'
- pad_to_width('', 3, '0') == '000'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0480 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def pad_to_width(text: str, width: int, fill: str) -> str:
    raise NotImplementedError("TODO: PB0480")


def self_test() -> None:
    assert pad_to_width('cat', 5, '.') == 'cat..'
    assert pad_to_width('python', 3, '-') == 'python'
    assert pad_to_width('', 3, '0') == '000'
