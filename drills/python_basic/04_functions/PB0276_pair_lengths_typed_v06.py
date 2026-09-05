"""
PB0276 — 문자열 쌍 길이

Chapter: Functions
Topic: Type Hints
Seed: 28 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
문자열 두 개의 길이를 같은 순서의 tuple로 반환한다.

연습 초점
---------
고정 길이 tuple 타입 힌트

구현할 함수
-----------
def pair_lengths_typed(pair: tuple[str, str]) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- pair_lengths_typed(('cat', 'hi')) == (3, 2)
- pair_lengths_typed(('', 'x')) == (0, 1)
- pair_lengths_typed(('한글', 'abc')) == (2, 3)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0276 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def pair_lengths_typed(pair: tuple[str, str]) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0276")


def self_test() -> None:
    assert pair_lengths_typed(('cat', 'hi')) == (3, 2)
    assert pair_lengths_typed(('', 'x')) == (0, 1)
    assert pair_lengths_typed(('한글', 'abc')) == (2, 3)
