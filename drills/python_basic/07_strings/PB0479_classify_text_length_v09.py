"""
PB0479 — 길이 등급 붙이기

Chapter: Strings
Topic: Length Function
Seed: 48 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
short_max < long_min이라고 가정한다. 길이가 short_max 이하면 'short', 그렇지 않고 long_min 이상이면 'long', 그 사이는 'medium'을 반환한다.

연습 초점
---------
서로 겹치지 않는 두 경계의 포함 여부와 분기 우선순위를 구분한다.

구현할 함수
-----------
def text_size_label(text: str, short_max: int, long_min: int) -> str:

예시 및 필수 테스트
-------------------
- text_size_label('cat', 3, 7) == 'short'
- text_size_label('hello', 3, 7) == 'medium'
- text_size_label('elephant', 3, 7) == 'long'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0479 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def text_size_label(text: str, short_max: int, long_min: int) -> str:
    raise NotImplementedError("TODO: PB0479")


def self_test() -> None:
    assert text_size_label('cat', 3, 7) == 'short'
    assert text_size_label('hello', 3, 7) == 'medium'
    assert text_size_label('elephant', 3, 7) == 'long'
