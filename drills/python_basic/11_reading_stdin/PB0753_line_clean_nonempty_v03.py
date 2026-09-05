"""
PB0753 — 빈 줄 제외하고 정리

Chapter: Reading Stdin
Topic: Reading Input
Seed: 76 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 줄을 strip한 뒤 빈 문자열이 아닌 줄만 순서대로 반환한다.

연습 초점
---------
여러 입력 줄의 정규화와 필터링

구현할 함수
-----------
def line_clean_nonempty(lines: list[str]) -> list[str]:

예시 및 필수 테스트
-------------------
- line_clean_nonempty([' a ', '   ', 'b']) == ['a', 'b']
- line_clean_nonempty([]) == []
- line_clean_nonempty([' x ']) == ['x']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0753 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def line_clean_nonempty(lines: list[str]) -> list[str]:
    raise NotImplementedError("TODO: PB0753")


def self_test() -> None:
    assert line_clean_nonempty([' a ', '   ', 'b']) == ['a', 'b']
    assert line_clean_nonempty([]) == []
    assert line_clean_nonempty([' x ']) == ['x']
