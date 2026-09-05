"""
PB0269 — 더 짧은 문자열 반환

Chapter: Functions
Topic: Return Statement
Seed: 27 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
더 짧은 문자열을 반환하고 길이가 같으면 left를 반환한다.

연습 초점
---------
결정된 값을 호출자에게 반환

구현할 함수
-----------
def choose_shorter_text(left: str, right: str) -> str:

예시 및 필수 테스트
-------------------
- choose_shorter_text('cat', 'python') == 'cat'
- choose_shorter_text('long', 'tiny') == 'long'
- choose_shorter_text('', 'x') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0269 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def choose_shorter_text(left: str, right: str) -> str:
    raise NotImplementedError("TODO: PB0269")


def self_test() -> None:
    assert choose_shorter_text('cat', 'python') == 'cat'
    assert choose_shorter_text('long', 'tiny') == 'long'
    assert choose_shorter_text('', 'x') == ''
