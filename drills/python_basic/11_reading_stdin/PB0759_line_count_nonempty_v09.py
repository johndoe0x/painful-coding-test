"""
PB0759 — 유효 입력 줄 개수

Chapter: Reading Stdin
Topic: Reading Input
Seed: 76 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
strip 결과가 비지 않은 줄의 개수를 반환한다.

연습 초점
---------
문자열 truthiness와 count 누적

구현할 함수
-----------
def line_count_nonempty(lines: list[str]) -> int:

예시 및 필수 테스트
-------------------
- line_count_nonempty(['a', ' ', 'b']) == 2
- line_count_nonempty([]) == 0
- line_count_nonempty(['', '   ']) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0759 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def line_count_nonempty(lines: list[str]) -> int:
    raise NotImplementedError("TODO: PB0759")


def self_test() -> None:
    assert line_count_nonempty(['a', ' ', 'b']) == 2
    assert line_count_nonempty([]) == 0
    assert line_count_nonempty(['', '   ']) == 0
