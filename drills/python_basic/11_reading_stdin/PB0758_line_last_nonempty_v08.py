"""
PB0758 — 마지막 유효 입력 줄

Chapter: Reading Stdin
Topic: Reading Input
Seed: 76 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
뒤에서부터 찾아 strip 결과가 비지 않은 첫 줄을 반환하고 없으면 None을 반환한다.

연습 초점
---------
역순 탐색과 조기 반환

구현할 함수
-----------
def line_last_nonempty(lines: list[str]) -> str | None:

예시 및 필수 테스트
-------------------
- line_last_nonempty(['a', ' ', ' b ']) == 'b'
- line_last_nonempty([]) is None
- line_last_nonempty([' ', '']) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0758 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def line_last_nonempty(lines: list[str]) -> str | None:
    raise NotImplementedError("TODO: PB0758")


def self_test() -> None:
    assert line_last_nonempty(['a', ' ', ' b ']) == 'b'
    assert line_last_nonempty([]) is None
    assert line_last_nonempty([' ', '']) is None
