"""
PB0757 — 첫 입력 token

Chapter: Reading Stdin
Topic: Reading Input
Seed: 76 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
공백으로 나눈 첫 token을 반환하고 token이 없으면 None을 반환한다.

연습 초점
---------
split 결과의 빈 목록 처리

구현할 함수
-----------
def line_first_token(line: str) -> str | None:

예시 및 필수 테스트
-------------------
- line_first_token('  alpha beta') == 'alpha'
- line_first_token('   ') is None
- line_first_token('x') == 'x'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0757 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def line_first_token(line: str) -> str | None:
    raise NotImplementedError("TODO: PB0757")


def self_test() -> None:
    assert line_first_token('  alpha beta') == 'alpha'
    assert line_first_token('   ') is None
    assert line_first_token('x') == 'x'
